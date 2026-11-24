# Sauvegarde et restauration au niveau de l'application de la base de données MariaDB à l'aide de KubeStash

KubeStash offre une fonctionnalité de sauvegarde et de restauration au niveau de l'application pour `MariaDB` bases de données. Il capture à la fois les sauvegardes de manifeste et de données de tout `MariaDB` base de données en un seul instantané. Pendant le processus de restauration, KubeStash applique d'abord le `MariaDB` manifeste au cluster, puis y restaure les données.

Ce guide vous donnera un aperçu de la façon dont vous pouvez effectuer une sauvegarde au niveau de l'application et restaurer votre `MariaDB` bases de données utilisant `Kubestash`.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant `Minikube` ou `Kind`.
* Installer `KubeDB` dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `KubeStash` dans votre cluster en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubestash).
* Installer KubeStash `kubectl` plugin en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont KubeStash sauvegarde et restaure les bases de données MariaDB, veuillez consulter le guide suivant [ici](overview.md).

Vous devriez être familier avec ce qui suit `KubeStash` notions :

* [BackupStorage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [BackupConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
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

> **Note:** Les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/backup/kubestash/application-level/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples) répertoire de [kubedb/docs](https://github.com/kubedb/docs) dépôt.

## Sauvegarde MariaDB

KubeStash prend en charge les sauvegardes pour `MariaDB` instances dans différentes configurations, y compris les configurations autonomes et Galera Cluster. Dans cette démonstration, nous nous concentrerons sur un `MariaDB` base de données utilisant la configuration du cluster Galera. Le processus de sauvegarde et de restauration est similaire pour la configuration autonome.

Cette section montrera comment effectuer une sauvegarde au niveau de l'application d'un `MariaDB` base de données. Ici, nous allons déployer un `MariaDB` base de données utilisant KubeDB. Ensuite, nous allons sauvegarder la base de données au niveau de l'application sur un `GCS` seau. Enfin, nous restaurerons l'intégralité `MariaDB` base de données.

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
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

KubeDB déploiera un `MariaDB` base de données selon la spécification ci-dessus. Cela créera également le nécessaire `Secrets` et `Services` pour accéder à la base de données.

Vérifions si la base de données est prête à être utilisée,

```bash
$ kubectl get md -n demo sample-mariadb
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m1s
```

La base de données est `Ready`. Vérifiez que KubeDB a créé un `Secret` et un `Service` pour cette base de données en utilisant les commandes suivantes,

```bash
$ kubectl get secret -n demo 
NAME                          TYPE                       DATA   AGE
sample-mariadb-auth           kubernetes.io/basic-auth   2      5m49s

$ kubectl get service -n demo -l=app.kubernetes.io/instance=sample-mariadb
NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE
sample-mariadb        ClusterIP   10.128.92.155   <none>        3306/TCP        62s
sample-mariadb-pods   ClusterIP   None            <none>        3306/TCP        62s
```

Ici, nous devons utiliser le service `sample-mariadb` et secret `sample-mariadb-auth` pour se connecter à la base de données. `KubeDB` crée un [Liaison d'application](../../concepts/appbinding.md) CR qui contient les informations nécessaires pour se connecter à la base de données.

**Vérifiez AppBinding :**

Vérifiez que le `AppBinding` a été créé avec succès à l'aide de la commande suivante,

```bash
$ kubectl get appbindings -n demo
NAME                      TYPE                  VERSION   AGE
sample-mariadb            kubedb.com/mariadb    11.1.3    6m14s
```

Vérifions le YAML de ce qui précède `AppBinding`,

```bash
$ kubectl get appbindings -n demo sample-mariadb -o yaml
```

```yaml
apiVersion: v1
items:
  - apiVersion: appcatalog.appscode.com/v1alpha1
    kind: AppBinding
    metadata:
      annotations:
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"deletionPolicy":"WipeOut","replicas":3,"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}}},"storageType":"Durable","version":"11.1.3"}}          
      creationTimestamp: "2024-09-18T08:31:32Z"
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
          uid: 35400a0b-97b1-4437-a3b9-416678b71adf
      resourceVersion: "1728063"
      uid: 8ebec467-32d5-416a-975a-67e890a4efe6
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
kind: List
metadata:
  resourceVersion: ""
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
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   2/2     Running   0          8m4s
sample-mariadb-1   2/2     Running   0          8m3s
sample-mariadb-2   2/2     Running   0          8m3s
```

Maintenant, exécutons le pod et créons une table,

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
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

**Créer une configuration de sauvegarde :**

Vous trouverez ci-dessous le YAML pour `BackupConfiguration` CR pour effectuer une sauvegarde au niveau de l'application du `sample-mariadb` base de données que nous avons déployée précédemment,

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
          - name: manifest-backup
          - name: logical-backup
```

* `.spec.sessions[*].schedule` précise que nous voulons sauvegarder à `5 minutes` intervalle.
* `.spec.target` fait référence à la cible `sample-mariadb` Base de données MariaDB que nous avons créée précédemment.
* `.spec.sessions[*].addon.tasks[*].name[*]` précise que les deux `manifest-backup` et `logical-backup` les tâches seront exécutées.

Créons le `BackupConfiguration` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/backupconfiguration.yaml
backupconfiguration.core.kubestash.com/sample-mariadb-backup created
```

**Vérifier la configuration de la sauvegarde avec succès**

Si tout se passe bien, la phase du `BackupConfiguration` devrait être `Ready`. Le `Ready` La phase indique que la configuration de la sauvegarde a réussi. Vérifions le `Phase` de la Configuration de Sauvegarde,

```bash
$ kubectl get backupconfiguration -n demo
NAME                     PHASE   PAUSED   AGE
sample-mariadb-backup   Ready            2m50s
```

De plus, nous pouvons vérifier que le `Repository` précisé dans le `BackupConfiguration` a été créé à l'aide de la commande suivante,

```bash
$ kubectl get repo -n demo
NAME                  INTEGRITY   SNAPSHOT-COUNT   SIZE     PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo                 0                0 B      Ready                            3m
```

KubeStash conserve la sauvegarde pour `Repository` YAML. Si nous naviguons vers le compartiment GCS, nous verrons le `Repository` YAML stocké dans le `demo/mariadb` annuaire.

**Vérifiez CronJob :**

Cela créera également un `CronJob` avec l'horaire spécifié dans `spec.sessions[*].scheduler.schedule` domaine de `BackupConfiguration` CR.

Vérifiez que le `CronJob` a été créé à l'aide de la commande suivante,

```bash
$ kubectl get cronjob -n demo
NAME                                             SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
trigger-sample-mariadb-backup-frequent-backup   */5 * * * *             0        2m45s           3m25s
```

**Vérifiez la session de sauvegarde :**

KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Après cela, les sauvegardes sont planifiées selon le calendrier spécifié.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                INVOKER-TYPE          INVOKER-NAME              PHASE       DURATION   AGE
sample-mariadb-backup-frequent-backup-1726651003   BackupConfiguration   sample-mariadb-backup    Succeeded              7m22s
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
$ kubectl get snapshots.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                  REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726651003       gcs-mariadb-repo   frequent-backup   2024-01-23T13:10:54Z   Delete            Succeeded   16h
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
$ kubectl get snapshots -n demo gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725449400 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T09:16:53Z"
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
  name: gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726651003
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: gcs-mariadb-repo
      uid: 82a72ef1-1071-49df-b44f-d1f395017262
  resourceVersion: "1734435"
  uid: b96499b6-f882-43e8-ba2a-badb54f96bb8
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: sample-mariadb-backup-frequent-backup-1726651003
  deletionPolicy: Delete
  repository: gcs-mariadb-repo
  session: frequent-backup
  snapshotID: 01J826Q68983K50JRZV2AX1QZF
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.291630733s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 6a9b3e0ccd380f93ff414157156f4ac9d144fa15c5c3adeea2faa09cf44fb175
            size: 3.139 KiB
            uploaded: 3.431 KiB
      size: 1.277 KiB
    manifest:
      driver: Restic
      duration: 2.613551084s
      integrity: true
      path: repository/v1/frequent-backup/manifest
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: /kubestash-tmp/manifest
            id: 47d89d4149cd59bfc8e701b8171a864d0259486820c477a9c2b3a8c0d80de237
            size: 2.507 KiB
            uploaded: 3.939 KiB
      size: 1.913 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T09:16:53Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T09:17:18Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 3.188 KiB
  snapshotTime: "2024-09-18T09:16:53Z"
  totalComponents: 2
```

> KubeStash utilise `mariadb-dump` pour effectuer des sauvegardes de la cible `MariaDB` bases de données. Par conséquent, le nom du composant pour les sauvegardes logiques est défini comme `dump`.

> KubeStash définit le nom du composant comme `manifest` pour le `manifest backup` des bases de données MariaDB.

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons les données de sauvegarde stockées dans le `demo/mariadb/repository/v1/frequent-backup/dump` annuaire. KubeStash conserve également la sauvegarde pour `Snapshot` Les YAML, que l'on peut trouver dans le `demo/mariadb/snapshots` annuaire.

> Remarque : KubeStash stocke toutes les données sauvegardées chiffrées dans le répertoire de sauvegarde, ce qui signifie qu'elles restent illisibles jusqu'à ce qu'elles soient déchiffrées.

## Restaurer

Dans cette section, nous allons restaurer l'intégralité de la base de données à partir de la sauvegarde que nous avons effectuée dans la section précédente.

Pour ce didacticiel, nous restaurerons la base de données dans un espace de noms distinct appelé `dev`.

Tout d'abord, créez l'espace de noms en exécutant la commande suivante :

```bash
$ kubectl create ns dev
namespace/dev created
```

#### Créer une session de restauration :

Nous devons créer un RestoreSession CR.

Ci-dessous, le contenu du fichier YAML du `RestoreSession` CR que nous allons créer pour restaurer l'intégralité de la base de données.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: restore-sample-mariadb
  namespace: demo
spec:
  manifestOptions:
    mariaDB:
      db: true
      restoreNamespace: dev
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
      - name: manifest-restore
```

Ici,

* `.spec.manifestOptions.mariadb.db` spécifie s'il faut restaurer le manifeste de base de données ou non.
* `.spec.dataSource.repository` spécifie l'objet Repository qui contient les données de sauvegarde.
* `.spec.dataSource.snapshot` spécifie de restaurer à partir du dernier `Snapshot`.
* `.spec.addon.tasks[*]` précise que les deux `manifest-restore` et `logical-backup-restore` tâches.

Créons l'objet RestoreSession CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/restoresession.yaml
restoresession.core.kubestash.com/restore-sample-mariadb created
```

Une fois que vous avez créé le `RestoreSession` objet, KubeStash créera une tâche de restauration. Exécutez la commande suivante pour regarder la phase du `RestoreSession` objet,

```bash
$ watch kubectl get restoresession -n demo
Every 2.0s: kubectl get restores... AppsCode-PC-03: Wed Aug 21 10:44:05 2024
NAME                      REPOSITORY            FAILURE-POLICY   PHASE       DURATION   AGE
restore-sample-mariadb   gcs-mariadb-repo                      Succeeded   3s         53s
```

Le `Succeeded` Cette phase signifie que le processus de restauration s'est terminé avec succès.

#### Vérifiez le manifeste MariaDB restauré :

Dans cette section, nous vérifierons si le `MariaDB` Le manifeste de la base de données a été appliqué avec succès au cluster.

```bash
$ kubectl get mariadb -n dev 
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m18s
```

La sortie confirme que le `MariaDB` La base de données a été créée avec succès avec la même configuration qu'au moment de la sauvegarde.

#### Vérifiez les données restaurées :

Dans cette section, nous allons vérifier si les données souhaitées ont été restaurées avec succès. Nous allons nous connecter au serveur de base de données et vérifier si la base de données et la table que nous avons créée précédemment dans la base de données d'origine sont restaurées.

Dans un premier temps, vérifiez si la base de données est entrée dans **`Ready`** énoncer par la commande suivante,

```bash
$ kubectl get mariadb -n dev sample-mariadb
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m18s
```

Maintenant, découvrez la base de données `Pod` par la commande suivante,

```bash
$ kubectl get pods -n dev --selector="app.kubernetes.io/instance=sample-mariadb"
NAME                READY   STATUS    RESTARTS   AGE
sample-mariadb-0   2/2     Running   0          12m
sample-mariadb-1   2/2     Running   0          12m
sample-mariadb-2   2/2     Running   0          12m
```

Maintenant, exécutons l'un des pods et vérifions les données restaurées.

```bash
$ kubectl exec -it -n dev sample-mariadb-0 -- bash
```

```mysql
mysql@restored-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> use hello;

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

Ainsi, à partir du résultat ci-dessus, nous pouvons voir le `hello` base de données que nous avions créée dans la base de données d'origine `sample-mariadb` a été restauré avec succès.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete backupconfigurations.core.kubestash.com  -n demo sample-mariadb-backup
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete restoresessions.core.kubestash.com -n demo restore-sample-mariadb
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadb -n dev sample-mariadb
```