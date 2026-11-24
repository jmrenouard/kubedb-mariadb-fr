> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Extension de volume MaxScale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur Ops-manager pour augmenter le volume du serveur MaxScale.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Vous devez avoir un `StorageClass` qui prend en charge l’expansion du volume.
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../concepts/mariadb.md)
  + [Réplication MariaDB](../clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](../concepts/opsrequest.md)
  + [Présentation de l'expansion du volume](overview.md)

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