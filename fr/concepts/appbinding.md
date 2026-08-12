> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Liaison d'application

## Qu'est-ce qu'AppBinding

Un `AppBinding` est un Kubernetes `CustomResourceDefinition`(CRD) qui pointe vers une application en utilisant soit son URL (généralement pour une instance de service non résidente de Kubernetes), soit un objet de service Kubernetes (s'il est auto-hébergé dans un cluster Kubernetes), certains paramètres facultatifs et un secret d'identification. Pour en savoir plus sur AppBinding et les problèmes qu'il résout, veuillez lire cet article de blog : [Le cas d’AppBinding](https://appscode.com/blog/post/the-case-for-appbinding).

Si vous déployez une base de données à l'aide [KubeDB](https://kubedb.com/docs/latest/welcome/), `AppBinding` l'objet sera créé automatiquement pour cela. Sinon, vous devez créer un `AppBinding` objet pointant manuellement vers la base de données souhaitée.

KubeDB utilise [Planque](https://appscode.com/products/stash/) pour effectuer une sauvegarde/récupération des bases de données. Stash doit savoir comment se connecter à une base de données cible et les informations d'identification nécessaires pour y accéder. Cela se fait via un `AppBinding`.

## Spécification AppBinding CRD

Comme toute ressource officielle Kubernetes, un `AppBinding` a `TypeMeta`, `ObjectMeta` et `Spec` sections. Cependant, contrairement aux autres ressources Kubernetes, elle ne dispose pas de `Status` section.

Un `AppBinding` objet créé par `KubeDB` pour la base de données MariaDB est illustré ci-dessous,

```yaml
apiVersion: appcatalog.appscode.com/v1alpha1
kind: AppBinding
metadata:
  labels:
    app.kubernetes.io/component: database
    app.kubernetes.io/instance: sample-mariadb
    app.kubernetes.io/managed-by: kubedb.com
    app.kubernetes.io/name: mariadbs.kubedb.com
  name: sample-mariadb
  namespace: demo
spec:
  clientConfig:
    caBundle: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURJekNDQWd1Z0F3SUJBZ0lVVUg1V24wOSt6MnR6RU5ESnF4N1AxZFg5aWM4d0RRWUpLb1pJaHZjTkFRRUwKQlFBd0lURU9NQXdHQTFVRUF3d0ZiWGx6Y1d3eER6QU5CZ05WQkFvTUJtdDFZbVZrWWpBZUZ3MHlNVEF5TURrdwpPVEkxTWpCYUZ3MHlNakF5TURrd09USTFNakJhTUNFeERqQU1CZ05WQkFNTUJXMTVjM0ZzTVE4d0RRWURWUVFLCkRBWnJkV0psWkdJd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUUM3ZDl5YUtMQ3UKYy9NclRBb0NkV1VORld3ckdqbVdvUEVTRWNMR0pjT0JVSTZ5NXZ5QXVGMG1TakZvNzR3SEdSbWRmS2ExMWh0Ygo4TWZ2UFNwWXVGWFpUSi9GbnkwNnU2ekZMVm5xV2h3MUdiZ2ZCUE5XK0w1ZGkzZmVjanBEZmtLbTcrd0ZUVnNmClVzWGVVcUR0VHFpdlJHVUQ5aURUTzNTUmdheVI5U0J0RnRxcHRtV0YrODFqZGlSS2pRTVlCVGJ2MDRueW9UdHUKK0hJZlFjbE40Q1p3NzJPckpUdFdiYnNiWHVlMU5RZU9nQzJmSVhkZEF0WEkxd3lOT04zckxuTFF1SUIrakVLSQpkZTlPandKSkJhSFVzRVZEbllnYlJLSTdIcVdFdk5kL29OU2VZRXF2TXk3K1hwTFV0cDBaVXlxUDV2cC9PSXJ3CmlVMWVxZGNZMzJDcEFnTUJBQUdqVXpCUk1CMEdBMVVkRGdRV0JCUlNnNDVpazFlT3lCU1VKWHkvQllZVDVLck8KeWpBZkJnTlZIU01FR0RBV2dCUlNnNDVpazFlT3lCU1VKWHkvQllZVDVLck95akFQQmdOVkhSTUJBZjhFQlRBRApBUUgvTUEwR0NTcUdTSWIzRFFFQkN3VUFBNElCQVFCNTlhNlFGQm1YMTh1b1dzQ3dGT1Y0R25GYnVBL2NoaVN6CkFwRVVhcjI1L2RNK2RpT0RVNkJuMXM3Wmpqem45WU9aVVJJL3UyRGRhdmNnQUNYR2FXWHJhSS84UUYxZDB3OGsKNXFlRmMxQWE5UEhFeEsxVm1xb21MV2xhMkdTOW1EbFpEOEtueDdjU3lpRmVqRXJYdWtld1B1VXA0dUUzTjAraApwQjQ0MDVRU2d4VVc3SmVhamFQdTNXOHgyRUFKMnViTkdMVEk5L0x4V1Z0YkxGcUFoSFphbGRjaXpOSHdTUGYzCkdMWEo3YTBWTW1JY0NuMWh5a0k2UkNrUTRLSE9tbDNOcXRRS2F5RnhUVHVpdzRiZ3k3czA1UnNzRlVUaWN1VmcKc3hnMjFVQUkvYW9WaXpQOVpESGE2TmV0YnpNczJmcmZBeHhBZk9pWDlzN1JuTmM0WHd4VAotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    service:
      name: sample-mariadb
      port: 3306
      scheme: mysql
  secret:
    name: sample-mariadb-auth
  type: kubedb.com/mariadb
  version: 12.1.2
```

Ici, nous allons décrire les sections d'un `AppBinding` crd.

### Liaison d'application `Spec`

Un `AppBinding` l'objet comporte les champs suivants dans le `spec` section:

#### spec.type

`spec.type` est un champ facultatif qui indique le type d'application que ce `AppBinding` pointe vers. Stash utilise ce champ pour résoudre les valeurs de `TARGET_APP_TYPE`, `TARGET_APP_GROUP` et `TARGET_APP_RESOURCE` variables de [Plan de sauvegarde](https://appscode.com/products/stash/latest/concepts/crds/backupblueprint/) objet.

Ce champ suit le format suivant : `<app group>/<resource kind>`. L'AppBinding ci-dessus pointe vers un `mariadb` ressource sous `kubedb.com` groupe.

Ici, les variables sont analysées comme suit :

| Variable | Usage |
| --- | --- |
| `TARGET_APP_GROUP` | Représente le groupe d'applications auquel appartient l'application respective (c'est-à-dire : `kubedb.com`). |
| `TARGET_APP_RESOURCE` | Représente la ressource sous ce groupe d'applications que cette liaison d'application représente (c'est-à-dire : `mariadb`). |
| `TARGET_APP_TYPE` | Représente le type complet de l’application. C'est simplement `TARGET_APP_GROUP/TARGET_APP_RESOURCE` (c'est-à-dire : `kubedb.com/mariadb`). |

#### spécification.secret

`spec.secret` spécifie le nom du secret qui contient les informations d'identification requises pour accéder à la base de données. Ce secret doit être dans le même espace de noms que le `AppBinding`.

Ce secret doit contenir les clés suivantes :

PostgreSQL :

| Clé | Usage |
| --- | --- |
| `POSTGRES_USER` | Nom d'utilisateur de la base de données cible. |
| `POSTGRES_PASSWORD` | Mot de passe de l'utilisateur spécifié par `POSTGRES_USER`. |

MySQL :

| Clé | Usage |
| --- | --- |
| `username` | Nom d'utilisateur de la base de données cible. |
| `password` | Mot de passe de l'utilisateur spécifié par `username`. |

MariaDB :

| Clé | Usage |
| --- | --- |
| `username` | Nom d'utilisateur de la base de données cible. |
| `password` | Mot de passe de l'utilisateur spécifié par `username`. |

MongoDB :

| Clé | Usage |
| --- | --- |
| `username` | Nom d'utilisateur de la base de données cible. |
| `password` | Mot de passe de l'utilisateur spécifié par `username`. |

MariaDB :

| Clé | Usage |
| --- | --- |
| `ADMIN_USERNAME` | Nom d'utilisateur administrateur |
| `ADMIN_PASSWORD` | Mot de passe pour l'utilisateur administrateur |

#### spec.clientConfig

`spec.clientConfig` définit comment communiquer avec la base de données cible. Vous pouvez utiliser une URL ou un service Kubernetes pour vous connecter à la base de données. Vous n’êtes pas obligé de spécifier les deux.

Vous pouvez configurer les champs suivants dans `spec.clientConfig` section:

* **spec.clientConfig.url**

  `spec.clientConfig.url` donne l'emplacement de la base de données, sous forme d'URL standard (c'est-à-dire `[scheme://]host:port/[path]`). Ceci est particulièrement utile lorsque la base de données cible s'exécute en dehors du cluster Kubernetes. Si votre base de données s'exécute à l'intérieur du cluster, utilisez `spec.clientConfig.service` section à la place.
  Notez que si vous tentez d'utiliser un utilisateur ou une authentification de base (par ex. `user:password@host:port`) n'est pas autorisé. Stash les insérera automatiquement à partir du secret respectif. Les fragments ("#…") et les paramètres de requête ("?…") ne sont pas non plus autorisés.
* **spec.clientConfig.service**

  Si vous exécutez la base de données dans le cluster Kubernetes, vous pouvez utiliser le service Kubernetes pour vous connecter à la base de données. Vous devez spécifier les champs suivants dans `spec.clientConfig.service` section si vous créez manuellement un `AppBinding` objet.

  + **nom :** `name` indique le nom du service qui se connecte à la base de données cible.
  + **schéma :** `scheme` spécifie le schéma (c'est-à-dire http, https) à utiliser pour se connecter à la base de données.
  + **port :** `port` spécifie le port sur lequel la base de données cible est exécutée.
* **spec.clientConfig.insecureSkipTLSVerify**

  `spec.clientConfig.insecureSkipTLSVerify` est utilisé pour désactiver la vérification du certificat TLS lors de la connexion à la base de données. Nous déconseillons fortement de désactiver la vérification TLS lors de la sauvegarde. Vous devez fournir le bundle CA correspondant via `spec.clientConfig.caBundle` champ à la place.
* **spec.clientConfig.caBundle**

  `spec.clientConfig.caBundle` est un bundle CA codé PEM qui sera utilisé pour valider le certificat de service de la base de données.