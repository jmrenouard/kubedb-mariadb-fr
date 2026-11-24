> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique du stockage d'un cluster MariaDB distribué

Ce guide vous montrera comment utiliser `KubeDB` pour mettre à l'échelle automatiquement le stockage d'un cluster MariaDB Galera distribué déployé sur plusieurs clusters Kubernetes.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'une configuration Kubernetes multicluster avec OCM et KubeSlice configurés. Suivez le [Présentation de MariaDB distribuée](../../overview.md) guide pour mettre en place l’infrastructure requise.
* Installer `KubeDB` Opérateur Community, Enterprise et Autoscaler dans votre cluster hub en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README). Assurez-vous d'activer la prise en charge OCM :

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* Installer `Metrics Server` depuis [ici](https://github.com/kubernetes-sigs/metrics-server#installation)
* Installez Prometheus dans chaque cluster de rayons. L'autoscaler interroge le point de terminaison Prometheus par cluster (configuré dans le `PlacementPolicy`) pour collecter des métriques d'utilisation du stockage. Vous pouvez l'installer à partir de [ici](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
* Vous devez avoir un `StorageClass` qui prend en charge l'expansion du volume dans chaque cluster de rayons.
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../../../concepts/mariadb.md)
  + [MariaDBAutoscaler](../../../concepts/autoscaler.md)
  + [MariaDBOpsRequest](../../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle automatique du stockage MariaDB distribué](overview.md)

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