# Backup and Point-in-Time Recovery with KubeStash

In this tutorial, you learn how KubeStash and `MariaDBArchiver` combine full volume snapshots with continuous binlog archiving to recover dropped data.

```mermaid
flowchart LR
  Cluster["MariaDB Cluster"] -->|Continuous Binlogs| Sidekick["Sidekick Container"]
  Sidekick -->|Upload| Repo["BackupStorage (S3 / NFS)"]
  Snap["VolumeSnapshot"] --> Restorer["Restore MariaDB CR"]
  Repo -->|Replay up to recoveryTimestamp| Restorer
  Restorer --> Restored["Restored MariaDB Cluster"]
```

## 1. Prepare Storage Credentials and `BackupStorage`

Create the storage secret and `BackupStorage` custom resource in namespace `demo`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: s3-secret
  namespace: demo
type: Opaque
stringData:
  AWS_ACCESS_KEY_ID: "replace-with-access-key"
  AWS_SECRET_ACCESS_KEY: "replace-with-secret-key"
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: s3-storage
  namespace: demo
spec:
  storage:
    provider: s3
    s3:
      bucket: kubedb-mariadb-backups
      region: us-east-1
      secretName: s3-secret
  usagePolicy:
    allowedNamespaces:
      from: Same
  default: true
```

```bash
kubectl apply -f s3-secret.yaml
kubectl apply -f s3-storage.yaml
```

## 2. Configure `RetentionPolicy` and `MariaDBArchiver`

Enable continuous binlog archiving alongside full scheduled backups:

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: demo-retention
  namespace: demo
spec:
  maxRetentionPeriod: 30d
  successfulSnapshots: 5
  failedSnapshots: 2
```

```yaml
apiVersion: archiver.kubedb.com/v1alpha1
kind: MariaDBArchiver
metadata:
  name: mariadb-archiver
  namespace: demo
spec:
  pause: false
  databaseRef:
    name: mariadb
    namespace: demo
  fullBackup:
    driver: VolumeSnapshotter
    task:
      name: mariadb-volumesnapshot-backup
    schedule: "*/5 * * * *"
    retentionPolicy:
      name: demo-retention
      namespace: demo
    backupStorage:
      name: s3-storage
      namespace: demo
```

```bash
kubectl apply -f retention.yaml
kubectl apply -f mariadb-archiver.yaml
kubectl get backupconfiguration,volumesnapshots -n demo
```

## 3. Record Timestamp Before Simulated Drop

Insert sample rows and capture `NOW()` before dropping `demo_table`:

```mysql
MariaDB [hello]> SELECT COUNT(*) FROM demo_table;
+----------+
| COUNT(*) |
+----------+
|       10 |
+----------+
1 row in set (0.001 sec)

MariaDB [hello]> SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2026-08-12 10:15:00 |
+---------------------+
1 row in set (0.000 sec)
```

## 4. Restore Using `spec.init.archiver`

Deploy a new `MariaDB` resource targeting `recoveryTimestamp`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: restore-mariadb
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  init:
    archiver:
      recoveryTimestamp: "2026-08-12T10:15:00Z"
  deletionPolicy: WipeOut
```

```bash
kubectl apply -f restore-mariadb.yaml
kubectl get mariadb -n demo
```

## Next Steps

- Execute production PITR steps in [Perform Backup and PITR Recovery](../02-how-to-guides/03-perform-backup-and-pitr-recovery.md).
- Inspect the architecture in [Storage, Backup, and Day-2 Reconciliation](../04-explanation/02-storage-backup-and-day2-reconciliation.md) and [PITR Overview](../pitr/overview.md).
