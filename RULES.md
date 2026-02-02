# RULES (правила генерации документации)

Этот репозиторий генерирует документацию по Go‑сервису. Документация хранится в каталоге:

- `docs/<repo_name>/`

где `<repo_name>` — имя репозитория, который “тегнул” генератор (или задано параметром `--repo-name`).

## Какие разделы заполняет скрипт, а какие пользователь

- **Пользователь заполняет вручную** (если нужны):
  - `docs/<repo_name>/user/architecture.md` — архитектура сервиса
  - `docs/<repo_name>/user/db.md` — структура БД (опционально)
  - `docs/<repo_name>/user/*.md` — любые дополнительные разделы (“Прочее”)

- **Скрипт заполняет автоматически**:
  - `docs/<repo_name>/README.md` — главный README со сводкой и навигацией (по правилам порядка ниже)
  - `docs/<repo_name>/RULES.md` — снимок применённых правил (генерируется, если отсутствует)
  - `docs/<repo_name>/CHANGELOG.md` — changelog (генерируется как заглушка, если отсутствует)
  - `docs/<repo_name>/sections/functions.md` — функции (меню + детализация)
  - `docs/<repo_name>/sections/structures.md` — структуры/типы из Go‑кода (best effort)
  - `docs/<repo_name>/sections/api.md` — спецификация API (gRPC + REST)
  - `docs/<repo_name>/sections/tests.md` — тесты/бенчмарки/примеры
  - `docs/<repo_name>/sections/libraries.md` — зависимости из `go.mod`
  - `docs/<repo_name>/sections/imports.md` — импорты и их использование (и типы — best effort)
  - `docs/<repo_name>/diagrams/*.puml` — PlantUML диаграммы компонентов/архитектуры

## Порядок секций в главном README.md

Порядок задаётся в конфиге ниже (`readme_order`). По умолчанию:

1) Архитектура (user)  
2) Структура БД (user, опционально)  
3) Диаграммы архитектуры (auto)  
4) Импорты (auto)  
5) Структуры (auto)  
6) Функции (auto)  
7) Спецификация API (auto)  
8) Тестирование (auto)  
9) Используемые библиотеки (auto)  
10) Прочее (user)

## Конфигурация (используется парсером)

По умолчанию используются встроенные **дефолтные правила**.

Если создать файл `./rules/<repo_name>.json`, то для конкретного репозитория будут использоваться правила из него (поверх дефолта).

`RULES.md` содержит справку и примеры. JSON‑блок ниже оставлен для обратной совместимости, но рекомендуемый способ — `./rules/<repo_name>.json`.

### Дополнительные возможности конфигурации

- **Взаимоисключаемость `imports` и `libraries`**
  - По умолчанию сохраняется **ровно один** из разделов.
  - Стратегия задаётся в `conflicts.imports_vs_libraries`: `"prefer_imports"` или `"prefer_libraries"`.

- **Клонирование git‑репозиториев для импортов (обогащение)**
  - Включается через `features.import_clone.enabled=true`
  - Позволяет для внешних импортов (например `github.com/org/repo/...`) попытаться **склонировать репозиторий** и извлечь типы/структуры для `sections/imports.md`.
  - Настройки:
    - `features.import_clone.max_repos` — лимит репозиториев на запуск
    - `features.import_clone.hosts` — allowlist хостов (пусто = все)
    - `features.import_clone.overrides` — ручные override для нетипичных VCS

```json
{
  "language": "ru",
  "sections": {
    "architecture_user": { "enabled": true, "source": "user" },
    "db_user":           { "enabled": false, "source": "user" },
    "diagrams":          { "enabled": true, "source": "auto" },
    "imports":           { "enabled": true, "source": "auto" },
    "structures":        { "enabled": true, "source": "auto" },
    "functions":         { "enabled": true, "source": "auto" },
    "api":               { "enabled": true, "source": "auto" },
    "tests":             { "enabled": true, "source": "auto" },
    "libraries":         { "enabled": true, "source": "auto" },
    "others_user":       { "enabled": true, "source": "user" }
  },
  "readme_order": [
    "architecture_user",
    "db_user",
    "diagrams",
    "imports",
    "structures",
    "functions",
    "api",
    "tests",
    "libraries",
    "others_user"
  ]
}
```

