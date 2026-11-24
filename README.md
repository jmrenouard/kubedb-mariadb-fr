# KubeDB MariaDB Documentation (v2026.7.10)

Welcome to the offline copy of the KubeDB MariaDB documentation.

- 🇬🇧 [English Version (EN)](en/README.md)
- 🇫🇷 [Version Française (FR)](fr/README.md)

## Architecture Overview

```mermaid
flowchart LR
  CRD["MariaDB / MariaDBOpsRequest CRD"] --> Operator["KubeDB Operator"]
  Operator --> Standalone["Standalone Pod + PVC"]
  Operator --> Galera["Galera Multi-Primary (wsrep)"]
  Operator --> Repl["Primary-Replica + MaxScale Proxy"]
  CRD --> Ops["Day-2 Ops (Scale, Upgrade, TLS, Reconfigure)"]
  Standalone --> Backup["KubeStash / Stash Backup and PITR"]
  Galera --> Backup
  Repl --> Backup
```

