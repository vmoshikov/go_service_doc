---
title: etcd-backup — метрики
type: code-metrics
components: [etcd-backup]
repo: https://gitlab.example.com/mk8s/etcd-backup
version: v1.5.0
commit: 3f21e81d1571
generated: true
---

# etcd-backup — метрики

| Метрика | Тип | Labels | Описание | Код |
|---------|-----|--------|----------|-----|
| `mk8s_etcd_backup_last_success_timestamp_seconds` | gauge | — | Время последнего успешного копирования. | `internal/backup/backup.go:18` |
| `mk8s_etcd_backup_runs_total` | counter_vec | `cluster`, `result` | Число запусков резервного копирования. | `internal/backup/backup.go:11` |
