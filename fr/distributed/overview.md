# Présentation du cluster MariaDB Galera distribué

## Introduction

KubeDB permet des déploiements MariaDB distribués à l'aide de la technologie de clustering Galera sur plusieurs clusters Kubernetes, fournissant ainsi une solution de base de données évolutive, hautement disponible et résiliente. En intégrant **Gestion de cluster ouverte (OCM)** pour l'orchestration multicluster et **KubeSlice** pour une connectivité réseau transparente de pod à pod, KubeDB simplifie le déploiement et la gestion des instances MariaDB sur les clusters. UN **Politique de placement** assure un contrôle précis sur la planification des pods, vous permettant de distribuer les pods MariaDB sur les clusters pour une utilisation optimale des ressources et une tolérance aux pannes.

Ce guide fournit un processus étape par étape pour déployer un cluster MariaDB Galera distribué, y compris les conditions préalables, la configuration et les étapes de vérification. Cela suppose une familiarité avec Kubernetes et les concepts de base des bases de données.

> **Vous êtes nouveau sur KubeDB ?** Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

## Comprendre les clusters OCM Hub et Spoke

Dans un **Gestion de cluster ouverte (OCM)** configuration, les clusters sont classés comme suit :

* **Cluster central**: Le plan de contrôle central où les politiques, les applications et les ressources sont définies et gérées. Il orchestre le cycle de vie des applications déployées sur les clusters Spoke.
* **Groupe de rayons**: clusters gérés enregistrés auprès du hub qui exécutent les charges de travail réelles (par exemple, les pods MariaDB).

Lorsqu'un cluster de rayons (par exemple, `demo-worker`) est joint au hub à l'aide du `clusteradm join` commande, OCM crée un espace de noms sur le cluster hub qui correspond au nom du cluster Spoke (par exemple, `demo-worker`). Cet espace de noms est utilisé pour gérer les ressources spécifiques au cluster Spoke à partir du hub.

## Conditions préalables

Avant de déployer un cluster MariaDB Galera distribué, assurez-vous que les conditions suivantes sont remplies :

