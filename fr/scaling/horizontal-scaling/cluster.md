> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB à échelle horizontale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour faire évoluer le cluster d'une base de données MariaDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../../concepts/mariadb.md)
  + [Cluster MariaDB](../../clustering/galera-cluster.md)
  + [MariaDBOpsRequest](../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle horizontale](overview.md)

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