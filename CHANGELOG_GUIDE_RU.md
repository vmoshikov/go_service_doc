# Руководство по генератору CHANGELOG

Генератор CHANGELOG автоматически создает и обновляет `CHANGELOG.md`, следуя формату [keepachangelog.com](https://keepachangelog.com/).

## Возможности

- ✅ **Интеграция с Git**: Анализирует историю коммитов git
- ✅ **Анализ Tree-sitter**: Понимает изменения в коде (функции, API, структуры)
- ✅ **На основе AI**: Генерирует человекочитаемые записи changelog
- ✅ **Стандартный формат**: Следует формату keepachangelog.com
- ✅ **Автоматическая категоризация**: Группирует изменения в Added/Changed/Deprecated/Removed/Fixed/Security

## Использование

### Базовое использование

```bash
# Генерация changelog для коммитов с последнего git тега
python changelog_generator.py /path/to/go-service
```

### С версией

```bash
# Указать номер версии
python changelog_generator.py /path/to/go-service --version 1.2.0
```

### С определенного тега/коммита

```bash
# Анализ коммитов с определенного тега
python changelog_generator.py /path/to/go-service --since v1.0.0

# Анализ последних N коммитов
python changelog_generator.py /path/to/go-service --since HEAD~10
```

## Как это работает

### 1. Анализ Git

Генератор:
- Анализирует историю коммитов git
- Извлекает сообщения коммитов, авторов, даты
- Определяет измененные файлы
- Получает diff для анализа кода

### 2. Анализ кода (Tree-sitter)

Для каждого измененного файла он обнаруживает:
- **Добавленные функции**: Новые определения функций
- **Удаленные функции**: Удаленные функции
- **Измененные функции**: Модифицированные функции
- **API эндпоинты**: Новые/удаленные REST/gRPC эндпоинты
- **Изменения структур**: Модифицированные структуры данных

### 3. Генерация AI

Использует AI для генерации человекочитаемых описаний:
- Анализирует имена и сигнатуры функций
- Понимает контекст из сообщений коммитов
- Создает четкие, лаконичные записи changelog

### 4. Категоризация

Автоматически категоризирует изменения:
- **Added**: Новые функции, функции, эндпоинты
- **Changed**: Измененная существующая функциональность
- **Deprecated**: Функции, помеченные для удаления
- **Removed**: Удаленные функции
- **Fixed**: Исправления ошибок
- **Security**: Изменения, связанные с безопасностью

## Формат вывода

Сгенерированный CHANGELOG.md следует этой структуре:

```markdown
# Changelog

Все значительные изменения в этом проекте будут документированы в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
и этот проект следует [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2024-01-15

### Added
- Добавлена функция `ListUsers()` в пакете handlers
- Добавлен эндпоинт GET /api/users

### Changed
- Обновлена функция `CreateUser()` в пакете handlers

### Fixed
- Исправлена ошибка аутентификации в обработчике входа

### Security
- Исправлена уязвимость SQL инъекции в запросе пользователей
```

## Анализ сообщений коммитов

Генератор анализирует сообщения коммитов для категоризации изменений:

- **Security**: Ключевые слова типа "security", "vulnerability", "CVE", "exploit"
- **Fixed**: Ключевые слова типа "fix", "bug", "error", "issue"
- **Deprecated**: Ключевые слова типа "deprecate", "obsolete"

## Интеграция с CI/CD

### Пример GitHub Actions

```yaml
name: Generate CHANGELOG

on:
  push:
    tags:
      - 'v*'

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Generate CHANGELOG
        run: |
          python changelog_generator.py . --version ${{ github.ref_name }}
      
      - name: Commit CHANGELOG
        run: |
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add CHANGELOG.md
          git commit -m "Update CHANGELOG for ${{ github.ref_name }}" || exit 0
          git push
```

## Настройка

### Интеграция AI

Чтобы использовать реальный AI (вместо демо строк), обновите `generators/ai_changelog.py`:

```python
def generate_changelog_entry(change_type: str, item: Dict) -> str:
    # Замените на ваш вызов AI API
    # Пример с OpenAI:
    import openai
    
    prompt = f"Сгенерируйте запись changelog для: {change_type} - {item}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

### Пользовательская категоризация

Измените `changelog/code_analyzer.py` для настройки категоризации изменений в соответствии с соглашениями вашего проекта.

## Лучшие практики

1. **Используйте Semantic Versioning**: Тегируйте релизы в формате `v1.0.0`
2. **Пишите четкие сообщения коммитов**: Помогает AI генерировать лучшие описания
3. **Запускайте перед релизами**: Генерируйте changelog перед созданием нового тега
4. **Проверяйте сгенерированные записи**: Контент, сгенерированный AI, должен быть проверен
5. **Ручные правки**: Вы можете вручную редактировать CHANGELOG.md - новые записи добавляются в начало

## Устранение неполадок

### Коммиты не найдены

Если вы видите "No new commits found":
- Проверьте, есть ли у вас git теги: `git tag`
- Попробуйте указать `--since HEAD~50` для анализа последних коммитов
- Убедитесь, что вы находитесь в git репозитории

### Отсутствующие изменения

Генератор фокусируется на:
- Определениях функций
- API эндпоинтах
- Значительных изменениях в коде

Незначительные изменения (комментарии, форматирование) могут не появиться. Вы можете вручную добавить записи в CHANGELOG.md.

### Обнаружение версии

Если автоматическое обнаружение версии не работает:
- Убедитесь, что у вас есть git теги: `git tag -a v1.0.0 -m "Release 1.0.0"`
- Или укажите версию вручную: `--version 1.0.0`
