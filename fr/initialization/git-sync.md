> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Initialisation MariaDB à partir d'un référentiel Git

Ce guide montre comment utiliser KubeDB pour initialiser une base de données MariaDB avec des scripts d'initialisation (.sql, .sh et/ou .sql.gz) stockés dans un référentiel Git public ou privé.
Pour récupérer le contenu du référentiel, KubeDB utilise un conteneur side-car appelé [git-sync](https://github.com/kubernetes/git-sync).
Dans cet exemple, nous allons initialiser MariaDB en utilisant un `.sql` script du dépôt GitHub [kubedb/mysql-init-scripts](https://github.com/kubedb/mysql-init-scripts).

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes, et le `kubectl` L'outil de ligne de commande doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).

Pour que tout reste isolé, nous allons utiliser un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

## À partir du référentiel Git public

KubeDB implémente un `MariaDB` Définition de ressources personnalisées (CRD) pour définir la spécification d'une base de données MariaDB.
Pour initialiser la base de données à partir d'un référentiel Git public, vous devez spécifier les arguments requis pour le `git-sync` Conteneur side-car dans la spécification de ressources MariaDB.
Le manifeste YAML suivant montre un exemple `MariaDB` objet configuré avec `git-sync`:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       - --repo=https://github.com/kubedb/mysql-init-scripts
       - --link=current
       - --root=/root
       # terminate after one successful sync
       - --one-time 
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

```bash
kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/examples/mariadb/initialization/git-sync-public.yaml
mariadb.kubedb.com/sample-mariadb created
```

Le `git-sync` Le conteneur a deux indicateurs obligatoires :

* `--repo` – spécifie le référentiel Git distant à synchroniser.
* `--root` – spécifie le répertoire de travail dans lequel le référentiel sera cloné.

Ici, la valeur du `--link` l'argument doit correspondre à la valeur de `spec.init.script.scriptPath`.
Le `--link` L'argument crée un lien symbolique qui pointe toujours vers les dernières données synchronisées.

> Pour en savoir plus sur `git-sync` configuration, visitez ceci [lien](https://github.com/kubernetes/git-sync).

Maintenant, attends `sample-mariadb` a un statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5   Ready    5m
```

Ensuite, nous nous connecterons à la base de données MariaDB et vérifierons les données insérées depuis le `*.sql` script stocké dans le référentiel Git.

```bash
kubectl exec -it -n demo sample-mariadb-0 -- bash
Defaulted container "mariadb" out of: mariadb, mariadb-init (init), git-sync (init)
```

```mysql
mysql@sample-mariadb-0:/$ mariadb -uroot -p$MYSQL_ROOT_PASSWORD
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 6
Server version: 10.5.23-MariaDB-1:11.8.5+maria~ubu2004 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mysql]> select * from kubedb_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.000 sec)

MariaDB [mysql]> select * from demo_table;
+----+-------+
| id | name  |
+----+-------+
|  1 | name1 |
|  2 | name2 |
|  3 | name3 |
+----+-------+
3 rows in set (0.000 sec)
```

## À partir du référentiel Git privé

### 1. Utilisation de la clé SSH

Git-sync prend en charge l'utilisation du protocole SSH pour extraire le contenu git.

Tout d’abord, obtenez les clés d’hôte de votre serveur git :

```bash
$ ssh-keyscan $YOUR_GIT_HOST > /tmp/known_hosts
```

> `$YOUR_GIT_HOST` fait référence au nom d'hôte de votre serveur Git.  
> Par exemple, si vous utilisez GitHub, définissez la variable comme suit :
>
> ```bash
> export YOUR_GIT_HOST=github.com
> ```

Utilisez le `kubectl create secret` commande pour créer un secret à partir de votre clé SSH locale et du fichier d'hôtes connus.
Ce secret sera utilisé par git-sync pour s'authentifier auprès du référentiel Git.

```bash
$ kubectl create secret generic -n demo git-creds \
    --from-file=ssh=$HOME/.ssh/id_rsa \
    --from-file=known_hosts=/tmp/known_hosts
```

Le manifeste YAML suivant fournit un exemple de `MariaDB` ressource configurée pour utiliser `git-sync` avec un dépôt Git privé :

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       # update with your private repository    
       - --repo=<your-ssh-repo-url>
       - --link=current
       - --root=/root
       # terminate after one successful sync
       - --one-time 
       authSecret:
         name: git-creds
       # run as git sync user 
       securityContext:
         runAsUser: 65533
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Ici,

* `.spec.init.git.securityContext.runAsUser: 65533` assurez-vous que le conteneur s'exécute en tant que non-root dédié `git-sync` utilisateur.
* `.spec.init.git.authSecret` précise le secret contenant le `SSH` clé.

Une fois que la base de données atteint le `Ready` état, vous pouvez vérifier les données en utilisant la méthode décrite ci-dessus.

### 2. Utilisation du nom d'utilisateur et du jeton d'accès personnel (PAT)

Tout d'abord, créez un `Personal Access Token (PAT)` sur votre serveur hôte Git avec les autorisations requises pour accéder au référentiel.
Créez ensuite un secret Kubernetes à l'aide du `Personal Access Token (PAT)`:

```bash
$ kubectl create secret generic -n demo git-pat \
    --from-literal=github-pat=<ghp_yourpersonalaccesstoken>
```

Maintenant, créez un `MariaDB` ressource qui fait référence au secret créé ci-dessus.
Le manifeste YAML suivant montre un exemple :

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  init:
   script:
     scriptPath: "current"
     git:
       args:
       # update with your private repository    
       - --repo=<your-https-repo-url>
       - --link=current
       - --root=/root
       - --credential={"url":"https://github.com","username":"<username>","password-file":"/etc/git-secret/github-pat"}
       # terminate after one successful sync
       - --one-time 
       authSecret:
         name: git-pat
       # run as git sync user 
       securityContext:
         runAsUser: 65533
  version: "12.1.2"
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Une fois que la base de données atteint le `Ready` état, vous pouvez vérifier les données en utilisant la méthode décrite ci-dessus.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
$ kubectl delete secret -n demo git-pat git-creds
$ kubectl delete ns demo
```