# Documentation KubeDB MariaDB - Version combinée (FR)

<!-- PAGE_START: README.md -->
> Vous êtes nouveau sur KubeDB ? Commencez [ici](https://kubedb.com/docs/v2026.7.10/README), ou parcourez le [Portail Diataxis FR](fr/index.md) ([Tutoriels](fr/01-tutoriels/index.md) | [Guides pratiques](fr/02-guides-pratiques/index.md) | [Référence](fr/03-reference/index.md) | [Explications](fr/04-explications/index.md)).

## Fonctionnalités MariaDB prises en charge

| Caractéristiques | Disponibilité |
| --- | --- |
| Regroupement | ✓ |
| Volume persistant | ✓ |
| Sauvegarde instantanée | ✓ |
| Sauvegarde planifiée | ✓ |
| Archivage continu à l'aide `wal-g` | ✓ |
| Initialiser à l'aide d'un instantané | ✓ |
| Initialiser à l'aide d'un script (\*.sql, \*sql.gz et/ou \*.sh) | ✓ |
| Configuration personnalisée | ✓ |
| Utilisation d'une image Docker personnalisée | ✓ |
| Découverte Prometheus intégrée | ✓ |
| Utiliser l'opérateur Prometheus | ✓ |

## Cycle de vie d'un objet MariaDB

![lifecycle](images/root_mariadb-lifecycle.png)

## Guide de l'utilisateur

* [Démarrage rapide MariaDB](fr/quickstart/overview.md) avec l'opérateur KubeDB.
* Concepts détaillés de [Objet MariaDB](fr/concepts/mariadb.md).
* Concepts détaillés de [Objet MariaDBVersion](fr/concepts/mariadb-version.md).
* Créer [Cluster MariaDB](fr/clustering/galera-cluster.md).
* Créer [MariaDB avec configuration personnalisée](fr/configuration/using-config-file.md).
* Utiliser [RBAC personnalisé](fr/custom-rbac/using-custom-rbac.md).
* Utiliser [registre Docker privé](fr/private-registry/quickstart.md) pour déployer MariaDB avec KubeDB.
* Initialiser [MariaDB avec script](fr/initialization/using-script.md).
* Sauvegarde et restauration [MariaDB](fr/backup/stash/overview.md).
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

## Index complet des pages

### Autoscaler ➔ Calcul

* [Mise à l'échelle automatique de la ressource de calcul d'une base de données de cluster MariaDB](fr/autoscaler/compute/cluster.md)
* [Mise à l'échelle automatique des ressources de calcul MariaDB](fr/autoscaler/compute/overview.md)

### Autoscaler ➔ Stockage

* [Mise à l'échelle automatique du stockage d'un cluster MariaDB](fr/autoscaler/storage/cluster.md)
* [Mise à l'échelle verticale automatique de MariaDB](fr/autoscaler/storage/overview.md)

### Sauvegarde ➔ KubeStash

* [Sauvegarde et restauration au niveau de l'application de la base de données MariaDB à l'aide de KubeStash](fr/backup/kubestash/application-level.md)
* [Sauvegarder MariaDB à l'aide de la sauvegarde automatique KubeStash](fr/backup/kubestash/auto-backup.md)
* [Personnalisation du processus de sauvegarde et de restauration](fr/backup/kubestash/customization.md)
* [Sauvegarder et restaurer la base de données MariaDB à l'aide de KubeStash](fr/backup/kubestash/logical.md)
* [Présentation de la sauvegarde et de la restauration MariaDB](fr/backup/kubestash/overview.md)

### Sauvegarde ➔ Stash

* [Sauvegarder MariaDB à l'aide de la sauvegarde automatique Stash](fr/backup/stash/auto-backup.md)
* [Personnalisation du processus de sauvegarde et de restauration](fr/backup/stash/customization.md)
* [Présentation de la sauvegarde et de la restauration MariaDB](fr/backup/stash/overview.md)

### Sauvegarde ➔ Stash ➔ Logique

* [Sauvegarder le cluster MariaDB géré par KubeDB à l'aide de Stash](fr/backup/stash/logical/cluster.md)
* [Sauvegarder une instance MariaDB autonome gérée par KubeDB avec Stash](fr/backup/stash/logical/standalone.md)

### Clustering

* [KubeDB-Cluster MariaDB](fr/clustering/galera-cluster.md)
* [KubeDB-Cluster MariaDB](fr/clustering/mariadb-replication.md)
* [Clustering MariaDB](fr/clustering/overview.md)

### Concepts

* [Liaison d'application](fr/concepts/appbinding.md)
* [MariaDBAutoscaler](fr/concepts/autoscaler.md)
* [Version MariaDB](fr/concepts/mariadb-version.md)
* [MariaDB](fr/concepts/mariadb.md)
* [MariaDBMigration](fr/concepts/migrator.md)
* [MariaDBOpsRequest](fr/concepts/opsrequest.md)

### Configuration

* [Utilisation d'un fichier de configuration personnalisé](fr/configuration/using-config-file.md)
* [Exécutez MariaDB avec un PodTemplate personnalisé](fr/configuration/using-pod-template.md)

### RBAC personnalisé

* [Utilisation de ressources RBAC personnalisées](fr/custom-rbac/using-custom-rbac.md)

### Déploiement distribué

* [Présentation du cluster MariaDB Galera distribué](fr/distributed/overview.md)

### Déploiement distribué ➔ Autoscaler ➔ Calcul

* [Mise à l'échelle automatique de la ressource de calcul d'un cluster MariaDB distribué](fr/distributed/autoscaler/compute/cluster.md)
* [Mise à l'échelle automatique des ressources de calcul MariaDB distribuées](fr/distributed/autoscaler/compute/overview.md)

### Déploiement distribué ➔ Autoscaler ➔ Stockage

* [Mise à l'échelle automatique du stockage d'un cluster MariaDB distribué](fr/distributed/autoscaler/storage/cluster.md)
* [Mise à l'échelle automatique du stockage MariaDB distribué](fr/distributed/autoscaler/storage/overview.md)

### Déploiement distribué ➔ OpsRequest

* [MariaDB distribuée à l'échelle horizontale](fr/distributed/opsrequest/horizontal_scale.md)

### Basculement (Failover)

* [Explorer la tolérance aux pannes dans MariaDB avec KubeDB](fr/failover/guide.md)

### GitOps

* [GitOps MariaDB utilisant l'opérateur KubeDB GitOps](fr/gitops/gitops.md)
* [Présentation de GitOps pour MariaDB](fr/gitops/overview.md)

### Initialisation

* [Initialisation MariaDB à partir d'un référentiel Git](fr/initialization/git-sync.md)
* [Initialiser MariaDB à l'aide d'un script](fr/initialization/using-script.md)

### Migration

* [Migration de la base de données MariaDB](fr/migration/databasemigration.md)

### Supervision (Monitoring)

* [Surveillance de MariaDB avec Prometheus intégré](fr/monitoring/builtin-prometheus.md)
* [Surveillance de MariaDB avec KubeDB](fr/monitoring/overview.md)
* [Surveillance de MariaDB à l'aide de l'opérateur Prometheus](fr/monitoring/prometheus-operator.md)

### Récupération ponctuelle (PITR)

* [KubeDB MariaDB - Archivage continu et récupération ponctuelle](fr/pitr/nfs.md)
* [KubeDB MariaDB - Archivage continu et récupération ponctuelle (PITR)](fr/pitr/overview.md)

### Registre privé

* [Déployer MariaDB à partir du registre Docker privé](fr/private-registry/quickstart.md)

### Démarrage rapide

* [Démarrage rapide de MariaDB](fr/quickstart/overview.md)

### Recommandations

* [Recommandation MariaDB](fr/recommendation/recommendation.md)

### Reconfiguration

* [Reconfigurer la base de données du cluster MariaDB](fr/reconfigure/cluster.md)
* [Reconfiguration de MariaDB](fr/reconfigure/overview.md)
* [Reconfigurer la base de données autonome MariaDB](fr/reconfigure/standalone.md)

### Reconfiguration TLS

* [Reconfigurer MariaDB TLS/SSL (chiffrement de transport)](fr/reconfigure-tls/cluster.md)
* [Reconfiguration de TLS de la base de données MariaDB](fr/reconfigure-tls/overview.md)

### Redémarrage

* [Redémarrer MariaDB](fr/restart/restart.md)

### Rotation des identifiants

* [Rotation de l'authentification de MariaDB](fr/rotate-auth/overview.md)
* [Rotation de l'authentification de MariaDB](fr/rotate-auth/rotateauth.md)

### Mise à l'échelle ➔ Horizontale

* [MariaDB à échelle horizontale](fr/scaling/horizontal-scaling/cluster.md)
* [Échelle horizontale MaxScale](fr/scaling/horizontal-scaling/maxscale.md)
* [Mise à l'échelle horizontale de MariaDB](fr/scaling/horizontal-scaling/overview.md)

### Mise à l'échelle ➔ Verticale

* [Cluster MariaDB à échelle verticale](fr/scaling/vertical-scaling/cluster.md)
* [Serveur MaxScale à échelle verticale](fr/scaling/vertical-scaling/maxscale.md)
* [Mise à l'échelle verticale de MariaDB](fr/scaling/vertical-scaling/overview.md)

### TLS / SSL

* [Configurer TLS/SSL dans MariaDB](fr/tls/configure.md)
* [Chiffrement MariaDB TLS/SSL](fr/tls/overview.md)

### Mise à jour de version

* [Mettre à jour la version d'un cluster MariaDB](fr/update-version/cluster.md)
* [Aperçu de la mise à jour de version MariaDB](fr/update-version/overview.md)

### Extension de volume

* [Extension de volume MaxScale](fr/volume-expansion/maxscale.md)
* [Extension du volume MariaDB](fr/volume-expansion/overview.md)
* [Extension du volume MariaDB](fr/volume-expansion/volume-expansion.md)


<!-- PAGE_START: clustering/galera-cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB-Cluster MariaDB

Ce tutoriel vous montrera comment utiliser KubeDB pour provisionner un cluster MariaDB Galera en mode multi-primaire.

## Avant de commencer

Avant de continuer :

* Lire [concept de cluster mariadb galera](fr/clustering/overview.md) pour en savoir plus sur le cluster MariaDB Galera.
* Vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel. Exécutez la commande suivante pour préparer votre cluster pour ce didacticiel :

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : Les fichiers yaml utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/clustering/galera-cluster/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/clustering/galera-cluster/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Déployer le cluster MariaDB

Ce qui suit est un exemple `MariaDB` objet qui crée un groupe MariaDB multi-maître avec trois membres.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: GaleraCluster
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

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/galera-cluster/examples/demo-1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Ici,

* `spec.replicas` est le nombre de nœuds dans le cluster.
* `spec.storage` spécifie la StorageClass de PVC allouée dynamiquement pour stocker les données de cette base de données. Cette spécification de stockage sera transmise au PetSet créé par l'opérateur KubeDB pour exécuter les pods de base de données. Ainsi, chaque membre disposera d’un pod de cette configuration de stockage. Vous pouvez spécifier n'importe quelle StorageClass disponible dans votre cluster avec les demandes de ressources appropriées.

L'opérateur KubeDB surveille `MariaDB` objets à l’aide de l’API Kubernetes. Quand un `MariaDB` est créé, l'opérateur KubeDB créera un nouveau PetSet et un service avec le nom d'objet MariaDB correspondant. L'opérateur KubeDB créera également un service de gouvernance pour le PetSet avec le nom `<mariadb-object-name>-pods`.

```bash
$ kubectl get mariadb -n demo sample-mariadb -o yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"replicas":3,"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}},"storageClassName":"standard"},"storageType":"Durable","deletionPolicy":"WipeOut","version":"11.8.5"}}
  creationTimestamp: "2021-03-16T09:39:01Z"
  finalizers:
  - kubedb.com
  generation: 2
  managedFields:
    ...
  name: sample-mariadb
  namespace: demo
spec:
  authSecret:
    name: sample-mariadb-auth
  podTemplate:
    ...
  replicas: 3
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
  conditions:
  - lastTransitionTime: "2021-03-16T09:39:01Z"
    message: 'The KubeDB operator has started the provisioning of MariaDB: demo/sample-mariadb'
    reason: DatabaseProvisioningStartedSuccessfully
    status: "True"
    type: ProvisioningStarted
  - lastTransitionTime: "2021-03-16T09:40:00Z"
    message: All desired replicas are ready.
    reason: AllReplicasReady
    status: "True"
    type: ReplicaReady
  - lastTransitionTime: "2021-03-16T09:39:09Z"
    message: 'The MariaDB: demo/sample-mariadb is accepting client requests.'
    observedGeneration: 2
    reason: DatabaseAcceptingConnectionRequest
    status: "True"
    type: AcceptingConnection
  - lastTransitionTime: "2021-03-16T09:39:50Z"
    message: 'The MariaDB: demo/sample-mariadb is ready.'
    observedGeneration: 2
    reason: ReadinessCheckSucceeded
    status: "True"
    type: Ready
  - lastTransitionTime: "2021-03-16T09:40:00Z"
    message: 'The MariaDB: demo/sample-mariadb is successfully provisioned.'
    observedGeneration: 2
    reason: DatabaseSuccessfullyProvisioned
    status: "True"
    type: Provisioned
  observedGeneration: 2
  phase: Ready


$ kubectl get petset,svc,secret,pvc,pv,pod -n demo
NAME                              READY   AGE
petset.apps/sample-mariadb   3/3     116m

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/sample-mariadb        ClusterIP   10.97.162.171   <none>        3306/TCP   116m
service/sample-mariadb-pods   ClusterIP   None            <none>        3306/TCP   116m

NAME                                TYPE                                  DATA   AGE
secret/default-token-696cj          kubernetes.io/service-account-token   3      121m
secret/sample-mariadb-auth          kubernetes.io/basic-auth              2      116m
secret/sample-mariadb-token-dk4dx   kubernetes.io/service-account-token   3      116m

NAME                                          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-sample-mariadb-0   Bound    pvc-1e259abc-5937-421a-990c-b903a83d2d8a   1Gi        RWO            standard       116m
persistentvolumeclaim/data-sample-mariadb-1   Bound    pvc-1d0b5bcd-2699-4b87-b57b-3072ddc1027f   1Gi        RWO            standard       116m
persistentvolumeclaim/data-sample-mariadb-2   Bound    pvc-5b85a06e-17f5-487a-9150-e928f5cf4590   1Gi        RWO            standard       116m

NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
persistentvolume/pvc-1d0b5bcd-2699-4b87-b57b-3072ddc1027f   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   standard                116m
persistentvolume/pvc-1e259abc-5937-421a-990c-b903a83d2d8a   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   standard                116m
persistentvolume/pvc-5b85a06e-17f5-487a-9150-e928f5cf4590   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   standard                116m

NAME                   READY   STATUS    RESTARTS   AGE
pod/sample-mariadb-0   1/1     Running   0          116m
pod/sample-mariadb-1   1/1     Running   0          116m
pod/sample-mariadb-2   1/1     Running   0          116m
```

## Connectez-vous à la base de données MariaDB

Une fois la base de données en cours d’exécution, nous pouvons nous connecter à chacun des trois nœuds. Nous utiliserons les identifiants de connexion `MYSQL_ROOT_USERNAME` et `MYSQL_ROOT_PASSWORD` enregistré en tant que variable d’environnement du conteneur.

```bash
# First Node
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1; 
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Second Node
$ kubectl exec -it -n demo sample-mariadb-1 -- bash
```

```mysql
root@sample-mariadb-1:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 94
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Third Node
$ kubectl exec -it -n demo sample-mariadb-2 -- bash
```

```mysql
root@sample-mariadb-2:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 78
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

## Vérifier l'état du cluster

Nous sommes maintenant prêts à vérifier l’état du cluster nouvellement créé. Connectez-vous et exécutez les commandes suivantes à partir de l'un des hôtes et vous obtiendrez le même résultat, c'est-à-dire que la taille du cluster est de trois.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 137
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
1 row in set (0.001 sec)
```

## Disponibilité des données

Dans un cluster MariaDB Galera, chaque membre peut lire et écrire. Dans cette section, nous insérerons les données de n'importe quel nœud et verrons si nous pouvons obtenir les données de tous les autres membres.

> Lisez le commentaire écrit pour les commandes suivantes. Ils contiennent les instructions et explications des commandes.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 202
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE playground;
Query OK, 1 row affected (0.013 sec)

# Create table in Node 1
MariaDB [(none)]> CREATE TABLE playground.equipment ( id INT NOT NULL AUTO_INCREMENT, type VARCHAR(50), quant INT, color VARCHAR(25), PRIMARY KEY(id));
Query OK, 0 rows affected (0.053 sec)

# Insert sample data into Node 1
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 2, 'blue');
Query OK, 1 row affected (0.003 sec)

# Read data from Node 1
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
root@sample-mariadb-0:/ exit
exit
~ $ kubectl exec -it -n demo sample-mariadb-1 -- bash
```

```mysql
root@sample-mariadb-1:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Read data from Node 2
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

#Insert data into node 2
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 4, 'red');
Query OK, 1 row affected (0.032 sec)

# Read data from Node 2 after insertion
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
+----+-------+-------+-------+
2 rows in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
root@sample-mariadb-1:/ exit
exit
~ $ kubectl exec -it -n demo sample-mariadb-2 -- bash
```

```mysql
root@sample-mariadb-2:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Insert data into Node 3
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 4, 'red');
Query OK, 1 row affected (0.005 sec)

# Read data from Node 3
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
|  6 | slide |     4 | red   |
+----+-------+-------+-------+
3 rows in set (0.000 sec)

MariaDB [(none)]> quit
Bye
```

```bash
root@sample-mariadb-2:/# exit
exit
```

## Basculement automatique

Pour tester le basculement automatique, nous allons forcer le redémarrage de l'un des trois pods et vérifier s'il peut rejoindre le cluster.

> Lisez le commentaire écrit pour les commandes suivantes. Ils contiennent les instructions et explications des commandes.

```bash
kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check current data
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
|  6 | slide |     4 | red   |
+----+-------+-------+-------+
3 rows in set (0.002 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
root@sample-mariadb-0:/ exit
exit

# Forcefully delete Node 1
~ $ kubectl delete pod -n demo sample-mariadb-0
pod "sample-mariadb-0" deleted

# Wait for sample-mariadb-0 to restart
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check data after rejoining
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
|  6 | slide |     4 | red   |
+----+-------+-------+-------+
3 rows in set (0.002 sec)

# Check cluster size
MariaDB [(none)]> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
1 row in set (0.002 sec)

MariaDB [(none)]> quit
Bye
```

## Nettoyage

Nettoyez ce que nous avons créé dans ce tutoriel.

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: clustering/mariadb-replication.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB-Cluster MariaDB

Ce didacticiel vous montrera comment utiliser KubeDB pour provisionner une réplication standard MariaDB en mode maître unique.

## Avant de commencer

Avant de continuer :

* Lire [ce](fr/clustering/overview.md#mariadb-standard-replication) pour en savoir plus sur la réplication standard MariaDB.
* Vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel. Exécutez la commande suivante pour préparer votre cluster pour ce didacticiel :

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : Les fichiers yaml utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/clustering/mariadb-replication/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/clustering/mariadb-replication/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Déployer le cluster MariaDB

Ce qui suit est un exemple `MariaDB` objet qui crée un cluster de réplication standard MariaDB à maître unique avec trois membres.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/mariadb-replication/examples/demo-1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Ici,

* `spec.replicas` Définit le nombre de pods (instances) MariaDB dans le cluster.
* `spec.storage` Spécifie la StorageClass de PVC allouée dynamiquement pour stocker les données de cette base de données. Cette spécification de stockage sera transmise au PetSet créé par l'opérateur KubeDB pour exécuter les pods de base de données. Ainsi, chaque membre disposera d’un pod de cette configuration de stockage. Vous pouvez spécifier n'importe quelle StorageClass disponible dans votre cluster avec les demandes de ressources appropriées.
* `spec.topology` Configure la topologie de la base de données et les composants associés.
* `spec.topology.maxscale` Spécifie la configuration du serveur proxy Maxscale.
* `spec.topology.maxscale.replicas` Définit le nombre de réplicas MaxScale dans le petset géré par l'opérateur KubeDB.
* `spec.topology.maxscale.enableUI` Un paramètre booléen (par exemple vrai ou faux) qui contrôle si l'interface graphique MaxScale (accessible via l'API REST) ​​est activée pour l'instance MaxScale.

L'opérateur KubeDB surveille `MariaDB` objets à l’aide de l’API Kubernetes. Quand un `MariaDB` est créé, l'opérateur KubeDB créera un nouveau PetSet et un service avec le nom d'objet MariaDB correspondant. L'opérateur KubeDB créera également un service de gouvernance pour le PetSet avec le nom `<mariadb-object-name>-pods`.

```bash
$ kubectl get mariadb -n demo sample-mariadb -o yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  allowedSchemas:
    namespaces:
      from: Same
  authSecret:
    activeFrom: "2025-04-08T06:42:36Z"
    name: sample-mariadb-auth
  deletionPolicy: WipeOut
  healthChecker:
    failureThreshold: 1
    periodSeconds: 10
    timeoutSeconds: 10
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          limits:
            memory: 1Gi
          requests:
            cpu: 500m
            memory: 1Gi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          runAsGroup: 999
          runAsNonRoot: true
          runAsUser: 999
          seccompProfile:
            type: RuntimeDefault
      - name: md-coordinator
        resources:
          limits:
            memory: 256Mi
          requests:
            cpu: 200m
            memory: 256Mi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          runAsGroup: 999
          runAsNonRoot: true
          runAsUser: 999
          seccompProfile:
            type: RuntimeDefault
      initContainers:
      - name: mariadb-init
        resources:
          limits:
            memory: 512Mi
          requests:
            cpu: 200m
            memory: 256Mi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          runAsGroup: 999
          runAsNonRoot: true
          runAsUser: 999
          seccompProfile:
            type: RuntimeDefault
      podPlacementPolicy:
        name: default
      securityContext:
        fsGroup: 999
      serviceAccountName: sample-mariadb
  replicas: 3
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  storageType: Durable
  topology:
    maxscale:
      enableUI: true
      podTemplate:
        spec:
          containers:
          - name: maxscale
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                drop:
                - ALL
              runAsNonRoot: true
              runAsUser: 997
              seccompProfile:
                type: RuntimeDefault
          initContainers:
          - name: maxscale-init
            resources:
              limits:
                memory: 512Mi
              requests:
                cpu: 200m
                memory: 256Mi
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                drop:
                - ALL
              runAsNonRoot: true
              runAsUser: 997
              seccompProfile:
                type: RuntimeDefault
          podPlacementPolicy:
            name: default
          securityContext:
            fsGroup: 997
          serviceAccountName: sample-mariadb
      replicas: 3
      storage:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
      storageType: Durable
    mode: MariaDBReplication
  version: 12.1.2
status:
  conditions:
  ...
  observedGeneration: 2
  phase: Ready



$ kubectl get petset,svc,secret,pvc,pv,pod -n demo
NAME                                             AGE
petset.apps.k8s.appscode.com/sample-mariadb      53s
petset.apps.k8s.appscode.com/sample-mariadb-mx   56s


NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/sample-mariadb           ClusterIP   10.43.110.13    <none>        3306/TCP            60s
service/sample-mariadb-mx        ClusterIP   10.43.149.170   <none>        3306/TCP,8989/TCP   60s
service/sample-mariadb-mx-pods   ClusterIP   None            <none>        3306/TCP            60s
service/sample-mariadb-pods      ClusterIP   None            <none>        3306/TCP            60s
service/sample-mariadb-standby   ClusterIP   10.43.84.224    <none>        3306/TCP            60s

NAME                                TYPE                                  DATA   AGE
secret/default-token-696cj          kubernetes.io/service-account-token   3      121m
secret/sample-mariadb-auth          kubernetes.io/basic-auth              2      116m
secret/sample-mariadb-token-dk4dx   kubernetes.io/service-account-token   3      116m

NAME                                             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-sample-mariadb-0      Bound    pvc-ce1faccf-8e33-49c6-8520-7b8bb24bb01a   1Gi        RWO            local-path     <unset>                 3m6s
persistentvolumeclaim/data-sample-mariadb-1      Bound    pvc-2fd2d566-0a32-45d8-af0d-88a1f755ccbc   1Gi        RWO            local-path     <unset>                 3m6s
persistentvolumeclaim/data-sample-mariadb-2      Bound    pvc-77a2cc33-4f8b-4de7-a591-acd97ceb3dce   1Gi        RWO            local-path     <unset>                 3m6s
persistentvolumeclaim/data-sample-mariadb-mx-0   Bound    pvc-c6b54166-9c42-4211-9439-ab63fd1aae89   50Mi       RWO            local-path     <unset>                 3m9s
persistentvolumeclaim/data-sample-mariadb-mx-1   Bound    pvc-eaec319b-33d1-4fac-8234-7eadfbad0e61   50Mi       RWO            local-path     <unset>                 3m9s
persistentvolumeclaim/data-sample-mariadb-mx-2   Bound    pvc-733c4cde-3756-44ab-b652-17425e0e210f   50Mi       RWO            local-path     <unset>                 3m9s

NAME                                                        CAPACITY    ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                           STORAGECLASS   REASON   AGE
persistentvolume/pvc-1d0b5bcd-2699-4b87-b57b-3072ddc1027f   1Gi         RWO            Delete           Bound    demo/data-sample-mariadb-1      local-path              116m
persistentvolume/pvc-1e259abc-5937-421a-990c-b903a83d2d8a   1Gi         RWO            Delete           Bound    demo/data-sample-mariadb-0      local-path              116m
persistentvolume/pvc-5b85a06e-17f5-487a-9150-e928f5cf4590   1Gi         RWO            Delete           Bound    demo/data-sample-mariadb-2      local-path              116m
persistentvolume/pvc-c6b54166-9c42-4211-9439-ab63fd1aae89   50Mi        RWO            Delete           Bound    demo/data-sample-mariadb-mx-0   local-path              116m
persistentvolume/pvc-c6b54166-9c42-4211-9439-ab63fd1aae89   50Mi        RWO            Delete           Bound    demo/data-sample-mariadb-mx-1   local-path              116m
persistentvolume/pvc-eaec319b-33d1-4fac-8234-7eadfbad0e61   50Mi        RWO            Delete           Bound    demo/data-sample-mariadb-mx-2   local-path              116m

NAME                   READY   STATUS    RESTARTS   AGE
pod/sample-mariadb-0      2/2     Running   0          3m6s
pod/sample-mariadb-1      2/2     Running   0          3m6s
pod/sample-mariadb-2      2/2     Running   0          3m6s
pod/sample-mariadb-mx-0   1/1     Running   0          3m9s
pod/sample-mariadb-mx-1   1/1     Running   0          3m9s
pod/sample-mariadb-mx-2   1/1     Running   0          3m9s
```

## Vérifier l'état du cluster

Nous sommes maintenant prêts à vérifier l’état du cluster nouvellement créé. Connectez-vous au pod maxscale et exécutez les commandes suivantes à partir de l’un des pods maxscale et vous obtiendrez le même résultat.

```bash
$ kubectl exec -it -n demo svc/sample-mariadb-mx -- bash
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬─────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID    │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-125 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-125 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-125 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴─────────┴────────────────────┘
```

## Connexion à la base de données MariaDB

Une fois la base de données en cours d’exécution, nous pouvons nous connecter à chacun des trois nœuds. Nous utiliserons les identifiants de connexion `MYSQL_ROOT_USERNAME` et `MYSQL_ROOT_PASSWORD` enregistré en tant que variable d’environnement du conteneur.

## Créer un utilisateur test

L'écriture sur une réplique esclave peut entraîner un problème de conflit de journal binaire (binlog). Initialement, la réplique esclave est en mode lecture seule. Mais les utilisateurs disposant de super privilèges peuvent toujours écrire dans la base de données en mode lecture seule. L'utilisateur root possède les privilèges de superutilisateur, lui permettant de modifier une base de données même en mode lecture seule.

Nous vous recommandons d'utiliser un utilisateur non root pour les environnements de production. L'utilisateur root dispose de privilèges étendus, ce qui peut présenter des risques de sécurité. Par conséquent, il est conseillé de créer un utilisateur dédié avec les autorisations appropriées pour une utilisation en production.

```bash
$ kubectl exec -it -n demo svc/sample-mariadb -- bash
mysql@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# create user
MariaDB [(none)]> CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpassword';
Query OK, 0 rows affected (0.001 sec)

# Grant all privileges to the user on all databases
MariaDB [(none)]> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, SHOW DATABASES ON *.* TO 'testuser'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> quit;
Bye
mysql@sample-mariadb-0:/ exit
exit
```

## Vérifier la connectivité à l'aide de l'utilisateur test

```bash
# Master Node
$ kubectl exec -it -n demo svc/sample-mariadb -- bash
```

```mysql
mysql@sample-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1; 
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Slave Node
$ kubectl exec -it -n demo svc/sample-mariadb-standby -- bash
```

```mysql
mysql@sample-mariadb-1:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 94
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye

MariaDB [(none)]> quit;
Bye
```

## Insérer des données et vérifier la disponibilité

Dans un cluster de réplication MariaDB, seul le membre maître peut écrire et le membre esclave peut lire. Dans cette section, nous insérerons les données du nœud maître et verrons si nous pouvons obtenir les données de tous les autres membres esclaves.
`sample-mariadb-0` est le nœud maître dans notre cas.

> Lisez le commentaire écrit pour les commandes suivantes. Ils contiennent les instructions et explications des commandes.

```bash
# master node
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
mysql@sample-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 202
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE playground;
Query OK, 1 row affected (0.013 sec)

# Create table in Node 1
MariaDB [(none)]> CREATE TABLE playground.equipment ( id INT NOT NULL AUTO_INCREMENT, type VARCHAR(50), quant INT, color VARCHAR(25), PRIMARY KEY(id));
Query OK, 0 rows affected (0.053 sec)

# Insert sample data into Node 1
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 2, 'blue');
Query OK, 1 row affected (0.003 sec)

# Read data from Node 1
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
mysql@sample-mariadb-0:/ exit
exit

# check slave node data

$ kubectl exec -it -n demo sample-mariadb-1 -- bash
```

```mysql
mysql@sample-mariadb-1:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Read data from Node 2
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)
MariaDB [(none)]> quit;
Bye
```

```bash
mysql@sample-mariadb-1:/ exit
exit
~ $ kubectl exec -it -n demo sample-mariadb-2 -- bash
```

```mysql
mysql@sample-mariadb-2:/  mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Read data from Node 3
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
3 rows in set (0.000 sec)

MariaDB [(none)]> quit
Bye
```

```bash
mysql@sample-mariadb-2:/# exit
exit
```

## Basculement automatique

Pour tester le basculement automatique, nous forcerons le redémarrage des pods maîtres et vérifierons s'il peut changer de maître et rejoindre le cluster.

> Lisez le commentaire écrit pour les commandes suivantes. Ils contiennent les instructions et explications des commandes.

```bash
# Forcefully delete master node
~ $ kubectl delete pod -n demo sample-mariadb-0
pod "sample-mariadb-0" deleted

Now exec into maxscale server and run the following command to check the server status and ensure the failover is working.

$ kubectl exec -it -n demo svc/sample-mariadb-mx -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬───────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID      │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Down            │ 0-1-14545 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-14545 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-14545 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴───────────┴────────────────────┘
```

```bash
# sample-mariadb-1 is new master.
# Wait some time to up sample-mariadb-0 and check the server list again

bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬───────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID      │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-2-14551 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-2-14551 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-2-14551 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴───────────┴────────────────────┘
```

```bash
All replicas up and srunning now.

# Now check `sample-mariadb-0` data
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
mysql@sample-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check data after rejoining
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
3 rows in set (0.002 sec)

MariaDB [(none)]> quit
Bye
```

## Vérification du proxy et de la répartition lecture-écriture à l'aide de Maxscale

Pour tester le routage du trafic via le serveur MaxScale, créons d'abord un pod contenant l'image de base Ubuntu. Nous utiliserons le yaml suivant.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: ubuntu
  name: ubuntu
  namespace: demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ubuntu
  strategy: {}
  template:
    metadata:
      labels:
        app: ubuntu
    spec:
      containers:
        - image: ubuntu
          imagePullPolicy: IfNotPresent
          name: ubuntu
          command: ["/bin/sleep", "3650d"]
          resources: {}
```

Appliquons le yaml.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/mariadb-replication/examples/ubuntu.yaml
```

```text
deployment.apps/ubuntu created
```

Exécutons dans le pod et installons mariadb-client.

```bash
$ kubectl exec -it -n demo pod/ubuntu-bb47d8d6c-4vhjv -- bash                12:00
mysql@ubuntu-bb47d8d6c-4vhjv:/# apt update
... ... ..
mysql@ubuntu-bb47d8d6c-4vhjv:/# apt install mariadb-client -y
Reading package lists... Done
... .. ...
mysql@ubuntu-bb47d8d6c-4vhjv:/#
```

Essayons maintenant de nous connecter au serveur proxy Maxscale via le `sample-mariadb-mx` service comme le `testuser` utilisateur.

```bash
mysql@ubuntu-bb47d8d6c-4vhjv:/# mariadb -utestuser -ptestpassword -hsample-mariadb-mx.demo -P3306
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

Nous avons réussi à nous connecter en tant que `testuser` utilisateur. Exécutons quelques requêtes de lecture et d'écriture en utilisant cette connexion.

```mysql
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| sys                |
+--------------------+
6 rows in set (0.001 sec)

MariaDB [(none)]> use playground;
Database changed

MariaDB [playground]> show tables;
+----------------------+
| Tables_in_playground |
+----------------------+
| equipment            |
+----------------------+
1 row in set (0.001 sec)

mysql> INSERT INTO equipment (type, quant, color) VALUES ('pot', 2, 'black');
Query OK, 1 row affected (0.01 sec)


MariaDB [playground]> select * from equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  2 | pot   |     2 | black |
+----+-------+-------+-------+
2 rows in set (0.001 sec)


# Currently our server state is -
➤ kubectl exec -it -n demo pod/sample-mariadb-mx-0 -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
```

```bash
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬───────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID      │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 1           │ Slave, Running  │ 0-2-52054 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 1           │ Master, Running │ 0-2-52054 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 1           │ Slave, Running  │ 0-2-52054 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴───────────┴────────────────────┘
```

```bash
# Now lets check read-write split
```

```mysql
MariaDB [playground]> SELECT NOW(),@@hostname;
+---------------------+------------------+
| NOW()               | @@hostname       |
+---------------------+------------------+
| 2025-04-24 13:11:06 | sample-mariadb-2 |
+---------------------+------------------+
1 row in set (0.000 sec)

MariaDB [playground]> SELECT NOW(),@@hostname;
+---------------------+------------------+
| NOW()               | @@hostname       |
+---------------------+------------------+
| 2025-04-24 13:11:31 | sample-mariadb-2 |
+---------------------+------------------+
1 row in set (0.000 sec)

MariaDB [playground]> SELECT NOW(),@@hostname;
+---------------------+------------------+
| NOW()               | @@hostname       |
+---------------------+------------------+
| 2025-04-24 13:12:00 | sample-mariadb-0 |
+---------------------+------------------+
1 row in set (0.000 sec)

# Read queries are executed on the slave replica
# FYI: Both read and write operations can be executed on the master node.

# Now, let's check the write split.

MariaDB [playground]> CREATE DATABASE IF NOT EXISTS test_db;
Query OK, 1 row affected (0.001 sec)

MariaDB [playground]> CREATE TABLE test_db.t1 (id INT, hostname VARCHAR(100));
Query OK, 0 rows affected (0.009 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (1, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (2, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (3, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (4, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> SELECT * FROM test_db.t1;
+------+------------------+
| id   | hostname         |
+------+------------------+
|    1 | sample-mariadb-1 |
|    2 | sample-mariadb-1 |
|    3 | sample-mariadb-1 |
|    4 | sample-mariadb-1 |
+------+------------------+
4 rows in set (0.001 sec)

# Write queries are executed only on the master node.
```

Nous pouvons voir que les requêtes sont exécutées avec succès via le serveur proxy Maxscale et que la répartition des lectures et des écritures fonctionne comme prévu.

## Accédez et explorez l'interface utilisateur MaxScale

Pour activer l'interface utilisateur MaxScale, définissez `spec.topology.maxscale.enableUI: true` dans la configuration. L'interface utilisateur MaxScale s'exécute sur le port 8989. Pour y accéder, utilisez la commande kubectl suivante pour transférer le port :

```bash
➤ kubectl port-forward -n demo service/sample-mariadb-mx 8989:8989
Forwarding from 127.0.0.1:8989 -> 8989
Forwarding from [::1]:8989 -> 8989
```

L'interface utilisateur MaxScale est accessible sur http://127.0.0.1:8989.

Utilisez les informations d'identification par défaut pour vous connecter :

* Nom d'utilisateur : administrateur
* Mot de passe : mariadb

Une fois connecté, vous serez accueilli par un tableau de bord intuitif présentant la liste des serveurs et l'état actuel des nœuds.

![Maxscale Dashboard](images/clustering_mariadb-replication_maxscale-homepage.png)

## Nettoyage

Nettoyons ce que nous avons créé dans ce tutoriel.

```bash
$ kubectl delete mariadb.kubedb.com -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete -n demo deployment.apps/ubuntu
deployment.apps "ubuntu" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: clustering/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Clustering MariaDB

KubeDB prend en charge deux modes de clustering principaux pour MariaDB : le cluster Galera multi-maître MariaDB et la réplication standard maître-esclave MariaDB. Ci-dessous, nous explorons les concepts clés de ces approches de clustering, en mettant en évidence leurs mécanismes, leurs avantages et leurs cas d'utilisation dans un environnement de base de données distribuée.

Ci-dessous, nous explorons les concepts clés du clustering MariaDB, en nous concentrant sur les deux modes de clustering pris en charge par KubeDB : cluster MariaDB Galera multi-maître et réplication standard MariaDB maître-esclave.

## Qu'est-ce que la réplication

La réplication dans MariaDB implique la duplication des données d'un serveur MariaDB (la source) vers un ou plusieurs autres serveurs MariaDB (répliques), plutôt que de les stocker sur un seul serveur. Ce processus améliore la disponibilité des données, l'évolutivité et la tolérance aux pannes. Le mode de réplication détermine les capacités de lecture et d'écriture de chaque serveur du cluster. MariaDB prend en charge deux architectures de réplication principales : multi-maître et maître-esclave.

* Réplication multi-maître : dans une configuration multi-maître, chaque serveur du cluster peut gérer à la fois les opérations de lecture et d'écriture. Cette architecture, illustrée par le cluster MariaDB Galera, garantit une haute disponibilité et une évolutivité en permettant aux applications de répartir les charges de travail sur tous les nœuds.
* Réplication maître-esclave : dans une architecture maître-esclave, le serveur maître prend en charge les opérations de lecture et d'écriture, tandis que les serveurs esclaves sont limités aux opérations de lecture. Cette configuration est idéale pour les charges de travail lourdes en lecture, avec des esclaves offrant une évolutivité pour les requêtes et servant de sauvegardes.

La figure suivante montre un cluster de quatre serveurs MariaDB de réplication multi-maître :

![MariaDB Cluster](images/clustering_overview_galera_small.png)

Référence de l'image : <https://mariadb.com/docs/galera-cluster>

## Réplication Galera

Le cluster MariaDB Galera est un [pratiquement synchrone](https://mariadb.com/kb/en/about-galera-replication/#synchronous-vs-asynchronous-replication) cluster multi-maître pour MariaDB. Le serveur réplique une transaction au moment de la validation en diffusant le jeu d'écriture associé à la transaction à chaque nœud du cluster. Le client se connecte directement au SGBD et expérimente un comportement similaire à celui de MariaDB natif dans la plupart des cas. L'API wsrep (Write Set Replication API) définit l'interface entre la réplication Galera et MariaDB.

Réf : [À propos de la réplication Galera](https://mariadb.com/kb/en/about-galera-replication/)

## Fonctionnalités du cluster MariaDB Galera

* Réplication virtuellement synchrone
* Topologie multi-maître actif-actif
* Lire et écrire sur n'importe quel nœud de cluster
* Contrôle automatique des membres, les nœuds défaillants sont supprimés du cluster
* Rejoindre automatiquement les nœuds
* Véritable réplication parallèle, au niveau des lignes
* Connexions client directes, apparence et convivialité natives de MariaDB

Réf : [Qu'est-ce que le cluster MariaDB Galera ?](https://mariadb.com/kb/en/what-is-mariadb-galera-cluster/#features)

### Limites

Certaines limitations du cluster MariaDB Galera sont répertoriées [ici](https://mariadb.com/kb/en/mariadb-galera-cluster-known-limitations/).

## Réplication standard MariaDB

```mermaid
flowchart LR
  App["Application cliente"] --> Proxy["Service MaxScale (:3306)"]
  Proxy -->|Écritures| Primary["ha-mariadb-0 (Primaire / RW)"]
  Proxy -->|Lectures| Replica1["ha-mariadb-1 (Réplica / RO)"]
  Proxy -->|Lectures| Replica2["ha-mariadb-2 (Réplica / RO)"]
  Primary -->|Binlog asynchrone + GTID| Replica1
  Primary -->|Binlog asynchrone + GTID| Replica2
  Monitor["ReplicationMonitor"] -.->|Détecte la panne et promeut| Replica1
```


La réplication standard MariaDB est un mécanisme largement utilisé pour copier des données d'un serveur MariaDB (maître) vers un ou plusieurs autres serveurs MariaDB (esclave). Ce mode de réplication garantit la redondance des données, améliore la disponibilité et prend en charge l'évolutivité de la lecture en répartissant les opérations de lecture sur plusieurs serveurs. Il fonctionne dans une architecture à maître unique et esclave, dans laquelle le serveur maître gère à la fois les opérations de lecture et d'écriture, tandis que les serveurs esclaves sont limités aux opérations de lecture.

Réf : [À propos de la réplication standard MariadDB](https://mariadb.com/kb/en/replication-overview/#standard-replication)

![MariaDB Standard Replication Cluster](images/clustering_overview_mariadb-standard-replication.png)

## Fonctionnalités du cluster de réplication standard MariaDB

* Réplication asynchrone
* Topologie à maître unique actif-passif
* Lire et écrire sur le maître, et lire uniquement sur le nœud esclave
* Rejoindre automatiquement les nœuds
* Basculement automatique à l'aide du serveur proxy Maxscale
* Réplication basée sur les journaux binaires
* Connexions client directes, apparence et convivialité natives de MariaDB
* Équilibrage de charge à l'aide du serveur proxy Maxscale
* Lecture et écriture partagées à l'aide du serveur proxy Maxscale

### Serveur proxy MariaDB Maxscale

MariaDB MaxScale est un outil qui agit comme intermédiaire entre vos applications et les bases de données MariaDB Server. Cela contribue à améliorer la disponibilité de la base de données, sa capacité à gérer davantage d’utilisateurs et sa sécurité. Cela facilite également la tâche des développeurs en séparant l'application de la configuration de la base de données.

MaxScale a une conception flexible qui prend en charge les modules complémentaires (plugins) pour faire plus qu'un simple équilibrage de charge de base. Par exemple, il peut agir comme un pare-feu de base de données pour protéger vos données. Il est livré avec des plugins intégrés pour acheminer les requêtes, filtrer les données et prendre en charge différents protocoles. Vous pouvez configurer MaxScale pour diriger les requêtes de base de données ou modifier les réponses en fonction de vos besoins, par exemple en masquant des informations sensibles ou en répartissant les requêtes de lecture sur plusieurs serveurs pour gérer davantage de trafic.

L'une de ses fonctionnalités clés est le basculement automatique, qui garantit que votre base de données reste disponible même en cas de panne d'un serveur principal. Le basculement automatique détecte automatiquement un nœud principal défaillant, encourage une réplique à le remplacer et redirige le trafic vers le nouveau nœud principal, minimisant ainsi les temps d'arrêt et assurant le bon fonctionnement de vos applications.

### Comment fonctionne le basculement automatique avec MaxScale

MaxScale utilise un moniteur (comme le plugin MariaDB-Monitor) pour suivre la santé des nœuds de base de données dans une configuration de réplication (par exemple, la réplique principale MariaDB). Si le nœud principal devient indisponible (en raison d'une panne, d'un problème de réseau ou d'une maintenance)

Échelle maximale :

* Détecte l'échec : le moniteur (ReplicationMonitor) vérifie en permanence l'état du nœud (à l'aide de pings MySQL ou de variables d'état).
* Sélectionne un nouveau primaire : il identifie la réplique la plus appropriée en fonction de critères tels que le délai de réplication ou l'état du serveur.
* Favorise la réplique : MaxScale exécute des commandes pour promouvoir la réplique choisie au rang principal (par exemple, STOP SLAVE ; RESET SLAVE ALL ;).
* Reconfigure les réplicas : les autres réplicas sont mis à jour pour être répliqués à partir du nouveau réplica principal.
* Redirige le trafic : le routeur de MaxScale (RW-Split-Router) dirige de manière transparente les requêtes d'écriture vers le nouveau principal et les requêtes de lecture vers les répliques.

Ce processus se déroule automatiquement, généralement en quelques secondes, garantissant ainsi une perturbation minimale.

# Prochaines étapes

* [Déployer le cluster MariaDB Galera](fr/clustering/galera-cluster.md) en utilisant KubeDB.

<!-- PAGE_START: concepts/appbinding.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Liaison d'application

## Qu'est-ce qu'AppBinding

Un `AppBinding` est un Kubernetes `CustomResourceDefinition`(CRD) qui pointe vers une application en utilisant soit son URL (généralement pour une instance de service non résidente de Kubernetes), soit un objet de service Kubernetes (s'il est auto-hébergé dans un cluster Kubernetes), certains paramètres facultatifs et un secret d'identification. Pour en savoir plus sur AppBinding et les problèmes qu'il résout, veuillez lire cet article de blog : [Le cas d’AppBinding](https://appscode.com/blog/post/the-case-for-appbinding).

Si vous déployez une base de données à l'aide [KubeDB](https://kubedb.com/docs/latest/welcome/), `AppBinding` l'objet sera créé automatiquement pour cela. Sinon, vous devez créer un `AppBinding` objet pointant manuellement vers la base de données souhaitée.

KubeDB utilise [Planque](https://appscode.com/products/stash/) pour effectuer une sauvegarde/récupération des bases de données. Stash doit savoir comment se connecter à une base de données cible et les informations d'identification nécessaires pour y accéder. Cela se fait via un `AppBinding`.

## Spécification AppBinding CRD

Comme toute ressource officielle Kubernetes, un `AppBinding` a `TypeMeta`, `ObjectMeta` et `Spec` sections. Cependant, contrairement aux autres ressources Kubernetes, elle ne dispose pas de `Status` section.

Un `AppBinding` objet créé par `KubeDB` pour la base de données MariaDB est illustré ci-dessous,

```yaml
apiVersion: appcatalog.appscode.com/v1alpha1
kind: AppBinding
metadata:
  labels:
    app.kubernetes.io/component: database
    app.kubernetes.io/instance: sample-mariadb
    app.kubernetes.io/managed-by: kubedb.com
    app.kubernetes.io/name: mariadbs.kubedb.com
  name: sample-mariadb
  namespace: demo
spec:
  clientConfig:
    caBundle: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURJekNDQWd1Z0F3SUJBZ0lVVUg1V24wOSt6MnR6RU5ESnF4N1AxZFg5aWM4d0RRWUpLb1pJaHZjTkFRRUwKQlFBd0lURU9NQXdHQTFVRUF3d0ZiWGx6Y1d3eER6QU5CZ05WQkFvTUJtdDFZbVZrWWpBZUZ3MHlNVEF5TURrdwpPVEkxTWpCYUZ3MHlNakF5TURrd09USTFNakJhTUNFeERqQU1CZ05WQkFNTUJXMTVjM0ZzTVE4d0RRWURWUVFLCkRBWnJkV0psWkdJd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUUM3ZDl5YUtMQ3UKYy9NclRBb0NkV1VORld3ckdqbVdvUEVTRWNMR0pjT0JVSTZ5NXZ5QXVGMG1TakZvNzR3SEdSbWRmS2ExMWh0Ygo4TWZ2UFNwWXVGWFpUSi9GbnkwNnU2ekZMVm5xV2h3MUdiZ2ZCUE5XK0w1ZGkzZmVjanBEZmtLbTcrd0ZUVnNmClVzWGVVcUR0VHFpdlJHVUQ5aURUTzNTUmdheVI5U0J0RnRxcHRtV0YrODFqZGlSS2pRTVlCVGJ2MDRueW9UdHUKK0hJZlFjbE40Q1p3NzJPckpUdFdiYnNiWHVlMU5RZU9nQzJmSVhkZEF0WEkxd3lOT04zckxuTFF1SUIrakVLSQpkZTlPandKSkJhSFVzRVZEbllnYlJLSTdIcVdFdk5kL29OU2VZRXF2TXk3K1hwTFV0cDBaVXlxUDV2cC9PSXJ3CmlVMWVxZGNZMzJDcEFnTUJBQUdqVXpCUk1CMEdBMVVkRGdRV0JCUlNnNDVpazFlT3lCU1VKWHkvQllZVDVLck8KeWpBZkJnTlZIU01FR0RBV2dCUlNnNDVpazFlT3lCU1VKWHkvQllZVDVLck95akFQQmdOVkhSTUJBZjhFQlRBRApBUUgvTUEwR0NTcUdTSWIzRFFFQkN3VUFBNElCQVFCNTlhNlFGQm1YMTh1b1dzQ3dGT1Y0R25GYnVBL2NoaVN6CkFwRVVhcjI1L2RNK2RpT0RVNkJuMXM3Wmpqem45WU9aVVJJL3UyRGRhdmNnQUNYR2FXWHJhSS84UUYxZDB3OGsKNXFlRmMxQWE5UEhFeEsxVm1xb21MV2xhMkdTOW1EbFpEOEtueDdjU3lpRmVqRXJYdWtld1B1VXA0dUUzTjAraApwQjQ0MDVRU2d4VVc3SmVhamFQdTNXOHgyRUFKMnViTkdMVEk5L0x4V1Z0YkxGcUFoSFphbGRjaXpOSHdTUGYzCkdMWEo3YTBWTW1JY0NuMWh5a0k2UkNrUTRLSE9tbDNOcXRRS2F5RnhUVHVpdzRiZ3k3czA1UnNzRlVUaWN1VmcKc3hnMjFVQUkvYW9WaXpQOVpESGE2TmV0YnpNczJmcmZBeHhBZk9pWDlzN1JuTmM0WHd4VAotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    service:
      name: sample-mariadb
      port: 3306
      scheme: mysql
  secret:
    name: sample-mariadb-auth
  type: kubedb.com/mariadb
  version: 12.1.2
```

Ici, nous allons décrire les sections d'un `AppBinding` crd.

### Liaison d'application `Spec`

Un `AppBinding` l'objet comporte les champs suivants dans le `spec` section:

#### spec.type

`spec.type` est un champ facultatif qui indique le type d'application que ce `AppBinding` pointe vers. Stash utilise ce champ pour résoudre les valeurs de `TARGET_APP_TYPE`, `TARGET_APP_GROUP` et `TARGET_APP_RESOURCE` variables de [Plan de sauvegarde](https://appscode.com/products/stash/latest/concepts/crds/backupblueprint/) objet.

Ce champ suit le format suivant : `<app group>/<resource kind>`. L'AppBinding ci-dessus pointe vers un `mariadb` ressource sous `kubedb.com` groupe.

Ici, les variables sont analysées comme suit :

| Variable | Usage |
| --- | --- |
| `TARGET_APP_GROUP` | Représente le groupe d'applications auquel appartient l'application respective (c'est-à-dire : `kubedb.com`). |
| `TARGET_APP_RESOURCE` | Représente la ressource sous ce groupe d'applications que cette liaison d'application représente (c'est-à-dire : `mariadb`). |
| `TARGET_APP_TYPE` | Représente le type complet de l’application. C'est simplement `TARGET_APP_GROUP/TARGET_APP_RESOURCE` (c'est-à-dire : `kubedb.com/mariadb`). |

#### spec.secret

`spec.secret` spécifie le nom du secret qui contient les informations d'identification requises pour accéder à la base de données. Ce secret doit être dans le même espace de noms que le `AppBinding`.

Ce secret doit contenir les clés suivantes :

PostgreSQL :

| Clé | Usage |
| --- | --- |
| `POSTGRES_USER` | Nom d'utilisateur de la base de données cible. |
| `POSTGRES_PASSWORD` | Mot de passe de l'utilisateur spécifié par `POSTGRES_USER`. |

MySQL :

| Clé | Usage |
| --- | --- |
| `username` | Nom d'utilisateur de la base de données cible. |
| `password` | Mot de passe de l'utilisateur spécifié par `username`. |

MariaDB :

| Clé | Usage |
| --- | --- |
| `username` | Nom d'utilisateur de la base de données cible. |
| `password` | Mot de passe de l'utilisateur spécifié par `username`. |

MongoDB :

| Clé | Usage |
| --- | --- |
| `username` | Nom d'utilisateur de la base de données cible. |
| `password` | Mot de passe de l'utilisateur spécifié par `username`. |

MariaDB :

| Clé | Usage |
| --- | --- |
| `ADMIN_USERNAME` | Nom d'utilisateur administrateur |
| `ADMIN_PASSWORD` | Mot de passe pour l'utilisateur administrateur |

#### spec.clientConfig

`spec.clientConfig` définit comment communiquer avec la base de données cible. Vous pouvez utiliser une URL ou un service Kubernetes pour vous connecter à la base de données. Vous n’êtes pas obligé de spécifier les deux.

Vous pouvez configurer les champs suivants dans `spec.clientConfig` section:

* **spec.clientConfig.url**

  `spec.clientConfig.url` donne l'emplacement de la base de données, sous forme d'URL standard (c'est-à-dire `[scheme://]host:port/[path]`). Ceci est particulièrement utile lorsque la base de données cible s'exécute en dehors du cluster Kubernetes. Si votre base de données s'exécute à l'intérieur du cluster, utilisez `spec.clientConfig.service` section à la place.
  Notez que si vous tentez d'utiliser un utilisateur ou une authentification de base (par ex. `user:password@host:port`) n'est pas autorisé. Stash les insérera automatiquement à partir du secret respectif. Les fragments ("#…") et les paramètres de requête ("?…") ne sont pas non plus autorisés.
* **spec.clientConfig.service**

  Si vous exécutez la base de données dans le cluster Kubernetes, vous pouvez utiliser le service Kubernetes pour vous connecter à la base de données. Vous devez spécifier les champs suivants dans `spec.clientConfig.service` section si vous créez manuellement un `AppBinding` objet.

  + **nom :** `name` indique le nom du service qui se connecte à la base de données cible.
  + **schéma :** `scheme` spécifie le schéma (c'est-à-dire http, https) à utiliser pour se connecter à la base de données.
  + **port :** `port` spécifie le port sur lequel la base de données cible est exécutée.
* **spec.clientConfig.insecureSkipTLSVerify**

  `spec.clientConfig.insecureSkipTLSVerify` est utilisé pour désactiver la vérification du certificat TLS lors de la connexion à la base de données. Nous déconseillons fortement de désactiver la vérification TLS lors de la sauvegarde. Vous devez fournir le bundle CA correspondant via `spec.clientConfig.caBundle` champ à la place.
* **spec.clientConfig.caBundle**

  `spec.clientConfig.caBundle` est un bundle CA codé PEM qui sera utilisé pour valider le certificat de service de la base de données.

<!-- PAGE_START: concepts/autoscaler.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBAutoscaler

## Qu'est-ce que MariaDBAutoscaler ?

`MariaDBAutoscaler` est un Kubernetes `Custom Resource Definitions` (CRD). Il fournit une configuration déclarative pour la mise à l'échelle automatique des ressources de calcul MariaDB et le stockage des composants de base de données de manière native Kubernetes.

## Spécifications du CRD de MariaDBAutoscaler

Comme toute ressource officielle Kubernetes, un `MariaDBAutoscaler` a `TypeMeta`, `ObjectMeta`, `Spec` et `Status` sections.

Ici, un échantillon `MariaDBAutoscaler` Les CRO pour la mise à l'échelle automatique de différents composants de la base de données sont indiqués ci-dessous :

**Échantillon `MariaDBAutoscaler` pour MariaDB :**

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  compute:
    mariadb:
      trigger: "On"
      podLifeTimeThreshold: 5m
      minAllowed:
        cpu: 250m
        memory: 350Mi
      maxAllowed:
        cpu: 1
        memory: 1Gi
      controlledResources: ["cpu", "memory"]
  storage:
    mariadb:
      trigger: "On"
      usageThreshold: 60
      scalingThreshold: 50
      expansionMode: "Online"
```

Nous allons décrire ici les différentes sections d'un `MariaDBAutoscaler` crd.

A `MariaDBAutoscaler` l'objet comporte les champs suivants dans le `spec` section.

### spec.databaseRef

`spec.databaseRef` est un champ obligatoire qui pointe vers le [MariaDB](fr/concepts/mariadb.md) objet pour lequel l’autoscaling sera effectué. Ce champ est constitué du sous-champ suivant :

* **spec.databaseRef.name :** précise le nom du [MariaDB](fr/concepts/mariadb.md) objet.

### spec.compute

`spec.compute` spécifie la configuration de mise à l'échelle automatique pour les ressources de calcul, c'est-à-dire le processeur et la mémoire des composants de base de données. Ce champ est constitué du sous-champ suivant :

* `spec.compute.mariadb` indique la configuration de mise à l'échelle automatique de calcul souhaitée pour un cluster ou un cluster MariaDB autonome.

Tous ont les sous-champs suivants :

* `trigger` indique si la mise à l'échelle automatique du calcul est activée pour ce composant de la base de données. Si « Activé », la mise à l'échelle automatique de calcul est activée. Si « Désactivé », la mise à l'échelle automatique de calcul est désactivée.
* `minAllowed` spécifie la quantité minimale de ressources qui sera recommandée, la valeur par défaut n'est pas un minimum.
* `maxAllowed` spécifie la quantité maximale de ressources qui sera recommandée, la valeur par défaut n'est pas de maximum.
* `controlledResources` spécifie le type de ressources de calcul (processeur et mémoire) autorisé pour la mise à l'échelle automatique. Les valeurs autorisées sont « cpu » et « mémoire ».
* `containerControlledValues` spécifie quelles valeurs de ressources doivent être contrôlées. Les valeurs autorisées sont « RequestsAndLimits » et « RequestsOnly ».
* `resourceDiffPercentage` spécifie la différence de ressource minimale entre la valeur recommandée et la valeur actuelle en pourcentage. Si le pourcentage de différence est supérieur à cette valeur, la mise à l'échelle automatique sera déclenchée.
* `podLifeTimeThreshold` spécifie la durée de vie minimale d'au moins un des pods avant de déclencher la mise à l'échelle automatique.
* `InMemoryScalingThreshold` le pourcentage de mémoire qui sera transmis comme inMemorySizeGB pour le moteur de base de données inmemory, qui n'est disponible que pour la variante percona de mariadb.

### spec.storage

`spec.compute` spécifie la configuration de mise à l'échelle automatique pour les ressources de stockage des composants de base de données. Ce champ est constitué du sous-champ suivant :

* `spec.compute.mairadb` indique la configuration de mise à l'échelle automatique du stockage souhaitée pour un cluster ou un cluster MariaDB autonome.

Tous ont les sous-champs suivants :

* `trigger` indique si la mise à l'échelle automatique du stockage est activée pour ce composant de la base de données. Si « Activé », la mise à l'échelle automatique du stockage est activée. Si « Désactivé », la mise à l'échelle automatique du stockage est désactivée.
* `usageThreshold` indique le seuil de pourcentage d'utilisation. Si l'utilisation actuelle du stockage dépasse, la mise à l'échelle automatique du stockage sera déclenchée.
* `scalingThreshold` indique le pourcentage du stockage actuel qui sera mis à l'échelle.
* `expansionMode` spécifie le mode d'expansion du volume lorsque l'autoscaler de stockage effectue une extension de volume OpsRequest. La valeur par défaut est `Online`.

<!-- PAGE_START: concepts/mariadb-version.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Version MariaDB

## Qu'est-ce que MariaDBVersion

`MariaDBVersion` est un Kubernetes `Custom Resource Definitions` (CRD). Il fournit une configuration déclarative pour spécifier les images Docker à utiliser pour la base de données MariaDB déployée avec KubeDB de manière native Kubernetes.

Lorsque vous installez KubeDB, un `MariaDBVersion` Une ressource personnalisée sera créée automatiquement pour toutes les versions de MariaDB prises en charge. Vous devez préciser le nom de `MariaDBVersion` crédit dans `spec.version` domaine de [MariaDB](fr/concepts/mariadb.md) crd. Ensuite, KubeDB utilisera les images Docker spécifiées dans le fichier `MariaDBVersion` crd pour créer votre base de données attendue.

L'utilisation d'un crd distinct pour spécifier les images Docker respectives et les noms des politiques de sécurité des pods nous permettent de modifier les images et les politiques indépendamment de l'opérateur KubeDB. Cela permettra également aux utilisateurs d'utiliser une image personnalisée pour la base de données.

## Spécification MariaDBVersion

Comme pour tous les autres objets Kubernetes, une MariaDBVersion a besoin `apiVersion`, `kind`, et `metadata` champs. Il faut également un `.spec` section.

```yaml
apiVersion: catalog.kubedb.com/v1alpha1
kind: MariaDBVersion
metadata:
  annotations:
    meta.helm.sh/release-name: kubedb
    meta.helm.sh/release-namespace: kubedb
  creationTimestamp: "2024-12-19T05:12:32Z"
  generation: 1
  labels:
    app.kubernetes.io/instance: kubedb
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: kubedb-catalog
    app.kubernetes.io/version: v2024.11.18
    helm.sh/chart: kubedb-catalog-v2024.11.18
  name: 11.8.5
  resourceVersion: "1585"
  uid: d6b463f0-032a-4832-8b87-4648da0b38a6
spec:
  archiver:
    addon:
      name: mariadb-addon
      tasks:
        fullBackup:
          name: logical-backup
        fullBackupRestore:
          name: logical-backup-restore
        manifestBackup:
          name: manifest-backup
        manifestRestore:
          name: manifest-restore
        volumeSnapshot:
          name: volume-snapshot
    walg:
      image: ghcr.io/kubedb/mariadb-archiver:v0.9.0_10.5.23-focal
  coordinator:
    image: ghcr.io/kubedb/mariadb-coordinator:v0.29.0
  db:
    image: ghcr.io/appscode-images/mariadb:11.8.5-focal
  exporter:
    image: prom/mysqld-exporter:v0.13.0
  initContainer:
    image: ghcr.io/kubedb/mariadb-init:0.5.2
  maxscale:
    image: mariadb/maxscale:24.02.4
    securityContext:
      runAsUser: 995
  podSecurityPolicies:
    databasePolicyName: maria-db
  securityContext:
    runAsUser: 999
  stash:
    addon:
      backupTask:
        name: mariadb-backup-10.6.23
      restoreTask:
        name: mariadb-restore-10.6.23
  ui:
    - name: phpmyadmin
      version: v2024.4.27
  updateConstraints:
    allowlist:
      - '> 10.5.23, <= 11.5.2'
  version: 10.5.23
```

### metadata.name

`metadata.name` est un champ obligatoire qui spécifie le nom du `MariaDBVersion` crd. Vous devez préciser ce nom dans `spec.version` domaine de [MariaDB](fr/concepts/mariadb.md) crd.

Nous suivons cette convention pour nommer MariaDBVersion crd :

* Format du nom : `{Original MariaDB image version}-{modification tag}`

Nous modifions l'image Docker MariaDB d'origine pour prendre en charge des fonctionnalités supplémentaires. Une image avec une balise de modification plus élevée aura plus de fonctionnalités que les images avec une balise de modification inférieure. Par conséquent, il est recommandé d'utiliser MariaDBVersion crd avec la balise de modification la plus élevée pour profiter des dernières fonctionnalités.

### spec.version

`spec.version` est un champ obligatoire qui spécifie la version originale de la base de données MariaDB qui a été utilisée pour créer l'image Docker spécifiée dans `spec.db.image` champ.

### spec.deprecated

`spec.deprecated` est un champ facultatif qui spécifie si les images Docker spécifiées ici sont prises en charge par l'opérateur KubeDB actuel.

La valeur par défaut de ce champ est `false`. Si `spec.deprecated` est réglé `true`, l'opérateur KubeDB ne créera pas la base de données et les autres ressources respectives pour cette version.

### spec.db.image

`spec.db.image` est un champ obligatoire qui spécifie l'image Docker qui sera utilisée pour créer Petset par l'opérateur KubeDB afin de créer la base de données MariaDB attendue.

### spec.exporter.image

`spec.exporter.image` est un champ obligatoire qui spécifie l'image qui sera utilisée pour exporter les métriques Prometheus.

### spec.initContainer.image

`spec.initContainer.image` est un champ obligatoire qui spécifie l'image qui sera utilisée pour supprimer `lost+found` répertoire et monter un `EmptyDir` volume de données.

### spec.podSecurityPolicies.databasePolicyName

`spec.podSecurityPolicies.databasePolicyName` est un champ obligatoire qui spécifie le nom de la stratégie de sécurité du pod requise pour faire fonctionner le ou les pods du serveur de base de données.

### spec.stash

`spec.stash` est un champ facultatif qui spécifie le nom de la tâche de sauvegarde et de restauration du stockage. En savoir plus sur [Module complémentaire Cacher MariaDB](https://stash.run/)

<!-- PAGE_START: concepts/mariadb.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB

## Qu'est-ce que MariaDB

`MariaDB` est un Kubernetes `Custom Resource Definitions` (CRD). Il fournit une configuration déclarative pour MariaDB de manière native Kubernetes. Il vous suffit de décrire la configuration de base de données souhaitée dans un objet MariaDB, et l'opérateur KubeDB créera pour vous les objets Kubernetes dans l'état souhaité.

## Spécification MariaDB

Comme pour tous les autres objets Kubernetes, une MariaDB a besoin `apiVersion`, `kind`, et `metadata` champs. Il faut également un `.spec` section. Vous trouverez ci-dessous un exemple d'objet MariaDB.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  authSecret:
    kind: Secret
    name: sample-mariadb-auth
  monitor:
    agent: prometheus.io
    prometheus:
      exporter:
        port: 56790
        resources: {}
      serviceMonitor:
        interval: 10s
        labels:
          release: prometheus
  podTemplate:
    controller: {}
    metadata: {}
    spec:
      containers:
      - name: mariadb
        resources:
          limits:
            cpu: 500m
            memory: 1Gi
          requests:
            cpu: 500m
            memory: 1Gi
      serviceAccountName: sample-mariadb
  replicas: 3
  requireSSL: true
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
    storageClassName: standard
  storageType: Durable
  deletionPolicy: WipeOut
  tls:
    certificates:
    - alias: server
      dnsNames:
      - localhost
      ipAddresses:
      - 127.0.0.1
      secretName: sample-mariadb-server-cert
      subject:
        organizations:
        - kubedb:server
    - alias: archiver
      secretName: sample-mariadb-archiver-cert
    - alias: metrics-exporter
      secretName: sample-mariadb-metrics-exporter-cert
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
  version: 12.1.2
```

### spec.version

`spec.version` est un champ obligatoire précisant le nom du [Version MariaDB](fr/concepts/mariadb-version.md) crd où les images du docker sont spécifiées. Actuellement, lorsque vous installez KubeDB, cela crée ce qui suit : `MariaDBVersion` ressources,

* `12.1.2`, `10.4.32`

### spec.authSecret

`spec.authSecret` est un champ facultatif qui pointe vers un secret utilisé pour conserver les informations d'identification de `mariadb` utilisateur root. S'il n'est pas défini, l'opérateur KubeDB crée un nouveau secret `{mariadb-object-name}-auth` pour stocker le mot de passe pour `mariadb` utilisateur root pour chaque objet MariaDB. Si vous souhaitez utiliser un secret existant, veuillez le préciser lors de la création de l'objet MariaDB à l'aide de `spec.authSecret.name`.

Ce secret contient un `username` clé et un `password` clé qui contient le `username` et `password` respectivement pour `mariadb` utilisateur root. Ici, la valeur de `username` la clé est fixée pour être `root`.

Les secrets fournis par les utilisateurs ne sont pas gérés par KubeDB et ne seront donc pas modifiés ni récupérés par l'opérateur KubeDB (version 0.13.0 et supérieure).

Exemple:

```bash
kubectl create secret generic mariadb-auth -n demo \
    --from-literal=username=root \
    --from-literal=password=6q8u_2jMOW-OOZXk
secret/mariadb-auth created
```

```yaml
apiVersion: v1
data:
  password: NnE4dV8yak1PVy1PT1pYaw==
  username: cm9vdA==
kind: Secret
metadata:
  name: mariadb-auth
  namespace: demo
type: Opaque
```

### spec.storageType

`spec.storageType` est un champ facultatif qui spécifie le type de stockage à utiliser pour la base de données. Cela peut être soit `Durable` ou `Ephemeral`. La valeur par défaut de ce champ est `Durable`. Si `Ephemeral` est utilisé, KubeDB créera la base de données MariaDB en utilisant [videDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volume. Dans ce cas, vous n’êtes pas obligé de préciser `spec.storage` champ.

### spec.storage

Si vous définissez `spec.storageType:` à `Durable`, alors `spec.storage` est un champ obligatoire qui spécifie la StorageClass des PVC alloués dynamiquement pour stocker les données de la base de données. Cette spécification de stockage sera transmise au PetSet créé par l'opérateur KubeDB pour exécuter les pods de base de données. Vous pouvez spécifier n'importe quelle StorageClass disponible dans votre cluster avec les demandes de ressources appropriées.

* `spec.storage.storageClassName` est le nom de la StorageClass utilisée pour provisionner les PVC. Les PVC ne doivent pas nécessairement demander un cours. Un PVC avec son storageClassName défini sur "" est toujours interprété comme demandant un PV sans classe, il ne peut donc être lié qu'à des PV sans classe (pas d'annotation ou un ensemble égal à ""). Un PVC sans storageClassName n'est pas tout à fait le même et est traité différemment par le cluster selon que le plugin d'admission DefaultStorageClass est activé ou non.
* `spec.storage.accessModes` utilise les mêmes conventions que les PVC Kubernetes lors de la demande de stockage avec des modes d'accès spécifiques.
* `spec.storage.resources` peut être utilisé pour demander des quantités spécifiques de stockage. Cela suit le même modèle de ressources utilisé par les PVC.

Pour apprendre à configurer `spec.storage`, veuillez consulter les liens ci-dessous :

* <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims>

### spec.init

`spec.init` est une section facultative qui peut être utilisée pour initialiser une base de données MariaDB nouvellement créée. Les bases de données MariaDB peuvent être initialisées de deux manières :

* Initialiser à partir du script
* Initialiser à partir de la restauration du stockage

#### Initialiser via un script

Pour initialiser une base de données MariaDB à l'aide d'un script (script shell, script sql, etc.), définissez le `spec.init.script` lors de la création d'un objet MariaDB. Il exécutera les fichiers par ordre alphabétique avec les extensions `.sh` , `.sql` et `.sql.gz` qui se trouve dans le référentiel. Les scripts contenus dans les dossiers enfants seront ignorés. le script doit contenir les informations suivantes :

* [VolumeSource](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes): L'endroit à partir duquel votre script est chargé.

Vous trouverez ci-dessous un exemple montrant comment un script d'un configMap peut être utilisé pour initialiser une base de données MariaDB.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: 12.1.2
  init:
    script:
      configMap:
        name: md-init-script
```

Dans l'exemple ci-dessus, l'opérateur KubeDB lancera un Job pour exécuter tous les scripts js de `md-init-script` par ordre alphabétique une fois que les pods PetSet sont en cours d’exécution.

### spec.monitor

MariaDB gérée par KubeDB peut être surveillée avec l'opérateur Prometheus et Prometheus intégré prêt à l'emploi.

### spec.requireSSL

`spec.requireSSL` spécifie si les connexions client nécessitent SSL. Si `spec.requireSSL` est `true` alors le serveur autorise uniquement les connexions TCP/IP qui utilisent SSL, ou les connexions qui utilisent un fichier socket (sous Unix) ou une mémoire partagée (sous Windows). Le serveur rejette toute tentative de connexion non sécurisée. Pour plus de détails, veuillez visiter [ici](https://mariadb.com/kb/en/securing-connections-for-client-and-server/#requiring-tls-for-specific-user-accounts)

### spec.tls

`spec.tls` spécifie les configurations TLS/SSL pour MariaDB.

Les champs suivants sont configurables dans le `spec.tls` section:

* `issuerRef` est une référence à `Issuer` ou `ClusterIssuer` RC de [gestionnaire de certificats](https://cert-manager.io/docs/concepts/issuer/) qui sera utilisé par `KubeDB` pour générer les certificats nécessaires.

  + `apiGroup` est le nom de groupe de la ressource référencée. La valeur pour `Issuer` ou `ClusterIssuer` est « cert-manager.io » (cert-manager v0.12.0 et versions ultérieures).
  + `kind` est le type de ressource référencée. KubeDB prend en charge les deux `Issuer` et `ClusterIssuer` comme valeurs pour ce champ.
  + `name` est le nom de la ressource (`Issuer` ou `ClusterIssuer`) étant référencé.
* `certificates` (facultatif) sont une liste de certificats utilisés pour configurer le certificat serveur et/ou client. Il comporte les champs suivants :

  + `alias` représente l'identifiant du certificat. Il a la valeur possible suivante :

    - `server` est utilisé pour l’identification du certificat du serveur.
    - `client` est utilisé pour l’identification du certificat client.
    - `metrics-exporter` est utilisé pour l’identification du certificat de l’exportateur de métriques.
  + `secretName` (facultatif) spécifie le nom secret k8s qui contient les certificats.
    Ce champ est facultatif. Si l'utilisateur ne précise pas ce champ, le nom du secret par défaut sera créé au format suivant : `<database-name>-<cert-alias>-cert`.
  + `subject` (facultatif) spécifie un `X.509` nom distingué. Il a le champ possible suivant,

    - `organizations` (facultatif) sont la liste des différents noms d’organisations à utiliser sur le certificat.
    - `organizationalUnits` (facultatif) sont la liste des différents noms d’unités d’organisation à utiliser sur le certificat.
    - `countries` (facultatif) sont la liste des noms de pays à utiliser sur le certificat.
    - `localities` (facultatif) sont la liste des noms de localités à utiliser sur le certificat.
    - `provinces` (facultatif) est la liste des noms de provinces à utiliser sur le certificat.
    - `streetAddresses` (facultatif) sont la liste d’une adresse postale à utiliser sur le certificat.
    - `postalCodes` (facultatif) sont la liste des codes postaux à utiliser sur le certificat.
    - `serialNumber` (facultatif) est un numéro de série à utiliser sur le certificat.
      Vous pouvez trouver plus de détails sur [Ici](https://golang.org/pkg/crypto/x509/pkix/#Name)
  + `duration` (facultatif) est la période pendant laquelle le certificat est valable.
  + `renewBefore` (facultatif) est un délai spécifiable avant la durée d'expiration.
  + `dnsNames` (facultatif) est une liste de noms alternatifs de sujets à utiliser dans le certificat.
  + `ipAddresses` (facultatif) est une liste d’adresses IP à utiliser dans le certificat.
  + `uriSANs` (facultatif) est une liste de noms alternatifs de sujets URI à définir dans le certificat.
  + `emailSANs` (facultatif) est une liste de noms alternatifs de sujets de courrier électronique à définir dans le certificat.

### spec.configuration

`spec.configuration` est un champ facultatif qui spécifie une configuration personnalisée pour le cluster Mariadb. Il comporte les champs suivants :

* `configuration.inline` est un champ facultatif qui vous permet de fournir une configuration personnalisée directement dans l'objet Mariadb.
  + Extrait de configuration :

    ```yaml
    configuration:
         inline:
           md.cnf: |
             [mysqld]
             max_connections = 500
    ```
* `configuration.secretName` est un champ facultatif qui spécifie le nom du secret contenant les fichiers de configuration personnalisés pour le cluster Mariadb.

### spec.podTemplate

KubeDB permet de fournir un modèle pour le pod de base de données via `spec.podTemplate`. L'opérateur KubeDB transmettra les informations fournies dans `spec.podTemplate` au PetSet créé pour la base de données MariaDB.

KubeDB accepte les champs suivants à définir `spec.podTemplate:`

* `metadata` :
  + `annotations` (annotation du pod)
* `controller` :
  + `annotations` (annotation de petset)
* `spec` :
  + `containers`
  + `volumes`
  + `podPlacementPolicy`
  + `initContainers`
  + `imagePullSecrets`
  + `nodeSelector`
  + `serviceAccountName`
  + `schedulerName`
  + `tolerations`
  + `priorityClassName`
  + `priority`
  + `securityContext`

Utilisations de certains domaines de `spec.podTemplate` est décrit ci-dessous,

Vous pouvez consulter la liste complète [ici](https://github.com/kmodules/offshoot-api/blob/master/api/v2/types.go#L26C1-L279C1).
Utilisations de certains domaines de `spec.podTemplate` est décrit ci-dessous,

#### spec.podTemplate.spec.tolerations

Le `spec.podTemplate.spec.tolerations` est un champ facultatif. Ceci peut être utilisé pour spécifier les tolérances du pod.

#### spec.podTemplate.spec.volumes

Le `spec.podTemplate.spec.volumes` est un champ facultatif. Ceci peut être utilisé pour fournir la liste des volumes pouvant être montés par les conteneurs appartenant au pod.

#### spec.podTemplate.spec.podPlacementPolicy

`spec.podTemplate.spec.podPlacementPolicy` est un champ facultatif. Ceci peut être utilisé pour fournir la référence du `podPlacementPolicy`. `name` de podPlacementPolicy est référencé sous cet attribut. Ceci sera utilisé par notre contrôleur Petset pour placer les pods de base de données dans toute la région, la zone et les nœuds conformément à la politique. Il utilise l'affinité Kubernetes et la fonctionnalité podTopologySpreadContraints pour ce faire.

```yaml
spec:
  podPlacementPolicy:
    name: default
```

#### spec.podTemplate.spec.containers

Le `spec.podTemplate.spec.containers` peut être utilisé pour fournir les conteneurs de liste et leurs configurations au pod de base de données. certains des champs sont décrits ci-dessous,

##### spec.podTemplate.spec.containers[].name

Le `spec.podTemplate.spec.containers[].name` champ utilisé pour spécifier le nom du conteneur spécifié comme DNS\_LABEL. Chaque conteneur d'un pod doit avoir un nom unique (DNS\_LABEL). Ne peut pas être mis à jour.

##### spec.podTemplate.spec.containers[].args

`spec.podTemplate.spec.containers[].args` est un champ facultatif. Cela peut être utilisé pour fournir des arguments supplémentaires à l'installation de la base de données.

##### spec.podTemplate.spec.containers[].resources

`spec.podTemplate.spec.containers[].resources` est un champ facultatif. Cela peut être utilisé pour demander les ressources de calcul requises par les conteneurs des pods de base de données. Pour en savoir plus, visitez [ici](http://kubernetes.io/docs/user-guide/compute-resources/).

##### spec.podTemplate.spec.containers[].env

`spec.podTemplate.spec.env` est un champ facultatif qui spécifie les variables d'environnement à transmettre à l'image Docker MariaDB. Pour connaître les variables d'environnement prises en charge, veuillez visiter [ici](https://hub.docker.com/_/mariadb/).

Notez que KubeDB n'autorise pas `MYSQL_ROOT_PASSWORD`, `MYSQL_ALLOW_EMPTY_PASSWORD`, `MYSQL_RANDOM_ROOT_PASSWORD`, et `MYSQL_ONETIME_PASSWORD` variables d'environnement à définir `spec.env`. Si vous souhaitez définir le mot de passe root, veuillez utiliser `spec.authSecret` au lieu de cela décrit plus tôt.

Si vous essayez de définir l'une des variables d'environnement interdites, c'est-à-dire `MYSQL_ROOT_PASSWORD` dans MariaDB crd, l'opérateur KubeDB rejettera la demande avec l'erreur suivante,

```bash
Error from server (Forbidden): error when creating "./mariadb.yaml": admission webhook "mariadb.validators.kubedb.com" denied the request: environment variable MYSQL_ROOT_PASSWORD is forbidden to use in MariaDB spec
```

Notez également que KubeDB ne permet pas de mettre à jour les variables d'environnement car leur mise à jour n'a aucun effet une fois la base de données créée. Si vous essayez de mettre à jour les variables d'environnement, l'opérateur KubeDB rejettera la demande avec l'erreur suivante :

```bash
Error from server (BadRequest): error when applying patch:
...
for: "./mariadb.yaml": admission webhook "mariadb.validators.kubedb.com" denied the request: precondition failed for:
...At least one of the following was changed:
    apiVersion
    kind
    name
    namespace
    spec.authSecret
    spec.init
    spec.storageType
    spec.storage
    spec.podTemplate.spec.nodeSelector
    spec.podTemplate.spec.env
```

#### spec.podTemplate.spec.imagePullSecrets

`KubeDB` offre la flexibilité de déployer la base de données MariaDB à partir d'un registre Docker privé. `spec.podTemplate.spec.imagePullSecrets` est un champ facultatif qui pointe vers les secrets à utiliser pour extraire l'image Docker si vous utilisez un registre Docker privé.

#### spec.podTemplate.spec.nodeSelector

`spec.podTemplate.spec.nodeSelector` est un champ facultatif qui spécifie une carte de paires clé-valeur. Pour que le pod puisse s'exécuter sur un nœud, le nœud doit avoir chacune des paires clé-valeur indiquées comme étiquettes (il peut également avoir des étiquettes supplémentaires). Pour en savoir plus, voir [ici](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) .

#### spec.podTemplate.spec.serviceAccountName

`serviceAccountName` est un champ facultatif pris en charge par KubeDB Operator (version 0.13.0 et ultérieure) qui peut être utilisé pour spécifier un compte de service personnalisé afin d'affiner le contrôle d'accès basé sur les rôles.

Si ce champ est laissé vide, l'opérateur KubeDB créera un nom de compte de service correspondant au nom de crd MariaDB. Le rôle et le RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés automatiquement pour ce compte de service.

Si un nom de compte de service est donné, mais qu'il n'existe aucun compte de service portant ce nom, l'opérateur KubeDB en créera un, et Role et RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés pour ce compte de service.

Si un nom de compte de service est donné et qu'il existe un compte de service portant ce nom, l'opérateur KubeDB utilisera ce compte de service existant. Étant donné que ce compte de service n'est pas géré par KubeDB, les utilisateurs sont responsables de fournir manuellement les autorisations d'accès nécessaires.

### spec.serviceTemplates

Vous pouvez également fournir un modèle pour les services créés par l'opérateur KubeDB pour la base de données MariaDB via `spec.serviceTemplates`. Cela vous permettra de définir le type et d'autres propriétés des services.

KubeDB permet de définir les champs suivants `spec.serviceTemplates`:

* `metadata` :
  + `annotations`
* `spec` :
  + `type`
  + `ports`
  + `clusterIP`
  + `externalIPs`
  + `loadBalancerIP`
  + `loadBalancerSourceRanges`
  + `externalTrafficPolicy`
  + `healthCheckNodePort`
  + `sessionAffinityConfig`

```yaml
spec:
  version: "12.1.2"
  serviceTemplates:
    - alias: primary
      metadata:
        annotations:
          kubedb.com/test-annotation: "test"
      spec:
        type: LoadBalancer
        ports:
          - port: 3306
```

Voir [ici](https://github.com/kmodules/offshoot-api/blob/kubernetes-1.16.3/api/v1/types.go#L163) pour comprendre ces domaines en détail.

### spec.halted

`spec.halted` est un champ facultatif. Supposons que vous vouliez supprimer le `MariaDB` ressources(`PetSet`, `Service` etc.) sauf `MariaDB` objet, `PVCs` et `Secret` alors vous devez définir `spec.halted` à `true`. Si vous définissez `spec.halted` à `true` alors le `deletionPolicy` dans `MariaDB` l'objet sera défini `Halt` par défaut.

### spec.deletionPolicy

`deletionPolicy` donne la flexibilité de savoir s'il faut `nullify`(rejeter) l'opération de suppression de `MariaDB` crd ou quelles ressources KubeDB doit conserver ou supprimer lorsque vous supprimez `MariaDB` crd. KubeDB fournit les quatre stratégies de résiliation suivantes :

* Ne pas terminer
* Arrêt
* Supprimer (`Default`)
* Anéantir

Quand `deletionPolicy` est `DoNotTerminate`, KubeDB profite de `ValidationWebhook` fonctionnalité dans les clusters Kubernetes 1.9.0 ou version ultérieure à implémenter `DoNotTerminate` fonctionnalité. Si le webhook d'admission est activé, `DoNotTerminate` empêche les utilisateurs de supprimer la base de données tant que le `spec.deletionPolicy` est réglé sur `DoNotTerminate`.

Le tableau suivant montre ce que KubeDB fait lorsque vous supprimez le crd MariaDB pour différentes politiques de résiliation,

| Comportement | Ne pas terminer | Arrêt | Supprimer | Anéantir |
| --- | --- | --- | --- | --- |
| 1. Opération de suppression de bloc | ✓ | ✗ | ✗ | ✗ |
| 2. Supprimer PetSet | ✗ | ✓ | ✓ | ✓ |
| 3. Supprimer des services | ✗ | ✓ | ✓ | ✓ |
| 4. Supprimer les PVC | ✗ | ✗ | ✓ | ✓ |
| 5. Supprimer les secrets | ✗ | ✗ | ✗ | ✓ |
| 6. Supprimer les instantanés | ✗ | ✗ | ✗ | ✓ |

Si vous ne précisez pas `spec.deletionPolicy` KubeDB utilise `Delete` politique de résiliation par défaut.

> Pour plus de détails, vous pouvez visiter [ici](https://appscode.com/blog/post/deletion-policy/)

<!-- PAGE_START: concepts/migrator.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBMigration

## Qu'est-ce que MariaDBMigration

`MariaDBMigration` est un Kubernetes `Custom Resource Definition` (CRD). Il fournit un moyen déclaratif de
migrer une base de données existante, telle qu'une base de données exécutée sur une instance externe ou gérée, vers une base de données
Base de données gérée par KubeDB. Il vous suffit de décrire les bases de données source et cible dans un `MariaDBMigration`
objet, et l'opérateur kubedb-courier exécutera le travail de migration qui copie les données et conserve
la cible synchronisée jusqu'à ce que vous effectuiez le basculement.

`MariaDBMigration` est le CRD de migration spécifique à MariaDB (`courier.kubedb.com/v1alpha1`) dont
`spec.source` et `spec.target` décrire directement la source et la cible MariaDB. Cette page décrit
le `MariaDBMigration` objet pour un **MariaDB** source et cible.

## Spécification de MariaDBMigration

Comme pour tous les autres objets Kubernetes, un `MariaDBMigration` besoins `apiVersion`, `kind`, et `metadata`
champs. Il faut également un `.spec` section. Ci-dessous un exemple `MariaDBMigration` objet pour migrer un
Base de données MariaDB.

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
      database: [] # databases to include
      excludeDatabase: [] # databases to exclude
    snapshot:
      enabled: true
      pipeline:
        workers: 3
        sinkers: 4
        buffer: 12
        read_batch_size: 1000
        write_batch_size: 200
    streaming:
      enabled: true
  target:
    connectionInfo:
      appBinding:
        name: target-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
  jobDefaults:
    imagePullPolicy: IfNotPresent
    backoffLimit: 6
    ttlSecondsAfterFinished: 3600
    activeDeadlineSeconds: 86400
  jobTemplate:
    spec:
      securityContext:
        fsGroup: 65534
```

### spec.source

`spec.source` est un champ obligatoire qui décrit la base de données en cours de migration **depuis**. Il détient le
Champs sources MariaDB (`connectionInfo`, `schema`, `snapshot`, `streaming`) directement.

### spec.target

`spec.target` est un champ obligatoire qui décrit la base de données gérée par KubeDB en cours de migration **dans**.
Il contient directement les champs cibles MariaDB.

### spec.source.connectionInfo

`connectionInfo` (également sous `spec.target`) indique à MariaDBMigration comment se connecter à MariaDB
par exemple. Il existe deux manières de fournir les détails de la connexion : définir **soit** `appBinding` **ou**
`url`:

* `appBinding` — fait référence à un `AppBinding` qui contient les informations de connexion pour cette MariaDB
  par exemple. Un `AppBinding` est une ressource KubeDB qui dissocie les détails de connexion (point de terminaison,
  informations d'identification, TLS) du consommateur ; en créer un avec les informations nécessaires et le référencer
  ici. C'est l'approche recommandée.
  + `name` - nom de l'AppBinding.
  + `namespace` - espace de noms de l'AppBinding.
* `url` — la chaîne de connexion à la base de données (par exemple `mysql://user:password@host:3306/`). Utilisez ceci
  comme alternative à `appBinding` lorsque vous souhaitez fournir le point de terminaison en ligne plutôt que via un
  Liaison d'application.
* `dbName` — la base de données interne utilisée comme point d'entrée de connexion initiale.
* `maxConnections` - limite le nombre de connexions simultanées que la migration ouvre à cette MariaDB
  par exemple.
* `tls` - chemins vers les fichiers PEM pour une connexion compatible TLS. Vous pouvez définir les champs suivants :
  + `caFile` — chemin d'accès au fichier de certificat CA codé en PEM.
  + `certFile` — chemin d'accès au certificat client codé PEM (pour TLS mutuel).
  + `keyFile` — chemin d'accès à la clé privée client codée PEM (pour TLS mutuel).
  + `insecureSkipVerify` - désactive la vérification du certificat du serveur et du nom d'hôte.
  + `serverName` — remplace le nom d'hôte utilisé pour TLS SNI et la vérification du certificat.

> Pour un `KubeDB`-base de données gérée, un `AppBinding` est créé par défaut, vous n'avez donc généralement besoin que de
> créez-en un pour la source. En savoir plus sur [Liaison d'application](fr/concepts/appbinding.md).

### spec.source.schema

`schema` configure la phase de migration du schéma, qui recrée les définitions de base de données et de table sur le
cible avant que les données ne soient copiées.

* `enabled` — active la phase de migration du schéma.
* `database` — liste des bases de données à inclure. Une liste vide signifie toutes les bases de données sauf le système
  bases de données (`mysql`, `information_schema`, `performance_schema`, `sys`).
* `excludeDatabase` — liste des bases de données à exclure de la migration.

### spec.source.snapshot

`snapshot` configure la phase initiale d'instantané en masse, qui copie les lignes existantes de la source
à la cible.

* `enabled` - active la phase d'instantané groupé.
* `pipeline` — ajuste le pipeline de copie parallèle :
  + `workers` — nombre de travailleurs parallèles, chacun traitant simultanément une table distincte. Valeurs par défaut
    à `3`.
  + `sinkers` — nombre de travailleurs d'écriture parallèle poussant les données vers la cible pour chaque travailleur. Valeurs par défaut
    à `3`.
  + `buffer` — taille de la file d'attente en mémoire (en enregistrements) entre les lecteurs et les écrivains. La valeur par défaut est `10`.
  + `read_batch_size` — nombre de lignes récupérées par lot de lecture à partir de la source. La valeur par défaut est `5000`.
  + `write_batch_size` — nombre de lignes écrites par lot sur la cible. La valeur par défaut est `500`.

### spec.source.streaming

`streaming` configure la phase de modification-data-capture (CDC).

* `enabled` - active le streaming CDC une fois l'instantané terminé, gardant la cible en permanence dans
  synchronisez-vous avec les modifications en cours sur la source jusqu'à ce que vous effectuiez la transition.

### spec.jobDefaults

`spec.jobDefaults` est un champ facultatif qui définit les paramètres par défaut pour le travail de migration.

* `imagePullPolicy` — la politique d'extraction d'image pour la tâche de migration. La valeur par défaut est `IfNotPresent`.
* `backoffLimit` — le nombre de tentatives avant que le travail ne soit marqué comme ayant échoué. La valeur par défaut est `6`.
* `ttlSecondsAfterFinished` — le TTL (en secondes) pour nettoyer un Job terminé.
* `activeDeadlineSeconds` — la durée (en secondes) par rapport à son heure de début pendant laquelle le Job peut être
  actif avant que le système ne tente d'y mettre fin.

### spec.jobTemplate

`spec.jobTemplate` est un champ facultatif qui contient la configuration d'exécution pour le pod de tâche de migration.
(un `PodTemplateSpec`). Utilisez-le pour définir les paramètres au niveau du pod tels que `securityContext`, `nodeSelector`,
`resources`, `serviceAccountName`, et ainsi de suite.

## Statut de MariaDBMigration

`status` reflète l’état observé de la migration.

* `status.phase` — la phase actuelle de la migration. L'un des :
  + `Pending` — la migration n'a pas encore commencé.
  + `Running` — la migration est en cours.
  + `Succeeded` — la migration s'est terminée avec succès.
  + `Failed` — la migration a échoué.
* `status.progress` — la progression actuelle de la migration:
  + `dbType` — le type de base de données en cours de migration.
  + `info` — des informations supplémentaires sur les progrès, y compris les `Stage`, `Lag`, et `Progress`
    (ceux-ci apparaissent sous forme de colonnes dans `kubectl get mariadbmigrations`).
* `status.conditions` — un ensemble de conditions décrivant l’état de la migration dans le temps (par
  exemple, `MigratorJobTriggered`, `MigrationRunning`, `MigrationSucceeded`, `MigrationFailed`).

## Prochaines étapes

* Migrez une base de données MariaDB étape par étape avec le [Migration de la base de données MariaDB](fr/migration/databasemigration.md) guide.
* Renseignez-vous sur le [Liaison d'application](fr/concepts/appbinding.md) concept.
* En savoir plus sur le CRD MariaDB [ici](fr/concepts/mariadb.md).

<!-- PAGE_START: concepts/opsrequest.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBOpsRequest

## Qu'est-ce que MariaDBOpsRequest

```mermaid
stateDiagram-v2
  [*] --> Pending: Appliquer MariaDBOpsRequest CR
  Pending --> Progressing: Validation Ops-Manager et verrouillage
  Progressing --> Successful: Mise à jour progressive PetSet/Pod terminée
  Progressing --> Failed: Échec de précondition ou validation
  Successful --> [*]
  Failed --> [*]
```


`MariaDBOpsRequest` est un Kubernetes `Custom Resource Definitions` (CRD). Il fournit une configuration déclarative pour les opérations administratives de MariaDB telles que la mise à jour de la version de la base de données, la mise à l'échelle horizontale, la mise à l'échelle verticale, etc. de manière native Kubernetes.

## Spécifications du CRD MariaDBOpsRequest

Comme toute ressource officielle Kubernetes, un `MariaDBOpsRequest` a `TypeMeta`, `ObjectMeta`, `Spec` et `Status` sections.

Ici, un échantillon `MariaDBOpsRequest` Les CR pour différentes opérations administratives sont indiqués ci-dessous :

**Échantillon `MariaDBOpsRequest` pour mettre à jour la base de données :**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-update
  namespace: demo
spec:
  type: UpdateVersion
  databaseRef:
    name: sample-mariadb
  updateVersion:
    targetVersion: 10.5.23
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Échantillon `MariaDBOpsRequest` Objets pour la mise à l'échelle horizontale du cluster de bases de données :**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdps-scale-horizontal
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: sample-mariadb
  horizontalScaling:
    member : 5
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Échantillon `MariaDBOpsRequest` Objets pour la mise à l'échelle verticale du cluster de bases de données :**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-scale-vertical
  namespace: demo
spec:
  type: VerticalScaling  
  databaseRef:
    name: sample-mariadb
  verticalScaling:
    mariadb:
      resources:
        requests:
          memory: "600Mi"
          cpu: "0.1"
        limits:
          memory: "600Mi"
          cpu: "0.1"
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Échantillon `MariaDBOpsRequest` Objets pour reconfigurer la base de données MariaDB :**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-reconfigure
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:
    applyConfig:
      my-apply.cnf: |-
        [mysqld]
        max_connections = 300
        read_buffer_size = 1234567        
    restart: "true"
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Échantillon `MariaDBOpsRequest` Objets pour l'expansion du volume de MariaDB :**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-volume-expansion
  namespace: demo
spec:
  type: VolumeExpansion  
  databaseRef:
    name: sample-mariadb
  volumeExpansion:   
    mode: "Online"
    mariadb: 2Gi
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Échantillon `MariaDBOpsRequest` Objets de reconfiguration TLS de la base de données :**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-recon-tls-add
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    requireSSL: true
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
```

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-recon-tls-rotate
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    rotateCertificates: true
```

Nous allons décrire ici les différentes sections d'un `MariaDBOpsRequest` crd.

A `MariaDBOpsRequest` l'objet comporte les champs suivants dans le `spec` section.

### spec.databaseRef

`spec.databaseRef` est un champ obligatoire qui pointe vers le [MariaDB](fr/concepts/mariadb.md) objet pour lequel les opérations administratives seront effectuées. Ce champ est constitué du sous-champ suivant :

* **spec.databaseRef.name :** précise le nom du [MariaDB](fr/concepts/mariadb.md) objet.

### spec.type

`spec.type` spécifie le type d'opération qui sera appliqué à la base de données. Actuellement, les types d'opérations suivants sont autorisés dans `MariaDBOpsRequest`.

* `Upgrade` / `UpdateVersion`
* `HorizontalScaling`
* `VerticalScaling`
* `VolumeExpansion`
* `Reconfigure`
* `ReconfigureTLS`
* `Restart`

> Vous ne pouvez effectuer qu'un seul type d'opération sur un seul `MariaDBOpsRequest` CR. Par exemple, si vous souhaitez mettre à jour votre base de données et augmenter sa réplique, vous devez créer deux `MariaDBOpsRequest`. Dans un premier temps, vous devez créer un `MariaDBOpsRequest` pour la mise à jour. Une fois terminé, vous pouvez alors en créer un autre `MariaDBOpsRequest` pour la mise à l'échelle. Il ne faut pas en créer deux `MariaDBOpsRequest` simultanément.

### spec.updateVersion

Si vous souhaitez mettre à jour votre version de MariaDB, vous devez spécifier le `spec.updateVersion` section qui spécifie les informations de version souhaitées. Ce champ est constitué du sous-champ suivant :

* `spec.updateVersion.targetVersion` fait référence à un [Version MariaDB](fr/concepts/mariadb-version.md) CR qui contient les informations de version de MariaDB sur laquelle vous souhaitez mettre à jour.

> Vous ne pouvez mettre à jour qu'entre les versions de MariaDB. KubeDB ne prend pas en charge la rétrogradation pour MariaDB.

### spec.horizontalScaling

Si vous souhaitez augmenter ou réduire votre cluster MariaDB ou ses différents composants, vous devez spécifier `spec.horizontalScaling` section. Ce champ est constitué du sous-champ suivant :

* `spec.horizontalScaling.member` indique le nombre souhaité de nœuds pour le cluster MariaDB après la mise à l'échelle. Par exemple, si votre cluster comporte actuellement 4 nœuds et que vous souhaitez ajouter 2 nœuds supplémentaires, vous devez en spécifier 6 dans `spec.horizontalScaling.member` champ. De même, si vous souhaitez supprimer un nœud du cluster, vous devez en spécifier 3 dans `spec.horizontalScaling.` champ.

### spec.verticalScaling

`spec.verticalScaling` est un champ obligatoire précisant les informations de `MariaDB` des ressources comme `cpu`, `memory` etc qui sera mis à l'échelle. Ce champ est constitué du sous-champ suivant :

* `spec.verticalScaling.mariadb` indique les ressources souhaitées pour MariaDB autonome ou en cluster après la mise à l'échelle.
* `spec.verticalScaling.exporter` indique les ressources souhaitées pour le `exporter` récipient.
* `spec.verticalScaling.coordinator` indique les ressources souhaitées pour le `coordinator` récipient.
* `spec.verticalScaling.mode` spécifie comment la mise à l'échelle est actionnée. `Restart` (valeur par défaut) applique les nouvelles ressources en redémarrant les Pods, tandis que `InPlace` redimensionne les Pods en cours d'exécution en place via Kubernetes `pods/resize` sous-ressource (pas de redémarrage), revenant automatiquement à `Restart` pour tout pod dont le nœud ne peut pas accueillir les nouvelles ressources. Facultatif; par défaut `Restart`. Pour un déploiement distribué, le redimensionnement sur place n'est pas possible. `InPlace` se dégrade en `Restart`.

Tous ont la structure ci-dessous :

```yaml
requests:
  memory: "200Mi"
  cpu: "0.1"
limits:
  memory: "300Mi"
  cpu: "0.2"
```

Ici, lorsque vous spécifiez la demande de ressources, le planificateur utilise ces informations pour décider sur quel nœud placer le conteneur du Pod et lorsque vous spécifiez une limite de ressources pour le conteneur, le `kubelet` applique ces limites afin que le conteneur en cours d'exécution ne soit pas autorisé à utiliser plus de cette ressource que la limite que vous avez définie. Vous pouvez trouver plus de détails sur [ici](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

### spec.volumeExpansion

> Pour utiliser la fonctionnalité d'extension de volume, la classe de stockage doit prendre en charge l'extension de volume.

Si vous souhaitez augmenter le volume de votre standalone ou cluster MariaDB, vous devez spécifier `spec.volumeExpansion` section. Ce champ est constitué du sous-champ suivant :

* `spec.volumeExpansion.mariadb` indique la taille souhaitée pour le volume persistant d'une MariaDB.
* `spec.volumeExpansion.mode` indique le mode d’expansion du volume. Cela peut être `online` ou `offline` en fonction de la classe de stockage.

Tous font référence aux types de quantité de Kubernetes.

Un exemple d'utilisation de ce champ est donné ci-dessous :

```yaml
spec:
  volumeExpansion:
    mariadb: "2Gi"
```

Cela augmentera la taille du volume de tous les nœuds mariadb à 2 Go.

### spec.configuration

Si vous souhaitez reconfigurer votre cluster Running MariaDB avec une nouvelle configuration personnalisée, vous devez spécifier `spec.configuration` section. Ce champ est composé des sous-champs suivants :

* `configSecret` pointe vers un secret dans le même espace de noms d'une ressource MariaDB, qui contient les nouvelles configurations personnalisées. S'il y a un configSecret défini auparavant dans la base de données, ce secret le remplacera.
* `applyConfig` contient la nouvelle configuration personnalisée sous forme de chaîne qui sera fusionnée avec la configuration précédente.
* `removeCustomConfig` supprime toutes les configurations personnalisées du serveur MariaDB.
* `restart` réduit considérablement les temps d’arrêt inutiles.
  + `auto` (par défaut) : redémarrer uniquement si nécessaire (déterminé par l'opérateur du gestionnaire d'opérations)
  + `false`: Si l'utilisateur définit le redémarrage sur false, le pod ne sera pas redémarré et la nouvelle configuration ne sera pas synchronisée avec la base de données.
  + `true`: redémarrez toujours

### spec.tls

Si vous souhaitez reconfigurer la configuration TLS de votre base de données, c'est-à-dire ajouter TLS, supprimer TLS, mettre à jour l'émetteur/cluster ou les certificats et faire pivoter les certificats, vous devez spécifier `spec.tls` section. Ce champ est constitué du sous-champ suivant :

* `spec.tls.issuerRef` spécifie le nom de l'émetteur, le type et le groupe d'API.
* `spec.tls.certificates` précise les certificats. Vous pouvez en apprendre davantage sur ce domaine sur [ici](fr/concepts/mariadb.md#spectls).
* `spec.tls.rotateCertificates` précise que nous souhaitons faire tourner le certificat de cette base de données.
* `spec.tls.remove` précise que nous souhaitons supprimer tls de cette base de données.

### MariaDBOpsRequest `Status`

`.status` décrit l'état actuel et la progression d'un `MariaDBOpsRequest` opération. Il comporte les champs suivants :

### status.phase

`status.phase` indique la phase globale de l'opération pour cette `MariaDBOpsRequest`. Il peut avoir les trois valeurs suivantes :

| Phase | Signification |
| --- | --- |
| `Successful` | KubeDB a effectué avec succès l'opération demandée dans MariaDBOpsRequest |
| `Failed` | KubeDB a échoué à l'opération demandée dans MariaDBOpsRequest |
| `Denied` | KubeDB a refusé l'opération demandée dans MariaDBOpsRequest |

### status.observedGeneration

`status.observedGeneration` montre la génération la plus récente observée par le `MariaDBOpsRequest` contrôleur.

### status.conditions

`status.conditions` est un tableau qui spécifie les conditions des différentes étapes de `MariaDBOpsRequest` traitement. Chaque entrée de condition comporte les champs suivants :

* `types` spécifie le type de la condition. MariaDBOpsRequest a les types de conditions suivants :

| Type | Signification |
| --- | --- |
| `Progressing` | Spécifie que l'opération est maintenant à l'état en cours |
| `Successful` | Spécifie un état tel que l'opération sur la base de données a réussi. |
| `Failed` | Spécifie un état tel que l'opération sur la base de données a échoué. |
| `ScaleDownCluster` | Spécifie un état tel que l'opération de réduction du jeu de réplicas |
| `ScaleUpCluster` | Spécifie un état tel que l'opération de mise à l'échelle du jeu de réplicas |
| `VolumeExpansion` | Spécifie un état tel que l'opération d'expansion du volume de la base de données |
| `Reconfigure` | Spécifie un état tel que la reconfiguration des nœuds du jeu de réplicas |

* Le `status` le champ est une chaîne, avec des valeurs possibles `True`, `False`, et `Unknown`.
  + `status` sera `True` si la transition actuelle réussissait.
  + `status` sera `False` si la transition en cours échoue.
  + `status` sera `Unknown` si la transition actuelle était refusée.
* Le `message` Le champ est un message lisible par l'homme indiquant des détails sur la condition.
* Le `reason` Le champ est une raison CamelCase unique, composée d'un seul mot, pour la dernière transition de la condition.
* Le `lastTransitionTime` Le champ fournit un horodatage de la dernière transition de l'opération d'un état à un autre.
* Le `observedGeneration` montre la génération de transition de condition la plus récente observée par le contrôleur.

<!-- PAGE_START: configuration/using-config-file.md -->
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

```bash
$ kubectl get secret -n demo md-configuration -o yaml
```

```text
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
# Connexion à la base de données
 $ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
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

<!-- PAGE_START: configuration/using-pod-template.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Exécutez MariaDB avec un PodTemplate personnalisé

KubeDB prend en charge la fourniture d'une configuration personnalisée pour MariaDB via [Modèle de pod](fr/concepts/mariadb.md#specpodtemplate). Ce didacticiel vous montrera comment utiliser KubeDB pour exécuter une base de données MariaDB avec une configuration personnalisée à l'aide de PodTemplate.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/configuration/using-pod-template/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/configuration/using-pod-template/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Aperçu

KubeDB permet de fournir un modèle pour le pod de base de données via `spec.podTemplate`. L'opérateur KubeDB transmettra les informations fournies dans `spec.podTemplate` au PetSet créé pour la base de données MariaDB.

KubeDB accepte les champs suivants à définir `spec.podTemplate:`

* `metadata` :
  + `annotations` (annotation du pod)
* `controller` :
  + `annotations` (annotation de petset)
* `spec` :
  + `env`
  + `resources`
  + `initContainers`
  + `imagePullSecrets`
  + `nodeSelector`
  + `schedulerName`
  + `tolerations`
  + `priorityClassName`
  + `priority`
  + `securityContext`

Découvrez les champs en détail dans [Concept de modèle de pod](fr/concepts/mariadb.md#specpodtemplate),

## Configuration du CRD

Vous trouverez ci-dessous le YAML pour MariaDB créé dans cet exemple. Ici, [`spec.podTemplate.spec.env`](fr/concepts/mariadb.md#specpodtemplatespecenv) spécifie les variables d'environnement et [`spec.podTemplate.spec.args`](fr/concepts/mariadb.md#specpodtemplatespecargs) fournit des arguments supplémentaires pour [Image Docker de MariaDB](https://hub.docker.com/_/mariadb/).

Dans ce tutoriel, une base de données initiale `mdDB` sera créé en fournissant `env` `MYSQL_DATABASE` tandis que le jeu de caractères du serveur sera défini sur `utf8mb4` en ajoutant un supplément `args`.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
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
  podTemplate:
    spec:
      containers:
      - name: mariadb
        env:
        - name: MYSQL_DATABASE
          value: mdDB
        args:
        - --character-set-server=utf8mb4
        resources:
          requests:
            memory: "1Gi"
            cpu: "250m"
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/configuration/using-pod-template/examples/md-misc-config.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attendez quelques minutes. L'opérateur KubeDB créera le PVC, le petset, les services, le secret, etc. Si tout se passe bien, nous verrons qu'un pod portant le nom `sample-mariadb` a été créé.

Vérifiez que le pod du petset est en cours d'exécution

```bash
$ kubectl get pod -n demo
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          96s
```

Vérifiez le journal du pod pour voir si la base de données est prête

```bash
$ kubectl logs -f -n demo sample-mariadb-0
2021-03-18 06:06:17+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 06:06:18+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 06:06:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 06:06:19+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  6:06:33 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

Une fois qu'on voit `Note] mysqld: ready for connections.` dans le journal, la base de données est prête.

Nous allons maintenant vérifier si la base de données a démarré avec la configuration personnalisée que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 22
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check mdDB
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mdDB               |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Check character_set_server
MariaDB [(none)]> show variables like 'char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | latin1                     |
| character_set_connection | latin1                     |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | latin1                     |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.001 sec)

MariaDB [(none)]> quit;
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

<!-- PAGE_START: custom-rbac/using-custom-rbac.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Utilisation de ressources RBAC personnalisées

KubeDB (version 0.13.0 et supérieure) prend en charge un contrôle utilisateur plus précis sur les autorisations d'accès basées sur les rôles fournies à une instance MariaDB. Ce didacticiel vous montrera comment utiliser KubeDB pour exécuter une instance MariaDB avec des ressources RBAC personnalisées.

## Avant de commencer

Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).

Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).

Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [ici](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Aperçu

KubeDB permet aux utilisateurs de fournir des ressources RBAC personnalisées, à savoir : `ServiceAccount`, `Role`, et `RoleBinding` pour MariaDB. Ceci est fourni via le `spec.podTemplate.spec.serviceAccountName` champ dans MariaDB crd. Si ce champ est laissé vide, l'opérateur KubeDB créera un nom de compte de service correspondant au nom de crd MariaDB. Le rôle et le RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés automatiquement pour ce compte de service.

Si un nom de compte de service est donné, mais qu'il n'existe aucun compte de service portant ce nom, l'opérateur KubeDB en créera un, et Role et RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés pour ce compte de service.

Si un nom de compte de service est donné et qu'il existe un compte de service portant ce nom, l'opérateur KubeDB utilisera ce compte de service existant. Étant donné que ce compte de service n'est pas géré par KubeDB, les utilisateurs sont responsables de fournir manuellement les autorisations d'accès nécessaires.

Ce guide vous montrera comment créer des `Service Account`, `Role`, et `RoleBinding` pour une instance MariaDB nommée `sample-mariadb` pour fournir le strict minimum d’autorisations d’accès.

## RBAC personnalisé pour MariaDB

Dans un premier temps, créons un `Service Acoount` dans `demo` espace de noms.

```bash
$ kubectl create serviceaccount -n demo md-custom-serviceaccount
serviceaccount/md-custom-serviceaccount created
```

Il devrait créer un compte de service.

```bash
$ kubectl get serviceaccount -n demo md-custom-serviceaccount -o yaml
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: "2021-03-18T04:38:59Z"
  name: md-custom-serviceaccount
  namespace: demo
  resourceVersion: "84669"
  selfLink: /api/v1/namespaces/demo/serviceaccounts/md-custom-serviceaccount
  uid: 788bd6c6-3eae-4797-b6ca-5722ef64c9dc
secrets:
- name: md-custom-serviceaccount-token-jnhvd
```

Maintenant, nous devons créer un rôle disposant des autorisations d'accès nécessaires pour l'instance MariaDB nommée `sample-mariadb`.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-role.yaml
role.rbac.authorization.k8s.io/md-custom-role created
```

Vous trouverez ci-dessous le YAML du rôle que nous venons de créer.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: md-custom-role
  namespace: demo
rules:
- apiGroups:
  - policy
  resourceNames:
  - maria-db
  resources:
  - podsecuritypolicies
  verbs:
  - use
```

Cette autorisation est requise pour les pods MariaDB exécutés sur des clusters compatibles PSP.

Créez maintenant un `RoleBinding` pour lier ça `Role` avec le compte de service déjà créé.

```bash
$ kubectl create rolebinding md-custom-rolebinding --role=md-custom-role --serviceaccount=demo:md-custom-serviceaccount --namespace=demo
rolebinding.rbac.authorization.k8s.io/md-custom-rolebinding created
```

Cela devrait lier `md-custom-role` et `md-custom-serviceaccount` avec succès.

Donc, toutes les ressources requises pour RBAC sont créées.

```bash
$ kubectl get serviceaccount,role,rolebindings -n demo
NAME                                      SECRETS   AGE
serviceaccount/default                    1         38m
serviceaccount/md-custom-serviceaccount   1         36m

NAME                                            CREATED AT
role.rbac.authorization.k8s.io/md-custom-role   2021-03-18T05:13:27Z

NAME                                                          ROLE                  AGE
rolebinding.rbac.authorization.k8s.io/md-custom-rolebinding   Role/md-custom-role   79s
```

Maintenant, créez un crd MariaDB spécifiant `spec.podTemplate.spec.serviceAccountName` champ à `md-custom-serviceaccount`.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-db.yaml
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
  storageType: Durable
  podTemplate:
    spec:
      serviceAccountName: md-custom-serviceaccount
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Maintenant, attendez quelques minutes. l'opérateur KubeDB créera les PVC, PetSet, services, secrets etc. nécessaires. Si tout se passe bien, nous devrions voir qu'un pod avec le nom `sample-mariadb-0` a été créé.

Vérifiez que le pod du petset est en cours d'exécution

```bash
$ kubectl get pod -n demo sample-mariadb-0
NAME            READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          2m44s
```

Vérifiez le journal du pod pour voir si la base de données est prête

```bash
$ kubectl logs -f -n demo sample-mariadb-0
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:35:14+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  5:35:22 0 [Note] Reading of all Master_info entries succeeded
2021-03-18  5:35:22 0 [Note] Added new Master_info '' to hash table
2021-03-18  5:35:22 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

Une fois qu'on voit `mysqld: ready for connections.` dans le journal, la base de données est prête.

## Réutilisation du compte de service

Un compte de service existant peut être réutilisé dans une autre instance MariaDB. Aucune nouvelle autorisation d'accès n'est requise pour exécuter la nouvelle instance MariaDB.

Maintenant, créez le crd MariaDB `another-mariadb` en utilisant le nom du compte de service existant `md-custom-serviceaccount` dans le `spec.podTemplate.spec.serviceAccountName` champ.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-db-2.yaml
mariadb.kubedb.com/another-mariadb created
```

Vous trouverez ci-dessous le YAML du crd MariaDB que nous venons de créer.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: another-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  podTemplate:
    spec:
      serviceAccountName: md-custom-serviceaccount
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Maintenant, attendez quelques minutes. l'opérateur KubeDB créera le PVC, le petset, les services, le secret, etc. nécessaires. Si tout se passe bien, nous devrions voir qu'un pod avec le nom `another-mariadb` a été créé.

Vérifiez que le pod du petset est en cours d'exécution

```bash
$ kubectl get pod -n demo another-mariadb-0
NAME                READY   STATUS    RESTARTS   AGE
another-mariadb-0   1/1     Running   0          37s
```

Vérifiez le journal du pod pour voir si la base de données est prête

```bash
...
$ kubectl logs -f -n demo another-mariadb-0
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:10.5.23+maria~focal started.
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  5:39:59 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

`mysqld: ready for connections.` dans le journal signifie que la base de données fonctionne correctement.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete mariadb -n demo another-mariadb
mariadb.kubedb.com "another-mariadb" deleted
$ kubectl delete -n demo role md-custom-role
role.rbac.authorization.k8s.io "md-custom-role" deleted
$ kubectl delete -n demo rolebinding md-custom-rolebinding
rolebinding.rbac.authorization.k8s.io "md-custom-rolebinding" deleted
$ kubectl delete sa -n demo md-custom-serviceaccount
serviceaccount "md-custom-serviceaccount" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: distributed/overview.md -->
# Présentation du cluster MariaDB Galera distribué

## Introduction

KubeDB permet des déploiements MariaDB distribués à l'aide de la technologie de clustering Galera sur plusieurs clusters Kubernetes, fournissant ainsi une solution de base de données évolutive, hautement disponible et résiliente. En intégrant **Gestion de cluster ouverte (OCM)** pour l'orchestration multicluster et **KubeSlice** pour une connectivité réseau transparente de pod à pod, KubeDB simplifie le déploiement et la gestion des instances MariaDB sur les clusters. UN **Politique de placement** assure un contrôle précis sur la planification des pods, vous permettant de distribuer les pods MariaDB sur les clusters pour une utilisation optimale des ressources et une tolérance aux pannes.

Ce guide fournit un processus étape par étape pour déployer un cluster MariaDB Galera distribué, y compris les conditions préalables, la configuration et les étapes de vérification. Cela suppose une familiarité avec Kubernetes et les concepts de base des bases de données.

> **Vous êtes nouveau sur KubeDB ?** Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

## Comprendre les clusters OCM Hub et Spoke

Dans un **Gestion de cluster ouverte (OCM)** configuration, les clusters sont classés comme suit :

* **Cluster central**: Le plan de contrôle central où les politiques, les applications et les ressources sont définies et gérées. Il orchestre le cycle de vie des applications déployées sur les clusters Spoke.
* **Groupe de rayons**: clusters gérés enregistrés auprès du hub qui exécutent les charges de travail réelles (par exemple, les pods MariaDB).

Lorsqu'un cluster de rayons (par exemple, `demo-worker`) est joint au hub à l'aide du `clusteradm join` commande, OCM crée un espace de noms sur le cluster hub qui correspond au nom du cluster Spoke (par exemple, `demo-worker`). Cet espace de noms est utilisé pour gérer les ressources spécifiques au cluster Spoke à partir du hub.

## Conditions préalables

Avant de déployer un cluster MariaDB Galera distribué, assurez-vous que les conditions suivantes sont remplies :

* **Clusters Kubernetes**: Plusieurs clusters Kubernetes (version 1.26 ou supérieure) configurés et accessibles.
* **Exigences du nœud**: Chaque nœud Kubernetes doit disposer d'au moins 4 vCPU et 16 Go de RAM.
* **Gestion de cluster ouverte (OCM)**: Installer `clusteradm` comme décrit dans le [Guide de démarrage rapide OCM](https://open-cluster-management.io/docs/getting-started/quick-start/).
* **Kubectl**: Installé et configuré pour interagir avec tous les clusters.
* **Barre**: Installé pour le déploiement des composants KubeDB Operator et KubeSlice.
* **Stockage persistant**: Une classe de stockage (par exemple, `local-path` ou une option spécifique au fournisseur de cloud) configurée pour les volumes persistants.

## Étapes de configuration

Suivez ces étapes pour déployer un cluster MariaDB Galera distribué sur plusieurs clusters Kubernetes.

### Étape 1 : Configurer la gestion des clusters ouverts (OCM)

#### 1. Configurez KUBECONFIG

Assurez-vous que votre `KUBECONFIG` est configuré pour basculer entre les clusters. Ce guide utilise deux clusters : `demo-controller` (moyeu et rayon) et `demo-worker` (rayon).

```bash
$ kubectl config get-contexts
```

**Sortir:**

```bash
CURRENT   NAME              CLUSTER           AUTHINFO          NAMESPACE
*         demo-controller   demo-controller   demo-controller   
          demo-worker       demo-worker       demo-worker
```

#### 2. Initialisez le hub OCM

Sur le `demo-controller` cluster, initialisez le hub OCM :

```bash
$ kubectl config use-context demo-controller
$ clusteradm init --wait --feature-gates=ManifestWorkReplicaSet=true
```

#### 3. Vérifiez le déploiement du hub

Vérifiez les dosettes dans le `open-cluster-management-hub` espace de noms pour garantir que tous les composants sont en cours d'exécution :

```bash
$ kubectl get pods -n open-cluster-management-hub
```

**Sortir:**

```
NAME                                                        READY   STATUS    RESTARTS   AGE
cluster-manager-addon-manager-controller-5f99f56896-qpzj8   1/1     Running   0          7m2s
cluster-manager-placement-controller-597d5ff644-wqjq2       1/1     Running   0          7m2s
cluster-manager-registration-controller-6d79d7dcc6-b8h9p    1/1     Running   0          7m2s
cluster-manager-registration-webhook-5d88cf97c7-2sq5m       1/1     Running   0          7m2s
cluster-manager-work-controller-7468bf4dc-5qn6q             1/1     Running   0          7m2s
cluster-manager-work-webhook-c5875947-d272b                 1/1     Running   0          7m2s
```

Tous les modules doivent être dans le `Running` état avec `1/1` préparation et aucun redémarrage, indiquant un déploiement de hub réussi.

#### 4. Enregistrez le cluster Spoke (`demo-worker`)

Obtenez le jeton de jointure du cluster hub :

```bash
$ clusteradm get token
```

**Sortir:**

```
token=<Your_Clusteradm_Join_Token>
please log on spoke and run:
clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name <cluster_name>
```

Sur le `demo-worker` cluster, joignez-le au hub. Inclure le `RawFeedbackJsonString` porte de fonctionnalité pour les commentaires sur les ressources :

```bash
$ kubectl config use-context demo-worker
$ clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name demo-worker --feature-gates=RawFeedbackJsonString=true
```

#### 5. Accepter le cluster Spoke

Sur le `demo-controller` cluster, acceptez le `demo-worker` grappe:

```bash
$ kubectl config use-context demo-controller
$ clusteradm accept --clusters demo-worker
```

> **Note:** Cela peut prendre quelques tentatives (par exemple, réessayer toutes les 10 secondes) si le cluster n'est pas immédiatement disponible.

**Résultat (en cas de succès) :**

```
Starting approve csrs for the cluster demo-worker
CSR demo-worker-2p2pb approved
set hubAcceptsClient to true for managed cluster demo-worker
Your managed cluster demo-worker has joined the Hub successfully.
```

#### 6. Vérifiez la création de l'espace de noms

Confirmez qu'un espace de noms pour `demo-worker` a été créé sur le cluster hub :

```bash
$ kubectl get ns
```

**Sortir:**

```bash
NAME                          STATUS   AGE
default                       Active   99m
demo-worker                   Active   58s
kube-node-lease               Active   99m
kube-public                   Active   99m
kube-system                   Active   99m
open-cluster-management       Active   6m7s
open-cluster-management-hub   Active   5m32s
```

#### 7. Inscrivez-vous `demo-controller` en tant que cluster de rayons

Répétez le processus de jointure et d'acceptation pour `demo-controller` il peut donc également agir comme un cluster de rayons :

```bash
$ kubectl config use-context demo-controller
$ clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name demo-controller --feature-gates=RawFeedbackJsonString=true
$ clusteradm accept --clusters demo-controller
```

Vérifiez l'espace de noms pour `demo-controller`:

```bash
$ kubectl get ns
```

**Sortir:**

```
NAME                                  STATUS   AGE
default                               Active   104m
demo-controller                       Active   3s
demo-worker                           Active   6m7s
kube-node-lease                       Active   104m
kube-public                           Active   104m
kube-system                           Active   104m
open-cluster-management               Active   11m
open-cluster-management-agent         Active   37s
open-cluster-management-agent-addon   Active   34s
open-cluster-management-hub           Active   10m
```

#### 8. Vérifiez les rôles OCM

Après l'enregistrement, utilisez ces commandes pour confirmer quel cluster est le hub et lesquels sont les rayons :

```bash
# Hub: lists all registered spoke clusters
$ kubectl get managedclusters

# Spoke: shows this cluster's registered name
$ kubectl get klusterlet klusterlet -o jsonpath='{.spec.clusterName}'

# Hub components run only on the hub cluster
$ kubectl get pods -n open-cluster-management-hub

# Spoke agent runs on every spoke cluster
$ kubectl get pods -n open-cluster-management-agent
```

### Étape 2 : Configurer la configuration de travail OCM

Exécutez ceci sur **chaque cluster de rayons** (`demo-controller` et `demo-worker`). Cela permet au `RawFeedbackJsonString` porte de fonctionnalité dont KubeDB a besoin pour lire l'état des pods sur les clusters et augmente les limites de débit de l'API pour empêcher la limitation.

> **Note:** Même si tu as réussi `--feature-gates=RawFeedbackJsonString=true` pendant `clusteradm join`, les champs de limite de débit ne sont pas définis par cet indicateur. Exécutez ce correctif sur tous les rayons malgré tout.
>
> **Pourquoi c'est important :** KubeDB utilise le mécanisme de rétroaction ManifestWork d'OCM pour surveiller l'état des pods MariaDB sur les clusters satellites distants. Sans `RawFeedbackJsonString`, le provisionneur KubeDB sur le hub ne reçoit jamais de mises à jour de l'état du pod des rayons et le CR MariaDB distribué restera indéfiniment dans un état non prêt. Les limites de débit empêchent l'agent klusterlet d'être limité par l'API lors de la formation initiale du cluster.

```bash
$ kubectl patch klusterlet klusterlet --type=merge -p '{
  "spec": {
    "workConfiguration": {
      "featureGates": [{"feature": "RawFeedbackJsonString", "mode": "Enable"}],
      "hubKubeAPIBurst": 100,
      "hubKubeAPIQPS": 50,
      "kubeAPIBurst": 100,
      "kubeAPIQPS": 50
    }
  }
}'
```

Vérifiez la configuration :

```bash
$ kubectl get klusterlet klusterlet -oyaml
```

**Exemple de résultat (abrégé) :**

```yaml
apiVersion: operator.open-cluster-management.io/v1
kind: Klusterlet
metadata:
  name: klusterlet
spec:
  clusterName: demo-worker
  workConfiguration:
    featureGates:
    - feature: RawFeedbackJsonString
      mode: Enable
    hubKubeAPIBurst: 100
    hubKubeAPIQPS: 50
    kubeAPIBurst: 100
    kubeAPIQPS: 50
```

### Étape 3 : Configurer KubeSlice pour la connectivité réseau

KubeSlice permet la communication de pod à pod entre les clusters. Installez le contrôleur KubeSlice sur le `demo-controller` cluster et le KubeSlice Worker sur les deux `demo-controller` et `demo-worker` groupes.

#### 1. Installez le contrôleur KubeSlice

Sur `demo-controller`, obtenez d'abord l'adresse du serveur API hub :

```bash
$ kubectl cluster-info | grep 'Kubernetes control plane'
```

Utilisez l'adresse IP et le port de cette sortie comme `endpoint` valeur. Créer un `controller.yaml` déposer:

```yaml
kubeslice:
  controller:
    loglevel: info
    rbacResourcePrefix: kubeslice-rbac
    projectnsPrefix: kubeslice
    endpoint: https://<hub-apiserver-ip>:6443
```

Déployez le contrôleur à l'aide de Helm :

```bash
$ helm upgrade -i kubeslice-controller oci://ghcr.io/appscode-charts/kubeslice-controller \
    --version v2026.1.15 \
    -f controller.yaml \
    --namespace kubeslice-controller \
    --create-namespace \
    --set ocm.enabled=true \
    --wait --burst-limit=10000 --debug
```

Vérifiez l'installation :

```bash
$ kubectl get pods -n kubeslice-controller
```

**Sortir:**

```
NAME                                            READY   STATUS    RESTARTS   AGE
kubeslice-controller-manager-7fd756fff6-5kddd   2/2     Running   0          98s
```

#### 2. Créez un projet KubeSlice

Créer un `project.yaml` déposer:

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: Project
metadata:
  name: demo-distributed-mariadb
  namespace: kubeslice-controller
spec:
  serviceAccount:
    readWrite:
      - admin
```

Appliquer le projet :

```bash
$ kubectl apply -f project.yaml
```

Vérifier:

```bash
$ kubectl get project -n kubeslice-controller
```

**Sortir:**

```bash
NAME                       AGE
demo-distributed-mariadb   31s
```

Vérifiez les comptes de service :

```bash
$ kubectl get sa -n kubeslice-demo-distributed-mariadb
```

**Sortir:**

```
NAME                      SECRETS   AGE
default                   0         69s
kubeslice-rbac-rw-admin   1         68s
```

#### 3. Étiqueter les nœuds pour KubeSlice

Attribuer le `kubeslice.io/node-type=gateway` étiquette au nœud où l’opérateur de travail sera déployé dans les deux clusters.

Sur `demo-controller`:

```bash
$ kubectl get nodes
$ kubectl label node <node-name> kubeslice.io/node-type=gateway
```

Sur `demo-worker`:

```bash
$ kubectl config use-context demo-worker
$ kubectl get nodes
$ kubectl label node <node-name> kubeslice.io/node-type=gateway
```

#### 4. Enregistrez les clusters avec KubeSlice

Identifiez l'interface réseau de chaque cluster en exécutant la commande suivante **sur le nœud passerelle de chaque cluster**:

```bash
$ ip route get 8.8.8.8 | awk '{ print $5 }'
```

**Sortie (exemple) :**

```
enp1s0
```
> **Important:** Le `networkInterface` La valeur doit correspondre à l’interface réseau principale du nœud de passerelle de chaque cluster. Exécutez la commande ci-dessus sur **chaque cluster séparément** et utilisez la sortie de ce cluster comme `networkInterface` valeur. Chaque cluster peut avoir un **nom d'interface différent** - ne présumez pas qu'ils sont identiques. L'utilisation d'un nom d'interface incorrect entraînera l'échec silencieux de la passerelle WireGuard et la réplication MariaDB entre clusters ne se connectera jamais.
>
> Exemple : si `demo-controller` retours `enp3s0` et `demo-worker` retours `eth0`, utilisez ces valeurs exactes dans le YAML ci-dessous.

Créer un `registration.yaml` déposer:

> **Note:**
>
> * Le nom du cluster doit correspondre exactement au nom du cluster OCM (spoke).
> * Le correspondant `ManagedClusterAddOn` La ressource doit être créée dans l'espace de noms qui porte le même nom que le cluster pour configurer automatiquement le travailleur KubeSlice.

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: Cluster
metadata:
  name: demo-controller
  namespace: kubeslice-demo-distributed-mariadb
spec:
  networkInterface: <demo-controller-interface>   # replace with output of ip route command
  clusterProperty: {}
---
apiVersion: controller.kubeslice.io/v1alpha1
kind: Cluster
metadata:
  name: demo-worker
  namespace: kubeslice-demo-distributed-mariadb
spec:
  networkInterface: <demo-worker-interface>   # replace with output of ip route command
  clusterProperty: {}
---
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: kubeslice
  namespace: demo-controller
spec:
  installNamespace: kubeslice-system
  configs:
    - name: demo-controller
      namespace: kubeslice-demo-distributed-mariadb
      group: controller.kubeslice.io
      resource: clusters
---
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: kubeslice
  namespace: demo-worker
spec:
  installNamespace: kubeslice-system
  configs:
    - name: demo-worker
      namespace: kubeslice-demo-distributed-mariadb
      group: controller.kubeslice.io
      resource: clusters
```

Appliquer sur `demo-controller`:

```bash
$ kubectl apply -f registration.yaml
```

Vérifiez qu'OCM déploie les manifestes de travail KubeSlice sur chaque cluster :

```bash
$ kubectl get managedclusteraddon -A
```

**Sortir:**

```
NAMESPACE         NAME        AVAILABLE   DEGRADED   PROGRESSING
demo-controller   kubeslice   Unknown                True
demo-worker       kubeslice   Unknown                True
```

`PROGRESSING: True` signifie qu'OCM se déploie activement. Attendez que `kubeslice-operator` montre `2/2 Running` sur les deux clusters avant de continuer :

```bash
# Run on each spoke cluster
$ kubectl get pods -n kubeslice-system --watch
```

**Résultat attendu (une fois le travailleur KubeSlice entièrement déployé) :**

```
NAME                                 READY   STATUS      RESTARTS   AGE
forwarder-kernel-bw5l4               1/1     Running     0          4m43s
kubeslice-dns-6bd9749f4d-pvh7g       1/1     Running     0          4m43s
kubeslice-install-crds-szhvc         0/1     Completed   0          4m56s
kubeslice-netop-g4dfn                1/1     Running     0          4m43s
kubeslice-operator-949b7d6f7-9wj7h   2/2     Running     0          4m43s
nsc-grpc-server-sbjj7                1/1     Running     0          4m43s
nsm-install-crds-5z4j9               0/1     Completed   0          4m53s
nsmgr-zzwgh                          2/2     Running     0          4m43s
registry-k8s-979455d6d-q2j8x         1/1     Running     0          4m43s
```

#### 5. Espace de noms d'application intégré

Créer un `SliceConfig` embarquer à bord du `demo` (demande) et `kubedb` Espaces de noms (opérateur) pour la connectivité réseau. Créer un `sliceconfig.yaml` déposer:

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: SliceConfig
metadata:
  name: demo-slice
  namespace: kubeslice-demo-distributed-mariadb
spec:
  sliceSubnet: 10.1.0.0/16
  maxClusters: 16
  sliceType: Application
  sliceGatewayProvider:
    sliceGatewayType: Wireguard
    sliceCaType: Local
  sliceIpamType: Local
  rotationInterval: 60
  vpnConfig:
    cipher: AES-128-CBC
  clusters:
    - demo-controller
    - demo-worker
  qosProfileDetails:
    queueType: HTB
    priority: 1
    tcType: BANDWIDTH_CONTROL
    bandwidthCeilingKbps: 5120
    bandwidthGuaranteedKbps: 2560
    dscpClass: AF11
  namespaceIsolationProfile:
    applicationNamespaces:
      - namespace: demo
        clusters:
          - '*'
      - namespace: kubedb
        clusters:
          - '*'
    isolationEnabled: false
    allowedNamespaces:
      - namespace: kube-system
        clusters:
          - '*'
```

Appliquer le `SliceConfig`:

```bash
$ kubectl apply -f sliceconfig.yaml
```

Une fois SliceConfig appliqué, un `vl3-slice-router` le pod apparaîtra dans `kubeslice-system` sur chaque cluster, indiquant que le tunnel VPN de tranche est en cours d'établissement.

#### 6. Configurer DNS pour KubeSlice

> Remarque : Vous devez mettre à jour le serveur DNS pour chaque cluster que vous avez mentionné dans la tranche afin de permettre une découverte appropriée des services entre clusters. Dans ce guide, nous utilisons CoreDNS, les modifications requises sont donc appliquées à la configuration CoreDNS.
> Si votre cluster utilise une solution DNS différente, assurez-vous d'y appliquer des règles de transfert équivalentes.
>
> Cette étape de configuration doit être effectuée sur tous les clusters participant à la tranche avant de continuer.

Mettre à jour CoreDNS pour transférer `*.slice.local` trafic vers le service DNS KubeSlice. Exécutez les étapes suivantes sur **chaque cluster** dans la tranche.

> **Important:** CoreDNS doit être mis à jour et redémarré sur tous les clusters avant de passer à l'étape 4 (installation de KubeDB). Utilisation des nœuds Galera `.slice.local` Noms DNS pour se découvrir entre les clusters. Si le DNS n'est pas configuré avant le démarrage des pods MariaDB, la réplication ne se formera pas.

Obtenez l'adresse IP du service DNS KubeSlice sur chaque cluster :

```bash
$ kubectl get svc -n kubeslice-system -owide -l 'app=kubeslice-dns'
```

**Sortir:**

```bash
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE   SELECTOR
kubeslice-dns   ClusterIP   10.43.172.191   <none>        53/UDP,53/TCP   8d    app=kubeslice-dns
```

Ajoutez le bloc suivant au **haut** de votre CoreDNS `Corefile` ConfigMap (remplacez l'IP par celle de votre cluster) :

```
slice.local:53 {
    errors
    cache 30
    forward . 10.43.172.191
}
```

Exemple de CoreDNS ConfigMap complet après édition :

```bash
$ kubectl get cm -n kube-system coredns -oyaml
```

**Sortir:**

```yaml
apiVersion: v1
data:
  Corefile: |
    slice.local:53 {
        errors
        cache 30
        forward . 10.43.172.191
    }
    .:53 {
        errors
        health
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          fallthrough in-addr.arpa ip6.arpa
        }
        hosts /etc/coredns/NodeHosts {
          ttl 60
          reload 15s
          fallthrough
        }
        prometheus :9153
        cache 30
        loop
        reload
        loadbalance
        import /etc/coredns/custom/*.override
        forward . /etc/resolv.conf
    }
    import /etc/coredns/custom/*.server    
  NodeHosts: |
    10.2.0.248 demo-worker    
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
```

Après avoir modifié le ConfigMap, redémarrez CoreDNS pour appliquer la modification :

```bash
$ kubectl rollout restart deploy/coredns -n kube-system
```

Répétez les étapes de configuration DNS sur chaque cluster de la tranche.

### Étape 4 : Installer l'opérateur KubeDB

> **Note:** Installez l'opérateur KubeDB uniquement sur le cluster hub (`demo-controller`). L'opérateur gère les pods MariaDB sur les clusters Spoke via OCM — aucune installation KubeDB n'est nécessaire sur `demo-worker`.

#### Obtenez une licence gratuite

La licence KubeDB est liée au `kube-system` UID d’espace de noms du cluster hub et a une date d’expiration. Obtenez l'UID de votre cluster et vérifiez la licence avant d'installer :

```bash
# Get your cluster UID (required when requesting the license)
$ kubectl get ns kube-system -o jsonpath='{.metadata.uid}'

# Verify the license is not expired
$ openssl x509 -noout -enddate -in $HOME/Downloads/kubedb-license-<uid>.txt
```

Si elle est expirée ou n'est pas encore obtenue, téléchargez une licence GRATUITE à partir du [Serveur de licences AppsCode](https://appscode.com/issue-license?p=kubedb) en utilisant l'UID du cluster ci-dessus.

```bash
$ helm upgrade -i kubedb oci://ghcr.io/appscode-charts/kubedb \
    --version v2026.2.26 \
    --namespace kubedb --create-namespace \
    --set-file global.license=$HOME/Downloads/kubedb-license-<uid>.txt \
    --set petset.features.ocm.enabled=true \
    --wait --burst-limit=10000 --debug
```

> **Note:** Le `--set petset.features.ocm.enabled=true` L'indicateur doit être défini pour activer la fonctionnalité distribuée MariaDB.

Pour plus de détails, reportez-vous au [Guide d'installation de KubeDB](https://kubedb.com/docs/v2026.7.10/setup/).

Vérifiez que les pods sont en cours d'exécution :

```bash
$ kubectl get pods -n kubedb
```

**Sortir:**

```bash
NAME                                           READY   STATUS    RESTARTS   AGE
kubedb-kubedb-autoscaler-0                     1/2     Running   0          44s
kubedb-kubedb-ops-manager-0                    1/2     Running   0          43s
kubedb-kubedb-provisioner-0                    1/2     Running   0          43s
kubedb-kubedb-webhook-server-df667cd85-tjdp9   2/2     Running   0          44s
kubedb-petset-cf9f5b6f4-d9558                  2/2     Running   0          44s
kubedb-sidekick-5dbf7bcf64-4b8cw               2/2     Running   0          44s
```

### Étape 5 : Définir une politique de placement

Vous pouvez définir le `storageClassName` sous `spec.clusterSpreadConstraint.distributionRules` pour chaque grappe. Si cela n’est pas explicitement spécifié, les clusters sélectionneront automatiquement une classe de stockage appropriée. De plus, vous pouvez contrôler le placement des réplicas en définissant quels réplicas appartiennent à quel cluster. Lors de la mise à l'échelle du nombre de réplicas, la distribution doit également être spécifiée au niveau du cluster. Dans cet exemple, nous utilisons trois répliques.

Pour gérer la distribution des pods entre les clusters, créez un `PlacementPolicy`. A cet effet, définissez un `pod-placement-policy.yaml` fichier comme indiqué ci-dessous :

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        storageClassName: local-path   # optional; omit to use the cluster's default storage class
        replicaIndices:
          - 0
          - 2
      - clusterName: demo-worker
        storageClassName: local-path   # optional; omit to use the cluster's default storage class
        replicaIndices:
          - 1
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Cette politique prévoit :

* `mariadb-0` et `mariadb-2` sur `demo-controller`
* `mariadb-1` sur `demo-worker`

Appliquer la politique sur `demo-controller`:

```bash
$ kubectl apply -f pod-placement-policy.yaml --context demo-controller --kubeconfig $HOME/.kube/config
```

### Étape 6 : Créer une instance MariaDB distribuée

Créer le `demo` espace de noms en premier :

```bash
$ kubectl create namespace demo
```

Définir une ressource personnalisée MariaDB avec `spec.distributed` réglé sur `true` et faire référence au `PlacementPolicy`. Créer un `mariadb.yaml` déposer:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
spec:
  distributed: true
  deletionPolicy: WipeOut
  replicas: 3
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 500Mi
  storageType: Durable
  version: 12.1.2
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
```

Appliquer la ressource sur `demo-controller`:

```bash
$ kubectl apply -f mariadb.yaml --context demo-controller --kubeconfig $HOME/.kube/config
```

### Étape 7 : vérifier le déploiement

#### 1. Vérifiez les ressources et les pods MariaDB sur `demo-controller`

```bash
$ kubectl get md,pods,secret -n demo --context demo-controller --kubeconfig $HOME/.kube/config
```

**Sortir:**

```bash
NAME                         VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb   11.5.2    Ready    99s

NAME            READY   STATUS    RESTARTS   AGE
pod/mariadb-0   3/3     Running   0          95s
pod/mariadb-2   3/3     Running   0          95s

NAME                  TYPE                       DATA   AGE
secret/mariadb-auth   kubernetes.io/basic-auth   2      95s
```

#### 2. Vérifiez les pods et les secrets sur `demo-worker`

```bash
$ kubectl get pods,secrets -n demo --context demo-worker --kubeconfig $HOME/.kube/config
```

**Sortir:**

```bash
NAME        READY   STATUS    RESTARTS   AGE
mariadb-1   3/3     Running   0          95s

NAME                  TYPE                       DATA   AGE
secret/mariadb-auth   kubernetes.io/basic-auth   2      95s
```

#### 3. Vérifiez l'état du cluster Galera

Connectez-vous à un pod MariaDB et vérifiez l'état du cluster Galera. Le DNS du service principal suit le format `<database-name>.<database-namespace>.svc`:

```bash
$ kubectl exec -it -n demo pod/mariadb-0 --context demo-controller -- bash
mariadb -uroot -p$MYSQL_ROOT_PASSWORD -hmariadb.demo.svc
```

Exécutez la requête suivante :

```sql
SHOW STATUS LIKE 'wsrep_cluster_status';
```

**Sortir:**

```bash
+----------------------+---------+
| Variable_name        | Value   |
+----------------------+---------+
| wsrep_cluster_status | Primary |
+----------------------+---------+
1 row in set (0.001 sec)
```

Vérifiez les variables d'état supplémentaires de Galera :

```sql
SHOW STATUS LIKE 'wsrep%';
```

## Prochaines étapes

* **Accéder à la base de données**: Utilisez le `mariadb-auth` secret pour récupérer les informations d'identification et se connecter à l'instance MariaDB.
* **Mise à l'échelle**: Réglez le `PlacementPolicy` pour ajouter ou supprimer des réplicas dans les clusters.
* **Surveillance**: Intégrez KubeDB à des outils de surveillance tels que Prometheus pour obtenir des informations sur l'état du cluster.

<!-- PAGE_START: failover/guide.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Explorer la tolérance aux pannes dans MariaDB avec KubeDB

## Comprendre le basculement et le clustering dans MariaDB sur KubeDB

`Failover` fait référence au processus de commutation automatique vers un système esclave ou une réplique lorsque le `Master`
le nœud de base de données échoue. Dans les systèmes de bases de données à haute disponibilité, le basculement garantit que les services restent
ininterrompu même lorsqu'un ou plusieurs nœuds tombent en panne. Cette fonctionnalité est essentielle dans les environnements cloud natifs modernes.
infrastructures où les temps d’arrêt peuvent entraîner des perturbations majeures.

Lors de l'exécution `MariaDB` sur Kubernetes à l'aide de KubeDB, le basculement devient plus transparent. KubeDB prend en charge deux types de stratégies de clustering MariaDB :

* **Réplication standard (maître-esclave) :**
  La réplication standard est un mécanisme dans lequel un serveur (maître) gère à la fois les opérations de lecture et d'écriture.
  tandis qu'un ou plusieurs serveurs (esclaves) répliquent les données de manière asynchrone et servent des requêtes en lecture seule.
  Cette configuration améliore la redondance des données, la disponibilité et l'évolutivité en lecture, avec un basculement automatique et
  équilibrage de charge pris en charge via `MariaDB MaxScale Server`.

> Remarque : L'écriture sur une réplique esclave peut entraîner un problème de conflit de journal binaire (binlog).

* **Cluster Galera (Multi-Maître) :**
  Dans cette configuration, tous les nœuds agissent comme `Master`, capable de gérer à la fois les opérations de lecture et d’écriture. Puisqu'il y a
  pas de point de défaillance unique, le système offre une réplication synchrone et une haute disponibilité intégrée,
  mais n'utilise pas le concept de basculement traditionnel, car tous les pods sont égaux.

Dans le reste de ce blog, nous nous concentrerons sur le fonctionnement du basculement dans le `standard replication` mode, et comment
KubeDB gère la récupération en cas de panne de nœud.

## Avant de commencer

Avant de continuer :

* Vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour
  communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en
  en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Lire [concept de cluster mariadb](fr/clustering/overview.md) pour en savoir plus sur MariaDB
  Grappe.
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.
  Exécutez la commande suivante pour préparer votre cluster pour ce didacticiel :

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Déployer le cluster MariaDB

Ce qui suit est un exemple `MariaDB` objet qui crée un MariaDB à maître unique `standard replication` cluster composé de trois membres.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: ha-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/galera-cluster/examples/demo-1.yaml
mariadb.kubedb.com/ha-mariadb created
```

Ici,

* `spec.replicas` Définit le nombre de pods (instances) MariaDB dans le cluster.
* `spec.storage` Spécifie la StorageClass de PVC allouée dynamiquement pour stocker les données de cette base de données. Cette spécification de stockage sera transmise au PetSet créé par l'opérateur KubeDB pour exécuter les pods de base de données. Ainsi, chaque membre disposera d’un pod de cette configuration de stockage. Vous pouvez spécifier n'importe quelle StorageClass disponible dans votre cluster avec les demandes de ressources appropriées.
* `spec.topology` Configure la topologie de la base de données et les composants associés.
* `spec.topology.maxscale` Spécifie la configuration du serveur proxy Maxscale.
* `spec.topology.maxscale.replicas` Définit le nombre de réplicas MaxScale dans le petset géré par l'opérateur KubeDB.
* `spec.topology.maxscale.enableUI` Un paramètre booléen (par exemple vrai ou faux) qui contrôle si l'interface graphique MaxScale (accessible via l'API REST) ​​est activée pour l'instance MaxScale.

L'opérateur KubeDB surveille `MariaDB` objets à l’aide de l’API Kubernetes. Quand un `MariaDB` est créé, l'opérateur KubeDB créera un nouveau PetSet et un service avec le nom d'objet MariaDB correspondant. L'opérateur KubeDB créera également un service de gouvernance pour le PetSet avec le nom `<mariadb-object-name>-pods`.

Vous pouvez surveiller l'état jusqu'à ce que tous les pods soient prêts :

```shell
watch kubectl get mariadb,petset,pods -n demo
```

Voir que la base de données est prête.

```shell
$ kubectl get mariadb,petset,pods -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/ha-mariadb   11.8.5   Ready    3m27s

NAME                                             AGE
petset.apps.k8s.appscode.com/ha-mariadb      3m20s
petset.apps.k8s.appscode.com/ha-mariadb-mx   3m23s

NAME                      READY   STATUS    RESTARTS   AGE
pod/ha-mariadb-0      2/2     Running   0          3m20s
pod/ha-mariadb-1      2/2     Running   0          3m20s
pod/ha-mariadb-2      2/2     Running   0          3m20s
pod/ha-mariadb-mx-0   1/1     Running   0          3m23s
pod/ha-mariadb-mx-1   1/1     Running   0          3m23s
pod/ha-mariadb-mx-2   1/1     Running   0          3m23s
```

Inspectez qui est `Master` et qui est `slave`.

```shell
# you can inspect the role of the pods 

$ kubectl get pods -n demo --show-labels | grep role
ha-mariadb-0      2/2     Running   0          4m9s    app.kubernetes.io/component=database,app.kubernetes.io/instance=ha-mariadb,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com,apps.kubernetes.io/pod-index=0,controller-revision-hash=ha-mariadb-598cd56869,kubedb.com/role=Master,statefulset.kubernetes.io/pod-name=ha-mariadb-0
ha-mariadb-1      2/2     Running   0          4m9s    app.kubernetes.io/component=database,app.kubernetes.io/instance=ha-mariadb,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com,apps.kubernetes.io/pod-index=1,controller-revision-hash=ha-mariadb-598cd56869,kubedb.com/role=Slave,statefulset.kubernetes.io/pod-name=ha-mariadb-1
ha-mariadb-2      2/2     Running   0          4m9s    app.kubernetes.io/component=database,app.kubernetes.io/instance=ha-mariadb,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com,apps.kubernetes.io/pod-index=2,controller-revision-hash=ha-mariadb-598cd56869,kubedb.com/role=Slave,statefulset.kubernetes.io/pod-name=ha-mariadb-2
```

La nacelle ayant `kubedb.com/role=Master` est le `Master` et `kubedb.com/role=Slave` sont les esclaves.
Vous pouvez également le vérifier sur l'état du cluster :

```shell
$ kubectl exec -it -n demo svc/ha-mariadb-mx -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬─────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID    │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server1 │ ha-mariadb-0.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-217 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server2 │ ha-mariadb-1.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-217 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server3 │ ha-mariadb-2.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-217 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴─────────┴────────────────────┘
```

## Vérifier l'accessibilité et l'état du pod

Une fois la base de données en cours d’exécution, nous pouvons nous connecter à chacun des trois nœuds.
Nous utiliserons les identifiants de connexion `MYSQL_ROOT_USERNAME` et `MYSQL_ROOT_PASSWORD` enregistré en tant que variable d’environnement du conteneur.

### Créer un utilisateur test

L'écriture sur une réplique esclave peut provoquer des conflits de journaux binaires. Par défaut, les répliques esclaves sont en lecture seule, mais un
l'utilisateur root (avec des super privilèges) peut toujours apporter des modifications. Pour des raisons de sécurité, évitez d'utiliser l'utilisateur root
en production et créez un utilisateur dédié avec uniquement les autorisations nécessaires.

```bash
$ kubectl exec -it -n demo svc/ha-mariadb -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
mysql@ha-mariadb-0:/$ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 443
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpassword';
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]>  GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, SHOW DATABASES ON *.* TO 'testuser'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> quit
Bye
mysql@ha-mariadb-0:/$ exit
exit
```

### Vérifier la connectivité à l'aide de l'utilisateur test

```bash
# Master Node
$ kubectl exec -it -n demo svc/ha-mariadb -- bash
```

```mysql
mysql@ha-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1; 
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Slave Node
$ kubectl exec -it -n demo svc/ha-mariadb-standby -- bash
```

```mysql
mysql@ha-mariadb-1:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 94
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye

MariaDB [(none)]> quit;
Bye
```

## Insérer des données et vérifier la disponibilité

Dans un cluster de réplication MariaDB, seul le membre maître peut écrire et le membre esclave peut lire. Dans cette section, nous insérerons les données du nœud maître et verrons si nous pouvons obtenir les données de tous les autres membres esclaves.
**Vérifiez quel est le pod maître**

```shell
$ kubectl get pods -n demo --show-labels | grep Master | awk '{ print $1 }'
ha-mariadb-0
```

insérons les données dans le nœud maître

```bash
$ kubectl exec -it -n demo ha-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-0:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3459
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE playground;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> CREATE TABLE playground.equipment ( id INT NOT NULL AUTO_INCREMENT, type VARCHAR(50), quant INT, color VARCHAR(25), PRIMARY KEY(id));
Query OK, 0 rows affected (0.032 sec)

MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 2, 'blue');
Query OK, 1 row affected (0.008 sec)

MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

```bash
mysql@ha-mariadb-0:/$ exit
exit
```

Vous pouvez lire les données des nœuds esclaves

```shell
kubectl exec -it -n demo ha-mariadb-1 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-1:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2304
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

```shell
mysql@ha-mariadb-1:/$ exit
exit
```

## Comment fonctionne le basculement

Avant de simuler le basculement, voyons comment cela fonctionne à l'aide de maxscale.

MaxScale utilise un moniteur (comme le plugin MariaDB-Monitor) pour suivre la santé des nœuds de base de données dans une configuration de réplication (par exemple MariaDB maître-esclave). Si le `Master` le nœud devient indisponible en raison d'un crash, d'un problème de réseau ou d'une maintenance.

Échelle maximale :

* Détecte l'échec : le moniteur (ReplicationMonitor) vérifie en permanence l'état du nœud (à l'aide de pings MySQL ou de variables d'état).
* Sélectionne un nouveau `Master`: Il identifie la réplique la plus appropriée en fonction de critères tels que le délai de réplication ou l'état du serveur.
* Favorise la réplique : MaxScale exécute des commandes pour promouvoir la réplique esclave choisie vers `Master` (par exemple, ARRÊTER L'ESCLAVE ; RÉINITIALISER TOUT L'ESCLAVE ;).
* Reconfigure les répliques : d'autres répliques esclaves sont mises à jour pour être répliquées à partir du nouveau `Master`.
* Redirige le trafic : le routeur de MaxScale (RW-Split-Router) dirige de manière transparente les requêtes d'écriture vers le nouveau `Master` et lisez les requêtes sur les répliques esclaves.

Ce processus se déroule automatiquement, généralement en quelques secondes, garantissant ainsi une perturbation minimale.
Ouvrons un autre terminal et surveillons l'état de tous les pods :

```shell
$ watch -n 2 "kubectl get pods -n demo -o jsonpath='{range .items[*]}{.metadata.name} {.metadata.labels.kubedb\\.com/role}{\"\\n\"}{end}'"
```

Vous verrez :

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

### Tests de basculement pratiques

#### Cas 1 : Supprimer le courant `Master`

Supprimons le courant `Master` pod et voyez comment le changement de rôle se produit presque immédiatement.

```shell
$ kubectl delete pods -n demo ha-mariadb-0 
pod "ha-mariadb-0" deleted
```

Vous verrez l’état des pods comme ceci :

```
ha-mariadb-0 Down
ha-mariadb-1 Master
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Après quelques minutes `ha-mariadb-0` reviendra comme `Slave` cosse

```shell
ha-mariadb-0 Slave
ha-mariadb-1 Master
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Maintenant que nous savons comment s'effectue le basculement, vérifions si le nouveau `Master` fonctionne.

```shell
$ kubectl exec -it -n demo ha-mariadb-1 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-1:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 652
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| sys                |
+--------------------+
6 rows in set (0.001 sec)

MariaDB [(none)]> CREATE DATABASE playground2;
Query OK, 1 row affected (0.000 sec)
MariaDB [(none)]> exit
Bye
```

```shell
mysql@ha-mariadb-1:/$ exit
exit
```

Vérifions si le nouvel esclave (`ha-mariadb-0`) a obtenu les données mises à jour du nouveau `Master`, `ha-mariadb-1`.

```shell
$  kubectl exec -it -n demo ha-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-0:/$ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 340
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| playground2        |
| sys                |
+--------------------+
7 rows in set (0.001 sec)

MariaDB [(none)]> exit 
Bye
```

```shell
mysql@ha-mariadb-0:/$ exit
exit
```

#### Cas 2 : Supprimer le courant `Master` et un esclave

```shell
$ kubectl delete pods -n demo ha-mariadb-1 ha-mariadb-2
pod "ha-mariadb-1" deleted
pod "ha-mariadb-2" deleted
```

Encore une fois, nous pouvons constater que le basculement s’est produit assez rapidement.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Down
ha-mariadb-2 Down
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Après 10 à 30 secondes, les pods supprimés seront de retour et auront leur rôle et les deux auront le rôle d'esclave.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Validons l'état du cluster à partir du nouveau `Master`(`ha-mariadb-0`).

```shell
$ kubectl exec -it -n demo ha-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-0:/$ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 377
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| playground2        |
| sys                |
+--------------------+
7 rows in set (0.000 sec)

MariaDB [(none)]> CREATE DATABASE playground3;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> exit
Bye
```

```shell
mysql@ha-mariadb-0:/$ exit
exit
```

Vérifions si les nœuds esclaves, `ha-mariadb-2` récupère toutes les données précédentes

```shell
kubectl exec -it -n demo ha-mariadb-2 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-2:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 47
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| playground2        |
| playground3        |
| sys                |
+--------------------+
8 rows in set (0.001 sec)
```

#### Cas 3 : Supprimez l’un des esclaves

Supprimons les deux nœuds esclaves.

```shell
kubectl delete pods -n demo ha-mariadb-1 ha-mariadb-2
pod "ha-mariadb-1" deleted
pod "ha-mariadb-2" deleted
```

```shell
ha-mariadb-0 Master
ha-mariadb-1 Down
ha-mariadb-2 Down
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Bientôt, les deux modules reprendront leur rôle.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

#### Cas 4 : supprimez les deux `Master` et toutes les répliques d'esclaves

Supprimons tous les pods.

```shell
$ kubectl delete pods -n demo ha-mariadb-0 ha-mariadb-1 ha-mariadb-2
pod "ha-mariadb-0" deleted
pod "ha-mariadb-1" deleted
pod "ha-mariadb-2" deleted
```

```shell
ha-mariadb-0 Down
ha-mariadb-1 Down
ha-mariadb-2 Down
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Dans 20 à 30 secondes, tout le pod devrait être de retour.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Vérifions maintenant l'état du cluster.

```shell
$ kubectl exec -it -n demo svc/ha-mariadb-mx -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬──────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID     │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼──────────┼────────────────────┤
│ server1 │ ha-mariadb-0.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-3297 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼──────────┼────────────────────┤
│ server2 │ ha-mariadb-1.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-3297 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼──────────┼────────────────────┤
│ server3 │ ha-mariadb-2.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-3297 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴──────────┴────────────────────┘
```

## Nettoyage

Pour nettoyer ce que nous avons créé dans ce tutoriel, suivez la commande suivante :

```shell
$ kubectl delete mariadb -n demo ha-mariadb
mariadb.kubedb.com "ha-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

## Prochaines étapes

* En savoir plus sur [sauvegarde et restauration](fr/backup/stash/overview.md) Base de données MariaDB utilisant Stash.
* Vous souhaitez configurer le cluster MariaDB ? Vérifiez comment [configurer le cluster MariaDB hautement disponible](fr/clustering/galera-cluster.md)
* Surveillez votre base de données MariaDB avec KubeDB en utilisant [Prometheus intégré](fr/monitoring/prometheus-operator.md).
* Concepts détaillés de [Objet MariaDB](fr/concepts/mariadb.md).
* Utiliser [registre Docker privé](fr/private-registry/quickstart.md) pour déployer MariaDB avec KubeDB.
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: gitops/gitops.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# GitOps MariaDB utilisant l'opérateur KubeDB GitOps

Ce guide vous montrera comment utiliser `KubeDB` Opérateur GitOps pour créer la base de données MariaDB et gérer les mises à jour à l'aide du workflow GitOps.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README). Passer `--set kubedb-crd-manager.installGitOpsCRDs=true` dans le processus d'installation de kubedb pour activer `GitOps` opérateur.
* Vous devez installer des outils GitOps comme `ArgoCD` ou `FluxCD` et configurez avec votre référentiel Git pour surveiller le référentiel Git et synchroniser l'état du cluster Kubernetes avec l'état souhaité défini dans Git.

  ```bash
  $ kubectl create ns monitoring
  namespace/monitoring created

  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/exemples/mariadb](https://github.com/kubedb/docs/tree/v2026.7.10/docs/examples/mariadb) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

Nous allons utiliser `ArgoCD` dans ce tutoriel. Vous pouvez installer `ArgoCD` dans votre cluster en suivant les étapes [ici](https://argo-cd.readthedocs.io/en/stable/getting_started/). De plus, vous devez installer `argocd` CLI sur votre ordinateur local. Vous pouvez installer `argocd` CLI en suivant les étapes [ici](https://argo-cd.readthedocs.io/en/stable/cli_installation/).

## Création d'applications via CLI

### Pour le référentiel public

```bash
argocd app create kubedb --repo <repo-url> --path kubedb --dest-server https://kubernetes.default.svc --dest-namespace <namespace>
```

### Pour le référentiel privé

#### Utiliser HTTPS

```bash
argocd app create kubedb --repo <repo-url> --path kubedb --dest-server https://kubernetes.default.svc --dest-namespace <namespace> --username <username> --password <github-token>
```

#### Utiliser SSH

Enregistrement d'un référentiel Git dans Argo CD à l'aide de l'authentification SSH

```bash
argocd repo add <ssh-repo-url> \
  --ssh-private-key-path <path-to-private-key>
```

Création d'une application Argo CD pour déployer les ressources du référentiel dans un cluster Kubernetes

```bash
argocd app create <application-name> \
  --repo <repository-url> \
  --path <repository-path> \
  --dest-server <kubernetes-api-server> \
  --dest-namespace <target-namespace>
```

## Créer une base de données MariaDB à l'aide de GitOps

### Créer un CR GitOps MariaDB

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Créez un répertoire comme ci-dessous,

```bash
$ tree .
├── kubedb
    └── MariaDB.yaml
1 directories, 1 files
```

Maintenant, validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est créé dans votre cluster.

Notre `gitops` l'opérateur créera un véritable `MariaDB` base de données CR dans le cluster. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get mariaDB.gitops.kubedb.com,mariaDB.kubedb.com -n demo
NAME                                       AGE
mariadb.gitops.kubedb.com/mariadb-gitops   22m

NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    22m
```

Répertoriez les ressources créées par `kubedb` opérateur créé pour `kubedb.com/v1` MariaDB.

```bash
$ kubectl get petset,pod,secret,service,appbinding -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME                                          AGE
petset.apps.k8s.appscode.com/mariadb-gitops   22m

NAME                   READY   STATUS    RESTARTS   AGE
pod/mariadb-gitops-0   2/2     Running   0          22m
pod/mariadb-gitops-1   2/2     Running   0          22m
pod/mariadb-gitops-2   2/2     Running   0          22m

NAME                         TYPE                       DATA   AGE
secret/mariadb-gitops-auth   kubernetes.io/basic-auth   2      22m

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/mariadb-gitops        ClusterIP   10.43.215.232   <none>        3306/TCP   22m
service/mariadb-gitops-pods   ClusterIP   None            <none>        3306/TCP   22m

NAME                                                TYPE                 VERSION   AGE
appbinding.appcatalog.appscode.com/mariadb-gitops   kubedb.com/mariadb   11.8.5    22m
```

## Mettre à jour la base de données MariaDB à l'aide de GitOps

### Faire évoluer les ressources de la base de données MariaDB

Avant de mettre à l'échelle les ressources de la base de données :

```shell
$ kubectl get pod -n demo mariadb-gitops-0 -o json | jq '.spec.containers[0].resources'
{
  "limits": {
    "memory": "1Gi"
  },
  "requests": {
    "cpu": "500m",
    "memory": "1Gi"
  }
}
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Les demandes et limites de ressources sont mises à jour pour `600m` Processeur et `1.2Gi` Mémoire. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de ressources et créera un `MariaDBOpsRequest` pour mettre à jour le `MariaDB` base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    39m

NAME                                                                     TYPE              STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268   VerticalScaling   Successful   9m17s
```

Une fois que la demande d'opérations devient `Successful`, On peut valider les changements en vérifiant celui du pod,

```bash
$ kubectl get pod -n demo mariadb-gitops-0 -o json | jq '.spec.containers[0].resources'
{
  "limits": {
    "cpu": "600m",
    "memory": "1288490188800m"
  },
  "requests": {
    "cpu": "600m",
    "memory": "1288490188800m"
  }
}
```

### Mettre à l'échelle les répliques MariaDB

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Mettre à jour le `replicas` à `5`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.
Maintenant, `gitops` L'opérateur détectera les modifications de la réplique et créera un `HorizontalScaling` MariaDBOpsRequest pour mettre à jour le `MariaDB` répliques de bases de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    107m

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   63m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   76m
```

Une fois que la demande d'opérations devient `Successful`, On peut valider les modifications en vérifiant le nombre de pods,

```bash
$ kubectl get pod -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME               READY   STATUS    RESTARTS   AGE
mariadb-gitops-0   2/2     Running   0          76m
mariadb-gitops-1   2/2     Running   0          75m
mariadb-gitops-2   2/2     Running   0          73m
mariadb-gitops-3   2/2     Running   0          63m
mariadb-gitops-4   2/2     Running   0          62m
```

Nous pouvons également réduire les répliques en mettant à jour le `replicas` champs.

### Développer le volume MariaDB

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
```

Mettre à jour le `storage.resources.requests.storage` à `2Gi`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de volume et créera un `VolumeExpansion` MariaDBOpsRequest pour mettre à jour le `MariaDB` volume de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    111m

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   68m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   81m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   115s
```

Une fois que la demande d'opérations devient `Successful`, Nous pouvons valider les modifications en vérifiant la taille du pvc,

```bash
$ kubectl get pvc -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
data-mariadb-gitops-0   Bound    pvc-f1a49c53-d095-43a7-b62f-e91a5a9f5496   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-1   Bound    pvc-79d99636-e0d7-413f-a6a6-559e908ed817   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-2   Bound    pvc-f66ccf56-63b6-4ac6-a7f9-09f573466266   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-3   Bound    pvc-b7744652-611a-4c10-a06f-c93f030fb90f   2Gi        RWO            longhorn       <unset>                 72m
data-mariadb-gitops-4   Bound    pvc-dee1c10d-0456-4935-9306-0d86c3db54d0   2Gi        RWO            longhorn       <unset>                 71m
```

## Reconfigurer MariaDB

Dans un premier temps, nous allons créer un secret contenant `user.conf` fichier avec les paramètres de configuration requis.
Pour en savoir plus sur ce fichier de configuration, consultez [ici](fr/reconfigure/overview.md)

```yaml
apiVersion: v1
stringData:
  user.cnf: |
    [mysqld]
    max_connections = 200
    read_buffer_size = 1048576    
kind: Secret
metadata:
  name: md-configuration
  namespace: demo
type: Opaque
```

Maintenant, nous allons ajouter ce fichier à `kubedb/md-configuration.yaml`.

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ └── mariadb.yaml
1 directories, 2 files
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
```

Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD`, le fichier de reconfiguration est créé le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de configuration et créera un `Reconfigure` MariaDBOpsRequest pour mettre à jour le `MariaDB` configuration de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    17h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   17h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

### Faire pivoter l'authentification MariaDB

Pour ce faire, créez un `kubernetes.io/basic-auth` tapez k8s secret avec le nouveau nom d'utilisateur et le nouveau mot de passe.

Nous allons faire cela en utilisant gitops, créez le fichier `kubedb/md-auth.yaml` avec le contenu suivant,

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mdauth
  namespace: demo
type: kubernetes.io/basic-auth
stringData:
  username: root
  password: md-secret
```

Ajoutons cela à notre `kubedb/md-auth.yaml` déposer. La structure du fichier ressemblera à ceci,

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ ├── md-auth.yaml
│ └── MariaDB.yaml
1 directories, 3 files
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
```

Changer le `authSecret` champ à `mdauth`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel a été synchronisé avec succès avec ArgoCD. Le `MariaDB` CR a été mis à jour et le fichier d'authentification a été créé dans le cluster.

Maintenant, `gitops` L'opérateur détectera les changements d'authentification et créera un `RotateAuth` MariaDBOpsRequest pour mettre à jour le `MariaDB` authentification de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   12m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

### Configuration TLS

Nous pouvons ajouter, faire pivoter ou supprimer la configuration TLS en utilisant `gitops`.

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
$ kubectl create secret tls md-ca \
  --cert=ca.crt \
  --key=ca.key \
  -n demo
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
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

Ajoutons cela à notre `kubedb/md-issuer.yaml` déposer. La structure du fichier ressemblera à ceci,

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ ├── md-auth.yaml
│ ├── md-secret.yaml
│ ├── md-issuer.yaml
│ └── MariaDB.yaml
1 directories, 5 files
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
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
```

Ajouter `requireSSL` comme `true` et `tls` champs dans la spécification. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel a été synchronisé avec succès avec ArgoCD. Le `MariaDB` CR a été mis à jour et les deux `issuer` et le correspondant `secret` ont été créés dans le cluster.

Maintenant, `gitops` L'opérateur détectera les modifications tls et créera un `ReconfigureTLS` MariaDBOpsRequest pour mettre à jour le `MariaDB` base de données tls. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$  kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   8m20s
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   35m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

> Nous pouvons également alterner la mise à jour des certificats `.spec.tls.certificates` champ. Vous pouvez également supprimer le `.spec.tls` champ pour supprimer tls pour MariaDB.

### Version mise à jour

Répertorier les versions de MariaDB en utilisant `kubectl get MariaDBversion` et choisissez la version souhaitée qui est compatible pour la mise à niveau à partir de la version actuelle. Vérifiez les contraintes de version et la demande d'opérations [ici](fr/update-version/overview.md).

Choisissons `12.1.2` dans cet exemple.

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
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
```

Mettre à jour le `version` champ à `12.1.2`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de version et créera un `VersionUpdate` MariaDBOpsRequest pour mettre à jour le `MariaDB` version de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   12.1.2    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   24m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   51m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-versionupdate-ksli15       UpdateVersion       Successful   10m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   19h
```

Nous allons maintenant vérifier si le `MariaDB`, `PetSet` et c'est `Pod` ont été mis à jour avec une nouvelle image. Vérifions,

```bash
$ kubectl get MariaDB -n demo mariadb-gitops -o=jsonpath='{.spec.version}{"\n"}'
12.1.2
$ kubectl get petset -n demo mariadb-gitops -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
ghcr.io/appscode-images/mariadb:12.1.2-noble@sha256:843852d8651b3f321896a4a91f8118605d988d70703e520927c8d2c9313aded4
$ kubectl get pod -n demo mariadb-gitops-0 -o=jsonpath='{.spec.containers[0].image}{"\n"}'
ghcr.io/appscode-images/mariadb:12.1.2-noble@sha256:843852d8651b3f321896a4a91f8118605d988d70703e520927c8d2c9313aded4
```

### Activer la surveillance

Si vous n'avez pas encore de serveur Prometheus en cours d'exécution, déployez le didacticiel suivant à partir de [ici](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/operator/README.md#deploy-prometheus-server).

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
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
  monitor:
    agent: prometheus.io/operator
    prometheus:
      serviceMonitor:
        labels:
          release: prometheus
        interval: 10s
```

Ajouter `monitor` champ dans la spécification. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de surveillance et créera un `Restart` MariaDBOpsRequest pour ajouter le `MariaDB` surveillance de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   12.1.2    Ready    19h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   40m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-restart-e7rv89             Restart             Successful   8m26s
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   67m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-versionupdate-ksli15       UpdateVersion       Successful   26m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   19h
```

Vérifiez que la surveillance est activée en vérifiant les cibles prometheus.

## Prochaines étapes

* Apprendre la mise à l'échelle de MariaDB
  + [Mise à l'échelle horizontale](fr/scaling/horizontal-scaling/overview.md)
  + [Mise à l'échelle verticale](fr/scaling/vertical-scaling/overview.md)
* Apprendre la demande et les contraintes des opérations de mise à jour de version [ici](fr/update-version/overview.md)
* Surveillez votre base de données MariaDBQL avec KubeDB en utilisant [Prometheus intégré](fr/monitoring/prometheus-operator.md).
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: gitops/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Présentation de GitOps pour MariaDB

Ce guide vous donnera un aperçu de la façon dont KubeDB `gitops` L'opérateur fonctionne avec les bases de données MariaDB en utilisant le `gitops.kubedb.com/v1alpha1` API. Cela vous aidera à comprendre le flux de travail GitOps pour
gestion des bases de données MariaDB dans Kubernetes.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Flux de travail GitOps avec MariaDB

Le diagramme suivant montre comment le `KubeDB` Opérateur GitOps utilisé pour se synchroniser avec votre base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

![GitOps Flow](images/gitops_overview_gitops.jpg)

Fig : Processus GitOps de MariaDB

1. **Définir GitOps MariaDB**: Créer une ressource personnalisée (CR) de type `MariaDB` en utilisant le `gitops.kubedb.com/v1alpha1` API.
2. **Stocker dans Git**: poussez le CR vers un référentiel Git.
3. **Déploiement automatisé**: Utilisez un outil GitOps (comme `ArgoCD` ou `FluxCD`) pour surveiller le référentiel Git et synchroniser l'état du cluster Kubernetes avec l'état souhaité défini dans Git.
4. **Créer une base de données**: L'opérateur GitOps crée un CR KubeDB MariaDB correspondant dans le cluster Kubernetes pour déployer la base de données.
5. **Gérer les mises à jour**: Lorsque vous mettez à jour le CR MariaDBGitOps, l'opérateur génère une demande Ops pour appliquer la mise à jour en toute sécurité (par ex. `VerticalScaling`, `HorizontalScaling`, `VolumeExapnsion`, `Reconfigure`, `RotateAuth`, `ReconfigureTLS`, `VersionUpdate`, et `Restart`.

Ce flux rend la gestion des bases de données MariaDB efficace, fiable et entièrement intégrée aux pratiques GitOps.

Dans le prochain document, nous allons montrer un guide étape par étape sur l'exécution de MariaDB à l'aide de GitOps.

<!-- PAGE_START: initialization/git-sync.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Initialisation MariaDB à partir d'un référentiel Git

Ce guide montre comment utiliser KubeDB pour initialiser une base de données MariaDB avec des scripts d'initialisation (.sql, .sh et/ou .sql.gz) stockés dans un référentiel Git public ou privé.
Pour récupérer le contenu du référentiel, KubeDB utilise un conteneur side-car appelé [git-sync](https://github.com/kubernetes/git-sync).
Dans cet exemple, nous allons initialiser MariaDB en utilisant un `.sql` script du dépôt GitHub [kubedb/mysql-init-scripts](https://github.com/kubedb/mysql-init-scripts).

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## À partir du référentiel Git public

KubeDB implémente un `MariaDB` Définition de ressources personnalisées (CRD) pour définir la spécification d'une base de données MariaDB.
Pour initialiser la base de données à partir d'un référentiel Git public, vous devez spécifier les arguments requis pour le `git-sync` Conteneur side-car dans la spécification de ressources MariaDB.
Le manifeste YAML suivant montre un exemple `MariaDB` objet configuré avec `git-sync`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       - --repo=https://github.com/kubedb/mysql-init-scripts
       - --link=current
       - --root=/root
       # terminate after one successful sync
       - --one-time 
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

```bash
kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/initialization/git-sync-public.yaml
mariadb.kubedb.com/sample-mariadb created
```

Le `git-sync` Le conteneur a deux indicateurs obligatoires :

* `--repo` – spécifie le référentiel Git distant à synchroniser.
* `--root` – spécifie le répertoire de travail dans lequel le référentiel sera cloné.

Ici, la valeur du `--link` l'argument doit correspondre à la valeur de `spec.init.script.scriptPath`.
Le `--link` L'argument crée un lien symbolique qui pointe toujours vers les dernières données synchronisées.

> Pour en savoir plus sur `git-sync` configuration, visitez ceci [lien](https://github.com/kubernetes/git-sync).

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5   Ready    5m
```

Ensuite, nous nous connecterons à la base de données MariaDB et vérifierons les données insérées depuis le `*.sql` script stocké dans le référentiel Git.

```bash
kubectl exec -it -n demo sample-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, mariadb-init (init), git-sync (init)
```

```mysql
mysql@sample-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 6
Server version: 10.5.23-MariaDB-1:11.8.5+maria~ubu2004 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mysql]> select * from kubedb_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.000 sec)

MariaDB [mysql]> select * from demo_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.000 sec)
```

## À partir du référentiel Git privé

### 1. Utilisation de la clé SSH

Git-sync prend en charge l'utilisation du protocole SSH pour extraire le contenu git.

Tout d’abord, obtenez les clés d’hôte de votre serveur git :

```bash
$ ssh-keyscan $YOUR_GIT_HOST > /tmp/known_hosts
```

> `$YOUR_GIT_HOST` fait référence au nom d'hôte de votre serveur Git.  
> Par exemple, si vous utilisez GitHub, définissez la variable comme suit :
>
> ```bash
> export YOUR_GIT_HOST=github.com
> ```

Utilisez le `kubectl create secret` commande pour créer un secret à partir de votre clé SSH locale et du fichier d'hôtes connus.
Ce secret sera utilisé par git-sync pour s'authentifier auprès du référentiel Git.

```bash
$ kubectl create secret generic -n demo git-creds \
    --from-file=ssh=$HOME/.ssh/id_rsa \
    --from-file=known_hosts=/tmp/known_hosts
```

Le manifeste YAML suivant fournit un exemple de `MariaDB` ressource configurée pour utiliser `git-sync` avec un dépôt Git privé :

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       # update with your private repository    
       - --repo=<your-ssh-repo-url>
       - --link=current
       - --root=/root
       # terminate after one successful sync
       - --one-time 
       authSecret:
         name: git-creds
       # run as git sync user 
       securityContext:
         runAsUser: 65533
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Ici,

* `.spec.init.git.securityContext.runAsUser: 65533` assurez-vous que le conteneur s'exécute en tant que non-root dédié `git-sync` utilisateur.
* `.spec.init.git.authSecret` précise le secret contenant le `SSH` clé.

Une fois que la base de données atteint le `Ready` état, vous pouvez vérifier les données en utilisant la méthode décrite ci-dessus.

### 2. Utilisation du nom d'utilisateur et du jeton d'accès personnel (PAT)

Tout d'abord, créez un `Personal Access Token (PAT)` sur votre serveur hôte Git avec les autorisations requises pour accéder au référentiel.
Créez ensuite un secret Kubernetes à l'aide du `Personal Access Token (PAT)`:

```bash
$ kubectl create secret generic -n demo git-pat \
    --from-literal=github-pat=<ghp_yourpersonalaccesstoken>
```

Maintenant, créez un `MariaDB` ressource qui fait référence au secret créé ci-dessus.
Le manifeste YAML suivant montre un exemple :

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       # update with your private repository    
       - --repo=<your-https-repo-url>
       - --link=current
       - --root=/root
       - --credential={"url":"https://github.com","username":"<username>","password-file":"/etc/git-secret/github-pat"}
       # terminate after one successful sync
       - --one-time 
       authSecret:
         name: git-pat
       # run as git sync user 
       securityContext:
         runAsUser: 65533
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Une fois que la base de données atteint le `Ready` état, vous pouvez vérifier les données en utilisant la méthode décrite ci-dessus.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete secret -n demo git-pat git-creds
$ kubectl delete ns demo
```

<!-- PAGE_START: initialization/using-script.md -->
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

<!-- PAGE_START: migration/databasemigration.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Migration de la base de données MariaDB

Ce guide vous montrera comment utiliser `KubeDB` Migration pour migrer un existant `MariaDB` base de données - telle qu'une base de données exécutée sur AWS RDS ou toute instance externe - entièrement dans une base de données gérée par KubeDB `MariaDB` avec un temps d'arrêt minimal.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` opérateur avec l'opérateur kubedb-courier activé dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/operatormanual/migration/).
* La source `MariaDB` L'instance doit être accessible par le réseau depuis votre cluster Kubernetes.
* La source `MariaDB` l'instance doit avoir la journalisation binaire activée avec `binlog_format=ROW` et `binlog_row_image=FULL`. L'utilisateur de base de données fourni pour la migration doit disposer de privilèges de réplication.
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [Liaison d'application](fr/concepts/appbinding.md)
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBMigration](fr/concepts/migrator.md)
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

Ici, nous étudions la migration vers le `shop` base de données (`schema.database: [shop]`), activez à la fois les phases d'instantané en masse et de streaming CDC, et limitez les connexions à 100 de chaque côté. Pour une description complète de chaque champ, consultez le [Référence MariaDBMigration CRD](fr/concepts/migrator.md).

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

<!-- PAGE_START: monitoring/builtin-prometheus.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Surveillance de MariaDB avec Prometheus intégré

Ce tutoriel va vous montrer comment surveiller la base de données MariaDB à l'aide de la fonction intégrée [Prométhée](https://github.com/prometheus/prometheus) grattoir.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installez l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Si vous ne savez pas comment configurer Prometheus pour récupérer les métriques de diverses ressources Kubernetes, veuillez lire le didacticiel de [ici](https://github.com/appscode/third-party-tools/tree/master/monitoring/prometheus/builtin).
* Pour savoir comment la surveillance Prometheus fonctionne avec KubeDB en général, veuillez visiter [ici](fr/monitoring/overview.md).
* Pour garder les ressources Prometheus isolées, nous allons utiliser un espace de noms distinct appelé `monitoring` pour déployer les ressources de surveillance respectives. Nous allons déployer la base de données dans `demo` espace de noms.

  ```bash
  $ kubectl create ns monitoring
  namespace/monitoring created

  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/monitoring/builtin-prometheus/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/monitoring/builtin-prometheus/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Déployer MariaDB avec la surveillance activée

Dans un premier temps, déployons une base de données MariaDB avec la surveillance activée. Ci-dessous se trouve l'objet MariaDB que nous allons créer.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: builtin-prom-md
  namespace: demo
spec:
  version: "12.1.2"
  deletionPolicy: WipeOut
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  monitor:
    agent: prometheus.io/builtin
```

Ici,

* `spec.monitor.agent: prometheus.io/builtin` précise que nous allons surveiller ce serveur à l'aide du scraper Prometheus intégré.

Créons le crd MariaDB que nous avons montré ci-dessus.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/monitoring/builtin-prometheus/examples/builtin-prom-md.yaml
mariadb.kubedb.com/builtin-prom-md created
```

Maintenant, attendez que la base de données entre dans `Running` État.

```bash
$ kubectl get mariadb -n demo builtin-prom-md
NAME              VERSION   STATUS   AGE
builtin-prom-md   11.8.5    Ready    76s
```

KubeDB créera un service de statistiques distinct avec le nom `{MariaDB crd name}-stats` à des fins de surveillance.

```bash
$ kubectl get svc -n demo --selector="app.kubernetes.io/instance=builtin-prom-md"
NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
builtin-prom-md         ClusterIP   10.106.32.194   <none>        3306/TCP    2m3s
builtin-prom-md-pods    ClusterIP   None            <none>        3306/TCP    2m3s
builtin-prom-md-stats   ClusterIP   10.109.106.92   <none>        56790/TCP   2m2s
```

Ici, `builtin-prom-md-stats` Le service a été créé à des fins de surveillance. Décrivons le service.

```bash
$ kubectl describe svc -n demo builtin-prom-md-stats
Name:              builtin-prom-md-stats
Namespace:         demo
Labels:            app.kubernetes.io/instance=builtin-prom-md
                   app.kubernetes.io/managed-by=kubedb.com
                   app.kubernetes.io/name=mariadbs.kubedb.com
                   kubedb.com/role=stats
Annotations:       monitoring.appscode.com/agent: prometheus.io/builtin
                   prometheus.io/path: /metrics
                   prometheus.io/port: 56790
                   prometheus.io/scrape: true
Selector:          app.kubernetes.io/instance=builtin-prom-md,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com
Type:              ClusterIP
IP:                10.109.106.92
Port:              metrics  56790/TCP
TargetPort:        metrics/TCP
Endpoints:         10.244.0.34:56790
Session Affinity:  None
Events:            <none>
```

Vous pouvez voir que le service contient les annotations suivantes.

```bash
prometheus.io/path: /metrics
prometheus.io/port: 56790
prometheus.io/scrape: true
```

Le serveur Prometheus découvrira le point de terminaison du service à l'aide de ces spécifications et récupérera les métriques de l'exportateur.

## Configurer le serveur Prometheus

Nous devons maintenant configurer une tâche de scraping Prometheus pour récupérer les métriques à l'aide de ce service. Nous allons configurer un travail de scraping similaire à celui-ci [points de terminaison du service Kubernetes](https://github.com/appscode/third-party-tools/tree/master/monitoring/prometheus/builtin#kubernetes-service-endpoints) travail qui récupère les métriques des points de terminaison d’un service.

Configurons une tâche de scraping Prometheus pour collecter les métriques de ce service.

```yaml
- job_name: 'kubedb-databases'
  honor_labels: true
  scheme: http
  kubernetes_sd_configs:
  - role: endpoints
  # by default Prometheus server select all Kubernetes services as possible target.
  # relabel_config is used to filter only desired endpoints
  relabel_configs:
  # keep only those services that has "prometheus.io/scrape","prometheus.io/path" and "prometheus.io/port" annotations
  - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape, __meta_kubernetes_service_annotation_prometheus_io_port]
    separator: ;
    regex: true;(.*)
    action: keep
  # currently KubeDB supported databases uses only "http" scheme to export metrics. so, drop any service that uses "https" scheme.
  - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
    action: drop
    regex: https
  # only keep the stats services created by KubeDB for monitoring purpose which has "-stats" suffix
  - source_labels: [__meta_kubernetes_service_name]
    separator: ;
    regex: (.*-stats)
    action: keep
  # service created by KubeDB will have "app.kubernetes.io/name" and "app.kubernetes.io/instance" annotations. keep only those services that have these annotations.
  - source_labels: [__meta_kubernetes_service_label_app_kubernetes_io_name]
    separator: ;
    regex: (.*)
    action: keep
  # read the metric path from "prometheus.io/path: <path>" annotation
  - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
    action: replace
    target_label: __metrics_path__
    regex: (.+)
  # read the port from "prometheus.io/port: <port>" annotation and update scraping address accordingly
  - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
    action: replace
    target_label: __address__
    regex: ([^:]+)(?::\d+)?;(\d+)
    replacement: $1:$2
  # add service namespace as label to the scraped metrics
  - source_labels: [__meta_kubernetes_namespace]
    separator: ;
    regex: (.*)
    target_label: namespace
    replacement: $1
    action: replace
  # add service name as a label to the scraped metrics
  - source_labels: [__meta_kubernetes_service_name]
    separator: ;
    regex: (.*)
    target_label: service
    replacement: $1
    action: replace
  # add stats service's labels to the scraped metrics
  - action: labelmap
    regex: __meta_kubernetes_service_label_(.+)
```

### Configurer le serveur Prometheus existant

Si vous disposez déjà d'un serveur Prometheus en cours d'exécution, vous devez ajouter la tâche de scraping ci-dessus dans le fichier `ConfigMap` utilisé pour configurer le serveur Prometheus. Ensuite, vous devez le redémarrer pour que la configuration mise à jour prenne effet.

> Si vous n'utilisez pas de volume persistant pour le stockage Prometheus, vous perdrez vos données précédemment récupérées au redémarrage.

### Déployer un nouveau serveur Prometheus

Si aucun serveur Prometheus n’est en cours d’exécution, vous devez en déployer un. Dans cette section, nous allons déployer un serveur Prometheus dans `monitoring` espace de noms pour collecter des métriques à l’aide de ce service de statistiques.

**Créez une ConfigMap :**

Dans un premier temps, créez un ConfigMap avec la configuration de scraping. Ci-dessous, le YAML de ConfigMap que nous allons créer dans ce tutoriel.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  labels:
    app: prometheus-demo
  namespace: monitoring
data:
  prometheus.yml: |-
    global:
      scrape_interval: 5s
      evaluation_interval: 5s
    scrape_configs:
    - job_name: 'kubedb-databases'
      honor_labels: true
      scheme: http
      kubernetes_sd_configs:
      - role: endpoints
      # by default Prometheus server select all Kubernetes services as possible target.
      # relabel_config is used to filter only desired endpoints
      relabel_configs:
      # keep only those services that has "prometheus.io/scrape","prometheus.io/path" and "prometheus.io/port" anootations
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape, __meta_kubernetes_service_annotation_prometheus_io_port]
        separator: ;
        regex: true;(.*)
        action: keep
      # currently KubeDB supported databases uses only "http" scheme to export metrics. so, drop any service that uses "https" scheme.
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
        action: drop
        regex: https
      # only keep the stats services created by KubeDB for monitoring purpose which has "-stats" suffix
      - source_labels: [__meta_kubernetes_service_name]
        separator: ;
        regex: (.*-stats)
        action: keep
      # service created by KubeDB will have "app.kubernetes.io/name" and "app.kubernetes.io/instance" annotations. keep only those services that have these annotations.
      - source_labels: [__meta_kubernetes_service_label_app_kubernetes_io_name]
        separator: ;
        regex: (.*)
        action: keep
      # read the metric path from "prometheus.io/path: <path>" annotation
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      # read the port from "prometheus.io/port: <port>" annotation and update scraping address accordingly
      - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
      # add service namespace as label to the scraped metrics
      - source_labels: [__meta_kubernetes_namespace]
        separator: ;
        regex: (.*)
        target_label: namespace
        replacement: $1
        action: replace
      # add service name as a label to the scraped metrics
      - source_labels: [__meta_kubernetes_service_name]
        separator: ;
        regex: (.*)
        target_label: service
        replacement: $1
        action: replace
      # add stats service's labels to the scraped metrics
      - action: labelmap
        regex: __meta_kubernetes_service_label_(.+)
```

Créons ci-dessus `ConfigMap`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/monitoring/builtin-prometheus/examples/prom-config.yaml
configmap/prometheus-config created
```

**Créer un RBAC :**

Si vous utilisez un cluster compatible RBAC, vous devez accorder les autorisations RBAC nécessaires pour Prometheus. Créons les éléments RBAC nécessaires pour Prometheus,

```bash
$ kubectl apply -f https://github.com/appscode/third-party-tools/raw/master/monitoring/prometheus/builtin/artifacts/rbac.yaml
clusterrole.rbac.authorization.k8s.io/prometheus created
serviceaccount/prometheus created
clusterrolebinding.rbac.authorization.k8s.io/prometheus created
```

> YAML pour les ressources RBAC créées ci-dessus peut être trouvé [ici](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/builtin/artifacts/rbac.yaml).

**Déployez Prometheus :**

Nous sommes maintenant prêts à déployer le serveur Prometheus. Nous allons utiliser ce qui suit [déploiement](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/builtin/artifacts/deployment.yaml) pour déployer le serveur Prometheus.

Déployons le serveur Prometheus.

```bash
$ kubectl apply -f https://github.com/appscode/third-party-tools/raw/master/monitoring/prometheus/builtin/artifacts/deployment.yaml
deployment.apps/prometheus created
```

### Vérifier les métriques de surveillance

Le serveur Prometheus écoute le port `9090`. Nous allons utiliser [redirection de port](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) pour accéder au tableau de bord Prometheus.

Dans un premier temps, vérifions si le pod Prometheus est présent `Running` État.

```bash
$ kubectl get pod -n monitoring -l=app=prometheus
NAME                          READY   STATUS    RESTARTS   AGE
prometheus-5dff66b455-cz9td   1/1     Running   0          42s
```

Maintenant, exécutez la commande suivante sur un terminal séparé pour transférer le port 9090 de `prometheus-8568c86d86-95zhn` cosse,

```bash
$ kubectl port-forward -n monitoring prometheus-8568c86d86-95zhn 9090
Forwarding from 127.0.0.1:9090 -> 9090
Forwarding from [::1]:9090 -> 9090
```

Maintenant, nous pouvons accéder au tableau de bord à l'adresse `localhost:9090`. Ouvrir <http://localhost:9090> dans votre navigateur. Vous devriez voir le point final de `builtin-prom-md-stats` service comme l’une des cibles.

![Prometheus Target](images/monitoring_builtin-prometheus_built-prom.png)

Vérifiez les étiquettes marquées d'un rectangle rouge. Ces étiquettes confirment que les métriques proviennent de `MariaDB` base de données `builtin-prom-md` via le service de statistiques `builtin-prom-md-stats`.

Vous pouvez désormais afficher les métriques collectées et créer un graphique à partir de la page d'accueil de ce tableau de bord Prometheus. Vous pouvez également utiliser ce serveur Prometheus comme source de données pour [Grafana](https://grafana.com/) et créez un magnifique tableau de bord avec les métriques collectées.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce didacticiel, exécutez les commandes suivantes

```bash
kubectl delete mariadb -n demo builtin-prom-md

kubectl delete -n monitoring deployment.apps/prometheus

kubectl delete -n monitoring clusterrole.rbac.authorization.k8s.io/prometheus
kubectl delete -n monitoring serviceaccount/prometheus
kubectl delete -n monitoring clusterrolebinding.rbac.authorization.k8s.io/prometheus

kubectl delete ns demo
kubectl delete ns monitoring
```

<!-- PAGE_START: monitoring/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Surveillance de MariaDB avec KubeDB

KubeDB prend en charge nativement la surveillance via [Prométhée](https://prometheus.io/). Vous pouvez utiliser le module intégré [Prométhée](https://github.com/prometheus/prometheus) grattoir ou [Opérateur Prométhée](https://github.com/prometheus-operator/prometheus-operator) pour surveiller les bases de données gérées par KubeDB. Ce didacticiel vous montrera comment fonctionne la surveillance de base de données avec KubeDB et comment configurer Database crd pour activer la surveillance.

## Aperçu

KubeDB utilise Prometheus [exportateur](https://prometheus.io/docs/instrumenting/exporters/#databases) images pour exporter les métriques Prometheus pour les bases de données respectives. Le diagramme suivant montre le flux logique de la surveillance de la base de données avec KubeDB.

![Database Monitoring Flow](images/monitoring_overview_database-monitoring-overview.svg)

Lorsqu'un utilisateur crée un crd de base de données avec `spec.monitor` configurée, l'opérateur KubeDB provisionne la base de données respective et injecte une image d'exportateur comme side-car dans le pod de base de données. Il crée également un service de statistiques dédié avec le nom `{database-crd-name}-stats` pour le suivi. Le serveur Prometheus peut récupérer des métriques à l'aide de ce service de statistiques.

## Configurer la surveillance

Afin d'activer la surveillance d'une base de données, vous devez configurer `spec.monitor` section. KubeDB fournit les options suivantes à configurer `spec.monitor` section:

| Champ | Type | Utilisations |
| --- | --- | --- |
| `spec.monitor.agent` | `Required` | Type de l'agent de surveillance qui sera utilisé pour surveiller cette base de données. Cela peut être `prometheus.io/builtin` ou `prometheus.io/operator`. |
| `spec.monitor.prometheus.exporter.port` | `Optional` | Numéro de port où le side-car de l'exportateur fournira des mesures. |
| `spec.monitor.prometheus.exporter.args` | `Optional` | Arguments à transmettre au side-car de l’exportateur. |
| `spec.monitor.prometheus.exporter.env` | `Optional` | Liste des variables d'environnement à définir dans le conteneur side-car de l'exportateur. |
| `spec.monitor.prometheus.exporter.resources` | `Optional` | Ressources requises par le conteneur side-car de l'exportateur. |
| `spec.monitor.prometheus.exporter.securityContext` | `Optional` | Options de sécurité avec lesquelles l’exportateur doit fonctionner. |
| `spec.monitor.prometheus.serviceMonitor.labels` | `Optional` | Étiquettes pour `ServiceMonitor` crd. |
| `spec.monitor.prometheus.serviceMonitor.interval` | `Optional` | Intervalle auquel les métriques doivent être récupérées. |

## Exemple de configuration

Un exemple de YAML pour le crd MariaDB avec `spec.monitor` section configurée pour permettre la surveillance avec [Opérateur Prométhée](https://github.com/prometheus-operator/prometheus-operator) est montré ci-dessous.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: coreos-prom-md
  namespace: demo
spec:
  version: "12.1.2"
  deletionPolicy: WipeOut
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  monitor:
    agent: prometheus.io/operator
    prometheus:
      serviceMonitor:
        labels:
          release: prometheus
        interval: 10s
```

Supposons que MariaDB ci-dessus soit configurée pour utiliser l'authentification de base. Ainsi, l’image de l’exportateur doit également fournir un mot de passe pour collecter des métriques. Nous l'avons fourni à travers `spec.monitor.prometheus.exporter.args` champ.

Ici, nous avons précisé que nous allons surveiller ce serveur à l'aide de l'opérateur Prometheus via `spec.monitor.agent: prometheus.io/operator`. KubeDB créera un `ServiceMonitor` crédit dans `monitoring` espace de noms et ceci `ServiceMonitor` aura `release: prometheus` étiquette.

## Prochaines étapes

* Apprenez à surveiller `MariaDB` base de données avec KubeDB en utilisant [intégré-Prométhée](fr/monitoring/builtin-prometheus.md) et en utilisant [Opérateur Prométhée](fr/monitoring/prometheus-operator.md).
* Apprenez à surveiller une base de données `Elasticsearch` avec KubeDB en utilisant [Prometheus intégré](https://kubedb.com/docs/v2026.7.10/guides/elasticsearch/monitoring/using-builtin-prometheus) et en utilisant [Opérateur Prométhée](https://kubedb.com/docs/v2026.7.10/guides/elasticsearch/monitoring/using-prometheus-operator).
* Apprenez à surveiller `PostgreSQL` base de données avec KubeDB en utilisant [intégré-Prométhée](https://kubedb.com/docs/v2026.7.10/guides/postgres/monitoring/using-builtin-prometheus) et en utilisant [Opérateur Prométhée](https://kubedb.com/docs/v2026.7.10/guides/postgres/monitoring/using-prometheus-operator).
* Apprenez à surveiller une base de données `MySQL` avec KubeDB en utilisant [intégré-Prométhée](https://kubedb.com/docs/v2026.7.10/guides/mysql/monitoring/builtin-prometheus/) et en utilisant [Opérateur Prométhée](https://kubedb.com/docs/v2026.7.10/guides/mysql/monitoring/prometheus-operator/).
* Apprenez à surveiller `MongoDB` base de données avec KubeDB en utilisant [intégré-Prométhée](https://kubedb.com/docs/v2026.7.10/guides/mongodb/monitoring/using-builtin-prometheus) et en utilisant [Opérateur Prométhée](https://kubedb.com/docs/v2026.7.10/guides/mongodb/monitoring/using-prometheus-operator).
* Apprenez à surveiller `Redis` serveur avec KubeDB utilisant [intégré-Prométhée](https://kubedb.com/docs/v2026.7.10/guides/redis/monitoring/using-builtin-prometheus) et en utilisant [Opérateur Prométhée](https://kubedb.com/docs/v2026.7.10/guides/redis/monitoring/using-prometheus-operator).
* Apprenez à surveiller `Memcached` serveur avec KubeDB utilisant [intégré-Prométhée](https://kubedb.com/docs/v2026.7.10/guides/memcached/monitoring/using-builtin-prometheus) et en utilisant [Opérateur Prométhée](https://kubedb.com/docs/v2026.7.10/guides/memcached/monitoring/using-prometheus-operator).

<!-- PAGE_START: monitoring/prometheus-operator.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Surveillance de MariaDB à l'aide de l'opérateur Prometheus

[Opérateur Prométhée](https://github.com/prometheus-operator/prometheus-operator) fournit un moyen simple et natif de Kubernetes de déployer et de configurer le serveur Prometheus. Ce didacticiel vous montrera comment utiliser l'opérateur Prometheus pour surveiller la base de données MariaDB déployée avec KubeDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Pour savoir comment la surveillance Prometheus fonctionne avec KubeDB en général, veuillez visiter [ici](fr/monitoring/overview.md).
* Pour conserver les ressources de base de données isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel. Exécutez la commande suivante pour préparer votre cluster :

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```
* Nous avons besoin d'un [Opérateur Prométhée](https://github.com/prometheus-operator/prometheus-operator) instance en cours d'exécution. Si vous n'avez pas encore d'instance en cours d'exécution, déployez-en une en suivant la documentation de [ici](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/operator/README.md).
* Si vous n'avez pas encore de serveur Prometheus en cours d'exécution, déployez le didacticiel suivant à partir de [ici](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/operator/README.md#deploy-prometheus-server).

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [/docs/guides/mariadb/monitoring/prometheus-operator/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/monitoring/prometheus-operator/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Découvrez les étiquettes requises pour ServiceMonitor

Nous devons connaître les étiquettes utilisées pour sélectionner `ServiceMonitor` par un `Prometheus` crd. Nous allons fournir ces étiquettes dans `spec.monitor.prometheus.labels` champ de MariaDB crd pour que KubeDB crée `ServiceMonitor` objecter en conséquence.

Dans un premier temps, découvrons le serveur Prometheus disponible dans notre cluster.

```bash
$ kubectl get prometheus --all-namespaces
NAMESPACE   NAME         VERSION   REPLICAS   AGE
default     prometheus             1          2m19s
```

> Si aucun serveur Prometheus n'est en cours d'exécution dans votre cluster, déployez-en un en suivant le guide spécifié dans **Avant de commencer** section.

Voyons maintenant le YAML du serveur Prometheus disponible `prometheus` dans `default` espace de noms.

```bash
$ kubectl get prometheus -n default prometheus -o yaml
```

```yaml
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"monitoring.coreos.com/v1","kind":"Prometheus","metadata":{"annotations":{},"labels":{"prometheus":"prometheus"},"name":"prometheus","namespace":"default"},"spec":{"replicas":1,"resources":{"requests":{"memory":"400Mi"}},"serviceAccountName":"prometheus","serviceMonitorNamespaceSelector":{"matchLabels":{"prometheus":"prometheus"}},"serviceMonitorSelector":{"matchLabels":{"release":"prometheus"}}}}      
  creationTimestamp: "2020-08-25T04:02:07Z"
  generation: 1
  labels:
    prometheus: prometheus
    manager: kubectl
    operation: Update
  name: prometheus
  namespace: default
  resourceVersion: "2087"
  selfLink: /apis/monitoring.coreos.com/v1/namespaces/default/prometheuses/prometheus
  uid: 972a50cb-b751-418b-b2bc-e0ecc9232730
spec:
  replicas: 1
  resources:
    requests:
      memory: 400Mi
  serviceAccountName: prometheus
  serviceMonitorNamespaceSelector:
    matchLabels:
      prometheus: prometheus
  serviceMonitorSelector:
    matchLabels:
      release: prometheus
```

* `spec.serviceMonitorSelector` Le champ spécifie quels ServiceMonitors doivent être inclus. L'étiquette ci-dessus `release: prometheus` est utilisé pour sélectionner `ServiceMonitors` par son sélecteur. Nous allons donc utiliser cette étiquette dans `spec.monitor.prometheus.labels` champ de MariaDB crd.
* `spec.serviceMonitorNamespaceSelector` champ précise que le `ServiceMonitors` peut être sélectionné en dehors de l'espace de noms Prometheus par Prometheus à l'aide du sélecteur d'espace de noms. L'étiquette ci-dessus `prometheus: prometheus` est utilisé pour sélectionner l'espace de noms où le `ServiceMonitor` est créé.

### Ajouter une étiquette à l'espace de noms de la base de données

KubeDB crée un `ServiceMonitor` dans l'espace de noms de la base de données `demo`. Nous devons ajouter une étiquette à `demo` espace de noms. Prometheus sélectionnera cet espace de noms en utilisant son `spec.serviceMonitorNamespaceSelector` champ.

Ajoutons une étiquette `prometheus: prometheus` à `demo` espace de noms,

```bash
$ kubectl patch namespace demo -p '{"metadata":{"labels": {"prometheus":"prometheus"}}}'
namespace/demo patched
```

## Déployer MariaDB avec la surveillance activée

Dans un premier temps, déployons une base de données MariaDB avec la surveillance activée. Ci-dessous se trouve l'objet MariaDB que nous allons créer.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: coreos-prom-md
  namespace: demo
spec:
  version: "12.1.2"
  deletionPolicy: WipeOut
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  monitor:
    agent: prometheus.io/operator
    prometheus:
      serviceMonitor:
        labels:
          release: prometheus
        interval: 10s
```

Ici,

* `monitor.agent: prometheus.io/operator` indique que nous allons surveiller ce serveur à l'aide de l'opérateur Prometheus.
* `monitor.prometheus.labels` spécifie que KubeDB doit créer `ServiceMonitor` avec ces étiquettes.
* `monitor.prometheus.interval` indique que le serveur Prometheus doit extraire les métriques de cette base de données avec un intervalle de 10 secondes.

Créons l'objet MariaDB que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/monitoring/prometheus-operator/examples/prom-operator-md.yaml
mariadb.kubedb.com/coreos-prom-md created
```

Maintenant, attendez que la base de données entre dans `Ready` État.

```bash
$ kubectl get mariadb -n demo coreos-prom-md
NAME             VERSION   STATUS   AGE
coreos-prom-md   10.5.23    Ready    59s
```

KubeDB créera un service de statistiques distinct avec le nom `{MariaDB crd name}-stats` à des fins de surveillance.

```bash
$ kubectl get svc -n demo --selector="app.kubernetes.io/instance=coreos-prom-md"
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
coreos-prom-md         ClusterIP   10.99.96.226    <none>        3306/TCP    107s
coreos-prom-md-pods    ClusterIP   None            <none>        3306/TCP    107s
coreos-prom-md-stats   ClusterIP   10.101.190.67   <none>        56790/TCP   107s
```

Ici, `coreos-prom-md-stats` Le service a été créé à des fins de surveillance.

Décrivons ce service de statistiques.

```bash
$ kubectl describe svc -n demo coreos-prom-md-stats
```

```text
Name:              coreos-prom-md-stats
Namespace:         demo
Labels:            app.kubernetes.io/instance=coreos-prom-md
                   app.kubernetes.io/managed-by=kubedb.com
                   app.kubernetes.io/name=mariadbs.kubedb.com
                   kubedb.com/role=stats
Annotations:       monitoring.appscode.com/agent: prometheus.io/operator
Selector:          app.kubernetes.io/instance=coreos-prom-md,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com
Type:              ClusterIP
IP:                10.101.190.67
Port:              metrics  56790/TCP
TargetPort:        metrics/TCP
Endpoints:         10.244.0.31:56790
Session Affinity:  None
Events:            <none>
```

Remarquez le `Labels` et `Port` champs. `ServiceMonitor` utilisera ces informations pour cibler ses points de terminaison.

KubeDB créera également un `ServiceMonitor` crédit dans `demo` espace de noms qui sélectionne les points de terminaison de `coreos-prom-md-stats` service. Vérifiez que le `ServiceMonitor` crd a été créé.

```bash
$ kubectl get servicemonitor -n demo
NAME                   AGE
coreos-prom-md-stats   4m8s
```

Vérifions que le `ServiceMonitor` porte l'étiquette que nous avions spécifiée dans `spec.monitor` section du crd MariaDB.

```bash
$ kubectl get servicemonitor -n demo coreos-prom-md-stats -o yaml
```

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  creationTimestamp: "2021-03-19T10:09:03Z"
  generation: 1
  labels:
    app.kubernetes.io/component: database
    app.kubernetes.io/instance: coreos-prom-md
    app.kubernetes.io/managed-by: kubedb.com
    app.kubernetes.io/name: mariadbs.kubedb.com
    release: prometheus
  managedFields:
  - apiVersion: monitoring.coreos.com/v1
    fieldsType: FieldsV1
    fieldsV1:
      f:metadata:
        f:labels:
          .: {}
          f:app.kubernetes.io/component: {}
          f:app.kubernetes.io/instance: {}
          f:app.kubernetes.io/managed-by: {}
          f:app.kubernetes.io/name: {}
          f:release: {}
        f:ownerReferences: {}
      f:spec:
        .: {}
        f:endpoints: {}
        f:namespaceSelector:
          .: {}
          f:matchNames: {}
        f:selector:
          .: {}
          f:matchLabels:
            .: {}
            f:app.kubernetes.io/instance: {}
            f:app.kubernetes.io/managed-by: {}
            f:app.kubernetes.io/name: {}
            f:kubedb.com/role: {}
    manager: mariadb-operator
    operation: Update
    time: "2021-03-19T10:09:03Z"
  name: coreos-prom-md-stats
  namespace: demo
  ownerReferences:
  - apiVersion: v1
    blockOwnerDeletion: true
    controller: true
    kind: Service
    name: coreos-prom-md-stats
    uid: 08260a99-0984-4d90-bf68-34080ad0ee5b
  resourceVersion: "241637"
  selfLink: /apis/monitoring.coreos.com/v1/namespaces/demo/servicemonitors/coreos-prom-md-stats
  uid: 4f022d98-d2d8-490f-9548-f6367d03ae1f
spec:
  endpoints:
  - bearerTokenSecret:
      key: ""
    honorLabels: true
    interval: 10s
    path: /metrics
    port: metrics
  namespaceSelector:
    matchNames:
    - demo
  selector:
    matchLabels:
      app.kubernetes.io/instance: coreos-prom-md
      app.kubernetes.io/managed-by: kubedb.com
      app.kubernetes.io/name: mariadbs.kubedb.com
      kubedb.com/role: stats
```

Notez que le `ServiceMonitor` a une étiquette `release: prometheus` que nous avions spécifié dans MariaDB crd.

Notez également que le `ServiceMonitor` a un sélecteur qui correspond aux étiquettes que nous avons vues dans le `coreos-prom-md-stats` service. Il cible également les `prom-http` port que nous avons vu dans le service de statistiques.

## Vérifier les métriques de surveillance

Dans un premier temps, découvrons le pod Prometheus respectif pour `prometheus` Serveur Prometheus.

```bash
$ kubectl get pod -n default -l=app=prometheus
NAME                      READY   STATUS    RESTARTS   AGE
prometheus-prometheus-0   3/3     Running   1          16m
```

Le serveur Prometheus écoute le port `9090` de `prometheus-prometheus-0` cosse. Nous allons utiliser [redirection de port](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) pour accéder au tableau de bord Prometheus.

Exécutez la commande suivante sur un terminal séparé pour transférer le port 9090 de `prometheus-prometheus-0` cosse,

```bash
$ kubectl port-forward -n default prometheus-prometheus-0 9090
Forwarding from 127.0.0.1:9090 -> 9090
Forwarding from [::1]:9090 -> 9090
```

Maintenant, nous pouvons accéder au tableau de bord à l'adresse `localhost:9090`. Ouvrir <http://localhost:9090> dans votre navigateur. Tu devrais voir `prom-http` point final de `coreos-prom-md-stats` service comme l’une des cibles.

![Prometheus Target](images/monitoring_prometheus-operator_prom-end.png)

Vérifiez le `endpoint` et `service` étiquettes. Il vérifie que la cible est notre base de données attendue. Vous pouvez désormais afficher les métriques collectées et créer un graphique à partir de la page d'accueil de ce tableau de bord Prometheus. Vous pouvez également utiliser ce serveur Prometheus comme source de données pour [Grafana](https://grafana.com/) et créez un magnifique tableau de bord avec les métriques collectées.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce didacticiel, exécutez les commandes suivantes

```bash
# cleanup database
kubectl delete mariadb -n demo coreos-prom-md

# cleanup Prometheus resources
kubectl delete -f https://raw.githubusercontent.com/appscode/third-party-tools/master/monitoring/prometheus/operator/artifacts/prometheus.yaml

kubectl delete -f https://raw.githubusercontent.com/appscode/third-party-tools/master/monitoring/prometheus/operator/artifacts/prometheus-rbac.yaml

# cleanup Prometheus operator resources
kubectl delete -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/release-0.41/bundle.yaml

# delete namespace
kubectl delete ns demo
```

<!-- PAGE_START: pitr/nfs.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB MariaDB - Archivage continu et récupération ponctuelle

Ici, nous allons vous montrer comment utiliser KubeDB pour provisionner une MariaDB afin d'archiver en continu et de restaurer à un moment donné.

## Avant de commencer

Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Pour cette démonstration, j'utilise le cluster linode.

Maintenant, installez `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).

Pour installer `KubeStash` opérateur dans votre cluster en suivant les étapes [ici](https://github.com/kubestash/installer/tree/master/charts/kubestash).

Pour installer `External-snapshotter` dans votre cluster en suivant les étapes [ici](https://github.com/kubernetes-csi/external-snapshotter/tree/release-5.0).

Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

> Remarque : Les fichiers yaml utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/pitr/nfs/yamls](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/remote-replica/yamls) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## archivage continu

L'archivage continu implique de faire des copies régulières (ou « archives ») des fichiers journaux de transactions MariaDB. Pour garantir un archivage continu sur un NFS, nous devons préparer `NFS Server` `BackupStorage`,`RetentionPolicy`,`MariaDBArchiver` pour les bases de données MariaDB gérées par KubeDB.

## Assurer volumeSnapshotClass

```bash
$ kubectl get volumesnapshotclasses
NAME                    DRIVER               DELETIONPOLICY   AGE
longhorn-snapshot-vsc   driver.longhorn.io   Delete           7d22h
```

Si ce n'est pas le cas, essayez d'utiliser `longhorn` ou tout autre [volumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/).

### Installer Longhorn

Longhorn est un système de stockage en bloc distribué pour Kubernetes qui gère le stockage persistant.

Ajoutez un référentiel de cartes Longhorn.

`helm repo add longhorn https://charts.longhorn.io`

Mettez à jour les informations cartographiques locales de Longhorn à partir du référentiel de cartes.

`helm repo update`

Installez la carte Longhorn.

Avec Helm 2, la commande suivante créera l'espace de noms du système Longhorn et installera la carte Longhorn ensemble.

`helm install longhorn/longhorn --name longhorn --namespace longhorn-system`

Avec Helm 3, les commandes suivantes créeront d'abord l'espace de noms du système Longhorn, puis installeront la carte Longhorn.

```bash
kubectl create namespace longhorn-system
helm install longhorn longhorn/longhorn --namespace longhorn-system
```

Créer une classe volumesnapshot en utilisant Longhorn

```yaml
kind: VolumeSnapshotClass
apiVersion: snapshot.storage.k8s.io/v1
metadata:
  name: longhorn-snapshot-vsc
driver: driver.longhorn.io
deletionPolicy: Delete
parameters:
  type: snap
```

```bash
$ kubectl apply -f volumesnapshotclass.yaml
  volumesnapshotclass.snapshot.storage.k8s.io/longhorn-snapshot-vsc unchanged
```

### Installer le pilote CSI pour NFS

Installez le pilote CSI pour créer un volume NFS à partir de [ici](https://github.com/kubernetes-csi/csi-driver-nfs/tree/master/charts).

```bash
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm install csi-driver-nfs csi-driver-nfs/csi-driver-nfs --namespace kube-system --version v4.5.0 --set feature.enableFSGroupPolicy=true
```

Soyez conscient de définir `--set feature.enableFSGroupPolicy=true` ce.

Nous utiliserons l'espace de noms `demo` tout au long de ce tutoriel.

```bash
➤ kubectl create ns demo
namespace/demo created
```

### Configurer le serveur NFS

Nous allons déployer un serveur nfs et un service utilisant les yamls ci-dessous. Notez que nous avons partagé `/exports` chemin.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nfs-server
  namespace: demo
spec:
  selector:
    matchLabels:
      app: nfs-server
  template:
    metadata:
      labels:
        app: nfs-server
    spec:
      containers:
        - name: nfs-server
          image: k8s.gcr.io/volume-nfs:0.8
          ports:
            - name: nfs
              containerPort: 2049
            - name: mountd
              containerPort: 20048
            - name: rpcbind
              containerPort: 111
          securityContext:
            privileged: true
          volumeMounts:
            - name: storage
              mountPath: /exports
      volumes:
        - name: storage
          hostPath:
            path: /data/nfs # store all data in "/data/nfs" directory of the node where it is running
            type: DirectoryOrCreate
---
apiVersion: v1
kind: Service
metadata:
  name: nfs-server
  namespace: demo
spec:
  ports:
    - name: nfs
      port: 2049
    - name: mountd
      port: 20048
    - name: rpcbind
      port: 111
  selector:
    app: nfs-server # must match with the label of NFS pod
```

```bash
➤ kubectl apply -f nfs-server.yaml
deployment.apps/nfs-server created
service/nfs-server created
```

le serveur nfs devrait fonctionner à l'intérieur `nfs-server-***` cosse

### Créer StorageClass pour NFS

```yaml
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: nfs 
parameters:
  server: nfs-server.demo.svc.cluster.local
  share: /
provisioner: nfs.csi.k8s.io
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

Ici, `parameters.server` doit être le nom DNS de votre service créé avec le serveur NFS, `parameters.share` devrait être le chemin à l’intérieur du répertoire partagé.

### Créer un stockage de sauvegarde

Créez d’abord un PVC que nous utiliserons comme stockage backend. Ce pvc doit être créé en utilisant `nfs` storageClass que nous avons créé précédemment.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nfs-pvc
  namespace: demo
spec:
  storageClassName: "nfs"
  resources:
    requests:
      storage: 1Gi
  accessModes: 
    - ReadWriteOnce
```

Maintenant, nous créons le backupStorage de la manière suivante.

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: local-storage
  namespace: demo
spec:
  storage:
    provider: local
    local:
      mountPath: /md/walg
      persistentVolumeClaim:
        claimName: nfs-pvc
  usagePolicy:
    allowedNamespaces:
      from: All
  default: false
  deletionPolicy: WipeOut
  runtimeSettings:
    pod:
      securityContext:
        fsGroup: 999
        runAsUser: 999
```

```bash
$ kubectl apply -f nfs-pvc.yaml
  persistentvolumeclaim/nfs-pvc  created
```

```bash
$ kubectl apply -f backupstorage.yaml
   backupstorage.storage.kubestash.com/linode-storage created
```

### Politique de rétention

RetentionPolicy est une ressource personnalisée (CR) fournie par KubeStash qui vous permet de définir la durée pendant laquelle vous souhaitez conserver les données de sauvegarde.

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: mariadb-retention-policy
  namespace: demo
spec:
  maxRetentionPeriod: "30d"
  successfulSnapshots:
    last: 2
  failedSnapshots:
    last: 2
```

```bash
$ kubectl apply -f  https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/nfs/yamls/retentionPolicy.yaml 
retentionpolicy.storage.kubestash.com/mariadb-retention-policy created
```

### ChiffrementSecret

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: encrypt-secret
  namespace: demo
stringData:
  RESTIC_PASSWORD: "changeit"
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/nfs/yamls/encryptionSecret.yaml
```

### MariaDBArchiver

MariaDBArchiver est une ressource personnalisée (CR) fournie par KubeDB pour gérer l'archivage des fichiers binlog MariaDB et effectuer des sauvegardes au niveau du volume.

```yaml
apiVersion: archiver.kubedb.com/v1alpha1
kind: MariaDBArchiver
metadata:
  name: mariadbarchiver-sample
  namespace: demo
spec:
  pause: false
  databases:
    namespaces:
      from: Selector
      selector:
        matchLabels:
          kubernetes.io/metadata.name: demo
    selector:
      matchLabels:
        archiver: "true"
  retentionPolicy:
    name: mariadb-retention-policy
    namespace: demo
  encryptionSecret:
    name: "encrypt-secret"
    namespace: "demo"
  fullBackup:
    jobTemplate:
      spec:
        securityContext:
          fsGroup: 999
          runAsUser: 999
    driver: "VolumeSnapshotter"
    task:
      params:
        volumeSnapshotClassName: "longhorn-snapshot-vsc"
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  manifestBackup:
    jobTemplate:
      spec:
        securityContext:
          fsGroup: 999
          runAsUser: 999
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  backupStorage:
    ref:
      name: "local-storage"
      namespace: "demo"
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/nfs/yamls/mariadbarchiver.yaml
 mariadbarchiver.archiver.kubedb.com/mariadbarchiver-sample created
```

# Déployer MariaDB

Jusqu'à présent, nous sommes prêts à configurer l'archivage continu de MariaDB. Nous déployons un mariadb faisant référence à l'objet archiveur MariaDB. Pour configurer correctement MariaDB pour l'archivage, vous devez transmettre des arguments spécifiques au conteneur MariaDB dans le fichier `spec.podTemplate.containers["mariadb"].args` champ. Vous trouverez ci-dessous un exemple de configuration YAML pour une instance MariaDB gérée par KubeDB, avec l'archivage activé.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
  labels:
    archiver: "true"
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  archiver:
    ref:
      name: mariadbarchiver-sample
      namespace: demo
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl get pod -n demo
NAME                                                              READY   STATUS      RESTARTS        AGE
mariadb-0                                                         2/2     Running     0               4m12s
mariadb-1                                                         2/2     Running     0               4m12s
mariadb-2                                                         2/2     Running     0               3m12s
mariadb-backup-full-backup-1726549703-bjk9w                       0/1     Completed   0               3m22s
mariadb-backup-manifest-backup-1726549703-fx9kx                   0/1     Completed   0               3m22s
mariadb-sidekick                                                  1/1     Running
retention-policy-mariadb-backup-full-backup-1726549703-wg7wt      0/1     Completed   0               3m42s
retention-policy-mariadb-backup-manifest-backup-17265497038pvjd   0/1     Completed   0               3m55s
```

`mariadb-sidekick` est responsable du téléchargement des fichiers binlog

`mariadb-backup-full-backup-1726549703-bjk9w` sont le pod de sauvegardes de niveaux de volumes pour MariaDB.

`mariadb-backup-manifest-backup-1726549703-fx9kx` sont le pod de la sauvegarde du manifeste lié à l'objet MariaDB

### valider BackupConfiguration et VolumeSnapshots

```bash
$ kubectl get backupconfigurations -n demo

NAME                    PHASE   PAUSED   AGE
mariadb-backup          Ready            2m43s

$ kubectl get backupsession -n demo
NAME                                           INVOKER-TYPE          INVOKER-NAME            PHASE       DURATION   AGE
mariadb-backup-full-backup-1726549703          BackupConfiguration   mariadb-backup          Succeeded   33s        11m
mariadb-backup-manifest-backup-1726549703      BackupConfiguration   mariadb-backup          Succeeded   20s        11m

kubectl get volumesnapshots -n demo
NAME                    READYTOUSE   SOURCEPVC        SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS           SNAPSHOTCONTENT                                    CREATIONTIME   AGE
mariadb-1726549985      true         data-mariadb-0                           10Gi          longhorn-snapshot-vsc   snapcontent-317aaac9-ae4f-438b-9763-4eb81ff828af    11m            11m
```

## Insertion de données et changement de fichier binlog

Après chaque changement de binlog, les fichiers binlog seront téléchargés vers le stockage de sauvegarde.

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');

MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

> À ce stade, nous avons 10 lignes dans notre tableau nouvellement créé `demo_table` sur la base de données `hello`

## Récupération ponctuelle

La récupération ponctuelle vous permet de restaurer une base de données MariaDB à un moment précis à l'aide des journaux de transactions archivés. Ceci est particulièrement utile dans les scénarios où vous devez restaurer un état juste avant qu'une erreur spécifique ou une corruption de données ne se produise.
Disons accidentellement que notre dba supprime la table demo\_table et que nous souhaitons la restaurer.

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash

MariaDB [hello]> drop table demo_table;

MariaDB [hello]> flush logs;
```

Nous ne pouvons pas restaurer à partir d'une sauvegarde complète car à ce stade, aucune sauvegarde complète n'a été effectuée. nous pouvons donc choisir une heure spécifique à laquelle nous voulons restaurer. Nous pouvons obtenir l'heure spécifique à partir du journal binaire archivé dans le stockage de sauvegarde. Accédez au fichier binlog et trouvez où stocker. Vous pouvez analyser les fichiers binlog en utilisant `mariadbbinlog`.

Pour la démo, j'utiliserai la fois précédente où nous recevrons le formulaire `select now()`

```mysql
MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+
```

### Restaurer MariaDB

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: restore-mariadb
  namespace: demo
spec:
  init:
    archiver:
      encryptionSecret:
        name: encrypt-secret
        namespace: demo
      fullDBRepository:
        name: mariadb-full
        namespace: demo
      recoveryTimestamp: "2024-09-17T05:28:26Z"
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl apply -f mariadbrestore.yaml
mariadb.kubedb.com/restore-mariadb created
```

**vérifier MariaDB restaurée**

```bash
$ kubectl get pod -n demo
restore-mariadb-0                                          1/1     Running     0             44s
restore-mariadb-1                                          1/1     Running     0             42s
restore-mariadb-2                                          1/1     Running     0             41s
restore-mariadb-restorer-z4brz                             0/2     Completed   0             113s
restore-mariadb-restoresession-lk6jq                       0/1     Completed   0             2m6s
```

```bash
$ kubectl get mariadb -n demo
NAME              VERSION   STATUS   AGE
mariadb           11.1.3    Ready    14m
restore-mariadb   11.1.3    Ready    5m37s
```

**Validation des données sur MariaDB restaurée**

```bash
$ kubectl exec -it -n demo restore-mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

mariadb> use hello

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
1 row in set (0.00 sec)
```

**afin que nous puissions nous remettre avec succès d'une catastrophe**

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete -n demo mariadb/mariadb
$ kubectl delete -n demo mariadb/restore-mariadb
$ kubectl delete -n demo backupstorage
$ kubectl delete -n demo mariadbarchiver
$ kubectl delete ns demo
```

## Prochaines étapes

* En savoir plus sur [sauvegarde et restauration](fr/backup/kubestash/overview.md) Base de données MariaDB utilisant KubeStash.
* En savoir plus sur l'initialisation [MariaDB avec script](fr/initialization/using-script.md).
* Vous souhaitez configurer le cluster MariaDB ? Vérifiez comment [configurer le cluster MariaDB hautement disponible](fr/clustering/galera-cluster.md)
* Surveillez votre base de données MariaDB avec KubeDB en utilisant [Prometheus intégré](fr/monitoring/builtin-prometheus.md).
* Surveillez votre base de données MariaDB avec KubeDB en utilisant [Opérateur Prométhée](fr/monitoring/prometheus-operator.md).
* Concepts détaillés de [Objet MariaDB](fr/concepts/mariadb.md).
* Utiliser [registre Docker privé](fr/private-registry/quickstart.md) pour déployer MariaDB avec KubeDB.
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: pitr/overview.md -->
> Vous débutez avec KubeDB ? Commencez [ici](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB MariaDB - Archivage continu et récupération ponctuelle (PITR)

Ici, nous allons vous montrer comment utiliser KubeDB pour provisionner une MariaDB afin d'archiver en continu et de restaurer à un moment donné.

## Avant de commencer

Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Pour cette démonstration, j'utilise le cluster linode.

Maintenant, installez `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).

Pour installer `KubeStash` opérateur dans votre cluster en suivant les étapes [ici](https://github.com/kubestash/installer/tree/master/charts/kubestash).

Pour installer `External-snapshotter` dans votre cluster en suivant les étapes [ici](https://github.com/kubernetes-csi/external-snapshotter/tree/release-5.0).

Pour isoler cet exercice, ce tutoriel utilise un espace de noms dédié appelé `demo`.

```bash
$ kubectl create ns demo
namespace/demo created
```

> Remarque : Les fichiers yaml utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/pitr/overview/yamls](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/remote-replica/yamls) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Archivage continu

```mermaid
flowchart LR
  DB["Pods MariaDB"] -->|Journaux binlog| Archiver["MariaDBArchiver + Sidekick"]
  Archiver -->|Téléversement continu| Store["Dépôt BackupStorage"]
  Snap["VolumeSnapshot (Sauvegarde complète)"] --> Restorer["Restauration MariaDB (recoveryTimestamp)"]
  Store -->|Relecture des binlogs| Restorer
  Restorer --> Target["Cluster MariaDB restauré"]
```

L'archivage continu implique la réalisation de copies régulières (ou « archives ») des fichiers journaux des transactions MariaDB. Pour garantir un archivage continu vers un emplacement distant, nous devons préparer `BackupStorage`,`RetentionPolicy`,`MariaDBArchiver` pour les bases de données MariaDB gérées par KubeDB.

### BackupStorage

BackupStorage est un CR fourni par KubeStash qui peut gérer le stockage de divers fournisseurs tels que GCS, S3, etc.
Nous allons stocker nos données de sauvegarde dans un `S3` seau. Nous devons créer un `Secret` avec les informations d'identification nécessaires et un `BackupStorage` CR pour utiliser ce backend. Si vous souhaitez utiliser un autre backend, veuillez lire le document de configuration du backend correspondant à partir de [ici](https://kubestash.com/docs/latest/guides/backends/overview/).

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: linode-storage
  namespace: demo
spec:
  storage:
    provider: s3
    s3:
      bucket: test-archiver
      endpoint: https://ap-south-1.linodeobjects.com
      region: ap-south-1
      prefix: backup
      secretName: storage
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: WipeOut
```

```bash
$ kubectl apply -f backupstorage.yaml
   backupstorage.storage.kubestash.com/linode-storage created
```

### Secrets pour BackupStorage

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: storage
  namespace: demo
stringData:
  AWS_ACCESS_KEY_ID: "*************26CX"
  AWS_SECRET_ACCESS_KEY: "************jj3lp"
  AWS_ENDPOINT: https://ap-south-1.linodeobjects.com
```

```bash
$ kubectl apply -f storage-secret.yaml 
  secret/storage created
```

### Politique de rétention (`RetentionPolicy`)

RetentionPolicy est une ressource personnalisée (CR) fournie par KubeStash qui vous permet de définir la durée pendant laquelle vous souhaitez conserver les données de sauvegarde.

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: mariadb-retention-policy
  namespace: demo
spec:
  maxRetentionPeriod: "30d"
  successfulSnapshots:
    last: 100
  failedSnapshots:
    last: 2
```

```bash
$ kubectl apply -f  https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/overview/yamls/retention-policy.yaml 
retentionpolicy.storage.kubestash.com/mariadb-retention-policy created
```

### MariaDBArchiver

MariaDBArchiver est une ressource personnalisée (CR) fournie par KubeDB pour gérer l'archivage des fichiers binlog MariaDB et effectuer des sauvegardes au niveau du volume.

```yaml
apiVersion: archiver.kubedb.com/v1alpha1
kind: MariaDBArchiver
metadata:
  name: mariadbarchiver-sample
  namespace: demo
spec:
  pause: false
  databases:
    namespaces:
      from: Selector
      selector:
        matchLabels:
          kubernetes.io/metadata.name: demo
    selector:
      matchLabels:
        archiver: "true"
  retentionPolicy:
    name: mariadb-retention-policy
    namespace: demo
  encryptionSecret:
    name: "encrypt-secret"
    namespace: "demo"
  fullBackup:
    driver: "VolumeSnapshotter"
    task:
      params:
        volumeSnapshotClassName: "longhorn-snapshot-vsc"
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  manifestBackup:
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  backupStorage:
    ref:
      name: "linode-storage"
      namespace: "demo"
```

### EncryptionSecret

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: encrypt-secret
  namespace: demo
stringData:
  RESTIC_PASSWORD: "changeit"
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/overview/yamls/mariadbarchiver.yaml
 mariadbarchiver.archiver.kubedb.com/mariadbarchiver-sample created
 $ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/overview/yamls/encryptionSecret.yaml
```

## Ensure volumeSnapshotClass

```bash
$ kubectl get volumesnapshotclasses
NAME                    DRIVER               DELETIONPOLICY   AGE
longhorn-snapshot-vsc   driver.longhorn.io   Delete           7d22h
```

Si ce n'est pas le cas, essayez d'utiliser `longhorn` ou tout autre [volumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/).

```yaml
kind: VolumeSnapshotClass
apiVersion: snapshot.storage.k8s.io/v1
metadata:
  name: longhorn-snapshot-vsc
driver: driver.longhorn.io
deletionPolicy: Delete
parameters:
  type: snap
```

```bash
$ helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace

$ kubectl apply -f volumesnapshotclass.yaml
  volumesnapshotclass.snapshot.storage.k8s.io/longhorn-snapshot-vsc unchanged
```

# Déployer MariaDB

Jusqu'à présent, nous sommes prêts à configurer l'archivage continu de MariaDB. Nous déployons un mariadb faisant référence à l'objet archiveur MariaDB. Pour configurer correctement MariaDB pour l'archivage, vous devez transmettre des arguments spécifiques au conteneur MariaDB dans le fichier `spec.podTemplate.containers["mariadb"].args` champ. Vous trouverez ci-dessous un exemple de configuration YAML pour une instance MariaDB gérée par KubeDB, avec l'archivage activé.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
  labels:
    archiver: "true"
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  archiver:
    ref:
      name: mariadbarchiver-sample
      namespace: demo
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl get pod -n demo
NAME                                                              READY   STATUS      RESTARTS        AGE
mariadb-0                                                         2/2     Running     0               4m12s
mariadb-1                                                         2/2     Running     0               4m12s
mariadb-2                                                         2/2     Running     0               3m12s
mariadb-backup-full-backup-1726549703-bjk9w                       0/1     Completed   0               3m22s
mariadb-backup-manifest-backup-1726549703-fx9kx                   0/1     Completed   0               3m22s
mariadb-sidekick                                                  1/1     Running
retention-policy-mariadb-backup-full-backup-1726549703-wg7wt      0/1     Completed   0               3m42s
retention-policy-mariadb-backup-manifest-backup-17265497038pvjd   0/1     Completed   0               3m55s
```

`mariadb-sidekick` est chargé de téléverser les fichiers binlog.

`mariadb-backup-full-backup-1726549703-bjk9w` sont le pod de sauvegardes de niveaux de volumes pour MariaDB.

`mariadb-backup-manifest-backup-1726549703-fx9kx` sont le pod de la sauvegarde du manifeste lié à l'objet MariaDB

### Valider BackupConfiguration et VolumeSnapshots

```bash
$ kubectl get backupconfigurations -n demo

NAME                    PHASE   PAUSED   AGE
mariadb-backup          Ready            2m43s

$ kubectl get backupsession -n demo
NAME                                           INVOKER-TYPE          INVOKER-NAME            PHASE       DURATION   AGE
mariadb-backup-full-backup-1726549703          BackupConfiguration   mariadb-backup          Succeeded   33s        11m
mariadb-backup-manifest-backup-1726549703      BackupConfiguration   mariadb-backup          Succeeded   20s        11m

kubectl get volumesnapshots -n demo
NAME                    READYTOUSE   SOURCEPVC        SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS           SNAPSHOTCONTENT                                    CREATIONTIME   AGE
mariadb-1726549985      true         data-mariadb-0                           10Gi          longhorn-snapshot-vsc   snapcontent-317aaac9-ae4f-438b-9763-4eb81ff828af    11m            11m
```

## Insertion de données et changement de fichier binlog

Après chaque changement de binlog, les fichiers binlog seront téléchargés vers le stockage de sauvegarde.

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');

MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

> À ce stade, nous avons 10 lignes dans notre tableau nouvellement créé `demo_table` on database `hello`

## Récupération ponctuelle

La récupération ponctuelle (PITR) permet de restaurer une base de données MariaDB à un instant précis à l'aide des journaux de transactions archivés. Ce mécanisme est particulièrement utile pour revenir à un état juste avant une erreur ou une corruption des données.
Supposons que notre DBA supprime accidentellement la table `demo_table` et souhaite la restaurer.

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash

MariaDB [hello]> drop table demo_table;

MariaDB [hello]> flush logs;
```

Nous ne pouvons pas restaurer à partir d'une sauvegarde complète car à ce stade, aucune sauvegarde complète n'a été effectuée. nous pouvons donc choisir une heure spécifique à laquelle nous voulons restaurer. Nous pouvons obtenir l'heure spécifique à partir du journal binaire archivé dans le stockage de sauvegarde. Accédez au fichier binlog et trouvez où stocker. Vous pouvez analyser les fichiers binlog en utilisant `mariadbbinlog`.

Pour cette démonstration, nous utilisons l'horodatage précédent obtenu avec `select now()`.

```mysql
MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+
```

### Restaurer MariaDB

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: restore-mariadb
  namespace: demo
spec:
  init:
    archiver:
      encryptionSecret:
        name: encrypt-secret
        namespace: demo
      fullDBRepository:
        name: mariadb-full
        namespace: demo
      recoveryTimestamp: "2024-09-17T05:28:26Z"
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl apply -f mariadbrestore.yaml
mariadb.kubedb.com/restore-mariadb created
```

**vérifier MariaDB restaurée**

```bash
$ kubectl get pod -n demo
restore-mariadb-0                                          1/1     Running     0             44s
restore-mariadb-1                                          1/1     Running     0             42s
restore-mariadb-2                                          1/1     Running     0             41s
restore-mariadb-restorer-z4brz                             0/2     Completed   0             113s
restore-mariadb-restoresession-lk6jq                       0/1     Completed   0             2m6s
```

```bash
$ kubectl get mariadb -n demo
NAME              VERSION   STATUS   AGE
mariadb           11.1.3    Ready    14m
restore-mariadb   11.1.3    Ready    5m37s
```

**Validation des données sur MariaDB restaurée**

```bash
$ kubectl exec -it -n demo restore-mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

mariadb> use hello

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
1 row in set (0.00 sec)
```

**Nous avons ainsi réussi la récupération après sinistre.**

## Nettoyage

Pour nettoyer les ressources Kubernetes créées dans ce tutoriel, exécutez :

```bash
$ kubectl delete -n demo mariadb/mariadb
$ kubectl delete -n demo mariadb/restore-mariadb
$ kubectl delete -n demo backupstorage
$ kubectl delete -n demo mariadbarchiver
$ kubectl delete ns demo
```

## Prochaines étapes

* En savoir plus sur [backup and restore](fr/backup/kubestash/overview.md) Base de données MariaDB utilisant KubeStash.
* En savoir plus sur l'initialisation [MariaDB with Script](fr/initialization/using-script.md).
* Vous souhaitez configurer le cluster MariaDB ? Vérifiez comment [configurer le cluster MariaDB hautement disponible](fr/clustering/galera-cluster.md)
* Surveillez votre base de données MariaDB avec KubeDB à l'aide de [Prometheus intégré](fr/monitoring/builtin-prometheus.md).
* Surveillez votre base de données MariaDB avec KubeDB à l'aide de [l'opérateur Prometheus](fr/monitoring/prometheus-operator.md).
* Consultez les concepts détaillés de l'[objet MariaDB](fr/concepts/mariadb.md).
* Utilisez un [registre Docker privé](fr/private-registry/quickstart.md) pour déployer MariaDB avec KubeDB.
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: private-registry/quickstart.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Déployer MariaDB à partir du registre Docker privé

L’opérateur KubeDB prend en charge l’utilisation du registre Docker privé. Ce didacticiel vous montrera comment utiliser KubeDB pour exécuter la base de données MariaDB à l'aide d'images Docker privées.

## Avant de commencer

* Lire [concept du catalogue de versions MariaDB](fr/concepts/mariadb-version.md) pour apprendre les concepts détaillés de `MariaDBVersion` objet.
* Vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Vous aurez également besoin d'un docker privé [enregistrement](https://docs.docker.com/registry/) ou [dépôt privé](https://docs.docker.com/docker-hub/repos/#private-repositories). Dans ce tutoriel, nous utiliserons un référentiel privé de [hub de docker](https://hub.docker.com/).
* Vous devez pousser les images requises depuis KubeDB [Compte Docker Hub](https://hub.docker.com/u/kubedb) dans votre registre privé. Pour MariaDB, appuyez sur `DB_IMAGE`, `EXPORTER_IMAGE`, `INITCONTAINER_IMAGE` des versions MariaDB suivantes, où `deprecated` n'est pas vrai, à votre registre privé.

```bash
$ kubectl get mariadbversions -n kube-system  -o=custom-columns=NAME:.metadata.name,VERSION:.spec.version,DB_IMAGE:.spec.db.image,EXPORTER_IMAGE:.spec.exporter.image,INITCONTAINER_IMAGE:.spec.initContainer.image,DEPRECATED:.spec.deprecated
NAME      VERSION   DB_IMAGE                                        EXPORTER_IMAGE                           INITCONTAINER_IMAGE                 DEPRECATED
10.10.7   10.10.7   ghcr.io/appscode-images/mariadb:10.10.7-jammy   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.11.6   10.11.6   ghcr.io/appscode-images/mariadb:10.11.6-jammy   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.4.32   10.4.32   ghcr.io/appscode-images/mariadb:10.4.32-focal   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.5.23   10.5.23   ghcr.io/appscode-images/mariadb:10.5.23-focal   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.6.16   10.6.16   ghcr.io/appscode-images/mariadb:10.6.16-focal   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.0.4    11.0.4    ghcr.io/appscode-images/mariadb:11.0.4-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.1.3    11.1.3    ghcr.io/appscode-images/mariadb:11.1.3-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.2.2    11.2.2    ghcr.io/appscode-images/mariadb:11.2.2-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.3.2    11.3.2    ghcr.io/appscode-images/mariadb:11.3.2-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.4.3    11.4.3    ghcr.io/appscode-images/mariadb:11.4.3-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.5.2    11.5.2    ghcr.io/appscode-images/mariadb:11.5.2-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.6.2    11.6.2    ghcr.io/appscode-images/mariadb:11.6.2-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.8.5    11.8.5    ghcr.io/appscode-images/mariadb:11.8.5-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
12.1.2    12.1.2    ghcr.io/appscode-images/mariadb:12.1.2-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
```

Dépôts du hub Docker :

* [kubedb/opérateur](https://hub.docker.com/r/kubedb/operator)
* [kubedb/mariadb](https://hub.docker.com/r/kubedb/mariadb)
* [kubedb/mysqld-exportateur](https://hub.docker.com/r/kubedb/mysqld-exporter)

  + Mettez à jour le catalogue KubeDB pour le registre Docker privé. Ex:

    ```yaml
    apiVersion: catalog.kubedb.com/v1alpha1
    kind: MariaDBVersion
    metadata:
      name: 11.8.5
    spec:
      coordinator:
        image: PRIVATE_REGISTRY/mariadb-coordinator:v0.40.0
      db:
        image: PRIVATE_REGISTRY/mariadb:11.8.5
      exporter:
        image: PRIVATE_REGISTRY/mysqld-exporter:v0.11.0
      initContainer:
        image: PRIVATE_REGISTRY/busybox
      maxscale:
        image: mariadb/maxscale:24.02.4
        securityContext:
          runAsUser: 995
      podSecurityPolicies:
        databasePolicyName: maria-db
      version: 12.1.2
    ```
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel. Exécutez la commande suivante pour préparer votre cluster pour ce didacticiel :

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Créer ImagePullSecret

ImagePullSecrets est un type de secret Kubernete dont le seul objectif est d'extraire des images privées d'un registre Docker. Il vous permet de spécifier l'URL du registre Docker, les informations d'identification pour vous connecter et le nom de votre image Docker privée.

Exécutez la commande suivante, en remplaçant les valeurs majuscules appropriées pour créer un secret d'extraction d'image pour votre registre Docker privé :

```bash
$ kubectl create secret docker-registry -n demo myregistrykey \
  --docker-server=DOCKER_REGISTRY_SERVER \
  --docker-username=DOCKER_USER \
  --docker-email=DOCKER_EMAIL \
  --docker-password=DOCKER_PASSWORD
secret/myregistrykey created
```

Si vous souhaitez suivre d'autres méthodes pour extraire des images privées, consultez [documents officiels](https://kubernetes.io/docs/concepts/containers/images/) de Kubernetes.

NB : Si vous utilisez `kubectl` 1.9.0, mettez à jour vers 1.9.1 ou version ultérieure pour éviter cela [problème](https://github.com/kubernetes/kubernetes/issues/57427).

## Installer l'opérateur KubeDB

Lors de l'installation de l'opérateur KubeDB, définissez les indicateurs `--docker-registry` et `--image-pull-secret` à une valeur appropriée. Suivez les étapes pour [installer l'opérateur KubeDB](https://kubedb.com/docs/v2026.7.10/setup/README) correctement dans le cluster afin qu'il pointe vers le DOCKER\_REGISTRY à partir duquel vous souhaitez extraire des images.

## Déployer la base de données MariaDB à partir du registre privé

Lors du déploiement `MariaDB` à partir du référentiel privé, vous devez ajouter `myregistrykey` secret dans `MariaDB` `spec.imagePullSecrets`.
Vous trouverez ci-dessous l'objet MariaDB CRD que nous allons créer.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-pvt-reg
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
  podTemplate:
    spec:
      imagePullSecrets:
      - name: myregistrykey
  deletionPolicy: WipeOut
```

Maintenant, exécutez la commande pour déployer ceci `MariaDB` objet:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/private-registry/quickstart/examples/demo.yaml
mariadb.kubedb.com/md-pvt-reg created
```

Pour vérifier si les images ont été extraites avec succès du référentiel, vérifiez si le `MariaDB` est en état de fonctionnement :

```bash
$ kubectl get pods -n demo
NAME              READY     STATUS    RESTARTS   AGE
md-pvt-reg-0   1/1       Running   0          56s
```

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo md-pvt-reg
mariadb.kubedb.com "md-pvt-reg" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: quickstart/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Démarrage rapide de MariaDB

Ce tutoriel vous montrera comment utiliser KubeDB pour exécuter une base de données MariaDB.

![lifecycle](images/quickstart_overview_mariadb-lifecycle.png)

> Remarque : Les fichiers yaml utilisés dans ce didacticiel sont stockés dans [ici](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples).

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* [Classe de stockage](https://kubernetes.io/docs/concepts/storage/storage-classes/) est requis pour exécuter KubeDB. Vérifiez la StorageClass disponible dans le cluster.

```bash
$ kubectl get storageclasses
NAME                 PROVISIONER             RECLAIMPOLICY     VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
standard (default)   rancher.io/local-path   Delete            WaitForFirstConsumer   false                  6h22m
```

* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```
$ kubectl create ns demo
namespace/demo created
```

## Rechercher la version MariaDB disponible

Lorsque vous avez installé KubeDB, il a créé `MariaDBVersion` crd pour toutes les versions de MariaDB prises en charge. Vérifiez-le en utilisant la commande suivante,

```bash
$ kubectl get mariadbversions
NAME      VERSION   DB_IMAGE                                        DEPRECATED   AGE
10.10.7   10.10.7   ghcr.io/appscode-images/mariadb:10.10.7-jammy                12d
10.11.6   10.11.6   ghcr.io/appscode-images/mariadb:10.11.6-jammy                12d
10.4.32   10.4.32   ghcr.io/appscode-images/mariadb:10.4.32-focal                12d
10.5.23   10.5.23   ghcr.io/appscode-images/mariadb:10.5.23-focal                12d
10.6.16   10.6.16   ghcr.io/appscode-images/mariadb:10.6.16-focal                12d
11.0.4    11.0.4    ghcr.io/appscode-images/mariadb:11.0.4-jammy                 12d
11.1.3    11.1.3    ghcr.io/appscode-images/mariadb:11.1.3-jammy                 12d
11.2.2    11.2.2    ghcr.io/appscode-images/mariadb:11.2.2-jammy                 12d
11.3.2    11.3.2    ghcr.io/appscode-images/mariadb:11.3.2-jammy                 12d
11.4.3    11.4.3    ghcr.io/appscode-images/mariadb:11.4.3-noble                 12d
11.5.2    11.5.2    ghcr.io/appscode-images/mariadb:11.5.2-noble                 12d
11.6.2    11.6.2    ghcr.io/appscode-images/mariadb:11.6.2-noble                 12d
11.8.5    11.8.5    ghcr.io/appscode-images/mariadb:11.8.5-noble                 12d
12.1.2    12.1.2    ghcr.io/appscode-images/mariadb:12.1.2-noble                 12d
```

## Créer une base de données MariaDB

KubeDB implémente un CRD `MariaDB` pour définir la spécification d'une base de données MariaDB. Vous trouverez ci-dessous l'objet `MariaDB` créé dans ce tutoriel.

`Note` : Si votre version de `KubeDB` est inférieure ou égale à `v2024.6.4`, utilisez la version d'API `v1alpha2`.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
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
  deletionPolicy: Delete
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples/sample-mariadb-v1.yaml
mariadb.kubedb.com/sample-mariadb created
```

```yaml
apiVersion: kubedb.com/v1alpha2
kind: MariaDB
metadata:
  name: sample-mariadb
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
  terminationPolicy: Delete
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples/sample-mariadb-v1alpha2.yaml
mariadb.kubedb.com/sample-mariadb created
```

Ici,

* `spec.version` est le nom du CRD MariaDBVersion où les images Docker sont spécifiées. Dans ce tutoriel, un MariaDB `12.1.2` la base de données va créer.
* `spec.storageType` spécifie le type de stockage qui sera utilisé pour la base de données MariaDB. Cela peut être `Durable` ou `Ephemeral`. La valeur par défaut de ce champ est `Durable`. Si `Ephemeral` est utilisé, KubeDB créera la base de données MariaDB en utilisant `EmptyDir` volume. Dans ce cas, vous n’êtes pas obligé de préciser `spec.storage` champ. Ceci est utile à des fins de test.
* `spec.storage` spécifie la StorageClass de PVC allouée dynamiquement pour stocker les données de cette base de données. Cette spécification de stockage sera transmise au PetSet créé par l'opérateur KubeDB pour exécuter les pods de base de données. Vous pouvez spécifier n'importe quelle StorageClass disponible dans votre cluster avec les demandes de ressources appropriées.
* `spec.terminationPolicy` ou `spec.deletionPolicy` donne la flexibilité de savoir s'il faut `nullify`(rejeter) l'opération de suppression de `MariaDB` crd ou quelles ressources KubeDB doit conserver ou supprimer lorsque vous supprimez `MariaDB` crd. Si le webhook d'admission est activé, il empêche les utilisateurs de supprimer la base de données tant que le `spec.terminationPolicy` est réglé sur `DoNotTerminate`.

> Remarque : la section spec.storage est utilisée pour créer un PVC pour le pod de base de données. Il créera un PVC avec une taille de stockage spécifiée dans le champ storage.resources.requests. Ne spécifiez pas de limites ici. Le PVC n'est pas redimensionné automatiquement.

L'opérateur KubeDB surveille `MariaDB` objets utilisant l’API Kubernetes. Quand un `MariaDB` est créé, l'opérateur KubeDB créera un nouveau PetSet et un service avec le nom d'objet MariaDB correspondant. L'opérateur KubeDB créera également un service de gouvernance pour les PetSets avec le nom `kubedb`, s'il n'y en a pas déjà un.

```bash
$ kubectl describe -n demo mariadb sample-mariadb
Name:         sample-mariadb
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  kubedb.com/v1
Kind:         MariaDB
Metadata:
  Creation Timestamp:  2022-06-06T04:42:27Z
  Finalizers:
    kubedb.com
  Generation:  2
  ...
  Resource Version:  2673
  UID:               2f9c9453-6e78-4521-91ea-34ad2da398bc
Spec:
  Allowed Schemas:
    Namespaces:
      From:  Same
  Auth Secret:
    Name:  sample-mariadb-auth
  Pod Template:
    ...
  Replicas:                  1
  Storage:
    Access Modes:
      ReadWriteOnce
    Resources:
      Requests:
        Storage:         1Gi
    Storage Class Name:  standard
  Storage Type:          Durable
  Termination Policy:    WipeOut
  Version:               11.8.5
Status:
  Conditions:
    Last Transition Time:  2022-06-06T04:42:27Z
    Message:               The KubeDB operator has started the provisioning of MariaDB: demo/sample-mariadb
    Reason:                DatabaseProvisioningStartedSuccessfully
    Status:                True
    Type:                  ProvisioningStarted
    Last Transition Time:  2022-06-06T04:43:37Z
    Message:               database sample-mariadb/demo is ready
    Reason:                AllReplicasReady
    Status:                True
    Type:                  Ready
    Last Transition Time:  2022-06-06T04:43:37Z
    Message:               database sample-mariadb/demo is accepting connection
    Reason:                AcceptingConnection
    Status:                True
    Type:                  AcceptingConnection
    Last Transition Time:  2022-06-06T04:43:26Z
    Message:               All desired replicas are ready.
    Reason:                AllReplicasReady
    Status:                True
    Type:                  ReplicaReady
    Last Transition Time:  2022-06-06T04:43:37Z
    Message:               The MariaDB: demo/sample-mariadb is successfully provisioned.
    Observed Generation:   2
    Reason:                DatabaseSuccessfullyProvisioned
    Status:                True
    Type:                  Provisioned
  Observed Generation:     2
  Phase:                   Ready
Events:
  Type    Reason      Age    From             Message
  ----    ------      ----   ----             -------
  Normal  Successful  3m49s  KubeDB Operator  Successfully created governing service
  Normal  Successful  3m49s  KubeDB Operator  Successfully created Service
  Normal  Successful  3m49s  KubeDB Operator  Successfully created PetSet demo/sample-mariadb
  Normal  Successful  3m49s  KubeDB Operator  Successfully created MariaDB
  Normal  Successful  3m49s  KubeDB Operator  Successfully created appbinding

  
  
$ kubectl get petset -n demo
NAME             READY   AGE
sample-mariadb   1/1     27m

$ kubectl get pvc -n demo
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-sample-mariadb-0   Bound    pvc-10651900-d975-467f-80ff-9c4755bdf917   1Gi        RWO            standard       27m

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-10651900-d975-467f-80ff-9c4755bdf917   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   standard                27m

$ kubectl get service -n demo
NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
sample-mariadb        ClusterIP   10.105.207.172   <none>        3306/TCP   28m
sample-mariadb-pods   ClusterIP   None             <none>        3306/TCP   28m
```

L'opérateur KubeDB définit le `status.phase` à `Running` une fois la base de données créée avec succès. Exécutez la commande suivante pour voir l'objet MariaDB modifié :

```bash
$ kubectl get mariadb -n demo sample-mariadb -o yaml
```

```text
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}},"storageClassName":"standard"},"storageType":"Durable","deletionPolicy":"WipeOut","version":"11.8.5"}}      
  creationTimestamp: "2021-03-10T04:31:09Z"
  finalizers:
  - kubedb.com
  generation: 2
  ...
  name: sample-mariadb
  namespace: demo
  resourceVersion: "7952"
  selfLink: /apis/kubedb.com/v1/namespaces/demo/mariadbs/sample-mariadb
  uid: 412a4739-ac65-4b5a-a943-5e148f3222b1
spec:
  authSecret:
    name: sample-mariadb-auth
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
  deletionPolicy: Delete
  version: 12.1.2
status:
  observedGeneration: 2
  phase: Ready
```

## Connectez-vous à la base de données MariaDB

L'opérateur KubeDB a créé un nouveau secret appelé `mariadb-quickstart-auth` *(format : {mariadb-object-name}-auth)* pour stocker le mot de passe pour `mariadb` superutilisateur. Ce secret contient un `username` clé qui contient le *nom d'utilisateur* pour le superutilisateur MariaDB et un `password` clé qui contient le *mot de passe* pour le superutilisateur MariaDB.

Si vous souhaitez utiliser un secret existant, veuillez le préciser lors de la création de l'objet MariaDB à l'aide de `spec.authSecret.name`. Lors de la création manuelle de ce secret, assurez-vous que le secret contient ces deux clés contenant des données `username` et `password` et assurez-vous également d'utiliser `root` comme valeur de `username`.

Maintenant, nous avons besoin de `username` et `password` pour nous connecter à cette base de données avec la commande `kubectl exec`. Dans cet exemple, le secret `sample-mariadb-auth` contient le nom d'utilisateur et le mot de passe.

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d
w*yOU$b53dTbjsjJ
```

Nous exécuterons dans le pod `sample-mariadb-0` et connectez-vous à la base de données en utilisant `username` et `password`.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- mariadb -u root --password='w*yOU$b53dTbjsjJ'
```

```mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 335
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.001 sec)
```

## Politique de suppression de base de données

Ce champ est utilisé pour réguler le processus de suppression des ressources associées lorsque `MariaDB` l'objet est supprimé. L'utilisateur peut définir la valeur de ce champ en fonction de ses besoins. Les options disponibles et leur scénario d'utilisation sont décrits ci-dessous :

**Ne pas terminer :**

Quand `deletionPolicy` est réglé sur `DoNotTerminate`, KubeDB profite de `ValidationWebhook` fonctionnalité dans les clusters Kubernetes 1.9.0 ou version ultérieure à implémenter `DoNotTerminate` fonctionnalité. Si le webhook d'admission est activé, il empêche les utilisateurs de supprimer la base de données tant que le `spec.deletionPolicy` est réglé sur `DoNotTerminate`. Si vous créez une base de données avec `deletionPolicy` `DoNotTerminate` et essayez de le supprimer, vous verrez ceci :

```bash
$ kubectl delete mariadb sample-mariadb -n demo
Error from server (BadRequest): admission webhook "mariadb.validators.kubedb.com" denied the request: mariadb "mariadb-quickstart" can't be halted. To delete, change spec.deletionPolicy
```

Exécutez maintenant `kubectl edit mariadb sample-mariadb -n demo` pour définir `spec.deletionPolicy` sur `Halt` (qui supprime l'objet mariadb et conserve le PVC, les instantanés et les secrets intacts) ou supprimez ce champ (qui est par défaut `Delete`). Vous pourrez ensuite supprimer/arrêter la base de données.

**Arrêt:**

Supposons que vous souhaitiez réutiliser le volume et les informations d'identification de votre base de données pour déployer votre base de données à l'avenir en utilisant les mêmes configurations. Mais pour le moment, vous souhaitez simplement supprimer la base de données, à l’exception des volumes et des informations d’identification de la base de données. Dans ce scénario, vous devez définir le `MariaDB` objet `deletionPolicy` à `Halt`.

Quand le `DeletionPolicy` est réglé sur `Halt` et l'objet MariaDB est supprimé, l'opérateur KubeDB supprimera le PetSet et ses pods mais laisse le `PVCs`, `secrets` et les données de sauvegarde de la base de données (`snapshots`) intact. Vous pouvez définir le `deletionPolicy` à `Halt` dans la base de données existante en utilisant `edit` commande pour tester.

Dans un premier temps, exécutez `kubectl edit mariadb sample-mariadb -n demo` pour définir `spec.deletionPolicy` sur `Halt`. Supprimez ensuite l'objet mariadb,

```bash
$ kubectl delete mariadb sample-mariadb -n demo
mariadb.kubedb.com "sample-mariadb" deleted
```

Maintenant, exécutez la commande suivante pour obtenir toutes les ressources mariadb dans `demo` les espaces de noms,

```bash
$ kubectl get petset,svc,secret,pvc -n demo
NAME                         TYPE                                  DATA   AGE
secret/default-token-w2pgw   kubernetes.io/service-account-token   3      31m
secret/sample-mariadb-auth   kubernetes.io/basic-auth              2      39s

NAME                                          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-sample-mariadb-0   Bound    pvc-7502c222-2b02-4363-9027-91ab0e7b76dc   1Gi        RWO            standard       39s
```

À partir du résultat ci-dessus, vous pouvez voir que toutes les ressources mariadb (`PetSet`, `Service`, etc.) sont supprimés sauf `PVC` et `Secret`. Vous pouvez recréer à nouveau votre mariadb en utilisant ces ressources.

**Supprimer:**

Si vous souhaitez supprimer la base de données existante ainsi que les volumes utilisés, mais que vous souhaitez restaurer la base de données à partir d'une base de données précédemment prise `snapshots` et `secrets` alors vous voudrez peut-être définir le `MariaDB` objet `deletionPolicy` à `Delete`. Dans ce cadre, `PetSet` et les volumes seront supprimés. Si vous décidez de restaurer la base de données, vous pouvez le faire à l'aide des instantanés et des informations d'identification.

Quand le `DeletionPolicy` est réglé sur `Delete` et l'objet MariaDB est supprimé, l'opérateur KubeDB supprimera le PetSet et ses pods ainsi que les PVC mais laisse le `secret` et les données de sauvegarde de la base de données (`snapshots`) intact.

Supposons que nous ayons une base de données avec `deletionPolicy` réglé sur `Delete`. Maintenant, nous allons supprimer la base de données à l'aide de la commande suivante :

```bash
$ kubectl delete mariadb sample-mariadb -n demo
mariadb.kubedb.com "sample-mariadb" deleted
```

Maintenant, exécutez la commande suivante pour obtenir toutes les ressources mariadb dans `demo` les espaces de noms,

```bash
$ kubectl get petset,svc,secret,pvc -n demo
NAME                         TYPE                                  DATA   AGE
secret/default-token-w2pgw   kubernetes.io/service-account-token   3      31m
secret/sample-mariadb-auth   kubernetes.io/basic-auth              2      39s
```

À partir du résultat ci-dessus, vous pouvez voir que toutes les ressources mariadb (`PetSet`, `Service`, `PVCs` etc.) sont supprimés sauf `Secret`. Vous pouvez initialiser votre mariadb en utilisant `snapshots`(si pris précédemment) et `secret`.

> Si vous ne définissez pas deletionPolicy, kubeDB définit DeletionPolicy sur Supprimer par défaut.

**Anéantir:**

Vous pouvez totalement supprimer le `MariaDB` base de données et ressources pertinentes sans aucun suivi par paramètre `deletionPolicy` à `WipeOut`. L'opérateur KubeDB supprimera toutes les ressources pertinentes de ce `MariaDB` base de données (c'est-à-dire `PVCs`, `Secrets`, `Snapshots`) lorsque le `deletionPolicy` est réglé sur `WipeOut`.

Supposons que nous ayons une base de données avec `deletionPolicy` réglé sur `WipeOut`. Maintenant, nous allons supprimer la base de données à l'aide de la commande suivante :

```bash
$ kubectl delete mariadb sample-mariadb -n demo
```

```text
mariadb.kubedb.com "sample-mariadb" deleted
```

Maintenant, exécutez la commande suivante pour obtenir toutes les ressources mariadb dans `demo` les espaces de noms,

```bash
$ kubectl get petset,svc,secret,pvc -n demo
No resources found in demo namespace.
```

À partir du résultat ci-dessus, vous pouvez voir que toutes les ressources mariadb sont supprimées. il n'y a pas d'option pour recréer/réinitialiser votre base de données si `deletionPolicy` est réglé sur `Delete`.

> Soyez prudent lorsque vous réglez le `deletionPolicy` à `Delete`. Parce qu'il n'y a aucune option pour retracer les ressources de la base de données si une fois la base de données supprimée.

## Base de données arrêtée

Si vous souhaitez supprimer les ressources MariaDB (`PetSet`,`Service`, etc.) sans supprimer le `MariaDB` objet, `PVCs` et `Secret` vous devez définir le `spec.halted` à `true`. L'opérateur KubeDB pourra supprimer les ressources liées à MariaDB à l'exception de `MariaDB` objet, `PVCs` et `Secret`.

Supposons que nous ayons une base de données en cours d'exécution `mariadb-quickstart` dans notre cluster. Maintenant, nous allons définir `spec.halted` à `true` dans `MariaDB` objet en exécutant `kubectl edit -n demo mariadb-quickstart` commande.

Exécutez la commande suivante pour obtenir les ressources MariaDB,

```bash
$ kubectl get mariadb,sts,secret,svc,pvc -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-quickstart   11.8.5    Halted   22m

NAME                           TYPE                                  DATA   AGE
secret/default-token-lgbjm     kubernetes.io/service-account-token   3      27h
secret/mariadb-quickstart-auth   Opaque                                2      22m

NAME                                            STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-mariadb-quickstart-0   Bound    pvc-7ab0ebb0-bb2e-45c1-9af1-4f175672605b   1Gi        RWO            standard       22m
```

À partir du résultat ci-dessus, vous pouvez voir que `MariaDB` objet, `PVCs`, `Secret` sont toujours en vie. Ensuite, vous pouvez recréer votre `MariaDB` avec la même configuration.

> Lorsque vous définissez `spec.halted` à `true` dans `MariaDB` objet alors le `deletionPolicy` est également réglé sur `Halt` par l'opérateur KubeDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete -n demo mariadb/sample-mariadb

kubectl delete ns demo
```

## Conseils pour les tests

Si vous testez simplement quelques fonctionnalités de base, vous souhaiterez peut-être éviter des tracas supplémentaires dus à certaines fonctionnalités de sécurité idéales pour l'environnement de production. Vous pouvez suivre ces conseils pour les éviter.

1. **Utiliser `storageType: Ephemeral`**. Les bases de données sont précieuses. Vous ne souhaiterez peut-être pas perdre vos données dans votre environnement de production en cas de panne du pod de base de données. Nous recommandons donc d'utiliser `spec.storageType: Durable` et fournir des spécifications de stockage dans `spec.storage` section. À des fins de test, vous pouvez simplement utiliser `spec.storageType: Ephemeral`. KubeDB utilisera [videDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) pour le stockage. Vous n'aurez pas besoin de fournir `spec.storage` section.
2. **Utiliser `deletionPolicy: WipeOut`**. C'est bien de pouvoir supprimer tout ce qui est créé par KubeDB pour un crd MariaDB particulier lorsque vous supprimez le crd.

## Prochaines étapes

* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: recommendation/recommendation.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Recommandation MariaDB

## Aperçu

A `Recommendation` est un CRD natif de Kubernetes créé par le **KubeDB Ops-Manager** et réconcilié par le **Superviseur KubeDB**. Pour une instance MariaDB gérée par KubeDB, Ops-Manager surveille l'état de la base de données et émet une recommandation chaque fois qu'il détecte une action que vous devez entreprendre : une version plus récente, un certificat TLS expirant ou un secret d'authentification proche de sa date limite de rotation.

Rien ne fonctionne tant que la recommandation n'est pas approuvée — soit par vous (`status.approvalStatus: Approved`) ou automatiquement via un `ApprovalPolicy` lié à un `MaintenanceWindow`. Une fois approuvé, le Superviseur crée le `MariaDBOpsRequest` et le suit jusqu'à son achèvement.

Cette page est la **Introduction spécifique à MariaDB**: quelles recommandations s'appliquent à MariaDB et quels champs de spécifications les déclenchent. Pour connaître les conditions préalables, les indicateurs Helm qui contrôlent le timing de génération et le cycle de vie complet de la recommandation, voir :

* [Configuration des recommandations](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/configuration) - les prérequis, l'installation du superviseur CRD et tous les indicateurs Helm.
* [Présentation des recommandations](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation) — présentation pas à pas de l'architecture et du cycle de vie.

![Recommendation Lifecycle](images/recommendation_recommendation_recommendation-generation.png)

---

## Concepts KubeDB associés

* [MariaDBOpsRequest](fr/concepts/opsrequest.md)
* [MariaDBRotateAuth](fr/rotate-auth/overview.md)
* [MariaDBReconfigureTLS](fr/tls/overview.md)
* [MariaDBUpdateVersion](fr/update-version/overview.md)

---

## Types de recommandations pour MariaDB

| Type | Déclenché lorsque | Procédure pas à pas |
| --- | --- | --- |
| **Mise à jour de la version** | Une nouvelle version majeure, mineure ou corrective devient disponible | [Recommandation de mise à jour de version](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/version-update-recommendation) |
| **Mise à jour de la même version** | L'image du conteneur pour votre *actuel* la version est actualisée (par exemple, correctif de sécurité) | [Recommandation de mise à jour de version](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/version-update-recommendation) |
| **Rotation des certificats TLS** | Un certificat émis approche de son seuil d’expiration | [Recommandation de rotation des certificats TLS](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/rotate-tls-recommendation) |
| **Rotation du secret d’authentification** | Le secret d'authentification approche de son terme `rotateAfter` date limite | [Recommandation de rotation des secrets d'authentification](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/rotate-auth-recommendation) |

---

## Déclencheurs spécifiques à MariaDB

Cette section montre les champs minimaux MariaDB CR qui entraînent la génération de chaque recommandation. Pour des procédures pas à pas plus approfondies de bout en bout, utilisez les liens dans le tableau ci-dessus.

### Rotation du secret d’authentification

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
  authSecret:
    kind: Secret
    name: mariadb-auth
    rotateAfter: 1h
```

Dans cette configuration :

* Le `rotateAfter` le champ définit la durée pendant laquelle le secret d'authentification reste valide

KubeDB surveille le cycle de vie configuré et génère une recommandation RotateAuth basée sur les conditions suivantes :

* Si la durée de vie du secret est supérieure à un mois, une recommandation est générée lorsqu'il reste moins d'un mois de validité
* Si la durée de vie du secret est inférieure à un mois, une recommandation est générée lorsqu'il reste environ un tiers de sa validité.

Une fois approuvé, KubeDB crée une requête opérationnelle pour alterner automatiquement les informations d'identification, garantissant :

* Aucun identifiant expiré
* Posture de sécurité amélioré
* Intervention manuelle réduite

### Rotation des certificats TLS

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: mariadb-ca-issuer
    certificates:
      - alias: client
        duration: 1h20m
      - alias: server
        duration: 2h10m
```

Dans cette configuration :

* Le `spec.tls.certificates.duration` le champ définit la durée pendant laquelle chaque certificat reste valide

KubeDB surveille le cycle de vie configuré et génère une recommandation RotateTLS basée sur les conditions suivantes :

* Si la durée du certificat est supérieure à un mois, une recommandation est générée lorsqu'il reste moins d'un mois de validité
* Si la durée du certificat est inférieure à un mois, une recommandation est générée lorsqu'il reste environ un tiers de sa validité.

Une fois approuvé, KubeDB crée une requête opérationnelle pour reconfigurer automatiquement TLS, garantissant :

* Communication sécurisée continue
* Aucune expiration inattendue du certificat
* Renouvellement fluide du certificat

### Mise à jour de la version

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
```

Dans cette configuration :

* KubeDB surveille la version en cours d'exécution de la base de données

KubeDB surveille le cycle de vie configuré et génère une recommandation VersionUpdate basée sur les conditions suivantes :

* Si une image de conteneur plus récente est disponible pour la version actuelle, une recommandation est générée
* Si une version de correctif est publiée, une recommandation est générée
* Si une version mineure ou majeure plus récente devient disponible, une recommandation est générée
* Si des modifications sont introduites dans l'image de version existante (par exemple, des correctifs de sécurité ou des mises à jour d'image sans changement de version), une recommandation est générée

Par exemple : Recommander une mise à jour de version à partir de `10.5.23` à `10.6.16`

Une fois approuvé, KubeDB crée une requête opérationnelle pour effectuer automatiquement la mise à niveau de la version, garantissant :

* Adoption en temps opportun des correctifs et correctifs de sécurité
* Accès aux nouvelles fonctionnalités et améliorations
* Performances et stabilité constantes dans tous les déploiements

### Mise à jour de la même version

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
```

Dans cette configuration :

* KubeDB surveille l'image du conteneur de la version actuelle de la base de données

KubeDB surveille le cycle de vie configuré et génère une recommandation SameVersionUpdate basée sur les conditions suivantes :

* Si l'image du conteneur supportant la version actuelle est mise à jour (par exemple, correctifs de sécurité ou reconstructions sans changement de version), une recommandation est générée

Une fois approuvé, KubeDB crée une requête opérationnelle pour mettre à jour automatiquement la charge de travail en cours d'exécution, garantissant :

* Les correctifs de sécurité sont appliqués sans nécessiter de mise à niveau de version
* Cohérence avec la dernière image de conteneur disponible
* Fiabilité et maintenabilité améliorées

---

Pour connaître les conditions préalables, les indicateurs de configuration Helm et le cycle de vie complet des recommandations inter-bases de données, consultez le [Configuration des recommandations](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/configuration) et [Présentation des recommandations](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation) dans le manuel d'utilisation.

<!-- PAGE_START: reconfigure-tls/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigurer MariaDB TLS/SSL (chiffrement de transport)

KubeDB prend en charge la reconfiguration, c'est-à-dire l'ajout, la suppression, la mise à jour et la rotation des certificats TLS/SSL pour la base de données MariaDB existante via une MariaDBOpsRequest. Ce tutoriel vous montrera comment utiliser KubeDB pour reconfigurer le chiffrement TLS/SSL.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer [`cert-manger`](https://cert-manager.io/docs/installation/) v1.6.0 ou version ultérieure sur votre cluster pour gérer vos certificats SSL/TLS.
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Ajouter TLS à un cluster MariaDB

Ici, nous allons créer une base de données MariaDB sans TLS puis reconfigurer la base de données pour utiliser TLS.

> **Note:** Étapes de reconfiguration de TLS de MariaDB `Standalone` est identique à MariaDB `Cluster`.

### Déployer MariaDB sans TLS

Dans cette section, nous allons déployer une base de données MariaDB Cluster sans TLS. Dans les prochaines sections, nous reconfigurerons TLS en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
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
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    9m17s
```

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d
U6(h_pYrekLZ2OOd

$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb  -- bash
```

```mysql
root@sample-mariadb-0:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 108
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  show variables like '%ssl%';
+---------------------+-----------------------------+
| Variable_name       | Value                       |
+---------------------+-----------------------------+
| have_openssl        | YES                         |
| have_ssl            | DISABLED                    |
| ssl_ca              |                             |
| ssl_capath          |                             |
| ssl_cert            |                             |
| ssl_cipher          |                             |
| ssl_crl             |                             |
| ssl_crlpath         |                             |
| ssl_key             |                             |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020 |
+---------------------+-----------------------------+
10 rows in set (0.001 sec)
```

Nous pouvons vérifier à partir du résultat ci-dessus que TLS est désactivé pour cette base de données.

### Créer un émetteur/clusterIssuer

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
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10//docs/guides/mariadb/reconfigure-tls/cluster/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

### Créer une demande MariaDBOps

Afin d'ajouter TLS à la base de données, nous devons créer un `MariaDBOpsRequest` CRO avec notre émetteur créé. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CRO que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-add-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    requireSSL: true
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
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.issuerRef` spécifie le nom de l'émetteur, le type et le groupe d'API.
* `requireSSL` spécifie que les clients qui se connectent au serveur doivent utiliser une connexion sécurisée.
* `spec.tls.certificates` précise les certificats. Vous pouvez en apprendre davantage sur ce domaine sur [ici](fr/concepts/mariadb.md#spectls).

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-add-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-add-tls created
```

#### Vérifiez que TLS est activé avec succès

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME            TYPE             STATUS       AGE
demo        mdops-add-tls   ReconfigureTLS   Successful   6m6s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi.

Maintenant, nous allons nous connecter à la base de données pour vérifier le `MariaDB` Le serveur a été configuré avec le cryptage TLS/SSL.

Exécutons dans le pod pour vérifier la configuration TLS/SSL,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
```

```bash
root@sample-mariadb-0:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 58
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
10 rows in set (0.005 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.005 sec)

MariaDB [(none)]> quit;
Bye
```

Nous pouvons voir à partir du résultat ci-dessus que, `have_ssl` est réglé sur `ture`. Ainsi, la base de données TLS est activée avec succès sur cette base de données.

> Remarque : Ajoutez ou mettez à jour, reconfigurez TLS avec `RequireSSL=true` créera un temps d'arrêt de la base de données pendant `MariaDBOpsRequest` est dans `Progressing` statut.

## Rotation du certificat

Nous allons maintenant faire tourner le certificat de cette base de données. Vérifions d’abord la date d’expiration actuelle du certificat.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/ openssl x509 -in /etc/mysql/certs/client/tls.crt -inform  PEM -enddate -nameopt RFC2253 -noout
notAfter=Apr 13 05:18:43 2022 GMT
```

Le certificat expirera donc à cette heure `Apr 13 05:18:43 2022 GMT`.

### Créer une demande MariaDBOps

Nous allons maintenant l'augmenter à l'aide d'un MariaDBOpsRequest. Ci-dessous se trouve le yaml de la requête ops que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    rotateCertificates: true
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.rotateCertificates` précise que nous souhaitons faire tourner le certificat de cette base de données.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-rotate-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-rotate-tls created
```

#### Vérifier que la rotation du certificat a réussi

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME               TYPE             STATUS       AGE
demo        mdops-rotate-tls   ReconfigureTLS   Successful    3m
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Vérifions maintenant la date d’expiration du certificat.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/# openssl x509 -in /etc/mysql/certs/client/tls.crt -inform  PEM -enddate -nameopt RFC2253 -noout
notAfter=Apr 13 06:04:50 2022 GMT
```

Comme nous pouvons le voir dans le résultat ci-dessus, la rotation du certificat a réussi.

## Mettre à jour le certificat

Nous allons maintenant mettre à jour le certificat du serveur.

* Décrivons le certificat du serveur `sample-mariadb-server-cert`

```bash
$ kubectl describe certificate -n demo sample-mariadb-server-cert
Name:         sample-mariadb-server-cert
Namespace:    demo
Labels:       app.kubernetes.io/component=database
              app.kubernetes.io/instance=sample-mariadb
              app.kubernetes.io/managed-by=kubedb.com
              app.kubernetes.io/name=mariadbs.kubedb.com
Annotations:  <none>
API Version:  cert-manager.io/v1
Kind:         Certificate
Metadata:
  Creation Timestamp:  2022-01-13T05:18:42Z
  Generation:          1
  ...
  Owner References:
    API Version:           kubedb.com/v1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  MariaDB
    Name:                  sample-mariadb
    UID:                   ed8f45c7-7caf-4890-8a9c-b8437b6ca48b
  Resource Version:        241340
  UID:                     3343e971-395d-46df-9536-47194eb96dcc
Spec:
  Common Name:  sample-mariadb.demo.svc
  Dns Names:
    *.sample-mariadb-pods.demo.svc
    *.sample-mariadb-pods.demo.svc.cluster.local
    *.sample-mariadb.demo.svc
    localhost
    sample-mariadb
    sample-mariadb.demo.svc
  Ip Addresses:
    127.0.0.1
  Issuer Ref:
    Group:      cert-manager.io
    Kind:       Issuer
    Name:       md-issuer
  Secret Name:  sample-mariadb-server-cert
  Subject:
    Organizations:
      kubedb:server
  Usages:
    digital signature
    key encipherment
    server auth
    client auth
Status:
  Conditions:
    Last Transition Time:  2022-01-13T05:18:43Z
    Message:               Certificate is up to date and has not expired
    Observed Generation:   1
    Reason:                Ready
    Status:                True
    Type:                  Ready
  Not After:               2022-04-13T06:04:50Z
  Not Before:              2022-01-13T06:04:50Z
  Renewal Time:            2022-03-14T06:04:50Z
  Revision:                6
Events:
  Type    Reason     Age                From          Message
  ----    ------     ----               ----          -------
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-8tnj5"
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-fw6sk"
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-cvphm"
  Normal  Requested  20m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-nvhp6"
  Normal  Requested  19m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-p5287"
  Normal  Reused     19m (x5 over 22m)  cert-manager  Reusing private key stored in existing Secret resource "sample-mariadb-server-cert"
  Normal  Issuing    19m (x6 over 65m)  cert-manager  The certificate has been successfully issued
```

Nous voulons ajouter `subject` et `emailAddresses` dans les spécifications du certificat de serveur.

### Créer une demande MariaDBOps

Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CRO que nous allons créer pour mettre à jour le certificat du serveur,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-update-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      emailAddresses:
      - "[email protected]"
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.issuerRef` spécifie le nom de l'émetteur, le type et le groupe d'API.
* `spec.tls.certificates` spécifie les modifications que nous souhaitons dans les objets de certificat.
* `spec.tls.certificates[].alias` spécifie le type de certificat qui est l'un des suivants : `server`, `client`, `metrics-exporter`.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-update-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-update-tls created
```

#### Vérifiez que le certificat est mis à jour avec succès

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                  TYPE             STATUS        AGE
mdops-update-tls   ReconfigureTLS     Successful      7m
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi.

Maintenant, exécutons-nous dans un nœud de base de données et découvrons le sujet ca pour voir s'il correspond à celui que nous avons fourni.

```bash
$ kubectl exec -it -n demo sample-mariadb-0  -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/ openssl x509 -in /etc/mysql/certs/server/tls.crt -inform PEM  -subject -email -nameopt RFC2253 -noout
subject=CN=sample-mariadb.demo.svc,O=kubedb:server
[email protected]
```

Nous pouvons voir à partir du résultat ci-dessus que le nom du sujet et l'adresse e-mail correspondent au nouveau certificat ca que nous avons créé. Ainsi, l’émetteur est modifié avec succès.

## Supprimer TLS de la base de données

Maintenant, nous allons supprimer TLS de cette base de données à l'aide d'un MariaDBOpsRequest.

### Créer une demande MariaDBOps

Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CRO que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-remove-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    remove: true
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.remove` précise que nous souhaitons supprimer tls de cette base de données.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-remove-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-remove-tls created
```

#### Vérifiez que TLS a été supprimé avec succès

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME               TYPE             STATUS       AGE
demo        mdops-remove-tls   ReconfigureTLS   Successful   6m27s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies.

Maintenant, entrons dans la base de données et découvrons si TLS est désactivé ou non.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb  -- bash
root@sample-mariadb-0:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 108
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  show variables like '%ssl%';
+---------------------+-----------------------------+
| Variable_name       | Value                       |
+---------------------+-----------------------------+
| have_openssl        | YES                         |
| have_ssl            | DISABLED                    |
| ssl_ca              |                             |
| ssl_capath          |                             |
| ssl_cert            |                             |
| ssl_cipher          |                             |
| ssl_crl             |                             |
| ssl_crlpath         |                             |
| ssl_key             |                             |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020 |
+---------------------+-----------------------------+
10 rows in set (0.001 sec)
```

Ainsi, nous pouvons voir à partir de ce qui précède que la sortie indique que tls est désactivé avec succès.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo --all
$ kubectl delete issuer -n demo --all
$ kubectl delete mariadbopsrequest -n demo --all
$ kubectl delete ns demo
```

<!-- PAGE_START: reconfigure-tls/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Reconfiguration de TLS de la base de données MariaDB

Ce guide donnera un aperçu de la façon dont KubeDB Ops Manager reconfigure la configuration TLS, c'est-à-dire ajouter TLS, supprimer TLS, mettre à jour l'émetteur/émetteur de cluster ou les certificats et faire pivoter les certificats d'un `MariaDB` base de données.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Fonctionnement de la reconfiguration du processus de configuration MariaDB TLS

Le diagramme suivant montre comment KubeDB Ops Manager reconfigure TLS d'un `MariaDB` base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Reconfiguring TLS process of MariaDB](images/reconfigure-tls_overview_reconfigure-tls.jpeg)

Fig : Reconfiguration du processus TLS de MariaDB

Le processus de reconfiguration de MariaDB TLS comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` Objet de ressource personnalisé (CRO).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CRO.
3. Lorsque l'opérateur trouve un `MariaDB` CR, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Ensuite, afin de reconfigurer la configuration TLS du `MariaDB` base de données, l'utilisateur crée un `MariaDBOpsRequest` CR avec les informations souhaitées.
5. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CR.
6. Lorsqu'il trouve un `MariaDBOpsRequest` CR, il met en pause le `MariaDB` objet auquel fait référence le `MariaDBOpsRequest`. Ainsi, le `KubeDB` L’opérateur communautaire n’effectue aucune opération sur le `MariaDB` objet pendant le processus de reconfiguration de TLS.
7. Puis le `KubeDB` L’opérateur d’entreprise ajoutera, supprimera, mettra à jour ou fera pivoter la configuration TLS en fonction du yaml Ops Request.
8. Puis le `KubeDB` L'opérateur Enterprise redémarrera tous les Pods de la base de données afin qu'ils redémarrent avec la nouvelle configuration TLS définie dans le `MariaDBOpsRequest` CR.
9. Après la reconfiguration réussie du `MariaDB` TLS, le `KubeDB` L'opérateur d'entreprise reprend le `MariaDB` objet afin que le `KubeDB` L'opérateur communautaire reprend ses opérations habituelles.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la reconfiguration de la configuration TLS d'une base de données MariaDB à l'aide de `MariaDBOpsRequest` CRD.

<!-- PAGE_START: reconfigure/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigurer la base de données du cluster MariaDB

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour reconfigurer un cluster MariaDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Cluster MariaDB](fr/clustering/galera-cluster.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la reconfiguration](fr/reconfigure/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

Maintenant, nous allons déployer un `MariaDB` Cluster utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBOpsRequest` pour reconfigurer sa configuration.

### Préparer le cluster MariaDB

Maintenant, nous allons déployer un `MariaDB` Base de données de cluster avec version `12.1.2`.

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
  replicas: 3
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
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/sample-mariadb-config.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo 
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    71s
```

Nous allons maintenant vérifier si la base de données a démarré avec la configuration personnalisée que nous avons fournie.

Nous devons d'abord obtenir le nom d'utilisateur et le mot de passe pour nous connecter à une instance mariadb,

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d                                                                       
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d                                                                         
nrKuxni0wDSMrgwy
```

Nous allons maintenant vérifier si la base de données a démarré avec la configuration personnalisée que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
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

* `spec.databaseRef.name` précise que nous sommes en train de reconfigurer `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `Reconfigure` sur notre base de données.
* `spec.configuration.configSecret.name` spécifie le nom du nouveau secret.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/reconfigure-using-secret.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-config created
```

#### Vérifiez que la nouvelle configuration fonctionne

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour le `configuration.secretName` de `MariaDB` objet.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-config   Reconfigure   Successful   3m8s
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
  Creation Timestamp:  2022-06-10T04:43:50Z
  Generation:          1
  Resource Version:  1123451
  UID:               27a73fc6-1d25-4019-8975-f7d4daf782b7
Spec:
  Configuration:
    Config Secret:
      Name:  new-md-configuration
  Database Ref:
    Name:  sample-mariadb
  Type:    Reconfigure
Status:
  Conditions:
    Last Transition Time:  2022-06-10T04:43:50Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-10T04:47:25Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-10T04:47:30Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-10T04:47:30Z
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
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
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
| max_connections | 250   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 122880  |
+------------------+---------+
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
Your MariaDB connection id is 23
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
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/mdops-reconfigure-apply-config.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-apply-config created
```

#### Vérifiez que la nouvelle configuration fonctionne

Si tout se passe bien, `KubeDB` l'opérateur mettra à jour le `configuration.secretName` de `MariaDB` objet.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest mdops-reconfigure-apply-config -n demo
NAME                             TYPE          STATUS       AGE
mdops-reconfigure-apply-config   Reconfigure   Successful   4m59s
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
  Creation Timestamp:  2022-06-10T09:13:49Z
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
    Last Transition Time:  2022-06-10T09:13:49Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-10T09:13:49Z
    Message:               Successfully prepared user provided custom config secret
    Observed Generation:   1
    Reason:                PrepareSecureCustomConfig
    Status:                True
    Type:                  PrepareCustomConfig
    Last Transition Time:  2022-06-10T09:17:24Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-10T09:17:29Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-10T09:17:29Z
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
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
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
| max_connections | 230   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1064960 |
+------------------+---------+
1 row in set (0.001 sec)

# value of `innodb_log_buffer_size` is same as provided
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
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/reconfigure-remove.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-remove created
```

#### Vérifiez que la nouvelle configuration fonctionne

Si tout se passe bien, `KubeDB` l'opérateur mettra à jour le `configuration.secretName` de `MariaDB` objet.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-remove   Reconfigure   Successful   2m1s
```

Connectons-nous maintenant à une instance mariadb et exécutons une commande interne mariadb pour vérifier la nouvelle configuration que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
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

<!-- PAGE_START: reconfigure/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Reconfiguration de MariaDB

Ce guide donnera un aperçu de la façon dont KubeDB Ops Manger reconfigure `MariaDB`.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Comment fonctionne la reconfiguration du processus MariaDB

Le diagramme suivant montre comment KubeDB Ops Manager reconfigure `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Reconfiguring process of MariaDB](images/reconfigure_overview_reconfigure.jpeg)

Fig : Processus de reconfiguration de MariaDB

Le processus de reconfiguration de MariaDB comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` Ressource personnalisée (CR).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CR.
3. Lorsque l'opérateur trouve un `MariaDB` CR, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Ensuite, afin de reconfigurer le `MariaDB` autonome ou en cluster, l'utilisateur crée un `MariaDBOpsRequest` CR avec les informations souhaitées.
5. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CR.
6. Lorsqu'il trouve un `MariaDBOpsRequest` CR, il arrête le `MariaDB` objet auquel fait référence le `MariaDBOpsRequest`. Ainsi, le `KubeDB` L’opérateur communautaire n’effectue aucune opération sur le `MariaDB` objet pendant le processus de reconfiguration.
7. Puis le `KubeDB` L'opérateur d'entreprise remplacera la configuration existante par la nouvelle configuration fournie ou fusionnera la nouvelle configuration avec la configuration existante selon les `MariaDBOpsRequest` CR.
8. Puis le `KubeDB` L'opérateur d'entreprise redémarrera les pods PetSet associés afin qu'ils redémarrent avec la nouvelle configuration définie dans le `MariaDBOpsRequest` CR.
9. Après la reconfiguration réussie du `MariaDB`, le `KubeDB` L'opérateur d'entreprise reprend le `MariaDB` objet afin que le `KubeDB` L'opérateur communautaire reprend ses opérations habituelles.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la reconfiguration des composants de la base de données MariaDB à l'aide de `MariaDBOpsRequest` CRD.

<!-- PAGE_START: reconfigure/standalone.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigurer la base de données autonome MariaDB

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour reconfigurer un MariaDB Standalone.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la reconfiguration](fr/reconfigure/overview.md)

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

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

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

<!-- PAGE_START: restart/restart.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Redémarrer MariaDB

KubeDB prend en charge le redémarrage de la base de données MariaDB via un `MariaDBOpsRequest`. Le redémarrage est utile si certains pods sont bloqués dans une phase ou s'ils ne fonctionnent pas correctement. Ce tutoriel vous montrera comment l'utiliser.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
  namespace/demo created
```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [documents/exemples/MariaDB](https://github.com/kubedb/docs/tree/v2026.7.10/docs/examples/mariadb) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Déployer MariaDB

Dans cette section, nous allons déployer une base de données MariaDB à l'aide de KubeDB.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/restart/MariaDB.yaml
MariaDB.kubedb.com/mariadb created
```

## Appliquer Redémarrer opsRequest

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: restart
  namespace: demo
spec:
  type: Restart
  databaseRef:
    name: mariadb
  timeout: 3m
  apply: Always
```

* `spec.type` spécifie le type de demande d'opérations
* `spec.databaseRef` contient le nom de la base de données MariaDB. La base de données doit être disponible dans le même espace de noms que opsRequest
* Le `spec.timeout` Le champ spécifie la durée maximale pendant laquelle l'opérateur attendra la fin de l'opération avant de la marquer comme ayant échoué.
* Le `spec.apply` Le champ détermine si l'opération doit toujours être appliquée (Always) ou si la phase base de données est prête (IfReady).

> Remarque : La méthode de redémarrage de la base de données en mode autonome et cluster est exactement la même que ci-dessus. Tout ce dont vous avez besoin est de spécifier le nom MariaDB correspondant dans `spec.databaseRef.name` section.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/restart/ops.yaml
MariaDBopsrequest.ops.kubedb.com/restart created
```

Dans `MariaDB`, tous les pods agissent comme des pods principaux, donc l'opérateur Ops-manager redémarrera les pods un par un dans l'ordre.

```shell
$ kubectl get mariaops -n demo restart 
NAME      TYPE      STATUS       AGE
restart   Restart   Successful   3m25s


$ kubectl get mariaops -n demo restart -oyaml
kubectl get mariaops -n demo restart -oyaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"ops.kubedb.com/v1alpha1","kind":"MariaDBOpsRequest","metadata":{"annotations":{},"name":"restart","namespace":"demo"},"spec":{"apply":"Always","databaseRef":{"name":"mariadb"},"timeout":"3m","type":"Restart"}}
  creationTimestamp: "2025-10-14T12:31:09Z"
  generation: 1
  name: restart
  namespace: demo
  resourceVersion: "1004302"
  uid: 4e135330-46c4-41cd-aff6-bf2ddb018911
spec:
  apply: Always
  databaseRef:
    name: mariadb
  timeout: 3m
  type: Restart
status:
  conditions:
  - lastTransitionTime: "2025-10-14T12:31:09Z"
    message: 'Controller has started to Progress the MariaDBOpsRequest: demo/restart'
    observedGeneration: 1
    reason: Running
    status: "True"
    type: Running
  - lastTransitionTime: "2025-10-14T12:31:17Z"
    message: evict pod; ConditionStatus:True; PodName:mariadb-0
    observedGeneration: 1
    status: "True"
    type: EvictPod--mariadb-0
  - lastTransitionTime: "2025-10-14T12:31:17Z"
    message: get pod; ConditionStatus:True; PodName:mariadb-0
    observedGeneration: 1
    status: "True"
    type: GetPod--mariadb-0
  - lastTransitionTime: "2025-10-14T12:32:27Z"
    message: evict pod; ConditionStatus:True; PodName:mariadb-1
    observedGeneration: 1
    status: "True"
    type: EvictPod--mariadb-1
  - lastTransitionTime: "2025-10-14T12:32:27Z"
    message: get pod; ConditionStatus:True; PodName:mariadb-1
    observedGeneration: 1
    status: "True"
    type: GetPod--mariadb-1
  - lastTransitionTime: "2025-10-14T12:33:37Z"
    message: evict pod; ConditionStatus:True; PodName:mariadb-2
    observedGeneration: 1
    status: "True"
    type: EvictPod--mariadb-2
  - lastTransitionTime: "2025-10-14T12:33:37Z"
    message: get pod; ConditionStatus:True; PodName:mariadb-2
    observedGeneration: 1
    status: "True"
    type: GetPod--mariadb-2
  - lastTransitionTime: "2025-10-14T12:34:47Z"
    message: 'Successfully started MariaDB pods for MariaDBOpsRequest: demo/restart '
    observedGeneration: 1
    reason: RestartPodsSucceeded
    status: "True"
    type: Restart
  - lastTransitionTime: "2025-10-14T12:34:47Z"
    message: Controller has successfully restart the MariaDB replicas
    observedGeneration: 1
    reason: Successful
    status: "True"
    type: Successful
  observedGeneration: 1
  phase: Successful
```

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete  mariaops -n demo restart
kubectl delete mariadb -n demo mariadb
kubectl delete ns demo
```

## Prochaines étapes

* En savoir plus sur [sauvegarde et restauration](fr/backup/kubestash/overview.md) Base de données MariaDBQL utilisant Stash.
* En savoir plus sur l'initialisation [MariaDBQL avec script](fr/initialization/using-script.md)
* Concepts détaillés de [Objet MariaDB](fr/concepts/mariadb.md).
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: rotate-auth/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Rotation de l'authentification de MariaDB

Ce guide donnera un aperçu de la configuration de l'authentification par rotation de l'opérateur KubeDB Ops-manager.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Fonctionnement du processus de rotation des identifiants MariaDB

Le processus de rotation d'authentification pour MariaDB à l'aide de KubeDB implique les étapes suivantes :

1. Un utilisateur crée d'abord un `MariaDB` Objet de ressource personnalisé (CRO).
2. Le `KubeDB Provisioner operator` surveille continuellement `MariaDB` CRO.
3. Lorsque l'opérateur détecte un `MariaDB` CR, il prévoit les `PetSets`, ainsi que les ressources associées telles que les secrets, les services et autres dépendances.
4. Pour lancer la rotation d'authentification, l'utilisateur crée un `MariaDBOpsRequest` CR avec la configuration souhaitée.
5. Le `KubeDB Ops-manager` l'opérateur surveille `MariaDBOpsRequest` CR.
6. Lors de la détection d'un `MariaDBOpsRequest`, l'opérateur met en pause l'action référencée `MariaDB` objet, en veillant à ce que le fournisseur
   L’opérateur n’effectue aucune opération pendant le processus de rotation d’authentification.
7. Le `Ops-manager` L'opérateur met ensuite à jour la configuration nécessaire (telle que les informations d'identification) en fonction des informations fournies. `MariaDBOpsRequest` spécification.
8. Après avoir appliqué la configuration mise à jour, l'opérateur redémarre tous `MariaDB` Pods afin qu'ils proposent les nouvelles variables et paramètres d'environnement d'authentification.
9. Une fois la rotation d'authentification terminée avec succès, l'opérateur reprend la `MariaDB` objet, permettant à l’opérateur Provisioner de poursuivre ses opérations habituelles.

Dans la section suivante, nous vous présenterons un guide étape par étape pour faire pivoter l'authentification MariaDB à l'aide de l'outil `MariaDBOpsRequest` CRD.

<!-- PAGE_START: rotate-auth/rotateauth.md -->
# Rotation de l'authentification de MariaDB

**Rotation de l'authentification** est une fonctionnalité de KubeDB Ops-Manager qui vous permet de faire pivoter un `MariaDB` les informations d'authentification de l'utilisateur à l'aide d'un `MariaDBOpsRequest`. Il existe deux manières d'effectuer cette rotation.

1. **Opérateur généré :** L'opérateur KubeDB génère automatiquement un identifiant aléatoire, met à jour le secret existant avec le nouveau identifiant. L'opérateur KubeDB génère automatiquement un identifiant aléatoire et met à jour le secret existant avec le nouveau identifiant.
2. **Défini par l'utilisateur :** L'utilisateur peut créer ses propres identifiants en définissant un Secret de type `kubernetes.io/basic-auth` contenant le souhaité `password` puis faites référence à ce secret dans le `MariaDBOpsRequest`.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/mariadb.md)
* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Créer une base de données MariaDB

KubeDB implémente un `MariaDB` CRD pour définir la spécification d'une base de données MariaDB. Ci-dessous se trouve le `MariaDB` objet créé dans ce tutoriel.

`Note`: Si votre `KubeDB version` est inférieur ou égal à `v2024.6.4`, Vous devez utiliser `v1alpha2` apiVersion.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
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
  deletionPolicy: Delete
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples/sample-mariadb-v1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attendez que sample-mariadb ait le statut Prêt. c'est-à-dire,

```shell
$ kubectl get mariadb -n demo -w
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5   Ready    30m
```

## Vérifier l'authentification

L'utilisateur peut vérifier s'il est autorisé en exécutant une requête directement dans la base de données. Pour ce faire, l'utilisateur a besoin `username` et `password` afin de se connecter à la base de données en utilisant le `kubectl exec` commande. Vous trouverez ci-dessous un exemple montrant comment récupérer les informations d'identification du secret.

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth"
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.username}' | base64 -d
root⏎                                  
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.password}' | base64 -d
s)cJQ*iL8wHySpvT⏎
```

Maintenant, vous pouvez exécuter dans le pod `sample-mariadb` et connectez-vous à la base de données en utilisant `username` et `password`

```shell
$ kubectl exec -it -n demo sample-mariadb-0 -- mariadb -u root --password='s)cJQ*iL8wHySpvT'
Defaulted container "mariadb" out of: mariadb, mariadb-init (init)
```

```mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 207
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.000 sec)

MariaDB [(none)]> CREATE DATABASE Bharatnaityam;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| Bharatnaityam      |
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
+--------------------+
5 rows in set (0.000 sec)
```

Si vous pouvez accéder à la table de données et exécuter des requêtes, cela signifie que les secrets fonctionnent correctement.

## Créer RotateAuth MariaDBOpsRequest

#### 1. Utilisation des informations d'identification générées par l'opérateur :

Afin de faire pivoter l'authentification vers `MariaDB` en utilisant l'opérateur généré, nous devons créer un
CR `MariaDBOpsRequest` de type `RotateAuth`. Vous trouverez ci-dessous le YAML du CR `MariaDBOpsRequest` que nous
allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-auth-generated
  namespace: demo
spec:
  type: RotateAuth
  databaseRef:
    name: sample-mariadb
  timeout: 5m
  apply: IfReady
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération d'authentification par rotation sur
  `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `RotateAuth` sur MariaDB.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```shell
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/rotate-auth/overview/examples/Mariadb-rotate-auth-generated.yaml
 mariadbopsrequest.ops.kubedb.com/mdops-rotate-auth-generated created
```

Attendons `MariaDBOpsrequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsrequest` CRO

```shell
$ kubectl get Mariadbopsrequest -n demo
NAME                          TYPE         STATUS       AGE
mdops-rotate-auth-generated   RotateAuth   Successful   6m28s
```

Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies.

```shell
$ kubectl describe Mariadbopsrequest -n demo mdops-rotate-auth-generated
Name:         mdops-rotate-auth-generated
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-11T06:43:21Z
  Generation:          1
  Resource Version:    635526
  UID:                 fdf5a041-9403-4c0b-a788-2adad326dd88
Spec:
  Apply:  IfReady
  Database Ref:
    Name:   sample-mariadb
  Timeout:  5m
  Type:     RotateAuth
Status:
  Conditions:
    Last Transition Time:  2025-07-11T06:43:21Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-11T06:43:24Z
    Message:               Successfully generated new credentials
    Observed Generation:   1
    Reason:                patchedSecret
    Status:                True
    Type:                  UpdateCredential
    Last Transition Time:  2025-07-11T06:43:32Z
    Message:               evict pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  EvictPod--sample-mariadb-0
    Last Transition Time:  2025-07-11T06:43:32Z
    Message:               get pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  GetPod--sample-mariadb-0
    Last Transition Time:  2025-07-11T06:44:07Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                UpdatePetSetsSucceeded
    Status:                True
    Type:                  UpdatePetSets
    Last Transition Time:  2025-07-11T06:44:12Z
    Message:               Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                UpdateCredential
    Status:                True
    Type:                  RotateAuth
    Last Transition Time:  2025-07-11T06:44:12Z
    Message:               Controller has successfully rotate MariaDB auth secret demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                                                     Age    From                         Message
  ----     ------                                                     ----   ----                         -------
  Normal   Starting                                                   9m17s  KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Starting                                                   9m17s  KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal   Successful                                                 9m17s  KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-rotate-auth-generated
  Normal   Starting                                                   9m6s   KubeDB Ops-manager Operator  Restarting Pod: demo/sample-mariadb-0
  Warning  evict pod; ConditionStatus:True; PodName:sample-mariadb-0  9m6s   KubeDB Ops-manager Operator  evict pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    9m6s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    9m1s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    8m31s  KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Normal   Successful                                                 8m31s  KubeDB Ops-manager Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Starting                                                   8m26s  KubeDB Ops-manager Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Controller has successfully rotate MariaDB auth secret
```

**Vérifiez que l'authentification est pivotée**

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth"
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.username}' | base64 -d
root⏎                                                               
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.password}' | base64 -d
gTJJMdgpKy9U(Eqi⏎
```

En outre, il y aura deux nouvelles clés supplémentaires dans le secret qui stocke les informations d'identification précédentes. Les clés sont `username.prev` et `password.prev`. Vous pouvez trouver le secret et ses données en exécutant la commande suivante :

```shell
$ kubectl get secret -n demo sample-mariadb-auth -o go-template='{{ index .data "username.prev" }}' | base64 -d
root⏎                                                                                                          
$ kubectl get secret -n demo sample-mariadb-auth -o go-template='{{ index .data "password.prev" }}' | base64 -d
s)cJQ*iL8wHySpvT⏎
```

Le résultat ci-dessus montre que le mot de passe a été modifié avec succès. Le nom d'utilisateur et le mot de passe précédents sont stockés à des fins de restauration.

#### 2. Utilisation des informations d'identification créées par l'utilisateur

Dans un premier temps, nous devons créer un secret avec le type kubernetes.io/basic-auth en utilisant un nom d'utilisateur et un mot de passe personnalisés. Vous trouverez ci-dessous la commande pour créer un secret avec le type kubernetes.io/basic-auth,

> Remarque : Vous ne pouvez pas modifier la base de données `username`, mais vous pouvez mettre à jour le `password` tout en gardant l'existant `username`.

```shell
$ kubectl create secret generic sample-mariadb-auth-user -n demo \
   --type=kubernetes.io/basic-auth \
   --from-literal=username=root \
   --from-literal=password=testpassword
secret/sample-mariadb-auth-user created
```

Créez maintenant un CR `MariaDBOpsRequest` de type `RotateAuth`. Vous trouverez ci-dessous le YAML du CR `MariaDBOpsRequest` que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-auth-user
  namespace: demo
spec:
  type: RotateAuth
  databaseRef:
    name: sample-mariadb
  authentication:
    secretRef:
      kind: Secret
      name: sample-mariadb-auth-user
  timeout: 5m
  apply: IfReady
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération d'authentification par rotation sur `sample-mariadb`grappe.
* `spec.type` précise que nous effectuons `RotateAuth` sur `MariaDB`.
* `spec.authentication.secretRef.name` précise que nous utilisons `sample-mariadb-auth-user` comme `spec.authSecret.name` pour l'authentification.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```shell
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/rotate-auth/overview/examples/rotate-auth-user.yaml
mariadbopsrequest.ops.kubedb.com/mdops-rotate-auth-user created
```

Attendons `MariaDBOpsRequest` pour réussir. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO :

```shell
$ kubectl get Mariadbopsrequest -n demo
NAME                          TYPE         STATUS       AGE
mdops-rotate-auth-generated   RotateAuth   Successful   100s
mdops-rotate-auth-user        RotateAuth   Successful   62s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies.

```shell
$  kubectl describe Mariadbopsrequest -n demo mdops-rotate-auth-user
Name:         mdops-rotate-auth-user
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-14T06:56:25Z
  Generation:          1
  Resource Version:    665963
  UID:                 6c30dc56-6ca9-4707-8b7c-5d4da6a1b585
Spec:
  Apply:  IfReady
  Authentication:
    Secret Ref:
      Name:  sample-mariadb-auth-user
  Database Ref:
    Name:   sample-mariadb
  Timeout:  5m
  Type:     RotateAuth
Status:
  Conditions:
    Last Transition Time:  2025-07-14T06:56:25Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-14T06:56:28Z
    Message:               Successfully referenced the user provided authSecret
    Observed Generation:   1
    Reason:                patchedSecret
    Status:                True
    Type:                  UpdateCredential
    Last Transition Time:  2025-07-14T06:56:35Z
    Message:               evict pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  EvictPod--sample-mariadb-0
    Last Transition Time:  2025-07-14T06:56:35Z
    Message:               get pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  GetPod--sample-mariadb-0
    Last Transition Time:  2025-07-14T06:56:40Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                UpdatePetSetsSucceeded
    Status:                True
    Type:                  UpdatePetSets
    Last Transition Time:  2025-07-14T06:56:45Z
    Message:               Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                UpdateCredential
    Status:                True
    Type:                  RotateAuth
    Last Transition Time:  2025-07-14T06:56:45Z
    Message:               Controller has successfully rotate MariaDB auth secret demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                                                     Age   From                         Message
  ----     ------                                                     ----  ----                         -------
  Normal   Starting                                                   83s   KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Starting                                                   83s   KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal   Successful                                                 83s   KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-rotate-auth-user
  Normal   Starting                                                   73s   KubeDB Ops-manager Operator  Restarting Pod: demo/sample-mariadb-0
  Warning  evict pod; ConditionStatus:True; PodName:sample-mariadb-0  73s   KubeDB Ops-manager Operator  evict pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    73s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    68s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Normal   Successful                                                 68s   KubeDB Ops-manager Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Starting                                                   63s   KubeDB Ops-manager Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Controller has successfully rotate MariaDB auth secret
```

**Vérifiez que l'authentification est en rotation**

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth-user"
$ kubectl get secret -n demo sample-mariadb-auth-user -o=jsonpath='{.data.username}' | base64 -d
root⏎                                                                    
$ kubectl get secret -n demo sample-mariadb-auth-user -o=jsonpath='{.data.password}' | base64 -d
testpassword⏎
```

En outre, il y aura deux nouvelles clés supplémentaires dans le secret qui stocke les informations d'identification précédentes. Les clés sont `username.prev` et `password.prev`. Vous pouvez trouver le secret et ses données en exécutant la commande suivante :

```shell
$ kubectl get secret -n demo sample-mariadb-auth-user -o go-template='{{ index .data "username.prev" }}' | base64 -d
root⏎                                                                                                          
$ kubectl get secret -n demo sample-mariadb-auth-user -o go-template='{{ index .data "password.prev" }}' | base64 -d
gTJJMdgpKy9U(Eqi⏎
```

Le résultat ci-dessus montre que le mot de passe a été modifié avec succès. Le nom d'utilisateur et le mot de passe précédents sont stockés dans le secret à des fins de restauration.

## Nettoyage

Pour nettoyer les ressources Kubernetes, vous pouvez supprimer le CRD ou l'espace de noms.
Ou, vous pouvez supprimer une ressource une par une par son nom grâce à ce tutoriel, exécutez :

```shell
$ kubectl delete Mariadbopsrequest mdops-rotate-auth-generated mdops-rotate-auth-user -n demo
mariadbopsrequest.ops.kubedb.com "mdops-rotate-auth-generated" deleted
mariadbopsrequest.ops.kubedb.com "mdops-rotate-auth-user" deleted
$ kubectl delete secret -n demo  sample-mariadb-auth-user
secret "sample-mariadb-auth-user" deleted
$ kubectl delete secret -n demo  sample-mariadb-auth
secret "sample-mariadb-auth" deleted
```

## Prochaines étapes

* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: tls/configure.md -->
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
  Vous pouvez trouver plus de détails sur [ici](fr/concepts/mariadb.md#spectls)

**Déployez MariaDB autonome :**

Créons le `MariaDB` cr nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/tls/configure/examples/tls-standalone.yaml
mariadb.kubedb.com/md-standalone-tls created
```

**Attendez que la base de données soit prête :**

Attendez ensuite que l'objet `MariaDB` passe à l'état `Running` et que son `PetSet` et son pod à créer et à destination `Running` État,

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
```

```mysql
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

La sortie ci-dessus montre que le serveur `MariaDB` est configuré pour TLS/SSL. Vous pouvez également voir que le `.crt` et `.key` les fichiers sont stockés dans `/etc/mysql/certs/client/` et `/etc/mysql/certs/server/` répertoire pour le client et le serveur respectivement.

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

Attendez ensuite que l'objet `MariaDB` passe à l'état `Running` et que son `PetSet` et ses pods à créer et à destination `Running` État,

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
```

```mysql
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
```

```mysql
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

La sortie ci-dessus montre que le serveur `MariaDB` est configuré pour TLS/SSL. Vous pouvez également voir que le `.crt` et `.key` les fichiers sont stockés dans `/etc/mysql/certs/client/` et `/etc/mysql/certs/server/` répertoire pour le client et le serveur respectivement.

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

<!-- PAGE_START: tls/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Cryptage MariaDB TLS/SSL

**Prérequis :** Pour configurer TLS/SSL dans `MariaDB`, `KubeDB` utilise `cert-manager` de délivrer des certificats. Vous devez donc d'abord vous assurer que le cluster a `cert-manager` installé. Pour installer `cert-manager` dans votre cluster, suivez les étapes [ici](https://cert-manager.io/docs/installation/kubernetes/).

Pour délivrer un certificat, le cr suivant de `cert-manager` est utilisé :

* `Issuer/ClusterIssuer`: Les émetteurs et les ClusterIssuers représentent des autorités de certification (CA) capables de générer des certificats signés en honorant les demandes de signature de certificat. Tous les certificats cert-manager nécessitent un émetteur référencé prêt à tenter d'honorer la demande. Vous pouvez en savoir plus [ici](https://cert-manager.io/docs/concepts/issuer/).
* `Certificate`: `cert-manager` a le concept de Certificats qui définissent le certificat x509 souhaité qui sera renouvelé et tenu à jour. Vous pouvez en savoir plus [ici](https://cert-manager.io/docs/concepts/certificate/).

**Spécification MariaDB CRD :**

KubeDB utilise les champs cr suivants pour activer le chiffrement SSL/TLS dans `MariaDB`.

* `spec:`
  + `requireSSL`
  + `tls:`
    - `issuerRef`
    - `certificates`

Découvrez les champs en détail sur [concept mariadb](fr/concepts/mariadb.md#spectls),

Quand, `requireSSL` est défini, les utilisateurs doivent spécifier le `tls.issuerRef` champ. `KubeDB` utilise le `issuer` ou `clusterIssuer` référencé dans le `tls.issuerRef` champ et les spécifications du certificat fournies dans `tls.certificate` pour générer des secrets de certificat à l'aide de `Issuer/ClusterIssuers` spécification. Ces certificats secrets comprennent `ca.crt`, `tls.crt` et `tls.key` etc. sont utilisés pour configurer `MariaDB` serveur, exportateur, etc. respectivement.

## Comment TLS/SSL se configure dans MariaDB

La figure suivante montre comment `KubeDB` Enterprise est utilisé pour configurer TLS/SSL dans MariaDB. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

![Stash Backup Flow](images/tls_overview_md-tls-ssl.png)

Fig : Déployer MariaDB avec TLS/SSL

Le déploiement de MariaDB avec le processus de configuration TLS/SSL comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `Issuer/ClusterIssuer` cr.
2. Ensuite, l'utilisateur crée un `MariaDB` cr.
3. `KubeDB` un opérateur communautaire surveille le `MariaDB` cr.
4. Quand il en trouve un, il crée `Secret`, `Service`, etc. pour le `MariaDB` base de données.
5. `KubeDB` Ops Manager surveille `MariaDB`(5c), `Issuer/ClusterIssuer`(5b), `Secret` et `Service`(5a).
6. Quand il trouve toutes les ressources (`MariaDB`, `Issuer/ClusterIssuer`, `Secret`, `Service`), cela crée `Certificates` en utilisant `tls.issuerRef` et `tls.certificates` spécification de champ de `MariaDB` cr.
7. `cert-manager` surveille les certificats.
8. Lorsqu'il en trouve un, il crée des secrets de certificat `tls-secrets`(secrets du serveur, du client, de l'exportateur, etc.) qui contiennent le véritable certificat auto-signé.
9. `KubeDB` l'opérateur communautaire surveille les secrets du certificat `tls-secrets`.
10. Lorsqu'il trouve tout le secret tls, il crée un `PetSet` afin que le serveur MariaDB soit configuré avec TLS/SSL.

Dans le prochain document, nous allons montrer un guide étape par étape sur la façon de configurer un `MariaDB` base de données avec TLS/SSL.

<!-- PAGE_START: update-version/cluster.md -->
> Vous débutez avec KubeDB ? Commencez [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mettre à jour la version d'un cluster MariaDB

Ce guide montre comment utiliser l'opérateur KubeDB Enterprise pour mettre à jour la version d'un cluster `MariaDB`.

## Avant de commencer

* Vous devez disposer d'un cluster Kubernetes et de l'outil en ligne de commande `kubectl` configuré pour communiquer avec lui. Si vous n'avez pas encore de cluster, créez-en un avec [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Cluster](fr/clustering/overview.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Mise à jour de l'aperçu](fr/update-version/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Préparer le cluster MariaDB

Maintenant, nous allons déployer un `MariaDB` base de données cluster avec version `11.8.5`.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer un cluster MariaDB. Ensuite, dans la section suivante, nous mettrons à jour la version de la base de données en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

> Pour mettre à jour une instance `MariaDB` autonome (`Standalone`), supprimez simplement `spec.replicas` du manifeste YAML ci-dessous ; les autres étapes restent identiques.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
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
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/update-version/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que la ressource `sample-mariadb` atteigne le statut `Ready` :

```bash
$ kubectl get mariadb -n demo                                                                                                                                             
NAME             VERSION    STATUS     AGE
sample-mariadb   11.8.5    Ready     3m15s
```

We are now ready to apply the `MariaDBOpsRequest` CR pour mettre à jour cette base de données.

### mettre à jour la version de MariaDB

Ici, nous allons mettre à jour `MariaDB` cluster de `11.8.5` à `12.1.2`.

#### Créez une demande MariaDBOps :

Afin de mettre à jour le cluster de base de données, nous devons créer un `MariaDBOpsRequest` CR avec la version souhaitée prise en charge par `KubeDB`. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-update
  namespace: demo
spec:
  type: UpdateVersion
  databaseRef:
    name: sample-mariadb
  updateVersion:
    targetVersion: "12.1.2"
```

Ici,

* `spec.databaseRef.name` indique que l'opération porte sur la base de données MariaDB `sample-mariadb`.
* `spec.type` précise que nous allons effectuer `UpdateVersion` sur notre base de données.
* `spec.updateVersion.targetVersion` spécifie la version attendue de la base de données `12.1.2`.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/update-version/cluster/examples/mdops-update.yaml
mariadbopsrequest.ops.kubedb.com/mdops-update created
```

#### Vérifiez la version de MariaDB mise à jour avec succès

Si tout se déroule correctement, l'opérateur KubeDB Enterprise met à jour l'image de l'objet `MariaDB` ainsi que des objets `PetSet` et `Pod` associés.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME              TYPE            STATUS       AGE
mdops-update      UpdateVersion   Successful    84s
```

La sortie ci-dessus confirme que la ressource `MariaDBOpsRequest` a réussi.

Vérifions maintenant que la ressource `MariaDB`, le `PetSet` associé et ses `Pods` utilisent bien l'image de la nouvelle version :

```bash
$ kubectl get mariadb -n demo sample-mariadb -o=jsonpath='{.spec.version}{"\n"}'
12.1.2

$ kubectl get petset -n demo sample-mariadb -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
mariadb:12.1.2

$ kubectl get pods -n demo sample-mariadb-0 -o=jsonpath='{.spec.containers[0].image}{"\n"}'
mariadb:12.1.2
```

La sortie ci-dessus confirme que le cluster `MariaDB` utilise désormais la nouvelle version et que la mise à jour est terminée.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées dans ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-update
```

<!-- PAGE_START: update-version/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# mise à jour de la version de MariaDB

Ce guide vous donnera un aperçu de la façon dont KubeDB Ops Manager met à jour la version de `MariaDB` base de données.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Comment fonctionne le processus de mise à jour de la version

Le diagramme suivant montre comment KubeDB Ops Manager a utilisé pour mettre à jour la version de `MariaDB`. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![updating Process of MariaDB](images/update-version_overview_mdops-update.jpeg)

Fig : processus de mise à jour de MariaDB

Le processus de mise à jour comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` Ressource personnalisée (CR).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CR.
3. Lorsque l'opérateur trouve un `MariaDB` CR, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Ensuite, afin de mettre à jour la version du `MariaDB` base de données, l'utilisateur crée un `MariaDBOpsRequest` CR avec la version souhaitée.
5. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CR.
6. Lorsqu'il trouve un `MariaDBOpsRequest` CR, il arrête le `MariaDB` objet auquel fait référence le `MariaDBOpsRequest`. Ainsi, le `KubeDB` L’opérateur communautaire n’effectue aucune opération sur le `MariaDB` objet pendant le processus de mise à jour.
7. En regardant la version cible de `MariaDBOpsRequest` CR, `KubeDB` L'opérateur d'entreprise met à jour les images de tous les `PetSets`. Après chaque mise à jour d'image, l'opérateur effectue certaines vérifications, par exemple si l'oplog est synchronisé et si la taille de la base de données est presque la même ou non.
8. Après avoir mis à jour avec succès le `PetSets` et leur `Pods` des images, les `KubeDB` L'opérateur d'entreprise met à jour l'image du `MariaDB` objet pour refléter l’état mis à jour de la base de données.
9. Après une mise à jour réussie de `MariaDB` objet, le `KubeDB` L'opérateur d'entreprise reprend le `MariaDB` objet afin que le `KubeDB` L'opérateur communautaire peut reprendre ses opérations habituelles.

Dans le prochain document, nous allons montrer un guide étape par étape sur la mise à jour d'une base de données MariaDB à l'aide de l'opération de mise à jour.

<!-- PAGE_START: volume-expansion/maxscale.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Extension de volume MaxScale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur Ops-manager pour augmenter le volume du serveur MaxScale.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Vous devez avoir un `StorageClass` qui prend en charge l’expansion du volume.
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Réplication MariaDB](fr/clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de l'expansion du volume](fr/volume-expansion/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Augmenter le volume de MaxScale

Ici, nous allons déployer un `MariaDB` cluster en mode réplication à l'aide d'une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBOpsRequest` pour augmenter son volume.

### Préparer la base de données MariaDB

Vérifiez d’abord que votre cluster dispose d’une classe de stockage prenant en charge l’expansion du volume. Vérifions,

```bash
$ kubectl get storageclass
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path             rancher.io/local-path   Delete          WaitForFirstConsumer   false                  46h
standard               driver.standard.io      Delete          Immediate              true                   2m27s
standard-static        driver.standard.io      Delete          Immediate              true                   2m24s
```

Nous pouvons voir sur la sortie que `standard` la classe de stockage a `ALLOWVOLUMEEXPANSION` field as true. Ainsi, cette classe de stockage prend en charge l’expansion du volume. Nous utiliserons cette classe de stockage.

Maintenant, nous allons déployer un `MariaDB` base de données avec `MaxScale` en mode réplication.

### Déployer MariaDB avec MaxScale

Dans cette section, nous allons déployer une base de données MariaDB avec `MaxScale` avec un volume de 50Mi.
Ensuite, dans la section suivante, nous augmenterons son volume à 100 Mi en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-replication
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        storageClassName: "standard"
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
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
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/volume-expansion/md-replication.yaml
mariadb.kubedb.com/md-replication created
```

Attendez maintenant que `md-replication` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
md-replication   11.8.5   Ready    2m30s
```

Vérifions la taille du volume à partir du petset et du volume persistant,

```bash
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"50Mi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                           STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-27e4f4b2-289b-44bb-97a2-729d9420f668   1Gi        RWO            Delete           Bound    demo/data-md-replication-2      standard       <unset>                          3m48s
pvc-2df9a141-5d32-4c92-b0ec-a8043975c2ae   1Gi        RWO            Delete           Bound    demo/data-md-replication-1      standard       <unset>                          3m48s
pvc-7609183e-f9a5-4177-b260-0d24796fb04c   1Gi        RWO            Delete           Bound    demo/data-md-replication-0      standard       <unset>                          3m48s
pvc-96449ed7-305e-4857-a2b6-6eda33c99207   50Mi       RWO            Delete           Bound    demo/data-md-replication-mx-2   standard       <unset>                          3m51s
pvc-c1424029-4a52-4ff4-9888-14d5e7b4fb61   50Mi       RWO            Delete           Bound    demo/data-md-replication-mx-0   standard       <unset>                          3m51s
pvc-d12d301c-58bd-4c59-bd5a-d9167df2b53d   50Mi       RWO            Delete           Bound    demo/data-md-replication-mx-1   standard       <unset>                          3m51s
```

Tu peux voir ça `MaxScale` petset a un stockage de 50Mi et la capacité du `MaxScale` les volumes persistants sont également de 50 Mi.

Nous sommes maintenant prêts à appliquer le `MariaDBOpsRequest` CR pour augmenter le volume de cette base de données.

### Expansion du volume

Ici, nous allons augmenter le volume du `MaxScale` grappe.

#### Créer une demande MariaDBOps

Afin d'augmenter le volume du serveur maxscale, nous devons créer un `MariaDBOpsRequest` CR avec la taille de volume souhaitée. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-volume-expansion
  namespace: demo
spec:
  type: VolumeExpansion
  databaseRef:
    name: md-replication
  volumeExpansion:
    mode: Online
    maxscale: 100Mi
```

Ici,

* `spec.type` précise que nous effectuons `VolumeExpansion` sur notre base de données.
* `spec.databaseRef.name` précise que nous effectuons une opération d'expansion de volume sur `md-replication` base de données.
* `spec.volumeExpansion.mode` spécifie le mode d'expansion du volume souhaité (`Online` ou `Offline`). Classe de stockage `standard` prend en charge `Online` expansion des volumes.
* `spec.volumeExpansion.maxscale` spécifie la taille de volume souhaitée du serveur maxscale.

> **Note:** Si la Storageclass que vous utilisez ne prend pas en charge `Online` Expansion du volume, essayez l'expansion du volume hors ligne en utilisant `spec.volumeExpansion.mode:"Offline"`. Les pods doivent être redémarrés pendant l’expansion du volume hors ligne.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/volume-expansion/maxscale-volume-expansion.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-volume-expansion created
```

#### Vérifiez que le volume MaxScale a été étendu avec succès

Si tout se passe bien, `KubeDB` L'opérateur Ops-manager mettra à jour la taille du volume de `MaxScale` objet et associé `PetSets` et `Persistent Volumes`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                        TYPE              STATUS       AGE
maxscale-volume-expansion   VolumeExpansion   Successful   3m
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour augmenter le volume de la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo maxscale-volume-expansion
Name:         maxscale-volume-expansion
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-23T06:46:12Z
  Generation:          1
  Resource Version:    96939
  UID:                 c33c6a08-2514-4818-932e-f4460bd612a7
Spec:
  Apply:  IfReady
  Database Ref:
    Name:  md-replication
  Type:    VolumeExpansion
  Volume Expansion:
    Maxscale:  100Mi
    Mode:      Online
Status:
  Conditions:
    Last Transition Time:  2025-07-23T06:46:12Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/maxscale-volume-expansion
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-23T06:46:20Z
    Message:               all pvc; ConditionStatus:True
    Observed Generation:   1
    Status:                True
    Type:                  AllPvc
    Last Transition Time:  2025-07-23T06:46:20Z
    Message:               is pvc patch; ConditionStatus:True
    Observed Generation:   1
    Status:                True
    Type:                  IsPvcPatch
    Last Transition Time:  2025-07-23T06:47:10Z
    Message:               delete pvc; ConditionStatus:True
    Observed Generation:   1
    Status:                True
    Type:                  DeletePvc
    Last Transition Time:  2025-07-23T06:47:15Z
    Message:               Online Volume Expansion performed successfully in MaxScale pod for MariaDBOpsRequest: demo/maxscale-volume-expansion
    Observed Generation:   1
    Reason:                VolumeExpansionSucceeded
    Status:                True
    Type:                  VolumeExpansion
    Last Transition Time:  2025-07-23T06:47:15Z
    Message:               Controller has successfully expand the volume of MaxScale: demo/maxscale-volume-expansion
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                              Age   From                         Message
  ----     ------                              ----  ----                         -------
  Normal   Starting                            15m   KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/maxscale-volume-expansion
  Normal   Starting                            15m   KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/md-replication
  Normal   Successful                          15m   KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/md-replication for MariaDBOpsRequest: maxscale-volume-expansion
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  is pvc patch; ConditionStatus:True  15m   KubeDB Ops-manager Operator  is pvc patch; ConditionStatus:True
  Warning  is pvc patch; ConditionStatus:True  15m   KubeDB Ops-manager Operator  is pvc patch; ConditionStatus:True
  Warning  is pvc patch; ConditionStatus:True  15m   KubeDB Ops-manager Operator  is pvc patch; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       14m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  delete pvc; ConditionStatus:True    14m   KubeDB Ops-manager Operator  delete pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       14m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  delete pvc; ConditionStatus:True    14m   KubeDB Ops-manager Operator  delete pvc; ConditionStatus:True
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Online Volume Expansion performed successfully in MaxScale pod for MariaDBOpsRequest: demo/maxscale-volume-expansion
  Normal   Starting                            14m   KubeDB Ops-manager Operator  Updating MaxScale storage
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Successfully updated MaxScale storage
  Normal   Starting                            14m   KubeDB Ops-manager Operator  Resuming MariaDB database: demo/md-replication
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/md-replication
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Controller has Successfully expand the volume of MaxScale: demo/md-replication
```

Maintenant, nous allons vérifier à partir du `Petset`, et le `Persistent Volumes` si le volume de la base de données s'est étendu pour atteindre l'état souhaité, vérifions,

```bash
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"100Mi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                           STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-27e4f4b2-289b-44bb-97a2-729d9420f668   1Gi        RWO            Delete           Bound    demo/data-md-replication-2      standard       <unset>                          34m
pvc-2df9a141-5d32-4c92-b0ec-a8043975c2ae   1Gi        RWO            Delete           Bound    demo/data-md-replication-1      standard       <unset>                          34m
pvc-7609183e-f9a5-4177-b260-0d24796fb04c   1Gi        RWO            Delete           Bound    demo/data-md-replication-0      standard       <unset>                          34m
pvc-96449ed7-305e-4857-a2b6-6eda33c99207   100Mi      RWO            Delete           Bound    demo/data-md-replication-mx-2   standard       <unset>                          34m
pvc-c1424029-4a52-4ff4-9888-14d5e7b4fb61   100Mi      RWO            Delete           Bound    demo/data-md-replication-mx-0   standard       <unset>                          34m
pvc-d12d301c-58bd-4c59-bd5a-d9167df2b53d   100Mi      RWO            Delete           Bound    demo/data-md-replication-mx-1   standard       <unset>                          34m
```

La sortie ci-dessus vérifie que nous avons réussi à augmenter le volume de la base de données MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo md-replication
$ kubectl delete mariadbopsrequest -n demo maxscale-volume-expansion
$ kubectl delete ns demo
```

<!-- PAGE_START: volume-expansion/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Extension du volume MariaDB

Ce guide donnera un aperçu de la façon dont KubeDB Ops Manager augmente le volume de `MariaDB`.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Comment fonctionne le processus d'expansion du volume

Le diagramme suivant montre comment KubeDB Ops Manager augmente les volumes de `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Volume Expansion process of MariaDB](images/volume-expansion_overview_volume-expansion.jpeg)

Fig : Processus d'expansion du volume de MariaDB

Le processus d'expansion du volume comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` Ressource personnalisée (CR).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CR.
3. Lorsque l'opérateur trouve un `MariaDB` CR, il crée requis `PetSet` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Le petSet crée des volumes persistants selon le modèle de réclamation de volume fourni dans la configuration du petset. Ce volume persistant sera étendu par le `KubeDB` Opérateur d'entreprise.
5. Ensuite, afin d'augmenter le volume du `MariaDB` base de données, l'utilisateur crée un `MariaDBOpsRequest` CR avec les informations souhaitées.
6. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CR.
7. Lorsqu'il trouve un `MariaDBOpsRequest` CR, il met en pause le `MariaDB` objet auquel fait référence le `MariaDBOpsRequest`. Ainsi, le `KubeDB` L’opérateur communautaire n’effectue aucune opération sur le `MariaDB` objet pendant le processus d’expansion du volume.
8. Puis le `KubeDB` L'opérateur d'entreprise augmentera le volume persistant pour atteindre la taille attendue définie dans le `MariaDBOpsRequest` CR.
9. Après l'expansion réussie du volume des PetSet Pods associés, le `KubeDB` L'opérateur d'entreprise met à jour la nouvelle taille du volume dans le `MariaDB` objet pour refléter l’état mis à jour.
10. Après l'expansion réussie du volume du `MariaDB`, le `KubeDB` L'opérateur d'entreprise reprend le `MariaDB` objet afin que le `KubeDB` L'opérateur communautaire reprend ses opérations habituelles.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur l'expansion du volume de diverses bases de données MariaDB à l'aide de `MariaDBOpsRequest` CRD.

<!-- PAGE_START: volume-expansion/volume-expansion.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Extension du volume MariaDB

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour augmenter le volume d'une MariaDB.

## Avant de commencer

* Au début, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Vous devez avoir un `StorageClass` qui prend en charge l’expansion du volume.
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de l'expansion du volume](fr/volume-expansion/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Augmenter le volume de MariaDB

Ici, nous allons déployer un `MariaDB` cluster utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBOpsRequest` pour augmenter son volume. Le processus d'expansion de MariaDB `standalone` est identique au cluster MariaDB.

### Préparer la base de données MariaDB

Vérifiez d’abord que votre cluster dispose d’une classe de stockage prenant en charge l’expansion du volume. Vérifions,

```bash
$ kubectl get storageclass
NAME                  PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
longhorn (default)    rancher.io/local-path   Delete          WaitForFirstConsumer   false                  69s
topolvm-provisioner   topolvm.cybozu.com      Delete          WaitForFirstConsumer   true                   37s
```

Nous pouvons voir à partir de la sortie le `topolvm-provisioner` la classe de stockage a `ALLOWVOLUMEEXPANSION` champ comme vrai. Ainsi, cette classe de stockage prend en charge l’expansion du volume. Nous utiliserons cette classe de stockage. Vous pouvez installer topolvm depuis [ici](https://github.com/topolvm/topolvm).

Maintenant, nous allons déployer un `MariaDB` base de données de 3 répliques avec version `12.1.2`.

### Déployer MariaDB

Dans cette section, nous allons déployer un cluster MariaDB avec un volume de 1 Go. Ensuite, dans la section suivante, nous augmenterons son volume à 2 Go en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "topolvm-provisioner"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/volume-expansion/volume-expansion/example/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    5m4s
```

Vérifions la taille du volume à partir du petset et du volume persistant,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1Gi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-331335d1-c8e0-4b73-9dab-dae57920e997   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            63s
pvc-b90179f8-c40a-4273-ad77-74ca8470b782   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            62s
pvc-f72411a4-80d5-4d32-b713-cb30ec662180   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            62s
```

Vous pouvez voir que le petset dispose de 1 Go de stockage et que la capacité de tous les volumes persistants est également de 1 Go.

Nous sommes maintenant prêts à appliquer le `MariaDBOpsRequest` CR pour augmenter le volume de cette base de données.

### Expansion du volume

Ici, nous allons étendre le volume du cluster MariaDB.

#### Créer une demande MariaDBOps

Afin d'augmenter le volume de la base de données, nous devons créer un `MariaDBOpsRequest` CR avec la taille de volume souhaitée. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-online-volume-expansion
  namespace: demo
spec:
  type: VolumeExpansion  
  databaseRef:
    name: sample-mariadb
  volumeExpansion:   
    mode: "Online"
    mariadb: 2Gi
```

Ici,

* `spec.databaseRef.name` précise que nous effectuons une opération d'expansion de volume sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `VolumeExpansion` sur notre base de données.
* `spec.volumeExpansion.mariadb` spécifie la taille de volume souhaitée.
* `spec.volumeExpansion.mode` spécifie le mode d'expansion du volume souhaité (`Online` ou `Offline`). Classe de stockage `topolvm-provisioner` prend en charge `Online` expansion des volumes.

> **Note:** Si la Storageclass que vous utilisez ne prend pas en charge `Online` Expansion du volume, essayez l'expansion du volume hors ligne en utilisant `spec.volumeExpansion.mode:"Offline"`.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/volume-expansion/volume-expansion/example/online-volume-expansion.yaml
mariadbopsrequest.ops.kubedb.com/md-online-volume-expansion created
```

#### Vérifiez que le volume MariaDB a été étendu avec succès

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour la taille du volume de `MariaDB` objet et associé `PetSets` et `Persistent Volumes`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                         TYPE              STATUS       AGE
md-online-volume-expansion   VolumeExpansion   Successful   96s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour augmenter le volume de la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo md-online-volume-expansion
Name:         md-online-volume-expansion
Namespace:    demo
Labels:       <none>
Annotations:  API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  UID:               09a119aa-4f2a-4cb4-b620-2aa3a514df11
Spec:
  Database Ref:
    Name:  sample-mariadb
  Type:    VolumeExpansion
  Volume Expansion:
    Mariadb:  2Gi
    Mode:     Online
Status:
  Conditions:
    Last Transition Time:  2022-01-07T06:38:29Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/md-online-volume-expansion
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-01-07T06:39:49Z
    Message:               Online Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/md-online-volume-expansion
    Observed Generation:   1
    Reason:                SuccessfullyVolumeExpanded
    Status:                True
    Type:                  VolumeExpansion
    Last Transition Time:  2022-01-07T06:39:49Z
    Message:               Controller has successfully expand the volume of MariaDB demo/md-online-volume-expansion
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
Events:
  Type    Reason      Age   From                        Message
  ----    ------      ----  ----                        -------
  Normal  Starting    2m1s  KubeDB Enterprise Operator  Start processing for MariaDBOpsRequest: demo/md-online-volume-expansion
  Normal  Starting    2m1s  KubeDB Enterprise Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal  Successful  2m1s  KubeDB Enterprise Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: md-online-volume-expansion
  Normal  Successful  41s   KubeDB Enterprise Operator  Online Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/md-online-volume-expansion
  Normal  Starting    41s   KubeDB Enterprise Operator  Updating MariaDB storage
  Normal  Successful  41s   KubeDB Enterprise Operator  Successfully Updated MariaDB storage
  Normal  Starting    41s   KubeDB Enterprise Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal  Successful  41s   KubeDB Enterprise Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal  Successful  41s   KubeDB Enterprise Operator  Controller has Successfully expand the volume of MariaDB: demo/sample-mariadb
```

Maintenant, nous allons vérifier à partir du `Petset`, et le `Persistent Volumes` si le volume de la base de données s'est étendu pour atteindre l'état souhaité, vérifions,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"2Gi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-331335d1-c8e0-4b73-9dab-dae57920e997   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            12m
pvc-b90179f8-c40a-4273-ad77-74ca8470b782   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            12m
pvc-f72411a4-80d5-4d32-b713-cb30ec662180   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            12m
```

La sortie ci-dessus vérifie que nous avons réussi à augmenter le volume de la base de données MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo md-online-volume-expansion
```

<!-- PAGE_START: autoscaler/compute/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique de la ressource de calcul d'une base de données de cluster MariaDB

Ce guide vous montrera comment utiliser `KubeDB` pour mettre à l'échelle automatiquement les ressources de calcul, c'est-à-dire le processeur et la mémoire d'une base de données de réplicas MariaDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` Opérateur Community, Ops-Manager et Autoscaler dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `Metrics Server` depuis [ici](https://github.com/kubernetes-sigs/metrics-server#installation)
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle automatique des ressources de calcul](fr/autoscaler/compute/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Mise à l'échelle automatique de la base de données du cluster

Ici, nous allons déployer un `MariaDB` Cluster utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBAutoscaler` pour configurer la mise à l'échelle automatique.

#### Déployer le cluster MariaDB

Dans cette section, nous allons déployer un cluster MariaDB avec la version `12.1.2`. Ensuite, dans la section suivante, nous configurerons la mise à l'échelle automatique pour cette base de données en utilisant `MariaDBAutoscaler` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

> Si vous souhaitez mettre à l'échelle automatiquement MariaDB `Standalone`, Supprimez simplement le `spec.Replicas` à partir du yaml ci-dessous et le reste des étapes sont les mêmes.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            cpu: "200m"
            memory: "300Mi"
          limits:
            cpu: "200m"
            memory: "300Mi"
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CRO que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/compute/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    14m
```

Vérifions les ressources des conteneurs Pod,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

Vérifions les ressources MariaDB,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

Vous pouvez voir à partir des résultats ci-dessus que les ressources sont les mêmes que celles que nous avons attribuées lors du déploiement de mariadb.

Nous sommes maintenant prêts à appliquer le `MariaDBAutoscaler` CRO pour configurer la mise à l'échelle automatique pour cette base de données.

### Mise à l'échelle automatique des ressources de calcul

Ici, nous allons configurer la mise à l'échelle automatique des ressources de calcul à l'aide d'un objet MariaDBAutoscaler.

#### Créer un objet MariaDBAutoscaler

Afin de configurer la mise à l'échelle automatique des ressources de calcul pour ce cluster de bases de données, nous devons créer un `MariaDBAutoscaler` CRO avec notre configuration souhaitée. Vous trouverez ci-dessous le YAML du `MariaDBAutoscaler` objet que nous allons créer,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-compute
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  opsRequestOptions:
    timeout: 3m
    apply: IfReady
  compute:
    mariadb:
      trigger: "On"
      podLifeTimeThreshold: 5m
      resourceDiffPercentage: 20
      minAllowed:
        cpu: 250m
        memory: 400Mi
      maxAllowed:
        cpu: 1
        memory: 1Gi
      containerControlledValues: "RequestsAndLimits"
      controlledResources: ["cpu", "memory"]
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle des ressources de calcul sur `sample-mariadb` base de données.
* `spec.compute.mariadb.trigger` spécifie que la mise à l'échelle automatique du calcul est activée pour cette base de données.
* `spec.compute.mariadb.podLifeTimeThreshold` spécifie la durée de vie minimale d'au moins un des pods pour lancer une mise à l'échelle verticale.
* `spec.compute.mariadb.resourceDiffPercentage` spécifie la différence de ressource minimale en pourcentage. La valeur par défaut est de 10 %.
  Si la différence entre les ressources actuelles et recommandées est inférieure à ResourceDiffPercentage, l’opérateur Autoscaler ignorera la mise à jour.
* `spec.compute.mariadb.minAllowed` spécifie les ressources minimales autorisées pour la base de données.
* `spec.compute.mariadb.maxAllowed` spécifie les ressources maximales autorisées pour la base de données.
* `spec.compute.mariadb.controlledResources` spécifie les ressources contrôlées par l'autoscaler.
* `spec.compute.mariadb.containerControlledValues` spécifie quelles valeurs de ressources doivent être contrôlées. La valeur par défaut est « RequestsAndLimits ».
* `spec.opsRequestOptions.apply` a deux valeurs prises en charge : `IfReady` & `Always`.
  Utiliser `IfReady` si vous souhaitez traiter l'opsReq uniquement lorsque la base de données est prête. Et utiliser `Always` si vous souhaitez traiter l'exécution de opsReq quel que soit l'état de la base de données.
* `spec.opsRequestOptions.timeout` spécifie la durée maximale de chaque étape de opsRequest (en secondes).
  Si une étape ne se termine pas dans le délai spécifié, la requête opérationnelle entraînera un échec.

Créons le `MariaDBAutoscaler` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/compute/cluster/examples/mdas-compute.yaml
mariadbautoscaler.autoscaling.kubedb.com/md-as-compute created
```

#### Vérifiez que l'autoscaling est configuré avec succès

Vérifions que le `mariadbautoscaler` la ressource est créée avec succès,

```bash
$ kubectl get mariadbautoscaler -n demo
NAME            AGE
md-as-compute   5m56s

$ kubectl describe mariadbautoscaler md-as-compute -n demo
Name:         md-as-compute
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-09-16T11:26:58Z
  Generation:          1
  Managed Fields:
    API Version:  autoscaling.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:metadata:
        f:annotations:
          .:
          f:kubectl.kubernetes.io/last-applied-configuration:
      f:spec:
        .:
        f:compute:
          .:
          f:mariadb:
            .:
            f:containerControlledValues:
            f:controlledResources:
            f:maxAllowed:
              .:
              f:cpu:
              f:memory:
            f:minAllowed:
              .:
              f:cpu:
              f:memory:
            f:podLifeTimeThreshold:
            f:resourceDiffPercentage:
            f:trigger:
        f:databaseRef:
          .:
          f:name:
        f:opsRequestOptions:
          .:
          f:apply:
          f:timeout:
    Manager:      kubectl-client-side-apply
    Operation:    Update
    Time:         2022-09-16T11:26:58Z
    API Version:  autoscaling.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:status:
        .:
        f:checkpoints:
        f:conditions:
        f:vpas:
    Manager:         kubedb-autoscaler
    Operation:       Update
    Subresource:     status
    Time:            2022-09-16T11:27:07Z
  Resource Version:  846645
  UID:               44bd46c3-bbc5-4c4a-aff4-00c7f84c6f58
Spec:
  Compute:
    Mariadb:
      Container Controlled Values:  RequestsAndLimits
      Controlled Resources:
        cpu
        memory
      Max Allowed:
        Cpu:     1
        Memory:  1Gi
      Min Allowed:
        Cpu:                     250m
        Memory:                  400Mi
      Pod Life Time Threshold:   5m0s
      Resource Diff Percentage:  20
      Trigger:                   On
  Database Ref:
    Name:  sample-mariadb
  Ops Request Options:
    Apply:    IfReady
    Timeout:  3m0s
Status:
  Checkpoints:
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              46
        Weight:             555
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Bucket Weights:
        Index:              1
        Weight:             10000
      Reference Timestamp:  2022-09-17T00:00:00Z
      Total Weight:         1.391848625060675
    Ref:
      Container Name:     md-coordinator
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              3
        Weight:             556
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Reference Timestamp:  2022-09-17T00:00:00Z
    Ref:
      Container Name:     mariadb
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
  Conditions:
    Last Transition Time:  2022-09-16T11:27:07Z
    Message:               Successfully created mariaDBOpsRequest demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                CreateOpsRequest
    Status:                True
    Type:                  CreateOpsRequest
  Vpas:
    Conditions:
      Last Transition Time:  2022-09-16T11:27:02Z
      Status:                True
      Type:                  RecommendationProvided
    Recommendation:
      Container Recommendations:
        Container Name:  mariadb
        Lower Bound:
          Cpu:     250m
          Memory:  400Mi
        Target:
          Cpu:     250m
          Memory:  400Mi
        Uncapped Target:
          Cpu:     25m
          Memory:  262144k
        Upper Bound:
          Cpu:     1
          Memory:  1Gi
    Vpa Name:      sample-mariadb
Events:            <none>
```

Ainsi, le `mariadbautoscaler` la ressource est créée avec succès.

Nous pouvons vérifier à partir du résultat ci-dessus que `status.vpas` contient le `RecommendationProvided` condition à vrai. Et en même temps, `status.vpas.recommendation.containerRecommendations` contiennent la recommandation réellement générée.

Notre opérateur d'autoscaler surveille en permanence la recommandation générée et crée un `mariadbopsrequest` en fonction des recommandations, si les ressources du pod de base de données doivent être augmentées ou réduites.

Regardons le `mariadbopsrequest` dans l'espace de noms de la démo pour voir s'il y en a `mariadbopsrequest` l'objet est créé. Après un certain temps, vous verrez qu'un `mariadbopsrequest` sera créé sur la base de la recommandation.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                          TYPE              STATUS       AGE
mdops-sample-mariadb-6xc1kc   VerticalScaling   Progressing  7s
```

Attendons que la demande d'opérations aboutisse.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                              TYPE              STATUS       AGE
mdops-vpa-sample-mariadb-z43wc8   VerticalScaling   Successful   3m32s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour faire évoluer la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-vpa-sample-mariadb-z43wc8
Name:         mdops-sample-mariadb-6xc1kc
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-09-16T11:27:07Z
  Generation:          1
  Managed Fields:
    API Version:  ops.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:metadata:
        f:ownerReferences:
          .:
          k:{"uid":"44bd46c3-bbc5-4c4a-aff4-00c7f84c6f58"}:
      f:spec:
        .:
        f:apply:
        f:databaseRef:
          .:
          f:name:
        f:timeout:
        f:type:
        f:verticalScaling:
          .:
          f:mariadb:
            .:
            f:limits:
              .:
              f:cpu:
              f:memory:
            f:requests:
              .:
              f:cpu:
              f:memory:
    Manager:      kubedb-autoscaler
    Operation:    Update
    Time:         2022-09-16T11:27:07Z
    API Version:  ops.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:status:
        .:
        f:conditions:
        f:observedGeneration:
        f:phase:
    Manager:      kubedb-ops-manager
    Operation:    Update
    Subresource:  status
    Time:         2022-09-16T11:27:07Z
  Owner References:
    API Version:           autoscaling.kubedb.com/v1alpha1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  MariaDBAutoscaler
    Name:                  md-as-compute
    UID:                   44bd46c3-bbc5-4c4a-aff4-00c7f84c6f58
  Resource Version:        846324
  UID:                     c2b30107-c6d3-44bb-adf3-135edc5d615b
Spec:
  Apply:  IfReady
  Database Ref:
    Name:   sample-mariadb
  Timeout:  2m0s
  Type:     VerticalScaling
  Vertical Scaling:
    Mariadb:
      Limits:
        Cpu:     250m
        Memory:  400Mi
      Requests:
        Cpu:     250m
        Memory:  400Mi
Status:
  Conditions:
    Last Transition Time:  2022-09-16T11:27:07Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-09-16T11:30:42Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSet
    Last Transition Time:  2022-09-16T11:30:47Z
    Message:               Vertical scale successful for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                SuccessfullyPerformedVerticalScaling
    Status:                True
    Type:                  VerticalScaling
    Last Transition Time:  2022-09-16T11:30:47Z
    Message:               Controller has successfully scaled the MariaDB demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type    Reason      Age    From                        Message
  ----    ------      ----   ----                        -------
  Normal  Starting    8m48s  KubeDB Enterprise Operator  Start processing for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
  Normal  Starting    8m48s  KubeDB Enterprise Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal  Successful  8m48s  KubeDB Enterprise Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-sample-mariadb-6xc1kc
  Normal  Starting    8m43s  KubeDB Enterprise Operator  Restarting Pod: demo/sample-mariadb-0
  Normal  Starting    7m33s  KubeDB Enterprise Operator  Restarting Pod: demo/sample-mariadb-1
  Normal  Starting    6m23s  KubeDB Enterprise Operator  Restarting Pod: demo/sample-mariadb-2
  Normal  Successful  5m13s  KubeDB Enterprise Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
  Normal  Successful  5m8s   KubeDB Enterprise Operator  Vertical scale successful for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
  Normal  Starting    5m8s   KubeDB Enterprise Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal  Successful  5m8s   KubeDB Enterprise Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal  Successful  5m8s   KubeDB Enterprise Operator  Controller has Successfully scaled the MariaDB database: demo/sample-mariadb
```

Maintenant, nous allons vérifier à partir du Pod et du yaml MariaDB si les ressources de la base de données du jeu de réplicas ont été mises à jour pour atteindre l'état souhaité. Vérifions,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}

$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}
```

Le résultat ci-dessus vérifie que nous avons réussi la mise à l'échelle automatique des ressources de la base de données du jeu de réplicas MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadbautoscaler -n demo md-as-compute
kubectl delete ns demo
```

<!-- PAGE_START: autoscaler/compute/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique des ressources de calcul MariaDB

Ce guide donnera un aperçu de la façon dont l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de calcul de la base de données, c'est-à-dire le processeur et la mémoire en utilisant `mariadbautoscaler` crd.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Fonctionnement de la mise à l'échelle automatique du calcul

Le diagramme suivant montre comment l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Auto Scaling process of MariaDB](images/autoscaler_compute_overview_mdas-compute.png)

Fig : Processus de mise à l'échelle automatique de MariaDB

Le processus Auto Scaling comprend les étapes suivantes :

1. Dans un premier temps, l'utilisateur crée un `MariaDB` Objet de ressource personnalisé (CRO).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CRO.
3. Lorsque l'opérateur trouve un `MariaDB` CRO, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Ensuite, afin de configurer l'autoscaling des ressources CPU et mémoire du `MariaDB` base de données, l'utilisateur crée un `MariaDBAutoscaler` CRO avec la configuration souhaitée.
5. `KubeDB` L'opérateur de l'autoscaler surveille le `MariaDBAutoscaler` CRO.
6. `KubeDB` L'opérateur Autoscaler utilise la version modifiée du responsable Kubernetes [Recommandateur APV](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/pkg) pour différents composants de la base de données, comme spécifié dans le `mariadbautoscaler` CRO.
   Il génère des recommandations basées sur l'utilisation des ressources et les stocke dans le `status` section du CRO de l'autoscaler.
7. Si la recommandation générée ne correspond pas aux ressources actuelles de la base de données, alors `KubeDB` L'opérateur Autoscaler crée un `MariaDBOpsRequest` CRO pour mettre à l'échelle la base de données afin qu'elle corresponde à la recommandation fournie par l'objet VPA.
8. `KubeDB Ops-Manager operator` regarde le `MariaDBOpsRequest` CRO.
9. Enfin, le `KubeDB Ops-Manager operator` mettra à l'échelle le composant de base de données verticalement comme spécifié sur le `MariaDBOpsRequest` CRO.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la mise à l'échelle automatique de la base de données MariaDB à l'aide de `MariaDBAutoscaler` CRD.

<!-- PAGE_START: autoscaler/storage/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique du stockage d'un cluster MariaDB

Ce guide vous montrera comment utiliser `KubeDB` pour mettre à l'échelle automatiquement le stockage d'une base de données MariaDB Replicaset.

## Avant de commencer

* Au début, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` Opérateur Community, Enterprise et Autoscaler dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `Metrics Server` depuis [ici](https://github.com/kubernetes-sigs/metrics-server#installation)
* Installez Prometheus à partir de [ici](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
* Vous devez avoir un `StorageClass` qui prend en charge l’expansion du volume.
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle automatique du stockage](fr/autoscaler/storage/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Mise à l'échelle automatique du stockage de la base de données du cluster

Vérifiez d’abord que votre cluster dispose d’une classe de stockage prenant en charge l’expansion du volume. Vérifions,

```bash
$ kubectl get storageclass
NAME                  PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
standard (default)    rancher.io/local-path   Delete          WaitForFirstConsumer   false                  79m
topolvm-provisioner   topolvm.cybozu.com      Delete          WaitForFirstConsumer   true                   78m
```

Nous pouvons voir à partir de la sortie le `topolvm-provisioner` la classe de stockage a `ALLOWVOLUMEEXPANSION` champ comme vrai. Ainsi, cette classe de stockage prend en charge l’expansion du volume. Nous pouvons l'utiliser. Vous pouvez installer topolvm depuis [ici](https://github.com/topolvm/topolvm)

Maintenant, nous allons déployer un `MariaDB` jeu de réplicas utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBAutoscaler` pour configurer la mise à l'échelle automatique.

#### Déployer le cluster MariaDB

Dans cette section, nous allons déployer une base de données de réplicats MariaDB avec la version `12.1.2`. Ensuite, dans la section suivante, nous configurerons la mise à l'échelle automatique pour cette base de données en utilisant `MariaDBAutoscaler` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

> Si vous souhaitez mettre à l'échelle automatiquement MariaDB `Standalone`, Supprimez simplement le `spec.Replicas` à partir du yaml ci-dessous et le reste des étapes sont les mêmes.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "topolvm-provisioner"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CRO que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/storage/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    3m46s
```

Vérifions la taille du volume à partir du petset et du volume persistant,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1Gi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-43266d76-f280-4cca-bd78-d13660a84db9   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            57s
pvc-4a509b05-774b-42d9-b36d-599c9056af37   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            58s
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            57s
```

Vous pouvez voir que le petset dispose de 1 Go de stockage et que la capacité de tout le volume persistant est également de 1 Go.

Nous sommes maintenant prêts à appliquer le `MariaDBAutoscaler` CRO pour configurer la mise à l'échelle automatique du stockage pour cette base de données.

### Mise à l'échelle automatique du stockage

Ici, nous allons configurer la mise à l'échelle automatique du stockage à l'aide d'un objet MariaDBAutoscaler.

#### Créer un objet MariaDBAutoscaler

Afin de configurer la mise à l'échelle automatique verticale pour cette base de données de réplicaset, nous devons créer un `MariaDBAutoscaler` CRO avec notre configuration souhaitée. Vous trouverez ci-dessous le YAML du `MariaDBAutoscaler` objet que nous allons créer,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-st
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  storage:
    mariadb:
      trigger: "On"
      usageThreshold: 20
      scalingThreshold: 20
      expansionMode: "Online"
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle verticale sur `sample-mariadb` base de données.
* `spec.storage.mariadb.trigger` spécifie que la mise à l'échelle automatique du stockage est activée pour cette base de données.
* `spec.storage.mariadb.usageThreshold` spécifie le seuil d'utilisation du stockage, si l'utilisation du stockage dépasse `20%` la mise à l'échelle automatique du stockage sera alors déclenchée.
* `spec.storage.mariadb.scalingThreshold` spécifie le seuil de mise à l'échelle. Le stockage sera adapté à `20%` du montant actuel.
* `spec.storage.mariadb.expansionMode` spécifie le mode d'expansion de l'expansion du volume `MariaDBOpsRequest` créé par `MariaDBAutoscaler`. topolvm-provisioner prend en charge l'expansion du volume en ligne, alors ici `expansionMode` est défini sur « En ligne ».

Créons le `MariaDBAutoscaler` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/storage/cluster/examples/mdas-storage.yaml
mariadbautoscaler.autoscaling.kubedb.com/md-as-st created
```

#### L'autoscaling du stockage est configuré avec succès

Vérifions que le `mariadbautoscaler` la ressource est créée avec succès,

```bash
$ kubectl get mariadbautoscaler -n demo
NAME           AGE
md-as-st   33s

$ kubectl describe mariadbautoscaler md-as-st -n demo
Name:         md-as-st
Namespace:    demo
Labels:       <none>
Annotations:  API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-01-14T06:08:02Z
  Generation:          1
  Managed Fields:
    ...
  Resource Version:  24009
  UID:               4f45a3b3-fc72-4d04-b52c-a770944311f6
Spec:
  Database Ref:
    Name:  sample-mariadb
  Storage:
    Mariadb:
      Scaling Threshold:  20
      Trigger:            On
      Usage Threshold:    20
Events:                   <none>
```

Ainsi, le `mariadbautoscaler` la ressource est créée avec succès.

Maintenant, pour cette démo, nous allons remplir manuellement le volume persistant pour dépasser le `usageThreshold` en utilisant `dd` commande pour voir si la mise à l’échelle automatique du stockage fonctionne ou non.

Exécutons dans le pod de base de données et remplissons le volume de la base de données (`var/lib/mysql`) à l'aide des commandes suivantes :

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  357M  658M  36% /var/lib/mysql
root@sample-mariadb-0:/ dd if=/dev/zero of=/var/lib/mysql/file.img bs=500M count=1
1+0 records in
1+0 records out
524288000 bytes (524 MB, 500 MiB) copied, 0.340877 s, 1.5 GB/s
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  857M  158M  85% /var/lib/mysql
```

Ainsi, à partir du résultat ci-dessus, nous pouvons voir que l'utilisation du stockage est de 83 %, ce qui dépasse le `usageThreshold` 20%.

Regardons le `mariadbopsrequest` dans l'espace de noms de la démo pour voir s'il y en a `mariadbopsrequest` l'objet est créé. Après un certain temps, vous verrez qu'un `mariadbopsrequest` de type `VolumeExpansion` sera créé sur la base de `scalingThreshold`.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                         TYPE              STATUS        AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Progressing   15s
```

Attendons que la demande d'opérations aboutisse.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                         TYPE              STATUS       AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Successful   97s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour augmenter le volume de la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo mops-sample-mariadb-xojkua
Name:         mops-sample-mariadb-xojkua
Namespace:    demo
Labels:       app.kubernetes.io/component=database
              app.kubernetes.io/instance=sample-mariadb
              app.kubernetes.io/managed-by=kubedb.com
              app.kubernetes.io/name=mariadbs.kubedb.com
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-01-14T06:13:10Z
  Generation:          1
  Managed Fields: ...
  Owner References:
    API Version:           autoscaling.kubedb.com/v1alpha1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  MariaDBAutoscaler
    Name:                  md-as-st
    UID:                   4f45a3b3-fc72-4d04-b52c-a770944311f6
  Resource Version:        25557
  UID:                     90763a49-a03f-407c-a233-fb20c4ab57d7
Spec:
  Database Ref:
    Name:  sample-mariadb
  Type:    VolumeExpansion
  Volume Expansion:
    Mariadb:  1594884096
Status:
  Conditions:
    Last Transition Time:  2022-01-14T06:13:10Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-01-14T06:14:25Z
    Message:               Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                SuccessfullyVolumeExpanded
    Status:                True
    Type:                  VolumeExpansion
    Last Transition Time:  2022-01-14T06:14:25Z
    Message:               Controller has successfully expand the volume of MariaDB demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
Events:
  Type    Reason      Age    From                        Message
  ----    ------      ----   ----                        -------
  Normal  Starting    2m58s  KubeDB Enterprise Operator  Start processing for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
  Normal  Starting    2m58s  KubeDB Enterprise Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal  Successful  2m58s  KubeDB Enterprise Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mops-sample-mariadb-xojkua
  Normal  Successful  103s   KubeDB Enterprise Operator  Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
  Normal  Starting    103s   KubeDB Enterprise Operator  Updating MariaDB storage
  Normal  Successful  103s   KubeDB Enterprise Operator  Successfully Updated MariaDB storage
  Normal  Starting    103s   KubeDB Enterprise Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal  Successful  103s   KubeDB Enterprise Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal  Successful  103s   KubeDB Enterprise Operator  Controller has Successfully expand the volume of MariaDB: demo/sample-mariadb
```

Maintenant, nous allons vérifier à partir du `Petset`, et le `Persistent Volume` si le volume de la base de données du jeu de réplicas s'est étendu pour atteindre l'état souhaité, vérifions,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1594884096"
$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-43266d76-f280-4cca-bd78-d13660a84db9   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            23m
pvc-4a509b05-774b-42d9-b36d-599c9056af37   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            24m
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            23m
```

La sortie ci-dessus vérifie que nous avons réussi la mise à l'échelle automatique du volume de la base de données du jeu de réplicas MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadbautoscaler -n demo md-as-st
kubectl delete ns demo
```

<!-- PAGE_START: autoscaler/storage/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle verticale automatique de MariaDB

Ce guide donnera un aperçu de la façon dont l'opérateur KubeDB Autoscaler met automatiquement à l'échelle le stockage de la base de données à l'aide de `mariadbautoscaler` crd.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Fonctionnement de la mise à l'échelle automatique du stockage

Le diagramme suivant montre comment l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Storage Autoscaling process of MariaDB](images/autoscaler_storage_overview_mdas-storage.jpeg)

Fig : Processus de mise à l'échelle automatique du stockage de MariaDB

Le processus Auto Scaling comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` Ressource personnalisée (CR).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CR.
3. Lorsque l'opérateur trouve un `MariaDB` CR, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Chaque PetSet crée un volume persistant selon le modèle de réclamation de volume fourni dans la configuration du petset. Ce volume persistant sera étendu par le `KubeDB` Opérateur d'entreprise.
5. Ensuite, afin de configurer l'autoscaling du stockage du `MariaDB` base de données, l'utilisateur crée un `MariaDBAutoscaler` CRO avec la configuration souhaitée.
6. `KubeDB` L'opérateur de l'autoscaler surveille le `MariaDBAutoscaler` CRO.
7. `KubeDB` L'opérateur Autoscaler surveille en permanence les volumes persistants des bases de données pour vérifier s'ils dépassent le seuil d'utilisation spécifié.
8. Si l'utilisation dépasse le seuil d'utilisation spécifié, alors `KubeDB` L'opérateur Autoscaler crée un `MariaDBOpsRequest` pour étendre le stockage de la base de données.
9. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CRO.
10. Puis le `KubeDB` L'opérateur d'entreprise étendra le stockage du composant de base de données comme spécifié sur le `MariaDBOpsRequest` CRO.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la mise à l'échelle automatique du stockage de divers composants de base de données MariaDB à l'aide de `MariaDBAutoscaler` CRD.

<!-- PAGE_START: backup/kubestash/application-level.md -->
# Sauvegarde et restauration au niveau de l'application de la base de données MariaDB à l'aide de KubeStash

KubeStash offre une fonctionnalité de sauvegarde et de restauration au niveau de l'application pour `MariaDB` bases de données. Il capture à la fois les sauvegardes de manifeste et de données de tout `MariaDB` base de données en un seul instantané. Pendant le processus de restauration, KubeStash applique d'abord le `MariaDB` manifeste au cluster, puis y restaure les données.

Ce guide vous donnera un aperçu de la façon dont vous pouvez effectuer une sauvegarde au niveau de l'application et restaurer votre `MariaDB` bases de données utilisant `Kubestash`.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant `Minikube` ou `Kind`.
* Installer `KubeDB` dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `KubeStash` dans votre cluster en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubestash).
* Installer KubeStash `kubectl` plugin en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont KubeStash sauvegarde et restaure les bases de données MariaDB, veuillez consulter le guide suivant [ici](fr/backup/kubestash/overview.md).

Vous devriez être familier avec ce qui suit `KubeStash` notions :

* [BackupStorage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [BackupConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
* [Session de sauvegarde](https://kubestash.com/docs/latest/concepts/crds/backupsession/)
* [Restaurer la session](https://kubestash.com/docs/latest/concepts/crds/restoresession/)
* [Ajouter sur](https://kubestash.com/docs/latest/concepts/crds/addon/)
* [Fonction](https://kubestash.com/docs/latest/concepts/crds/function/)
* [Tâche](https://kubestash.com/docs/latest/concepts/crds/addon/#task-specification)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

> **Note:** Les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/backup/kubestash/application-level/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples) répertoire de [kubedb/docs](https://github.com/kubedb/docs) dépôt.

## Sauvegarde MariaDB

KubeStash prend en charge les sauvegardes pour `MariaDB` instances dans différentes configurations, y compris les configurations autonomes et Galera Cluster. Dans cette démonstration, nous nous concentrerons sur un `MariaDB` base de données utilisant la configuration du cluster Galera. Le processus de sauvegarde et de restauration est similaire pour la configuration autonome.

Cette section montrera comment effectuer une sauvegarde au niveau de l'application d'un `MariaDB` base de données. Ici, nous allons déployer un `MariaDB` base de données utilisant KubeDB. Ensuite, nous allons sauvegarder la base de données au niveau de l'application sur un `GCS` seau. Enfin, nous restaurerons l'intégralité `MariaDB` base de données.

### Déployer un exemple de base de données MariaDB

Déployons un exemple `MariaDB` base de données et insérez-y des données.

**Créez MariaDB CR :**

Vous trouverez ci-dessous le YAML d'un exemple `MariaDB` CR que nous allons créer pour ce tutoriel :

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créer ce qui précède `MariaDB` CR,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

KubeDB déploiera un `MariaDB` base de données selon la spécification ci-dessus. Cela créera également le nécessaire `Secrets` et `Services` pour accéder à la base de données.

Vérifions si la base de données est prête à être utilisée,

```bash
$ kubectl get md -n demo sample-mariadb
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m1s
```

La base de données est `Ready`. Vérifiez que KubeDB a créé un `Secret` et un `Service` pour cette base de données en utilisant les commandes suivantes,

```bash
$ kubectl get secret -n demo 
NAME                          TYPE                       DATA   AGE
sample-mariadb-auth           kubernetes.io/basic-auth   2      5m49s

$ kubectl get service -n demo -l=app.kubernetes.io/instance=sample-mariadb
NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE
sample-mariadb        ClusterIP   10.128.92.155   <none>        3306/TCP        62s
sample-mariadb-pods   ClusterIP   None            <none>        3306/TCP        62s
```

Ici, nous devons utiliser le service `sample-mariadb` et secret `sample-mariadb-auth` pour se connecter à la base de données. `KubeDB` crée un [Liaison d'application](fr/concepts/appbinding.md) CR qui contient les informations nécessaires pour se connecter à la base de données.

**Vérifiez AppBinding :**

Vérifiez que le `AppBinding` a été créé avec succès à l'aide de la commande suivante,

```bash
$ kubectl get appbindings -n demo
NAME                      TYPE                  VERSION   AGE
sample-mariadb            kubedb.com/mariadb    11.1.3    6m14s
```

Vérifions le YAML de ce qui précède `AppBinding`,

```bash
$ kubectl get appbindings -n demo sample-mariadb -o yaml
```

```yaml
apiVersion: v1
items:
  - apiVersion: appcatalog.appscode.com/v1alpha1
    kind: AppBinding
    metadata:
      annotations:
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"deletionPolicy":"WipeOut","replicas":3,"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}}},"storageType":"Durable","version":"11.1.3"}}          
      creationTimestamp: "2024-09-18T08:31:32Z"
      generation: 1
      labels:
        app.kubernetes.io/component: database
        app.kubernetes.io/instance: sample-mariadb
        app.kubernetes.io/managed-by: kubedb.com
        app.kubernetes.io/name: mariadbs.kubedb.com
      name: sample-mariadb
      namespace: demo
      ownerReferences:
        - apiVersion: kubedb.com/v1
          blockOwnerDeletion: true
          controller: true
          kind: MariaDB
          name: sample-mariadb
          uid: 35400a0b-97b1-4437-a3b9-416678b71adf
      resourceVersion: "1728063"
      uid: 8ebec467-32d5-416a-975a-67e890a4efe6
    spec:
      appRef:
        apiGroup: kubedb.com
        kind: MariaDB
        name: sample-mariadb
        namespace: demo
      clientConfig:
        service:
          name: sample-mariadb
          port: 3306
          scheme: tcp
        url: tcp(sample-mariadb.demo.svc:3306)/
      parameters:
        address: gcomm://sample-mariadb-0.sample-mariadb-pods.demo,sample-mariadb-1.sample-mariadb-pods.demo,sample-mariadb-2.sample-mariadb-pods.demo
        apiVersion: config.kubedb.com/v1alpha1
        group: sample-mariadb
        kind: GaleraArbitratorConfiguration
        sstMethod: xtrabackup-v2
        stash:
          addon:
            backupTask:
              name: mariadb-backup-10.5.8
            restoreTask:
              name: mariadb-restore-10.5.8
      secret:
        name: sample-mariadb-auth
        
        
        
        
      type: kubedb.com/mariadb
      version: 12.1.2
kind: List
metadata:
  resourceVersion: ""
```

KubeStash utilise le `AppBinding` CR pour se connecter à la base de données cible. Il nécessite que les deux champs suivants soient définis dans AppBinding `.spec` section.

Ici,

* `.spec.clientConfig.service.name` spécifie le nom du service qui se connecte à la base de données.
* `.spec.secret` spécifie le nom du secret qui contient les informations d'identification nécessaires pour accéder à la base de données.
* `.spec.type` spécifie les types d’application vers lesquels pointe cet AppBinding. L'AppBinding généré par KubeDB suit le format suivant : `<app group>/<app resource type>`.

**Insérer des exemples de données :**

Maintenant, nous allons exécuter dans l'un des modules de base de données et créer des exemples de données. Dans un premier temps, découvrez la base de données `Pod` en utilisant la commande suivante,

```bash
$ kubectl get pods -n demo --selector="app.kubernetes.io/instance=sample-mariadb" 
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   2/2     Running   0          8m4s
sample-mariadb-1   2/2     Running   0          8m3s
sample-mariadb-2   2/2     Running   0          8m3s
```

Maintenant, exécutons le pod et créons une table,

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');
    
MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

Nous sommes maintenant prêts à sauvegarder la base de données.

### Préparer le back-end

Nous allons stocker nos données de sauvegarde dans un `GCS` seau. Nous devons créer un `Secret` avec les informations d'identification nécessaires et un `BackupStorage` CR pour utiliser ce backend. Si vous souhaitez utiliser un autre backend, veuillez lire le document de configuration du backend correspondant à partir de [ici](https://kubestash.com/docs/latest/guides/backends/overview/).

**Créer un secret :**

Créons un secret appelé `gcs-secret` avec les informations d'identification d'accès à notre compartiment GCS souhaité,

```bash
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat /path/to/downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Créer un stockage de sauvegarde :**

Maintenant, créez un `BackupStorage` en utilisant ce secret. Ci-dessous se trouve le YAML de `BackupStorage` CR que nous allons créer,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: gcs-storage
  namespace: demo
spec:
  storage:
    provider: gcs
    gcs:
      bucket: kubestash-qa
      prefix: demo
      secretName: gcs-secret
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: Delete
```

Créons le BackupStorage que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/backupstorage.yaml
backupstorage.storage.kubestash.com/gcs-storage created
```

Nous sommes maintenant prêts à sauvegarder notre base de données sur le backend souhaité.

**Créer une politique de rétention :**

Maintenant, créons un `RetentionPolicy` pour spécifier comment les anciens instantanés doivent être nettoyés.

Vous trouverez ci-dessous le YAML du `RetentionPolicy` objet que nous allons créer,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: demo-retention
  namespace: demo
spec:
  default: true
  failedSnapshots:
    last: 2
  maxRetentionPeriod: 2mo
  successfulSnapshots:
    last: 5
  usagePolicy:
    allowedNamespaces:
      from: All
```

Créons ce qui précède `RetentionPolicy`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/retentionpolicy.yaml
retentionpolicy.storage.kubestash.com/demo-retention created
```

### Sauvegarde

Nous devons créer un `BackupConfiguration` ciblant respectivement `sample-mariadb` Base de données MariaDB. Ensuite, KubeStash créera un `CronJob` pour chaque session pour effectuer une sauvegarde périodique de cette base de données.

Dans un premier temps, nous devons créer un secret avec un mot de passe Restic pour le cryptage des données de sauvegarde.

**Créer un secret :**

Créons un secret appelé `encrypt-secret` avec le mot de passe Restic,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ kubectl create secret generic -n demo encrypt-secret \
    --from-file=./RESTIC_PASSWORD \
secret "encrypt-secret" created
```

**Créer une configuration de sauvegarde :**

Vous trouverez ci-dessous le YAML pour `BackupConfiguration` CR pour effectuer une sauvegarde au niveau de l'application du `sample-mariadb` base de données que nous avons déployée précédemment,

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: manifest-backup
          - name: logical-backup
```

* `.spec.sessions[*].schedule` précise que nous voulons sauvegarder à `5 minutes` intervalle.
* `.spec.target` fait référence à la cible `sample-mariadb` Base de données MariaDB que nous avons créée précédemment.
* `.spec.sessions[*].addon.tasks[*].name[*]` précise que les deux `manifest-backup` et `logical-backup` les tâches seront exécutées.

Créons le `BackupConfiguration` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/backupconfiguration.yaml
backupconfiguration.core.kubestash.com/sample-mariadb-backup created
```

**Vérifier la configuration de la sauvegarde avec succès**

Si tout se passe bien, la phase du `BackupConfiguration` devrait être `Ready`. Le `Ready` La phase indique que la configuration de la sauvegarde a réussi. Vérifions le `Phase` de la Configuration de Sauvegarde,

```bash
$ kubectl get backupconfiguration -n demo
NAME                     PHASE   PAUSED   AGE
sample-mariadb-backup   Ready            2m50s
```

De plus, nous pouvons vérifier que le `Repository` précisé dans le `BackupConfiguration` a été créé à l'aide de la commande suivante,

```bash
$ kubectl get repo -n demo
NAME                  INTEGRITY   SNAPSHOT-COUNT   SIZE     PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo                 0                0 B      Ready                            3m
```

KubeStash conserve la sauvegarde pour `Repository` YAML. Si nous naviguons vers le compartiment GCS, nous verrons le `Repository` YAML stocké dans le `demo/mariadb` annuaire.

**Vérifiez CronJob :**

Cela créera également un `CronJob` avec l'horaire spécifié dans `spec.sessions[*].scheduler.schedule` domaine de `BackupConfiguration` CR.

Vérifiez que le `CronJob` a été créé à l'aide de la commande suivante,

```bash
$ kubectl get cronjob -n demo
NAME                                             SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
trigger-sample-mariadb-backup-frequent-backup   */5 * * * *             0        2m45s           3m25s
```

**Vérifiez la session de sauvegarde :**

KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Après cela, les sauvegardes sont planifiées selon le calendrier spécifié.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                INVOKER-TYPE          INVOKER-NAME              PHASE       DURATION   AGE
sample-mariadb-backup-frequent-backup-1726651003   BackupConfiguration   sample-mariadb-backup    Succeeded              7m22s
```

Nous pouvons voir à partir du résultat ci-dessus que la session de sauvegarde a réussi. Nous allons maintenant vérifier si les données de sauvegarde ont été stockées dans le backend.

**Vérifier la sauvegarde :**

Une fois la sauvegarde terminée, KubeStash mettra à jour les fichiers respectifs. `Repository` CR pour refléter la sauvegarde. Vérifiez que le référentiel `sample-mariadb-backup` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo gcs-mariadb-repo
NAME                       INTEGRITY   SNAPSHOT-COUNT   SIZE    PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo           true        1                806 B   Ready   8m27s                    9m18s
```

En ce moment nous en avons un `Snapshot`. Exécutez la commande suivante pour vérifier les `Snapshot` qui représente l'état d'une sauvegarde exécutée pour une application.

```bash
$ kubectl get snapshots.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                  REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726651003       gcs-mariadb-repo   frequent-backup   2024-01-23T13:10:54Z   Delete            Succeeded   16h
```

> Remarque : KubeStash crée un `Snapshot` avec les étiquettes suivantes :
>
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> Ces étiquettes peuvent être utilisées pour regarder uniquement `Snapshot`s liés à notre base de données cible ou `Repository`.

Si nous vérifions le YAML du `Snapshot`, nous pouvons trouver les informations sur les composants de sauvegarde de la base de données.

```bash
$ kubectl get snapshots -n demo gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725449400 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T09:16:53Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: gcs-mariadb-repo
  annotations:
    kubedb.com/db-version: 11.1.3
  name: gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726651003
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: gcs-mariadb-repo
      uid: 82a72ef1-1071-49df-b44f-d1f395017262
  resourceVersion: "1734435"
  uid: b96499b6-f882-43e8-ba2a-badb54f96bb8
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: sample-mariadb-backup-frequent-backup-1726651003
  deletionPolicy: Delete
  repository: gcs-mariadb-repo
  session: frequent-backup
  snapshotID: 01J826Q68983K50JRZV2AX1QZF
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.291630733s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 6a9b3e0ccd380f93ff414157156f4ac9d144fa15c5c3adeea2faa09cf44fb175
            size: 3.139 KiB
            uploaded: 3.431 KiB
      size: 1.277 KiB
    manifest:
      driver: Restic
      duration: 2.613551084s
      integrity: true
      path: repository/v1/frequent-backup/manifest
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: /kubestash-tmp/manifest
            id: 47d89d4149cd59bfc8e701b8171a864d0259486820c477a9c2b3a8c0d80de237
            size: 2.507 KiB
            uploaded: 3.939 KiB
      size: 1.913 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T09:16:53Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T09:17:18Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 3.188 KiB
  snapshotTime: "2024-09-18T09:16:53Z"
  totalComponents: 2
```

> KubeStash utilise `mariadb-dump` pour effectuer des sauvegardes de la cible `MariaDB` bases de données. Par conséquent, le nom du composant pour les sauvegardes logiques est défini comme `dump`.

> KubeStash définit le nom du composant comme `manifest` pour le `manifest backup` des bases de données MariaDB.

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons les données de sauvegarde stockées dans le `demo/mariadb/repository/v1/frequent-backup/dump` annuaire. KubeStash conserve également la sauvegarde pour `Snapshot` Les YAML, que l'on peut trouver dans le `demo/mariadb/snapshots` annuaire.

> Remarque : KubeStash stocke toutes les données sauvegardées chiffrées dans le répertoire de sauvegarde, ce qui signifie qu'elles restent illisibles jusqu'à ce qu'elles soient déchiffrées.

## Restaurer

Dans cette section, nous allons restaurer l'intégralité de la base de données à partir de la sauvegarde que nous avons effectuée dans la section précédente.

Pour ce didacticiel, nous restaurerons la base de données dans un espace de noms distinct appelé `dev`.

Tout d'abord, créez l'espace de noms en exécutant la commande suivante :

```bash
$ kubectl create ns dev
namespace/dev created
```

#### Créer une session de restauration :

Nous devons créer un RestoreSession CR.

Ci-dessous, le contenu du fichier YAML du `RestoreSession` CR que nous allons créer pour restaurer l'intégralité de la base de données.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: restore-sample-mariadb
  namespace: demo
spec:
  manifestOptions:
    mariaDB:
      db: true
      restoreNamespace: dev
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
      - name: manifest-restore
```

Ici,

* `.spec.manifestOptions.mariadb.db` spécifie s'il faut restaurer le manifeste de base de données ou non.
* `.spec.dataSource.repository` spécifie l'objet Repository qui contient les données de sauvegarde.
* `.spec.dataSource.snapshot` spécifie de restaurer à partir du dernier `Snapshot`.
* `.spec.addon.tasks[*]` précise que les deux `manifest-restore` et `logical-backup-restore` tâches.

Créons l'objet RestoreSession CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/restoresession.yaml
restoresession.core.kubestash.com/restore-sample-mariadb created
```

Une fois que vous avez créé le `RestoreSession` objet, KubeStash créera une tâche de restauration. Exécutez la commande suivante pour regarder la phase du `RestoreSession` objet,

```bash
$ watch kubectl get restoresession -n demo
Every 2.0s: kubectl get restores... AppsCode-PC-03: Wed Aug 21 10:44:05 2024
NAME                      REPOSITORY            FAILURE-POLICY   PHASE       DURATION   AGE
restore-sample-mariadb   gcs-mariadb-repo                      Succeeded   3s         53s
```

Le `Succeeded` Cette phase signifie que le processus de restauration s'est terminé avec succès.

#### Vérifiez le manifeste MariaDB restauré :

Dans cette section, nous vérifierons si le `MariaDB` Le manifeste de la base de données a été appliqué avec succès au cluster.

```bash
$ kubectl get mariadb -n dev 
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m18s
```

La sortie confirme que le `MariaDB` La base de données a été créée avec succès avec la même configuration qu'au moment de la sauvegarde.

#### Vérifiez les données restaurées :

Dans cette section, nous allons vérifier si les données souhaitées ont été restaurées avec succès. Nous allons nous connecter au serveur de base de données et vérifier si la base de données et la table que nous avons créée précédemment dans la base de données d'origine sont restaurées.

Dans un premier temps, vérifiez si la base de données est entrée dans **`Ready`** énoncer par la commande suivante,

```bash
$ kubectl get mariadb -n dev sample-mariadb
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m18s
```

Maintenant, découvrez la base de données `Pod` par la commande suivante,

```bash
$ kubectl get pods -n dev --selector="app.kubernetes.io/instance=sample-mariadb"
NAME                READY   STATUS    RESTARTS   AGE
sample-mariadb-0   2/2     Running   0          12m
sample-mariadb-1   2/2     Running   0          12m
sample-mariadb-2   2/2     Running   0          12m
```

Maintenant, exécutons l'un des pods et vérifions les données restaurées.

```bash
$ kubectl exec -it -n dev sample-mariadb-0 -- bash
```

```mysql
mysql@restored-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> use hello;

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

Ainsi, à partir du résultat ci-dessus, nous pouvons voir le `hello` base de données que nous avions créée dans la base de données d'origine `sample-mariadb` a été restauré avec succès.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete backupconfigurations.core.kubestash.com  -n demo sample-mariadb-backup
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete restoresessions.core.kubestash.com -n demo restore-sample-mariadb
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadb -n dev sample-mariadb
```

<!-- PAGE_START: backup/kubestash/auto-backup.md -->
# Sauvegarder MariaDB à l'aide de la sauvegarde automatique KubeStash

KubeStash peut être automatiquement configuré pour sauvegarder n'importe quel `MariaDB` bases de données de votre cluster. KubeStash permet aux administrateurs de cluster de déployer des sauvegardes `blueprints` à l'avance afin que les propriétaires de bases de données puissent facilement sauvegarder n'importe quel `MariaDB` base de données avec quelques annotations.

Dans ce didacticiel, nous allons montrer comment configurer un plan de sauvegarde pour `MariaDB` bases de données de votre cluster et sauvegardez-les avec quelques annotations.

## Avant de commencer

* Au début, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant `Minikube` ou `Kind`.
* Installer `KubeDB` dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `KubeStash` dans votre cluster en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubestash).
* Installer KubeStash `kubectl` plugin en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont KubeStash sauvegarde et restaure `MariaDB` bases de données, veuillez consulter le guide suivant [ici](fr/backup/kubestash/overview.md).

Vous devriez être familier avec ce qui suit `KubeStash` notions :

* [BackupStorage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [BackupConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
* [Session de sauvegarde](https://kubestash.com/docs/latest/concepts/crds/backupsession/)
* [Restaurer la session](https://kubestash.com/docs/latest/concepts/crds/restoresession/)
* [Ajouter sur](https://kubestash.com/docs/latest/concepts/crds/addon/)
* [Fonction](https://kubestash.com/docs/latest/concepts/crds/function/)
* [Tâche](https://kubestash.com/docs/latest/concepts/crds/addon/#task-specification)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

> **Note:** Les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/backup/kubestash/auto-backup/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples) répertoire de [kubedb/docs](https://github.com/kubedb/docs) dépôt.

### Préparer le back-end

Nous allons stocker nos données de sauvegarde dans un `GCS` seau. Nous devons créer un `Secret` avec les informations d'identification nécessaires et un `BackupStorage` CR pour utiliser ce backend. Si vous souhaitez utiliser un autre backend, veuillez lire le document de configuration du backend correspondant à partir de [ici](https://kubestash.com/docs/latest/guides/backends/overview/).

**Créer un secret :**

Créons un secret appelé `gcs-secret` avec les informations d'identification d'accès à notre compartiment GCS souhaité,

```bash
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat /path/to/downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Créer un stockage de sauvegarde :**

Maintenant, créez un `BackupStorage` en utilisant ce secret. Ci-dessous se trouve le YAML de `BackupStorage` CR que nous allons créer,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: gcs-storage
  namespace: demo
spec:
  storage:
    provider: gcs
    gcs:
      bucket: kubestash-qa
      prefix: blueprint
      secretName: gcs-secret
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: Delete
```

Créons le BackupStorage que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/backupstorage.yaml
backupstorage.storage.kubestash.com/gcs-storage created
```

Nous sommes maintenant prêts à sauvegarder notre base de données sur le backend souhaité.

**Créer une politique de rétention :**

Maintenant, créons un `RetentionPolicy` pour spécifier comment les anciens instantanés doivent être nettoyés.

Vous trouverez ci-dessous le YAML du `RetentionPolicy` objet que nous allons créer,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: demo-retention
  namespace: demo
spec:
  default: true
  failedSnapshots:
    last: 2
  maxRetentionPeriod: 2mo
  successfulSnapshots:
    last: 5
  usagePolicy:
    allowedNamespaces:
      from: All
```

Créons ce qui précède `RetentionPolicy`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/retentionpolicy.yaml
retentionpolicy.storage.kubestash.com/demo-retention created
```

**Créer un secret :**

Nous devons également créer un secret avec un `Restic` mot de passe pour le cryptage des données de sauvegarde.

Créons un secret appelé `encrypt-secret` avec le mot de passe Restic,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ kubectl create secret generic -n demo encrypt-secret \
    --from-file=./RESTIC_PASSWORD \
secret "encrypt-secret" created
```

## Sauvegarde automatique avec configurations par défaut

Dans cette section, nous allons sauvegarder un `MariaDB` base de données de `demo` espace de noms. Nous allons utiliser les configurations par défaut qui seront précisées dans le `BackupBlueprint` CR.

**Préparer le plan de sauvegarde**

A `BackupBlueprint` vous permet de spécifier un modèle pour le `Repository`,`Session` ou `Variables` de `BackupConfiguration` de manière native Kubernetes.

Maintenant, nous devons créer un `BackupBlueprint` CR avec un plan pour `BackupConfiguration` objet.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupBlueprint
metadata:
  name: mariadb-default-backup-blueprint
  namespace: demo
spec:
  usagePolicy:
    allowedNamespaces:
      from: All
  backupConfigurationTemplate:
    deletionPolicy: OnDelete
    backends:
      - name: gcs-backend
        storageRef:
          namespace: demo
          name: gcs-storage
        retentionPolicy:
          name: demo-retention
          namespace: demo
    sessions:
      - name: frequent-backup
        sessionHistoryLimit: 3
        scheduler:
          schedule: "*/5 * * * *"
          jobTemplate:
            backoffLimit: 1
        repositories:
          - name: default-blueprint
            backend: gcs-backend
            directory: /default-blueprint
            encryptionSecret:
              name: encrypt-secret
              namespace: demo
        addon:
          name: mariadb-addon
          tasks:
            - name: logical-backup
```

Ici,

* `.spec.backupConfigurationTemplate.backends[*].storageRef` fait référence à notre création précédente `gcs-storage` stockage de sauvegarde.
* `.spec.backupConfigurationTemplate.sessions[*].schedule` précise que nous voulons sauvegarder la base de données à `5 minutes` intervalle.

Créons le `BackupBlueprint` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/default-backupblueprint.yaml
backupblueprint.core.kubestash.com/mariadb-default-backup-blueprint created
```

Maintenant, nous sommes prêts à sauvegarder notre `MariaDB` bases de données utilisant peu d’annotations.

**Créer une base de données**

Maintenant, nous allons créer un `MariaDB` CR dans l'espace de noms de démonstration.

Vous trouverez ci-dessous le YAML du `MariaDB` objet que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
  annotations:
    blueprint.kubestash.com/name: mariadb-default-backup-blueprint
    blueprint.kubestash.com/namespace: demo
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Ici,

* `.spec.annotations.blueprint.kubestash.com/name: mariadb-default-backup-blueprint` précise le nom du `BackupBlueprint` qui sera utilisé en sauvegarde.
* `.spec.annotations.blueprint.kubestash.com/namespace: demo` précise le nom du `namespace` où le `BackupBlueprint` réside.

Créons le `MariaDB` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

**Vérifier la configuration de la sauvegarde**

Si tout se passe bien, KubeStash devrait créer un `BackupConfiguration` pour notre MariaDB dans l'espace de noms de démonstration et la phase de celui-ci `BackupConfiguration` devrait être `Ready`. Vérifiez le `BackupConfiguration` objet par la commande suivante,

```bash
$ kubectl get backupconfiguration -n demo
NAME                         PHASE   PAUSED   AGE
appbinding-sample-mariadb   Ready            2m50m
```

Maintenant, vérifions le YAML du `BackupConfiguration`.

```bash
$ kubectl get backupconfiguration -n demo appbinding-sample-mariadb  -o yaml
```

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  creationTimestamp: "2024-09-18T05:34:15Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    app.kubernetes.io/managed-by: kubestash.com
    kubestash.com/invoker-name: mariadb-default-backup-blueprint
    kubestash.com/invoker-namespace: demo
  name: appbinding-sample-mariadb
  namespace: demo
  resourceVersion: "1700384"
  uid: 927ac985-e3d2-43a2-9d25-00ba55ce5fc1
spec:
  backends:
    - name: gcs-backend
      retentionPolicy:
        name: demo-retention
        namespace: demo
      storageRef:
        name: gcs-storage
        namespace: demo
  sessions:
    - addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
      name: frequent-backup
      repositories:
        - backend: gcs-backend
          directory: /default-blueprint
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
          name: default-blueprint
      scheduler:
        jobTemplate:
          backoffLimit: 1
          template:
            controller: {}
            metadata: {}
            spec:
              resources: {}
        schedule: '*/5 * * * *'
      sessionHistoryLimit: 3
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
status:
  backends:
    - name: gcs-backend
      ready: true
      retentionPolicy:
        found: true
        ref:
          name: demo-retention
          namespace: demo
      storage:
        phase: Ready
        ref:
          name: gcs-storage
          namespace: demo
  conditions:
    - lastTransitionTime: "2024-09-18T05:34:17Z"
      message: Validation has been passed successfully.
      reason: ResourceValidationPassed
      status: "True"
      type: ValidationPassed
  dependencies:
    - found: true
      kind: Addon
      name: mariadb-addon
  phase: Ready
  repositories:
    - name: default-blueprint
      phase: Ready
  sessions:
    - conditions:
        - lastTransitionTime: "2024-09-18T05:34:17Z"
          message: Scheduler has been ensured successfully.
          reason: SchedulerEnsured
          status: "True"
          type: SchedulerEnsured
        - lastTransitionTime: "2024-09-18T05:34:18Z"
          message: Initial backup has been triggered successfully.
          reason: SuccessfullyTriggeredInitialBackup
          status: "True"
          type: InitialBackupTriggered
      name: frequent-backup
  targetFound: true
```

Remarquez le `spec.backends`, `spec.sessions` et `spec.target` sections, KubeStash a automatiquement résolu ces informations à partir du `BackupBluePrint` et créé ci-dessus `BackupConfiguration`.

**Vérifiez la session de sauvegarde :**

KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Après cela, les sauvegardes sont planifiées selon le calendrier spécifié.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                    INVOKER-TYPE          INVOKER-NAME                 PHASE       DURATION   AGE
appbinding-sample-mariadb-frequent-backup-1726637655    BackupConfiguration   appbinding-sample-mariadb   Succeeded   2m11s      3m15s
```

Nous pouvons voir à partir du résultat ci-dessus que la session de sauvegarde a réussi. Nous allons maintenant vérifier si les données de sauvegarde ont été stockées dans le backend.

**Vérifier la sauvegarde :**

Une fois la sauvegarde terminée, KubeStash mettra à jour les fichiers respectifs. `Repository` CR pour refléter la sauvegarde. Vérifiez que le référentiel `sample-mariadb-backup` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo default-blueprint
NAME                INTEGRITY   SNAPSHOT-COUNT   SIZE        PHASE   LAST-SUCCESSFUL-BACKUP   AGE
default-blueprint   true        3                1.559 KiB   Ready   80s                      7m32s
```

En ce moment nous en avons un `Snapshot`. Exécutez la commande suivante pour vérifier les `Snapshot` qui représente l'état d'une sauvegarde exécutée pour une application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=default-blueprint
NAME                                                              REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
default-blueprint-appbinding-samiadb-frequent-backup-1726637655   default-blueprint   frequent-backup   2024-09-18T05:34:18Z   Delete            Succeeded   7m39s
```

> Remarque : KubeStash crée un `Snapshot` avec les étiquettes suivantes :
>
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> Ces étiquettes peuvent être utilisées pour regarder uniquement `Snapshot`s liés à notre base de données cible ou `Repository`.

Si nous vérifions le YAML du `Snapshot`, nous pouvons trouver les informations sur les composants de sauvegarde de la base de données.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo default-blueprint-appbinding-samgres-frequent-backup-1725533628 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T05:34:18Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: default-blueprint
  annotations:
    kubedb.com/db-version: 11.1.3
  name: default-blueprint-appbinding-samiadb-frequent-backup-1726637655
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: default-blueprint
      uid: ec1ba99f-ac95-4197-9ddd-0f978053a5d6
  resourceVersion: "1701057"
  uid: fee77218-c06a-43a5-8ad4-fa9baf72a128
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: appbinding-sample-mariadb-frequent-backup-1726637655
  deletionPolicy: Delete
  repository: default-blueprint
  session: frequent-backup
  snapshotID: 01J81SZM8G6AQ5XZAN85CSBP96
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.762583481s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: c4d4c26ad6e03f372b60dfc8bb7901900c4be9b791d44c68564753fb9e9e424c
            size: 2.206 KiB
            uploaded: 2.498 KiB
      size: 2.190 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T05:34:18Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T05:36:26Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 2.189 KiB
  snapshotTime: "2024-09-18T05:34:18Z"
  totalComponents: 1
```

> KubeStash utilise `mariadb-dump` pour effectuer des sauvegardes de la cible `MariaDB` bases de données. Par conséquent, le nom du composant pour les sauvegardes logiques est défini comme `dump`.

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons les données de sauvegarde stockées dans le `blueprint/default-blueprint/repository/v1/frequent-backup/dump` annuaire. KubeStash conserve également la sauvegarde pour `Snapshot` Les YAML, que l'on peut trouver dans le `blueprint/default-blueprint/snapshots` annuaire.

> Remarque : KubeStash stocke toutes les données sauvegardées chiffrées dans le répertoire de sauvegarde, ce qui signifie qu'elles restent illisibles jusqu'à ce qu'elles soient déchiffrées.

## Sauvegarde automatique avec configurations personnalisées

Dans cette section, nous allons sauvegarder un `MariaDB` base de données de `demo` espace de noms. Nous allons utiliser les configurations personnalisées qui seront spécifiées dans le `BackupBlueprint` CR.

**Préparer le plan de sauvegarde**

A `BackupBlueprint` vous permet de spécifier un modèle pour le `Repository`,`Session` ou `Variables` de `BackupConfiguration` de manière native Kubernetes.

Maintenant, nous devons créer un `BackupBlueprint` CR avec un plan pour `BackupConfiguration` objet.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupBlueprint
metadata:
  name: mariadb-customize-backup-blueprint
  namespace: demo
spec:
  usagePolicy:
    allowedNamespaces:
      from: All
  backupConfigurationTemplate:
    deletionPolicy: OnDelete
    backends:
      - name: gcs-backend
        storageRef:
          namespace: demo
          name: gcs-storage
        retentionPolicy:
          name: demo-retention
          namespace: demo
    sessions:
      - name: frequent-backup
        sessionHistoryLimit: 3
        scheduler:
          schedule: ${schedule}
          jobTemplate:
            backoffLimit: 1
        repositories:
          - name: ${repoName}
            backend: gcs-backend
            directory: ${namespace}/${targetName}
            encryptionSecret:
              name: encrypt-secret
              namespace: demo
        addon:
          name: mariadb-addon
          tasks:
            - name: logical-backup
              params:
                args: ${targetedDatabase}
```

Notez que nous avons utilisé quelques variables (format : `${<variable name>}`) dans différents domaines. KubeStash remplacera ces variables par les valeurs des annotations de la cible respective. Vous êtes libre d’utiliser toutes les variables de votre choix.

Ici,

* `.spec.backupConfigurationTemplate.backends[*].storageRef` fait référence à notre création précédente `gcs-storage` stockage de sauvegarde.
* `.spec.backupConfigurationTemplate.sessions[*]`:
  + `.schedule` définit `${schedule}` variable, qui détermine l’intervalle de temps pour la sauvegarde.
  + `.repositories[*].name` définit le `${repoName}` variable, qui spécifie le nom de la sauvegarde `Repository`.
  + `.repositories[*].directory` définit deux variables, `${namespace}` et `${targetName}`, qui sont utilisés pour déterminer le chemin où la sauvegarde sera stockée.
  + `.addon.tasks[*].params.args` définit `${targetedDatabase}` variable, qui identifie une seule base de données à sauvegarder.

Créons le `BackupBlueprint` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/customize-backupblueprint.yaml
backupblueprint.core.kubestash.com/mariadb-customize-backup-blueprint created
```

Maintenant, nous sommes prêts à sauvegarder notre `MariaDB` bases de données utilisant peu d’annotations. Vous pouvez vérifier les annotations de sauvegarde automatique disponibles pour une base de données à partir de [ici](https://kubestash.com/docs/latest/concepts/crds/backupblueprint/).

**Créer une base de données**

Maintenant, nous allons créer un `MariaDB` CR dans l'espace de noms de démonstration.

Vous trouverez ci-dessous le YAML du `MariaDB` objet que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb-2
  namespace: demo
  annotations:
    blueprint.kubestash.com/name: mariadb-customize-backup-blueprint
    blueprint.kubestash.com/namespace: demo
    variables.kubestash.com/schedule: "*/10 * * * *"
    variables.kubestash.com/repoName: customize-blueprint
    variables.kubestash.com/namespace: demo
    variables.kubestash.com/targetName: sample-mariadb-2
    variables.kubestash.com/targetedDatabase: mysql
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Remarquez le `metadata.annotations` champ, où nous avons défini les annotations liées à la configuration de la sauvegarde automatique. Plus précisément, nous avons défini le `BackupBlueprint` nom comme `mariadb-customize-backup-blueprint` et l'espace de noms comme `demo`. Nous avons également fourni des valeurs pour les variables du modèle de plan, telles que la sauvegarde `schedule`, `repositoryName`, `namespace`, `targetName`, et `targetedDatabase`. Ces annotations seront utilisées pour créer un `BackupConfiguration` pour ça `MariaDB` base de données.

Créons le `MariaDB` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/sample-mariadb-2.yaml
mariadb.kubedb.com/sample-mariadb-2 created
```

**Vérifier la configuration de la sauvegarde**

Si tout se passe bien, KubeStash devrait créer un `BackupConfiguration` pour notre MariaDB dans l'espace de noms de démonstration et la phase de celui-ci `BackupConfiguration` devrait être `Ready`. Vérifiez le `BackupConfiguration` objet par la commande suivante,

```bash
$ kubectl get backupconfiguration -n demo
NAME                           PHASE   PAUSED      AGE
appbinding-sample-mariadb-2    Ready               2m50m
```

Maintenant, vérifions le YAML du `BackupConfiguration`.

```bash
$ kubectl get backupconfiguration -n demo appbinding-sample-mariadb-2  -o yaml
```

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  creationTimestamp: "2024-09-18T06:23:21Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    app.kubernetes.io/managed-by: kubestash.com
    kubestash.com/invoker-name: mariadb-customize-backup-blueprint
    kubestash.com/invoker-namespace: demo
  name: appbinding-sample-mariadb-2
  namespace: demo
  resourceVersion: "1709334"
  uid: 08ff19bc-ab81-46c1-9e40-32ff3eb02144
spec:
  backends:
    - name: gcs-backend
      retentionPolicy:
        name: demo-retention
        namespace: demo
      storageRef:
        name: gcs-storage
        namespace: demo
  sessions:
    - addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
            params:
              args: mysql
      name: frequent-backup
      repositories:
        - backend: gcs-backend
          directory: demo/sample-mariadb-2
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
          name: customize-blueprint
      scheduler:
        jobTemplate:
          backoffLimit: 1
          template:
            controller: {}
            metadata: {}
            spec:
              resources: {}
        schedule: '*/10 * * * *'
      sessionHistoryLimit: 3
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb-2
    namespace: demo
status:
  backends:
    - name: gcs-backend
      ready: true
      retentionPolicy:
        found: true
        ref:
          name: demo-retention
          namespace: demo
      storage:
        phase: Ready
        ref:
          name: gcs-storage
          namespace: demo
  conditions:
    - lastTransitionTime: "2024-09-18T06:23:21Z"
      message: Validation has been passed successfully.
      reason: ResourceValidationPassed
      status: "True"
      type: ValidationPassed
  dependencies:
    - found: true
      kind: Addon
      name: mariadb-addon
  phase: Ready
  repositories:
    - name: customize-blueprint
      phase: Ready
  sessions:
    - conditions:
        - lastTransitionTime: "2024-09-18T06:23:23Z"
          message: Scheduler has been ensured successfully.
          reason: SchedulerEnsured
          status: "True"
          type: SchedulerEnsured
        - lastTransitionTime: "2024-09-18T06:23:24Z"
          message: Initial backup has been triggered successfully.
          reason: SuccessfullyTriggeredInitialBackup
          status: "True"
          type: InitialBackupTriggered
      name: frequent-backup
  targetFound: true
```

Remarquez le `spec.backends`, `spec.sessions` et `spec.target` sections, KubeStash a automatiquement résolu ces informations à partir du `BackupBluePrint` et créé ci-dessus `BackupConfiguration`.

**Vérifiez la session de sauvegarde :**

KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Après cela, les sauvegardes sont planifiées selon le calendrier spécifié.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                      INVOKER-TYPE          INVOKER-NAME                   PHASE       DURATION   AGE
appbinding-sample-mariadb-2-frequent-backup-1726640601    BackupConfiguration   appbinding-sample-mariadb-2   Succeeded   2m6s       10m
```

Nous pouvons voir à partir du résultat ci-dessus que la session de sauvegarde a réussi. Nous allons maintenant vérifier si les données de sauvegarde ont été stockées dans le backend.

**Vérifier la sauvegarde :**

Une fois la sauvegarde terminée, KubeStash mettra à jour les fichiers respectifs. `Repository` CR pour refléter la sauvegarde. Vérifiez que le référentiel `customize-blueprint` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo customize-blueprint
NAME                         INTEGRITY   SNAPSHOT-COUNT   SIZE    PHASE   LAST-SUCCESSFUL-BACKUP   AGE
customize-blueprint          true        2                1.021 MiB   Ready   4m29s                    11ms
```

En ce moment nous en avons un `Snapshot`. Exécutez la commande suivante pour vérifier les `Snapshot` qui représente l'état d'une sauvegarde exécutée pour une application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=customize-blueprint
NAME                                                              REPOSITORY            SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
customize-blueprint-appbinding-sdb-2-frequent-backup-1726640601   customize-blueprint   frequent-backup   2024-09-18T06:23:24Z   Delete            Succeeded   12m
```

> Remarque : KubeStash crée un `Snapshot` avec les étiquettes suivantes :
>
> * `kubedb.com/db-version: <db-version>`
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> Ces étiquettes peuvent être utilisées pour regarder uniquement `Snapshot`s liés à notre base de données cible ou `Repository`.

Si nous vérifions le YAML du `Snapshot`, nous pouvons trouver les informations sur les composants de sauvegarde de la base de données.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo customize-blueprint-appbinding-sql-2-frequent-backup-1725597000 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T06:23:24Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb-2
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: customize-blueprint
  annotations:
    kubedb.com/db-version: 11.1.3
  name: customize-blueprint-appbinding-sdb-2-frequent-backup-1726640601
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: customize-blueprint
      uid: 224a1fe8-4897-4de6-b933-fc3537c2a881
  resourceVersion: "1709934"
  uid: e28deec8-a7a4-43ba-b314-b95ef2991a85
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb-2
    namespace: demo
  backupSession: appbinding-sample-mariadb-2-frequent-backup-1726640601
  deletionPolicy: Delete
  repository: customize-blueprint
  session: frequent-backup
  snapshotID: 01J81WSH71CCD611AZ5PTC1N6G
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.836904485s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 6aa144d43ea5d70fd1018390d4d22f98f6ab568c74eee9a386d6a9b29ad21d8b
            size: 4.887 MiB
            uploaded: 4.887 MiB
      size: 907.341 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T06:23:24Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T06:25:27Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 907.341 KiB
  snapshotTime: "2024-09-18T06:23:24Z"
  totalComponents: 1
```

> KubeStash utilise `mariadb-dump` pour effectuer des sauvegardes de la cible `MariaDB` bases de données. Par conséquent, le nom du composant pour les sauvegardes logiques est défini comme `dump`.

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons les données de sauvegarde stockées dans le `blueprint/demo/sample-mariadb-2/repository/v1/frequent-backup/dump` annuaire. KubeStash conserve également la sauvegarde pour `Snapshot` Les YAML, que l'on peut trouver dans le `blueprint/demo/sample-mariadb-2/snapshots` annuaire.

> Remarque : KubeStash stocke toutes les données sauvegardées chiffrées dans le répertoire de sauvegarde, ce qui signifie qu'elles restent illisibles jusqu'à ce qu'elles soient déchiffrées.

## Nettoyage

Pour nettoyer les ressources créées par ce didacticiel, exécutez les commandes suivantes :

```bash
kubectl delete backupblueprints.core.kubestash.com  -n demo mariadb-default-backup-blueprint
kubectl delete backupblueprints.core.kubestash.com  -n demo mariadb-customize-backup-blueprint
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadb -n demo sample-mariadb-2
```

<!-- PAGE_START: backup/kubestash/customization.md -->
# Personnalisation du processus de sauvegarde et de restauration

KubeStash fournit de riches supports de personnalisation pour le processus de sauvegarde et de restauration afin de répondre aux exigences de diverses configurations de cluster. Ce guide vous montrera quelques exemples de ces personnalisations.

## Personnalisation du processus de sauvegarde

Dans cette section, nous allons vous montrer comment personnaliser le processus de sauvegarde. Ici, nous allons montrer quelques exemples de fourniture d'arguments au processus de sauvegarde, d'exécution du processus de sauvegarde en tant qu'utilisateur spécifique, etc.

### Passer des arguments au processus de sauvegarde

Le module complémentaire KubeStash MariaDB utilise le [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) commande par défaut pour les sauvegardes.
L'exemple ci-dessous montre comment vous pouvez transmettre le `--flush-logs` pour vider les fichiers journaux du serveur MariaDB avant de démarrer le vidage.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
            params:
              args: --flush-logs
```

### Passer une base de données cible au processus de sauvegarde

L'exemple ci-dessous montre comment transmettre le nom de la base de données cible lors de la sauvegarde.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
            params:
              args: --databases testdb
```

> **AVERTISSEMENT**: Assurez-vous que la base de données fournie a été créée avant d'effectuer une sauvegarde.

### Utiliser plusieurs backends

Vous pouvez configurer plusieurs backends au sein d'un seul `backupConfiguration`. Pour sauvegarder les mêmes données sur différents backends, tels que S3 et GCS, déclarez chaque backend dans le fichier `.spe.backends` section. Ensuite, référencez ces backends dans le `.spec.sessions[*].repositories` section.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
    - name: s3-backend
      storageRef:
        namespace: demo
        name: s3-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
        - name: s3-mariadb-repo
          backend: s3-backend
          directory: /mariadb-copy
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
```

### Exécution d'une tâche de sauvegarde en tant qu'utilisateur spécifique

Si votre cluster nécessite l'exécution de la tâche de sauvegarde en tant qu'utilisateur spécifique, vous pouvez fournir `securityContext` sous `addon.jobTemplate.spec.securityContext` section. L'exemple ci-dessous montre comment exécuter le travail de sauvegarde en tant que `root` utilisateur.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        jobTemplate:
          spec:
            securityContext:
              runAsUser: 0
              runAsGroup: 0
        tasks:
          - name: logical-backup
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de sauvegarde

Si vous souhaitez spécifier la limite/demande de mémoire/CPU pour votre tâche de sauvegarde, vous pouvez spécifier `resources` champ sous `addon.jobTemplate.spec` section.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        jobTemplate:
          spec:
            resources:
              requests:
                cpu: "200m"
                memory: "1Gi"
              limits:
                cpu: "200m"
                memory: "1Gi"
        tasks:
          - name: logical-backup
```

> Vous pouvez configurer des paramètres d'exécution supplémentaires pour les tâches de sauvegarde dans le `addon.jobTemplate.spec` sections. Pour plus de détails, veuillez vous référer au [référence](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/#podtemplate-spec).

## Personnalisation du processus de restauration

`KubeStash` utilise [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) pendant le processus de restauration. Dans cette section, nous allons montrer comment transmettre des arguments au processus de restauration, restaurer un instantané spécifique, exécuter une tâche de restauration en tant qu'utilisateur spécifique, etc.

### Passer des arguments au processus de restauration

Semblable au processus de sauvegarde, vous pouvez transmettre des arguments au processus de restauration via les paramètres args sous la section addon.tasks[\*].params.

Cet exemple restaurera les données de la base de données testdb uniquement.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
        params:
          args: testdb
```

### Restaurer un instantané spécifique

Vous pouvez également restaurer un instantané spécifique. Dans un premier temps, répertoriez l'instantané disponible comme ci-dessous,

```bash
$ kubectl get snapshots.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                    REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725257849   gcs-mariadb-repo   frequent-backup   2024-09-02T06:18:01Z      Delete            Succeeded   15m
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258000   gcs-mariadb-repo   frequent-backup   2024-09-02T06:20:00Z      Delete            Succeeded   13m
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258300   gcs-mariadb-repo   frequent-backup   2024-09-02T06:25:00Z      Delete            Succeeded   8m34s
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258600   gcs-mariadb-repo   frequent-backup   2024-09-02T06:30:00Z      Delete            Succeeded   3m34s
```

L'exemple ci-dessous montre comment transmettre un nom d'instantané spécifique dans `.spec.dataSource` section.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258000
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
```

### Exécution d'une tâche de restauration en tant qu'utilisateur spécifique

Semblable au processus de sauvegarde sous le `addon.jobTemplate.spec.` vous pouvez fournir `securityContext` pour exécuter le travail de restauration en tant qu'utilisateur spécifique.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    jobTemplate:
      spec:
        securityContext:
          runAsUser: 0
          runAsGroup: 0
    tasks:
      - name: logical-backup-restore
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de restauration

Semblable au processus de sauvegarde, vous pouvez également fournir `resources` champ sous le `addon.jobTemplate.spec.resources` section pour limiter la mémoire/CPU pour votre travail de restauration.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    jobTemplate:
      spec:
        resources:
          requests:
            cpu: "200m"
            memory: "1Gi"
          limits:
            cpu: "200m"
            memory: "1Gi"
    tasks:
      - name: logical-backup-restore
```

> Vous pouvez configurer des paramètres d'exécution supplémentaires pour les tâches de restauration dans le `addon.jobTemplate.spec` sections. Pour plus de détails, veuillez vous référer au [référence](https://kubestash.com/docs/latest/concepts/crds/restoresession/#podtemplate-spec).

<!-- PAGE_START: backup/kubestash/logical.md -->
# Sauvegarder et restaurer la base de données MariaDB à l'aide de KubeStash

KubeStash vous permet de sauvegarder et de restaurer `MariaDB` bases de données. Il prend en charge les sauvegardes pour `MariaDB` instances exécutées dans des configurations de cluster autonomes et Galera. KubeStash facilite la gestion de votre `MariaDB` sauvegardes et restaurations plus simples et efficaces.

Ce guide vous donnera un aperçu de la façon dont vous pouvez effectuer une sauvegarde et restaurer votre `MariaDB` bases de données utilisant `Kubestash`.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant `Minikube` ou `Kind`.
* Installer `KubeDB` dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `KubeStash` dans votre cluster en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubestash).
* Installer KubeStash `kubectl` plugin en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont KubeStash sauvegarde et restaure les bases de données MariaDB, veuillez consulter le guide suivant [ici](fr/backup/kubestash/overview.md).

Vous devriez être familier avec ce qui suit `KubeStash` notions :

* [BackupStorage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [BackupConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
* [Session de sauvegarde](https://kubestash.com/docs/latest/concepts/crds/backupsession/)
* [Restaurer la session](https://kubestash.com/docs/latest/concepts/crds/restoresession/)
* [Ajouter sur](https://kubestash.com/docs/latest/concepts/crds/addon/)
* [Fonction](https://kubestash.com/docs/latest/concepts/crds/function/)
* [Tâche](https://kubestash.com/docs/latest/concepts/crds/addon/#task-specification)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

> **Note:** Les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/backup/kubestash/logical/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples) répertoire de [kubedb/docs](https://github.com/kubedb/docs) dépôt.

## Sauvegarde MariaDB

KubeStash prend en charge les sauvegardes pour `MariaDB` instances dans différentes configurations, y compris les configurations autonomes et Galera Cluster. Dans cette démonstration, nous nous concentrerons sur un `MariaDB` base de données utilisant la configuration du cluster Galera. Le processus de sauvegarde et de restauration est similaire pour la configuration autonome.

Cette section montrera comment sauvegarder un `MariaDB` base de données. Ici, nous allons déployer un `MariaDB` base de données utilisant KubeDB. Ensuite, nous allons sauvegarder cette base de données dans un `GCS` seau. Enfin, nous allons restaurer les données de sauvegarde dans un autre `MariaDB` base de données.

### Déployer un exemple de base de données MariaDB

Déployons un exemple `MariaDB` base de données et insérez-y des données.

**Créez MariaDB CR :**

Vous trouverez ci-dessous le YAML d'un exemple `MariaDB` CR que nous allons créer pour ce tutoriel :

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créer ce qui précède `MariaDB` CR,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

KubeDB déploiera un `MariaDB` base de données selon la spécification ci-dessus. Cela créera également le nécessaire `Secrets` et `Services` pour accéder à la base de données.

Vérifions si la base de données est prête à être utilisée,

```bash
$ kubectl get md -n demo sample-mariadb
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/sample-mariadb   11.1.3    Ready    5m4s
```

La base de données est `Ready`. Vérifiez que KubeDB a créé un `Secret` et un `Service` pour cette base de données en utilisant les commandes suivantes,

```bash
$ kubectl get secret -n demo 
NAME                          TYPE                       DATA   AGE
sample-mariadb-auth           kubernetes.io/basic-auth   2      5m49s

$ kubectl get service -n demo -l=app.kubernetes.io/instance=sample-mariadb
NAME                      TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
sample-mariadb            ClusterIP   10.128.7.155   <none>        3306/TCP                     6m28s
sample-mariadb-pods       ClusterIP   None           <none>        3306/TCP                     6m28s
```

Ici, nous devons utiliser le service `sample-mariadb` et secret `sample-mariadb-auth` pour se connecter à la base de données. `KubeDB` crée un [Liaison d'application](fr/concepts/appbinding.md) CR qui contient les informations nécessaires pour se connecter à la base de données.

**Vérifiez AppBinding :**

Vérifiez que le `AppBinding` a été créé avec succès à l'aide de la commande suivante,

```bash
$ kubectl get appbindings -n demo
NAME                       TYPE                  VERSION   AGE
sample-mariadb             kubedb.com/mariadb    11.1.3    7m56s
```

Vérifions le YAML de ce qui précède `AppBinding`,

```bash
$ kubectl get appbindings -n demo sample-mariadb -o yaml
```

```yaml
apiVersion: appcatalog.appscode.com/v1alpha1
kind: AppBinding
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"deletionPolicy":"WipeOut","replicas":3,"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}}},"storageType":"Durable","version":"11.1.3"}}      
  creationTimestamp: "2024-09-17T10:07:37Z"
  generation: 1
  labels:
    app.kubernetes.io/component: database
    app.kubernetes.io/instance: sample-mariadb
    app.kubernetes.io/managed-by: kubedb.com
    app.kubernetes.io/name: mariadbs.kubedb.com
  name: sample-mariadb
  namespace: demo
  ownerReferences:
    - apiVersion: kubedb.com/v1
      blockOwnerDeletion: true
      controller: true
      kind: MariaDB
      name: sample-mariadb
      uid: c19117ca-582b-4d6c-90e5-ac80d5cf95b9
  resourceVersion: "1561857"
  uid: fd3868ef-f54b-4cc9-87b0-4986d9a8aaf0
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  clientConfig:
    service:
      name: sample-mariadb
      port: 3306
      scheme: tcp
    url: tcp(sample-mariadb.demo.svc:3306)/
  parameters:
    address: gcomm://sample-mariadb-0.sample-mariadb-pods.demo,sample-mariadb-1.sample-mariadb-pods.demo,sample-mariadb-2.sample-mariadb-pods.demo
    apiVersion: config.kubedb.com/v1alpha1
    group: sample-mariadb
    kind: GaleraArbitratorConfiguration
    sstMethod: xtrabackup-v2
    stash:
      addon:
        backupTask:
          name: mariadb-backup-10.5.8
        restoreTask:
          name: mariadb-restore-10.5.8
  secret:
    name: sample-mariadb-auth
  type: kubedb.com/mariadb
  version: 12.1.2
```

KubeStash utilise le `AppBinding` CR pour se connecter à la base de données cible. Il nécessite que les deux champs suivants soient définis dans AppBinding `.spec` section.

Ici,

* `.spec.clientConfig.service.name` spécifie le nom du service qui se connecte à la base de données.
* `.spec.secret` spécifie le nom du secret qui contient les informations d'identification nécessaires pour accéder à la base de données.
* `.spec.type` spécifie les types d’application vers lesquels pointe cet AppBinding. L'AppBinding généré par KubeDB suit le format suivant : `<app group>/<app resource type>`.

**Insérer des exemples de données :**

Maintenant, nous allons exécuter dans l'un des modules de base de données et créer des exemples de données. Dans un premier temps, découvrez la base de données `Pod` en utilisant la commande suivante,

```bash
$ kubectl get pods -n demo --selector="app.kubernetes.io/instance=sample-mariadb" 
NAME                READY   STATUS    RESTARTS   AGE
sample-mariadb-0    2/2     Running   0          10m
sample-mariadb-1    2/2     Running   0          10m
sample-mariadb-2    2/2     Running   0          10m
```

Maintenant, exécutons le pod et créons une table,

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');
    
MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

Nous sommes maintenant prêts à sauvegarder la base de données.

### Préparer le back-end

Nous allons stocker nos données de sauvegarde dans un `GCS` seau. Nous devons créer un `Secret` avec les informations d'identification nécessaires et un `BackupStorage` CR pour utiliser ce backend. Si vous souhaitez utiliser un autre backend, veuillez lire le document de configuration du backend correspondant à partir de [ici](https://kubestash.com/docs/latest/guides/backends/overview/).

**Créer un secret :**

Créons un secret appelé `gcs-secret` avec les informations d'identification d'accès à notre compartiment GCS souhaité,

```bash
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat /path/to/downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Créer un stockage de sauvegarde :**

Maintenant, créez un `BackupStorage` en utilisant ce secret. Ci-dessous se trouve le YAML de `BackupStorage` CR que nous allons créer,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: gcs-storage
  namespace: demo
spec:
  storage:
    provider: gcs
    gcs:
      bucket: kubestash-qa
      prefix: demo
      secretName: gcs-secret
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: Delete
```

Créons le BackupStorage que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/backupstorage.yaml
backupstorage.storage.kubestash.com/gcs-storage created
```

Nous sommes maintenant prêts à sauvegarder notre base de données sur le backend souhaité.

**Créer une politique de rétention :**

Maintenant, créons un `RetentionPolicy` pour spécifier comment les anciens instantanés doivent être nettoyés.

Vous trouverez ci-dessous le YAML du `RetentionPolicy` objet que nous allons créer,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: demo-retention
  namespace: demo
spec:
  default: true
  failedSnapshots:
    last: 2
  maxRetentionPeriod: 2mo
  successfulSnapshots:
    last: 5
  usagePolicy:
    allowedNamespaces:
      from: All
```

Créons ce qui précède `RetentionPolicy`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/retentionpolicy.yaml
retentionpolicy.storage.kubestash.com/demo-retention created
```

### Sauvegarde

Nous devons créer un `BackupConfiguration` ciblant respectivement `sample-mariadb` Base de données MariaDB. Ensuite, KubeStash créera un `CronJob` pour chaque session pour effectuer une sauvegarde périodique de cette base de données.

Dans un premier temps, nous devons créer un secret avec un mot de passe Restic pour le cryptage des données de sauvegarde.

**Créer un secret :**

Créons un secret appelé `encrypt-secret` avec le mot de passe Restic,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ kubectl create secret generic -n demo encrypt-secret \
    --from-file=./RESTIC_PASSWORD \
secret "encrypt-secret" created
```

Vous trouverez ci-dessous le YAML pour `BackupConfiguration` CR pour sauvegarder le `sample-mariadb` base de données que nous avons déployée précédemment,

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
```

* `.spec.sessions[*].schedule` précise que nous voulons sauvegarder la base de données à `5 minutes` intervalle.
* `.spec.target` fait référence à la cible `sample-mariadb` Base de données MariaDB que nous avons créée précédemment.

Créons le `BackupConfiguration` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/backupconfiguration.yaml
backupconfiguration.core.kubestash.com/sample-mariadb-backup created
```

**Vérifier la configuration de la sauvegarde avec succès**

Si tout se passe bien, la phase du `BackupConfiguration` devrait être `Ready`. Le `Ready` La phase indique que la configuration de la sauvegarde a réussi. Vérifions le `Phase` de la Configuration de Sauvegarde,

```bash
$ kubectl get backupconfiguration -n demo
NAME                     PHASE   PAUSED   AGE
sample-mariadb-backup    Ready            2m50s
```

De plus, nous pouvons vérifier que le `Repository` précisé dans le `BackupConfiguration` a été créé à l'aide de la commande suivante,

```bash
$ kubectl get repo -n demo
NAME                  INTEGRITY   SNAPSHOT-COUNT   SIZE        PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo      true        1                1.096 KiB   Ready   3m3s                     3m13s
```

KubeStash conserve la sauvegarde pour `Repository` YAML. Si nous naviguons vers le compartiment GCS, nous verrons le `Repository` YAML stocké dans le `demo/mariadb` annuaire.

**Vérifiez CronJob :**

Cela créera également un `CronJob` avec l'horaire spécifié dans `spec.sessions[*].scheduler.schedule` domaine de `BackupConfiguration` CR.

Vérifiez que le `CronJob` a été créé à l'aide de la commande suivante,

```bash
$ kubectl get cronjob -n demo
NAME                                             SCHEDULE     TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
trigger-sample-mariadb-backup-frequent-backup   */5 * * * *   <none>     False     0        <none>          4m23s
```

**Vérifiez la session de sauvegarde :**

KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Après cela, les sauvegardes sont planifiées selon le calendrier spécifié.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                INVOKER-TYPE          INVOKER-NAME              PHASE       DURATION   AGE
sample-mariadb-backup-frequent-backup-1725449400    BackupConfiguration   sample-mariadb-backup     Succeeded              7m22s
```

Nous pouvons voir à partir du résultat ci-dessus que la session de sauvegarde a réussi. Nous allons maintenant vérifier si les données de sauvegarde ont été stockées dans le backend.

**Vérifier la sauvegarde :**

Une fois la sauvegarde terminée, KubeStash mettra à jour les fichiers respectifs. `Repository` CR pour refléter la sauvegarde. Vérifiez que le référentiel `sample-mariadb-backup` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo gcs-mariadb-repo
NAME                       INTEGRITY   SNAPSHOT-COUNT   SIZE    PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo           true        1                806 B   Ready   8m27s                    9m18s
```

En ce moment nous en avons un `Snapshot`. Exécutez la commande suivante pour vérifier les `Snapshot` qui représente l'état d'une sauvegarde exécutée pour une application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                  REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726569774       gcs-mariadb-repo    frequent-backup   2024-09-17T10:43:04Z   Delete            Succeeded   41m
```

> Remarque : KubeStash crée un `Snapshot` avec les étiquettes suivantes :
>
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> Ces étiquettes peuvent être utilisées pour regarder uniquement `Snapshot`s liés à notre base de données cible ou `Repository`.

Si nous vérifions le YAML du `Snapshot`, nous pouvons trouver les informations sur les composants de sauvegarde de la base de données.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726569774 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-17T10:43:04Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: gcs-mariadb-repo
  annotations:
    kubedb.com/db-version: 11.1.3
  name: gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726569774
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: gcs-mariadb-repo
      uid: 7abe82a2-5ecc-4904-b848-910becab54bc
  resourceVersion: "1566893"
  uid: a18e95f2-d7ec-4334-9ba4-f689280a51ab
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: sample-mariadb-backup-frequent-backup-1726569774
  deletionPolicy: Delete
  repository: gcs-mariadb-repo
  session: frequent-backup
  snapshotID: 01J7ZS88VNPD5B7HFVXVP576P6
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 3.279948033s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 0a6dfb754cb32bdaf17581fa42b20e8915aabd0b48f37c854b72812f53b7e5b6
            size: 2.206 KiB
            uploaded: 2.498 KiB
      size: 1.096 KiB
  conditions:
    - lastTransitionTime: "2024-09-17T10:43:04Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-17T10:43:24Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 1.096 KiB
  snapshotTime: "2024-09-17T10:43:04Z"
  totalComponents: 1
```

> KubeStash utilise `mariadb-dump` pour effectuer des sauvegardes de la cible `MariaDB` bases de données. Par conséquent, le nom du composant pour les sauvegardes logiques est défini comme `dump`.

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons les données de sauvegarde stockées dans le `demo/mariadb/repository/v1/frequent-backup/dump` annuaire. KubeStash conserve également la sauvegarde pour `Snapshot` Les YAML, que l'on peut trouver dans le `demo/mariadb/snapshots` annuaire.

> Remarque : KubeStash stocke toutes les données sauvegardées chiffrées dans le répertoire de sauvegarde, ce qui signifie qu'elles restent illisibles jusqu'à ce qu'elles soient déchiffrées.

## Restaurer

Dans cette section, nous allons restaurer la base de données à partir de la sauvegarde que nous avons effectuée dans la section précédente. Nous allons déployer une nouvelle base de données et l'initialiser à partir de la sauvegarde.

Maintenant, nous devons déployer la base de données restaurée de la même manière que nous avons déployé la base de données d'origine. `sample-mariadb` base de données. Cependant, cette fois, il y aura les différences suivantes :

* Nous allons préciser `.spec.init.waitForInitialRestore` champ qui indique à KubeDB d'attendre la fin de la première restauration avant de marquer cette base de données comme prête à être utilisée.

Vous trouverez ci-dessous le YAML pour `MariaDB` CR que nous allons déployer pour initialiser à partir de la sauvegarde,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: restored-mariadb
  namespace: demo
spec:
  init:
    waitForInitialRestore: true
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créons la base de données ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/restored-mariadb.yaml
mariadb.kubedb.com/restored-mariadb created
```

Si vous vérifiez l'état de la base de données, vous verrez qu'elle est bloquée **`Provisioning`** État.

```bash
$ kubectl get mariadb -n demo restored-mariadb
NAME                VERSION   STATUS         AGE
restored-mariadb    11.1.3    Provisioning   110s
```

#### Créer une session de restauration :

Maintenant, nous devons créer un `RestoreSession` CR pointant vers ciblé `MariaDB` base de données.

Ci-dessous, le contenu du fichier YAML du `RestoreSession` objet que nous allons créer pour restaurer les données de sauvegarde dans le nouveau fichier créé `MariaDB` base de données nommée `restored-mariadb`.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
```

Ici,

* `.spec.target` fait référence au nouveau créé `restored-mariadb` MariaDB s'oppose à l'endroit où nous souhaitons restaurer les données de sauvegarde.
* `.spec.dataSource.repository` spécifie l'objet Repository qui contient les données de sauvegarde.
* `.spec.dataSource.snapshot` spécifie de restaurer à partir du dernier `Snapshot`.

Créons l'objet RestoreSession CRD que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/restoresession.yaml
restoresession.core.kubestash.com/sample-mariadb-restore created
```

Une fois que vous avez créé le `RestoreSession` objet, KubeStash créera une tâche de restauration. Exécutez la commande suivante pour regarder la phase du `RestoreSession` objet,

```bash
$ watch kubectl get restoresession -n demo
NAME                      REPOSITORY          FAILURE-POLICY   PHASE       DURATION   AGE
sample-mariadb-restore   gcs-mariadb-repo                    Succeeded   7s         116s
```

Le `Succeeded` Cette phase signifie que le processus de restauration s'est terminé avec succès.

#### Vérifiez les données restaurées :

Dans cette section, nous allons vérifier si les données souhaitées ont été restaurées avec succès. Nous allons nous connecter au serveur de base de données et vérifier si la base de données et la table que nous avons créée précédemment dans la base de données d'origine sont restaurées.

Dans un premier temps, vérifiez si la base de données est entrée dans **`Ready`** énoncer par la commande suivante,

```bash
$ kubectl get mariadb -n demo restored-mariadb
NAME                VERSION   STATUS   AGE
restored-mariadb    11.1.3    Ready    6m
```

Maintenant, découvrez la base de données `Pod` par la commande suivante,

```bash
$ kubectl get pods -n demo --selector="app.kubernetes.io/instance=restored-mariadb"
NAME                            READY   STATUS      RESTARTS   AGE
restored-mariadb-0              2/2     Running     0          7m
restored-mariadb-1              2/2     Running     0          7m
restored-mariadb-2              2/2     Running     0          7m
```

Maintenant, exécutons l'un des `Pod` et vérifiez les données restaurées.

```bash
$ kubectl exec -it -n demo restored-mariadb-0 -- bash
```

```mysql
mysql@restored-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> use hello;

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

Ainsi, à partir du résultat ci-dessus, nous pouvons voir le `hello` base de données que nous avions créée dans la base de données d'origine `sample-mariadb` a été restauré dans le `restored-mariadb` base de données.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete backupconfigurations.core.kubestash.com  -n demo sample-mariadb-backup
kubectl delete restoresessions.core.kubestash.com -n demo restore-sample-mariadb
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo restored-mariadb
kubectl delete mariadb -n demo sample-mariadb
```

<!-- PAGE_START: backup/kubestash/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

Veuillez installer [KubeStash](https://kubestash.com/docs/latest/setup/install/kubestash/) pour essayer cette fonctionnalité. La sauvegarde de la base de données avec KubeStash est déjà incluse dans la licence KubeDB. Vous n’avez donc pas besoin d’une licence distincte pour KubeStash.

# Présentation de la sauvegarde et de la restauration MariaDB

KubeDB utilise également [KubeStash](https://kubestash.com) pour sauvegarder et restaurer des bases de données. KubeStash d'AppsCode est une solution cloud native de sauvegarde et de récupération de données pour les charges de travail et les bases de données Kubernetes. KubeStash utilise [restique](https://github.com/restic/restic) pour sauvegarder en toute sécurité des applications avec état sur n'importe quel backend de stockage cloud ou sur site (par exemple, S3, GCS, stockage Azure Blob, Minio, NetApp, Dell EMC, etc.).

  ![KubeDB + KubeStash](images/backup_kubestash_overview_kubedb_plus_kubestash.svg)

Fig : Sauvegarder les bases de données KubeDB à l'aide de KubeStash

## Comment fonctionne la sauvegarde

```mermaid
flowchart LR
  User["Appliquer BackupConfiguration"] --> KS["Contrôleur KubeStash"]
  KS --> Repo["Repository + BackupStorage + Secret"]
  KS --> Cron["CronJob -> BackupSession -> Snapshot"]
  Cron --> Job["Job de sauvegarde"]
  AppBind["AppBinding (Hôte, Port, Secret Auth)"] --> Job
  MariaDB["Pod MariaDB"] -->|Flux Dump / Volume| Job
  Job -->|Téléversement Restic chiffré| Backend["Stockage S3 / GCS / NFS"]
```


Le diagramme suivant montre comment KubeStash effectue la sauvegarde d'un `MariaDB` base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![MariaDB Backup Overview](images/backup_kubestash_overview_backup_overview.svg)

Figure : Présentation de la sauvegarde MariaDB

Le processus de sauvegarde comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `Secret`. Ce secret contient les informations d'identification permettant d'accéder au backend où les données sauvegardées seront stockées.
2. Ensuite, elle crée un `BackupStorage` ressource personnalisée qui spécifie les informations du backend, ainsi que les `Secret` contenant les informations d'identification nécessaires pour accéder au backend.
3. L'opérateur KubeStash surveille `BackupStorage` ressources personnalisées. Lorsqu'il trouve un `BackupStorage` objet, il initialise le `BackupStorage` en téléchargeant le `metadata.yaml` fichier vers le backend spécifié.
4. Ensuite, elle crée un `BackupConfiguration` ressource personnalisée qui spécifie la base de données cible, les informations complémentaires (y compris les tâches de sauvegarde), les planifications de sauvegarde, les backends de stockage pour stocker les données de sauvegarde et d'autres paramètres supplémentaires.
5. L'opérateur KubeStash surveille `BackupConfiguration` objets.
6. Une fois que l'opérateur KubeStash trouve un `BackupConfiguration` objet, il crée `Repository` avec les informations spécifiées dans le `BackupConfiguration`.
7. L'opérateur KubeStash surveille `Repository` ressources personnalisées. Lorsqu'il trouve le `Repository` objet, il initialise `Repository` en téléchargeant `repository.yaml` déposer dans le `spec.sessions[*].repositories[*].directory` chemin spécifié dans `BackupConfiguration`.
8. Ensuite, cela crée un `CronJob` pour chaque séance selon l'horaire précisé dans `BackupConfiguration` pour déclencher une sauvegarde périodiquement.
9. L'opérateur KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Les sauvegardes sont autrement déclenchées par le `CronJob` en fonction du calendrier spécifié.
10. L'opérateur KubeStash surveille `BackupSession` ressources personnalisées.
11. Lorsqu'il trouve un `BackupSession` objet, il crée un `Snapshot` ressource personnalisée pour chacun `Repository` précisé dans le `BackupConfiguration`.
12. Ensuite, il résout le problème respectif `Addon` et `Function` et prépare la sauvegarde `Job` définition.
13. Ensuite, il crée le `Job` pour sauvegarder la cible `MariaDB` base de données.
14. La sauvegarde `Job` lit les informations nécessaires (par exemple, secret d'authentification, port) pour se connecter à la base de données à partir du `AppBinding` CR. Il lit également les informations du backend et accède aux informations d'identification à partir de `BackupStorage` CR, secret de stockage et `Repository` chemin respectivement.
15. Ensuite, le `Job` jette la cible `MariaDB` base de données et télécharge la sortie vers le backend. KubeStash redirige la sortie de la commande dump vers le processus de téléchargement. Par conséquent, sauvegarde `Job` ne nécessite pas un volume important pour contenir la totalité de la sortie de vidage.
16. Une fois le processus de sauvegarde terminé, la sauvegarde `Job` met à jour le `status.components[dump]` domaine de la `Snapshot` ressources avec les informations de sauvegarde de la cible `MariaDB` base de données.

## Comment fonctionne le processus de restauration

Le diagramme suivant montre comment KubeStash restaure les données sauvegardées dans un `MariaDB` base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Database Restore Overview](images/backup_kubestash_overview_restore_overview.svg)

Fig : Présentation du processus de restauration MariaDB

Le processus de restauration comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` base de données où les données seront restaurées ou l'utilisateur pourra utiliser la même `MariaDB` base de données.
2. Ensuite, elle crée un `RestoreSession` ressource personnalisée qui spécifie la base de données cible dans laquelle les données sauvegardées seront restaurées, les informations sur le module complémentaire (y compris les tâches de restauration), l'instantané cible à restaurer, le référentiel contenant cet instantané et d'autres paramètres supplémentaires.
3. L'opérateur KubeStash surveille `RestoreSession` ressources personnalisées.
4. Lorsqu'il trouve un `RestoreSession` ressource personnalisée, il résout les problèmes respectifs `Addon` et `Function` et prépare une restauration `Job` définition.
5. Ensuite, il crée le `Job` pour restaurer la cible.
6. Le `Job` lit les informations nécessaires pour se connecter à la base de données à partir de leurs `AppBinding` CR. Il lit également les informations du backend et accède aux informations d'identification à partir de `Repository` CR et stockage `Secret` respectivement.
7. Ensuite, le `Job` télécharge les données sauvegardées depuis le backend et les injecte dans la base de données souhaitée. KubeStash dirige les données téléchargées vers l'outil de base de données correspondant pour les injecter dans la base de données. Par conséquent, restaurez `Job` ne nécessite pas un volume important pour télécharger l’intégralité des données de sauvegarde qu’il contient.
8. Enfin, lorsque le processus de restauration est terminé, le `Job` met à jour le `status.components[*]` domaine de la `RestoreSession` avec les informations de restauration de la base de données cible.

## Prochaines étapes

* Sauvegarder un `MariaDB` base de données utilisant KubeStash par les guides suivants de [ici](fr/backup/kubestash/logical.md).

<!-- PAGE_START: backup/stash/auto-backup.md -->
# Sauvegarder MariaDB à l'aide de la sauvegarde automatique Stash

Stash peut être configuré pour sauvegarder automatiquement n'importe quelle base de données MariaDB de votre cluster. Stash permet aux administrateurs de cluster de déployer des plans de sauvegarde à l'avance afin que les propriétaires de bases de données puissent facilement sauvegarder leur base de données avec seulement quelques annotations.

Dans ce didacticiel, nous allons montrer comment configurer un plan de sauvegarde pour les bases de données MariaDB dans votre cluster et les sauvegarder avec quelques annotations.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installez Stash dans votre cluster en suivant les étapes [ici](https://stash.run/docs/latest/setup/install/stash/).
* Installez KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Si vous n'êtes pas familier avec la façon dont Stash sauvegarde et restaure les bases de données MariaDB, veuillez consulter le guide suivant [ici](fr/backup/stash/overview.md).
* Si vous n'êtes pas familier avec le fonctionnement de la sauvegarde automatique dans Stash, veuillez consulter le guide suivant [ici](https://stash.run/docs/latest/guides/auto-backup/overview/).
* Si vous n'êtes pas familier avec les options de sauvegarde automatique disponibles pour les bases de données dans Stash, veuillez consulter le guide suivant [ici](https://stash.run/docs/latest/guides/auto-backup/database/).

Vous devriez être familier avec ce qui suit `Stash` notions :

* [Plan de sauvegarde](https://stash.run/docs/latest/concepts/crds/backupblueprint/)
* [BackupConfiguration](https://stash.run/docs/latest/concepts/crds/backupconfiguration/)
* [Session de sauvegarde](https://stash.run/docs/latest/concepts/crds/backupsession/)
* [Dépôt](https://stash.run/docs/latest/concepts/crds/repository/)
* [Fonction](https://stash.run/docs/latest/concepts/crds/function/)
* [Tâche](https://stash.run/docs/latest/concepts/crds/task/)

Dans ce tutoriel, nous allons montrer la sauvegarde de trois bases de données MariaDB différentes sur trois espaces de noms différents nommés `demo`, `demo-2`, et `demo-3`. Create the namespaces as below if you haven’t done it already.

```bash
❯ kubectl create ns demo
namespace/demo created

❯ kubectl create ns demo-2
namespace/demo-2 created

❯ kubectl create ns demo-3
namespace/demo-3 created
```

Lorsque vous installez Stash, il installe automatiquement tous les modules complémentaires de base de données officiels. Vérifiez qu'il a installé les modules complémentaires MariaDB à l'aide de la commande suivante.

```bash
❯ kubectl get tasks.stash.appscode.com | grep mariadb
mariadb-backup-11.8.5    62m
mariadb-restore-11.8.5   62m
```

## Préparer le plan de sauvegarde

Pour sauvegarder une base de données MariaDB à l'aide de Stash, vous devez créer un `` contenant les informations d'identification du backend, un `Repository` contenant les informations du backend, et un `BackupConfiguration` contenant le calendrier et les informations sur la cible. UN `BackupBlueprint` vous permet de spécifier un modèle pour le `Repository` et le `BackupConfiguration`.

Le `BackupBlueprint` est un CRD sans espace de noms. Ainsi, une fois que vous avez créé un `BackupBlueprint`, vous pouvez l'utiliser pour sauvegarder n'importe quelle base de données MariaDB de n'importe quel espace de noms simplement en créant le stockage `` dans cet espace de noms et en ajoutant quelques annotations à votre CRO MariaDB. Ensuite, Stash créera automatiquement un `Repository` et un `BackupConfiguration` selon le modèle pour sauvegarder la base de données.

Ci-dessous se trouve le `BackupBlueprint` objet que nous allons utiliser dans ce tutoriel,

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupBlueprint
metadata:
  name: mariadb-backup-template
spec:
  # ============== Blueprint for Repository ==========================
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/${TARGET_NAMESPACE}/${TARGET_APP_RESOURCE}/${TARGET_NAME}
  # ============== Blueprint for BackupConfiguration =================
  schedule: "*/5 * * * *"
  retentionPolicy:
    name: 'keep-last-5'
    keepLast: 5
    prune: true
```

Ici, nous utilisons un bucket GCS comme backend. Nous fournissons `gcs-` à la `storageName` champ. Par conséquent, nous devons créer un nom `gcs-` avec les informations d'identification d'accès de notre compartiment dans chaque espace de noms où nous souhaitons activer la sauvegarde via ce plan.

Remarquez le `prefix` domaine de `backend` section. Nous avons utilisé quelques variables sous forme de `${VARIABLE_NAME}`. Stash résoudra automatiquement ces variables à partir des informations de la base de données pour rendre le préfixe backend unique pour chaque instance de base de données.

Créons le `BackupBlueprint` nous l'avons montré ci-dessus,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/backupblueprint.yaml
backupblueprint.stash.appscode.com/mariadb-backup-template created
```

Nous sommes maintenant prêts à sauvegarder nos bases de données MariaDB en utilisant quelques annotations. Vous pouvez vérifier les annotations de sauvegarde automatique disponibles pour une base de données à partir de [ici](https://stash.run/docs/latest/guides/auto-backup/database/#available-auto-backup-annotations-for-database).

## Sauvegarde automatique avec configurations par défaut

Dans cette section, nous allons sauvegarder une base de données MariaDB de `demo` espace de noms. Nous allons utiliser les configurations par défaut spécifiées dans le `BackupBlueprint`.

### Créer un stockage

Dans un premier temps, créons le `gcs-` dans `demo` espace de noms avec les informations d'identification d'accès à notre bucket GCS.

```bash
❯ echo -n 'changeit' > RESTIC_PASSWORD
❯ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
❯ cat downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
❯ kubectl create  generic -n demo gcs- \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
/gcs- created
```

### Créer une base de données

Maintenant, nous allons créer un CRO MariaDB dans `demo` espace de noms. Ci-dessous se trouve le YAML de l'objet MariaDB que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
  annotations:
    stash.appscode.com/backup-blueprint: mariadb-backup-template
spec:
  version: "12.1.2"
  replicas: 1
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

Remarquez le `annotations` section. Nous pointons du doigt le `BackupBlueprint` que nous avons créé plus tôt cependant `stash.appscode.com/backup-blueprint` annotation. Stash surveillera cette annotation et créera un `Repository` et un `BackupConfiguration` selon le `BackupBlueprint`.

Créons le MariaDB CRO ci-dessus,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

### Vérifier la sauvegarde automatique configurée

Dans cette section, nous allons vérifier si Stash a créé le fichier respectif `Repository` et `BackupConfiguration` pour notre base de données MariaDB que nous venons de déployer ou non.

#### Vérifier le référentiel

Dans un premier temps, vérifions si Stash a créé un `Repository` pour notre MariaDB ou pas.

```bash
❯ kubectl get repository -n demo
NAME                 INTEGRITY   SIZE   SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
app-sample-mariadb                                                                10s
```

Maintenant, vérifions le YAML du `Repository`.

```bash
❯ kubectl get repository -n demo app-sample-mariadb -o yaml
```

```text
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
...  
  name: app-sample-mariadb
  namespace: demo
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/demo/mariadb/sample-mariadb
    storageName: gcs-
```

Ici, vous pouvez voir que Stash a résolu les variables dans `prefix` champ et les a remplacés par les informations équivalentes de cette base de données.

#### Vérifier la configuration de la sauvegarde

Si tout se passe bien, Stash devrait créer un `BackupConfiguration` pour notre MariaDB en `demo` espace de noms et la phase de celui-ci `BackupConfiguration` devrait être `Ready`. Vérifiez le `BackupConfiguration` crd par la commande suivante,

```bash
❯ kubectl get backupconfiguration -n demo
NAME                 TASK                    SCHEDULE      PAUSED   PHASE   AGE
app-sample-mariadb   mariadb-backup-11.8.5   */5 * * * *            Ready   7m28s
```

Maintenant, vérifions le YAML du `BackupConfiguration`.

```bash
❯ kubectl get backupconfiguration -n demo app-sample-mariadb -o yaml
```

```text
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: app-sample-mariadb
  namespace: demo
  ...
  spec:
  driver: Restic
  repository:
    name: app-sample-mariadb
  retentionPolicy:
    keepLast: 5
    name: keep-last-5
    prune: true
  runtimeSettings: {}
  schedule: '*/5 * * * *'
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  tempDir: {}
status:
  conditions:
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Repository demo/app-sample-mariadb exist.
    reason: RepositoryAvailable
    status: "True"
    type: RepositoryFound
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Backend  demo/gcs- exist.
    reason: BackendAvailable
    status: "True"
    type: BackendFound
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Backup target appcatalog.appscode.com/v1alpha1 appbinding/sample-mariadb
      found.
    reason: TargetAvailable
    status: "True"
    type: BackupTargetFound
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Successfully created backup triggering CronJob.
    reason: CronJobCreationSucceeded
    status: "True"
    type: CronJobCreated
  observedGeneration: 1
```

Remarquez le `target` section. Stash a automatiquement ajouté MariaDB comme cible de ce `BackupConfiguration`.

#### Vérifier la sauvegarde

Maintenant, attendons la fin d’une sauvegarde. Vous pouvez surveiller `BackupSession` comme ci-dessous,

```bash
❯ kubectl get backupsession -n demo -w
NAME                            INVOKER-TYPE          INVOKER-NAME         PHASE       AGE
app-sample-mariadb-1614230401   BackupConfiguration   app-sample-mariadb   Succeeded   5m40s
app-sample-mariadb-1614230701   BackupConfiguration   app-sample-mariadb   Running     39s
```

Une fois la sauvegarde terminée avec succès, vous devriez voir que les données sauvegardées ont été stockées dans le compartiment dans le répertoire pointé par le `prefix` domaine de la `Repository`.

![Backup data in GCS Bucket](images/backup_stash_auto-backup_sample-mariadb.png)

Fig : Sauvegarder les données dans le compartiment GCS

## Sauvegarde automatique avec un calendrier personnalisé

Dans cette section, nous allons sauvegarder une base de données MariaDB de `demo-2` espace de noms. Cette fois, nous allons écraser le planning par défaut utilisé dans le `BackupBlueprint`.

### Créer un stockage

Dans un premier temps, créons le `gcs-` dans `demo-2` espace de noms avec les informations d'identification d'accès à notre bucket GCS.

```bash
❯ kubectl create  generic -n demo-2 gcs- \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
/gcs- created
```

### Créer une base de données

Maintenant, nous allons créer un CRO MariaDB dans `demo-2` espace de noms. Ci-dessous se trouve le YAML de l'objet MariaDB que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb-2
  namespace: demo-2
  annotations:
    stash.appscode.com/backup-blueprint: mariadb-backup-template
    stash.appscode.com/schedule: "*/3 * * * *"
spec:
  version: "12.1.2"
  replicas: 1
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

Remarquez le `annotations` section. Cette fois, nous avons passé un planning via `stash.appscode.com/schedule` annotation avec le `stash.appscode.com/backup-blueprint` annotation.

Créons le MariaDB CRO ci-dessus,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/sample-mariadb-2.yaml
mariadb.kubedb.com/sample-mariadb-2 created
```

### Vérifier la sauvegarde automatique configurée

Vérifions maintenant si la sauvegarde automatique a été configurée correctement ou non.

#### Vérifier le référentiel

Dans un premier temps, vérifions si Stash a créé un `Repository` pour notre MariaDB ou pas.

```bash
❯ kubectl get repository -n demo-2
NAME                   INTEGRITY   SIZE   SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
app-sample-mariadb-2                                                                4s
```

Maintenant, vérifions le YAML du `Repository`.

```bash
❯ kubectl get repository -n demo-2 app-sample-mariadb-2  -o yaml
```

```text
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: app-sample-mariadb-2
  namespace: demo-2
  ...
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/demo-2/mariadb/sample-mariadb-2
    storageName: gcs-
```

Ici, vous pouvez voir que Stash a résolu les variables dans `prefix` champ et les a remplacés par les informations équivalentes de cette nouvelle base de données.

#### Vérifier la configuration de la sauvegarde

Si tout se passe bien, Stash devrait créer un `BackupConfiguration` pour notre MariaDB en `demo-2` espace de noms et la phase de celui-ci `BackupConfiguration` devrait être `Ready`. Vérifiez le `BackupConfiguration` crd par la commande suivante,

```bash
❯ kubectl get backupconfiguration -n demo-2
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
app-sample-mariadb-2   mariadb-backup-11.8.5   */3 * * * *            Ready   3m24s
```

Maintenant, vérifions le YAML du `BackupConfiguration`.

```bash
❯ kubectl get backupconfiguration -n demo-2 app-sample-mariadb-2 -o yaml
```

```text
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: app-sample-mariadb-2
  namespace: demo-2
  ...
  ownerReferences:
  - apiVersion: appcatalog.appscode.com/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: AppBinding
    name: sample-mariadb-2
    uid: 7cbdf140-5fd1-487a-b04f-1847def418e8
  resourceVersion: "56888"
  selfLink: /apis/stash.appscode.com/v1beta1/namespaces/demo-2/backupconfigurations/app-sample-mariadb-2
  uid: e85dd3db-fa41-48b8-b253-5731ee8cc956
spec:
  driver: Restic
  repository:
    name: app-sample-mariadb-2
  retentionPolicy:
    keepLast: 5
    name: keep-last-5
    prune: true
  runtimeSettings: {}
  schedule: '*/3 * * * *'
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb-2
  tempDir: {}
status:
  conditions:
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Repository demo-2/app-sample-mariadb-2 exist.
    reason: RepositoryAvailable
    status: "True"
    type: RepositoryFound
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Backend  demo-2/gcs- exist.
    reason: BackendAvailable
    status: "True"
    type: BackendFound
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Backup target appcatalog.appscode.com/v1alpha1 appbinding/sample-mariadb-2
      found.
    reason: TargetAvailable
    status: "True"
    type: BackupTargetFound
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Successfully created backup triggering CronJob.
    reason: CronJobCreationSucceeded
    status: "True"
    type: CronJobCreated
  observedGeneration: 1
```

Remarquez le `schedule` section. Cette fois le `BackupConfiguration` a été créé avec le calendrier que nous avons fourni via annotation.

Notez également le `target` section. Stash a automatiquement ajouté la nouvelle MariaDB comme cible de ce `BackupConfiguration`.

#### Vérifier la sauvegarde

Maintenant, attendons la fin d’une sauvegarde. Vous pouvez surveiller `BackupSession` comme ci-dessous,

```bash
❯ kubectl get backupsession -n demo-2 -w
NAME                              INVOKER-TYPE          INVOKER-NAME           PHASE       AGE
app-sample-mariadb-2-1614233715   BackupConfiguration   app-sample-mariadb-2   Succeeded   3m2s
app-sample-mariadb-2-1614233880   BackupConfiguration   app-sample-mariadb-2   Running     17s
```

Une fois la sauvegarde terminée avec succès, vous devriez voir que Stash a créé un nouveau répertoire comme indiqué par le `prefix` domaine du nouveau `Repository` et y ont stocké les données sauvegardées.

![Backup data in GCS Bucket](images/backup_stash_auto-backup_sample-mariadb-2.png)

Fig : Sauvegarder les données dans le compartiment GCS

## Sauvegarde automatique avec paramètres personnalisés

Dans cette section, nous allons sauvegarder une base de données MariaDB de `demo-3` espace de noms. Cette fois, nous allons transmettre certains paramètres de la tâche via les annotations.

### Créer un stockage

Dans un premier temps, créons le `gcs-` dans `demo-3` espace de noms avec les informations d'identification d'accès à notre bucket GCS.

```bash
❯ kubectl create  generic -n demo-3 gcs- \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
/gcs- created
```

### Créer une base de données

Maintenant, nous allons créer un CRO MariaDB dans `demo-3` espace de noms. Ci-dessous se trouve le YAML de l'objet MariaDB que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb-3
  namespace: demo-3
  annotations:
    stash.appscode.com/backup-blueprint: mariadb-backup-template
    params.stash.appscode.com/args: --databases mysql
spec:
  version: "12.1.2"
  replicas: 1
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

Remarquez le `annotations` section. Cette fois, nous avons passé un argument via `params.stash.appscode.com/args` annotation avec le `stash.appscode.com/backup-blueprint` annotation.

Créons le MariaDB CRO ci-dessus,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/sample-mariadb-3.yaml
mariadb.kubedb.com/sample-mariadb-3 created
```

### Vérifier la sauvegarde automatique configurée

Vérifions maintenant si les ressources de sauvegarde automatique ont été créées ou non.

#### Vérifier le référentiel

Dans un premier temps, vérifions si Stash a créé un `Repository` pour notre MariaDB ou pas.

```bash
❯ kubectl get repository -n demo-3
NAME                   INTEGRITY   SIZE   SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
app-sample-mariadb-3                                                                8s
```

Maintenant, vérifions le YAML du `Repository`.

```bash
❯ kubectl get repository -n demo-3 app-sample-mariadb-3 -o yaml
```

```text
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: app-sample-mariadb-3
  namespace: demo-3
  ...
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/demo-3/mariadb/sample-mariadb-3
    storageName: gcs-
```

Ici, vous pouvez voir que Stash a résolu les variables dans `prefix` champ et les a remplacés par les informations équivalentes de cette nouvelle base de données.

#### Vérifier la configuration de la sauvegarde

Si tout se passe bien, Stash devrait créer un `BackupConfiguration` pour notre MariaDB en `demo-3` espace de noms et la phase de celui-ci `BackupConfiguration` devrait être `Ready`. Vérifiez le `BackupConfiguration` crd par la commande suivante,

```bash
❯ kubectl get backupconfiguration -n demo-3
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
app-sample-mariadb-3   mariadb-backup-11.8.5   */5 * * * *            Ready   106s
```

Maintenant, vérifions le YAML du `BackupConfiguration`.

```bash
❯ kubectl get backupconfiguration -n demo-3 app-sample-mariadb-3 -o yaml
```

```text
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: app-sample-mariadb-3
  namespace: demo-3
  ...
spec:
  driver: Restic
  repository:
    name: app-sample-mariadb-3
  retentionPolicy:
    keepLast: 5
    name: keep-last-5
    prune: true
  runtimeSettings: {}
  schedule: '*/5 * * * *'
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb-3
  task:
    params:
    - name: args
      value: --databases mysql
  tempDir: {}
status:
  conditions:
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Repository demo-3/app-sample-mariadb-3 exist.
    reason: RepositoryAvailable
    status: "True"
    type: RepositoryFound
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Backend  demo-3/gcs- exist.
    reason: BackendAvailable
    status: "True"
    type: BackendFound
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Backup target appcatalog.appscode.com/v1alpha1 appbinding/sample-mariadb-3
      found.
    reason: TargetAvailable
    status: "True"
    type: BackupTargetFound
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Successfully created backup triggering CronJob.
    reason: CronJobCreationSucceeded
    status: "True"
    type: CronJobCreated
  observedGeneration: 1
```

Remarquez le `task` section. Le `args` Le paramètre que nous avions passé via les annotations a été ajouté au `params` section.

Notez également le `target` section. Stash a automatiquement ajouté la nouvelle MariaDB comme cible de ce `BackupConfiguration`.

#### Vérifier la sauvegarde

Maintenant, attendons la fin d’une sauvegarde. Vous pouvez surveiller `BackupSession` comme ci-dessous,

```bash
❯ kubectl get backupsession -n demo-3 -w
NAME                              INVOKER-TYPE          INVOKER-NAME           PHASE       AGE
app-sample-mariadb-3-1614254408   BackupConfiguration   app-sample-mariadb-3   Succeeded   5m23s
app-sample-mariadb-3-1614254708   BackupConfiguration   app-sample-mariadb-3   Running     23s
```

Une fois la sauvegarde terminée avec succès, vous devriez voir que Stash a créé un nouveau répertoire comme indiqué par le `prefix` domaine du nouveau `Repository` et y ont stocké les données sauvegardées.

![Backup data in GCS Bucket](images/backup_stash_auto-backup_sample-mariadb-3.png)

Fig : Sauvegarder les données dans le compartiment GCS

## Nettoyage

Pour nettoyer les ressources créées par ce didacticiel, exécutez les commandes suivantes :

```bash
❯ kubectl delete -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/
backupblueprint.stash.appscode.com "mariadb-backup-template" deleted
mariadb.kubedb.com "sample-mariadb-2" deleted
mariadb.kubedb.com "sample-mariadb-3" deleted
mariadb.kubedb.com "sample-mariadb" deleted

❯ kubectl delete repository -n demo --all
repository.stash.appscode.com "app-sample-mariadb" deleted
❯ kubectl delete repository -n demo-2 --all
repository.stash.appscode.com "app-sample-mariadb-2" deleted
❯ kubectl delete repository -n demo-3 --all
repository.stash.appscode.com "app-sample-mariadb-3" deleted
```

<!-- PAGE_START: backup/stash/customization.md -->
# Personnalisation du processus de sauvegarde et de restauration

Stash fournit de riches supports de personnalisation pour le processus de sauvegarde et de restauration afin de répondre aux exigences de diverses configurations de cluster. Ce guide vous montrera quelques exemples de ces personnalisations.

## Personnalisation du processus de sauvegarde

Dans cette section, nous allons vous montrer comment personnaliser le processus de sauvegarde. Ici, nous allons montrer quelques exemples de fourniture d'arguments au processus de sauvegarde, d'exécution du processus de sauvegarde en tant qu'utilisateur spécifique, d'ignorance de certains index pendant le processus de sauvegarde, etc.

### Passer des arguments au processus de sauvegarde

Utilisations du module complémentaire Stash MariaDB [mysqldump](https://mariadb.com/kb/en/mysqldump) pour la sauvegarde. Vous pouvez transmettre des arguments au `mysqldump` à travers `args` paramètre sous `task.params` section.

L'exemple ci-dessous montre comment vous pouvez transmettre le `--databases testdb` pour effectuer une sauvegarde d'une base de données mariadb spécifique nommée `testdb`.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  task:
    params:
    - name: args
      value: --databases testdb
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

> **AVERTISSEMENT**: Assurez-vous d'avoir créé la base de données spécifique avant d'effectuer une sauvegarde. Dans ce cas, Base de données `testdb` doit exister avant le démarrage du travail de sauvegarde.

### Exécution d'une tâche de sauvegarde en tant qu'utilisateur spécifique

Si votre cluster nécessite l'exécution de la tâche de sauvegarde en tant qu'utilisateur spécifique, vous pouvez fournir `securityContext` sous `runtimeSettings.pod` section. L'exemple ci-dessous montre comment exécuter la tâche de sauvegarde en tant qu'utilisateur root.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/2 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    pod:
      securityContext:
        runAsUser: 0
        runAsGroup: 0
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de sauvegarde

Si vous souhaitez spécifier la limite/demande de mémoire/CPU pour votre tâche de sauvegarde, vous pouvez spécifier `resources` champ sous `runtimeSettings.container` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/2 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    container:
      resources:
        requests:
          cpu: "200m"
          memory: "1Gi"
        limits:
          cpu: "200m"
          memory: "1Gi"
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

### Utilisation de plusieurs politiques de rétention

Vous pouvez également spécifier plusieurs politiques de conservation pour vos données sauvegardées. Par exemple, vous souhaiterez peut-être conserver quelques instantanés quotidiens, quelques instantanés hebdomadaires et quelques instantanés mensuels, etc. Il vous suffit de transmettre le numéro souhaité avec la clé correspondante sous le `retentionPolicy` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: sample-mariadb-retention
    keepLast: 5
    keepDaily: 10
    keepWeekly: 20
    keepMonthly: 50
    keepYearly: 100
    prune: true
```

Pour en savoir plus sur les options disponibles pour les politiques de rétention, veuillez visiter [ici](https://stash.run/docs/latest/concepts/crds/backupconfiguration/#specretentionpolicy).

## Personnalisation du processus de restauration

Stash utilise également `mysql` pendant le processus de restauration. Dans cette section, nous allons montrer comment transmettre des arguments au processus de restauration, restaurer un instantané spécifique, exécuter une tâche de restauration en tant qu'utilisateur spécifique, etc.

### Passer des arguments au processus de restauration

Comme pour le processus de sauvegarde, vous pouvez transmettre des arguments au processus de restauration via le `args` paramètres sous `task.params` section. Cet exemple restaurera les données de la base de données `testdb` seulement.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  task:
    params:
    - name: args
      value: --one-database testdb
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [latest]
```

### Restaurer un instantané spécifique

Vous pouvez également restaurer un instantané spécifique. Dans un premier temps, répertoriez l'instantané disponible comme ci-dessous,

```bash
❯ kubectl get snapshots -n demo
NAME                ID         REPOSITORY   HOSTNAME   CREATED AT
gcs-repo-4bc21d6f   4bc21d6f   gcs-repo     host-0     2022-01-12T14:54:27Z
gcs-repo-f0ac7cbd   f0ac7cbd   gcs-repo     host-0     2022-01-12T14:56:26Z
gcs-repo-9210ebb6   9210ebb6   gcs-repo     host-0     2022-01-12T14:58:27Z
gcs-repo-0aff8890   0aff8890   gcs-repo     host-0     2022-01-12T15:00:28Z
```

> Vous pouvez également filtrer les instantanés comme indiqué dans le guide [ici](https://stash.run/docs/latest/concepts/crds/snapshot/#working-with-snapshot).

Vous pouvez utiliser l'ID respectif de l'instantané pour restaurer cet instantané.

L'exemple ci-dessous montre comment transmettre un ID d'instantané spécifique via le `snapshots` domaine de `rules` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [4bc21d6f]
```

> Veuillez ne pas spécifier plusieurs instantanés ici. Chaque instantané représente une sauvegarde complète de votre base de données. Plusieurs instantanés ne sont utilisables que lors de la restauration de fichiers/répertoires.

### Exécution d'une tâche de restauration en tant qu'utilisateur spécifique

Vous pouvez fournir `securityContext` sous `runtimeSettings.pod` pour exécuter le travail de restauration en tant qu'utilisateur spécifique.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    pod:
      securityContext:
        runAsUser: 0
        runAsGroup: 0
  rules:
  - snapshots: [latest]
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de restauration

Semblable au processus de sauvegarde, vous pouvez également fournir `resources` champ sous le `runtimeSettings.container` section pour limiter la mémoire/CPU pour votre travail de restauration.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    container:
      resources:
        requests:
          cpu: "200m"
          memory: "1Gi"
        limits:
          cpu: "200m"
          memory: "1Gi"
  rules:
  - snapshots: [latest]
```

<!-- PAGE_START: backup/stash/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

Veuillez installer [Planque](https://stash.run/docs/latest/setup/install/stash/) pour essayer cette fonctionnalité. La sauvegarde de la base de données avec Stash est déjà incluse dans la licence KubeDB. Vous n’avez donc pas besoin d’une licence distincte pour Stash.

# Présentation de la sauvegarde et de la restauration MariaDB

KubeDB utilise [Planque](https://stash.run) pour sauvegarder et restaurer des bases de données. Stash by AppsCode est une solution cloud native de sauvegarde et de récupération de données pour les charges de travail Kubernetes. Stash utilise [restique](https://github.com/restic/restic) pour sauvegarder en toute sécurité des applications avec état sur n'importe quel backend de stockage cloud ou sur site (par exemple, S3, GCS, stockage Azure Blob, Minio, NetApp, Dell EMC, etc.).

  ![KubeDB + Stash](images/backup_stash_overview_kubedb_plus_stash.svg)

Fig : Sauvegarder les bases de données KubeDB à l'aide de Stash

# Comment stocker les sauvegardes et les restaurations de la base de données MariaDB

Stash 0.9.0+ prend en charge les opérations de sauvegarde et de restauration de nombreuses bases de données. Ce guide vous donnera un aperçu du fonctionnement du processus de sauvegarde et de restauration de la base de données MariaDB dans Stash.

## Sauvegarde logique

Stash prend en charge la prise [sauvegarde logique](https://mariadb.com/kb/en/backup-and-restore-overview/#logical-vs-physical-backups) des bases de données MariaDB utilisant [mysqldump](https://mariadb.com/kb/en/mysqldump/). Il s'agit du moyen le plus flexible d'effectuer une sauvegarde et une restauration, et constitue un bon choix lorsque la taille des données est relativement petite.

### Comment fonctionne la sauvegarde logique

Le diagramme suivant montre comment Stash effectue la sauvegarde logique d'une base de données MariaDB. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![MariaDB Backup Overview](images/backup_stash_overview_mariadb-logical-backup.svg)

Fig : Présentation de la sauvegarde logique MariaDB

Le processus de sauvegarde comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un secret avec les informations d'identification d'accès au backend où les données sauvegardées seront stockées.
2. Ensuite, elle crée un `Repository` crd qui spécifie les informations du backend ainsi que le secret contenant les informations d'identification pour accéder au backend.
3. Ensuite, elle crée un `BackupConfiguration` crd ciblant le [Liaison d'application](fr/concepts/appbinding.md) crd de la base de données souhaitée. Le `BackupConfiguration` l'objet spécifie également le `Task` à utiliser pour sauvegarder la base de données.
4. L'opérateur de la cachette surveille `BackupConfiguration` crd.
5. Une fois que l'opérateur Stash trouve un `BackupConfiguration` crd, il crée un CronJob avec le planning spécifié dans `BackupConfiguration` objet pour déclencher une sauvegarde périodiquement.
6. Sur le prochain slot planifié, le CronJob déclenche une sauvegarde en créant un `BackupSession` crd.
7. L'opérateur de cachette surveille également `BackupSession` crd.
8. Lorsqu'il trouve un `BackupSession` objet, il résout le problème respectif `Task` et `Function` et prépare une définition de travail à sauvegarder.
9. Ensuite, il crée le Job pour sauvegarder la base de données ciblée.
10. Le Job de sauvegarde lit les informations nécessaires pour se connecter à la base de données à partir du `AppBinding` crd. Il lit également les informations du backend et accède aux informations d'identification à partir de `Repository` crd et Storage Secret respectivement.
11. Ensuite, le Job vide la base de données ciblée et télécharge la sortie vers le backend. Stash redirige la sortie de la commande dump vers le processus de téléchargement. Par conséquent, le travail de sauvegarde ne nécessite pas un volume important pour contenir la totalité de la sortie de vidage.
12. Enfin, une fois la sauvegarde terminée, le Job envoie les métriques Prometheus au Pushgateway exécuté dans le pod de l'opérateur Stash. Il met également à jour le `BackupSession` et `Repository` statut pour refléter la procédure de sauvegarde.

### Comment fonctionne la restauration à partir d'une sauvegarde logique

Le diagramme suivant montre comment Stash restaure une base de données MariaDB à partir d'une sauvegarde logique. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Database Restore Overview](images/backup_stash_overview_mariadb-logical-restore.svg)

Fig : Présentation du processus de restauration logique MariaDB

Le processus de restauration comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `RestoreSession` crd ciblant le `AppBinding` de la base de données souhaitée où les données sauvegardées seront restaurées. Il précise également le `Repository` crd qui contient les informations du backend et le `Task` à utiliser pour restaurer la cible.
2. L'opérateur de la cachette surveille `RestoreSession` objet.
3. Une fois qu'il a trouvé un `RestoreSession` objet, il résout le problème respectif `Task` et `Function` et prépare une définition de travail à restaurer.
4. Ensuite, il crée le Job pour restaurer la cible.
5. Le Job lit les informations nécessaires pour se connecter à la base de données à partir des `AppBinding` crd. Il lit également les informations du backend et accède aux informations d'identification à partir de `Repository` crd et Storage Secret respectivement.
6. Ensuite, le travail télécharge les données sauvegardées depuis le backend et les injecte dans la base de données souhaitée. Stash redirige les données téléchargées vers l'outil de base de données respectif pour les injecter dans la base de données. Par conséquent, le travail de restauration ne nécessite pas un volume important pour télécharger l’intégralité des données de sauvegarde qu’il contient.
7. Enfin, une fois le processus de restauration terminé, le Job envoie les métriques Prometheus au Pushgateway et met à jour le `RestoreSession` état pour refléter l’achèvement de la restauration.

## Prochaines étapes

* Sauvegardez une base de données MariaDB autonome à l'aide de Stash en suivant le guide de [ici](fr/backup/stash/logical/standalone.md).
* Sauvegardez un cluster MariaDB à l'aide de Stash en suivant le guide de [ici](fr/backup/stash/logical/cluster.md).
* Configurez un modèle de sauvegarde générique pour toutes les bases de données MariaDB de votre cluster à l'aide de la sauvegarde automatique Stash en suivant le guide de [ici](fr/backup/stash/auto-backup.md).
* Personnalisez le processus de sauvegarde et de restauration de votre cluster en suivant les guides de [ici](fr/backup/stash/customization.md).

<!-- PAGE_START: distributed/opsrequest/horizontal_scale.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB distribuée à l'échelle horizontale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur Opsrequest pour mettre à l'échelle horizontalement un cluster MariaDB Galera distribué sur plusieurs clusters Kubernetes.

> **Note:** Tous les autres `OpsRequest` les opérations se comportent de manière cohérente dans un environnement distribué. Seulement `HorizontalScaling` comporte des considérations spécifiques au cluster abordées dans ce guide.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'une configuration Kubernetes multicluster avec OCM et KubeSlice configurés. Suivez le [Présentation de MariaDB distribuée](fr/distributed/overview.md) guide pour mettre en place l’infrastructure requise.
* Installer `KubeDB` Opérateur de communauté et d'entreprise dans votre cluster hub en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README). Assurez-vous d'activer la prise en charge OCM :

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Présentation de MariaDB distribuée](fr/distributed/overview.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle horizontale](fr/scaling/horizontal-scaling/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Appliquer une mise à l'échelle horizontale sur un cluster distribué

Ici, nous allons déployer un système distribué `MariaDB` Cluster Galera, puis appliquez une mise à l'échelle horizontale à l'aide de `MariaDBOpsRequest`.

### Déployer une stratégie de placement

Pour un cluster MariaDB distribué, le `PlacementPolicy` doit être créé avant de déployer la base de données. Il définit quel index de réplique est planifié sur quel cluster et agit comme limite supérieure pour la mise à l'échelle, le nombre de répliques en cours d'exécution peut être inférieur ou égal à n'importe quel nombre d'index totaux défini dans la politique.

> Remarque : Assurez-vous de spécifier correctement le mappage de chaque index de pod de base de données sur son cluster cible. Un cluster correspondant doit être défini pour chaque index de pod DB. Tout index manquant entraînera des erreurs de provisionnement.

Dans cet exemple, le `PlacementPolicy` est configuré avec **cinq** indices de réplique répartis sur deux clusters. Le cluster MariaDB démarrera avec **trois** répliques (indices `0`, `1`, `2`), et peut être étendu à **cinq** (indices `0`–`4`) sans modifier la politique.

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        replicaIndices:
          - 0
          - 2
          - 4
      - clusterName: demo-worker
        replicaIndices:
          - 1
          - 3
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Ici,

* `spec.clusterSpreadConstraint.distributionRules[].replicaIndices` spécifie quels index de réplica MariaDB sont planifiés sur ce cluster. `demo-controller` hébergera des répliques `0`, `2`, et `4`; `demo-worker` hébergera des répliques `1` et `3`.

Appliquer le `PlacementPolicy` sur le hub (`demo-controller`) grappe:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/placement-policy.yaml --context demo-controller
placementpolicy.apps.k8s.appscode.com/distributed-mariadb created
```

### Déployer un cluster MariaDB distribué

Dans cette section, nous allons déployer un cluster MariaDB Galera distribué avec la version `12.1.2`. Noter que `spec.distributed` est réglé sur `true` et `spec.replicas` est `3` ce qui est inférieur aux cinq indices définis dans le `PlacementPolicy`. L'opérateur créera uniquement des pods pour les index `0`, `1`, et `2`.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
spec:
  version: "12.1.2"
  distributed: true
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
      containers:
        - name: mariadb
          resources:
            requests:
              cpu: "200m"
              memory: "300Mi"
            limits:
              cpu: "200m"
              memory: "300Mi"
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/mariadb.yaml --context demo-controller
mariadb.kubedb.com/mariadb created
```

Attendez maintenant que la ressource `mariadb` passe au statut `Ready` :

```bash
$ kubectl get mariadb -n demo --context demo-controller
NAME             VERSION   STATUS   AGE
mariadb          11.5.2    Ready    2m36s
```

Vérifions le nombre de répliques de cette base de données à partir de l'objet MariaDB :

```bash
$ kubectl get mariadb -n demo mariadb -o json | jq '.spec.replicas'
3
```

Les pods sont répartis sur les clusters tels que définis par le `PlacementPolicy`. Indices `0` et `2` atterrir sur `demo-controller`; indice `1` atterrit sur `demo-worker`:

```bash
$ kubectl get pods -n demo --context demo-controller
NAME          READY   STATUS    RESTARTS   AGE
mariadb-0     3/3     Running   0          2m30s
mariadb-2     3/3     Running   0          2m30s

$ kubectl get pods -n demo --context demo-worker
NAME          READY   STATUS    RESTARTS   AGE
mariadb-1     3/3     Running   0          2m30s
```

Nous pouvons voir que le cluster comporte 3 pods. Nous sommes maintenant prêts à postuler `MariaDBOpsRequest` pour faire évoluer cette base de données.

## Augmenter les répliques

Ici, nous allons étendre les répliques de `3` à `5`. Parce que le `PlacementPolicy` définit déjà les indices `0`–`4`, aucune modification de la politique n'est requise : l'opérateur sait où placer les nouveaux pods.

### Créer une demande MariaDBOps

Afin d'augmenter les répliques, nous devons créer un `MariaDBOpsRequest` CR avec nos répliques souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer :

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-up
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: mariadb
  horizontalScaling:
    member : 5
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une mise à l'échelle horizontale sur `mariadb`.
* `spec.type` précise que nous effectuons `HorizontalScaling`.
* `spec.horizontalScaling.member` spécifie le nombre de réplicas souhaité après la mise à l'échelle. Cette valeur ne doit pas dépasser le nombre total d'indices définis dans le `PlacementPolicy` (5 dans cet exemple).

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/mdops-upscale.yaml --context demo-controller
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-up created
```

### Vérifier que les réplicas de cluster ont été mis à l'échelle avec succès

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour les répliques du `MariaDB` objet et créez les nouveaux pods sur les clusters spécifiés par le `PlacementPolicy`.

Attendons `MariaDBOpsRequest` être `Successful`:

```bash
$ watch kubectl get mariadbopsrequest -n demo --context demo-controller
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                        TYPE                STATUS       AGE
mdops-scale-horizontal-up   HorizontalScaling   Successful   18m
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Vérifions maintenant le nombre de répliques :

```bash
$ kubectl get mariadb -n demo mariadb -o json | jq '.spec.replicas'
5
```

Les deux nouveaux pods sont placés sur les clusters selon le `PlacementPolicy` — indice `4` sur `demo-controller` et index `3` sur `demo-worker`:

```bash
$ kubectl get pods -n demo --context demo-controller
NAME        READY   STATUS    RESTARTS   AGE
mariadb-0   3/3     Running   0          58m
mariadb-2   3/3     Running   0          55m
mariadb-4   3/3     Running   0          17m


$ kubectl get pods -n demo --context demo-worker
NAME        READY   STATUS    RESTARTS   AGE
mariadb-1   3/3     Running   0          57m
mariadb-3   3/3     Running   0          19m
```

De tous les résultats ci-dessus, nous pouvons voir que le cluster a désormais `5` répliques. Nous avons réussi à faire évoluer le cluster distribué MariaDB.

## Réduire les répliques

Ici, nous allons réduire les répliques de `5` à `3`. Le `PlacementPolicy` n'a pas besoin d'être modifié — l'opérateur supprimera les pods les plus indexés (`mariadb-3` et `mariadb-4`) et les pods restants continueront de s'exécuter comme défini par la stratégie.

### Créer une demande MariaDBOps

Afin de réduire le cluster, nous devons créer un `MariaDBOpsRequest` CR avec nos répliques souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer :

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-down
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: mariadb
  horizontalScaling:
    member: 3
```

Ici,

* `spec.databaseRef.name` précise que nous effectuons une réduction horizontale sur `mariadb`.
* `spec.type` précise que nous effectuons `HorizontalScaling`.
* `spec.horizontalScaling.member` spécifie le nombre de réplicas souhaité après la mise à l'échelle.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/mdops-downscale.yaml --context demo-controller
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-down created
```

### Vérifier que les réplicas de cluster ont été réduits avec succès

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour les répliques du `MariaDB` et supprimez les pods les plus indexés de leurs clusters respectifs.

Attendons `MariaDBOpsRequest` être `Successful`:

```bash
$ watch kubectl get mariadbopsrequest -n demo --context demo-controller
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                          TYPE               STATUS       AGE
mdops-scale-horizontal-down   HorizontalScaling  Successful   2m32s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Vérifions maintenant le nombre de répliques :

```bash
$ kubectl get mariadb -n demo mariadb -o json | jq '.spec.replicas'
3
```

Gousses `mariadb-3` et `mariadb-4` ont été supprimés de leurs clusters respectifs :

```bash
$ kubectl get pods -n demo --context demo-controller
NAME          READY   STATUS    RESTARTS   AGE
mariadb-0     3/3     Running   0          20m
mariadb-2     3/3     Running   0          20m

$ kubectl get pods -n demo --context demo-worker
NAME          READY   STATUS    RESTARTS   AGE
mariadb-1     3/3     Running   0          20m
```

De tous les résultats ci-dessus, nous pouvons voir que le cluster a désormais `3` répliques. Nous avons réussi à réduire le cluster distribué MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo mariadb --context demo-controller
$ kubectl delete mariadbopsrequest -n demo mdops-scale-horizontal-up mdops-scale-horizontal-down --context demo-controller
$ kubectl delete placementpolicy distributed-mariadb --context demo-controller
```

<!-- PAGE_START: scaling/horizontal-scaling/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB à échelle horizontale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour faire évoluer le cluster d'une base de données MariaDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Cluster MariaDB](fr/clustering/galera-cluster.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle horizontale](fr/scaling/horizontal-scaling/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Appliquer une mise à l'échelle horizontale sur le cluster

Ici, nous allons déployer un `MariaDB` cluster utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons lui appliquer une mise à l’échelle horizontale.

### Préparer la base de données du cluster MariaDB

Maintenant, nous allons déployer un `MariaDB` cluster avec version `12.1.2`.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer un cluster MariaDB. Ensuite, dans la section suivante, nous mettrons à l'échelle la base de données en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
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
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/horizontal-scaling/cluster/example/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    2m36s
```

Vérifions le nombre de répliques de cette base de données à partir de l'objet MariaDB, le nombre de pods dont dispose le petset,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.replicas'
3
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.replicas'
3
```

Nous pouvons voir dans les deux commandes que la base de données a 3 répliques dans le cluster.

En outre, nous pouvons vérifier les répliques du jeu de réplicas à partir d'une commande mariadb interne en les exécutant dans une réplique.

Nous devons d'abord obtenir le nom d'utilisateur et le mot de passe pour nous connecter à une instance mariadb,

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d
nrKuxni0wDSMrgwy
```

Connectons-nous maintenant à une instance mariadb et exécutons une commande interne mariadb pour vérifier le nombre de répliques,

```bash
$  kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "show status like 'wsrep_cluster_size';"
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
```

Nous pouvons voir à partir du résultat ci-dessus que le cluster a 3 nœuds.

Nous sommes maintenant prêts à appliquer le `MariaDBOpsRequest` CR pour faire évoluer cette base de données.

## Augmenter les répliques

Ici, nous allons mettre à l'échelle les répliques du jeu de réplicas pour atteindre le nombre de répliques souhaité après la mise à l'échelle.

#### Créer une demande MariaDBOps

Afin de faire évoluer les répliques du jeu de réplicas de la base de données, nous devons créer un `MariaDBOpsRequest` CR avec nos répliques souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-up
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: sample-mariadb
  horizontalScaling:
    member : 5
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle horizontale sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `HorizontalScaling` sur notre base de données.
* `spec.horizontalScaling.member` spécifie les répliques souhaitées après la mise à l'échelle.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/horizontal-scaling/cluster/example/mdops-upscale.yaml
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-up created
```

#### Vérifier que les réplicas de cluster ont été mis à l'échelle avec succès

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour les répliques de `MariaDB` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                        TYPE                STATUS       AGE
mdps-scale-horizontal    HorizontalScaling    Successful     106s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier le nombre de répliques de cette base de données à partir de l'objet MariaDB, le nombre de pods dont dispose le petset,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.replicas'
5
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.replicas'
5
```

Connectons-nous maintenant à une instance mariadb et exécutons une commande interne mariadb pour vérifier le nombre de répliques,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "show status like 'wsrep_cluster_size';"
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 5     |
+--------------------+-------+
```

À partir de toutes les sorties ci-dessus, nous pouvons voir que les répliques du cluster sont `5`. Cela signifie que nous avons réussi à faire évoluer les répliques du jeu de réplicas MariaDB.

### Réduire les répliques

Ici, nous allons réduire les répliques du cluster pour atteindre le nombre de répliques souhaité après la mise à l'échelle.

#### Créer une demande MariaDBOps

Afin de réduire le cluster de la base de données, nous devons créer un `MariaDBOpsRequest` CR avec nos répliques souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-down
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: sample-mariadb
  horizontalScaling:
    member : 3
```

Ici,

* `spec.databaseRef.name` précise que nous effectuons une opération de réduction horizontale sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `HorizontalScaling` sur notre base de données.
* `spec.horizontalScaling.replicas` spécifie les répliques souhaitées après la mise à l'échelle.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/horizontal-scaling/cluster/example/mdops-downscale.yaml
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-down created
```

#### Vérifiez que les réplicas de cluster ont été réduits avec succès

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour les répliques de `MariaDB` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                          TYPE                STATUS       AGE
mops-hscale-down-replicaset   HorizontalScaling   Successful   2m32s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier le nombre de répliques de cette base de données à partir de l'objet MariaDB, le nombre de pods dont dispose le petset,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.replicas' 
3
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.replicas'
3
```

Connectons-nous maintenant à une instance mariadb et exécutons une commande interne mariadb pour vérifier le nombre de répliques,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "show status like 'wsrep_cluster_size';"
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
```

À partir de toutes les sorties ci-dessus, nous pouvons voir que les répliques du cluster sont `3`. Cela signifie que nous avons réussi à réduire les répliques du jeu de réplicas MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo  mdops-scale-horizontal-up mdops-scale-horizontal-down
```

<!-- PAGE_START: scaling/horizontal-scaling/maxscale.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Échelle horizontale MaxScale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur de gestion des opérations pour faire évoluer le serveur MaxScale.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Réplication MariaDB](fr/clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle horizontale](fr/scaling/horizontal-scaling/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Appliquer une mise à l'échelle horizontale sur MaxScale Server

Ici, nous allons déployer un `MariaDB` cluster en mode réplication à l'aide d'une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer une mise à l'échelle horizontale sur `MaxScale` serveur.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer un cluster MariaDB en mode réplication. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-replication
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/md-replication.yaml
mariadb.kubedb.com/md-replication created
```

Attendez maintenant que `md-replication` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
md-replication   11.8.5   Ready    2m8s
```

Vérifions le nombre de répliques `Maxscale` a de l'objet MariaDB, ainsi que le nombre de répliques du petset,

```bash
$ kubectl get mariadb -n demo md-replication -o json | jq '.spec.topology.maxscale.replicas'
3
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.replicas'
3
```

Nous pouvons voir à partir des deux commandes que le `MaxScale` a 3 répliques dans le cluster.

## Augmenter les répliques

Ici, nous allons mettre à l'échelle les répliques du jeu de réplicas pour atteindre le nombre de répliques souhaité après la mise à l'échelle.

#### Créer une demande MariaDBOps

Afin de mettre à l'échelle les répliques du jeu de réplicas du `MaxScale` serveur, nous devons créer un `MariaDBOpsRequest` CR avec nos répliques souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-horizontal-scale-up
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: md-replication
  horizontalScaling:
    maxscale: true
    member: 4
```

Ici,

* `spec.type` précise que nous effectuons `HorizontalScaling` sur notre base de données.
* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle horizontale sur `md-replication` base de données.
* `spec.horizontalScaling.maxscale` spécifie que nous effectuons une opération de mise à l'échelle horizontale sur le serveur maxscale. Si faux, la mise à l'échelle horizontale s'effectue sur la base de données mariadb.
* `spec.horizontalScaling.member` spécifie les répliques souhaitées après la mise à l'échelle.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/horizontal-scaling/mx-hscale-up.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-horizontal-scale-up created
```

#### Vérifier que les réplicas de cluster ont été mis à l'échelle avec succès

Si tout se passe bien, `KubeDB` L'opérateur Ops-manager mettra à jour les répliques de `MaxScale` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                           TYPE                STATUS       AGE
maxscale-horizontal-scale-up   HorizontalScaling   Successful   2m31s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier le nombre de répliques de cette base de données à partir de l'objet MariaDB, le nombre de pods dont dispose le petset,

```bash
$ kubectl get mariadb -n demo md-replication -o json | jq '.spec.topology.maxscale.replicas'
4
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.replicas'
4
```

De toutes les sorties ci-dessus, nous pouvons voir que les répliques du `MaxScale` le serveur est `4`. Cela signifie que nous avons réussi à faire évoluer les répliques du serveur MaxScale.

### Réduire les répliques

Ici, nous allons réduire les répliques du cluster pour atteindre le nombre de répliques souhaité après la mise à l'échelle.

#### Créer une demande MariaDBOps

Afin de réduire les répliques du `MaxScale` serveur, nous devons créer un `MariaDBOpsRequest` CR avec nos répliques souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-horizontal-scale-down
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: md-replication
  horizontalScaling:
    maxscale: true
    member: 3
```

Ici,

* `spec.type` précise que nous effectuons `HorizontalScaling` sur notre base de données.
* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle horizontale sur `md-replication` base de données.
* `spec.horizontalScaling.maxscale` spécifie que nous effectuons une opération de mise à l'échelle horizontale sur le serveur maxscale. Si faux, la mise à l'échelle horizontale s'effectue sur la base de données mariadb.
* `spec.horizontalScaling.member` spécifie les répliques souhaitées après la mise à l'échelle.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/horizontal-scaling/mx-hscale-down.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-horizontal-scale-down created
```

#### Vérifiez que les réplicas de cluster ont été réduits avec succès

Si tout se passe bien, `KubeDB` L'opérateur Ops-manager mettra à jour les répliques de `MaxScale` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                             TYPE                STATUS       AGE
maxscale-horizontal-scale-down   HorizontalScaling   Successful   55s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier le nombre de répliques `MaxScale` le serveur dispose de l'objet MariaDB, le nombre de pods dont dispose le petset,

```bash
$ kubectl get mariadb -n demo md-replication -o json | jq '.spec.topology.maxscale.replicas'
3
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.replicas'
3
```

À partir de toutes les sorties ci-dessus, nous pouvons voir que les répliques du cluster sont `3`. Cela signifie que nous avons réussi à réduire les répliques du serveur MaxScale.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo md-replication
$ kubectl delete mariadbopsrequest -n demo  maxscale-horizontal-scale-up maxscale-horizontal-scale-down
$ kubectl delete ns demo
```

<!-- PAGE_START: scaling/horizontal-scaling/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle horizontale de MariaDB

Ce guide donnera un aperçu de la manière dont KubeDB Ops Manager évolue vers le haut ou vers le bas. `MariaDB Cluster`.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Comment fonctionne le processus de mise à l'échelle horizontale

Le diagramme suivant montre comment KubeDB Ops Manager évolue vers le haut ou vers le bas `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Horizontal scaling process of MariaDB](images/scaling_horizontal-scaling_overview_horizontal-scaling.jpg)

Fig : Processus de mise à l'échelle horizontale de MariaDB

Le processus de mise à l'échelle horizontale comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` Ressource personnalisée (CR).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CR.
3. Lorsque l'opérateur trouve un `MariaDB` CR, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Ensuite, afin d'augmenter l'échelle `MariaDB` base de données, l'utilisateur crée un `MariaDBOpsRequest` CR avec les informations souhaitées.
5. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CR.
6. Lorsqu'il trouve un `MariaDBOpsRequest` CR, il met en pause le `MariaDB` objet auquel fait référence le `MariaDBOpsRequest`. Ainsi, le `KubeDB` L’opérateur communautaire n’effectue aucune opération sur le `MariaDB` objet pendant le processus de mise à l’échelle horizontale.
7. Puis le `KubeDB` L'opérateur d'entreprise mettra à l'échelle les pods PetSet associés pour atteindre le nombre attendu de répliques défini dans le `MariaDBOpsRequest` CR.
8. Après avoir mis à l'échelle avec succès les répliques des pods PetSet, le `KubeDB` L'opérateur d'entreprise met à jour le nombre de répliques dans le `MariaDB` objet pour refléter l’état mis à jour.
9. Après la mise à l'échelle réussie du `MariaDB` répliques, les `KubeDB` L'opérateur d'entreprise reprend le `MariaDB` objet afin que le `KubeDB` L'opérateur communautaire reprend ses opérations habituelles.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la mise à l'échelle horizontale de la base de données MariaDB à l'aide de `MariaDBOpsRequest` CRD.

<!-- PAGE_START: scaling/vertical-scaling/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Cluster MariaDB à échelle verticale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour mettre à jour les ressources d'une base de données de cluster MariaDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Regroupement](fr/clustering/galera-cluster.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle verticale](fr/scaling/vertical-scaling/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Appliquer une mise à l'échelle verticale sur le cluster

Ici, nous allons déployer un `MariaDB` cluster utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons lui appliquer une mise à l’échelle verticale.

### Préparer le cluster MariaDB

Maintenant, nous allons déployer un `MariaDB` base de données cluster avec version `12.1.2`.

> Mise à l'échelle verticale pour `MariaDB Standalone` peut être effectué de la même manière que `MariaDB Cluster`. Retirez uniquement le `spec.replicas` champ du yaml ci-dessous pour déployer un MariaDB Standalone.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer une base de données de cluster MariaDB. Ensuite, dans la section suivante, nous mettrons à jour les ressources de la base de données en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
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
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION    STATUS     AGE
sample-mariadb    11.8.5     Ready     3m46s
```

Vérifions les ressources des conteneurs Pod,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "500m",
    "memory": "1Gi"
  },
  "requests": {
    "cpu": "500m",
    "memory": "1Gi"
  }
}
```

Vous pouvez voir que le pod dispose des ressources par défaut attribuées par l'opérateur KubeDB.

Nous sommes maintenant prêts à appliquer le `MariaDBOpsRequest` CR pour mettre à jour les ressources de cette base de données.

### Mise à l'échelle verticale

Ici, nous allons mettre à jour les ressources de la base de données pour répondre aux ressources souhaitées après la mise à l'échelle.

#### Créer une demande MariaDBOps

Afin de mettre à jour les ressources de la base de données, nous devons créer un `MariaDBOpsRequest` CR avec nos ressources souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-vscale
  namespace: demo
spec:
  type: VerticalScaling
  databaseRef:
    name: sample-mariadb
  verticalScaling:
    mariadb:
      resources:
        requests:
          memory: "1.2Gi"
          cpu: "0.6"
        limits:
          memory: "1.2Gi"
          cpu: "0.6"
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle verticale sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `VerticalScaling` sur notre base de données.
* `spec.VerticalScaling.mariadb` spécifie les ressources souhaitées après la mise à l'échelle.
* `spec.verticalScaling.mode` spécifie comment la mise à l'échelle est actionnée - `Restart` (par défaut, redémarre les Pods) ou `InPlace` (redimensionne les pods en cours d'exécution sans redémarrage, en revenant au redémarrage si un nœud ne peut pas accueillir les nouvelles ressources). Voir [Modes de mise à l'échelle verticale](fr/scaling/vertical-scaling/overview.md#vertical-scaling-modes).

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/mdops-vscale.yaml
mariadbopsrequest.ops.kubedb.com/mdops-vscale created
```

#### Vérifiez que les ressources du cluster MariaDB ont été mises à jour avec succès

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour les ressources de `MariaDB` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                     TYPE              STATUS       AGE
mdops-vscale        VerticalScaling      Successful    3m56s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier depuis l'un des Pod yaml si les ressources de la base de données ont été mises à jour pour répondre à l'état souhaité, vérifions,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "600m",
    "memory": "1288490188800m"
  },
  "requests": {
    "cpu": "600m",
    "memory": "1288490188800m"
  }
}
```

Le résultat ci-dessus vérifie que nous avons réussi à augmenter les ressources de la base de données MariaDB.

### Mise à l'échelle verticale sur place

Pour redimensionner les pods **sans redémarrage**, ensemble `spec.verticalScaling.mode` à `InPlace` dans le
`MariaDBOpsRequest`. L'opérateur redimensionne les conteneurs en cours d'exécution via Kubernetes `pods/resize`
sous-ressource et redémarre un Pod uniquement si son nœud ne peut pas accueillir les nouvelles ressources.

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-vscale-inplace
  namespace: demo
spec:
  type: VerticalScaling
  databaseRef:
    name: sample-mariadb
  verticalScaling:
    mode: InPlace
    mariadb:
      resources:
        requests:
          memory: "1.2Gi"
          cpu: "0.6"
        limits:
          memory: "1.2Gi"
          cpu: "0.6"
```

Appliquons-le de la même manière que ci-dessus :

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/mdops-vscale-inplace.yaml
mariadbopsrequest.ops.kubedb.com/mdops-vscale-inplace created
```

Les ressources sont mises à jour sans redémarrage du pod.

> **Note:** Pour un **distribué** `MariaDB` déploiement, un véritable redimensionnement sur place n'est pas possible, donc `InPlace` se dégrade automatiquement en `Restart`.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-vscale
```

<!-- PAGE_START: scaling/vertical-scaling/maxscale.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Serveur MaxScale à échelle verticale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur Ops-manager pour mettre à jour les ressources d'un serveur MaxScale.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [Réplication MariaDB](fr/clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle verticale](fr/scaling/vertical-scaling/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Appliquer la mise à l'échelle verticale sur MaxScale Server

Ici, nous allons déployer un `MariaDB` cluster en mode réplication à l'aide d'une version prise en charge par `KubeDB` opérateur. Ensuite, nous appliquerons une mise à l'échelle verticale sur `MaxScale` serveur.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer une base de données MariaDB en mode réplication. Ensuite, dans la section suivante, nous mettrons à jour les ressources du `MaxScale` serveur utilisant `MariaDBOpsRequest` CR. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-replication
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/md-replication.yaml
mariadb.kubedb.com/md-replication created
```

Attendez maintenant que `md-replication` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
md-replication   11.8.5   Ready    2m39s
```

Vérifions les ressources des conteneurs Pod,

```bash
$ kubectl get pod -n demo md-replication-mx-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "memory": "512Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "256Mi"
  }
}
```

Vous pouvez voir que le pod dispose des ressources par défaut attribuées par l'opérateur KubeDB.

Nous sommes maintenant prêts à appliquer le `MariaDBOpsRequest` CR pour mettre à jour les ressources de cette base de données.

### Mise à l'échelle verticale

Ici, nous allons mettre à jour les ressources de `MaxScale` serveur pour répondre aux ressources souhaitées après la mise à l’échelle.

#### Créer une demande MariaDBOps

Afin de mettre à jour les ressources de la base de données, nous devons créer un `MariaDBOpsRequest` CR avec nos ressources souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-vertical-scale
  namespace: demo
spec:
  type: VerticalScaling
  databaseRef:
    name: md-replication
  verticalScaling:
    maxscale:
      resources:
        requests:
          memory: "512Mi"
          cpu: "0.3"
        limits:
          memory: "1Gi"
          cpu: "0.6"
```

Ici,

* `spec.type` précise que nous effectuons `VerticalScaling` sur notre base de données.
* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle verticale sur `md-replication` base de données.
* `spec.VerticalScaling.maxscale` spécifie les ressources souhaitées du serveur maxscale après la mise à l'échelle.
* `spec.verticalScaling.mode` spécifie comment la mise à l'échelle est actionnée - `Restart` (par défaut, redémarre les Pods) ou `InPlace` (redimensionne les pods en cours d'exécution sans redémarrage, en revenant au redémarrage si un nœud ne peut pas accueillir les nouvelles ressources). Voir [Modes de mise à l'échelle verticale](fr/scaling/vertical-scaling/overview.md#vertical-scaling-modes).

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/vertical-scaling/mx-vscale.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-vertical-scale created
```

#### Vérifiez que les ressources du serveur MaxScale ont été mises à jour avec succès

Si tout se passe bien, `KubeDB` L’opérateur Ops-manager mettra à jour les ressources de `MariaDB` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo 

NAME                      TYPE              STATUS       AGE
maxscale-vertical-scale   VerticalScaling   Successful   3m8s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier à partir de l'un des Pod yaml si les ressources du serveur maxscale ont été mises à jour pour atteindre l'état souhaité, vérifions,

```bash
$ kubectl get pod -n demo md-replication-mx-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "600m",
    "memory": "1Gi"
  },
  "requests": {
    "cpu": "300m",
    "memory": "512Mi"
  }
}
```

Le résultat ci-dessus vérifie que nous avons réussi à augmenter les ressources de la base de données MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo md-replication
$ kubectl delete mariadbopsrequest -n demo maxscale-vertical-scale
$ kubectl delete ns demo
```

<!-- PAGE_START: scaling/vertical-scaling/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle verticale de MariaDB

Ce guide donnera un aperçu de la façon dont KubeDB Ops Manager évolue verticalement `MariaDB`.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)

## Comment fonctionne le processus de mise à l'échelle verticale

Le diagramme suivant montre comment KubeDB Ops Manager évolue vers le haut ou vers le bas `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Vertical scaling process of MariaDB](images/scaling_vertical-scaling_overview_vertical-scaling.jpg)

Fig : Processus de mise à l'échelle verticale de MariaDB

Le processus de mise à l'échelle verticale comprend les étapes suivantes :

1. Dans un premier temps, un utilisateur crée un `MariaDB` Ressource personnalisée (CR).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CR.
3. Lorsque l'opérateur trouve un `MariaDB` CR, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Ensuite, afin de mettre à jour les ressources(par exemple `CPU`, `Memory` etc.) du `MariaDB` base de données, l'utilisateur crée un `MariaDBOpsRequest` CR avec les informations souhaitées.
5. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CR.
6. Lorsqu'il trouve un `MariaDBOpsRequest` CR, il arrête le `MariaDB` objet auquel fait référence le `MariaDBOpsRequest`. Ainsi, le `KubeDB` L’opérateur communautaire n’effectue aucune opération sur le `MariaDB` objet pendant le processus de mise à l’échelle verticale.
7. Puis le `KubeDB` L'opérateur d'entreprise mettra à jour les ressources des pods PetSet pour atteindre l'état souhaité.
8. Après la mise à jour réussie des ressources de la réplique du PetSet, le `KubeDB` L'opérateur d'entreprise met à jour le `MariaDB` objet pour refléter l’état mis à jour.
9. Après la mise à jour réussie du `MariaDB` ressources, les `KubeDB` L'opérateur d'entreprise reprend le `MariaDB` objet afin que le `KubeDB` L'opérateur communautaire reprend ses opérations habituelles.

## Modes de mise à l'échelle verticale

KubeDB active la mise à l'échelle verticale dans l'un des deux modes, sélectionnés via le `spec.verticalScaling.mode`
domaine de la `MariaDBOpsRequest`:

* **`Restart`** (par défaut) : l'opérateur corrige le `PetSet` avec les nouvelles ressources et redémarre le
  Pods (un à la fois, respectant les règles de basculement de la base de données) afin qu'ils reviennent avec le processeur mis à jour
  et Mémoire. Cela fonctionne sur chaque cluster Kubernetes.
* **`InPlace`**: L'opérateur redimensionne les conteneurs en cours d'exécution en place à l'aide du Kubernetes
  [Redimensionnement du pod sur place](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/)
  (`pods/resize` sous-ressource) : pas de redémarrage du pod, la mise à l'échelle s'effectue donc sans temps d'arrêt ni basculement. Si un
  Le nœud ne peut pas accueillir les nouvelles ressources (le redimensionnement est signalé `Infeasible`), l'opérateur
  revient automatiquement au `Restart` comportement pour ce Pod. Pour un **distribué** `MariaDB`
  déploiement, le redimensionnement sur place n'est pas possible, donc `InPlace` se dégrade automatiquement en `Restart`.

Si `spec.verticalScaling.mode` est omis, la valeur par défaut est `Restart`.

> **Note:** `InPlace` le mode s'appuie sur Kubernetes `InPlacePodVerticalScaling` porte de fonctionnalité, qui est
> activé par défaut à partir de Kubernetes v1.33. Sur les clusters plus anciens, ou lorsque la porte de fonctionnalités est désactivée,
> utiliser `Restart` mode.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la mise à jour des ressources de la base de données MariaDB à l'aide de `MariaDBOpsRequest` CRD.

<!-- PAGE_START: backup/stash/logical/cluster.md -->
# Sauvegarder le cluster MariaDB géré par KubeDB à l'aide de Stash

Planque `v0.11.8+` prend en charge la sauvegarde et la restauration des bases de données MariaDB. Ce guide vous montrera comment effectuer une sauvegarde logique de votre cluster de bases de données MariaDB et les restaurer à l'aide de Stash.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installez l'opérateur KubeDB dans votre cluster à partir de [ici](https://kubedb.com/docs/latest/setup).
* Installez Stash dans votre cluster en suivant les étapes [ici](https://stash.run/docs/latest/setup/install/stash/).
* Installer la cachette `kubectl` plugin en suivant les étapes [ici](https://stash.run/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont Stash sauvegarde et restaure les bases de données MariaDB, veuillez consulter le guide suivant [ici](fr/backup/stash/overview.md).

Vous devez être familier avec les ressources personnalisées suivantes :

* [Liaison d'application](fr/concepts/appbinding.md)
* [Fonction](https://stash.run/docs/latest/concepts/crds/function/)
* [Tâche](https://stash.run/docs/latest/concepts/crds/task/)
* [BackupConfiguration](https://stash.run/docs/latest/concepts/crds/backupconfiguration/)
* [Session de sauvegarde](https://stash.run/docs/latest/concepts/crds/backupsession/)
* [Restaurer la session](https://stash.run/docs/latest/concepts/crds/restoresession/)

Pour garder les choses isolées, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel. Créer `demo` espace de noms si vous ne l’avez pas encore créé.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Préparer MariaDB

Dans cette section, nous allons déployer une base de données MariaDB à l'aide de KubeDB. Ensuite, nous allons y insérer quelques exemples de données.

### Déployer MariaDB à l'aide de KubeDB

Dans un premier temps, déployons une base de données MariaDB nommée `sample-mariadb` de 3 répliques.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
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
  deletionPolicy: WipeOut
```

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Cet objet MariaDB créera le PetSet, Secret, Service, etc. nécessaires pour la base de données. Vous pouvez facilement visualiser toutes les ressources créées par l'objet MariaDB en utilisant [ketall](https://github.com/corneliusweig/ketall) `kubectl` plugin comme ci-dessous,

```bash
$ kubectl get-all -n demo -l app.kubernetes.io/instance=sample-mariadb
NAME                                                  NAMESPACE  AGE
endpoints/sample-mariadb                              demo       28m  
endpoints/sample-mariadb-pods                         demo       28m  
persistentvolumeclaim/data-sample-mariadb-0           demo       28m  
pod/sample-mariadb-0                                  demo       28m  
secret/sample-mariadb-auth                            demo       28m  
serviceaccount/sample-mariadb                         demo       28m  
service/sample-mariadb                                demo       28m  
service/sample-mariadb-pods                           demo       28m  
appbinding.appcatalog.appscode.com/sample-mariadb     demo       28m  
controllerrevision.apps/sample-mariadb-7b7f58b68f     demo       28m  
petset.apps/sample-mariadb                       demo       28m  
poddisruptionbudget.policy/sample-mariadb             demo       28m  
rolebinding.rbac.authorization.k8s.io/sample-mariadb  demo       28m  
role.rbac.authorization.k8s.io/sample-mariadb         demo       28m
```

Maintenant, attendez que 3 pods de base de données entrent dans `Running` État,

```bash
$ kubectl get pod -n demo -l app.kubernetes.io/instance=sample-mariadb
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          2m7s
sample-mariadb-1   1/1     Running   0          101s
sample-mariadb-2   1/1     Running   0          81s
```

Une fois le pod de base de données installé `Running` état, vérifiez que les 3 nœuds ont rejoint le cluster.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

D'après le journal ci-dessus, nous pouvons voir que 3 nœuds sont prêts à accepter les connexions.

### Insérer des exemples de données

Maintenant, nous allons exécuter dans le pod de base de données et créer des exemples de données. Le `sample-mariadb` l'objet crée un secret contenant les informations d'identification de MariaDB et les définit comme variables d'environnement du pod `MYSQL_ROOT_USERNAME` et `MYSQL_ROOT_PASSWORD`.

Ici, nous allons utiliser l'utilisateur root (`MYSQL_ROOT_USERNAME`) informations d'identification `MYSQL_ROOT_PASSWORD` pour insérer les exemples de données. Maintenant, exécutons dans l'un des pods et insérons quelques exemples de données,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Let's create a database named "company"
MariaDB [(none)]>  create database company;
Query OK, 1 row affected (0.000 sec)

# Verify that the database has been created successfully
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Now, let's create a table called "employee" in the "company" table
MariaDB [(none)]> create table company.employees ( name varchar(50), salary int);
Query OK, 0 rows affected (0.018 sec)

# Verify that the table has been created successfully
MariaDB [(none)]> show tables in company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.007 sec)

# Now, let's insert a sample row in the table
MariaDB [(none)]> insert into company.employees values ('John Doe', 5000);
Query OK, 1 row affected (0.003 sec)

# Insert another sample row
MariaDB [(none)]> insert into company.employees values ('James William', 7000);
Query OK, 1 row affected (0.002 sec)

# Verify that the rows have been inserted into the table successfully
MariaDB [(none)]>  select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Nous avons déployé avec succès une base de données MariaDB et y avons inséré quelques exemples de données. Dans les sections suivantes, nous allons sauvegarder ces données à l'aide de Stash.

## Préparer la sauvegarde

Dans cette section, nous allons préparer les ressources nécessaires (c'est-à-dire les informations de connexion à la base de données, les informations backend, etc.) avant la sauvegarde.

### Vérifier que le module complémentaire Stash MariaDB est installé

Lorsque vous installez Stash, il installe automatiquement tous les modules complémentaires de base de données officiels. Vérifiez qu'il a installé les modules complémentaires MariaDB à l'aide de la commande suivante.

```bash
$ kubectl get tasks.stash.appscode.com | grep mariadb
mariadb-backup-11.8.5    35s
mariadb-restore-11.8.5   35s
```

### Assurer la liaison d'application

Stash doit savoir comment se connecter à la base de données. Un `AppBinding` fournit exactement cette information. Il contient les informations de service et secrètes de la base de données. Vous devez indiquer le respectif `AppBinding` comme cible de sauvegarde au lieu de la base de données elle-même.

Stash s'attend à ce que le secret de votre base de données ait `username` et `password` clés. Si le secret de votre base de données ne les contient pas, le `AppBinding` peut également aider ici. Vous pouvez spécifier un `secretTransforms` section avec le mappage entre les touches actuelles et les touches souhaitées.

Vous n'avez pas à vous soucier des liaisons d'application si vous utilisez KubeDB. Il crée une liaison d'application contenant les informations nécessaires lorsque vous déployez la base de données. Assurons-nous que la liaison d'application est créée par `KubeDB` opérateur.

```bash
$ kubectl get appbinding -n demo 
NAME             TYPE                 VERSION   AGE
sample-mariadb   kubedb.com/mariadb   11.8.5      62m
```

Nous avons une liaison d'application nommée de la même manière que le nom de la base de données `sample-mariadb`. Nous l'utiliserons plus tard pour nous connecter à cette base de données.

### Préparer le back-end

Nous allons stocker nos données sauvegardées dans un bucket GCS. Nous devons donc créer un secret avec les informations d'identification GCS et un `Repository` objet avec les informations du compartiment. Si vous souhaitez utiliser un autre backend, veuillez lire le document de configuration du backend correspondant à partir de [ici](https://stash.run/docs/latest/guides/backends/overview/).

**Créer un secret de stockage :**

Dans un premier temps, créons un secret appelé `gcs-secret` avec les informations d'identification d'accès à notre compartiment GCS souhaité,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Créer un référentiel :**

Maintenant, en Crète `Repository` objet avec les informations du compartiment souhaité. Ci-dessous se trouve le YAML de `Repository` objet que nous allons créer,

```yaml
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: gcs-repo
  namespace: demo
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: /demo/mariadb/sample-mariadb
    storageSecretName: gcs-secret
```

Créons le `Repository` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/repository.yaml
repository.stash.appscode.com/gcs-repo created
```

Nous sommes maintenant prêts à sauvegarder notre base de données dans le backend souhaité.

### Sauvegarde

Pour planifier une sauvegarde, nous devons créer un `BackupConfiguration` objet ciblant le respectif `AppBinding` de notre base de données souhaitée. Ensuite, Stash créera un CronJob pour sauvegarder périodiquement la base de données.

#### Créer une configuration de sauvegarde

Vous trouverez ci-dessous le YAML pour `BackupConfiguration` objet que nous allons utiliser pour sauvegarder le `sample-mariadb` base de données que nous avons déployée plus tôt,

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

Ici,

* `.spec.schedule` spécifie que nous souhaitons sauvegarder la base de données à intervalles de 5 minutes.
* `.spec.target.ref` fait référence à l'objet AppBinding qui contient les informations de connexion de notre base de données ciblée.

Créons le `BackupConfiguration` objet que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/backupconfiguration.yaml
backupconfiguration.stash.appscode.com/sample-mariadb-backup created
```

### Vérifier la configuration de la sauvegarde avec succès

Si tout se passe bien, la phase du `BackupConfiguration` devrait être `Ready`. Le `Ready` La phase indique que la configuration de la sauvegarde a réussi. Vérifions le `Phase` de la Configuration de Sauvegarde,

```bash
$ kubectl get backupconfiguration -n demo
NAME                    TASK                    SCHEDULE      PAUSED   PHASE      AGE
sample-mariadb-backup   mariadb-backup-11.8.5   */5 * * * *            Ready      11s
```

#### Vérifier CronJob

Stash créera un CronJob avec le calendrier spécifié dans `spec.schedule` domaine de `BackupConfiguration` objet.

Vérifiez que le CronJob a été créé à l'aide de la commande suivante,

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        15s             17s
```

#### Attendez la session de sauvegarde

Le `sample-mariadb-backup` CronJob déclenchera une sauvegarde sur chaque slot planifié en créant un `BackupSession` objet.

Maintenant, attendez qu'un calendrier apparaisse. Exécutez la commande suivante pour rechercher un `BackupSession` objet,

```bash
$ kubectl get backupsession -n demo -w
NAME                               INVOKER-TYPE          INVOKER-NAME            PHASE     AGE
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   24s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   75s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Succeeded   103s
```

Ici, la phase `Succeeded` signifie que le processus de sauvegarde s'est terminé avec succès.

#### Vérifier la sauvegarde

Maintenant, nous allons vérifier si les données sauvegardées sont présentes ou non dans le backend. Une fois la sauvegarde terminée, Stash mettra à jour les fichiers respectifs `Repository` objet pour refléter l’achèvement de la sauvegarde. Vérifiez que le référentiel `gcs-repo` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo gcs-repo
NAME       INTEGRITY   SIZE        SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
gcs-repo   true        1.327 MiB   1                60s                      8m
```

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons que les données sauvegardées ont été stockées dans `demo/mariadb/sample-mariadb` répertoire tel que spécifié par `.spec.backend.gcs.prefix` domaine de la `Repository` objet.

![Backup data in GCS Bucket](images/backup_stash_logical_cluster_sample-mariadb-backup.png)

Fig : Sauvegarder les données dans le compartiment GCS

> Remarque : Stash conserve toutes les données sauvegardées cryptées. Ainsi, les données du backend n’auront aucun sens tant qu’elles ne seront pas déchiffrées.

## Restaurer MariaDB

Si vous avez correctement suivi les sections précédentes, vous devriez avoir une sauvegarde logique réussie de votre base de données MariaDB. Nous allons maintenant montrer comment restaurer la base de données à partir des données sauvegardées.

### Restaurer dans la même base de données

Vous pouvez restaurer vos données dans la même base de données que celle à partir de laquelle vous avez sauvegardé ou dans une autre base de données du même cluster ou d'un cluster différent. Dans cette section, nous allons vous montrer comment restaurer dans la même base de données ce qui peut être nécessaire lorsque vous avez accidentellement supprimé des données de la base de données en cours d'exécution.

#### Suspendre temporairement la sauvegarde

Dans un premier temps, arrêtons d’effectuer toute sauvegarde supplémentaire de la base de données afin qu’aucune sauvegarde ne soit exécutée après la suppression des exemples de données. Nous allons mettre en pause le `BackupConfiguration` objet. Stash cessera d'effectuer toute sauvegarde supplémentaire lorsque le `BackupConfiguration` est en pause.

Faisons une pause `sample-mariadb-backup` Configuration de sauvegarde,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup --type="merge" --patch='{"spec": {"paused": true}}'
backupconfiguration.stash.appscode.com/sample-mariadb-backup patched
```

Ou vous pouvez utiliser Stash `kubectl` plugin pour mettre en pause la BackupConfiguration,

```bash
$ kubectl stash pause backup -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been paused successfully.
```

Vérifiez que le `BackupConfiguration` a été mis en pause,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup  mariadb-backup-11.8.5   */5 * * * *   true     Ready   26m
```

Remarquez le `PAUSED` colonne. Valeur `true` pour ce champ signifie que le `BackupConfiguration` a été mis en pause.

Stash suspendra également le CronJob concerné.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   True      0        2m59s           20m
```

#### Simuler une catastrophe

Maintenant, simulons un scénario de suppression accidentelle. Ici, nous allons exécuter dans le pod de base de données et supprimer le `company` base de données que nous avions créée précédemment.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# View current databases
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Let's delete the "company" database
MariaDB [(none)]> drop database company;
Query OK, 1 row affected (0.268 sec)

# Verify that the "company" database has been deleted
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

#### Créer une session de restauration

Pour restaurer la base de données, vous devez créer un `RestoreSession` objet pointant vers le `AppBinding` de la base de données ciblée.

Voici le YAML du `RestoreSession` objet que nous allons utiliser pour restaurer notre `sample-mariadb` base de données.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [latest]
```

Ici,

* `.spec.repository.name` spécifie l'objet Repository qui contient les informations backend dans lesquelles nos données sauvegardées ont été stockées.
* `.spec.target.ref` fait référence à l'AppBinding respectif du `sample-mariadb` base de données.
* `.spec.rules` spécifie que nous restaurons les données à partir du dernier instantané de sauvegarde de la base de données.

Créons le `RestoreSession` objet objet que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/restoresession.yaml
restoresession.stash.appscode.com/sample-mariadb-restore created
```

Une fois que vous avez créé le `RestoreSession` objet, Stash créera une tâche de restauration. Exécutez la commande suivante pour regarder la phase du `RestoreSession` objet,

```bash
$ kubectl get restoresession -n demo -w
NAME                     REPOSITORY   PHASE     AGE
sample-mariadb-restore   gcs-repo     Running   15s
sample-mariadb-restore   gcs-repo     Succeeded   18s
```

Le `Succeeded` Cette phase signifie que le processus de restauration s'est terminé avec succès.

#### Vérifier les données restaurées

Maintenant, exécutons le pod de base de données et vérifions si les données réelles ont été restaurées ou non,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Verify that the "company" database has been restored
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Verify that the tables of the "company" database have been restored
MariaDB [(none)]> show tables from company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.000 sec)

# Verify that the sample data of the "employees" table has been restored
MariaDB [(none)]> select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

Par conséquent, nous pouvons voir à partir du résultat ci-dessus que les données supprimées ont été restaurées avec succès à partir de la sauvegarde.

#### Reprendre la sauvegarde

Puisque nos données ont été restaurées avec succès, nous pouvons désormais reprendre notre processus de sauvegarde habituel. Reprendre le `BackupConfiguration` en utilisant la commande suivante,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup --type="merge" --patch='{"spec": {"paused": false}}'
backupconfiguration.stash.appscode.com/sample-mariadb-backup patched
```

Ou vous pouvez utiliser le Stash `kubectl` plugin pour reprendre le `BackupConfiguration`,

```bash
$ kubectl stash resume -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been resumed successfully.
```

Vérifiez que le `BackupConfiguration` a été repris,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                    TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup   mariadb-backup-11.8.5   */5 * * * *   false    Ready   29m
```

Ici, `false` dans le `PAUSED` La colonne signifie que la sauvegarde a été reprise avec succès. Le CronJob devrait également être repris maintenant.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        2m59s           29m
```

Ici, `False` dans le `SUSPEND` La colonne signifie que le CronJob n'est plus suspendu et se déclenchera lors de la prochaine planification.

### Restaurer dans une base de données différente du même espace de noms

Si vous souhaitez restaurer les données sauvegardées dans une autre base de données du même espace de noms, vous devez utiliser le `AppBinding` de la base de données souhaitée. Ensuite, vous devez créer le `RestoreSession` pointant vers le nouveau `AppBinding`.

### Restaurer dans un espace de noms différent

Si vous souhaitez restaurer dans un espace de noms différent du même cluster, vous devez créer le référentiel, backend Secret dans l'espace de noms souhaité. Vous pouvez utiliser [Plugin Kubectl de cache](https://stash.run/docs/latest/guides/cli/kubectl-plugin/) pour copier facilement les ressources dans un nouvel espace de noms. Ensuite, vous devez créer le `RestoreSession` objet dans l'espace de noms souhaité pointant vers le référentiel, AppBinding de cet espace de noms.

### Restaurer dans un cluster différent

Si vous souhaitez restaurer dans un autre cluster, vous devez installer Stash dans le cluster souhaité. Ensuite, vous devez également installer le module complémentaire Stash MariaDB dans ce cluster. Ensuite, vous devez créer le référentiel, backend Secret, AppBinding, dans le cluster souhaité. Enfin, vous devez créer le `RestoreSession` objet dans le cluster souhaité pointant vers le référentiel, AppBinding de ce cluster.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete -n demo backupconfiguration sample-mariadb-backup
kubectl delete -n demo restoresession sample-mariadb-restore
kubectl delete -n demo repository gcs-repo
# delete the database resources
kubectl delete ns demo
```

<!-- PAGE_START: backup/stash/logical/standalone.md -->
# Sauvegarder une instance MariaDB autonome gérée par KubeDB avec Stash

Planque `v0.11.8+` prend en charge la sauvegarde et la restauration des bases de données MariaDB. Ce guide vous montrera comment effectuer une sauvegarde logique de vos bases de données MariaDB et les restaurer à l'aide de Stash.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installez l'opérateur KubeDB dans votre cluster à partir de [ici](https://kubedb.com/docs/latest/setup).
* Installez Stash dans votre cluster en suivant les étapes [ici](https://stash.run/docs/latest/setup/install/stash/).
* Installer la cachette `kubectl` plugin en suivant les étapes [ici](https://stash.run/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont Stash sauvegarde et restaure les bases de données MariaDB, veuillez consulter le guide suivant [ici](fr/backup/stash/overview.md).

Vous devez être familier avec les ressources personnalisées suivantes :

* [Liaison d'application](https://kubedb.com/docs/v2026.7.10/guides/elasticsearch/concepts/appbinding/)
* [Fonction](https://stash.run/docs/latest/concepts/crds/function/)
* [Tâche](https://stash.run/docs/latest/concepts/crds/task/)
* [BackupConfiguration](https://stash.run/docs/latest/concepts/crds/backupconfiguration/)
* [Session de sauvegarde](https://stash.run/docs/latest/concepts/crds/backupsession/)
* [Restaurer la session](https://stash.run/docs/latest/concepts/crds/restoresession/)

Pour garder les choses isolées, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel. Créer `demo` espace de noms si vous ne l’avez pas encore créé.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Préparer MariaDB

Dans cette section, nous allons déployer une base de données MariaDB à l'aide de KubeDB. Ensuite, nous allons y insérer quelques exemples de données.

### Déployer MariaDB à l'aide de KubeDB

Dans un premier temps, déployons une base de données autonome MariaDB nommée `sample-mariadb using` [KubeDB](https://kubedb.com/).

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 1
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

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Cet objet MariaDB créera le PetSet, Secret, Service etc. nécessaire pour la base de données. Vous pouvez facilement visualiser toutes les ressources créées par l'objet MariaDB en utilisant [ketall](https://github.com/corneliusweig/ketall) `kubectl` plugin comme ci-dessous,

```bash
$ kubectl get-all -n demo -l app.kubernetes.io/instance=sample-mariadb
NAME                                                  NAMESPACE  AGE
endpoints/sample-mariadb                              demo       28m  
endpoints/sample-mariadb-pods                         demo       28m  
persistentvolumeclaim/data-sample-mariadb-0           demo       28m  
pod/sample-mariadb-0                                  demo       28m  
secret/sample-mariadb-auth                            demo       28m  
serviceaccount/sample-mariadb                         demo       28m  
service/sample-mariadb                                demo       28m  
service/sample-mariadb-pods                           demo       28m  
appbinding.appcatalog.appscode.com/sample-mariadb     demo       28m  
controllerrevision.apps/sample-mariadb-7b7f58b68f     demo       28m  
petset.apps/sample-mariadb                       demo       28m  
poddisruptionbudget.policy/sample-mariadb             demo       28m  
rolebinding.rbac.authorization.k8s.io/sample-mariadb  demo       28m  
role.rbac.authorization.k8s.io/sample-mariadb         demo       28m
```

Maintenant, attendez le pod de la base de données `sample-mariadb-0` entrer dans `Running` État,

```bash
$ kubectl get pod -n demo sample-mariadb-0
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          29m
```

Une fois le pod de base de données installé `Running` état, vérifiez que la base de données est prête à accepter les connexions.

```bash
$ kubectl logs -n demo sample-mariadb-0
2021-02-22  9:41:37 0 [Note] Reading of all Master_info entries succeeded
2021-02-22  9:41:37 0 [Note] Added new Master_info '' to hash table
2021-02-22  9:41:37 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

À partir du journal ci-dessus, nous pouvons voir que la base de données est prête à accepter les connexions.

### Insérer des exemples de données

Maintenant, nous allons exécuter dans le pod de base de données et créer des exemples de données. Le `sample-mariadb` l'objet crée un secret contenant les informations d'identification de MariaDB et les définit comme variables d'environnement du pod `MYSQL_ROOT_USERNAME` et `MYSQL_ROOT_PASSWORD`.

Ici, nous allons utiliser l'utilisateur root (`MYSQL_ROOT_USERNAME`) informations d'identification `MYSQL_ROOT_PASSWORD` pour insérer les exemples de données. Maintenant, exécutons dans le pod de base de données et insérons quelques exemples de données,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Let's create a database named "company"
MariaDB [(none)]>  create database company;
Query OK, 1 row affected (0.000 sec)

# Verify that the database has been created successfully
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Now, let's create a table called "employee" in the "company" table
MariaDB [(none)]> create table company.employees ( name varchar(50), salary int);
Query OK, 0 rows affected (0.018 sec)

# Verify that the table has been created successfully
MariaDB [(none)]> show tables in company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.007 sec)

# Now, let's insert a sample row in the table
MariaDB [(none)]> insert into company.employees values ('John Doe', 5000);
Query OK, 1 row affected (0.003 sec)

# Insert another sample row
MariaDB [(none)]> insert into company.employees values ('James William', 7000);
Query OK, 1 row affected (0.002 sec)

# Verify that the rows have been inserted into the table successfully
MariaDB [(none)]>  select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Nous avons déployé avec succès une base de données MariaDB et y avons inséré quelques exemples de données. Dans les sections suivantes, nous allons sauvegarder ces données à l'aide de Stash.

## Préparer la sauvegarde

Dans cette section, nous allons préparer les ressources nécessaires (c'est-à-dire les informations de connexion à la base de données, les informations backend, etc.) avant la sauvegarde.

### Vérifier que le module complémentaire Stash MariaDB est installé

Lorsque vous installez Stash, il installe automatiquement tous les modules complémentaires de base de données officiels. Vérifiez qu'il a installé les modules complémentaires MariaDB à l'aide de la commande suivante.

```bash
$ kubectl get tasks.stash.appscode.com | grep mariadb
mariadb-backup-10.6.23    35s
mariadb-backup-10.6.23   35s
```

### Assurer la liaison d'application

Stash doit savoir comment se connecter à la base de données. Un `AppBinding` fournit exactement cette information. Il contient les informations de service et secrètes de la base de données. Vous devez indiquer le respectif `AppBinding` comme cible de sauvegarde au lieu de la base de données elle-même.

Stash s'attend à ce que le secret de votre base de données ait `username` et `password` clés. Si le secret de votre base de données ne les contient pas, le `AppBinding` peut également aider ici. Vous pouvez spécifier un `secretTransforms` section avec le mappage entre les touches actuelles et les touches souhaitées.

Vous n'avez pas à vous soucier des liaisons d'application si vous utilisez KubeDB. Il crée une liaison d'application contenant les informations nécessaires lorsque vous déployez la base de données. Assurons-nous que la liaison d'application est créée par `KubeDB` opérateur.

```bash
$ kubectl get appbinding -n demo 
NAME             TYPE                 VERSION   AGE
sample-mariadb   kubedb.com/mariadb   11.8.5      62m
```

Nous avons une liaison d'application nommée de la même manière que le nom de la base de données `sample-mariadb`. Nous l'utiliserons plus tard pour nous connecter à cette base de données.

### Préparer le back-end

Nous allons stocker nos données sauvegardées dans un bucket GCS. Nous devons donc créer un secret avec les informations d'identification GCS et un `Repository` objet avec les informations du compartiment. Si vous souhaitez utiliser un autre backend, veuillez lire le document de configuration du backend correspondant à partir de [ici](https://stash.run/docs/latest/guides/backends/overview/).

**Créer un secret de stockage :**

Dans un premier temps, créons un secret appelé `gcs-secret` avec les informations d'identification d'accès à notre compartiment GCS souhaité,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Créer un référentiel :**

Maintenant, en Crète `Repository` objet avec les informations du compartiment souhaité. Ci-dessous se trouve le YAML de `Repository` objet que nous allons créer,

```yaml
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: gcs-repo
  namespace: demo
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: /demo/mariadb/sample-mariadb
    storageSecretName: gcs-secret
```

Créons le `Repository` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/repository.yaml
repository.stash.appscode.com/gcs-repo created
```

Nous sommes maintenant prêts à sauvegarder notre base de données dans le backend souhaité.

### Sauvegarde

Pour planifier une sauvegarde, nous devons créer un `BackupConfiguration` objet ciblant le respectif `AppBinding` de notre base de données souhaitée. Ensuite, Stash créera un CronJob pour sauvegarder périodiquement la base de données.

#### Créer une configuration de sauvegarde

Vous trouverez ci-dessous le YAML pour `BackupConfiguration` objet que nous allons utiliser pour sauvegarder le `sample-mariadb` base de données que nous avons déployée plus tôt,

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

Ici,

* `.spec.schedule` spécifie que nous souhaitons sauvegarder la base de données à intervalles de 5 minutes.
* `.spec.target.ref` fait référence à l'objet AppBinding qui contient les informations de connexion de notre base de données ciblée.

Créons le `BackupConfiguration` objet que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/backupconfiguration.yaml
backupconfiguration.stash.appscode.com/sample-mariadb-backup created
```

#### Vérifier la configuration de la sauvegarde avec succès

Si tout se passe bien, la phase du `BackupConfiguration` devrait être `Ready`. Le `Ready` La phase indique que la configuration de la sauvegarde a réussi. Vérifions le `Phase` de la Configuration de Sauvegarde,

```bash
$ kubectl get backupconfiguration -n demo
NAME                    TASK                    SCHEDULE      PAUSED   PHASE      AGE
sample-mariadb-backup   mariadb-backup-10.6.23   */5 * * * *            Ready      11s
```

#### Vérifier CronJob

Stash créera un CronJob avec le calendrier spécifié dans `spec.schedule` domaine de `BackupConfiguration` objet.

Vérifiez que le CronJob a été créé à l'aide de la commande suivante,

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        15s             17s
```

#### Attendez la session de sauvegarde

Le `sample-mariadb-backup` CronJob déclenchera une sauvegarde sur chaque slot planifié en créant un `BackupSession` objet.

Maintenant, attendez qu'un calendrier apparaisse. Exécutez la commande suivante pour rechercher un `BackupSession` objet,

```bash
$ kubectl get backupsession -n demo -w
NAME                               INVOKER-TYPE          INVOKER-NAME            PHASE     AGE
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   24s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   75s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Succeeded   103s
```

Ici, la phase `Succeeded` signifie que le processus de sauvegarde s'est terminé avec succès.

#### Vérifier la sauvegarde

Maintenant, nous allons vérifier si les données sauvegardées sont présentes ou non dans le backend. Une fois la sauvegarde terminée, Stash mettra à jour les fichiers respectifs `Repository` objet pour refléter l’achèvement de la sauvegarde. Vérifiez que le référentiel `gcs-repo` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo gcs-repo
NAME       INTEGRITY   SIZE        SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
gcs-repo   true        1.327 MiB   1                60s                      8m
```

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons que les données sauvegardées ont été stockées dans `demo/mariadb/sample-mariadb` répertoire tel que spécifié par `.spec.backend.gcs.prefix` domaine de la `Repository` objet.

![Backup data in GCS Bucket](images/backup_stash_logical_standalone_sample-mariadb-backup.png)

Fig : Sauvegarder les données dans le compartiment GCS

> Remarque : Stash conserve toutes les données sauvegardées cryptées. Ainsi, les données du backend n’auront aucun sens tant qu’elles ne seront pas déchiffrées.

## Restaurer MariaDB

Si vous avez correctement suivi les sections précédentes, vous devriez avoir une sauvegarde logique réussie de votre base de données MariaDB. Nous allons maintenant montrer comment restaurer la base de données à partir des données sauvegardées.

### Restaurer dans la même base de données

Vous pouvez restaurer vos données dans la même base de données que celle à partir de laquelle vous avez sauvegardé ou dans une autre base de données du même cluster ou d'un cluster différent. Dans cette section, nous allons vous montrer comment restaurer dans la même base de données ce qui peut être nécessaire lorsque vous avez accidentellement supprimé des données de la base de données en cours d'exécution.

#### Suspendre temporairement la sauvegarde

Dans un premier temps, arrêtons d’effectuer toute sauvegarde supplémentaire de la base de données afin qu’aucune sauvegarde ne soit exécutée après la suppression des exemples de données. Nous allons mettre en pause le `BackupConfiguration` objet. Stash cessera d'effectuer toute sauvegarde supplémentaire lorsque le `BackupConfiguration` est en pause.

Faisons une pause `sample-mariadb-backup` Configuration de sauvegarde,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup--type="merge" --patch='{"spec": {"paused": true}}'
backupconfiguration.stash.appscode.com/sample-mgo-rs-backup patched
```

Ou vous pouvez utiliser le Stash `kubectl` plugin pour mettre en pause le `BackupConfiguration`,

```bash
$ kubectl stash pause backup -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been paused successfully.
```

Vérifiez que le `BackupConfiguration` a été mis en pause,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup  mariadb-backup-10.6.23   */5 * * * *   true     Ready   26m
```

Remarquez le `PAUSED` colonne. Valeur `true` pour ce champ signifie que le `BackupConfiguration` a été mis en pause.

Stash suspendra également le CronJob concerné.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   True      0        2m59s           20m
```

#### Simuler une catastrophe

Maintenant, simulons un scénario de suppression accidentelle. Ici, nous allons exécuter dans le pod de base de données et supprimer le `company` base de données que nous avions créée précédemment.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# View current databases
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Let's delete the "company" database
MariaDB [(none)]> drop database company;
Query OK, 1 row affected (0.268 sec)

# Verify that the "company" database has been deleted
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

#### Créer une session de restauration

Pour restaurer la base de données, vous devez créer un `RestoreSession` objet pointant vers le `AppBinding` de la base de données ciblée.

Voici le YAML du `RestoreSession` objet que nous allons utiliser pour restaurer notre `sample-mariadb` base de données.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  task:
    name: mariadb-backup-10.6.23
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [latest]
```

Ici,

* `.spec.task.name` spécifie le nom de l'objet Task qui spécifie les fonctions nécessaires et leur ordre d'exécution pour restaurer une base de données MariaDB.
* `.spec.repository.name` spécifie l'objet Repository qui contient les informations backend dans lesquelles nos données sauvegardées ont été stockées.
* `.spec.target.ref` fait référence à l'AppBinding respectif du `sample-mariadb` base de données.
* `.spec.rules` spécifie que nous restaurons les données à partir du dernier instantané de sauvegarde de la base de données.

Créons le `RestoreSession` objet objet que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/restoresession.yaml
restoresession.stash.appscode.com/sample-mariadb-restore created
```

Une fois que vous avez créé le `RestoreSession` objet, Stash créera une tâche de restauration. Exécutez la commande suivante pour regarder la phase du `RestoreSession` objet,

```bash
$ kubectl get restoresession -n demo -w
NAME                     REPOSITORY   PHASE     AGE
sample-mariadb-restore   gcs-repo     Running   15s
sample-mariadb-restore   gcs-repo     Succeeded   18s
```

Le `Succeeded` Cette phase signifie que le processus de restauration s'est terminé avec succès.

#### Vérifier les données restaurées

Maintenant, exécutons le pod de base de données et vérifions si les données réelles ont été restaurées ou non,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Verify that the "company" database has been restored
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Verify that the tables of the "company" database have been restored
MariaDB [(none)]> show tables from company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.000 sec)

# Verify that the sample data of the "employees" table has been restored
MariaDB [(none)]> select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

Par conséquent, nous pouvons voir à partir du résultat ci-dessus que les données supprimées ont été restaurées avec succès à partir de la sauvegarde.

#### Reprendre la sauvegarde

Puisque nos données ont été restaurées avec succès, nous pouvons désormais reprendre notre processus de sauvegarde habituel. Reprendre le `BackupConfiguration` en utilisant la commande suivante,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup --type="merge" --patch='{"spec": {"paused": false}}'
backupconfiguration.stash.appscode.com/sample-mariadb-backup patched
```

Ou vous pouvez utiliser le Stash `kubectl` plugin pour reprendre le `BackupConfiguration`,

```bash
$ kubectl stash resume -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been resumed successfully.
```

Vérifiez que le `BackupConfiguration` a été repris,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                    TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup   mariadb-backup-10.6.23   */5 * * * *   false    Ready   29m
```

Ici, `false` dans le `PAUSED` La colonne signifie que la sauvegarde a été reprise avec succès. Le CronJob devrait également être repris maintenant.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        2m59s           29m
```

Ici, `False` dans le `SUSPEND` La colonne signifie que le CronJob n'est plus suspendu et se déclenchera lors de la prochaine planification.

### Restaurer dans une base de données différente du même espace de noms

Si vous souhaitez restaurer les données sauvegardées dans une autre base de données du même espace de noms, vous devez utiliser le `AppBinding` de la base de données souhaitée. Ensuite, vous devez créer le `RestoreSession` pointant vers le nouveau `AppBinding`.

### Restaurer dans un espace de noms différent

Si vous souhaitez restaurer dans un espace de noms différent du même cluster, vous devez créer le référentiel, backend Secret dans l'espace de noms souhaité. Vous pouvez utiliser [Plugin Kubectl de cache](https://stash.run/docs/latest/guides/cli/kubectl-plugin/) pour copier facilement les ressources dans un nouvel espace de noms. Ensuite, vous devez créer le `RestoreSession` objet dans l'espace de noms souhaité pointant vers le référentiel, AppBinding de cet espace de noms.

### Restaurer dans un cluster différent

Si vous souhaitez restaurer dans un autre cluster, vous devez installer Stash dans le cluster souhaité. Ensuite, vous devez également installer le module complémentaire Stash MariaDB dans ce cluster. Ensuite, vous devez créer le référentiel, backend Secret, AppBinding, dans le cluster souhaité. Enfin, vous devez créer le `RestoreSession` objet dans le cluster souhaité pointant vers le référentiel, AppBinding de ce cluster.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete -n demo backupconfiguration sample-mariadb-backup
kubectl delete -n demo restoresession sample-mariadb-restore
kubectl delete -n demo repository gcs-repo
# delete the database resources
kubectl delete ns demo
```

<!-- PAGE_START: distributed/autoscaler/compute/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique de la ressource de calcul d'un cluster MariaDB distribué

Ce guide vous montrera comment utiliser `KubeDB` pour mettre à l'échelle automatiquement les ressources de calcul, c'est-à-dire le processeur et la mémoire d'un cluster MariaDB Galera distribué déployé sur plusieurs clusters Kubernetes.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'une configuration Kubernetes multicluster avec OCM et KubeSlice configurés. Suivez le [Présentation de MariaDB distribuée](fr/distributed/overview.md) guide pour mettre en place l’infrastructure requise.
* Installer `KubeDB` Opérateur de communauté, Ops-Manager et Autoscaler dans votre cluster hub en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README). Assurez-vous d'activer la prise en charge OCM :

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* Installer `Metrics Server` depuis [ici](https://github.com/kubernetes-sigs/metrics-server#installation)
* Installez Prometheus dans chaque cluster de rayons. L'autoscaler interroge le point de terminaison Prometheus par cluster (configuré dans le `PlacementPolicy`) pour collecter des métriques d'utilisation des ressources. Vous pouvez l'installer à partir de [ici](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle automatique du calcul MariaDB distribué](fr/distributed/autoscaler/compute/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Mise à l'échelle automatique de la base de données de cluster distribué

Ici, nous allons déployer un système distribué `MariaDB` Cluster Galera utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBAutoscaler` pour configurer la mise à l'échelle automatique.

### Déployer une stratégie de placement

Vous trouverez ci-dessous le YAML du `PlacementPolicy` que nous allons créer. Il distribue 3 réplicas sur deux clusters :

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        replicaIndices:
          - 0
          - 2
      - clusterName: demo-worker
        replicaIndices:
          - 1
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Ici,

* `spec.clusterSpreadConstraint.distributionRules[].replicaIndices` spécifie quels index de réplica MariaDB sont planifiés sur ce cluster. Ici `demo-controller` héberge des répliques `0` et `2`, et `demo-worker` réplique d'hôtes `1`.

Appliquer le `PlacementPolicy` sur le hub (`demo-controller`) grappe:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/compute/cluster/examples/placement-policy.yaml --context demo-controller
placementpolicy.apps.k8s.appscode.com/distributed-mariadb created
```

### Déployer un cluster MariaDB distribué

Dans cette section, nous allons déployer un cluster MariaDB Galera distribué avec la version `12.1.2`. Ensuite, dans la section suivante, nous configurerons la mise à l'échelle automatique pour cette base de données en utilisant `MariaDBAutoscaler` CRD.

Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer. Noter que `spec.distributed` est réglé sur `true` et le `PlacementPolicy` est référencé via `spec.podTemplate.spec.podPlacementPolicy`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  distributed: true
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
      containers:
      - name: mariadb
        resources:
          requests:
            cpu: "200m"
            memory: "300Mi"
          limits:
            cpu: "200m"
            memory: "300Mi"
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CRO que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/compute/cluster/examples/sample-mariadb.yaml --context demo-controller
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo --context demo-controller
NAME             VERSION   STATUS   AGE
sample-mariadb   11.5.2   Ready    14m
```

Les pods sont répartis sur les clusters tels que définis par le `PlacementPolicy`:

```bash
$ kubectl get pod -n demo --context demo-controller
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   3/3     Running   0          14m
sample-mariadb-2   3/3     Running   0          14m

$ kubectl get pod -n demo --context demo-worker
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-1   3/3     Running   0          14m
```

Vérifions les ressources des conteneurs Pod,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json --context demo-worker | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

Vérifions les ressources MariaDB,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json --context demo-controller | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

Vous pouvez voir à partir des résultats ci-dessus que les ressources sont les mêmes que celles que nous avons attribuées lors du déploiement de mariadb.

Nous sommes maintenant prêts à appliquer le `MariaDBAutoscaler` CRO pour configurer la mise à l'échelle automatique pour cette base de données.

### Mise à l'échelle automatique des ressources de calcul

Ici, nous allons configurer la mise à l'échelle automatique des ressources de calcul à l'aide d'un objet MariaDBAutoscaler.

#### Créer un objet MariaDBAutoscaler

Afin de configurer la mise à l'échelle automatique des ressources de calcul pour ce cluster de bases de données distribuées, nous devons créer un `MariaDBAutoscaler` CRO avec notre configuration souhaitée. Vous trouverez ci-dessous le YAML du `MariaDBAutoscaler` objet que nous allons créer,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-compute
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  opsRequestOptions:
    timeout: 3m
    apply: IfReady
  compute:
    mariadb:
      trigger: "On"
      podLifeTimeThreshold: 5m
      resourceDiffPercentage: 20
      minAllowed:
        cpu: 250m
        memory: 400Mi
      maxAllowed:
        cpu: 1
        memory: 1Gi
      containerControlledValues: "RequestsAndLimits"
      controlledResources: ["cpu", "memory"]
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle des ressources de calcul sur `sample-mariadb` base de données.
* `spec.compute.mariadb.trigger` spécifie que la mise à l'échelle automatique du calcul est activée pour cette base de données.
* `spec.compute.mariadb.podLifeTimeThreshold` spécifie la durée de vie minimale d'au moins un des pods pour lancer une mise à l'échelle verticale.
* `spec.compute.mariadb.resourceDiffPercentage` spécifie la différence de ressource minimale en pourcentage. La valeur par défaut est de 10 %.
  Si la différence entre les ressources actuelles et recommandées est inférieure à ResourceDiffPercentage, l’opérateur Autoscaler ignorera la mise à jour.
* `spec.compute.mariadb.minAllowed` spécifie les ressources minimales autorisées pour la base de données.
* `spec.compute.mariadb.maxAllowed` spécifie les ressources maximales autorisées pour la base de données.
* `spec.compute.mariadb.controlledResources` spécifie les ressources contrôlées par l'autoscaler.
* `spec.compute.mariadb.containerControlledValues` spécifie quelles valeurs de ressources doivent être contrôlées. La valeur par défaut est « RequestsAndLimits ».
* `spec.opsRequestOptions.apply` a deux valeurs prises en charge : `IfReady` & `Always`.
  Utiliser `IfReady` si vous souhaitez traiter l'opsReq uniquement lorsque la base de données est prête. Et utiliser `Always` si vous souhaitez traiter l'exécution de opsReq quel que soit l'état de la base de données.
* `spec.opsRequestOptions.timeout` spécifie la durée maximale de chaque étape de opsRequest (en secondes).
  Si une étape ne se termine pas dans le délai spécifié, la requête opérationnelle entraînera un échec.

> **Note:** L'autoscaler collecte les métriques de ressources pour chaque pod en interrogeant le point de terminaison Prometheus du cluster Spoke où ce pod est planifié, comme configuré dans le `PlacementPolicy`.

Créons le `MariaDBAutoscaler` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/compute/cluster/examples/mdas-compute.yaml --context demo-controller
mariadbautoscaler.autoscaling.kubedb.com/md-as-compute created
```

#### Vérifiez que l'autoscaling est configuré avec succès

Vérifions que le `mariadbautoscaler` la ressource est créée avec succès,

```bash
$ kubectl get mariadbautoscaler -n demo --context demo-controller
NAME            AGE
md-as-compute   5m56s

$ kubectl describe mariadbautoscaler md-as-compute -n demo --context demo-controller
Name:         md-as-compute
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-09-16T11:26:58Z
  Generation:          1
  ...
Spec:
  Compute:
    Mariadb:
      Container Controlled Values:  RequestsAndLimits
      Controlled Resources:
        cpu
        memory
      Max Allowed:
        Cpu:     1
        Memory:  1Gi
      Min Allowed:
        Cpu:                     250m
        Memory:                  400Mi
      Pod Life Time Threshold:   5m0s
      Resource Diff Percentage:  20
      Trigger:                   On
  Database Ref:
    Name:  sample-mariadb
  Ops Request Options:
    Apply:    IfReady
    Timeout:  3m0s
Status:
  Checkpoints:
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              46
        Weight:             555
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Bucket Weights:
        Index:              1
        Weight:             10000
      Reference Timestamp:  2022-09-17T00:00:00Z
      Total Weight:         1.391848625060675
    Ref:
      Container Name:     md-coordinator
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              3
        Weight:             556
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Reference Timestamp:  2022-09-17T00:00:00Z
    Ref:
      Container Name:     mariadb
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
  Conditions:
    Last Transition Time:  2022-09-16T11:27:07Z
    Message:               Successfully created mariaDBOpsRequest demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                CreateOpsRequest
    Status:                True
    Type:                  CreateOpsRequest
  Vpas:
    Conditions:
      Last Transition Time:  2022-09-16T11:27:02Z
      Status:                True
      Type:                  RecommendationProvided
    Recommendation:
      Container Recommendations:
        Container Name:  mariadb
        Lower Bound:
          Cpu:     250m
          Memory:  400Mi
        Target:
          Cpu:     250m
          Memory:  400Mi
        Uncapped Target:
          Cpu:     25m
          Memory:  262144k
        Upper Bound:
          Cpu:     1
          Memory:  1Gi
    Vpa Name:      sample-mariadb
Events:            <none>
```

Ainsi, le `mariadbautoscaler` la ressource est créée avec succès.

Nous pouvons vérifier à partir du résultat ci-dessus que `status.vpas` contient le `RecommendationProvided` condition à vrai. Et en même temps, `status.vpas.recommendation.containerRecommendations` contiennent la recommandation réellement générée.

Notre opérateur d'autoscaler surveille en permanence la recommandation générée et crée un `mariadbopsrequest` en fonction des recommandations, si les ressources du pod de base de données doivent être augmentées ou réduites.

Regardons le `mariadbopsrequest` dans l'espace de noms de la démo pour voir s'il y en a `mariadbopsrequest` l'objet est créé. Après un certain temps, vous verrez qu'un `mariadbopsrequest` sera créé sur la base de la recommandation.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                          TYPE              STATUS       AGE
mdops-sample-mariadb-6xc1kc   VerticalScaling   Progressing  7s
```

Attendons que la demande d'opérations aboutisse.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                              TYPE              STATUS       AGE
mdops-vpa-sample-mariadb-z43wc8   VerticalScaling   Successful   3m32s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour faire évoluer la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-vpa-sample-mariadb-z43wc8 --context demo-controller
Name:         mdops-sample-mariadb-6xc1kc
Namespace:    demo
...
Spec:
  Apply:  IfReady
  Database Ref:
    Name:   sample-mariadb
  Timeout:  2m0s
  Type:     VerticalScaling
  Vertical Scaling:
    Mariadb:
      Limits:
        Cpu:     250m
        Memory:  400Mi
      Requests:
        Cpu:     250m
        Memory:  400Mi
Status:
  Conditions:
    ...
    Last Transition Time:  2022-09-16T11:30:47Z
    Message:               Vertical scale successful for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                SuccessfullyPerformedVerticalScaling
    Status:                True
    Type:                  VerticalScaling
    ...
  Phase:  Successful
```

Maintenant, nous allons vérifier à partir du Pod et du yaml MariaDB si les ressources de la base de données du cluster distribué ont été mises à jour pour atteindre l'état souhaité. Vérifions,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json --context demo-worker | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}

$ kubectl get mariadb -n demo sample-mariadb -o json --context demo-controller | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}
```

Le résultat ci-dessus vérifie que nous avons réussi la mise à l'échelle automatique des ressources du cluster MariaDB distribué.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete mariadb -n demo sample-mariadb --context demo-controller
kubectl delete mariadbautoscaler -n demo md-as-compute --context demo-controller
kubectl delete placementpolicy distributed-mariadb --context demo-controller
kubectl delete ns demo --context demo-controller
kubectl delete ns demo --context demo-worker
```

<!-- PAGE_START: distributed/autoscaler/compute/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique des ressources de calcul MariaDB distribuées

Ce guide donnera un aperçu de la façon dont l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de calcul, c'est-à-dire le processeur et la mémoire d'un **distribué** Cluster MariaDB utilisant `mariadbautoscaler` crd.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de MariaDB distribuée](fr/distributed/overview.md)

## Fonctionnement de la mise à l'échelle automatique du calcul

Le diagramme suivant montre comment l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

![Auto Scaling process of MariaDB](images/distributed_autoscaler_compute_overview_mdas-compute.png)

Fig : Processus de mise à l'échelle automatique de MariaDB

Le processus Auto Scaling comprend les étapes suivantes :

1. Dans un premier temps, l'utilisateur crée un `PlacementPolicy` Ressource personnalisée (CR) avec `monitoring.prometheus.url` configuré pour chaque cluster de rayons. Cela permet à l'autoscaler d'extraire les métriques de l'instance Prometheus exécutée dans chaque cluster Spoke.
2. L'utilisateur crée un `MariaDB` Objet de ressource personnalisé (CRO) avec `spec.distributed: true` et une référence à `PlacementPolicy`.
3. `KubeDB` L'opérateur communautaire surveille `MariaDB` CRO.
4. Lorsque l'opérateur trouve un `MariaDB` CRO, il crée le nombre requis de `PetSets` et les distribue sur les clusters de rayons tels que définis par le `PlacementPolicy`.
5. Ensuite, afin de configurer l'autoscaling des ressources CPU et mémoire du `MariaDB` base de données, l'utilisateur crée un `MariaDBAutoscaler` CRO avec la configuration souhaitée.
6. `KubeDB` L'opérateur de l'autoscaler surveille le `MariaDBAutoscaler` CRO.
7. `KubeDB` L'opérateur Autoscaler utilise la version modifiée du responsable Kubernetes [Recommandateur APV](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/pkg) pour différents composants de la base de données, comme spécifié dans le `mariadbautoscaler` CRO.
   Il génère des recommandations basées sur l'utilisation des ressources en interrogeant les points de terminaison Prometheus configurés dans le `PlacementPolicy`, et les stocke dans le `status` section du CRO de l'autoscaler.
8. Si la recommandation générée ne correspond pas aux ressources actuelles de la base de données, alors `KubeDB` L'opérateur Autoscaler crée un `MariaDBOpsRequest` CRO pour mettre à l'échelle la base de données afin qu'elle corresponde à la recommandation fournie par l'objet VPA.
9. `KubeDB Ops-Manager operator` regarde le `MariaDBOpsRequest` CRO.
10. Enfin, le `KubeDB Ops-Manager operator` mettra à l'échelle le composant de base de données verticalement comme spécifié sur le `MariaDBOpsRequest` CRO.

> **Différence clé par rapport à la mise à l'échelle automatique non distribuée**: Pour MariaDB distribuée, le `PlacementPolicy` doit inclure un `monitoring.prometheus.url` pour chaque cluster de rayons `distributionRules` entrée. L'autoscaler utilise ces points de terminaison Prometheus pour collecter des métriques de ressources à partir de pods exécutés sur plusieurs clusters Kubernetes.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la mise à l'échelle automatique de la base de données MariaDB distribuée à l'aide de `MariaDBAutoscaler` CRD.

<!-- PAGE_START: distributed/autoscaler/storage/cluster.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique du stockage d'un cluster MariaDB distribué

Ce guide vous montrera comment utiliser `KubeDB` pour mettre à l'échelle automatiquement le stockage d'un cluster MariaDB Galera distribué déployé sur plusieurs clusters Kubernetes.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'une configuration Kubernetes multicluster avec OCM et KubeSlice configurés. Suivez le [Présentation de MariaDB distribuée](fr/distributed/overview.md) guide pour mettre en place l’infrastructure requise.
* Installer `KubeDB` Opérateur Community, Enterprise et Autoscaler dans votre cluster hub en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README). Assurez-vous d'activer la prise en charge OCM :

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* Installer `Metrics Server` depuis [ici](https://github.com/kubernetes-sigs/metrics-server#installation)
* Installez Prometheus dans chaque cluster de rayons. L'autoscaler interroge le point de terminaison Prometheus par cluster (configuré dans le `PlacementPolicy`) pour collecter des métriques d'utilisation du stockage. Vous pouvez l'installer à partir de [ici](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
* Vous devez avoir un `StorageClass` qui prend en charge l'expansion du volume dans chaque cluster de rayons.
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle automatique du stockage MariaDB distribué](fr/distributed/autoscaler/storage/overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Mise à l'échelle automatique du stockage de la base de données de cluster distribué

Vérifiez d’abord que vos clusters disposent d’une classe de stockage prenant en charge l’extension de volume. Vérifions d’abord la classe de stockage de `Controler` grappe,

```bash
$ kubectl get storageclass --context demo-controller
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  4d
longhorn (default)     driver.longhorn.io      Delete          Immediate              true                   24h
longhorn-static        driver.longhorn.io      Delete          Immediate              true                   24h
```

Vérifiez ensuite la classe de stockage de `Worker` grappe,

```bash
$ kubectl get storageclass --context demo-worker
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  4d
longhorn (default)     driver.longhorn.io      Delete          Immediate              true                   23h
longhorn-static        driver.longhorn.io      Delete          Immediate              true                   23h
```

Nous pouvons voir à partir de la sortie le `longhorn (default)` et `longhorn-static` la classe de stockage a `ALLOWVOLUMEEXPANSION` champ comme vrai. Ainsi, cette classe de stockage prend en charge l’expansion du volume. Nous pouvons l'utiliser. Vous pouvez installer `longhorn` depuis [ici](https://longhorn.io/docs/1.11.2/deploy/install/)

### Déployer une stratégie de placement

Pour distribué `MariaDB` mise à l'échelle automatique, la PlacementPolicy doit définir une valeur valide `monitoring.prometheus.url` pour chaque cluster de rayons. Ces points de terminaison sont requis par l'autoscaler pour collecter des métriques et surveiller l'utilisation du stockage sur tous les clusters où les pods MariaDB sont déployés.

De plus, il est essentiel de spécifier explicitement la classe de stockage pour chaque cluster à l'aide de `spec.clusterSpreadConstraint.distributionRules.storageClassName`. Si ce champ n'est pas fourni, le système reviendra à la classe de stockage par défaut, ce qui peut entraîner un comportement inattendu ou des risques potentiels de gestion des données dans un environnement distribué.

Vous trouverez ci-dessous le YAML du `PlacementPolicy` que nous allons créer. Il distribue 3 réplicas sur deux clusters et fournit le point de terminaison Prometheus pour chacun :

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        storageClassName: local-path
        monitoring:
          prometheus:
            url: http://prometheus-operated.monitoring.svc.cluster.local:9090
        replicaIndices:
          - 0
          - 2
      - clusterName: demo-worker
        storageClassName: local-path
        monitoring:
          prometheus:
            url: http://prometheus-operated.monitoring.svc.cluster.local:9090
        replicaIndices:
          - 1
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Ici,

* `spec.clusterSpreadConstraint.distributionRules[].monitoring.prometheus.url` spécifie le point de terminaison Prometheus pour le cluster Spoke correspondant. L'autoscaler utilise cette URL pour récupérer les métriques d'utilisation du stockage pour les pods exécutés dans ce cluster.
* `spec.clusterSpreadConstraint.distributionRules[].replicaIndices` spécifie quels index de réplica MariaDB sont planifiés sur ce cluster. Ici `demo-controller` héberge des répliques `0` et `2`, et `demo-worker` réplique d'hôtes `1`.

Appliquer le `PlacementPolicy` sur le hub (`demo-controller`) grappe:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/storage/cluster/examples/placement-policy.yaml --context demo-controller
placementpolicy.apps.k8s.appscode.com/distributed-mariadb created
```

> **Note:** Mettre à jour le `monitoring.prometheus.url` valeurs pour correspondre aux points de terminaison réels du service Prometheus dans chacun de vos clusters Spoke.

### Déployer un cluster MariaDB distribué

Dans cette section, nous allons déployer une base de données de réplicats MariaDB distribuée avec la version `12.1.2`. Ensuite, dans la section suivante, nous configurerons la mise à l'échelle automatique pour cette base de données en utilisant `MariaDBAutoscaler` CRD.

Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer. Noter que `spec.distributed` est réglé sur `true` et le `PlacementPolicy` est référencé via `spec.podTemplate.spec.podPlacementPolicy`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  distributed: true
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "topolvm-provisioner"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CRO que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/storage/cluster/examples/sample-mariadb.yaml --context demo-controller
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo --context demo-controller
NAME             VERSION   STATUS   AGE
sample-mariadb   11.5.2   Ready    3m46s
```

Les pods sont répartis sur les clusters tels que définis par le `PlacementPolicy`:

```bash
$ kubectl get pod -n demo --context demo-controller
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   3/3     Running   0          3m46s
sample-mariadb-2   3/3     Running   0          3m46s

$ kubectl get pod -n demo --context demo-worker
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-1   3/3     Running   0          3m46s
```

Vérifions la taille du volume à partir du petset et du volume persistant sur `demo-worker`,

```bash
$ kubectl get petset -n demo sample-mariadb -o json --context demo-worker | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1Gi"

$ kubectl get pv -n demo --context demo-worker
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            57s
```

Vous pouvez voir que le petset dispose de 1 Go de stockage et que la capacité de tous les volumes persistants est également de 1 Go.

Nous sommes maintenant prêts à appliquer le `MariaDBAutoscaler` CRO pour configurer la mise à l'échelle automatique du stockage pour cette base de données.

### Mise à l'échelle automatique du stockage

Ici, nous allons configurer la mise à l'échelle automatique du stockage à l'aide d'un objet MariaDBAutoscaler.

#### Créer un objet MariaDBAutoscaler

Afin de configurer la mise à l'échelle verticale pour cette base de données de jeux de réplicas distribués, nous devons créer un `MariaDBAutoscaler` CRO avec notre configuration souhaitée. Vous trouverez ci-dessous le YAML du `MariaDBAutoscaler` objet que nous allons créer,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-st
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  storage:
    mariadb:
      trigger: "On"
      usageThreshold: 20
      scalingThreshold: 20
      expansionMode: "Online"
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle verticale sur `sample-mariadb` base de données.
* `spec.storage.mariadb.trigger` spécifie que la mise à l'échelle automatique du stockage est activée pour cette base de données.
* `spec.storage.mariadb.usageThreshold` spécifie le seuil d'utilisation du stockage, si l'utilisation du stockage dépasse `20%` la mise à l'échelle automatique du stockage sera alors déclenchée. L'autoscaler surveille l'utilisation du stockage en interrogeant le point de terminaison Prometheus du cluster Spoke sur lequel chaque pod est exécuté, comme configuré dans le `PlacementPolicy`.
* `spec.storage.mariadb.scalingThreshold` spécifie le seuil de mise à l'échelle. Le stockage sera adapté à `20%` du montant actuel.
* `spec.storage.mariadb.expansionMode` spécifie le mode d'expansion de l'expansion du volume `MariaDBOpsRequest` créé par `MariaDBAutoscaler`. topolvm-provisioner prend en charge l'expansion du volume en ligne, alors ici `expansionMode` est défini sur « En ligne ».

Créons le `MariaDBAutoscaler` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/storage/cluster/examples/mdas-storage.yaml --context demo-controller
mariadbautoscaler.autoscaling.kubedb.com/md-as-st created
```

#### L'autoscaling du stockage est configuré avec succès

Vérifions que le `mariadbautoscaler` la ressource est créée avec succès,

```bash
$ kubectl get mariadbautoscaler -n demo --context demo-controller
NAME           AGE
md-as-st   33s

$ kubectl describe mariadbautoscaler md-as-st -n demo --context demo-controller
Name:         md-as-st
Namespace:    demo
Labels:       <none>
Annotations:  API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-01-14T06:08:02Z
  Generation:          1
  ...
  Resource Version:  24009
  UID:               4f45a3b3-fc72-4d04-b52c-a770944311f6
Spec:
  Database Ref:
    Name:  sample-mariadb
  Storage:
    Mariadb:
      Scaling Threshold:  20
      Trigger:            On
      Usage Threshold:    20
Events:                   <none>
```

Ainsi, le `mariadbautoscaler` la ressource est créée avec succès.

Maintenant, pour cette démo, nous allons remplir manuellement le volume persistant pour dépasser le `usageThreshold` en utilisant `dd` commande pour voir si la mise à l’échelle automatique du stockage fonctionne ou non.

Exécutons dans un pod de base de données sur `demo-worker` et remplissez le volume de la base de données (`var/lib/mysql`) à l'aide des commandes suivantes :

```bash
$ kubectl exec -it -n demo sample-mariadb-0 --context demo-worker -- bash
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  357M  658M  36% /var/lib/mysql
root@sample-mariadb-0:/ dd if=/dev/zero of=/var/lib/mysql/file.img bs=500M count=1
1+0 records in
1+0 records out
524288000 bytes (524 MB, 500 MiB) copied, 0.340877 s, 1.5 GB/s
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  857M  158M  85% /var/lib/mysql
```

Ainsi, à partir du résultat ci-dessus, nous pouvons voir que l'utilisation du stockage est de 85 %, ce qui dépasse le `usageThreshold` 20%.

Regardons le `mariadbopsrequest` dans l'espace de noms de la démo pour voir s'il y en a `mariadbopsrequest` l'objet est créé. Après un certain temps, vous verrez qu'un `mariadbopsrequest` de type `VolumeExpansion` sera créé sur la base de `scalingThreshold`.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                         TYPE              STATUS        AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Progressing   15s
```

Attendons que la demande d'opérations aboutisse.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                         TYPE              STATUS       AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Successful   97s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour augmenter le volume de la base de données.

```bash
$ kubectl describe mariadbopsrequest -n demo mops-sample-mariadb-xojkua --context demo-controller
Name:         mops-sample-mariadb-xojkua
Namespace:    demo
...
Spec:
  Database Ref:
    Name:  sample-mariadb
  Type:    VolumeExpansion
  Volume Expansion:
    Mariadb:  1594884096
Status:
  Conditions:
    ...
    Last Transition Time:  2022-01-14T06:14:25Z
    Message:               Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                SuccessfullyVolumeExpanded
    Status:                True
    Type:                  VolumeExpansion
    ...
  Phase:  Successful
```

Maintenant, nous allons vérifier à partir du `Petset` et le `Persistent Volume` si le volume de la base de données du jeu de réplicas distribués s'est étendu pour atteindre l'état souhaité, vérifions,

```bash
$ kubectl get petset -n demo sample-mariadb -o json --context demo-worker | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1594884096"
$ kubectl get pv -n demo --context demo-worker
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            23m
```

Le résultat ci-dessus vérifie que nous avons réussi la mise à l'échelle automatique du volume du cluster MariaDB distribué.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete mariadb -n demo sample-mariadb --context demo-controller
kubectl delete mariadbautoscaler -n demo md-as-st --context demo-controller
kubectl delete placementpolicy distributed-mariadb --context demo-controller
kubectl delete ns demo --context demo-controller
kubectl delete ns demo --context demo-worker
```

<!-- PAGE_START: distributed/autoscaler/storage/overview.md -->
> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique du stockage MariaDB distribué

Ce guide donnera un aperçu de la façon dont l'opérateur KubeDB Autoscaler met automatiquement à l'échelle le stockage de base de données d'un **distribué** Cluster MariaDB utilisant `mariadbautoscaler` crd.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](fr/concepts/mariadb.md)
  + [MariaDBAutoscaler](fr/concepts/autoscaler.md)
  + [MariaDBOpsRequest](fr/concepts/opsrequest.md)
  + [Présentation de MariaDB distribuée](fr/distributed/overview.md)

## Fonctionnement de la mise à l'échelle automatique du stockage

Le diagramme suivant montre comment l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

![Storage Autoscaling process of MariaDB](images/distributed_autoscaler_storage_overview_mdas-storage.jpeg)

Fig : Processus de mise à l'échelle automatique du stockage de MariaDB

Le processus Auto Scaling comprend les étapes suivantes :

1. Dans un premier temps, l'utilisateur crée un `PlacementPolicy` Ressource personnalisée (CR) avec `monitoring.prometheus.url` configuré pour chaque cluster de rayons. Cela permet à l'autoscaler de surveiller l'utilisation du stockage sur tous les clusters sur lesquels les pods MariaDB sont exécutés.
2. L'utilisateur crée un `MariaDB` Ressource personnalisée (CR) avec `spec.distributed: true` et une référence à `PlacementPolicy`.
3. `KubeDB` L'opérateur communautaire surveille `MariaDB` CR.
4. Lorsque l'opérateur trouve un `MariaDB` CR, il crée le nombre requis de `PetSets` et les distribue sur les clusters de rayons tels que définis par le `PlacementPolicy`.
5. Chaque PetSet crée un volume persistant selon le modèle de réclamation de volume fourni dans la configuration du petset. Ce volume persistant sera étendu par le `KubeDB` Opérateur d'entreprise.
6. Ensuite, afin de configurer l'autoscaling du stockage du `MariaDB` base de données, l'utilisateur crée un `MariaDBAutoscaler` CRO avec la configuration souhaitée.
7. `KubeDB` L'opérateur de l'autoscaler surveille le `MariaDBAutoscaler` CRO.
8. `KubeDB` L'opérateur de mise à l'échelle automatique surveille en permanence les volumes persistants des bases de données sur tous les clusters Spoke pour vérifier si l'utilisation du stockage dépasse le seuil spécifié. Il interroge les points de terminaison Prometheus configurés par cluster dans le `PlacementPolicy` pour collecter des métriques de stockage.
9. Si l'utilisation dépasse le seuil d'utilisation spécifié, alors `KubeDB` L'opérateur Autoscaler crée un `MariaDBOpsRequest` pour étendre le stockage de la base de données.
10. `KubeDB` L'opérateur d'entreprise surveille le `MariaDBOpsRequest` CRO.
11. Puis le `KubeDB` L'opérateur d'entreprise étendra le stockage du composant de base de données comme spécifié sur le `MariaDBOpsRequest` CRO.

> **Différence clé par rapport à la mise à l'échelle automatique non distribuée**: Pour MariaDB distribuée, le `PlacementPolicy` doit inclure un `monitoring.prometheus.url` pour chaque cluster de rayons `distributionRules` entrée. L'autoscaler utilise ces points de terminaison Prometheus pour collecter des métriques d'utilisation du stockage à partir de pods exécutés sur plusieurs clusters Kubernetes.

Dans la documentation suivante, nous allons montrer un guide étape par étape sur la mise à l'échelle automatique du stockage d'une base de données MariaDB distribuée à l'aide de `MariaDBAutoscaler` CRD.
