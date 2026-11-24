> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Mise à l'échelle automatique des ressources de calcul MariaDB

Ce guide donnera un aperçu de la façon dont l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de calcul de la base de données, c'est-à-dire le processeur et la mémoire en utilisant `mariadbautoscaler` crd.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](../../concepts/mariadb.md)
  + [MariaDBAutoscaler](../../concepts/autoscaler.md)
  + [MariaDBOpsRequest](../../concepts/opsrequest.md)

## Fonctionnement de la mise à l'échelle automatique du calcul

Le diagramme suivant montre comment l'opérateur KubeDB Autoscaler met automatiquement à l'échelle les ressources de `MariaDB` composants de base de données. Ouvrez l'image dans un nouvel onglet pour voir la version agrandie.

  ![Auto Scaling process of MariaDB](../../../images/autoscaler_compute_overview_mdas-compute.png)

Fig : Processus de mise à l'échelle automatique de MariaDB

Le processus Auto Scaling comprend les étapes suivantes :

1. Dans un premier temps, l'utilisateur crée un `MariaDB` Objet de ressource personnalisé (CRO).
2. `KubeDB` L'opérateur communautaire surveille `MariaDB` CRO.
3. Lorsque l'opérateur trouve un `MariaDB` CRO, il crée le nombre requis de `PetSets` et les éléments nécessaires connexes comme les secrets, les services, etc.
4. Ensuite, afin de configurer l'autoscaling des ressources CPU et mémoire du `MariaDB` base de données, l'utilisateur crée un `MariaDBAutoscaler` CRO avec la configuration souhaitée.
5. `KubeDB` L'opérateur de l'autoscaler surveille le `MariaDBAutoscaler` CRO.
6. `KubeDB` L'opérateur Autoscaler utilise la version modifiée du responsable Kubernetes [Recommandateur APV](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/pkg) pour différents composants de la base de données, comme spécifié dans le `mariadbautoscaler` CRO.
   Il génère des recommandations basées sur l'utilisation des ressources et les stocke dans le `status` section du CRO de l'autoscaler.
7. Si la recommandation générée ne correspond pas aux ressources actuelles de la base de données, alors `KubeDB` L'opérateur Autoscaler crée un `MariaDBOpsRequest` CRO pour mettre à l'échelle la base de données afin qu'elle corresponde à la recommandation fournie par l'objet VPA.
8. `KubeDB Ops-Manager operator` regarde le `MariaDBOpsRequest` CRO.
9. Enfin, le `KubeDB Ops-Manager operator` mettra à l'échelle le composant de base de données verticalement comme spécifié sur le `MariaDBOpsRequest` CRO.

Dans la prochaine documentation, nous allons montrer un guide étape par étape sur la mise à l'échelle automatique de la base de données MariaDB à l'aide de `MariaDBAutoscaler` CRD.