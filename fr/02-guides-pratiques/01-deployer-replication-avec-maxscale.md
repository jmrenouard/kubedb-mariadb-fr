# Déployer un cluster répliqué avec MaxScale

Consultez l'[aide-mémoire kubectl et maxctrl](../03-reference/02-aide-memoire-kubectl-maxctrl.md) avant de démarrer cette procédure.

## Prérequis

- Installez `kubectl` sur votre poste et connectez cet outil au cluster Kubernetes.
- Installez les opérateurs KubeDB Community et Enterprise dans le cluster.
- Créez l'espace de noms `demo` dans le cluster.

## Étapes

1. Enregistrez ce manifeste `MariaDB` dans le fichier `ha-mariadb.yaml` :

   ```yaml
   apiVersion: kubedb.com/v1
   kind: MariaDB
   metadata:
     name: ha-mariadb
     namespace: demo
   spec:
     version: "11.8.5"
     replicas: 3
     topology:
       mode: MariaDBReplication
       maxscale:
         replicas: 1
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

2. Appliquez le fichier `ha-mariadb.yaml` dans l'espace de noms `demo` :

   ```bash
   kubectl apply -f ha-mariadb.yaml
   ```

3. Attendez le démarrage de tous les pods MariaDB et du pod MaxScale :

   ```bash
   kubectl get pods -n demo -l app.kubernetes.io/instance=ha-mariadb
   ```

**NOTE :** Le service proxy MaxScale écoute sur le port `3306` après la mise en service des réplicas.

## Vérification

1. Exécutez `maxctrl list servers` dans le conteneur MaxScale :

   ```bash
   kubectl exec -it -n demo svc/ha-mariadb-mx -- maxctrl list servers
   ```

2. Vérifiez qu'un serveur affiche `Master, Running` et deux serveurs affichent `Slave, Running`.
3. Vérifiez que la ressource `MariaDB` affiche la phase `Ready` :

   ```bash
   kubectl get mariadb -n demo ha-mariadb
   ```

## Retour arrière

1. Si les vérifications échouent, supprimez l'objet `MariaDB` dans `demo` :

   ```bash
   kubectl delete mariadb -n demo ha-mariadb
   ```

2. Vérifiez que `kubectl get pods -n demo` n'affiche plus aucun pod `ha-mariadb`.
