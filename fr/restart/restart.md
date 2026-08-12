> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Redémarrer MariaDB

KubeDB prend en charge le redémarrage de la base de données MariaDB via un `MariaDBOpsRequest`. Le redémarrage est utile si certains pods sont bloqués dans une phase ou s'ils ne fonctionnent pas correctement. Ce tutoriel vous montrera comment l'utiliser.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
  namespace/demo created
```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [documents/exemples/MariaDB](https://github.com/kubedb/docs/tree/v2026.7.10/docs/examples/mariadb) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Déployer MariaDB

Dans cette section, nous allons déployer une base de données MariaDB à l'aide de KubeDB.

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

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/restart/MariaDB.yaml
MariaDB.kubedb.com/mariadb created
```

## Appliquer Redémarrer opsRequest

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

* `spec.type` spécifie le type de demande d'opérations
* `spec.databaseRef` contient le nom de la base de données MariaDB. La base de données doit être disponible dans le même espace de noms que opsRequest
* Le `spec.timeout` Le champ spécifie la durée maximale pendant laquelle l'opérateur attendra la fin de l'opération avant de la marquer comme ayant échoué.
* Le `spec.apply` Le champ détermine si l'opération doit toujours être appliquée (Always) ou si la phase base de données est prête (IfReady).

> Remarque : La méthode de redémarrage de la base de données en mode autonome et cluster est exactement la même que ci-dessus. Tout ce dont vous avez besoin est de spécifier le nom MariaDB correspondant dans `spec.databaseRef.name` section.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/restart/ops.yaml
MariaDBopsrequest.ops.kubedb.com/restart created
```

Dans `MariaDB`, tous les pods agissent comme des pods principaux, donc l'opérateur Ops-manager redémarrera les pods un par un dans l'ordre.

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

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete  mariaops -n demo restart
kubectl delete mariadb -n demo mariadb
kubectl delete ns demo
```

## Prochaines étapes

* En savoir plus sur [sauvegarde et restauration](../backup/kubestash/overview.md) Base de données MariaDBQL utilisant Stash.
* En savoir plus sur l'initialisation [MariaDBQL avec script](../initialization/using-script.md)
* Concepts détaillés de [Objet MariaDB](../concepts/mariadb.md).
* Vous voulez pirater KubeDB ? Consultez notre [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).