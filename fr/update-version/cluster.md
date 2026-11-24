> Vous débutez avec KubeDB ? Commencez [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mettre à jour la version d'un cluster MariaDB

Ce guide montre comment utiliser l'opérateur KubeDB Enterprise pour mettre à jour la version d'un cluster `MariaDB`.

## Avant de commencer

* Vous devez disposer d'un cluster Kubernetes et de l'outil en ligne de commande `kubectl` configuré pour communiquer avec lui. Si vous n'avez pas encore de cluster, créez-en un avec [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../concepts/mariadb.md)
  + [Cluster](../clustering/overview.md)
  + [MariaDBOpsRequest](../concepts/opsrequest.md)
  + [Mise à jour de l'aperçu](overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Préparer le cluster MariaDB

Maintenant, nous allons déployer un `MariaDB` base de données cluster avec version `11.8.5`.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer un cluster MariaDB. Ensuite, dans la section suivante, nous mettrons à jour la version de la base de données en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

> Pour mettre à jour une instance `MariaDB` autonome (`Standalone`), supprimez simplement `spec.replicas` du manifeste YAML ci-dessous ; les autres étapes restent identiques.

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

* `spec.databaseRef.name` indique que l'opération porte sur la base de données MariaDB `sample-mariadb`.
* `spec.type` précise que nous allons effectuer `UpdateVersion` sur notre base de données.
* `spec.updateVersion.targetVersion` spécifie la version attendue de la base de données `12.1.2`.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/update-version/cluster/examples/mdops-update.yaml
mariadbopsrequest.ops.kubedb.com/mdops-update created
```

#### Vérifiez la version de MariaDB mise à jour avec succès

Si tout se déroule correctement, l'opérateur KubeDB Enterprise met à jour l'image de l'objet `MariaDB` ainsi que des objets `PetSet` et `Pod` associés.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME              TYPE            STATUS       AGE
mdops-update      UpdateVersion   Successful    84s
```

La sortie ci-dessus confirme que la ressource `MariaDBOpsRequest` a réussi.

Vérifions maintenant que la ressource `MariaDB`, le `PetSet` associé et ses `Pods` utilisent bien l'image de la nouvelle version :

```bash
$ kubectl get mariadb -n demo sample-mariadb -o=jsonpath='{.spec.version}{"\n"}'
12.1.2

$ kubectl get petset -n demo sample-mariadb -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
mariadb:12.1.2

$ kubectl get pods -n demo sample-mariadb-0 -o=jsonpath='{.spec.containers[0].image}{"\n"}'
mariadb:12.1.2
```

La sortie ci-dessus confirme que le cluster `MariaDB` utilise désormais la nouvelle version et que la mise à jour est terminée.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées dans ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-update
```