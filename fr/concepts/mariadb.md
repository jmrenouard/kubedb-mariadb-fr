> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# MariaDB

## Qu'est-ce que MariaDB

`MariaDB` est un Kubernetes `Custom Resource Definitions` (CRD). Il fournit une configuration déclarative pour MariaDB de manière native Kubernetes. Il vous suffit de décrire la configuration de base de données souhaitée dans un objet MariaDB, et l'opérateur KubeDB créera pour vous les objets Kubernetes dans l'état souhaité.

## Spécification MariaDB

Comme pour tous les autres objets Kubernetes, une MariaDB a besoin `apiVersion`, `kind`, et `metadata` champs. Il faut également un `.spec` section. Vous trouverez ci-dessous un exemple d'objet MariaDB.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  authSecret:
    kind: Secret
    name: sample-mariadb-auth
  monitor:
    agent: prometheus.io
    prometheus:
      exporter:
        port: 56790
        resources: {}
      serviceMonitor:
        interval: 10s
        labels:
          release: prometheus
  podTemplate:
    controller: {}
    metadata: {}
    spec:
      containers:
      - name: mariadb
        resources:
          limits:
            cpu: 500m
            memory: 1Gi
          requests:
            cpu: 500m
            memory: 1Gi
      serviceAccountName: sample-mariadb
  replicas: 3
  requireSSL: true
  storage:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
    storageClassName: standard
  storageType: Durable
  deletionPolicy: WipeOut
  tls:
    certificates:
    - alias: server
      dnsNames:
      - localhost
      ipAddresses:
      - 127.0.0.1
      secretName: sample-mariadb-server-cert
      subject:
        organizations:
        - kubedb:server
    - alias: archiver
      secretName: sample-mariadb-archiver-cert
    - alias: metrics-exporter
      secretName: sample-mariadb-metrics-exporter-cert
    issuerRef:
      apiGroup: cert-manager.io
      kind: Issuer
      name: md-issuer
  version: 12.1.2
```

### spec.version

`spec.version` est un champ obligatoire précisant le nom du [Version MariaDB](mariadb-version.md) crd où les images du docker sont spécifiées. Actuellement, lorsque vous installez KubeDB, cela crée ce qui suit : `MariaDBVersion` ressources,

* `12.1.2`, `10.4.32`

### spec.authSecret

`spec.authSecret` est un champ facultatif qui pointe vers un secret utilisé pour conserver les informations d'identification de `mariadb` utilisateur root. S'il n'est pas défini, l'opérateur KubeDB crée un nouveau secret `{mariadb-object-name}-auth` pour stocker le mot de passe pour `mariadb` utilisateur root pour chaque objet MariaDB. Si vous souhaitez utiliser un secret existant, veuillez le préciser lors de la création de l'objet MariaDB à l'aide de `spec.authSecret.name`.

Ce secret contient un `username` clé et un `password` clé qui contient le `username` et `password` respectivement pour `mariadb` utilisateur root. Ici, la valeur de `username` la clé est fixée pour être `root`.

Les secrets fournis par les utilisateurs ne sont pas gérés par KubeDB et ne seront donc pas modifiés ni récupérés par l'opérateur KubeDB (version 0.13.0 et supérieure).

Exemple:

```bash
kubectl create secret generic mariadb-auth -n demo \
    --from-literal=username=root \
    --from-literal=password=6q8u_2jMOW-OOZXk
secret/mariadb-auth created
```

```yaml
apiVersion: v1
data:
  password: NnE4dV8yak1PVy1PT1pYaw==
  username: cm9vdA==
kind: Secret
metadata:
  name: mariadb-auth
  namespace: demo
