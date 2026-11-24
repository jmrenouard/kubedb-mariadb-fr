> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigurer la base de données autonome MariaDB

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour reconfigurer un MariaDB Standalone.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../concepts/mariadb.md)
  + [MariaDBOpsRequest](../concepts/opsrequest.md)
  + [Présentation de la reconfiguration](overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

Maintenant, nous allons déployer un `MariaDB` Autonome utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBOpsRequest` pour reconfigurer sa configuration.

### Préparer MariaDB autonome

Maintenant, nous allons déployer un `MariaDB` Base de données autonome avec version `12.1.2`.

### Déployer MariaDB

Dans un premier temps, nous créerons `md-config.cnf` fichier contenant les paramètres de configuration requis.

```ini
$ cat md-config.cnf 
[mysqld]
max_connections = 200
read_buffer_size = 1048576
```

Ici, `max_connections` est réglé sur `200`, alors que la valeur par défaut est `151`. De même, `read_buffer_size` a la valeur par défaut `131072`.

Maintenant, nous allons créer un secret avec ce fichier de configuration.

```bash
$ kubectl create secret generic -n demo md-configuration --from-file=./md-config.cnf
secret/md-configuration created
```

Dans cette section, nous allons créer un objet MariaDB spécifiant `spec.configuration` champ pour appliquer cette configuration personnalisée. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

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

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/sample-mariadb-config.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attends `sample-mariadb` a un statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo 
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    61s
```

Nous allons maintenant vérifier si la base de données a démarré avec la configuration personnalisée que nous avons fournie.

Nous devons d'abord obtenir le nom d'utilisateur et le mot de passe pour nous connecter à une instance mariadb,

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d                                                                       
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d                                                                         
PlWA6JNLkNFudl4I
```

Nous allons maintenant vérifier si la base de données a démarré avec la configuration personnalisée que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 200   |
+-----------------+-------+
1 row in set (0.001 sec)

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

Comme nous pouvons le voir d'après la configuration de ready mariadb, la valeur de `max_connections` a été réglé sur `200` et `read_buffer_size` a été réglé sur `1048576`.

### Reconfigurer à l'aide du nouveau secret de configuration

Nous allons maintenant reconfigurer cette base de données pour définir `max_connections` à `250` et `read_buffer_size` à `122880`.

Maintenant, nous allons créer un nouveau fichier `new-md-config.cnf` contenant les paramètres de configuration requis.

```ini
$ cat new-md-config.cnf 
[mysqld]
max_connections = 250
read_buffer_size = 122880
```

Ensuite, nous créerons un nouveau secret avec ce fichier de configuration.

```bash
$ kubectl create secret generic -n demo new-md-configuration --from-file=./new-md-config.cnf
secret/new-md-configuration created
```

#### Créer une demande MariaDBOps

Maintenant, nous allons utiliser ce secret pour remplacer le secret précédent en utilisant un `MariaDBOpsRequest` CR. Le `MariaDBOpsRequest` yaml est donné ci-dessous,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-config
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    configSecret:
      name: new-md-configuration
```

Ici,

* `spec.databaseRef.name` précise que nous sommes en train de reconfigurer `mdops-reconfigure-config` base de données.
* `spec.type` précise que nous effectuons `Reconfigure` sur notre base de données.
* `spec.configuration.configSecret.name` spécifie le nom du nouveau secret.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/reconfigure-using-secret.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-config created
```

#### Vérifiez que la nouvelle configuration fonctionne

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour le `configSecret` de `MariaDB` objet.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-config   Reconfigure   Successful   2m8s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour reconfigurer la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-reconfigure-config
Name:         mdops-reconfigure-config
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-06-14T10:56:01Z
  Generation:          1
  Resource Version:  21589
  UID:               43997fe8-fa12-4d38-a29f-d101889d4e72
Spec:
  Configuration:
    Config Secret:
      Name:  new-md-configuration
  Database Ref:
    Name:  sample-mariadb
  Type:    Reconfigure
Status:
  Conditions:
    Last Transition Time:  2022-06-14T10:56:01Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-14T10:56:11Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-14T10:56:16Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-14T10:56:16Z
    Message:               Controller has successfully reconfigure the MariaDB demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
```

Connectons-nous maintenant à une instance mariadb et exécutons une commande interne mariadb pour vérifier la nouvelle configuration que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 21
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 250   |
+-----------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+--------+
| Variable_name    | Value  |
+------------------+--------+
| read_buffer_size | 122880 |
+------------------+--------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Comme nous pouvons le voir d'après la configuration, la valeur de `max_connections` a été changé de `200` à `250` et et le `read_buffer_size` a été modifié `1048576` à `122880`. La reconfiguration de la base de données est donc réussie.

### Reconfigurer le secret de configuration existant

Maintenant, nous allons créer un nouveau `MariaDBOpsRequest` reconfigurer notre secret existant `new-md-configuration` en modifiant notre `new-md-config.cnf` fichier utilisant `applyConfig`. Le `MariaDBOpsRequest` yaml est donné ci-dessous,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-apply-config
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    applyConfig:
      new-md-config.cnf: |
        [mysqld]
        max_connections = 230
        read_buffer_size = 1064960        
      innodb-config.cnf: |
        [mysqld]
        innodb_log_buffer_size = 17408000
```

> Remarque : Vous pouvez modifier plusieurs champs de votre configuration actuelle en utilisant `applyConfig`. Si tu n'as pas de secrets alors `applyConfig` créera un secret pour vous. Ici, nous avons modifié la valeur de nos deux champs existants qui sont `max_connections` et `read_buffer_size` aussi, nous avons modifié un nouveau champ `innodb_log_buffer_size` de notre configuration.

Ici,

* `spec.databaseRef.name` précise que nous sommes en train de reconfigurer `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `Reconfigure` sur notre base de données.
* `spec.configuration.applyConfig` contient la configuration du secret existant ou nouvellement créé.

Avant d'appliquer ce yaml nous allons vérifier la valeur existante de notre nouveau champ,

```bash
$ kubectl exec -it sample-mariadb-0 -n demo -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 21
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 16777216 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Ici, nous pouvons voir la valeur par défaut pour `innodb_log_buffer_size` est `16777216`.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/mdops-reconfigure-apply-config.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-apply-config created
```

#### Vérifiez que la nouvelle configuration fonctionne

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour le `configSecret` de `MariaDB` objet.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest mdops-reconfigure-apply-config -n demo
NAME                             TYPE          STATUS       AGE
mdops-reconfigure-apply-config   Reconfigure   Successful   3m11s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour reconfigurer la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-reconfigure-apply-config
Name:         mdops-reconfigure-apply-config
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-06-14T09:13:49Z
  Generation:          1
  Resource Version:  14120
  UID:               eb8d5df5-a0ce-4011-890c-c18c0200b5ac
Spec:
  Configuration:
    Apply Config:
      innodb-config.cnf:  [mysqld]
innodb_log_buffer_size = 17408000

      new-md-config.cnf:  [mysqld]
max_connections = 230
read_buffer_size = 1064960

  Database Ref:
    Name:  sample-mariadb
  Type:    Reconfigure
Status:
  Conditions:
    Last Transition Time:  2022-06-14T09:13:49Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-14T09:13:49Z
    Message:               Successfully prepared user provided custom config secret
    Observed Generation:   1
    Reason:                PrepareSecureCustomConfig
    Status:                True
    Type:                  PrepareCustomConfig
    Last Transition Time:  2022-06-14T09:17:24Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-14T09:17:29Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-14T09:17:29Z
    Message:               Controller has successfully reconfigure the MariaDB demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
```

Connectons-nous maintenant à une instance mariadb et exécutons une commande interne mariadb pour vérifier la nouvelle configuration que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 24
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 230   |
+-----------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1064960 |
+------------------+---------+
1 row in set (0.002 sec)

MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 17408000 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Comme on peut le voir ci-dessus la configuration a été modifiée, la valeur de `max_connections` a été changé de `250` à `230` et le `read_buffer_size` a été modifié `122880` à `1064960` aussi, `innodb_log_buffer_size` a été changé de `16777216` à `17408000`. Ainsi, la reconfiguration du `sample-mariadb` la base de données réussit.

### Supprimer la configuration personnalisée

Nous pouvons également supprimer la configuration personnalisée existante en utilisant `MariaDBOpsRequest`. Fournir `true` champ `spec.configuration.removeCustomConfig` et effectuez une demande opérationnelle pour supprimer la configuration personnalisée existante.

#### Créer une demande MariaDBOps

Créons un `MariaDBOpsRequest` ayant `spec.configuration.removeCustomConfig` est égal `true`,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-remove
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    removeCustomConfig: true
```

Ici,

* `spec.databaseRef.name` précise que nous sommes en train de reconfigurer `mdops-reconfigure-remove` base de données.
* `spec.type` précise que nous effectuons `Reconfigure` sur notre base de données.
* `spec.configuration.removeCustomConfig` est un champ booléen qui devrait être `true` lorsque vous souhaitez supprimer une configuration personnalisée existante.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/reconfigure-remove.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-remove created
```

#### Vérifiez que la nouvelle configuration fonctionne

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour le `configSecret` de `MariaDB` objet.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-remove   Reconfigure   Successful   2m5s
```

Connectons-nous maintenant à une instance mariadb et exécutons une commande interne mariadb pour vérifier la nouvelle configuration que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is default
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 151   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is default
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 131072  |
+------------------+---------+
1 row in set (0.001 sec)

# value of `innodb_log_buffer_size` is default
MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 16777216 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Comme nous pouvons le voir, la configuration a changé pour sa valeur par défaut. Donc suppression de la configuration personnalisée existante à l'aide de `MariaDBOpsRequest` est réussi.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-reconfigure-config mdops-reconfigure-apply-config mdops-reconfigure-remove
$ kubectl delete ns demo
```