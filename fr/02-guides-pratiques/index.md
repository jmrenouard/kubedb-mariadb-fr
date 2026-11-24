# Guides pratiques (FR)

Procédures opérationnelles rédigées selon la norme ASD-STF100 pour déployer, redimensionner, sauvegarder et rétablir des clusters KubeDB MariaDB.

- [Déployer un cluster répliqué avec MaxScale](01-deployer-replication-avec-maxscale.md) : déployer une topologie primaire-réplica avec routage MaxScale.
- [Mettre à l'échelle un cluster MariaDB](02-mettre-a-lechelle-cluster-mariadb.md) : ajuster les réplicas et les limites CPU/mémoire via `MariaDBOpsRequest`.
- [Exécuter une sauvegarde et une restauration PITR](03-executer-sauvegarde-et-restauration-pitr.md) : restaurer un cluster MariaDB à un horodatage exact avec KubeStash.
- [Gérer un basculement primaire MaxScale](04-gerer-basculement-primaire-maxscale.md) : contrôler la promotion du primaire avec `maxctrl` après perte d'un nœud.
