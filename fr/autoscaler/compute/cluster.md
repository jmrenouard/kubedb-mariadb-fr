> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique de la ressource de calcul d'une base de données de cluster MariaDB

Ce guide vous montrera comment utiliser `KubeDB` pour mettre à l'échelle automatiquement les ressources de calcul, c'est-à-dire le processeur et la mémoire d'une base de données de réplicas MariaDB.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster.
* Installer `KubeDB` Opérateur Community, Ops-Manager et Autoscaler dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Installer `Metrics Server` depuis [ici](https://github.com/kubernetes-sigs/metrics-server#installation)
* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../../concepts/mariadb.md)
  + [MariaDBAutoscaler](../../concepts/autoscaler.md)
  + [MariaDBOpsDemande](../../concepts/opsrequest.md)
  + [Présentation de la mise à l'échelle automatique des ressources de calcul](overview.md)

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## Mise à l'échelle automatique de la base de données du cluster

Ici, nous allons déployer un `MariaDB` Cluster utilisant une version prise en charge par `KubeDB` opérateur. Ensuite, nous allons appliquer `MariaDBAutoscaler` pour configurer la mise à l'échelle automatique.

#### Déployer le cluster MariaDB

Dans cette section, nous allons déployer un cluster MariaDB avec la version `12.1.2`. Ensuite, dans la section suivante, nous configurerons la mise à l'échelle automatique pour cette base de données en utilisant `MariaDBAutoscaler` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

> Si vous souhaitez mettre à l'échelle automatiquement MariaDB `Standalone`, Supprimez simplement le `spec.Replicas` à partir du yaml ci-dessous et le reste des étapes sont les mêmes.

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

Créons le `MariaDB` CRO que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/compute/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attends `sample-mariadb` a un statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    14m
```

Vérifions les ressources des conteneurs Pod,

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

Vérifions les ressources MariaDB,

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

Vous pouvez voir à partir des résultats ci-dessus que les ressources sont les mêmes que celles que nous avons attribuées lors du déploiement de mariadb.

Nous sommes maintenant prêts à appliquer le `MariaDBAutoscaler` CRO pour configurer la mise à l'échelle automatique pour cette base de données.

### Mise à l'échelle automatique des ressources de calcul

Ici, nous allons configurer la mise à l'échelle automatique des ressources de calcul à l'aide d'un objet MariaDBAutoscaler.

#### Créer un objet MariaDBAutoscaler

Afin de configurer la mise à l'échelle automatique des ressources de calcul pour ce cluster de bases de données, nous devons créer un `MariaDBAutoscaler` CRO avec notre configuration souhaitée. Vous trouverez ci-dessous le YAML du `MariaDBAutoscaler` objet que nous allons créer,

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

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de mise à l'échelle des ressources de calcul sur `sample-mariadb` base de données.
* `spec.compute.mariadb.trigger` spécifie que la mise à l'échelle automatique du calcul est activée pour cette base de données.
* `spec.compute.mariadb.podLifeTimeThreshold` spécifie la durée de vie minimale d'au moins un des pods pour lancer une mise à l'échelle verticale.
* `spec.compute.mariadb.resourceDiffPercentage` spécifie la différence de ressource minimale en pourcentage. La valeur par défaut est de 10 %.
  Si la différence entre les ressources actuelles et recommandées est inférieure à ResourceDiffPercentage, l’opérateur Autoscaler ignorera la mise à jour.
* `spec.compute.mariadb.minAllowed` spécifie les ressources minimales autorisées pour la base de données.
* `spec.compute.mariadb.maxAllowed` spécifie les ressources maximales autorisées pour la base de données.
* `spec.compute.mariadb.controlledResources` spécifie les ressources contrôlées par l'autoscaler.
* `spec.compute.mariadb.containerControlledValues` spécifie quelles valeurs de ressources doivent être contrôlées. La valeur par défaut est « RequestsAndLimits ».
* `spec.opsRequestOptions.apply` a deux valeurs prises en charge : `IfReady` & `Always`.
  Utiliser `IfReady` si vous souhaitez traiter l'opsReq uniquement lorsque la base de données est prête. Et utiliser `Always` si vous souhaitez traiter l'exécution de opsReq quel que soit l'état de la base de données.
* `spec.opsRequestOptions.timeout` spécifie la durée maximale de chaque étape de opsRequest (en secondes).
  Si une étape ne se termine pas dans le délai spécifié, la requête opérationnelle entraînera un échec.

Créons le `MariaDBAutoscaler` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/autoscaler/compute/cluster/examples/mdas-compute.yaml
mariadbautoscaler.autoscaling.kubedb.com/md-as-compute created
```

#### Vérifiez que l'autoscaling est configuré avec succès

Vérifions que le `mariadbautoscaler` la ressource est créée avec succès,

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

Ainsi, le `mariadbautoscaler` la ressource est créée avec succès.

Nous pouvons vérifier à partir du résultat ci-dessus que `status.vpas` contient le `RecommendationProvided` condition à vrai. Et en même temps, `status.vpas.recommendation.containerRecommendations` contiennent la recommandation réellement générée.

Notre opérateur d'autoscaler surveille en permanence la recommandation générée et crée un `mariadbopsrequest` en fonction des recommandations, si les ressources du pod de base de données doivent être augmentées ou réduites.

Regardons le `mariadbopsrequest` dans l'espace de noms de la démo pour voir s'il y en a `mariadbopsrequest` l'objet est créé. Après un certain temps, vous verrez qu'un `mariadbopsrequest` sera créé sur la base de la recommandation.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                          TYPE              STATUS       AGE
mdops-sample-mariadb-6xc1kc   VerticalScaling   Progressing  7s
```

Attendons que la demande d'opérations aboutisse.

```bash
$ kubectl get mariadbopsrequest -n demo
NAME                              TYPE              STATUS       AGE
mdops-vpa-sample-mariadb-z43wc8   VerticalScaling   Successful   3m32s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies pour faire évoluer la base de données.

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

Maintenant, nous allons vérifier à partir du Pod et du yaml MariaDB si les ressources de la base de données du jeu de réplicas ont été mises à jour pour atteindre l'état souhaité. Vérifions,

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

Le résultat ci-dessus vérifie que nous avons réussi la mise à l'échelle automatique des ressources de la base de données du jeu de réplicas MariaDB.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
kubectl delete mariadb -n demo sample-mariadb
kubectl delete mariadbautoscaler -n demo md-as-compute
kubectl delete ns demo
```