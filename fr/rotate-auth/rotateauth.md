# Rotation de l'authentification de MariaDB

**Rotation de l'authentification** est une fonctionnalité de KubeDB Ops-Manager qui vous permet de faire pivoter un `MariaDB` les informations d'authentification de l'utilisateur à l'aide d'un `MariaDBOpsRequest`. Il existe deux manières d'effectuer cette rotation.

1. **Opérateur généré :** L'opérateur KubeDB génère automatiquement un identifiant aléatoire, met à jour le secret existant avec le nouveau identifiant. L'opérateur KubeDB génère automatiquement un identifiant aléatoire et met à jour le secret existant avec le nouveau identifiant.
2. **Défini par l'utilisateur :** L'utilisateur peut créer ses propres identifiants en définissant un Secret de type `kubernetes.io/basic-auth` contenant le souhaité `password` puis faites référence à ce secret dans le `MariaDBOpsRequest`.

## Avant de commencer

* Vous devriez être familier avec ce qui suit `KubeDB` notions :

  + [MariaDB](../concepts/mariadb.md)
  + [MariaDBOpsRequest](../concepts/mariadb.md)
* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Créer une base de données MariaDB

KubeDB implémente un `MariaDB` CRD pour définir la spécification d'une base de données MariaDB. Ci-dessous se trouve le `MariaDB` objet créé dans ce tutoriel.

`Note`: Si votre `KubeDB version` est inférieur ou égal à `v2024.6.4`, Vous devez utiliser `v1alpha2` apiVersion.

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
  deletionPolicy: Delete
```

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/quickstart/overview/examples/sample-mariadb-v1.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attendez que sample-mariadb ait le statut Prêt. c'est-à-dire,

```shell
$ kubectl get mariadb -n demo -w
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5   Ready    30m
```

## Vérifier l'authentification

L'utilisateur peut vérifier s'il est autorisé en exécutant une requête directement dans la base de données. Pour ce faire, l'utilisateur a besoin `username` et `password` afin de se connecter à la base de données en utilisant le `kubectl exec` commande. Vous trouverez ci-dessous un exemple montrant comment récupérer les informations d'identification du secret.

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth"
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.username}' | base64 -d
root⏎                                  
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.password}' | base64 -d
s)cJQ*iL8wHySpvT⏎
```

Maintenant, vous pouvez exécuter dans le pod `sample-mariadb` et connectez-vous à la base de données en utilisant `username` et `password`

```shell
$ kubectl exec -it -n demo sample-mariadb-0 -- mariadb -u root --password='s)cJQ*iL8wHySpvT'
Defaulted container "mariadb" out of: mariadb, mariadb-init (init)
```

```mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 207
Server version: 11.8.5-MariaDB-1:11.8.5+maria~ubu2004 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.000 sec)

MariaDB [(none)]> CREATE DATABASE Bharatnaityam;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| Bharatnaityam      |
| information_schema |
| kubedb_system      |
| mysql              |
| performance_schema |
+--------------------+
5 rows in set (0.000 sec)
```

Si vous pouvez accéder à la table de données et exécuter des requêtes, cela signifie que les secrets fonctionnent correctement.

## Créer RotateAuth MariaDBOpsRequest

#### 1. Utilisation des informations d'identification générées par l'opérateur :

Afin de faire pivoter l'authentification vers `MariaDB` en utilisant l'opérateur généré, nous devons créer un
CR `MariaDBOpsRequest` de type `RotateAuth`. Vous trouverez ci-dessous le YAML du CR `MariaDBOpsRequest` que nous
allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-auth-generated
  namespace: demo
spec:
  type: RotateAuth
  databaseRef:
    name: sample-mariadb
  timeout: 5m
  apply: IfReady
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération d'authentification par rotation sur
  `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `RotateAuth` sur MariaDB.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```shell
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/rotate-auth/overview/examples/Mariadb-rotate-auth-generated.yaml
 mariadbopsrequest.ops.kubedb.com/mdops-rotate-auth-generated created
```

Attendons `MariaDBOpsrequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsrequest` CRO

```shell
$ kubectl get Mariadbopsrequest -n demo
NAME                          TYPE         STATUS       AGE
mdops-rotate-auth-generated   RotateAuth   Successful   6m28s
```

Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies.

```shell
$ kubectl describe Mariadbopsrequest -n demo mdops-rotate-auth-generated
Name:         mdops-rotate-auth-generated
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-11T06:43:21Z
  Generation:          1
  Resource Version:    635526
  UID:                 fdf5a041-9403-4c0b-a788-2adad326dd88
Spec:
  Apply:  IfReady
  Database Ref:
    Name:   sample-mariadb
  Timeout:  5m
  Type:     RotateAuth
