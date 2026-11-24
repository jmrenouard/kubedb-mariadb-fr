# Matrice des CRD et opérations

## Ressources personnalisées KubeDB MariaDB

| Type (`Kind`) | Groupe API | Rôle principal | Documentation |
| --- | --- | --- | --- |
| `MariaDB` | `kubedb.com/v1` | Déploiement déclaratif autonome, Galera ou réplication | [CRD MariaDB](../concepts/mariadb.md) |
| `MariaDBVersion` | `catalog.kubedb.com/v1alpha1` | Catalogue des images conteneur et politiques PodSecurity | [MariaDBVersion](../concepts/mariadb-version.md) |
| `MariaDBOpsRequest` | `ops.kubedb.com/v1alpha1` | Opérations Jour 2 : mise à jour, échelle, reconfiguration, TLS, rotation | [MariaDBOpsRequest](../concepts/opsrequest.md) |
| `MariaDBAutoscaler` | `autoscaler.kubedb.com/v1alpha1` | Mise à l'échelle automatique calcul et stockage | [MariaDBAutoscaler](../concepts/autoscaler.md) |
| `MariaDBMigration` | `migrator.kubedb.com/v1alpha1` | Migration par cliché et flux continu via `kubedb-courier` | [MariaDBMigration](../concepts/migrator.md) |
| `AppBinding` | `appcatalog.appscode.com/v1alpha1` | Point d'accès, port et référence de secret applicatif | [AppBinding](../concepts/appbinding.md) |

## Types d'opérations `MariaDBOpsRequest`

| Valeur `spec.type` | Périmètre cible | Sous-spécification associée |
| --- | --- | --- |
| `UpdateVersion` | Image MariaDB | `spec.updateVersion.targetVersion` |
| `HorizontalScaling` | Nombre de réplicas MariaDB ou MaxScale | `spec.horizontalScaling.member` / `.maxscale` |
| `VerticalScaling` | Requêtes et limites CPU / mémoire | `spec.verticalScaling.mariadb` / `.maxscale` |
| `VolumeExpansion` | Capacité du volume PVC | `spec.volumeExpansion.mariadb` / `.maxscale` |
| `Reconfigure` | Paramètres `my.cnf` personnalisés | `spec.configuration.applyConfig` / `.configSecret` |
| `ReconfigureTLS` | Ajout, rotation ou suppression TLS/SSL | `spec.tls.issuerRef` / `.rotateCertificates` / `.remove` |
| `RotateAuth` | Rotation des identifiants base | `spec.authentication` |
| `Restart` | Redémarrage contrôlé par rotation | `spec.restart` |

## Ports réseau et politiques de suppression

| Port | Protocole | Usage |
| --- | --- | --- |
| `3306` | TCP | Connexions client MariaDB et proxy MaxScale |
| `4567` | TCP/UDP | Communication de réplication Galera (`wsrep`) |
| `4568` | TCP | Transfert incrémental d'état Galera (IST) |
| `4444` | TCP | Transfert complet d'instantané Galera (SST) |
| `56790` | TCP | Métriques Prometheus exporter (service `*-stats`) |

| `spec.deletionPolicy` | PetSet et Service | PVC | Secrets | Snapshots |
| --- | --- | --- | --- | --- |
| `DoNotTerminate` | Bloqué par webhook | Conservés | Conservés | Conservés |
| `Halt` | Supprimés | Conservés | Conservés | Conservés |
| `Delete` (Défaut) | Supprimés | Supprimés | Conservés | Conservés |
| `WipeOut` | Supprimés | Supprimés | Supprimés | Supprimés |
