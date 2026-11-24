# KubeDB MariaDB Documentation - Combined (EN)

<!-- PAGE_START: README.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

## Supported MariaDB Features

| Features | Availability |
| --- | --- |
| Clustering | ✓ |
| Persistent Volume | ✓ |
| Instant Backup | ✓ |
| Scheduled Backup | ✓ |
| Continuous Archiving using `wal-g` | ✓ |
| Initialize using Snapshot | ✓ |
| Initialize using Script (\*.sql, \*sql.gz and/or \*.sh) | ✓ |
| Custom Configuration | ✓ |
| Using Custom docker image | ✓ |
| Builtin Prometheus Discovery | ✓ |
| Using Prometheus operator | ✓ |

## Life Cycle of a MariaDB Object

![lifecycle](images/root_mariadb-lifecycle.png)

## User Guide

* [Quickstart MariaDB](en/quickstart/overview.md) with KubeDB Operator.
* Detail concepts of [MariaDB object](en/concepts/mariadb.md).
* Detail concepts of [MariaDBVersion object](en/concepts/mariadb-version.md).
* Create [MariaDB Cluster](en/clustering/galera-cluster.md).
* Create [MariaDB with Custom Configuration](en/configuration/using-config-file.md).
* Use [Custom RBAC](en/custom-rbac/using-custom-rbac.md).
* Use [private Docker registry](en/private-registry/quickstart.md) to deploy MariaDB with KubeDB.
* Initialize [MariaDB with Script](en/initialization/using-script.md).
* Backup and Restore [MariaDB](en/backup/stash/overview.md).
* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

## Complete Documentation Index

### Autoscaler ➔ Compute

* [Autoscaling the Compute Resource of a MariaDB Cluster Database](en/autoscaler/compute/cluster.md)
* [MariaDB Compute Resource Autoscaling](en/autoscaler/compute/overview.md)

### Autoscaler ➔ Storage

* [Storage Autoscaling of a MariaDB Cluster](en/autoscaler/storage/cluster.md)
* [MariaDB Vertical Autoscaling](en/autoscaler/storage/overview.md)

### Backup ➔ Kubestash

* [Application Level Backup and Restore MariaDB database using KubeStash](en/backup/kubestash/application-level.md)
* [Backup MariaDB using KubeStash Auto-Backup](en/backup/kubestash/auto-backup.md)
* [Customizing Backup and Restore Process](en/backup/kubestash/customization.md)
* [Backup and Restore MariaDB database using KubeStash](en/backup/kubestash/logical.md)
* [MariaDB Backup & Restore Overview](en/backup/kubestash/overview.md)

### Backup ➔ Stash

* [Backup MariaDB using Stash Auto-Backup](en/backup/stash/auto-backup.md)
* [Customizing Backup and Restore Process](en/backup/stash/customization.md)
* [MariaDB Backup & Restore Overview](en/backup/stash/overview.md)

### Backup ➔ Stash ➔ Logical

* [Backup KubeDB managed MariaDB Cluster using Stash](en/backup/stash/logical/cluster.md)
* [Backup KubeDB managed standalone MariaDB using Stash](en/backup/stash/logical/standalone.md)

### Clustering

* [KubeDB - MariaDB Cluster](en/clustering/galera-cluster.md)
* [KubeDB - MariaDB Cluster](en/clustering/mariadb-replication.md)
* [MariaDB Clustering](en/clustering/overview.md)

### Concepts

* [AppBinding](en/concepts/appbinding.md)
* [MariaDBAutoscaler](en/concepts/autoscaler.md)
* [MariaDBVersion](en/concepts/mariadb-version.md)
* [MariaDB](en/concepts/mariadb.md)
* [MariaDBMigration](en/concepts/migrator.md)
* [MariaDBOpsRequest](en/concepts/opsrequest.md)

### Configuration

* [Using Custom Configuration File](en/configuration/using-config-file.md)
* [Run MariaDB with Custom PodTemplate](en/configuration/using-pod-template.md)

### Custom-Rbac

* [Using Custom RBAC resources](en/custom-rbac/using-custom-rbac.md)

### Distributed

* [Distributed MariaDB Galera Cluster Overview](en/distributed/overview.md)

### Distributed ➔ Autoscaler ➔ Compute

* [Autoscaling the Compute Resource of a Distributed MariaDB Cluster](en/distributed/autoscaler/compute/cluster.md)
* [Distributed MariaDB Compute Resource Autoscaling](en/distributed/autoscaler/compute/overview.md)

### Distributed ➔ Autoscaler ➔ Storage

* [Storage Autoscaling of a Distributed MariaDB Cluster](en/distributed/autoscaler/storage/cluster.md)
* [Distributed MariaDB Storage Autoscaling](en/distributed/autoscaler/storage/overview.md)

### Distributed ➔ Opsrequest

* [Horizontal Scale Distributed MariaDB](en/distributed/opsrequest/horizontal_scale.md)

### Failover

* [Exploring Fault Tolerance in MariaDB with KubeDB](en/failover/guide.md)

### Gitops

* [GitOps MariaDB using KubeDB GitOps Operator](en/gitops/gitops.md)
* [GitOps Overview for MariaDB](en/gitops/overview.md)

### Initialization

* [Initialization MariaDB from a Git Repository](en/initialization/git-sync.md)
* [Initialize MariaDB using Script](en/initialization/using-script.md)

### Migration

* [MariaDB Database Migration](en/migration/databasemigration.md)

### Monitoring

* [Monitoring MariaDB with builtin Prometheus](en/monitoring/builtin-prometheus.md)
* [Monitoring MariaDB with KubeDB](en/monitoring/overview.md)
* [Monitoring MariaDB Using Prometheus operator](en/monitoring/prometheus-operator.md)

### Pitr

* [KubeDB MariaDB - Continuous Archiving and Point-in-time Recovery](en/pitr/nfs.md)
* [KubeDB MariaDB - Continuous Archiving and Point-in-time Recovery](en/pitr/overview.md)

### Private-Registry

* [Deploy MariaDB from private Docker registry](en/private-registry/quickstart.md)

### Quickstart

* [MariaDB QuickStart](en/quickstart/overview.md)

### Recommendation

* [MariaDB Recommendation](en/recommendation/recommendation.md)

### Reconfigure

* [Reconfigure MariaDB Cluster Database](en/reconfigure/cluster.md)
* [Reconfiguring MariaDB](en/reconfigure/overview.md)
* [Reconfigure MariaDB Standalone Database](en/reconfigure/standalone.md)

### Reconfigure-Tls

* [Reconfigure MariaDB TLS/SSL (Transport Encryption)](en/reconfigure-tls/cluster.md)
* [Reconfiguring TLS of MariaDB Database](en/reconfigure-tls/overview.md)

### Restart

* [Restart MariaDB](en/restart/restart.md)

### Rotate-Auth

* [Rotate Authentication of MariaDB](en/rotate-auth/overview.md)
* [Rotate Authentication of MariaDB](en/rotate-auth/rotateauth.md)

### Scaling ➔ Horizontal-Scaling

* [Horizontal Scale MariaDB](en/scaling/horizontal-scaling/cluster.md)
* [Horizontal Scale MaxScale](en/scaling/horizontal-scaling/maxscale.md)
* [MariaDB Horizontal Scaling](en/scaling/horizontal-scaling/overview.md)

### Scaling ➔ Vertical-Scaling

* [Vertical Scale MariaDB Cluster](en/scaling/vertical-scaling/cluster.md)
* [Vertical Scale MaxScale Server](en/scaling/vertical-scaling/maxscale.md)
* [MariaDB Vertical Scaling](en/scaling/vertical-scaling/overview.md)

### Tls

* [Configure TLS/SSL in MariaDB](en/tls/configure.md)
* [MariaDB TLS/SSL Encryption](en/tls/overview.md)

### Update-Version

* [Update Version of MariaDB Cluster](en/update-version/cluster.md)
* [Updating MariaDB Version Overview](en/update-version/overview.md)

### Volume-Expansion

* [MaxScale Volume Expansion](en/volume-expansion/maxscale.md)
* [MariaDB Volume Expansion](en/volume-expansion/overview.md)
* [MariaDB Volume Expansion](en/volume-expansion/volume-expansion.md)


<!-- PAGE_START: clustering/galera-cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB - MariaDB Cluster

This tutorial will show you how to use KubeDB to provision a MariaDB Galera Cluster in multi-primary mode.

## Before You Begin

Before proceeding:

* Read [mariadb galera cluster concept](en/clustering/overview.md) to learn about MariaDB Galera Cluster.
* You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial. Run the following command to prepare your cluster for this tutorial:

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Note: The yaml files used in this tutorial are stored in [docs/guides/mariadb/clustering/galera-cluster/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/clustering/galera-cluster/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Deploy MariaDB Cluster

The following is an example `MariaDB` object which creates a multi-master MariaDB group with three members.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: GaleraCluster
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

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/galera-cluster/examples/demo-1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Here,

* `spec.replicas` is the number of nodes in the cluster.
* `spec.storage` specifies the StorageClass of PVC dynamically allocated to store data for this database. This storage spec will be passed to the PetSet created by KubeDB operator to run database pods. So, each members will have a pod of this storage configuration. You can specify any StorageClass available in your cluster with appropriate resource requests.

KubeDB operator watches for `MariaDB` objects using Kubernetes API. When a `MariaDB` object is created, KubeDB operator will create a new PetSet and a Service with the matching MariaDB object name. KubeDB operator will also create a governing service for the PetSet with the name `<mariadb-object-name>-pods`.

```bash
$ kubectl get mariadb -n demo sample-mariadb -o yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"replicas":3,"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}},"storageClassName":"standard"},"storageType":"Durable","deletionPolicy":"WipeOut","version":"11.8.5"}}
  creationTimestamp: "2021-03-16T09:39:01Z"
  finalizers:
  - kubedb.com
  generation: 2
  managedFields:
    ...
  name: sample-mariadb
  namespace: demo
spec:
  authSecret:
    name: sample-mariadb-auth
  podTemplate:
    ...
  replicas: 3
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
    storageClassName: standard
  storageType: Durable
  deletionPolicy: WipeOut
  version: 12.1.2
status:
  conditions:
  - lastTransitionTime: "2021-03-16T09:39:01Z"
    message: 'The KubeDB operator has started the provisioning of MariaDB: demo/sample-mariadb'
    reason: DatabaseProvisioningStartedSuccessfully
    status: "True"
    type: ProvisioningStarted
  - lastTransitionTime: "2021-03-16T09:40:00Z"
    message: All desired replicas are ready.
    reason: AllReplicasReady
    status: "True"
    type: ReplicaReady
  - lastTransitionTime: "2021-03-16T09:39:09Z"
    message: 'The MariaDB: demo/sample-mariadb is accepting client requests.'
    observedGeneration: 2
    reason: DatabaseAcceptingConnectionRequest
    status: "True"
    type: AcceptingConnection
  - lastTransitionTime: "2021-03-16T09:39:50Z"
    message: 'The MariaDB: demo/sample-mariadb is ready.'
    observedGeneration: 2
    reason: ReadinessCheckSucceeded
    status: "True"
    type: Ready
  - lastTransitionTime: "2021-03-16T09:40:00Z"
    message: 'The MariaDB: demo/sample-mariadb is successfully provisioned.'
    observedGeneration: 2
    reason: DatabaseSuccessfullyProvisioned
    status: "True"
    type: Provisioned
  observedGeneration: 2
  phase: Ready


$ kubectl get petset,svc,secret,pvc,pv,pod -n demo
NAME                              READY   AGE
petset.apps/sample-mariadb   3/3     116m

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/sample-mariadb        ClusterIP   10.97.162.171   <none>        3306/TCP   116m
service/sample-mariadb-pods   ClusterIP   None            <none>        3306/TCP   116m

NAME                                TYPE                                  DATA   AGE
secret/default-token-696cj          kubernetes.io/service-account-token   3      121m
secret/sample-mariadb-auth          kubernetes.io/basic-auth              2      116m
secret/sample-mariadb-token-dk4dx   kubernetes.io/service-account-token   3      116m

NAME                                          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-sample-mariadb-0   Bound    pvc-1e259abc-5937-421a-990c-b903a83d2d8a   1Gi        RWO            standard       116m
persistentvolumeclaim/data-sample-mariadb-1   Bound    pvc-1d0b5bcd-2699-4b87-b57b-3072ddc1027f   1Gi        RWO            standard       116m
persistentvolumeclaim/data-sample-mariadb-2   Bound    pvc-5b85a06e-17f5-487a-9150-e928f5cf4590   1Gi        RWO            standard       116m

NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
persistentvolume/pvc-1d0b5bcd-2699-4b87-b57b-3072ddc1027f   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   standard                116m
persistentvolume/pvc-1e259abc-5937-421a-990c-b903a83d2d8a   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   standard                116m
persistentvolume/pvc-5b85a06e-17f5-487a-9150-e928f5cf4590   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   standard                116m

NAME                   READY   STATUS    RESTARTS   AGE
pod/sample-mariadb-0   1/1     Running   0          116m
pod/sample-mariadb-1   1/1     Running   0          116m
pod/sample-mariadb-2   1/1     Running   0          116m
```

## Connect with MariaDB database

Once the database is in running state we can conncet to each of three nodes. We will use login credentials `MYSQL_ROOT_USERNAME` and `MYSQL_ROOT_PASSWORD` saved as container’s environment variable.

```bash
# First Node
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1; 
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Second Node
$ kubectl exec -it -n demo sample-mariadb-1 -- bash
```

```mysql
root@sample-mariadb-1:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 94
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Third Node
$ kubectl exec -it -n demo sample-mariadb-2 -- bash
```

```mysql
root@sample-mariadb-2:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 78
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

## Check the Cluster Status

Now, we are ready to check newly created cluster status. Connect and run the following commands from any of the hosts and you will get the same result, that is the cluster size is three.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 137
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
1 row in set (0.001 sec)
```

## Data Availability

In a MariaDB Galera Cluster, Each member can read and write. In this section, we will insert data from any nodes, and we will see whether we can get the data from every other members.

> Read the comment written for the following commands. They contain the instructions and explanations of the commands.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 202
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE playground;
Query OK, 1 row affected (0.013 sec)

# Create table in Node 1
MariaDB [(none)]> CREATE TABLE playground.equipment ( id INT NOT NULL AUTO_INCREMENT, type VARCHAR(50), quant INT, color VARCHAR(25), PRIMARY KEY(id));
Query OK, 0 rows affected (0.053 sec)

# Insert sample data into Node 1
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 2, 'blue');
Query OK, 1 row affected (0.003 sec)

# Read data from Node 1
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
root@sample-mariadb-0:/ exit
exit
~ $ kubectl exec -it -n demo sample-mariadb-1 -- bash
```

```mysql
root@sample-mariadb-1:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Read data from Node 2
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

#Insert data into node 2
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 4, 'red');
Query OK, 1 row affected (0.032 sec)

# Read data from Node 2 after insertion
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
+----+-------+-------+-------+
2 rows in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
root@sample-mariadb-1:/ exit
exit
~ $ kubectl exec -it -n demo sample-mariadb-2 -- bash
```

```mysql
root@sample-mariadb-2:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Insert data into Node 3
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 4, 'red');
Query OK, 1 row affected (0.005 sec)

# Read data from Node 3
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
|  6 | slide |     4 | red   |
+----+-------+-------+-------+
3 rows in set (0.000 sec)

MariaDB [(none)]> quit
Bye
```

```bash
root@sample-mariadb-2:/# exit
exit
```

## Automatic Failover

To test automatic failover, we will force the one of three pods to restart and check if it can rejoin the cluster.

> Read the comment written for the following commands. They contain the instructions and explanations of the commands.

```bash
kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check current data
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
|  6 | slide |     4 | red   |
+----+-------+-------+-------+
3 rows in set (0.002 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
root@sample-mariadb-0:/ exit
exit

# Forcefully delete Node 1
~ $ kubectl delete pod -n demo sample-mariadb-0
pod "sample-mariadb-0" deleted

# Wait for sample-mariadb-0 to restart
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check data after rejoining
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  5 | slide |     4 | red   |
|  6 | slide |     4 | red   |
+----+-------+-------+-------+
3 rows in set (0.002 sec)

# Check cluster size
MariaDB [(none)]> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
1 row in set (0.002 sec)

MariaDB [(none)]> quit
Bye
```

## Cleaning up

Clean what we created in this tutorial.

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: clustering/mariadb-replication.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB - MariaDB Cluster

This tutorial will show you how to use KubeDB to provision a MariaDB Standard Replication in single-master mode.

## Before You Begin

Before proceeding:

* Read [this](en/clustering/overview.md#mariadb-standard-replication) to learn about MariaDB Standard Replication.
* You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial. Run the following command to prepare your cluster for this tutorial:

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Note: The yaml files used in this tutorial are stored in [docs/guides/mariadb/clustering/mariadb-replication/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/clustering/mariadb-replication/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Deploy MariaDB Cluster

The following is an example `MariaDB` object which creates a single-master MariaDB standard replication cluster with three members.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/mariadb-replication/examples/demo-1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Here,

* `spec.replicas` Defines the number of MariaDB pods (instances) in the cluster.
* `spec.storage` Specifies the StorageClass of PVC dynamically allocated to store data for this database. This storage spec will be passed to the PetSet created by KubeDB operator to run database pods. So, each members will have a pod of this storage configuration. You can specify any StorageClass available in your cluster with appropriate resource requests.
* `spec.topology` Configures the database topology and associated components.
* `spec.topology.maxscale` Specifies the Maxscale proxy server configuration.
* `spec.topology.maxscale.replicas` Defines the number of MaxScale replicas in the petset managed by the KubeDB Operator.
* `spec.topology.maxscale.enableUI` A boolean parameter (e.g. true or false) that controls whether the MaxScale GUI (accessible via the REST API) is enabled for the MaxScale instance.

KubeDB operator watches for `MariaDB` objects using Kubernetes API. When a `MariaDB` object is created, KubeDB operator will create a new PetSet and a Service with the matching MariaDB object name. KubeDB operator will also create a governing service for the PetSet with the name `<mariadb-object-name>-pods`.

```bash
$ kubectl get mariadb -n demo sample-mariadb -o yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  allowedSchemas:
    namespaces:
      from: Same
  authSecret:
    activeFrom: "2025-04-08T06:42:36Z"
    name: sample-mariadb-auth
  deletionPolicy: WipeOut
  healthChecker:
    failureThreshold: 1
    periodSeconds: 10
    timeoutSeconds: 10
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          limits:
            memory: 1Gi
          requests:
            cpu: 500m
            memory: 1Gi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          runAsGroup: 999
          runAsNonRoot: true
          runAsUser: 999
          seccompProfile:
            type: RuntimeDefault
      - name: md-coordinator
        resources:
          limits:
            memory: 256Mi
          requests:
            cpu: 200m
            memory: 256Mi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          runAsGroup: 999
          runAsNonRoot: true
          runAsUser: 999
          seccompProfile:
            type: RuntimeDefault
      initContainers:
      - name: mariadb-init
        resources:
          limits:
            memory: 512Mi
          requests:
            cpu: 200m
            memory: 256Mi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          runAsGroup: 999
          runAsNonRoot: true
          runAsUser: 999
          seccompProfile:
            type: RuntimeDefault
      podPlacementPolicy:
        name: default
      securityContext:
        fsGroup: 999
      serviceAccountName: sample-mariadb
  replicas: 3
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  storageType: Durable
  topology:
    maxscale:
      enableUI: true
      podTemplate:
        spec:
          containers:
          - name: maxscale
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                drop:
                - ALL
              runAsNonRoot: true
              runAsUser: 997
              seccompProfile:
                type: RuntimeDefault
          initContainers:
          - name: maxscale-init
            resources:
              limits:
                memory: 512Mi
              requests:
                cpu: 200m
                memory: 256Mi
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                drop:
                - ALL
              runAsNonRoot: true
              runAsUser: 997
              seccompProfile:
                type: RuntimeDefault
          podPlacementPolicy:
            name: default
          securityContext:
            fsGroup: 997
          serviceAccountName: sample-mariadb
      replicas: 3
      storage:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
      storageType: Durable
    mode: MariaDBReplication
  version: 12.1.2
status:
  conditions:
  ...
  observedGeneration: 2
  phase: Ready



$ kubectl get petset,svc,secret,pvc,pv,pod -n demo
NAME                                             AGE
petset.apps.k8s.appscode.com/sample-mariadb      53s
petset.apps.k8s.appscode.com/sample-mariadb-mx   56s


NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/sample-mariadb           ClusterIP   10.43.110.13    <none>        3306/TCP            60s
service/sample-mariadb-mx        ClusterIP   10.43.149.170   <none>        3306/TCP,8989/TCP   60s
service/sample-mariadb-mx-pods   ClusterIP   None            <none>        3306/TCP            60s
service/sample-mariadb-pods      ClusterIP   None            <none>        3306/TCP            60s
service/sample-mariadb-standby   ClusterIP   10.43.84.224    <none>        3306/TCP            60s

NAME                                TYPE                                  DATA   AGE
secret/default-token-696cj          kubernetes.io/service-account-token   3      121m
secret/sample-mariadb-auth          kubernetes.io/basic-auth              2      116m
secret/sample-mariadb-token-dk4dx   kubernetes.io/service-account-token   3      116m

NAME                                             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-sample-mariadb-0      Bound    pvc-ce1faccf-8e33-49c6-8520-7b8bb24bb01a   1Gi        RWO            local-path     <unset>                 3m6s
persistentvolumeclaim/data-sample-mariadb-1      Bound    pvc-2fd2d566-0a32-45d8-af0d-88a1f755ccbc   1Gi        RWO            local-path     <unset>                 3m6s
persistentvolumeclaim/data-sample-mariadb-2      Bound    pvc-77a2cc33-4f8b-4de7-a591-acd97ceb3dce   1Gi        RWO            local-path     <unset>                 3m6s
persistentvolumeclaim/data-sample-mariadb-mx-0   Bound    pvc-c6b54166-9c42-4211-9439-ab63fd1aae89   50Mi       RWO            local-path     <unset>                 3m9s
persistentvolumeclaim/data-sample-mariadb-mx-1   Bound    pvc-eaec319b-33d1-4fac-8234-7eadfbad0e61   50Mi       RWO            local-path     <unset>                 3m9s
persistentvolumeclaim/data-sample-mariadb-mx-2   Bound    pvc-733c4cde-3756-44ab-b652-17425e0e210f   50Mi       RWO            local-path     <unset>                 3m9s

NAME                                                        CAPACITY    ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                           STORAGECLASS   REASON   AGE
persistentvolume/pvc-1d0b5bcd-2699-4b87-b57b-3072ddc1027f   1Gi         RWO            Delete           Bound    demo/data-sample-mariadb-1      local-path              116m
persistentvolume/pvc-1e259abc-5937-421a-990c-b903a83d2d8a   1Gi         RWO            Delete           Bound    demo/data-sample-mariadb-0      local-path              116m
persistentvolume/pvc-5b85a06e-17f5-487a-9150-e928f5cf4590   1Gi         RWO            Delete           Bound    demo/data-sample-mariadb-2      local-path              116m
persistentvolume/pvc-c6b54166-9c42-4211-9439-ab63fd1aae89   50Mi        RWO            Delete           Bound    demo/data-sample-mariadb-mx-0   local-path              116m
persistentvolume/pvc-c6b54166-9c42-4211-9439-ab63fd1aae89   50Mi        RWO            Delete           Bound    demo/data-sample-mariadb-mx-1   local-path              116m
persistentvolume/pvc-eaec319b-33d1-4fac-8234-7eadfbad0e61   50Mi        RWO            Delete           Bound    demo/data-sample-mariadb-mx-2   local-path              116m

NAME                   READY   STATUS    RESTARTS   AGE
pod/sample-mariadb-0      2/2     Running   0          3m6s
pod/sample-mariadb-1      2/2     Running   0          3m6s
pod/sample-mariadb-2      2/2     Running   0          3m6s
pod/sample-mariadb-mx-0   1/1     Running   0          3m9s
pod/sample-mariadb-mx-1   1/1     Running   0          3m9s
pod/sample-mariadb-mx-2   1/1     Running   0          3m9s
```

## Check the Cluster Status

Now, we are ready to check newly created cluster status. Connect to maxscale pod and run the following commands from any of the maxscale pod and you will get the same result.

```bash
$ kubectl exec -it -n demo svc/sample-mariadb-mx -- bash
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬─────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID    │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-125 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-125 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-125 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴─────────┴────────────────────┘
```

## Connecting to MariaDB Database

Once the database is in running state we can conncet to each of three nodes. We will use login credentials `MYSQL_ROOT_USERNAME` and `MYSQL_ROOT_PASSWORD` saved as container’s environment variable.

## Create a Test User

Writing to a slave replica may result in a binary log (binlog) conflict issue. Initially the slave replica are in read only mode. But user with super privileges can still write the database of read only mode. The root user possesses superuser privileges, enabling them to modify a database even in read-only mode.

We recommend using a non-root user for production environments. The root user has extensive privileges, which can pose security risks. Therefore, it is advisable to create a dedicated user with appropriate permissions for production use.

```bash
$ kubectl exec -it -n demo svc/sample-mariadb -- bash
mysql@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# create user
MariaDB [(none)]> CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpassword';
Query OK, 0 rows affected (0.001 sec)

# Grant all privileges to the user on all databases
MariaDB [(none)]> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, SHOW DATABASES ON *.* TO 'testuser'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> quit;
Bye
mysql@sample-mariadb-0:/ exit
exit
```

## Check Connectivity using Test User

```bash
# Master Node
$ kubectl exec -it -n demo svc/sample-mariadb -- bash
```

```mysql
mysql@sample-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1; 
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Slave Node
$ kubectl exec -it -n demo svc/sample-mariadb-standby -- bash
```

```mysql
mysql@sample-mariadb-1:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 94
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye

MariaDB [(none)]> quit;
Bye
```

## Insert Data and Check Availability

In a MariaDB Replication Cluster, Only master member can write, and slave member can read. In this section, we will insert data from master node, and we will see whether we can get the data from every other slave members.
`sample-mariadb-0` is the master node in our case.

> Read the comment written for the following commands. They contain the instructions and explanations of the commands.

```bash
# master node
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
mysql@sample-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 202
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE playground;
Query OK, 1 row affected (0.013 sec)

# Create table in Node 1
MariaDB [(none)]> CREATE TABLE playground.equipment ( id INT NOT NULL AUTO_INCREMENT, type VARCHAR(50), quant INT, color VARCHAR(25), PRIMARY KEY(id));
Query OK, 0 rows affected (0.053 sec)

# Insert sample data into Node 1
MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 2, 'blue');
Query OK, 1 row affected (0.003 sec)

# Read data from Node 1
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
mysql@sample-mariadb-0:/ exit
exit

# check slave node data

$ kubectl exec -it -n demo sample-mariadb-1 -- bash
```

```mysql
mysql@sample-mariadb-1:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Read data from Node 2
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)
MariaDB [(none)]> quit;
Bye
```

```bash
mysql@sample-mariadb-1:/ exit
exit
~ $ kubectl exec -it -n demo sample-mariadb-2 -- bash
```

```mysql
mysql@sample-mariadb-2:/  mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 209
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Read data from Node 3
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
3 rows in set (0.000 sec)

MariaDB [(none)]> quit
Bye
```

```bash
mysql@sample-mariadb-2:/# exit
exit
```

## Automatic Failover

To test automatic failover, we will force the master pods to restart and check if it can switch the master and rejoin the cluster.

> Read the comment written for the following commands. They contain the instructions and explanations of the commands.

```bash
# Forcefully delete master node
~ $ kubectl delete pod -n demo sample-mariadb-0
pod "sample-mariadb-0" deleted

Now exec into maxscale server and run the following command to check the server status and ensure the failover is working.

$ kubectl exec -it -n demo svc/sample-mariadb-mx -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬───────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID      │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Down            │ 0-1-14545 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-14545 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-14545 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴───────────┴────────────────────┘
```

```bash
# sample-mariadb-1 is new master.
# Wait some time to up sample-mariadb-0 and check the server list again

bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬───────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID      │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-2-14551 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-2-14551 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-2-14551 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴───────────┴────────────────────┘
```

```bash
All replicas up and srunning now.

# Now check `sample-mariadb-0` data
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
mysql@sample-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check data after rejoining
MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
3 rows in set (0.002 sec)

MariaDB [(none)]> quit
Bye
```

## Checking Proxy and Read-Write Split using Maxscale

To test the traffic routing through the MaxScale server let’s first create a pod with ubuntu base image in it. We will use the following yaml.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: ubuntu
  name: ubuntu
  namespace: demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ubuntu
  strategy: {}
  template:
    metadata:
      labels:
        app: ubuntu
    spec:
      containers:
        - image: ubuntu
          imagePullPolicy: IfNotPresent
          name: ubuntu
          command: ["/bin/sleep", "3650d"]
          resources: {}
```

Let’s apply the yaml.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/mariadb-replication/examples/ubuntu.yaml
```

```yaml
deployment.apps/ubuntu created
```

Let’s exec into the pod and install mariadb-client.

```bash
$ kubectl exec -it -n demo pod/ubuntu-bb47d8d6c-4vhjv -- bash                12:00
mysql@ubuntu-bb47d8d6c-4vhjv:/# apt update
... ... ..
mysql@ubuntu-bb47d8d6c-4vhjv:/# apt install mariadb-client -y
Reading package lists... Done
... .. ...
mysql@ubuntu-bb47d8d6c-4vhjv:/#
```

Now let’s try to connect with the Maxscale Proxy server through the `sample-mariadb-mx` service as the `testuser` user.

```bash
mysql@ubuntu-bb47d8d6c-4vhjv:/# mariadb -utestuser -ptestpassword -hsample-mariadb-mx.demo -P3306
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

We have successfully connected as the `testuser` user. Let’s execute some read and write queries using this connection.

```mysql
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| sys                |
+--------------------+
6 rows in set (0.001 sec)

MariaDB [(none)]> use playground;
Database changed

MariaDB [playground]> show tables;
+----------------------+
| Tables_in_playground |
+----------------------+
| equipment            |
+----------------------+
1 row in set (0.001 sec)

mysql> INSERT INTO equipment (type, quant, color) VALUES ('pot', 2, 'black');
Query OK, 1 row affected (0.01 sec)


MariaDB [playground]> select * from equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
|  2 | pot   |     2 | black |
+----+-------+-------+-------+
2 rows in set (0.001 sec)


# Currently our server state is -
➤ kubectl exec -it -n demo pod/sample-mariadb-mx-0 -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
```

```bash
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬───────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID      │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server1 │ sample-mariadb-0.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 1           │ Slave, Running  │ 0-2-52054 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server2 │ sample-mariadb-1.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 1           │ Master, Running │ 0-2-52054 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼───────────┼────────────────────┤
│ server3 │ sample-mariadb-2.sample-mariadb-pods.demo.svc.cluster.local │ 3306 │ 1           │ Slave, Running  │ 0-2-52054 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴───────────┴────────────────────┘
```

```bash
# Now lets check read-write split
```

```mysql
MariaDB [playground]> SELECT NOW(),@@hostname;
+---------------------+------------------+
| NOW()               | @@hostname       |
+---------------------+------------------+
| 2025-04-24 13:11:06 | sample-mariadb-2 |
+---------------------+------------------+
1 row in set (0.000 sec)

MariaDB [playground]> SELECT NOW(),@@hostname;
+---------------------+------------------+
| NOW()               | @@hostname       |
+---------------------+------------------+
| 2025-04-24 13:11:31 | sample-mariadb-2 |
+---------------------+------------------+
1 row in set (0.000 sec)

MariaDB [playground]> SELECT NOW(),@@hostname;
+---------------------+------------------+
| NOW()               | @@hostname       |
+---------------------+------------------+
| 2025-04-24 13:12:00 | sample-mariadb-0 |
+---------------------+------------------+
1 row in set (0.000 sec)

# Read queries are executed on the slave replica
# FYI: Both read and write operations can be executed on the master node.

# Now, let's check the write split.

MariaDB [playground]> CREATE DATABASE IF NOT EXISTS test_db;
Query OK, 1 row affected (0.001 sec)

MariaDB [playground]> CREATE TABLE test_db.t1 (id INT, hostname VARCHAR(100));
Query OK, 0 rows affected (0.009 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (1, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (2, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (3, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> INSERT INTO test_db.t1 (id, hostname) VALUES (4, @@hostname);
Query OK, 1 row affected (0.002 sec)

MariaDB [playground]> SELECT * FROM test_db.t1;
+------+------------------+
| id   | hostname         |
+------+------------------+
|    1 | sample-mariadb-1 |
|    2 | sample-mariadb-1 |
|    3 | sample-mariadb-1 |
|    4 | sample-mariadb-1 |
+------+------------------+
4 rows in set (0.001 sec)

# Write queries are executed only on the master node.
```

We can see the queries are successfully executed through the Maxscale Proxy server and read write split is working as expected.

## Access and Explore the MaxScale UI

To enable the MaxScale UI, set `spec.topology.maxscale.enableUI: true` in the configuration. The MaxScale UI runs on port 8989. To access it, use the following kubectl command to forward the port:

```bash
➤ kubectl port-forward -n demo service/sample-mariadb-mx 8989:8989
Forwarding from 127.0.0.1:8989 -> 8989
Forwarding from [::1]:8989 -> 8989
```

The MaxScale UI is accessible at http://127.0.0.1:8989.

Use the default credentials to log in:

* Username: admin
* Password: mariadb

After logging in, you will be greeted by an intuitive dashboard showcasing servers list and current node state.

![Maxscale Dashboard](images/clustering_mariadb-replication_maxscale-homepage.png)

## Cleaning up

Let’s clean up what we created in this tutorial.

```bash
$ kubectl delete mariadb.kubedb.com -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete -n demo deployment.apps/ubuntu
deployment.apps "ubuntu" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: clustering/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Clustering

KubeDB supports two primary clustering modes for MariaDB: Multi-Master MariaDB Galera Cluster and Master-Slave MariaDB Standard Replication. Below, we explore key concepts of these clustering approaches, highlighting their mechanisms, benefits, and use cases in a distributed database environment.

Below, we explore key concepts of MariaDB clustering, focusing on the two clustering modes supported by KubeDB: Multi-Master MariaDB Galera Cluster and Master-Slave MariaDB Standard Replication

## What is Replication

Replication in MariaDB involves duplicating data from one MariaDB server (the source) to one or more other MariaDB servers (replicas), rather than storing it on a single server. This process enhances data availability, scalability, and fault tolerance. The replication mode determines the read and write capabilities of each server in the cluster. MariaDB supports two primary replication architectures: multi-master and master-slave.

* Multi-Master Replication: In a multi-master setup, every server in the cluster can handle both read and write operations. This architecture, exemplified by the MariaDB Galera Cluster, ensures high availability and scalability by allowing applications to distribute workloads across all nodes.
* Master-Slave Replication: In a master-slave architecture, the master server supports both read and write operations, while slave servers are limited to read operations. This setup is ideal for read-heavy workloads, with slaves providing scalability for queries and serving as backups.

The following figure shows a cluster of four MariaDB servers of multi-master replication:

![MariaDB Cluster](images/clustering_overview_galera_small.png)

Image ref: <https://mariadb.com/docs/galera-cluster>

## Galera Replication

MariaDB Galera Cluster is a [virtually synchronous](https://mariadb.com/kb/en/about-galera-replication/#synchronous-vs-asynchronous-replication) multi-master cluster for MariaDB. The Server replicates a transaction at commit time by broadcasting the write set associated with the transaction to every node in the cluster. The client connects directly to the DBMS and experiences behavior that is similar to native MariaDB in most cases. The wsrep API (write set replication API) defines the interface between Galera replication and MariaDB.

Ref: [About Galera Replication](https://mariadb.com/kb/en/about-galera-replication/)

## MariaDB Galera Cluster Features

* Virtually synchronous replication
* Active-active multi-master topology
* Read and write to any cluster node
* Automatic membership control, failed nodes drop from the cluster
* Automatic node joining
* True parallel replication, on row level
* Direct client connections, native MariaDB look & feel

Ref: [What is MariaDB Galera Cluster?](https://mariadb.com/kb/en/what-is-mariadb-galera-cluster/#features)

### Limitations

There are some limitations in MariaDB Galera Cluster that are listed [here](https://mariadb.com/kb/en/mariadb-galera-cluster-known-limitations/).

## MariaDB Standard Replication

```mermaid
flowchart LR
  App["Client Application"] --> Proxy["MaxScale Service (:3306)"]
  Proxy -->|Writes| Primary["ha-mariadb-0 (Primary / RW)"]
  Proxy -->|Reads| Replica1["ha-mariadb-1 (Replica / RO)"]
  Proxy -->|Reads| Replica2["ha-mariadb-2 (Replica / RO)"]
  Primary -->|Async Binlog + GTID| Replica1
  Primary -->|Async Binlog + GTID| Replica2
  Monitor["ReplicationMonitor"] -.->|Detects Failure and Promotes| Replica1
```


MariaDB Standard Replication is a widely used mechanism for copying data from one MariaDB server (master) to one or more other MariaDB servers (slave). This replication mode ensures data redundancy, enhances availability, and supports read scalability by distributing read operations across multiple servers. It operates in a single-master and slave architecture, where the master server handles both read and write operations, while slave servers are limited to read operations.

Ref: [About MariadDB Standard Replication](https://mariadb.com/kb/en/replication-overview/#standard-replication)

![MariaDB Standard Replication Cluster](images/clustering_overview_mariadb-standard-replication.png)

## MariaDB Standard Replication Cluster Features

* Asynchronous Replication
* Active-passive single-master topology
* Read and write to master, and read only to slave node
* Automatic node joining
* Automatic failover using Maxscale Proxy Server
* Binary Log-Based replication
* Direct client connections, native MariaDB look & feel
* Load Balance using Maxscale Proxy Server
* Read Write Split using Maxscale Proxy Server

### MariaDB Maxscale Proxy Server

MariaDB MaxScale is a tool that acts as a middleman between your applications and MariaDB Server databases. It helps improve the database’s availability, ability to handle more users, and security. It also makes it easier for developers by separating the application from the database setup.

MaxScale has a flexible design that supports add-ons (plugins) to do more than just basic load balancing. For example, it can act as a database firewall to protect your data. It comes with built-in plugins for routing queries, filtering data, and supporting different protocols. You can set up MaxScale to direct database requests or modify responses based on your needs, such as hiding sensitive information or spreading read requests across multiple servers to handle more traffic.

One of its key features is auto failover, which ensures your database remains available even if a primary server fails. Auto failover automatically detects a failed primary node, promotes a replica to take its place, and redirects traffic to the new primary, minimizing downtime and keeping your applications running smoothly.

### How Auto Failover Works with MaxScale

MaxScale uses a monitor (like the MariaDB-Monitor plugin) to track the health of database nodes in a replication setup (e.g. MariaDB master-replica). If the primary node becomes unavailable—due to a crash, network issue, or maintenance—

MaxScale:

* Detects the Failure: The monitor(ReplicationMonitor) continuously checks node status (using MySQL pings or status variables).
* Selects a New Primary: It identifies the most suitable replica based on criteria like replication lag or server state.
* Promotes the Replica: MaxScale executes commands to promote the chosen replica to primary (e.g. STOP SLAVE; RESET SLAVE ALL;).
* Reconfigures Replicas: Other replicas are updated to replicate from the new primary.
* Redirects Traffic: MaxScale’s router (RW-Split-Router) seamlessly directs write queries to the new primary and read queries to replicas.

This process happens automatically, typically within seconds, ensuring minimal disruption.

# Next Steps

* [Deploy MariaDB Galera Cluster](en/clustering/galera-cluster.md) using KubeDB.

<!-- PAGE_START: concepts/appbinding.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# AppBinding

## What is AppBinding

An `AppBinding` is a Kubernetes `CustomResourceDefinition`(CRD) which points to an application using either its URL (usually for a non-Kubernetes resident service instance) or a Kubernetes service object (if self-hosted in a Kubernetes cluster), some optional parameters and a credential secret. To learn more about AppBinding and the problems it solves, please read this blog post: [The case for AppBinding](https://appscode.com/blog/post/the-case-for-appbinding).

If you deploy a database using [KubeDB](https://kubedb.com/docs/latest/welcome/), `AppBinding` object will be created automatically for it. Otherwise, you have to create an `AppBinding` object manually pointing to your desired database.

KubeDB uses [Stash](https://appscode.com/products/stash/) to perform backup/recovery of databases. Stash needs to know how to connect with a target database and the credentials necessary to access it. This is done via an `AppBinding`.

## AppBinding CRD Specification

Like any official Kubernetes resource, an `AppBinding` has `TypeMeta`, `ObjectMeta` and `Spec` sections. However, unlike other Kubernetes resources, it does not have a `Status` section.

An `AppBinding` object created by `KubeDB` for MariaDB database is shown below,

```yaml
apiVersion: appcatalog.appscode.com/v1alpha1
kind: AppBinding
metadata:
  labels:
    app.kubernetes.io/component: database
    app.kubernetes.io/instance: sample-mariadb
    app.kubernetes.io/managed-by: kubedb.com
    app.kubernetes.io/name: mariadbs.kubedb.com
  name: sample-mariadb
  namespace: demo
spec:
  clientConfig:
    caBundle: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURJekNDQWd1Z0F3SUJBZ0lVVUg1V24wOSt6MnR6RU5ESnF4N1AxZFg5aWM4d0RRWUpLb1pJaHZjTkFRRUwKQlFBd0lURU9NQXdHQTFVRUF3d0ZiWGx6Y1d3eER6QU5CZ05WQkFvTUJtdDFZbVZrWWpBZUZ3MHlNVEF5TURrdwpPVEkxTWpCYUZ3MHlNakF5TURrd09USTFNakJhTUNFeERqQU1CZ05WQkFNTUJXMTVjM0ZzTVE4d0RRWURWUVFLCkRBWnJkV0psWkdJd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUUM3ZDl5YUtMQ3UKYy9NclRBb0NkV1VORld3ckdqbVdvUEVTRWNMR0pjT0JVSTZ5NXZ5QXVGMG1TakZvNzR3SEdSbWRmS2ExMWh0Ygo4TWZ2UFNwWXVGWFpUSi9GbnkwNnU2ekZMVm5xV2h3MUdiZ2ZCUE5XK0w1ZGkzZmVjanBEZmtLbTcrd0ZUVnNmClVzWGVVcUR0VHFpdlJHVUQ5aURUTzNTUmdheVI5U0J0RnRxcHRtV0YrODFqZGlSS2pRTVlCVGJ2MDRueW9UdHUKK0hJZlFjbE40Q1p3NzJPckpUdFdiYnNiWHVlMU5RZU9nQzJmSVhkZEF0WEkxd3lOT04zckxuTFF1SUIrakVLSQpkZTlPandKSkJhSFVzRVZEbllnYlJLSTdIcVdFdk5kL29OU2VZRXF2TXk3K1hwTFV0cDBaVXlxUDV2cC9PSXJ3CmlVMWVxZGNZMzJDcEFnTUJBQUdqVXpCUk1CMEdBMVVkRGdRV0JCUlNnNDVpazFlT3lCU1VKWHkvQllZVDVLck8KeWpBZkJnTlZIU01FR0RBV2dCUlNnNDVpazFlT3lCU1VKWHkvQllZVDVLck95akFQQmdOVkhSTUJBZjhFQlRBRApBUUgvTUEwR0NTcUdTSWIzRFFFQkN3VUFBNElCQVFCNTlhNlFGQm1YMTh1b1dzQ3dGT1Y0R25GYnVBL2NoaVN6CkFwRVVhcjI1L2RNK2RpT0RVNkJuMXM3Wmpqem45WU9aVVJJL3UyRGRhdmNnQUNYR2FXWHJhSS84UUYxZDB3OGsKNXFlRmMxQWE5UEhFeEsxVm1xb21MV2xhMkdTOW1EbFpEOEtueDdjU3lpRmVqRXJYdWtld1B1VXA0dUUzTjAraApwQjQ0MDVRU2d4VVc3SmVhamFQdTNXOHgyRUFKMnViTkdMVEk5L0x4V1Z0YkxGcUFoSFphbGRjaXpOSHdTUGYzCkdMWEo3YTBWTW1JY0NuMWh5a0k2UkNrUTRLSE9tbDNOcXRRS2F5RnhUVHVpdzRiZ3k3czA1UnNzRlVUaWN1VmcKc3hnMjFVQUkvYW9WaXpQOVpESGE2TmV0YnpNczJmcmZBeHhBZk9pWDlzN1JuTmM0WHd4VAotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    service:
      name: sample-mariadb
      port: 3306
      scheme: mysql
  secret:
    name: sample-mariadb-auth
  type: kubedb.com/mariadb
  version: 12.1.2
```

Here, we are going to describe the sections of an `AppBinding` crd.

### AppBinding `Spec`

An `AppBinding` object has the following fields in the `spec` section:

#### spec.type

`spec.type` is an optional field that indicates the type of the app that this `AppBinding` is pointing to. Stash uses this field to resolve the values of `TARGET_APP_TYPE`, `TARGET_APP_GROUP` and `TARGET_APP_RESOURCE` variables of [BackupBlueprint](https://appscode.com/products/stash/latest/concepts/crds/backupblueprint/) object.

This field follows the following format: `<app group>/<resource kind>`. The above AppBinding is pointing to a `mariadb` resource under `kubedb.com` group.

Here, the variables are parsed as follows:

| Variable | Usage |
| --- | --- |
| `TARGET_APP_GROUP` | Represents the application group where the respective app belongs (i.e: `kubedb.com`). |
| `TARGET_APP_RESOURCE` | Represents the resource under that application group that this appbinding represents (i.e: `mariadb`). |
| `TARGET_APP_TYPE` | Represents the complete type of the application. It’s simply `TARGET_APP_GROUP/TARGET_APP_RESOURCE` (i.e: `kubedb.com/mariadb`). |

#### spec.secret

`spec.secret` specifies the name of the secret which contains the credentials that are required to access the database. This secret must be in the same namespace as the `AppBinding`.

This secret must contain the following keys:

PostgreSQL :

| Key | Usage |
| --- | --- |
| `POSTGRES_USER` | Username of the target database. |
| `POSTGRES_PASSWORD` | Password for the user specified by `POSTGRES_USER`. |

MySQL :

| Key | Usage |
| --- | --- |
| `username` | Username of the target database. |
| `password` | Password for the user specified by `username`. |

MariaDB :

| Key | Usage |
| --- | --- |
| `username` | Username of the target database. |
| `password` | Password for the user specified by `username`. |

MongoDB :

| Key | Usage |
| --- | --- |
| `username` | Username of the target database. |
| `password` | Password for the user specified by `username`. |

MariaDB:

| Key | Usage |
| --- | --- |
| `ADMIN_USERNAME` | Admin username |
| `ADMIN_PASSWORD` | Password for admin user |

#### spec.clientConfig

`spec.clientConfig` defines how to communicate with the target database. You can use either an URL or a Kubernetes service to connect with the database. You don’t have to specify both of them.

You can configure following fields in `spec.clientConfig` section:

* **spec.clientConfig.url**

  `spec.clientConfig.url` gives the location of the database, in standard URL form (i.e. `[scheme://]host:port/[path]`). This is particularly useful when the target database is running outside of the Kubernetes cluster. If your database is running inside the cluster, use `spec.clientConfig.service` section instead.
  Note that, attempting to use a user or basic auth (e.g. `user:password@host:port`) is not allowed. Stash will insert them automatically from the respective secret. Fragments ("#…") and query parameters ("?…") are not allowed either.
* **spec.clientConfig.service**

  If you are running the database inside the Kubernetes cluster, you can use Kubernetes service to connect with the database. You have to specify the following fields in `spec.clientConfig.service` section if you manually create an `AppBinding` object.

  + **name :** `name` indicates the name of the service that connects with the target database.
  + **scheme :** `scheme` specifies the scheme (i.e. http, https) to use to connect with the database.
  + **port :** `port` specifies the port where the target database is running.
* **spec.clientConfig.insecureSkipTLSVerify**

  `spec.clientConfig.insecureSkipTLSVerify` is used to disable TLS certificate verification while connecting with the database. We strongly discourage to disable TLS verification during backup. You should provide the respective CA bundle through `spec.clientConfig.caBundle` field instead.
* **spec.clientConfig.caBundle**

  `spec.clientConfig.caBundle` is a PEM encoded CA bundle which will be used to validate the serving certificate of the database.

<!-- PAGE_START: concepts/autoscaler.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBAutoscaler

## What is MariaDBAutoscaler

`MariaDBAutoscaler` is a Kubernetes `Custom Resource Definitions` (CRD). It provides a declarative configuration for autoscaling MariaDB compute resources and storage of database components in a Kubernetes native way.

## MariaDBAutoscaler CRD Specifications

Like any official Kubernetes resource, a `MariaDBAutoscaler` has `TypeMeta`, `ObjectMeta`, `Spec` and `Status` sections.

Here, some sample `MariaDBAutoscaler` CROs for autoscaling different components of database is given below:

**Sample `MariaDBAutoscaler` for MariaDB:**

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  compute:
    mariadb:
      trigger: "On"
      podLifeTimeThreshold: 5m
      minAllowed:
        cpu: 250m
        memory: 350Mi
      maxAllowed:
        cpu: 1
        memory: 1Gi
      controlledResources: ["cpu", "memory"]
  storage:
    mariadb:
      trigger: "On"
      usageThreshold: 60
      scalingThreshold: 50
      expansionMode: "Online"
```

Here, we are going to describe the various sections of a `MariaDBAutoscaler` crd.

A `MariaDBAutoscaler` object has the following fields in the `spec` section.

### spec.databaseRef

`spec.databaseRef` is a required field that point to the [MariaDB](en/concepts/mariadb.md) object for which the autoscaling will be performed. This field consists of the following sub-field:

* **spec.databaseRef.name :** specifies the name of the [MariaDB](en/concepts/mariadb.md) object.

### spec.compute

`spec.compute` specifies the autoscaling configuration for the compute resources i.e. cpu and memory of the database components. This field consists of the following sub-field:

* `spec.compute.mariadb` indicates the desired compute autoscaling configuration for a MariaDB standalone or cluster.

All of them has the following sub-fields:

* `trigger` indicates if compute autoscaling is enabled for this component of the database. If “On” then compute autoscaling is enabled. If “Off” then compute autoscaling is disabled.
* `minAllowed` specifies the minimal amount of resources that will be recommended, default is no minimum.
* `maxAllowed` specifies the maximum amount of resources that will be recommended, default is no maximum.
* `controlledResources` specifies which type of compute resources (cpu and memory) are allowed for autoscaling. Allowed values are “cpu” and “memory”.
* `containerControlledValues` specifies which resource values should be controlled. Allowed values are “RequestsAndLimits” and “RequestsOnly”.
* `resourceDiffPercentage` specifies the minimum resource difference between recommended value and the current value in percentage. If the difference percentage is greater than this value than autoscaling will be triggered.
* `podLifeTimeThreshold` specifies the minimum pod lifetime of at least one of the pods before triggering autoscaling.
* `InMemoryScalingThreshold` the percentage of the Memory that will be passed as inMemorySizeGB for inmemory database engine, which is only available for the percona variant of the mariadb.

### spec.storage

`spec.compute` specifies the autoscaling configuration for the storage resources of the database components. This field consists of the following sub-field:

* `spec.compute.mairadb` indicates the desired storage autoscaling configuration for a MariaDB standalone or cluster.

All of them has the following sub-fields:

* `trigger` indicates if storage autoscaling is enabled for this component of the database. If “On” then storage autoscaling is enabled. If “Off” then storage autoscaling is disabled.
* `usageThreshold` indicates usage percentage threshold, if the current storage usage exceeds then storage autoscaling will be triggered.
* `scalingThreshold` indicates the percentage of the current storage that will be scaled.
* `expansionMode` specifies the mode of volume expansion when storage autoscaler performs volume expansion OpsRequest. Default value is `Online`.

<!-- PAGE_START: concepts/mariadb-version.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBVersion

## What is MariaDBVersion

`MariaDBVersion` is a Kubernetes `Custom Resource Definitions` (CRD). It provides a declarative configuration to specify the docker images to be used for MariaDB database deployed with KubeDB in a Kubernetes native way.

When you install KubeDB, a `MariaDBVersion` custom resource will be created automatically for every supported MariaDB versions. You have to specify the name of `MariaDBVersion` crd in `spec.version` field of [MariaDB](en/concepts/mariadb.md) crd. Then, KubeDB will use the docker images specified in the `MariaDBVersion` crd to create your expected database.

Using a separate crd for specifying respective docker images, and pod security policy names allow us to modify the images, and policies independent of KubeDB operator. This will also allow the users to use a custom image for the database.

## MariaDBVersion Specification

As with all other Kubernetes objects, a MariaDBVersion needs `apiVersion`, `kind`, and `metadata` fields. It also needs a `.spec` section.

```yaml
apiVersion: catalog.kubedb.com/v1alpha1
kind: MariaDBVersion
metadata:
  annotations:
    meta.helm.sh/release-name: kubedb
    meta.helm.sh/release-namespace: kubedb
  creationTimestamp: "2024-12-19T05:12:32Z"
  generation: 1
  labels:
    app.kubernetes.io/instance: kubedb
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: kubedb-catalog
    app.kubernetes.io/version: v2024.11.18
    helm.sh/chart: kubedb-catalog-v2024.11.18
  name: 11.8.5
  resourceVersion: "1585"
  uid: d6b463f0-032a-4832-8b87-4648da0b38a6
spec:
  archiver:
    addon:
      name: mariadb-addon
      tasks:
        fullBackup:
          name: logical-backup
        fullBackupRestore:
          name: logical-backup-restore
        manifestBackup:
          name: manifest-backup
        manifestRestore:
          name: manifest-restore
        volumeSnapshot:
          name: volume-snapshot
    walg:
      image: ghcr.io/kubedb/mariadb-archiver:v0.9.0_10.5.23-focal
  coordinator:
    image: ghcr.io/kubedb/mariadb-coordinator:v0.29.0
  db:
    image: ghcr.io/appscode-images/mariadb:11.8.5-focal
  exporter:
    image: prom/mysqld-exporter:v0.13.0
  initContainer:
    image: ghcr.io/kubedb/mariadb-init:0.5.2
  maxscale:
    image: mariadb/maxscale:24.02.4
    securityContext:
      runAsUser: 995
  podSecurityPolicies:
    databasePolicyName: maria-db
  securityContext:
    runAsUser: 999
  stash:
    addon:
      backupTask:
        name: mariadb-backup-10.6.23
      restoreTask:
        name: mariadb-restore-10.6.23
  ui:
    - name: phpmyadmin
      version: v2024.4.27
  updateConstraints:
    allowlist:
      - '> 10.5.23, <= 11.5.2'
  version: 10.5.23
```

### metadata.name

`metadata.name` is a required field that specifies the name of the `MariaDBVersion` crd. You have to specify this name in `spec.version` field of [MariaDB](en/concepts/mariadb.md) crd.

We follow this convention for naming MariaDBVersion crd:

* Name format: `{Original MariaDB image version}-{modification tag}`

We modify original MariaDB docker image to support additional features. An image with higher modification tag will have more features than the images with lower modification tag. Hence, it is recommended to use MariaDBVersion crd with highest modification tag to take advantage of the latest features.

### spec.version

`spec.version` is a required field that specifies the original version of MariaDB database that has been used to build the docker image specified in `spec.db.image` field.

### spec.deprecated

`spec.deprecated` is an optional field that specifies whether the docker images specified here is supported by the current KubeDB operator.

The default value of this field is `false`. If `spec.deprecated` is set `true`, KubeDB operator will not create the database and other respective resources for this version.

### spec.db.image

`spec.db.image` is a required field that specifies the docker image which will be used to create Petset by KubeDB operator to create expected MariaDB database.

### spec.exporter.image

`spec.exporter.image` is a required field that specifies the image which will be used to export Prometheus metrics.

### spec.initContainer.image

`spec.initContainer.image` is a required field that specifies the image which will be used to remove `lost+found` directory and mount an `EmptyDir` data volume.

### spec.podSecurityPolicies.databasePolicyName

`spec.podSecurityPolicies.databasePolicyName` is a required field that specifies the name of the pod security policy required to get the database server pod(s) running.

### spec.stash

`spec.stash` is an optional field that specifies the name of the task for stash backup and restore. Learn more about [Stash MariaDB addon](https://stash.run/)

<!-- PAGE_START: concepts/mariadb.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB

## What is MariaDB

`MariaDB` is a Kubernetes `Custom Resource Definitions` (CRD). It provides declarative configuration for MariaDB in a Kubernetes native way. You only need to describe the desired database configuration in a MariaDB object, and the KubeDB operator will create Kubernetes objects in the desired state for you.

## MariaDB Spec

As with all other Kubernetes objects, a MariaDB needs `apiVersion`, `kind`, and `metadata` fields. It also needs a `.spec` section. Below is an example MariaDB object.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  authSecret:
    kind: Secret
    name: sample-mariadb-auth
  monitor:
    agent: prometheus.io
    prometheus:
      exporter:
        port: 56790
        resources: {}
      serviceMonitor:
        interval: 10s
        labels:
          release: prometheus
  podTemplate:
    controller: {}
    metadata: {}
    spec:
      containers:
      - name: mariadb
        resources:
          limits:
            cpu: 500m
            memory: 1Gi
          requests:
            cpu: 500m
            memory: 1Gi
      serviceAccountName: sample-mariadb
  replicas: 3
  requireSSL: true
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
    storageClassName: standard
  storageType: Durable
  deletionPolicy: WipeOut
  tls:
    certificates:
    - alias: server
      dnsNames:
      - localhost
      ipAddresses:
      - 127.0.0.1
      secretName: sample-mariadb-server-cert
      subject:
        organizations:
        - kubedb:server
    - alias: archiver
      secretName: sample-mariadb-archiver-cert
    - alias: metrics-exporter
      secretName: sample-mariadb-metrics-exporter-cert
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
  version: 12.1.2
```

### spec.version

`spec.version` is a required field specifying the name of the [MariaDBVersion](en/concepts/mariadb-version.md) crd where the docker images are specified. Currently, when you install KubeDB, it creates the following `MariaDBVersion` resources,

* `12.1.2`, `10.4.32`

### spec.authSecret

`spec.authSecret` is an optional field that points to a Secret used to hold credentials for `mariadb` root user. If not set, the KubeDB operator creates a new Secret `{mariadb-object-name}-auth` for storing the password for `mariadb` root user for each MariaDB object. If you want to use an existing secret please specify that when creating the MariaDB object using `spec.authSecret.name`.

This secret contains a `username` key and a `password` key which contains the `username` and `password` respectively for `mariadb` root user. Here, the value of `username` key is fixed to be `root`.

Secrets provided by users are not managed by KubeDB, and therefore, won’t be modified or garbage collected by the KubeDB operator (version 0.13.0 and higher).

Example:

```bash
kubectl create secret generic mariadb-auth -n demo \
    --from-literal=username=root \
    --from-literal=password=6q8u_2jMOW-OOZXk
secret/mariadb-auth created
```

```yaml
apiVersion: v1
data:
  password: NnE4dV8yak1PVy1PT1pYaw==
  username: cm9vdA==
kind: Secret
metadata:
  name: mariadb-auth
  namespace: demo
type: Opaque
```

### spec.storageType

`spec.storageType` is an optional field that specifies the type of storage to use for the database. It can be either `Durable` or `Ephemeral`. The default value of this field is `Durable`. If `Ephemeral` is used then KubeDB will create MariaDB database using [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volume. In this case, you don’t have to specify `spec.storage` field.

### spec.storage

If you set `spec.storageType:` to `Durable`, then `spec.storage` is a required field that specifies the StorageClass of PVCs dynamically allocated to store data for the database. This storage spec will be passed to the PetSet created by KubeDB operator to run database pods. You can specify any StorageClass available in your cluster with appropriate resource requests.

* `spec.storage.storageClassName` is the name of the StorageClass used to provision PVCs. PVCs don’t necessarily have to request a class. A PVC with its storageClassName set equal to "" is always interpreted to be requesting a PV with no class, so it can only be bound to PVs with no class (no annotation or one set equal to “”). A PVC with no storageClassName is not quite the same and is treated differently by the cluster depending on whether the DefaultStorageClass admission plugin is turned on.
* `spec.storage.accessModes` uses the same conventions as Kubernetes PVCs when requesting storage with specific access modes.
* `spec.storage.resources` can be used to request specific quantities of storage. This follows the same resource model used by PVCs.

To learn how to configure `spec.storage`, please visit the links below:

* <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims>

### spec.init

`spec.init` is an optional section that can be used to initialize a newly created MariaDB database. MariaDB databases can be initialized in one of two ways:

* Initialize from Script
* Initialize from Stash Restore

#### Initialize via Script

To initialize a MariaDB database using a script (shell script, sql script, etc.), set the `spec.init.script` section when creating a MariaDB object. It will execute files alphabetically with extensions `.sh` , `.sql` and `.sql.gz` that is found in the repository. The scripts inside child folders will be skipped. script must have the following information:

* [VolumeSource](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes): Where your script is loaded from.

Below is an example showing how a script from a configMap can be used to initialize a MariaDB database.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: 12.1.2
  init:
    script:
      configMap:
        name: md-init-script
```

In the above example, KubeDB operator will launch a Job to execute all js script of `md-init-script` in alphabetical order once PetSet pods are running.

### spec.monitor

MariaDB managed by KubeDB can be monitored with builtin-Prometheus and Prometheus operator out-of-the-box.

### spec.requireSSL

`spec.requireSSL` specifies whether the client connections require SSL. If `spec.requireSSL` is `true` then the server permits only TCP/IP connections that use SSL, or connections that use a socket file (on Unix) or shared memory (on Windows). The server rejects any non-secure connection attempt. For more details, please visit [here](https://mariadb.com/kb/en/securing-connections-for-client-and-server/#requiring-tls-for-specific-user-accounts)

### spec.tls

`spec.tls` specifies the TLS/SSL configurations for the MariaDB.

The following fields are configurable in the `spec.tls` section:

* `issuerRef` is a reference to the `Issuer` or `ClusterIssuer` CR of [cert-manager](https://cert-manager.io/docs/concepts/issuer/) that will be used by `KubeDB` to generate necessary certificates.

  + `apiGroup` is the group name of the resource being referenced. The value for `Issuer` or `ClusterIssuer` is “cert-manager.io” (cert-manager v0.12.0 and later).
  + `kind` is the type of resource being referenced. KubeDB supports both `Issuer` and `ClusterIssuer` as values for this field.
  + `name` is the name of the resource (`Issuer` or `ClusterIssuer`) being referenced.
* `certificates` (optional) are a list of certificates used to configure the server and/or client certificate. It has the following fields:

  + `alias` represents the identifier of the certificate. It has the following possible value:

    - `server` is used for server certificate identification.
    - `client` is used for client certificate identification.
    - `metrics-exporter` is used for metrics exporter certificate identification.
  + `secretName` (optional) specifies the k8s secret name that holds the certificates.
    This field is optional. If the user does not specify this field, the default secret name will be created in the following format: `<database-name>-<cert-alias>-cert`.
  + `subject` (optional) specifies an `X.509` distinguished name. It has the following possible field,

    - `organizations` (optional) are the list of different organization names to be used on the Certificate.
    - `organizationalUnits` (optional) are the list of different organization unit name to be used on the Certificate.
    - `countries` (optional) are the list of country names to be used on the Certificate.
    - `localities` (optional) are the list of locality names to be used on the Certificate.
    - `provinces` (optional) are the list of province names to be used on the Certificate.
    - `streetAddresses` (optional) are the list of a street address to be used on the Certificate.
    - `postalCodes` (optional) are the list of postal code to be used on the Certificate.
    - `serialNumber` (optional) is a serial number to be used on the Certificate.
      You can found more details from [Here](https://golang.org/pkg/crypto/x509/pkix/#Name)
  + `duration` (optional) is the period during which the certificate is valid.
  + `renewBefore` (optional) is a specifiable time before expiration duration.
  + `dnsNames` (optional) is a list of subject alt names to be used in the Certificate.
  + `ipAddresses` (optional) is a list of IP addresses to be used in the Certificate.
  + `uriSANs` (optional) is a list of URI Subject Alternative Names to be set in the Certificate.
  + `emailSANs` (optional) is a list of email Subject Alternative Names to be set in the Certificate.

### spec.configuration

`spec.configuration` is an optional field that specifies custom configuration for Mariadb cluster. It has the following fields:

* `configuration.inline` is an optional field that allows you to provide custom configuration directly in the Mariadb object.
  + Configuration snippet:

    ```yaml
    configuration:
         inline:
           md.cnf: |
             [mysqld]
             max_connections = 500
    ```
* `configuration.secretName` is an optional field that specifies the name of the secret that holds custom configuration files for Mariadb cluster.

### spec.podTemplate

KubeDB allows providing a template for database pod through `spec.podTemplate`. KubeDB operator will pass the information provided in `spec.podTemplate` to the PetSet created for the MariaDB database.

KubeDB accepts the following fields to set in `spec.podTemplate:`

* metadata:
  + annotations (pod’s annotation)
* controller:
  + annotations (petset’s annotation)
* spec:
  + containers
  + volumes
  + podPlacementPolicy
  + initContainers
  + imagePullSecrets
  + nodeSelector
  + serviceAccountName
  + schedulerName
  + tolerations
  + priorityClassName
  + priority
  + securityContext

Uses of some field of `spec.podTemplate` is described below,

You can check out the full list [here](https://github.com/kmodules/offshoot-api/blob/master/api/v2/types.go#L26C1-L279C1).
Uses of some field of `spec.podTemplate` is described below,

#### spec.podTemplate.spec.tolerations

The `spec.podTemplate.spec.tolerations` is an optional field. This can be used to specify the pod’s tolerations.

#### spec.podTemplate.spec.volumes

The `spec.podTemplate.spec.volumes` is an optional field. This can be used to provide the list of volumes that can be mounted by containers belonging to the pod.

#### spec.podTemplate.spec.podPlacementPolicy

`spec.podTemplate.spec.podPlacementPolicy` is an optional field. This can be used to provide the reference of the `podPlacementPolicy`. `name` of the podPlacementPolicy is referred under this attribute. This will be used by our Petset controller to place the db pods throughout the region, zone & nodes according to the policy. It utilizes kubernetes affinity & podTopologySpreadContraints feature to do so.

```yaml
spec:
  podPlacementPolicy:
    name: default
```

#### spec.podTemplate.spec.containers

The `spec.podTemplate.spec.containers` can be used to provide the list containers and their configurations for to the database pod. some of the fields are described below,

##### spec.podTemplate.spec.containers[].name

The `spec.podTemplate.spec.containers[].name` field used to specify the name of the container specified as a DNS\_LABEL. Each container in a pod must have a unique name (DNS\_LABEL). Cannot be updated.

##### spec.podTemplate.spec.containers[].args

`spec.podTemplate.spec.containers[].args` is an optional field. This can be used to provide additional arguments to database installation.

##### spec.podTemplate.spec.containers[].resources

`spec.podTemplate.spec.containers[].resources` is an optional field. This can be used to request compute resources required by containers of the database pods. To learn more, visit [here](http://kubernetes.io/docs/user-guide/compute-resources/).

##### spec.podTemplate.spec.containers[].env

`spec.podTemplate.spec.env` is an optional field that specifies the environment variables to pass to the MariaDB docker image. To know about supported environment variables, please visit [here](https://hub.docker.com/_/mariadb/).

Note that, KubeDB does not allow `MYSQL_ROOT_PASSWORD`, `MYSQL_ALLOW_EMPTY_PASSWORD`, `MYSQL_RANDOM_ROOT_PASSWORD`, and `MYSQL_ONETIME_PASSWORD` environment variables to set in `spec.env`. If you want to set the root password, please use `spec.authSecret` instead described earlier.

If you try to set any of the forbidden environment variables i.e. `MYSQL_ROOT_PASSWORD` in the MariaDB CRD, KubeDB operator will reject the request with the following error,

```bash
Error from server (Forbidden): error when creating "./mariadb.yaml": admission webhook "mariadb.validators.kubedb.com" denied the request: environment variable MYSQL_ROOT_PASSWORD is forbidden to use in MariaDB spec
```

Also, note that KubeDB does not allow to update the environment variables as updating them does not have any effect once the database is created. If you try to update environment variables, KubeDB operator will reject the request with the following error,

```bash
Error from server (BadRequest): error when applying patch:
...
for: "./mariadb.yaml": admission webhook "mariadb.validators.kubedb.com" denied the request: precondition failed for:
...At least one of the following was changed:
    apiVersion
    kind
    name
    namespace
    spec.authSecret
    spec.init
    spec.storageType
    spec.storage
    spec.podTemplate.spec.nodeSelector
    spec.podTemplate.spec.env
```

#### spec.podTemplate.spec.imagePullSecrets

`KubeDB` provides the flexibility of deploying MariaDB database from a private Docker registry. `spec.podTemplate.spec.imagePullSecrets` is an optional field that points to secrets to be used for pulling docker image if you are using a private docker registry.

#### spec.podTemplate.spec.nodeSelector

`spec.podTemplate.spec.nodeSelector` is an optional field that specifies a map of key-value pairs. For the pod to be eligible to run on a node, the node must have each of the indicated key-value pairs as labels (it can have additional labels as well). To learn more, see [here](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) .

#### spec.podTemplate.spec.serviceAccountName

`serviceAccountName` is an optional field supported by KubeDB Operator (version 0.13.0 and higher) that can be used to specify a custom service account to fine-tune role-based access control.

If this field is left empty, the KubeDB operator will create a service account name matching MariaDB crd name. Role and RoleBinding that provide necessary access permissions will also be generated automatically for this service account.

If a service account name is given, but there’s no existing service account by that name, the KubeDB operator will create one, and Role and RoleBinding that provide necessary access permissions will also be generated for this service account.

If a service account name is given, and there’s an existing service account by that name, the KubeDB operator will use that existing service account. Since this service account is not managed by KubeDB, users are responsible for providing necessary access permissions manually.

### spec.serviceTemplates

You can also provide a template for the services created by KubeDB operator for MariaDB database through `spec.serviceTemplates`. This will allow you to set the type and other properties of the services.

KubeDB allows following fields to set in `spec.serviceTemplates`:

* metadata:
  + annotations
* spec:
  + type
  + ports
  + clusterIP
  + externalIPs
  + loadBalancerIP
  + loadBalancerSourceRanges
  + externalTrafficPolicy
  + healthCheckNodePort
  + sessionAffinityConfig

```yaml
spec:
  version: "12.1.2"
  serviceTemplates:
    - alias: primary
      metadata:
        annotations:
          kubedb.com/test-annotation: "test"
      spec:
        type: LoadBalancer
        ports:
          - port: 3306
```

See [here](https://github.com/kmodules/offshoot-api/blob/kubernetes-1.16.3/api/v1/types.go#L163) to understand these fields in detail.

### spec.halted

`spec.halted` is an optional field. Suppose you want to delete the `MariaDB` resources(`PetSet`, `Service` etc.) except `MariaDB` object, `PVCs` and `Secret` then you need to set `spec.halted` to `true`. If you set `spec.halted` to `true` then the `deletionPolicy` in `MariaDB` object will be set `Halt` by-default.

### spec.deletionPolicy

`deletionPolicy` gives flexibility whether to `nullify`(reject) the delete operation of `MariaDB` crd or which resources KubeDB should keep or delete when you delete `MariaDB` crd. KubeDB provides the following four termination policies:

* DoNotTerminate
* Halt
* Delete (`Default`)
* WipeOut

When `deletionPolicy` is `DoNotTerminate`, KubeDB takes advantage of `ValidationWebhook` feature in Kubernetes 1.9.0 or later clusters to implement `DoNotTerminate` feature. If admission webhook is enabled, `DoNotTerminate` prevents users from deleting the database as long as the `spec.deletionPolicy` is set to `DoNotTerminate`.

Following table show what KubeDB does when you delete MariaDB crd for different termination policies,

| Behavior | DoNotTerminate | Halt | Delete | WipeOut |
| --- | --- | --- | --- | --- |
| 1. Block Delete operation | ✓ | ✗ | ✗ | ✗ |
| 2. Delete PetSet | ✗ | ✓ | ✓ | ✓ |
| 3. Delete Services | ✗ | ✓ | ✓ | ✓ |
| 4. Delete PVCs | ✗ | ✗ | ✓ | ✓ |
| 5. Delete Secrets | ✗ | ✗ | ✗ | ✓ |
| 6. Delete Snapshots | ✗ | ✗ | ✗ | ✓ |

If you don’t specify `spec.deletionPolicy` KubeDB uses `Delete` termination policy by default.

> For more details you can visit [here](https://appscode.com/blog/post/deletion-policy/)

<!-- PAGE_START: concepts/migrator.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBMigration

## What is MariaDBMigration

`MariaDBMigration` is a Kubernetes `Custom Resource Definition` (CRD). It provides a declarative way to
migrate an existing database — such as one running on an external or managed instance — into a
KubeDB-managed database. You only need to describe the source and target databases in a `MariaDBMigration`
object, and the kubedb-courier operator will run the migration Job that copies the data and keeps
the target in sync until you cut over.

`MariaDBMigration` is the MariaDB-specific migration CRD (`courier.kubedb.com/v1alpha1`) whose
`spec.source` and `spec.target` describe the MariaDB source and target directly. This page describes
the `MariaDBMigration` object for a **MariaDB** source and target.

## MariaDBMigration Spec

As with all other Kubernetes objects, a `MariaDBMigration` needs `apiVersion`, `kind`, and `metadata`
fields. It also needs a `.spec` section. Below is an example `MariaDBMigration` object for migrating a
MariaDB database.

```yaml
apiVersion: courier.kubedb.com/v1alpha1
kind: MariaDBMigration
metadata:
  name: mariadb-migrate
  namespace: demo
spec:
  source:
    connectionInfo:
      appBinding:
        name: source-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
    schema:
      enabled: true
      database: [] # databases to include
      excludeDatabase: [] # databases to exclude
    snapshot:
      enabled: true
      pipeline:
        workers: 3
        sinkers: 4
        buffer: 12
        read_batch_size: 1000
        write_batch_size: 200
    streaming:
      enabled: true
  target:
    connectionInfo:
      appBinding:
        name: target-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
  jobDefaults:
    imagePullPolicy: IfNotPresent
    backoffLimit: 6
    ttlSecondsAfterFinished: 3600
    activeDeadlineSeconds: 86400
  jobTemplate:
    spec:
      securityContext:
        fsGroup: 65534
```

### spec.source

`spec.source` is a required field that describes the database being migrated **from**. It holds the
MariaDB source fields (`connectionInfo`, `schema`, `snapshot`, `streaming`) directly.

### spec.target

`spec.target` is a required field that describes the KubeDB-managed database being migrated **into**.
It holds the MariaDB target fields directly.

### spec.source.connectionInfo

`connectionInfo` (also under `spec.target`) tells the MariaDBMigration how to connect to the MariaDB
instance. There are two ways to provide the connection details — set **either** `appBinding` **or**
`url`:

* `appBinding` — references an `AppBinding` that holds the connection information for this MariaDB
  instance. An `AppBinding` is a KubeDB resource that decouples the connection details (endpoint,
  credentials, TLS) from the consumer; create one with the necessary information and reference it
  here. This is the recommended approach.
  + `name` — name of the AppBinding.
  + `namespace` — namespace of the AppBinding.
* `url` — the database connection string (for example `mysql://user:password@host:3306/`). Use this
  as an alternative to `appBinding` when you want to provide the endpoint inline instead of through an
  AppBinding.
* `dbName` — the internal database used as the initial connection entry point.
* `maxConnections` — limits the number of concurrent connections the Migration opens to this MariaDB
  instance.
* `tls` — paths to PEM files for a TLS-enabled connection. You can set the following fields:
  + `caFile` — path to the PEM-encoded CA certificate file.
  + `certFile` — path to the PEM-encoded client certificate (for mutual TLS).
  + `keyFile` — path to the PEM-encoded client private key (for mutual TLS).
  + `insecureSkipVerify` — disables server certificate and hostname verification.
  + `serverName` — overrides the hostname used for TLS SNI and certificate verification.

> For a `KubeDB`-managed database, an `AppBinding` is created by default, so you usually only need to
> create one for the source. Learn more about [AppBinding](en/concepts/appbinding.md).

### spec.source.schema

`schema` configures the schema migration phase, which recreates database and table definitions on the
target before any data is copied.

* `enabled` — enables the schema migration phase.
* `database` — list of databases to include. An empty list means all databases except the system
  databases (`mysql`, `information_schema`, `performance_schema`, `sys`).
* `excludeDatabase` — list of databases to exclude from migration.

### spec.source.snapshot

`snapshot` configures the initial bulk snapshot phase, which copies the existing rows from the source
to the target.

* `enabled` — enables the bulk snapshot phase.
* `pipeline` — tunes the parallel copy pipeline:
  + `workers` — number of parallel workers, each processing a separate table concurrently. Defaults
    to `3`.
  + `sinkers` — number of parallel write workers pushing data to the target for each worker. Defaults
    to `3`.
  + `buffer` — size of the in-memory queue (in records) between readers and writers. Defaults to `10`.
  + `read_batch_size` — number of rows fetched per read batch from the source. Defaults to `5000`.
  + `write_batch_size` — number of rows written per batch to the target. Defaults to `500`.

### spec.source.streaming

`streaming` configures the change-data-capture (CDC) phase.

* `enabled` — enables CDC streaming after the snapshot completes, keeping the target continuously in
  sync with ongoing changes on the source until you cut over.

### spec.jobDefaults

`spec.jobDefaults` is an optional field that sets default settings for the migration Job.

* `imagePullPolicy` — the image pull policy for the Migration Job. Defaults to `IfNotPresent`.
* `backoffLimit` — the number of retries before the Job is marked as failed. Defaults to `6`.
* `ttlSecondsAfterFinished` — the TTL (in seconds) for cleaning up a completed Job.
* `activeDeadlineSeconds` — the duration (in seconds) relative to its start time that the Job may be
  active before the system tries to terminate it.

### spec.jobTemplate

`spec.jobTemplate` is an optional field that holds runtime configuration for the migration Job pod
(a `PodTemplateSpec`). Use it to set pod-level settings such as `securityContext`, `nodeSelector`,
`resources`, `serviceAccountName`, and so on.

## MariaDBMigration Status

`status` reflects the observed state of the migration.

* `status.phase` — the current phase of the migration. One of:
  + `Pending` — the migration has not started yet.
  + `Running` — the migration is in progress.
  + `Succeeded` — the migration completed successfully.
  + `Failed` — the migration failed.
* `status.progress` — the current progress of the migration:
  + `dbType` — the type of database being migrated.
  + `info` — additional progress information, including the current `Stage`, `Lag`, and `Progress`
    (these are surfaced as columns in `kubectl get mariadbmigrations`).
* `status.conditions` — an array of conditions describing the migration’s state over time (for
  example, `MigratorJobTriggered`, `MigrationRunning`, `MigrationSucceeded`, `MigrationFailed`).

## Next Steps

* Migrate a MariaDB database step by step with the [MariaDB Database Migration](en/migration/databasemigration.md) guide.
* Learn about the [AppBinding](en/concepts/appbinding.md) concept.
* Learn about the MariaDB CRD [here](en/concepts/mariadb.md).

<!-- PAGE_START: concepts/opsrequest.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBOpsRequest

## What is MariaDBOpsRequest

```mermaid
stateDiagram-v2
  [*] --> Pending: Apply MariaDBOpsRequest CR
  Pending --> Progressing: Ops-Manager validates and acquires lock
  Progressing --> Successful: Rolling PetSet and Pod update complete
  Progressing --> Failed: Precondition or validation fails
  Successful --> [*]
  Failed --> [*]
```


`MariaDBOpsRequest` is a Kubernetes `Custom Resource Definitions` (CRD). It provides a declarative configuration for MariaDB administrative operations like database version updating, horizontal scaling, vertical scaling etc. in a Kubernetes native way.

## MariaDBOpsRequest CRD Specifications

Like any official Kubernetes resource, a `MariaDBOpsRequest` has `TypeMeta`, `ObjectMeta`, `Spec` and `Status` sections.

Here, some sample `MariaDBOpsRequest` CRs for different administrative operations is given below:

**Sample `MariaDBOpsRequest` for updating database:**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-update
  namespace: demo
spec:
  type: UpdateVersion
  databaseRef:
    name: sample-mariadb
  updateVersion:
    targetVersion: 10.5.23
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Sample `MariaDBOpsRequest` Objects for Horizontal Scaling of database cluster:**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdps-scale-horizontal
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: sample-mariadb
  horizontalScaling:
    member : 5
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Sample `MariaDBOpsRequest` Objects for Vertical Scaling of the database cluster:**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-scale-vertical
  namespace: demo
spec:
  type: VerticalScaling  
  databaseRef:
    name: sample-mariadb
  verticalScaling:
    mariadb:
      resources:
        requests:
          memory: "600Mi"
          cpu: "0.1"
        limits:
          memory: "600Mi"
          cpu: "0.1"
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Sample `MariaDBOpsRequest` Objects for Reconfiguring MariaDB Database:**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-reconfigure
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:
    applyConfig:
      my-apply.cnf: |-
        [mysqld]
        max_connections = 300
        read_buffer_size = 1234567        
    restart: "true"
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Sample `MariaDBOpsRequest` Objects for Volume Expansion of MariaDB:**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-volume-expansion
  namespace: demo
spec:
  type: VolumeExpansion  
  databaseRef:
    name: sample-mariadb
  volumeExpansion:   
    mode: "Online"
    mariadb: 2Gi
status:
  conditions:
    - lastTransitionTime: "2020-08-25T18:22:38Z"
      message: Successfully completed the modification process
      observedGeneration: 1
      reason: Successful
      status: "True"
      type: Successful
  observedGeneration: 1
  phase: Successful
```

**Sample `MariaDBOpsRequest` Objects for Reconfiguring TLS of the database:**

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-recon-tls-add
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    requireSSL: true
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
```

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-recon-tls-rotate
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    rotateCertificates: true
```

Here, we are going to describe the various sections of a `MariaDBOpsRequest` crd.

A `MariaDBOpsRequest` object has the following fields in the `spec` section.

### spec.databaseRef

`spec.databaseRef` is a required field that point to the [MariaDB](en/concepts/mariadb.md) object for which the administrative operations will be performed. This field consists of the following sub-field:

* **spec.databaseRef.name :** specifies the name of the [MariaDB](en/concepts/mariadb.md) object.

### spec.type

`spec.type` specifies the kind of operation that will be applied to the database. Currently, the following types of operations are allowed in `MariaDBOpsRequest`.

* `Upgrade` / `UpdateVersion`
* `HorizontalScaling`
* `VerticalScaling`
* `VolumeExpansion`
* `Reconfigure`
* `ReconfigureTLS`
* `Restart`

> You can perform only one type of operation on a single `MariaDBOpsRequest` CR. For example, if you want to update your database and scale up its replica then you have to create two separate `MariaDBOpsRequest`. At first, you have to create a `MariaDBOpsRequest` for updating. Once it is completed, then you can create another `MariaDBOpsRequest` for scaling. You should not create two `MariaDBOpsRequest` simultaneously.

### spec.updateVersion

If you want to update your MariaDB version, you have to specify the `spec.updateVersion` section that specifies the desired version information. This field consists of the following sub-field:

* `spec.updateVersion.targetVersion` refers to a [MariaDBVersion](en/concepts/mariadb-version.md) CR that contains the MariaDB version information where you want to update.

> You can only update between MariaDB versions. KubeDB does not support downgrade for MariaDB.

### spec.horizontalScaling

If you want to scale-up or scale-down your MariaDB cluster or different components of it, you have to specify `spec.horizontalScaling` section. This field consists of the following sub-field:

* `spec.horizontalScaling.member` indicates the desired number of nodes for MariaDB cluster after scaling. For example, if your cluster currently has 4 nodes, and you want to add additional 2 nodes then you have to specify 6 in `spec.horizontalScaling.member` field. Similarly, if you want to remove one node from the cluster, you have to specify 3 in `spec.horizontalScaling.` field.

### spec.verticalScaling

`spec.verticalScaling` is a required field specifying the information of `MariaDB` resources like `cpu`, `memory` etc that will be scaled. This field consists of the following sub-field:

* `spec.verticalScaling.mariadb` indicates the desired resources for MariaDB standalone or cluster after scaling.
* `spec.verticalScaling.exporter` indicates the desired resources for the `exporter` container.
* `spec.verticalScaling.coordinator` indicates the desired resources for the `coordinator` container.
* `spec.verticalScaling.mode` specifies how the scaling is actuated. `Restart` (the default) applies the new resources by restarting the Pods, while `InPlace` resizes the running Pods in place via the Kubernetes `pods/resize` subresource (no restart), automatically falling back to `Restart` for any Pod whose Node cannot fit the new resources. Optional; defaults to `Restart`. For a distributed deployment, in-place resize is not possible, so `InPlace` degrades to `Restart`.

All of them has the below structure:

```yaml
requests:
  memory: "200Mi"
  cpu: "0.1"
limits:
  memory: "300Mi"
  cpu: "0.2"
```

Here, when you specify the resource request, the scheduler uses this information to decide which node to place the container of the Pod on and when you specify a resource limit for the container, the `kubelet` enforces those limits so that the running container is not allowed to use more of that resource than the limit you set. You can found more details from [here](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

### spec.volumeExpansion

> To use the volume expansion feature the storage class must support volume expansion

If you want to expand the volume of your MariaDB standalone or cluster, you have to specify `spec.volumeExpansion` section. This field consists of the following sub-field:

* `spec.volumeExpansion.mariadb` indicates the desired size for the persistent volume of a MariaDB.
* `spec.volumeExpansion.mode` indicates the mode of volume expansion. It can be `online` or `offline` based on the storage class.

All of them refer to Quantity types of Kubernetes.

Example usage of this field is given below:

```yaml
spec:
  volumeExpansion:
    mariadb: "2Gi"
```

This will expand the volume size of all the mariadb nodes to 2 GB.

### spec.configuration

If you want to reconfigure your Running MariaDB cluster with new custom configuration, you have to specify `spec.configuration` section. This field consists of the following sub-fields:

* `configSecret` points to a secret in the same namespace of a MariaDB resource, which contains the new custom configurations. If there are any configSecret set before in the database, this secret will replace it.
* `applyConfig` contains the new custom config as a string which will be merged with the previous configuration.
* `removeCustomConfig` reomoves all the custom configs of the MariaDB server.
* `restart` significantly reduces unnecessary downtime.
  + `auto` (default): restart only if required (determined by ops manager operator)
  + `false`: If user set the restart to false, then pod will not be restarted and new config will not be synced with database.
  + `true`: always restart

### spec.tls

If you want to reconfigure the TLS configuration of your database i.e. add TLS, remove TLS, update issuer/cluster issuer or Certificates and rotate the certificates, you have to specify `spec.tls` section. This field consists of the following sub-field:

* `spec.tls.issuerRef` specifies the issuer name, kind and api group.
* `spec.tls.certificates` specifies the certificates. You can learn more about this field from [here](en/concepts/mariadb.md#spectls).
* `spec.tls.rotateCertificates` specifies that we want to rotate the certificate of this database.
* `spec.tls.remove` specifies that we want to remove tls from this database.

### MariaDBOpsRequest `Status`

`.status` describes the current state and progress of a `MariaDBOpsRequest` operation. It has the following fields:

### status.phase

`status.phase` indicates the overall phase of the operation for this `MariaDBOpsRequest`. It can have the following three values:

| Phase | Meaning |
| --- | --- |
| Successful | KubeDB has successfully performed the operation requested in the MariaDBOpsRequest |
| Failed | KubeDB has failed the operation requested in the MariaDBOpsRequest |
| Denied | KubeDB has denied the operation requested in the MariaDBOpsRequest |

### status.observedGeneration

`status.observedGeneration` shows the most recent generation observed by the `MariaDBOpsRequest` controller.

### status.conditions

`status.conditions` is an array that specifies the conditions of different steps of `MariaDBOpsRequest` processing. Each condition entry has the following fields:

* `types` specifies the type of the condition. MariaDBOpsRequest has the following types of conditions:

| Type | Meaning |
| --- | --- |
| `Progressing` | Specifies that the operation is now in the progressing state |
| `Successful` | Specifies such a state that the operation on the database was successful. |
| `Failed` | Specifies such a state that the operation on the database failed. |
| `ScaleDownCluster` | Specifies such a state that the scale down operation of replicaset |
| `ScaleUpCluster` | Specifies such a state that the scale up operation of replicaset |
| `VolumeExpansion` | Specifies such a state that the volume expansion operaton of the database |
| `Reconfigure` | Specifies such a state that the reconfiguration of replicaset nodes |

* The `status` field is a string, with possible values `True`, `False`, and `Unknown`.
  + `status` will be `True` if the current transition succeeded.
  + `status` will be `False` if the current transition failed.
  + `status` will be `Unknown` if the current transition was denied.
* The `message` field is a human-readable message indicating details about the condition.
* The `reason` field is a unique, one-word, CamelCase reason for the condition’s last transition.
* The `lastTransitionTime` field provides a timestamp for when the operation last transitioned from one state to another.
* The `observedGeneration` shows the most recent condition transition generation observed by the controller.

<!-- PAGE_START: configuration/using-config-file.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Using Custom Configuration File

KubeDB supports providing custom configuration for MariaDB. This tutorial will show you how to use KubeDB to run a MariaDB database with custom configuration.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

  ```bash
  $ kubectl create ns demo
  namespace/demo created

  $ kubectl get ns demo
  NAME    STATUS  AGE
  demo    Active  5s
  ```

> Note: YAML files used in this tutorial are stored in [here](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/configuration/using-config-file/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Overview

MariaDB allows to configure database via configuration file. The default configuration for MariaDB can be found in `/etc/mysql/my.cnf` file. When MariaDB starts, it will look for custom configuration file in `/etc/mysql/conf.d` directory. If configuration file exist, MariaDB instance will use combined startup setting from both `/etc/mysql/my.cnf` and `*.cnf` files in `/etc/mysql/conf.d` directory. This custom configuration will overwrite the existing default one. To know more about configuring MariaDB see [here](https://mariadb.com/kb/en/configuring-mariadb-with-option-files/).

At first, you have to create a config file with `.cnf` extension with your desired configuration. Then create a Secret with this configuration file and provide its name in `spec.configuration.secretName`. The operator reads this Secret internally and applies the configuration automatically, without mounting any volume into the Pod.

In this tutorial, we will configure [max\_connections](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_connections) and [read\_buffer\_size](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#read_buffer_size/) via a custom config file. We will use Secret as volume source.

## Custom Configuration

At first, let’s create `md-config.cnf` file setting `max_connections` and `read_buffer_size` parameters.

```bash
cat <<EOF > md-config.cnf
[mysqld]
max_connections = 200
read_buffer_size = 1048576
EOF

$ cat md-config.cnf
[mysqld]
max_connections = 200
read_buffer_size = 1048576
```

Here, `read_buffer_size` is set to 1MB in bytes.

Now, create a Secret with this configuration file.

```bash
$ kubectl create secret generic -n demo md-configuration --from-file=./md-config.cnf
secret/md-configuration created
```

Verify the Secret has the configuration file.

```bash
$ kubectl get secret -n demo md-configuration -o yaml
```

```text
apiVersion: v1
stringData:
  md-config.cnf: |
    [mysqld]
    max_connections = 200
    read_buffer_size = 1048576    
kind: Secret
metadata:
  name: md-configuration
  namespace: demo
  ...
```

Now, create MariaDB crd specifying `spec.configuration.secretName` field.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/configuration/using-config-file/examples/md-custom.yaml
mariadb.kubedb.com/sample-mariadb created
```

Below is the YAML for the MariaDB crd we just created.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  configuration:
    secretName: md-configuration
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

Now, wait a few minutes. KubeDB operator will create necessary PVC, petset, services, secret etc. If everything goes well, we will see that a pod with the name `sample-mariadb-0` has been created.

Check that the petset’s pod is running

```bash
$ kubectl get pod -n demo
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          21s

$ kubectl get mariadb -n demo 
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    71s
```

We can see the database is in ready phase so it can accept conncetion.

Now, we will check if the database has started with the custom configuration we have provided.

> Read the comment written for the following commands. They contain the instructions and explanations of the commands.

```bash
# Connecting to the database
 $ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is same as provided 
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 200   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1048576 |
+------------------+---------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: configuration/using-pod-template.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Run MariaDB with Custom PodTemplate

KubeDB supports providing custom configuration for MariaDB via [PodTemplate](en/concepts/mariadb.md#specpodtemplate). This tutorial will show you how to use KubeDB to run a MariaDB database with custom configuration using PodTemplate.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Note: YAML files used in this tutorial are stored in [docs/guides/mariadb/configuration/using-pod-template/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/configuration/using-pod-template/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Overview

KubeDB allows providing a template for database pod through `spec.podTemplate`. KubeDB operator will pass the information provided in `spec.podTemplate` to the PetSet created for MariaDB database.

KubeDB accept following fields to set in `spec.podTemplate:`

* metadata:
  + annotations (pod’s annotation)
* controller:
  + annotations (petset’s annotation)
* spec:
  + env
  + resources
  + initContainers
  + imagePullSecrets
  + nodeSelector
  + schedulerName
  + tolerations
  + priorityClassName
  + priority
  + securityContext

Read about the fields in details in [PodTemplate concept](en/concepts/mariadb.md#specpodtemplate),

## CRD Configuration

Below is the YAML for the MariaDB created in this example. Here, [`spec.podTemplate.spec.env`](en/concepts/mariadb.md#specpodtemplatespecenv) specifies environment variables and [`spec.podTemplate.spec.args`](en/concepts/mariadb.md#specpodtemplatespecargs) provides extra arguments for [MariaDB Docker Image](https://hub.docker.com/_/mariadb/).

In this tutorial, an initial database `mdDB` will be created by providing `env` `MYSQL_DATABASE` while the server character set will be set to `utf8mb4` by adding extra `args`.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      containers:
      - name: mariadb
        env:
        - name: MYSQL_DATABASE
          value: mdDB
        args:
        - --character-set-server=utf8mb4
        resources:
          requests:
            memory: "1Gi"
            cpu: "250m"
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/configuration/using-pod-template/examples/md-misc-config.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait a few minutes. KubeDB operator will create necessary PVC, petset, services, secret etc. If everything goes well, we will see that a pod with the name `sample-mariadb` has been created.

Check that the petset’s pod is running

```bash
$ kubectl get pod -n demo
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          96s
```

Check the pod’s log to see if the database is ready

```bash
$ kubectl logs -f -n demo sample-mariadb-0
2021-03-18 06:06:17+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 06:06:18+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 06:06:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 06:06:19+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  6:06:33 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

Once we see `Note] mysqld: ready for connections.` in the log, the database is ready.

Now, we will check if the database has started with the custom configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 22
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check mdDB
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mdDB               |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Check character_set_server
MariaDB [(none)]> show variables like 'char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | latin1                     |
| character_set_connection | latin1                     |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | latin1                     |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: custom-rbac/using-custom-rbac.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Using Custom RBAC resources

KubeDB (version 0.13.0 and higher) supports finer user control over role based access permissions provided to a MariaDB instance. This tutorial will show you how to use KubeDB to run MariaDB instance with custom RBAC resources.

## Before You Begin

At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).

Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).

To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

> Note: YAML files used in this tutorial are stored in [here](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Overview

KubeDB allows users to provide custom RBAC resources, namely, `ServiceAccount`, `Role`, and `RoleBinding` for MariaDB. This is provided via the `spec.podTemplate.spec.serviceAccountName` field in MariaDB crd. If this field is left empty, the KubeDB operator will create a service account name matching MariaDB crd name. Role and RoleBinding that provide necessary access permissions will also be generated automatically for this service account.

If a service account name is given, but there’s no existing service account by that name, the KubeDB operator will create one, and Role and RoleBinding that provide necessary access permissions will also be generated for this service account.

If a service account name is given, and there’s an existing service account by that name, the KubeDB operator will use that existing service account. Since this service account is not managed by KubeDB, users are responsible for providing necessary access permissions manually.

This guide will show you how to create custom `Service Account`, `Role`, and `RoleBinding` for a MariaDB instance named `sample-mariadb` to provide the bare minimum access permissions.

## Custom RBAC for MariaDB

At first, let’s create a `Service Acoount` in `demo` namespace.

```bash
$ kubectl create serviceaccount -n demo md-custom-serviceaccount
serviceaccount/md-custom-serviceaccount created
```

It should create a service account.

```bash
$ kubectl get serviceaccount -n demo md-custom-serviceaccount -o yaml
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: "2021-03-18T04:38:59Z"
  name: md-custom-serviceaccount
  namespace: demo
  resourceVersion: "84669"
  selfLink: /api/v1/namespaces/demo/serviceaccounts/md-custom-serviceaccount
  uid: 788bd6c6-3eae-4797-b6ca-5722ef64c9dc
secrets:
- name: md-custom-serviceaccount-token-jnhvd
```

Now, we need to create a role that has necessary access permissions for the MariaDB instance named `sample-mariadb`.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-role.yaml
role.rbac.authorization.k8s.io/md-custom-role created
```

Below is the YAML for the Role we just created.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: md-custom-role
  namespace: demo
rules:
- apiGroups:
  - policy
  resourceNames:
  - maria-db
  resources:
  - podsecuritypolicies
  verbs:
  - use
```

This permission is required for MariaDB pods running on PSP enabled clusters.

Now create a `RoleBinding` to bind this `Role` with the already created service account.

```bash
$ kubectl create rolebinding md-custom-rolebinding --role=md-custom-role --serviceaccount=demo:md-custom-serviceaccount --namespace=demo
rolebinding.rbac.authorization.k8s.io/md-custom-rolebinding created
```

It should bind `md-custom-role` and `md-custom-serviceaccount` successfully.

SO, All required resources for RBAC are created.

```bash
$ kubectl get serviceaccount,role,rolebindings -n demo
NAME                                      SECRETS   AGE
serviceaccount/default                    1         38m
serviceaccount/md-custom-serviceaccount   1         36m

NAME                                            CREATED AT
role.rbac.authorization.k8s.io/md-custom-role   2021-03-18T05:13:27Z

NAME                                                          ROLE                  AGE
rolebinding.rbac.authorization.k8s.io/md-custom-rolebinding   Role/md-custom-role   79s
```

Now, create a MariaDB crd specifying `spec.podTemplate.spec.serviceAccountName` field to `md-custom-serviceaccount`.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-db.yaml
mariadb.kubedb.com/sample-mariadb created
```

Below is the YAML for the MariaDB crd we just created.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  podTemplate:
    spec:
      serviceAccountName: md-custom-serviceaccount
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Now, wait a few minutes. the KubeDB operator will create necessary PVC, PetSet, services, secret etc. If everything goes well, we should see that a pod with the name `sample-mariadb-0` has been created.

Check that the petset’s pod is running

```bash
$ kubectl get pod -n demo sample-mariadb-0
NAME            READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          2m44s
```

Check the pod’s log to see if the database is ready

```bash
$ kubectl logs -f -n demo sample-mariadb-0
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:35:14+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  5:35:22 0 [Note] Reading of all Master_info entries succeeded
2021-03-18  5:35:22 0 [Note] Added new Master_info '' to hash table
2021-03-18  5:35:22 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

Once we see `mysqld: ready for connections.` in the log, the database is ready.

## Reusing Service Account

An existing service account can be reused in another MariaDB instance. No new access permission is required to run the new MariaDB instance.

Now, create MariaDB crd `another-mariadb` using the existing service account name `md-custom-serviceaccount` in the `spec.podTemplate.spec.serviceAccountName` field.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-db-2.yaml
mariadb.kubedb.com/another-mariadb created
```

Below is the YAML for the MariaDB crd we just created.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: another-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  podTemplate:
    spec:
      serviceAccountName: md-custom-serviceaccount
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Now, wait a few minutes. the KubeDB operator will create necessary PVC, petset, services, secret etc. If everything goes well, we should see that a pod with the name `another-mariadb` has been created.

Check that the petset’s pod is running

```bash
$ kubectl get pod -n demo another-mariadb-0
NAME                READY   STATUS    RESTARTS   AGE
another-mariadb-0   1/1     Running   0          37s
```

Check the pod’s log to see if the database is ready

```bash
...
$ kubectl logs -f -n demo another-mariadb-0
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:10.5.23+maria~focal started.
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  5:39:59 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

`mysqld: ready for connections.` in the log signifies that the database is running successfully.

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete mariadb -n demo another-mariadb
mariadb.kubedb.com "another-mariadb" deleted
$ kubectl delete -n demo role md-custom-role
role.rbac.authorization.k8s.io "md-custom-role" deleted
$ kubectl delete -n demo rolebinding md-custom-rolebinding
rolebinding.rbac.authorization.k8s.io "md-custom-rolebinding" deleted
$ kubectl delete sa -n demo md-custom-serviceaccount
serviceaccount "md-custom-serviceaccount" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: distributed/overview.md -->
# Distributed MariaDB Galera Cluster Overview

## Introduction

KubeDB enables distributed MariaDB deployments using Galera clustering technology across multiple Kubernetes clusters, providing a scalable, highly available, and resilient database solution. By integrating **Open Cluster Management (OCM)** for multi-cluster orchestration and **KubeSlice** for seamless pod-to-pod network connectivity, KubeDB simplifies the deployment and management of MariaDB instances across clusters. A **PlacementPolicy** ensures precise control over pod scheduling, allowing you to distribute MariaDB pods across clusters for optimal resource utilization and fault tolerance.

This guide provides a step-by-step process to deploy a distributed MariaDB Galera cluster, including prerequisites, configuration, and verification steps. It assumes familiarity with Kubernetes and basic database concepts.

> **New to KubeDB?** Please start [here](https://kubedb.com/docs/v2026.7.10/README).

## Understanding OCM Hub and Spoke Clusters

In an **Open Cluster Management (OCM)** setup, clusters are categorized as follows:

* **Hub Cluster**: The central control plane where policies, applications, and resources are defined and managed. It orchestrates the lifecycle of applications deployed across spoke clusters.
* **Spoke Cluster**: Managed clusters registered with the hub that run the actual workloads (e.g., MariaDB pods).

When a spoke cluster (e.g., `demo-worker`) is joined to the hub using the `clusteradm join` command, OCM creates a namespace on the hub cluster that matches the spoke cluster’s name (e.g., `demo-worker`). This namespace is used to manage resources specific to the spoke cluster from the hub.

## Prerequisites

Before deploying a distributed MariaDB Galera cluster, ensure the following requirements are met:

* **Kubernetes Clusters**: Multiple Kubernetes clusters (version 1.26 or higher) configured and accessible.
* **Node Requirements**: Each Kubernetes node should have at least 4 vCPUs and 16 GB of RAM.
* **Open Cluster Management (OCM)**: Install `clusteradm` as described in the [OCM Quick Start Guide](https://open-cluster-management.io/docs/getting-started/quick-start/).
* **kubectl**: Installed and configured to interact with all clusters.
* **Helm**: Installed for deploying the KubeDB Operator and KubeSlice components.
* **Persistent Storage**: A storage class (e.g., `local-path` or a cloud provider-specific option) configured for persistent volumes.

## Configuration Steps

Follow these steps to deploy a distributed MariaDB Galera cluster across multiple Kubernetes clusters.

### Step 1: Set Up Open Cluster Management (OCM)

#### 1. Configure KUBECONFIG

Ensure your `KUBECONFIG` is set up to switch between clusters. This guide uses two clusters: `demo-controller` (hub and spoke) and `demo-worker` (spoke).

```bash
$ kubectl config get-contexts
```

**Output:**

```bash
CURRENT   NAME              CLUSTER           AUTHINFO          NAMESPACE
*         demo-controller   demo-controller   demo-controller   
          demo-worker       demo-worker       demo-worker
```

#### 2. Initialize the OCM Hub

On the `demo-controller` cluster, initialize the OCM hub:

```bash
$ kubectl config use-context demo-controller
$ clusteradm init --wait --feature-gates=ManifestWorkReplicaSet=true
```

#### 3. Verify Hub Deployment

Check the pods in the `open-cluster-management-hub` namespace to ensure all components are running:

```bash
$ kubectl get pods -n open-cluster-management-hub
```

**Output:**

```
NAME                                                        READY   STATUS    RESTARTS   AGE
cluster-manager-addon-manager-controller-5f99f56896-qpzj8   1/1     Running   0          7m2s
cluster-manager-placement-controller-597d5ff644-wqjq2       1/1     Running   0          7m2s
cluster-manager-registration-controller-6d79d7dcc6-b8h9p    1/1     Running   0          7m2s
cluster-manager-registration-webhook-5d88cf97c7-2sq5m       1/1     Running   0          7m2s
cluster-manager-work-controller-7468bf4dc-5qn6q             1/1     Running   0          7m2s
cluster-manager-work-webhook-c5875947-d272b                 1/1     Running   0          7m2s
```

All pods should be in the `Running` state with `1/1` readiness and no restarts, indicating a successful hub deployment.

#### 4. Register Spoke Cluster (`demo-worker`)

Obtain the join token from the hub cluster:

```bash
$ clusteradm get token
```

**Output:**

```
token=<Your_Clusteradm_Join_Token>
please log on spoke and run:
clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name <cluster_name>
```

On the `demo-worker` cluster, join it to the hub. Include the `RawFeedbackJsonString` feature gate for resource feedback:

```bash
$ kubectl config use-context demo-worker
$ clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name demo-worker --feature-gates=RawFeedbackJsonString=true
```

#### 5. Accept Spoke Cluster

On the `demo-controller` cluster, accept the `demo-worker` cluster:

```bash
$ kubectl config use-context demo-controller
$ clusteradm accept --clusters demo-worker
```

> **Note:** It may take a few attempts (e.g., retry every 10 seconds) if the cluster is not immediately available.

**Output (on success):**

```
Starting approve csrs for the cluster demo-worker
CSR demo-worker-2p2pb approved
set hubAcceptsClient to true for managed cluster demo-worker
Your managed cluster demo-worker has joined the Hub successfully.
```

#### 6. Verify Namespace Creation

Confirm that a namespace for `demo-worker` was created on the hub cluster:

```bash
$ kubectl get ns
```

**Output:**

```bash
NAME                          STATUS   AGE
default                       Active   99m
demo-worker                   Active   58s
kube-node-lease               Active   99m
kube-public                   Active   99m
kube-system                   Active   99m
open-cluster-management       Active   6m7s
open-cluster-management-hub   Active   5m32s
```

#### 7. Register `demo-controller` as a Spoke Cluster

Repeat the join and accept process for `demo-controller` so it can also act as a spoke cluster:

```bash
$ kubectl config use-context demo-controller
$ clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name demo-controller --feature-gates=RawFeedbackJsonString=true
$ clusteradm accept --clusters demo-controller
```

Verify the namespace for `demo-controller`:

```bash
$ kubectl get ns
```

**Output:**

```
NAME                                  STATUS   AGE
default                               Active   104m
demo-controller                       Active   3s
demo-worker                           Active   6m7s
kube-node-lease                       Active   104m
kube-public                           Active   104m
kube-system                           Active   104m
open-cluster-management               Active   11m
open-cluster-management-agent         Active   37s
open-cluster-management-agent-addon   Active   34s
open-cluster-management-hub           Active   10m
```

#### 8. Verify OCM Roles

After registration, use these commands to confirm which cluster is the hub and which are spokes:

```bash
# Hub: lists all registered spoke clusters
$ kubectl get managedclusters

# Spoke: shows this cluster's registered name
$ kubectl get klusterlet klusterlet -o jsonpath='{.spec.clusterName}'

# Hub components run only on the hub cluster
$ kubectl get pods -n open-cluster-management-hub

# Spoke agent runs on every spoke cluster
$ kubectl get pods -n open-cluster-management-agent
```

### Step 2: Configure OCM WorkConfiguration

Run this on **every spoke cluster** (`demo-controller` and `demo-worker`). This enables the `RawFeedbackJsonString` feature gate that KubeDB requires to read pod status across clusters, and raises the API rate limits to prevent throttling.

> **Note:** Even if you passed `--feature-gates=RawFeedbackJsonString=true` during `clusteradm join`, the rate limit fields are not set by that flag. Run this patch on all spokes regardless.
>
> **Why this matters:** KubeDB uses OCM’s ManifestWork feedback mechanism to watch the status of MariaDB pods on remote spoke clusters. Without `RawFeedbackJsonString`, the KubeDB provisioner on the hub never receives pod status updates from spokes and the distributed MariaDB CR will stay in a non-Ready state indefinitely. The rate limits prevent the klusterlet agent from being API-throttled during initial cluster formation.

```bash
$ kubectl patch klusterlet klusterlet --type=merge -p '{
  "spec": {
    "workConfiguration": {
      "featureGates": [{"feature": "RawFeedbackJsonString", "mode": "Enable"}],
      "hubKubeAPIBurst": 100,
      "hubKubeAPIQPS": 50,
      "kubeAPIBurst": 100,
      "kubeAPIQPS": 50
    }
  }
}'
```

Verify the configuration:

```bash
$ kubectl get klusterlet klusterlet -oyaml
```

**Sample Output (abridged):**

```yaml
apiVersion: operator.open-cluster-management.io/v1
kind: Klusterlet
metadata:
  name: klusterlet
spec:
  clusterName: demo-worker
  workConfiguration:
    featureGates:
    - feature: RawFeedbackJsonString
      mode: Enable
    hubKubeAPIBurst: 100
    hubKubeAPIQPS: 50
    kubeAPIBurst: 100
    kubeAPIQPS: 50
```

### Step 3: Configure KubeSlice for Network Connectivity

KubeSlice enables pod-to-pod communication across clusters. Install the KubeSlice Controller on the `demo-controller` cluster and the KubeSlice Worker on both `demo-controller` and `demo-worker` clusters.

#### 1. Install KubeSlice Controller

On `demo-controller`, get the hub API server address first:

```bash
$ kubectl cluster-info | grep 'Kubernetes control plane'
```

Use the IP and port from that output as the `endpoint` value. Create a `controller.yaml` file:

```yaml
kubeslice:
  controller:
    loglevel: info
    rbacResourcePrefix: kubeslice-rbac
    projectnsPrefix: kubeslice
    endpoint: https://<hub-apiserver-ip>:6443
```

Deploy the controller using Helm:

```bash
$ helm upgrade -i kubeslice-controller oci://ghcr.io/appscode-charts/kubeslice-controller \
    --version v2026.1.15 \
    -f controller.yaml \
    --namespace kubeslice-controller \
    --create-namespace \
    --set ocm.enabled=true \
    --wait --burst-limit=10000 --debug
```

Verify the installation:

```bash
$ kubectl get pods -n kubeslice-controller
```

**Output:**

```
NAME                                            READY   STATUS    RESTARTS   AGE
kubeslice-controller-manager-7fd756fff6-5kddd   2/2     Running   0          98s
```

#### 2. Create a KubeSlice Project

Create a `project.yaml` file:

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: Project
metadata:
  name: demo-distributed-mariadb
  namespace: kubeslice-controller
spec:
  serviceAccount:
    readWrite:
      - admin
```

Apply the project:

```bash
$ kubectl apply -f project.yaml
```

Verify:

```bash
$ kubectl get project -n kubeslice-controller
```

**Output:**

```bash
NAME                       AGE
demo-distributed-mariadb   31s
```

Check service accounts:

```bash
$ kubectl get sa -n kubeslice-demo-distributed-mariadb
```

**Output:**

```
NAME                      SECRETS   AGE
default                   0         69s
kubeslice-rbac-rw-admin   1         68s
```

#### 3. Label Nodes for KubeSlice

Assign the `kubeslice.io/node-type=gateway` label to the node where the worker operator will be deployed in both clusters.

On `demo-controller`:

```bash
$ kubectl get nodes
$ kubectl label node <node-name> kubeslice.io/node-type=gateway
```

On `demo-worker`:

```bash
$ kubectl config use-context demo-worker
$ kubectl get nodes
$ kubectl label node <node-name> kubeslice.io/node-type=gateway
```

#### 4. Register Clusters with KubeSlice

Identify the network interface for each cluster by running the following command **on the gateway node of each cluster**:

```bash
$ ip route get 8.8.8.8 | awk '{ print $5 }'
```

**Output (example):**

```
enp1s0
```
> **Important:** The `networkInterface` value must match the primary network interface of each cluster’s gateway node. Run the command above on **each cluster separately** and use that cluster’s output as its `networkInterface` value. Each cluster may have a **different interface name** — do not assume they are the same. Using the wrong interface name will cause the WireGuard gateway to silently fail and cross-cluster MariaDB replication will never connect.
>
> Example: if `demo-controller` returns `enp3s0` and `demo-worker` returns `eth0`, use those exact values in the YAML below.

Create a `registration.yaml` file:

> **Note:**
>
> * The cluster name must exactly match the name of the OCM (spoke) cluster.
> * The corresponding `ManagedClusterAddOn` resource must be created in the namespace that bears the same name as the cluster to set up the KubeSlice worker automatically.

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: Cluster
metadata:
  name: demo-controller
  namespace: kubeslice-demo-distributed-mariadb
spec:
  networkInterface: <demo-controller-interface>   # replace with output of ip route command
  clusterProperty: {}
---
apiVersion: controller.kubeslice.io/v1alpha1
kind: Cluster
metadata:
  name: demo-worker
  namespace: kubeslice-demo-distributed-mariadb
spec:
  networkInterface: <demo-worker-interface>   # replace with output of ip route command
  clusterProperty: {}
---
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: kubeslice
  namespace: demo-controller
spec:
  installNamespace: kubeslice-system
  configs:
    - name: demo-controller
      namespace: kubeslice-demo-distributed-mariadb
      group: controller.kubeslice.io
      resource: clusters
---
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: kubeslice
  namespace: demo-worker
spec:
  installNamespace: kubeslice-system
  configs:
    - name: demo-worker
      namespace: kubeslice-demo-distributed-mariadb
      group: controller.kubeslice.io
      resource: clusters
```

Apply on `demo-controller`:

```bash
$ kubectl apply -f registration.yaml
```

Verify OCM is deploying the KubeSlice worker manifests to each cluster:

```bash
$ kubectl get managedclusteraddon -A
```

**Output:**

```
NAMESPACE         NAME        AVAILABLE   DEGRADED   PROGRESSING
demo-controller   kubeslice   Unknown                True
demo-worker       kubeslice   Unknown                True
```

`PROGRESSING: True` means OCM is actively deploying. Wait until `kubeslice-operator` shows `2/2 Running` on both clusters before proceeding:

```bash
# Run on each spoke cluster
$ kubectl get pods -n kubeslice-system --watch
```

**Expected output (after KubeSlice worker is fully deployed):**

```
NAME                                 READY   STATUS      RESTARTS   AGE
forwarder-kernel-bw5l4               1/1     Running     0          4m43s
kubeslice-dns-6bd9749f4d-pvh7g       1/1     Running     0          4m43s
kubeslice-install-crds-szhvc         0/1     Completed   0          4m56s
kubeslice-netop-g4dfn                1/1     Running     0          4m43s
kubeslice-operator-949b7d6f7-9wj7h   2/2     Running     0          4m43s
nsc-grpc-server-sbjj7                1/1     Running     0          4m43s
nsm-install-crds-5z4j9               0/1     Completed   0          4m53s
nsmgr-zzwgh                          2/2     Running     0          4m43s
registry-k8s-979455d6d-q2j8x         1/1     Running     0          4m43s
```

#### 5. Onboard Application Namespace

Create a `SliceConfig` to onboard the `demo` (application) and `kubedb` (operator) namespaces for network connectivity. Create a `sliceconfig.yaml` file:

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: SliceConfig
metadata:
  name: demo-slice
  namespace: kubeslice-demo-distributed-mariadb
spec:
  sliceSubnet: 10.1.0.0/16
  maxClusters: 16
  sliceType: Application
  sliceGatewayProvider:
    sliceGatewayType: Wireguard
    sliceCaType: Local
  sliceIpamType: Local
  rotationInterval: 60
  vpnConfig:
    cipher: AES-128-CBC
  clusters:
    - demo-controller
    - demo-worker
  qosProfileDetails:
    queueType: HTB
    priority: 1
    tcType: BANDWIDTH_CONTROL
    bandwidthCeilingKbps: 5120
    bandwidthGuaranteedKbps: 2560
    dscpClass: AF11
  namespaceIsolationProfile:
    applicationNamespaces:
      - namespace: demo
        clusters:
          - '*'
      - namespace: kubedb
        clusters:
          - '*'
    isolationEnabled: false
    allowedNamespaces:
      - namespace: kube-system
        clusters:
          - '*'
```

Apply the `SliceConfig`:

```bash
$ kubectl apply -f sliceconfig.yaml
```

After the SliceConfig is applied, a `vl3-slice-router` pod will appear in `kubeslice-system` on each cluster, indicating the slice VPN tunnel is being established.

#### 6. Configure DNS for KubeSlice

> Note: You must update the DNS server for each cluster you mentioned in the slice to enable proper cross-cluster service discovery. In this guide, we are using CoreDNS, so the required changes are applied to the CoreDNS configuration.
> If your cluster uses a different DNS solution, make sure to apply equivalent forwarding rules there.
>
> This configuration step must be completed on all clusters participating in the slice before proceeding further.

Update CoreDNS to forward `*.slice.local` traffic to the KubeSlice DNS service. Run the following steps on **every cluster** in the slice.

> **Important:** CoreDNS must be updated and restarted on all clusters before proceeding to Step 4 (KubeDB install). Galera nodes use `.slice.local` DNS names to discover each other across clusters. If DNS is not configured before MariaDB pods start, replication will not form.

Get the KubeSlice DNS service IP address on each cluster:

```bash
$ kubectl get svc -n kubeslice-system -owide -l 'app=kubeslice-dns'
```

**Output:**

```bash
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE   SELECTOR
kubeslice-dns   ClusterIP   10.43.172.191   <none>        53/UDP,53/TCP   8d    app=kubeslice-dns
```

Add the following block to the **top** of your CoreDNS `Corefile` ConfigMap (replace the IP with the one from your cluster):

```
slice.local:53 {
    errors
    cache 30
    forward . 10.43.172.191
}
```

Example of the full CoreDNS ConfigMap after editing:

```bash
$ kubectl get cm -n kube-system coredns -oyaml
```

**Output:**

```yaml
apiVersion: v1
data:
  Corefile: |
    slice.local:53 {
        errors
        cache 30
        forward . 10.43.172.191
    }
    .:53 {
        errors
        health
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          fallthrough in-addr.arpa ip6.arpa
        }
        hosts /etc/coredns/NodeHosts {
          ttl 60
          reload 15s
          fallthrough
        }
        prometheus :9153
        cache 30
        loop
        reload
        loadbalance
        import /etc/coredns/custom/*.override
        forward . /etc/resolv.conf
    }
    import /etc/coredns/custom/*.server    
  NodeHosts: |
    10.2.0.248 demo-worker    
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
```

After editing the ConfigMap, restart CoreDNS to apply the change:

```bash
$ kubectl rollout restart deploy/coredns -n kube-system
```

Repeat the DNS configuration steps on every cluster in the slice.

### Step 4: Install the KubeDB Operator

> **Note:** Install the KubeDB operator only on the hub cluster (`demo-controller`). The operator manages MariaDB pods on spoke clusters through OCM — no KubeDB installation is needed on `demo-worker`.

#### Get a Free License

The KubeDB license is tied to the `kube-system` namespace UID of the hub cluster and has an expiry date. Get your cluster UID and verify the license before installing:

```bash
# Get your cluster UID (required when requesting the license)
$ kubectl get ns kube-system -o jsonpath='{.metadata.uid}'

# Verify the license is not expired
$ openssl x509 -noout -enddate -in $HOME/Downloads/kubedb-license-<uid>.txt
```

If expired or not yet obtained, download a FREE license from the [AppsCode License Server](https://appscode.com/issue-license?p=kubedb) using the cluster UID above.

```bash
$ helm upgrade -i kubedb oci://ghcr.io/appscode-charts/kubedb \
    --version v2026.2.26 \
    --namespace kubedb --create-namespace \
    --set-file global.license=$HOME/Downloads/kubedb-license-<uid>.txt \
    --set petset.features.ocm.enabled=true \
    --wait --burst-limit=10000 --debug
```

> **Note:** The `--set petset.features.ocm.enabled=true` flag must be set to enable the MariaDB Distributed feature.

For additional details, refer to the [KubeDB Installation Guide](https://kubedb.com/docs/v2026.7.10/setup/).

Verify that the pods are running:

```bash
$ kubectl get pods -n kubedb
```

**Output:**

```bash
NAME                                           READY   STATUS    RESTARTS   AGE
kubedb-kubedb-autoscaler-0                     1/2     Running   0          44s
kubedb-kubedb-ops-manager-0                    1/2     Running   0          43s
kubedb-kubedb-provisioner-0                    1/2     Running   0          43s
kubedb-kubedb-webhook-server-df667cd85-tjdp9   2/2     Running   0          44s
kubedb-petset-cf9f5b6f4-d9558                  2/2     Running   0          44s
kubedb-sidekick-5dbf7bcf64-4b8cw               2/2     Running   0          44s
```

### Step 5: Define a PlacementPolicy

You can define the `storageClassName` under `spec.clusterSpreadConstraint.distributionRules` for each cluster. If not explicitly specified, the clusters will automatically select an appropriate storage class. Additionally, you can control replica placement by defining which replicas belong to which cluster. When scaling the number of replicas, the distribution must also be specified at the cluster level. In this example, we are using three replicas.

To manage pod distribution across clusters, create a `PlacementPolicy`. For this purpose, define a `pod-placement-policy.yaml` file as shown below:

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        storageClassName: local-path   # optional; omit to use the cluster's default storage class
        replicaIndices:
          - 0
          - 2
      - clusterName: demo-worker
        storageClassName: local-path   # optional; omit to use the cluster's default storage class
        replicaIndices:
          - 1
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

This policy schedules:

* `mariadb-0` and `mariadb-2` on `demo-controller`
* `mariadb-1` on `demo-worker`

Apply the policy on `demo-controller`:

```bash
$ kubectl apply -f pod-placement-policy.yaml --context demo-controller --kubeconfig $HOME/.kube/config
```

### Step 6: Create a Distributed MariaDB Instance

Create the `demo` namespace first:

```bash
$ kubectl create namespace demo
```

Define a MariaDB custom resource with `spec.distributed` set to `true` and reference the `PlacementPolicy`. Create a `mariadb.yaml` file:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
spec:
  distributed: true
  deletionPolicy: WipeOut
  replicas: 3
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 500Mi
  storageType: Durable
  version: 12.1.2
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
```

Apply the resource on `demo-controller`:

```bash
$ kubectl apply -f mariadb.yaml --context demo-controller --kubeconfig $HOME/.kube/config
```

### Step 7: Verify the Deployment

#### 1. Check MariaDB Resource and Pods on `demo-controller`

```bash
$ kubectl get md,pods,secret -n demo --context demo-controller --kubeconfig $HOME/.kube/config
```

**Output:**

```bash
NAME                         VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb   11.5.2    Ready    99s

NAME            READY   STATUS    RESTARTS   AGE
pod/mariadb-0   3/3     Running   0          95s
pod/mariadb-2   3/3     Running   0          95s

NAME                  TYPE                       DATA   AGE
secret/mariadb-auth   kubernetes.io/basic-auth   2      95s
```

#### 2. Check Pods and Secrets on `demo-worker`

```bash
$ kubectl get pods,secrets -n demo --context demo-worker --kubeconfig $HOME/.kube/config
```

**Output:**

```bash
NAME        READY   STATUS    RESTARTS   AGE
mariadb-1   3/3     Running   0          95s

NAME                  TYPE                       DATA   AGE
secret/mariadb-auth   kubernetes.io/basic-auth   2      95s
```

#### 3. Verify Galera Cluster Status

Connect to a MariaDB pod and check the Galera cluster status. The primary service DNS follows the format `<database-name>.<database-namespace>.svc`:

```bash
$ kubectl exec -it -n demo pod/mariadb-0 --context demo-controller -- bash
mariadb -uroot -p$MYSQL_ROOT_PASSWORD -hmariadb.demo.svc
```

Run the following query:

```sql
SHOW STATUS LIKE 'wsrep_cluster_status';
```

**Output:**

```bash
+----------------------+---------+
| Variable_name        | Value   |
+----------------------+---------+
| wsrep_cluster_status | Primary |
+----------------------+---------+
1 row in set (0.001 sec)
```

Check additional Galera status variables:

```sql
SHOW STATUS LIKE 'wsrep%';
```

## Next Steps

* **Accessing the Database**: Use the `mariadb-auth` secret to retrieve credentials and connect to the MariaDB instance.
* **Scaling**: Adjust the `PlacementPolicy` to add or remove replicas across clusters.
* **Monitoring**: Integrate KubeDB with monitoring tools like Prometheus for cluster health insights.

<!-- PAGE_START: failover/guide.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Exploring Fault Tolerance in MariaDB with KubeDB

## Understanding Failover and Clustering in MariaDB on KubeDB

`Failover` refers to the process of automatically switching to a slave system or replica when the `Master`
database node fails. In high-availability database systems, failover ensures that services remain
uninterrupted even when one or more nodes go down. This capability is critical in modern, cloud-native
infrastructure where downtime can lead to major disruptions.

When running `MariaDB` on Kubernetes using KubeDB, failover becomes more seamless. KubeDB supports two types of MariaDB clustering strategies:

* **Standard Replication (Master-Slave):**
  Standard Replication is a mechanism where one server (master) handles both read and write operations,
  while one or more servers (slaves) replicate data asynchronously and serve read-only queries.
  This setup improves data redundancy, availability, and read scalability, with automatic failover and
  load balancing supported through `MariaDB MaxScale Server`.

> note: Writing to a slave replica may result in a binary log (binlog) conflict issue.

* **Galera Cluster (Multi-Master):**
  In this setup, all nodes act as `Master`, capable of handling both read and write operations. Since there’s
  no single point of failure, the system provides synchronous replication and built-in high availability,
  but doesn’t use the traditional failover concept, as all pods are equal.

In the rest of this blog, we’ll focus on how failover works in the `standard replication` mode, and how
KubeDB handles recovery in the event of a node failure.

## Before You Begin

Before proceeding:

* You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to
  communicate with your cluster. If you do not already have a cluster, you can create one by
  using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* Read [mariadb cluster concept](en/clustering/overview.md) to learn about MariaDB
  Cluster.
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.
  Run the following command to prepare your cluster for this tutorial:

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Deploy MariaDB Cluster

The following is an example `MariaDB` object which creates a single-master MariaDB `standard replication` cluster with three members.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: ha-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/clustering/galera-cluster/examples/demo-1.yaml
mariadb.kubedb.com/ha-mariadb created
```

Here,

* `spec.replicas` Defines the number of MariaDB pods (instances) in the cluster.
* `spec.storage` Specifies the StorageClass of PVC dynamically allocated to store data for this database. This storage spec will be passed to the PetSet created by KubeDB operator to run database pods. So, each members will have a pod of this storage configuration. You can specify any StorageClass available in your cluster with appropriate resource requests.
* `spec.topology` Configures the database topology and associated components.
* `spec.topology.maxscale` Specifies the Maxscale proxy server configuration.
* `spec.topology.maxscale.replicas` Defines the number of MaxScale replicas in the petset managed by the KubeDB Operator.
* `spec.topology.maxscale.enableUI` A boolean parameter (e.g. true or false) that controls whether the MaxScale GUI (accessible via the REST API) is enabled for the MaxScale instance.

KubeDB operator watches for `MariaDB` objects using Kubernetes API. When a `MariaDB` object is created, KubeDB operator will create a new PetSet and a Service with the matching MariaDB object name. KubeDB operator will also create a governing service for the PetSet with the name `<mariadb-object-name>-pods`.

You can monitor the status until all pods are ready:

```shell
watch kubectl get mariadb,petset,pods -n demo
```

See the database is ready.

```shell
$ kubectl get mariadb,petset,pods -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/ha-mariadb   11.8.5   Ready    3m27s

NAME                                             AGE
petset.apps.k8s.appscode.com/ha-mariadb      3m20s
petset.apps.k8s.appscode.com/ha-mariadb-mx   3m23s

NAME                      READY   STATUS    RESTARTS   AGE
pod/ha-mariadb-0      2/2     Running   0          3m20s
pod/ha-mariadb-1      2/2     Running   0          3m20s
pod/ha-mariadb-2      2/2     Running   0          3m20s
pod/ha-mariadb-mx-0   1/1     Running   0          3m23s
pod/ha-mariadb-mx-1   1/1     Running   0          3m23s
pod/ha-mariadb-mx-2   1/1     Running   0          3m23s
```

Inspect who is `Master` and who is `slave`.

```shell
# you can inspect the role of the pods 

$ kubectl get pods -n demo --show-labels | grep role
ha-mariadb-0      2/2     Running   0          4m9s    app.kubernetes.io/component=database,app.kubernetes.io/instance=ha-mariadb,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com,apps.kubernetes.io/pod-index=0,controller-revision-hash=ha-mariadb-598cd56869,kubedb.com/role=Master,statefulset.kubernetes.io/pod-name=ha-mariadb-0
ha-mariadb-1      2/2     Running   0          4m9s    app.kubernetes.io/component=database,app.kubernetes.io/instance=ha-mariadb,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com,apps.kubernetes.io/pod-index=1,controller-revision-hash=ha-mariadb-598cd56869,kubedb.com/role=Slave,statefulset.kubernetes.io/pod-name=ha-mariadb-1
ha-mariadb-2      2/2     Running   0          4m9s    app.kubernetes.io/component=database,app.kubernetes.io/instance=ha-mariadb,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com,apps.kubernetes.io/pod-index=2,controller-revision-hash=ha-mariadb-598cd56869,kubedb.com/role=Slave,statefulset.kubernetes.io/pod-name=ha-mariadb-2
```

The pod having `kubedb.com/role=Master` is the `Master` and `kubedb.com/role=Slave` are the slaves.
You can also check it on the cluster status:

```shell
$ kubectl exec -it -n demo svc/ha-mariadb-mx -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬─────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID    │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server1 │ ha-mariadb-0.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-217 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server2 │ ha-mariadb-1.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-217 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼─────────┼────────────────────┤
│ server3 │ ha-mariadb-2.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-217 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴─────────┴────────────────────┘
```

## Verify Pod Reachability and Status

Once the database is in running state we can connect to each of three nodes.
We will use login credentials `MYSQL_ROOT_USERNAME` and `MYSQL_ROOT_PASSWORD` saved as container’s environment variable.

### Create a Test User

Writing to a slave replica can cause binlog conflicts. By default, slave-replicas are read-only, but a
root user (with super privileges) can still make changes. For security, avoid using the root user
in production and create a dedicated user with only the needed permissions instead.

```bash
$ kubectl exec -it -n demo svc/ha-mariadb -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
mysql@ha-mariadb-0:/$ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 443
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpassword';
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]>  GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, SHOW DATABASES ON *.* TO 'testuser'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> quit
Bye
mysql@ha-mariadb-0:/$ exit
exit
```

### Check Connectivity using Test User

```bash
# Master Node
$ kubectl exec -it -n demo svc/ha-mariadb -- bash
```

```mysql
mysql@ha-mariadb-0:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1; 
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye
```

```bash
# Slave Node
$ kubectl exec -it -n demo svc/ha-mariadb-standby -- bash
```

```mysql
mysql@ha-mariadb-1:/ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 94
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

MariaDB [(none)]> quit;
Bye

MariaDB [(none)]> quit;
Bye
```

## Insert Data and Check Availability

In a MariaDB Replication Cluster, Only master member can write, and slave member can read. In this section, we will insert data from master node, and we will see whether we can get the data from every other slave members.
**Check which is the master pod**

```shell
$ kubectl get pods -n demo --show-labels | grep Master | awk '{ print $1 }'
ha-mariadb-0
```

let’s insert data in the master node

```bash
$ kubectl exec -it -n demo ha-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-0:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3459
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE playground;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> CREATE TABLE playground.equipment ( id INT NOT NULL AUTO_INCREMENT, type VARCHAR(50), quant INT, color VARCHAR(25), PRIMARY KEY(id));
Query OK, 0 rows affected (0.032 sec)

MariaDB [(none)]> INSERT INTO playground.equipment (type, quant, color) VALUES ('slide', 2, 'blue');
Query OK, 1 row affected (0.008 sec)

MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

```bash
mysql@ha-mariadb-0:/$ exit
exit
```

You can read data from the slave nodes

```shell
kubectl exec -it -n demo ha-mariadb-1 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-1:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2304
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT * FROM playground.equipment;
+----+-------+-------+-------+
| id | type  | quant | color |
+----+-------+-------+-------+
|  1 | slide |     2 | blue  |
+----+-------+-------+-------+
1 row in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

```shell
mysql@ha-mariadb-1:/$ exit
exit
```

## How Failover Works

Before simulating failover let’s know how it works with the help of maxscale.

MaxScale uses a monitor (like the MariaDB-Monitor plugin) to track the health of database nodes in a replication setup (e.g. MariaDB master-slave). If the `Master` node becomes unavailable—due to a crash, network issue, or maintenance—

MaxScale:

* Detects the Failure: The monitor(ReplicationMonitor) continuously checks node status (using MySQL pings or status variables).
* Selects a New `Master`: It identifies the most suitable replica based on criteria like replication lag or server state.
* Promotes the Replica: MaxScale executes commands to promote the chosen slave-replica to `Master` (e.g. STOP SLAVE; RESET SLAVE ALL;).
* Reconfigures Replicas: Other slave-replicas are updated to replicate from the new `Master`.
* Redirects Traffic: MaxScale’s router (RW-Split-Router) seamlessly directs write queries to the new `Master` and read queries to slave-replicas.

This process happens automatically, typically within seconds, ensuring minimal disruption.
Lets open another terminal and monitor the state of all the pods:

```shell
$ watch -n 2 "kubectl get pods -n demo -o jsonpath='{range .items[*]}{.metadata.name} {.metadata.labels.kubedb\\.com/role}{\"\\n\"}{end}'"
```

You’ll see:

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

### Hands-on Failover Testing

#### Case 1: Delete the current `Master`

Let’s delete the current `Master` pod and see how the role change happens almost immediately.

```shell
$ kubectl delete pods -n demo ha-mariadb-0 
pod "ha-mariadb-0" deleted
```

You’ll see the pods’ status like that:

```
ha-mariadb-0 Down
ha-mariadb-1 Master
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

After few minutes `ha-mariadb-0` will back as `Slave` pod

```shell
ha-mariadb-0 Slave
ha-mariadb-1 Master
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Now we know how failover is done, let’s check if the new `Master` is working.

```shell
$ kubectl exec -it -n demo ha-mariadb-1 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-1:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 652
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| sys                |
+--------------------+
6 rows in set (0.001 sec)

MariaDB [(none)]> CREATE DATABASE playground2;
Query OK, 1 row affected (0.000 sec)
MariaDB [(none)]> exit
Bye
```

```shell
mysql@ha-mariadb-1:/$ exit
exit
```

Lets check if the new Slave(`ha-mariadb-0`) got the updated data from new `Master`, `ha-mariadb-1`.

```shell
$  kubectl exec -it -n demo ha-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-0:/$ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 340
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| playground2        |
| sys                |
+--------------------+
7 rows in set (0.001 sec)

MariaDB [(none)]> exit 
Bye
```

```shell
mysql@ha-mariadb-0:/$ exit
exit
```

#### Case 2: Delete the current `Master` and One slave

```shell
$ kubectl delete pods -n demo ha-mariadb-1 ha-mariadb-2
pod "ha-mariadb-1" deleted
pod "ha-mariadb-2" deleted
```

Again we can see the failover happened pretty quickly.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Down
ha-mariadb-2 Down
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

After 10-30 second, the deleted pods will be back and will have its role and both will have Slave role.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Lets validate the cluster state from new `Master`(`ha-mariadb-0`).

```shell
$ kubectl exec -it -n demo ha-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-0:/$ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 377
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| playground2        |
| sys                |
+--------------------+
7 rows in set (0.000 sec)

MariaDB [(none)]> CREATE DATABASE playground3;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> exit
Bye
```

```shell
mysql@ha-mariadb-0:/$ exit
exit
```

Let’s check whether the Slave nodes, `ha-mariadb-2` gets all the previous data

```shell
kubectl exec -it -n demo ha-mariadb-2 -- bash
Defaulted container "mariadb" out of: mariadb, md-coordinator, mariadb-init (init)
```

```mysql
mysql@ha-mariadb-2:/$ mariadb -utestuser -ptestpassword
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 47
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
| playground         |
| playground2        |
| playground3        |
| sys                |
+--------------------+
8 rows in set (0.001 sec)
```

#### Case3: Delete any of the slave’s

Let’s delete both of the slave nodes.

```shell
kubectl delete pods -n demo ha-mariadb-1 ha-mariadb-2
pod "ha-mariadb-1" deleted
pod "ha-mariadb-2" deleted
```

```shell
ha-mariadb-0 Master
ha-mariadb-1 Down
ha-mariadb-2 Down
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Shortly both of the pods will be back with its role.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

#### Case 4: Delete both `Master` and all slave-replicas

Let’s delete all the pods.

```shell
$ kubectl delete pods -n demo ha-mariadb-0 ha-mariadb-1 ha-mariadb-2
pod "ha-mariadb-0" deleted
pod "ha-mariadb-1" deleted
pod "ha-mariadb-2" deleted
```

```shell
ha-mariadb-0 Down
ha-mariadb-1 Down
ha-mariadb-2 Down
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Within 20-30 second, all of the pod should be back.

```shell
ha-mariadb-0 Master
ha-mariadb-1 Slave
ha-mariadb-2 Slave
ha-mariadb-mx-0
ha-mariadb-mx-1
ha-mariadb-mx-2
```

Lets verify the cluster state now.

```shell
$ kubectl exec -it -n demo svc/ha-mariadb-mx -- bash
Defaulted container "maxscale" out of: maxscale, maxscale-init (init)
bash-4.4$ maxctrl list servers
```

```text
┌─────────┬─────────────────────────────────────────────────────────────┬──────┬─────────────┬─────────────────┬──────────┬────────────────────┐
│ Server  │ Address                                                     │ Port │ Connections │ State           │ GTID     │ Monitor            │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼──────────┼────────────────────┤
│ server1 │ ha-mariadb-0.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Master, Running │ 0-1-3297 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼──────────┼────────────────────┤
│ server2 │ ha-mariadb-1.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-3297 │ ReplicationMonitor │
├─────────┼─────────────────────────────────────────────────────────────┼──────┼─────────────┼─────────────────┼──────────┼────────────────────┤
│ server3 │ ha-mariadb-2.ha-mariadb-pods.demo.svc.cluster.local │ 3306 │ 0           │ Slave, Running  │ 0-1-3297 │ ReplicationMonitor │
└─────────┴─────────────────────────────────────────────────────────────┴──────┴─────────────┴─────────────────┴──────────┴────────────────────┘
```

## CleanUp

For cleaning up what we created in this tutorial follow the following command:

```shell
$ kubectl delete mariadb -n demo ha-mariadb
mariadb.kubedb.com "ha-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

## Next Steps

* Learn about [backup and restore](en/backup/stash/overview.md) MariaDB database using Stash.
* Want to setup MariaDB cluster? Check how to [configure Highly Available MariaDB Cluster](en/clustering/galera-cluster.md)
* Monitor your MariaDB database with KubeDB using [built-in Prometheus](en/monitoring/prometheus-operator.md).
* Detail concepts of [MariaDB object](en/concepts/mariadb.md).
* Use [private Docker registry](en/private-registry/quickstart.md) to deploy MariaDB with KubeDB.
* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: gitops/gitops.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# GitOps MariaDB using KubeDB GitOps Operator

This guide will show you how to use `KubeDB` GitOps operator to create MariaDB database and manage updates using GitOps workflow.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install `KubeDB` operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README). Pass `--set kubedb-crd-manager.installGitOpsCRDs=true` in the kubedb installation process to enable `GitOps` operator.
* You need to install GitOps tools like `ArgoCD` or `FluxCD` and configure with your Git Repository to monitor the Git repository and synchronize the state of the Kubernetes cluster with the desired state defined in Git.

  ```bash
  $ kubectl create ns monitoring
  namespace/monitoring created

  $ kubectl create ns demo
  namespace/demo created
  ```

> Note: YAML files used in this tutorial are stored in [docs/examples/mariadb](https://github.com/kubedb/docs/tree/v2026.7.10/docs/examples/mariadb) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

We are going to use `ArgoCD` in this tutorial. You can install `ArgoCD` in your cluster by following the steps [here](https://argo-cd.readthedocs.io/en/stable/getting_started/). Also, you need to install `argocd` CLI in your local machine. You can install `argocd` CLI by following the steps [here](https://argo-cd.readthedocs.io/en/stable/cli_installation/).

## Creating Apps via CLI

### For Public Repository

```bash
argocd app create kubedb --repo <repo-url> --path kubedb --dest-server https://kubernetes.default.svc --dest-namespace <namespace>
```

### For Private Repository

#### Using HTTPS

```bash
argocd app create kubedb --repo <repo-url> --path kubedb --dest-server https://kubernetes.default.svc --dest-namespace <namespace> --username <username> --password <github-token>
```

#### Using SSH

Registering a Git repository in Argo CD using SSH authentication

```bash
argocd repo add <ssh-repo-url> \
  --ssh-private-key-path <path-to-private-key>
```

Creating an Argo CD Application to deploy resources from the repository into a Kubernetes cluster

```bash
argocd app create <application-name> \
  --repo <repository-url> \
  --path <repository-path> \
  --dest-server <kubernetes-api-server> \
  --dest-namespace <target-namespace>
```

## Create MariaDB Database using GitOps

### Create a MariaDB GitOps CR

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Create a directory like below,

```bash
$ tree .
├── kubedb
    └── MariaDB.yaml
1 directories, 1 files
```

Now commit the changes and push to your Git repository. Your repository is synced with `ArgoCD` and the `MariaDB` CR is created in your cluster.

Our `gitops` operator will create an actual `MariaDB` database CR in the cluster. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get mariaDB.gitops.kubedb.com,mariaDB.kubedb.com -n demo
NAME                                       AGE
mariadb.gitops.kubedb.com/mariadb-gitops   22m

NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    22m
```

List the resources created by `kubedb` operator created for `kubedb.com/v1` MariaDB.

```bash
$ kubectl get petset,pod,secret,service,appbinding -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME                                          AGE
petset.apps.k8s.appscode.com/mariadb-gitops   22m

NAME                   READY   STATUS    RESTARTS   AGE
pod/mariadb-gitops-0   2/2     Running   0          22m
pod/mariadb-gitops-1   2/2     Running   0          22m
pod/mariadb-gitops-2   2/2     Running   0          22m

NAME                         TYPE                       DATA   AGE
secret/mariadb-gitops-auth   kubernetes.io/basic-auth   2      22m

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/mariadb-gitops        ClusterIP   10.43.215.232   <none>        3306/TCP   22m
service/mariadb-gitops-pods   ClusterIP   None            <none>        3306/TCP   22m

NAME                                                TYPE                 VERSION   AGE
appbinding.appcatalog.appscode.com/mariadb-gitops   kubedb.com/mariadb   11.8.5    22m
```

## Update MariaDB Database using GitOps

### Scale MariaDB Database Resources

Before scaling database resouces:

```shell
$ kubectl get pod -n demo mariadb-gitops-0 -o json | jq '.spec.containers[0].resources'
{
  "limits": {
    "memory": "1Gi"
  },
  "requests": {
    "cpu": "500m",
    "memory": "1Gi"
  }
}
```

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Resource Requests and Limits are updated to `600m` CPU and `1.2Gi` Memory. Commit the changes and push to your Git repository. Your repository is synced with `ArgoCD` and the `MariaDB` CR is updated in your cluster.

Now, `gitops` operator will detect the resource changes and create a `MariaDBOpsRequest` to update the `MariaDB` database. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    39m

NAME                                                                     TYPE              STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268   VerticalScaling   Successful   9m17s
```

After Ops Request becomes `Successful`, We can validate the changes by checking the one of the pod,

```bash
$ kubectl get pod -n demo mariadb-gitops-0 -o json | jq '.spec.containers[0].resources'
{
  "limits": {
    "cpu": "600m",
    "memory": "1288490188800m"
  },
  "requests": {
    "cpu": "600m",
    "memory": "1288490188800m"
  }
}
```

### Scale MariaDB Replicas

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Update the `replicas` to `5`. Commit the changes and push to your Git repository. Your repository is synced with `ArgoCD` and the `MariaDB` CR is updated in your cluster.
Now, `gitops` operator will detect the replica changes and create a `HorizontalScaling` MariaDBOpsRequest to update the `MariaDB` database replicas. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    107m

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   63m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   76m
```

After Ops Request becomes `Successful`, We can validate the changes by checking the number of pods,

```bash
$ kubectl get pod -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME               READY   STATUS    RESTARTS   AGE
mariadb-gitops-0   2/2     Running   0          76m
mariadb-gitops-1   2/2     Running   0          75m
mariadb-gitops-2   2/2     Running   0          73m
mariadb-gitops-3   2/2     Running   0          63m
mariadb-gitops-4   2/2     Running   0          62m
```

We can also scale down the replicas by updating the `replicas` fields.

### Expand MariaDB Volume

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
```

Update the `storage.resources.requests.storage` to `2Gi`. Commit the changes and push to your Git repository. Your repository is synced with `ArgoCD` and the `MariaDB` CR is updated in your cluster.

Now, `gitops` operator will detect the volume changes and create a `VolumeExpansion` MariaDBOpsRequest to update the `MariaDB` database volume. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    111m

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   68m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   81m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   115s
```

After Ops Request becomes `Successful`, We can validate the changes by checking the pvc size,

```bash
$ kubectl get pvc -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
data-mariadb-gitops-0   Bound    pvc-f1a49c53-d095-43a7-b62f-e91a5a9f5496   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-1   Bound    pvc-79d99636-e0d7-413f-a6a6-559e908ed817   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-2   Bound    pvc-f66ccf56-63b6-4ac6-a7f9-09f573466266   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-3   Bound    pvc-b7744652-611a-4c10-a06f-c93f030fb90f   2Gi        RWO            longhorn       <unset>                 72m
data-mariadb-gitops-4   Bound    pvc-dee1c10d-0456-4935-9306-0d86c3db54d0   2Gi        RWO            longhorn       <unset>                 71m
```

## Reconfigure MariaDB

At first, we will create a secret containing `user.conf` file with required configuration settings.
To know more about this configuration file, check [here](en/reconfigure/overview.md)

```yaml
apiVersion: v1
stringData:
  user.cnf: |
    [mysqld]
    max_connections = 200
    read_buffer_size = 1048576    
kind: Secret
metadata:
  name: md-configuration
  namespace: demo
type: Opaque
```

Now, we will add this file to `kubedb/md-configuration.yaml`.

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ └── mariadb.yaml
1 directories, 2 files
```

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
```

Commit the changes and push to your Git repository. Your repository is synced with `ArgoCD`, the reconfiguration file is created the `MariaDB` CR is updated in your cluster.

Now, `gitops` operator will detect the configuration changes and create a `Reconfigure` MariaDBOpsRequest to update the `MariaDB` database configuration. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    17h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   17h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

### Rotate MariaDB Auth

To do that, create a `kubernetes.io/basic-auth` type k8s secret with the new username and password.

We will do that using gitops, create the file `kubedb/md-auth.yaml` with the following content,

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mdauth
  namespace: demo
type: kubernetes.io/basic-auth
stringData:
  username: root
  password: md-secret
```

Let’s add that to our `kubedb/md-auth.yaml` file. File structure will look like this,

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ ├── md-auth.yaml
│ └── MariaDB.yaml
1 directories, 3 files
```

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
```

Change the `authSecret` field to `mdauth`. Commit the changes and push to your Git repository. Your repository has been successfully synchronized with ArgoCD. The `MariaDB` CR has been updated, and the authentication file has been created in the cluster.

Now, `gitops` operator will detect the auth changes and create a `RotateAuth` MariaDBOpsRequest to update the `MariaDB` database auth. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   12m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

### TLS configuration

We can add, rotate or remove TLS configuration using `gitops`.

Now, we are going to create an example `Issuer` that will be used throughout the duration of this tutorial. Alternatively, you can follow this [cert-manager tutorial](https://cert-manager.io/docs/configuration/ca/) to create your own `Issuer`. By following the below steps, we are going to create our desired issuer,

* Start off by generating our ca-certificates using openssl,

```bash
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./ca.key -out ./ca.crt -subj "/CN=mariadb/O=kubedb"
Generating a RSA private key
...........................................................................+++++
........................................................................................................+++++
writing new private key to './ca.key'
```

* create a secret using the certificate files we have just generated,

```bash
$ kubectl create secret tls md-ca \
  --cert=ca.crt \
  --key=ca.key \
  -n demo
```

Now, we are going to create an `Issuer` using the `md-ca` secret that hols the ca-certificate we have just created. Below is the YAML of the `Issuer` cr that we are going to create,

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: md-issuer
  namespace: demo
spec:
  ca:
    secretName: md-ca
```

Let’s create the `Issuer` cr we have shown above,

```bash
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

Let’s add that to our `kubedb/md-issuer.yaml` file. File structure will look like this,

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ ├── md-auth.yaml
│ ├── md-secret.yaml
│ ├── md-issuer.yaml
│ └── MariaDB.yaml
1 directories, 5 files
```

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
```

Add `requireSSL` as `true` and `tls` fields in the spec. Commit the changes and push to your Git repository. Your repository has been successfully synchronized with ArgoCD. The `MariaDB` CR has been updated, and both the `issuer` and the corresponding `secret` have been created in the cluster.

Now, `gitops` operator will detect the tls changes and create a `ReconfigureTLS` MariaDBOpsRequest to update the `MariaDB` database tls. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$  kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   8m20s
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   35m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

> We can also rotate the certificates updating `.spec.tls.certificates` field. Also you can remove the `.spec.tls` field to remove tls for MariaDB.

### Update Version

List MariaDB versions using `kubectl get MariaDBversion` and choose desired version that is compatible for upgrade from current version. Check the version constraints and ops request [here](en/update-version/overview.md).

Let’s choose `12.1.2` in this example.

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
```

Update the `version` field to `12.1.2`. Commit the changes and push to your Git repository. Your repository is synced with `ArgoCD` and the `MariaDB` CR is updated in your cluster.

Now, `gitops` operator will detect the version changes and create a `VersionUpdate` MariaDBOpsRequest to update the `MariaDB` database version. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   12.1.2    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   24m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   51m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-versionupdate-ksli15       UpdateVersion       Successful   10m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   19h
```

Now, we are going to verify whether the `MariaDB`, `PetSet` and it’s `Pod` have updated with new image. Let’s check,

```bash
$ kubectl get MariaDB -n demo mariadb-gitops -o=jsonpath='{.spec.version}{"\n"}'
12.1.2
$ kubectl get petset -n demo mariadb-gitops -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
ghcr.io/appscode-images/mariadb:12.1.2-noble@sha256:843852d8651b3f321896a4a91f8118605d988d70703e520927c8d2c9313aded4
$ kubectl get pod -n demo mariadb-gitops-0 -o=jsonpath='{.spec.containers[0].image}{"\n"}'
ghcr.io/appscode-images/mariadb:12.1.2-noble@sha256:843852d8651b3f321896a4a91f8118605d988d70703e520927c8d2c9313aded4
```

### Enable Monitoring

If you already don’t have a Prometheus server running, deploy one following tutorial from [here](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/operator/README.md#deploy-prometheus-server).

Update the `MariaDB.yaml` with the following,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
  monitor:
    agent: prometheus.io/operator
    prometheus:
      serviceMonitor:
        labels:
          release: prometheus
        interval: 10s
```

Add `monitor` field in the spec. Commit the changes and push to your Git repository. Your repository is synced with `ArgoCD` and the `MariaDB` CR is updated in your cluster.

Now, `gitops` operator will detect the monitoring changes and create a `Restart` MariaDBOpsRequest to add the `MariaDB` database monitoring. List the resources created by `gitops` operator in the `demo` namespace.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   12.1.2    Ready    19h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   40m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-restart-e7rv89             Restart             Successful   8m26s
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   67m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-versionupdate-ksli15       UpdateVersion       Successful   26m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   19h
```

Verify the monitoring is enabled by checking the prometheus targets.

## Next Steps

* Learn MariaDB Scaling
  + [Horizontal Scaling](en/scaling/horizontal-scaling/overview.md)
  + [Vertical Scaling](en/scaling/vertical-scaling/overview.md)
* Learn Version Update Ops Request and Constraints [here](en/update-version/overview.md)
* Monitor your MariaDBQL database with KubeDB using [built-in Prometheus](en/monitoring/prometheus-operator.md).
* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: gitops/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# GitOps Overview for MariaDB

This guide will give you an overview of how KubeDB `gitops` operator works with MariaDB databases using the `gitops.kubedb.com/v1alpha1` API. It will help you understand the GitOps workflow for
managing MariaDB databases in Kubernetes.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## Workflow GitOps with MariaDB

The following diagram shows how the `KubeDB` GitOps Operator used to sync with your database. Open the image in a new tab to see the enlarged version.

![GitOps Flow](images/gitops_overview_gitops.jpg)

Fig: GitOps process of MariaDB

1. **Define GitOps MariaDB**: Create Custom Resource (CR) of kind `MariaDB` using the `gitops.kubedb.com/v1alpha1` API.
2. **Store in Git**: Push the CR to a Git repository.
3. **Automated Deployment**: Use a GitOps tool (like `ArgoCD` or `FluxCD`) to monitor the Git repository and synchronize the state of the Kubernetes cluster with the desired state defined in Git.
4. **Create Database**: The GitOps operator creates a corresponding KubeDB MariaDB CR in the Kubernetes cluster to deploy the database.
5. **Handle Updates**: When you update the MariaDBGitOps CR, the operator generates an Ops Request to safely apply the update(e.g. `VerticalScaling`, `HorizontalScaling`, `VolumeExapnsion`, `Reconfigure`, `RotateAuth`, `ReconfigureTLS`, `VersionUpdate`, ans `Restart`.

This flow makes managing MariaDB databases efficient, reliable, and fully integrated with GitOps practices.

In the next doc, we are going to show a step by step guide on running MariaDB using GitOps.

<!-- PAGE_START: initialization/git-sync.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Initialization MariaDB from a Git Repository

This guide demonstrates how to use KubeDB to initialize a MariaDB database with initialization scripts (.sql, .sh, and/or .sql.gz) stored in a public or private Git repository.
To fetch the repository contents, KubeDB uses a sidecar container called [git-sync](https://github.com/kubernetes/git-sync).
In this example, we will initialize MariaDB using a `.sql` script from the GitHub repository [kubedb/mysql-init-scripts](https://github.com/kubedb/mysql-init-scripts).

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB operator in your cluster by following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## From Public Git Repository

KubeDB implements a `MariaDB` Custom Resource Definition (CRD) to define the specification of a MariaDB database.
To initialize the database from a public Git repository, you need to specify the required arguments for the `git-sync` sidecar container within the MariaDB resource specification.
The following YAML manifest shows an example `MariaDB` object configured with `git-sync`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       - --repo=https://github.com/kubedb/mysql-init-scripts
       - --link=current
       - --root=/root
       # terminate after one successful sync
       - --one-time 
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

```bash
kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/initialization/git-sync-public.yaml
mariadb.kubedb.com/sample-mariadb created
```

The `git-sync` container has two required flags:

* `--repo` – specifies the remote Git repository to sync.
* `--root` – specifies the working directory where the repository will be cloned.

Here, the value of the `--link` argument must match the value of `spec.init.script.scriptPath`.
The `--link` argument creates a symlink that always points to the latest synced data.

> To know more about `git-sync` configuration visit this [link](https://github.com/kubernetes/git-sync).

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5   Ready    5m
```

Next, we will connect to the MariaDB database and verify the data inserted from the `*.sql` script stored in the Git repository.

```bash
kubectl exec -it -n demo sample-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, mariadb-init (init), git-sync (init)
```

```mysql
mysql@sample-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 6
Server version: 10.5.23-MariaDB-1:11.8.5+maria~ubu2004 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mysql]> select * from kubedb_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.000 sec)

MariaDB [mysql]> select * from demo_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.000 sec)
```

## From Private Git Repository

### 1. Using SSH Key

Git-sync supports using SSH protocol for pulling git content.

First, Obtain the host keys for your git server:

```bash
$ ssh-keyscan $YOUR_GIT_HOST > /tmp/known_hosts
```

> `$YOUR_GIT_HOST` refers to the hostname of your Git server.  
> For example, if you are using GitHub, set the variable as follows:
>
> ```bash
> export YOUR_GIT_HOST=github.com
> ```

Use the `kubectl create secret` command to create a secret from your local SSH key and known hosts file.
This secret will be used by git-sync to authenticate with the Git repository.

```bash
$ kubectl create secret generic -n demo git-creds \
    --from-file=ssh=$HOME/.ssh/id_rsa \
    --from-file=known_hosts=/tmp/known_hosts
```

The following YAML manifest provides an example of a `MariaDB` resource configured to use `git-sync` with a private Git repository:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       # update with your private repository    
       - --repo=<your-ssh-repo-url>
       - --link=current
       - --root=/root
       # terminate after one successful sync
       - --one-time 
       authSecret:
         name: git-creds
       # run as git sync user 
       securityContext:
         runAsUser: 65533
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Here,

* `.spec.init.git.securityContext.runAsUser: 65533` ensure the container runs as the dedicated non-root `git-sync` user.
* `.spec.init.git.authSecret` specifies the secret containing the `SSH` key.

Once the database reaches the `Ready` state, you can verify the data using the method described above.

### 2. Using Username and Personal Access Token(PAT)

First, create a `Personal Access Token (PAT)` on your Git host server with the required permissions to access the repository.
Then create a Kubernetes secret using the `Personal Access Token (PAT)`:

```bash
$ kubectl create secret generic -n demo git-pat \
    --from-literal=github-pat=<ghp_yourpersonalaccesstoken>
```

Now, create a `MariaDB` resource that references the secret created above.
The following YAML manifest shows an example:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       # update with your private repository    
       - --repo=<your-https-repo-url>
       - --link=current
       - --root=/root
       - --credential={"url":"https://github.com","username":"<username>","password-file":"/etc/git-secret/github-pat"}
       # terminate after one successful sync
       - --one-time 
       authSecret:
         name: git-pat
       # run as git sync user 
       securityContext:
         runAsUser: 65533
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Once the database reaches the `Ready` state, you can verify the data using the method described above.

## CleanUp

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete secret -n demo git-pat git-creds
$ kubectl delete ns demo
```

<!-- PAGE_START: initialization/using-script.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Initialize MariaDB using Script

This tutorial will show you how to use KubeDB to initialize a MariaDB database with \*.sql, \*.sh and/or \*.sql.gz script.
In this tutorial we will use .sql script stored in GitHub repository [kubedb/mysql-init-scripts](https://github.com/kubedb/mysql-init-scripts).

> Note: The yaml files that are used in this tutorial are stored [here](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/initialization/using-script/example) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Prepare Initialization Scripts

MariaDB supports initialization with `.sh`, `.sql` and `.sql.gz` files. In this tutorial, we will use `init.sql` script from [mysql-init-scripts](https://github.com/kubedb/mysql-init-scripts) git repository to create a TABLE `kubedb_table` in `mysql` database.

We will use a ConfigMap as script source. You can use any Kubernetes supported [volume](https://kubernetes.io/docs/concepts/storage/volumes) as script source.

At first, we will create a ConfigMap from `init.sql` file. Then, we will provide this ConfigMap as script source in `init.script` of MariaDB crd spec.

Let’s create a ConfigMap with initialization script,

```bash
$ kubectl create configmap -n demo md-init-script \
--from-literal=init.sql="$(curl -fsSL https://github.com/kubedb/mysql-init-scripts/raw/master/init.sql)"
configmap/md-init-script created
```

## Create a MariaDB database with Init-Script

Below is the `MariaDB` object created in this tutorial.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  init:
    script:
      configMap:
        name: md-init-script
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/initialization/using-script/example/demo-1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Here,

* `spec.init.script` specifies a script source used to initialize the database before database server starts. The scripts will be executed alphabatically. In this tutorial, a sample .sql script from the git repository `https://github.com/kubedb/mysql-init-scripts.git` is used to create a test database. You can use other [volume sources](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes) instead of `ConfigMap`. The \*.sql, \*sql.gz and/or \*.sh sripts that are stored inside the root folder will be executed alphabatically. The scripts inside child folders will be skipped.

KubeDB operator watches for `MariaDB` objects using Kubernetes api. When a `MariaDB` object is created, KubeDB operator will create a new PetSet and a Service with the matching MariaDB object name. KubeDB operator will also create a governing service for PetSets with the name `kubedb`, if one is not already present. No MariaDB specific RBAC roles are required for [RBAC enabled clusters](https://kubedb.com/docs/v2026.7.10/setup/README#using-yaml).

```bash
$ kubectl get mariadb -n demo sample-mariadb -oyaml
```

```text
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  ...
  name: sample-mariadb
  namespace: demo
  ...
spec:
  authSecret:
    name: sample-mariadb-auth
  init:
    initialized: true
    script:
      configMap:
        name: md-init-script
  ...
  replicas: 1
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
    storageClassName: standard
  storageType: Durable
  deletionPolicy: WipeOut
  version: 12.1.2
status:
  ...
  phase: Ready
```

KubeDB operator sets the `status.phase` to `Ready` once the database is successfully created.

Now, we will connect to this database and check the data inserted by the initlization script.

```bash
# Connecting to the database
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 40
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

# Showing the inserted `kubedb_table`
Database changed
MariaDB [mysql]> select * from  kubedb_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.001 sec)

MariaDB [mysql]> quit;
Bye
```

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: migration/databasemigration.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Database Migration

This guide will show you how to use `KubeDB` Migration to migrate an existing `MariaDB` database — such as one running on AWS RDS or any external instance — entirely into a KubeDB-managed `MariaDB` with minimal downtime.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install `KubeDB` operator with the kubedb-courier operator enabled in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/operatormanual/migration/).
* The source `MariaDB` instance must be network-reachable from within your Kubernetes cluster.
* The source `MariaDB` instance must have binary logging enabled with `binlog_format=ROW` and `binlog_row_image=FULL`. The database user provided for migration must have replication privileges.
* You should be familiar with the following `KubeDB` concepts:

  + [AppBinding](en/concepts/appbinding.md)
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBMigration](en/concepts/migrator.md)
  + [Migration](https://kubedb.com/docs/v2026.7.10/operatormanual/migration/)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Prepare Source Database

We will use an **AWS RDS MariaDB** instance as the source. Connect to it as the admin user to verify the prerequisites and set up the migration user and test data.

**Configuring your source instance.**

**Self-hosted MariaDB**

Add the following to your `my.cnf` and restart MariaDB:

```ini
[mysqld]
log_bin          = mysql-bin
binlog_format    = ROW
binlog_row_image = FULL
```

Then grant the required privileges to the migration user:

```sql
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '<migration-user>'@'%';
FLUSH PRIVILEGES;
```

**AWS RDS MariaDB**

Enable [Automated Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html) on the instance (this activates binary logging). Set `binlog_format = ROW` and `binlog_row_image = FULL` in an RDS Parameter Group. Then grant replication privileges via SQL as shown above.

**Azure Database for MariaDB**

Binary logging is enabled automatically when backups are on. Set `binlog_format` and `binlog_row_image` under **Server Parameters** in the [Azure Portal](https://learn.microsoft.com/en-us/azure/mariadb/concepts-read-replicas). Then grant replication privileges via SQL as shown above.

See the official [MariaDB Binary Log](https://mariadb.com/kb/en/binary-log/) docs for more details.

### Verify prerequisites

```bash
$ mysql -h <rds-endpoint>.rds.amazonaws.com -u admin -p
```

```sql
-- Verify binary logging is enabled
SHOW VARIABLES LIKE 'log_bin';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
+---------------+-------+

-- Verify binlog format and row image
SHOW VARIABLES LIKE 'binlog_format';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+

SHOW VARIABLES LIKE 'binlog_row_image';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| binlog_row_image | FULL  |
+------------------+-------+
```

### Create a dedicated migration user

Create a dedicated user with the minimum required privileges:

```sql
CREATE USER 'migrator'@'%' IDENTIFIED BY '<password>';

-- For CDC (binlog streaming)
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'migrator'@'%';

-- For schema migration (mariadb-dump) and snapshot
GRANT SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, EVENT, LOCK TABLES, PROCESS ON *.* TO 'migrator'@'%';

FLUSH PRIVILEGES;

-- Verify
SHOW GRANTS FOR 'migrator'@'%';
```

The `migrator` user is referenced in the Kubernetes secret and AppBinding for the rest of this guide.

### Create table and seed data

```sql
CREATE DATABASE shop;
USE shop;

CREATE TABLE orders (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  product       VARCHAR(100) NOT NULL,
  quantity      INT          NOT NULL DEFAULT 1,
  status        VARCHAR(20)  NOT NULL DEFAULT 'pending',
  created_at    TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO orders (customer_name, product, quantity, status) VALUES
  ('Alice', 'Laptop',     1, 'shipped'),
  ('Bob',   'Headphones', 2, 'pending'),
  ('Carol', 'Keyboard',   3, 'delivered');

SELECT * FROM orders;
+----+---------------+------------+----------+-----------+---------------------+
| id | customer_name | product    | quantity | status    | created_at          |
+----+---------------+------------+----------+-----------+---------------------+
|  1 | Alice         | Laptop     |        1 | shipped   | 2026-06-29 08:00:00 |
|  2 | Bob           | Headphones |        2 | pending   | 2026-06-29 08:00:01 |
|  3 | Carol         | Keyboard   |        3 | delivered | 2026-06-29 08:00:02 |
+----+---------------+------------+----------+-----------+---------------------+
3 rows in set (0.00 sec)
```

## Prepare Source Connection Information

First, create an authentication secret using the `migrator` user credentials:

```bash
$ kubectl create secret generic source-mariadb-auth -n demo \
                --type=kubernetes.io/basic-auth \
                --from-literal=username=migrator \
                --from-literal=password=<password>
```

If your database has TLS enabled, create a secret with the CA certificate:

```bash
kubectl create secret generic ca-secret \
  --from-file=ca.crt=$CERT_PATH/ca.crt \
  --namespace=demo
```

> **Note:** For mTLS, also include the client certificate and key by appending  
> `--from-file=tls.crt=$CERT_PATH/tls.crt`  
> `--from-file=tls.key=$CERT_PATH/tls.key`  
> to the command above.

Now create an `AppBinding` with the necessary information. The kubedb-courier operator reads the source MariaDB connection information from this AppBinding CR. Use the following YAML to create your AppBinding:

```yaml
apiVersion: appcatalog.appscode.com/v1alpha1
kind: AppBinding
metadata:
  name: source-mariadb
  namespace: demo
spec:
  type: mariadb
  version: "10.5.23"
  clientConfig:
    url: "mariadb://<rds-endpoint>.rds.amazonaws.com:3306"
  secret:
    name: source-mariadb-auth
  tlsSecret: # omit if TLS is disabled
    name: ca-secret
```

Here,

* `spec.clientConfig.url` is the connection URL of the source MariaDB instance.
* `spec.secret.name` is the reference to the secret we created earlier, containing the MariaDB authentication information.

> For a `KubeDB`-managed database, an `AppBinding` is created by default. So there is no need to create one for the target database.

## Create Target MariaDB Database

KubeDB implements a `MariaDB` CRD to define the specification of a MariaDB database. Follow the `MariaDB` object to create the target database.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: target-mariadb
  namespace: demo
spec:
  version: "10.5.23"
  storageType: Durable
  storage:
    storageClassName: "local-path"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 20Gi
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/migration/target-mariadb.yaml
mariadb.kubedb.com/target-mariadb created
```

> Note: Adjust the `resources.requests.storage` based on the source database size.

Wait until `target-mariadb` has status `Ready`.

## Apply MariaDBMigration CR

To migrate the database we have to create a `MariaDBMigration` CR. Below is the YAML of the `MariaDBMigration` CR that we are going to create:

```yaml
apiVersion: courier.kubedb.com/v1alpha1
kind: MariaDBMigration
metadata:
  name: mariadb-migrate
  namespace: demo
spec:
  source:
    connectionInfo:
      appBinding:
        name: source-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
    schema:
      enabled: true
      database:
        - shop
      excludeDatabase: []
    snapshot:
      enabled: true
      pipeline:
        workers: 3
        sinkers: 4
        buffer: 12
        write_batch_size: 200
        read_batch_size: 1000
    streaming:
      enabled: true

  target:
    connectionInfo:
      appBinding:
        name: target-mariadb
        namespace: demo
      dbName: "mysql"
      maxConnections: 100
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/migration/mariadb-migrate.yaml
mariadbmigration.courier.kubedb.com/mariadb-migrate created
```

Here we scope the migration to the `shop` database (`schema.database: [shop]`), enable both the bulk snapshot and CDC streaming phases, and cap connections at 100 on each side. For a full description of every field, see the [MariaDBMigration CRD reference](en/concepts/migrator.md).

## Watch Migration Progress

Let’s wait for the `LAG` to reach near zero. Run the following command to watch `MariaDBMigration` CR:

```bash
Every 2.0s: kubectl get mariadbmigrations -n demo

NAME              PHASE     DBTYPE    STAGE       LAG   PROGRESS   AGE
mariadb-migrate   Running   mariadb   Streaming   0B    100%       4h36m
```

### Verify initial snapshot on target

Once the migration reaches the `Streaming` stage, exec into the KubeDB target pod and confirm all seed rows were copied over:

```bash
$ kubectl exec -it -n demo target-mariadb-0 -- mysql -u root -p<root-password>
```

```sql
USE shop;
SELECT * FROM orders;
+----+---------------+------------+----------+-----------+---------------------+
| id | customer_name | product    | quantity | status    | created_at          |
+----+---------------+------------+----------+-----------+---------------------+
|  1 | Alice         | Laptop     |        1 | shipped   | 2026-06-29 08:00:00 |
|  2 | Bob           | Headphones |        2 | pending   | 2026-06-29 08:00:01 |
|  3 | Carol         | Keyboard   |        3 | delivered | 2026-06-29 08:00:02 |
+----+---------------+------------+----------+-----------+---------------------+
3 rows in set (0.00 sec)
```

### Test live CDC streaming

With the migration still running, connect to the **source RDS** instance and run some DML:

```bash
$ mysql -h <rds-endpoint>.rds.amazonaws.com -u migrator -p
```

```sql
-- Insert a new order
INSERT INTO shop.orders (customer_name, product, quantity, status)
VALUES ('Dave', 'Mouse', 1, 'pending');

-- Mark Bob's headphones as delivered
UPDATE shop.orders SET status = 'delivered' WHERE id = 2;

-- Remove the already-shipped laptop order
DELETE FROM shop.orders WHERE id = 1;
```

Wait a few seconds for the binlog events to propagate, then re-query the **target**:

```sql
USE shop;
SELECT * FROM orders;
+----+---------------+------------+----------+-----------+---------------------+
| id | customer_name | product    | quantity | status    | created_at          |
+----+---------------+------------+----------+-----------+---------------------+
|  2 | Bob           | Headphones |        2 | delivered | 2026-06-29 08:00:01 |
|  3 | Carol         | Keyboard   |        3 | delivered | 2026-06-29 08:00:02 |
|  4 | Dave          | Mouse      |        1 | pending   | 2026-06-29 08:10:00 |
+----+---------------+------------+----------+-----------+---------------------+
3 rows in set (0.00 sec)
```

The INSERT, UPDATE, and DELETE are all reflected on the target — CDC streaming is working correctly.

## Cutover

Once the `LAG` drops to near zero, stop all writes to the source database. Wait until the `LAG` reaches exactly zero — at that point both databases are fully in sync.

Now delete the `MariaDBMigration` CR to stop the migration process:

```bash
$ kubectl delete mariadbmigrations -n demo mariadb-migrate
mariadbmigration.courier.kubedb.com "mariadb-migrate" deleted
```

Finally, update your application’s connection string to point to the target KubeDB-managed `MariaDB` database. The migration is complete.

<!-- PAGE_START: monitoring/builtin-prometheus.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Monitoring MariaDB with builtin Prometheus

This tutorial will show you how to monitor MariaDB database using builtin [Prometheus](https://github.com/prometheus/prometheus) scraper.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* If you are not familiar with how to configure Prometheus to scrape metrics from various Kubernetes resources, please read the tutorial from [here](https://github.com/appscode/third-party-tools/tree/master/monitoring/prometheus/builtin).
* To learn how Prometheus monitoring works with KubeDB in general, please visit [here](en/monitoring/overview.md).
* To keep Prometheus resources isolated, we are going to use a separate namespace called `monitoring` to deploy respective monitoring resources. We are going to deploy database in `demo` namespace.

  ```bash
  $ kubectl create ns monitoring
  namespace/monitoring created

  $ kubectl create ns demo
  namespace/demo created
  ```

> Note: YAML files used in this tutorial are stored in [docs/guides/mariadb/monitoring/builtin-prometheus/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/monitoring/builtin-prometheus/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Deploy MariaDB with Monitoring Enabled

At first, let’s deploy an MariaDB database with monitoring enabled. Below is the MariaDB object that we are going to create.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: builtin-prom-md
  namespace: demo
spec:
  version: "12.1.2"
  deletionPolicy: WipeOut
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  monitor:
    agent: prometheus.io/builtin
```

Here,

* `spec.monitor.agent: prometheus.io/builtin` specifies that we are going to monitor this server using builtin Prometheus scraper.

Let’s create the MariaDB crd we have shown above.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/monitoring/builtin-prometheus/examples/builtin-prom-md.yaml
mariadb.kubedb.com/builtin-prom-md created
```

Now, wait for the database to go into `Running` state.

```bash
$ kubectl get mariadb -n demo builtin-prom-md
NAME              VERSION   STATUS   AGE
builtin-prom-md   11.8.5    Ready    76s
```

KubeDB will create a separate stats service with name `{MariaDB crd name}-stats` for monitoring purpose.

```bash
$ kubectl get svc -n demo --selector="app.kubernetes.io/instance=builtin-prom-md"
NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
builtin-prom-md         ClusterIP   10.106.32.194   <none>        3306/TCP    2m3s
builtin-prom-md-pods    ClusterIP   None            <none>        3306/TCP    2m3s
builtin-prom-md-stats   ClusterIP   10.109.106.92   <none>        56790/TCP   2m2s
```

Here, `builtin-prom-md-stats` service has been created for monitoring purpose. Let’s describe the service.

```bash
$ kubectl describe svc -n demo builtin-prom-md-stats
Name:              builtin-prom-md-stats
Namespace:         demo
Labels:            app.kubernetes.io/instance=builtin-prom-md
                   app.kubernetes.io/managed-by=kubedb.com
                   app.kubernetes.io/name=mariadbs.kubedb.com
                   kubedb.com/role=stats
Annotations:       monitoring.appscode.com/agent: prometheus.io/builtin
                   prometheus.io/path: /metrics
                   prometheus.io/port: 56790
                   prometheus.io/scrape: true
Selector:          app.kubernetes.io/instance=builtin-prom-md,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com
Type:              ClusterIP
IP:                10.109.106.92
Port:              metrics  56790/TCP
TargetPort:        metrics/TCP
Endpoints:         10.244.0.34:56790
Session Affinity:  None
Events:            <none>
```

You can see that the service contains following annotations.

```bash
prometheus.io/path: /metrics
prometheus.io/port: 56790
prometheus.io/scrape: true
```

The Prometheus server will discover the service endpoint using these specifications and will scrape metrics from the exporter.

## Configure Prometheus Server

Now, we have to configure a Prometheus scraping job to scrape the metrics using this service. We are going to configure scraping job similar to this [kubernetes-service-endpoints](https://github.com/appscode/third-party-tools/tree/master/monitoring/prometheus/builtin#kubernetes-service-endpoints) job that scrapes metrics from endpoints of a service.

Let’s configure a Prometheus scraping job to collect metrics from this service.

```yaml
- job_name: 'kubedb-databases'
  honor_labels: true
  scheme: http
  kubernetes_sd_configs:
  - role: endpoints
  # by default Prometheus server select all Kubernetes services as possible target.
  # relabel_config is used to filter only desired endpoints
  relabel_configs:
  # keep only those services that has "prometheus.io/scrape","prometheus.io/path" and "prometheus.io/port" annotations
  - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape, __meta_kubernetes_service_annotation_prometheus_io_port]
    separator: ;
    regex: true;(.*)
    action: keep
  # currently KubeDB supported databases uses only "http" scheme to export metrics. so, drop any service that uses "https" scheme.
  - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
    action: drop
    regex: https
  # only keep the stats services created by KubeDB for monitoring purpose which has "-stats" suffix
  - source_labels: [__meta_kubernetes_service_name]
    separator: ;
    regex: (.*-stats)
    action: keep
  # service created by KubeDB will have "app.kubernetes.io/name" and "app.kubernetes.io/instance" annotations. keep only those services that have these annotations.
  - source_labels: [__meta_kubernetes_service_label_app_kubernetes_io_name]
    separator: ;
    regex: (.*)
    action: keep
  # read the metric path from "prometheus.io/path: <path>" annotation
  - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
    action: replace
    target_label: __metrics_path__
    regex: (.+)
  # read the port from "prometheus.io/port: <port>" annotation and update scraping address accordingly
  - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
    action: replace
    target_label: __address__
    regex: ([^:]+)(?::\d+)?;(\d+)
    replacement: $1:$2
  # add service namespace as label to the scraped metrics
  - source_labels: [__meta_kubernetes_namespace]
    separator: ;
    regex: (.*)
    target_label: namespace
    replacement: $1
    action: replace
  # add service name as a label to the scraped metrics
  - source_labels: [__meta_kubernetes_service_name]
    separator: ;
    regex: (.*)
    target_label: service
    replacement: $1
    action: replace
  # add stats service's labels to the scraped metrics
  - action: labelmap
    regex: __meta_kubernetes_service_label_(.+)
```

### Configure Existing Prometheus Server

If you already have a Prometheus server running, you have to add above scraping job in the `ConfigMap` used to configure the Prometheus server. Then, you have to restart it for the updated configuration to take effect.

> If you don’t use a persistent volume for Prometheus storage, you will lose your previously scraped data on restart.

### Deploy New Prometheus Server

If you don’t have any existing Prometheus server running, you have to deploy one. In this section, we are going to deploy a Prometheus server in `monitoring` namespace to collect metrics using this stats service.

**Create ConfigMap:**

At first, create a ConfigMap with the scraping configuration. Below, the YAML of the ConfigMap that we are going to create in this tutorial.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  labels:
    app: prometheus-demo
  namespace: monitoring
data:
  prometheus.yml: |-
    global:
      scrape_interval: 5s
      evaluation_interval: 5s
    scrape_configs:
    - job_name: 'kubedb-databases'
      honor_labels: true
      scheme: http
      kubernetes_sd_configs:
      - role: endpoints
      # by default Prometheus server select all Kubernetes services as possible target.
      # relabel_config is used to filter only desired endpoints
      relabel_configs:
      # keep only those services that has "prometheus.io/scrape","prometheus.io/path" and "prometheus.io/port" anootations
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape, __meta_kubernetes_service_annotation_prometheus_io_port]
        separator: ;
        regex: true;(.*)
        action: keep
      # currently KubeDB supported databases uses only "http" scheme to export metrics. so, drop any service that uses "https" scheme.
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
        action: drop
        regex: https
      # only keep the stats services created by KubeDB for monitoring purpose which has "-stats" suffix
      - source_labels: [__meta_kubernetes_service_name]
        separator: ;
        regex: (.*-stats)
        action: keep
      # service created by KubeDB will have "app.kubernetes.io/name" and "app.kubernetes.io/instance" annotations. keep only those services that have these annotations.
      - source_labels: [__meta_kubernetes_service_label_app_kubernetes_io_name]
        separator: ;
        regex: (.*)
        action: keep
      # read the metric path from "prometheus.io/path: <path>" annotation
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      # read the port from "prometheus.io/port: <port>" annotation and update scraping address accordingly
      - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
      # add service namespace as label to the scraped metrics
      - source_labels: [__meta_kubernetes_namespace]
        separator: ;
        regex: (.*)
        target_label: namespace
        replacement: $1
        action: replace
      # add service name as a label to the scraped metrics
      - source_labels: [__meta_kubernetes_service_name]
        separator: ;
        regex: (.*)
        target_label: service
        replacement: $1
        action: replace
      # add stats service's labels to the scraped metrics
      - action: labelmap
        regex: __meta_kubernetes_service_label_(.+)
```

Let’s create above `ConfigMap`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/monitoring/builtin-prometheus/examples/prom-config.yaml
configmap/prometheus-config created
```

**Create RBAC:**

If you are using an RBAC enabled cluster, you have to give necessary RBAC permissions for Prometheus. Let’s create necessary RBAC stuffs for Prometheus,

```bash
$ kubectl apply -f https://github.com/appscode/third-party-tools/raw/master/monitoring/prometheus/builtin/artifacts/rbac.yaml
clusterrole.rbac.authorization.k8s.io/prometheus created
serviceaccount/prometheus created
clusterrolebinding.rbac.authorization.k8s.io/prometheus created
```

> YAML for the RBAC resources created above can be found [here](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/builtin/artifacts/rbac.yaml).

**Deploy Prometheus:**

Now, we are ready to deploy Prometheus server. We are going to use following [deployment](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/builtin/artifacts/deployment.yaml) to deploy Prometheus server.

Let’s deploy the Prometheus server.

```bash
$ kubectl apply -f https://github.com/appscode/third-party-tools/raw/master/monitoring/prometheus/builtin/artifacts/deployment.yaml
deployment.apps/prometheus created
```

### Verify Monitoring Metrics

Prometheus server is listening to port `9090`. We are going to use [port forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) to access Prometheus dashboard.

At first, let’s check if the Prometheus pod is in `Running` state.

```bash
$ kubectl get pod -n monitoring -l=app=prometheus
NAME                          READY   STATUS    RESTARTS   AGE
prometheus-5dff66b455-cz9td   1/1     Running   0          42s
```

Now, run following command on a separate terminal to forward 9090 port of `prometheus-8568c86d86-95zhn` pod,

```bash
$ kubectl port-forward -n monitoring prometheus-8568c86d86-95zhn 9090
Forwarding from 127.0.0.1:9090 -> 9090
Forwarding from [::1]:9090 -> 9090
```

Now, we can access the dashboard at `localhost:9090`. Open <http://localhost:9090> in your browser. You should see the endpoint of `builtin-prom-md-stats` service as one of the targets.

![Prometheus Target](images/monitoring_builtin-prometheus_built-prom.png)

Check the labels marked with red rectangle. These labels confirm that the metrics are coming from `MariaDB` database `builtin-prom-md` through stats service `builtin-prom-md-stats`.

Now, you can view the collected metrics and create a graph from homepage of this Prometheus dashboard. You can also use this Prometheus server as data source for [Grafana](https://grafana.com/) and create beautiful dashboard with collected metrics.

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run following commands

```bash
kubectl delete mariadb -n demo builtin-prom-md

kubectl delete -n monitoring deployment.apps/prometheus

kubectl delete -n monitoring clusterrole.rbac.authorization.k8s.io/prometheus
kubectl delete -n monitoring serviceaccount/prometheus
kubectl delete -n monitoring clusterrolebinding.rbac.authorization.k8s.io/prometheus

kubectl delete ns demo
kubectl delete ns monitoring
```

<!-- PAGE_START: monitoring/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Monitoring MariaDB with KubeDB

KubeDB has native support for monitoring via [Prometheus](https://prometheus.io/). You can use builtin [Prometheus](https://github.com/prometheus/prometheus) scraper or [Prometheus operator](https://github.com/prometheus-operator/prometheus-operator) to monitor KubeDB managed databases. This tutorial will show you how database monitoring works with KubeDB and how to configure Database crd to enable monitoring.

## Overview

KubeDB uses Prometheus [exporter](https://prometheus.io/docs/instrumenting/exporters/#databases) images to export Prometheus metrics for respective databases. Following diagram shows the logical flow of database monitoring with KubeDB.

![Database Monitoring Flow](images/monitoring_overview_database-monitoring-overview.svg)

When a user creates a database crd with `spec.monitor` section configured, KubeDB operator provisions the respective database and injects an exporter image as sidecar to the database pod. It also creates a dedicated stats service with name `{database-crd-name}-stats` for monitoring. Prometheus server can scrape metrics using this stats service.

## Configure Monitoring

In order to enable monitoring for a database, you have to configure `spec.monitor` section. KubeDB provides following options to configure `spec.monitor` section:

| Field | Type | Uses |
| --- | --- | --- |
| `spec.monitor.agent` | `Required` | Type of the monitoring agent that will be used to monitor this database. It can be `prometheus.io/builtin` or `prometheus.io/operator`. |
| `spec.monitor.prometheus.exporter.port` | `Optional` | Port number where the exporter side car will serve metrics. |
| `spec.monitor.prometheus.exporter.args` | `Optional` | Arguments to pass to the exporter sidecar. |
| `spec.monitor.prometheus.exporter.env` | `Optional` | List of environment variables to set in the exporter sidecar container. |
| `spec.monitor.prometheus.exporter.resources` | `Optional` | Resources required by exporter sidecar container. |
| `spec.monitor.prometheus.exporter.securityContext` | `Optional` | Security options the exporter should run with. |
| `spec.monitor.prometheus.serviceMonitor.labels` | `Optional` | Labels for `ServiceMonitor` crd. |
| `spec.monitor.prometheus.serviceMonitor.interval` | `Optional` | Interval at which metrics should be scraped. |

## Sample Configuration

A sample YAML for MariaDB crd with `spec.monitor` section configured to enable monitoring with [Prometheus operator](https://github.com/prometheus-operator/prometheus-operator) is shown below.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: coreos-prom-md
  namespace: demo
spec:
  version: "12.1.2"
  deletionPolicy: WipeOut
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  monitor:
    agent: prometheus.io/operator
    prometheus:
      serviceMonitor:
        labels:
          release: prometheus
        interval: 10s
```

Assume that above MariaDB is configured to use basic authentication. So, exporter image also need to provide password to collect metrics. We have provided it through `spec.monitor.prometheus.exporter.args` field.

Here, we have specified that we are going to monitor this server using Prometheus operator through `spec.monitor.agent: prometheus.io/operator`. KubeDB will create a `ServiceMonitor` crd in `monitoring` namespace and this `ServiceMonitor` will have `release: prometheus` label.

## Next Steps

* Learn how to monitor `MariaDB` database with KubeDB using [builtin-Prometheus](en/monitoring/builtin-prometheus.md) and using [Prometheus operator](en/monitoring/prometheus-operator.md).
* Learn how to monitor `Elasticsearch` database with KubeDB using [builtin-Prometheus](https://kubedb.com/docs/v2026.7.10/guides/elasticsearch/monitoring/using-builtin-prometheus) and using [Prometheus operator](https://kubedb.com/docs/v2026.7.10/guides/elasticsearch/monitoring/using-prometheus-operator).
* Learn how to monitor `PostgreSQL` database with KubeDB using [builtin-Prometheus](https://kubedb.com/docs/v2026.7.10/guides/postgres/monitoring/using-builtin-prometheus) and using [Prometheus operator](https://kubedb.com/docs/v2026.7.10/guides/postgres/monitoring/using-prometheus-operator).
* Learn how to monitor `MySQL` database with KubeDB using [builtin-Prometheus](https://kubedb.com/docs/v2026.7.10/guides/mysql/monitoring/builtin-prometheus/) and using [Prometheus operator](https://kubedb.com/docs/v2026.7.10/guides/mysql/monitoring/prometheus-operator/).
* Learn how to monitor `MongoDB` database with KubeDB using [builtin-Prometheus](https://kubedb.com/docs/v2026.7.10/guides/mongodb/monitoring/using-builtin-prometheus) and using [Prometheus operator](https://kubedb.com/docs/v2026.7.10/guides/mongodb/monitoring/using-prometheus-operator).
* Learn how to monitor `Redis` server with KubeDB using [builtin-Prometheus](https://kubedb.com/docs/v2026.7.10/guides/redis/monitoring/using-builtin-prometheus) and using [Prometheus operator](https://kubedb.com/docs/v2026.7.10/guides/redis/monitoring/using-prometheus-operator).
* Learn how to monitor `Memcached` server with KubeDB using [builtin-Prometheus](https://kubedb.com/docs/v2026.7.10/guides/memcached/monitoring/using-builtin-prometheus) and using [Prometheus operator](https://kubedb.com/docs/v2026.7.10/guides/memcached/monitoring/using-prometheus-operator).

<!-- PAGE_START: monitoring/prometheus-operator.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Monitoring MariaDB Using Prometheus operator

[Prometheus operator](https://github.com/prometheus-operator/prometheus-operator) provides simple and Kubernetes native way to deploy and configure Prometheus server. This tutorial will show you how to use Prometheus operator to monitor MariaDB database deployed with KubeDB.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* To learn how Prometheus monitoring works with KubeDB in general, please visit [here](en/monitoring/overview.md).
* To keep database resources isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial. Run the following command to prepare your cluster:

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```
* We need a [Prometheus operator](https://github.com/prometheus-operator/prometheus-operator) instance running. If you don’t already have a running instance, deploy one following the docs from [here](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/operator/README.md).
* If you already don’t have a Prometheus server running, deploy one following tutorial from [here](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/operator/README.md#deploy-prometheus-server).

> Note: YAML files used in this tutorial are stored in [/docs/guides/mariadb/monitoring/prometheus-operator/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/monitoring/prometheus-operator/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Find out required labels for ServiceMonitor

We need to know the labels used to select `ServiceMonitor` by a `Prometheus` crd. We are going to provide these labels in `spec.monitor.prometheus.labels` field of MariaDB crd so that KubeDB creates `ServiceMonitor` object accordingly.

At first, let’s find out the available Prometheus server in our cluster.

```bash
$ kubectl get prometheus --all-namespaces
NAMESPACE   NAME         VERSION   REPLICAS   AGE
default     prometheus             1          2m19s
```

> If you don’t have any Prometheus server running in your cluster, deploy one following the guide specified in **Before You Begin** section.

Now, let’s view the YAML of the available Prometheus server `prometheus` in `default` namespace.

```bash
$ kubectl get prometheus -n default prometheus -o yaml
```

```yaml
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"monitoring.coreos.com/v1","kind":"Prometheus","metadata":{"annotations":{},"labels":{"prometheus":"prometheus"},"name":"prometheus","namespace":"default"},"spec":{"replicas":1,"resources":{"requests":{"memory":"400Mi"}},"serviceAccountName":"prometheus","serviceMonitorNamespaceSelector":{"matchLabels":{"prometheus":"prometheus"}},"serviceMonitorSelector":{"matchLabels":{"release":"prometheus"}}}}      
  creationTimestamp: "2020-08-25T04:02:07Z"
  generation: 1
  labels:
    prometheus: prometheus
    manager: kubectl
    operation: Update
  name: prometheus
  namespace: default
  resourceVersion: "2087"
  selfLink: /apis/monitoring.coreos.com/v1/namespaces/default/prometheuses/prometheus
  uid: 972a50cb-b751-418b-b2bc-e0ecc9232730
spec:
  replicas: 1
  resources:
    requests:
      memory: 400Mi
  serviceAccountName: prometheus
  serviceMonitorNamespaceSelector:
    matchLabels:
      prometheus: prometheus
  serviceMonitorSelector:
    matchLabels:
      release: prometheus
```

* `spec.serviceMonitorSelector` field specifies which ServiceMonitors should be included. The Above label `release: prometheus` is used to select `ServiceMonitors` by its selector. So, we are going to use this label in `spec.monitor.prometheus.labels` field of MariaDB crd.
* `spec.serviceMonitorNamespaceSelector` field specifies that the `ServiceMonitors` can be selected outside the Prometheus namespace by Prometheus using namespace selector. The Above label `prometheus: prometheus` is used to select the namespace where the `ServiceMonitor` is created.

### Add Label to database namespace

KubeDB creates a `ServiceMonitor` in database namespace `demo`. We need to add label to `demo` namespace. Prometheus will select this namespace by using its `spec.serviceMonitorNamespaceSelector` field.

Let’s add label `prometheus: prometheus` to `demo` namespace,

```bash
$ kubectl patch namespace demo -p '{"metadata":{"labels": {"prometheus":"prometheus"}}}'
namespace/demo patched
```

## Deploy MariaDB with Monitoring Enabled

At first, let’s deploy an MariaDB database with monitoring enabled. Below is the MariaDB object that we are going to create.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: coreos-prom-md
  namespace: demo
spec:
  version: "12.1.2"
  deletionPolicy: WipeOut
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  monitor:
    agent: prometheus.io/operator
    prometheus:
      serviceMonitor:
        labels:
          release: prometheus
        interval: 10s
```

Here,

* `monitor.agent: prometheus.io/operator` indicates that we are going to monitor this server using Prometheus operator.
* `monitor.prometheus.labels` specifies that KubeDB should create `ServiceMonitor` with these labels.
* `monitor.prometheus.interval` indicates that the Prometheus server should scrape metrics from this database with 10 seconds interval.

Let’s create the MariaDB object that we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/monitoring/prometheus-operator/examples/prom-operator-md.yaml
mariadb.kubedb.com/coreos-prom-md created
```

Now, wait for the database to go into `Ready` state.

```bash
$ kubectl get mariadb -n demo coreos-prom-md
NAME             VERSION   STATUS   AGE
coreos-prom-md   10.5.23    Ready    59s
```

KubeDB will create a separate stats service with name `{MariaDB crd name}-stats` for monitoring purpose.

```bash
$ kubectl get svc -n demo --selector="app.kubernetes.io/instance=coreos-prom-md"
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
coreos-prom-md         ClusterIP   10.99.96.226    <none>        3306/TCP    107s
coreos-prom-md-pods    ClusterIP   None            <none>        3306/TCP    107s
coreos-prom-md-stats   ClusterIP   10.101.190.67   <none>        56790/TCP   107s
```

Here, `coreos-prom-md-stats` service has been created for monitoring purpose.

Let’s describe this stats service.

```bash
$ kubectl describe svc -n demo coreos-prom-md-stats
```

```text
Name:              coreos-prom-md-stats
Namespace:         demo
Labels:            app.kubernetes.io/instance=coreos-prom-md
                   app.kubernetes.io/managed-by=kubedb.com
                   app.kubernetes.io/name=mariadbs.kubedb.com
                   kubedb.com/role=stats
Annotations:       monitoring.appscode.com/agent: prometheus.io/operator
Selector:          app.kubernetes.io/instance=coreos-prom-md,app.kubernetes.io/managed-by=kubedb.com,app.kubernetes.io/name=mariadbs.kubedb.com
Type:              ClusterIP
IP:                10.101.190.67
Port:              metrics  56790/TCP
TargetPort:        metrics/TCP
Endpoints:         10.244.0.31:56790
Session Affinity:  None
Events:            <none>
```

Notice the `Labels` and `Port` fields. `ServiceMonitor` will use these information to target its endpoints.

KubeDB will also create a `ServiceMonitor` crd in `demo` namespace that select the endpoints of `coreos-prom-md-stats` service. Verify that the `ServiceMonitor` crd has been created.

```bash
$ kubectl get servicemonitor -n demo
NAME                   AGE
coreos-prom-md-stats   4m8s
```

Let’s verify that the `ServiceMonitor` has the label that we had specified in `spec.monitor` section of MariaDB crd.

```bash
$ kubectl get servicemonitor -n demo coreos-prom-md-stats -o yaml
```

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  creationTimestamp: "2021-03-19T10:09:03Z"
  generation: 1
  labels:
    app.kubernetes.io/component: database
    app.kubernetes.io/instance: coreos-prom-md
    app.kubernetes.io/managed-by: kubedb.com
    app.kubernetes.io/name: mariadbs.kubedb.com
    release: prometheus
  managedFields:
  - apiVersion: monitoring.coreos.com/v1
    fieldsType: FieldsV1
    fieldsV1:
      f:metadata:
        f:labels:
          .: {}
          f:app.kubernetes.io/component: {}
          f:app.kubernetes.io/instance: {}
          f:app.kubernetes.io/managed-by: {}
          f:app.kubernetes.io/name: {}
          f:release: {}
        f:ownerReferences: {}
      f:spec:
        .: {}
        f:endpoints: {}
        f:namespaceSelector:
          .: {}
          f:matchNames: {}
        f:selector:
          .: {}
          f:matchLabels:
            .: {}
            f:app.kubernetes.io/instance: {}
            f:app.kubernetes.io/managed-by: {}
            f:app.kubernetes.io/name: {}
            f:kubedb.com/role: {}
    manager: mariadb-operator
    operation: Update
    time: "2021-03-19T10:09:03Z"
  name: coreos-prom-md-stats
  namespace: demo
  ownerReferences:
  - apiVersion: v1
    blockOwnerDeletion: true
    controller: true
    kind: Service
    name: coreos-prom-md-stats
    uid: 08260a99-0984-4d90-bf68-34080ad0ee5b
  resourceVersion: "241637"
  selfLink: /apis/monitoring.coreos.com/v1/namespaces/demo/servicemonitors/coreos-prom-md-stats
  uid: 4f022d98-d2d8-490f-9548-f6367d03ae1f
spec:
  endpoints:
  - bearerTokenSecret:
      key: ""
    honorLabels: true
    interval: 10s
    path: /metrics
    port: metrics
  namespaceSelector:
    matchNames:
    - demo
  selector:
    matchLabels:
      app.kubernetes.io/instance: coreos-prom-md
      app.kubernetes.io/managed-by: kubedb.com
      app.kubernetes.io/name: mariadbs.kubedb.com
      kubedb.com/role: stats
```

Notice that the `ServiceMonitor` has label `release: prometheus` that we had specified in MariaDB crd.

Also notice that the `ServiceMonitor` has selector which match the labels we have seen in the `coreos-prom-md-stats` service. It also, target the `prom-http` port that we have seen in the stats service.

## Verify Monitoring Metrics

At first, let’s find out the respective Prometheus pod for `prometheus` Prometheus server.

```bash
$ kubectl get pod -n default -l=app=prometheus
NAME                      READY   STATUS    RESTARTS   AGE
prometheus-prometheus-0   3/3     Running   1          16m
```

Prometheus server is listening to port `9090` of `prometheus-prometheus-0` pod. We are going to use [port forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) to access Prometheus dashboard.

Run following command on a separate terminal to forward the port 9090 of `prometheus-prometheus-0` pod,

```bash
$ kubectl port-forward -n default prometheus-prometheus-0 9090
Forwarding from 127.0.0.1:9090 -> 9090
Forwarding from [::1]:9090 -> 9090
```

Now, we can access the dashboard at `localhost:9090`. Open <http://localhost:9090> in your browser. You should see `prom-http` endpoint of `coreos-prom-md-stats` service as one of the targets.

![Prometheus Target](images/monitoring_prometheus-operator_prom-end.png)

Check the `endpoint` and `service` labels. It verifies that the target is our expected database. Now, you can view the collected metrics and create a graph from homepage of this Prometheus dashboard. You can also use this Prometheus server as data source for [Grafana](https://grafana.com/) and create beautiful dashboard with collected metrics.

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run following commands

```bash
# cleanup database
kubectl delete mariadb -n demo coreos-prom-md

# cleanup Prometheus resources
kubectl delete -f https://raw.githubusercontent.com/appscode/third-party-tools/master/monitoring/prometheus/operator/artifacts/prometheus.yaml

kubectl delete -f https://raw.githubusercontent.com/appscode/third-party-tools/master/monitoring/prometheus/operator/artifacts/prometheus-rbac.yaml

# cleanup Prometheus operator resources
kubectl delete -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/release-0.41/bundle.yaml

# delete namespace
kubectl delete ns demo
```

<!-- PAGE_START: pitr/nfs.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB MariaDB - Continuous Archiving and Point-in-time Recovery

Here, will show you how to use KubeDB to provision a MariaDB to Archive continuously and Restore point-in-time.

## Before You Begin

At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. For this demonstration, I’m using linode cluster.

Now,install `KubeDB` operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).

To install `KubeStash` operator in your cluster following the steps [here](https://github.com/kubestash/installer/tree/master/charts/kubestash).

To install `External-snapshotter` in your cluster following the steps [here](https://github.com/kubernetes-csi/external-snapshotter/tree/release-5.0).

To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

> Note: The yaml files used in this tutorial are stored in [docs/guides/mariadb/pitr/nfs/yamls](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/remote-replica/yamls) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## continuous archiving

Continuous archiving involves making regular copies (or “archives”) of the MariaDB transaction log files.To ensure continuous archiving to a nfs we need prepare `NFS Server` `BackupStorage`,`RetentionPolicy`,`MariaDBArchiver` for the KubeDB Managed MariaDB Databases.

## Ensure volumeSnapshotClass

```bash
$ kubectl get volumesnapshotclasses
NAME                    DRIVER               DELETIONPOLICY   AGE
longhorn-snapshot-vsc   driver.longhorn.io   Delete           7d22h
```

If not any, try using `longhorn` or any other [volumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/).

### Install Longhorn

Longhorn is a distributed block storage system for Kubernetes that manages persistent storage.

Add Longhorn chart repository.

`helm repo add longhorn https://charts.longhorn.io`

Update local Longhorn chart information from chart repository.

`helm repo update`

Install Longhorn chart.

With Helm 2, the following command will create the longhorn-system namespace and install the Longhorn chart together.

`helm install longhorn/longhorn --name longhorn --namespace longhorn-system`

With Helm 3, the following commands will create the longhorn-system namespace first, then install the Longhorn chart.

```bash
kubectl create namespace longhorn-system
helm install longhorn longhorn/longhorn --namespace longhorn-system
```

Create volumesnapshot class using longhorn

```yaml
kind: VolumeSnapshotClass
apiVersion: snapshot.storage.k8s.io/v1
metadata:
  name: longhorn-snapshot-vsc
driver: driver.longhorn.io
deletionPolicy: Delete
parameters:
  type: snap
```

```bash
$ kubectl apply -f volumesnapshotclass.yaml
  volumesnapshotclass.snapshot.storage.k8s.io/longhorn-snapshot-vsc unchanged
```

### Install CSI driver for NFS

Install CSI driver for creating nfs volume from [here](https://github.com/kubernetes-csi/csi-driver-nfs/tree/master/charts).

```bash
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm install csi-driver-nfs csi-driver-nfs/csi-driver-nfs --namespace kube-system --version v4.5.0 --set feature.enableFSGroupPolicy=true
```

Be aware to set `--set feature.enableFSGroupPolicy=true` this.

We will use namespace `demo` throughout this tutorial.

```bash
➤ kubectl create ns demo
namespace/demo created
```

### Setup NFS Server

We will deploy a nfs server and a service using the below yamls. Note we have shared `/exports` path.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nfs-server
  namespace: demo
spec:
  selector:
    matchLabels:
      app: nfs-server
  template:
    metadata:
      labels:
        app: nfs-server
    spec:
      containers:
        - name: nfs-server
          image: k8s.gcr.io/volume-nfs:0.8
          ports:
            - name: nfs
              containerPort: 2049
            - name: mountd
              containerPort: 20048
            - name: rpcbind
              containerPort: 111
          securityContext:
            privileged: true
          volumeMounts:
            - name: storage
              mountPath: /exports
      volumes:
        - name: storage
          hostPath:
            path: /data/nfs # store all data in "/data/nfs" directory of the node where it is running
            type: DirectoryOrCreate
---
apiVersion: v1
kind: Service
metadata:
  name: nfs-server
  namespace: demo
spec:
  ports:
    - name: nfs
      port: 2049
    - name: mountd
      port: 20048
    - name: rpcbind
      port: 111
  selector:
    app: nfs-server # must match with the label of NFS pod
```

```bash
➤ kubectl apply -f nfs-server.yaml
deployment.apps/nfs-server created
service/nfs-server created
```

nfs server should be running inside `nfs-server-***` pod

### Create StorageClass for NFS

```yaml
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: nfs 
parameters:
  server: nfs-server.demo.svc.cluster.local
  share: /
provisioner: nfs.csi.k8s.io
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

Here, `parameters.server` should be the dns name of your service that is created along with nfs server, `parameters.share` should be the path inside the shared directory.

### Create BackupStorage

First create a PVC which we will use as our backend storage. This pvc should be created using `nfs` storageClass that we have created earlier.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nfs-pvc
  namespace: demo
spec:
  storageClassName: "nfs"
  resources:
    requests:
      storage: 1Gi
  accessModes: 
    - ReadWriteOnce
```

Now we create the backupStorage following way.

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: local-storage
  namespace: demo
spec:
  storage:
    provider: local
    local:
      mountPath: /md/walg
      persistentVolumeClaim:
        claimName: nfs-pvc
  usagePolicy:
    allowedNamespaces:
      from: All
  default: false
  deletionPolicy: WipeOut
  runtimeSettings:
    pod:
      securityContext:
        fsGroup: 999
        runAsUser: 999
```

```bash
$ kubectl apply -f nfs-pvc.yaml
  persistentvolumeclaim/nfs-pvc  created
```

```bash
$ kubectl apply -f backupstorage.yaml
   backupstorage.storage.kubestash.com/linode-storage created
```

### Retention policy

RetentionPolicy is a custom resource(CR) provided by KubeStash that allows you to set how long you’d like to retain the backup data.

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: mariadb-retention-policy
  namespace: demo
spec:
  maxRetentionPeriod: "30d"
  successfulSnapshots:
    last: 2
  failedSnapshots:
    last: 2
```

```bash
$ kubectl apply -f  https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/nfs/yamls/retentionPolicy.yaml 
retentionpolicy.storage.kubestash.com/mariadb-retention-policy created
```

### EncryptionSecret

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: encrypt-secret
  namespace: demo
stringData:
  RESTIC_PASSWORD: "changeit"
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/nfs/yamls/encryptionSecret.yaml
```

### MariaDBArchiver

MariaDBArchiver is a custom resource(CR) provided by KubeDB for managing the archiving of MariaDB binlog files and performing volume-level backups

```yaml
apiVersion: archiver.kubedb.com/v1alpha1
kind: MariaDBArchiver
metadata:
  name: mariadbarchiver-sample
  namespace: demo
spec:
  pause: false
  databases:
    namespaces:
      from: Selector
      selector:
        matchLabels:
          kubernetes.io/metadata.name: demo
    selector:
      matchLabels:
        archiver: "true"
  retentionPolicy:
    name: mariadb-retention-policy
    namespace: demo
  encryptionSecret:
    name: "encrypt-secret"
    namespace: "demo"
  fullBackup:
    jobTemplate:
      spec:
        securityContext:
          fsGroup: 999
          runAsUser: 999
    driver: "VolumeSnapshotter"
    task:
      params:
        volumeSnapshotClassName: "longhorn-snapshot-vsc"
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  manifestBackup:
    jobTemplate:
      spec:
        securityContext:
          fsGroup: 999
          runAsUser: 999
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  backupStorage:
    ref:
      name: "local-storage"
      namespace: "demo"
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/nfs/yamls/mariadbarchiver.yaml
 mariadbarchiver.archiver.kubedb.com/mariadbarchiver-sample created
```

# Deploy MariaDB

So far we are ready with setup for continuously archive MariaDB, We deploy a mariadb referring the MariaDB archiver object.To properly configure MariaDB for archiving, you need to pass specific arguments to the MariaDB container in the `spec.podTemplate.containers["mariadb"].args` field. Below is an example of a YAML configuration for a MariaDB instance managed by KubeDB, with archiving enabled.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
  labels:
    archiver: "true"
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  archiver:
    ref:
      name: mariadbarchiver-sample
      namespace: demo
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl get pod -n demo
NAME                                                              READY   STATUS      RESTARTS        AGE
mariadb-0                                                         2/2     Running     0               4m12s
mariadb-1                                                         2/2     Running     0               4m12s
mariadb-2                                                         2/2     Running     0               3m12s
mariadb-backup-full-backup-1726549703-bjk9w                       0/1     Completed   0               3m22s
mariadb-backup-manifest-backup-1726549703-fx9kx                   0/1     Completed   0               3m22s
mariadb-sidekick                                                  1/1     Running
retention-policy-mariadb-backup-full-backup-1726549703-wg7wt      0/1     Completed   0               3m42s
retention-policy-mariadb-backup-manifest-backup-17265497038pvjd   0/1     Completed   0               3m55s
```

`mariadb-sidekick` is responsible for uploading binlog files

`mariadb-backup-full-backup-1726549703-bjk9w` are the pod of volumes levels backups for MariaDB.

`mariadb-backup-manifest-backup-1726549703-fx9kx` are the pod of the manifest backup related to MariaDB object

### validate BackupConfiguration and VolumeSnapshots

```bash
$ kubectl get backupconfigurations -n demo

NAME                    PHASE   PAUSED   AGE
mariadb-backup          Ready            2m43s

$ kubectl get backupsession -n demo
NAME                                           INVOKER-TYPE          INVOKER-NAME            PHASE       DURATION   AGE
mariadb-backup-full-backup-1726549703          BackupConfiguration   mariadb-backup          Succeeded   33s        11m
mariadb-backup-manifest-backup-1726549703      BackupConfiguration   mariadb-backup          Succeeded   20s        11m

kubectl get volumesnapshots -n demo
NAME                    READYTOUSE   SOURCEPVC        SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS           SNAPSHOTCONTENT                                    CREATIONTIME   AGE
mariadb-1726549985      true         data-mariadb-0                           10Gi          longhorn-snapshot-vsc   snapcontent-317aaac9-ae4f-438b-9763-4eb81ff828af    11m            11m
```

## Data Insert and Switch Binlog File

After each and every binlog switch the binlog files will be uploaded to backup storage

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');

MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

> At this point We have 10 rows in our newly created table `demo_table` on database `hello`

## Point-in-time Recovery

Point-In-Time Recovery allows you to restore a MariaDB database to a specific point in time using the archived transaction logs. This is particularly useful in scenarios where you need to recover to a state just before a specific error or data corruption occurred.
Let’s say accidentally our dba drops the table demo\_table and we want to restore.

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash

MariaDB [hello]> drop table demo_table;

MariaDB [hello]> flush logs;
```

We can’t restore from a full backup since at this point no full backup was perform. so we can choose a specific time in which time we want to restore.We can get the specfice time from the binlog that archived in the backup storage . Go to the binlog file and find where to store. You can parse binlog-files using `mariadbbinlog`.

For the demo I will use the previous time we get form `select now()`

```mysql
MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+
```

### Restore MariaDB

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: restore-mariadb
  namespace: demo
spec:
  init:
    archiver:
      encryptionSecret:
        name: encrypt-secret
        namespace: demo
      fullDBRepository:
        name: mariadb-full
        namespace: demo
      recoveryTimestamp: "2024-09-17T05:28:26Z"
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl apply -f mariadbrestore.yaml
mariadb.kubedb.com/restore-mariadb created
```

**check for Restored MariaDB**

```bash
$ kubectl get pod -n demo
restore-mariadb-0                                          1/1     Running     0             44s
restore-mariadb-1                                          1/1     Running     0             42s
restore-mariadb-2                                          1/1     Running     0             41s
restore-mariadb-restorer-z4brz                             0/2     Completed   0             113s
restore-mariadb-restoresession-lk6jq                       0/1     Completed   0             2m6s
```

```bash
$ kubectl get mariadb -n demo
NAME              VERSION   STATUS   AGE
mariadb           11.1.3    Ready    14m
restore-mariadb   11.1.3    Ready    5m37s
```

**Validating data on Restored MariaDB**

```bash
$ kubectl exec -it -n demo restore-mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

mariadb> use hello

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
1 row in set (0.00 sec)
```

**so we are able to successfully recover from a disaster**

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete -n demo mariadb/mariadb
$ kubectl delete -n demo mariadb/restore-mariadb
$ kubectl delete -n demo backupstorage
$ kubectl delete -n demo mariadbarchiver
$ kubectl delete ns demo
```

## Next Steps

* Learn about [backup and restore](en/backup/kubestash/overview.md) MariaDB database using KubeStash.
* Learn about initializing [MariaDB with Script](en/initialization/using-script.md).
* Want to setup MariaDB cluster? Check how to [configure Highly Available MariaDB Cluster](en/clustering/galera-cluster.md)
* Monitor your MariaDB database with KubeDB using [built-in Prometheus](en/monitoring/builtin-prometheus.md).
* Monitor your MariaDB database with KubeDB using [Prometheus operator](en/monitoring/prometheus-operator.md).
* Detail concepts of [MariaDB object](en/concepts/mariadb.md).
* Use [private Docker registry](en/private-registry/quickstart.md) to deploy MariaDB with KubeDB.
* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: pitr/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# KubeDB MariaDB - Continuous Archiving and Point-in-time Recovery

Here, will show you how to use KubeDB to provision a MariaDB to Archive continuously and Restore point-in-time.

## Before You Begin

At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. For this demonstration, I’m using linode cluster.

Now,install `KubeDB` operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).

To install `KubeStash` operator in your cluster following the steps [here](https://github.com/kubestash/installer/tree/master/charts/kubestash).

To install `External-snapshotter` in your cluster following the steps [here](https://github.com/kubernetes-csi/external-snapshotter/tree/release-5.0).

To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

> Note: The yaml files used in this tutorial are stored in [docs/guides/mariadb/pitr/overview/yamls](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/remote-replica/yamls) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Continuous Archiving

```mermaid
flowchart LR
  DB["MariaDB Cluster Pods"] -->|Write Binlogs| Archiver["MariaDBArchiver + Sidekick"]
  Archiver -->|Upload Binlogs| Store["BackupStorage Repository"]
  Snap["VolumeSnapshot (Full Backup)"] --> Restorer["Restore MariaDB CR (recoveryTimestamp)"]
  Store -->|Replay Binlogs| Restorer
  Restorer --> Target["Recovered MariaDB Cluster"]
```

Continuous archiving involves making regular copies (or “archives”) of the MariaDB transaction log files.To ensure continuous archiving to a remote location we need prepare `BackupStorage`,`RetentionPolicy`,`MariaDBArchiver` for the KubeDB Managed MariaDB Databases.

### BackupStorage

BackupStorage is a CR provided by KubeStash that can manage storage from various providers like GCS, S3, and more.
We are going to store our backup data into a `S3` bucket. We have to create a `Secret` with necessary credentials and a `BackupStorage` CR to use this backend. If you want to use a different backend, please read the respective backend configuration doc from [here](https://kubestash.com/docs/latest/guides/backends/overview/).

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: linode-storage
  namespace: demo
spec:
  storage:
    provider: s3
    s3:
      bucket: test-archiver
      endpoint: https://ap-south-1.linodeobjects.com
      region: ap-south-1
      prefix: backup
      secretName: storage
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: WipeOut
```

```bash
$ kubectl apply -f backupstorage.yaml
   backupstorage.storage.kubestash.com/linode-storage created
```

### secrets for backup-storage

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: storage
  namespace: demo
stringData:
  AWS_ACCESS_KEY_ID: "*************26CX"
  AWS_SECRET_ACCESS_KEY: "************jj3lp"
  AWS_ENDPOINT: https://ap-south-1.linodeobjects.com
```

```bash
$ kubectl apply -f storage-secret.yaml 
  secret/storage created
```

### Retention policy

RetentionPolicy is a custom resource(CR) provided by KubeStash that allows you to set how long you’d like to retain the backup data.

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: mariadb-retention-policy
  namespace: demo
spec:
  maxRetentionPeriod: "30d"
  successfulSnapshots:
    last: 100
  failedSnapshots:
    last: 2
```

```bash
$ kubectl apply -f  https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/overview/yamls/retention-policy.yaml 
retentionpolicy.storage.kubestash.com/mariadb-retention-policy created
```

### MariaDBArchiver

MariaDBArchiver is a custom resource(CR) provided by KubeDB for managing the archiving of MariaDB binlog files and performing volume-level backups

```yaml
apiVersion: archiver.kubedb.com/v1alpha1
kind: MariaDBArchiver
metadata:
  name: mariadbarchiver-sample
  namespace: demo
spec:
  pause: false
  databases:
    namespaces:
      from: Selector
      selector:
        matchLabels:
          kubernetes.io/metadata.name: demo
    selector:
      matchLabels:
        archiver: "true"
  retentionPolicy:
    name: mariadb-retention-policy
    namespace: demo
  encryptionSecret:
    name: "encrypt-secret"
    namespace: "demo"
  fullBackup:
    driver: "VolumeSnapshotter"
    task:
      params:
        volumeSnapshotClassName: "longhorn-snapshot-vsc"
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  manifestBackup:
    scheduler:
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
      schedule: "*/30 * * * *"
    sessionHistoryLimit: 2
  backupStorage:
    ref:
      name: "linode-storage"
      namespace: "demo"
```

### EncryptionSecret

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: encrypt-secret
  namespace: demo
stringData:
  RESTIC_PASSWORD: "changeit"
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/overview/yamls/mariadbarchiver.yaml
 mariadbarchiver.archiver.kubedb.com/mariadbarchiver-sample created
 $ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/pitr/overview/yamls/encryptionSecret.yaml
```

## Ensure volumeSnapshotClass

```bash
$ kubectl get volumesnapshotclasses
NAME                    DRIVER               DELETIONPOLICY   AGE
longhorn-snapshot-vsc   driver.longhorn.io   Delete           7d22h
```

If not any, try using `longhorn` or any other [volumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/).

```yaml
kind: VolumeSnapshotClass
apiVersion: snapshot.storage.k8s.io/v1
metadata:
  name: longhorn-snapshot-vsc
driver: driver.longhorn.io
deletionPolicy: Delete
parameters:
  type: snap
```

```bash
$ helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace

$ kubectl apply -f volumesnapshotclass.yaml
  volumesnapshotclass.snapshot.storage.k8s.io/longhorn-snapshot-vsc unchanged
```

# Deploy MariaDB

So far we are ready with setup for continuously archive MariaDB, We deploy a mariadb referring the MariaDB archiver object.To properly configure MariaDB for archiving, you need to pass specific arguments to the MariaDB container in the `spec.podTemplate.containers["mariadb"].args` field. Below is an example of a YAML configuration for a MariaDB instance managed by KubeDB, with archiving enabled.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
  labels:
    archiver: "true"
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  archiver:
    ref:
      name: mariadbarchiver-sample
      namespace: demo
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl get pod -n demo
NAME                                                              READY   STATUS      RESTARTS        AGE
mariadb-0                                                         2/2     Running     0               4m12s
mariadb-1                                                         2/2     Running     0               4m12s
mariadb-2                                                         2/2     Running     0               3m12s
mariadb-backup-full-backup-1726549703-bjk9w                       0/1     Completed   0               3m22s
mariadb-backup-manifest-backup-1726549703-fx9kx                   0/1     Completed   0               3m22s
mariadb-sidekick                                                  1/1     Running
retention-policy-mariadb-backup-full-backup-1726549703-wg7wt      0/1     Completed   0               3m42s
retention-policy-mariadb-backup-manifest-backup-17265497038pvjd   0/1     Completed   0               3m55s
```

`mariadb-sidekick` is responsible for uploading binlog files

`mariadb-backup-full-backup-1726549703-bjk9w` are the pod of volumes levels backups for MariaDB.

`mariadb-backup-manifest-backup-1726549703-fx9kx` are the pod of the manifest backup related to MariaDB object

### validate BackupConfiguration and VolumeSnapshots

```bash
$ kubectl get backupconfigurations -n demo

NAME                    PHASE   PAUSED   AGE
mariadb-backup          Ready            2m43s

$ kubectl get backupsession -n demo
NAME                                           INVOKER-TYPE          INVOKER-NAME            PHASE       DURATION   AGE
mariadb-backup-full-backup-1726549703          BackupConfiguration   mariadb-backup          Succeeded   33s        11m
mariadb-backup-manifest-backup-1726549703      BackupConfiguration   mariadb-backup          Succeeded   20s        11m

kubectl get volumesnapshots -n demo
NAME                    READYTOUSE   SOURCEPVC        SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS           SNAPSHOTCONTENT                                    CREATIONTIME   AGE
mariadb-1726549985      true         data-mariadb-0                           10Gi          longhorn-snapshot-vsc   snapcontent-317aaac9-ae4f-438b-9763-4eb81ff828af    11m            11m
```

## Data Insert and Switch Binlog File

After each and every binlog switch the binlog files will be uploaded to backup storage

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');

MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

> At this point We have 10 rows in our newly created table `demo_table` on database `hello`

## Point-in-time Recovery

Point-In-Time Recovery allows you to restore a MariaDB database to a specific point in time using the archived transaction logs. This is particularly useful in scenarios where you need to recover to a state just before a specific error or data corruption occurred.
Let’s say accidentally our dba drops the table demo\_table and we want to restore.

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash

MariaDB [hello]> drop table demo_table;

MariaDB [hello]> flush logs;
```

We can’t restore from a full backup since at this point no full backup was perform. so we can choose a specific time in which time we want to restore.We can get the specfice time from the binlog that archived in the backup storage . Go to the binlog file and find where to store. You can parse binlog-files using `mariadbbinlog`.

For the demo I will use the previous time we get form `select now()`

```mysql
MariaDB [hello]> select now();
+---------------------+
| now()               |
+---------------------+
| 2024-09-17 05:28:26 |
+---------------------+
```

### Restore MariaDB

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: restore-mariadb
  namespace: demo
spec:
  init:
    archiver:
      encryptionSecret:
        name: encrypt-secret
        namespace: demo
      fullDBRepository:
        name: mariadb-full
        namespace: demo
      recoveryTimestamp: "2024-09-17T05:28:26Z"
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
  deletionPolicy: WipeOut
  podTemplate:
    spec:
      containers:
        - name: mariadb
          args:
            - "--log-bin"
            - "--log-slave-updates"
            - "--wsrep-gtid-mode=ON"
```

```bash
$ kubectl apply -f mariadbrestore.yaml
mariadb.kubedb.com/restore-mariadb created
```

**check for Restored MariaDB**

```bash
$ kubectl get pod -n demo
restore-mariadb-0                                          1/1     Running     0             44s
restore-mariadb-1                                          1/1     Running     0             42s
restore-mariadb-2                                          1/1     Running     0             41s
restore-mariadb-restorer-z4brz                             0/2     Completed   0             113s
restore-mariadb-restoresession-lk6jq                       0/1     Completed   0             2m6s
```

```bash
$ kubectl get mariadb -n demo
NAME              VERSION   STATUS   AGE
mariadb           11.1.3    Ready    14m
restore-mariadb   11.1.3    Ready    5m37s
```

**Validating data on Restored MariaDB**

```bash
$ kubectl exec -it -n demo restore-mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

mariadb> use hello

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
1 row in set (0.00 sec)
```

**so we are able to successfully recover from a disaster**

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete -n demo mariadb/mariadb
$ kubectl delete -n demo mariadb/restore-mariadb
$ kubectl delete -n demo backupstorage
$ kubectl delete -n demo mariadbarchiver
$ kubectl delete ns demo
```

## Next Steps

* Learn about [backup and restore](en/backup/kubestash/overview.md) MariaDB database using KubeStash.
* Learn about initializing [MariaDB with Script](en/initialization/using-script.md).
* Want to setup MariaDB cluster? Check how to [configure Highly Available MariaDB Cluster](en/clustering/galera-cluster.md)
* Monitor your MariaDB database with KubeDB using [built-in Prometheus](en/monitoring/builtin-prometheus.md).
* Monitor your MariaDB database with KubeDB using [Prometheus operator](en/monitoring/prometheus-operator.md).
* Detail concepts of [MariaDB object](en/concepts/mariadb.md).
* Use [private Docker registry](en/private-registry/quickstart.md) to deploy MariaDB with KubeDB.
* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: private-registry/quickstart.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Deploy MariaDB from private Docker registry

KubeDB operator supports using private Docker registry. This tutorial will show you how to use KubeDB to run MariaDB database using private Docker images.

## Before You Begin

* Read [concept of MariaDB Version Catalog](en/concepts/mariadb-version.md) to learn detail concepts of `MariaDBVersion` object.
* You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* You will also need a docker private [registry](https://docs.docker.com/registry/) or [private repository](https://docs.docker.com/docker-hub/repos/#private-repositories). In this tutorial we will use private repository of [docker hub](https://hub.docker.com/).
* You have to push the required images from KubeDB’s [Docker hub account](https://hub.docker.com/u/kubedb) into your private registry. For mariadb, push `DB_IMAGE`, `EXPORTER_IMAGE`, `INITCONTAINER_IMAGE` of following MariaDBVersions, where `deprecated` is not true, to your private registry.

```bash
$ kubectl get mariadbversions -n kube-system  -o=custom-columns=NAME:.metadata.name,VERSION:.spec.version,DB_IMAGE:.spec.db.image,EXPORTER_IMAGE:.spec.exporter.image,INITCONTAINER_IMAGE:.spec.initContainer.image,DEPRECATED:.spec.deprecated
NAME      VERSION   DB_IMAGE                                        EXPORTER_IMAGE                           INITCONTAINER_IMAGE                 DEPRECATED
10.10.7   10.10.7   ghcr.io/appscode-images/mariadb:10.10.7-jammy   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.11.6   10.11.6   ghcr.io/appscode-images/mariadb:10.11.6-jammy   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.4.32   10.4.32   ghcr.io/appscode-images/mariadb:10.4.32-focal   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.5.23   10.5.23   ghcr.io/appscode-images/mariadb:10.5.23-focal   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
10.6.16   10.6.16   ghcr.io/appscode-images/mariadb:10.6.16-focal   docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.0.4    11.0.4    ghcr.io/appscode-images/mariadb:11.0.4-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.1.3    11.1.3    ghcr.io/appscode-images/mariadb:11.1.3-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.2.2    11.2.2    ghcr.io/appscode-images/mariadb:11.2.2-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.3.2    11.3.2    ghcr.io/appscode-images/mariadb:11.3.2-jammy    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.4.3    11.4.3    ghcr.io/appscode-images/mariadb:11.4.3-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.5.2    11.5.2    ghcr.io/appscode-images/mariadb:11.5.2-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.6.2    11.6.2    ghcr.io/appscode-images/mariadb:11.6.2-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
11.8.5    11.8.5    ghcr.io/appscode-images/mariadb:11.8.5-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
12.1.2    12.1.2    ghcr.io/appscode-images/mariadb:12.1.2-noble    docker.io/prom/mysqld-exporter:v0.18.0   ghcr.io/kubedb/mariadb-init:0.8.0   <none>
```

Docker hub repositories:

* [kubedb/operator](https://hub.docker.com/r/kubedb/operator)
* [kubedb/mariadb](https://hub.docker.com/r/kubedb/mariadb)
* [kubedb/mysqld-exporter](https://hub.docker.com/r/kubedb/mysqld-exporter)

  + Update KubeDB catalog for private Docker registry. Ex:

    ```yaml
    apiVersion: catalog.kubedb.com/v1alpha1
    kind: MariaDBVersion
    metadata:
      name: 11.8.5
    spec:
      coordinator:
        image: PRIVATE_REGISTRY/mariadb-coordinator:v0.40.0
      db:
        image: PRIVATE_REGISTRY/mariadb:11.8.5
      exporter:
        image: PRIVATE_REGISTRY/mysqld-exporter:v0.11.0
      initContainer:
        image: PRIVATE_REGISTRY/busybox
      maxscale:
        image: mariadb/maxscale:24.02.4
        securityContext:
          runAsUser: 995
      podSecurityPolicies:
        databasePolicyName: maria-db
      version: 12.1.2
    ```
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial. Run the following command to prepare your cluster for this tutorial:

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Create ImagePullSecret

ImagePullSecrets is a type of a Kubernete Secret whose sole purpose is to pull private images from a Docker registry. It allows you to specify the url of the docker registry, credentials for logging in and the image name of your private docker image.

Run the following command, substituting the appropriate uppercase values to create an image pull secret for your private Docker registry:

```bash
$ kubectl create secret docker-registry -n demo myregistrykey \
  --docker-server=DOCKER_REGISTRY_SERVER \
  --docker-username=DOCKER_USER \
  --docker-email=DOCKER_EMAIL \
  --docker-password=DOCKER_PASSWORD
secret/myregistrykey created
```

If you wish to follow other ways to pull private images see [official docs](https://kubernetes.io/docs/concepts/containers/images/) of Kubernetes.

NB: If you are using `kubectl` 1.9.0, update to 1.9.1 or later to avoid this [issue](https://github.com/kubernetes/kubernetes/issues/57427).

## Install KubeDB operator

When installing KubeDB operator, set the flags `--docker-registry` and `--image-pull-secret` to appropriate value. Follow the steps to [install KubeDB operator](https://kubedb.com/docs/v2026.7.10/setup/README) properly in cluster so that to points to the DOCKER\_REGISTRY you wish to pull images from.

## Deploy MariaDB database from Private Registry

While deploying `MariaDB` from private repository, you have to add `myregistrykey` secret in `MariaDB` `spec.imagePullSecrets`.
Below is the MariaDB CRD object we will create.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-pvt-reg
  namespace: demo
spec:
  version: "12.1.2"
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      imagePullSecrets:
      - name: myregistrykey
  deletionPolicy: WipeOut
```

Now run the command to deploy this `MariaDB` object:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/private-registry/quickstart/examples/demo.yaml
mariadb.kubedb.com/md-pvt-reg created
```

To check if the images pulled successfully from the repository, see if the `MariaDB` is in running state:

```bash
$ kubectl get pods -n demo
NAME              READY     STATUS    RESTARTS   AGE
md-pvt-reg-0   1/1       Running   0          56s
```

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo md-pvt-reg
mariadb.kubedb.com "md-pvt-reg" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: quickstart/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB QuickStart

This tutorial will show you how to use KubeDB to run a MariaDB database.

![lifecycle](images/quickstart_overview_mariadb-lifecycle.png)

> Note: The yaml files used in this tutorial are stored in [here](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples).

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) is required to run KubeDB. Check the available StorageClass in cluster.

```bash
$ kubectl get storageclasses
NAME                 PROVISIONER             RECLAIMPOLICY     VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
standard (default)   rancher.io/local-path   Delete            WaitForFirstConsumer   false                  6h22m
```

* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

```
$ kubectl create ns demo
namespace/demo created
```

## Find Available MariaDBVersion

When you have installed KubeDB, it has created `MariaDBVersion` crd for all supported MariaDB versions. Check it by using the following command,

```bash
$ kubectl get mariadbversions
NAME      VERSION   DB_IMAGE                                        DEPRECATED   AGE
10.10.7   10.10.7   ghcr.io/appscode-images/mariadb:10.10.7-jammy                12d
10.11.6   10.11.6   ghcr.io/appscode-images/mariadb:10.11.6-jammy                12d
10.4.32   10.4.32   ghcr.io/appscode-images/mariadb:10.4.32-focal                12d
10.5.23   10.5.23   ghcr.io/appscode-images/mariadb:10.5.23-focal                12d
10.6.16   10.6.16   ghcr.io/appscode-images/mariadb:10.6.16-focal                12d
11.0.4    11.0.4    ghcr.io/appscode-images/mariadb:11.0.4-jammy                 12d
11.1.3    11.1.3    ghcr.io/appscode-images/mariadb:11.1.3-jammy                 12d
11.2.2    11.2.2    ghcr.io/appscode-images/mariadb:11.2.2-jammy                 12d
11.3.2    11.3.2    ghcr.io/appscode-images/mariadb:11.3.2-jammy                 12d
11.4.3    11.4.3    ghcr.io/appscode-images/mariadb:11.4.3-noble                 12d
11.5.2    11.5.2    ghcr.io/appscode-images/mariadb:11.5.2-noble                 12d
11.6.2    11.6.2    ghcr.io/appscode-images/mariadb:11.6.2-noble                 12d
11.8.5    11.8.5    ghcr.io/appscode-images/mariadb:11.8.5-noble                 12d
12.1.2    12.1.2    ghcr.io/appscode-images/mariadb:12.1.2-noble                 12d
```

## Create a MariaDB database

KubeDB implements a `MariaDB` CRD to define the specification of a MariaDB database. Below is the `MariaDB` object created in this tutorial.

`Note`: If your `KubeDB version` is less or equal to `v2024.6.4`, You have to use `v1alpha2` apiVersion.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: Delete
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples/sample-mariadb-v1.yaml
mariadb.kubedb.com/sample-mariadb created
```

```yaml
apiVersion: kubedb.com/v1alpha2
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  terminationPolicy: Delete
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples/sample-mariadb-v1alpha2.yaml
mariadb.kubedb.com/sample-mariadb created
```

Here,

* `spec.version` is the name of the MariaDBVersion CRD where the docker images are specified. In this tutorial, a MariaDB `12.1.2` database is going to create.
* `spec.storageType` specifies the type of storage that will be used for MariaDB database. It can be `Durable` or `Ephemeral`. Default value of this field is `Durable`. If `Ephemeral` is used then KubeDB will create MariaDB database using `EmptyDir` volume. In this case, you don’t have to specify `spec.storage` field. This is useful for testing purposes.
* `spec.storage` specifies the StorageClass of PVC dynamically allocated to store data for this database. This storage spec will be passed to the PetSet created by KubeDB operator to run database pods. You can specify any StorageClass available in your cluster with appropriate resource requests.
* `spec.terminationPolicy` or `spec.deletionPolicy` gives flexibility whether to `nullify`(reject) the delete operation of `MariaDB` crd or which resources KubeDB should keep or delete when you delete `MariaDB` crd. If admission webhook is enabled, It prevents users from deleting the database as long as the `spec.terminationPolicy` is set to `DoNotTerminate`.

> Note: spec.storage section is used to create PVC for database pod. It will create PVC with storage size specified instorage.resources.requests field. Don’t specify limits here. PVC does not get resized automatically.

KubeDB operator watches for `MariaDB` objects using Kubernetes api. When a `MariaDB` object is created, KubeDB operator will create a new PetSet and a Service with the matching MariaDB object name. KubeDB operator will also create a governing service for PetSets with the name `kubedb`, if one is not already present.

```bash
$ kubectl describe -n demo mariadb sample-mariadb
Name:         sample-mariadb
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  kubedb.com/v1
Kind:         MariaDB
Metadata:
  Creation Timestamp:  2022-06-06T04:42:27Z
  Finalizers:
    kubedb.com
  Generation:  2
  ...
  Resource Version:  2673
  UID:               2f9c9453-6e78-4521-91ea-34ad2da398bc
Spec:
  Allowed Schemas:
    Namespaces:
      From:  Same
  Auth Secret:
    Name:  sample-mariadb-auth
  Pod Template:
    ...
  Replicas:                  1
  Storage:
    Access Modes:
      ReadWriteOnce
    Resources:
      Requests:
        Storage:         1Gi
    Storage Class Name:  standard
  Storage Type:          Durable
  Termination Policy:    WipeOut
  Version:               11.8.5
Status:
  Conditions:
    Last Transition Time:  2022-06-06T04:42:27Z
    Message:               The KubeDB operator has started the provisioning of MariaDB: demo/sample-mariadb
    Reason:                DatabaseProvisioningStartedSuccessfully
    Status:                True
    Type:                  ProvisioningStarted
    Last Transition Time:  2022-06-06T04:43:37Z
    Message:               database sample-mariadb/demo is ready
    Reason:                AllReplicasReady
    Status:                True
    Type:                  Ready
    Last Transition Time:  2022-06-06T04:43:37Z
    Message:               database sample-mariadb/demo is accepting connection
    Reason:                AcceptingConnection
    Status:                True
    Type:                  AcceptingConnection
    Last Transition Time:  2022-06-06T04:43:26Z
    Message:               All desired replicas are ready.
    Reason:                AllReplicasReady
    Status:                True
    Type:                  ReplicaReady
    Last Transition Time:  2022-06-06T04:43:37Z
    Message:               The MariaDB: demo/sample-mariadb is successfully provisioned.
    Observed Generation:   2
    Reason:                DatabaseSuccessfullyProvisioned
    Status:                True
    Type:                  Provisioned
  Observed Generation:     2
  Phase:                   Ready
Events:
  Type    Reason      Age    From             Message
  ----    ------      ----   ----             -------
  Normal  Successful  3m49s  KubeDB Operator  Successfully created governing service
  Normal  Successful  3m49s  KubeDB Operator  Successfully created Service
  Normal  Successful  3m49s  KubeDB Operator  Successfully created PetSet demo/sample-mariadb
  Normal  Successful  3m49s  KubeDB Operator  Successfully created MariaDB
  Normal  Successful  3m49s  KubeDB Operator  Successfully created appbinding

  
  
$ kubectl get petset -n demo
NAME             READY   AGE
sample-mariadb   1/1     27m

$ kubectl get pvc -n demo
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-sample-mariadb-0   Bound    pvc-10651900-d975-467f-80ff-9c4755bdf917   1Gi        RWO            standard       27m

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-10651900-d975-467f-80ff-9c4755bdf917   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   standard                27m

$ kubectl get service -n demo
NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
sample-mariadb        ClusterIP   10.105.207.172   <none>        3306/TCP   28m
sample-mariadb-pods   ClusterIP   None             <none>        3306/TCP   28m
```

KubeDB operator sets the `status.phase` to `Running` once the database is successfully created. Run the following command to see the modified MariaDB object:

```bash
$ kubectl get mariadb -n demo sample-mariadb -o yaml
```

```text
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}},"storageClassName":"standard"},"storageType":"Durable","deletionPolicy":"WipeOut","version":"11.8.5"}}      
  creationTimestamp: "2021-03-10T04:31:09Z"
  finalizers:
  - kubedb.com
  generation: 2
  ...
  name: sample-mariadb
  namespace: demo
  resourceVersion: "7952"
  selfLink: /apis/kubedb.com/v1/namespaces/demo/mariadbs/sample-mariadb
  uid: 412a4739-ac65-4b5a-a943-5e148f3222b1
spec:
  authSecret:
    name: sample-mariadb-auth
  ...
  replicas: 1
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
    storageClassName: standard
  storageType: Durable
  deletionPolicy: Delete
  version: 12.1.2
status:
  observedGeneration: 2
  phase: Ready
```

## Connect with MariaDB database

KubeDB operator has created a new Secret called `mariadb-quickstart-auth` *(format: {mariadb-object-name}-auth)* for storing the password for `mariadb` superuser. This secret contains a `username` key which contains the *username* for MariaDB superuser and a `password` key which contains the *password* for MariaDB superuser.

If you want to use an existing secret please specify that when creating the MariaDB object using `spec.authSecret.name`. While creating this secret manually, make sure the secret contains these two keys containing data `username` and `password` and also make sure of using `root` as value of `username`.

Now, we need `username` and `password` to connect to this database from `kubeclt exec` command. In this example, `sample-mariadb-auth` secret holds username and password.

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d
w*yOU$b53dTbjsjJ
```

We will exec into the pod `sample-mariadb-0` and conncet to the database using `username` and `password`.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- mariadb -u root --password='w*yOU$b53dTbjsjJ'
```

```mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 335
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.001 sec)
```

## Database DeletionPolicy

This field is used to regulate the deletion process of the related resources when `MariaDB` object is deleted. User can set the value of this field according to their needs. The available options and their use case scenario is described below:

**DoNotTerminate:**

When `deletionPolicy` is set to `DoNotTerminate`, KubeDB takes advantage of `ValidationWebhook` feature in Kubernetes 1.9.0 or later clusters to implement `DoNotTerminate` feature. If admission webhook is enabled, It prevents users from deleting the database as long as the `spec.deletionPolicy` is set to `DoNotTerminate`. If you create a database with `deletionPolicy` `DoNotTerminate` and try to delete it, you will see this:

```bash
$ kubectl delete mariadb sample-mariadb -n demo
Error from server (BadRequest): admission webhook "mariadb.validators.kubedb.com" denied the request: mariadb "mariadb-quickstart" can't be halted. To delete, change spec.deletionPolicy
```

Now, run `kubectl edit mariadb sample-mariadb -n demo` to set `spec.deletionPolicy` to `Halt` (which deletes the mariadb object and keeps PVC, snapshots, Secrets intact) or remove this field (which default to `Delete`). Then you will be able to delete/halt the database.

**Halt:**

Suppose you want to reuse your database volume and credential to deploy your database in future using the same configurations. But, right now you just want to delete the database except the database volumes and credentials. In this scenario, you must set the `MariaDB` object `deletionPolicy` to `Halt`.

When the `DeletionPolicy` is set to `Halt` and the MariaDB object is deleted, the KubeDB operator will delete the PetSet and its pods but leaves the `PVCs`, `secrets` and database backup data(`snapshots`) intact. You can set the `deletionPolicy` to `Halt` in existing database using `edit` command for testing.

At first, run `kubectl edit mariadb sample-mariadb -n demo` to set `spec.deletionPolicy` to `Halt`. Then delete the mariadb object,

```bash
$ kubectl delete mariadb sample-mariadb -n demo
mariadb.kubedb.com "sample-mariadb" deleted
```

Now, run the following command to get all mariadb resources in `demo` namespaces,

```bash
$ kubectl get petset,svc,secret,pvc -n demo
NAME                         TYPE                                  DATA   AGE
secret/default-token-w2pgw   kubernetes.io/service-account-token   3      31m
secret/sample-mariadb-auth   kubernetes.io/basic-auth              2      39s

NAME                                          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-sample-mariadb-0   Bound    pvc-7502c222-2b02-4363-9027-91ab0e7b76dc   1Gi        RWO            standard       39s
```

From the above output, you can see that all mariadb resources(`PetSet`, `Service`, etc.) are deleted except `PVC` and `Secret`. You can recreate your mariadb again using this resources.

**Delete:**

If you want to delete the existing database along with the volumes used, but want to restore the database from previously taken `snapshots` and `secrets` then you might want to set the `MariaDB` object `deletionPolicy` to `Delete`. In this setting, `PetSet` and the volumes will be deleted. If you decide to restore the database, you can do so using the snapshots and the credentials.

When the `DeletionPolicy` is set to `Delete` and the MariaDB object is deleted, the KubeDB operator will delete the PetSet and its pods along with PVCs but leaves the `secret` and database backup data(`snapshots`) intact.

Suppose, we have a database with `deletionPolicy` set to `Delete`. Now, are going to delete the database using the following command:

```bash
$ kubectl delete mariadb sample-mariadb -n demo
mariadb.kubedb.com "sample-mariadb" deleted
```

Now, run the following command to get all mariadb resources in `demo` namespaces,

```bash
$ kubectl get petset,svc,secret,pvc -n demo
NAME                         TYPE                                  DATA   AGE
secret/default-token-w2pgw   kubernetes.io/service-account-token   3      31m
secret/sample-mariadb-auth   kubernetes.io/basic-auth              2      39s
```

From the above output, you can see that all mariadb resources(`PetSet`, `Service`, `PVCs` etc.) are deleted except `Secret`. You can initialize your mariadb using `snapshots`(if previously taken) and `secret`.

> If you don’t set the deletionPolicy then the kubeDB set the DeletionPolicy to Delete by-default.

**WipeOut:**

You can totally delete the `MariaDB` database and relevant resources without any tracking by setting `deletionPolicy` to `WipeOut`. KubeDB operator will delete all relevant resources of this `MariaDB` database (i.e, `PVCs`, `Secrets`, `Snapshots`) when the `deletionPolicy` is set to `WipeOut`.

Suppose, we have a database with `deletionPolicy` set to `WipeOut`. Now, are going to delete the database using the following command:

```bash
$ kubectl delete mariadb sample-mariadb -n demo
```

```yaml
mariadb.kubedb.com "sample-mariadb" deleted
```

Now, run the following command to get all mariadb resources in `demo` namespaces,

```bash
$ kubectl get petset,svc,secret,pvc -n demo
No resources found in demo namespace.
```

From the above output, you can see that all mariadb resources are deleted. there is no option to recreate/reinitialize your database if `deletionPolicy` is set to `Delete`.

> Be careful when you set the `deletionPolicy` to `Delete`. Because there is no option to trace the database resources if once deleted the database.

## Database Halted

If you want to delete MariaDB resources(`PetSet`,`Service`, etc.) without deleting the `MariaDB` object, `PVCs` and `Secret` you have to set the `spec.halted` to `true`. KubeDB operator will be able to delete the MariaDB related resources except the `MariaDB` object, `PVCs` and `Secret`.

Suppose we have a database running `mariadb-quickstart` in our cluster. Now, we are going to set `spec.halted` to `true` in `MariaDB` object by running `kubectl edit -n demo mariadb-quickstart` command.

Run the following command to get MariaDB resources,

```bash
$ kubectl get mariadb,sts,secret,svc,pvc -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-quickstart   11.8.5    Halted   22m

NAME                           TYPE                                  DATA   AGE
secret/default-token-lgbjm     kubernetes.io/service-account-token   3      27h
secret/mariadb-quickstart-auth   Opaque                                2      22m

NAME                                            STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-mariadb-quickstart-0   Bound    pvc-7ab0ebb0-bb2e-45c1-9af1-4f175672605b   1Gi        RWO            standard       22m
```

From the above output , you can see that `MariaDB` object, `PVCs`, `Secret` are still alive. Then you can recreate your `MariaDB` with same configuration.

> When you set `spec.halted` to `true` in `MariaDB` object then the `deletionPolicy` is also set to `Halt` by KubeDB operator.

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete -n demo mariadb/sample-mariadb

kubectl delete ns demo
```

## Tips for Testing

If you are just testing some basic functionalities, you might want to avoid additional hassles due to some safety features that are great for production environment. You can follow these tips to avoid them.

1. **Use `storageType: Ephemeral`**. Databases are precious. You might not want to lose your data in your production environment if database pod fail. So, we recommend to use `spec.storageType: Durable` and provide storage spec in `spec.storage` section. For testing purpose, you can just use `spec.storageType: Ephemeral`. KubeDB will use [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) for storage. You will not require to provide `spec.storage` section.
2. **Use `deletionPolicy: WipeOut`**. It is nice to be able to delete everything created by KubeDB for a particular MariaDB crd when you delete the crd.

## Next Steps

* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: recommendation/recommendation.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Recommendation

## Overview

A `Recommendation` is a Kubernetes-native CRD created by the **KubeDB Ops-Manager** and reconciled by the **KubeDB Supervisor**. For a MariaDB instance managed by KubeDB, the Ops-Manager watches the database’s state and emits a Recommendation whenever it detects an action you should take — a newer version, an expiring TLS certificate, or an authentication secret nearing its rotation deadline.

Nothing runs until the Recommendation is approved — either by you (`status.approvalStatus: Approved`) or automatically through an `ApprovalPolicy` bound to a `MaintenanceWindow`. Once approved, the Supervisor creates the corresponding `MariaDBOpsRequest` and tracks it to completion.

This page is the **MariaDB-specific intro**: which recommendations apply to MariaDB and which spec fields trigger them. For prerequisites, Helm flags that control generation timing, and the full Recommendation lifecycle, see:

* [Recommendation Configuration](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/configuration) — prerequisites, Supervisor CRD install, and all Helm flags.
* [Recommendation Overview](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation) — architecture and lifecycle walkthrough.

![Recommendation Lifecycle](images/recommendation_recommendation_recommendation-generation.png)

---

## Relevant KubeDB concepts

* [MariaDBOpsRequest](en/concepts/opsrequest.md)
* [MariaDBRotateAuth](en/rotate-auth/overview.md)
* [MariaDBReconfigureTLS](en/tls/overview.md)
* [MariaDBUpdateVersion](en/update-version/overview.md)

---

## Recommendation types for MariaDB

| Type | Triggered when | Walkthrough |
| --- | --- | --- |
| **Version Update** | A newer major, minor, or patch version becomes available | [Version Update Recommendation](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/version-update-recommendation) |
| **Same-Version Update** | The container image for your *current* version is refreshed (e.g. security patch) | [Version Update Recommendation](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/version-update-recommendation) |
| **TLS Certificate Rotation** | An issued certificate is approaching its expiry threshold | [TLS Certificate Rotation Recommendation](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/rotate-tls-recommendation) |
| **Authentication Secret Rotation** | The auth secret is approaching its `rotateAfter` deadline | [Authentication Secret Rotation Recommendation](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/rotate-auth-recommendation) |

---

## Triggers specific to MariaDB

This section shows the minimal MariaDB CR fields that cause each recommendation to be generated. For deeper, end-to-end walkthroughs use the links in the table above.

### Authentication Secret Rotation

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
  authSecret:
    kind: Secret
    name: mariadb-auth
    rotateAfter: 1h
```

In this configuration:

* The `rotateAfter` field defines how long the authentication secret remains valid

KubeDB monitors the configured lifecycle and generates a RotateAuth Recommendation based on the following conditions:

* If the secret lifespan is greater than one month, a recommendation is generated when less than one month of validity remains
* If the secret lifespan is less than one month, a recommendation is generated when approximately one-third of its validity remains

Once approved, KubeDB creates an opsrequest to rotate the credentials automatically, ensuring:

* No expired credentials
* Improved security posture
* Reduced manual intervention

### TLS Certificate Rotation

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: mariadb-ca-issuer
    certificates:
      - alias: client
        duration: 1h20m
      - alias: server
        duration: 2h10m
```

In this configuration:

* The `spec.tls.certificates.duration` field defines how long each certificate remains valid

KubeDB monitors the configured lifecycle and generates a RotateTLS Recommendation based on the following conditions:

* If the certificate duration is greater than one month, a recommendation is generated when less than one month of validity remains
* If the certificate duration is less than one month, a recommendation is generated when approximately one-third of its validity remains

Once approved, KubeDB creates an opsrequest to reconfigure TLS automatically, ensuring:

* Continuous secure communication
* No unexpected certificate expiry
* Seamless certificate renewal

### Version Update

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
```

In this configuration:

* KubeDB monitors the running version of the database

KubeDB monitors the configured lifecycle and generates a VersionUpdate Recommendation based on the following conditions:

* If a newer container image is available for the current version, a recommendation is generated
* If a patch version is released, a recommendation is generated
* If a newer minor or major version becomes available, a recommendation is generated
* If changes are introduced in the existing version image (e.g., security fixes or image updates without a version bump), a recommendation is generated

For example: Recommending version update from `10.5.23` to `10.6.16`

Once approved, KubeDB creates an opsrequest to perform the version upgrade automatically, ensuring:

* Timely adoption of security patches and fixes
* Access to new features and improvements
* Consistent performance and stability across deployments

### Same-Version Update

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb-recommendation
  namespace: demo
spec:
  version: "10.5.23"
```

In this configuration:

* KubeDB monitors the container image of the current database version

KubeDB monitors the configured lifecycle and generates a SameVersionUpdate Recommendation based on the following conditions:

* If the container image backing the current version is updated (e.g., security patches or rebuilds without a version change), a recommendation is generated

Once approved, KubeDB creates an opsrequest to update the running workload automatically, ensuring:

* Security patches are applied without requiring a version upgrade
* Consistency with the latest available container image
* Improved reliability and maintainability

---

For prerequisites, Helm configuration flags, and the full cross-database Recommendation lifecycle, see the [Recommendation Configuration](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation/configuration) and [Recommendation Overview](https://kubedb.com/docs/v2026.7.10/operatormanual/recommendation) in the operator manual.

<!-- PAGE_START: reconfigure-tls/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigure MariaDB TLS/SSL (Transport Encryption)

KubeDB supports reconfigure i.e. add, remove, update and rotation of TLS/SSL certificates for existing MariaDB database via a MariaDBOpsRequest. This tutorial will show you how to use KubeDB to reconfigure TLS/SSL encryption.

## Before You Begin

* At first, you need to have a Kubernetes Cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install [`cert-manger`](https://cert-manager.io/docs/installation/) v1.6.0 or later to your cluster to manage your SSL/TLS certificates.
* Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Add TLS to a MariaDB Cluster

Here, We are going to create a MariaDB database without TLS and then reconfigure the database to use TLS.

> **Note:** Steps for reconfiguring TLS of MariaDB `Standalone` is same as MariaDB `Cluster`.

### Deploy MariaDB without TLS

In this section, we are going to deploy a MariaDB Cluster database without TLS. In the next few sections we will reconfigure TLS using `MariaDBOpsRequest` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
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

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    9m17s
```

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d
U6(h_pYrekLZ2OOd

$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb  -- bash
```

```mysql
root@sample-mariadb-0:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 108
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  show variables like '%ssl%';
+---------------------+-----------------------------+
| Variable_name       | Value                       |
+---------------------+-----------------------------+
| have_openssl        | YES                         |
| have_ssl            | DISABLED                    |
| ssl_ca              |                             |
| ssl_capath          |                             |
| ssl_cert            |                             |
| ssl_cipher          |                             |
| ssl_crl             |                             |
| ssl_crlpath         |                             |
| ssl_key             |                             |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020 |
+---------------------+-----------------------------+
10 rows in set (0.001 sec)
```

We can verify from the above output that TLS is disabled for this database.

### Create Issuer/ ClusterIssuer

Now, we are going to create an example `Issuer` that will be used throughout the duration of this tutorial. Alternatively, you can follow this [cert-manager tutorial](https://cert-manager.io/docs/configuration/ca/) to create your own `Issuer`. By following the below steps, we are going to create our desired issuer,

* Start off by generating our ca-certificates using openssl,

```bash
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./ca.key -out ./ca.crt -subj "/CN=mariadb/O=kubedb"
Generating a RSA private key
...........................................................................+++++
........................................................................................................+++++
writing new private key to './ca.key'
```

* create a secret using the certificate files we have just generated,

```bash
kubectl create secret tls md-ca \
     --cert=ca.crt \
     --key=ca.key \
     --namespace=demo
secret/md-ca created
```

Now, we are going to create an `Issuer` using the `md-ca` secret that hols the ca-certificate we have just created. Below is the YAML of the `Issuer` cr that we are going to create,

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: md-issuer
  namespace: demo
spec:
  ca:
    secretName: md-ca
```

Let’s create the `Issuer` cr we have shown above,

```bash
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10//docs/guides/mariadb/reconfigure-tls/cluster/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

### Create MariaDBOpsRequest

In order to add TLS to the database, we have to create a `MariaDBOpsRequest` CRO with our created issuer. Below is the YAML of the `MariaDBOpsRequest` CRO that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-add-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    requireSSL: true
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
```

Here,

* `spec.databaseRef.name` specifies that we are performing reconfigure TLS operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `ReconfigureTLS` on our database.
* `spec.tls.issuerRef` specifies the issuer name, kind and api group.
* `requireSSL` specifies that the clients connecting to the server are required to use secured connection.
* `spec.tls.certificates` specifies the certificates. You can learn more about this field from [here](en/concepts/mariadb.md#spectls).

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-add-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-add-tls created
```

#### Verify TLS Enabled Successfully

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME            TYPE             STATUS       AGE
demo        mdops-add-tls   ReconfigureTLS   Successful   6m6s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded.

Now, we are going to connect to the database for verifying the `MariaDB` server has configured with TLS/SSL encryption.

Let’s exec into the pod to verify TLS/SSL configuration,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
```

```bash
root@sample-mariadb-0:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 58
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.005 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.005 sec)

MariaDB [(none)]> quit;
Bye
```

We can see from the above output that, `have_ssl` is set to `ture`. So, database TLS is enabled successfully to this database.

> Note: Add or Update reconfigure TLS with with `RequireSSL=true` will create downtime of the database while `MariaDBOpsRequest` is in `Progressing` status.

## Rotate Certificate

Now we are going to rotate the certificate of this database. First let’s check the current expiration date of the certificate.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/ openssl x509 -in /etc/mysql/certs/client/tls.crt -inform  PEM -enddate -nameopt RFC2253 -noout
notAfter=Apr 13 05:18:43 2022 GMT
```

So, the certificate will expire on this time `Apr 13 05:18:43 2022 GMT`.

### Create MariaDBOpsRequest

Now we are going to increase it using a MariaDBOpsRequest. Below is the yaml of the ops request that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    rotateCertificates: true
```

Here,

* `spec.databaseRef.name` specifies that we are performing reconfigure TLS operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `ReconfigureTLS` on our database.
* `spec.tls.rotateCertificates` specifies that we want to rotate the certificate of this database.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-rotate-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-rotate-tls created
```

#### Verify Certificate Rotated Successfully

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME               TYPE             STATUS       AGE
demo        mdops-rotate-tls   ReconfigureTLS   Successful    3m
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, let’s check the expiration date of the certificate.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/# openssl x509 -in /etc/mysql/certs/client/tls.crt -inform  PEM -enddate -nameopt RFC2253 -noout
notAfter=Apr 13 06:04:50 2022 GMT
```

As we can see from the above output, the certificate has been rotated successfully.

## Update Certificate

Now, we are going to update the server certificate.

* Let’s describe the server certificate `sample-mariadb-server-cert`

```bash
$ kubectl describe certificate -n demo sample-mariadb-server-cert
Name:         sample-mariadb-server-cert
Namespace:    demo
Labels:       app.kubernetes.io/component=database
              app.kubernetes.io/instance=sample-mariadb
              app.kubernetes.io/managed-by=kubedb.com
              app.kubernetes.io/name=mariadbs.kubedb.com
Annotations:  <none>
API Version:  cert-manager.io/v1
Kind:         Certificate
Metadata:
  Creation Timestamp:  2022-01-13T05:18:42Z
  Generation:          1
  ...
  Owner References:
    API Version:           kubedb.com/v1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  MariaDB
    Name:                  sample-mariadb
    UID:                   ed8f45c7-7caf-4890-8a9c-b8437b6ca48b
  Resource Version:        241340
  UID:                     3343e971-395d-46df-9536-47194eb96dcc
Spec:
  Common Name:  sample-mariadb.demo.svc
  Dns Names:
    *.sample-mariadb-pods.demo.svc
    *.sample-mariadb-pods.demo.svc.cluster.local
    *.sample-mariadb.demo.svc
    localhost
    sample-mariadb
    sample-mariadb.demo.svc
  Ip Addresses:
    127.0.0.1
  Issuer Ref:
    Group:      cert-manager.io
    Kind:       Issuer
    Name:       md-issuer
  Secret Name:  sample-mariadb-server-cert
  Subject:
    Organizations:
      kubedb:server
  Usages:
    digital signature
    key encipherment
    server auth
    client auth
Status:
  Conditions:
    Last Transition Time:  2022-01-13T05:18:43Z
    Message:               Certificate is up to date and has not expired
    Observed Generation:   1
    Reason:                Ready
    Status:                True
    Type:                  Ready
  Not After:               2022-04-13T06:04:50Z
  Not Before:              2022-01-13T06:04:50Z
  Renewal Time:            2022-03-14T06:04:50Z
  Revision:                6
Events:
  Type    Reason     Age                From          Message
  ----    ------     ----               ----          -------
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-8tnj5"
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-fw6sk"
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-cvphm"
  Normal  Requested  20m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-nvhp6"
  Normal  Requested  19m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-p5287"
  Normal  Reused     19m (x5 over 22m)  cert-manager  Reusing private key stored in existing Secret resource "sample-mariadb-server-cert"
  Normal  Issuing    19m (x6 over 65m)  cert-manager  The certificate has been successfully issued
```

We want to add `subject` and `emailAddresses` in the spec of server sertificate.

### Create MariaDBOpsRequest

Below is the YAML of the `MariaDBOpsRequest` CRO that we are going to create ton update the server certificate,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-update-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      emailAddresses:
      - "[email protected]"
```

Here,

* `spec.databaseRef.name` specifies that we are performing reconfigure TLS operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `ReconfigureTLS` on our database.
* `spec.tls.issuerRef` specifies the issuer name, kind and api group.
* `spec.tls.certificates` specifies the changes that we want in certificate objects.
* `spec.tls.certificates[].alias` specifies the certificate type which is one of these: `server`, `client`, `metrics-exporter`.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-update-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-update-tls created
```

#### Verify certificate is updated successfully

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                  TYPE             STATUS        AGE
mdops-update-tls   ReconfigureTLS     Successful      7m
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded.

Now, Let’s exec into a database node and find out the ca subject to see if it matches the one we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0  -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/ openssl x509 -in /etc/mysql/certs/server/tls.crt -inform PEM  -subject -email -nameopt RFC2253 -noout
subject=CN=sample-mariadb.demo.svc,O=kubedb:server
[email protected]
```

We can see from the above output that, the subject name and email address match with the new ca certificate that we have created. So, the issuer is changed successfully.

## Remove TLS from the Database

Now, we are going to remove TLS from this database using a MariaDBOpsRequest.

### Create MariaDBOpsRequest

Below is the YAML of the `MariaDBOpsRequest` CRO that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-remove-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    remove: true
```

Here,

* `spec.databaseRef.name` specifies that we are performing reconfigure TLS operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `ReconfigureTLS` on our database.
* `spec.tls.remove` specifies that we want to remove tls from this database.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-remove-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-remove-tls created
```

#### Verify TLS Removed Successfully

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME               TYPE             STATUS       AGE
demo        mdops-remove-tls   ReconfigureTLS   Successful   6m27s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed.

Now, Let’s exec into the database and find out that TLS is disabled or not.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb  -- bash
root@sample-mariadb-0:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 108
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  show variables like '%ssl%';
+---------------------+-----------------------------+
| Variable_name       | Value                       |
+---------------------+-----------------------------+
| have_openssl        | YES                         |
| have_ssl            | DISABLED                    |
| ssl_ca              |                             |
| ssl_capath          |                             |
| ssl_cert            |                             |
| ssl_cipher          |                             |
| ssl_crl             |                             |
| ssl_crlpath         |                             |
| ssl_key             |                             |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020 |
+---------------------+-----------------------------+
10 rows in set (0.001 sec)
```

So, we can see from the above that, output that tls is disabled successfully.

## Cleaning up

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo --all
$ kubectl delete issuer -n demo --all
$ kubectl delete mariadbopsrequest -n demo --all
$ kubectl delete ns demo
```

<!-- PAGE_START: reconfigure-tls/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Reconfiguring TLS of MariaDB Database

This guide will give an overview on how KubeDB Ops Manager reconfigures TLS configuration i.e. add TLS, remove TLS, update issuer/cluster issuer or Certificates and rotate the certificates of a `MariaDB` database.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Reconfiguring MariaDB TLS Configuration Process Works

The following diagram shows how KubeDB Ops Manager reconfigures TLS of a `MariaDB` database. Open the image in a new tab to see the enlarged version.

  ![Reconfiguring TLS process of MariaDB](images/reconfigure-tls_overview_reconfigure-tls.jpeg)

Fig: Reconfiguring TLS process of MariaDB

The Reconfiguring MariaDB TLS process consists of the following steps:

1. At first, a user creates a `MariaDB` Custom Resource Object (CRO).
2. `KubeDB` Community operator watches the `MariaDB` CRO.
3. When the operator finds a `MariaDB` CR, it creates required number of `PetSets` and related necessary stuff like secrets, services, etc.
4. Then, in order to reconfigure the TLS configuration of the `MariaDB` database the user creates a `MariaDBOpsRequest` CR with desired information.
5. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CR.
6. When it finds a `MariaDBOpsRequest` CR, it pauses the `MariaDB` object which is referred from the `MariaDBOpsRequest`. So, the `KubeDB` Community operator doesn’t perform any operations on the `MariaDB` object during the reconfiguring TLS process.
7. Then the `KubeDB` Enterprise operator will add, remove, update or rotate TLS configuration based on the Ops Request yaml.
8. Then the `KubeDB` Enterprise operator will restart all the Pods of the database so that they restart with the new TLS configuration defined in the `MariaDBOpsRequest` CR.
9. After the successful reconfiguring of the `MariaDB` TLS, the `KubeDB` Enterprise operator resumes the `MariaDB` object so that the `KubeDB` Community operator resumes its usual operations.

In the next docs, we are going to show a step by step guide on reconfiguring TLS configuration of a MariaDB database using `MariaDBOpsRequest` CRD.

<!-- PAGE_START: reconfigure/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigure MariaDB Cluster Database

This guide will show you how to use `KubeDB` Enterprise operator to reconfigure a MariaDB Cluster.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install `KubeDB` Community and Enterprise operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDB Cluster](en/clustering/galera-cluster.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Reconfigure Overview](en/reconfigure/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

Now, we are going to deploy a `MariaDB` Cluster using a supported version by `KubeDB` operator. Then we are going to apply `MariaDBOpsRequest` to reconfigure its configuration.

### Prepare MariaDB Cluster

Now, we are going to deploy a `MariaDB` Cluster database with version `12.1.2`.

### Deploy MariaDB

At first, we will create `md-config.cnf` file containing required configuration settings.

```ini
$ cat md-config.cnf 
[mysqld]
max_connections = 200
read_buffer_size = 1048576
```

Here, `max_connections` is set to `200`, whereas the default value is `151`. Likewise, `read_buffer_size` has the deafult value `131072`.

Now, we will create a secret with this configuration file.

```bash
$ kubectl create secret generic -n demo md-configuration --from-file=./md-config.cnf
secret/md-configuration created
```

In this section, we are going to create a MariaDB object specifying `spec.configuration` field to apply this custom configuration. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  configuration:
    secretName: md-configuration
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

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/sample-mariadb-config.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo 
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    71s
```

Now, we will check if the database has started with the custom configuration we have provided.

First we need to get the username and password to connect to a mariadb instance,

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d                                                                       
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d                                                                         
nrKuxni0wDSMrgwy
```

Now, we will check if the database has started with the custom configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is same as provided 
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 200   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1048576 |
+------------------+---------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from the configuration of ready mariadb, the value of `max_connections` has been set to `200` and `read_buffer_size` has been set to `1048576`.

### Reconfigure using new config secret

Now we will reconfigure this database to set `max_connections` to `250` and `read_buffer_size` to `122880`.

Now, we will create new file `new-md-config.cnf` containing required configuration settings.

```ini
$ cat new-md-config.cnf 
[mysqld]
max_connections = 250
read_buffer_size = 122880
```

Then, we will create a new secret with this configuration file.

```bash
$ kubectl create secret generic -n demo new-md-configuration --from-file=./new-md-config.cnf
secret/new-md-configuration created
```

#### Create MariaDBOpsRequest

Now, we will use this secret to replace the previous secret using a `MariaDBOpsRequest` CR. The `MariaDBOpsRequest` yaml is given below,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-config
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    configSecret:
      name: new-md-configuration
```

Here,

* `spec.databaseRef.name` specifies that we are reconfiguring `sample-mariadb` database.
* `spec.type` specifies that we are performing `Reconfigure` on our database.
* `spec.configuration.configSecret.name` specifies the name of the new secret.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/reconfigure-using-secret.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-config created
```

#### Verify the new configuration is working

If everything goes well, `KubeDB` Enterprise operator will update the `configuration.secretName` of `MariaDB` object.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-config   Reconfigure   Successful   3m8s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to reconfigure the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-reconfigure-config
Name:         mdops-reconfigure-config
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-06-10T04:43:50Z
  Generation:          1
  Resource Version:  1123451
  UID:               27a73fc6-1d25-4019-8975-f7d4daf782b7
Spec:
  Configuration:
    Config Secret:
      Name:  new-md-configuration
  Database Ref:
    Name:  sample-mariadb
  Type:    Reconfigure
Status:
  Conditions:
    Last Transition Time:  2022-06-10T04:43:50Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-10T04:47:25Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-10T04:47:30Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-10T04:47:30Z
    Message:               Controller has successfully reconfigure the MariaDB demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the new configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is same as provided 
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 250   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 122880  |
+------------------+---------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from the configuration has changed, the value of `max_connections` has been changed from `200` to `250` and and the `read_buffer_size` has been changed `1048576` to `122880`. So the reconfiguration of the database is successful.

### Reconfigure Existing Config Secret

Now, we will create a new `MariaDBOpsRequest` to reconfigure our existing secret `new-md-configuration` by modifying our `new-md-config.cnf` file using `applyConfig`. The `MariaDBOpsRequest` yaml is given below,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-apply-config
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    applyConfig:
      new-md-config.cnf: |
        [mysqld]
        max_connections = 230
        read_buffer_size = 1064960        
      innodb-config.cnf: |
        [mysqld]
        innodb_log_buffer_size = 17408000
```

> Note: You can modify multiple fields of your current configuration using `applyConfig`. If you don’t have any secrets then `applyConfig` will create a secret for you. Here, we modified value of our two existing fields which are `max_connections` and `read_buffer_size` also, we modified a new field `innodb_log_buffer_size` of our configuration.

Here,

* `spec.databaseRef.name` specifies that we are reconfiguring `sample-mariadb` database.
* `spec.type` specifies that we are performing `Reconfigure` on our database.
* `spec.configuration.applyConfig` contains the configuration of existing or newly created secret.

Before applying this yaml we are going to check the existing value of our new field,

```bash
$ kubectl exec -it sample-mariadb-0 -n demo -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 16777216 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Here, we can see the default value for `innodb_log_buffer_size` is `16777216`.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/mdops-reconfigure-apply-config.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-apply-config created
```

#### Verify the new configuration is working

If everything goes well, `KubeDB` operator will update the `configuration.secretName` of `MariaDB` object.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest mdops-reconfigure-apply-config -n demo
NAME                             TYPE          STATUS       AGE
mdops-reconfigure-apply-config   Reconfigure   Successful   4m59s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to reconfigure the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-reconfigure-apply-config
Name:         mdops-reconfigure-apply-config
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-06-10T09:13:49Z
  Generation:          1
  Resource Version:  14120
  UID:               eb8d5df5-a0ce-4011-890c-c18c0200b5ac
Spec:
  Configuration:
    Apply Config:
      innodb-config.cnf:  [mysqld]
innodb_log_buffer_size = 17408000

      new-md-config.cnf:  [mysqld]
max_connections = 230
read_buffer_size = 1064960

  Database Ref:
    Name:  sample-mariadb
  Type:    Reconfigure
Status:
  Conditions:
    Last Transition Time:  2022-06-10T09:13:49Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-10T09:13:49Z
    Message:               Successfully prepared user provided custom config secret
    Observed Generation:   1
    Reason:                PrepareSecureCustomConfig
    Status:                True
    Type:                  PrepareCustomConfig
    Last Transition Time:  2022-06-10T09:17:24Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-10T09:17:29Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-10T09:17:29Z
    Message:               Controller has successfully reconfigure the MariaDB demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the new configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is same as provided 
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 230   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1064960 |
+------------------+---------+
1 row in set (0.001 sec)

# value of `innodb_log_buffer_size` is same as provided
MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 17408000 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from above the configuration has been changed, the value of `max_connections` has been changed from `250` to `230` and the `read_buffer_size` has been changed `122880` to `1064960` also, `innodb_log_buffer_size` has been changed from `16777216` to `17408000`. So the reconfiguration of the `sample-mariadb` database is successful.

### Remove Custom Configuration

We can also remove exisiting custom config using `MariaDBOpsRequest`. Provide `true` to field `spec.configuration.removeCustomConfig` and make an Ops Request to remove existing custom configuration.

#### Create MariaDBOpsRequest

Lets create an `MariaDBOpsRequest` having `spec.configuration.removeCustomConfig` is equal `true`,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-remove
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    removeCustomConfig: true
```

Here,

* `spec.databaseRef.name` specifies that we are reconfiguring `mdops-reconfigure-remove` database.
* `spec.type` specifies that we are performing `Reconfigure` on our database.
* `spec.configuration.removeCustomConfig` is a bool field that should be `true` when you want to remove existing custom configuration.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/cluster/examples/reconfigure-remove.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-remove created
```

#### Verify the new configuration is working

If everything goes well, `KubeDB` operator will update the `configuration.secretName` of `MariaDB` object.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-remove   Reconfigure   Successful   2m1s
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the new configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 23
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is default
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 151   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is default
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 131072  |
+------------------+---------+
1 row in set (0.001 sec)

# value of `innodb_log_buffer_size` is default
MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 16777216 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from the configuration has changed to its default value. So removal of existing custom configuration using `MariaDBOpsRequest` is successful.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-reconfigure-config mdops-reconfigure-apply-config mdops-reconfigure-remove
$ kubectl delete ns demo
```

<!-- PAGE_START: reconfigure/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Reconfiguring MariaDB

This guide will give an overview on how KubeDB Ops Manger reconfigures `MariaDB`.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Reconfiguring MariaDB Process Works

The following diagram shows how KubeDB Ops Manager reconfigures `MariaDB` database components. Open the image in a new tab to see the enlarged version.

  ![Reconfiguring process of MariaDB](images/reconfigure_overview_reconfigure.jpeg)

Fig: Reconfiguring process of MariaDB

The Reconfiguring MariaDB process consists of the following steps:

1. At first, a user creates a `MariaDB` Custom Resource (CR).
2. `KubeDB` Community operator watches the `MariaDB` CR.
3. When the operator finds a `MariaDB` CR, it creates required number of `PetSets` and related necessary stuff like secrets, services, etc.
4. Then, in order to reconfigure the `MariaDB` standalone or cluster the user creates a `MariaDBOpsRequest` CR with desired information.
5. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CR.
6. When it finds a `MariaDBOpsRequest` CR, it halts the `MariaDB` object which is referred from the `MariaDBOpsRequest`. So, the `KubeDB` Community operator doesn’t perform any operations on the `MariaDB` object during the reconfiguring process.
7. Then the `KubeDB` Enterprise operator will replace the existing configuration with the new configuration provided or merge the new configuration with the existing configuration according to the `MariaDBOpsRequest` CR.
8. Then the `KubeDB` Enterprise operator will restart the related PetSet Pods so that they restart with the new configuration defined in the `MariaDBOpsRequest` CR.
9. After the successful reconfiguring of the `MariaDB`, the `KubeDB` Enterprise operator resumes the `MariaDB` object so that the `KubeDB` Community operator resumes its usual operations.

In the next docs, we are going to show a step by step guide on reconfiguring MariaDB database components using `MariaDBOpsRequest` CRD.

<!-- PAGE_START: reconfigure/standalone.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigure MariaDB Standalone Database

This guide will show you how to use `KubeDB` Enterprise operator to reconfigure a MariaDB Standalone.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install `KubeDB` Community and Enterprise operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Reconfigure Overview](en/reconfigure/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

Now, we are going to deploy a `MariaDB` Standalone using a supported version by `KubeDB` operator. Then we are going to apply `MariaDBOpsRequest` to reconfigure its configuration.

### Prepare MariaDB Standalone

Now, we are going to deploy a `MariaDB` Standalone database with version `12.1.2`.

### Deploy MariaDB

At first, we will create `md-config.cnf` file containing required configuration settings.

```ini
$ cat md-config.cnf 
[mysqld]
max_connections = 200
read_buffer_size = 1048576
```

Here, `max_connections` is set to `200`, whereas the default value is `151`. Likewise, `read_buffer_size` has the deafult value `131072`.

Now, we will create a secret with this configuration file.

```bash
$ kubectl create secret generic -n demo md-configuration --from-file=./md-config.cnf
secret/md-configuration created
```

In this section, we are going to create a MariaDB object specifying `spec.configuration` field to apply this custom configuration. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  configuration:
    secretName: md-configuration
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

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/sample-mariadb-config.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo 
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    61s
```

Now, we will check if the database has started with the custom configuration we have provided.

First we need to get the username and password to connect to a mariadb instance,

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d                                                                       
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d                                                                         
PlWA6JNLkNFudl4I
```

Now, we will check if the database has started with the custom configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 200   |
+-----------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1048576 |
+------------------+---------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from the configuration of ready mariadb, the value of `max_connections` has been set to `200` and `read_buffer_size` has been set to `1048576`.

### Reconfigure using new config secret

Now we will reconfigure this database to set `max_connections` to `250` and `read_buffer_size` to `122880`.

Now, we will create new file `new-md-config.cnf` containing required configuration settings.

```ini
$ cat new-md-config.cnf 
[mysqld]
max_connections = 250
read_buffer_size = 122880
```

Then, we will create a new secret with this configuration file.

```bash
$ kubectl create secret generic -n demo new-md-configuration --from-file=./new-md-config.cnf
secret/new-md-configuration created
```

#### Create MariaDBOpsRequest

Now, we will use this secret to replace the previous secret using a `MariaDBOpsRequest` CR. The `MariaDBOpsRequest` yaml is given below,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-config
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    configSecret:
      name: new-md-configuration
```

Here,

* `spec.databaseRef.name` specifies that we are reconfiguring `mdops-reconfigure-config` database.
* `spec.type` specifies that we are performing `Reconfigure` on our database.
* `spec.configuration.configSecret.name` specifies the name of the new secret.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/reconfigure-using-secret.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-config created
```

#### Verify the new configuration is working

If everything goes well, `KubeDB` Enterprise operator will update the `configSecret` of `MariaDB` object.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-config   Reconfigure   Successful   2m8s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to reconfigure the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-reconfigure-config
Name:         mdops-reconfigure-config
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-06-14T10:56:01Z
  Generation:          1
  Resource Version:  21589
  UID:               43997fe8-fa12-4d38-a29f-d101889d4e72
Spec:
  Configuration:
    Config Secret:
      Name:  new-md-configuration
  Database Ref:
    Name:  sample-mariadb
  Type:    Reconfigure
Status:
  Conditions:
    Last Transition Time:  2022-06-14T10:56:01Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-14T10:56:11Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-14T10:56:16Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-14T10:56:16Z
    Message:               Controller has successfully reconfigure the MariaDB demo/mdops-reconfigure-config
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the new configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 21
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 250   |
+-----------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+--------+
| Variable_name    | Value  |
+------------------+--------+
| read_buffer_size | 122880 |
+------------------+--------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from the configuration has changed, the value of `max_connections` has been changed from `200` to `250` and and the `read_buffer_size` has been changed `1048576` to `122880`. So the reconfiguration of the database is successful.

### Reconfigure Existing Config Secret

Now, we will create a new `MariaDBOpsRequest` to reconfigure our existing secret `new-md-configuration` by modifying our `new-md-config.cnf` file using `applyConfig`. The `MariaDBOpsRequest` yaml is given below,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-apply-config
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    applyConfig:
      new-md-config.cnf: |
        [mysqld]
        max_connections = 230
        read_buffer_size = 1064960        
      innodb-config.cnf: |
        [mysqld]
        innodb_log_buffer_size = 17408000
```

> Note: You can modify multiple fields of your current configuration using `applyConfig`. If you don’t have any secrets then `applyConfig` will create a secret for you. Here, we modified value of our two existing fields which are `max_connections` and `read_buffer_size` also, we modified a new field `innodb_log_buffer_size` of our configuration.

Here,

* `spec.databaseRef.name` specifies that we are reconfiguring `sample-mariadb` database.
* `spec.type` specifies that we are performing `Reconfigure` on our database.
* `spec.configuration.applyConfig` contains the configuration of existing or newly created secret.

Before applying this yaml we are going to check the existing value of our new field,

```bash
$ kubectl exec -it sample-mariadb-0 -n demo -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 21
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 16777216 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

Here, we can see the default value for `innodb_log_buffer_size` is `16777216`.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/mdops-reconfigure-apply-config.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-apply-config created
```

#### Verify the new configuration is working

If everything goes well, `KubeDB` Enterprise operator will update the `configSecret` of `MariaDB` object.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest mdops-reconfigure-apply-config -n demo
NAME                             TYPE          STATUS       AGE
mdops-reconfigure-apply-config   Reconfigure   Successful   3m11s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to reconfigure the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-reconfigure-apply-config
Name:         mdops-reconfigure-apply-config
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-06-14T09:13:49Z
  Generation:          1
  Resource Version:  14120
  UID:               eb8d5df5-a0ce-4011-890c-c18c0200b5ac
Spec:
  Configuration:
    Apply Config:
      innodb-config.cnf:  [mysqld]
innodb_log_buffer_size = 17408000

      new-md-config.cnf:  [mysqld]
max_connections = 230
read_buffer_size = 1064960

  Database Ref:
    Name:  sample-mariadb
  Type:    Reconfigure
Status:
  Conditions:
    Last Transition Time:  2022-06-14T09:13:49Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-06-14T09:13:49Z
    Message:               Successfully prepared user provided custom config secret
    Observed Generation:   1
    Reason:                PrepareSecureCustomConfig
    Status:                True
    Type:                  PrepareCustomConfig
    Last Transition Time:  2022-06-14T09:17:24Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSetPods
    Last Transition Time:  2022-06-14T09:17:29Z
    Message:               Successfully reconfigured MariaDB for MariaDBOpsRequest: demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                SuccessfullyDBReconfigured
    Status:                True
    Type:                  DBReady
    Last Transition Time:  2022-06-14T09:17:29Z
    Message:               Controller has successfully reconfigure the MariaDB demo/mdops-reconfigure-apply-config
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the new configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/# mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 24
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 230   |
+-----------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 1064960 |
+------------------+---------+
1 row in set (0.002 sec)

MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 17408000 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from above the configuration has been changed, the value of `max_connections` has been changed from `250` to `230` and the `read_buffer_size` has been changed `122880` to `1064960` also, `innodb_log_buffer_size` has been changed from `16777216` to `17408000`. So the reconfiguration of the `sample-mariadb` database is successful.

### Remove Custom Configuration

We can also remove exisiting custom config using `MariaDBOpsRequest`. Provide `true` to field `spec.configuration.removeCustomConfig` and make an Ops Request to remove existing custom configuration.

#### Create MariaDBOpsRequest

Lets create an `MariaDBOpsRequest` having `spec.configuration.removeCustomConfig` is equal `true`,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-reconfigure-remove
  namespace: demo
spec:
  type: Reconfigure
  databaseRef:
    name: sample-mariadb
  configuration:   
    removeCustomConfig: true
```

Here,

* `spec.databaseRef.name` specifies that we are reconfiguring `mdops-reconfigure-remove` database.
* `spec.type` specifies that we are performing `Reconfigure` on our database.
* `spec.configuration.removeCustomConfig` is a bool field that should be `true` when you want to remove existing custom configuration.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure/standalone/examples/reconfigure-remove.yaml
mariadbopsrequest.ops.kubedb.com/mdops-reconfigure-remove created
```

#### Verify the new configuration is working

If everything goes well, `KubeDB` Enterprise operator will update the `configSecret` of `MariaDB` object.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME                       TYPE          STATUS       AGE
demo        mdops-reconfigure-remove   Reconfigure   Successful   2m5s
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the new configuration we have provided.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# value of `max_conncetions` is default
MariaDB [(none)]> show variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 151   |
+-----------------+-------+
1 row in set (0.001 sec)

# value of `read_buffer_size` is default
MariaDB [(none)]> show variables like 'read_buffer_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| read_buffer_size | 131072  |
+------------------+---------+
1 row in set (0.001 sec)

# value of `innodb_log_buffer_size` is default
MariaDB [(none)]> show variables like 'innodb_log_buffer_size';
+------------------------+----------+
| Variable_name          | Value    |
+------------------------+----------+
| innodb_log_buffer_size | 16777216 |
+------------------------+----------+
1 row in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

As we can see from the configuration has changed to its default value. So removal of existing custom configuration using `MariaDBOpsRequest` is successful.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-reconfigure-config mdops-reconfigure-apply-config mdops-reconfigure-remove
$ kubectl delete ns demo
```

<!-- PAGE_START: restart/restart.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Restart MariaDB

KubeDB supports restarting the MariaDB database via a `MariaDBOpsRequest`. Restarting is useful if some pods are got stuck in some phase, or they are not working correctly. This tutorial will show you how to use that.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
  namespace/demo created
```

> Note: YAML files used in this tutorial are stored in [docs/examples/MariaDB](https://github.com/kubedb/docs/tree/v2026.7.10/docs/examples/mariadb) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

## Deploy MariaDB

In this section, we are going to deploy a MariaDB database using KubeDB.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/restart/MariaDB.yaml
MariaDB.kubedb.com/mariadb created
```

## Apply Restart opsRequest

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: restart
  namespace: demo
spec:
  type: Restart
  databaseRef:
    name: mariadb
  timeout: 3m
  apply: Always
```

* `spec.type` specifies the Type of the ops Request
* `spec.databaseRef` holds the name of the MariaDB database. The db should be available in the same namespace as the opsRequest
* The `spec.timeout` field specifies the maximum amount of time the operator will wait for the operation to complete before marking it as failed.
* The `spec.apply` field determines whether the operation should always be applied (Always) or if the database phase is ready (IfReady).

> Note: The method of restarting the standalone & cluster mode db is exactly same as above. All you need, is to specify the corresponding MariaDB name in `spec.databaseRef.name` section.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/restart/ops.yaml
MariaDBopsrequest.ops.kubedb.com/restart created
```

In `MariaDB`, all pods act as primary, so the Ops-manager operator will restart the pods one by one in sequence.

```shell
$ kubectl get mariaops -n demo restart 
NAME      TYPE      STATUS       AGE
restart   Restart   Successful   3m25s


$ kubectl get mariaops -n demo restart -oyaml
kubectl get mariaops -n demo restart -oyaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"ops.kubedb.com/v1alpha1","kind":"MariaDBOpsRequest","metadata":{"annotations":{},"name":"restart","namespace":"demo"},"spec":{"apply":"Always","databaseRef":{"name":"mariadb"},"timeout":"3m","type":"Restart"}}
  creationTimestamp: "2025-10-14T12:31:09Z"
  generation: 1
  name: restart
  namespace: demo
  resourceVersion: "1004302"
  uid: 4e135330-46c4-41cd-aff6-bf2ddb018911
spec:
  apply: Always
  databaseRef:
    name: mariadb
  timeout: 3m
  type: Restart
status:
  conditions:
  - lastTransitionTime: "2025-10-14T12:31:09Z"
    message: 'Controller has started to Progress the MariaDBOpsRequest: demo/restart'
    observedGeneration: 1
    reason: Running
    status: "True"
    type: Running
  - lastTransitionTime: "2025-10-14T12:31:17Z"
    message: evict pod; ConditionStatus:True; PodName:mariadb-0
    observedGeneration: 1
    status: "True"
    type: EvictPod--mariadb-0
  - lastTransitionTime: "2025-10-14T12:31:17Z"
    message: get pod; ConditionStatus:True; PodName:mariadb-0
    observedGeneration: 1
    status: "True"
    type: GetPod--mariadb-0
  - lastTransitionTime: "2025-10-14T12:32:27Z"
    message: evict pod; ConditionStatus:True; PodName:mariadb-1
    observedGeneration: 1
    status: "True"
    type: EvictPod--mariadb-1
  - lastTransitionTime: "2025-10-14T12:32:27Z"
    message: get pod; ConditionStatus:True; PodName:mariadb-1
    observedGeneration: 1
    status: "True"
    type: GetPod--mariadb-1
  - lastTransitionTime: "2025-10-14T12:33:37Z"
    message: evict pod; ConditionStatus:True; PodName:mariadb-2
    observedGeneration: 1
    status: "True"
    type: EvictPod--mariadb-2
  - lastTransitionTime: "2025-10-14T12:33:37Z"
    message: get pod; ConditionStatus:True; PodName:mariadb-2
    observedGeneration: 1
    status: "True"
    type: GetPod--mariadb-2
  - lastTransitionTime: "2025-10-14T12:34:47Z"
    message: 'Successfully started MariaDB pods for MariaDBOpsRequest: demo/restart '
    observedGeneration: 1
    reason: RestartPodsSucceeded
    status: "True"
    type: Restart
  - lastTransitionTime: "2025-10-14T12:34:47Z"
    message: Controller has successfully restart the MariaDB replicas
    observedGeneration: 1
    reason: Successful
    status: "True"
    type: Successful
  observedGeneration: 1
  phase: Successful
```

## Cleaning up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete  mariaops -n demo restart
kubectl delete mariadb -n demo mariadb
kubectl delete ns demo
```

## Next Steps

* Learn about [backup and restore](en/backup/kubestash/overview.md) MariaDBQL database using Stash.
* Learn about initializing [MariaDBQL with Script](en/initialization/using-script.md)
* Detail concepts of [MariaDB object](en/concepts/mariadb.md).
* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: rotate-auth/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Rotate Authentication of MariaDB

This guide will give an overview on how KubeDB Ops-manager operator Rotate Authentication configuration.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Rotate MariaDB Authentication Configuration Process Works

The authentication rotation process for MariaDB using KubeDB involves the following steps:

1. A user first creates a `MariaDB` Custom Resource Object (CRO).
2. The `KubeDB Provisioner operator` continuously watches for `MariaDB` CROs.
3. When the operator detects a `MariaDB` CR, it provisions the required `PetSets`, along with related resources such as secrets, services, and other dependencies.
4. To initiate authentication rotation, the user creates a `MariaDBOpsRequest` CR with the desired configuration.
5. The `KubeDB Ops-manager` operator watches for `MariaDBOpsRequest` CRs.
6. Upon detecting a `MariaDBOpsRequest`, the operator pauses the referenced `MariaDB` object, ensuring that the Provisioner
   operator does not perform any operations during the authentication rotation process.
7. The `Ops-manager` operator then updates the necessary configuration (such as credentials) based on the provided `MariaDBOpsRequest` specification.
8. After applying the updated configuration, the operator restarts all `MariaDB` Pods so they come up with the new authentication environment variables and settings.
9. Once the authentication rotation is completed successfully, the operator resumes the `MariaDB` object, allowing the Provisioner operator to continue its usual operations.

In the next section, we will walk you through a step-by-step guide to rotating MariaDB authentication using the `MariaDBOpsRequest` CRD.

<!-- PAGE_START: rotate-auth/rotateauth.md -->
# Rotate Authentication of MariaDB

**Rotate Authentication** is a feature of the KubeDB Ops-Manager that allows you to rotate a `MariaDB` user’s authentication credentials using a `MariaDBOpsRequest`. There are two ways to perform this rotation.

1. **Operator Generated:** The KubeDB operator automatically generates a random credential, updates the existing secret with the new credential The KubeDB operator automatically generates a random credential and updates the existing secret with the new credential..
2. **User Defined:** The user can create their own credentials by defining a Secret of type `kubernetes.io/basic-auth` containing the desired `password` and then reference this secret in the `MariaDBOpsRequest`.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/mariadb.md)
* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Now, install KubeDB cli on your workstation and KubeDB operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Create a MariaDB database

KubeDB implements a `MariaDB` CRD to define the specification of a MariaDB database. Below is the `MariaDB` object created in this tutorial.

`Note`: If your `KubeDB version` is less or equal to `v2024.6.4`, You have to use `v1alpha2` apiVersion.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: Delete
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples/sample-mariadb-v1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until sample-mariadb has status Ready. i.e,

```shell
$ kubectl get mariadb -n demo -w
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5   Ready    30m
```

## Verify authentication

The user can verify whether they are authorized by executing a query directly in the database. To do this, the user needs `username` and `password` in order to connect to the database using the `kubectl exec` command. Below is an example showing how to retrieve the credentials from the Secret.

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth"
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.username}' | base64 -d
root⏎                                  
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.password}' | base64 -d
s)cJQ*iL8wHySpvT⏎
```

Now, you can exec into the pod `sample-mariadb` and connect to database using `username` and `password`

```shell
$ kubectl exec -it -n demo sample-mariadb-0 -- mariadb -u root --password='s)cJQ*iL8wHySpvT'
Defaulted container "mariadb" out of: mariadb, mariadb-init (init)
```

```mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 207
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.000 sec)

MariaDB [(none)]> CREATE DATABASE Bharatnaityam;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| Bharatnaityam      |
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
+--------------------+
5 rows in set (0.000 sec)
```

If you can access the data table and run queries, it means the secrets are working correctly.

## Create RotateAuth MariaDBOpsRequest

#### 1. Using operator generated credentials:

In order to rotate authentication to the `MariaDB` using operator generated, we have to create a
`MariaDBOpsRequest` CRO with `RotateAuth` type. Below is the YAML of the `MariaDBOpsRequest` CRO that we
are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-auth-generated
  namespace: demo
spec:
  type: RotateAuth
  databaseRef:
    name: sample-mariadb
  timeout: 5m
  apply: IfReady
```

Here,

* `spec.databaseRef.name` specifies that we are performing rotate authentication operation on
  `sample-mariadb` database.
* `spec.type` specifies that we are performing `RotateAuth` on MariaDB.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```shell
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/rotate-auth/overview/examples/Mariadb-rotate-auth-generated.yaml
 mariadbopsrequest.ops.kubedb.com/mdops-rotate-auth-generated created
```

Let’s wait for `MariaDBOpsrequest` to be `Successful`. Run the following command to watch `MariaDBOpsrequest` CRO

```shell
$ kubectl get Mariadbopsrequest -n demo
NAME                          TYPE         STATUS       AGE
mdops-rotate-auth-generated   RotateAuth   Successful   6m28s
```

If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed.

```shell
$ kubectl describe Mariadbopsrequest -n demo mdops-rotate-auth-generated
Name:         mdops-rotate-auth-generated
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-11T06:43:21Z
  Generation:          1
  Resource Version:    635526
  UID:                 fdf5a041-9403-4c0b-a788-2adad326dd88
Spec:
  Apply:  IfReady
  Database Ref:
    Name:   sample-mariadb
  Timeout:  5m
  Type:     RotateAuth
Status:
  Conditions:
    Last Transition Time:  2025-07-11T06:43:21Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-11T06:43:24Z
    Message:               Successfully generated new credentials
    Observed Generation:   1
    Reason:                patchedSecret
    Status:                True
    Type:                  UpdateCredential
    Last Transition Time:  2025-07-11T06:43:32Z
    Message:               evict pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  EvictPod--sample-mariadb-0
    Last Transition Time:  2025-07-11T06:43:32Z
    Message:               get pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  GetPod--sample-mariadb-0
    Last Transition Time:  2025-07-11T06:44:07Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                UpdatePetSetsSucceeded
    Status:                True
    Type:                  UpdatePetSets
    Last Transition Time:  2025-07-11T06:44:12Z
    Message:               Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                UpdateCredential
    Status:                True
    Type:                  RotateAuth
    Last Transition Time:  2025-07-11T06:44:12Z
    Message:               Controller has successfully rotate MariaDB auth secret demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                                                     Age    From                         Message
  ----     ------                                                     ----   ----                         -------
  Normal   Starting                                                   9m17s  KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Starting                                                   9m17s  KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal   Successful                                                 9m17s  KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-rotate-auth-generated
  Normal   Starting                                                   9m6s   KubeDB Ops-manager Operator  Restarting Pod: demo/sample-mariadb-0
  Warning  evict pod; ConditionStatus:True; PodName:sample-mariadb-0  9m6s   KubeDB Ops-manager Operator  evict pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    9m6s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    9m1s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    8m31s  KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Normal   Successful                                                 8m31s  KubeDB Ops-manager Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Starting                                                   8m26s  KubeDB Ops-manager Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Controller has successfully rotate MariaDB auth secret
```

**Verify Auth is rotated**

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth"
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.username}' | base64 -d
root⏎                                                               
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.password}' | base64 -d
gTJJMdgpKy9U(Eqi⏎
```

Also, there will be two more new keys in the secret that stores the previous credentials. The keys are `username.prev` and `password.prev`. You can find the secret and its data by running the following command:

```shell
$ kubectl get secret -n demo sample-mariadb-auth -o go-template='{{ index .data "username.prev" }}' | base64 -d
root⏎                                                                                                          
$ kubectl get secret -n demo sample-mariadb-auth -o go-template='{{ index .data "password.prev" }}' | base64 -d
s)cJQ*iL8wHySpvT⏎
```

The above output shows that the password has been changed successfully. The previous username & password is stored for rollback purpose.

#### 2. Using user created credentials

At first, we need to create a secret with kubernetes.io/basic-auth type using custom username and password. Below is the command to create a secret with kubernetes.io/basic-auth type,

> Note: You cannot change the database `username`, but you can update the `password` while keeping the existing `username`.

```shell
$ kubectl create secret generic sample-mariadb-auth-user -n demo \
   --type=kubernetes.io/basic-auth \
   --from-literal=username=root \
   --from-literal=password=testpassword
secret/sample-mariadb-auth-user created
```

Now create a `MariaDBOpsRequest` with `RotateAuth` type. Below is the YAML of the `MariaDBOpsRequest` that we are going to create,

```shell
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-auth-user
  namespace: demo
spec:
  type: RotateAuth
  databaseRef:
    name: sample-mariadb
  authentication:
    secretRef:
      kind: Secret
      name: sample-mariadb-auth-user
  timeout: 5m
  apply: IfReady
```

Here,

* `spec.databaseRef.name` specifies that we are performing rotate authentication operation on `sample-mariadb`cluster.
* `spec.type` specifies that we are performing `RotateAuth` on `MariaDB`.
* `spec.authentication.secretRef.name` specifies that we are using `sample-mariadb-auth-user` as `spec.authSecret.name` for authentication.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```shell
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/rotate-auth/overview/examples/rotate-auth-user.yaml
mariadbopsrequest.ops.kubedb.com/mdops-rotate-auth-user created
```

Let’s wait for `MariaDBOpsRequest` to be Successful. Run the following command to watch `MariaDBOpsRequest` CRO:

```shell
$ kubectl get Mariadbopsrequest -n demo
NAME                          TYPE         STATUS       AGE
mdops-rotate-auth-generated   RotateAuth   Successful   100s
mdops-rotate-auth-user        RotateAuth   Successful   62s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed.

```shell
$  kubectl describe Mariadbopsrequest -n demo mdops-rotate-auth-user
Name:         mdops-rotate-auth-user
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-14T06:56:25Z
  Generation:          1
  Resource Version:    665963
  UID:                 6c30dc56-6ca9-4707-8b7c-5d4da6a1b585
Spec:
  Apply:  IfReady
  Authentication:
    Secret Ref:
      Name:  sample-mariadb-auth-user
  Database Ref:
    Name:   sample-mariadb
  Timeout:  5m
  Type:     RotateAuth
Status:
  Conditions:
    Last Transition Time:  2025-07-14T06:56:25Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-14T06:56:28Z
    Message:               Successfully referenced the user provided authSecret
    Observed Generation:   1
    Reason:                patchedSecret
    Status:                True
    Type:                  UpdateCredential
    Last Transition Time:  2025-07-14T06:56:35Z
    Message:               evict pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  EvictPod--sample-mariadb-0
    Last Transition Time:  2025-07-14T06:56:35Z
    Message:               get pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  GetPod--sample-mariadb-0
    Last Transition Time:  2025-07-14T06:56:40Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                UpdatePetSetsSucceeded
    Status:                True
    Type:                  UpdatePetSets
    Last Transition Time:  2025-07-14T06:56:45Z
    Message:               Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                UpdateCredential
    Status:                True
    Type:                  RotateAuth
    Last Transition Time:  2025-07-14T06:56:45Z
    Message:               Controller has successfully rotate MariaDB auth secret demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                                                     Age   From                         Message
  ----     ------                                                     ----  ----                         -------
  Normal   Starting                                                   83s   KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Starting                                                   83s   KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal   Successful                                                 83s   KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-rotate-auth-user
  Normal   Starting                                                   73s   KubeDB Ops-manager Operator  Restarting Pod: demo/sample-mariadb-0
  Warning  evict pod; ConditionStatus:True; PodName:sample-mariadb-0  73s   KubeDB Ops-manager Operator  evict pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    73s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    68s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Normal   Successful                                                 68s   KubeDB Ops-manager Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Starting                                                   63s   KubeDB Ops-manager Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Controller has successfully rotate MariaDB auth secret
```

**Verify auth is rotate**

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth-user"
$ kubectl get secret -n demo sample-mariadb-auth-user -o=jsonpath='{.data.username}' | base64 -d
root⏎                                                                    
$ kubectl get secret -n demo sample-mariadb-auth-user -o=jsonpath='{.data.password}' | base64 -d
testpassword⏎
```

Also, there will be two more new keys in the secret that stores the previous credentials. The keys are `username.prev` and `password.prev`. You can find the secret and its data by running the following command:

```shell
$ kubectl get secret -n demo sample-mariadb-auth-user -o go-template='{{ index .data "username.prev" }}' | base64 -d
root⏎                                                                                                          
$ kubectl get secret -n demo sample-mariadb-auth-user -o go-template='{{ index .data "password.prev" }}' | base64 -d
gTJJMdgpKy9U(Eqi⏎
```

The above output shows that the password has been changed successfully. The previous username & password is stored in the secret for rollback purpose.

## Cleaning up

To clean up the Kubernetes resources you can delete the CRD or namespace.
Or, you can delete one by one resource by their name by this tutorial, run:

```shell
$ kubectl delete Mariadbopsrequest mdops-rotate-auth-generated mdops-rotate-auth-user -n demo
mariadbopsrequest.ops.kubedb.com "mdops-rotate-auth-generated" deleted
mariadbopsrequest.ops.kubedb.com "mdops-rotate-auth-user" deleted
$ kubectl delete secret -n demo  sample-mariadb-auth-user
secret "sample-mariadb-auth-user" deleted
$ kubectl delete secret -n demo  sample-mariadb-auth
secret "sample-mariadb-auth" deleted
```

## Next Steps

* Want to hack on KubeDB? Check our [contribution guidelines](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).

<!-- PAGE_START: tls/configure.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Configure TLS/SSL in MariaDB

`KubeDB` supports providing TLS/SSL encryption (via, `requireSSL` mode) for `MariaDB`. This tutorial will show you how to use `KubeDB` to deploy a `MariaDB` database with TLS/SSL configuration.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install [`cert-manger`](https://cert-manager.io/docs/installation/) v1.0.0 or later to your cluster to manage your SSL/TLS certificates.
* Install `KubeDB` in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* To keep things isolated, this tutorial uses a separate namespace called `demo` throughout this tutorial.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Note: YAML files used in this tutorial are stored in [docs/guides/mariadb/tls/configure/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/tls/configure/examples) folder in GitHub repository [kubedb/docs](https://github.com/kubedb/docs).

### Deploy MariaDB database with TLS/SSL configuration

As pre-requisite, at first, we are going to create an Issuer/ClusterIssuer. This Issuer/ClusterIssuer is used to create certificates. Then we are going to deploy a MariaDB standalone and a group replication that will be configured with these certificates by `KubeDB` operator.

### Create Issuer/ClusterIssuer

Now, we are going to create an example `Issuer` that will be used throughout the duration of this tutorial. Alternatively, you can follow this [cert-manager tutorial](https://cert-manager.io/docs/configuration/ca/) to create your own `Issuer`. By following the below steps, we are going to create our desired issuer,

* Start off by generating our ca-certificates using openssl,

```bash
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./ca.key -out ./ca.crt -subj "/CN=mariadb/O=kubedb"
Generating a RSA private key
...........................................................................+++++
........................................................................................................+++++
writing new private key to './ca.key'
```

* create a secret using the certificate files we have just generated,

```bash
kubectl create secret tls md-ca \
     --cert=ca.crt \
     --key=ca.key \
     --namespace=demo
secret/md-ca created
```

Now, we are going to create an `Issuer` using the `md-ca` secret that hols the ca-certificate we have just created. Below is the YAML of the `Issuer` cr that we are going to create,

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: md-issuer
  namespace: demo
spec:
  ca:
    secretName: md-ca
```

Let’s create the `Issuer` cr we have shown above,

```bash
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/tls/configure/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

### Deploy MariaDB Standalone with TLS/SSL configuration

Here, our issuer `md-issuer` is ready to deploy a `MariaDB` standalone with TLS/SSL configuration. Below is the YAML for MariaDB Standalone that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-standalone-tls
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi   
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
  deletionPolicy: WipeOut
```

Here,

* `spec.requireSSL` specifies the SSL/TLS client connection to the server is required.
* `spec.tls.issuerRef` refers to the `md-issuer` issuer.
* `spec.tls.certificates` gives you a lot of options to configure so that the certificate will be renewed and kept up to date.
  You can found more details from [here](en/concepts/mariadb.md#spectls)

**Deploy MariaDB Standalone:**

Let’s create the `MariaDB` cr we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/tls/configure/examples/tls-standalone.yaml
mariadb.kubedb.com/md-standalone-tls created
```

**Wait for the database to be ready:**

Now, wait for `MariaDB` going on `Running` state and also wait for `PetSet` and its pod to be created and going to `Running` state,

```bash
$ kubectl get mariadb -n demo md-standalone-tls
NAME             VERSION   STATUS   AGE
md-standalone-tls   11.8.5    Ready    5m48s

$ kubectl get petset -n demo md-standalone-tls
NAME             READY   AGE
md-standalone-tls   1/1     7m5s
```

**Verify tls-secrets created successfully:**

If everything goes well, you can see that our tls-secrets will be created which contains server, client, exporter certificate. Server tls-secret will be used for server configuration and client tls-secret will be used for a secure connection.

All tls-secret are created by `KubeDB` Ops Manager. Default tls-secret name formed as *{mariadb-object-name}-{cert-alias}-cert*.

Let’s check the tls-secrets have created,

```bash
$ kubectl get secrets -n demo | grep md-standalone-tls
md-standalone-tls-archiver-cert             kubernetes.io/tls                     3      7m53s
md-standalone-tls-auth                      kubernetes.io/basic-auth              2      7m54s
md-standalone-tls-metrics-exporter-cert     kubernetes.io/tls                     3      7m53s
md-standalone-tls-metrics-exporter-config   Opaque                                1      7m54s
md-standalone-tls-server-cert               kubernetes.io/tls                     3      7m53s
md-standalone-tls-token-7hhg2
```

**Verify MariaDB Standalone configured with TLS/SSL:**

Now, we are going to connect to the database for verifying the `MariaDB` server has configured with TLS/SSL encryption.

Let’s exec into the pod to verify TLS/SSL configuration,

```bash
$ kubectl exec -it -n demo md-standalone-tls-0 -- bash

root@md-standalone-tls-0:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
root@md-standalone-tls-0:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key
```

```mysql
root@md-standalone-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 64
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.002 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

The above output shows that the `MariaDB` server is configured to TLS/SSL. You can also see that the `.crt` and `.key` files are stored in `/etc/mysql/certs/client/` and `/etc/mysql/certs/server/` directory for client and server respectively.

**Verify secure connection for SSL required user:**

Now, you can create an SSL required user that will be used to connect to the database with a secure connection.

Let’s connect to the database server with a secure connection,

```bash
$ kubectl exec -it -n demo md-standalone-tls-0 -- bash
root@md-standalone-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 92
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE USER 'new_user'@'localhost' IDENTIFIED BY '1234' REQUIRE SSL;
Query OK, 0 rows affected (0.028 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> exit
Bye

#  accessing the database server with newly created user
root@md-standalone-tls-0:/ mariadb -unew_user -p1234
ERROR 1045 (28000): Access denied for user 'new_user'@'localhost' (using password: YES)

# accessing the database server newly created user with certificates
root@md-standalone-tls-0:/ mariadb -unew_user -p1234 --ssl-ca=/etc/mysql/certs/server/ca.crt  --ssl-cert=/etc/mysql/certs/server/tls.crt --ssl-key=/etc/mysql/certs/server/tls.key
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 116
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> exit 
Bye
```

From the above output, you can see that only using client certificate we can access the database securely, otherwise, it shows “Access denied”. Our client certificate is stored in `/etc/mysql/certs/client/` directory.

## Deploy MariaDB Cluster with TLS/SSL configuration

Now, we are going to deploy a `MariaDB` Cluster with TLS/SSL configuration. Below is the YAML for MariaDB cluster that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-cluster-tls
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi   
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
  deletionPolicy: WipeOut
```

**Deploy MariaDB Cluster:**

```bash
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/tls/configure/examples/tls-cluster.yaml
mariadb.kubedb.com/md-cluster-tls created
```

**Wait for the database to be ready :**

Now, wait for `MariaDB` going on `Running` state and also wait for `PetSet` and its pods to be created and going to `Running` state,

```bash
$ kubectl get mariadb -n demo md-cluster-tls
NAME             VERSION   STATUS   AGE
md-cluster-tls   11.8.5    Ready    2m49s

$ kubectl get pod -n demo | grep md-cluster-tls
md-cluster-tls-0   1/1     Running   0          3m29s
md-cluster-tls-1   1/1     Running   0          3m9s
md-cluster-tls-2   1/1     Running   0          2m49s
```

**Verify tls-secrets created successfully :**

If everything goes well, you can see that our tls-secrets will be created which contains server, client, exporter certificate. Server tls-secret will be used for server configuration and client tls-secret will be used for a secure connection.

All tls-secret are created by `KubeDB` Ops Manager. Default tls-secret name formed as *{mariadb-object-name}-{cert-alias}-cert*.

Let’s check the tls-secrets have created,

```bash
$ kubectl get secrets -n demo | grep md-cluster-tls
md-cluster-tls-archiver-cert             kubernetes.io/tls                     3      6m20s
md-cluster-tls-auth                      kubernetes.io/basic-auth              2      6m22s
md-cluster-tls-metrics-exporter-cert     kubernetes.io/tls                     3      6m20s
md-cluster-tls-metrics-exporter-config   Opaque                                1      6m21s
md-cluster-tls-server-cert               kubernetes.io/tls                     3      6m21s
md-cluster-tls-token-nrs75
```

**Verify MariaDB Cluster configured with TLS/SSL:**

Now, we are going to connect to the database for verifying the `MariaDB` server has configured with TLS/SSL encryption.

Let’s exec into the first pod to verify TLS/SSL configuration,

```bash
$ kubectl exec -it -n demo md-cluster-tls-0 -- bash

root@md-cluster-tls-0:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
root@md-cluster-tls-0:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key
```

```mysql
root@md-cluster-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 64
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.002 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

Now let’s check for the second database server,

```bash
$ kubectl exec -it -n demo md-cluster-tls-1 -- bash
root@md-cluster-tls-1:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
root@md-cluster-tls-1:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key
```

```mysql
root@md-cluster-tls-1:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 34
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.001 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

The above output shows that the `MariaDB` server is configured to TLS/SSL. You can also see that the `.crt` and `.key` files are stored in `/etc/mysql/certs/client/` and `/etc/mysql/certs/server/` directory for client and server respectively.

**Verify secure connection for SSL required user:**

Now, you can create an SSL required user that will be used to connect to the database with a secure connection.

Let’s connect to the database server with a secure connection,

```bash
$ kubectl exec -it -n demo md-cluster-tls-0 -- bash
root@md-cluster-tls-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 92
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE USER 'new_user'@'localhost' IDENTIFIED BY '1234' REQUIRE SSL;
Query OK, 0 rows affected (0.028 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> exit
Bye

#  accessing the database server with newly created user
root@md-cluster-tls-0:/ mariadb -unew_user -p1234
ERROR 1045 (28000): Access denied for user 'new_user'@'localhost' (using password: YES)

# accessing the database server newly created user with certificates
root@md-cluster-tls-0:/ mariadb -unew_user -p1234 --ssl-ca=/etc/mysql/certs/server/ca.crt  --ssl-cert=/etc/mysql/certs/server/tls.crt --ssl-key=/etc/mysql/certs/server/tls.key
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 116
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> exit 
Bye
```

From the above output, you can see that only using client certificate we can access the database securely, otherwise, it shows “Access denied”. Our client certificate is stored in `/etc/mysql/certs/client/` directory.

## Cleaning up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete  mariadb demo  md-standalone-tls
mariadb.kubedb.com "md-standalone-tls" deleted
$ kubectl delete  mariadb demo  md-cluster-tls
mariadb.kubedb.com "md-cluster-tls" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```

<!-- PAGE_START: tls/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB TLS/SSL Encryption

**Prerequisite :** To configure TLS/SSL in `MariaDB`, `KubeDB` uses `cert-manager` to issue certificates. So first you have to make sure that the cluster has `cert-manager` installed. To install `cert-manager` in your cluster following steps [here](https://cert-manager.io/docs/installation/kubernetes/).

To issue a certificate, the following cr of `cert-manager` is used:

* `Issuer/ClusterIssuer`: Issuers and ClusterIssuers represent certificate authorities (CAs) that are able to generate signed certificates by honoring certificate signing requests. All cert-manager certificates require a referenced issuer that is in a ready condition to attempt to honor the request. You can learn more details [here](https://cert-manager.io/docs/concepts/issuer/).
* `Certificate`: `cert-manager` has the concept of Certificates that define the desired x509 certificate which will be renewed and kept up to date. You can learn more details [here](https://cert-manager.io/docs/concepts/certificate/).

**MariaDB CRD Specification:**

KubeDB uses the following cr fields to enable SSL/TLS encryption in `MariaDB`.

* `spec:`
  + `requireSSL`
  + `tls:`
    - `issuerRef`
    - `certificates`

Read about the fields in details from [mariadb concept](en/concepts/mariadb.md#spectls),

When, `requireSSL` is set, the users must specify the `tls.issuerRef` field. `KubeDB` uses the `issuer` or `clusterIssuer` referenced in the `tls.issuerRef` field, and the certificate specs provided in `tls.certificate` to generate certificate secrets using `Issuer/ClusterIssuers` specification. These certificates secrets including `ca.crt`, `tls.crt` and `tls.key` etc. are used to configure `MariaDB` server, exporter etc. respectively.

## How TLS/SSL configures in MariaDB

The following figure shows how `KubeDB` enterprise is used to configure TLS/SSL in MariaDB. Open the image in a new tab to see the enlarged version.

![Stash Backup Flow](images/tls_overview_md-tls-ssl.png)

Fig: Deploy MariaDB with TLS/SSL

Deploying MariaDB with TLS/SSL configuration process consists of the following steps:

1. At first, a user creates an `Issuer/ClusterIssuer` cr.
2. Then the user creates a `MariaDB` cr.
3. `KubeDB` community operator watches for the `MariaDB` cr.
4. When it finds one, it creates `Secret`, `Service`, etc. for the `MariaDB` database.
5. `KubeDB` Ops Manager watches for `MariaDB`(5c), `Issuer/ClusterIssuer`(5b), `Secret` and `Service`(5a).
6. When it finds all the resources(`MariaDB`, `Issuer/ClusterIssuer`, `Secret`, `Service`), it creates `Certificates` by using `tls.issuerRef` and `tls.certificates` field specification from `MariaDB` cr.
7. `cert-manager` watches for certificates.
8. When it finds one, it creates certificate secrets `tls-secrets`(server, client, exporter secrets, etc.) that hold the actual self-signed certificate.
9. `KubeDB` community operator watches for the Certificate secrets `tls-secrets`.
10. When it finds all the tls-secret, it creates a `PetSet` so that MariaDB server is configured with TLS/SSL.

In the next doc, we are going to show a step by step guide on how to configure a `MariaDB` database with TLS/SSL.

<!-- PAGE_START: update-version/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# update version of MariaDB Cluster

This guide will show you how to use `KubeDB` Enterprise operator to update the version of `MariaDB` Cluster.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install `KubeDB` Community and Enterprise operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [Cluster](en/clustering/overview.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Updating Overview](en/update-version/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Prepare MariaDB Cluster

Now, we are going to deploy a `MariaDB` cluster database with version `11.8.5`.

### Deploy MariaDB cluster

In this section, we are going to deploy a MariaDB Cluster. Then, in the next section we will update the version of the database using `MariaDBOpsRequest` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

> If you want to update `MariaDB Standalone`, Just remove the `spec.Replicas` from the below yaml and rest of the steps are same.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
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

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/update-version/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` created has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo                                                                                                                                             
NAME             VERSION    STATUS     AGE
sample-mariadb   11.8.5    Ready     3m15s
```

We are now ready to apply the `MariaDBOpsRequest` CR to update this database.

### update MariaDB Version

Here, we are going to update `MariaDB` cluster from `11.8.5` to `12.1.2`.

#### Create MariaDBOpsRequest:

In order to update the database cluster, we have to create a `MariaDBOpsRequest` CR with your desired version that is supported by `KubeDB`. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-update
  namespace: demo
spec:
  type: UpdateVersion
  databaseRef:
    name: sample-mariadb
  updateVersion:
    targetVersion: "12.1.2"
```

Here,

* `spec.databaseRef.name` specifies that we are performing operation on `sample-mariadb` MariaDB database.
* `spec.type` specifies that we are going to perform `UpdateVersion` on our database.
* `spec.updateVersion.targetVersion` specifies the expected version of the database `12.1.2`.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/update-version/cluster/examples/mdops-update.yaml
mariadbopsrequest.ops.kubedb.com/mdops-update created
```

#### Verify MariaDB version updated successfully

If everything goes well, `KubeDB` Enterprise operator will update the image of `MariaDB` object and related `PetSets` and `Pods`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME              TYPE            STATUS       AGE
mdops-update      UpdateVersion   Successful    84s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded.

Now, we are going to verify whether the `MariaDB` and the related `PetSets` and their `Pods` have the new version image. Let’s check,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o=jsonpath='{.spec.version}{"\n"}'
12.1.2

$ kubectl get petset -n demo sample-mariadb -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
mariadb:12.1.2

$ kubectl get pods -n demo sample-mariadb-0 -o=jsonpath='{.spec.containers[0].image}{"\n"}'
mariadb:12.1.2
```

You can see from above, our `MariaDB` cluster database has been updated with the new version. So, the update process is successfully completed.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-update
```

<!-- PAGE_START: update-version/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# updating MariaDB version Overview

This guide will give you an overview on how KubeDB Ops Manager update the version of `MariaDB` database.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How update version Process Works

The following diagram shows how KubeDB Ops Manager used to update the version of `MariaDB`. Open the image in a new tab to see the enlarged version.

  ![updating Process of MariaDB](images/update-version_overview_mdops-update.jpeg)

Fig: updating Process of MariaDB

The updating process consists of the following steps:

1. At first, a user creates a `MariaDB` Custom Resource (CR).
2. `KubeDB` Community operator watches the `MariaDB` CR.
3. When the operator finds a `MariaDB` CR, it creates required number of `PetSets` and related necessary stuff like secrets, services, etc.
4. Then, in order to update the version of the `MariaDB` database the user creates a `MariaDBOpsRequest` CR with the desired version.
5. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CR.
6. When it finds a `MariaDBOpsRequest` CR, it halts the `MariaDB` object which is referred from the `MariaDBOpsRequest`. So, the `KubeDB` Community operator doesn’t perform any operations on the `MariaDB` object during the updating process.
7. By looking at the target version from `MariaDBOpsRequest` CR, `KubeDB` Enterprise operator updates the images of all the `PetSets`. After each image update, the operator performs some checks such as if the oplog is synced and database size is almost same or not.
8. After successfully updating the `PetSets` and their `Pods` images, the `KubeDB` Enterprise operator updates the image of the `MariaDB` object to reflect the updated state of the database.
9. After successfully updating of `MariaDB` object, the `KubeDB` Enterprise operator resumes the `MariaDB` object so that the `KubeDB` Community operator can resume its usual operations.

In the next doc, we are going to show a step by step guide on updating of a MariaDB database using update operation.

<!-- PAGE_START: volume-expansion/maxscale.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MaxScale Volume Expansion

This guide will show you how to use `KubeDB` Ops-manager operator to expand the volume of MaxScale server.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* You must have a `StorageClass` that supports volume expansion.
* Install `KubeDB` operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDB Replication](en/clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Volume Expansion Overview](en/volume-expansion/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Expand Volume of MaxScale

Here, we are going to deploy a `MariaDB` cluster in replication mode using a supported version by `KubeDB` operator. Then we are going to apply `MariaDBOpsRequest` to expand its volume.

### Prepare MariaDB Database

At first verify that your cluster has a storage class, that supports volume expansion. Let’s check,

```bash
$ kubectl get storageclass
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path             rancher.io/local-path   Delete          WaitForFirstConsumer   false                  46h
standard               driver.standard.io      Delete          Immediate              true                   2m27s
standard-static        driver.standard.io      Delete          Immediate              true                   2m24s
```

We can see from the output that `standard` storage class has `ALLOWVOLUMEEXPANSION` field as true. So, this storage class supports volume expansion. We will use this storage class.

Now, we are going to deploy a `MariaDB` database with `MaxScale` in replication mode.

### Deploy MariaDB with MaxScale

In this section, we are going to deploy a MariaDB database along with `MaxScale` with 50Mi volume.
Then, in the next section we will expand its volume to 100Mi using `MariaDBOpsRequest` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-replication
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        storageClassName: "standard"
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
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

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/volume-expansion/md-replication.yaml
mariadb.kubedb.com/md-replication created
```

Now, wait until `md-replication` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
md-replication   11.8.5   Ready    2m30s
```

Let’s check volume size from petset, and from the persistent volume,

```bash
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"50Mi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                           STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-27e4f4b2-289b-44bb-97a2-729d9420f668   1Gi        RWO            Delete           Bound    demo/data-md-replication-2      standard       <unset>                          3m48s
pvc-2df9a141-5d32-4c92-b0ec-a8043975c2ae   1Gi        RWO            Delete           Bound    demo/data-md-replication-1      standard       <unset>                          3m48s
pvc-7609183e-f9a5-4177-b260-0d24796fb04c   1Gi        RWO            Delete           Bound    demo/data-md-replication-0      standard       <unset>                          3m48s
pvc-96449ed7-305e-4857-a2b6-6eda33c99207   50Mi       RWO            Delete           Bound    demo/data-md-replication-mx-2   standard       <unset>                          3m51s
pvc-c1424029-4a52-4ff4-9888-14d5e7b4fb61   50Mi       RWO            Delete           Bound    demo/data-md-replication-mx-0   standard       <unset>                          3m51s
pvc-d12d301c-58bd-4c59-bd5a-d9167df2b53d   50Mi       RWO            Delete           Bound    demo/data-md-replication-mx-1   standard       <unset>                          3m51s
```

You can see that `MaxScale` petset has 50Mi storage, and the capacity of the `MaxScale` persistent volumes are also 50Mi.

We are now ready to apply the `MariaDBOpsRequest` CR to expand the volume of this database.

### Volume Expansion

Here, we are going to expand the volume of the `MaxScale` cluster.

#### Create MariaDBOpsRequest

In order to expand the volume of the maxscale server, we have to create a `MariaDBOpsRequest` CR with our desired volume size. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-volume-expansion
  namespace: demo
spec:
  type: VolumeExpansion
  databaseRef:
    name: md-replication
  volumeExpansion:
    mode: Online
    maxscale: 100Mi
```

Here,

* `spec.type` specifies that we are performing `VolumeExpansion` on our database.
* `spec.databaseRef.name` specifies that we are performing volume expansion operation on `md-replication` database.
* `spec.volumeExpansion.mode` specifies the desired volume expansion mode (`Online` or `Offline`). Storageclass `standard` supports `Online` volume expansion.
* `spec.volumeExpansion.maxscale` specifies the desired volume size of maxscale server.

> **Note:** If the Storageclass you are using doesn’t support `Online` Volume Expansion, Try offline volume expansion by using `spec.volumeExpansion.mode:"Offline"`. The pods need to be restarted during offline volume expansion.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/volume-expansion/maxscale-volume-expansion.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-volume-expansion created
```

#### Verify MaxScale volume expanded successfully

If everything goes well, `KubeDB` Ops-manager operator will update the volume size of `MaxScale` object and related `PetSets` and `Persistent Volumes`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                        TYPE              STATUS       AGE
maxscale-volume-expansion   VolumeExpansion   Successful   3m
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to expand the volume of the database.

```bash
$ kubectl describe mariadbopsrequest -n demo maxscale-volume-expansion
Name:         maxscale-volume-expansion
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-23T06:46:12Z
  Generation:          1
  Resource Version:    96939
  UID:                 c33c6a08-2514-4818-932e-f4460bd612a7
Spec:
  Apply:  IfReady
  Database Ref:
    Name:  md-replication
  Type:    VolumeExpansion
  Volume Expansion:
    Maxscale:  100Mi
    Mode:      Online
Status:
  Conditions:
    Last Transition Time:  2025-07-23T06:46:12Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/maxscale-volume-expansion
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-23T06:46:20Z
    Message:               all pvc; ConditionStatus:True
    Observed Generation:   1
    Status:                True
    Type:                  AllPvc
    Last Transition Time:  2025-07-23T06:46:20Z
    Message:               is pvc patch; ConditionStatus:True
    Observed Generation:   1
    Status:                True
    Type:                  IsPvcPatch
    Last Transition Time:  2025-07-23T06:47:10Z
    Message:               delete pvc; ConditionStatus:True
    Observed Generation:   1
    Status:                True
    Type:                  DeletePvc
    Last Transition Time:  2025-07-23T06:47:15Z
    Message:               Online Volume Expansion performed successfully in MaxScale pod for MariaDBOpsRequest: demo/maxscale-volume-expansion
    Observed Generation:   1
    Reason:                VolumeExpansionSucceeded
    Status:                True
    Type:                  VolumeExpansion
    Last Transition Time:  2025-07-23T06:47:15Z
    Message:               Controller has successfully expand the volume of MaxScale: demo/maxscale-volume-expansion
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                              Age   From                         Message
  ----     ------                              ----  ----                         -------
  Normal   Starting                            15m   KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/maxscale-volume-expansion
  Normal   Starting                            15m   KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/md-replication
  Normal   Successful                          15m   KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/md-replication for MariaDBOpsRequest: maxscale-volume-expansion
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  is pvc patch; ConditionStatus:True  15m   KubeDB Ops-manager Operator  is pvc patch; ConditionStatus:True
  Warning  is pvc patch; ConditionStatus:True  15m   KubeDB Ops-manager Operator  is pvc patch; ConditionStatus:True
  Warning  is pvc patch; ConditionStatus:True  15m   KubeDB Ops-manager Operator  is pvc patch; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       15m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       14m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  delete pvc; ConditionStatus:True    14m   KubeDB Ops-manager Operator  delete pvc; ConditionStatus:True
  Warning  all pvc; ConditionStatus:True       14m   KubeDB Ops-manager Operator  all pvc; ConditionStatus:True
  Warning  delete pvc; ConditionStatus:True    14m   KubeDB Ops-manager Operator  delete pvc; ConditionStatus:True
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Online Volume Expansion performed successfully in MaxScale pod for MariaDBOpsRequest: demo/maxscale-volume-expansion
  Normal   Starting                            14m   KubeDB Ops-manager Operator  Updating MaxScale storage
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Successfully updated MaxScale storage
  Normal   Starting                            14m   KubeDB Ops-manager Operator  Resuming MariaDB database: demo/md-replication
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/md-replication
  Normal   Successful                          14m   KubeDB Ops-manager Operator  Controller has Successfully expand the volume of MaxScale: demo/md-replication
```

Now, we are going to verify from the `Petset`, and the `Persistent Volumes` whether the volume of the database has expanded to meet the desired state, Let’s check,

```bash
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"100Mi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                           STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-27e4f4b2-289b-44bb-97a2-729d9420f668   1Gi        RWO            Delete           Bound    demo/data-md-replication-2      standard       <unset>                          34m
pvc-2df9a141-5d32-4c92-b0ec-a8043975c2ae   1Gi        RWO            Delete           Bound    demo/data-md-replication-1      standard       <unset>                          34m
pvc-7609183e-f9a5-4177-b260-0d24796fb04c   1Gi        RWO            Delete           Bound    demo/data-md-replication-0      standard       <unset>                          34m
pvc-96449ed7-305e-4857-a2b6-6eda33c99207   100Mi      RWO            Delete           Bound    demo/data-md-replication-mx-2   standard       <unset>                          34m
pvc-c1424029-4a52-4ff4-9888-14d5e7b4fb61   100Mi      RWO            Delete           Bound    demo/data-md-replication-mx-0   standard       <unset>                          34m
pvc-d12d301c-58bd-4c59-bd5a-d9167df2b53d   100Mi      RWO            Delete           Bound    demo/data-md-replication-mx-1   standard       <unset>                          34m
```

The above output verifies that we have successfully expanded the volume of the MariaDB database.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo md-replication
$ kubectl delete mariadbopsrequest -n demo maxscale-volume-expansion
$ kubectl delete ns demo
```

<!-- PAGE_START: volume-expansion/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Volume Expansion

This guide will give an overview on how KubeDB Ops Manager expand the volume of `MariaDB`.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Volume Expansion Process Works

The following diagram shows how KubeDB Ops Manager expand the volumes of `MariaDB` database components. Open the image in a new tab to see the enlarged version.

  ![Volume Expansion process of MariaDB](images/volume-expansion_overview_volume-expansion.jpeg)

Fig: Volume Expansion process of MariaDB

The Volume Expansion process consists of the following steps:

1. At first, a user creates a `MariaDB` Custom Resource (CR).
2. `KubeDB` Community operator watches the `MariaDB` CR.
3. When the operator finds a `MariaDB` CR, it creates required `PetSet` and related necessary stuff like secrets, services, etc.
4. The petSet creates Persistent Volumes according to the Volume Claim Template provided in the petset configuration. This Persistent Volume will be expanded by the `KubeDB` Enterprise operator.
5. Then, in order to expand the volume of the `MariaDB` database the user creates a `MariaDBOpsRequest` CR with desired information.
6. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CR.
7. When it finds a `MariaDBOpsRequest` CR, it pauses the `MariaDB` object which is referred from the `MariaDBOpsRequest`. So, the `KubeDB` Community operator doesn’t perform any operations on the `MariaDB` object during the volume expansion process.
8. Then the `KubeDB` Enterprise operator will expand the persistent volume to reach the expected size defined in the `MariaDBOpsRequest` CR.
9. After the successfully expansion of the volume of the related PetSet Pods, the `KubeDB` Enterprise operator updates the new volume size in the `MariaDB` object to reflect the updated state.
10. After the successful Volume Expansion of the `MariaDB`, the `KubeDB` Enterprise operator resumes the `MariaDB` object so that the `KubeDB` Community operator resumes its usual operations.

In the next docs, we are going to show a step by step guide on Volume Expansion of various MariaDB database using `MariaDBOpsRequest` CRD.

<!-- PAGE_START: volume-expansion/volume-expansion.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Volume Expansion

This guide will show you how to use `KubeDB` Enterprise operator to expand the volume of a MariaDB.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* You must have a `StorageClass` that supports volume expansion.
* Install `KubeDB` Community and Enterprise operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Volume Expansion Overview](en/volume-expansion/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Expand Volume of MariaDB

Here, we are going to deploy a `MariaDB` cluster using a supported version by `KubeDB` operator. Then we are going to apply `MariaDBOpsRequest` to expand its volume. The process of expanding MariaDB `standalone` is same as MariaDB cluster.

### Prepare MariaDB Database

At first verify that your cluster has a storage class, that supports volume expansion. Let’s check,

```bash
$ kubectl get storageclass
NAME                  PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
longhorn (default)    rancher.io/local-path   Delete          WaitForFirstConsumer   false                  69s
topolvm-provisioner   topolvm.cybozu.com      Delete          WaitForFirstConsumer   true                   37s
```

We can see from the output the `topolvm-provisioner` storage class has `ALLOWVOLUMEEXPANSION` field as true. So, this storage class supports volume expansion. We will use this storage class. You can install topolvm from [here](https://github.com/topolvm/topolvm).

Now, we are going to deploy a `MariaDB` database of 3 replicas with version `12.1.2`.

### Deploy MariaDB

In this section, we are going to deploy a MariaDB Cluster with 1GB volume. Then, in the next section we will expand its volume to 2GB using `MariaDBOpsRequest` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "topolvm-provisioner"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/volume-expansion/volume-expansion/example/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    5m4s
```

Let’s check volume size from petset, and from the persistent volume,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1Gi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-331335d1-c8e0-4b73-9dab-dae57920e997   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            63s
pvc-b90179f8-c40a-4273-ad77-74ca8470b782   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            62s
pvc-f72411a4-80d5-4d32-b713-cb30ec662180   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            62s
```

You can see the petset has 1GB storage, and the capacity of all the persistent volumes are also 1GB.

We are now ready to apply the `MariaDBOpsRequest` CR to expand the volume of this database.

### Volume Expansion

Here, we are going to expand the volume of the MariaDB cluster.

#### Create MariaDBOpsRequest

In order to expand the volume of the database, we have to create a `MariaDBOpsRequest` CR with our desired volume size. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: md-online-volume-expansion
  namespace: demo
spec:
  type: VolumeExpansion  
  databaseRef:
    name: sample-mariadb
  volumeExpansion:   
    mode: "Online"
    mariadb: 2Gi
```

Here,

* `spec.databaseRef.name` specifies that we are performing volume expansion operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `VolumeExpansion` on our database.
* `spec.volumeExpansion.mariadb` specifies the desired volume size.
* `spec.volumeExpansion.mode` specifies the desired volume expansion mode (`Online` or `Offline`). Storageclass `topolvm-provisioner` supports `Online` volume expansion.

> **Note:** If the Storageclass you are using doesn’t support `Online` Volume Expansion, Try offline volume expansion by using `spec.volumeExpansion.mode:"Offline"`.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/volume-expansion/volume-expansion/example/online-volume-expansion.yaml
mariadbopsrequest.ops.kubedb.com/md-online-volume-expansion created
```

#### Verify MariaDB volume expanded successfully

If everything goes well, `KubeDB` Enterprise operator will update the volume size of `MariaDB` object and related `PetSets` and `Persistent Volumes`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                         TYPE              STATUS       AGE
md-online-volume-expansion   VolumeExpansion   Successful   96s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to expand the volume of the database.

```bash
$ kubectl describe mariadbopsrequest -n demo md-online-volume-expansion
Name:         md-online-volume-expansion
Namespace:    demo
Labels:       <none>
Annotations:  API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  UID:               09a119aa-4f2a-4cb4-b620-2aa3a514df11
Spec:
  Database Ref:
    Name:  sample-mariadb
  Type:    VolumeExpansion
  Volume Expansion:
    Mariadb:  2Gi
    Mode:     Online
Status:
  Conditions:
    Last Transition Time:  2022-01-07T06:38:29Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/md-online-volume-expansion
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-01-07T06:39:49Z
    Message:               Online Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/md-online-volume-expansion
    Observed Generation:   1
    Reason:                SuccessfullyVolumeExpanded
    Status:                True
    Type:                  VolumeExpansion
    Last Transition Time:  2022-01-07T06:39:49Z
    Message:               Controller has successfully expand the volume of MariaDB demo/md-online-volume-expansion
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
Events:
  Type    Reason      Age   From                        Message
  ----    ------      ----  ----                        -------
  Normal  Starting    2m1s  KubeDB Enterprise Operator  Start processing for MariaDBOpsRequest: demo/md-online-volume-expansion
  Normal  Starting    2m1s  KubeDB Enterprise Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal  Successful  2m1s  KubeDB Enterprise Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: md-online-volume-expansion
  Normal  Successful  41s   KubeDB Enterprise Operator  Online Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/md-online-volume-expansion
  Normal  Starting    41s   KubeDB Enterprise Operator  Updating MariaDB storage
  Normal  Successful  41s   KubeDB Enterprise Operator  Successfully Updated MariaDB storage
  Normal  Starting    41s   KubeDB Enterprise Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal  Successful  41s   KubeDB Enterprise Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal  Successful  41s   KubeDB Enterprise Operator  Controller has Successfully expand the volume of MariaDB: demo/sample-mariadb
```

Now, we are going to verify from the `Petset`, and the `Persistent Volumes` whether the volume of the database has expanded to meet the desired state, Let’s check,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"2Gi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-331335d1-c8e0-4b73-9dab-dae57920e997   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            12m
pvc-b90179f8-c40a-4273-ad77-74ca8470b782   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            12m
pvc-f72411a4-80d5-4d32-b713-cb30ec662180   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            12m
```

The above output verifies that we have successfully expanded the volume of the MariaDB database.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo md-online-volume-expansion
```

<!-- PAGE_START: autoscaler/compute/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Autoscaling the Compute Resource of a MariaDB Cluster Database

This guide will show you how to use `KubeDB` to autoscale compute resources i.e. cpu and memory of a MariaDB replicaset database.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install `KubeDB` Community, Ops-Manager and Autoscaler operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* Install `Metrics Server` from [here](https://github.com/kubernetes-sigs/metrics-server#installation)
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Compute Resource Autoscaling Overview](en/autoscaler/compute/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Autoscaling of Cluster Database

Here, we are going to deploy a `MariaDB` Cluster using a supported version by `KubeDB` operator. Then we are going to apply `MariaDBAutoscaler` to set up autoscaling.

#### Deploy MariaDB Cluster

In this section, we are going to deploy a MariaDB Cluster with version `12.1.2`. Then, in the next section we will set up autoscaling for this database using `MariaDBAutoscaler` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

> If you want to autoscale MariaDB `Standalone`, Just remove the `spec.Replicas` from the below yaml and rest of the steps are same.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            cpu: "200m"
            memory: "300Mi"
          limits:
            cpu: "200m"
            memory: "300Mi"
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CRO we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/compute/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    14m
```

Let’s check the Pod containers resources,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

Let’s check the MariaDB resources,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

You can see from the above outputs that the resources are same as the one we have assigned while deploying the mariadb.

We are now ready to apply the `MariaDBAutoscaler` CRO to set up autoscaling for this database.

### Compute Resource Autoscaling

Here, we are going to set up compute resource autoscaling using a MariaDBAutoscaler Object.

#### Create MariaDBAutoscaler Object

In order to set up compute resource autoscaling for this database cluster, we have to create a `MariaDBAutoscaler` CRO with our desired configuration. Below is the YAML of the `MariaDBAutoscaler` object that we are going to create,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-compute
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  opsRequestOptions:
    timeout: 3m
    apply: IfReady
  compute:
    mariadb:
      trigger: "On"
      podLifeTimeThreshold: 5m
      resourceDiffPercentage: 20
      minAllowed:
        cpu: 250m
        memory: 400Mi
      maxAllowed:
        cpu: 1
        memory: 1Gi
      containerControlledValues: "RequestsAndLimits"
      controlledResources: ["cpu", "memory"]
```

Here,

* `spec.databaseRef.name` specifies that we are performing compute resource scaling operation on `sample-mariadb` database.
* `spec.compute.mariadb.trigger` specifies that compute autoscaling is enabled for this database.
* `spec.compute.mariadb.podLifeTimeThreshold` specifies the minimum lifetime for at least one of the pod to initiate a vertical scaling.
* `spec.compute.mariadb.resourceDiffPercentage` specifies the minimum resource difference in percentage. The default is 10%.
  If the difference between current & recommended resource is less than ResourceDiffPercentage, Autoscaler Operator will ignore the updating.
* `spec.compute.mariadb.minAllowed` specifies the minimum allowed resources for the database.
* `spec.compute.mariadb.maxAllowed` specifies the maximum allowed resources for the database.
* `spec.compute.mariadb.controlledResources` specifies the resources that are controlled by the autoscaler.
* `spec.compute.mariadb.containerControlledValues` specifies which resource values should be controlled. The default is “RequestsAndLimits”.
* `spec.opsRequestOptions.apply` has two supported value : `IfReady` & `Always`.
  Use `IfReady` if you want to process the opsReq only when the database is Ready. And use `Always` if you want to process the execution of opsReq irrespective of the Database state.
* `spec.opsRequestOptions.timeout` specifies the maximum time for each step of the opsRequest(in seconds).
  If a step doesn’t finish within the specified timeout, the ops request will result in failure.

Let’s create the `MariaDBAutoscaler` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/compute/cluster/examples/mdas-compute.yaml
mariadbautoscaler.autoscaling.kubedb.com/md-as-compute created
```

#### Verify Autoscaling is set up successfully

Let’s check that the `mariadbautoscaler` resource is created successfully,

```bash
$ kubectl get mariadbautoscaler -n demo
NAME            AGE
md-as-compute   5m56s

$ kubectl describe mariadbautoscaler md-as-compute -n demo
Name:         md-as-compute
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-09-16T11:26:58Z
  Generation:          1
  Managed Fields:
    API Version:  autoscaling.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:metadata:
        f:annotations:
          .:
          f:kubectl.kubernetes.io/last-applied-configuration:
      f:spec:
        .:
        f:compute:
          .:
          f:mariadb:
            .:
            f:containerControlledValues:
            f:controlledResources:
            f:maxAllowed:
              .:
              f:cpu:
              f:memory:
            f:minAllowed:
              .:
              f:cpu:
              f:memory:
            f:podLifeTimeThreshold:
            f:resourceDiffPercentage:
            f:trigger:
        f:databaseRef:
          .:
          f:name:
        f:opsRequestOptions:
          .:
          f:apply:
          f:timeout:
    Manager:      kubectl-client-side-apply
    Operation:    Update
    Time:         2022-09-16T11:26:58Z
    API Version:  autoscaling.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:status:
        .:
        f:checkpoints:
        f:conditions:
        f:vpas:
    Manager:         kubedb-autoscaler
    Operation:       Update
    Subresource:     status
    Time:            2022-09-16T11:27:07Z
  Resource Version:  846645
  UID:               44bd46c3-bbc5-4c4a-aff4-00c7f84c6f58
Spec:
  Compute:
    Mariadb:
      Container Controlled Values:  RequestsAndLimits
      Controlled Resources:
        cpu
        memory
      Max Allowed:
        Cpu:     1
        Memory:  1Gi
      Min Allowed:
        Cpu:                     250m
        Memory:                  400Mi
      Pod Life Time Threshold:   5m0s
      Resource Diff Percentage:  20
      Trigger:                   On
  Database Ref:
    Name:  sample-mariadb
  Ops Request Options:
    Apply:    IfReady
    Timeout:  3m0s
Status:
  Checkpoints:
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              46
        Weight:             555
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Bucket Weights:
        Index:              1
        Weight:             10000
      Reference Timestamp:  2022-09-17T00:00:00Z
      Total Weight:         1.391848625060675
    Ref:
      Container Name:     md-coordinator
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              3
        Weight:             556
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Reference Timestamp:  2022-09-17T00:00:00Z
    Ref:
      Container Name:     mariadb
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
  Conditions:
    Last Transition Time:  2022-09-16T11:27:07Z
    Message:               Successfully created mariaDBOpsRequest demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                CreateOpsRequest
    Status:                True
    Type:                  CreateOpsRequest
  Vpas:
    Conditions:
      Last Transition Time:  2022-09-16T11:27:02Z
      Status:                True
      Type:                  RecommendationProvided
    Recommendation:
      Container Recommendations:
        Container Name:  mariadb
        Lower Bound:
          Cpu:     250m
          Memory:  400Mi
        Target:
          Cpu:     250m
          Memory:  400Mi
        Uncapped Target:
          Cpu:     25m
          Memory:  262144k
        Upper Bound:
          Cpu:     1
          Memory:  1Gi
    Vpa Name:      sample-mariadb
Events:            <none>
```

So, the `mariadbautoscaler` resource is created successfully.

We can verify from the above output that `status.vpas` contains the `RecommendationProvided` condition to true. And in the same time, `status.vpas.recommendation.containerRecommendations` contain the actual generated recommendation.

Our autoscaler operator continuously watches the recommendation generated and creates an `mariadbopsrequest` based on the recommendations, if the database pod resources are needed to scaled up or down.

Let’s watch the `mariadbopsrequest` in the demo namespace to see if any `mariadbopsrequest` object is created. After some time you’ll see that a `mariadbopsrequest` will be created based on the recommendation.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                          TYPE              STATUS       AGE
mdops-sample-mariadb-6xc1kc   VerticalScaling   Progressing  7s
```

Let’s wait for the ops request to become successful.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                              TYPE              STATUS       AGE
mdops-vpa-sample-mariadb-z43wc8   VerticalScaling   Successful   3m32s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to scale the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-vpa-sample-mariadb-z43wc8
Name:         mdops-sample-mariadb-6xc1kc
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-09-16T11:27:07Z
  Generation:          1
  Managed Fields:
    API Version:  ops.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:metadata:
        f:ownerReferences:
          .:
          k:{"uid":"44bd46c3-bbc5-4c4a-aff4-00c7f84c6f58"}:
      f:spec:
        .:
        f:apply:
        f:databaseRef:
          .:
          f:name:
        f:timeout:
        f:type:
        f:verticalScaling:
          .:
          f:mariadb:
            .:
            f:limits:
              .:
              f:cpu:
              f:memory:
            f:requests:
              .:
              f:cpu:
              f:memory:
    Manager:      kubedb-autoscaler
    Operation:    Update
    Time:         2022-09-16T11:27:07Z
    API Version:  ops.kubedb.com/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:status:
        .:
        f:conditions:
        f:observedGeneration:
        f:phase:
    Manager:      kubedb-ops-manager
    Operation:    Update
    Subresource:  status
    Time:         2022-09-16T11:27:07Z
  Owner References:
    API Version:           autoscaling.kubedb.com/v1alpha1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  MariaDBAutoscaler
    Name:                  md-as-compute
    UID:                   44bd46c3-bbc5-4c4a-aff4-00c7f84c6f58
  Resource Version:        846324
  UID:                     c2b30107-c6d3-44bb-adf3-135edc5d615b
Spec:
  Apply:  IfReady
  Database Ref:
    Name:   sample-mariadb
  Timeout:  2m0s
  Type:     VerticalScaling
  Vertical Scaling:
    Mariadb:
      Limits:
        Cpu:     250m
        Memory:  400Mi
      Requests:
        Cpu:     250m
        Memory:  400Mi
Status:
  Conditions:
    Last Transition Time:  2022-09-16T11:27:07Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-09-16T11:30:42Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                SuccessfullyRestatedPetSet
    Status:                True
    Type:                  RestartPetSet
    Last Transition Time:  2022-09-16T11:30:47Z
    Message:               Vertical scale successful for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                SuccessfullyPerformedVerticalScaling
    Status:                True
    Type:                  VerticalScaling
    Last Transition Time:  2022-09-16T11:30:47Z
    Message:               Controller has successfully scaled the MariaDB demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type    Reason      Age    From                        Message
  ----    ------      ----   ----                        -------
  Normal  Starting    8m48s  KubeDB Enterprise Operator  Start processing for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
  Normal  Starting    8m48s  KubeDB Enterprise Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal  Successful  8m48s  KubeDB Enterprise Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-sample-mariadb-6xc1kc
  Normal  Starting    8m43s  KubeDB Enterprise Operator  Restarting Pod: demo/sample-mariadb-0
  Normal  Starting    7m33s  KubeDB Enterprise Operator  Restarting Pod: demo/sample-mariadb-1
  Normal  Starting    6m23s  KubeDB Enterprise Operator  Restarting Pod: demo/sample-mariadb-2
  Normal  Successful  5m13s  KubeDB Enterprise Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
  Normal  Successful  5m8s   KubeDB Enterprise Operator  Vertical scale successful for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
  Normal  Starting    5m8s   KubeDB Enterprise Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal  Successful  5m8s   KubeDB Enterprise Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal  Successful  5m8s   KubeDB Enterprise Operator  Controller has Successfully scaled the MariaDB database: demo/sample-mariadb
```

Now, we are going to verify from the Pod, and the MariaDB yaml whether the resources of the replicaset database has updated to meet up the desired state, Let’s check,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}

$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}
```

The above output verifies that we have successfully autoscaled the resources of the MariaDB replicaset database.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadbautoscaler -n demo md-as-compute
kubectl delete ns demo
```

<!-- PAGE_START: autoscaler/compute/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Compute Resource Autoscaling

This guide will give an overview on how KubeDB Autoscaler operator autoscales the database compute resources i.e. cpu and memory using `mariadbautoscaler` crd.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Compute Autoscaling Works

The following diagram shows how KubeDB Autoscaler operator autoscales the resources of `MariaDB` database components. Open the image in a new tab to see the enlarged version.

  ![Auto Scaling process of MariaDB](images/autoscaler_compute_overview_mdas-compute.png)

Fig: Auto Scaling process of MariaDB

The Auto Scaling process consists of the following steps:

1. At first, the user creates a `MariaDB` Custom Resource Object (CRO).
2. `KubeDB` Community operator watches the `MariaDB` CRO.
3. When the operator finds a `MariaDB` CRO, it creates required number of `PetSets` and related necessary stuff like secrets, services, etc.
4. Then, in order to set up autoscaling of the CPU & Memory resources of the `MariaDB` database the user creates a `MariaDBAutoscaler` CRO with desired configuration.
5. `KubeDB` Autoscaler operator watches the `MariaDBAutoscaler` CRO.
6. `KubeDB` Autoscaler operator utilizes the modified version of Kubernetes official [VPA-Recommender](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/pkg) for different components of the database, as specified in the `mariadbautoscaler` CRO.
   It generates recommendations based on resource usages, & store them in the `status` section of the autoscaler CRO.
7. If the generated recommendation doesn’t match the current resources of the database, then `KubeDB` Autoscaler operator creates a `MariaDBOpsRequest` CRO to scale the database to match the recommendation provided by the VPA object.
8. `KubeDB Ops-Manager operator` watches the `MariaDBOpsRequest` CRO.
9. Lastly, the `KubeDB Ops-Manager operator` will scale the database component vertically as specified on the `MariaDBOpsRequest` CRO.

In the next docs, we are going to show a step by step guide on Autoscaling of MariaDB database using `MariaDBAutoscaler` CRD.

<!-- PAGE_START: autoscaler/storage/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Storage Autoscaling of a MariaDB Cluster

This guide will show you how to use `KubeDB` to autoscale the storage of a MariaDB Replicaset database.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install `KubeDB` Community, Enterprise and Autoscaler operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* Install `Metrics Server` from [here](https://github.com/kubernetes-sigs/metrics-server#installation)
* Install Prometheus from [here](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
* You must have a `StorageClass` that supports volume expansion.
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Storage Autoscaling Overview](en/autoscaler/storage/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Storage Autoscaling of Cluster Database

At first verify that your cluster has a storage class, that supports volume expansion. Let’s check,

```bash
$ kubectl get storageclass
NAME                  PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
standard (default)    rancher.io/local-path   Delete          WaitForFirstConsumer   false                  79m
topolvm-provisioner   topolvm.cybozu.com      Delete          WaitForFirstConsumer   true                   78m
```

We can see from the output the `topolvm-provisioner` storage class has `ALLOWVOLUMEEXPANSION` field as true. So, this storage class supports volume expansion. We can use it. You can install topolvm from [here](https://github.com/topolvm/topolvm)

Now, we are going to deploy a `MariaDB` replicaset using a supported version by `KubeDB` operator. Then we are going to apply `MariaDBAutoscaler` to set up autoscaling.

#### Deploy MariaDB Cluster

In this section, we are going to deploy a MariaDB replicaset database with version `12.1.2`. Then, in the next section we will set up autoscaling for this database using `MariaDBAutoscaler` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

> If you want to autoscale MariaDB `Standalone`, Just remove the `spec.Replicas` from the below yaml and rest of the steps are same.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "topolvm-provisioner"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CRO we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/storage/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    3m46s
```

Let’s check volume size from petset, and from the persistent volume,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1Gi"

$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-43266d76-f280-4cca-bd78-d13660a84db9   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            57s
pvc-4a509b05-774b-42d9-b36d-599c9056af37   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            58s
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            57s
```

You can see the petset has 1GB storage, and the capacity of all the persistent volume is also 1GB.

We are now ready to apply the `MariaDBAutoscaler` CRO to set up storage autoscaling for this database.

### Storage Autoscaling

Here, we are going to set up storage autoscaling using a MariaDBAutoscaler Object.

#### Create MariaDBAutoscaler Object

In order to set up vertical autoscaling for this replicaset database, we have to create a `MariaDBAutoscaler` CRO with our desired configuration. Below is the YAML of the `MariaDBAutoscaler` object that we are going to create,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-st
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  storage:
    mariadb:
      trigger: "On"
      usageThreshold: 20
      scalingThreshold: 20
      expansionMode: "Online"
```

Here,

* `spec.databaseRef.name` specifies that we are performing vertical scaling operation on `sample-mariadb` database.
* `spec.storage.mariadb.trigger` specifies that storage autoscaling is enabled for this database.
* `spec.storage.mariadb.usageThreshold` specifies storage usage threshold, if storage usage exceeds `20%` then storage autoscaling will be triggered.
* `spec.storage.mariadb.scalingThreshold` specifies the scaling threshold. Storage will be scaled to `20%` of the current amount.
* `spec.storage.mariadb.expansionMode` specifies the expansion mode of volume expansion `MariaDBOpsRequest` created by `MariaDBAutoscaler`. topolvm-provisioner supports online volume expansion so here `expansionMode` is set as “Online”.

Let’s create the `MariaDBAutoscaler` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/storage/cluster/examples/mdas-storage.yaml
mariadbautoscaler.autoscaling.kubedb.com/md-as-st created
```

#### Storage Autoscaling is set up successfully

Let’s check that the `mariadbautoscaler` resource is created successfully,

```bash
$ kubectl get mariadbautoscaler -n demo
NAME           AGE
md-as-st   33s

$ kubectl describe mariadbautoscaler md-as-st -n demo
Name:         md-as-st
Namespace:    demo
Labels:       <none>
Annotations:  API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-01-14T06:08:02Z
  Generation:          1
  Managed Fields:
    ...
  Resource Version:  24009
  UID:               4f45a3b3-fc72-4d04-b52c-a770944311f6
Spec:
  Database Ref:
    Name:  sample-mariadb
  Storage:
    Mariadb:
      Scaling Threshold:  20
      Trigger:            On
      Usage Threshold:    20
Events:                   <none>
```

So, the `mariadbautoscaler` resource is created successfully.

Now, for this demo, we are going to manually fill up the persistent volume to exceed the `usageThreshold` using `dd` command to see if storage autoscaling is working or not.

Let’s exec into the database pod and fill the database volume(`var/lib/mysql`) using the following commands:

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  357M  658M  36% /var/lib/mysql
root@sample-mariadb-0:/ dd if=/dev/zero of=/var/lib/mysql/file.img bs=500M count=1
1+0 records in
1+0 records out
524288000 bytes (524 MB, 500 MiB) copied, 0.340877 s, 1.5 GB/s
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  857M  158M  85% /var/lib/mysql
```

So, from the above output we can see that the storage usage is 83%, which exceeded the `usageThreshold` 20%.

Let’s watch the `mariadbopsrequest` in the demo namespace to see if any `mariadbopsrequest` object is created. After some time you’ll see that a `mariadbopsrequest` of type `VolumeExpansion` will be created based on the `scalingThreshold`.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                         TYPE              STATUS        AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Progressing   15s
```

Let’s wait for the ops request to become successful.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                         TYPE              STATUS       AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Successful   97s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to expand the volume of the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mops-sample-mariadb-xojkua
Name:         mops-sample-mariadb-xojkua
Namespace:    demo
Labels:       app.kubernetes.io/component=database
              app.kubernetes.io/instance=sample-mariadb
              app.kubernetes.io/managed-by=kubedb.com
              app.kubernetes.io/name=mariadbs.kubedb.com
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2022-01-14T06:13:10Z
  Generation:          1
  Managed Fields: ...
  Owner References:
    API Version:           autoscaling.kubedb.com/v1alpha1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  MariaDBAutoscaler
    Name:                  md-as-st
    UID:                   4f45a3b3-fc72-4d04-b52c-a770944311f6
  Resource Version:        25557
  UID:                     90763a49-a03f-407c-a233-fb20c4ab57d7
Spec:
  Database Ref:
    Name:  sample-mariadb
  Type:    VolumeExpansion
  Volume Expansion:
    Mariadb:  1594884096
Status:
  Conditions:
    Last Transition Time:  2022-01-14T06:13:10Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                OpsRequestProgressingStarted
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2022-01-14T06:14:25Z
    Message:               Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                SuccessfullyVolumeExpanded
    Status:                True
    Type:                  VolumeExpansion
    Last Transition Time:  2022-01-14T06:14:25Z
    Message:               Controller has successfully expand the volume of MariaDB demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                OpsRequestProcessedSuccessfully
    Status:                True
    Type:                  Successful
  Observed Generation:     3
  Phase:                   Successful
Events:
  Type    Reason      Age    From                        Message
  ----    ------      ----   ----                        -------
  Normal  Starting    2m58s  KubeDB Enterprise Operator  Start processing for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
  Normal  Starting    2m58s  KubeDB Enterprise Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal  Successful  2m58s  KubeDB Enterprise Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mops-sample-mariadb-xojkua
  Normal  Successful  103s   KubeDB Enterprise Operator  Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
  Normal  Starting    103s   KubeDB Enterprise Operator  Updating MariaDB storage
  Normal  Successful  103s   KubeDB Enterprise Operator  Successfully Updated MariaDB storage
  Normal  Starting    103s   KubeDB Enterprise Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal  Successful  103s   KubeDB Enterprise Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal  Successful  103s   KubeDB Enterprise Operator  Controller has Successfully expand the volume of MariaDB: demo/sample-mariadb
```

Now, we are going to verify from the `Petset`, and the `Persistent Volume` whether the volume of the replicaset database has expanded to meet the desired state, Let’s check,

```bash
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1594884096"
$ kubectl get pv -n demo
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-43266d76-f280-4cca-bd78-d13660a84db9   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-2   topolvm-provisioner            23m
pvc-4a509b05-774b-42d9-b36d-599c9056af37   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-0   topolvm-provisioner            24m
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            23m
```

The above output verifies that we have successfully autoscaled the volume of the MariaDB replicaset database.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadbautoscaler -n demo md-as-st
kubectl delete ns demo
```

<!-- PAGE_START: autoscaler/storage/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Vertical Autoscaling

This guide will give an overview on how KubeDB Autoscaler operator autoscales the database storage using `mariadbautoscaler` crd.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Storage Autoscaling Works

The following diagram shows how KubeDB Autoscaler operator autoscales the resources of `MariaDB` database components. Open the image in a new tab to see the enlarged version.

  ![Storage Autoscaling process of MariaDB](images/autoscaler_storage_overview_mdas-storage.jpeg)

Fig: Storage Autoscaling process of MariaDB

The Auto Scaling process consists of the following steps:

1. At first, a user creates a `MariaDB` Custom Resource (CR).
2. `KubeDB` Community operator watches the `MariaDB` CR.
3. When the operator finds a `MariaDB` CR, it creates required number of `PetSets` and related necessary stuff like secrets, services, etc.
4. Each PetSet creates a Persistent Volume according to the Volume Claim Template provided in the petset configuration. This Persistent Volume will be expanded by the `KubeDB` Enterprise operator.
5. Then, in order to set up storage autoscaling of the `MariaDB` database the user creates a `MariaDBAutoscaler` CRO with desired configuration.
6. `KubeDB` Autoscaler operator watches the `MariaDBAutoscaler` CRO.
7. `KubeDB` Autoscaler operator continuously watches persistent volumes of the databases to check if it exceeds the specified usage threshold.
8. If the usage exceeds the specified usage threshold, then `KubeDB` Autoscaler operator creates a `MariaDBOpsRequest` to expand the storage of the database.
9. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CRO.
10. Then the `KubeDB` Enterprise operator will expand the storage of the database component as specified on the `MariaDBOpsRequest` CRO.

In the next docs, we are going to show a step by step guide on Autoscaling storage of various MariaDB database components using `MariaDBAutoscaler` CRD.

<!-- PAGE_START: backup/kubestash/application-level.md -->
# Application Level Backup and Restore MariaDB database using KubeStash

KubeStash offers application-level backup and restore functionality for `MariaDB` databases. It captures both manifest and data backups of any `MariaDB` database in a single snapshot. During the restore process, KubeStash first applies the `MariaDB` manifest to the cluster and then restores the data into it.

This guide will give you an overview how you can take application-level backup and restore your `MariaDB` databases using `Kubestash`.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using `Minikube` or `Kind`.
* Install `KubeDB` in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* Install `KubeStash` in your cluster following the steps [here](https://kubestash.com/docs/latest/setup/install/kubestash).
* Install KubeStash `kubectl` plugin following the steps [here](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* If you are not familiar with how KubeStash backup and restore MariaDB databases, please check the following guide [here](en/backup/kubestash/overview.md).

You should be familiar with the following `KubeStash` concepts:

* [BackupStorage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [BackupConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
* [BackupSession](https://kubestash.com/docs/latest/concepts/crds/backupsession/)
* [RestoreSession](https://kubestash.com/docs/latest/concepts/crds/restoresession/)
* [Addon](https://kubestash.com/docs/latest/concepts/crds/addon/)
* [Function](https://kubestash.com/docs/latest/concepts/crds/function/)
* [Task](https://kubestash.com/docs/latest/concepts/crds/addon/#task-specification)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

> **Note:** YAML files used in this tutorial are stored in [docs/guides/mariadb/backup/kubestash/application-level/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples) directory of [kubedb/docs](https://github.com/kubedb/docs) repository.

## Backup MariaDB

KubeStash supports backups for `MariaDB` instances across different configurations, including Standalone and Galera Cluster setups. In this demonstration, we’ll focus on a `MariaDB` database using Galera cluster configuration. The backup and restore process is similar for Standalone configuration.

This section will demonstrate how to take application-level backup of a `MariaDB` database. Here, we are going to deploy a `MariaDB` database using KubeDB. Then, we are going to back up the database at the application level to a `GCS` bucket. Finally, we will restore the entire `MariaDB` database.

### Deploy Sample MariaDB Database

Let’s deploy a sample `MariaDB` database and insert some data into it.

**Create MariaDB CR:**

Below is the YAML of a sample `MariaDB` CR that we are going to create for this tutorial:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Create the above `MariaDB` CR,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

KubeDB will deploy a `MariaDB` database according to the above specification. It will also create the necessary `Secrets` and `Services` to access the database.

Let’s check if the database is ready to use,

```bash
$ kubectl get md -n demo sample-mariadb
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m1s
```

The database is `Ready`. Verify that KubeDB has created a `Secret` and a `Service` for this database using the following commands,

```bash
$ kubectl get secret -n demo 
NAME                          TYPE                       DATA   AGE
sample-mariadb-auth           kubernetes.io/basic-auth   2      5m49s

$ kubectl get service -n demo -l=app.kubernetes.io/instance=sample-mariadb
NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE
sample-mariadb        ClusterIP   10.128.92.155   <none>        3306/TCP        62s
sample-mariadb-pods   ClusterIP   None            <none>        3306/TCP        62s
```

Here, we have to use service `sample-mariadb` and secret `sample-mariadb-auth` to connect with the database. `KubeDB` creates an [AppBinding](en/concepts/appbinding.md) CR that holds the necessary information to connect with the database.

**Verify AppBinding:**

Verify that the `AppBinding` has been created successfully using the following command,

```bash
$ kubectl get appbindings -n demo
NAME                      TYPE                  VERSION   AGE
sample-mariadb            kubedb.com/mariadb    11.1.3    6m14s
```

Let’s check the YAML of the above `AppBinding`,

```bash
$ kubectl get appbindings -n demo sample-mariadb -o yaml
```

```yaml
apiVersion: v1
items:
  - apiVersion: appcatalog.appscode.com/v1alpha1
    kind: AppBinding
    metadata:
      annotations:
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"deletionPolicy":"WipeOut","replicas":3,"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}}},"storageType":"Durable","version":"11.1.3"}}          
      creationTimestamp: "2024-09-18T08:31:32Z"
      generation: 1
      labels:
        app.kubernetes.io/component: database
        app.kubernetes.io/instance: sample-mariadb
        app.kubernetes.io/managed-by: kubedb.com
        app.kubernetes.io/name: mariadbs.kubedb.com
      name: sample-mariadb
      namespace: demo
      ownerReferences:
        - apiVersion: kubedb.com/v1
          blockOwnerDeletion: true
          controller: true
          kind: MariaDB
          name: sample-mariadb
          uid: 35400a0b-97b1-4437-a3b9-416678b71adf
      resourceVersion: "1728063"
      uid: 8ebec467-32d5-416a-975a-67e890a4efe6
    spec:
      appRef:
        apiGroup: kubedb.com
        kind: MariaDB
        name: sample-mariadb
        namespace: demo
      clientConfig:
        service:
          name: sample-mariadb
          port: 3306
          scheme: tcp
        url: tcp(sample-mariadb.demo.svc:3306)/
      parameters:
        address: gcomm://sample-mariadb-0.sample-mariadb-pods.demo,sample-mariadb-1.sample-mariadb-pods.demo,sample-mariadb-2.sample-mariadb-pods.demo
        apiVersion: config.kubedb.com/v1alpha1
        group: sample-mariadb
        kind: GaleraArbitratorConfiguration
        sstMethod: xtrabackup-v2
        stash:
          addon:
            backupTask:
              name: mariadb-backup-10.5.8
            restoreTask:
              name: mariadb-restore-10.5.8
      secret:
        name: sample-mariadb-auth
        
        
        
        
      type: kubedb.com/mariadb
      version: 12.1.2
kind: List
metadata:
  resourceVersion: ""
```

KubeStash uses the `AppBinding` CR to connect with the target database. It requires the following two fields to set in AppBinding’s `.spec` section.

Here,

* `.spec.clientConfig.service.name` specifies the name of the Service that connects to the database.
* `.spec.secret` specifies the name of the Secret that holds necessary credentials to access the database.
* `.spec.type` specifies the types of the app that this AppBinding is pointing to. KubeDB generated AppBinding follows the following format: `<app group>/<app resource type>`.

**Insert Sample Data:**

Now, we are going to exec into one of the database pod and create some sample data. At first, find out the database `Pod` using the following command,

```bash
$ kubectl get pods -n demo --selector="app.kubernetes.io/instance=sample-mariadb" 
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   2/2     Running   0          8m4s
sample-mariadb-1   2/2     Running   0          8m3s
sample-mariadb-2   2/2     Running   0          8m3s
```

Now, let’s exec into the pod and create a table,

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');
    
MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

Now, we are ready to backup the database.

### Prepare Backend

We are going to store our backup data into a `GCS` bucket. We have to create a `Secret` with necessary credentials and a `BackupStorage` CR to use this backend. If you want to use a different backend, please read the respective backend configuration doc from [here](https://kubestash.com/docs/latest/guides/backends/overview/).

**Create Secret:**

Let’s create a secret called `gcs-secret` with access credentials to our desired GCS bucket,

```bash
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat /path/to/downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Create BackupStorage:**

Now, create a `BackupStorage` using this secret. Below is the YAML of `BackupStorage` CR we are going to create,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: gcs-storage
  namespace: demo
spec:
  storage:
    provider: gcs
    gcs:
      bucket: kubestash-qa
      prefix: demo
      secretName: gcs-secret
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: Delete
```

Let’s create the BackupStorage we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/backupstorage.yaml
backupstorage.storage.kubestash.com/gcs-storage created
```

Now, we are ready to backup our database to our desired backend.

**Create RetentionPolicy:**

Now, let’s create a `RetentionPolicy` to specify how the old Snapshots should be cleaned up.

Below is the YAML of the `RetentionPolicy` object that we are going to create,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: demo-retention
  namespace: demo
spec:
  default: true
  failedSnapshots:
    last: 2
  maxRetentionPeriod: 2mo
  successfulSnapshots:
    last: 5
  usagePolicy:
    allowedNamespaces:
      from: All
```

Let’s create the above `RetentionPolicy`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/retentionpolicy.yaml
retentionpolicy.storage.kubestash.com/demo-retention created
```

### Backup

We have to create a `BackupConfiguration` targeting respective `sample-mariadb` MariaDB database. Then, KubeStash will create a `CronJob` for each session to take periodic backup of that database.

At first, we need to create a secret with a Restic password for backup data encryption.

**Create Secret:**

Let’s create a secret called `encrypt-secret` with the Restic password,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ kubectl create secret generic -n demo encrypt-secret \
    --from-file=./RESTIC_PASSWORD \
secret "encrypt-secret" created
```

**Create BackupConfiguration:**

Below is the YAML for `BackupConfiguration` CR to take application-level backup of the `sample-mariadb` database that we have deployed earlier,

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: manifest-backup
          - name: logical-backup
```

* `.spec.sessions[*].schedule` specifies that we want to backup at `5 minutes` interval.
* `.spec.target` refers to the targeted `sample-mariadb` MariaDB database that we created earlier.
* `.spec.sessions[*].addon.tasks[*].name[*]` specifies that both the `manifest-backup` and `logical-backup` tasks will be executed.

Let’s create the `BackupConfiguration` CR that we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/backupconfiguration.yaml
backupconfiguration.core.kubestash.com/sample-mariadb-backup created
```

**Verify Backup Setup Successful**

If everything goes well, the phase of the `BackupConfiguration` should be `Ready`. The `Ready` phase indicates that the backup setup is successful. Let’s verify the `Phase` of the BackupConfiguration,

```bash
$ kubectl get backupconfiguration -n demo
NAME                     PHASE   PAUSED   AGE
sample-mariadb-backup   Ready            2m50s
```

Additionally, we can verify that the `Repository` specified in the `BackupConfiguration` has been created using the following command,

```bash
$ kubectl get repo -n demo
NAME                  INTEGRITY   SNAPSHOT-COUNT   SIZE     PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo                 0                0 B      Ready                            3m
```

KubeStash keeps the backup for `Repository` YAMLs. If we navigate to the GCS bucket, we will see the `Repository` YAML stored in the `demo/mariadb` directory.

**Verify CronJob:**

It will also create a `CronJob` with the schedule specified in `spec.sessions[*].scheduler.schedule` field of `BackupConfiguration` CR.

Verify that the `CronJob` has been created using the following command,

```bash
$ kubectl get cronjob -n demo
NAME                                             SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
trigger-sample-mariadb-backup-frequent-backup   */5 * * * *             0        2m45s           3m25s
```

**Verify BackupSession:**

KubeStash triggers an instant backup as soon as the `BackupConfiguration` is ready. After that, backups are scheduled according to the specified schedule.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                INVOKER-TYPE          INVOKER-NAME              PHASE       DURATION   AGE
sample-mariadb-backup-frequent-backup-1726651003   BackupConfiguration   sample-mariadb-backup    Succeeded              7m22s
```

We can see from the above output that the backup session has succeeded. Now, we are going to verify whether the backup data has been stored in the backend.

**Verify Backup:**

Once a backup is complete, KubeStash will update the respective `Repository` CR to reflect the backup. Check that the repository `sample-mariadb-backup` has been updated by the following command,

```bash
$ kubectl get repository -n demo gcs-mariadb-repo
NAME                       INTEGRITY   SNAPSHOT-COUNT   SIZE    PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo           true        1                806 B   Ready   8m27s                    9m18s
```

At this moment we have one `Snapshot`. Run the following command to check the respective `Snapshot` which represents the state of a backup run for an application.

```bash
$ kubectl get snapshots.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                  REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726651003       gcs-mariadb-repo   frequent-backup   2024-01-23T13:10:54Z   Delete            Succeeded   16h
```

> Note: KubeStash creates a `Snapshot` with the following labels:
>
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> These labels can be used to watch only the `Snapshot`s related to our target Database or `Repository`.

If we check the YAML of the `Snapshot`, we can find the information about the backup components of the Database.

```bash
$ kubectl get snapshots -n demo gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725449400 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T09:16:53Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: gcs-mariadb-repo
  annotations:
    kubedb.com/db-version: 11.1.3
  name: gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726651003
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: gcs-mariadb-repo
      uid: 82a72ef1-1071-49df-b44f-d1f395017262
  resourceVersion: "1734435"
  uid: b96499b6-f882-43e8-ba2a-badb54f96bb8
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: sample-mariadb-backup-frequent-backup-1726651003
  deletionPolicy: Delete
  repository: gcs-mariadb-repo
  session: frequent-backup
  snapshotID: 01J826Q68983K50JRZV2AX1QZF
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.291630733s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 6a9b3e0ccd380f93ff414157156f4ac9d144fa15c5c3adeea2faa09cf44fb175
            size: 3.139 KiB
            uploaded: 3.431 KiB
      size: 1.277 KiB
    manifest:
      driver: Restic
      duration: 2.613551084s
      integrity: true
      path: repository/v1/frequent-backup/manifest
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: /kubestash-tmp/manifest
            id: 47d89d4149cd59bfc8e701b8171a864d0259486820c477a9c2b3a8c0d80de237
            size: 2.507 KiB
            uploaded: 3.939 KiB
      size: 1.913 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T09:16:53Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T09:17:18Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 3.188 KiB
  snapshotTime: "2024-09-18T09:16:53Z"
  totalComponents: 2
```

> KubeStash uses `mariadb-dump` to perform backups of target `MariaDB` databases. Therefore, the component name for logical backups is set as `dump`.

> KubeStash set component name as `manifest` for the `manifest backup` of MariaDB databases.

Now, if we navigate to the GCS bucket, we will see the backup data stored in the `demo/mariadb/repository/v1/frequent-backup/dump` directory. KubeStash also keeps the backup for `Snapshot` YAMLs, which can be found in the `demo/mariadb/snapshots` directory.

> Note: KubeStash stores all dumped data encrypted in the backup directory, meaning it remains unreadable until decrypted.

## Restore

In this section, we are going to restore the entire database from the backup that we have taken in the previous section.

For this tutorial, we will restore the database in a separate namespace called `dev`.

First, create the namespace by running the following command:

```bash
$ kubectl create ns dev
namespace/dev created
```

#### Create RestoreSession:

We need to create a RestoreSession CR.

Below, is the contents of YAML file of the `RestoreSession` CR that we are going to create to restore the entire database.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: restore-sample-mariadb
  namespace: demo
spec:
  manifestOptions:
    mariaDB:
      db: true
      restoreNamespace: dev
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
      - name: manifest-restore
```

Here,

* `.spec.manifestOptions.mariadb.db` specifies whether to restore the DB manifest or not.
* `.spec.dataSource.repository` specifies the Repository object that holds the backup data.
* `.spec.dataSource.snapshot` specifies to restore from latest `Snapshot`.
* `.spec.addon.tasks[*]` specifies that both the `manifest-restore` and `logical-backup-restore` tasks.

Let’s create the RestoreSession CR object we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/application-level/examples/restoresession.yaml
restoresession.core.kubestash.com/restore-sample-mariadb created
```

Once, you have created the `RestoreSession` object, KubeStash will create restore Job. Run the following command to watch the phase of the `RestoreSession` object,

```bash
$ watch kubectl get restoresession -n demo
Every 2.0s: kubectl get restores... AppsCode-PC-03: Wed Aug 21 10:44:05 2024
NAME                      REPOSITORY            FAILURE-POLICY   PHASE       DURATION   AGE
restore-sample-mariadb   gcs-mariadb-repo                      Succeeded   3s         53s
```

The `Succeeded` phase means that the restore process has been completed successfully.

#### Verify Restored MariaDB Manifest:

In this section, we will verify whether the desired `MariaDB` database manifest has been successfully applied to the cluster.

```bash
$ kubectl get mariadb -n dev 
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m18s
```

The output confirms that the `MariaDB` database has been successfully created with the same configuration as it had at the time of backup.

#### Verify Restored Data:

In this section, we are going to verify whether the desired data has been restored successfully. We are going to connect to the database server and check whether the database and the table we created earlier in the original database are restored.

At first, check if the database has gone into **`Ready`** state by the following command,

```bash
$ kubectl get mariadb -n dev sample-mariadb
NAME              VERSION   STATUS   AGE
sample-mariadb    11.1.3    Ready    5m18s
```

Now, find out the database `Pod` by the following command,

```bash
$ kubectl get pods -n dev --selector="app.kubernetes.io/instance=sample-mariadb"
NAME                READY   STATUS    RESTARTS   AGE
sample-mariadb-0   2/2     Running   0          12m
sample-mariadb-1   2/2     Running   0          12m
sample-mariadb-2   2/2     Running   0          12m
```

Now, lets exec one of the Pod and verify restored data.

```bash
$ kubectl exec -it -n dev sample-mariadb-0 -- bash
```

```mysql
mysql@restored-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> use hello;

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

So, from the above output, we can see the `hello` database we had created in the original database `sample-mariadb` has been restored successfully.

## Cleanup

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete backupconfigurations.core.kubestash.com  -n demo sample-mariadb-backup
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete restoresessions.core.kubestash.com -n demo restore-sample-mariadb
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadb -n dev sample-mariadb
```

<!-- PAGE_START: backup/kubestash/auto-backup.md -->
# Backup MariaDB using KubeStash Auto-Backup

KubeStash can automatically be configured to backup any `MariaDB` databases in your cluster. KubeStash enables cluster administrators to deploy backup `blueprints` ahead of time so database owners can easily backup any `MariaDB` database with a few annotations.

In this tutorial, we are going to show how you can configure a backup blueprint for `MariaDB` databases in your cluster and backup them with a few annotations.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using `Minikube` or `Kind`.
* Install `KubeDB` in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* Install `KubeStash` in your cluster following the steps [here](https://kubestash.com/docs/latest/setup/install/kubestash).
* Install KubeStash `kubectl` plugin following the steps [here](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* If you are not familiar with how KubeStash backup and restore `MariaDB` databases, please check the following guide [here](en/backup/kubestash/overview.md).

You should be familiar with the following `KubeStash` concepts:

* [BackupStorage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [BackupConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
* [BackupSession](https://kubestash.com/docs/latest/concepts/crds/backupsession/)
* [RestoreSession](https://kubestash.com/docs/latest/concepts/crds/restoresession/)
* [Addon](https://kubestash.com/docs/latest/concepts/crds/addon/)
* [Function](https://kubestash.com/docs/latest/concepts/crds/function/)
* [Task](https://kubestash.com/docs/latest/concepts/crds/addon/#task-specification)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

> **Note:** YAML files used in this tutorial are stored in [docs/guides/mariadb/backup/kubestash/auto-backup/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples) directory of [kubedb/docs](https://github.com/kubedb/docs) repository.

### Prepare Backend

We are going to store our backup data into a `GCS` bucket. We have to create a `Secret` with necessary credentials and a `BackupStorage` CR to use this backend. If you want to use a different backend, please read the respective backend configuration doc from [here](https://kubestash.com/docs/latest/guides/backends/overview/).

**Create Secret:**

Let’s create a secret called `gcs-secret` with access credentials to our desired GCS bucket,

```bash
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat /path/to/downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Create BackupStorage:**

Now, create a `BackupStorage` using this secret. Below is the YAML of `BackupStorage` CR we are going to create,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: gcs-storage
  namespace: demo
spec:
  storage:
    provider: gcs
    gcs:
      bucket: kubestash-qa
      prefix: blueprint
      secretName: gcs-secret
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: Delete
```

Let’s create the BackupStorage we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/backupstorage.yaml
backupstorage.storage.kubestash.com/gcs-storage created
```

Now, we are ready to backup our database to our desired backend.

**Create RetentionPolicy:**

Now, let’s create a `RetentionPolicy` to specify how the old Snapshots should be cleaned up.

Below is the YAML of the `RetentionPolicy` object that we are going to create,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: demo-retention
  namespace: demo
spec:
  default: true
  failedSnapshots:
    last: 2
  maxRetentionPeriod: 2mo
  successfulSnapshots:
    last: 5
  usagePolicy:
    allowedNamespaces:
      from: All
```

Let’s create the above `RetentionPolicy`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/retentionpolicy.yaml
retentionpolicy.storage.kubestash.com/demo-retention created
```

**Create Secret:**

We also need to create a secret with a `Restic` password for backup data encryption.

Let’s create a secret called `encrypt-secret` with the Restic password,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ kubectl create secret generic -n demo encrypt-secret \
    --from-file=./RESTIC_PASSWORD \
secret "encrypt-secret" created
```

## Auto-backup with default configurations

In this section, we are going to backup a `MariaDB` database of `demo` namespace. We are going to use the default configurations which will be specified in the `BackupBlueprint` CR.

**Prepare Backup Blueprint**

A `BackupBlueprint` allows you to specify a template for the `Repository`,`Session` or `Variables` of `BackupConfiguration` in a Kubernetes native way.

Now, we have to create a `BackupBlueprint` CR with a blueprint for `BackupConfiguration` object.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupBlueprint
metadata:
  name: mariadb-default-backup-blueprint
  namespace: demo
spec:
  usagePolicy:
    allowedNamespaces:
      from: All
  backupConfigurationTemplate:
    deletionPolicy: OnDelete
    backends:
      - name: gcs-backend
        storageRef:
          namespace: demo
          name: gcs-storage
        retentionPolicy:
          name: demo-retention
          namespace: demo
    sessions:
      - name: frequent-backup
        sessionHistoryLimit: 3
        scheduler:
          schedule: "*/5 * * * *"
          jobTemplate:
            backoffLimit: 1
        repositories:
          - name: default-blueprint
            backend: gcs-backend
            directory: /default-blueprint
            encryptionSecret:
              name: encrypt-secret
              namespace: demo
        addon:
          name: mariadb-addon
          tasks:
            - name: logical-backup
```

Here,

* `.spec.backupConfigurationTemplate.backends[*].storageRef` refers our earlier created `gcs-storage` backupStorage.
* `.spec.backupConfigurationTemplate.sessions[*].schedule` specifies that we want to backup the database at `5 minutes` interval.

Let’s create the `BackupBlueprint` we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/default-backupblueprint.yaml
backupblueprint.core.kubestash.com/mariadb-default-backup-blueprint created
```

Now, we are ready to backup our `MariaDB` databases using few annotations.

**Create Database**

Now, we are going to create an `MariaDB` CR in demo namespace.

Below is the YAML of the `MariaDB` object that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
  annotations:
    blueprint.kubestash.com/name: mariadb-default-backup-blueprint
    blueprint.kubestash.com/namespace: demo
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Here,

* `.spec.annotations.blueprint.kubestash.com/name: mariadb-default-backup-blueprint` specifies the name of the `BackupBlueprint` that will use in backup.
* `.spec.annotations.blueprint.kubestash.com/namespace: demo` specifies the name of the `namespace` where the `BackupBlueprint` resides.

Let’s create the `MariaDB` we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

**Verify BackupConfiguration**

If everything goes well, KubeStash should create a `BackupConfiguration` for our MariaDB in demo namespace and the phase of that `BackupConfiguration` should be `Ready`. Verify the `BackupConfiguration` object by the following command,

```bash
$ kubectl get backupconfiguration -n demo
NAME                         PHASE   PAUSED   AGE
appbinding-sample-mariadb   Ready            2m50m
```

Now, let’s check the YAML of the `BackupConfiguration`.

```bash
$ kubectl get backupconfiguration -n demo appbinding-sample-mariadb  -o yaml
```

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  creationTimestamp: "2024-09-18T05:34:15Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    app.kubernetes.io/managed-by: kubestash.com
    kubestash.com/invoker-name: mariadb-default-backup-blueprint
    kubestash.com/invoker-namespace: demo
  name: appbinding-sample-mariadb
  namespace: demo
  resourceVersion: "1700384"
  uid: 927ac985-e3d2-43a2-9d25-00ba55ce5fc1
spec:
  backends:
    - name: gcs-backend
      retentionPolicy:
        name: demo-retention
        namespace: demo
      storageRef:
        name: gcs-storage
        namespace: demo
  sessions:
    - addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
      name: frequent-backup
      repositories:
        - backend: gcs-backend
          directory: /default-blueprint
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
          name: default-blueprint
      scheduler:
        jobTemplate:
          backoffLimit: 1
          template:
            controller: {}
            metadata: {}
            spec:
              resources: {}
        schedule: '*/5 * * * *'
      sessionHistoryLimit: 3
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
status:
  backends:
    - name: gcs-backend
      ready: true
      retentionPolicy:
        found: true
        ref:
          name: demo-retention
          namespace: demo
      storage:
        phase: Ready
        ref:
          name: gcs-storage
          namespace: demo
  conditions:
    - lastTransitionTime: "2024-09-18T05:34:17Z"
      message: Validation has been passed successfully.
      reason: ResourceValidationPassed
      status: "True"
      type: ValidationPassed
  dependencies:
    - found: true
      kind: Addon
      name: mariadb-addon
  phase: Ready
  repositories:
    - name: default-blueprint
      phase: Ready
  sessions:
    - conditions:
        - lastTransitionTime: "2024-09-18T05:34:17Z"
          message: Scheduler has been ensured successfully.
          reason: SchedulerEnsured
          status: "True"
          type: SchedulerEnsured
        - lastTransitionTime: "2024-09-18T05:34:18Z"
          message: Initial backup has been triggered successfully.
          reason: SuccessfullyTriggeredInitialBackup
          status: "True"
          type: InitialBackupTriggered
      name: frequent-backup
  targetFound: true
```

Notice the `spec.backends`, `spec.sessions` and `spec.target` sections, KubeStash automatically resolved those info from the `BackupBluePrint` and created above `BackupConfiguration`.

**Verify BackupSession:**

KubeStash triggers an instant backup as soon as the `BackupConfiguration` is ready. After that, backups are scheduled according to the specified schedule.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                    INVOKER-TYPE          INVOKER-NAME                 PHASE       DURATION   AGE
appbinding-sample-mariadb-frequent-backup-1726637655    BackupConfiguration   appbinding-sample-mariadb   Succeeded   2m11s      3m15s
```

We can see from the above output that the backup session has succeeded. Now, we are going to verify whether the backup data has been stored in the backend.

**Verify Backup:**

Once a backup is complete, KubeStash will update the respective `Repository` CR to reflect the backup. Check that the repository `sample-mariadb-backup` has been updated by the following command,

```bash
$ kubectl get repository -n demo default-blueprint
NAME                INTEGRITY   SNAPSHOT-COUNT   SIZE        PHASE   LAST-SUCCESSFUL-BACKUP   AGE
default-blueprint   true        3                1.559 KiB   Ready   80s                      7m32s
```

At this moment we have one `Snapshot`. Run the following command to check the respective `Snapshot` which represents the state of a backup run for an application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=default-blueprint
NAME                                                              REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
default-blueprint-appbinding-samiadb-frequent-backup-1726637655   default-blueprint   frequent-backup   2024-09-18T05:34:18Z   Delete            Succeeded   7m39s
```

> Note: KubeStash creates a `Snapshot` with the following labels:
>
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> These labels can be used to watch only the `Snapshot`s related to our target Database or `Repository`.

If we check the YAML of the `Snapshot`, we can find the information about the backup components of the Database.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo default-blueprint-appbinding-samgres-frequent-backup-1725533628 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T05:34:18Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: default-blueprint
  annotations:
    kubedb.com/db-version: 11.1.3
  name: default-blueprint-appbinding-samiadb-frequent-backup-1726637655
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: default-blueprint
      uid: ec1ba99f-ac95-4197-9ddd-0f978053a5d6
  resourceVersion: "1701057"
  uid: fee77218-c06a-43a5-8ad4-fa9baf72a128
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: appbinding-sample-mariadb-frequent-backup-1726637655
  deletionPolicy: Delete
  repository: default-blueprint
  session: frequent-backup
  snapshotID: 01J81SZM8G6AQ5XZAN85CSBP96
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.762583481s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: c4d4c26ad6e03f372b60dfc8bb7901900c4be9b791d44c68564753fb9e9e424c
            size: 2.206 KiB
            uploaded: 2.498 KiB
      size: 2.190 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T05:34:18Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T05:36:26Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 2.189 KiB
  snapshotTime: "2024-09-18T05:34:18Z"
  totalComponents: 1
```

> KubeStash uses `mariadb-dump` to perform backups of target `MariaDB` databases. Therefore, the component name for logical backups is set as `dump`.

Now, if we navigate to the GCS bucket, we will see the backup data stored in the `blueprint/default-blueprint/repository/v1/frequent-backup/dump` directory. KubeStash also keeps the backup for `Snapshot` YAMLs, which can be found in the `blueprint/default-blueprint/snapshots` directory.

> Note: KubeStash stores all dumped data encrypted in the backup directory, meaning it remains unreadable until decrypted.

## Auto-backup with custom configurations

In this section, we are going to backup a `MariaDB` database of `demo` namespace. We are going to use the custom configurations which will be specified in the `BackupBlueprint` CR.

**Prepare Backup Blueprint**

A `BackupBlueprint` allows you to specify a template for the `Repository`,`Session` or `Variables` of `BackupConfiguration` in a Kubernetes native way.

Now, we have to create a `BackupBlueprint` CR with a blueprint for `BackupConfiguration` object.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupBlueprint
metadata:
  name: mariadb-customize-backup-blueprint
  namespace: demo
spec:
  usagePolicy:
    allowedNamespaces:
      from: All
  backupConfigurationTemplate:
    deletionPolicy: OnDelete
    backends:
      - name: gcs-backend
        storageRef:
          namespace: demo
          name: gcs-storage
        retentionPolicy:
          name: demo-retention
          namespace: demo
    sessions:
      - name: frequent-backup
        sessionHistoryLimit: 3
        scheduler:
          schedule: ${schedule}
          jobTemplate:
            backoffLimit: 1
        repositories:
          - name: ${repoName}
            backend: gcs-backend
            directory: ${namespace}/${targetName}
            encryptionSecret:
              name: encrypt-secret
              namespace: demo
        addon:
          name: mariadb-addon
          tasks:
            - name: logical-backup
              params:
                args: ${targetedDatabase}
```

Note that we have used some variables (format: `${<variable name>}`) in different fields. KubeStash will substitute these variables with values from the respective target’s annotations. You’re free to use any variables you like.

Here,

* `.spec.backupConfigurationTemplate.backends[*].storageRef` refers our earlier created `gcs-storage` backupStorage.
* `.spec.backupConfigurationTemplate.sessions[*]`:
  + `.schedule` defines `${schedule}` variable, which determines the time interval for the backup.
  + `.repositories[*].name` defines the `${repoName}` variable, which specifies the name of the backup `Repository`.
  + `.repositories[*].directory` defines two variables, `${namespace}` and `${targetName}`, which are used to determine the path where the backup will be stored.
  + `.addon.tasks[*].params.args` defines `${targetedDatabase}` variable, which identifies a single database to backup.

Let’s create the `BackupBlueprint` we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/customize-backupblueprint.yaml
backupblueprint.core.kubestash.com/mariadb-customize-backup-blueprint created
```

Now, we are ready to backup our `MariaDB` databases using few annotations. You can check available auto-backup annotations for a databases from [here](https://kubestash.com/docs/latest/concepts/crds/backupblueprint/).

**Create Database**

Now, we are going to create an `MariaDB` CR in demo namespace.

Below is the YAML of the `MariaDB` object that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb-2
  namespace: demo
  annotations:
    blueprint.kubestash.com/name: mariadb-customize-backup-blueprint
    blueprint.kubestash.com/namespace: demo
    variables.kubestash.com/schedule: "*/10 * * * *"
    variables.kubestash.com/repoName: customize-blueprint
    variables.kubestash.com/namespace: demo
    variables.kubestash.com/targetName: sample-mariadb-2
    variables.kubestash.com/targetedDatabase: mysql
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Notice the `metadata.annotations` field, where we have defined the annotations related to the automatic backup configuration. Specifically, we’ve set the `BackupBlueprint` name as `mariadb-customize-backup-blueprint` and the namespace as `demo`. We have also provided values for the blueprint template variables, such as the backup `schedule`, `repositoryName`, `namespace`, `targetName`, and `targetedDatabase`. These annotations will be used to create a `BackupConfiguration` for this `MariaDB` database.

Let’s create the `MariaDB` we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/auto-backup/examples/sample-mariadb-2.yaml
mariadb.kubedb.com/sample-mariadb-2 created
```

**Verify BackupConfiguration**

If everything goes well, KubeStash should create a `BackupConfiguration` for our MariaDB in demo namespace and the phase of that `BackupConfiguration` should be `Ready`. Verify the `BackupConfiguration` object by the following command,

```bash
$ kubectl get backupconfiguration -n demo
NAME                           PHASE   PAUSED      AGE
appbinding-sample-mariadb-2    Ready               2m50m
```

Now, let’s check the YAML of the `BackupConfiguration`.

```bash
$ kubectl get backupconfiguration -n demo appbinding-sample-mariadb-2  -o yaml
```

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  creationTimestamp: "2024-09-18T06:23:21Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    app.kubernetes.io/managed-by: kubestash.com
    kubestash.com/invoker-name: mariadb-customize-backup-blueprint
    kubestash.com/invoker-namespace: demo
  name: appbinding-sample-mariadb-2
  namespace: demo
  resourceVersion: "1709334"
  uid: 08ff19bc-ab81-46c1-9e40-32ff3eb02144
spec:
  backends:
    - name: gcs-backend
      retentionPolicy:
        name: demo-retention
        namespace: demo
      storageRef:
        name: gcs-storage
        namespace: demo
  sessions:
    - addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
            params:
              args: mysql
      name: frequent-backup
      repositories:
        - backend: gcs-backend
          directory: demo/sample-mariadb-2
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
          name: customize-blueprint
      scheduler:
        jobTemplate:
          backoffLimit: 1
          template:
            controller: {}
            metadata: {}
            spec:
              resources: {}
        schedule: '*/10 * * * *'
      sessionHistoryLimit: 3
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb-2
    namespace: demo
status:
  backends:
    - name: gcs-backend
      ready: true
      retentionPolicy:
        found: true
        ref:
          name: demo-retention
          namespace: demo
      storage:
        phase: Ready
        ref:
          name: gcs-storage
          namespace: demo
  conditions:
    - lastTransitionTime: "2024-09-18T06:23:21Z"
      message: Validation has been passed successfully.
      reason: ResourceValidationPassed
      status: "True"
      type: ValidationPassed
  dependencies:
    - found: true
      kind: Addon
      name: mariadb-addon
  phase: Ready
  repositories:
    - name: customize-blueprint
      phase: Ready
  sessions:
    - conditions:
        - lastTransitionTime: "2024-09-18T06:23:23Z"
          message: Scheduler has been ensured successfully.
          reason: SchedulerEnsured
          status: "True"
          type: SchedulerEnsured
        - lastTransitionTime: "2024-09-18T06:23:24Z"
          message: Initial backup has been triggered successfully.
          reason: SuccessfullyTriggeredInitialBackup
          status: "True"
          type: InitialBackupTriggered
      name: frequent-backup
  targetFound: true
```

Notice the `spec.backends`, `spec.sessions` and `spec.target` sections, KubeStash automatically resolved those info from the `BackupBluePrint` and created above `BackupConfiguration`.

**Verify BackupSession:**

KubeStash triggers an instant backup as soon as the `BackupConfiguration` is ready. After that, backups are scheduled according to the specified schedule.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                      INVOKER-TYPE          INVOKER-NAME                   PHASE       DURATION   AGE
appbinding-sample-mariadb-2-frequent-backup-1726640601    BackupConfiguration   appbinding-sample-mariadb-2   Succeeded   2m6s       10m
```

We can see from the above output that the backup session has succeeded. Now, we are going to verify whether the backup data has been stored in the backend.

**Verify Backup:**

Once a backup is complete, KubeStash will update the respective `Repository` CR to reflect the backup. Check that the repository `customize-blueprint` has been updated by the following command,

```bash
$ kubectl get repository -n demo customize-blueprint
NAME                         INTEGRITY   SNAPSHOT-COUNT   SIZE    PHASE   LAST-SUCCESSFUL-BACKUP   AGE
customize-blueprint          true        2                1.021 MiB   Ready   4m29s                    11ms
```

At this moment we have one `Snapshot`. Run the following command to check the respective `Snapshot` which represents the state of a backup run for an application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=customize-blueprint
NAME                                                              REPOSITORY            SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
customize-blueprint-appbinding-sdb-2-frequent-backup-1726640601   customize-blueprint   frequent-backup   2024-09-18T06:23:24Z   Delete            Succeeded   12m
```

> Note: KubeStash creates a `Snapshot` with the following labels:
>
> * `kubedb.com/db-version: <db-version>`
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> These labels can be used to watch only the `Snapshot`s related to our target Database or `Repository`.

If we check the YAML of the `Snapshot`, we can find the information about the backup components of the Database.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo customize-blueprint-appbinding-sql-2-frequent-backup-1725597000 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-18T06:23:24Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb-2
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: customize-blueprint
  annotations:
    kubedb.com/db-version: 11.1.3
  name: customize-blueprint-appbinding-sdb-2-frequent-backup-1726640601
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: customize-blueprint
      uid: 224a1fe8-4897-4de6-b933-fc3537c2a881
  resourceVersion: "1709934"
  uid: e28deec8-a7a4-43ba-b314-b95ef2991a85
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb-2
    namespace: demo
  backupSession: appbinding-sample-mariadb-2-frequent-backup-1726640601
  deletionPolicy: Delete
  repository: customize-blueprint
  session: frequent-backup
  snapshotID: 01J81WSH71CCD611AZ5PTC1N6G
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 2.836904485s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 6aa144d43ea5d70fd1018390d4d22f98f6ab568c74eee9a386d6a9b29ad21d8b
            size: 4.887 MiB
            uploaded: 4.887 MiB
      size: 907.341 KiB
  conditions:
    - lastTransitionTime: "2024-09-18T06:23:24Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-18T06:25:27Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 907.341 KiB
  snapshotTime: "2024-09-18T06:23:24Z"
  totalComponents: 1
```

> KubeStash uses `mariadb-dump` to perform backups of target `MariaDB` databases. Therefore, the component name for logical backups is set as `dump`.

Now, if we navigate to the GCS bucket, we will see the backup data stored in the `blueprint/demo/sample-mariadb-2/repository/v1/frequent-backup/dump` directory. KubeStash also keeps the backup for `Snapshot` YAMLs, which can be found in the `blueprint/demo/sample-mariadb-2/snapshots` directory.

> Note: KubeStash stores all dumped data encrypted in the backup directory, meaning it remains unreadable until decrypted.

## Cleanup

To cleanup the resources crated by this tutorial, run the following commands,

```bash
kubectl delete backupblueprints.core.kubestash.com  -n demo mariadb-default-backup-blueprint
kubectl delete backupblueprints.core.kubestash.com  -n demo mariadb-customize-backup-blueprint
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadb -n demo sample-mariadb-2
```

<!-- PAGE_START: backup/kubestash/customization.md -->
# Customizing Backup and Restore Process

KubeStash provides rich customization supports for the backup and restore process to meet the requirements of various cluster configurations. This guide will show you some examples of these customizations.

## Customizing Backup Process

In this section, we are going to show you how to customize the backup process. Here, we are going to show some examples of providing arguments to the backup process, running the backup process as a specific user, etc.

### Passing arguments to the backup process

KubeStash MariaDB addon uses the [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) command by default for backups.
The below example shows how you can pass the `--flush-logs` to flush the MariaDB server log files before starting the dump.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
            params:
              args: --flush-logs
```

### Passing a target database to the backup process

The below example shows how you can pass target database name during backup.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
            params:
              args: --databases testdb
```

> **WARNING**: Make sure that your provided database has been created before taking backup.

### Using multiple backends

You can configure multiple backends within a single `backupConfiguration`. To back up the same data to different backends, such as S3 and GCS, declare each backend in the `.spe.backends` section. Then, reference these backends in the `.spec.sessions[*].repositories` section.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
    - name: s3-backend
      storageRef:
        namespace: demo
        name: s3-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
        - name: s3-mariadb-repo
          backend: s3-backend
          directory: /mariadb-copy
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
```

### Running backup job as a specific user

If your cluster requires running the backup job as a specific user, you can provide `securityContext` under `addon.jobTemplate.spec.securityContext` section. The below example shows how you can run the backup job as the `root` user.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        jobTemplate:
          spec:
            securityContext:
              runAsUser: 0
              runAsGroup: 0
        tasks:
          - name: logical-backup
```

### Specifying Memory/CPU limit/request for the backup job

If you want to specify the Memory/CPU limit/request for your backup job, you can specify `resources` field under `addon.jobTemplate.spec` section.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        jobTemplate:
          spec:
            resources:
              requests:
                cpu: "200m"
                memory: "1Gi"
              limits:
                cpu: "200m"
                memory: "1Gi"
        tasks:
          - name: logical-backup
```

> You can configure additional runtime settings for backup jobs within the `addon.jobTemplate.spec` sections. For further details, please refer to the [reference](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/#podtemplate-spec).

## Customizing Restore Process

`KubeStash` uses [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) during the restore process. In this section, we are going to show how you can pass arguments to the restore process, restore a specific snapshot, run restore job as a specific user, etc.

### Passing arguments to the restore process

Similar to the backup process, you can pass arguments to the restore process through the args params under addon.tasks[\*].params section.

This example will restore data from database testdb only.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
        params:
          args: testdb
```

### Restore specific snapshot

You can also restore a specific snapshot. At first, list the available snapshot as bellow,

```bash
$ kubectl get snapshots.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                    REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725257849   gcs-mariadb-repo   frequent-backup   2024-09-02T06:18:01Z      Delete            Succeeded   15m
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258000   gcs-mariadb-repo   frequent-backup   2024-09-02T06:20:00Z      Delete            Succeeded   13m
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258300   gcs-mariadb-repo   frequent-backup   2024-09-02T06:25:00Z      Delete            Succeeded   8m34s
gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258600   gcs-mariadb-repo   frequent-backup   2024-09-02T06:30:00Z      Delete            Succeeded   3m34s
```

The below example shows how you can pass a specific snapshot name in `.spec.dataSource` section.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: gcs-mariadb-repo-sample-mariadb-backup-frequent-backup-1725258000
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
```

### Running restore job as a specific user

Similar to the backup process under the `addon.jobTemplate.spec.` you can provide `securityContext` to run the restore job as a specific user.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    jobTemplate:
      spec:
        securityContext:
          runAsUser: 0
          runAsGroup: 0
    tasks:
      - name: logical-backup-restore
```

### Specifying Memory/CPU limit/request for the restore job

Similar to the backup process, you can also provide `resources` field under the `addon.jobTemplate.spec.resources` section to limit the Memory/CPU for your restore job.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    jobTemplate:
      spec:
        resources:
          requests:
            cpu: "200m"
            memory: "1Gi"
          limits:
            cpu: "200m"
            memory: "1Gi"
    tasks:
      - name: logical-backup-restore
```

> You can configure additional runtime settings for restore jobs within the `addon.jobTemplate.spec` sections. For further details, please refer to the [reference](https://kubestash.com/docs/latest/concepts/crds/restoresession/#podtemplate-spec).

<!-- PAGE_START: backup/kubestash/logical.md -->
# Backup and Restore MariaDB database using KubeStash

KubeStash allows you to backup and restore `MariaDB` databases. It supports backups for `MariaDB` instances running in Standalone, and Galera cluster configurations. KubeStash makes managing your `MariaDB` backups and restorations more straightforward and efficient.

This guide will give you an overview how you can take backup and restore your `MariaDB` databases using `Kubestash`.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using `Minikube` or `Kind`.
* Install `KubeDB` in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* Install `KubeStash` in your cluster following the steps [here](https://kubestash.com/docs/latest/setup/install/kubestash).
* Install KubeStash `kubectl` plugin following the steps [here](https://kubestash.com/docs/latest/setup/install/kubectl-plugin/).
* If you are not familiar with how KubeStash backup and restore MariaDB databases, please check the following guide [here](en/backup/kubestash/overview.md).

You should be familiar with the following `KubeStash` concepts:

* [BackupStorage](https://kubestash.com/docs/latest/concepts/crds/backupstorage/)
* [BackupConfiguration](https://kubestash.com/docs/latest/concepts/crds/backupconfiguration/)
* [BackupSession](https://kubestash.com/docs/latest/concepts/crds/backupsession/)
* [RestoreSession](https://kubestash.com/docs/latest/concepts/crds/restoresession/)
* [Addon](https://kubestash.com/docs/latest/concepts/crds/addon/)
* [Function](https://kubestash.com/docs/latest/concepts/crds/function/)
* [Task](https://kubestash.com/docs/latest/concepts/crds/addon/#task-specification)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

> **Note:** YAML files used in this tutorial are stored in [docs/guides/mariadb/backup/kubestash/logical/examples](https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples) directory of [kubedb/docs](https://github.com/kubedb/docs) repository.

## Backup MariaDB

KubeStash supports backups for `MariaDB` instances across different configurations, including Standalone and Galera Cluster setups. In this demonstration, we’ll focus on a `MariaDB` database using Galera cluster configuration. The backup and restore process is similar for Standalone configuration.

This section will demonstrate how to backup a `MariaDB` database. Here, we are going to deploy a `MariaDB` database using KubeDB. Then, we are going to backup this database into a `GCS` bucket. Finally, we are going to restore the backup up data into another `MariaDB` database.

### Deploy Sample MariaDB Database

Let’s deploy a sample `MariaDB` database and insert some data into it.

**Create MariaDB CR:**

Below is the YAML of a sample `MariaDB` CR that we are going to create for this tutorial:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Create the above `MariaDB` CR,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

KubeDB will deploy a `MariaDB` database according to the above specification. It will also create the necessary `Secrets` and `Services` to access the database.

Let’s check if the database is ready to use,

```bash
$ kubectl get md -n demo sample-mariadb
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/sample-mariadb   11.1.3    Ready    5m4s
```

The database is `Ready`. Verify that KubeDB has created a `Secret` and a `Service` for this database using the following commands,

```bash
$ kubectl get secret -n demo 
NAME                          TYPE                       DATA   AGE
sample-mariadb-auth           kubernetes.io/basic-auth   2      5m49s

$ kubectl get service -n demo -l=app.kubernetes.io/instance=sample-mariadb
NAME                      TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
sample-mariadb            ClusterIP   10.128.7.155   <none>        3306/TCP                     6m28s
sample-mariadb-pods       ClusterIP   None           <none>        3306/TCP                     6m28s
```

Here, we have to use service `sample-mariadb` and secret `sample-mariadb-auth` to connect with the database. `KubeDB` creates an [AppBinding](en/concepts/appbinding.md) CR that holds the necessary information to connect with the database.

**Verify AppBinding:**

Verify that the `AppBinding` has been created successfully using the following command,

```bash
$ kubectl get appbindings -n demo
NAME                       TYPE                  VERSION   AGE
sample-mariadb             kubedb.com/mariadb    11.1.3    7m56s
```

Let’s check the YAML of the above `AppBinding`,

```bash
$ kubectl get appbindings -n demo sample-mariadb -o yaml
```

```yaml
apiVersion: appcatalog.appscode.com/v1alpha1
kind: AppBinding
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"kubedb.com/v1","kind":"MariaDB","metadata":{"annotations":{},"name":"sample-mariadb","namespace":"demo"},"spec":{"deletionPolicy":"WipeOut","replicas":3,"storage":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"1Gi"}}},"storageType":"Durable","version":"11.1.3"}}      
  creationTimestamp: "2024-09-17T10:07:37Z"
  generation: 1
  labels:
    app.kubernetes.io/component: database
    app.kubernetes.io/instance: sample-mariadb
    app.kubernetes.io/managed-by: kubedb.com
    app.kubernetes.io/name: mariadbs.kubedb.com
  name: sample-mariadb
  namespace: demo
  ownerReferences:
    - apiVersion: kubedb.com/v1
      blockOwnerDeletion: true
      controller: true
      kind: MariaDB
      name: sample-mariadb
      uid: c19117ca-582b-4d6c-90e5-ac80d5cf95b9
  resourceVersion: "1561857"
  uid: fd3868ef-f54b-4cc9-87b0-4986d9a8aaf0
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  clientConfig:
    service:
      name: sample-mariadb
      port: 3306
      scheme: tcp
    url: tcp(sample-mariadb.demo.svc:3306)/
  parameters:
    address: gcomm://sample-mariadb-0.sample-mariadb-pods.demo,sample-mariadb-1.sample-mariadb-pods.demo,sample-mariadb-2.sample-mariadb-pods.demo
    apiVersion: config.kubedb.com/v1alpha1
    group: sample-mariadb
    kind: GaleraArbitratorConfiguration
    sstMethod: xtrabackup-v2
    stash:
      addon:
        backupTask:
          name: mariadb-backup-10.5.8
        restoreTask:
          name: mariadb-restore-10.5.8
  secret:
    name: sample-mariadb-auth
  type: kubedb.com/mariadb
  version: 12.1.2
```

KubeStash uses the `AppBinding` CR to connect with the target database. It requires the following two fields to set in AppBinding’s `.spec` section.

Here,

* `.spec.clientConfig.service.name` specifies the name of the Service that connects to the database.
* `.spec.secret` specifies the name of the Secret that holds necessary credentials to access the database.
* `.spec.type` specifies the types of the app that this AppBinding is pointing to. KubeDB generated AppBinding follows the following format: `<app group>/<app resource type>`.

**Insert Sample Data:**

Now, we are going to exec into one of the database pod and create some sample data. At first, find out the database `Pod` using the following command,

```bash
$ kubectl get pods -n demo --selector="app.kubernetes.io/instance=sample-mariadb" 
NAME                READY   STATUS    RESTARTS   AGE
sample-mariadb-0    2/2     Running   0          10m
sample-mariadb-1    2/2     Running   0          10m
sample-mariadb-2    2/2     Running   0          10m
```

Now, let’s exec into the pod and create a table,

```bash
$ kubectl exec -it -n demo  mariadb-0 -- bash
```

```mysql
bash-4.4$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> create database hello;

MariaDB> use hello;

MariaDB [hello]> CREATE TABLE `demo_table`(
    ->     `id` BIGINT(20) NOT NULL,
    ->     `name` VARCHAR(255) DEFAULT NULL,
    ->     PRIMARY KEY (`id`)
    -> );

MariaDB [hello]> INSERT INTO `demo_table` (`id`, `name`)
    -> VALUES
    ->     (1, 'John'),
    ->     (2, 'Jane'),
    ->     (3, 'Bob'),
    ->     (4, 'Alice'),
    ->     (5, 'Charlie'),
    ->     (6, 'Diana'),
    ->     (7, 'Eve'),
    ->     (8, 'Frank'),
    ->     (9, 'Grace'),
    ->     (10, 'Henry');
    
MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

Now, we are ready to backup the database.

### Prepare Backend

We are going to store our backup data into a `GCS` bucket. We have to create a `Secret` with necessary credentials and a `BackupStorage` CR to use this backend. If you want to use a different backend, please read the respective backend configuration doc from [here](https://kubestash.com/docs/latest/guides/backends/overview/).

**Create Secret:**

Let’s create a secret called `gcs-secret` with access credentials to our desired GCS bucket,

```bash
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat /path/to/downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Create BackupStorage:**

Now, create a `BackupStorage` using this secret. Below is the YAML of `BackupStorage` CR we are going to create,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: BackupStorage
metadata:
  name: gcs-storage
  namespace: demo
spec:
  storage:
    provider: gcs
    gcs:
      bucket: kubestash-qa
      prefix: demo
      secretName: gcs-secret
  usagePolicy:
    allowedNamespaces:
      from: All
  default: true
  deletionPolicy: Delete
```

Let’s create the BackupStorage we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/backupstorage.yaml
backupstorage.storage.kubestash.com/gcs-storage created
```

Now, we are ready to backup our database to our desired backend.

**Create RetentionPolicy:**

Now, let’s create a `RetentionPolicy` to specify how the old Snapshots should be cleaned up.

Below is the YAML of the `RetentionPolicy` object that we are going to create,

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: RetentionPolicy
metadata:
  name: demo-retention
  namespace: demo
spec:
  default: true
  failedSnapshots:
    last: 2
  maxRetentionPeriod: 2mo
  successfulSnapshots:
    last: 5
  usagePolicy:
    allowedNamespaces:
      from: All
```

Let’s create the above `RetentionPolicy`,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/retentionpolicy.yaml
retentionpolicy.storage.kubestash.com/demo-retention created
```

### Backup

We have to create a `BackupConfiguration` targeting respective `sample-mariadb` MariaDB database. Then, KubeStash will create a `CronJob` for each session to take periodic backup of that database.

At first, we need to create a secret with a Restic password for backup data encryption.

**Create Secret:**

Let’s create a secret called `encrypt-secret` with the Restic password,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ kubectl create secret generic -n demo encrypt-secret \
    --from-file=./RESTIC_PASSWORD \
secret "encrypt-secret" created
```

Below is the YAML for `BackupConfiguration` CR to backup the `sample-mariadb` database that we have deployed earlier,

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: sample-mariadb
  backends:
    - name: gcs-backend
      storageRef:
        namespace: demo
        name: gcs-storage
      retentionPolicy:
        name: demo-retention
        namespace: demo
  sessions:
    - name: frequent-backup
      scheduler:
        schedule: "*/5 * * * *"
        jobTemplate:
          backoffLimit: 1
      repositories:
        - name: gcs-mariadb-repo
          backend: gcs-backend
          directory: /mariadb
          encryptionSecret:
            name: encrypt-secret
            namespace: demo
      addon:
        name: mariadb-addon
        tasks:
          - name: logical-backup
```

* `.spec.sessions[*].schedule` specifies that we want to backup the database at `5 minutes` interval.
* `.spec.target` refers to the targeted `sample-mariadb` MariaDB database that we created earlier.

Let’s create the `BackupConfiguration` CR that we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/backupconfiguration.yaml
backupconfiguration.core.kubestash.com/sample-mariadb-backup created
```

**Verify Backup Setup Successful**

If everything goes well, the phase of the `BackupConfiguration` should be `Ready`. The `Ready` phase indicates that the backup setup is successful. Let’s verify the `Phase` of the BackupConfiguration,

```bash
$ kubectl get backupconfiguration -n demo
NAME                     PHASE   PAUSED   AGE
sample-mariadb-backup    Ready            2m50s
```

Additionally, we can verify that the `Repository` specified in the `BackupConfiguration` has been created using the following command,

```bash
$ kubectl get repo -n demo
NAME                  INTEGRITY   SNAPSHOT-COUNT   SIZE        PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo      true        1                1.096 KiB   Ready   3m3s                     3m13s
```

KubeStash keeps the backup for `Repository` YAMLs. If we navigate to the GCS bucket, we will see the `Repository` YAML stored in the `demo/mariadb` directory.

**Verify CronJob:**

It will also create a `CronJob` with the schedule specified in `spec.sessions[*].scheduler.schedule` field of `BackupConfiguration` CR.

Verify that the `CronJob` has been created using the following command,

```bash
$ kubectl get cronjob -n demo
NAME                                             SCHEDULE     TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
trigger-sample-mariadb-backup-frequent-backup   */5 * * * *   <none>     False     0        <none>          4m23s
```

**Verify BackupSession:**

KubeStash triggers an instant backup as soon as the `BackupConfiguration` is ready. After that, backups are scheduled according to the specified schedule.

```bash
$ kubectl get backupsession -n demo -w
NAME                                                INVOKER-TYPE          INVOKER-NAME              PHASE       DURATION   AGE
sample-mariadb-backup-frequent-backup-1725449400    BackupConfiguration   sample-mariadb-backup     Succeeded              7m22s
```

We can see from the above output that the backup session has succeeded. Now, we are going to verify whether the backup data has been stored in the backend.

**Verify Backup:**

Once a backup is complete, KubeStash will update the respective `Repository` CR to reflect the backup. Check that the repository `sample-mariadb-backup` has been updated by the following command,

```bash
$ kubectl get repository -n demo gcs-mariadb-repo
NAME                       INTEGRITY   SNAPSHOT-COUNT   SIZE    PHASE   LAST-SUCCESSFUL-BACKUP   AGE
gcs-mariadb-repo           true        1                806 B   Ready   8m27s                    9m18s
```

At this moment we have one `Snapshot`. Run the following command to check the respective `Snapshot` which represents the state of a backup run for an application.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo -l=kubestash.com/repo-name=gcs-mariadb-repo
NAME                                                                  REPOSITORY          SESSION           SNAPSHOT-TIME          DELETION-POLICY   PHASE       AGE
gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726569774       gcs-mariadb-repo    frequent-backup   2024-09-17T10:43:04Z   Delete            Succeeded   41m
```

> Note: KubeStash creates a `Snapshot` with the following labels:
>
> * `kubestash.com/app-ref-kind: <target-kind>`
> * `kubestash.com/app-ref-name: <target-name>`
> * `kubestash.com/app-ref-namespace: <target-namespace>`
> * `kubestash.com/repo-name: <repository-name>`
>
> These labels can be used to watch only the `Snapshot`s related to our target Database or `Repository`.

If we check the YAML of the `Snapshot`, we can find the information about the backup components of the Database.

```bash
$ kubectl get snapshot.storage.kubestash.com -n demo gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726569774 -oyaml
```

```yaml
apiVersion: storage.kubestash.com/v1alpha1
kind: Snapshot
metadata:
  creationTimestamp: "2024-09-17T10:43:04Z"
  finalizers:
    - kubestash.com/cleanup
  generation: 1
  labels:
    kubestash.com/app-ref-kind: MariaDB
    kubestash.com/app-ref-name: sample-mariadb
    kubestash.com/app-ref-namespace: demo
    kubestash.com/repo-name: gcs-mariadb-repo
  annotations:
    kubedb.com/db-version: 11.1.3
  name: gcs-mariadb-repo-sample-mariadb-ckup-frequent-backup-1726569774
  namespace: demo
  ownerReferences:
    - apiVersion: storage.kubestash.com/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: Repository
      name: gcs-mariadb-repo
      uid: 7abe82a2-5ecc-4904-b848-910becab54bc
  resourceVersion: "1566893"
  uid: a18e95f2-d7ec-4334-9ba4-f689280a51ab
spec:
  appRef:
    apiGroup: kubedb.com
    kind: MariaDB
    name: sample-mariadb
    namespace: demo
  backupSession: sample-mariadb-backup-frequent-backup-1726569774
  deletionPolicy: Delete
  repository: gcs-mariadb-repo
  session: frequent-backup
  snapshotID: 01J7ZS88VNPD5B7HFVXVP576P6
  type: FullBackup
  version: v1
status:
  components:
    dump:
      driver: Restic
      duration: 3.279948033s
      integrity: true
      path: repository/v1/frequent-backup/dump
      phase: Succeeded
      resticStats:
        - summary:
            hostPath: dumpfile.sql
            id: 0a6dfb754cb32bdaf17581fa42b20e8915aabd0b48f37c854b72812f53b7e5b6
            size: 2.206 KiB
            uploaded: 2.498 KiB
      size: 1.096 KiB
  conditions:
    - lastTransitionTime: "2024-09-17T10:43:04Z"
      message: Recent snapshot list updated successfully
      reason: SuccessfullyUpdatedRecentSnapshotList
      status: "True"
      type: RecentSnapshotListUpdated
    - lastTransitionTime: "2024-09-17T10:43:24Z"
      message: Metadata uploaded to backend successfully
      reason: SuccessfullyUploadedSnapshotMetadata
      status: "True"
      type: SnapshotMetadataUploaded
  integrity: true
  phase: Succeeded
  size: 1.096 KiB
  snapshotTime: "2024-09-17T10:43:04Z"
  totalComponents: 1
```

> KubeStash uses `mariadb-dump` to perform backups of target `MariaDB` databases. Therefore, the component name for logical backups is set as `dump`.

Now, if we navigate to the GCS bucket, we will see the backup data stored in the `demo/mariadb/repository/v1/frequent-backup/dump` directory. KubeStash also keeps the backup for `Snapshot` YAMLs, which can be found in the `demo/mariadb/snapshots` directory.

> Note: KubeStash stores all dumped data encrypted in the backup directory, meaning it remains unreadable until decrypted.

## Restore

In this section, we are going to restore the database from the backup we have taken in the previous section. We are going to deploy a new database and initialize it from the backup.

Now, we have to deploy the restored database similarly as we have deployed the original `sample-mariadb` database. However, this time there will be the following differences:

* We are going to specify `.spec.init.waitForInitialRestore` field that tells KubeDB to wait for first restore to complete before marking this database is ready to use.

Below is the YAML for `MariaDB` CR we are going deploy to initialize from backup,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: restored-mariadb
  namespace: demo
spec:
  init:
    waitForInitialRestore: true
  version: 12.1.2
  replicas: 3
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Let’s create the above database,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/restored-mariadb.yaml
mariadb.kubedb.com/restored-mariadb created
```

If you check the database status, you will see it is stuck in **`Provisioning`** state.

```bash
$ kubectl get mariadb -n demo restored-mariadb
NAME                VERSION   STATUS         AGE
restored-mariadb    11.1.3    Provisioning   110s
```

#### Create RestoreSession:

Now, we need to create a `RestoreSession` CR pointing to targeted `MariaDB` database.

Below, is the contents of YAML file of the `RestoreSession` object that we are going to create to restore backup data into the newly created `MariaDB` database named `restored-mariadb`.

```yaml
apiVersion: core.kubestash.com/v1alpha1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  target:
    apiGroup: kubedb.com
    kind: MariaDB
    namespace: demo
    name: restored-mariadb
  dataSource:
    repository: gcs-mariadb-repo
    snapshot: latest
    encryptionSecret:
      name: encrypt-secret
      namespace: demo
  addon:
    name: mariadb-addon
    tasks:
      - name: logical-backup-restore
```

Here,

* `.spec.target` refers to the newly created `restored-mariadb` MariaDB object to where we want to restore backup data.
* `.spec.dataSource.repository` specifies the Repository object that holds the backup data.
* `.spec.dataSource.snapshot` specifies to restore from latest `Snapshot`.

Let’s create the RestoreSession CRD object we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/kubestash/logical/examples/restoresession.yaml
restoresession.core.kubestash.com/sample-mariadb-restore created
```

Once, you have created the `RestoreSession` object, KubeStash will create restore Job. Run the following command to watch the phase of the `RestoreSession` object,

```bash
$ watch kubectl get restoresession -n demo
NAME                      REPOSITORY          FAILURE-POLICY   PHASE       DURATION   AGE
sample-mariadb-restore   gcs-mariadb-repo                    Succeeded   7s         116s
```

The `Succeeded` phase means that the restore process has been completed successfully.

#### Verify Restored Data:

In this section, we are going to verify whether the desired data has been restored successfully. We are going to connect to the database server and check whether the database and the table we created earlier in the original database are restored.

At first, check if the database has gone into **`Ready`** state by the following command,

```bash
$ kubectl get mariadb -n demo restored-mariadb
NAME                VERSION   STATUS   AGE
restored-mariadb    11.1.3    Ready    6m
```

Now, find out the database `Pod` by the following command,

```bash
$ kubectl get pods -n demo --selector="app.kubernetes.io/instance=restored-mariadb"
NAME                            READY   STATUS      RESTARTS   AGE
restored-mariadb-0              2/2     Running     0          7m
restored-mariadb-1              2/2     Running     0          7m
restored-mariadb-2              2/2     Running     0          7m
```

Now, lets exec one of the `Pod` and verify restored data.

```bash
$ kubectl exec -it -n demo restored-mariadb-0 -- bash
```

```mysql
mysql@restored-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD

MariaDB> use hello;

MariaDB [hello]> select count(*) from demo_table;
+----------+
| count(*) |
+----------+
|       10 |
+----------+
```

So, from the above output, we can see the `hello` database we had created in the original database `sample-mariadb` has been restored in the `restored-mariadb` database.

## Cleanup

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete backupconfigurations.core.kubestash.com  -n demo sample-mariadb-backup
kubectl delete restoresessions.core.kubestash.com -n demo restore-sample-mariadb
kubectl delete retentionpolicies.storage.kubestash.com -n demo demo-retention
kubectl delete backupstorage -n demo gcs-storage
kubectl delete secret -n demo gcs-secret
kubectl delete secret -n demo encrypt-secret
kubectl delete mariadb -n demo restored-mariadb
kubectl delete mariadb -n demo sample-mariadb
```

<!-- PAGE_START: backup/kubestash/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

Please install [KubeStash](https://kubestash.com/docs/latest/setup/install/kubestash/) to try this feature. Database backup with KubeStash is already included in the KubeDB license. So, you don’t need a separate license for KubeStash.

# MariaDB Backup & Restore Overview

KubeDB also uses [KubeStash](https://kubestash.com) to backup and restore databases. KubeStash by AppsCode is a cloud native data backup and recovery solution for Kubernetes workloads and databases. KubeStash utilizes [restic](https://github.com/restic/restic) to securely backup stateful applications to any cloud or on-prem storage backends (for example, S3, GCS, Azure Blob storage, Minio, NetApp, Dell EMC etc.).

  ![KubeDB + KubeStash](images/backup_kubestash_overview_kubedb_plus_kubestash.svg)

Fig: Backup KubeDB Databases Using KubeStash

## How Backup Works

```mermaid
flowchart LR
  User["Operator Applies BackupConfiguration"] --> KS["KubeStash Controller"]
  KS --> Repo["Repository + BackupStorage + Secret"]
  KS --> Cron["CronJob -> BackupSession -> Snapshot"]
  Cron --> Job["Backup Job"]
  AppBind["AppBinding (Host, Port, Auth Secret)"] --> Job
  MariaDB["MariaDB Pod"] -->|Dump / Volume Stream| Job
  Job -->|Restic Encrypted Upload| Backend["Cloud or On-Prem Storage"]
```


The following diagram shows how KubeStash takes backup of a `MariaDB` database. Open the image in a new tab to see the enlarged version.

  ![MariaDB Backup Overview](images/backup_kubestash_overview_backup_overview.svg)

Fig: MariaDB Backup Overview

The backup process consists of the following steps:

1. At first, a user creates a `Secret`. This secret holds the credentials to access the backend where the backed up data will be stored.
2. Then, she creates a `BackupStorage` custom resource that specifies the backend information, along with the `Secret` containing the credentials needed to access the backend.
3. KubeStash operator watches for `BackupStorage` custom resources. When it finds a `BackupStorage` object, it initializes the `BackupStorage` by uploading the `metadata.yaml` file to the specified backend.
4. Next, she creates a `BackupConfiguration` custom resource that specifies the target database, addon information (including backup tasks), backup schedules, storage backends for storing the backup data, and other additional settings.
5. KubeStash operator watches for `BackupConfiguration` objects.
6. Once the KubeStash operator finds a `BackupConfiguration` object, it creates `Repository` with the information specified in the `BackupConfiguration`.
7. KubeStash operator watches for `Repository` custom resources. When it finds the `Repository` object, it Initializes `Repository` by uploading `repository.yaml` file into the `spec.sessions[*].repositories[*].directory` path specified in `BackupConfiguration`.
8. Then, it creates a `CronJob` for each session with the schedule specified in `BackupConfiguration` to trigger backup periodically.
9. KubeStash operator triggers an instant backup as soon as the `BackupConfiguration` is ready. Backups are otherwise triggered by the `CronJob` based on the specified schedule.
10. KubeStash operator watches for `BackupSession` custom resources.
11. When it finds a `BackupSession` object, it creates a `Snapshot` custom resource for each `Repository` specified in the `BackupConfiguration`.
12. Then it resolves the respective `Addon` and `Function` and prepares backup `Job` definition.
13. Then, it creates the `Job` to backup the targeted `MariaDB` database.
14. The backup `Job` reads necessary information (e.g. auth secret, port) to connect with the database from the `AppBinding` CR. It also reads backend information and access credentials from `BackupStorage` CR, Storage Secret and `Repository` path respectively.
15. Then, the `Job` dumps the targeted `MariaDB` database and uploads the output to the backend. KubeStash pipes the output of dump command to uploading process. Hence, backup `Job` does not require a large volume to hold the entire dump output.
16. After the backup process is completed, the backup `Job` updates the `status.components[dump]` field of the `Snapshot` resources with backup information of the target `MariaDB` database.

## How Restore Process Works

The following diagram shows how KubeStash restores backed up data into a `MariaDB` database. Open the image in a new tab to see the enlarged version.

  ![Database Restore Overview](images/backup_kubestash_overview_restore_overview.svg)

Fig: MariaDB Restore Process Overview

The restore process consists of the following steps:

1. At first, a user creates a `MariaDB` database where the data will be restored or the user can use the same `MariaDB` database.
2. Then, she creates a `RestoreSession` custom resource that specifies the target database where the backed-up data will be restored, addon information (including restore tasks), the target snapshot to be restored, the Repository containing that snapshot, and other additional settings.
3. KubeStash operator watches for `RestoreSession` custom resources.
4. When it finds a `RestoreSession` custom resource, it resolves the respective `Addon` and `Function` and prepares a restore `Job` definition.
5. Then, it creates the `Job` to restore the target.
6. The `Job` reads necessary information to connect with the database from respective `AppBinding` CR. It also reads backend information and access credentials from `Repository` CR and storage `Secret` respectively.
7. Then, the `Job` downloads the backed up data from the backend and injects into the desired database. KubeStash pipes the downloaded data to the respective database tool to inject into the database. Hence, restore `Job` does not require a large volume to download entire backup data inside it.
8. Finally, when the restore process is completed, the `Job` updates the `status.components[*]` field of the `RestoreSession` with restore information of the target database.

## Next Steps

* Backup a `MariaDB` database using KubeStash by the following guides from [here](en/backup/kubestash/logical.md).

<!-- PAGE_START: backup/stash/auto-backup.md -->
# Backup MariaDB using Stash Auto-Backup

Stash can be configured to automatically backup any MariaDB database in your cluster. Stash enables cluster administrators to deploy backup blueprints ahead of time so that the database owners can easily backup their database with just a few annotations.

In this tutorial, we are going to show how you can configure a backup blueprint for MariaDB databases in your cluster and backup them with few annotations.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install Stash in your cluster following the steps [here](https://stash.run/docs/latest/setup/install/stash/).
* Install KubeDB in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* If you are not familiar with how Stash backup and restore MariaDB databases, please check the following guide [here](en/backup/stash/overview.md).
* If you are not familiar with how auto-backup works in Stash, please check the following guide [here](https://stash.run/docs/latest/guides/auto-backup/overview/).
* If you are not familiar with the available auto-backup options for databases in Stash, please check the following guide [here](https://stash.run/docs/latest/guides/auto-backup/database/).

You should be familiar with the following `Stash` concepts:

* [BackupBlueprint](https://stash.run/docs/latest/concepts/crds/backupblueprint/)
* [BackupConfiguration](https://stash.run/docs/latest/concepts/crds/backupconfiguration/)
* [BackupSession](https://stash.run/docs/latest/concepts/crds/backupsession/)
* [Repository](https://stash.run/docs/latest/concepts/crds/repository/)
* [Function](https://stash.run/docs/latest/concepts/crds/function/)
* [Task](https://stash.run/docs/latest/concepts/crds/task/)

In this tutorial, we are going to show backup of three different MariaDB databases on three different namespaces named `demo`, `demo-2`, and `demo-3`. Create the namespaces as below if you haven’t done it already.

```bash
❯ kubectl create ns demo
namespace/demo created

❯ kubectl create ns demo-2
namespace/demo-2 created

❯ kubectl create ns demo-3
namespace/demo-3 created
```

When you install the Stash, it automatically installs all the official database addons. Verify that it has installed the MariaDB addons using the following command.

```bash
❯ kubectl get tasks.stash.appscode.com | grep mariadb
mariadb-backup-11.8.5    62m
mariadb-restore-11.8.5   62m
```

## Prepare Backup Blueprint

To backup an MariaDB database using Stash, you have to create a `` containing the backend credentials, a `Repository` containing the backend information, and a `BackupConfiguration` containing the schedule and target information. A `BackupBlueprint` allows you to specify a template for the `Repository` and the `BackupConfiguration`.

The `BackupBlueprint` is a non-namespaced CRD. So, once you have created a `BackupBlueprint`, you can use it to backup any MariaDB database of any namespace just by creating the storage `` in that namespace and adding few annotations to your MariaDB CRO. Then, Stash will automatically create a `Repository` and a `BackupConfiguration` according to the template to backup the database.

Below is the `BackupBlueprint` object that we are going to use in this tutorial,

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupBlueprint
metadata:
  name: mariadb-backup-template
spec:
  # ============== Blueprint for Repository ==========================
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/${TARGET_NAMESPACE}/${TARGET_APP_RESOURCE}/${TARGET_NAME}
  # ============== Blueprint for BackupConfiguration =================
  schedule: "*/5 * * * *"
  retentionPolicy:
    name: 'keep-last-5'
    keepLast: 5
    prune: true
```

Here, we are using a GCS bucket as our backend. We are providing `gcs-` at the `storageName` field. Hence, we have to create a named `gcs-` with the access credentials of our bucket in every namespace where we want to enable backup through this blueprint.

Notice the `prefix` field of `backend` section. We have used some variables in form of `${VARIABLE_NAME}`. Stash will automatically resolve those variables from the database information to make the backend prefix unique for each database instance.

Let’s create the `BackupBlueprint` we have shown above,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/backupblueprint.yaml
backupblueprint.stash.appscode.com/mariadb-backup-template created
```

Now, we are ready to backup our MariaDB databases using few annotations. You can check available auto-backup annotations for a databases from [here](https://stash.run/docs/latest/guides/auto-backup/database/#available-auto-backup-annotations-for-database).

## Auto-backup with default configurations

In this section, we are going to backup an MariaDB database of `demo` namespace. We are going to use the default configurations specified in the `BackupBlueprint`.

### Create Storage

At first, let’s create the `gcs-` in `demo` namespace with the access credentials to our GCS bucket.

```bash
❯ echo -n 'changeit' > RESTIC_PASSWORD
❯ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
❯ cat downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
❯ kubectl create  generic -n demo gcs- \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
/gcs- created
```

### Create Database

Now, we are going to create an MariaDB CRO in `demo` namespace. Below is the YAML of the MariaDB object that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
  annotations:
    stash.appscode.com/backup-blueprint: mariadb-backup-template
spec:
  version: "12.1.2"
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

Notice the `annotations` section. We are pointing to the `BackupBlueprint` that we have created earlier though `stash.appscode.com/backup-blueprint` annotation. Stash will watch this annotation and create a `Repository` and a `BackupConfiguration` according to the `BackupBlueprint`.

Let’s create the above MariaDB CRO,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

### Verify Auto-backup configured

In this section, we are going to verify whether Stash has created the respective `Repository` and `BackupConfiguration` for our MariaDB database we have just deployed or not.

#### Verify Repository

At first, let’s verify whether Stash has created a `Repository` for our MariaDB or not.

```bash
❯ kubectl get repository -n demo
NAME                 INTEGRITY   SIZE   SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
app-sample-mariadb                                                                10s
```

Now, let’s check the YAML of the `Repository`.

```bash
❯ kubectl get repository -n demo app-sample-mariadb -o yaml
```

```text
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
...  
  name: app-sample-mariadb
  namespace: demo
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/demo/mariadb/sample-mariadb
    storageName: gcs-
```

Here, you can see that Stash has resolved the variables in `prefix` field and substituted them with the equivalent information from this database.

#### Verify BackupConfiguration

If everything goes well, Stash should create a `BackupConfiguration` for our MariaDB in `demo` namespace and the phase of that `BackupConfiguration` should be `Ready`. Verify the `BackupConfiguration` crd by the following command,

```bash
❯ kubectl get backupconfiguration -n demo
NAME                 TASK                    SCHEDULE      PAUSED   PHASE   AGE
app-sample-mariadb   mariadb-backup-11.8.5   */5 * * * *            Ready   7m28s
```

Now, let’s check the YAML of the `BackupConfiguration`.

```bash
❯ kubectl get backupconfiguration -n demo app-sample-mariadb -o yaml
```

```text
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: app-sample-mariadb
  namespace: demo
  ...
  spec:
  driver: Restic
  repository:
    name: app-sample-mariadb
  retentionPolicy:
    keepLast: 5
    name: keep-last-5
    prune: true
  runtimeSettings: {}
  schedule: '*/5 * * * *'
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  tempDir: {}
status:
  conditions:
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Repository demo/app-sample-mariadb exist.
    reason: RepositoryAvailable
    status: "True"
    type: RepositoryFound
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Backend  demo/gcs- exist.
    reason: BackendAvailable
    status: "True"
    type: BackendFound
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Backup target appcatalog.appscode.com/v1alpha1 appbinding/sample-mariadb
      found.
    reason: TargetAvailable
    status: "True"
    type: BackupTargetFound
  - lastTransitionTime: "2021-02-25T05:14:51Z"
    message: Successfully created backup triggering CronJob.
    reason: CronJobCreationSucceeded
    status: "True"
    type: CronJobCreated
  observedGeneration: 1
```

Notice the `target` section. Stash has automatically added the MariaDB as the target of this `BackupConfiguration`.

#### Verify Backup

Now, let’s wait for a backup run to complete. You can watch for `BackupSession` as below,

```bash
❯ kubectl get backupsession -n demo -w
NAME                            INVOKER-TYPE          INVOKER-NAME         PHASE       AGE
app-sample-mariadb-1614230401   BackupConfiguration   app-sample-mariadb   Succeeded   5m40s
app-sample-mariadb-1614230701   BackupConfiguration   app-sample-mariadb   Running     39s
```

Once the backup has been completed successfully, you should see the backed up data has been stored in the bucket at the directory pointed by the `prefix` field of the `Repository`.

![Backup data in GCS Bucket](images/backup_stash_auto-backup_sample-mariadb.png)

Fig: Backup data in GCS Bucket

## Auto-backup with a custom schedule

In this section, we are going to backup an MariaDB database of `demo-2` namespace. This time, we are going to overwrite the default schedule used in the `BackupBlueprint`.

### Create Storage

At first, let’s create the `gcs-` in `demo-2` namespace with the access credentials to our GCS bucket.

```bash
❯ kubectl create  generic -n demo-2 gcs- \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
/gcs- created
```

### Create Database

Now, we are going to create an MariaDB CRO in `demo-2` namespace. Below is the YAML of the MariaDB object that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb-2
  namespace: demo-2
  annotations:
    stash.appscode.com/backup-blueprint: mariadb-backup-template
    stash.appscode.com/schedule: "*/3 * * * *"
spec:
  version: "12.1.2"
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

Notice the `annotations` section. This time, we have passed a schedule via `stash.appscode.com/schedule` annotation along with the `stash.appscode.com/backup-blueprint` annotation.

Let’s create the above MariaDB CRO,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/sample-mariadb-2.yaml
mariadb.kubedb.com/sample-mariadb-2 created
```

### Verify Auto-backup configured

Now, let’s verify whether the auto-backup has been configured properly or not.

#### Verify Repository

At first, let’s verify whether Stash has created a `Repository` for our MariaDB or not.

```bash
❯ kubectl get repository -n demo-2
NAME                   INTEGRITY   SIZE   SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
app-sample-mariadb-2                                                                4s
```

Now, let’s check the YAML of the `Repository`.

```bash
❯ kubectl get repository -n demo-2 app-sample-mariadb-2  -o yaml
```

```text
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: app-sample-mariadb-2
  namespace: demo-2
  ...
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/demo-2/mariadb/sample-mariadb-2
    storageName: gcs-
```

Here, you can see that Stash has resolved the variables in `prefix` field and substituted them with the equivalent information from this new database.

#### Verify BackupConfiguration

If everything goes well, Stash should create a `BackupConfiguration` for our MariaDB in `demo-2` namespace and the phase of that `BackupConfiguration` should be `Ready`. Verify the `BackupConfiguration` crd by the following command,

```bash
❯ kubectl get backupconfiguration -n demo-2
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
app-sample-mariadb-2   mariadb-backup-11.8.5   */3 * * * *            Ready   3m24s
```

Now, let’s check the YAML of the `BackupConfiguration`.

```bash
❯ kubectl get backupconfiguration -n demo-2 app-sample-mariadb-2 -o yaml
```

```text
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: app-sample-mariadb-2
  namespace: demo-2
  ...
  ownerReferences:
  - apiVersion: appcatalog.appscode.com/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: AppBinding
    name: sample-mariadb-2
    uid: 7cbdf140-5fd1-487a-b04f-1847def418e8
  resourceVersion: "56888"
  selfLink: /apis/stash.appscode.com/v1beta1/namespaces/demo-2/backupconfigurations/app-sample-mariadb-2
  uid: e85dd3db-fa41-48b8-b253-5731ee8cc956
spec:
  driver: Restic
  repository:
    name: app-sample-mariadb-2
  retentionPolicy:
    keepLast: 5
    name: keep-last-5
    prune: true
  runtimeSettings: {}
  schedule: '*/3 * * * *'
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb-2
  tempDir: {}
status:
  conditions:
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Repository demo-2/app-sample-mariadb-2 exist.
    reason: RepositoryAvailable
    status: "True"
    type: RepositoryFound
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Backend  demo-2/gcs- exist.
    reason: BackendAvailable
    status: "True"
    type: BackendFound
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Backup target appcatalog.appscode.com/v1alpha1 appbinding/sample-mariadb-2
      found.
    reason: TargetAvailable
    status: "True"
    type: BackupTargetFound
  - lastTransitionTime: "2021-02-25T06:10:14Z"
    message: Successfully created backup triggering CronJob.
    reason: CronJobCreationSucceeded
    status: "True"
    type: CronJobCreated
  observedGeneration: 1
```

Notice the `schedule` section. This time the `BackupConfiguration` has been created with the schedule we have provided via annotation.

Also, notice the `target` section. Stash has automatically added the new MariaDB as the target of this `BackupConfiguration`.

#### Verify Backup

Now, let’s wait for a backup run to complete. You can watch for `BackupSession` as below,

```bash
❯ kubectl get backupsession -n demo-2 -w
NAME                              INVOKER-TYPE          INVOKER-NAME           PHASE       AGE
app-sample-mariadb-2-1614233715   BackupConfiguration   app-sample-mariadb-2   Succeeded   3m2s
app-sample-mariadb-2-1614233880   BackupConfiguration   app-sample-mariadb-2   Running     17s
```

Once the backup has been completed successfully, you should see that Stash has created a new directory as pointed by the `prefix` field of the new `Repository` and stored the backed up data there.

![Backup data in GCS Bucket](images/backup_stash_auto-backup_sample-mariadb-2.png)

Fig: Backup data in GCS Bucket

## Auto-backup with custom parameters

In this section, we are going to backup an MariaDB database of `demo-3` namespace. This time, we are going to pass some parameters for the Task through the annotations.

### Create Storage

At first, let’s create the `gcs-` in `demo-3` namespace with the access credentials to our GCS bucket.

```bash
❯ kubectl create  generic -n demo-3 gcs- \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
/gcs- created
```

### Create Database

Now, we are going to create an MariaDB CRO in `demo-3` namespace. Below is the YAML of the MariaDB object that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb-3
  namespace: demo-3
  annotations:
    stash.appscode.com/backup-blueprint: mariadb-backup-template
    params.stash.appscode.com/args: --databases mysql
spec:
  version: "12.1.2"
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

Notice the `annotations` section. This time, we have passed an argument via `params.stash.appscode.com/args` annotation along with the `stash.appscode.com/backup-blueprint` annotation.

Let’s create the above MariaDB CRO,

```bash
❯ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/sample-mariadb-3.yaml
mariadb.kubedb.com/sample-mariadb-3 created
```

### Verify Auto-backup configured

Now, let’s verify whether the auto-backup resources has been created or not.

#### Verify Repository

At first, let’s verify whether Stash has created a `Repository` for our MariaDB or not.

```bash
❯ kubectl get repository -n demo-3
NAME                   INTEGRITY   SIZE   SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
app-sample-mariadb-3                                                                8s
```

Now, let’s check the YAML of the `Repository`.

```bash
❯ kubectl get repository -n demo-3 app-sample-mariadb-3 -o yaml
```

```text
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: app-sample-mariadb-3
  namespace: demo-3
  ...
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: mariadb-backup/demo-3/mariadb/sample-mariadb-3
    storageName: gcs-
```

Here, you can see that Stash has resolved the variables in `prefix` field and substituted them with the equivalent information from this new database.

#### Verify BackupConfiguration

If everything goes well, Stash should create a `BackupConfiguration` for our MariaDB in `demo-3` namespace and the phase of that `BackupConfiguration` should be `Ready`. Verify the `BackupConfiguration` crd by the following command,

```bash
❯ kubectl get backupconfiguration -n demo-3
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
app-sample-mariadb-3   mariadb-backup-11.8.5   */5 * * * *            Ready   106s
```

Now, let’s check the YAML of the `BackupConfiguration`.

```bash
❯ kubectl get backupconfiguration -n demo-3 app-sample-mariadb-3 -o yaml
```

```text
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: app-sample-mariadb-3
  namespace: demo-3
  ...
spec:
  driver: Restic
  repository:
    name: app-sample-mariadb-3
  retentionPolicy:
    keepLast: 5
    name: keep-last-5
    prune: true
  runtimeSettings: {}
  schedule: '*/5 * * * *'
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb-3
  task:
    params:
    - name: args
      value: --databases mysql
  tempDir: {}
status:
  conditions:
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Repository demo-3/app-sample-mariadb-3 exist.
    reason: RepositoryAvailable
    status: "True"
    type: RepositoryFound
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Backend  demo-3/gcs- exist.
    reason: BackendAvailable
    status: "True"
    type: BackendFound
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Backup target appcatalog.appscode.com/v1alpha1 appbinding/sample-mariadb-3
      found.
    reason: TargetAvailable
    status: "True"
    type: BackupTargetFound
  - lastTransitionTime: "2021-02-25T11:58:12Z"
    message: Successfully created backup triggering CronJob.
    reason: CronJobCreationSucceeded
    status: "True"
    type: CronJobCreated
  observedGeneration: 1
```

Notice the `task` section. The `args` parameter that we had passed via annotations has been added to the `params` section.

Also, notice the `target` section. Stash has automatically added the new MariaDB as the target of this `BackupConfiguration`.

#### Verify Backup

Now, let’s wait for a backup run to complete. You can watch for `BackupSession` as below,

```bash
❯ kubectl get backupsession -n demo-3 -w
NAME                              INVOKER-TYPE          INVOKER-NAME           PHASE       AGE
app-sample-mariadb-3-1614254408   BackupConfiguration   app-sample-mariadb-3   Succeeded   5m23s
app-sample-mariadb-3-1614254708   BackupConfiguration   app-sample-mariadb-3   Running     23s
```

Once the backup has been completed successfully, you should see that Stash has created a new directory as pointed by the `prefix` field of the new `Repository` and stored the backed up data there.

![Backup data in GCS Bucket](images/backup_stash_auto-backup_sample-mariadb-3.png)

Fig: Backup data in GCS Bucket

## Cleanup

To cleanup the resources crated by this tutorial, run the following commands,

```bash
❯ kubectl delete -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/backup/auto-backup/examples/
backupblueprint.stash.appscode.com "mariadb-backup-template" deleted
mariadb.kubedb.com "sample-mariadb-2" deleted
mariadb.kubedb.com "sample-mariadb-3" deleted
mariadb.kubedb.com "sample-mariadb" deleted

❯ kubectl delete repository -n demo --all
repository.stash.appscode.com "app-sample-mariadb" deleted
❯ kubectl delete repository -n demo-2 --all
repository.stash.appscode.com "app-sample-mariadb-2" deleted
❯ kubectl delete repository -n demo-3 --all
repository.stash.appscode.com "app-sample-mariadb-3" deleted
```

<!-- PAGE_START: backup/stash/customization.md -->
# Customizing Backup and Restore Process

Stash provides rich customization supports for the backup and restore process to meet the requirements of various cluster configurations. This guide will show you some examples of these customizations.

## Customizing Backup Process

In this section, we are going to show you how to customize the backup process. Here, we are going to show some examples of providing arguments to the backup process, running the backup process as a specific user, ignoring some indexes during the backup process, etc.

### Passing arguments to the backup process

Stash MariaDB addon uses [mysqldump](https://mariadb.com/kb/en/mysqldump) for backup. You can pass arguments to the `mysqldump` through `args` param under `task.params` section.

The below example shows how you can pass the `--databases testdb` to take backup for a specific mariadb databases named `testdb`.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  task:
    params:
    - name: args
      value: --databases testdb
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

> **WARNING**: Make sure that you have the specific database created before taking backup. In this case, Database `testdb` should exist before the backup job starts.

### Running backup job as a specific user

If your cluster requires running the backup job as a specific user, you can provide `securityContext` under `runtimeSettings.pod` section. The below example shows how you can run the backup job as the root user.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/2 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    pod:
      securityContext:
        runAsUser: 0
        runAsGroup: 0
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

### Specifying Memory/CPU limit/request for the backup job

If you want to specify the Memory/CPU limit/request for your backup job, you can specify `resources` field under `runtimeSettings.container` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/2 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    container:
      resources:
        requests:
          cpu: "200m"
          memory: "1Gi"
        limits:
          cpu: "200m"
          memory: "1Gi"
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

### Using multiple retention policies

You can also specify multiple retention policies for your backed up data. For example, you may want to keep few daily snapshots, few weekly snapshots, and few monthly snapshots, etc. You just need to pass the desired number with the respective key under the `retentionPolicy` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: sample-mariadb-retention
    keepLast: 5
    keepDaily: 10
    keepWeekly: 20
    keepMonthly: 50
    keepYearly: 100
    prune: true
```

To know more about the available options for retention policies, please visit [here](https://stash.run/docs/latest/concepts/crds/backupconfiguration/#specretentionpolicy).

## Customizing Restore Process

Stash also uses `mysql` during the restore process. In this section, we are going to show how you can pass arguments to the restore process, restore a specific snapshot, run restore job as a specific user, etc.

### Passing arguments to the restore process

Similar to the backup process, you can pass arguments to the restore process through the `args` params under `task.params` section. This example will restore data from database `testdb` only.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  task:
    params:
    - name: args
      value: --one-database testdb
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [latest]
```

### Restore specific snapshot

You can also restore a specific snapshot. At first, list the available snapshot as bellow,

```bash
❯ kubectl get snapshots -n demo
NAME                ID         REPOSITORY   HOSTNAME   CREATED AT
gcs-repo-4bc21d6f   4bc21d6f   gcs-repo     host-0     2022-01-12T14:54:27Z
gcs-repo-f0ac7cbd   f0ac7cbd   gcs-repo     host-0     2022-01-12T14:56:26Z
gcs-repo-9210ebb6   9210ebb6   gcs-repo     host-0     2022-01-12T14:58:27Z
gcs-repo-0aff8890   0aff8890   gcs-repo     host-0     2022-01-12T15:00:28Z
```

> You can also filter the snapshots as shown in the guide [here](https://stash.run/docs/latest/concepts/crds/snapshot/#working-with-snapshot).

You can use the respective ID of the snapshot to restore that snapshot.

The below example shows how you can pass a specific snapshot ID through the `snapshots` field of `rules` section.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [4bc21d6f]
```

> Please, do not specify multiple snapshots here. Each snapshot represents a complete backup of your database. Multiple snapshots are only usable during file/directory restore.

### Running restore job as a specific user

You can provide `securityContext` under `runtimeSettings.pod` section to run the restore job as a specific user.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    pod:
      securityContext:
        runAsUser: 0
        runAsGroup: 0
  rules:
  - snapshots: [latest]
```

### Specifying Memory/CPU limit/request for the restore job

Similar to the backup process, you can also provide `resources` field under the `runtimeSettings.container` section to limit the Memory/CPU for your restore job.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  runtimeSettings:
    container:
      resources:
        requests:
          cpu: "200m"
          memory: "1Gi"
        limits:
          cpu: "200m"
          memory: "1Gi"
  rules:
  - snapshots: [latest]
```

<!-- PAGE_START: backup/stash/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

Please install [Stash](https://stash.run/docs/latest/setup/install/stash/) to try this feature. Database backup with Stash is already included in the KubeDB license. So, you don’t need a separate license for Stash.

# MariaDB Backup & Restore Overview

KubeDB uses [Stash](https://stash.run) to backup and restore databases. Stash by AppsCode is a cloud native data backup and recovery solution for Kubernetes workloads. Stash utilizes [restic](https://github.com/restic/restic) to securely backup stateful applications to any cloud or on-prem storage backends (for example, S3, GCS, Azure Blob storage, Minio, NetApp, Dell EMC etc.).

  ![KubeDB + Stash](images/backup_stash_overview_kubedb_plus_stash.svg)

Fig: Backup KubeDB Databases Using Stash

# How Stash Backups & Restores MariaDB Database

Stash 0.9.0+ supports backup and restore operation of many databases. This guide will give you an overview of how MariaDB database backup and restore process works in Stash.

## Logical Backup

Stash supports taking [logical backup](https://mariadb.com/kb/en/backup-and-restore-overview/#logical-vs-physical-backups) of MariaDB databases using [mysqldump](https://mariadb.com/kb/en/mysqldump/). It is the most flexible way to perform a backup and restore, and a good choice when the data size is relatively small.

### How Logical Backup Works

The following diagram shows how Stash takes logical backup of a MariaDB database. Open the image in a new tab to see the enlarged version.

  ![MariaDB Backup Overview](images/backup_stash_overview_mariadb-logical-backup.svg)

Fig: MariaDB Logical Backup Overview

The backup process consists of the following steps:

1. At first, a user creates a secret with access credentials of the backend where the backed up data will be stored.
2. Then, she creates a `Repository` crd that specifies the backend information along with the secret that holds the credentials to access the backend.
3. Then, she creates a `BackupConfiguration` crd targeting the [AppBinding](en/concepts/appbinding.md) crd of the desired database. The `BackupConfiguration` object also specifies the `Task` to use to backup the database.
4. Stash operator watches for `BackupConfiguration` crd.
5. Once Stash operator finds a `BackupConfiguration` crd, it creates a CronJob with the schedule specified in `BackupConfiguration` object to trigger backup periodically.
6. On the next scheduled slot, the CronJob triggers a backup by creating a `BackupSession` crd.
7. Stash operator also watches for `BackupSession` crd.
8. When it finds a `BackupSession` object, it resolves the respective `Task` and `Function` and prepares a Job definition to backup.
9. Then, it creates the Job to backup the targeted database.
10. The backup Job reads necessary information to connect with the database from the `AppBinding` crd. It also reads backend information and access credentials from `Repository` crd and Storage Secret respectively.
11. Then, the Job dumps the targeted database and uploads the output to the backend. Stash pipes the output of dump command to uploading process. Hence, backup Job does not require a large volume to hold the entire dump output.
12. Finally, when the backup is complete, the Job sends Prometheus metrics to the Pushgateway running inside Stash operator pod. It also updates the `BackupSession` and `Repository` status to reflect the backup procedure.

### How Restore from Logical Backup Works

The following diagram shows how Stash restores a MariaDB database from a logical backup. Open the image in a new tab to see the enlarged version.

  ![Database Restore Overview](images/backup_stash_overview_mariadb-logical-restore.svg)

Fig: MariaDB Logical Restore Process Overview

The restore process consists of the following steps:

1. At first, a user creates a `RestoreSession` crd targeting the `AppBinding` of the desired database where the backed up data will be restored. It also specifies the `Repository` crd which holds the backend information and the `Task` to use to restore the target.
2. Stash operator watches for `RestoreSession` object.
3. Once it finds a `RestoreSession` object, it resolves the respective `Task` and `Function` and prepares a Job definition to restore.
4. Then, it creates the Job to restore the target.
5. The Job reads necessary information to connect with the database from respective `AppBinding` crd. It also reads backend information and access credentials from `Repository` crd and Storage Secret respectively.
6. Then, the job downloads the backed up data from the backend and injects into the desired database. Stash pipes the downloaded data to the respective database tool to inject into the database. Hence, restore job does not require a large volume to download entire backup data inside it.
7. Finally, when the restore process is complete, the Job sends Prometheus metrics to the Pushgateway and update the `RestoreSession` status to reflect restore completion.

## Next Steps

* Backup a standalone MariaDB databases using Stash following the guide from [here](en/backup/stash/logical/standalone.md).
* Backup a MariaDB cluster using Stash following the guide from [here](en/backup/stash/logical/cluster.md).
* Configure a generic backup template for all the MariaDB databases of your cluster using Stash Auto-backup by following the guide from [here](en/backup/stash/auto-backup.md).
* Customize the backup & restore process for your cluster by following the guides from [here](en/backup/stash/customization.md).

<!-- PAGE_START: distributed/opsrequest/horizontal_scale.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Horizontal Scale Distributed MariaDB

This guide will show you how to use `KubeDB` Opsrequest operator to horizontally scale a distributed MariaDB Galera cluster across multiple Kubernetes clusters.

> **Note:** All other `OpsRequest` operations behave consistently in a distributed environment. Only `HorizontalScaling` has cluster-specific considerations covered in this guide.

## Before You Begin

* At first, you need to have a multi-cluster Kubernetes setup with OCM and KubeSlice configured. Follow the [Distributed MariaDB Overview](en/distributed/overview.md) guide to set up the required infrastructure.
* Install `KubeDB` Community and Enterprise operator in your hub cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README). Make sure to enable OCM support:

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [Distributed MariaDB Overview](en/distributed/overview.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Horizontal Scaling Overview](en/scaling/horizontal-scaling/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Apply Horizontal Scaling on Distributed Cluster

Here, we are going to deploy a distributed `MariaDB` Galera cluster and then apply horizontal scaling using `MariaDBOpsRequest`.

### Deploy PlacementPolicy

For a distributed MariaDB cluster, the `PlacementPolicy` must be created before deploying the database. It defines which replica index is scheduled on which cluster and acts as the upper bound for scaling, the actual running replicas can be any number less than or equal to the total indices defined in the policy.

> Note: Ensure you correctly specify the mapping of every DB pod index to its target cluster. A corresponding cluster must be defined for each DB pod index. Any missing index will result in provisioning errors.

In this example, the `PlacementPolicy` is configured with **five** replica indices distributed across two clusters. The MariaDB cluster will start with **three** replicas (indices `0`, `1`, `2`), and can be scaled up to **five** (indices `0`–`4`) without modifying the policy.

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        replicaIndices:
          - 0
          - 2
          - 4
      - clusterName: demo-worker
        replicaIndices:
          - 1
          - 3
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Here,

* `spec.clusterSpreadConstraint.distributionRules[].replicaIndices` specifies which MariaDB replica indices are scheduled on that cluster. `demo-controller` will host replicas `0`, `2`, and `4`; `demo-worker` will host replicas `1` and `3`.

Apply the `PlacementPolicy` on the hub (`demo-controller`) cluster:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/placement-policy.yaml --context demo-controller
placementpolicy.apps.k8s.appscode.com/distributed-mariadb created
```

### Deploy Distributed MariaDB Cluster

In this section, we are going to deploy a distributed MariaDB Galera cluster with version `12.1.2`. Note that `spec.distributed` is set to `true` and `spec.replicas` is `3` which is less than the five indices defined in the `PlacementPolicy`. The operator will only create pods for indices `0`, `1`, and `2`.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
spec:
  version: "12.1.2"
  distributed: true
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "longhorn"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
      containers:
        - name: mariadb
          resources:
            requests:
              cpu: "200m"
              memory: "300Mi"
            limits:
              cpu: "200m"
              memory: "300Mi"
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/mariadb.yaml --context demo-controller
mariadb.kubedb.com/mariadb created
```

Now, wait until `mariadb` has status `Ready`:

```bash
$ kubectl get mariadb -n demo --context demo-controller
NAME             VERSION   STATUS   AGE
mariadb          11.5.2    Ready    2m36s
```

Let’s check the number of replicas this database has from the MariaDB object:

```bash
$ kubectl get mariadb -n demo mariadb -o json | jq '.spec.replicas'
3
```

The pods are distributed across clusters as defined by the `PlacementPolicy`. Indices `0` and `2` land on `demo-controller`; index `1` lands on `demo-worker`:

```bash
$ kubectl get pods -n demo --context demo-controller
NAME          READY   STATUS    RESTARTS   AGE
mariadb-0     3/3     Running   0          2m30s
mariadb-2     3/3     Running   0          2m30s

$ kubectl get pods -n demo --context demo-worker
NAME          READY   STATUS    RESTARTS   AGE
mariadb-1     3/3     Running   0          2m30s
```

We can see the cluster has 3 pods. We are now ready to apply `MariaDBOpsRequest` to scale this database.

## Scale Up Replicas

Here, we are going to scale up the replicas from `3` to `5`. Because the `PlacementPolicy` already defines indices `0`–`4`, no changes to the policy are required — the operator knows where to place the new pods.

### Create MariaDBOpsRequest

In order to scale up the replicas, we have to create a `MariaDBOpsRequest` CR with our desired replicas. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create:

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-up
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: mariadb
  horizontalScaling:
    member : 5
```

Here,

* `spec.databaseRef.name` specifies that we are performing horizontal scaling on `mariadb`.
* `spec.type` specifies that we are performing `HorizontalScaling`.
* `spec.horizontalScaling.member` specifies the desired replica count after scaling. This value must not exceed the total number of indices defined in the `PlacementPolicy` (5 in this example).

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/mdops-upscale.yaml --context demo-controller
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-up created
```

### Verify Cluster Replicas Scaled Up Successfully

If everything goes well, `KubeDB` Enterprise operator will update the replicas of the `MariaDB` object and create the new pods on the clusters specified by the `PlacementPolicy`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`:

```bash
$ watch kubectl get mariadbopsrequest -n demo --context demo-controller
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                        TYPE                STATUS       AGE
mdops-scale-horizontal-up   HorizontalScaling   Successful   18m
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, let’s verify the number of replicas:

```bash
$ kubectl get mariadb -n demo mariadb -o json | jq '.spec.replicas'
5
```

The two new pods are placed on the clusters according to the `PlacementPolicy` — index `4` on `demo-controller` and index `3` on `demo-worker`:

```bash
$ kubectl get pods -n demo --context demo-controller
NAME        READY   STATUS    RESTARTS   AGE
mariadb-0   3/3     Running   0          58m
mariadb-2   3/3     Running   0          55m
mariadb-4   3/3     Running   0          17m


$ kubectl get pods -n demo --context demo-worker
NAME        READY   STATUS    RESTARTS   AGE
mariadb-1   3/3     Running   0          57m
mariadb-3   3/3     Running   0          19m
```

From all the above outputs we can see that the cluster now has `5` replicas. We have successfully scaled up the distributed MariaDB cluster.

## Scale Down Replicas

Here, we are going to scale down the replicas from `5` to `3`. The `PlacementPolicy` does not need to be modified — the operator will remove the highest-indexed pods (`mariadb-3` and `mariadb-4`) and the remaining pods will continue running as defined by the policy.

### Create MariaDBOpsRequest

In order to scale down the cluster, we have to create a `MariaDBOpsRequest` CR with our desired replicas. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create:

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-down
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: mariadb
  horizontalScaling:
    member: 3
```

Here,

* `spec.databaseRef.name` specifies that we are performing horizontal scaling down on `mariadb`.
* `spec.type` specifies that we are performing `HorizontalScaling`.
* `spec.horizontalScaling.member` specifies the desired replica count after scaling.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/opsrequest/examples/mdops-downscale.yaml --context demo-controller
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-down created
```

### Verify Cluster Replicas Scaled Down Successfully

If everything goes well, `KubeDB` Enterprise operator will update the replicas of the `MariaDB` object and remove the highest-indexed pods from their respective clusters.

Let’s wait for `MariaDBOpsRequest` to be `Successful`:

```bash
$ watch kubectl get mariadbopsrequest -n demo --context demo-controller
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                          TYPE               STATUS       AGE
mdops-scale-horizontal-down   HorizontalScaling  Successful   2m32s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, let’s verify the number of replicas:

```bash
$ kubectl get mariadb -n demo mariadb -o json | jq '.spec.replicas'
3
```

Pods `mariadb-3` and `mariadb-4` have been removed from their respective clusters:

```bash
$ kubectl get pods -n demo --context demo-controller
NAME          READY   STATUS    RESTARTS   AGE
mariadb-0     3/3     Running   0          20m
mariadb-2     3/3     Running   0          20m

$ kubectl get pods -n demo --context demo-worker
NAME          READY   STATUS    RESTARTS   AGE
mariadb-1     3/3     Running   0          20m
```

From all the above outputs we can see that the cluster now has `3` replicas. We have successfully scaled down the distributed MariaDB cluster.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo mariadb --context demo-controller
$ kubectl delete mariadbopsrequest -n demo mdops-scale-horizontal-up mdops-scale-horizontal-down --context demo-controller
$ kubectl delete placementpolicy distributed-mariadb --context demo-controller
```

<!-- PAGE_START: scaling/horizontal-scaling/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Horizontal Scale MariaDB

This guide will show you how to use `KubeDB` Enterprise operator to scale the cluster of a MariaDB database.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install `KubeDB` Community and Enterprise operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDB Cluster](en/clustering/galera-cluster.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Horizontal Scaling Overview](en/scaling/horizontal-scaling/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Apply Horizontal Scaling on Cluster

Here, we are going to deploy a `MariaDB` cluster using a supported version by `KubeDB` operator. Then we are going to apply horizontal scaling on it.

### Prepare MariaDB Cluster Database

Now, we are going to deploy a `MariaDB` cluster with version `12.1.2`.

### Deploy MariaDB Cluster

In this section, we are going to deploy a MariaDB cluster. Then, in the next section we will scale the database using `MariaDBOpsRequest` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
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

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/horizontal-scaling/cluster/example/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    2m36s
```

Let’s check the number of replicas this database has from the MariaDB object, number of pods the petset have,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.replicas'
3
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.replicas'
3
```

We can see from both command that the database has 3 replicas in the cluster.

Also, we can verify the replicas of the replicaset from an internal mariadb command by execing into a replica.

First we need to get the username and password to connect to a mariadb instance,

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d
nrKuxni0wDSMrgwy
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the number of replicas,

```bash
$  kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "show status like 'wsrep_cluster_size';"
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
```

We can see from the above output that the cluster has 3 nodes.

We are now ready to apply the `MariaDBOpsRequest` CR to scale this database.

## Scale Up Replicas

Here, we are going to scale up the replicas of the replicaset to meet the desired number of replicas after scaling.

#### Create MariaDBOpsRequest

In order to scale up the replicas of the replicaset of the database, we have to create a `MariaDBOpsRequest` CR with our desired replicas. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-up
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: sample-mariadb
  horizontalScaling:
    member : 5
```

Here,

* `spec.databaseRef.name` specifies that we are performing horizontal scaling operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `HorizontalScaling` on our database.
* `spec.horizontalScaling.member` specifies the desired replicas after scaling.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/horizontal-scaling/cluster/example/mdops-upscale.yaml
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-up created
```

#### Verify Cluster replicas scaled up successfully

If everything goes well, `KubeDB` Enterprise operator will update the replicas of `MariaDB` object and related `PetSets` and `Pods`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                        TYPE                STATUS       AGE
mdps-scale-horizontal    HorizontalScaling    Successful     106s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, we are going to verify the number of replicas this database has from the MariaDB object, number of pods the petset have,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.replicas'
5
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.replicas'
5
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the number of replicas,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "show status like 'wsrep_cluster_size';"
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 5     |
+--------------------+-------+
```

From all the above outputs we can see that the replicas of the cluster is `5`. That means we have successfully scaled up the replicas of the MariaDB replicaset.

### Scale Down Replicas

Here, we are going to scale down the replicas of the cluster to meet the desired number of replicas after scaling.

#### Create MariaDBOpsRequest

In order to scale down the cluster of the database, we have to create a `MariaDBOpsRequest` CR with our desired replicas. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-scale-horizontal-down
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: sample-mariadb
  horizontalScaling:
    member : 3
```

Here,

* `spec.databaseRef.name` specifies that we are performing horizontal scaling down operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `HorizontalScaling` on our database.
* `spec.horizontalScaling.replicas` specifies the desired replicas after scaling.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/horizontal-scaling/cluster/example/mdops-downscale.yaml
mariadbopsrequest.ops.kubedb.com/mdops-scale-horizontal-down created
```

#### Verify Cluster replicas scaled down successfully

If everything goes well, `KubeDB` Enterprise operator will update the replicas of `MariaDB` object and related `PetSets` and `Pods`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                          TYPE                STATUS       AGE
mops-hscale-down-replicaset   HorizontalScaling   Successful   2m32s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, we are going to verify the number of replicas this database has from the MariaDB object, number of pods the petset have,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json | jq '.spec.replicas' 
3
$ kubectl get petset -n demo sample-mariadb -o json | jq '.spec.replicas'
3
```

Now let’s connect to a mariadb instance and run a mariadb internal command to check the number of replicas,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "show status like 'wsrep_cluster_size';"
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
```

From all the above outputs we can see that the replicas of the cluster is `3`. That means we have successfully scaled down the replicas of the MariaDB replicaset.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo  mdops-scale-horizontal-up mdops-scale-horizontal-down
```

<!-- PAGE_START: scaling/horizontal-scaling/maxscale.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Horizontal Scale MaxScale

This guide will show you how to use `KubeDB` Ops-manager operator to scale MaxScale server.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install `KubeDB` operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDB Replication](en/clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Horizontal Scaling Overview](en/scaling/horizontal-scaling/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Apply Horizontal Scaling on MaxScale Server

Here, we are going to deploy a `MariaDB` cluster in replication mode using a supported version by `KubeDB` operator. Then we are going to apply horizontal scaling on `MaxScale` server.

### Deploy MariaDB Cluster

In this section, we are going to deploy a MariaDB cluster in replication mode. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-replication
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/md-replication.yaml
mariadb.kubedb.com/md-replication created
```

Now, wait until `md-replication` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
md-replication   11.8.5   Ready    2m8s
```

Let’s check the number of replicas `Maxscale` has from the MariaDB object, also the number of replicas the petset have,

```bash
$ kubectl get mariadb -n demo md-replication -o json | jq '.spec.topology.maxscale.replicas'
3
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.replicas'
3
```

We can see from both command that the `MaxScale` has 3 replicas in the cluster.

## Scale Up Replicas

Here, we are going to scale up the replicas of the replicaset to meet the desired number of replicas after scaling.

#### Create MariaDBOpsRequest

In order to scale up the replicas of the replicaset of the `MaxScale` server, we have to create a `MariaDBOpsRequest` CR with our desired replicas. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-horizontal-scale-up
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: md-replication
  horizontalScaling:
    maxscale: true
    member: 4
```

Here,

* `spec.type` specifies that we are performing `HorizontalScaling` on our database.
* `spec.databaseRef.name` specifies that we are performing horizontal scaling operation on `md-replication` database.
* `spec.horizontalScaling.maxscale` specifies that we are performing horizontal scaling operation on maxscale server. If false then horizontal scaling performs on mariadb database.
* `spec.horizontalScaling.member` specifies the desired replicas after scaling.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/horizontal-scaling/mx-hscale-up.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-horizontal-scale-up created
```

#### Verify Cluster replicas scaled up successfully

If everything goes well, `KubeDB` Ops-manager operator will update the replicas of `MaxScale` object and related `PetSets` and `Pods`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                           TYPE                STATUS       AGE
maxscale-horizontal-scale-up   HorizontalScaling   Successful   2m31s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, we are going to verify the number of replicas this database has from the MariaDB object, number of pods the petset have,

```bash
$ kubectl get mariadb -n demo md-replication -o json | jq '.spec.topology.maxscale.replicas'
4
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.replicas'
4
```

From all the above outputs we can see that the replicas of the `MaxScale` server is `4`. That means we have successfully scaled up the replicas of the MaxScale server.

### Scale Down Replicas

Here, we are going to scale down the replicas of the cluster to meet the desired number of replicas after scaling.

#### Create MariaDBOpsRequest

In order to scale down the replicas of the `MaxScale` server, we have to create a `MariaDBOpsRequest` CR with our desired replicas. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-horizontal-scale-down
  namespace: demo
spec:
  type: HorizontalScaling
  databaseRef:
    name: md-replication
  horizontalScaling:
    maxscale: true
    member: 3
```

Here,

* `spec.type` specifies that we are performing `HorizontalScaling` on our database.
* `spec.databaseRef.name` specifies that we are performing horizontal scaling operation on `md-replication` database.
* `spec.horizontalScaling.maxscale` specifies that we are performing horizontal scaling operation on maxscale server. If false then horizontal scaling performs on mariadb database.
* `spec.horizontalScaling.member` specifies the desired replicas after scaling.

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/horizontal-scaling/mx-hscale-down.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-horizontal-scale-down created
```

#### Verify Cluster replicas scaled down successfully

If everything goes well, `KubeDB` Ops-manager operator will update the replicas of `MaxScale` object and related `PetSets` and `Pods`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                             TYPE                STATUS       AGE
maxscale-horizontal-scale-down   HorizontalScaling   Successful   55s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, we are going to verify the number of replicas `MaxScale` server has from the MariaDB object, number of pods the petset have,

```bash
$ kubectl get mariadb -n demo md-replication -o json | jq '.spec.topology.maxscale.replicas'
3
$ kubectl get petset -n demo md-replication-mx -o json | jq '.spec.replicas'
3
```

From all the above outputs we can see that the replicas of the cluster is `3`. That means we have successfully scaled down the replicas of the MaxScale server.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo md-replication
$ kubectl delete mariadbopsrequest -n demo  maxscale-horizontal-scale-up maxscale-horizontal-scale-down
$ kubectl delete ns demo
```

<!-- PAGE_START: scaling/horizontal-scaling/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Horizontal Scaling

This guide will give an overview on how KubeDB Ops Manager scales up or down `MariaDB Cluster`.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Horizontal Scaling Process Works

The following diagram shows how KubeDB Ops Manager scales up or down `MariaDB` database components. Open the image in a new tab to see the enlarged version.

  ![Horizontal scaling process of MariaDB](images/scaling_horizontal-scaling_overview_horizontal-scaling.jpg)

Fig: Horizontal scaling process of MariaDB

The Horizontal scaling process consists of the following steps:

1. At first, a user creates a `MariaDB` Custom Resource (CR).
2. `KubeDB` Community operator watches the `MariaDB` CR.
3. When the operator finds a `MariaDB` CR, it creates required number of `PetSets` and related necessary stuff like secrets, services, etc.
4. Then, in order to scale the `MariaDB` database the user creates a `MariaDBOpsRequest` CR with desired information.
5. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CR.
6. When it finds a `MariaDBOpsRequest` CR, it pauses the `MariaDB` object which is referred from the `MariaDBOpsRequest`. So, the `KubeDB` Community operator doesn’t perform any operations on the `MariaDB` object during the horizontal scaling process.
7. Then the `KubeDB` Enterprise operator will scale the related PetSet Pods to reach the expected number of replicas defined in the `MariaDBOpsRequest` CR.
8. After the successfully scaling the replicas of the PetSet Pods, the `KubeDB` Enterprise operator updates the number of replicas in the `MariaDB` object to reflect the updated state.
9. After the successful scaling of the `MariaDB` replicas, the `KubeDB` Enterprise operator resumes the `MariaDB` object so that the `KubeDB` Community operator resumes its usual operations.

In the next docs, we are going to show a step by step guide on horizontal scaling of MariaDB database using `MariaDBOpsRequest` CRD.

<!-- PAGE_START: scaling/vertical-scaling/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Vertical Scale MariaDB Cluster

This guide will show you how to use `KubeDB` Enterprise operator to update the resources of a MariaDB cluster database.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install `KubeDB` Community and Enterprise operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [Clustering](en/clustering/galera-cluster.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Vertical Scaling Overview](en/scaling/vertical-scaling/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Apply Vertical Scaling on Cluster

Here, we are going to deploy a `MariaDB` cluster using a supported version by `KubeDB` operator. Then we are going to apply vertical scaling on it.

### Prepare MariaDB Cluster

Now, we are going to deploy a `MariaDB` cluster database with version `12.1.2`.

> Vertical Scaling for `MariaDB Standalone` can be performed in the same way as `MariaDB Cluster`. Only remove the `spec.replicas` field from the below yaml to deploy a MariaDB Standalone.

### Deploy MariaDB Cluster

In this section, we are going to deploy a MariaDB cluster database. Then, in the next section we will update the resources of the database using `MariaDBOpsRequest` CRD. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
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

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION    STATUS     AGE
sample-mariadb    11.8.5     Ready     3m46s
```

Let’s check the Pod containers resources,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "500m",
    "memory": "1Gi"
  },
  "requests": {
    "cpu": "500m",
    "memory": "1Gi"
  }
}
```

You can see the Pod has the default resources which is assigned by KubeDB operator.

We are now ready to apply the `MariaDBOpsRequest` CR to update the resources of this database.

### Vertical Scaling

Here, we are going to update the resources of the database to meet the desired resources after scaling.

#### Create MariaDBOpsRequest

In order to update the resources of the database, we have to create a `MariaDBOpsRequest` CR with our desired resources. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

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
          memory: "1.2Gi"
          cpu: "0.6"
        limits:
          memory: "1.2Gi"
          cpu: "0.6"
```

Here,

* `spec.databaseRef.name` specifies that we are performing vertical scaling operation on `sample-mariadb` database.
* `spec.type` specifies that we are performing `VerticalScaling` on our database.
* `spec.VerticalScaling.mariadb` specifies the desired resources after scaling.
* `spec.verticalScaling.mode` specifies how the scaling is actuated — `Restart` (default, restarts the Pods) or `InPlace` (resizes the running Pods without a restart, falling back to restart if a Node can’t fit the new resources). See [Vertical Scaling Modes](en/scaling/vertical-scaling/overview.md#vertical-scaling-modes).

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/mdops-vscale.yaml
mariadbopsrequest.ops.kubedb.com/mdops-vscale created
```

#### Verify MariaDB Cluster resources updated successfully

If everything goes well, `KubeDB` Enterprise operator will update the resources of `MariaDB` object and related `PetSets` and `Pods`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                     TYPE              STATUS       AGE
mdops-vscale        VerticalScaling      Successful    3m56s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, we are going to verify from one of the Pod yaml whether the resources of the database has updated to meet up the desired state, Let’s check,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "600m",
    "memory": "1288490188800m"
  },
  "requests": {
    "cpu": "600m",
    "memory": "1288490188800m"
  }
}
```

The above output verifies that we have successfully scaled up the resources of the MariaDB database.

### In-Place Vertical Scaling

To resize the Pods **without a restart**, set `spec.verticalScaling.mode` to `InPlace` in the
`MariaDBOpsRequest`. The operator resizes the running containers via the Kubernetes `pods/resize`
subresource and only restarts a Pod if its Node cannot accommodate the new resources.

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-vscale-inplace
  namespace: demo
spec:
  type: VerticalScaling
  databaseRef:
    name: sample-mariadb
  verticalScaling:
    mode: InPlace
    mariadb:
      resources:
        requests:
          memory: "1.2Gi"
          cpu: "0.6"
        limits:
          memory: "1.2Gi"
          cpu: "0.6"
```

Let’s apply it the same way as above:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/mdops-vscale-inplace.yaml
mariadbopsrequest.ops.kubedb.com/mdops-vscale-inplace created
```

The resources update in place with no Pod restart.

> **Note:** For a **distributed** `MariaDB` deployment, true in-place resize is not possible, so `InPlace` automatically degrades to `Restart`.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-vscale
```

<!-- PAGE_START: scaling/vertical-scaling/maxscale.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Vertical Scale MaxScale Server

This guide will show you how to use `KubeDB` Ops-manager operator to update the resources of a MaxScale server.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Install `KubeDB` operator in your cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDB Replication](en/clustering/mariadb-replication.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Vertical Scaling Overview](en/scaling/vertical-scaling/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Apply Vertical Scaling on MaxScale Server

Here, we are going to deploy a `MariaDB` cluster in replication mode using a supported version by `KubeDB` operator. Then we will apply vertical scaling on `MaxScale` server.

### Deploy MariaDB Cluster

In this section, we are going to deploy a MariaDB database in replication mode. Then, in the next section we will update the resources of the `MaxScale` server using `MariaDBOpsRequest` CR. Below is the YAML of the `MariaDB` CR that we are going to create,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: md-replication
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  topology:
    mode: MariaDBReplication
    maxscale:
      replicas: 3
      enableUI: true
      storageType: Durable
      storage:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 50Mi
  storageType: Durable
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CR we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/md-replication.yaml
mariadb.kubedb.com/md-replication created
```

Now, wait until `md-replication` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
md-replication   11.8.5   Ready    2m39s
```

Let’s check the Pod containers resources,

```bash
$ kubectl get pod -n demo md-replication-mx-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "memory": "512Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "256Mi"
  }
}
```

You can see the Pod has the default resources which is assigned by KubeDB operator.

We are now ready to apply the `MariaDBOpsRequest` CR to update the resources of this database.

### Vertical Scaling

Here, we are going to update the resources of `MaxScale` server to meet the desired resources after scaling.

#### Create MariaDBOpsRequest

In order to update the resources of the database, we have to create a `MariaDBOpsRequest` CR with our desired resources. Below is the YAML of the `MariaDBOpsRequest` CR that we are going to create,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: maxscale-vertical-scale
  namespace: demo
spec:
  type: VerticalScaling
  databaseRef:
    name: md-replication
  verticalScaling:
    maxscale:
      resources:
        requests:
          memory: "512Mi"
          cpu: "0.3"
        limits:
          memory: "1Gi"
          cpu: "0.6"
```

Here,

* `spec.type` specifies that we are performing `VerticalScaling` on our database.
* `spec.databaseRef.name` specifies that we are performing vertical scaling operation on `md-replication` database.
* `spec.VerticalScaling.maxscale` specifies the desired resources of maxscale server after scaling.
* `spec.verticalScaling.mode` specifies how the scaling is actuated — `Restart` (default, restarts the Pods) or `InPlace` (resizes the running Pods without a restart, falling back to restart if a Node can’t fit the new resources). See [Vertical Scaling Modes](en/scaling/vertical-scaling/overview.md#vertical-scaling-modes).

Let’s create the `MariaDBOpsRequest` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/vertical-scaling/mx-vscale.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-vertical-scale created
```

#### Verify MaxScale server resources updated successfully

If everything goes well, `KubeDB` Ops-manager operator will update the resources of `MariaDB` object and related `PetSets` and `Pods`.

Let’s wait for `MariaDBOpsRequest` to be `Successful`. Run the following command to watch `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo 

NAME                      TYPE              STATUS       AGE
maxscale-vertical-scale   VerticalScaling   Successful   3m8s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. Now, we are going to verify from one of the Pod yaml whether the resources of maxscale server has updated to meet up the desired state, Let’s check,

```bash
$ kubectl get pod -n demo md-replication-mx-0 -o json | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "600m",
    "memory": "1Gi"
  },
  "requests": {
    "cpu": "300m",
    "memory": "512Mi"
  }
}
```

The above output verifies that we have successfully scaled up the resources of the MariaDB database.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo md-replication
$ kubectl delete mariadbopsrequest -n demo maxscale-vertical-scale
$ kubectl delete ns demo
```

<!-- PAGE_START: scaling/vertical-scaling/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB Vertical Scaling

This guide will give an overview on how KubeDB Ops Manager vertically scales up `MariaDB`.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)

## How Vertical Scaling Process Works

The following diagram shows how KubeDB Ops Manager scales up or down `MariaDB` database components. Open the image in a new tab to see the enlarged version.

  ![Vertical scaling process of MariaDB](images/scaling_vertical-scaling_overview_vertical-scaling.jpg)

Fig: Vertical scaling process of MariaDB

The vertical scaling process consists of the following steps:

1. At first, a user creates a `MariaDB` Custom Resource (CR).
2. `KubeDB` Community operator watches the `MariaDB` CR.
3. When the operator finds a `MariaDB` CR, it creates required number of `PetSets` and related necessary stuff like secrets, services, etc.
4. Then, in order to update the resources(for example `CPU`, `Memory` etc.) of the `MariaDB` database the user creates a `MariaDBOpsRequest` CR with desired information.
5. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CR.
6. When it finds a `MariaDBOpsRequest` CR, it halts the `MariaDB` object which is referred from the `MariaDBOpsRequest`. So, the `KubeDB` Community operator doesn’t perform any operations on the `MariaDB` object during the vertical scaling process.
7. Then the `KubeDB` Enterprise operator will update resources of the PetSet Pods to reach desired state.
8. After the successful update of the resources of the PetSet’s replica, the `KubeDB` Enterprise operator updates the `MariaDB` object to reflect the updated state.
9. After the successful update of the `MariaDB` resources, the `KubeDB` Enterprise operator resumes the `MariaDB` object so that the `KubeDB` Community operator resumes its usual operations.

## Vertical Scaling Modes

KubeDB actuates vertical scaling in one of two modes, selected through the `spec.verticalScaling.mode`
field of the `MariaDBOpsRequest`:

* **`Restart`** (default): The operator patches the `PetSet` with the new resources and restarts the
  Pods (one at a time, honoring the database’s failover rules) so they come back with the updated CPU
  and Memory. This works on every Kubernetes cluster.
* **`InPlace`**: The operator resizes the running containers in place using the Kubernetes
  [in-place Pod resize](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/)
  (`pods/resize` subresource) — no Pod restart, so scaling happens without downtime or failover. If a
  Node cannot accommodate the new resources (the resize is reported `Infeasible`), the operator
  automatically falls back to the `Restart` behavior for that Pod. For a **distributed** `MariaDB`
  deployment, in-place resize is not possible, so `InPlace` automatically degrades to `Restart`.

If `spec.verticalScaling.mode` is omitted, it defaults to `Restart`.

> **Note:** `InPlace` mode relies on the Kubernetes `InPlacePodVerticalScaling` feature gate, which is
> enabled by default from Kubernetes v1.33. On older clusters, or when the feature gate is disabled,
> use `Restart` mode.

In the next docs, we are going to show a step by step guide on updating resources of MariaDB database using `MariaDBOpsRequest` CRD.

<!-- PAGE_START: backup/stash/logical/cluster.md -->
# Backup KubeDB managed MariaDB Cluster using Stash

Stash `v0.11.8+` supports backup and restoration of MariaDB databases. This guide will show you how you can take a logical backup of your MariaDB database cluster and restore them using Stash.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install KubeDB operator in your cluster from [here](https://kubedb.com/docs/latest/setup).
* Install Stash in your cluster following the steps [here](https://stash.run/docs/latest/setup/install/stash/).
* Install Stash `kubectl` plugin following the steps [here](https://stash.run/docs/latest/setup/install/kubectl-plugin/).
* If you are not familiar with how Stash backup and restore MariaDB databases, please check the following guide [here](en/backup/stash/overview.md).

You have to be familiar with following custom resources:

* [AppBinding](en/concepts/appbinding.md)
* [Function](https://stash.run/docs/latest/concepts/crds/function/)
* [Task](https://stash.run/docs/latest/concepts/crds/task/)
* [BackupConfiguration](https://stash.run/docs/latest/concepts/crds/backupconfiguration/)
* [BackupSession](https://stash.run/docs/latest/concepts/crds/backupsession/)
* [RestoreSession](https://stash.run/docs/latest/concepts/crds/restoresession/)

To keep things isolated, we are going to use a separate namespace called `demo` throughout this tutorial. Create `demo` namespace if you haven’t created it yet.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Prepare MariaDB

In this section, we are going to deploy a MariaDB database using KubeDB. Then, we are going to insert some sample data into it.

### Deploy MariaDB using KubeDB

At first, let’s deploy a MariaDB database named `sample-mariadb` of 3 replicas.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
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

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

This MariaDB object will create the necessary PetSet, Secret, Service etc for the database. You can easily view all the resources created by MariaDB object using [ketall](https://github.com/corneliusweig/ketall) `kubectl` plugin as below,

```bash
$ kubectl get-all -n demo -l app.kubernetes.io/instance=sample-mariadb
NAME                                                  NAMESPACE  AGE
endpoints/sample-mariadb                              demo       28m  
endpoints/sample-mariadb-pods                         demo       28m  
persistentvolumeclaim/data-sample-mariadb-0           demo       28m  
pod/sample-mariadb-0                                  demo       28m  
secret/sample-mariadb-auth                            demo       28m  
serviceaccount/sample-mariadb                         demo       28m  
service/sample-mariadb                                demo       28m  
service/sample-mariadb-pods                           demo       28m  
appbinding.appcatalog.appscode.com/sample-mariadb     demo       28m  
controllerrevision.apps/sample-mariadb-7b7f58b68f     demo       28m  
petset.apps/sample-mariadb                       demo       28m  
poddisruptionbudget.policy/sample-mariadb             demo       28m  
rolebinding.rbac.authorization.k8s.io/sample-mariadb  demo       28m  
role.rbac.authorization.k8s.io/sample-mariadb         demo       28m
```

Now, wait for 3 database pods to go into `Running` state,

```bash
$ kubectl get pod -n demo -l app.kubernetes.io/instance=sample-mariadb
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          2m7s
sample-mariadb-1   1/1     Running   0          101s
sample-mariadb-2   1/1     Running   0          81s
```

Once the database pod is in `Running` state, verify that all 3 nodes joined the cluster.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 26
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
1 row in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

From the above log, we can see that 3 nodes are ready to accept connections.

### Insert Sample Data

Now, we are going to exec into the database pod and create some sample data. The `sample-mariadb` object creates a secret containing the credentials of MariaDB and set them as pod’s Environment varibles `MYSQL_ROOT_USERNAME` and `MYSQL_ROOT_PASSWORD`.

Here, we are going to use the root user (`MYSQL_ROOT_USERNAME`) credential `MYSQL_ROOT_PASSWORD` to insert the sample data. Now, let’s exec into one of the pods and insert some sample data,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Let's create a database named "company"
MariaDB [(none)]>  create database company;
Query OK, 1 row affected (0.000 sec)

# Verify that the database has been created successfully
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Now, let's create a table called "employee" in the "company" table
MariaDB [(none)]> create table company.employees ( name varchar(50), salary int);
Query OK, 0 rows affected (0.018 sec)

# Verify that the table has been created successfully
MariaDB [(none)]> show tables in company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.007 sec)

# Now, let's insert a sample row in the table
MariaDB [(none)]> insert into company.employees values ('John Doe', 5000);
Query OK, 1 row affected (0.003 sec)

# Insert another sample row
MariaDB [(none)]> insert into company.employees values ('James William', 7000);
Query OK, 1 row affected (0.002 sec)

# Verify that the rows have been inserted into the table successfully
MariaDB [(none)]>  select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

We have successfully deployed a MariaDB database and inserted some sample data into it. In the subsequent sections, we are going to backup these data using Stash.

## Prepare for Backup

In this section, we are going to prepare the necessary resources (i.e. database connection information, backend information, etc.) before backup.

### Verify Stash MariaDB Addon Installed

When you install the Stash, it automatically installs all the official database addons. Verify that it has installed the MariaDB addons using the following command.

```bash
$ kubectl get tasks.stash.appscode.com | grep mariadb
mariadb-backup-11.8.5    35s
mariadb-restore-11.8.5   35s
```

### Ensure AppBinding

Stash needs to know how to connect with the database. An `AppBinding` exactly provides this information. It holds the Service and Secret information of the database. You have to point to the respective `AppBinding` as a target of backup instead of the database itself.

Stash expect your database Secret to have `username` and `password` keys. If your database secret does not have them, the `AppBinding` can also help here. You can specify a `secretTransforms` section with the mapping between the current keys and the desired keys.

You don’t need to worry about appbindings if you are using KubeDB. It creates an appbinding containing the necessary informations when you deploy the database. Let’s ensure the appbinding create by `KubeDB` operator.

```bash
$ kubectl get appbinding -n demo 
NAME             TYPE                 VERSION   AGE
sample-mariadb   kubedb.com/mariadb   11.8.5      62m
```

We have a appbinding named same as database name `sample-mariadb`. We will use this later for connecting into this database.

### Prepare Backend

We are going to store our backed up data into a GCS bucket. So, we need to create a Secret with GCS credentials and a `Repository` object with the bucket information. If you want to use a different backend, please read the respective backend configuration doc from [here](https://stash.run/docs/latest/guides/backends/overview/).

**Create Storage Secret:**

At first, let’s create a secret called `gcs-secret` with access credentials to our desired GCS bucket,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Create Repository:**

Now, crete a `Repository` object with the information of your desired bucket. Below is the YAML of `Repository` object we are going to create,

```yaml
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: gcs-repo
  namespace: demo
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: /demo/mariadb/sample-mariadb
    storageSecretName: gcs-secret
```

Let’s create the `Repository` we have shown above,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/repository.yaml
repository.stash.appscode.com/gcs-repo created
```

Now, we are ready to backup our database into our desired backend.

### Backup

To schedule a backup, we have to create a `BackupConfiguration` object targeting the respective `AppBinding` of our desired database. Then Stash will create a CronJob to periodically backup the database.

#### Create BackupConfiguration

Below is the YAML for `BackupConfiguration` object we are going to use to backup the `sample-mariadb` database we have deployed earlier,

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

Here,

* `.spec.schedule` specifies that we want to backup the database at 5 minutes intervals.
* `.spec.target.ref` refers to the AppBinding object that holds the connection information of our targeted database.

Let’s create the `BackupConfiguration` object we have shown above,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/backupconfiguration.yaml
backupconfiguration.stash.appscode.com/sample-mariadb-backup created
```

### Verify Backup Setup Successful

If everything goes well, the phase of the `BackupConfiguration` should be `Ready`. The `Ready` phase indicates that the backup setup is successful. Let’s verify the `Phase` of the BackupConfiguration,

```bash
$ kubectl get backupconfiguration -n demo
NAME                    TASK                    SCHEDULE      PAUSED   PHASE      AGE
sample-mariadb-backup   mariadb-backup-11.8.5   */5 * * * *            Ready      11s
```

#### Verify CronJob

Stash will create a CronJob with the schedule specified in `spec.schedule` field of `BackupConfiguration` object.

Verify that the CronJob has been created using the following command,

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        15s             17s
```

#### Wait for BackupSession

The `sample-mariadb-backup` CronJob will trigger a backup on each scheduled slot by creating a `BackupSession` object.

Now, wait for a schedule to appear. Run the following command to watch for a `BackupSession` object,

```bash
$ kubectl get backupsession -n demo -w
NAME                               INVOKER-TYPE          INVOKER-NAME            PHASE     AGE
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   24s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   75s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Succeeded   103s
```

Here, the phase `Succeeded` means that the backup process has been completed successfully.

#### Verify Backup

Now, we are going to verify whether the backed up data is present in the backend or not. Once a backup is completed, Stash will update the respective `Repository` object to reflect the backup completion. Check that the repository `gcs-repo` has been updated by the following command,

```bash
$ kubectl get repository -n demo gcs-repo
NAME       INTEGRITY   SIZE        SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
gcs-repo   true        1.327 MiB   1                60s                      8m
```

Now, if we navigate to the GCS bucket, we will see the backed up data has been stored in `demo/mariadb/sample-mariadb` directory as specified by `.spec.backend.gcs.prefix` field of the `Repository` object.

![Backup data in GCS Bucket](images/backup_stash_logical_cluster_sample-mariadb-backup.png)

Fig: Backup data in GCS Bucket

> Note: Stash keeps all the backed up data encrypted. So, data in the backend will not make any sense until they are decrypted.

## Restore MariaDB

If you have followed the previous sections properly, you should have a successful logical backup of your MariaDB database. Now, we are going to show how you can restore the database from the backed up data.

### Restore Into the Same Database

You can restore your data into the same database you have backed up from or into a different database in the same cluster or a different cluster. In this section, we are going to show you how to restore in the same database which may be necessary when you have accidentally deleted any data from the running database.

#### Temporarily Pause Backup

At first, let’s stop taking any further backup of the database so that no backup runs after we delete the sample data. We are going to pause the `BackupConfiguration` object. Stash will stop taking any further backup when the `BackupConfiguration` is paused.

Let’s pause the `sample-mariadb-backup` BackupConfiguration,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup --type="merge" --patch='{"spec": {"paused": true}}'
backupconfiguration.stash.appscode.com/sample-mariadb-backup patched
```

Or you can use Stash `kubectl` plugin to pause the BackupConfiguration,

```bash
$ kubectl stash pause backup -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been paused successfully.
```

Verify that the `BackupConfiguration` has been paused,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup  mariadb-backup-11.8.5   */5 * * * *   true     Ready   26m
```

Notice the `PAUSED` column. Value `true` for this field means that the `BackupConfiguration` has been paused.

Stash will also suspend the respective CronJob.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   True      0        2m59s           20m
```

#### Simulate Disaster

Now, let’s simulate an accidental deletion scenario. Here, we are going to exec into the database pod and delete the `company` database we had created earlier.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# View current databases
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Let's delete the "company" database
MariaDB [(none)]> drop database company;
Query OK, 1 row affected (0.268 sec)

# Verify that the "company" database has been deleted
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

#### Create RestoreSession

To restore the database, you have to create a `RestoreSession` object pointing to the `AppBinding` of the targeted database.

Here, is the YAML of the `RestoreSession` object that we are going to use for restoring our `sample-mariadb` database.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [latest]
```

Here,

* `.spec.repository.name` specifies the Repository object that holds the backend information where our backed up data has been stored.
* `.spec.target.ref` refers to the respective AppBinding of the `sample-mariadb` database.
* `.spec.rules` specifies that we are restoring data from the latest backup snapshot of the database.

Let’s create the `RestoreSession` object object we have shown above,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/cluster/examples/restoresession.yaml
restoresession.stash.appscode.com/sample-mariadb-restore created
```

Once, you have created the `RestoreSession` object, Stash will create a restore Job. Run the following command to watch the phase of the `RestoreSession` object,

```bash
$ kubectl get restoresession -n demo -w
NAME                     REPOSITORY   PHASE     AGE
sample-mariadb-restore   gcs-repo     Running   15s
sample-mariadb-restore   gcs-repo     Succeeded   18s
```

The `Succeeded` phase means that the restore process has been completed successfully.

#### Verify Restored Data

Now, let’s exec into the database pod and verify whether data actual data was restored or not,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Verify that the "company" database has been restored
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Verify that the tables of the "company" database have been restored
MariaDB [(none)]> show tables from company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.000 sec)

# Verify that the sample data of the "employees" table has been restored
MariaDB [(none)]> select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

Hence, we can see from the above output that the deleted data has been restored successfully from the backup.

#### Resume Backup

Since our data has been restored successfully we can now resume our usual backup process. Resume the `BackupConfiguration` using following command,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup --type="merge" --patch='{"spec": {"paused": false}}'
backupconfiguration.stash.appscode.com/sample-mariadb-backup patched
```

Or you can use the Stash `kubectl` plugin to resume the `BackupConfiguration`,

```bash
$ kubectl stash resume -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been resumed successfully.
```

Verify that the `BackupConfiguration` has been resumed,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                    TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup   mariadb-backup-11.8.5   */5 * * * *   false    Ready   29m
```

Here, `false` in the `PAUSED` column means the backup has been resume successfully. The CronJob also should be resumed now.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        2m59s           29m
```

Here, `False` in the `SUSPEND` column means the CronJob is no longer suspended and will trigger in the next schedule.

### Restore Into Different Database of the Same Namespace

If you want to restore the backed up data into a different database of the same namespace, you have to use the `AppBinding` of desired database. Then, you have to create the `RestoreSession` pointing to the new `AppBinding`.

### Restore Into Different Namespace

If you want to restore into a different namespace of the same cluster, you have to create the Repository, backend Secret in the desired namespace. You can use [Stash kubectl plugin](https://stash.run/docs/latest/guides/cli/kubectl-plugin/) to easily copy the resources into a new namespace. Then, you have to create the `RestoreSession` object in the desired namespace pointing to the Repository, AppBinding of that namespace.

### Restore Into Different Cluster

If you want to restore into a different cluster, you have to install Stash in the desired cluster. Then, you have to install Stash MariaDB addon in that cluster too. Then, you have to create the Repository, backend Secret, AppBinding, in the desired cluster. Finally, you have to create the `RestoreSession` object in the desired cluster pointing to the Repository, AppBinding of that cluster.

## Cleanup

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete -n demo backupconfiguration sample-mariadb-backup
kubectl delete -n demo restoresession sample-mariadb-restore
kubectl delete -n demo repository gcs-repo
# delete the database resources
kubectl delete ns demo
```

<!-- PAGE_START: backup/stash/logical/standalone.md -->
# Backup KubeDB Managed Standalone MariaDB using Stash

Stash `v0.11.8+` supports backup and restoration of MariaDB databases. This guide will show you how you can take a logical backup of your MariaDB databases and restore them using Stash.

## Before You Begin

* At first, you need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
* Install KubeDB operator in your cluster from [here](https://kubedb.com/docs/latest/setup).
* Install Stash in your cluster following the steps [here](https://stash.run/docs/latest/setup/install/stash/).
* Install Stash `kubectl` plugin following the steps [here](https://stash.run/docs/latest/setup/install/kubectl-plugin/).
* If you are not familiar with how Stash backup and restore MariaDB databases, please check the following guide [here](en/backup/stash/overview.md).

You have to be familiar with following custom resources:

* [AppBinding](https://kubedb.com/docs/v2026.7.10/guides/elasticsearch/concepts/appbinding/)
* [Function](https://stash.run/docs/latest/concepts/crds/function/)
* [Task](https://stash.run/docs/latest/concepts/crds/task/)
* [BackupConfiguration](https://stash.run/docs/latest/concepts/crds/backupconfiguration/)
* [BackupSession](https://stash.run/docs/latest/concepts/crds/backupsession/)
* [RestoreSession](https://stash.run/docs/latest/concepts/crds/restoresession/)

To keep things isolated, we are going to use a separate namespace called `demo` throughout this tutorial. Create `demo` namespace if you haven’t created it yet.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Prepare MariaDB

In this section, we are going to deploy a MariaDB database using KubeDB. Then, we are going to insert some sample data into it.

### Deploy MariaDB using KubeDB

At first, let’s deploy a MariaDB standalone database named `sample-mariadb using` [KubeDB](https://kubedb.com/).

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
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

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

This MariaDB objetc will create the necessary PetSet, Secret, Service etc. for the database. You can easily view all the resources created by MariaDB object using [ketall](https://github.com/corneliusweig/ketall) `kubectl` plugin as below,

```bash
$ kubectl get-all -n demo -l app.kubernetes.io/instance=sample-mariadb
NAME                                                  NAMESPACE  AGE
endpoints/sample-mariadb                              demo       28m  
endpoints/sample-mariadb-pods                         demo       28m  
persistentvolumeclaim/data-sample-mariadb-0           demo       28m  
pod/sample-mariadb-0                                  demo       28m  
secret/sample-mariadb-auth                            demo       28m  
serviceaccount/sample-mariadb                         demo       28m  
service/sample-mariadb                                demo       28m  
service/sample-mariadb-pods                           demo       28m  
appbinding.appcatalog.appscode.com/sample-mariadb     demo       28m  
controllerrevision.apps/sample-mariadb-7b7f58b68f     demo       28m  
petset.apps/sample-mariadb                       demo       28m  
poddisruptionbudget.policy/sample-mariadb             demo       28m  
rolebinding.rbac.authorization.k8s.io/sample-mariadb  demo       28m  
role.rbac.authorization.k8s.io/sample-mariadb         demo       28m
```

Now, wait for the database pod `sample-mariadb-0` to go into `Running` state,

```bash
$ kubectl get pod -n demo sample-mariadb-0
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          29m
```

Once the database pod is in `Running` state, verify that the database is ready to accept the connections.

```bash
$ kubectl logs -n demo sample-mariadb-0
2021-02-22  9:41:37 0 [Note] Reading of all Master_info entries succeeded
2021-02-22  9:41:37 0 [Note] Added new Master_info '' to hash table
2021-02-22  9:41:37 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

From the above log, we can see the database is ready to accept connections.

### Insert Sample Data

Now, we are going to exec into the database pod and create some sample data. The `sample-mariadb` object creates a secret containing the credentials of MariaDB and set them as pod’s Environment varibles `MYSQL_ROOT_USERNAME` and `MYSQL_ROOT_PASSWORD`.

Here, we are going to use the root user (`MYSQL_ROOT_USERNAME`) credential `MYSQL_ROOT_PASSWORD` to insert the sample data. Now, let’s exec into the database pod and insert some sample data,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Let's create a database named "company"
MariaDB [(none)]>  create database company;
Query OK, 1 row affected (0.000 sec)

# Verify that the database has been created successfully
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Now, let's create a table called "employee" in the "company" table
MariaDB [(none)]> create table company.employees ( name varchar(50), salary int);
Query OK, 0 rows affected (0.018 sec)

# Verify that the table has been created successfully
MariaDB [(none)]> show tables in company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.007 sec)

# Now, let's insert a sample row in the table
MariaDB [(none)]> insert into company.employees values ('John Doe', 5000);
Query OK, 1 row affected (0.003 sec)

# Insert another sample row
MariaDB [(none)]> insert into company.employees values ('James William', 7000);
Query OK, 1 row affected (0.002 sec)

# Verify that the rows have been inserted into the table successfully
MariaDB [(none)]>  select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.001 sec)

MariaDB [(none)]> exit
Bye
```

We have successfully deployed a MariaDB database and inserted some sample data into it. In the subsequent sections, we are going to backup these data using Stash.

## Prepare for Backup

In this section, we are going to prepare the necessary resources (i.e. database connection information, backend information, etc.) before backup.

### Verify Stash MariaDB Addon Installed

When you install the Stash, it automatically installs all the official database addons. Verify that it has installed the MariaDB addons using the following command.

```bash
$ kubectl get tasks.stash.appscode.com | grep mariadb
mariadb-backup-10.6.23    35s
mariadb-backup-10.6.23   35s
```

### Ensure AppBinding

Stash needs to know how to connect with the database. An `AppBinding` exactly provides this information. It holds the Service and Secret information of the database. You have to point to the respective `AppBinding` as a target of backup instead of the database itself.

Stash expect your database Secret to have `username` and `password` keys. If your database secret does not have them, the `AppBinding` can also help here. You can specify a `secretTransforms` section with the mapping between the current keys and the desired keys.

You don’t need to worry about appbindings if you are using KubeDB. It creates an appbinding containing the necessary informations when you deploy the database. Let’s ensure the appbinding create by `KubeDB` operator.

```bash
$ kubectl get appbinding -n demo 
NAME             TYPE                 VERSION   AGE
sample-mariadb   kubedb.com/mariadb   11.8.5      62m
```

We have a appbinding named same as database name `sample-mariadb`. We will use this later for connecting into this database.

### Prepare Backend

We are going to store our backed up data into a GCS bucket. So, we need to create a Secret with GCS credentials and a `Repository` object with the bucket information. If you want to use a different backend, please read the respective backend configuration doc from [here](https://stash.run/docs/latest/guides/backends/overview/).

**Create Storage Secret:**

At first, let’s create a secret called `gcs-secret` with access credentials to our desired GCS bucket,

```bash
$ echo -n 'changeit' > RESTIC_PASSWORD
$ echo -n '<your-project-id>' > GOOGLE_PROJECT_ID
$ cat downloaded-sa-key.json > GOOGLE_SERVICE_ACCOUNT_JSON_KEY
$ kubectl create secret generic -n demo gcs-secret \
    --from-file=./RESTIC_PASSWORD \
    --from-file=./GOOGLE_PROJECT_ID \
    --from-file=./GOOGLE_SERVICE_ACCOUNT_JSON_KEY
secret/gcs-secret created
```

**Create Repository:**

Now, crete a `Repository` object with the information of your desired bucket. Below is the YAML of `Repository` object we are going to create,

```yaml
apiVersion: stash.appscode.com/v1alpha1
kind: Repository
metadata:
  name: gcs-repo
  namespace: demo
spec:
  backend:
    gcs:
      bucket: stash-testing
      prefix: /demo/mariadb/sample-mariadb
    storageSecretName: gcs-secret
```

Let’s create the `Repository` we have shown above,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/repository.yaml
repository.stash.appscode.com/gcs-repo created
```

Now, we are ready to backup our database into our desired backend.

### Backup

To schedule a backup, we have to create a `BackupConfiguration` object targeting the respective `AppBinding` of our desired database. Then Stash will create a CronJob to periodically backup the database.

#### Create BackupConfiguration

Below is the YAML for `BackupConfiguration` object we are going to use to backup the `sample-mariadb` database we have deployed earlier,

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: BackupConfiguration
metadata:
  name: sample-mariadb-backup
  namespace: demo
spec:
  schedule: "*/5 * * * *"
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  retentionPolicy:
    name: keep-last-5
    keepLast: 5
    prune: true
```

Here,

* `.spec.schedule` specifies that we want to backup the database at 5 minutes intervals.
* `.spec.target.ref` refers to the AppBinding object that holds the connection information of our targeted database.

Let’s create the `BackupConfiguration` object we have shown above,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/backupconfiguration.yaml
backupconfiguration.stash.appscode.com/sample-mariadb-backup created
```

#### Verify Backup Setup Successful

If everything goes well, the phase of the `BackupConfiguration` should be `Ready`. The `Ready` phase indicates that the backup setup is successful. Let’s verify the `Phase` of the BackupConfiguration,

```bash
$ kubectl get backupconfiguration -n demo
NAME                    TASK                    SCHEDULE      PAUSED   PHASE      AGE
sample-mariadb-backup   mariadb-backup-10.6.23   */5 * * * *            Ready      11s
```

#### Verify CronJob

Stash will create a CronJob with the schedule specified in `spec.schedule` field of `BackupConfiguration` object.

Verify that the CronJob has been created using the following command,

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        15s             17s
```

#### Wait for BackupSession

The `sample-mariadb-backup` CronJob will trigger a backup on each scheduled slot by creating a `BackupSession` object.

Now, wait for a schedule to appear. Run the following command to watch for a `BackupSession` object,

```bash
$ kubectl get backupsession -n demo -w
NAME                               INVOKER-TYPE          INVOKER-NAME            PHASE     AGE
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   24s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Running   75s
sample-mariadb-backup-1606994706   BackupConfiguration   sample-mariadb-backup   Succeeded   103s
```

Here, the phase `Succeeded` means that the backup process has been completed successfully.

#### Verify Backup

Now, we are going to verify whether the backed up data is present in the backend or not. Once a backup is completed, Stash will update the respective `Repository` object to reflect the backup completion. Check that the repository `gcs-repo` has been updated by the following command,

```bash
$ kubectl get repository -n demo gcs-repo
NAME       INTEGRITY   SIZE        SNAPSHOT-COUNT   LAST-SUCCESSFUL-BACKUP   AGE
gcs-repo   true        1.327 MiB   1                60s                      8m
```

Now, if we navigate to the GCS bucket, we will see the backed up data has been stored in `demo/mariadb/sample-mariadb` directory as specified by `.spec.backend.gcs.prefix` field of the `Repository` object.

![Backup data in GCS Bucket](images/backup_stash_logical_standalone_sample-mariadb-backup.png)

Fig: Backup data in GCS Bucket

> Note: Stash keeps all the backed up data encrypted. So, data in the backend will not make any sense until they are decrypted.

## Restore MariaDB

If you have followed the previous sections properly, you should have a successful logical backup of your MariaDB database. Now, we are going to show how you can restore the database from the backed up data.

### Restore Into the Same Database

You can restore your data into the same database you have backed up from or into a different database in the same cluster or a different cluster. In this section, we are going to show you how to restore in the same database which may be necessary when you have accidentally deleted any data from the running database.

#### Temporarily Pause Backup

At first, let’s stop taking any further backup of the database so that no backup runs after we delete the sample data. We are going to pause the `BackupConfiguration` object. Stash will stop taking any further backup when the `BackupConfiguration` is paused.

Let’s pause the `sample-mariadb-backup` BackupConfiguration,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup--type="merge" --patch='{"spec": {"paused": true}}'
backupconfiguration.stash.appscode.com/sample-mgo-rs-backup patched
```

Or you can use the Stash `kubectl` plugin to pause the `BackupConfiguration`,

```bash
$ kubectl stash pause backup -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been paused successfully.
```

Verify that the `BackupConfiguration` has been paused,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                   TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup  mariadb-backup-10.6.23   */5 * * * *   true     Ready   26m
```

Notice the `PAUSED` column. Value `true` for this field means that the `BackupConfiguration` has been paused.

Stash will also suspend the respective CronJob.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   True      0        2m59s           20m
```

#### Simulate Disaster

Now, let’s simulate an accidental deletion scenario. Here, we are going to exec into the database pod and delete the `company` database we had created earlier.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# View current databases
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Let's delete the "company" database
MariaDB [(none)]> drop database company;
Query OK, 1 row affected (0.268 sec)

# Verify that the "company" database has been deleted
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

#### Create RestoreSession

To restore the database, you have to create a `RestoreSession` object pointing to the `AppBinding` of the targeted database.

Here, is the YAML of the `RestoreSession` object that we are going to use for restoring our `sample-mariadb` database.

```yaml
apiVersion: stash.appscode.com/v1beta1
kind: RestoreSession
metadata:
  name: sample-mariadb-restore
  namespace: demo
spec:
  task:
    name: mariadb-backup-10.6.23
  repository:
    name: gcs-repo
  target:
    ref:
      apiVersion: appcatalog.appscode.com/v1alpha1
      kind: AppBinding
      name: sample-mariadb
  rules:
  - snapshots: [latest]
```

Here,

* `.spec.task.name` specifies the name of the Task object that specifies the necessary Functions and their execution order to restore a MariaDB database.
* `.spec.repository.name` specifies the Repository object that holds the backend information where our backed up data has been stored.
* `.spec.target.ref` refers to the respective AppBinding of the `sample-mariadb` database.
* `.spec.rules` specifies that we are restoring data from the latest backup snapshot of the database.

Let’s create the `RestoreSession` object object we have shown above,

```bash
$ kubectl apply -f https://github.com/logical/docs/raw/v2026.7.10/docs/guides/mariadb/backup/logical/standalone/examples/restoresession.yaml
restoresession.stash.appscode.com/sample-mariadb-restore created
```

Once, you have created the `RestoreSession` object, Stash will create a restore Job. Run the following command to watch the phase of the `RestoreSession` object,

```bash
$ kubectl get restoresession -n demo -w
NAME                     REPOSITORY   PHASE     AGE
sample-mariadb-restore   gcs-repo     Running   15s
sample-mariadb-restore   gcs-repo     Succeeded   18s
```

The `Succeeded` phase means that the restore process has been completed successfully.

#### Verify Restored Data

Now, let’s exec into the database pod and verify whether data actual data was restored or not,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Verify that the "company" database has been restored
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Verify that the tables of the "company" database have been restored
MariaDB [(none)]> show tables from company;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.000 sec)

# Verify that the sample data of the "employees" table has been restored
MariaDB [(none)]> select * from company.employees;
+---------------+--------+
| name          | salary |
+---------------+--------+
| John Doe      |   5000 |
| James William |   7000 |
+---------------+--------+
2 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
```

Hence, we can see from the above output that the deleted data has been restored successfully from the backup.

#### Resume Backup

Since our data has been restored successfully we can now resume our usual backup process. Resume the `BackupConfiguration` using following command,

```bash
$ kubectl patch backupconfiguration -n demo sample-mariadb-backup --type="merge" --patch='{"spec": {"paused": false}}'
backupconfiguration.stash.appscode.com/sample-mariadb-backup patched
```

Or you can use the Stash `kubectl` plugin to resume the `BackupConfiguration`,

```bash
$ kubectl stash resume -n demo --backupconfig=sample-mariadb-backup
BackupConfiguration demo/sample-mariadb-backup has been resumed successfully.
```

Verify that the `BackupConfiguration` has been resumed,

```bash
$ kubectl get backupconfiguration -n demo sample-mariadb-backup
NAME                    TASK                    SCHEDULE      PAUSED   PHASE   AGE
sample-mariadb-backup   mariadb-backup-10.6.23   */5 * * * *   false    Ready   29m
```

Here, `false` in the `PAUSED` column means the backup has been resume successfully. The CronJob also should be resumed now.

```bash
$ kubectl get cronjob -n demo
NAME                                 SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
stash-backup-sample-mariadb-backup   */5 * * * *   False     0        2m59s           29m
```

Here, `False` in the `SUSPEND` column means the CronJob is no longer suspended and will trigger in the next schedule.

### Restore Into Different Database of the Same Namespace

If you want to restore the backed up data into a different database of the same namespace, you have to use the `AppBinding` of desired database. Then, you have to create the `RestoreSession` pointing to the new `AppBinding`.

### Restore Into Different Namespace

If you want to restore into a different namespace of the same cluster, you have to create the Repository, backend Secret in the desired namespace. You can use [Stash kubectl plugin](https://stash.run/docs/latest/guides/cli/kubectl-plugin/) to easily copy the resources into a new namespace. Then, you have to create the `RestoreSession` object in the desired namespace pointing to the Repository, AppBinding of that namespace.

### Restore Into Different Cluster

If you want to restore into a different cluster, you have to install Stash in the desired cluster. Then, you have to install Stash MariaDB addon in that cluster too. Then, you have to create the Repository, backend Secret, AppBinding, in the desired cluster. Finally, you have to create the `RestoreSession` object in the desired cluster pointing to the Repository, AppBinding of that cluster.

## Cleanup

To cleanup the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete -n demo backupconfiguration sample-mariadb-backup
kubectl delete -n demo restoresession sample-mariadb-restore
kubectl delete -n demo repository gcs-repo
# delete the database resources
kubectl delete ns demo
```

<!-- PAGE_START: distributed/autoscaler/compute/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Autoscaling the Compute Resource of a Distributed MariaDB Cluster

This guide will show you how to use `KubeDB` to autoscale compute resources i.e. cpu and memory of a distributed MariaDB Galera cluster deployed across multiple Kubernetes clusters.

## Before You Begin

* At first, you need to have a multi-cluster Kubernetes setup with OCM and KubeSlice configured. Follow the [Distributed MariaDB Overview](en/distributed/overview.md) guide to set up the required infrastructure.
* Install `KubeDB` Community, Ops-Manager and Autoscaler operator in your hub cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README). Make sure to enable OCM support:

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* Install `Metrics Server` from [here](https://github.com/kubernetes-sigs/metrics-server#installation)
* Install Prometheus in each spoke cluster. The autoscaler queries the per-cluster Prometheus endpoint (configured in the `PlacementPolicy`) to collect resource usage metrics. You can install it from [here](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Distributed MariaDB Compute Autoscaling Overview](en/distributed/autoscaler/compute/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Autoscaling of Distributed Cluster Database

Here, we are going to deploy a distributed `MariaDB` Galera cluster using a supported version by `KubeDB` operator. Then we are going to apply `MariaDBAutoscaler` to set up autoscaling.

### Deploy PlacementPolicy

Below is the YAML of the `PlacementPolicy` that we are going to create. It distributes 3 replicas across two clusters:

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        replicaIndices:
          - 0
          - 2
      - clusterName: demo-worker
        replicaIndices:
          - 1
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Here,

* `spec.clusterSpreadConstraint.distributionRules[].replicaIndices` specifies which MariaDB replica indices are scheduled on that cluster. Here `demo-controller` hosts replicas `0` and `2`, and `demo-worker` hosts replica `1`.

Apply the `PlacementPolicy` on the hub (`demo-controller`) cluster:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/compute/cluster/examples/placement-policy.yaml --context demo-controller
placementpolicy.apps.k8s.appscode.com/distributed-mariadb created
```

### Deploy Distributed MariaDB Cluster

In this section, we are going to deploy a distributed MariaDB Galera cluster with version `12.1.2`. Then, in the next section we will set up autoscaling for this database using `MariaDBAutoscaler` CRD.

Below is the YAML of the `MariaDB` CR that we are going to create. Note that `spec.distributed` is set to `true` and the `PlacementPolicy` is referenced via `spec.podTemplate.spec.podPlacementPolicy`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  distributed: true
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
      containers:
      - name: mariadb
        resources:
          requests:
            cpu: "200m"
            memory: "300Mi"
          limits:
            cpu: "200m"
            memory: "300Mi"
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CRO we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/compute/cluster/examples/sample-mariadb.yaml --context demo-controller
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo --context demo-controller
NAME             VERSION   STATUS   AGE
sample-mariadb   11.5.2   Ready    14m
```

The pods are distributed across clusters as defined by the `PlacementPolicy`:

```bash
$ kubectl get pod -n demo --context demo-controller
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   3/3     Running   0          14m
sample-mariadb-2   3/3     Running   0          14m

$ kubectl get pod -n demo --context demo-worker
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-1   3/3     Running   0          14m
```

Let’s check the Pod containers resources,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json --context demo-worker | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

Let’s check the MariaDB resources,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o json --context demo-controller | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "200m",
    "memory": "300Mi"
  },
  "requests": {
    "cpu": "200m",
    "memory": "300Mi"
  }
}
```

You can see from the above outputs that the resources are same as the one we have assigned while deploying the mariadb.

We are now ready to apply the `MariaDBAutoscaler` CRO to set up autoscaling for this database.

### Compute Resource Autoscaling

Here, we are going to set up compute resource autoscaling using a MariaDBAutoscaler Object.

#### Create MariaDBAutoscaler Object

In order to set up compute resource autoscaling for this distributed database cluster, we have to create a `MariaDBAutoscaler` CRO with our desired configuration. Below is the YAML of the `MariaDBAutoscaler` object that we are going to create,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-compute
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  opsRequestOptions:
    timeout: 3m
    apply: IfReady
  compute:
    mariadb:
      trigger: "On"
      podLifeTimeThreshold: 5m
      resourceDiffPercentage: 20
      minAllowed:
        cpu: 250m
        memory: 400Mi
      maxAllowed:
        cpu: 1
        memory: 1Gi
      containerControlledValues: "RequestsAndLimits"
      controlledResources: ["cpu", "memory"]
```

Here,

* `spec.databaseRef.name` specifies that we are performing compute resource scaling operation on `sample-mariadb` database.
* `spec.compute.mariadb.trigger` specifies that compute autoscaling is enabled for this database.
* `spec.compute.mariadb.podLifeTimeThreshold` specifies the minimum lifetime for at least one of the pod to initiate a vertical scaling.
* `spec.compute.mariadb.resourceDiffPercentage` specifies the minimum resource difference in percentage. The default is 10%.
  If the difference between current & recommended resource is less than ResourceDiffPercentage, Autoscaler Operator will ignore the updating.
* `spec.compute.mariadb.minAllowed` specifies the minimum allowed resources for the database.
* `spec.compute.mariadb.maxAllowed` specifies the maximum allowed resources for the database.
* `spec.compute.mariadb.controlledResources` specifies the resources that are controlled by the autoscaler.
* `spec.compute.mariadb.containerControlledValues` specifies which resource values should be controlled. The default is “RequestsAndLimits”.
* `spec.opsRequestOptions.apply` has two supported value : `IfReady` & `Always`.
  Use `IfReady` if you want to process the opsReq only when the database is Ready. And use `Always` if you want to process the execution of opsReq irrespective of the Database state.
* `spec.opsRequestOptions.timeout` specifies the maximum time for each step of the opsRequest(in seconds).
  If a step doesn’t finish within the specified timeout, the ops request will result in failure.

> **Note:** The autoscaler collects resource metrics for each pod by querying the Prometheus endpoint of the spoke cluster where that pod is scheduled, as configured in the `PlacementPolicy`.

Let’s create the `MariaDBAutoscaler` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/compute/cluster/examples/mdas-compute.yaml --context demo-controller
mariadbautoscaler.autoscaling.kubedb.com/md-as-compute created
```

#### Verify Autoscaling is set up successfully

Let’s check that the `mariadbautoscaler` resource is created successfully,

```bash
$ kubectl get mariadbautoscaler -n demo --context demo-controller
NAME            AGE
md-as-compute   5m56s

$ kubectl describe mariadbautoscaler md-as-compute -n demo --context demo-controller
Name:         md-as-compute
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-09-16T11:26:58Z
  Generation:          1
  ...
Spec:
  Compute:
    Mariadb:
      Container Controlled Values:  RequestsAndLimits
      Controlled Resources:
        cpu
        memory
      Max Allowed:
        Cpu:     1
        Memory:  1Gi
      Min Allowed:
        Cpu:                     250m
        Memory:                  400Mi
      Pod Life Time Threshold:   5m0s
      Resource Diff Percentage:  20
      Trigger:                   On
  Database Ref:
    Name:  sample-mariadb
  Ops Request Options:
    Apply:    IfReady
    Timeout:  3m0s
Status:
  Checkpoints:
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              46
        Weight:             555
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Bucket Weights:
        Index:              1
        Weight:             10000
      Reference Timestamp:  2022-09-17T00:00:00Z
      Total Weight:         1.391848625060675
    Ref:
      Container Name:     md-coordinator
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
    Cpu Histogram:
      Bucket Weights:
        Index:              0
        Weight:             10000
        Index:              3
        Weight:             556
      Reference Timestamp:  2022-09-16T00:00:00Z
      Total Weight:         2.648440345821337
    First Sample Start:     2022-09-16T11:26:48Z
    Last Sample Start:      2022-09-16T11:32:52Z
    Last Update Time:       2022-09-16T11:33:02Z
    Memory Histogram:
      Reference Timestamp:  2022-09-17T00:00:00Z
    Ref:
      Container Name:     mariadb
      Vpa Object Name:    sample-mariadb
    Total Samples Count:  19
    Version:              v3
  Conditions:
    Last Transition Time:  2022-09-16T11:27:07Z
    Message:               Successfully created mariaDBOpsRequest demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                CreateOpsRequest
    Status:                True
    Type:                  CreateOpsRequest
  Vpas:
    Conditions:
      Last Transition Time:  2022-09-16T11:27:02Z
      Status:                True
      Type:                  RecommendationProvided
    Recommendation:
      Container Recommendations:
        Container Name:  mariadb
        Lower Bound:
          Cpu:     250m
          Memory:  400Mi
        Target:
          Cpu:     250m
          Memory:  400Mi
        Uncapped Target:
          Cpu:     25m
          Memory:  262144k
        Upper Bound:
          Cpu:     1
          Memory:  1Gi
    Vpa Name:      sample-mariadb
Events:            <none>
```

So, the `mariadbautoscaler` resource is created successfully.

We can verify from the above output that `status.vpas` contains the `RecommendationProvided` condition to true. And in the same time, `status.vpas.recommendation.containerRecommendations` contain the actual generated recommendation.

Our autoscaler operator continuously watches the recommendation generated and creates an `mariadbopsrequest` based on the recommendations, if the database pod resources are needed to scaled up or down.

Let’s watch the `mariadbopsrequest` in the demo namespace to see if any `mariadbopsrequest` object is created. After some time you’ll see that a `mariadbopsrequest` will be created based on the recommendation.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                          TYPE              STATUS       AGE
mdops-sample-mariadb-6xc1kc   VerticalScaling   Progressing  7s
```

Let’s wait for the ops request to become successful.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                              TYPE              STATUS       AGE
mdops-vpa-sample-mariadb-z43wc8   VerticalScaling   Successful   3m32s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to scale the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mdops-vpa-sample-mariadb-z43wc8 --context demo-controller
Name:         mdops-sample-mariadb-6xc1kc
Namespace:    demo
...
Spec:
  Apply:  IfReady
  Database Ref:
    Name:   sample-mariadb
  Timeout:  2m0s
  Type:     VerticalScaling
  Vertical Scaling:
    Mariadb:
      Limits:
        Cpu:     250m
        Memory:  400Mi
      Requests:
        Cpu:     250m
        Memory:  400Mi
Status:
  Conditions:
    ...
    Last Transition Time:  2022-09-16T11:30:47Z
    Message:               Vertical scale successful for MariaDBOpsRequest: demo/mdops-sample-mariadb-6xc1kc
    Observed Generation:   1
    Reason:                SuccessfullyPerformedVerticalScaling
    Status:                True
    Type:                  VerticalScaling
    ...
  Phase:  Successful
```

Now, we are going to verify from the Pod, and the MariaDB yaml whether the resources of the distributed cluster database has updated to meet up the desired state, Let’s check,

```bash
$ kubectl get pod -n demo sample-mariadb-0 -o json --context demo-worker | jq '.spec.containers[].resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}

$ kubectl get mariadb -n demo sample-mariadb -o json --context demo-controller | jq '.spec.podTemplate.spec.containers[] | select(.name == "mariadb") | .resources'
{
  "limits": {
    "cpu": "250m",
    "memory": "400Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "400Mi"
  }
}
```

The above output verifies that we have successfully autoscaled the resources of the distributed MariaDB cluster.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete mariadb -n demo sample-mariadb --context demo-controller
kubectl delete mariadbautoscaler -n demo md-as-compute --context demo-controller
kubectl delete placementpolicy distributed-mariadb --context demo-controller
kubectl delete ns demo --context demo-controller
kubectl delete ns demo --context demo-worker
```

<!-- PAGE_START: distributed/autoscaler/compute/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Distributed MariaDB Compute Resource Autoscaling

This guide will give an overview on how KubeDB Autoscaler operator autoscales the compute resources i.e. cpu and memory of a **distributed** MariaDB cluster using `mariadbautoscaler` crd.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Distributed MariaDB Overview](en/distributed/overview.md)

## How Compute Autoscaling Works

The following diagram shows how KubeDB Autoscaler operator autoscales the resources of `MariaDB` database components. Open the image in a new tab to see the enlarged version.

![Auto Scaling process of MariaDB](images/distributed_autoscaler_compute_overview_mdas-compute.png)

Fig: Auto Scaling process of MariaDB

The Auto Scaling process consists of the following steps:

1. At first, the user creates a `PlacementPolicy` Custom Resource (CR) with `monitoring.prometheus.url` configured for each spoke cluster. This allows the autoscaler to scrape metrics from the Prometheus instance running in each spoke cluster.
2. The user creates a `MariaDB` Custom Resource Object (CRO) with `spec.distributed: true` and a reference to the `PlacementPolicy`.
3. `KubeDB` Community operator watches the `MariaDB` CRO.
4. When the operator finds a `MariaDB` CRO, it creates required number of `PetSets` and distributes them across spoke clusters as defined by the `PlacementPolicy`.
5. Then, in order to set up autoscaling of the CPU & Memory resources of the `MariaDB` database the user creates a `MariaDBAutoscaler` CRO with desired configuration.
6. `KubeDB` Autoscaler operator watches the `MariaDBAutoscaler` CRO.
7. `KubeDB` Autoscaler operator utilizes the modified version of Kubernetes official [VPA-Recommender](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/pkg) for different components of the database, as specified in the `mariadbautoscaler` CRO.
   It generates recommendations based on resource usages by querying Prometheus endpoints configured in the `PlacementPolicy`, & stores them in the `status` section of the autoscaler CRO.
8. If the generated recommendation doesn’t match the current resources of the database, then `KubeDB` Autoscaler operator creates a `MariaDBOpsRequest` CRO to scale the database to match the recommendation provided by the VPA object.
9. `KubeDB Ops-Manager operator` watches the `MariaDBOpsRequest` CRO.
10. Lastly, the `KubeDB Ops-Manager operator` will scale the database component vertically as specified on the `MariaDBOpsRequest` CRO.

> **Key Difference from Non-Distributed Autoscaling**: For distributed MariaDB, the `PlacementPolicy` must include a `monitoring.prometheus.url` for each spoke cluster’s `distributionRules` entry. The autoscaler uses these Prometheus endpoints to collect resource metrics from pods running across multiple Kubernetes clusters.

In the next docs, we are going to show a step by step guide on Autoscaling of Distributed MariaDB database using `MariaDBAutoscaler` CRD.

<!-- PAGE_START: distributed/autoscaler/storage/cluster.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Storage Autoscaling of a Distributed MariaDB Cluster

This guide will show you how to use `KubeDB` to autoscale the storage of a distributed MariaDB Galera cluster deployed across multiple Kubernetes clusters.

## Before You Begin

* At first, you need to have a multi-cluster Kubernetes setup with OCM and KubeSlice configured. Follow the [Distributed MariaDB Overview](en/distributed/overview.md) guide to set up the required infrastructure.
* Install `KubeDB` Community, Enterprise and Autoscaler operator in your hub cluster following the steps [here](https://kubedb.com/docs/v2026.7.10/setup/README). Make sure to enable OCM support:

  ```bash
  --set petset.features.ocm.enabled=true
  ```
* Install `Metrics Server` from [here](https://github.com/kubernetes-sigs/metrics-server#installation)
* Install Prometheus in each spoke cluster. The autoscaler queries the per-cluster Prometheus endpoint (configured in the `PlacementPolicy`) to collect storage usage metrics. You can install it from [here](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
* You must have a `StorageClass` that supports volume expansion in each spoke cluster.
* You should be familiar with the following `KubeDB` concepts:

  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Distributed MariaDB Storage Autoscaling Overview](en/distributed/autoscaler/storage/overview.md)

To keep everything isolated, we are going to use a separate namespace called `demo` throughout this tutorial.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Storage Autoscaling of Distributed Cluster Database

At first verify that your clusters have a storage class that supports volume expansion. First let’s check the storagclass of `Controler` cluster,

```bash
$ kubectl get storageclass --context demo-controller
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  4d
longhorn (default)     driver.longhorn.io      Delete          Immediate              true                   24h
longhorn-static        driver.longhorn.io      Delete          Immediate              true                   24h
```

Then check the storageclass of `Worker` cluster,

```bash
$ kubectl get storageclass --context demo-worker
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  4d
longhorn (default)     driver.longhorn.io      Delete          Immediate              true                   23h
longhorn-static        driver.longhorn.io      Delete          Immediate              true                   23h
```

We can see from the output the `longhorn (default)` and `longhorn-static` storage class has `ALLOWVOLUMEEXPANSION` field as true. So, this storage class supports volume expansion. We can use it. You can install `longhorn` from [here](https://longhorn.io/docs/1.11.2/deploy/install/)

### Deploy PlacementPolicy

For distributed `MariaDB` autoscaling, the PlacementPolicy must define a valid `monitoring.prometheus.url` for each spoke cluster. These endpoints are required by the autoscaler to collect metrics and monitor storage usage across all clusters where MariaDB pods are deployed.

Additionally, it is essential to explicitly specify the storage class for each cluster using `spec.clusterSpreadConstraint.distributionRules.storageClassName`. If this field is not provided, the system will fall back to the default storage class, which may lead to unintended behavior or potential data management risks in a distributed environment.

Below is the YAML of the `PlacementPolicy` that we are going to create. It distributes 3 replicas across two clusters and provides the Prometheus endpoint for each:

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        storageClassName: local-path
        monitoring:
          prometheus:
            url: http://prometheus-operated.monitoring.svc.cluster.local:9090
        replicaIndices:
          - 0
          - 2
      - clusterName: demo-worker
        storageClassName: local-path
        monitoring:
          prometheus:
            url: http://prometheus-operated.monitoring.svc.cluster.local:9090
        replicaIndices:
          - 1
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Here,

* `spec.clusterSpreadConstraint.distributionRules[].monitoring.prometheus.url` specifies the Prometheus endpoint for the corresponding spoke cluster. The autoscaler uses this URL to scrape storage usage metrics for pods running in that cluster.
* `spec.clusterSpreadConstraint.distributionRules[].replicaIndices` specifies which MariaDB replica indices are scheduled on that cluster. Here `demo-controller` hosts replicas `0` and `2`, and `demo-worker` hosts replica `1`.

Apply the `PlacementPolicy` on the hub (`demo-controller`) cluster:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/storage/cluster/examples/placement-policy.yaml --context demo-controller
placementpolicy.apps.k8s.appscode.com/distributed-mariadb created
```

> **Note:** Update the `monitoring.prometheus.url` values to match the actual Prometheus service endpoints in each of your spoke clusters.

### Deploy Distributed MariaDB Cluster

In this section, we are going to deploy a distributed MariaDB replicaset database with version `12.1.2`. Then, in the next section we will set up autoscaling for this database using `MariaDBAutoscaler` CRD.

Below is the YAML of the `MariaDB` CR that we are going to create. Note that `spec.distributed` is set to `true` and the `PlacementPolicy` is referenced via `spec.podTemplate.spec.podPlacementPolicy`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  distributed: true
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "topolvm-provisioner"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
  deletionPolicy: WipeOut
```

Let’s create the `MariaDB` CRO we have shown above,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/storage/cluster/examples/sample-mariadb.yaml --context demo-controller
mariadb.kubedb.com/sample-mariadb created
```

Now, wait until `sample-mariadb` has status `Ready`. i.e,

```bash
$ kubectl get mariadb -n demo --context demo-controller
NAME             VERSION   STATUS   AGE
sample-mariadb   11.5.2   Ready    3m46s
```

The pods are distributed across clusters as defined by the `PlacementPolicy`:

```bash
$ kubectl get pod -n demo --context demo-controller
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   3/3     Running   0          3m46s
sample-mariadb-2   3/3     Running   0          3m46s

$ kubectl get pod -n demo --context demo-worker
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-1   3/3     Running   0          3m46s
```

Let’s check volume size from petset, and from the persistent volume on `demo-worker`,

```bash
$ kubectl get petset -n demo sample-mariadb -o json --context demo-worker | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1Gi"

$ kubectl get pv -n demo --context demo-worker
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   1Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            57s
```

You can see the petset has 1GB storage, and the capacity of all the persistent volumes is also 1GB.

We are now ready to apply the `MariaDBAutoscaler` CRO to set up storage autoscaling for this database.

### Storage Autoscaling

Here, we are going to set up storage autoscaling using a MariaDBAutoscaler Object.

#### Create MariaDBAutoscaler Object

In order to set up vertical autoscaling for this distributed replicaset database, we have to create a `MariaDBAutoscaler` CRO with our desired configuration. Below is the YAML of the `MariaDBAutoscaler` object that we are going to create,

```yaml
apiVersion: autoscaling.kubedb.com/v1alpha1
kind: MariaDBAutoscaler
metadata:
  name: md-as-st
  namespace: demo
spec:
  databaseRef:
    name: sample-mariadb
  storage:
    mariadb:
      trigger: "On"
      usageThreshold: 20
      scalingThreshold: 20
      expansionMode: "Online"
```

Here,

* `spec.databaseRef.name` specifies that we are performing vertical scaling operation on `sample-mariadb` database.
* `spec.storage.mariadb.trigger` specifies that storage autoscaling is enabled for this database.
* `spec.storage.mariadb.usageThreshold` specifies storage usage threshold, if storage usage exceeds `20%` then storage autoscaling will be triggered. The autoscaler monitors storage usage by querying the Prometheus endpoint of the spoke cluster where each pod is running, as configured in the `PlacementPolicy`.
* `spec.storage.mariadb.scalingThreshold` specifies the scaling threshold. Storage will be scaled to `20%` of the current amount.
* `spec.storage.mariadb.expansionMode` specifies the expansion mode of volume expansion `MariaDBOpsRequest` created by `MariaDBAutoscaler`. topolvm-provisioner supports online volume expansion so here `expansionMode` is set as “Online”.

Let’s create the `MariaDBAutoscaler` CR we have shown above,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/distributed/autoscaler/storage/cluster/examples/mdas-storage.yaml --context demo-controller
mariadbautoscaler.autoscaling.kubedb.com/md-as-st created
```

#### Storage Autoscaling is set up successfully

Let’s check that the `mariadbautoscaler` resource is created successfully,

```bash
$ kubectl get mariadbautoscaler -n demo --context demo-controller
NAME           AGE
md-as-st   33s

$ kubectl describe mariadbautoscaler md-as-st -n demo --context demo-controller
Name:         md-as-st
Namespace:    demo
Labels:       <none>
Annotations:  API Version:  autoscaling.kubedb.com/v1alpha1
Kind:         MariaDBAutoscaler
Metadata:
  Creation Timestamp:  2022-01-14T06:08:02Z
  Generation:          1
  ...
  Resource Version:  24009
  UID:               4f45a3b3-fc72-4d04-b52c-a770944311f6
Spec:
  Database Ref:
    Name:  sample-mariadb
  Storage:
    Mariadb:
      Scaling Threshold:  20
      Trigger:            On
      Usage Threshold:    20
Events:                   <none>
```

So, the `mariadbautoscaler` resource is created successfully.

Now, for this demo, we are going to manually fill up the persistent volume to exceed the `usageThreshold` using `dd` command to see if storage autoscaling is working or not.

Let’s exec into a database pod on `demo-worker` and fill the database volume(`var/lib/mysql`) using the following commands:

```bash
$ kubectl exec -it -n demo sample-mariadb-0 --context demo-worker -- bash
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  357M  658M  36% /var/lib/mysql
root@sample-mariadb-0:/ dd if=/dev/zero of=/var/lib/mysql/file.img bs=500M count=1
1+0 records in
1+0 records out
524288000 bytes (524 MB, 500 MiB) copied, 0.340877 s, 1.5 GB/s
root@sample-mariadb-0:/ df -h /var/lib/mysql
Filesystem                                         Size  Used Avail Use% Mounted on
/dev/topolvm/57cd4330-784f-42c1-bf8e-e743241df164 1014M  857M  158M  85% /var/lib/mysql
```

So, from the above output we can see that the storage usage is 85%, which exceeded the `usageThreshold` 20%.

Let’s watch the `mariadbopsrequest` in the demo namespace to see if any `mariadbopsrequest` object is created. After some time you’ll see that a `mariadbopsrequest` of type `VolumeExpansion` will be created based on the `scalingThreshold`.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                         TYPE              STATUS        AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Progressing   15s
```

Let’s wait for the ops request to become successful.

```bash
$ kubectl get mariadbopsrequest -n demo --context demo-controller
NAME                         TYPE              STATUS       AGE
mops-sample-mariadb-xojkua   VolumeExpansion   Successful   97s
```

We can see from the above output that the `MariaDBOpsRequest` has succeeded. If we describe the `MariaDBOpsRequest` we will get an overview of the steps that were followed to expand the volume of the database.

```bash
$ kubectl describe mariadbopsrequest -n demo mops-sample-mariadb-xojkua --context demo-controller
Name:         mops-sample-mariadb-xojkua
Namespace:    demo
...
Spec:
  Database Ref:
    Name:  sample-mariadb
  Type:    VolumeExpansion
  Volume Expansion:
    Mariadb:  1594884096
Status:
  Conditions:
    ...
    Last Transition Time:  2022-01-14T06:14:25Z
    Message:               Volume Expansion performed successfully in MariaDB pod for MariaDBOpsRequest: demo/mops-sample-mariadb-xojkua
    Observed Generation:   1
    Reason:                SuccessfullyVolumeExpanded
    Status:                True
    Type:                  VolumeExpansion
    ...
  Phase:  Successful
```

Now, we are going to verify from the `Petset` and the `Persistent Volume` whether the volume of the distributed replicaset database has expanded to meet the desired state, Let’s check,

```bash
$ kubectl get petset -n demo sample-mariadb -o json --context demo-worker | jq '.spec.volumeClaimTemplates[].spec.resources.requests.storage'
"1594884096"
$ kubectl get pv -n demo --context demo-worker
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS          REASON   AGE
pvc-c27eee12-cd86-4410-b39e-b1dd735fc14d   2Gi        RWO            Delete           Bound    demo/data-sample-mariadb-1   topolvm-provisioner            23m
```

The above output verifies that we have successfully autoscaled the volume of the distributed MariaDB cluster.

## Cleaning Up

To clean up the Kubernetes resources created by this tutorial, run:

```bash
kubectl delete mariadb -n demo sample-mariadb --context demo-controller
kubectl delete mariadbautoscaler -n demo md-as-st --context demo-controller
kubectl delete placementpolicy distributed-mariadb --context demo-controller
kubectl delete ns demo --context demo-controller
kubectl delete ns demo --context demo-worker
```

<!-- PAGE_START: distributed/autoscaler/storage/overview.md -->
> New to KubeDB? Please start [here](https://kubedb.com/docs/v2026.7.10/README).

# Distributed MariaDB Storage Autoscaling

This guide will give an overview on how KubeDB Autoscaler operator autoscales the database storage of a **distributed** MariaDB cluster using `mariadbautoscaler` crd.

## Before You Begin

* You should be familiar with the following `KubeDB` concepts:
  + [MariaDB](en/concepts/mariadb.md)
  + [MariaDBAutoscaler](en/concepts/autoscaler.md)
  + [MariaDBOpsRequest](en/concepts/opsrequest.md)
  + [Distributed MariaDB Overview](en/distributed/overview.md)

## How Storage Autoscaling Works

The following diagram shows how KubeDB Autoscaler operator autoscales the resources of `MariaDB` database components. Open the image in a new tab to see the enlarged version.

![Storage Autoscaling process of MariaDB](images/distributed_autoscaler_storage_overview_mdas-storage.jpeg)

Fig: Storage Autoscaling process of MariaDB

The Auto Scaling process consists of the following steps:

1. At first, the user creates a `PlacementPolicy` Custom Resource (CR) with `monitoring.prometheus.url` configured for each spoke cluster. This allows the autoscaler to monitor storage usage across all clusters where MariaDB pods are running.
2. The user creates a `MariaDB` Custom Resource (CR) with `spec.distributed: true` and a reference to the `PlacementPolicy`.
3. `KubeDB` Community operator watches the `MariaDB` CR.
4. When the operator finds a `MariaDB` CR, it creates required number of `PetSets` and distributes them across spoke clusters as defined by the `PlacementPolicy`.
5. Each PetSet creates a Persistent Volume according to the Volume Claim Template provided in the petset configuration. This Persistent Volume will be expanded by the `KubeDB` Enterprise operator.
6. Then, in order to set up storage autoscaling of the `MariaDB` database the user creates a `MariaDBAutoscaler` CRO with desired configuration.
7. `KubeDB` Autoscaler operator watches the `MariaDBAutoscaler` CRO.
8. `KubeDB` Autoscaler operator continuously watches persistent volumes of the databases across all spoke clusters to check if storage usage exceeds the specified threshold. It queries the Prometheus endpoints configured per cluster in the `PlacementPolicy` to collect storage metrics.
9. If the usage exceeds the specified usage threshold, then `KubeDB` Autoscaler operator creates a `MariaDBOpsRequest` to expand the storage of the database.
10. `KubeDB` Enterprise operator watches the `MariaDBOpsRequest` CRO.
11. Then the `KubeDB` Enterprise operator will expand the storage of the database component as specified on the `MariaDBOpsRequest` CRO.

> **Key Difference from Non-Distributed Autoscaling**: For distributed MariaDB, the `PlacementPolicy` must include a `monitoring.prometheus.url` for each spoke cluster’s `distributionRules` entry. The autoscaler uses these Prometheus endpoints to collect storage usage metrics from pods running across multiple Kubernetes clusters.

In the next docs, we are going to show a step by step guide on Autoscaling storage of a Distributed MariaDB database using `MariaDBAutoscaler` CRD.
