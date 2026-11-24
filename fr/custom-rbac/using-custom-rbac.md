> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Utilisation de ressources RBAC personnalisées

KubeDB (version 0.13.0 et supérieure) prend en charge un contrôle utilisateur plus précis sur les autorisations d'accès basées sur les rôles fournies à une instance MariaDB. Ce didacticiel vous montrera comment utiliser KubeDB pour exécuter une instance MariaDB avec des ressources RBAC personnalisées.

## Avant de commencer

Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).

Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).

Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

```bash
$ kubectl create ns demo
namespace/demo created
```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [ici](https://github.com/kubedb/docs/tree/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

## Aperçu

KubeDB permet aux utilisateurs de fournir des ressources RBAC personnalisées, à savoir : `ServiceAccount`, `Role`, et `RoleBinding` pour MariaDB. Ceci est fourni via le `spec.podTemplate.spec.serviceAccountName` champ dans MariaDB crd. Si ce champ est laissé vide, l'opérateur KubeDB créera un nom de compte de service correspondant au nom de crd MariaDB. Le rôle et le RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés automatiquement pour ce compte de service.

Si un nom de compte de service est donné, mais qu'il n'existe aucun compte de service portant ce nom, l'opérateur KubeDB en créera un, et Role et RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés pour ce compte de service.

Si un nom de compte de service est donné et qu'il existe un compte de service portant ce nom, l'opérateur KubeDB utilisera ce compte de service existant. Étant donné que ce compte de service n'est pas géré par KubeDB, les utilisateurs sont responsables de fournir manuellement les autorisations d'accès nécessaires.

Ce guide vous montrera comment créer des `Service Account`, `Role`, et `RoleBinding` pour une instance MariaDB nommée `sample-mariadb` pour fournir le strict minimum d’autorisations d’accès.

## RBAC personnalisé pour MariaDB

Dans un premier temps, créons un `Service Acoount` dans `demo` espace de noms.

```bash
$ kubectl create serviceaccount -n demo md-custom-serviceaccount
serviceaccount/md-custom-serviceaccount created
```

Il devrait créer un compte de service.

```bash
$ kubectl get serviceaccount -n demo md-custom-serviceaccount -o yaml
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: "2021-03-18T04:38:59Z"
  name: md-custom-serviceaccount
  namespace: demo
  resourceVersion: "84669"
  selfLink: /api/v1/namespaces/demo/serviceaccounts/md-custom-serviceaccount
  uid: 788bd6c6-3eae-4797-b6ca-5722ef64c9dc
secrets:
- name: md-custom-serviceaccount-token-jnhvd
```

Maintenant, nous devons créer un rôle disposant des autorisations d'accès nécessaires pour l'instance MariaDB nommée `sample-mariadb`.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-role.yaml
role.rbac.authorization.k8s.io/md-custom-role created
```

Vous trouverez ci-dessous le YAML du rôle que nous venons de créer.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: md-custom-role
  namespace: demo
rules:
- apiGroups:
  - policy
  resourceNames:
  - maria-db
  resources:
  - podsecuritypolicies
  verbs:
  - use
```

Cette autorisation est requise pour les pods MariaDB exécutés sur des clusters compatibles PSP.

Créez maintenant un `RoleBinding` pour lier ça `Role` avec le compte de service déjà créé.

```bash
$ kubectl create rolebinding md-custom-rolebinding --role=md-custom-role --serviceaccount=demo:md-custom-serviceaccount --namespace=demo
rolebinding.rbac.authorization.k8s.io/md-custom-rolebinding created
```

Cela devrait lier `md-custom-role` et `md-custom-serviceaccount` avec succès.

Donc, toutes les ressources requises pour RBAC sont créées.

```bash
$ kubectl get serviceaccount,role,rolebindings -n demo
NAME                                      SECRETS   AGE
serviceaccount/default                    1         38m
serviceaccount/md-custom-serviceaccount   1         36m

NAME                                            CREATED AT
role.rbac.authorization.k8s.io/md-custom-role   2021-03-18T05:13:27Z

NAME                                                          ROLE                  AGE
rolebinding.rbac.authorization.k8s.io/md-custom-rolebinding   Role/md-custom-role   79s
```

Maintenant, créez un crd MariaDB spécifiant `spec.podTemplate.spec.serviceAccountName` champ à `md-custom-serviceaccount`.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-db.yaml
mariadb.kubedb.com/sample-mariadb created
```

Vous trouverez ci-dessous le YAML du crd MariaDB que nous venons de créer.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  podTemplate:
    spec:
      serviceAccountName: md-custom-serviceaccount
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Maintenant, attendez quelques minutes. l'opérateur KubeDB créera les PVC, PetSet, services, secrets etc. nécessaires. Si tout se passe bien, nous devrions voir qu'un pod avec le nom `sample-mariadb-0` a été créé.

Vérifiez que le pod du petset est en cours d'exécution

```bash
$ kubectl get pod -n demo sample-mariadb-0
NAME            READY   STATUS    RESTARTS   AGE
sample-mariadb-0   1/1     Running   0          2m44s
```

Vérifiez le journal du pod pour voir si la base de données est prête

```bash
$ kubectl logs -f -n demo sample-mariadb-0
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 05:35:13+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:35:14+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  5:35:22 0 [Note] Reading of all Master_info entries succeeded
2021-03-18  5:35:22 0 [Note] Added new Master_info '' to hash table
2021-03-18  5:35:22 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

Une fois qu'on voit `mysqld: ready for connections.` dans le journal, la base de données est prête.

## Réutilisation du compte de service

Un compte de service existant peut être réutilisé dans une autre instance MariaDB. Aucune nouvelle autorisation d'accès n'est requise pour exécuter la nouvelle instance MariaDB.

Maintenant, créez le crd MariaDB `another-mariadb` en utilisant le nom du compte de service existant `md-custom-serviceaccount` dans le `spec.podTemplate.spec.serviceAccountName` champ.

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/custom-rbac/using-custom-rbac/examples/md-custom-db-2.yaml
mariadb.kubedb.com/another-mariadb created
```

Vous trouverez ci-dessous le YAML du crd MariaDB que nous venons de créer.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: another-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  storageType: Durable
  podTemplate:
    spec:
      serviceAccountName: md-custom-serviceaccount
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Maintenant, attendez quelques minutes. l'opérateur KubeDB créera le PVC, le petset, les services, le secret, etc. nécessaires. Si tout se passe bien, nous devrions voir qu'un pod avec le nom `another-mariadb` a été créé.

Vérifiez que le pod du petset est en cours d'exécution

```bash
$ kubectl get pod -n demo another-mariadb-0
NAME                READY   STATUS    RESTARTS   AGE
another-mariadb-0   1/1     Running   0          37s
```

Vérifiez le journal du pod pour voir si la base de données est prête

```bash
...
$ kubectl logs -f -n demo another-mariadb-0
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:11.8.5+maria~focal started.
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:10.5.23+maria~focal started.
2021-03-18 05:39:50+00:00 [Note] [Entrypoint]: Initializing database files
...
2021-03-18  5:39:59 0 [Note] mysqld: ready for connections.
Version: '11.8.5-MariaDB-1:11.8.5+maria~focal'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

`mysqld: ready for connections.` dans le journal signifie que la base de données fonctionne correctement.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo sample-mariadb
mariadb.kubedb.com "sample-mariadb" deleted
$ kubectl delete mariadb -n demo another-mariadb
mariadb.kubedb.com "another-mariadb" deleted
$ kubectl delete -n demo role md-custom-role
role.rbac.authorization.k8s.io "md-custom-role" deleted
$ kubectl delete -n demo rolebinding md-custom-rolebinding
rolebinding.rbac.authorization.k8s.io "md-custom-rolebinding" deleted
$ kubectl delete sa -n demo md-custom-serviceaccount
serviceaccount "md-custom-serviceaccount" deleted
$ kubectl delete ns demo
namespace "demo" deleted
```