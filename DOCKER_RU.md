# Руководство по использованию Docker

## Быстрый старт

### Сборка образа

```bash
docker build -t go-doc-generator .
```

### Запуск как сервис (Рекомендуется)

Запустите контейнер сервиса (остается запущенным для доступа через exec):

```bash
docker run -d --name doc-gen \
  -v /path/to/your/go-service:/workspace \
  go-doc-generator
```

### Выполнение команд

После запуска контейнера вы можете выполнять команды:

```bash
# Генерация документации
docker exec -it doc-gen doc_generator.py /workspace

# Генерация с пользовательским именем файла
docker exec -it doc-gen doc_generator.py /workspace --output CUSTOM_README.md

# Доступ к интерактивному shell
docker exec -it doc-gen bash

# Список файлов в workspace
docker exec -it doc-gen ls -la /workspace

# Просмотр сгенерированных документов
docker exec -it doc-gen ls -la /workspace/docs

# Проверка существования Go сервиса
docker exec -it doc-gen test -d /workspace && echo "Directory exists"
```

### Просмотр логов контейнера

```bash
docker logs doc-gen
```

### Остановка и удаление

```bash
docker stop doc-gen
docker rm doc-gen
```

## Использование Docker Compose

### Запуск сервиса

```bash
docker-compose up -d
```

### Выполнение генератора

```bash
docker-compose exec doc-generator doc_generator.py /workspace
```

### Доступ к shell

```bash
docker-compose exec doc-generator bash
```

### Остановка сервиса

```bash
docker-compose down
```

## Монтирование нескольких путей

Вы можете монтировать несколько директорий:

```bash
docker run -d --name doc-gen \
  -v /path/to/go-service-1:/workspace/service1 \
  -v /path/to/go-service-2:/workspace/service2 \
  go-doc-generator

# Генерация документации для сервиса 1
docker exec -it doc-gen doc_generator.py /workspace/service1

# Генерация документации для сервиса 2
docker exec -it doc-gen doc_generator.py /workspace/service2
```

## Устранение неполадок

### Проверка запущен ли контейнер

```bash
docker ps | grep doc-gen
```

### Просмотр статуса контейнера

```bash
docker inspect doc-gen
```

### Доступ к контейнеру даже если он остановлен

```bash
docker start doc-gen
docker exec -it doc-gen bash
```

### Пересборка после изменений кода

```bash
docker build -t go-doc-generator .
docker stop doc-gen && docker rm doc-gen
docker run -d --name doc-gen -v /path/to/go-service:/workspace go-doc-generator
```
