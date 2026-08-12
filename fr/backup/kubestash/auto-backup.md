# Sauvegarder MariaDB à l'aide de la sauvegarde automatique KubeStash

KubeStash peut être automatiquement configuré pour sauvegarder n'importe quel `MariaDB` bases de données de votre cluster. KubeStash permet aux administrateurs de cluster de déployer des sauvegardes `blueprints` à l'avance afin que les propriétaires de bases de données puissent facilement sauvegarder n'importe quel `MariaDB` base de données avec quelques annotations.

Dans ce didacticiel, nous allons montrer comment configurer un plan de sauvegarde pour `MariaDB` bases de données de votre cluster et sauvegardez-les avec quelques annotations.

## Avant de commencer

* Au début, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant `Minikube` ou `Kind`.
* Installer `KubeDB` dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `KubeStash` dans votre cluster en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubestash).
* Installer KubeStash `kubectl` plugin en suivant les étapes [ici](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* Si vous n'êtes pas familier avec la façon dont KubeStash sauvegarde et restaure `MariaDB` bases de données, veuillez consulter le guide suivant [ici](overview.md).

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

> **Note:** Les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/backup/kubestash/auto-backup/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples) répertoire de [kubedb/docs](https://github.com/kubedb/docs) dépôt.

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
      prefix: blueprint
      secretName: gcs-secret
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: Delete
```

Créons le BackupStorage que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/backupstorage.yaml
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
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/retentionpolicy.yaml
retentionpolicy.storage.kubestash.com/demo-retention created
```

**Créer un secret :**

Nous devons également créer un secret avec un `Restic` mot de passe pour le cryptage des données de sauvegarde.

Créons un secret appelé `encrypt-secret` avec le mot de passe Restic,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ kubectl create secret generic -n demo encrypt-secret \
    --from-file=./RESTIC_PASSWORD \
secret "encrypt-secret" created
```

## Sauvegarde automatique avec configurations par défaut

Dans cette section, nous allons sauvegarder un `MariaDB` base de données de `demo` espace de noms. Nous allons utiliser les configurations par défaut qui seront précisées dans le `BackupBlueprint` CR.

**Préparer le plan de sauvegarde**

A `BackupBlueprint` vous permet de spécifier un modèle pour le `Repository`,`Session` ou `Variables` de `BackupConfiguration` de manière native Kubernetes.

Maintenant, nous devons créer un `BackupBlueprint` CR avec un plan pour `BackupConfiguration` objet.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupBlueprint
metadata:
  name: mariadb-default-backup-blueprint
  namespace: demo
spec:
  usagePolicy:
    allowedNamespaces:
      from: All
  backupConfigurationTemplate:
    deletionPolicy: OnDelete
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
        sessionHistoryLimit: 3
        scheduler:
          schedule: "*/5 * * * *"
          jobTemplate:
            backoffLimit: 1
        repositories:
          - name: default-blueprint
            backend: gcs-backend
            directory: /default-blueprint
            encryptionSecret:
              name: encrypt-secret
              namespace: demo
        addon:
          name: mariadb-addon
          tasks:
            - name: logical-backup
```

Ici,

* `.spec.backupConfigurationTemplate.backends[*].storageRef` fait référence à notre création précédente `gcs-storage` stockage de sauvegarde.
* `.spec.backupConfigurationTemplate.sessions[*].schedule` précise que nous voulons sauvegarder la base de données à `5 minutes` intervalle.

Créons le `BackupBlueprint` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/default-backupblueprint.yaml
backupblueprint.core.kubestash.com/mariadb-default-backup-blueprint created
```

Maintenant, nous sommes prêts à sauvegarder notre `MariaDB` bases de données utilisant peu d’annotations.

**Créer une base de données**

Maintenant, nous allons créer un `MariaDB` CR dans l'espace de noms de démonstration.

Vous trouverez ci-dessous le YAML du `MariaDB` objet que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
  annotations:
    blueprint.kubestash.com/name: mariadb-default-backup-blueprint
    blueprint.kubestash.com/namespace: demo
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

Ici,

* `.spec.annotations.blueprint.kubestash.com/name: mariadb-default-backup-blueprint` précise le nom du `BackupBlueprint` qui sera utilisé en sauvegarde.
* `.spec.annotations.blueprint.kubestash.com/namespace: demo` précise le nom du `namespace` où le `BackupBlueprint` réside.

Créons le `MariaDB` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

**Vérifier la configuration de la sauvegarde**

Si tout se passe bien, KubeStash devrait créer un `BackupConfiguration` pour notre MariaDB dans l'espace de noms de démonstration et la phase de celui-ci `BackupConfiguration` devrait être `Ready`. Vérifiez le `BackupConfiguration` objet par la commande suivante,

```bash
$ kubectl get backupconfiguration -n demo
NAME                         PHASE   PAUSED   AGE
appbinding-sample-mariadb   Ready            2m50m
```

Maintenant, vérifions le YAML du `BackupConfiguration`.

```bash
$ kubectl get backupconfiguration -n demo appbinding-sample-mariadb  -o yaml
```

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  creationTimestamp: "2024-09-18T05:34:15Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    app.kubernetes.io/managed-by: kubestash.com
    kubestash.com/invoker-name: mariadb-default-backup-blueprint
    kubestash.com/invoker-namespace: demo
  name: appbinding-sample-mariadb
  namespace: demo
  resourceVersion: "1700384"
  uid: 927ac985-e3d2-43a2-9d25-00ba55ce5fc1
spec:
  backends:
    - name: gcs-backend
      retentionPolicy:
        name: demo-retention
        namespace: demo
      storageRef:
        name: gcs-storage
        namespace: demo
  sessions:
    - addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
      name: frequent-backup
      repositories:
        - backend: gcs-backend
          directory: /default-blueprint
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
          name: default-blueprint
      scheduler:
        jobTemplate:
          backoffLimit: 1
          template:
            controller: {}
            metadata: {}
            spec:
              resources: {}
        schedule: '*/5 * * * *'
      sessionHistoryLimit: 3
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
status:
  backends:
    - name: gcs-backend
      ready: true
      retentionPolicy:
        found: true
        ref:
          name: demo-retention
          namespace: demo
      storage:
        phase: Ready
        ref:
          name: gcs-storage
          namespace: demo
  conditions:
    - lastTransitionTime: "2024-09-18T05:34:17Z"
      message: Validation has been passed successfully.
      reason: ResourceValidationPassed
      status: "True"
      type: ValidationPassed
  dependencies:
    - found: true
      kind: Addon
      name: mariadb-addon
  phase: Ready
  repositories:
    - name: default-blueprint
      phase: Ready
  sessions:
    - conditions:
        - lastTransitionTime: "2024-09-18T05:34:17Z"
          message: Scheduler has been ensured successfully.
          reason: SchedulerEnsured
          status: "True"
          type: SchedulerEnsured
        - lastTransitionTime: "2024-09-18T05:34:18Z"
          message: Initial backup has been triggered successfully.
          reason: SuccessfullyTriggeredInitialBackup
          status: "True"
          type: InitialBackupTriggered
      name: frequent-backup
  targetFound: true
```

Remarquez le `spec.backends`, `spec.sessions` et `spec.target` sections, KubeStash a automatiquement résolu ces informations à partir du `BackupBluePrint` et créé ci-dessus `BackupConfiguration`.

**Vérifiez la session de sauvegarde :**

KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Après cela, les sauvegardes sont planifiées selon le calendrier spécifié.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                    INVOKER-TYPE          INVOKER-NAME                 PHASE       DURATION   AGE
appbinding-sample-mariadb-frequent-backup-1726637655    BackupConfiguration   appbinding-sample-mariadb   Succeeded   2m11s      3m15s
```

Nous pouvons voir à partir du résultat ci-dessus que la session de sauvegarde a réussi. Nous allons maintenant vérifier si les données de sauvegarde ont été stockées dans le backend.

**Vérifier la sauvegarde :**

Une fois la sauvegarde terminée, KubeStash mettra à jour les fichiers respectifs. `Repository` CR pour refléter la sauvegarde. Vérifiez que le référentiel `sample-mariadb-backup` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo default-blueprint
NAME                INTEGRITY   SNAPSHOT-COUNT   SIZE        PHASE   LAST-SUCCESSFUL-BACKUP   AGE
default-blueprint   true        3                1.559 KiB   Ready   80s                      7m32s
```

En ce moment nous en avons un `Snapshot`. Exécutez la commande suivante pour vérifier les `Snapshot` qui représente l'état d'une sauvegarde exécutée pour une application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=default-blueprint
NAME                                                              REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
default-blueprint-appbinding-samiadb-frequent-backup-1726637655   default-blueprint   frequent-backup   2024-09-18T05:34:18Z   Delete            Succeeded   7m39s
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
$ kubectl get snapshot.storage.kubestash.com -n demo default-blueprint-appbinding-samgres-frequent-backup-1725533628 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T05:34:18Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: default-blueprint
  annotations:
    kubedb.com/db-version: 11.1.3
  name: default-blueprint-appbinding-samiadb-frequent-backup-1726637655
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: default-blueprint
      uid: ec1ba99f-ac95-4197-9ddd-0f978053a5d6
  resourceVersion: "1701057"
  uid: fee77218-c06a-43a5-8ad4-fa9baf72a128
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: appbinding-sample-mariadb-frequent-backup-1726637655
  deletionPolicy: Delete
  repository: default-blueprint
  session: frequent-backup
  snapshotID: 01J81SZM8G6AQ5XZAN85CSBP96
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.762583481s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: c4d4c26ad6e03f372b60dfc8bb7901900c4be9b791d44c68564753fb9e9e424c
            size: 2.206 KiB
            uploaded: 2.498 KiB
      size: 2.190 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T05:34:18Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T05:36:26Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 2.189 KiB
  snapshotTime: "2024-09-18T05:34:18Z"
  totalComponents: 1
```

> KubeStash utilise `mariadb-dump` pour effectuer des sauvegardes de la cible `MariaDB` bases de données. Par conséquent, le nom du composant pour les sauvegardes logiques est défini comme `dump`.

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons les données de sauvegarde stockées dans le `blueprint/default-blueprint/repository/v1/frequent-backup/dump` annuaire. KubeStash conserve également la sauvegarde pour `Snapshot` Les YAML, que l'on peut trouver dans le `blueprint/default-blueprint/snapshots` annuaire.

> Remarque : KubeStash stocke toutes les données sauvegardées chiffrées dans le répertoire de sauvegarde, ce qui signifie qu'elles restent illisibles jusqu'à ce qu'elles soient déchiffrées.

## Sauvegarde automatique avec configurations personnalisées

Dans cette section, nous allons sauvegarder un `MariaDB` base de données de `demo` espace de noms. Nous allons utiliser les configurations personnalisées qui seront spécifiées dans le `BackupBlueprint` CR.

**Préparer le plan de sauvegarde**

A `BackupBlueprint` vous permet de spécifier un modèle pour le `Repository`,`Session` ou `Variables` de `BackupConfiguration` de manière native Kubernetes.

Maintenant, nous devons créer un `BackupBlueprint` CR avec un plan pour `BackupConfiguration` objet.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupBlueprint
metadata:
  name: mariadb-customize-backup-blueprint
  namespace: demo
spec:
  usagePolicy:
    allowedNamespaces:
      from: All
  backupConfigurationTemplate:
    deletionPolicy: OnDelete
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
        sessionHistoryLimit: 3
        scheduler:
          schedule: ${schedule}
          jobTemplate:
            backoffLimit: 1
        repositories:
          - name: ${repoName}
            backend: gcs-backend
            directory: ${namespace}/${targetName}
            encryptionSecret:
              name: encrypt-secret
              namespace: demo
        addon:
          name: mariadb-addon
          tasks:
            - name: logical-backup
              params:
                args: ${targetedDatabase}
```

Notez que nous avons utilisé quelques variables (format : `${<variable name>}`) dans différents domaines. KubeStash remplacera ces variables par les valeurs des annotations de la cible respective. Vous êtes libre d’utiliser toutes les variables de votre choix.

Ici,

* `.spec.backupConfigurationTemplate.backends[*].storageRef` fait référence à notre création précédente `gcs-storage` stockage de sauvegarde.
* `.spec.backupConfigurationTemplate.sessions[*]`:
  + `.schedule` définit `${schedule}` variable, qui détermine l’intervalle de temps pour la sauvegarde.
  + `.repositories[*].name` définit le `${repoName}` variable, qui spécifie le nom de la sauvegarde `Repository`.
  + `.repositories[*].directory` définit deux variables, `${namespace}` et `${targetName}`, qui sont utilisés pour déterminer le chemin où la sauvegarde sera stockée.
  + `.addon.tasks[*].params.args` définit `${targetedDatabase}` variable, qui identifie une seule base de données à sauvegarder.

Créons le `BackupBlueprint` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/customize-backupblueprint.yaml
backupblueprint.core.kubestash.com/mariadb-customize-backup-blueprint created
```

Maintenant, nous sommes prêts à sauvegarder notre `MariaDB` bases de données utilisant peu d’annotations. Vous pouvez vérifier les annotations de sauvegarde automatique disponibles pour une base de données à partir de [ici](https://kubestash.com/docs/latest/concepts/crds/backupblueprint/).

**Créer une base de données**

Maintenant, nous allons créer un `MariaDB` CR dans l'espace de noms de démonstration.

Vous trouverez ci-dessous le YAML du `MariaDB` objet que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb-2
  namespace: demo
  annotations:
    blueprint.kubestash.com/name: mariadb-customize-backup-blueprint
    blueprint.kubestash.com/namespace: demo
    variables.kubestash.com/schedule: "*/10 * * * *"
    variables.kubestash.com/repoName: customize-blueprint
    variables.kubestash.com/namespace: demo
    variables.kubestash.com/targetName: sample-mariadb-2
    variables.kubestash.com/targetedDatabase: mysql
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

Remarquez le `metadata.annotations` champ, où nous avons défini les annotations liées à la configuration de la sauvegarde automatique. Plus précisément, nous avons défini le `BackupBlueprint` nom comme `mariadb-customize-backup-blueprint` et l'espace de noms comme `demo`. Nous avons également fourni des valeurs pour les variables du modèle de plan, telles que la sauvegarde `schedule`, `repositoryName`, `namespace`, `targetName`, et `targetedDatabase`. Ces annotations seront utilisées pour créer un `BackupConfiguration` pour ça `MariaDB` base de données.

Créons le `MariaDB` nous l'avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/sample-mariadb-2.yaml
mariadb.kubedb.com/sample-mariadb-2 created
```

**Vérifier la configuration de la sauvegarde**

Si tout se passe bien, KubeStash devrait créer un `BackupConfiguration` pour notre MariaDB dans l'espace de noms de démonstration et la phase de celui-ci `BackupConfiguration` devrait être `Ready`. Vérifiez le `BackupConfiguration` objet par la commande suivante,

```bash
$ kubectl get backupconfiguration -n demo
NAME                           PHASE   PAUSED      AGE
appbinding-sample-mariadb-2    Ready               2m50m
```

Maintenant, vérifions le YAML du `BackupConfiguration`.

```bash
$ kubectl get backupconfiguration -n demo appbinding-sample-mariadb-2  -o yaml
```

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  creationTimestamp: "2024-09-18T06:23:21Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    app.kubernetes.io/managed-by: kubestash.com
    kubestash.com/invoker-name: mariadb-customize-backup-blueprint
    kubestash.com/invoker-namespace: demo
  name: appbinding-sample-mariadb-2
  namespace: demo
  resourceVersion: "1709334"
  uid: 08ff19bc-ab81-46c1-9e40-32ff3eb02144
spec:
  backends:
    - name: gcs-backend
      retentionPolicy:
        name: demo-retention
        namespace: demo
      storageRef:
        name: gcs-storage
        namespace: demo
  sessions:
    - addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
            params:
              args: mysql
      name: frequent-backup
      repositories:
        - backend: gcs-backend
          directory: demo/sample-mariadb-2
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
          name: customize-blueprint
      scheduler:
        jobTemplate:
          backoffLimit: 1
          template:
            controller: {}
            metadata: {}
            spec:
              resources: {}
        schedule: '*/10 * * * *'
      sessionHistoryLimit: 3
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb-2
    namespace: demo
status:
  backends:
    - name: gcs-backend
      ready: true
      retentionPolicy:
        found: true
        ref:
          name: demo-retention
          namespace: demo
      storage:
        phase: Ready
        ref:
          name: gcs-storage
          namespace: demo
  conditions:
    - lastTransitionTime: "2024-09-18T06:23:21Z"
      message: Validation has been passed successfully.
      reason: ResourceValidationPassed
      status: "True"
      type: ValidationPassed
  dependencies:
    - found: true
      kind: Addon
      name: mariadb-addon
  phase: Ready
  repositories:
    - name: customize-blueprint
      phase: Ready
  sessions:
    - conditions:
        - lastTransitionTime: "2024-09-18T06:23:23Z"
          message: Scheduler has been ensured successfully.
          reason: SchedulerEnsured
          status: "True"
          type: SchedulerEnsured
        - lastTransitionTime: "2024-09-18T06:23:24Z"
          message: Initial backup has been triggered successfully.
          reason: SuccessfullyTriggeredInitialBackup
          status: "True"
          type: InitialBackupTriggered
      name: frequent-backup
  targetFound: true
```

Remarquez le `spec.backends`, `spec.sessions` et `spec.target` sections, KubeStash a automatiquement résolu ces informations à partir du `BackupBluePrint` et créé ci-dessus `BackupConfiguration`.

**Vérifiez la session de sauvegarde :**

KubeStash déclenche une sauvegarde instantanée dès que le `BackupConfiguration` est prêt. Après cela, les sauvegardes sont planifiées selon le calendrier spécifié.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                      INVOKER-TYPE          INVOKER-NAME                   PHASE       DURATION   AGE
appbinding-sample-mariadb-2-frequent-backup-1726640601    BackupConfiguration   appbinding-sample-mariadb-2   Succeeded   2m6s       10m
```

Nous pouvons voir à partir du résultat ci-dessus que la session de sauvegarde a réussi. Nous allons maintenant vérifier si les données de sauvegarde ont été stockées dans le backend.

**Vérifier la sauvegarde :**

Une fois la sauvegarde terminée, KubeStash mettra à jour les fichiers respectifs. `Repository` CR pour refléter la sauvegarde. Vérifiez que le référentiel `customize-blueprint` a été mis à jour par la commande suivante,

```bash
$ kubectl get repository -n demo customize-blueprint
NAME                         INTEGRITY   SNAPSHOT-COUNT   SIZE    PHASE   LAST-SUCCESSFUL-BACKUP   AGE
customize-blueprint          true        2                1.021 MiB   Ready   4m29s                    11ms
```

En ce moment nous en avons un `Snapshot`. Exécutez la commande suivante pour vérifier les `Snapshot` qui représente l'état d'une sauvegarde exécutée pour une application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=customize-blueprint
NAME                                                              REPOSITORY            SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
customize-blueprint-appbinding-sdb-2-frequent-backup-1726640601   customize-blueprint   frequent-backup   2024-09-18T06:23:24Z   Delete            Succeeded   12m
```

> Remarque : KubeStash crée un `Snapshot` avec les étiquettes suivantes :
>
> * `kubedb.com/db-version: <db-version>`
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> Ces étiquettes peuvent être utilisées pour regarder uniquement `Snapshot`s liés à notre base de données cible ou `Repository`.

Si nous vérifions le YAML du `Snapshot`, nous pouvons trouver les informations sur les composants de sauvegarde de la base de données.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo customize-blueprint-appbinding-sql-2-frequent-backup-1725597000 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T06:23:24Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb-2
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: customize-blueprint
  annotations:
    kubedb.com/db-version: 11.1.3
  name: customize-blueprint-appbinding-sdb-2-frequent-backup-1726640601
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: customize-blueprint
      uid: 224a1fe8-4897-4de6-b933-fc3537c2a881
  resourceVersion: "1709934"
  uid: e28deec8-a7a4-43ba-b314-b95ef2991a85
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb-2
    namespace: demo
  backupSession: appbinding-sample-mariadb-2-frequent-backup-1726640601
  deletionPolicy: Delete
  repository: customize-blueprint
  session: frequent-backup
  snapshotID: 01J81WSH71CCD611AZ5PTC1N6G
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.836904485s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 6aa144d43ea5d70fd1018390d4d22f98f6ab568c74eee9a386d6a9b29ad21d8b
            size: 4.887 MiB
            uploaded: 4.887 MiB
      size: 907.341 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T06:23:24Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T06:25:27Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 907.341 KiB
  snapshotTime: "2024-09-18T06:23:24Z"
  totalComponents: 1
```

> KubeStash utilise `mariadb-dump` pour effectuer des sauvegardes de la cible `MariaDB` bases de données. Par conséquent, le nom du composant pour les sauvegardes logiques est défini comme `dump`.

Maintenant, si nous naviguons vers le compartiment GCS, nous verrons les données de sauvegarde stockées dans le `blueprint/demo/sample-mariadb-2/repository/v1/frequent-backup/dump` annuaire. KubeStash conserve également la sauvegarde pour `Snapshot` Les YAML, que l'on peut trouver dans le `blueprint/demo/sample-mariadb-2/snapshots` annuaire.

> Remarque : KubeStash stocke toutes les données sauvegardées chiffrées dans le répertoire de sauvegarde, ce qui signifie qu'elles restent illisibles jusqu'à ce qu'elles soient déchiffrées.

## Nettoyage

Pour nettoyer les ressources créées par ce didacticiel, exécutez les commandes suivantes :

```bash
kubectl delete backupblueprints.core.kubestash.com  -n demo mariadb-default-backup-blueprint
kubectl delete backupblueprints.core.kubestash.com  -n demo mariadb-customize-backup-blueprint
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadb -n demo sample-mariadb-2
```