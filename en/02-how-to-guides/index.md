# How-To Guides (EN)

Operational runbooks written in strict ASD-STE100 Issue 9 for KubeDB MariaDB cluster deploy, scale, backup, and recovery tasks.

- [Deploy a Replication Cluster with MaxScale](01-deploy-replication-cluster-with-maxscale.md): Deploy primary-replica MariaDB with MaxScale query routing and verify server state.
- [Scale a Cluster Horizontally and Vertically](02-scale-cluster-horizontally-and-vertically.md): Change MariaDB replica count and compute limits with `MariaDBOpsRequest`.
- [Perform Backup and PITR Recovery](03-perform-backup-and-pitr-recovery.md): Trigger KubeStash backup snapshots and restore to a recovery timestamp.
- [Handle MaxScale Primary Failover](04-handle-maxscale-primary-failover.md): Verify primary promotion with `maxctrl` after a node failure and restore node count.
