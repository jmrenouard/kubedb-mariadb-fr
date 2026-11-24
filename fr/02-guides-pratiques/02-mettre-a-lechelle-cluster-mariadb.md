# Mettre à l'échelle un cluster MariaDB

Consultez la [matrice des CRD et opérations](../03-reference/01-matrice-crd-et-operations.md) avant de démarrer cette procédure.

## Prérequis

- Vérifiez que le cluster `sample-mariadb` affiche l'état `Ready` dans `demo`.
- Installez l'opérateur KubeDB Enterprise Ops-Manager dans le cluster.

## Consignes de sécurité

**ATTENTION :** Vérifiez les ressources CPU et mémoire libres sur les nœuds avant la mise à l'échelle. Un nœud saturé bloque les pods à l'état `Pending`.

## Étapes

1. Enregistrez ce manifeste `MariaDBOpsRequest` dans `mdops-scale.yaml` pour passer à trois réplicas :

   ```yaml
   apiVersion: ops.kubedb.com/v1alpha1
   kind: MariaDBOpsRequest
   metadata:
     name: mdops-hscale-up
     namespace: demo
   spec:
     type: HorizontalScaling
     databaseRef:
       name: sample-mariadb
     horizontalScaling:
       member: 3
   ```

2. Appliquez la demande de mise à l'échelle dans `demo` :

   ```bash
   kubectl apply -f mdops-scale.yaml
   ```

3. Attendez le statut `Successful` sur l'objet `MariaDBOpsRequest` :

   ```bash
   kubectl get mariadbopsrequest -n demo mdops-hscale-up
   ```

4. Enregistrez ce manifeste `MariaDBOpsRequest` dans `mdops-vscale.yaml` pour ajuster le CPU et la mémoire :

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
         requests:
           cpu: "500m"
           memory: "512Mi"
         limits:
           cpu: "1000m"
           memory: "1Gi"
   ```

5. Appliquez le fichier `mdops-vscale.yaml` dans `demo` :

   ```bash
   kubectl apply -f mdops-vscale.yaml
   ```

## Vérification

1. Vérifiez que `kubectl get mariadbopsrequest -n demo` affiche `Successful` pour chaque demande.
2. Vérifiez que `kubectl get mariadb -n demo sample-mariadb` affiche trois réplicas en phase `Ready`.
3. Exécutez `kubectl describe pod -n demo sample-mariadb-0` puis vérifiez les nouvelles limites CPU et mémoire.

## Retour arrière

1. Si des pods restent en état `Pending`, créez un manifeste `MariaDBOpsRequest` avec le nombre initial de réplicas.
2. Appliquez ce manifeste de repli puis vérifiez le retour en phase `Ready`.
