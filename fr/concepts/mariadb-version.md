> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Version MariaDB

## Qu'est-ce que MariaDBVersion

`MariaDBVersion` est un Kubernetes `Custom Resource Definitions` (CRD). Il fournit une configuration déclarative pour spécifier les images Docker à utiliser pour la base de données MariaDB déployée avec KubeDB de manière native Kubernetes.

Lorsque vous installez KubeDB, un `MariaDBVersion` Une ressource personnalisée sera créée automatiquement pour toutes les versions de MariaDB prises en charge. Vous devez préciser le nom de `MariaDBVersion` crédit dans `spec.version` domaine de [MariaDB](mariadb.md) crd. Ensuite, KubeDB utilisera les images Docker spécifiées dans le fichier `MariaDBVersion` crd pour créer votre base de données attendue.

L'utilisation d'un crd distinct pour spécifier les images Docker respectives et les noms des politiques de sécurité des pods nous permettent de modifier les images et les politiques indépendamment de l'opérateur KubeDB. Cela permettra également aux utilisateurs d'utiliser une image personnalisée pour la base de données.

## Spécification MariaDBVersion

Comme pour tous les autres objets Kubernetes, une MariaDBVersion a besoin `apiVersion`, `kind`, et `metadata` champs. Il faut également un `.spec` section.

```yaml
apiVersion: catalog.kubedb.com/v1alpha1
kind: MariaDBVersion
metadata:
  annotations:
    meta.helm.sh/release-name: kubedb
    meta.helm.sh/release-namespace: kubedb
  creationTimestamp: "2024-12-19T05:12:32Z"
  generation: 1
  labels:
    app.kubernetes.io/instance: kubedb
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: kubedb-catalog
    app.kubernetes.io/version: v2024.11.18
    helm.sh/chart: kubedb-catalog-v2024.11.18
  name: 11.8.5
  resourceVersion: "1585"
  uid: d6b463f0-032a-4832-8b87-4648da0b38a6
spec:
  archiver:
    addon:
      name: mariadb-addon
      tasks:
        fullBackup:
          name: logical-backup
        fullBackupRestore:
          name: logical-backup-restore
        manifestBackup:
          name: manifest-backup
        manifestRestore:
          name: manifest-restore
        volumeSnapshot:
          name: volume-snapshot
    walg:
      image: ghcr.io/kubedb/mariadb-archiver:v0.9.0_10.5.23-focal
  coordinator:
    image: ghcr.io/kubedb/mariadb-coordinator:v0.29.0
  db:
    image: ghcr.io/appscode-images/mariadb:11.8.5-focal
  exporter:
    image: prom/mysqld-exporter:v0.13.0
  initContainer:
    image: ghcr.io/kubedb/mariadb-init:0.5.2
  maxscale:
    image: mariadb/maxscale:24.02.4
    securityContext:
      runAsUser: 995
  podSecurityPolicies:
    databasePolicyName: maria-db
  securityContext:
    runAsUser: 999
  stash:
    addon:
      backupTask:
        name: mariadb-backup-10.6.23
      restoreTask:
        name: mariadb-restore-10.6.23
  ui:
    - name: phpmyadmin
      version: v2024.4.27
  updateConstraints:
    allowlist:
      - '> 10.5.23, <= 11.5.2'
  version: 10.5.23
```

### metadata.name

`metadata.name` est un champ obligatoire qui spécifie le nom du `MariaDBVersion` crd. Vous devez préciser ce nom dans `spec.version` domaine de [MariaDB](mariadb.md) crd.

Nous suivons cette convention pour nommer MariaDBVersion crd :

* Format du nom : `{Original MariaDB image version}-{modification tag}`

Nous modifions l'image Docker MariaDB d'origine pour prendre en charge des fonctionnalités supplémentaires. Une image avec une balise de modification plus élevée aura plus de fonctionnalités que les images avec une balise de modification inférieure. Par conséquent, il est recommandé d'utiliser MariaDBVersion crd avec la balise de modification la plus élevée pour profiter des dernières fonctionnalités.

### spec.version

`spec.version` est un champ obligatoire qui spécifie la version originale de la base de données MariaDB qui a été utilisée pour créer l'image Docker spécifiée dans `spec.db.image` champ.

### spec.deprecated

`spec.deprecated` est un champ facultatif qui spécifie si les images Docker spécifiées ici sont prises en charge par l'opérateur KubeDB actuel.

La valeur par défaut de ce champ est `false`. Si `spec.deprecated` est réglé `true`, l'opérateur KubeDB ne créera pas la base de données et les autres ressources respectives pour cette version.

### spec.db.image

`spec.db.image` est un champ obligatoire qui spécifie l'image Docker qui sera utilisée pour créer Petset par l'opérateur KubeDB afin de créer la base de données MariaDB attendue.

### spec.exporter.image

`spec.exporter.image` est un champ obligatoire qui spécifie l'image qui sera utilisée pour exporter les métriques Prometheus.

### spec.initContainer.image

`spec.initContainer.image` est un champ obligatoire qui spécifie l'image qui sera utilisée pour supprimer `lost+found` répertoire et monter un `EmptyDir` volume de données.

### spec.podSecurityPolicies.databasePolicyName

`spec.podSecurityPolicies.databasePolicyName` est un champ obligatoire qui spécifie le nom de la stratégie de sécurité du pod requise pour faire fonctionner le ou les pods du serveur de base de données.

### spec.stash

`spec.stash` est un champ facultatif qui spécifie le nom de la tâche de sauvegarde et de restauration du stockage. En savoir plus sur [Module complémentaire Cacher MariaDB](https://stash.run/)