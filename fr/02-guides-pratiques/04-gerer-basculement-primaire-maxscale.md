# Gérer un basculement primaire MaxScale

Consultez le guide d'architecture [Clustering et basculement](../04-explications/01-architecture-clustering-et-basculement.md) avant de démarrer cette procédure.

## Prérequis

- Vérifiez que le cluster `ha-mariadb` fonctionne en mode `MariaDBReplication` avec MaxScale actif.
- Disposez des droits `kubectl` pour lister les pods et exécuter `kubectl exec` dans `demo`.

## Consignes de sécurité

**ATTENTION :** N'écrivez jamais directement sur un pod réplica pendant un basculement. Une écriture directe contourne MaxScale et cause une divergence GTID.

## Étapes

1. Relevez les rôles initiaux des serveurs avec `maxctrl` :

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers
   ```

2. Vérifiez l'état et les redémarrages des pods dans `demo` :

   ```bash
   kubectl get pods -n demo -l app.kubernetes.io/instance=ha-mariadb
   ```

3. Attendez que `ReplicationMonitor` promeuve un réplica sain après la panne du primaire.
4. Exécutez de nouveau `maxctrl list servers` pour identifier le nouveau nœud `Master, Running` :

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers
   ```

5. Si l'ancien primaire tarde à rejoindre le cluster, examinez les événements et journaux :

   ```bash
   kubectl describe pod -n demo ha-mariadb-0
   kubectl logs -n demo ha-mariadb-0 -c mariadb
   ```

**NOTE :** Le contrôleur `PetSet` recrée automatiquement tout pod primaire supprimé puis le réintègre comme réplica.

## Vérification

1. Exécutez `kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers`.
2. Vérifiez qu'un seul nœud indique `Master, Running` et que les autres indiquent `Slave, Running`.
3. Connectez un client sur le service MaxScale puis vérifiez l'hôte actif :

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- mariadb -u root -p -e "SELECT @@hostname, @@read_only;"
   ```

## Retour arrière

1. Si le routage reste bloqué après la reprise, redémarrez le pod proxy MaxScale :

   ```bash
   kubectl delete pod -n demo -l app.kubernetes.io/component=maxscale
   ```

2. Attendez la phase `Ready` du pod MaxScale puis exécutez `maxctrl list servers`.
