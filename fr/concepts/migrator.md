> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBMigration

## Qu'est-ce que MariaDBMigration

`MariaDBMigration` est un Kubernetes `Custom Resource Definition` (CRD). Il fournit un moyen déclaratif de
migrer une base de données existante, telle qu'une base de données exécutée sur une instance externe ou gérée, vers une base de données
Base de données gérée par KubeDB. Il vous suffit de décrire les bases de données source et cible dans un `MariaDBMigration`
objet, et l'opérateur kubedb-courier exécutera le travail de migration qui copie les données et conserve
la cible synchronisée jusqu'à ce que vous effectuiez le basculement.

`MariaDBMigration` est le CRD de migration spécifique à MariaDB (`courier.kubedb.com/v1alpha1`) dont
`spec.source` et `spec.target` décrire directement la source et la cible MariaDB. Cette page décrit
le `MariaDBMigration` objet pour un **MariaDB** source et cible.

## Spécification de MariaDBMigration

Comme pour tous les autres objets Kubernetes, un `MariaDBMigration` besoins `apiVersion`, `kind`, et `metadata`
champs. Il faut également un `.spec` section. Ci-dessous un exemple `MariaDBMigration` objet pour migrer un
Base de données MariaDB.

```yaml
apiVersion: courier.kubedb.com/v1alpha1
kind: MariaDBMigration
metadata:
  name: mariadb-migrate
  namespace: demo
spec:
  source:
    connectionInfo:
      appBinding:
        name: source-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
    schema:
      enabled: true
      database: [] # databases to include
      excludeDatabase: [] # databases to exclude
    snapshot:
      enabled: true
      pipeline:
        workers: 3
        sinkers: 4
        buffer: 12
        read_batch_size: 1000
        write_batch_size: 200
    streaming:
      enabled: true
  target:
    connectionInfo:
      appBinding:
        name: target-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
  jobDefaults:
    imagePullPolicy: IfNotPresent
    backoffLimit: 6
    ttlSecondsAfterFinished: 3600
    activeDeadlineSeconds: 86400
  jobTemplate:
    spec:
      securityContext:
        fsGroup: 65534
```

### spec.source

`spec.source` est un champ obligatoire qui décrit la base de données en cours de migration **depuis**. Il détient le
Champs sources MariaDB (`connectionInfo`, `schema`, `snapshot`, `streaming`) directement.

### spec.target

`spec.target` est un champ obligatoire qui décrit la base de données gérée par KubeDB en cours de migration **dans**.
Il contient directement les champs cibles MariaDB.

### spec.source.connectionInfo

`connectionInfo` (également sous `spec.target`) indique à MariaDBMigration comment se connecter à MariaDB
par exemple. Il existe deux manières de fournir les détails de la connexion : définir **soit** `appBinding` **ou**
`url`:

