# Руководство по интеграции GitLab CI

Это руководство объясняет, как настроить генератор документации для работы как GitLab CI джоба в репозитории docs.

## Обзор

Сервис разработан для работы как GitLab CI джоба, которая:
- Триггерится из внешних репозиториев через webhooks
- Генерирует документацию для каждого проекта
- Сохраняет документацию в проектно-специфичные директории
- Поддерживает конфигурацию корпоративного VPN для pip

## Структура репозитория

```
docs-repo/
├── .gitlab-ci.yml          # CI конфигурация
├── docs/                   # Корень сгенерированной документации
│   ├── project1/          # Документация для project1
│   │   ├── README.md
│   │   └── docs/
│   ├── project2/          # Документация для project2
│   │   ├── README.md
│   │   └── docs/
│   └── <project_id>/       # Каждый проект имеет свою директорию
│       └── user/          # Пользовательская документация
│           ├── user_architecture.md
│           └── user_db_structure.md
└── doc_generator.py       # Генератор документации
```

## Конфигурация GitLab CI

### Базовая настройка

`.gitlab-ci.yml` уже настроен. Вам нужно настроить:

1. **CI/CD Переменные** в GitLab Settings:
   - `CI_PIP_INDEX_URL` - URL корпоративного PyPI (например, `https://pypi.company.com/simple`)
   - `CI_PIP_TRUSTED_HOST` - Хост корпоративного PyPI (например, `pypi.company.com`)

2. **Переменные проекта** (опционально):
   - `PROJECT_REPO_URL` - URL внешнего репозитория для клонирования
   - `PROJECT_REF` - Ветка/тег для checkout (по умолчанию: main)
   - `PROJECT_PATH` - Локальный путь к проекту (если не клонируется)

### Ручной триггер

Запустите джобу вручную:

```bash
# Через GitLab UI: CI/CD > Pipelines > Run Pipeline
# Или через API:
curl -X POST \
  -F token=YOUR_TRIGGER_TOKEN \
  -F ref=main \
  -F "variables[PROJECT_REPO_URL]=https://gitlab.com/group/project.git" \
  -F "variables[PROJECT_REF]=main" \
  https://gitlab.com/api/v4/projects/PROJECT_ID/trigger/pipeline
```

### Webhook триггер

Настройте webhook во внешнем репозитории для триггера генерации документации:

1. Перейдите во внешний проект: Settings > Webhooks
2. Добавьте URL webhook: `https://gitlab.com/api/v4/projects/DOCS_PROJECT_ID/trigger/pipeline`
3. Установите trigger token
4. Выберите события: Push events, Tag push events

## Конфигурация корпоративного VPN

### Вариант 1: CI/CD Переменные (Рекомендуется)

Установите в GitLab: Settings > CI/CD > Variables

```
CI_PIP_INDEX_URL = https://your-corporate-pypi.com/simple
CI_PIP_TRUSTED_HOST = your-corporate-pypi.com
```

### Вариант 2: pip.conf в репозитории

Создайте `pip.conf` в корне репозитория:

```ini
[global]
index-url = https://your-corporate-pypi.com/simple
trusted-host = your-corporate-pypi.com
```

CI джоба автоматически использует его.

## Структура пользовательской документации

Пользовательская документация должна храниться в:

```
docs/
└── <project_id>/
    └── user/
        ├── user_architecture.md
        ├── user_db_structure.md
        └── other_custom.md
```

Где `<project_id>` извлекается из пути проекта (например, `group_project` из `group/project`).

## Идентификация проекта

Проекты идентифицируются по их пути:
- `group/project` → `group_project`
- `namespace:project` → `namespace_project`

Это создает уникальные директории для документации каждого проекта.

## Пример workflow

1. **Внешний репозиторий** делает push изменений
2. **Webhook** триггерит GitLab CI джобу в репозитории docs
3. **CI джоба**:
   - Клонирует внешний репозиторий
   - Генерирует документацию
   - Копирует пользовательские документы из `docs/<project_id>/user/`
   - Сохраняет все в `docs/<project_id>/`
4. **Документация** коммитится и доступна в репозитории docs

## Переменные окружения

### Обязательные
- `PROJECT_REPO_URL` или `PROJECT_PATH` - Источник Go сервиса

### Опциональные
- `PROJECT_REF` - Ветка/тег для checkout (по умолчанию: main)
- `CI_PIP_INDEX_URL` - URL корпоративного PyPI
- `CI_PIP_TRUSTED_HOST` - Хост корпоративного PyPI
- `DOCS_ROOT` - Корневая директория документации (по умолчанию: docs)

## Устранение неполадок

### Установка pip не удается

1. Проверьте переменные `CI_PIP_INDEX_URL` и `CI_PIP_TRUSTED_HOST`
2. Убедитесь в доступе к VPN с GitLab runners
3. Проверьте pip.conf, если используете файловую конфигурацию

### Документация не генерируется

1. Проверьте, что путь проекта правильный
2. Проверьте логи GitLab CI джобы
3. Убедитесь, что репозиторий Go сервиса доступен
4. Проверьте структуру директории пользовательских документов

### Пользовательские документы не найдены

1. Проверьте структуру директории: `docs/<project_id>/user/`
2. Убедитесь, что project_id совпадает (используйте подчеркивания, не слэши)
3. Убедитесь, что файлы имеют правильные имена (`user_architecture.md`, и т.д.)
