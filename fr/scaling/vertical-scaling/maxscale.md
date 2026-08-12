> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Serveur MaxScale à échelle verticale

Ce guide vous montrera comment utiliser `KubeDB` Opérateur Ops-manager pour mettre à jour les ressources d'un serveur MaxScale.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../../concepts/mariadb.md)
  + [Réplication MariaDB](../../clustering/mariadb-replication.md)
  + [MariaDBOpsDemande](../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle verticale](overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Appliquer la mise à l'échelle verticale sur MaxScale Server

Ici, nous allons déployer un `MariaDB` cluster en mode réplication à l'aide d'une version prise en charge par `KubeDB` opérateur. Ensuite, nous appliquerons une mise à l'échelle verticale sur `MaxScale` serveur.

### Déployer le cluster MariaDB

Dans cette section, nous allons déployer une base de données MariaDB en mode réplication. Ensuite, dans la section suivante, nous mettrons à jour les ressources du `MaxScale` serveur utilisant `MariaDBOpsRequest` CR. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

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

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/md-replication.yaml
mariadb.kubedb.com/md-replication created
```

Maintenant, attends `md-replication` a un statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
md-replication   11.8.5   Ready    2m39s
```

Vérifions les ressources des conteneurs Pod,

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

Vous pouvez voir que le pod dispose des ressources par défaut attribuées par l'opérateur KubeDB.

Nous sommes maintenant prêts à appliquer le `MariaDBOpsRequest` CR pour mettre à jour les ressources de cette base de données.

### Mise à l'échelle verticale

Ici, nous allons mettre à jour les ressources de `MaxScale` serveur pour répondre aux ressources souhaitées après la mise à l’échelle.

#### Créer une demande MariaDBOps

Afin de mettre à jour les ressources de la base de données, nous devons créer un `MariaDBOpsRequest` CR avec nos ressources souhaitées. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CR que nous allons créer,

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

Ici,

* `spec.type` précise que nous effectuons `VerticalScaling` sur notre base de données.
* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle verticale sur `md-replication` base de données.
* `spec.VerticalScaling.maxscale` spécifie les ressources souhaitées du serveur maxscale après la mise à l'échelle.
* `spec.verticalScaling.mode` spécifie comment la mise à l'échelle est actionnée - `Restart` (par défaut, redémarre les Pods) ou `InPlace` (redimensionne les pods en cours d'exécution sans redémarrage, en revenant au redémarrage si un nœud ne peut pas accueillir les nouvelles ressources). Voir [Modes de mise à l'échelle verticale](overview.md#vertical-scaling-modes).

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/scaling/vertical-scaling/mx-vscale.yaml
mariadbopsrequest.ops.kubedb.com/maxscale-vertical-scale created
```

#### Vérifiez que les ressources du serveur MaxScale ont été mises à jour avec succès

Si tout se passe bien, `KubeDB` L’opérateur Ops-manager mettra à jour les ressources de `MariaDB` objet et associé `PetSets` et `Pods`.

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CR,

```bash
$ watch kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo 

NAME                      TYPE              STATUS       AGE
maxscale-vertical-scale   VerticalScaling   Successful   3m8s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Maintenant, nous allons vérifier à partir de l'un des Pod yaml si les ressources du serveur maxscale ont été mises à jour pour atteindre l'état souhaité, vérifions,

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

Le résultat ci-dessus vérifie que nous avons réussi à augmenter les ressources de la base de données MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo md-replication
$ kubectl delete mariadbopsrequest -n demo maxscale-vertical-scale
$ kubectl delete ns demo
```