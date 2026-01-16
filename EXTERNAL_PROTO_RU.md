# Конфигурация внешних Proto репозиториев

Это руководство объясняет, как настроить ссылки на внешние protobuf репозитории.

## Обзор

Когда ваш Go сервис использует определения protobuf из других репозиториев или директорий, вы можете настроить генератор документации для создания ссылок на эти внешние proto определения.

## Файл конфигурации

Создайте файл `.doc_config.json` в корневой директории вашего Go сервиса:

```json
{
  "external_repositories": {
    "proto-repo": {
      "url": "https://github.com/your-org/proto-definitions",
      "path": "proto",
      "branch": "main",
      "description": "Общие определения protobuf"
    },
    "common-proto": {
      "url": "https://gitlab.com/your-org/common-proto",
      "path": "definitions",
      "branch": "master",
      "description": "Общие proto определения"
    }
  },
  "proto_mappings": {
    "pbExample": "proto-repo",
    "pbCommon": "common-proto",
    "com.example": "proto-repo"
  }
}
```

## Поля конфигурации

### external_repositories

Определяет внешние репозитории, содержащие proto определения:

- **url**: URL репозитория (GitHub, GitLab или любой Git хостинг)
- **path**: Путь внутри репозитория, где находятся proto файлы
- **branch**: Имя ветки (по умолчанию: "main" или "master")
- **description**: Человекочитаемое описание

### proto_mappings

Сопоставляет имена proto пакетов с именами репозиториев:

- Ключ: Имя proto пакета или префикс (например, `pbExample`, `com.example`)
- Значение: Имя репозитория из `external_repositories`

## Примеры

### Пример 1: Один Proto репозиторий

```json
{
  "external_repositories": {
    "shared-proto": {
      "url": "https://github.com/mycompany/shared-proto",
      "path": "proto",
      "branch": "main",
      "description": "Общие определения protobuf"
    }
  },
  "proto_mappings": {
    "pb": "shared-proto",
    "api": "shared-proto"
  }
}
```

### Пример 2: Несколько Proto репозиториев

```json
{
  "external_repositories": {
    "user-proto": {
      "url": "https://github.com/mycompany/user-service",
      "path": "api/proto",
      "branch": "main",
      "description": "Proto определения сервиса пользователей"
    },
    "order-proto": {
      "url": "https://github.com/mycompany/order-service",
      "path": "proto",
      "branch": "main",
      "description": "Proto определения сервиса заказов"
    }
  },
  "proto_mappings": {
    "pbUser": "user-proto",
    "pbOrder": "order-proto"
  }
}
```

### Пример 3: Локальная директория

Если proto файлы находятся в локальной директории (не в git репозитории):

```json
{
  "external_repositories": {
    "local-proto": {
      "url": "file:///path/to/proto-definitions",
      "path": "",
      "branch": "",
      "description": "Локальные proto определения"
    }
  },
  "proto_mappings": {
    "pb": "local-proto"
  }
}
```

## Как это работает

1. **Обнаружение пакета**: Генератор обнаруживает имена proto пакетов в вашем Go коде (например, `pbExample.ListUsersRequest`)

2. **Поиск сопоставления**: Он ищет имя пакета в `proto_mappings`, чтобы найти репозиторий

3. **Генерация ссылки**: Создает ссылку на proto файл во внешнем репозитории

4. **Документация**: Добавляет ссылку в документацию API

## Генерируемая документация

При настройке документация API будет включать:

```markdown
### ListUsers

ListUsers - это gRPC метод, который принимает pbExample.ListUsersRequest и возвращает pbExample.ListUsersResponse.

**Request Type:** `pbExample.ListUsersRequest` - [Просмотр Proto определения](https://github.com/your-org/proto-definitions/blob/main/proto/example.proto)

**Response Type:** `pbExample.ListUsersResponse` - [Просмотр Proto определения](https://github.com/your-org/proto-definitions/blob/main/proto/example.proto)

*Proto определения из: Общие определения protobuf*
```

## Создание файла конфигурации

Вы можете создать пример файла конфигурации:

```bash
python -c "from config import Config; Config.create_example_config(Path('.'))"
```

Или вручную создайте `.doc_config.json` в корне вашего Go сервиса.

## Поддерживаемые хостинги репозиториев

- **GitHub**: `https://github.com/owner/repo`
- **GitLab**: `https://gitlab.com/owner/repo`
- **Bitbucket**: `https://bitbucket.org/owner/repo`
- **Generic Git**: Любой URL Git хостинга
- **Локальный**: `file:///path/to/directory`

## Устранение неполадок

### Ссылки не появляются

1. Проверьте, что `.doc_config.json` существует в корне вашего Go сервиса
2. Убедитесь, что имена пакетов в `proto_mappings` соответствуют вашим Go импортам
3. Убедитесь, что URL репозиториев правильные и доступны

### Неправильные ссылки

1. Проверьте, что поле `path` соответствует фактическому расположению proto файлов
2. Убедитесь, что имя ветки `branch` правильное
3. Убедитесь, что сопоставление имен пакетов корректно

### Несколько пакетов из одного репозитория

Вы можете сопоставить несколько префиксов пакетов с одним репозиторием:

```json
{
  "proto_mappings": {
    "pbUser": "shared-proto",
    "pbOrder": "shared-proto",
    "pbCommon": "shared-proto"
  }
}
```