type: Opaque
```

### spec.storageType

`spec.storageType` est un champ facultatif qui spécifie le type de stockage à utiliser pour la base de données. Cela peut être soit `Durable` ou `Ephemeral`. La valeur par défaut de ce champ est `Durable`. Si `Ephemeral` est utilisé, KubeDB créera la base de données MariaDB en utilisant [videDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volume. Dans ce cas, vous n’êtes pas obligé de préciser `spec.storage` champ.

### spec.storage

Si vous définissez `spec.storageType:` à `Durable`, alors `spec.storage` est un champ obligatoire qui spécifie la StorageClass des PVC alloués dynamiquement pour stocker les données de la base de données. Cette spécification de stockage sera transmise au PetSet créé par l'opérateur KubeDB pour exécuter les pods de base de données. Vous pouvez spécifier n'importe quelle StorageClass disponible dans votre cluster avec les demandes de ressources appropriées.

* `spec.storage.storageClassName` est le nom de la StorageClass utilisée pour provisionner les PVC. Les PVC ne doivent pas nécessairement demander un cours. Un PVC avec son storageClassName défini sur "" est toujours interprété comme demandant un PV sans classe, il ne peut donc être lié qu'à des PV sans classe (pas d'annotation ou un ensemble égal à ""). Un PVC sans storageClassName n'est pas tout à fait le même et est traité différemment par le cluster selon que le plugin d'admission DefaultStorageClass est activé ou non.
* `spec.storage.accessModes` utilise les mêmes conventions que les PVC Kubernetes lors de la demande de stockage avec des modes d'accès spécifiques.
* `spec.storage.resources` peut être utilisé pour demander des quantités spécifiques de stockage. Cela suit le même modèle de ressources utilisé par les PVC.

Pour apprendre à configurer `spec.storage`, veuillez consulter les liens ci-dessous :

* <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims>

### spec.init

`spec.init` est une section facultative qui peut être utilisée pour initialiser une base de données MariaDB nouvellement créée. Les bases de données MariaDB peuvent être initialisées de deux manières :

* Initialiser à partir du script
* Initialiser à partir de la restauration du stockage

#### Initialiser via un script

Pour initialiser une base de données MariaDB à l'aide d'un script (script shell, script sql, etc.), définissez le `spec.init.script` lors de la création d'un objet MariaDB. Il exécutera les fichiers par ordre alphabétique avec les extensions `.sh` , `.sql` et `.sql.gz` qui se trouve dans le référentiel. Les scripts contenus dans les dossiers enfants seront ignorés. le script doit contenir les informations suivantes :

* [VolumeSource](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes): L'endroit à partir duquel votre script est chargé.

Vous trouverez ci-dessous un exemple montrant comment un script d'un configMap peut être utilisé pour initialiser une base de données MariaDB.

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: 12.1.2
  init:
    script:
      configMap:
        name: md-init-script
```

Dans l'exemple ci-dessus, l'opérateur KubeDB lancera un Job pour exécuter tous les scripts js de `md-init-script` par ordre alphabétique une fois que les pods PetSet sont en cours d’exécution.

### spec.monitor

MariaDB gérée par KubeDB peut être surveillée avec l'opérateur Prometheus et Prometheus intégré prêt à l'emploi.

### spec.requireSSL

