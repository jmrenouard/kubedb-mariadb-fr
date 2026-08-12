> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Migration de la base de données MariaDB

Ce guide vous montrera comment utiliser `KubeDB` Migration pour migrer un existant `MariaDB` base de données - telle qu'une base de données exécutée sur AWS RDS ou toute instance externe - entièrement dans une base de données gérée par KubeDB `MariaDB` avec un temps d'arrêt minimal.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` opérateur avec l'opérateur kubedb-courier activé dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/operatormanual/migration/).
* La source `MariaDB` L'instance doit être accessible par le réseau depuis votre cluster Kubernetes.
* La source `MariaDB` l'instance doit avoir la journalisation binaire activée avec `binlog_format=ROW` et `binlog_row_image=FULL`. L'utilisateur de base de données fourni pour la migration doit disposer de privilèges de réplication.
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [Liaison d'application](../concepts/appbinding.md)
  + [MariaDB](../concepts/mariadb.md)
  + [MariaDBMigration](../concepts/migrator.md)
  + [Migration](https://kubedb.com/docs/v2026.7.10/operatormanual/migration/)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Préparer la base de données source

Nous utiliserons un **AWS RDS MariaDB** exemple comme source. Connectez-vous-y en tant qu'utilisateur administrateur pour vérifier les conditions préalables et configurer l'utilisateur de migration et tester les données.

**Configuration de votre instance source.**

**MariaDB auto-hébergée**

Ajoutez ce qui suit à votre `my.cnf` et redémarrez MariaDB :

```ini
[mysqld]
log_bin          = mysql-bin
binlog_format    = ROW
binlog_row_image = FULL
```

Accordez ensuite les privilèges requis à l'utilisateur de migration :

```sql
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '<migration-user>'@'%';
FLUSH PRIVILEGES;
```

**AWS RDS MariaDB**

Activer [Sauvegardes automatisées](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html) sur l'instance (cela active la journalisation binaire). Ensemble `binlog_format = ROW` et `binlog_row_image = FULL` dans un groupe de paramètres RDS. Accordez ensuite les privilèges de réplication via SQL comme indiqué ci-dessus.

**Base de données Azure pour MariaDB**

La journalisation binaire est activée automatiquement lorsque les sauvegardes sont activées. Ensemble `binlog_format` et `binlog_row_image` sous **Paramètres du serveur** dans le [Portail Azure](https://learn.microsoft.com/en-us/azure/mariadb/concepts-read-replicas). Accordez ensuite les privilèges de réplication via SQL comme indiqué ci-dessus.

Voir le fonctionnaire [Journal binaire MariaDB](https://mariadb.com/kb/en/binary-log/) documents pour plus de détails.

### Vérifier les prérequis

```bash
$ mysql -h <rds-endpoint>.rds.amazonaws.com -u admin -p
```

```sql
-- Verify binary logging is enabled
SHOW VARIABLES LIKE 'log_bin';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
+---------------+-------+

-- Verify binlog format and row image
SHOW VARIABLES LIKE 'binlog_format';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+

SHOW VARIABLES LIKE 'binlog_row_image';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| binlog_row_image | FULL  |
+------------------+-------+
```

### Créer un utilisateur de migration dédié

Créez un utilisateur dédié avec les privilèges minimum requis :

```sql
CREATE USER 'migrator'@'%' IDENTIFIED BY '<password>';

-- For CDC (binlog streaming)
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'migrator'@'%';

-- For schema migration (mariadb-dump) and snapshot
GRANT SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, EVENT, LOCK TABLES, PROCESS ON *.* TO 'migrator'@'%';

FLUSH PRIVILEGES;

-- Verify
SHOW GRANTS FOR 'migrator'@'%';
```

Le `migrator` L'utilisateur est référencé dans le secret Kubernetes et AppBinding pour le reste de ce guide.

### Créer une table et des données de départ

```sql
CREATE DATABASE shop;
USE shop;

