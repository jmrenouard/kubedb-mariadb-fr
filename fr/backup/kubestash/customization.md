# Personnalisation du processus de sauvegarde et de restauration

KubeStash fournit de riches supports de personnalisation pour le processus de sauvegarde et de restauration afin de répondre aux exigences de diverses configurations de cluster. Ce guide vous montrera quelques exemples de ces personnalisations.

## Personnalisation du processus de sauvegarde

Dans cette section, nous allons vous montrer comment personnaliser le processus de sauvegarde. Ici, nous allons montrer quelques exemples de fourniture d'arguments au processus de sauvegarde, d'exécution du processus de sauvegarde en tant qu'utilisateur spécifique, etc.

### Passer des arguments au processus de sauvegarde

Le module complémentaire KubeStash MariaDB utilise le [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) commande par défaut pour les sauvegardes.
L'exemple ci-dessous montre comment vous pouvez transmettre le `--flush-logs` pour vider les fichiers journaux du serveur MariaDB avant de démarrer le vidage.

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
            params:
              args: --flush-logs
```

### Passer une base de données cible au processus de sauvegarde

L'exemple ci-dessous montre comment transmettre le nom de la base de données cible lors de la sauvegarde.

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
            params:
              args: --databases testdb
```

> **AVERTISSEMENT**: Assurez-vous que la base de données fournie a été créée avant d'effectuer une sauvegarde.

### Utiliser plusieurs backends

Vous pouvez configurer plusieurs backends au sein d'un seul `backupConfiguration`. Pour sauvegarder les mêmes données sur différents backends, tels que S3 et GCS, déclarez chaque backend dans le fichier `.spe.backends` section. Ensuite, référencez ces backends dans le `.spec.sessions[*].repositories` section.

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
    - name: s3-backend
      storageRef:
        namespace: demo
        name: s3-storage
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
        - name: s3-mariadb-repo
          backend: s3-backend
          directory: /mariadb-copy
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
```

### Exécution d'une tâche de sauvegarde en tant qu'utilisateur spécifique

Si votre cluster nécessite l'exécution de la tâche de sauvegarde en tant qu'utilisateur spécifique, vous pouvez fournir `securityContext` sous `addon.jobTemplate.spec.securityContext` section. L'exemple ci-dessous montre comment exécuter le travail de sauvegarde en tant que `root` utilisateur.

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
        jobTemplate:
          spec:
            securityContext:
              runAsUser: 0
              runAsGroup: 0
        tasks:
          - name: logical-backup
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de sauvegarde

Si vous souhaitez spécifier la limite/demande de mémoire/CPU pour votre tâche de sauvegarde, vous pouvez spécifier `resources` champ sous `addon.jobTemplate.spec` section.

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
        jobTemplate:
          spec:
            resources:
              requests:
                cpu: "200m"
                memory: "1Gi"
              limits:
                cpu: "200m"
                memory: "1Gi"
        tasks:
          - name: logical-backup
```

> Vous pouvez configurer des paramètres d'exécution supplémentaires pour les tâches de sauvegarde dans le `addon.jobTemplate.spec` sections. Pour plus de détails, veuillez vous référer au [référence](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/#podtemplate-spec).

## Personnalisation du processus de restauration

`KubeStash` utilise [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) pendant le processus de restauration. Dans cette section, nous allons montrer comment transmettre des arguments au processus de restauration, restaurer un instantané spécifique, exécuter une tâche de restauration en tant qu'utilisateur spécifique, etc.

### Passer des arguments au processus de restauration

Semblable au processus de sauvegarde, vous pouvez transmettre des arguments au processus de restauration via les paramètres args sous la section addon.tasks[\*].params.

Cet exemple restaurera les données de la base de données testdb uniquement.

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
        params:
          args: testdb
```

### Restaurer un instantané spécifique

Vous pouvez également restaurer un instantané spécifique. Dans un premier temps, répertoriez l'instantané disponible comme ci-dessous,

```bash
$ kubectl get snapshots.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                    REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725257849   gcs-mariadb-repo   frequent-backup   2024-09-02T06:18:01Z      Delete            Succeeded   15m
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258000   gcs-mariadb-repo   frequent-backup   2024-09-02T06:20:00Z      Delete            Succeeded   13m
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258300   gcs-mariadb-repo   frequent-backup   2024-09-02T06:25:00Z      Delete            Succeeded   8m34s
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258600   gcs-mariadb-repo   frequent-backup   2024-09-02T06:30:00Z      Delete            Succeeded   3m34s
```

L'exemple ci-dessous montre comment transmettre un nom d'instantané spécifique dans `.spec.dataSource` section.

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
    snapshot: gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258000
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
```

### Exécution d'une tâche de restauration en tant qu'utilisateur spécifique

Semblable au processus de sauvegarde sous le `addon.jobTemplate.spec.` vous pouvez fournir `securityContext` pour exécuter le travail de restauration en tant qu'utilisateur spécifique.

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
    jobTemplate:
      spec:
        securityContext:
          runAsUser: 0
          runAsGroup: 0
    tasks:
      - name: logical-backup-restore
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de restauration

Semblable au processus de sauvegarde, vous pouvez également fournir `resources` champ sous le `addon.jobTemplate.spec.resources` section pour limiter la mémoire/CPU pour votre travail de restauration.

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
    jobTemplate:
      spec:
        resources:
          requests:
            cpu: "200m"
            memory: "1Gi"
          limits:
            cpu: "200m"
            memory: "1Gi"
    tasks:
      - name: logical-backup-restore
```

> Vous pouvez configurer des paramètres d'exécution supplémentaires pour les tâches de restauration dans le `addon.jobTemplate.spec` sections. Pour plus de détails, veuillez vous référer au [référence](https://kubestash.com/docs/latest/concepts/crds/restoresession/#podtemplate-spec).