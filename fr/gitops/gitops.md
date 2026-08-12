> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# GitOps MariaDB utilisant l'opérateur KubeDB GitOps

Ce guide vous montrera comment utiliser `KubeDB` Opérateur GitOps pour créer la base de données MariaDB et gérer les mises à jour à l'aide du workflow GitOps.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer `KubeDB` opérateur dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README). Passer `--set kubedb-crd-manager.installGitOpsCRDs=true` dans le processus d'installation de kubedb pour activer `GitOps` opérateur.
* Vous devez installer des outils GitOps comme `ArgoCD` ou `FluxCD` et configurez avec votre référentiel Git pour surveiller le référentiel Git et synchroniser l'état du cluster Kubernetes avec l'état souhaité défini dans Git.

  ```bash
  $ kubectl create ns monitoring
  namespace/monitoring created

  $ kubectl create ns demo
  namespace/demo created
  ```

> Remarque : les fichiers YAML utilisés dans ce didacticiel sont stockés dans [docs/exemples/mariadb](https://github.com/kubedb/docs/tree/v2026.7.10/docs/examples/mariadb) dossier dans le référentiel GitHub [kubedb/docs](https://github.com/kubedb/docs).

Nous allons utiliser `ArgoCD` dans ce tutoriel. Vous pouvez installer `ArgoCD` dans votre cluster en suivant les étapes [ici](https://argo-cd.readthedocs.io/en/stable/getting_started/). De plus, vous devez installer `argocd` CLI sur votre ordinateur local. Vous pouvez installer `argocd` CLI en suivant les étapes [ici](https://argo-cd.readthedocs.io/en/stable/cli_installation/).

## Création d'applications via CLI

### Pour le référentiel public

```bash
argocd app create kubedb --repo <repo-url> --path kubedb --dest-server https://kubernetes.default.svc --dest-namespace <namespace>
```

### Pour le référentiel privé

#### Utiliser HTTPS

```bash
argocd app create kubedb --repo <repo-url> --path kubedb --dest-server https://kubernetes.default.svc --dest-namespace <namespace> --username <username> --password <github-token>
```

#### Utiliser SSH

Enregistrement d'un référentiel Git dans Argo CD à l'aide de l'authentification SSH

```bash
argocd repo add <ssh-repo-url> \
  --ssh-private-key-path <path-to-private-key>
```

Création d'une application Argo CD pour déployer les ressources du référentiel dans un cluster Kubernetes

```bash
argocd app create <application-name> \
  --repo <repository-url> \
  --path <repository-path> \
  --dest-server <kubernetes-api-server> \
  --dest-namespace <target-namespace>
```

## Créer une base de données MariaDB à l'aide de GitOps

### Créer un CR GitOps MariaDB

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Créez un répertoire comme ci-dessous,

```bash
$ tree .
├── kubedb
    └── MariaDB.yaml
1 directories, 1 files
```

Maintenant, validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est créé dans votre cluster.

Notre `gitops` l'opérateur créera un véritable `MariaDB` base de données CR dans le cluster. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get mariaDB.gitops.kubedb.com,mariaDB.kubedb.com -n demo
NAME                                       AGE
mariadb.gitops.kubedb.com/mariadb-gitops   22m

NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    22m
```

Répertoriez les ressources créées par `kubedb` opérateur créé pour `kubedb.com/v1` MariaDB.

```bash
$ kubectl get petset,pod,secret,service,appbinding -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME                                          AGE
petset.apps.k8s.appscode.com/mariadb-gitops   22m

NAME                   READY   STATUS    RESTARTS   AGE
pod/mariadb-gitops-0   2/2     Running   0          22m
pod/mariadb-gitops-1   2/2     Running   0          22m
pod/mariadb-gitops-2   2/2     Running   0          22m

NAME                         TYPE                       DATA   AGE
secret/mariadb-gitops-auth   kubernetes.io/basic-auth   2      22m

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/mariadb-gitops        ClusterIP   10.43.215.232   <none>        3306/TCP   22m
service/mariadb-gitops-pods   ClusterIP   None            <none>        3306/TCP   22m

NAME                                                TYPE                 VERSION   AGE
appbinding.appcatalog.appscode.com/mariadb-gitops   kubedb.com/mariadb   11.8.5    22m
```

## Mettre à jour la base de données MariaDB à l'aide de GitOps

### Faire évoluer les ressources de la base de données MariaDB

Avant de mettre à l'échelle les ressources de la base de données :

```shell
$ kubectl get pod -n demo mariadb-gitops-0 -o json | jq '.spec.containers[0].resources'
{
  "limits": {
    "memory": "1Gi"
  },
  "requests": {
    "cpu": "500m",
    "memory": "1Gi"
  }
}
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 3
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Les demandes et limites de ressources sont mises à jour pour `600m` Processeur et `1.2Gi` Mémoire. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de ressources et créera un `MariaDBOpsRequest` pour mettre à jour le `MariaDB` base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    39m

NAME                                                                     TYPE              STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268   VerticalScaling   Successful   9m17s
```

Une fois que la demande d'opérations devient `Successful`, On peut valider les changements en vérifiant celui du pod,

```bash
$ kubectl get pod -n demo mariadb-gitops-0 -o json | jq '.spec.containers[0].resources'
{
  "limits": {
    "cpu": "600m",
    "memory": "1288490188800m"
  },
  "requests": {
    "cpu": "600m",
    "memory": "1288490188800m"
  }
}
```

### Mettre à l'échelle les répliques MariaDB

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

Mettre à jour le `replicas` à `5`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.
Maintenant, `gitops` L'opérateur détectera les modifications de la réplique et créera un `HorizontalScaling` MariaDBOpsRequest pour mettre à jour le `MariaDB` répliques de bases de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    107m

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   63m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   76m
```

Une fois que la demande d'opérations devient `Successful`, On peut valider les modifications en vérifiant le nombre de pods,

```bash
$ kubectl get pod -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME               READY   STATUS    RESTARTS   AGE
mariadb-gitops-0   2/2     Running   0          76m
mariadb-gitops-1   2/2     Running   0          75m
mariadb-gitops-2   2/2     Running   0          73m
mariadb-gitops-3   2/2     Running   0          63m
mariadb-gitops-4   2/2     Running   0          62m
```

Nous pouvons également réduire les répliques en mettant à jour le `replicas` champs.

### Développer le volume MariaDB

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
```

Mettre à jour le `storage.resources.requests.storage` à `2Gi`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de volume et créera un `VolumeExpansion` MariaDBOpsRequest pour mettre à jour le `MariaDB` volume de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    111m

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   68m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   81m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   115s
```

Une fois que la demande d'opérations devient `Successful`, Nous pouvons valider les modifications en vérifiant la taille du pvc,

```bash
$ kubectl get pvc -n demo -l 'app.kubernetes.io/instance=mariadb-gitops'
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
data-mariadb-gitops-0   Bound    pvc-f1a49c53-d095-43a7-b62f-e91a5a9f5496   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-1   Bound    pvc-79d99636-e0d7-413f-a6a6-559e908ed817   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-2   Bound    pvc-f66ccf56-63b6-4ac6-a7f9-09f573466266   2Gi        RWO            longhorn       <unset>                 116m
data-mariadb-gitops-3   Bound    pvc-b7744652-611a-4c10-a06f-c93f030fb90f   2Gi        RWO            longhorn       <unset>                 72m
data-mariadb-gitops-4   Bound    pvc-dee1c10d-0456-4935-9306-0d86c3db54d0   2Gi        RWO            longhorn       <unset>                 71m
```

## Reconfigurer MariaDB

Dans un premier temps, nous allons créer un secret contenant `user.conf` fichier avec les paramètres de configuration requis.
Pour en savoir plus sur ce fichier de configuration, consultez [ici](../reconfigure/overview.md)

```yaml
apiVersion: v1
stringData:
  user.cnf: |
    [mysqld]
    max_connections = 200
    read_buffer_size = 1048576    
kind: Secret
metadata:
  name: md-configuration
  namespace: demo
type: Opaque
```

Maintenant, nous allons ajouter ce fichier à `kubedb/md-configuration.yaml`.

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ └── mariadb.yaml
1 directories, 2 files
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
```

Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD`, le fichier de reconfiguration est créé le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de configuration et créera un `Reconfigure` MariaDBOpsRequest pour mettre à jour le `MariaDB` configuration de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    17h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   17h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

### Faire pivoter l'authentification MariaDB

Pour ce faire, créez un `kubernetes.io/basic-auth` tapez k8s secret avec le nouveau nom d'utilisateur et le nouveau mot de passe.

Nous allons faire cela en utilisant gitops, créez le fichier `kubedb/md-auth.yaml` avec le contenu suivant,

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mdauth
  namespace: demo
type: kubernetes.io/basic-auth
stringData:
  username: root
  password: md-secret
```

Ajoutons cela à notre `kubedb/md-auth.yaml` déposer. La structure du fichier ressemblera à ceci,

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ ├── md-auth.yaml
│ └── MariaDB.yaml
1 directories, 3 files
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
```

Changer le `authSecret` champ à `mdauth`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel a été synchronisé avec succès avec ArgoCD. Le `MariaDB` CR a été mis à jour et le fichier d'authentification a été créé dans le cluster.

Maintenant, `gitops` L'opérateur détectera les changements d'authentification et créera un `RotateAuth` MariaDBOpsRequest pour mettre à jour le `MariaDB` authentification de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   12m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

### Configuration TLS

Nous pouvons ajouter, faire pivoter ou supprimer la configuration TLS en utilisant `gitops`.

Maintenant, nous allons créer un exemple `Issuer` qui sera utilisé tout au long de ce tutoriel. Alternativement, vous pouvez suivre ceci [tutoriel du gestionnaire de certificats](https://cert-manager.io/docs/configuration/ca/) pour créer le vôtre `Issuer`. En suivant les étapes ci-dessous, nous allons créer l'émetteur souhaité,

* Commencez par générer nos certificats ca en utilisant openssl,

```bash
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./ca.key -out ./ca.crt -subj "/CN=mariadb/O=kubedb"
Generating a RSA private key
...........................................................................+++++
........................................................................................................+++++
writing new private key to './ca.key'
```

* créer un secret en utilisant les fichiers de certificat que nous venons de générer,

```bash
$ kubectl create secret tls md-ca \
  --cert=ca.crt \
  --key=ca.key \
  -n demo
```

Maintenant, nous allons créer un `Issuer` en utilisant le `md-ca` secret que renferme le certificat ca que nous venons de créer. Vous trouverez ci-dessous le YAML du `Issuer` cr que nous allons créer,

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: md-issuer
  namespace: demo
spec:
  ca:
    secretName: md-ca
```

Créons le `Issuer` cr nous l'avons montré ci-dessus,

```bash
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

Ajoutons cela à notre `kubedb/md-issuer.yaml` déposer. La structure du fichier ressemblera à ceci,

```bash
$ tree .
├── kubedb
│ ├── md-configuration.yaml
│ ├── md-auth.yaml
│ ├── md-secret.yaml
│ ├── md-issuer.yaml
│ └── MariaDB.yaml
1 directories, 5 files
```

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "11.8.5"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
```

Ajouter `requireSSL` comme `true` et `tls` champs dans la spécification. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel a été synchronisé avec succès avec ArgoCD. Le `MariaDB` CR a été mis à jour et les deux `issuer` et le correspondant `secret` ont été créés dans le cluster.

Maintenant, `gitops` L'opérateur détectera les modifications tls et créera un `ReconfigureTLS` MariaDBOpsRequest pour mettre à jour le `MariaDB` base de données tls. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$  kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   11.8.5    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   8m20s
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   35m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   18h
```

> Nous pouvons également alterner la mise à jour des certificats `.spec.tls.certificates` champ. Vous pouvez également supprimer le `.spec.tls` champ pour supprimer tls pour MariaDB.

### Version mise à jour

Répertorier les versions de MariaDB en utilisant `kubectl get MariaDBversion` et choisissez la version souhaitée qui est compatible pour la mise à niveau à partir de la version actuelle. Vérifiez les contraintes de version et la demande d'opérations [ici](../update-version/overview.md).

Choisissons `12.1.2` dans cet exemple.

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
```

Mettre à jour le `version` champ à `12.1.2`. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de version et créera un `VersionUpdate` MariaDBOpsRequest pour mettre à jour le `MariaDB` version de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   12.1.2    Ready    18h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   18h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   24m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   51m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-versionupdate-ksli15       UpdateVersion       Successful   10m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   19h
```

Nous allons maintenant vérifier si le `MariaDB`, `PetSet` et c'est `Pod` ont été mis à jour avec une nouvelle image. Vérifions,

```bash
$ kubectl get MariaDB -n demo mariadb-gitops -o=jsonpath='{.spec.version}{"\n"}'
12.1.2
$ kubectl get petset -n demo mariadb-gitops -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
ghcr.io/appscode-images/mariadb:12.1.2-noble@sha256:843852d8651b3f321896a4a91f8118605d988d70703e520927c8d2c9313aded4
$ kubectl get pod -n demo mariadb-gitops-0 -o=jsonpath='{.spec.containers[0].image}{"\n"}'
ghcr.io/appscode-images/mariadb:12.1.2-noble@sha256:843852d8651b3f321896a4a91f8118605d988d70703e520927c8d2c9313aded4
```

### Activer la surveillance

Si vous n'avez pas encore de serveur Prometheus en cours d'exécution, déployez le didacticiel suivant à partir de [ici](https://github.com/appscode/third-party-tools/blob/master/monitoring/prometheus/operator/README.md#deploy-prometheus-server).

Mettre à jour le `MariaDB.yaml` avec ce qui suit,

```yaml
apiVersion: gitops.kubedb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-gitops
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 5
  podTemplate:
    spec:
      containers:
      - name: mariadb
        resources:
          requests:
            memory: "1.2Gi"
            cpu: "0.6"
          limits:
            memory: "1.2Gi"
            cpu: "0.6"
  storageType: Durable
  deletionPolicy: WipeOut
  storage:
    storageClassName: longhorn
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 2Gi
  configuration:
    secretName: md-configuration
  authSecret:
    kind: Secret
    name: mdauth
  requireSSL: true
  tls:
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      dnsNames:
      - localhost
      ipAddresses:
      - "127.0.0.1"
  monitor:
    agent: prometheus.io/operator
    prometheus:
      serviceMonitor:
        labels:
          release: prometheus
        interval: 10s
```

Ajouter `monitor` champ dans la spécification. Validez les modifications et transférez-les vers votre référentiel Git. Votre référentiel est synchronisé avec `ArgoCD` et le `MariaDB` CR est mis à jour dans votre cluster.

Maintenant, `gitops` L'opérateur détectera les changements de surveillance et créera un `Restart` MariaDBOpsRequest pour ajouter le `MariaDB` surveillance de la base de données. Répertoriez les ressources créées par `gitops` opérateur dans le `demo` espace de noms.

```bash
$ kubectl get md,mariadbopsrequest -n demo
NAME                                VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb-gitops   12.1.2    Ready    19h

NAME                                                                       TYPE                STATUS       AGE
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-horizontalscaling-m7iex7   HorizontalScaling   Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfigure-1leaj8         Reconfigure         Successful   19h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-reconfiguretls-ftyfdq      ReconfigureTLS      Successful   40m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-restart-e7rv89             Restart             Successful   8m26s
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-rotate-auth-1xy3d7         RotateAuth          Successful   67m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-versionupdate-ksli15       UpdateVersion       Successful   26m
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-verticalscaling-rjs268     VerticalScaling     Successful   20h
mariadbopsrequest.ops.kubedb.com/mariadb-gitops-volumeexpansion-01m39b     VolumeExpansion     Successful   19h
```

Vérifiez que la surveillance est activée en vérifiant les cibles prometheus.

## Prochaines étapes

* Apprendre la mise à l'échelle de MariaDB
  + [Mise à l'échelle horizontale](../scaling/horizontal-scaling/overview.md)
  + [Mise à l'échelle verticale](../scaling/vertical-scaling/overview.md)
* Apprendre la demande et les contraintes des opérations de mise à jour de version [ici](../update-version/overview.md)
* Surveillez votre base de données MariaDBQL avec KubeDB en utilisant [Prometheus intégré](../monitoring/prometheus-operator.md).
* Vous voulez pirater KubeDB ? Consultez notre [directives de contribution](https://kubedb.com/docs/v2026.7.10/CONTRIBUTING).