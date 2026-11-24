# Scale a Cluster Horizontally and Vertically

Read [CRDs and Operations Matrix](../03-reference/01-crds-and-operations-matrix.md) before you start this procedure.

## Prerequisites

- Confirm that target `MariaDB` cluster `sample-mariadb` is in `Ready` state in namespace `demo`.
- Install KubeDB Enterprise Ops-Manager operator in the cluster.

## Safety Instructions

**CAUTION:** Verify sufficient CPU and memory capacity on worker nodes before you scale up. Insufficient node capacity keeps database pods in `Pending` state.

## Steps

1. Save this `MariaDBOpsRequest` manifest as `mdops-scale.yaml` to set three replicas:

   ```yaml
   apiVersion: ops.kubedb.com/v1alpha1
   kind: MariaDBOpsRequest
   metadata:
     name: mdops-hscale-up
     namespace: demo
   spec:
     type: HorizontalScaling
     databaseRef:
       name: sample-mariadb
     horizontalScaling:
       member: 3
   ```

2. Apply the scale request in namespace `demo`:

   ```bash
   kubectl apply -f mdops-scale.yaml
   ```

3. Wait for `MariaDBOpsRequest` status `Successful`:

   ```bash
   kubectl get mariadbopsrequest -n demo mdops-hscale-up
   ```

4. Save this `MariaDBOpsRequest` manifest as `mdops-vscale.yaml` to update CPU and memory limits:

   ```yaml
   apiVersion: ops.kubedb.com/v1alpha1
   kind: MariaDBOpsRequest
   metadata:
     name: mdops-vscale
     namespace: demo
   spec:
     type: VerticalScaling
     databaseRef:
       name: sample-mariadb
     verticalScaling:
       mariadb:
         resources:
           requests:
             cpu: "500m"
             memory: "512Mi"
           limits:
             cpu: "1000m"
             memory: "1Gi"
   ```

5. Apply `mdops-vscale.yaml` in namespace `demo`:

   ```bash
   kubectl apply -f mdops-vscale.yaml
   ```

## Verification

1. Check that `kubectl get mariadbopsrequest -n demo` shows `Successful` for both requests.
2. Check that `kubectl get mariadb -n demo sample-mariadb` shows `3` replicas in `Ready` phase.
3. Run `kubectl describe pod -n demo sample-mariadb-0` and confirm updated CPU and memory limits.

## Rollback

1. If pods stay `Pending` after the scale step, create a `MariaDBOpsRequest` manifest with original replica count and lower resource limits.
2. Apply the revert manifest and confirm that `MariaDB` returns to `Ready` phase.
