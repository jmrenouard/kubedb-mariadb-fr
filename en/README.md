> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

## Supported MariaDB Features

| Features | Availability |
| --- | --- |
| Clustering | ✓ |
| Persistent Volume | ✓ |
| Instant Backup | ✓ |
| Scheduled Backup | ✓ |
| Continuous Archiving using `wal-g` | ✓ |
| Initialize using Snapshot | ✓ |
| Initialize using Script (\*.sql, \*sql.gz and/or \*.sh) | ✓ |
| Custom Configuration | ✓ |
| Using Custom docker image | ✓ |
| Builtin Prometheus Discovery | ✓ |
| Using Prometheus operator | ✓ |

## Life Cycle of a MariaDB Object

![lifecycle](../images/root_mariadb-lifecycle.png)

## User Guide

* [Quickstart MariaDB](quickstart/overview.md) with KubeDB Operator.
* Detail concepts of [MariaDB object](concepts/mariadb.md).
* Detail concepts of [MariaDBVersion object](concepts/mariadb-version.md).
* Create [MariaDB Cluster](clustering/galera-cluster.md).
* Create [MariaDB with Custom Configuration](configuration/using-config-file.md).
* Use [Custom RBAC](custom-rbac/using-custom-rbac.md).
* Use [private Docker registry](private-registry/quickstart.md) to deploy MariaDB with KubeDB.
* Initialize [MariaDB with Script](initialization/using-script.md).
* Backup and Restore [MariaDB](backup/stash/overview.md).
* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

## Complete Documentation Index

### Autoscaler ➔ Compute

* [Autoscaling the Compute Resource of a MariaDB Cluster Database](autoscaler/compute/cluster.md)
* [MariaDB Compute Resource Autoscaling](autoscaler/compute/overview.md)

### Autoscaler ➔ Storage

* [Storage Autoscaling of a MariaDB Cluster](autoscaler/storage/cluster.md)
* [MariaDB Vertical Autoscaling](autoscaler/storage/overview.md)

### Backup ➔ Kubestash

* [Application Level Backup and Restore MariaDB database using KubeStash](backup/kubestash/application-level.md)
* [Backup MariaDB using KubeStash Auto-Backup](backup/kubestash/auto-backup.md)
* [Customizing Backup and Restore Process](backup/kubestash/customization.md)
* [Backup and Restore MariaDB database using KubeStash](backup/kubestash/logical.md)
* [MariaDB Backup & Restore Overview](backup/kubestash/overview.md)

### Backup ➔ Stash

* [Backup MariaDB using Stash Auto-Backup](backup/stash/auto-backup.md)
* [Customizing Backup and Restore Process](backup/stash/customization.md)
* [MariaDB Backup & Restore Overview](backup/stash/overview.md)

### Backup ➔ Stash ➔ Logical

* [Backup KubeDB managed MariaDB Cluster using Stash](backup/stash/logical/cluster.md)
* [Backup KubeDB managed standalone MariaDB using Stash](backup/stash/logical/standalone.md)

### Clustering

* [KubeDB - MariaDB Cluster](clustering/galera-cluster.md)
* [KubeDB - MariaDB Cluster](clustering/mariadb-replication.md)
* [MariaDB Clustering](clustering/overview.md)

### Concepts

* [AppBinding](concepts/appbinding.md)
* [MariaDBAutoscaler](concepts/autoscaler.md)
* [MariaDBVersion](concepts/mariadb-version.md)
* [MariaDB](concepts/mariadb.md)
* [MariaDBMigration](concepts/migrator.md)
* [MariaDBOpsRequest](concepts/opsrequest.md)

### Configuration

* [Using Custom Configuration File](configuration/using-config-file.md)
* [Run MariaDB with Custom PodTemplate](configuration/using-pod-template.md)

### Custom-Rbac

* [Using Custom RBAC resources](custom-rbac/using-custom-rbac.md)

### Distributed

* [Distributed MariaDB Galera Cluster Overview](distributed/overview.md)

