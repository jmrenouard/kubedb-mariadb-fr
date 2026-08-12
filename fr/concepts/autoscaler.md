> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDBAutoscaler

## Qu'est-ce que MariaDBAutoscaler ?

`MariaDBAutoscaler` est un Kubernetes `Custom Resource Definitions` (CRD). Il fournit une configuration déclarative pour la mise à l'échelle automatique des ressources de calcul MariaDB et le stockage des composants de base de données de manière native Kubernetes.

## Spécifications du CRD de MariaDBAutoscaler

Comme toute ressource officielle Kubernetes, un `MariaDBAutoscaler` a `TypeMeta`, `ObjectMeta`, `Spec` et `Status` sections.

Ici, un échantillon `MariaDBAutoscaler` Les CRO pour la mise à l'échelle automatique de différents composants de la base de données sont indiqués ci-dessous :

**Échantillon `MariaDBAutoscaler` pour MariaDB :**

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

Nous allons décrire ici les différentes sections d'un `MariaDBAutoscaler` crd.

A `MariaDBAutoscaler` l'objet comporte les champs suivants dans le `spec` section.

### spec.databaseRef

`spec.databaseRef` est un champ obligatoire qui pointe vers le [MariaDB](mariadb.md) objet pour lequel l’autoscaling sera effectué. Ce champ est constitué du sous-champ suivant :

* **spec.databaseRef.name :** précise le nom du [MariaDB](mariadb.md) objet.

### spec.compute

`spec.compute` spécifie la configuration de mise à l'échelle automatique pour les ressources de calcul, c'est-à-dire le processeur et la mémoire des composants de base de données. Ce champ est constitué du sous-champ suivant :

* `spec.compute.mariadb` indique la configuration de mise à l'échelle automatique de calcul souhaitée pour un cluster ou un cluster MariaDB autonome.

Tous ont les sous-champs suivants :

* `trigger` indique si la mise à l'échelle automatique du calcul est activée pour ce composant de la base de données. Si « Activé », la mise à l'échelle automatique de calcul est activée. Si « Désactivé », la mise à l'échelle automatique de calcul est désactivée.
* `minAllowed` spécifie la quantité minimale de ressources qui sera recommandée, la valeur par défaut n'est pas un minimum.
* `maxAllowed` spécifie la quantité maximale de ressources qui sera recommandée, la valeur par défaut n'est pas de maximum.
* `controlledResources` spécifie le type de ressources de calcul (processeur et mémoire) autorisé pour la mise à l'échelle automatique. Les valeurs autorisées sont « cpu » et « mémoire ».
* `containerControlledValues` spécifie quelles valeurs de ressources doivent être contrôlées. Les valeurs autorisées sont « RequestsAndLimits » et « RequestsOnly ».
* `resourceDiffPercentage` spécifie la différence de ressource minimale entre la valeur recommandée et la valeur actuelle en pourcentage. Si le pourcentage de différence est supérieur à cette valeur, la mise à l'échelle automatique sera déclenchée.
* `podLifeTimeThreshold` spécifie la durée de vie minimale d'au moins un des pods avant de déclencher la mise à l'échelle automatique.
* `InMemoryScalingThreshold` le pourcentage de mémoire qui sera transmis comme inMemorySizeGB pour le moteur de base de données inmemory, qui n'est disponible que pour la variante percona de mariadb.

### spécification.stockage

`spec.compute` spécifie la configuration de mise à l'échelle automatique pour les ressources de stockage des composants de base de données. Ce champ est constitué du sous-champ suivant :

* `spec.compute.mairadb` indique la configuration de mise à l'échelle automatique du stockage souhaitée pour un cluster ou un cluster MariaDB autonome.

Tous ont les sous-champs suivants :

* `trigger` indique si la mise à l'échelle automatique du stockage est activée pour ce composant de la base de données. Si « Activé », la mise à l'échelle automatique du stockage est activée. Si « Désactivé », la mise à l'échelle automatique du stockage est désactivée.
* `usageThreshold` indique le seuil de pourcentage d'utilisation. Si l'utilisation actuelle du stockage dépasse, la mise à l'échelle automatique du stockage sera déclenchée.
* `scalingThreshold` indique le pourcentage du stockage actuel qui sera mis à l'échelle.
* `expansionMode` spécifie le mode d'expansion du volume lorsque l'autoscaler de stockage effectue une extension de volume OpsRequest. La valeur par défaut est `Online`.