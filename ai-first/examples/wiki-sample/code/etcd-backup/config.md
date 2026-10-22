---
title: etcd-backup — конфигурация чарта
type: code-config
components: [etcd-backup]
chart: charts/etcd-backup
chart_version: 0.8.0
release: 2026.11.0
generated: true
---

# etcd-backup — конфигурация чарта

Чарт `charts/etcd-backup` версии `0.8.0` в платформе `2026.11.0`. Тег образа: `v1.5.0`.
Значения платформы: `platform/values.yaml#etcdBackup`.

Колонка «Платформа» заполнена, если сборка платформы меняет значение чарта.

| Параметр | По умолчанию | Платформа | Описание |
|----------|--------------|-----------|----------|
| `image.repository` | `nexus.example.local/mk8s/etcd-backup` |  | Репозиторий образа. |
| `image.tag` | `v1.5.0` |  | — |
| `replicaCount` | `1` | `2` | Число реплик. |
| `backup.schedule` | `0 */6 * * *` |  | Расписание по умолчанию в формате cron. |
| `backup.retention` | `7` | `14` | Сколько копий хранить. |
| `s3.endpoint` | `""` |  | — |
| `s3.secretKey` | `***` |  | Ключ доступа. Задаётся секретом. |
| `resources` | `{}` |  | — |
