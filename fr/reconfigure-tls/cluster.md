> Vous êtes nouveau sur KubeDB ? Veuillez commencer [ici](https://kubedb.com/docs/v2026.7.10/README).

# Reconfigurer MariaDB TLS/SSL (chiffrement de transport)

KubeDB prend en charge la reconfiguration, c'est-à-dire l'ajout, la suppression, la mise à jour et la rotation des certificats TLS/SSL pour la base de données MariaDB existante via une MariaDBOpsRequest. Ce tutoriel vous montrera comment utiliser KubeDB pour reconfigurer le chiffrement TLS/SSL.

## Avant de commencer

* Dans un premier temps, vous devez disposer d'un cluster Kubernetes et l'outil de ligne de commande kubectl doit être configuré pour communiquer avec votre cluster. Si vous n'avez pas encore de cluster, vous pouvez en créer un en utilisant [gentil](https://kind.sigs.k8s.io/docs/user/quick-start/).
* Installer [`cert-manger`](https://cert-manager.io/docs/installation/) v1.6.0 ou version ultérieure sur votre cluster pour gérer vos certificats SSL/TLS.
* Maintenant, installez KubeDB cli sur votre poste de travail et l'opérateur KubeDB dans votre cluster en suivant les étapes [ici](https://kubedb.com/docs/v2026.7.10/setup/README).
* Pour garder les choses isolées, ce didacticiel utilise un espace de noms distinct appelé `demo` tout au long de ce tutoriel.

  ```bash
  $ kubectl create ns demo
  namespace/demo created
  ```

## Ajouter TLS à un cluster MariaDB

Ici, nous allons créer une base de données MariaDB sans TLS puis reconfigurer la base de données pour utiliser TLS.

> **Note:** Étapes de reconfiguration de TLS de MariaDB `Standalone` est identique à MariaDB `Cluster`.

### Déployer MariaDB sans TLS

Dans cette section, nous allons déployer une base de données MariaDB Cluster sans TLS. Dans les prochaines sections, nous reconfigurerons TLS en utilisant `MariaDBOpsRequest` CRD. Vous trouverez ci-dessous le YAML du `MariaDB` CR que nous allons créer,

```yaml
apiVersion: kubedb.com/v1
kind: MariaDB
metadata:
  name: sample-mariadb
  namespace: demo
spec:
  version: "12.1.2"
  replicas: 3
  storageType: Durable
  storage:
    storageClassName: "standard"
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  deletionPolicy: WipeOut
```

Créons le `MariaDB` CR que nous avons montré ci-dessus,

```bash
$ kubectl create -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/sample-mariadb.yaml
mariadb.kubedb.com/sample-mariadb created
```

Maintenant, attends `sample-mariadb` a un statut `Ready`. c'est-à-dire,

```bash
$ kubectl get mariadb -n demo
NAME             VERSION   STATUS   AGE
sample-mariadb   11.8.5    Ready    9m17s
```

```bash
$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.username}' | base64 -d
root

$ kubectl get secrets -n demo sample-mariadb-auth -o jsonpath='{.data.password}' | base64 -d
U6(h_pYrekLZ2OOd

$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb  -- bash
```

```mysql
root@sample-mariadb-0:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 108
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  show variables like '%ssl%';
+---------------------+-----------------------------+
| Variable_name       | Value                       |
+---------------------+-----------------------------+
| have_openssl        | YES                         |
| have_ssl            | DISABLED                    |
| ssl_ca              |                             |
| ssl_capath          |                             |
| ssl_cert            |                             |
| ssl_cipher          |                             |
| ssl_crl             |                             |
| ssl_crlpath         |                             |
| ssl_key             |                             |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020 |
+---------------------+-----------------------------+
10 rows in set (0.001 sec)
```

Nous pouvons vérifier à partir du résultat ci-dessus que TLS est désactivé pour cette base de données.

### Créer un émetteur/clusterIssuer

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
kubectl create secret tls md-ca \
     --cert=ca.crt \
     --key=ca.key \
     --namespace=demo
secret/md-ca created
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
kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10//docs/guides/mariadb/reconfigure-tls/cluster/examples/issuer.yaml
issuer.cert-manager.io/md-issuer created
```

### Créer une demande MariaDBOps

Afin d'ajouter TLS à la base de données, nous devons créer un `MariaDBOpsRequest` CRO avec notre émetteur créé. Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CRO que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-add-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    requireSSL: true
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

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.issuerRef` spécifie le nom de l'émetteur, le type et le groupe d'API.
* `requireSSL` spécifie que les clients qui se connectent au serveur doivent utiliser une connexion sécurisée.
* `spec.tls.certificates` précise les certificats. Vous pouvez en apprendre davantage sur ce domaine sur [ici](../concepts/mariadb.md#spectls).

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-add-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-add-tls created
```

#### Vérifiez que TLS est activé avec succès

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME            TYPE             STATUS       AGE
demo        mdops-add-tls   ReconfigureTLS   Successful   6m6s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi.

Maintenant, nous allons nous connecter à la base de données pour vérifier le `MariaDB` Le serveur a été configuré avec le cryptage TLS/SSL.

Exécutons dans le pod pour vérifier la configuration TLS/SSL,

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
```

```mysql
root@sample-mariadb-0:/ ls /etc/mysql/certs/client
ca.crt  tls.crt  tls.key
```

```bash
root@sample-mariadb-0:/ ls /etc/mysql/certs/server
ca.crt  tls.crt  tls.key
```

```mysql
root@sample-mariadb-0:/ mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 58
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like '%ssl%';
+---------------------+---------------------------------+
| Variable_name       | Value                           |
+---------------------+---------------------------------+
| have_openssl        | YES                             |
| have_ssl            | YES                             |
| ssl_ca              | /etc/mysql/certs/server/ca.crt  |
| ssl_capath          | /etc/mysql/certs/server         |
| ssl_cert            | /etc/mysql/certs/server/tls.crt |
| ssl_cipher          |                                 |
| ssl_crl             |                                 |
| ssl_crlpath         |                                 |
| ssl_key             | /etc/mysql/certs/server/tls.key |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020     |
+---------------------+---------------------------------+
10 rows in set (0.005 sec)

MariaDB [(none)]> show variables like '%require_secure_transport%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| require_secure_transport | ON    |
+--------------------------+-------+
1 row in set (0.005 sec)

MariaDB [(none)]> quit;
Bye
```

Nous pouvons voir à partir du résultat ci-dessus que, `have_ssl` est réglé sur `ture`. Ainsi, la base de données TLS est activée avec succès sur cette base de données.

> Remarque : Ajoutez ou mettez à jour, reconfigurez TLS avec `RequireSSL=true` créera un temps d'arrêt de la base de données pendant `MariaDBOpsRequest` est dans `Progressing` statut.

## Rotation du certificat

Nous allons maintenant faire tourner le certificat de cette base de données. Vérifions d’abord la date d’expiration actuelle du certificat.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/ openssl x509 -in /etc/mysql/certs/client/tls.crt -inform  PEM -enddate -nameopt RFC2253 -noout
notAfter=Apr 13 05:18:43 2022 GMT
```

Le certificat expirera donc à cette heure `Apr 13 05:18:43 2022 GMT`.

### Créer une demande MariaDBOps

Nous allons maintenant l'augmenter à l'aide d'un MariaDBOpsRequest. Ci-dessous se trouve le yaml de la requête ops que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-rotate-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    rotateCertificates: true
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.rotateCertificates` précise que nous souhaitons faire tourner le certificat de cette base de données.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-rotate-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-rotate-tls created
```

#### Vérifier que la rotation du certificat a réussi

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME               TYPE             STATUS       AGE
demo        mdops-rotate-tls   ReconfigureTLS   Successful    3m
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Vérifions maintenant la date d’expiration du certificat.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/# openssl x509 -in /etc/mysql/certs/client/tls.crt -inform  PEM -enddate -nameopt RFC2253 -noout
notAfter=Apr 13 06:04:50 2022 GMT
```

Comme nous pouvons le voir dans le résultat ci-dessus, la rotation du certificat a réussi.

## Mettre à jour le certificat

Nous allons maintenant mettre à jour le certificat du serveur.

* Décrivons le certificat du serveur `sample-mariadb-server-cert`

```bash
$ kubectl describe certificate -n demo sample-mariadb-server-cert
Name:         sample-mariadb-server-cert
Namespace:    demo
Labels:       app.kubernetes.io/component=database
              app.kubernetes.io/instance=sample-mariadb
              app.kubernetes.io/managed-by=kubedb.com
              app.kubernetes.io/name=mariadbs.kubedb.com
Annotations:  <none>
API Version:  cert-manager.io/v1
Kind:         Certificate
Metadata:
  Creation Timestamp:  2022-01-13T05:18:42Z
  Generation:          1
  ...
  Owner References:
    API Version:           kubedb.com/v1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  MariaDB
    Name:                  sample-mariadb
    UID:                   ed8f45c7-7caf-4890-8a9c-b8437b6ca48b
  Resource Version:        241340
  UID:                     3343e971-395d-46df-9536-47194eb96dcc
Spec:
  Common Name:  sample-mariadb.demo.svc
  Dns Names:
    *.sample-mariadb-pods.demo.svc
    *.sample-mariadb-pods.demo.svc.cluster.local
    *.sample-mariadb.demo.svc
    localhost
    sample-mariadb
    sample-mariadb.demo.svc
  Ip Addresses:
    127.0.0.1
  Issuer Ref:
    Group:      cert-manager.io
    Kind:       Issuer
    Name:       md-issuer
  Secret Name:  sample-mariadb-server-cert
  Subject:
    Organizations:
      kubedb:server
  Usages:
    digital signature
    key encipherment
    server auth
    client auth
Status:
  Conditions:
    Last Transition Time:  2022-01-13T05:18:43Z
    Message:               Certificate is up to date and has not expired
    Observed Generation:   1
    Reason:                Ready
    Status:                True
    Type:                  Ready
  Not After:               2022-04-13T06:04:50Z
  Not Before:              2022-01-13T06:04:50Z
  Renewal Time:            2022-03-14T06:04:50Z
  Revision:                6
Events:
  Type    Reason     Age                From          Message
  ----    ------     ----               ----          -------
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-8tnj5"
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-fw6sk"
  Normal  Requested  22m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-cvphm"
  Normal  Requested  20m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-nvhp6"
  Normal  Requested  19m                cert-manager  Created new CertificateRequest resource "sample-mariadb-server-cert-p5287"
  Normal  Reused     19m (x5 over 22m)  cert-manager  Reusing private key stored in existing Secret resource "sample-mariadb-server-cert"
  Normal  Issuing    19m (x6 over 65m)  cert-manager  The certificate has been successfully issued
```

Nous voulons ajouter `subject` et `emailAddresses` dans les spécifications du certificat de serveur.

### Créer une demande MariaDBOps

Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CRO que nous allons créer pour mettre à jour le certificat du serveur,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-update-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    certificates:
    - alias: server
      subject:
        organizations:
        - kubedb:server
      emailAddresses:
      - "[email protected]"
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.issuerRef` spécifie le nom de l'émetteur, le type et le groupe d'API.
* `spec.tls.certificates` spécifie les modifications que nous souhaitons dans les objets de certificat.
* `spec.tls.certificates[].alias` spécifie le type de certificat qui est l'un des suivants : `server`, `client`, `metrics-exporter`.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-update-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-update-tls created
```

#### Vérifiez que le certificat est mis à jour avec succès

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest -n demo
Every 2.0s: kubectl get mariadbopsrequest -n demo
NAME                  TYPE             STATUS        AGE
mdops-update-tls   ReconfigureTLS     Successful      7m
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi.

Maintenant, exécutons-nous dans un nœud de base de données et découvrons le sujet ca pour voir s'il correspond à celui que nous avons fourni.

```bash
$ kubectl exec -it -n demo sample-mariadb-0  -c mariadb -- bash
root@sample-mariadb-0:/ apt update
root@sample-mariadb-0:/ apt install openssl
root@sample-mariadb-0:/ openssl x509 -in /etc/mysql/certs/server/tls.crt -inform PEM  -subject -email -nameopt RFC2253 -noout
subject=CN=sample-mariadb.demo.svc,O=kubedb:server
[email protected]
```

Nous pouvons voir à partir du résultat ci-dessus que le nom du sujet et l'adresse e-mail correspondent au nouveau certificat ca que nous avons créé. Ainsi, l’émetteur est modifié avec succès.

## Supprimer TLS de la base de données

Maintenant, nous allons supprimer TLS de cette base de données à l'aide d'un MariaDBOpsRequest.

### Créer une demande MariaDBOps

Vous trouverez ci-dessous le YAML du `MariaDBOpsRequest` CRO que nous allons créer,

```yaml
apiVersion: ops.kubedb.com/v1alpha1
kind: MariaDBOpsRequest
metadata:
  name: mdops-remove-tls
  namespace: demo
spec:
  type: ReconfigureTLS
  databaseRef:
    name: sample-mariadb
  tls:
    remove: true
```

Ici,

* `spec.databaseRef.name` spécifie que nous effectuons une opération de reconfiguration TLS sur `sample-mariadb` base de données.
* `spec.type` précise que nous effectuons `ReconfigureTLS` sur notre base de données.
* `spec.tls.remove` précise que nous souhaitons supprimer tls de cette base de données.

Créons le `MariaDBOpsRequest` CR que nous avons montré ci-dessus,

```bash
$ kubectl apply -f https://github.com/kubedb/docs/raw/v2026.7.10/docs/guides/mariadb/reconfigure-tls/cluster/examples/mdops-remove-tls.yaml
mariadbopsrequest.ops.kubedb.com/mdops-remove-tls created
```

#### Vérifiez que TLS a été supprimé avec succès

Attendons `MariaDBOpsRequest` être `Successful`. Exécutez la commande suivante pour regarder `MariaDBOpsRequest` CRO,

```bash
$ kubectl get mariadbopsrequest --all-namespaces
NAMESPACE   NAME               TYPE             STATUS       AGE
demo        mdops-remove-tls   ReconfigureTLS   Successful   6m27s
```

Nous pouvons voir à partir du résultat ci-dessus que le `MariaDBOpsRequest` a réussi. Si l'on décrit le `MariaDBOpsRequest` nous aurons un aperçu des étapes qui ont été suivies.

Maintenant, entrons dans la base de données et découvrons si TLS est désactivé ou non.

```bash
$ kubectl exec -it -n demo sample-mariadb-0 -c mariadb  -- bash
root@sample-mariadb-0:/  mariadb -u${MYSQL_ROOT_USERNAME} -p${MYSQL_ROOT_PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 108
Server version: 11.8.5-MariaDB-1:11.8.5+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>  show variables like '%ssl%';
+---------------------+-----------------------------+
| Variable_name       | Value                       |
+---------------------+-----------------------------+
| have_openssl        | YES                         |
| have_ssl            | DISABLED                    |
| ssl_ca              |                             |
| ssl_capath          |                             |
| ssl_cert            |                             |
| ssl_cipher          |                             |
| ssl_crl             |                             |
| ssl_crlpath         |                             |
| ssl_key             |                             |
| version_ssl_library | OpenSSL 1.1.1f  31 Mar 2020 |
+---------------------+-----------------------------+
10 rows in set (0.001 sec)
```

Ainsi, nous pouvons voir à partir de ce qui précède que la sortie indique que tls est désactivé avec succès.

## Nettoyage

Pour nettoyer les ressources Kubernetes créées par ce tutoriel, exécutez :

```bash
$ kubectl delete mariadb -n demo --all
$ kubectl delete issuer -n demo --all
$ kubectl delete mariadbopsrequest -n demo --all
$ kubectl delete ns demo
```