# CLI and kubectl Cheatsheet

## Inspect KubeDB Resources

| Task | Command |
| --- | --- |
| List supported MariaDB versions | `kubectl get mariadbversions` |
| Check MariaDB instance status | `kubectl get mariadb,petset,svc,pvc,secret -n demo` |
| Watch `MariaDBOpsRequest` progress | `kubectl get mariadbopsrequest -n demo -w` |
| Read generated root username | `kubectl get secret -n demo <db>-auth -o jsonpath='{.data.username}' \| base64 -d` |
| Read generated root password | `kubectl get secret -n demo <db>-auth -o jsonpath='{.data.password}' \| base64 -d` |
| Inspect KubeStash backups | `kubectl get backupstorage,backupconfiguration,volumesnapshots -n demo` |

## MariaDB and MaxScale Verification Commands

```bash
kubectl exec -it -n demo svc/<db>-mx -- maxctrl list servers
kubectl exec -it -n demo <db>-0 -- mariadb -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size';"
kubectl exec -it -n demo <db>-0 -- mariadb -u root -p -e "SHOW SLAVE STATUS\G"
```

## `MariaDBOpsRequest` Condition Phases

- `Pending`: Waiting for admission and lock acquisition.
- `Progressing`: Actively rolling pods, expanding volumes, or rotating credentials.
- `Successful`: Operation completed cleanly.
- `Failed`: Precondition check or execution failed; inspect `status.conditions`.
