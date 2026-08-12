> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Déployer MariaDB à partir du registre Docker privé

L’opérateur KubeDB prend en charge l’utilisation du registre Docker privé. Ce didacticiel vous montrera comment utiliser KubeDB pour exécuter la base de données MariaDB à l'aide d'images Docker privées.

## Avant de commencer

* Lire [concept du catalogue de versions MariaDB](../concepts/mariadb-version.md) pour apprendre les concepts détaillés de `MariaDBVersion` objet.
* Vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Vous aurez également besoin d'un docker privé [enregistrement](https://docs.docker.com/registry/) ou [dépôt privé](https://docs.docker.com/docker-hub/repos/#private-repositories). Dans ce tutoriel, nous utiliserons un référentiel privé de [hub de docker](https://hub.docker.com/).
* Vous devez pousser les images requises depuis KubeDB [Compte Docker Hub](https://hub.docker.com/u/kubedb) dans votre registre privé. Pour MariaDB, appuyez sur `DB_IMAGE`, `EXPORTER_IMAGE`, `INITCONTAINER_IMAGE` des versions MariaDB suivantes, où `deprecated` n'est pas vrai, à votre registre privé.

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

Dépôts du hub Docker :

* [kubedb/opérateur](https://hub.docker.com/r/kubedb/operator)
* [kubedb/mariadb](https://hub.docker.com/r/kubedb/mariadb)
* [kubedb/mysqld-exportateur](https://hub.docker.com/r/kubedb/mysqld-exporter)

  + Mettez à jour le catalogue KubeDB pour le registre Docker privé. Ex:

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
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel. Exécutez la commande suivante pour préparer votre cluster pour ce didacticiel :

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Créer ImagePullSecret

ImagePullSecrets est un type de secret Kubernete dont le seul objectif est d'extraire des images privées d'un registre Docker. Il vous permet de spécifier l'URL du registre Docker, les informations d'identification pour vous connecter et le nom de votre image Docker privée.

Exécutez la commande suivante, en remplaçant les valeurs majuscules appropriées pour créer un secret d'extraction d'image pour votre registre Docker privé :

```bash
$ kubectl create secret docker-registry -n demo myregistrykey \
  --docker-server=DOCKER_REGISTRY_SERVER \
  --docker-username=DOCKER_USER \
  --docker-email=DOCKER_EMAIL \
  --docker-password=DOCKER_PASSWORD
secret/myregistrykey created
```

Si vous souhaitez suivre d'autres méthodes pour extraire des images privées, consultez [documents officiels](https://kubernetes.io/docs/concepts/containers/images/) de Kubernetes.

NB : Si vous utilisez `kubectl` 1.9.0, mettez à jour vers 1.9.1 ou version ultérieure pour éviter cela [problème](https://github.com/kubernetes/kubernetes/issues/57427).

## Installer l'opérateur KubeDB

Lors de l'installation de l'opérateur KubeDB, définissez les indicateurs `--docker-registry` et `--image-pull-secret` à une valeur appropriée. Suivez les étapes pour [installer l'opérateur KubeDB](https://kubedb.com/docs/v2026.7.10/setup/README) correctement dans le cluster afin qu'il pointe vers le DOCKER\_REGISTRY à partir duquel vous souhaitez extraire des images.

## Déployer la base de données MariaDB à partir du registre privé

Lors du déploiement `MariaDB` à partir du référentiel privé, vous devez ajouter `myregistrykey` secret dans `MariaDB` `spec.imagePullSecrets`.
Vous trouverez ci-dessous l'objet MariaDB CRD que nous allons créer.

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

Maintenant, exécutez la commande pour déployer ceci `MariaDB` objet:

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/private-registry/quickstart/examples/demo.yaml
mariadb.kubedb.com/md-pvt-reg created
```

Pour vérifier si les images ont été extraites avec succès du référentiel, vérifiez si le `MariaDB` est en état de fonctionnement :

```bash
$ kubectl get pods -n demo
NAME              READY     STATUS    RESTARTS   AGE
md-pvt-reg-0   1/1       Running   0          56s
```

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo md-pvt-reg
mariadb.kubedb.com "md-pvt-reg" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```