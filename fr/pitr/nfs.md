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

```bash
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

* En savoir plus sur [sauvegarde et restauration](../backup/kubestash/overview.md) Base de données MariaDB utilisant KubeStash.
* En savoir plus sur l'initialisation [MariaDB avec script](../initialization/using-script.md).
* Vous souhaitez configurer le cluster MariaDB ? Vérifiez comment [configurer le cluster MariaDB hautement disponible](../clustering/galera-cluster.md)
* Surveillez votre base de données MariaDB avec KubeDB en utilisant [Prometheus intégré](../monitoring/builtin-prometheus.md).
* Surveillez votre base de données MariaDB avec KubeDB en utilisant [Opérateur Prométhée](../monitoring/prometheus-operator.md).
* Concepts détaillés de [Objet MariaDB](../concepts/mariadb.md).
* Utiliser [registre Docker privé](../private-registry/quickstart.md) pour déployer MariaDB avec KubeDB.
* Vous voulez pirater KubeDB ? Consultez notre [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).