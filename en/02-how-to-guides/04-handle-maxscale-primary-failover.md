# Handle MaxScale Primary Failover

Read the [Failover Architecture Guide](../04-explanation/01-clustering-and-failover-architecture.md) before you start this procedure.

## Prerequisites

- Verify that `ha-mariadb` operates in `MariaDBReplication` mode with MaxScale enabled.
- Ensure `kubectl` has permission to list pods and run `kubectl exec` in namespace `demo`.

## Safety Instructions

**CAUTION:** Do not write directly to replica pods during failover. Direct writes bypass MaxScale routing and cause GTID divergence.

## Steps

1. Check current server roles through MaxScale before intervention:

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers
   ```

2. Check Kubernetes pod status and pod restart counts in namespace `demo`:

   ```bash
   kubectl get pods -n demo -l app.kubernetes.io/instance=ha-mariadb
   ```

3. Wait for `ReplicationMonitor` to promote a healthy replica when the old primary fails.
4. Check `maxctrl list servers` again to confirm the newly promoted `Master, Running` node:

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers
   ```

5. If the old primary pod fails to rejoin cleanly, inspect pod events and MariaDB logs:

   ```bash
   kubectl describe pod -n demo ha-mariadb-0
   kubectl logs -n demo ha-mariadb-0 -c mariadb
   ```

**NOTE:** KubeDB PetSet automatically recreates a deleted primary pod and rejoins it as a replica.

## Verification

1. Run `kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers`.
2. Confirm that one node reports `Master, Running` and the other nodes report `Slave, Running`.
3. Connect through MaxScale service `svc/ha-mariadb-mx` and run a read-write check query:

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- mariadb -u root -p -e "SELECT @@hostname, @@read_only;"
   ```

## Rollback

1. If traffic stalls after recovery, restart the MaxScale proxy pod safely:

   ```bash
   kubectl delete pod -n demo -l app.kubernetes.io/component=maxscale
   ```

2. Wait for the new MaxScale pod to reach `Ready` state and verify `maxctrl list servers`.
