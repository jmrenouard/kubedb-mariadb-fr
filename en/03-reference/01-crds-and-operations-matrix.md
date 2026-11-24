# CRDs and Operations Matrix

## KubeDB MariaDB Custom Resources

| Kind | API Group | Primary Purpose | Reference Guide |
| --- | --- | --- | --- |
| `MariaDB` | `kubedb.com/v1` | Declarative standalone, Galera, or replication cluster | [MariaDB CRD](../concepts/mariadb.md) |
| `MariaDBVersion` | `catalog.kubedb.com/v1alpha1` | Supported container images and PodSecurity metadata | [MariaDBVersion](../concepts/mariadb-version.md) |
| `MariaDBOpsRequest` | `ops.kubedb.com/v1alpha1` | Day-2 upgrade, scale, reconfigure, TLS, restart, rotate | [MariaDBOpsRequest](../concepts/opsrequest.md) |
| `MariaDBAutoscaler` | `autoscaler.kubedb.com/v1alpha1` | Automated compute and storage autoscaling | [MariaDBAutoscaler](../concepts/autoscaler.md) |
| `MariaDBMigration` | `migrator.kubedb.com/v1alpha1` | Snapshot and streaming migration via `kubedb-courier` | [MariaDBMigration](../concepts/migrator.md) |
| `AppBinding` | `appcatalog.appscode.com/v1alpha1` | Connection endpoint, port, and auth secret binding | [AppBinding](../concepts/appbinding.md) |

## `MariaDBOpsRequest` Operation Types

| `spec.type` Value | Target Scope | Supported Reconcile Sub-Spec |
| --- | --- | --- |
| `UpdateVersion` | Database image tag | `spec.updateVersion.targetVersion` |
| `HorizontalScaling` | MariaDB or MaxScale replicas | `spec.horizontalScaling.member` / `.maxscale` |
| `VerticalScaling` | CPU and memory requests/limits | `spec.verticalScaling.mariadb` / `.maxscale` |
| `VolumeExpansion` | PVC storage size | `spec.volumeExpansion.mariadb` / `.maxscale` |
| `Reconfigure` | Custom MariaDB `my.cnf` parameters | `spec.configuration.applyConfig` / `.configSecret` |
| `ReconfigureTLS` | Enable, rotate, or remove TLS/SSL | `spec.tls.issuerRef` / `.rotateCertificates` / `.remove` |
| `RotateAuth` | Database credential rotation | `spec.authentication` |
| `Restart` | Controlled rolling restart | `spec.restart` |

## Network Ports and Deletion Policies

| Resource / Port | Protocol | Usage |
| --- | --- | --- |
| `3306` | TCP | MariaDB client connections and MaxScale proxy frontend |
| `4567` | TCP/UDP | Galera replication communication (`wsrep`) |
| `4568` | TCP | Galera Incremental State Transfer (IST) |
| `4444` | TCP | Galera State Snapshot Transfer (SST) |
| `56790` | TCP | Prometheus exporter metrics endpoint (`*-stats` service) |

| `spec.deletionPolicy` | PetSet & Service | PVCs | Secrets | Snapshots |
| --- | --- | --- | --- | --- |
| `DoNotTerminate` | Blocked by webhook | Preserved | Preserved | Preserved |
| `Halt` | Deleted | Preserved | Preserved | Preserved |
| `Delete` (Default) | Deleted | Deleted | Preserved | Preserved |
| `WipeOut` | Deleted | Deleted | Deleted | Deleted |