* **Clusters Kubernetes**: Plusieurs clusters Kubernetes (version 1.26 ou supérieure) configurés et accessibles.
* **Exigences du nœud**: Chaque nœud Kubernetes doit disposer d'au moins 4 vCPU et 16 Go de RAM.
* **Gestion de cluster ouverte (OCM)**: Installer `clusteradm` comme décrit dans le [Guide de démarrage rapide OCM](https://open-cluster-management.io/docs/getting-started/quick-start/).
* **Kubectl**: Installé et configuré pour interagir avec tous les clusters.
* **Barre**: Installé pour le déploiement des composants KubeDB Operator et KubeSlice.
* **Stockage persistant**: Une classe de stockage (par exemple, `local-path` ou une option spécifique au fournisseur de cloud) configurée pour les volumes persistants.

## Étapes de configuration

Suivez ces étapes pour déployer un cluster MariaDB Galera distribué sur plusieurs clusters Kubernetes.

### Étape 1 : Configurer la gestion des clusters ouverts (OCM)

#### 1. Configurez KUBECONFIG

Assurez-vous que votre `KUBECONFIG` est configuré pour basculer entre les clusters. Ce guide utilise deux clusters : `demo-controller` (moyeu et rayon) et `demo-worker` (rayon).

```bash
$ kubectl config get-contexts
```

**Sortir:**

```bash
CURRENT   NAME              CLUSTER           AUTHINFO          NAMESPACE
*         demo-controller   demo-controller   demo-controller   
          demo-worker       demo-worker       demo-worker
```

#### 2. Initialisez le hub OCM

Sur le `demo-controller` cluster, initialisez le hub OCM :

```bash
$ kubectl config use-context demo-controller
$ clusteradm init --wait --feature-gates=ManifestWorkReplicaSet=true
```

#### 3. Vérifiez le déploiement du hub

Vérifiez les dosettes dans le `open-cluster-management-hub` espace de noms pour garantir que tous les composants sont en cours d'exécution :

```bash
$ kubectl get pods -n open-cluster-management-hub
```

**Sortir:**

```
NAME                                                        READY   STATUS    RESTARTS   AGE
cluster-manager-addon-manager-controller-5f99f56896-qpzj8   1/1     Running   0          7m2s
cluster-manager-placement-controller-597d5ff644-wqjq2       1/1     Running   0          7m2s
cluster-manager-registration-controller-6d79d7dcc6-b8h9p    1/1     Running   0          7m2s
cluster-manager-registration-webhook-5d88cf97c7-2sq5m       1/1     Running   0          7m2s
cluster-manager-work-controller-7468bf4dc-5qn6q             1/1     Running   0          7m2s
cluster-manager-work-webhook-c5875947-d272b                 1/1     Running   0          7m2s
```

Tous les modules doivent être dans le `Running` état avec `1/1` préparation et aucun redémarrage, indiquant un déploiement de hub réussi.

#### 4. Enregistrez le cluster Spoke (`demo-worker`)

Obtenez le jeton de jointure du cluster hub :

```bash
$ clusteradm get token
```

**Sortir:**

```
token=<Your_Clusteradm_Join_Token>
please log on spoke and run:
clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name <cluster_name>
```

Sur le `demo-worker` cluster, joignez-le au hub. Inclure le `RawFeedbackJsonString` porte de fonctionnalité pour les commentaires sur les ressources :

```bash
$ kubectl config use-context demo-worker
$ clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name demo-worker --feature-gates=RawFeedbackJsonString=true
```

#### 5. Accepter le cluster Spoke

Sur le `demo-controller` cluster, acceptez le `demo-worker` grappe:

```bash
$ kubectl config use-context demo-controller
$ clusteradm accept --clusters demo-worker
```

> **Note:** Cela peut prendre quelques tentatives (par exemple, réessayer toutes les 10 secondes) si le cluster n'est pas immédiatement disponible.

**Résultat (en cas de succès) :**

```
Starting approve csrs for the cluster demo-worker
CSR demo-worker-2p2pb approved
set hubAcceptsClient to true for managed cluster demo-worker
Your managed cluster demo-worker has joined the Hub successfully.
```

#### 6. Vérifiez la création de l'espace de noms

Confirmez qu'un espace de noms pour `demo-worker` a été créé sur le cluster hub :

```bash
$ kubectl get ns
```

**Sortir:**

```bash
NAME                          STATUS   AGE
default                       Active   99m
demo-worker                   Active   58s
kube-node-lease               Active   99m
kube-public                   Active   99m
kube-system                   Active   99m
open-cluster-management       Active   6m7s
open-cluster-management-hub   Active   5m32s
```

#### 7. Inscrivez-vous `demo-controller` en tant que cluster de rayons

Répétez le processus de jointure et d'acceptation pour `demo-controller` il peut donc également agir comme un cluster de rayons :

```bash
$ kubectl config use-context demo-controller
$ clusteradm join --hub-token <Your_Clusteradm_Join_Token> --hub-apiserver https://<hub-apiserver-ip>:6443 --cluster-name demo-controller --feature-gates=RawFeedbackJsonString=true
$ clusteradm accept --clusters demo-controller
```

Vérifiez l'espace de noms pour `demo-controller`:

```bash
$ kubectl get ns
```

**Sortir:**

```
NAME                                  STATUS   AGE
default                               Active   104m
demo-controller                       Active   3s
demo-worker                           Active   6m7s
kube-node-lease                       Active   104m
kube-public                           Active   104m
kube-system                           Active   104m
open-cluster-management               Active   11m
open-cluster-management-agent         Active   37s
open-cluster-management-agent-addon   Active   34s
open-cluster-management-hub           Active   10m
```

#### 8. Vérifiez les rôles OCM

Après l'enregistrement, utilisez ces commandes pour confirmer quel cluster est le hub et lesquels sont les rayons :

```bash
# Hub: lists all registered spoke clusters
$ kubectl get managedclusters

# Spoke: shows this cluster's registered name
$ kubectl get klusterlet klusterlet -o jsonpath='{.spec.clusterName}'

# Hub components run only on the hub cluster
$ kubectl get pods -n open-cluster-management-hub

# Spoke agent runs on every spoke cluster
$ kubectl get pods -n open-cluster-management-agent
```

### Étape 2 : Configurer la configuration de travail OCM

Exécutez ceci sur **chaque cluster de rayons** (`demo-controller` et `demo-worker`). Cela permet au `RawFeedbackJsonString` porte de fonctionnalité dont KubeDB a besoin pour lire l'état des pods sur les clusters et augmente les limites de débit de l'API pour empêcher la limitation.

> **Note:** Même si tu as réussi `--feature-gates=RawFeedbackJsonString=true` pendant `clusteradm join`, les champs de limite de débit ne sont pas définis par cet indicateur. Exécutez ce correctif sur tous les rayons malgré tout.
>
> **Pourquoi c'est important :** KubeDB utilise le mécanisme de rétroaction ManifestWork d'OCM pour surveiller l'état des pods MariaDB sur les clusters satellites distants. Sans `RawFeedbackJsonString`, le provisionneur KubeDB sur le hub ne reçoit jamais de mises à jour de l'état du pod des rayons et le CR MariaDB distribué restera indéfiniment dans un état non prêt. Les limites de débit empêchent l'agent klusterlet d'être limité par l'API lors de la formation initiale du cluster.

```bash
$ kubectl patch klusterlet klusterlet --type=merge -p '{
  "spec": {
    "workConfiguration": {
      "featureGates": [{"feature": "RawFeedbackJsonString", "mode": "Enable"}],
      "hubKubeAPIBurst": 100,
      "hubKubeAPIQPS": 50,
      "kubeAPIBurst": 100,
      "kubeAPIQPS": 50
    }
  }
}'
```

Vérifiez la configuration :

```bash
$ kubectl get klusterlet klusterlet -oyaml
```

**Exemple de résultat (abrégé) :**

```yaml
apiVersion: operator.open-cluster-management.io/v1
kind: Klusterlet
metadata:
  name: klusterlet
spec:
  clusterName: demo-worker
  workConfiguration:
    featureGates:
    - feature: RawFeedbackJsonString
      mode: Enable
    hubKubeAPIBurst: 100
    hubKubeAPIQPS: 50
    kubeAPIBurst: 100
    kubeAPIQPS: 50
```

### Étape 3 : Configurer KubeSlice pour la connectivité réseau

KubeSlice permet la communication de pod à pod entre les clusters. Installez le contrôleur KubeSlice sur le `demo-controller` cluster et le KubeSlice Worker sur les deux `demo-controller` et `demo-worker` groupes.

#### 1. Installez le contrôleur KubeSlice

Sur `demo-controller`, obtenez d'abord l'adresse du serveur API hub :

```bash
$ kubectl cluster-info | grep 'Kubernetes control plane'
```

Utilisez l'adresse IP et le port de cette sortie comme `endpoint` valeur. Créer un `controller.yaml` déposer:

```yaml
kubeslice:
  controller:
    loglevel: info
    rbacResourcePrefix: kubeslice-rbac
    projectnsPrefix: kubeslice
    endpoint: https://<hub-apiserver-ip>:6443
```

Déployez le contrôleur à l'aide de Helm :

```bash
$ helm upgrade -i kubeslice-controller oci://ghcr.io/appscode-charts/kubeslice-controller \
    --version v2026.1.15 \
    -f controller.yaml \
    --namespace kubeslice-controller \
    --create-namespace \
    --set ocm.enabled=true \
    --wait --burst-limit=10000 --debug
```

Vérifiez l'installation :

```bash
$ kubectl get pods -n kubeslice-controller
```

**Sortir:**

```
NAME                                            READY   STATUS    RESTARTS   AGE
kubeslice-controller-manager-7fd756fff6-5kddd   2/2     Running   0          98s
```

#### 2. Créez un projet KubeSlice

Créer un `project.yaml` déposer:

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: Project
metadata:
  name: demo-distributed-mariadb
  namespace: kubeslice-controller
spec:
  serviceAccount:
    readWrite:
      - admin
```

Appliquer le projet :

```bash
$ kubectl apply -f project.yaml
```

Vérifier:

```bash
$ kubectl get project -n kubeslice-controller
```

**Sortir:**

```bash
NAME                       AGE
demo-distributed-mariadb   31s
```

Vérifiez les comptes de service :

```bash
$ kubectl get sa -n kubeslice-demo-distributed-mariadb
```

**Sortir:**

```
NAME                      SECRETS   AGE
default                   0         69s
kubeslice-rbac-rw-admin   1         68s
```

#### 3. Étiqueter les nœuds pour KubeSlice

Attribuer le `kubeslice.io/node-type=gateway` étiquette au nœud où l’opérateur de travail sera déployé dans les deux clusters.

Sur `demo-controller`:

```bash
$ kubectl get nodes
$ kubectl label node <node-name> kubeslice.io/node-type=gateway
```

Sur `demo-worker`:

```bash
$ kubectl config use-context demo-worker
$ kubectl get nodes
$ kubectl label node <node-name> kubeslice.io/node-type=gateway
```

#### 4. Enregistrez les clusters avec KubeSlice

Identifiez l'interface réseau de chaque cluster en exécutant la commande suivante **sur le nœud passerelle de chaque cluster**:

```bash
$ ip route get 8.8.8.8 | awk '{ print $5 }'
```

**Sortie (exemple) :**

```
enp1s0
```
> **Important:** Le `networkInterface` La valeur doit correspondre à l’interface réseau principale du nœud de passerelle de chaque cluster. Exécutez la commande ci-dessus sur **chaque cluster séparément** et utilisez la sortie de ce cluster comme `networkInterface` valeur. Chaque cluster peut avoir un **nom d'interface différent** - ne présumez pas qu'ils sont identiques. L'utilisation d'un nom d'interface incorrect entraînera l'échec silencieux de la passerelle WireGuard et la réplication MariaDB entre clusters ne se connectera jamais.
>
> Exemple : si `demo-controller` retours `enp3s0` et `demo-worker` retours `eth0`, utilisez ces valeurs exactes dans le YAML ci-dessous.

Créer un `registration.yaml` déposer:

> **Note:**
>
> * Le nom du cluster doit correspondre exactement au nom du cluster OCM (spoke).
> * Le correspondant `ManagedClusterAddOn` La ressource doit être créée dans l'espace de noms qui porte le même nom que le cluster pour configurer automatiquement le travailleur KubeSlice.

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: Cluster
metadata:
  name: demo-controller
  namespace: kubeslice-demo-distributed-mariadb
spec:
  networkInterface: <demo-controller-interface>   # replace with output of ip route command
  clusterProperty: {}
---
apiVersion: controller.kubeslice.io/v1alpha1
kind: Cluster
metadata:
  name: demo-worker
  namespace: kubeslice-demo-distributed-mariadb
spec:
  networkInterface: <demo-worker-interface>   # replace with output of ip route command
  clusterProperty: {}
---
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: kubeslice
  namespace: demo-controller
spec:
  installNamespace: kubeslice-system
  configs:
    - name: demo-controller
      namespace: kubeslice-demo-distributed-mariadb
      group: controller.kubeslice.io
      resource: clusters
---
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: kubeslice
  namespace: demo-worker
spec:
  installNamespace: kubeslice-system
  configs:
    - name: demo-worker
      namespace: kubeslice-demo-distributed-mariadb
      group: controller.kubeslice.io
      resource: clusters
```

Appliquer sur `demo-controller`:

```bash
$ kubectl apply -f registration.yaml
```

Vérifiez qu'OCM déploie les manifestes de travail KubeSlice sur chaque cluster :

```bash
$ kubectl get managedclusteraddon -A
```

**Sortir:**

```
NAMESPACE         NAME        AVAILABLE   DEGRADED   PROGRESSING
demo-controller   kubeslice   Unknown                True
demo-worker       kubeslice   Unknown                True
```

`PROGRESSING: True` signifie qu'OCM se déploie activement. Attendez que `kubeslice-operator` montre `2/2 Running` sur les deux clusters avant de continuer :

```bash
# Run on each spoke cluster
$ kubectl get pods -n kubeslice-system --watch
```

**Résultat attendu (une fois le travailleur KubeSlice entièrement déployé) :**

```
NAME                                 READY   STATUS      RESTARTS   AGE
forwarder-kernel-bw5l4               1/1     Running     0          4m43s
kubeslice-dns-6bd9749f4d-pvh7g       1/1     Running     0          4m43s
kubeslice-install-crds-szhvc         0/1     Completed   0          4m56s
kubeslice-netop-g4dfn                1/1     Running     0          4m43s
kubeslice-operator-949b7d6f7-9wj7h   2/2     Running     0          4m43s
nsc-grpc-server-sbjj7                1/1     Running     0          4m43s
nsm-install-crds-5z4j9               0/1     Completed   0          4m53s
nsmgr-zzwgh                          2/2     Running     0          4m43s
registry-k8s-979455d6d-q2j8x         1/1     Running     0          4m43s
```

#### 5. Espace de noms d'application intégré

Créer un `SliceConfig` embarquer à bord du `demo` (demande) et `kubedb` Espaces de noms (opérateur) pour la connectivité réseau. Créer un `sliceconfig.yaml` déposer:

```yaml
apiVersion: controller.kubeslice.io/v1alpha1
kind: SliceConfig
metadata:
  name: demo-slice
  namespace: kubeslice-demo-distributed-mariadb
spec:
  sliceSubnet: 10.1.0.0/16
  maxClusters: 16
  sliceType: Application
  sliceGatewayProvider:
    sliceGatewayType: Wireguard
    sliceCaType: Local
  sliceIpamType: Local
  rotationInterval: 60
  vpnConfig:
    cipher: AES-128-CBC
  clusters:
    - demo-controller
    - demo-worker
  qosProfileDetails:
    queueType: HTB
    priority: 1
    tcType: BANDWIDTH_CONTROL
    bandwidthCeilingKbps: 5120
    bandwidthGuaranteedKbps: 2560
    dscpClass: AF11
  namespaceIsolationProfile:
    applicationNamespaces:
      - namespace: demo
        clusters:
          - '*'
      - namespace: kubedb
        clusters:
          - '*'
    isolationEnabled: false
    allowedNamespaces:
      - namespace: kube-system
        clusters:
          - '*'
```

Appliquer le `SliceConfig`:

```bash
$ kubectl apply -f sliceconfig.yaml
```

Une fois SliceConfig appliqué, un `vl3-slice-router` le pod apparaîtra dans `kubeslice-system` sur chaque cluster, indiquant que le tunnel VPN de tranche est en cours d'établissement.

#### 6. Configurer DNS pour KubeSlice

> Remarque : Vous devez mettre à jour le serveur DNS pour chaque cluster que vous avez mentionné dans la tranche afin de permettre une découverte appropriée des services entre clusters. Dans ce guide, nous utilisons CoreDNS, les modifications requises sont donc appliquées à la configuration CoreDNS.
> Si votre cluster utilise une solution DNS différente, assurez-vous d'y appliquer des règles de transfert équivalentes.
>
> Cette étape de configuration doit être effectuée sur tous les clusters participant à la tranche avant de continuer.

Mettre à jour CoreDNS pour transférer `*.slice.local` trafic vers le service DNS KubeSlice. Exécutez les étapes suivantes sur **chaque cluster** dans la tranche.

> **Important:** CoreDNS doit être mis à jour et redémarré sur tous les clusters avant de passer à l'étape 4 (installation de KubeDB). Utilisation des nœuds Galera `.slice.local` Noms DNS pour se découvrir entre les clusters. Si le DNS n'est pas configuré avant le démarrage des pods MariaDB, la réplication ne se formera pas.

Obtenez l'adresse IP du service DNS KubeSlice sur chaque cluster :

```bash
$ kubectl get svc -n kubeslice-system -owide -l 'app=kubeslice-dns'
```

**Sortir:**

```bash
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE   SELECTOR
kubeslice-dns   ClusterIP   10.43.172.191   <none>        53/UDP,53/TCP   8d    app=kubeslice-dns
```

Ajoutez le bloc suivant au **haut** de votre CoreDNS `Corefile` ConfigMap (remplacez l'IP par celle de votre cluster) :

```
slice.local:53 {
    errors
    cache 30
    forward . 10.43.172.191
}
```

Exemple de CoreDNS ConfigMap complet après édition :

```bash
$ kubectl get cm -n kube-system coredns -oyaml
```

**Sortir:**

```yaml
apiVersion: v1
data:
  Corefile: |
    slice.local:53 {
        errors
        cache 30
        forward . 10.43.172.191
    }
    .:53 {
        errors
        health
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          fallthrough in-addr.arpa ip6.arpa
        }
        hosts /etc/coredns/NodeHosts {
          ttl 60
          reload 15s
          fallthrough
        }
        prometheus :9153
        cache 30
        loop
        reload
        loadbalance
        import /etc/coredns/custom/*.override
        forward . /etc/resolv.conf
    }
    import /etc/coredns/custom/*.server    
  NodeHosts: |
    10.2.0.248 demo-worker    
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
```

Après avoir modifié le ConfigMap, redémarrez CoreDNS pour appliquer la modification :

```bash
$ kubectl rollout restart deploy/coredns -n kube-system
```

Répétez les étapes de configuration DNS sur chaque cluster de la tranche.

### Étape 4 : Installer l'opérateur KubeDB

> **Note:** Installez l'opérateur KubeDB uniquement sur le cluster hub (`demo-controller`). L'opérateur gère les pods MariaDB sur les clusters Spoke via OCM — aucune installation KubeDB n'est nécessaire sur `demo-worker`.

#### Obtenez une licence gratuite

La licence KubeDB est liée au `kube-system` UID d’espace de noms du cluster hub et a une date d’expiration. Obtenez l'UID de votre cluster et vérifiez la licence avant d'installer :

```bash
# Get your cluster UID (required when requesting the license)
$ kubectl get ns kube-system -o jsonpath='{.metadata.uid}'

# Verify the license is not expired
$ openssl x509 -noout -enddate -in $HOME/Downloads/kubedb-license-<uid>.txt
```

Si elle est expirée ou n'est pas encore obtenue, téléchargez une licence GRATUITE à partir du [Serveur de licences AppsCode](https://appscode.com/issue-license?p=kubedb) en utilisant l'UID du cluster ci-dessus.

```bash
$ helm upgrade -i kubedb oci://ghcr.io/appscode-charts/kubedb \
    --version v2026.2.26 \
    --namespace kubedb --create-namespace \
    --set-file global.license=$HOME/Downloads/kubedb-license-<uid>.txt \
    --set petset.features.ocm.enabled=true \
    --wait --burst-limit=10000 --debug
```

> **Note:** Le `--set petset.features.ocm.enabled=true` L'indicateur doit être défini pour activer la fonctionnalité distribuée MariaDB.

Pour plus de détails, reportez-vous au [Guide d'installation de KubeDB](https://kubedb.com/docs/v2026.7.10/setup/).

Vérifiez que les pods sont en cours d'exécution :

```bash
$ kubectl get pods -n kubedb
```

**Sortir:**

```bash
NAME                                           READY   STATUS    RESTARTS   AGE
kubedb-kubedb-autoscaler-0                     1/2     Running   0          44s
kubedb-kubedb-ops-manager-0                    1/2     Running   0          43s
kubedb-kubedb-provisioner-0                    1/2     Running   0          43s
kubedb-kubedb-webhook-server-df667cd85-tjdp9   2/2     Running   0          44s
kubedb-petset-cf9f5b6f4-d9558                  2/2     Running   0          44s
kubedb-sidekick-5dbf7bcf64-4b8cw               2/2     Running   0          44s
```

### Étape 5 : Définir une politique de placement

Vous pouvez définir le `storageClassName` sous `spec.clusterSpreadConstraint.distributionRules` pour chaque grappe. Si cela n’est pas explicitement spécifié, les clusters sélectionneront automatiquement une classe de stockage appropriée. De plus, vous pouvez contrôler le placement des réplicas en définissant quels réplicas appartiennent à quel cluster. Lors de la mise à l'échelle du nombre de réplicas, la distribution doit également être spécifiée au niveau du cluster. Dans cet exemple, nous utilisons trois répliques.

Pour gérer la distribution des pods entre les clusters, créez un `PlacementPolicy`. A cet effet, définissez un `pod-placement-policy.yaml` fichier comme indiqué ci-dessous :

```yaml
apiVersion: apps.k8s.appscode.com/v1
kind: PlacementPolicy
metadata:
  labels:
    app.kubernetes.io/managed-by: Helm
  name: distributed-mariadb
spec:
  clusterSpreadConstraint:
    distributionRules:
      - clusterName: demo-controller
        storageClassName: local-path   # optional; omit to use the cluster's default storage class
        replicaIndices:
          - 0
          - 2
      - clusterName: demo-worker
        storageClassName: local-path   # optional; omit to use the cluster's default storage class
        replicaIndices:
          - 1
    slice:
      projectNamespace: kubeslice-demo-distributed-mariadb
      sliceName: demo-slice
  nodeSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  zoneSpreadConstraint:
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
```

Cette politique prévoit :

* `mariadb-0` et `mariadb-2` sur `demo-controller`
* `mariadb-1` sur `demo-worker`

Appliquer la politique sur `demo-controller`:

```bash
$ kubectl apply -f pod-placement-policy.yaml --context demo-controller --kubeconfig $HOME/.kube/config
```

### Étape 6 : Créer une instance MariaDB distribuée

Créer le `demo` espace de noms en premier :

```bash
$ kubectl create namespace demo
```

Définir une ressource personnalisée MariaDB avec `spec.distributed` réglé sur `true` et faire référence au `PlacementPolicy`. Créer un `mariadb.yaml` déposer:

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: mariadb
  namespace: demo
spec:
  distributed: true
  deletionPolicy: WipeOut
  replicas: 3
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 500Mi
  storageType: Durable
  version: 12.1.2
  podTemplate:
    spec:
      podPlacementPolicy:
        name: distributed-mariadb
```

Appliquer la ressource sur `demo-controller`:

```bash
$ kubectl apply -f mariadb.yaml --context demo-controller --kubeconfig $HOME/.kube/config
```

### Étape 7 : vérifier le déploiement

#### 1. Vérifiez les ressources et les pods MariaDB sur `demo-controller`

```bash
$ kubectl get md,pods,secret -n demo --context demo-controller --kubeconfig $HOME/.kube/config
```

**Sortir:**

```bash
NAME                         VERSION   STATUS   AGE
mariadb.kubedb.com/mariadb   11.5.2    Ready    99s

NAME            READY   STATUS    RESTARTS   AGE
pod/mariadb-0   3/3     Running   0          95s
pod/mariadb-2   3/3     Running   0          95s

NAME                  TYPE                       DATA   AGE
secret/mariadb-auth   kubernetes.io/basic-auth   2      95s
```

#### 2. Vérifiez les pods et les secrets sur `demo-worker`

```bash
$ kubectl get pods,secrets -n demo --context demo-worker --kubeconfig $HOME/.kube/config
```

**Sortir:**

```bash
NAME        READY   STATUS    RESTARTS   AGE
mariadb-1   3/3     Running   0          95s

NAME                  TYPE                       DATA   AGE
secret/mariadb-auth   kubernetes.io/basic-auth   2      95s
```

#### 3. Vérifiez l'état du cluster Galera

Connectez-vous à un pod MariaDB et vérifiez l'état du cluster Galera. Le DNS du service principal suit le format `<database-name>.<database-namespace>.svc`:

```bash
$ kubectl exec -it -n demo pod/mariadb-0 --context demo-controller -- bash
mariadb -uroot -p$MYSQL_ROOT_PASSWORD -hmariadb.demo.svc
```

Exécutez la requête suivante :

```sql
SHOW STATUS LIKE 'wsrep_cluster_status';
```

**Sortir:**

```bash
+----------------------+---------+
| Variable_name        | Value   |
+----------------------+---------+
| wsrep_cluster_status | Primary |
+----------------------+---------+
1 row in set (0.001 sec)
```

Vérifiez les variables d'état supplémentaires de Galera :

```sql
SHOW STATUS LIKE 'wsrep%';
```

## Prochaines étapes

* **Accéder à la base de données**: Utilisez le `mariadb-auth` secret pour récupérer les informations d'identification et se connecter à l'instance MariaDB.
* **Mise à l'échelle**: Réglez le `PlacementPolicy` pour ajouter ou supprimer des réplicas dans les clusters.
* **Surveillance**: Intégrez KubeDB à des outils de surveillance tels que Prometheus pour obtenir des informations sur l'état du cluster.