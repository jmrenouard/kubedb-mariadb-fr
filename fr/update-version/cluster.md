> Vous êtes nouveau sur KubeDB ? Veuillez commencer [here](https://kubedb.com/docs/v2026.7.10/README).

# version de mise à jour du cluster MariaDB

This guide will show you how to use `KubeDB` Enterprise operator to update the version of `MariaDB` Cluster.

## Before You Begin

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` command-line tool must be configured to communicate with your cluster. If you do not already have a cluster, you can create one by using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [here](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../concepts/mariadb.md)
  + [Cluster](../clustering/overview.md)
  + [MariaDBOpsDemande](../concepts/opsrequest.md)
  + [Mise à jour de l'aperçu](overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Prepare MariaDB Cluster

Maintenant, nous allons déployer un `MariaDB` base de données cluster avec version `11.8.5`.

### Deploy MariaDB cluster

Dans cette section, nous allons déployer un cluster MariaDB. Ensuite, dans la section suivante, nous mettrons à jour la version de la base de données en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

> If you want to update `MariaDB Standalone`, Just remove the `spec.Replicas` à partir du yaml ci-dessous et le reste des étapes sont les mêmes.

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

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/update-version/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attends `sample-mariadb` créé a le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo                                                                                                                                             
NAME             VERSION    STATUS     AGE
sample-mariadb   11.8.5    Ready     3m15s
```

We are now ready to apply the `MariaDBOpsRequest` CR pour mettre à jour cette base de données.

### mettre à jour la version de MariaDB

Ici, nous allons mettre à jour `MariaDB` cluster de `11.8.5` à `12.1.2`.

#### Créez une demande MariaDBOps :

Afin de mettre à jour le cluster de base de données, nous devons créer un `MariaDBOpsRequest` CR avec la version souhaitée prise en charge par `KubeDB`. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

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

Ici,

* `spec.databaseRef.name` specifies that we are performing operation on `sample-mariadb` MariaDB database.
* `spec.type` précise que nous allons effectuer `UpdateVersion` sur notre base de données.
* `spec.updateVersion.targetVersion` spécifie la version attendue de la base de données `12.1.2`.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/update-version/cluster/examples/mdops-update.yaml
mariadbopsrequest.ops.kubedb.com/mdops-update created
```

#### Vérifiez la version de MariaDB mise à jour avec succès

If everything goes well, `KubeDB` Enterprise operator will update the image of `MariaDB` objet et associé `PetSets` and `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME              TYPE            STATUS       AGE
mdops-update      UpdateVersion   Successful    84s
```

We can see from the above output that the `MariaDBOpsRequest` a réussi.

Now, we are going to verify whether the `MariaDB` et le connexe `PetSets` and their `Pods` avoir l'image de la nouvelle version. Vérifions,

```bash
$ kubectl get mariadb -n demo sample-mariadb -o=jsonpath='{.spec.version}{"\n"}'
12.1.2

$ kubectl get petset -n demo sample-mariadb -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
mariadb:12.1.2

$ kubectl get pods -n demo sample-mariadb-0 -o=jsonpath='{.spec.containers[0].image}{"\n"}'
mariadb:12.1.2
```

You can see from above, our `MariaDB` cluster database has been updated with the new version. So, the update process is successfully completed.

## Nettoyage

To clean up the Kubernetes resources created by this tutorial, run:

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-update
```