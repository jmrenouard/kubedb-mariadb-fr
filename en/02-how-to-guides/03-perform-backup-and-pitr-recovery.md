# Perform Backup and PITR Recovery

Read [Backup and PITR Workflow](../01-tutorials/02-backup-and-pitr-workflow.md) before you start this procedure.

## Prerequisites

- Verify that `BackupStorage`, `RetentionPolicy`, and `MariaDBArchiver` exist in namespace `demo`.
- Confirm that a recent `VolumeSnapshot` and archived binlogs exist in remote storage.

## Safety Instructions

**WARNING:** Restore data into a new `MariaDB` object rather than an active production instance. Do not overwrite an active instance because you lose live data.

## Steps

1. Record the target recovery UTC timestamp before data corruption occurred.
2. Save this recovery manifest as `restore-mariadb.yaml` with `spec.init.archiver.recoveryTimestamp`:

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

3. Apply `restore-mariadb.yaml` in namespace `demo`:

   ```bash
   kubectl apply -f restore-mariadb.yaml
   ```

4. Monitor restore pods and database pods until status reaches `Ready`:

   ```bash
   kubectl get pods,mariadb -n demo
   ```

## Verification

1. Run `kubectl get mariadb -n demo restore-mariadb` and verify `Ready` phase.
2. Connect to `restore-mariadb-0` and count restored rows in the target table:

   ```bash
   kubectl exec -it -n demo restore-mariadb-0 -- bash
   ```

   ```mysql
   MariaDB [hello]> SELECT COUNT(*) FROM demo_table;
   ```

3. Verify that all expected rows match the source record count before the incident.

## Rollback

1. If the restored timestamp shows incomplete data, delete the failed `restore-mariadb` instance:

   ```bash
   kubectl delete mariadb -n demo restore-mariadb
   ```

2. Update `spec.init.archiver.recoveryTimestamp` in `restore-mariadb.yaml` and run `kubectl apply -f restore-mariadb.yaml` again.
