> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Initialiser MariaDB à l'aide d'un script

Ce tutoriel vous montrera comment utiliser KubeDB pour initialiser une base de données MariaDB avec le script \*.sql, \*.sh et/ou \*.sql.gz.
Dans ce tutoriel, nous utiliserons le script .sql stocké dans le référentiel GitHub [kubedb/mysql-init-scripts](https://github.com/kubedb/mysql-init-scripts).

> Remarque : Les fichiers yaml utilisés dans ce didacticiel sont stockés [ici](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/initialization/using-script/example) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Préparer les scripts d'initialisation

MariaDB prend en charge l'initialisation avec `.sh`, `.sql` et `.sql.gz` fichiers. Dans ce tutoriel, nous utiliserons `init.sql` script de [scripts d'initialisation mysql](https://github.com/kubedb/mysql-init-scripts) dépôt git pour créer une TABLE `kubedb_table` dans `mysql` base de données.

Nous utiliserons un ConfigMap comme source de script. Vous pouvez utiliser n'importe quel Kubernetes pris en charge [volume](https://kubernetes.io/docs/concepts/storage/volumes) comme source de script.

Dans un premier temps, nous allons créer un ConfigMap à partir de `init.sql` déposer. Ensuite, nous fournirons ce ConfigMap comme source de script dans `init.script` de la spécification crd MariaDB.

Créons un ConfigMap avec un script d'initialisation,

```bash
$ kubectl create configmap -n demo md-init-script \
--from-literal=init.sql="$(curl -fsSL https://github.com/kubedb/mysql-init-scripts/raw/master/init.sql)"
configmap/md-init-script created
```

## Créer une base de données MariaDB avec Init-Script

Ci-dessous se trouve le `MariaDB` objet créé dans ce tutoriel.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  init:
    script:
      configMap:
        name: md-init-script
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/initialization/using-script/example/demo-1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Ici,

* `spec.init.script` spécifie une source de script utilisée pour initialiser la base de données avant le démarrage du serveur de base de données. Les scripts seront exécutés par ordre alphabétique. Dans ce tutoriel, un exemple de script .sql du référentiel git `https://github.com/kubedb/mysql-init-scripts.git` est utilisé pour créer une base de données de test. Vous pouvez utiliser d'autres [sources de volume](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes) au lieu de `ConfigMap`. Les scripts \*.sql, \*sql.gz et/ou \*.sh stockés dans le dossier racine seront exécutés par ordre alphabétique. Les scripts contenus dans les dossiers enfants seront ignorés.

L'opérateur KubeDB surveille `MariaDB` objets utilisant l’API Kubernetes. Quand un `MariaDB` est créé, l'opérateur KubeDB créera un nouveau PetSet et un service avec le nom d'objet MariaDB correspondant. L'opérateur KubeDB créera également un service de gouvernance pour les PetSets avec le nom `kubedb`, s'il n'y en a pas déjà un. Aucun rôle RBAC spécifique à MariaDB n'est requis pour [Clusters compatibles RBAC](https://kubedb.com/docs/v2026.7.10/setup/README#using-yaml).

```bash
$ kubectl get mariadb -n demo sample-mariadb -oyaml
```

```text
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  ...
  name: sample-mariadb
  namespace: demo
  ...
spec:
  authSecret:
    name: sample-mariadb-auth
  init:
    initialized: true
    script:
      configMap:
        name: md-init-script
  ...
  replicas: 1
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
    storageClassName: standard
  storageType: Durable
  deletionPolicy: WipeOut
  version: 12.1.2
status:
  ...
  phase: Ready
```

L'opérateur KubeDB définit le `status.phase` à `Ready` une fois la base de données créée avec succès.

Maintenant, nous allons nous connecter à cette base de données et vérifier les données insérées par le script d'initialisation.

```bash
# Connecting to the database
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 40
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

# Showing the inserted `kubedb_table`
Database changed
MariaDB [mysql]> select * from  kubedb_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.001 sec)

MariaDB [mysql]> quit;
Bye
```

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```