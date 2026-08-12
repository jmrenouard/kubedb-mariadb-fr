# Sauvegarder et restaurer la base de données MariaDB à l'aide de KubeStash

KubeStash vous permet de sauvegarder et de restaurer `MariaDB` bases de données. Il prend en charge les sauvegardes pour `MariaDB` instances exécutées dans des configurations de cluster autonomes et Galera. KubeStash facilite la gestion de votre `MariaDB` sauvegardes et restaurations plus simples et efficaces.

Ce guide vous donnera un aperçu de la façon dont vous pouvez effectuer une sauvegarde et restaurer votre `MariaDB` bases de données utilisant `Kubestash`.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant `Minikube` ou `Kind`.
* Installer `KubeDB` dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `KubeStash` dans votre cluster en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubestash).
* Installer KubeStash `kubectl` plugin en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont KubeStash sauvegarde et restaure les bases de données MariaDB, veuillez consulter le guide suivant [ici](overview.md).

Vous devriez être familier avec ce qui suit `KubeStash` notions :

* [SauvegardeStockage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [SauvegardeConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
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

Ici, nous devons utiliser le service `sample-mariadb` et secret `sample-mariadb-auth` pour se connecter à la base de données. `KubeDB` crée un [Liaison d'application](../../concepts/appbinding.md) CR qui contient les informations nécessaires pour se connecter à la base de données.

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