> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Utilisation d'un fichier de configuration personnalisé

KubeDB prend en charge la fourniture d'une configuration personnalisée pour MariaDB. Ce didacticiel vous montrera comment utiliser KubeDB pour exécuter une base de données MariaDB avec une configuration personnalisée.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created

  $ kubectl get ns demo
  NAME    STATUS  AGE
  demo    Active  5s
  ```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [ici](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/configuration/using-config-file/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Aperçu

MariaDB permet de configurer la base de données via le fichier de configuration. La configuration par défaut de MariaDB se trouve dans `/etc/mysql/my.cnf` déposer. Lorsque MariaDB démarre, il recherchera le fichier de configuration personnalisé dans `/etc/mysql/conf.d` annuaire. Si le fichier de configuration existe, l'instance MariaDB utilisera les paramètres de démarrage combinés des deux `/etc/mysql/my.cnf` et `*.cnf` fichiers dans `/etc/mysql/conf.d` annuaire. Cette configuration personnalisée écrasera celle par défaut existante. Pour en savoir plus sur la configuration de MariaDB, voir [ici](https://mariadb.com/kb/en/configuring-mariadb-with-option-files/).

Dans un premier temps, vous devez créer un fichier de configuration avec `.cnf` extension avec la configuration souhaitée. Créez ensuite un Secret avec ce fichier de configuration et indiquez son nom dans `spec.configuration.secretName`. L'opérateur lit ce secret en interne et applique la configuration automatiquement, sans monter de volume dans le Pod.

Dans ce tutoriel, nous allons configurer [max\_connections](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_connections) et [read\_buffer\_size](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#read_buffer_size/) via un fichier de configuration personnalisé. Nous utiliserons Secret comme source de volume.

## Configuration personnalisée

Dans un premier temps, créons `md-config.cnf` paramètre de fichier `max_connections` et `read_buffer_size` paramètres.

```bash
cat <<EOF > md-config.cnf
[mysqld]
max_connections = 200
read_buffer_size = 1048576
EOF

$ cat md-config.cnf
[mysqld]
max_connections = 200
read_buffer_size = 1048576
```

Ici, `read_buffer_size` est défini sur 1 Mo en octets.

Maintenant, créez un secret avec ce fichier de configuration.

```bash
$ kubectl create secret generic -n demo md-configuration --from-file=./md-config.cnf
secret/md-configuration created
```

Vérifiez que le secret contient le fichier de configuration.

```yaml
$ kubectl get secret -n demo md-configuration -o yaml
apiVersion: v1
stringData:
  md-config.cnf: |
    [mysqld]
    max_connections = 200
    read_buffer_size = 1048576    
kind: Secret
metadata:
  name: md-configuration
  namespace: demo
  ...
```

Maintenant, créez le crd MariaDB en spécifiant `spec.configuration.secretName` champ.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/configuration/using-config-file/examples/md-custom.yaml
mariadb.kubedb.com/sample-mariadb created
```

Vous trouverez ci-dessous le YAML du crd MariaDB que nous venons de créer.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  configuration:
    secretName: md-configuration
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Maintenant, attendez quelques minutes. L'opérateur KubeDB créera le PVC, le petset, les services, le secret, etc. Si tout se passe bien, nous verrons qu'un pod portant le nom `sample-mariadb-0` a été créé.

Vérifiez que le pod du petset est en cours d'exécution

```bash
$ kubectl get pod -n demo
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          21s

$ kubectl get mariadb -n demo 
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    71s
```

Nous pouvons voir que la base de données est en phase prête afin qu'elle puisse accepter la connexion.

Nous allons maintenant vérifier si la base de données a démarré avec la configuration personnalisée que nous avons fournie.

> Lisez le commentaire écrit pour les commandes suivantes. Ils contiennent les instructions et explications des commandes.

```bash
# Connceting to the database
 $ kubectl exec -it -n demo sample-mariadb-0 -- bash
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is same as provided 
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 200   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1048576 |
+------------------+---------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
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