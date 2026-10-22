---
title: etcd-backup — изменения
type: code-changelog
components: [etcd-backup]
repo: https://gitlab.example.com/mk8s/etcd-backup
generated: true
---

# etcd-backup — изменения

Одна merge-ветка — один пункт. Новые версии сверху.

## [v1.5.0] — 2026-10-21

### Добавлено

- Повторные попытки записи в S3 ([MK8S-130](https://jira.example.com/browse/MK8S-130))
  - Влияние на L2/L3: новый алерт EtcdBackupS3Retries, обновить runbook бэкапов.

## [v1.4.0] — 2026-10-21

### Добавлено

- Incremental backup ([MK8S-101](https://jira.example.com/browse/MK8S-101))

### Изменено

- Cleanup ([MK8S-120](https://jira.example.com/browse/MK8S-120))

### Исправлено

- Timeout on large db ([MK8S-117](https://jira.example.com/browse/MK8S-117))

## [v1.3.0] — 2026-10-21

Первая версия в документации. Изменения до неё не собраны.
