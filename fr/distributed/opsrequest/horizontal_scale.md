> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB distribuée à l'échelle horizontale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur Opsrequest pour mettre à l'échelle horizontalement un cluster MariaDB Galera distribué sur plusieurs clusters Kubernetes.

> **Note:** Tous les autres `OpsRequest` les opérations se comportent de manière cohérente dans un environnement distribué. Seulement `HorizontalScaling` comporte des considérations spécifiques au cluster abordées dans ce guide.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'une configuration Kubernetes multicluster avec OCM et KubeSlice configurés. Suivez le [Présentation de MariaDB distribuée](../overview.md) guide pour mettre en place l’infrastructure requise.
* Installer `KubeDB` Opérateur de communauté et d'entreprise dans votre cluster hub en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README). Assurez-vous d'activer la prise en charge OCM :

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../../concepts/mariadb.md)
  + [Présentation de MariaDB distribuée](../overview.md)
  + [MariaDBOpsDemande](../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle horizontale](../../scaling/horizontal-scaling/overview.md)

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

Maintenant, attends `mariadb` a un statut `Ready`:

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