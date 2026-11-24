# Explanation (EN)

Architectural background, design trade-offs, and lifecycle mechanics behind KubeDB MariaDB topologies and Day-2 operations.

- [Clustering and Failover Architecture](01-clustering-and-failover-architecture.md): Trade-offs between standalone pods, Galera multi-primary replication, and MaxScale primary-replica failover.
- [Storage, Backup, and Day-2 Reconciliation](02-storage-backup-and-day2-reconciliation.md): Durable storage lifecycle, Stash vs KubeStash backup pipelines, continuous binlog PITR, and `MariaDBOpsRequest` control loops.
