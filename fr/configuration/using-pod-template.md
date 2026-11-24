> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Exécutez MariaDB avec un PodTemplate personnalisé

KubeDB prend en charge la fourniture d'une configuration personnalisée pour MariaDB via [Modèle de pod](../concepts/mariadb.md#specpodtemplate). Ce didacticiel vous montrera comment utiliser KubeDB pour exécuter une base de données MariaDB avec une configuration personnalisée à l'aide de PodTemplate.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/guides/mariadb/configuration/using-pod-template/examples](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/configuration/using-pod-template/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Aperçu

KubeDB permet de fournir un modèle pour le pod de base de données via `spec.podTemplate`. L'opérateur KubeDB transmettra les informations fournies dans `spec.podTemplate` au PetSet créé pour la base de données MariaDB.

KubeDB accepte les champs suivants à définir `spec.podTemplate:`

* métadonnées :
  + annotations (annotation du pod)
* contrôleur:
  + annotations (annotation de petset)
* spécification :
  + env
  + ressources
  + initConteneurs
  + imagePullSecrets
  + sélecteur de nœud
  + Nom du planificateur
  + tolérances
  + nomClassePriorité
  + priorité
  + contexte de sécurité

Découvrez les champs en détail dans [Concept de modèle de pod](../concepts/mariadb.md#specpodtemplate),

## Configuration du CRD

Vous trouverez ci-dessous le YAML pour MariaDB créé dans cet exemple. Ici, [`spec.podTemplate.spec.env`](../concepts/mariadb.md#specpodtemplatespecenv) spécifie les variables d'environnement et [`spec.podTemplate.spec.args`](../concepts/mariadb.md#specpodtemplatespecargs) fournit des arguments supplémentaires pour [Image Docker de MariaDB](https://hub.docker.com/_/mariadb/).

Dans ce tutoriel, une base de données initiale `mdDB` sera créé en fournissant `env` `MYSQL_DATABASE` tandis que le jeu de caractères du serveur sera défini sur `utf8mb4` en ajoutant un supplément `args`.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  podTemplate:
    spec:
      containers:
      - name: mariadb
        env:
        - name: MYSQL_DATABASE
          value: mdDB
        args:
        - --character-set-server=utf8mb4
        resources:
          requests:
            memory: "1Gi"
            cpu: "250m"
  deletionPolicy: WipeOut
```

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/configuration/using-pod-template/examples/md-misc-config.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attendez quelques minutes. L'opérateur KubeDB créera le PVC, le petset, les services, le secret, etc. Si tout se passe bien, nous verrons qu'un pod portant le nom `sample-mariadb` a été créé.

Vérifiez que le pod du petset est en cours d'exécution

```bash
$ kubectl get pod -n demo
NAME               READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          96s
```

Vérifiez le journal du pod pour voir si la base de données est prête

```bash
$ kubectl logs -f -n demo sample-mariadb-0
2021-03-18 06:06:17+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 06:06:18+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 06:06:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 06:06:19+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  6:06:33 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

Une fois qu'on voit `Note] mysqld: ready for connections.` dans le journal, la base de données est prête.

Nous allons maintenant vérifier si la base de données a démarré avec la configuration personnalisée que nous avons fournie.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -- bash
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 22
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# Check mdDB
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mdDB               |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

# Check character_set_server
MariaDB [(none)]> show variables like 'char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | latin1                     |
| character_set_connection | latin1                     |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | latin1                     |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.001 sec)

MariaDB [(none)]> quit;
Bye
```

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```