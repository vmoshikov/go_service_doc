# RULES (правила генерации документации)

Этот репозиторий генерирует документацию по Go‑сервису. Документация хранится в каталоге:

- `docs/<repo_name>/`

где `<repo_name>` — имя репозитория, который “тегнул” генератор (или задано параметром `--repo-name`).

## Какие разделы заполняет скрипт, а какие пользователь

- **Пользователь заполняет вручную** (в исходном Go‑репозитории):
  - `<go_repo>/docs/architecture.md` — архитектура сервиса
  - `<go_repo>/docs/db.md` — структура БД (опционально)
  - `<go_repo>/docs/*.md` — любые дополнительные разделы (“Прочее”)
  
  При генерации документации эти файлы автоматически включаются в `docs/<repo_name>/README.md`.

- **Скрипт заполняет автоматически**:
  - `docs/<repo_name>/README.md` — главный README со сводкой и навигацией (по правилам порядка ниже)
  - `docs/<repo_name>/RULES.md` — снимок применённых правил (генерируется, если отсутствует)
  - `docs/<repo_name>/CHANGELOG.md` — changelog (генерируется как заглушка, если отсутствует)
  - `docs/<repo_name>/sections/functions.md` — функции (индекс по директориям)
  - `docs/<repo_name>/sections/functions/*.md` — функции (группировка по родительской директории каждого .go файла)
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

Приоритет загрузки правил (от высшего к низшему):

1. **`docs/<repo_name>/RULES.md`** в репозитории документации (пользователь может создать перед первой генерацией)
2. **`./rules/<repo_name>.json`** в репозитории генератора (repo-specific override)
3. **Дефолтные правила** (встроенные)

`RULES.md` в репозитории документации создаётся автоматически при первой генерации (если отсутствует) и **не перезаписывается** при последующих запусках, чтобы сохранить пользовательские настройки.

### Дополнительные возможности конфигурации

- **Группировка разделов «Функции» по глубине**
  - В правилах задаётся **`functions_group_depth`**: `1` — по директории верхнего уровня, `2` — по двум уровням пути, `0` или не задано — по полной родительской директории каждого `.go` файла (максимальная детализация). По умолчанию: `2` (меньше файлов в `sections/functions/`).

- **Исключение директорий из анализа**
  - Настройки задаются в JSON-файле: **`docs/<repo_name>/exclude.json`**. Пути — относительно корня анализируемого репозитория; файлы из этих каталогов (и подкаталогов) не участвуют в парсинге.
  - Если файл отсутствует, используется значение из правил (по умолчанию в правилах: `["vendor"]`).

  Пример `docs/<repo_name>/exclude.json`:

  ```json
  {
    "exclude_dirs": ["vendor", "third_party", "generated"]
  }
  ```

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

- **Changelog (по веткам)**
  - Changelog формируется **только по merge-веткам** в теге. 1 ветка = 1 задача = 1 пункт.
  - `changelog.branches_only` — true (по умолчанию): только merge-коммиты
  - `changelog.task_key_pattern` — regex для ключа задачи (форма: ключ-число). Пример: `[A-Z][A-Z0-9]+-\d+` (ABC-123), `[A-Za-z0-9]+-\d+` (гибче)
  - `changelog.branch_prefix_to_category` — маппинг префикса ветки → категория: `feature/` → Добавлено, `fix/` → Исправлено, `remove/` → Удалено и т.д.
  - `changelog.task_tracker_url` — URL трекера для ссылок (иначе JIRA_BASE_URL из env)

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
  ],
  "changelog": {
    "branches_only": true,
    "task_key_pattern": "[A-Z][A-Z0-9]+-\\d+",
    "branch_prefix_to_category": {
      "feature/": "Добавлено",
      "fix/": "Исправлено",
      "remove/": "Удалено"
    },
    "task_tracker_url": null
  }
}
```