`spec.requireSSL` spécifie si les connexions client nécessitent SSL. Si `spec.requireSSL` est `true` alors le serveur autorise uniquement les connexions TCP/IP qui utilisent SSL, ou les connexions qui utilisent un fichier socket (sous Unix) ou une mémoire partagée (sous Windows). Le serveur rejette toute tentative de connexion non sécurisée. Pour plus de détails, veuillez visiter [ici](https://mariadb.com/kb/en/securing-connections-for-client-and-server/#requiring-tls-for-specific-user-accounts)

### spec.tls

`spec.tls` spécifie les configurations TLS/SSL pour MariaDB.

Les champs suivants sont configurables dans le `spec.tls` section:

* `issuerRef` est une référence à `Issuer` ou `ClusterIssuer` RC de [gestionnaire de certificats](https://cert-manager.io/docs/concepts/issuer/) qui sera utilisé par `KubeDB` pour générer les certificats nécessaires.

  + `apiGroup` est le nom de groupe de la ressource référencée. La valeur pour `Issuer` ou `ClusterIssuer` est « cert-manager.io » (cert-manager v0.12.0 et versions ultérieures).
  + `kind` est le type de ressource référencée. KubeDB prend en charge les deux `Issuer` et `ClusterIssuer` comme valeurs pour ce champ.
  + `name` est le nom de la ressource (`Issuer` ou `ClusterIssuer`) étant référencé.
* `certificates` (facultatif) sont une liste de certificats utilisés pour configurer le certificat serveur et/ou client. Il comporte les champs suivants :

  + `alias` représente l'identifiant du certificat. Il a la valeur possible suivante :

    - `server` est utilisé pour l’identification du certificat du serveur.
    - `client` est utilisé pour l’identification du certificat client.
    - `metrics-exporter` est utilisé pour l’identification du certificat de l’exportateur de métriques.
  + `secretName` (facultatif) spécifie le nom secret k8s qui contient les certificats.
    Ce champ est facultatif. Si l'utilisateur ne précise pas ce champ, le nom du secret par défaut sera créé au format suivant : `<database-name>-<cert-alias>-cert`.
  + `subject` (facultatif) spécifie un `X.509` nom distingué. Il a le champ possible suivant,

    - `organizations` (facultatif) sont la liste des différents noms d’organisations à utiliser sur le certificat.
    - `organizationalUnits` (facultatif) sont la liste des différents noms d’unités d’organisation à utiliser sur le certificat.
    - `countries` (facultatif) sont la liste des noms de pays à utiliser sur le certificat.
    - `localities` (facultatif) sont la liste des noms de localités à utiliser sur le certificat.
    - `provinces` (facultatif) est la liste des noms de provinces à utiliser sur le certificat.
    - `streetAddresses` (facultatif) sont la liste d’une adresse postale à utiliser sur le certificat.
    - `postalCodes` (facultatif) sont la liste des codes postaux à utiliser sur le certificat.
    - `serialNumber` (facultatif) est un numéro de série à utiliser sur le certificat.
      Vous pouvez trouver plus de détails sur [Ici](https://golang.org/pkg/crypto/x509/pkix/#Name)
  + `duration` (facultatif) est la période pendant laquelle le certificat est valable.
  + `renewBefore` (facultatif) est un délai spécifiable avant la durée d'expiration.
  + `dnsNames` (facultatif) est une liste de noms alternatifs de sujets à utiliser dans le certificat.
  + `ipAddresses` (facultatif) est une liste d’adresses IP à utiliser dans le certificat.
  + `uriSANs` (facultatif) est une liste de noms alternatifs de sujets URI à définir dans le certificat.
  + `emailSANs` (facultatif) est une liste de noms alternatifs de sujets de courrier électronique à définir dans le certificat.

### spec.configuration

`spec.configuration` est un champ facultatif qui spécifie une configuration personnalisée pour le cluster Mariadb. Il comporte les champs suivants :

* `configuration.inline` est un champ facultatif qui vous permet de fournir une configuration personnalisée directement dans l'objet Mariadb.
  + Configuration snippet:

    ```yaml
    configuration:
         inline:
           md.cnf: |
             [mysqld]
             max_connections = 500
    ```
* `configuration.secretName` est un champ facultatif qui spécifie le nom du secret contenant les fichiers de configuration personnalisés pour le cluster Mariadb.

### spec.podTemplate

KubeDB permet de fournir un modèle pour le pod de base de données via `spec.podTemplate`. L'opérateur KubeDB transmettra les informations fournies dans `spec.podTemplate` au PetSet créé pour la base de données MariaDB.

KubeDB accepte les champs suivants à définir `spec.podTemplate:`

* métadonnées :
  + annotations (annotation du pod)
* contrôleur:
  + annotations (annotation de petset)
* spécification :
  + conteneurs
  + tomes
  + podPlacementPolitique
  + initConteneurs
  + imagePullSecrets
  + sélecteur de nœud
  + serviceAccountName
  + Nom du planificateur
  + tolérances
  + nomClassePriorité
  + priorité
  + contexte de sécurité

Utilisations de certains domaines de `spec.podTemplate` est décrit ci-dessous,

Vous pouvez consulter la liste complète [ici](https://github.com/kmodules/offshoot-api/blob/master/api/v2/types.go#L26C1-L279C1).
Utilisations de certains domaines de `spec.podTemplate` est décrit ci-dessous,

#### spec.podTemplate.spec.tolerations

Le `spec.podTemplate.spec.tolerations` est un champ facultatif. Ceci peut être utilisé pour spécifier les tolérances du pod.

#### spec.podTemplate.spec.volumes

Le `spec.podTemplate.spec.volumes` est un champ facultatif. Ceci peut être utilisé pour fournir la liste des volumes pouvant être montés par les conteneurs appartenant au pod.

#### spec.podTemplate.spec.podPlacementPolicy

`spec.podTemplate.spec.podPlacementPolicy` est un champ facultatif. Ceci peut être utilisé pour fournir la référence du `podPlacementPolicy`. `name` de podPlacementPolicy est référencé sous cet attribut. Ceci sera utilisé par notre contrôleur Petset pour placer les pods de base de données dans toute la région, la zone et les nœuds conformément à la politique. Il utilise l'affinité Kubernetes et la fonctionnalité podTopologySpreadContraints pour ce faire.

```yaml
spec:
  podPlacementPolicy:
    name: default
```

#### spec.podTemplate.spec.containers

Le `spec.podTemplate.spec.containers` peut être utilisé pour fournir les conteneurs de liste et leurs configurations au pod de base de données. certains des champs sont décrits ci-dessous,

##### spec.podTemplate.spec.containers[].name

Le `spec.podTemplate.spec.containers[].name` champ utilisé pour spécifier le nom du conteneur spécifié comme DNS\_LABEL. Chaque conteneur d'un pod doit avoir un nom unique (DNS\_LABEL). Ne peut pas être mis à jour.

##### spec.podTemplate.spec.containers[].args

`spec.podTemplate.spec.containers[].args` est un champ facultatif. Cela peut être utilisé pour fournir des arguments supplémentaires à l'installation de la base de données.

##### spec.podTemplate.spec.containers[].resources

`spec.podTemplate.spec.containers[].resources` est un champ facultatif. Cela peut être utilisé pour demander les ressources de calcul requises par les conteneurs des pods de base de données. Pour en savoir plus, visitez [ici](http://kubernetes.io/docs/user-guide/compute-resources/).

##### spec.podTemplate.spec.containers[].env

`spec.podTemplate.spec.env` est un champ facultatif qui spécifie les variables d'environnement à transmettre à l'image Docker MariaDB. Pour connaître les variables d'environnement prises en charge, veuillez visiter [ici](https://hub.docker.com/_/mariadb/).

Notez que KubeDB n'autorise pas `MYSQL_ROOT_PASSWORD`, `MYSQL_ALLOW_EMPTY_PASSWORD`, `MYSQL_RANDOM_ROOT_PASSWORD`, et `MYSQL_ONETIME_PASSWORD` variables d'environnement à définir `spec.env`. Si vous souhaitez définir le mot de passe root, veuillez utiliser `spec.authSecret` au lieu de cela décrit plus tôt.

Si vous essayez de définir l'une des variables d'environnement interdites, c'est-à-dire `MYSQL_ROOT_PASSWORD` dans MariaDB crd, l'opérateur KubeDB rejettera la demande avec l'erreur suivante,

```bash
Error from server (Forbidden): error when creating "./mariadb.yaml": admission webhook "mariadb.validators.kubedb.com" denied the request: environment variable MYSQL_ROOT_PASSWORD is forbidden to use in MariaDB spec
```

Notez également que KubeDB ne permet pas de mettre à jour les variables d'environnement car leur mise à jour n'a aucun effet une fois la base de données créée. Si vous essayez de mettre à jour les variables d'environnement, l'opérateur KubeDB rejettera la demande avec l'erreur suivante :

```bash
Error from server (BadRequest): error when applying patch:
...
for: "./mariadb.yaml": admission webhook "mariadb.validators.kubedb.com" denied the request: precondition failed for:
...At least one of the following was changed:
    apiVersion
    kind
    name
    namespace
    spec.authSecret
    spec.init
    spec.storageType
    spec.storage
    spec.podTemplate.spec.nodeSelector
    spec.podTemplate.spec.env
```

#### spec.podTemplate.spec.imagePullSecrets

`KubeDB` offre la flexibilité de déployer la base de données MariaDB à partir d'un registre Docker privé. `spec.podTemplate.spec.imagePullSecrets` est un champ facultatif qui pointe vers les secrets à utiliser pour extraire l'image Docker si vous utilisez un registre Docker privé.

#### spec.podTemplate.spec.nodeSelector

`spec.podTemplate.spec.nodeSelector` est un champ facultatif qui spécifie une carte de paires clé-valeur. Pour que le pod puisse s'exécuter sur un nœud, le nœud doit avoir chacune des paires clé-valeur indiquées comme étiquettes (il peut également avoir des étiquettes supplémentaires). Pour en savoir plus, voir [ici](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) .

#### spec.podTemplate.spec.serviceAccountName

`serviceAccountName` est un champ facultatif pris en charge par KubeDB Operator (version 0.13.0 et ultérieure) qui peut être utilisé pour spécifier un compte de service personnalisé afin d'affiner le contrôle d'accès basé sur les rôles.

Si ce champ est laissé vide, l'opérateur KubeDB créera un nom de compte de service correspondant au nom de crd MariaDB. Le rôle et le RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés automatiquement pour ce compte de service.

Si un nom de compte de service est donné, mais qu'il n'existe aucun compte de service portant ce nom, l'opérateur KubeDB en créera un, et Role et RoleBinding qui fournissent les autorisations d'accès nécessaires seront également générés pour ce compte de service.

Si un nom de compte de service est donné et qu'il existe un compte de service portant ce nom, l'opérateur KubeDB utilisera ce compte de service existant. Étant donné que ce compte de service n'est pas géré par KubeDB, les utilisateurs sont responsables de fournir manuellement les autorisations d'accès nécessaires.

### spec.serviceTemplates

Vous pouvez également fournir un modèle pour les services créés par l'opérateur KubeDB pour la base de données MariaDB via `spec.serviceTemplates`. Cela vous permettra de définir le type et d'autres propriétés des services.

KubeDB permet de définir les champs suivants `spec.serviceTemplates`:

* métadonnées :
  + annotations
* spécification :
  + taper
  + ports
  + clusterIP
  + adresses IP externes
  + LoadBalancerIP
  + loadBalancerSourceRanges
  + politique de trafic externe
  + healthCheckNodePort
  + sessionAffinityConfig

```yaml
spec:
  version: "12.1.2"
  serviceTemplates:
    - alias: primary
      metadata:
        annotations:
          kubedb.com/test-annotation: "test"
      spec:
        type: LoadBalancer
        ports:
          - port: 3306
```

Voir [ici](https://github.com/kmodules/offshoot-api/blob/kubernetes-1.16.3/api/v1/types.go#L163) pour comprendre ces domaines en détail.

### spec.halted

`spec.halted` est un champ facultatif. Supposons que vous vouliez supprimer le `MariaDB` ressources(`PetSet`, `Service` etc.) sauf `MariaDB` objet, `PVCs` et `Secret` alors vous devez définir `spec.halted` à `true`. Si vous définissez `spec.halted` à `true` alors le `deletionPolicy` dans `MariaDB` l'objet sera défini `Halt` par défaut.

### spec.deletionPolicy

`deletionPolicy` donne la flexibilité de savoir s'il faut `nullify`(rejeter) l'opération de suppression de `MariaDB` crd ou quelles ressources KubeDB doit conserver ou supprimer lorsque vous supprimez `MariaDB` crd. KubeDB fournit les quatre stratégies de résiliation suivantes :

* Ne pas terminer
* Arrêt
* Supprimer (`Default`)
* Anéantir

Quand `deletionPolicy` est `DoNotTerminate`, KubeDB profite de `ValidationWebhook` fonctionnalité dans les clusters Kubernetes 1.9.0 ou version ultérieure à implémenter `DoNotTerminate` fonctionnalité. Si le webhook d'admission est activé, `DoNotTerminate` empêche les utilisateurs de supprimer la base de données tant que le `spec.deletionPolicy` est réglé sur `DoNotTerminate`.

Le tableau suivant montre ce que KubeDB fait lorsque vous supprimez le crd MariaDB pour différentes politiques de résiliation,

| Comportement | Ne pas terminer | Arrêt | Supprimer | Anéantir |
| --- | --- | --- | --- | --- |
| 1. Opération de suppression de bloc | ✓ | ✗ | ✗ | ✗ |
| 2. Supprimer PetSet | ✗ | ✓ | ✓ | ✓ |
| 3. Supprimer des services | ✗ | ✓ | ✓ | ✓ |
| 4. Supprimer les PVC | ✗ | ✗ | ✓ | ✓ |
| 5. Supprimer les secrets | ✗ | ✗ | ✗ | ✓ |
| 6. Supprimer les instantanés | ✗ | ✗ | ✗ | ✓ |

Si vous ne précisez pas `spec.deletionPolicy` KubeDB utilise `Delete` politique de résiliation par défaut.

> Pour plus de détails, vous pouvez visiter [ici](https://appscode.com/blog/post/deletion-policy/)