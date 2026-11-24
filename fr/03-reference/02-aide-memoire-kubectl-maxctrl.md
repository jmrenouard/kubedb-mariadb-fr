# Aide-mémoire kubectl et maxctrl

## Inspection des ressources KubeDB

| Tâche | Commande |
| --- | --- |
| Lister les versions MariaDB disponibles | `kubectl get mariadbversions` |
| Contrôler l'état de l'instance MariaDB | `kubectl get mariadb,petset,svc,pvc,secret -n demo` |
| Suivre une ressource `MariaDBOpsRequest` | `kubectl get mariadbopsrequest -n demo -w` |
| Lire l'utilisateur root généré | `kubectl get secret -n demo <db>-auth -o jsonpath='{.data.username}' \| base64 -d` |
| Lire le mot de passe root généré | `kubectl get secret -n demo <db>-auth -o jsonpath='{.data.password}' \| base64 -d` |
| Inspecter les sauvegardes KubeStash | `kubectl get backupstorage,backupconfiguration,volumesnapshots -n demo` |

## Commandes de vérification MariaDB et MaxScale

```bash
kubectl exec -it -n demo svc/<db>-mx -- maxctrl list servers
kubectl exec -it -n demo <db>-0 -- mariadb -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size';"
kubectl exec -it -n demo <db>-0 -- mariadb -u root -p -e "SHOW SLAVE STATUS\G"
```

## Phases de statut `MariaDBOpsRequest`

- `Pending` : en attente de validation et d'acquisition de verrou.
- `Progressing` : exécution progressive sur les pods, volumes ou secrets.
- `Successful` : opération terminée avec succès.
- `Failed` : échec d'une précondition ou de l'exécution ; inspectez `status.conditions`.