Status:
  Conditions:
    Last Transition Time:  2025-07-11T06:43:21Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-11T06:43:24Z
    Message:               Successfully generated new credentials
    Observed Generation:   1
    Reason:                patchedSecret
    Status:                True
    Type:                  UpdateCredential
    Last Transition Time:  2025-07-11T06:43:32Z
    Message:               evict pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  EvictPod--sample-mariadb-0
    Last Transition Time:  2025-07-11T06:43:32Z
    Message:               get pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  GetPod--sample-mariadb-0
    Last Transition Time:  2025-07-11T06:44:07Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                UpdatePetSetsSucceeded
    Status:                True
    Type:                  UpdatePetSets
    Last Transition Time:  2025-07-11T06:44:12Z
    Message:               Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                UpdateCredential
    Status:                True
    Type:                  RotateAuth
    Last Transition Time:  2025-07-11T06:44:12Z
    Message:               Controller has successfully rotate MariaDB auth secret demo/mdops-rotate-auth-generated
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                                                     Age    From                         Message
  ----     ------                                                     ----   ----                         -------
  Normal   Starting                                                   9m17s  KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Starting                                                   9m17s  KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal   Successful                                                 9m17s  KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-rotate-auth-generated
  Normal   Starting                                                   9m6s   KubeDB Ops-manager Operator  Restarting Pod: demo/sample-mariadb-0
  Warning  evict pod; ConditionStatus:True; PodName:sample-mariadb-0  9m6s   KubeDB Ops-manager Operator  evict pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    9m6s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    9m1s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    8m31s  KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Normal   Successful                                                 8m31s  KubeDB Ops-manager Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-generated
  Normal   Starting                                                   8m26s  KubeDB Ops-manager Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 8m26s  KubeDB Ops-manager Operator  Controller has successfully rotate MariaDB auth secret
```

**Vérifiez que l'authentification est pivotée**

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth"
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.username}' | base64 -d
root⏎                                                               
$ kubectl get secret -n demo sample-mariadb-auth -o=jsonpath='{.data.password}' | base64 -d
gTJJMdgpKy9U(Eqi⏎
```

En outre, il y aura deux nouvelles clés supplémentaires dans le secret qui stocke les informations d'identification précédentes. Les clés sont `username.prev` et `password.prev`. Vous pouvez trouver le secret et ses données en exécutant la commande suivante :

```shell
$ kubectl get secret -n demo sample-mariadb-auth -o go-template='{{ index .data "username.prev" }}' | base64 -d
root⏎                                                                                                          
$ kubectl get secret -n demo sample-mariadb-auth -o go-template='{{ index .data "password.prev" }}' | base64 -d
s)cJQ*iL8wHySpvT⏎
```

Le résultat ci-dessus montre que le mot de passe a été modifié avec succès. Le nom d'utilisateur et le mot de passe précédents sont stockés à des fins de restauration.

#### 2. Utilisation des informations d'identification créées par l'utilisateur

Dans un premier temps, nous devons créer un secret avec le type kubernetes.io/basic-auth en utilisant un nom d'utilisateur et un mot de passe personnalisés. Vous trouverez ci-dessous la commande pour créer un secret avec le type kubernetes.io/basic-auth,

> Remarque : Vous ne pouvez pas modifier la base de données `username`, mais vous pouvez mettre à jour le `password` tout en gardant l'existant `username`.

```shell
$ kubectl create secret generic sample-mariadb-auth-user -n demo \
   --type=kubernetes.io/basic-auth \
   --from-literal=username=root \
   --from-literal=password=testpassword
secret/sample-mariadb-auth-user created
```

Créez maintenant un CR `MariaDBOpsRequest` de type `RotateAuth`. Vous trouverez ci-dessous le YAML du CR `MariaDBOpsRequest` que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-auth-user
  namespace: demo
spec:
  type: RotateAuth
  databaseRef:
    name: sample-mariadb
  authentication:
    secretRef:
      kind: Secret
      name: sample-mariadb-auth-user
  timeout: 5m
  apply: IfReady
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération d'authentification par rotation sur `sample-mariadb`grappe.
* `spec.type` précise que nous effectuons `RotateAuth` sur `MariaDB`.
* `spec.authentication.secretRef.name` précise que nous utilisons `sample-mariadb-auth-user` comme `spec.authSecret.name` pour l'authentification.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```shell
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/rotate-auth/overview/examples/rotate-auth-user.yaml
mariadbopsrequest.ops.kubedb.com/mdops-rotate-auth-user created
```

Attendons `MariaDBOpsRequest` pour réussir. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO :

```shell
$ kubectl get Mariadbopsrequest -n demo
NAME                          TYPE         STATUS       AGE
mdops-rotate-auth-generated   RotateAuth   Successful   100s
mdops-rotate-auth-user        RotateAuth   Successful   62s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies.

