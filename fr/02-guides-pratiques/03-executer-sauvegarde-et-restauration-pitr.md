# Exécuter une sauvegarde et une restauration PITR

Consultez le tutoriel [Sauvegarde KubeStash et récupération ponctuelle](../01-tutoriels/02-sauvegarde-kubestash-et-pitr.md) avant de démarrer cette procédure.

## Prérequis

- Vérifiez que `BackupStorage`, `RetentionPolicy` et `MariaDBArchiver` existent dans `demo`.
- Vérifiez la présence d'un instantané récent et des journaux binlog archivés dans le stockage distant.

## Consignes de sécurité

**AVERTISSEMENT :** Restaurez les données vers un nouvel objet `MariaDB` distinct de l'instance active. Une restauration sur une instance active détruit les données de production.

## Étapes

1. Relevez l'horodatage UTC exact avant l'incident applicatif.
2. Enregistrez ce manifeste de restauration dans `restore-mariadb.yaml` avec `spec.init.archiver.recoveryTimestamp` :

   ```yaml
   apiVersion: kubedb.com/v1
   kind: MariaDB
   metadata:
     name: restore-mariadb
     namespace: demo
   spec:
     version: "11.8.5"
     replicas: 3
     storageType: Durable
     storage:
       storageClassName: "longhorn"
       accessModes:
         - ReadWriteOnce
       resources:
         requests:
           storage: 10Gi
     init:
       archiver:
         recoveryTimestamp: "2026-08-12T10:15:00Z"
     deletionPolicy: WipeOut
   ```

3. Appliquez le fichier `restore-mariadb.yaml` dans `demo` :

   ```bash
   kubectl apply -f restore-mariadb.yaml
   ```

4. Surveillez les pods de restauration jusqu'à la phase `Ready` du cluster `restore-mariadb` :

   ```bash
   kubectl get pods,mariadb -n demo
   ```

## Vérification

1. Exécutez `kubectl get mariadb -n demo restore-mariadb` puis vérifiez la phase `Ready`.
2. Ouvrez un shell dans `restore-mariadb-0` puis comptez les lignes restaurées :

   ```bash
   kubectl exec -it -n demo restore-mariadb-0 -- bash
   ```

   ```mysql
   MariaDB [hello]> SELECT COUNT(*) FROM demo_table;
   ```

3. Vérifiez que le nombre de lignes correspond aux données avant l'incident.

## Retour arrière

1. Si les données restaurées restent incomplètes, supprimez l'instance `restore-mariadb` :

   ```bash
   kubectl delete mariadb -n demo restore-mariadb
   ```

2. Corrigez `spec.init.archiver.recoveryTimestamp` dans `restore-mariadb.yaml` puis lancez `kubectl apply -f restore-mariadb.yaml`.
