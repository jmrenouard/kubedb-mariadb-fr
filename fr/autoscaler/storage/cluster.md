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

  + [MariaDB](../../concepts/mariadb.md)
  + [MariaDBAutoscaler](../../concepts/autoscaler.md)
  + [MariaDBOpsRequest](../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle automatique du stockage](overview.md)

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