* `appBinding` — fait référence à un `AppBinding` qui contient les informations de connexion pour cette MariaDB
  par exemple. Un `AppBinding` est une ressource KubeDB qui dissocie les détails de connexion (point de terminaison,
  informations d'identification, TLS) du consommateur ; en créer un avec les informations nécessaires et le référencer
  ici. C'est l'approche recommandée.
  + `name` - nom de l'AppBinding.
  + `namespace` - espace de noms de l'AppBinding.
* `url` — la chaîne de connexion à la base de données (par exemple `mysql://user:password@host:3306/`). Utilisez ceci
  comme alternative à `appBinding` lorsque vous souhaitez fournir le point de terminaison en ligne plutôt que via un
  Liaison d'application.
* `dbName` — la base de données interne utilisée comme point d'entrée de connexion initiale.
* `maxConnections` - limite le nombre de connexions simultanées que la migration ouvre à cette MariaDB
  par exemple.
* `tls` - chemins vers les fichiers PEM pour une connexion compatible TLS. Vous pouvez définir les champs suivants :
  + `caFile` — chemin d'accès au fichier de certificat CA codé en PEM.
  + `certFile` — chemin d'accès au certificat client codé PEM (pour TLS mutuel).
  + `keyFile` — chemin d'accès à la clé privée client codée PEM (pour TLS mutuel).
  + `insecureSkipVerify` - désactive la vérification du certificat du serveur et du nom d'hôte.
  + `serverName` — remplace le nom d'hôte utilisé pour TLS SNI et la vérification du certificat.

> Pour un `KubeDB`-base de données gérée, un `AppBinding` est créé par défaut, vous n'avez donc généralement besoin que de
> créez-en un pour la source. En savoir plus sur [Liaison d'application](appbinding.md).

### spec.source.schema

`schema` configure la phase de migration du schéma, qui recrée les définitions de base de données et de table sur le
cible avant que les données ne soient copiées.

* `enabled` — active la phase de migration du schéma.
* `database` — liste des bases de données à inclure. Une liste vide signifie toutes les bases de données sauf le système
  bases de données (`mysql`, `information_schema`, `performance_schema`, `sys`).
* `excludeDatabase` — liste des bases de données à exclure de la migration.

### spec.source.snapshot

`snapshot` configure la phase initiale d'instantané en masse, qui copie les lignes existantes de la source
à la cible.

* `enabled` - active la phase d'instantané groupé.
* `pipeline` — ajuste le pipeline de copie parallèle :
  + `workers` — nombre de travailleurs parallèles, chacun traitant simultanément une table distincte. Valeurs par défaut
    à `3`.
  + `sinkers` — nombre de travailleurs d'écriture parallèle poussant les données vers la cible pour chaque travailleur. Valeurs par défaut
    à `3`.
  + `buffer` — taille de la file d'attente en mémoire (en enregistrements) entre les lecteurs et les écrivains. La valeur par défaut est `10`.
  + `read_batch_size` — nombre de lignes récupérées par lot de lecture à partir de la source. La valeur par défaut est `5000`.
  + `write_batch_size` — nombre de lignes écrites par lot sur la cible. La valeur par défaut est `500`.

### spec.source.streaming

`streaming` configure la phase de modification-data-capture (CDC).

* `enabled` - active le streaming CDC une fois l'instantané terminé, gardant la cible en permanence dans
  synchronisez-vous avec les modifications en cours sur la source jusqu'à ce que vous effectuiez la transition.

### spec.jobDefaults

`spec.jobDefaults` est un champ facultatif qui définit les paramètres par défaut pour le travail de migration.

* `imagePullPolicy` — la politique d'extraction d'image pour la tâche de migration. La valeur par défaut est `IfNotPresent`.
* `backoffLimit` — le nombre de tentatives avant que le travail ne soit marqué comme ayant échoué. La valeur par défaut est `6`.
* `ttlSecondsAfterFinished` — le TTL (en secondes) pour nettoyer un Job terminé.
* `activeDeadlineSeconds` — la durée (en secondes) par rapport à son heure de début pendant laquelle le Job peut être
  actif avant que le système ne tente d'y mettre fin.

### spec.jobTemplate

`spec.jobTemplate` est un champ facultatif qui contient la configuration d'exécution pour le pod de tâche de migration.
(un `PodTemplateSpec`). Utilisez-le pour définir les paramètres au niveau du pod tels que `securityContext`, `nodeSelector`,
`resources`, `serviceAccountName`, et ainsi de suite.

## Statut de MariaDBMigration

`status` reflète l’état observé de la migration.

* `status.phase` — la phase actuelle de la migration. L'un des :
  + `Pending` — la migration n'a pas encore commencé.
  + `Running` — la migration est en cours.
  + `Succeeded` — la migration s'est terminée avec succès.
  + `Failed` — la migration a échoué.
* `status.progress` — la progression actuelle de la migration:
  + `dbType` — le type de base de données en cours de migration.
  + `info` — des informations supplémentaires sur les progrès, y compris les `Stage`, `Lag`, et `Progress`
    (ceux-ci apparaissent sous forme de colonnes dans `kubectl get mariadbmigrations`).
* `status.conditions` — un ensemble de conditions décrivant l’état de la migration dans le temps (par
  exemple, `MigratorJobTriggered`, `MigrationRunning`, `MigrationSucceeded`, `MigrationFailed`).

## Prochaines étapes

* Migrez une base de données MariaDB étape par étape avec le [Migration de la base de données MariaDB](../migration/databasemigration.md) guide.
* Renseignez-vous sur le [Liaison d'application](appbinding.md) concept.
* En savoir plus sur le CRD MariaDB [ici](mariadb.md).