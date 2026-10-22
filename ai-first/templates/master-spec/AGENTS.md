# AGENTS.md — master-spec

Этот репозиторий — единственное место спецификаций платформы Managed Kubernetes. Кода здесь нет.
Правила работы — в `AGENTS.md` репозитория ai-first, раздел «Роли и спецификации».

```
openspec/changes/intents/<key>-<slug>/  discovery.md, intent.md — пишет аналитик, приходит через MR из intent/<KEY>
openspec/changes/<key>-<slug>/          specs/, design.md, tasks.md — пишет разработчик; .openspec.yaml: x-jira, x-intent
openspec/specs/                 main-спеки; меняет только openspec archive
```

- Работай только через скрипты ai-first: `analyst.py`, `developer.py`. Не создавай ветки и папки вручную.
- Ветка `intent/<KEY>` — файлы аналитика. Ветка `change/<KEY>` — файлы разработчика.
- `openspec/changes/intents/` — служебная папка, не change. OpenSpec видит её как change `intents` со `skip_specs: true`.
  Не выбирай `intents` в `/opsx:apply` и `/opsx:archive`. Не меняй `openspec/changes/intents/.openspec.yaml`.
- CI проверяет каждый MR скриптом `spec_guard.py`. MR с чужими файлами не проходит.
