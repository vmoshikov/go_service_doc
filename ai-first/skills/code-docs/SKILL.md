---
name: code-docs
description: Используй для документации компонента или модуля по тегу. Обычно запускает CI ai-first по тегу компонента; вручную — для проверки.
---

# code-docs

Скил создаёт `wiki/code/<имя>/` из репозитория компонента или общего Go-модуля.

## Запуск

```bash
python scripts/code_docs.py etcd-backup v1.4.0                       # клонирует компонент по реестру
python scripts/code_docs.py https://gitlab.example.com/mk8s/etcd-backup v1.4.0   # так вызывает CI
python scripts/code_docs.py etcd-backup v1.4.0 --repo ../etcd-backup # локальный репозиторий на этом теге
```

Первый аргумент — имя из `wiki/code/components.toml` или URL репозитория.
`--since` — предыдущий тег для CHANGELOG. По умолчанию — версия, которую wiki описывает сейчас.

Если wiki уже описывает этот тег или более новый, скрипт ничего не меняет и завершается с кодом 0.
После генерации скрипт обновляет `wiki/index.md` и пишет событие `code` в `wiki/log.md`.

## Источники фактов

| Страница | Источник |
|----------|----------|
| `README.md` | `go.mod`, пакеты и их комментарии, импорты между пакетами, `docs/architecture.md`, тесты; обзор — LLM |
| `api.md` | `.proto`: сервисы, методы, HTTP-привязки, сообщения; CRD из `config/crd/`, `crds/`, `deploy/crds/` и `crds/` чарта |
| `metrics.md` | вызовы `prometheus.New*` и `promauto.New*` |
| `packages.md` | только для модулей: экспортируемые типы, функции, методы |
| `CHANGELOG.md` | merge-коммиты между `--since` и тегом |
| `docs/` | копия `docs/*.md` репозитория, кроме `architecture.md` |

Разбор Go — через tree-sitter. Если tree-sitter не установлен, скрипт завершается ошибкой: `pip install -r requirements.txt`.

## Текст LLM

Обзор компонента и описания без комментария пишет LLM через OpenAI-совместимый API. Настройки:

| Поле | Значение |
|------|----------|
| `openai.base_url` | адрес LLM-шлюза, например `https://llm-gateway.example.local/v1` |
| `openai.api_key` / `OPENAI_API_KEY` | ключ шлюза |
| `docs_llm.model` | модель для документации, например Qwen или DeepSeek; по умолчанию `openai.model` |
| `docs_llm.max_calls` | лимит вызовов на запуск, по умолчанию 300 |
| `docs_llm.cache_dir` | кэш ответов, по умолчанию `.llm-cache/`; CI кэширует его |

Проверки ответа: имена в обратных кавычках есть в фактах парсера; лишние ключи отброшены; нет ПДн и секретов.
Строки с секретами скрипт скрывает до отправки.
Без ключа, при отказе API или с `--no-llm` скрипт пишет только факты. Итог по вызовам — в выводе и в `wiki/log.md`.

## Результат

Каталог `wiki/code/<имя>/`. Файл `config.md` создаёт `release_docs.py`; этот скрипт его не трогает.
