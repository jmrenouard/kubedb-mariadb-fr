> Vous êtes nouveau sur KubeDB ? Commencez [ici](https://kubedb.com/docs/v2026.7.10/README), ou parcourez le [Portail Diataxis FR](index.md) ([Tutoriels](01-tutoriels/index.md) | [Guides pratiques](02-guides-pratiques/index.md) | [Référence](03-reference/index.md) | [Explications](04-explications/index.md)).

## Fonctionnalités MariaDB prises en charge

| Caractéristiques | Disponibilité |
| --- | --- |
| Regroupement | ✓ |
| Volume persistant | ✓ |
| Sauvegarde instantanée | ✓ |
| Sauvegarde planifiée | ✓ |
| Archivage continu à l'aide `wal-g` | ✓ |
| Initialiser à l'aide d'un instantané | ✓ |
| Initialiser à l'aide d'un script (\*.sql, \*sql.gz et/ou \*.sh) | ✓ |
| Configuration personnalisée | ✓ |
| Utilisation d'une image Docker personnalisée | ✓ |
| Découverte Prometheus intégrée | ✓ |
| Utiliser l'opérateur Prometheus | ✓ |

## Cycle de vie d'un objet MariaDB

![lifecycle](../images/root_mariadb-lifecycle.png)

## Guide de l'utilisateur

* [Démarrage rapide MariaDB](quickstart/overview.md) avec l'opérateur KubeDB.
* Concepts détaillés de [Objet MariaDB](concepts/mariadb.md).
* Concepts détaillés de [Objet MariaDBVersion](concepts/mariadb-version.md).
* Créer [Cluster MariaDB](clustering/galera-cluster.md).
* Créer [MariaDB avec configuration personnalisée](configuration/using-config-file.md).
* Utiliser [RBAC personnalisé](custom-rbac/using-custom-rbac.md).
* Utiliser [registre Docker privé](private-registry/quickstart.md) pour déployer MariaDB avec KubeDB.
* Initialiser [MariaDB avec script](initialization/using-script.md).
* Sauvegarde et restauration [MariaDB](backup/stash/overview.md).
* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

## Index complet des pages

### Autoscaler ➔ Calcul

* [Mise à l'échelle automatique de la ressource de calcul d'une base de données de cluster MariaDB](autoscaler/compute/cluster.md)
* [Mise à l'échelle automatique des ressources de calcul MariaDB](autoscaler/compute/overview.md)

### Autoscaler ➔ Stockage

* [Mise à l'échelle automatique du stockage d'un cluster MariaDB](autoscaler/storage/cluster.md)
* [Mise à l'échelle verticale automatique de MariaDB](autoscaler/storage/overview.md)

### Sauvegarde ➔ KubeStash

* [Sauvegarde et restauration au niveau de l'application de la base de données MariaDB à l'aide de KubeStash](backup/kubestash/application-level.md)
* [Sauvegarder MariaDB à l'aide de la sauvegarde automatique KubeStash](backup/kubestash/auto-backup.md)
* [Personnalisation du processus de sauvegarde et de restauration](backup/kubestash/customization.md)
* [Sauvegarder et restaurer la base de données MariaDB à l'aide de KubeStash](backup/kubestash/logical.md)
* [Présentation de la sauvegarde et de la restauration MariaDB](backup/kubestash/overview.md)

### Sauvegarde ➔ Stash

* [Sauvegarder MariaDB à l'aide de la sauvegarde automatique Stash](backup/stash/auto-backup.md)
* [Personnalisation du processus de sauvegarde et de restauration](backup/stash/customization.md)
* [Présentation de la sauvegarde et de la restauration MariaDB](backup/stash/overview.md)

### Sauvegarde ➔ Stash ➔ Logique

* [Sauvegarder le cluster MariaDB géré par KubeDB à l'aide de Stash](backup/stash/logical/cluster.md)
* [Sauvegarder une instance MariaDB autonome gérée par KubeDB avec Stash](backup/stash/logical/standalone.md)

### Clustering

* [KubeDB-Cluster MariaDB](clustering/galera-cluster.md)
* [KubeDB-Cluster MariaDB](clustering/mariadb-replication.md)
* [Clustering MariaDB](clustering/overview.md)

### Concepts

* [Liaison d'application](concepts/appbinding.md)
* [MariaDBAutoscaler](concepts/autoscaler.md)
* [Version MariaDB](concepts/mariadb-version.md)
* [MariaDB](concepts/mariadb.md)
* [MariaDBMigration](concepts/migrator.md)
* [MariaDBOpsRequest](concepts/opsrequest.md)

### Configuration

* [Utilisation d'un fichier de configuration personnalisé](configuration/using-config-file.md)
* [Exécutez MariaDB avec un PodTemplate personnalisé](configuration/using-pod-template.md)

### RBAC personnalisé

* [Utilisation de ressources RBAC personnalisées](custom-rbac/using-custom-rbac.md)

### Déploiement distribué

* [Présentation du cluster MariaDB Galera distribué](distributed/overview.md)

### Déploiement distribué ➔ Autoscaler ➔ Calcul

* [Mise à l'échelle automatique de la ressource de calcul d'un cluster MariaDB distribué](distributed/autoscaler/compute/cluster.md)
* [Mise à l'échelle automatique des ressources de calcul MariaDB distribuées](distributed/autoscaler/compute/overview.md)

### Déploiement distribué ➔ Autoscaler ➔ Stockage

* [Mise à l'échelle automatique du stockage d'un cluster MariaDB distribué](distributed/autoscaler/storage/cluster.md)
* [Mise à l'échelle automatique du stockage MariaDB distribué](distributed/autoscaler/storage/overview.md)

### Déploiement distribué ➔ OpsRequest

* [MariaDB distribuée à l'échelle horizontale](distributed/opsrequest/horizontal_scale.md)

### Basculement (Failover)

* [Explorer la tolérance aux pannes dans MariaDB avec KubeDB](failover/guide.md)

### GitOps

* [GitOps MariaDB utilisant l'opérateur KubeDB GitOps](gitops/gitops.md)
* [Présentation de GitOps pour MariaDB](gitops/overview.md)

### Initialisation

* [Initialisation MariaDB à partir d'un référentiel Git](initialization/git-sync.md)
* [Initialiser MariaDB à l'aide d'un script](initialization/using-script.md)

### Migration

* [Migration de la base de données MariaDB](migration/databasemigration.md)

### Supervision (Monitoring)

* [Surveillance de MariaDB avec Prometheus intégré](monitoring/builtin-prometheus.md)
* [Surveillance de MariaDB avec KubeDB](monitoring/overview.md)
* [Surveillance de MariaDB à l'aide de l'opérateur Prometheus](monitoring/prometheus-operator.md)

### Récupération ponctuelle (PITR)

* [KubeDB MariaDB - Archivage continu et récupération ponctuelle](pitr/nfs.md)
* [KubeDB MariaDB - Archivage continu et récupération ponctuelle (PITR)](pitr/overview.md)

### Registre privé

* [Déployer MariaDB à partir du registre Docker privé](private-registry/quickstart.md)

### Démarrage rapide

* [Démarrage rapide de MariaDB](quickstart/overview.md)

### Recommandations

* [Recommandation MariaDB](recommendation/recommendation.md)

### Reconfiguration

* [Reconfigurer la base de données du cluster MariaDB](reconfigure/cluster.md)
* [Reconfiguration de MariaDB](reconfigure/overview.md)
* [Reconfigurer la base de données autonome MariaDB](reconfigure/standalone.md)

### Reconfiguration TLS

* [Reconfigurer MariaDB TLS/SSL (chiffrement de transport)](reconfigure-tls/cluster.md)
* [Reconfiguration de TLS de la base de données MariaDB](reconfigure-tls/overview.md)

### Redémarrage

* [Redémarrer MariaDB](restart/restart.md)

### Rotation des identifiants

* [Rotation de l'authentification de MariaDB](rotate-auth/overview.md)
* [Rotation de l'authentification de MariaDB](rotate-auth/rotateauth.md)

### Mise à l'échelle ➔ Horizontale

* [MariaDB à échelle horizontale](scaling/horizontal-scaling/cluster.md)
* [Échelle horizontale MaxScale](scaling/horizontal-scaling/maxscale.md)
* [Mise à l'échelle horizontale de MariaDB](scaling/horizontal-scaling/overview.md)

### Mise à l'échelle ➔ Verticale

* [Cluster MariaDB à échelle verticale](scaling/vertical-scaling/cluster.md)
* [Serveur MaxScale à échelle verticale](scaling/vertical-scaling/maxscale.md)
* [Mise à l'échelle verticale de MariaDB](scaling/vertical-scaling/overview.md)

### TLS / SSL

* [Configurer TLS/SSL dans MariaDB](tls/configure.md)
* [Chiffrement MariaDB TLS/SSL](tls/overview.md)

### Mise à jour de version

* [Mettre à jour la version d'un cluster MariaDB](update-version/cluster.md)
* [Aperçu de la mise à jour de version MariaDB](update-version/overview.md)

### Extension de volume

* [Extension de volume MaxScale](volume-expansion/maxscale.md)
* [Extension du volume MariaDB](volume-expansion/overview.md)
* [Extension du volume MariaDB](volume-expansion/volume-expansion.md)