### Distributed ➔ Autoscaler ➔ Compute

* [Autoscaling the Compute Resource of a Distributed MariaDB Cluster](distributed/autoscaler/compute/cluster.md)
* [Distributed MariaDB Compute Resource Autoscaling](distributed/autoscaler/compute/overview.md)

### Distributed ➔ Autoscaler ➔ Storage

* [Storage Autoscaling of a Distributed MariaDB Cluster](distributed/autoscaler/storage/cluster.md)
* [Distributed MariaDB Storage Autoscaling](distributed/autoscaler/storage/overview.md)

### Distributed ➔ Opsrequest

* [Horizontal Scale Distributed MariaDB](distributed/opsrequest/horizontal_scale.md)

### Failover

* [Exploring Fault Tolerance in MariaDB with KubeDB](failover/guide.md)

### Gitops

* [GitOps MariaDB using KubeDB GitOps Operator](gitops/gitops.md)
* [GitOps Overview for MariaDB](gitops/overview.md)

### Initialization

* [Initialization MariaDB from a Git Repository](initialization/git-sync.md)
* [Initialize MariaDB using Script](initialization/using-script.md)

### Migration

* [MariaDB Database Migration](migration/databasemigration.md)

### Monitoring

* [Monitoring MariaDB with builtin Prometheus](monitoring/builtin-prometheus.md)
* [Monitoring MariaDB with KubeDB](monitoring/overview.md)
* [Monitoring MariaDB Using Prometheus operator](monitoring/prometheus-operator.md)

### Pitr

* [KubeDB MariaDB - Continuous Archiving and Point-in-time Recovery](pitr/nfs.md)
* [KubeDB MariaDB - Continuous Archiving and Point-in-time Recovery](pitr/overview.md)

### Private-Registry

* [Deploy MariaDB from private Docker registry](private-registry/quickstart.md)

### Quickstart

* [MariaDB QuickStart](quickstart/overview.md)

### Recommendation

* [MariaDB Recommendation](recommendation/recommendation.md)

### Reconfigure

* [Reconfigure MariaDB Cluster Database](reconfigure/cluster.md)
* [Reconfiguring MariaDB](reconfigure/overview.md)
* [Reconfigure MariaDB Standalone Database](reconfigure/standalone.md)

### Reconfigure-Tls

* [Reconfigure MariaDB TLS/SSL (Transport Encryption)](reconfigure-tls/cluster.md)
* [Reconfiguring TLS of MariaDB Database](reconfigure-tls/overview.md)

### Restart

* [Restart MariaDB](restart/restart.md)

### Rotate-Auth

* [Rotate Authentication of MariaDB](rotate-auth/overview.md)
* [Rotate Authentication of MariaDB](rotate-auth/rotateauth.md)

### Scaling ➔ Horizontal-Scaling

* [Horizontal Scale MariaDB](scaling/horizontal-scaling/cluster.md)
* [Horizontal Scale MaxScale](scaling/horizontal-scaling/maxscale.md)
* [MariaDB Horizontal Scaling](scaling/horizontal-scaling/overview.md)

### Scaling ➔ Vertical-Scaling

* [Vertical Scale MariaDB Cluster](scaling/vertical-scaling/cluster.md)
* [Vertical Scale MaxScale Server](scaling/vertical-scaling/maxscale.md)
* [MariaDB Vertical Scaling](scaling/vertical-scaling/overview.md)

### Tls

* [Configure TLS/SSL in MariaDB](tls/configure.md)
* [MariaDB TLS/SSL Encryption](tls/overview.md)

### Update-Version

* [Update Version of MariaDB Cluster](update-version/cluster.md)
* [Updating MariaDB Version Overview](update-version/overview.md)

### Volume-Expansion

* [MaxScale Volume Expansion](volume-expansion/maxscale.md)
* [MariaDB Volume Expansion](volume-expansion/overview.md)
* [MariaDB Volume Expansion](volume-expansion/volume-expansion.md)

