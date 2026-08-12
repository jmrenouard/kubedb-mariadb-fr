# Personnalisation du processus de sauvegarde et de restauration

Stash fournit de riches supports de personnalisation pour le processus de sauvegarde et de restauration afin de répondre aux exigences de diverses configurations de cluster. Ce guide vous montrera quelques exemples de ces personnalisations.

## Personnalisation du processus de sauvegarde

Dans cette section, nous allons vous montrer comment personnaliser le processus de sauvegarde. Ici, nous allons montrer quelques exemples de fourniture d'arguments au processus de sauvegarde, d'exécution du processus de sauvegarde en tant qu'utilisateur spécifique, d'ignorance de certains index pendant le processus de sauvegarde, etc.

### Passer des arguments au processus de sauvegarde

Utilisations du module complémentaire Stash MariaDB [mysqldump](https://mariadb.com/kb/en/mysqldump) pour la sauvegarde. Vous pouvez transmettre des arguments au `mysqldump` à travers `args` paramètre sous `task.params` section.

L'exemple ci-dessous montre comment vous pouvez transmettre le `--databases testdb` pour effectuer une sauvegarde d'une base de données mariadb spécifique nommée `testdb`.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  task:
    params:
    - name: args
      value: --databases testdb
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

> **AVERTISSEMENT**: Assurez-vous d'avoir créé la base de données spécifique avant d'effectuer une sauvegarde. Dans ce cas, Base de données `testdb` doit exister avant le démarrage du travail de sauvegarde.

### Exécution d'une tâche de sauvegarde en tant qu'utilisateur spécifique

Si votre cluster nécessite l'exécution de la tâche de sauvegarde en tant qu'utilisateur spécifique, vous pouvez fournir `securityContext` sous `runtimeSettings.pod` section. L'exemple ci-dessous montre comment exécuter la tâche de sauvegarde en tant qu'utilisateur root.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/2 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    pod:
      securityContext:
        runAsUser: 0
        runAsGroup: 0
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de sauvegarde

Si vous souhaitez spécifier la limite/demande de mémoire/CPU pour votre tâche de sauvegarde, vous pouvez spécifier `resources` champ sous `runtimeSettings.container` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/2 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    container:
      resources:
        requests:
          cpu: "200m"
          memory: "1Gi"
        limits:
          cpu: "200m"
          memory: "1Gi"
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

### Utilisation de plusieurs politiques de rétention

Vous pouvez également spécifier plusieurs politiques de conservation pour vos données sauvegardées. Par exemple, vous souhaiterez peut-être conserver quelques instantanés quotidiens, quelques instantanés hebdomadaires et quelques instantanés mensuels, etc. Il vous suffit de transmettre le numéro souhaité avec la clé correspondante sous le `retentionPolicy` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: sample-mariadb-retention
    keepLast: 5
    keepDaily: 10
    keepWeekly: 20
    keepMonthly: 50
    keepYearly: 100
    prune: true
```

Pour en savoir plus sur les options disponibles pour les politiques de rétention, veuillez visiter [ici](https://stash.run/docs/latest/concepts/crds/backupconfiguration/#specretentionpolicy).

## Personnalisation du processus de restauration

Stash utilise également `mysql` pendant le processus de restauration. Dans cette section, nous allons montrer comment transmettre des arguments au processus de restauration, restaurer un instantané spécifique, exécuter une tâche de restauration en tant qu'utilisateur spécifique, etc.

### Passer des arguments au processus de restauration

Comme pour le processus de sauvegarde, vous pouvez transmettre des arguments au processus de restauration via le `args` paramètres sous `task.params` section. Cet exemple restaurera les données de la base de données `testdb` seulement.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  task:
    params:
    - name: args
      value: --one-database testdb
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [latest]
```

### Restaurer un instantané spécifique

Vous pouvez également restaurer un instantané spécifique. Dans un premier temps, répertoriez l'instantané disponible comme ci-dessous,

```bash
❯ kubectl get snapshots -n demo
NAME                ID         REPOSITORY   HOSTNAME   CREATED AT
gcs-repo-4bc21d6f   4bc21d6f   gcs-repo     host-0     2022-01-12T14:54:27Z
gcs-repo-f0ac7cbd   f0ac7cbd   gcs-repo     host-0     2022-01-12T14:56:26Z
gcs-repo-9210ebb6   9210ebb6   gcs-repo     host-0     2022-01-12T14:58:27Z
gcs-repo-0aff8890   0aff8890   gcs-repo     host-0     2022-01-12T15:00:28Z
```

> Vous pouvez également filtrer les instantanés comme indiqué dans le guide [ici](https://stash.run/docs/latest/concepts/crds/snapshot/#working-with-snapshot).

Vous pouvez utiliser l'ID respectif de l'instantané pour restaurer cet instantané.

L'exemple ci-dessous montre comment transmettre un ID d'instantané spécifique via le `snapshots` domaine de `rules` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [4bc21d6f]
```

> Veuillez ne pas spécifier plusieurs instantanés ici. Chaque instantané représente une sauvegarde complète de votre base de données. Plusieurs instantanés ne sont utilisables que lors de la restauration de fichiers/répertoires.

### Exécution d'une tâche de restauration en tant qu'utilisateur spécifique

Vous pouvez fournir `securityContext` sous `runtimeSettings.pod` pour exécuter le travail de restauration en tant qu'utilisateur spécifique.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    pod:
      securityContext:
        runAsUser: 0
        runAsGroup: 0
  rules:
  - snapshots: [latest]
```

### Spécification de la limite/demande de mémoire/CPU pour le travail de restauration

Semblable au processus de sauvegarde, vous pouvez également fournir `resources` champ sous le `runtimeSettings.container` section pour limiter la mémoire/CPU pour votre travail de restauration.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    container:
      resources:
        requests:
          cpu: "200m"
          memory: "1Gi"
        limits:
          cpu: "200m"
          memory: "1Gi"
  rules:
  - snapshots: [latest]
```