CREATE TABLE orders (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  product       VARCHAR(100) NOT NULL,
  quantity      INT          NOT NULL DEFAULT 1,
  status        VARCHAR(20)  NOT NULL DEFAULT 'pending',
  created_at    TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO orders (customer_name, product, quantity, status) VALUES
  ('Alice', 'Laptop',     1, 'shipped'),
  ('Bob',   'Headphones', 2, 'pending'),
  ('Carol', 'Keyboard',   3, 'delivered');

SELECT * FROM orders;
+----+---------------+------------+----------+-----------+---------------------+
| id | customer_name | product    | quantity | status    | created_at          |
+----+---------------+------------+----------+-----------+---------------------+
|  1 | Alice         | Laptop     |        1 | shipped   | 2026-06-29 08:00:00 |
|  2 | Bob           | Headphones |        2 | pending   | 2026-06-29 08:00:01 |
|  3 | Carol         | Keyboard   |        3 | delivered | 2026-06-29 08:00:02 |
+----+---------------+------------+----------+-----------+---------------------+
3 rows in set (0.00 sec)
```

## Préparer les informations de connexion source

Tout d'abord, créez un secret d'authentification à l'aide du `migrator` identifiants utilisateur :

```bash
$ kubectl create secret generic source-mariadb-auth -n demo \
                --type=kubernetes.io/basic-auth \
                --from-literal=username=migrator \
                --from-literal=password=<password>
```

Si TLS est activé sur votre base de données, créez un secret avec le certificat CA :

```bash
kubectl create secret generic ca-secret \
  --from-file=ca.crt=$CERT_PATH/ca.crt \
  --namespace=demo
```

> **Note:** Pour mTLS, incluez également le certificat client et la clé en ajoutant  
> `--from-file=tls.crt=$CERT_PATH/tls.crt`  
> `--from-file=tls.key=$CERT_PATH/tls.key`  
> à la commande ci-dessus.

Créez maintenant un `AppBinding` avec les informations nécessaires. L'opérateur kubedb-courier lit les informations de connexion source MariaDB à partir de ce CR AppBinding. Utilisez le YAML suivant pour créer votre AppBinding :

```yaml
apiVersion: appcatalog.appscode.com/v1alpha1
kind: AppBinding
metadata:
  name: source-mariadb
  namespace: demo
spec:
  type: mariadb
  version: "10.5.23"
  clientConfig:
    url: "mariadb://<rds-endpoint>.rds.amazonaws.com:3306"
  secret:
    name: source-mariadb-auth
  tlsSecret: # omit if TLS is disabled
    name: ca-secret
```

Ici,

* `spec.clientConfig.url` est l'URL de connexion de l'instance MariaDB source.
* `spec.secret.name` est la référence au secret que nous avons créé précédemment, contenant les informations d'authentification MariaDB.

> Pour un `KubeDB`-base de données gérée, un `AppBinding` est créé par défaut. Il n’est donc pas nécessaire d’en créer une pour la base de données cible.

## Créer une base de données MariaDB cible

KubeDB implémente un `MariaDB` CRD pour définir la spécification d'une base de données MariaDB. Suivez le `MariaDB` objet pour créer la base de données cible.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: target-mariadb
  namespace: demo
spec:
  version: "10.5.23"
  storageType: Durable
  storage:
    storageClassName: "local-path"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 20Gi
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/migration/target-mariadb.yaml
mariadb.kubedb.com/target-mariadb created
```

> Remarque : Ajustez le `resources.requests.storage` en fonction de la taille de la base de données source.

Attendez que `target-mariadb` a un statut `Ready`.

## Appliquer MariaDBMigration CR

Pour migrer la base de données, nous devons créer un `MariaDBMigration` CR. Vous trouverez ci-dessous le YAML du `MariaDBMigration` CR que nous allons créer :

```yaml
apiVersion: courier.kubedb.com/v1alpha1
kind: MariaDBMigration
metadata:
  name: mariadb-migrate
  namespace: demo
spec:
  source:
    connectionInfo:
      appBinding:
        name: source-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
    schema:
      enabled: true
      database:
        - shop
      excludeDatabase: []
    snapshot:
      enabled: true
      pipeline:
        workers: 3
        sinkers: 4
        buffer: 12
        write_batch_size: 200
        read_batch_size: 1000
    streaming:
      enabled: true

  target:
    connectionInfo:
      appBinding:
        name: target-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/migration/mariadb-migrate.yaml
mariadbmigration.courier.kubedb.com/mariadb-migrate created
```

Ici, nous étudions la migration vers le `shop` base de données (`schema.database: [shop]`), activez à la fois les phases d'instantané en masse et de streaming CDC, et limitez les connexions à 100 de chaque côté. Pour une description complète de chaque champ, consultez le [Référence MariaDBMigration CRD](../concepts/migrator.md).

## Regardez les progrès de la migration

Attendons le `LAG` pour atteindre près de zéro. Exécutez la commande suivante pour regarder `MariaDBMigration` CR :

```bash
Every 2.0s: kubectl get mariadbmigrations -n demo

NAME              PHASE     DBTYPE    STAGE       LAG   PROGRESS   AGE
mariadb-migrate   Running   mariadb   Streaming   0B    100%       4h36m
```

### Vérifier l'instantané initial sur la cible

Une fois que la migration atteint le `Streaming` étape, exécutez dans le pod cible KubeDB et confirmez que toutes les lignes de départ ont été copiées :

```bash
$ kubectl exec -it -n demo target-mariadb-0 -- mysql -u root -p<root-password>
```

```sql
USE shop;
SELECT * FROM orders;
+----+---------------+------------+----------+-----------+---------------------+
| id | customer_name | product    | quantity | status    | created_at          |
+----+---------------+------------+----------+-----------+---------------------+
|  1 | Alice         | Laptop     |        1 | shipped   | 2026-06-29 08:00:00 |
|  2 | Bob           | Headphones |        2 | pending   | 2026-06-29 08:00:01 |
|  3 | Carol         | Keyboard   |        3 | delivered | 2026-06-29 08:00:02 |
+----+---------------+------------+----------+-----------+---------------------+
3 rows in set (0.00 sec)
```

### Testez le streaming CDC en direct

La migration étant toujours en cours, connectez-vous au **sourceRDS** instance et exécutez du DML :

```bash
$ mysql -h <rds-endpoint>.rds.amazonaws.com -u migrator -p
```

```sql
-- Insert a new order
INSERT INTO shop.orders (customer_name, product, quantity, status)
VALUES ('Dave', 'Mouse', 1, 'pending');

-- Mark Bob's headphones as delivered
UPDATE shop.orders SET status = 'delivered' WHERE id = 2;

-- Remove the already-shipped laptop order
DELETE FROM shop.orders WHERE id = 1;
```

Attendez quelques secondes que les événements binlog se propagent, puis réinterrogez le **cible**:

```sql
USE shop;
SELECT * FROM orders;
+----+---------------+------------+----------+-----------+---------------------+
| id | customer_name | product    | quantity | status    | created_at          |
+----+---------------+------------+----------+-----------+---------------------+
|  2 | Bob           | Headphones |        2 | delivered | 2026-06-29 08:00:01 |
|  3 | Carol         | Keyboard   |        3 | delivered | 2026-06-29 08:00:02 |
|  4 | Dave          | Mouse      |        1 | pending   | 2026-06-29 08:10:00 |
+----+---------------+------------+----------+-----------+---------------------+
3 rows in set (0.00 sec)
```

Les éléments INSERT, UPDATE et DELETE sont tous reflétés sur la cible : le streaming CDC fonctionne correctement.

## Basculement

Une fois le `LAG` tombe à près de zéro, arrêtez toutes les écritures dans la base de données source. Attendez que le `LAG` atteint exactement zéro — à ce stade, les deux bases de données sont entièrement synchronisées.

Supprimez maintenant le `MariaDBMigration` CR pour arrêter le processus de migration :

```bash
$ kubectl delete mariadbmigrations -n demo mariadb-migrate
mariadbmigration.courier.kubedb.com "mariadb-migrate" deleted
```

Enfin, mettez à jour la chaîne de connexion de votre application pour qu'elle pointe vers la cible gérée par KubeDB. `MariaDB` base de données. La migration est terminée.