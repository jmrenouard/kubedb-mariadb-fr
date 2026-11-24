> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Cluster MariaDB à échelle verticale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur d'entreprise pour mettre à jour les ressources d'une base de données de cluster MariaDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` Opérateur Communauté et Entreprise dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../../concepts/mariadb.md)
  + [Regroupement](../../clustering/galera-cluster.md)
  + [MariaDBOpsRequest](../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle verticale](overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Appliquer une mise à l'échelle verticale sur le cluster

Ici, nous allons déployer un `MariaDB` cluster utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons lui appliquer une mise à l’échelle verticale.

### Préparer le cluster MariaDB

Maintenant, nous allons déployer un `MariaDB` base de données cluster avec version `12.1.2`.

> Mise à l'échelle verticale pour `MariaDB Standalone` peut être effectué de la même manière que `MariaDB Cluster`. Retirez uniquement le `spec.replicas` champ du yaml ci-dessous pour déployer un MariaDB Standalone.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer une base de données de cluster MariaDB. Ensuite, dans la section suivante, nous mettrons à jour les ressources de la base de données en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

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

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Attendez maintenant que `sample-mariadb` atteigne le statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION    STATUS     AGE
sample-mariadb    11.8.5     Ready     3m46s
```

Vérifions les ressources des conteneurs Pod,

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

Vous pouvez voir que le pod dispose des ressources par défaut attribuées par l'opérateur KubeDB.

Nous sommes maintenant prêts à appliquer le `MariaDBOpsRequest` CR pour mettre à jour les ressources de cette base de données.

### Mise à l'échelle verticale

Ici, nous allons mettre à jour les ressources de la base de données pour répondre aux ressources souhaitées après la mise à l'échelle.

#### Créer une demande MariaDBOps

Afin de mettre à jour les ressources de la base de données, nous devons créer un `MariaDBOpsRequest` CR avec nos ressources souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

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

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle verticale sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `VerticalScaling` sur notre base de données.
* `spec.VerticalScaling.mariadb` spécifie les ressources souhaitées après la mise à l'échelle.
* `spec.verticalScaling.mode` spécifie comment la mise à l'échelle est actionnée - `Restart` (par défaut, redémarre les Pods) ou `InPlace` (redimensionne les pods en cours d'exécution sans redémarrage, en revenant au redémarrage si un nœud ne peut pas accueillir les nouvelles ressources). Voir [Modes de mise à l'échelle verticale](overview.md#vertical-scaling-modes).

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/mdops-vscale.yaml
mariadbopsrequest.ops.kubedb.com/mdops-vscale created
```

#### Vérifiez que les ressources du cluster MariaDB ont été mises à jour avec succès

Si tout se passe bien, `KubeDB` L'opérateur d'entreprise mettra à jour les ressources de `MariaDB` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                     TYPE              STATUS       AGE
mdops-vscale        VerticalScaling      Successful    3m56s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier depuis l'un des Pod yaml si les ressources de la base de données ont été mises à jour pour répondre à l'état souhaité, vérifions,

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

Le résultat ci-dessus vérifie que nous avons réussi à augmenter les ressources de la base de données MariaDB.

### Mise à l'échelle verticale sur place

Pour redimensionner les pods **sans redémarrage**, ensemble `spec.verticalScaling.mode` à `InPlace` dans le
`MariaDBOpsRequest`. L'opérateur redimensionne les conteneurs en cours d'exécution via Kubernetes `pods/resize`
sous-ressource et redémarre un Pod uniquement si son nœud ne peut pas accueillir les nouvelles ressources.

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

Appliquons-le de la même manière que ci-dessus :

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/scaling/vertical-scaling/cluster/example/mdops-vscale-inplace.yaml
mariadbopsrequest.ops.kubedb.com/mdops-vscale-inplace created
```

Les ressources sont mises à jour sans redémarrage du pod.

> **Note:** Pour un **distribué** `MariaDB` déploiement, un véritable redimensionnement sur place n'est pas possible, donc `InPlace` se dégrade automatiquement en `Restart`.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete mariadbopsrequest -n demo mdops-vscale
```