```shell
$  kubectl describe Mariadbopsrequest -n demo mdops-rotate-auth-user
Name:         mdops-rotate-auth-user
Namespace:    demo
Labels:       <none>
Annotations:  <none>
API Version:  ops.kubedb.com/v1alpha1
Kind:         MariaDBOpsRequest
Metadata:
  Creation Timestamp:  2025-07-14T06:56:25Z
  Generation:          1
  Resource Version:    665963
  UID:                 6c30dc56-6ca9-4707-8b7c-5d4da6a1b585
Spec:
  Apply:  IfReady
  Authentication:
    Secret Ref:
      Name:  sample-mariadb-auth-user
  Database Ref:
    Name:   sample-mariadb
  Timeout:  5m
  Type:     RotateAuth
Status:
  Conditions:
    Last Transition Time:  2025-07-14T06:56:25Z
    Message:               Controller has started to Progress the MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                Running
    Status:                True
    Type:                  Running
    Last Transition Time:  2025-07-14T06:56:28Z
    Message:               Successfully referenced the user provided authSecret
    Observed Generation:   1
    Reason:                patchedSecret
    Status:                True
    Type:                  UpdateCredential
    Last Transition Time:  2025-07-14T06:56:35Z
    Message:               evict pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  EvictPod--sample-mariadb-0
    Last Transition Time:  2025-07-14T06:56:35Z
    Message:               get pod; ConditionStatus:True; PodName:sample-mariadb-0
    Observed Generation:   1
    Status:                True
    Type:                  GetPod--sample-mariadb-0
    Last Transition Time:  2025-07-14T06:56:40Z
    Message:               Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                UpdatePetSetsSucceeded
    Status:                True
    Type:                  UpdatePetSets
    Last Transition Time:  2025-07-14T06:56:45Z
    Message:               Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                UpdateCredential
    Status:                True
    Type:                  RotateAuth
    Last Transition Time:  2025-07-14T06:56:45Z
    Message:               Controller has successfully rotate MariaDB auth secret demo/mdops-rotate-auth-user
    Observed Generation:   1
    Reason:                Successful
    Status:                True
    Type:                  Successful
  Observed Generation:     1
  Phase:                   Successful
Events:
  Type     Reason                                                     Age   From                         Message
  ----     ------                                                     ----  ----                         -------
  Normal   Starting                                                   83s   KubeDB Ops-manager Operator  Start processing for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Starting                                                   83s   KubeDB Ops-manager Operator  Pausing MariaDB databse: demo/sample-mariadb
  Normal   Successful                                                 83s   KubeDB Ops-manager Operator  Successfully paused MariaDB database: demo/sample-mariadb for MariaDBOpsRequest: mdops-rotate-auth-user
  Normal   Starting                                                   73s   KubeDB Ops-manager Operator  Restarting Pod: demo/sample-mariadb-0
  Warning  evict pod; ConditionStatus:True; PodName:sample-mariadb-0  73s   KubeDB Ops-manager Operator  evict pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    73s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Warning  get pod; ConditionStatus:True; PodName:sample-mariadb-0    68s   KubeDB Ops-manager Operator  get pod; ConditionStatus:True; PodName:sample-mariadb-0
  Normal   Successful                                                 68s   KubeDB Ops-manager Operator  Successfully restarted MariaDB pods for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Successfully rotate MariaDB auth for MariaDBOpsRequest: demo/mdops-rotate-auth-user
  Normal   Starting                                                   63s   KubeDB Ops-manager Operator  Resuming MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Successfully resumed MariaDB database: demo/sample-mariadb
  Normal   Successful                                                 63s   KubeDB Ops-manager Operator  Controller has successfully rotate MariaDB auth secret
```

**Vérifiez que l'authentification est en rotation**

```shell
$ kubectl get mariadb -n demo sample-mariadb -ojson | jq .spec.authSecret.name
"sample-mariadb-auth-user"
$ kubectl get secret -n demo sample-mariadb-auth-user -o=jsonpath='{.data.username}' | base64 -d
root⏎                                                                    
$ kubectl get secret -n demo sample-mariadb-auth-user -o=jsonpath='{.data.password}' | base64 -d
testpassword⏎
```

En outre, il y aura deux nouvelles clés supplémentaires dans le secret qui stocke les informations d'identification précédentes. Les clés sont `username.prev` et `password.prev`. Vous pouvez trouver le secret et ses données en exécutant la commande suivante :

```shell
$ kubectl get secret -n demo sample-mariadb-auth-user -o go-template='{{ index .data "username.prev" }}' | base64 -d
root⏎                                                                                                          
$ kubectl get secret -n demo sample-mariadb-auth-user -o go-template='{{ index .data "password.prev" }}' | base64 -d
gTJJMdgpKy9U(Eqi⏎
```

Le résultat ci-dessus montre que le mot de passe a été modifié avec succès. Le nom d'utilisateur et le mot de passe précédents sont stockés dans le secret à des fins de restauration.

## Nettoyage

Pour nettoyer les ressources Kubernetes, vous pouvez supprimer le CRD ou l'espace de noms.
Ou, vous pouvez supprimer une ressource une par une par son nom grâce à ce tutoriel, exécutez :

```shell
$ kubectl delete Mariadbopsrequest mdops-rotate-auth-generated mdops-rotate-auth-user -n demo
mariadbopsrequest.ops.kubedb.com "mdops-rotate-auth-generated" deleted
mariadbopsrequest.ops.kubedb.com "mdops-rotate-auth-user" deleted
$ kubectl delete secret -n demo  sample-mariadb-auth-user
secret "sample-mariadb-auth-user" deleted
$ kubectl delete secret -n demo  sample-mariadb-auth
secret "sample-mariadb-auth" deleted
```

## Prochaines étapes

* Vous souhaitez contribuer à KubeDB ? Consultez nos [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).