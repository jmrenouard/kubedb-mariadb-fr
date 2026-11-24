> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Échelle horizontale MaxScale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur de gestion des opérations pour faire évoluer le serveur MaxScale.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../../concepts/mariadb.md)
  + [Réplication MariaDB](../../clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle horizontale](overview.md)

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

Maintenant, attends `md-replication` a un statut `Ready`. c'est-à-dire,

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