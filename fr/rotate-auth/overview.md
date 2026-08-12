> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Rotation de l'authentification de MariaDB

Ce guide donnera un aperçu de la configuration de l'authentification par rotation de l'opérateur KubeDB Ops-manager.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :
  + [MariaDB](../concepts/mariadb.md)
  + [MariaDBOpsDemande](../concepts/opsrequest.md)

## Comment fonctionne le processus de configuration de l'authentification Rotate MariaDB

Le processus de rotation d'authentification pour MariaDB à l'aide de KubeDB implique les étapes suivantes :

1. Un utilisateur crée d'abord un `MariaDB` Objet de ressource personnalisé (CRO).
2. Le `KubeDB Provisioner operator` surveille continuellement `MariaDB` CRO.
3. Lorsque l'opérateur détecte un `MariaDB` CR, il prévoit les `PetSets`, ainsi que les ressources associées telles que les secrets, les services et autres dépendances.
4. Pour lancer la rotation d'authentification, l'utilisateur crée un `MariaDBOpsRequest` CR avec la configuration souhaitée.
5. Le `KubeDB Ops-manager` l'opérateur surveille `MariaDBOpsRequest` CR.
6. Lors de la détection d'un `MariaDBOpsRequest`, l'opérateur met en pause l'action référencée `MariaDB` objet, en veillant à ce que le fournisseur
   L’opérateur n’effectue aucune opération pendant le processus de rotation d’authentification.
7. Le `Ops-manager` L'opérateur met ensuite à jour la configuration nécessaire (telle que les informations d'identification) en fonction des informations fournies. `MariaDBOpsRequest` spécification.
8. Après avoir appliqué la configuration mise à jour, l'opérateur redémarre tous `MariaDB` Pods afin qu'ils proposent les nouvelles variables et paramètres d'environnement d'authentification.
9. Une fois la rotation d'authentification terminée avec succès, l'opérateur reprend la `MariaDB` objet, permettant à l’opérateur Provisioner de poursuivre ses opérations habituelles.

Dans la section suivante, nous vous présenterons un guide étape par étape pour faire pivoter l'authentification MariaDB à l'aide de l'outil `MariaDBOpsRequest` CRD.