# Explications (FR)

Principes d'architecture, compromis de conception et mécanismes de réconciliation sous-jacents aux topologies KubeDB MariaDB et aux opérations Jour 2.

- [Architecture de clustering et basculement](01-architecture-clustering-et-basculement.md) : compromis entre déploiement autonome, réplication multi-primaire Galera et basculement automatique MaxScale.
- [Stockage, sauvegarde et réconciliation](02-stockage-sauvegarde-et-reconciliation.md) : cycle de vie des volumes durables, pipelines KubeStash/Stash, archivage PITR continu et boucle `MariaDBOpsRequest`.
