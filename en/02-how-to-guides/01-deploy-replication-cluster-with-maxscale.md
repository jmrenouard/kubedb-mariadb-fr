# Deploy a Replication Cluster with MaxScale

Read [CLI and kubectl Cheatsheet](../03-reference/02-cli-and-kubectl-cheatsheet.md) before you start this procedure.

## Prerequisites

- Install `kubectl` and connect to the target Kubernetes cluster.
- Install KubeDB Community and Enterprise operators on the cluster.
- Create namespace `demo` in the cluster.

## Steps

1. Save this `MariaDB` replication manifest as `ha-mariadb.yaml`:

   ```yaml
   apiVersion: kubedb.com/v1
   kind: MariaDB
   metadata:
     name: ha-mariadb
     namespace: demo
   spec:
     version: "11.8.5"
     replicas: 3
     topology:
       mode: MariaDBReplication
       maxscale:
         replicas: 1
     storageType: Durable
     storage:
       storageClassName: "standard"
       accessModes:
         - ReadWriteOnce
       resources:
         requests:
           storage: 1Gi
     deletionPolicy: WipeOut
   ```

2. Apply the `ha-mariadb.yaml` manifest in namespace `demo`:

   ```bash
   kubectl apply -f ha-mariadb.yaml
   ```

3. Wait for all database pods and the MaxScale pod to start:

   ```bash
   kubectl get pods -n demo -l app.kubernetes.io/instance=ha-mariadb
   ```

**NOTE:** The MaxScale proxy service listens on port `3306` after all replicas reach `Ready`.

## Verification

1. Run `maxctrl list servers` inside the MaxScale service container:

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers
   ```

2. Check that one primary shows `Master, Running` and two replicas show `Slave, Running`.
3. Check that the `MariaDB` resource phase shows `Ready`:

   ```bash
   kubectl get mariadb -n demo ha-mariadb
   ```

## Rollback

1. If the cluster fails health checks, delete the `MariaDB` object in namespace `demo`:

   ```bash
   kubectl delete mariadb -n demo ha-mariadb
   ```

2. Verify that `kubectl get pods -n demo` shows no remaining `ha-mariadb` pods.
