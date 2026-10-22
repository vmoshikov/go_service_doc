---
title: etcd-backup — API
type: code-api
components: [etcd-backup]
repo: https://gitlab.example.com/mk8s/etcd-backup
version: v1.5.0
commit: 3f21e81d1571
generated: true
---

# etcd-backup — API

## gRPC: EtcdBackup.CreateBackup

`api/etcd/v1/backup.proto:7` · пакет `mk8s.etcd.v1` · `CreateBackupRequest` → `CreateBackupResponse`

CreateBackup создаёт копию etcd кластера. Возвращает ID задачи.

`CreateBackupRequest`:

| Поле | Тип | № | Описание |
|------|-----|---|----------|
| `cluster_id` | `string` | 1 | ID кластера |
| `storage` | `Storage` | 2 | — |

`CreateBackupResponse`:

| Поле | Тип | № | Описание |
|------|-----|---|----------|
| `task_id` | `string` | 1 | — |

## gRPC: EtcdBackup.ListBackups

`api/etcd/v1/backup.proto:9` · пакет `mk8s.etcd.v1` · `ListBackupsRequest` → `stream Backup`

ListBackups возвращает копии кластера.

HTTP: `GET /v1/clusters/{cluster_id}/backups`

`ListBackupsRequest`:

| Поле | Тип | № | Описание |
|------|-----|---|----------|
| `cluster_id` | `string` | 1 | — |

`Backup`:

| Поле | Тип | № | Описание |
|------|-----|---|----------|
| `id` | `string` | 1 | — |
| `size_bytes` | `int64` | 2 | — |
| `tags` | `repeated string` | 3 | — |

## Перечисления

### Storage

`api/etcd/v1/backup.proto:32`

`STORAGE_UNSPECIFIED` = 0, `STORAGE_S3` = 1

## CRD: EtcdBackupSchedule (mk8s.example.com/v1)

Область: `Namespaced` · хранение: да

| Поле | Тип | Обязательно | По умолчанию | Описание |
|------|-----|-------------|--------------|----------|
| `spec` | object |  |  | — |
| `spec.schedule` | string | да |  | Расписание в формате cron. |
| `spec.retention` | integer |  | `7` | Сколько копий хранить. |
| `spec.storage` | object |  |  | — |
| `spec.storage.bucket` | string |  |  | — |
| `status` | object |  |  | — |
| `status.lastRun` | string (date-time) |  |  | — |

