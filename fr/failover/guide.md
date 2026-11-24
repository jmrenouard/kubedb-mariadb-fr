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
* Lire [concept de cluster mariadb](../clustering/overview.md) pour en savoir plus sur MariaDB
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

* En savoir plus sur [sauvegarde et restauration](../backup/stash/overview.md) Base de données MariaDB utilisant Stash.
* Vous souhaitez configurer le cluster MariaDB ? Vérifiez comment [configurer le cluster MariaDB hautement disponible](../clustering/galera-cluster.md)
* Surveillez votre base de données MariaDB avec KubeDB en utilisant [Prometheus intégré](../monitoring/prometheus-operator.md).
* Concepts détaillés de [Objet MariaDB](../concepts/mariadb.md).
* Utiliser [registre Docker privé](../private-registry/quickstart.md) pour déployer MariaDB avec KubeDB.
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).