> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Extension du volume MariaDB

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour augmenter le volume d'une MariaDB.

## Avant de commencer

* Au début, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Vous devez avoir un `StorageClass` qui prend en charge l’expansion du volume.
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../concepts/mariadb.md)
  + [MariaDBOpsRequest](../concepts/opsrequest.md)
  + [Présentation de l'expansion du volume](overview.md)

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