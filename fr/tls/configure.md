> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Configurer TLS/SSL dans MariaDB

`KubeDB` prend en charge le cryptage TLS/SSL (via, `requireSSL` mode) pour `MariaDB`. Ce tutoriel va vous montrer comment utiliser `KubeDB` déployer un `MariaDB` base de données avec configuration TLS/SSL.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer [`cert-manger`](https://cert-manager.io/docs/installation/) v1.0.0 ou version ultérieure sur votre cluster pour gérer vos certificats SSL/TLS.
* Installer `KubeDB` dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/tls/configure/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/tls/configure/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

### Déployer la base de données MariaDB avec la configuration TLS/SSL

Comme pré-requis, dans un premier temps, nous allons créer un Issuer/ClusterIssuer. Cet émetteur/ClusterIssuer est utilisé pour créer des certificats. Ensuite, nous allons déployer une réplication MariaDB autonome et de groupe qui sera configurée avec ces certificats par `KubeDB` opérateur.

### Créer un émetteur/un clusterIssuer

Maintenant, nous allons créer un exemple `Issuer` qui sera utilisé tout au long de ce tutoriel. Alternativement, vous pouvez suivre ceci [tutoriel du gestionnaire de certificats](https://cert-manager.io/docs/configuration/ca/) pour créer le vôtre `Issuer`. En suivant les étapes ci-dessous, nous allons créer l'émetteur souhaité,

* Commencez par générer nos certificats ca en utilisant openssl,

```bash
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./ca.key -out ./ca.crt -subj "/CN=mariadb/O=kubedb"
Generating a RSA private key
...........................................................................+++++
........................................................................................................+++++
writing new private key to './ca.key'
```

* créer un secret en utilisant les fichiers de certificat que nous venons de générer,

```bash
kubectl create secret tls md-ca \
     --cert=ca.crt \
     --key=ca.key \
     --namespace=demo
secret/md-ca created
```

Maintenant, nous allons créer un `Issuer` en utilisant le `md-ca` secret que renferme le certificat ca que nous venons de créer. Vous trouverez ci-dessous le YAML du `Issuer` cr que nous allons créer,

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: md-issuer
  namespace: demo
spec:
  ca:
    secretName: md-ca
```

Créons le `Issuer` cr nous l'avons montré ci-dessus,

```bash
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/tls/configure/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

### Déployer MariaDB Standalone avec la configuration TLS/SSL

Ici, notre émetteur `md-issuer` est prêt à déployer un `MariaDB` autonome avec configuration TLS/SSL. Vous trouverez ci-dessous le YAML pour MariaDB Standalone que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-standalone-tls
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi   
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
  deletionPolicy: WipeOut
```

Ici,

* `spec.requireSSL` spécifie que la connexion client SSL/TLS au serveur est requise.
* `spec.tls.issuerRef` fait référence au `md-issuer` émetteur.
* `spec.tls.certificates` vous offre de nombreuses options à configurer pour que le certificat soit renouvelé et tenu à jour.
  Vous pouvez trouver plus de détails sur [ici](../concepts/mariadb.md#spectls)

**Déployez MariaDB autonome :**

Créons le `MariaDB` cr nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/tls/configure/examples/tls-standalone.yaml
mariadb.kubedb.com/md-standalone-tls created
```

**Attendez que la base de données soit prête :**

Maintenant, attends `MariaDB` en cours `Running` état et aussi attendre `PetSet` et son pod à créer et à destination `Running` État,

```bash
$ kubectl get mariadb -n demo md-standalone-tls
NAME             VERSION   STATUS   AGE
md-standalone-tls   11.8.5    Ready    5m48s

$ kubectl get petset -n demo md-standalone-tls
NAME             READY   AGE
md-standalone-tls   1/1     7m5s
```

**Vérifiez que les secrets tls ont été créés avec succès :**

Si tout se passe bien, vous pouvez voir que nos secrets tls seront créés et contiennent le certificat du serveur, du client et de l'exportateur. Le serveur tls-secret sera utilisé pour la configuration du serveur et le client tls-secret sera utilisé pour une connexion sécurisée.

Tous les tls-secret sont créés par `KubeDB` Gestionnaire des opérations. Nom tls-secret par défaut formé comme *{mariadb-object-name}-{cert-alias}-cert*.

Vérifions les secrets tls créés,

```bash
$ kubectl get secrets -n demo | grep md-standalone-tls
md-standalone-tls-archiver-cert             kubernetes.io/tls                     3      7m53s
md-standalone-tls-auth                      kubernetes.io/basic-auth              2      7m54s
md-standalone-tls-metrics-exporter-cert     kubernetes.io/tls                     3      7m53s
md-standalone-tls-metrics-exporter-config   Opaque                                1      7m54s
md-standalone-tls-server-cert               kubernetes.io/tls                     3      7m53s
md-standalone-tls-token-7hhg2
```

**Vérifiez MariaDB Standalone configuré avec TLS/SSL :**

Maintenant, nous allons nous connecter à la base de données pour vérifier le `MariaDB` Le serveur a été configuré avec le cryptage TLS/SSL.

Exécutons dans le pod pour vérifier la configuration TLS/SSL,

```bash
$ kubectl exec -it -n demo md-standalone-tls-0 -- bash

root@md-standalone-tls-0:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
root@md-standalone-tls-0:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key

root@md-standalone-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 64
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.002 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

La sortie ci-dessus montre que le `MariaDB` Le serveur est configuré sur TLS/SSL. Vous pouvez également voir que le `.crt` et `.key` les fichiers sont stockés dans `/etc/mysql/certs/client/` et `/etc/mysql/certs/server/` répertoire pour le client et le serveur respectivement.

**Vérifiez la connexion sécurisée pour l'utilisateur SSL requis :**

Maintenant, vous pouvez créer un utilisateur SSL requis qui sera utilisé pour vous connecter à la base de données avec une connexion sécurisée.

Connectons-nous au serveur de base de données avec une connexion sécurisée,

```bash
$ kubectl exec -it -n demo md-standalone-tls-0 -- bash
root@md-standalone-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 92
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE USER 'new_user'@'localhost' IDENTIFIED BY '1234' REQUIRE SSL;
Query OK, 0 rows affected (0.028 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> exit
Bye

#  accessing the database server with newly created user
root@md-standalone-tls-0:/ mariadb -unew_user -p1234
ERROR 1045 (28000): Access denied for user 'new_user'@'localhost' (using password: YES)

# accessing the database server newly created user with certificates
root@md-standalone-tls-0:/ mariadb -unew_user -p1234 --ssl-ca=/etc/mysql/certs/server/ca.crt  --ssl-cert=/etc/mysql/certs/server/tls.crt --ssl-key=/etc/mysql/certs/server/tls.key
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 116
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> exit 
Bye
```

À partir de la sortie ci-dessus, vous pouvez voir qu'en utilisant uniquement le certificat client, nous pouvons accéder à la base de données en toute sécurité, sinon, il affiche « Accès refusé ». Notre certificat client est stocké dans `/etc/mysql/certs/client/` annuaire.

## Déployer le cluster MariaDB avec la configuration TLS/SSL

Maintenant, nous allons déployer un `MariaDB` Cluster avec configuration TLS/SSL. Ci-dessous se trouve le cluster YAML pour MariaDB que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-cluster-tls
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi   
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
  deletionPolicy: WipeOut
```

**Déployez le cluster MariaDB :**

```bash
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/tls/configure/examples/tls-cluster.yaml
mariadb.kubedb.com/md-cluster-tls created
```

**Attendez que la base de données soit prête :**

Maintenant, attends `MariaDB` en cours `Running` état et aussi attendre `PetSet` et ses pods à créer et à destination `Running` État,

```bash
$ kubectl get mariadb -n demo md-cluster-tls
NAME             VERSION   STATUS   AGE
md-cluster-tls   11.8.5    Ready    2m49s

$ kubectl get pod -n demo | grep md-cluster-tls
md-cluster-tls-0   1/1     Running   0          3m29s
md-cluster-tls-1   1/1     Running   0          3m9s
md-cluster-tls-2   1/1     Running   0          2m49s
```

**Vérifiez les tls-secrets créés avec succès :**

Si tout se passe bien, vous pouvez voir que nos secrets tls seront créés et contiennent le certificat du serveur, du client et de l'exportateur. Le serveur tls-secret sera utilisé pour la configuration du serveur et le client tls-secret sera utilisé pour une connexion sécurisée.

Tous les tls-secret sont créés par `KubeDB` Gestionnaire des opérations. Nom tls-secret par défaut formé comme *{mariadb-object-name}-{cert-alias}-cert*.

Vérifions les secrets tls créés,

```bash
$ kubectl get secrets -n demo | grep md-cluster-tls
md-cluster-tls-archiver-cert             kubernetes.io/tls                     3      6m20s
md-cluster-tls-auth                      kubernetes.io/basic-auth              2      6m22s
md-cluster-tls-metrics-exporter-cert     kubernetes.io/tls                     3      6m20s
md-cluster-tls-metrics-exporter-config   Opaque                                1      6m21s
md-cluster-tls-server-cert               kubernetes.io/tls                     3      6m21s
md-cluster-tls-token-nrs75
```

**Vérifiez le cluster MariaDB configuré avec TLS/SSL :**

Maintenant, nous allons nous connecter à la base de données pour vérifier le `MariaDB` Le serveur a été configuré avec le cryptage TLS/SSL.

Exécutons le premier pod pour vérifier la configuration TLS/SSL,

```bash
$ kubectl exec -it -n demo md-cluster-tls-0 -- bash

root@md-cluster-tls-0:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
root@md-cluster-tls-0:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key

root@md-cluster-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 64
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.002 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

Vérifions maintenant le deuxième serveur de base de données,

```bash
$ kubectl exec -it -n demo md-cluster-tls-1 -- bash
root@md-cluster-tls-1:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
root@md-cluster-tls-1:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key
root@md-cluster-tls-1:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 34
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.001 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

La sortie ci-dessus montre que le `MariaDB` Le serveur est configuré sur TLS/SSL. Vous pouvez également voir que le `.crt` et `.key` les fichiers sont stockés dans `/etc/mysql/certs/client/` et `/etc/mysql/certs/server/` répertoire pour le client et le serveur respectivement.

**Vérifiez la connexion sécurisée pour l'utilisateur SSL requis :**

Maintenant, vous pouvez créer un utilisateur SSL requis qui sera utilisé pour vous connecter à la base de données avec une connexion sécurisée.

Connectons-nous au serveur de base de données avec une connexion sécurisée,

```bash
$ kubectl exec -it -n demo md-cluster-tls-0 -- bash
root@md-cluster-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 92
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE USER 'new_user'@'localhost' IDENTIFIED BY '1234' REQUIRE SSL;
Query OK, 0 rows affected (0.028 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> exit
Bye

#  accessing the database server with newly created user
root@md-cluster-tls-0:/ mariadb -unew_user -p1234
ERROR 1045 (28000): Access denied for user 'new_user'@'localhost' (using password: YES)

# accessing the database server newly created user with certificates
root@md-cluster-tls-0:/ mariadb -unew_user -p1234 --ssl-ca=/etc/mysql/certs/server/ca.crt  --ssl-cert=/etc/mysql/certs/server/tls.crt --ssl-key=/etc/mysql/certs/server/tls.key
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 116
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> exit 
Bye
```

À partir de la sortie ci-dessus, vous pouvez voir qu'en utilisant uniquement le certificat client, nous pouvons accéder à la base de données en toute sécurité, sinon, il affiche « Accès refusé ». Notre certificat client est stocké dans `/etc/mysql/certs/client/` annuaire.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete  mariadb demo  md-standalone-tls
mariadb.kubedb.com "md-standalone-tls" deleted
$ kubectl delete  mariadb demo  md-cluster-tls
mariadb.kubedb.com "md-cluster-tls" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```