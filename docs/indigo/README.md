---
title: Документация сервиса
type: readme
repo: indigo
language: ru
chunk_boundary: h2
---

# Документация сервиса
Документация автоматически сгенерирована из Go‑кода.

## Навигация

- [Диаграммы архитектуры](#диаграммы-архитектуры)
- [Импорты](#импорты)
- [Структуры и типы](#структуры-и-типы)
- [Функции](#функции)
- [Спецификация API](#спецификация-api)
- [Тестирование](#тестирование)

---

## Диаграммы архитектуры

Диаграммы сохраняются в директорию `diagrams/`.

- 📄 Подробнее: [diagrams/](diagrams/)
- 🔗 [Зависимости компонентов](diagrams/component_diagram.puml)
- 🔗 [Архитектура сервиса](diagrams/architecture_diagram.puml)


---

## Импорты

- 📄 Подробнее: [sections/imports.md](sections/imports.md)
- 📚 Меню:
  - 🔗 [Навигация](sections/imports.md#навигация)
  - 🔗 [Стандартная библиотека](sections/imports.md#стандартная-библиотека)
  - 🔗 [Внешние зависимости](sections/imports.md#внешние-зависимости)
  - 🔗 [Локальные пакеты](sections/imports.md#локальные-пакеты)
  - 🔗 [Навигация](sections/imports.md#навигация)


---

## Структуры и типы

- 📄 Подробнее: [sections/structures.md](sections/structures.md)
- 📚 Меню:
  - 🔗 [Навигация](sections/structures.md#навигация)
  - 🔗 [api](sections/structures.md#api)
  - 🔗 [atproto](sections/structures.md#atproto)
  - 🔗 [automod](sections/structures.md#automod)
  - 🔗 [backfill](sections/structures.md#backfill)
  - 🔗 [carstore](sections/structures.md#carstore)
  - 🔗 [cmd](sections/structures.md#cmd)
  - 🔗 [events](sections/structures.md#events)
  - 🔗 [fakedata](sections/structures.md#fakedata)
  - 🔗 [lex](sections/structures.md#lex)
  - 🔗 [models](sections/structures.md#models)
  - 🔗 [mst](sections/structures.md#mst)
  - 🔗 [repo](sections/structures.md#repo)
  - 🔗 [repomgr](sections/structures.md#repomgr)
  - 🔗 [search](sections/structures.md#search)
  - 🔗 [splitter](sections/structures.md#splitter)
  - 🔗 [testing](sections/structures.md#testing)
  - 🔗 [util](sections/structures.md#util)
  - 🔗 [xrpc](sections/structures.md#xrpc)
  - 🔗 [Навигация](sections/structures.md#навигация)


---

## Функции

- 📄 Подробнее: [sections/functions.md](sections/functions.md)
- 📚 Меню:
  - 🔗 [Навигация](sections/functions.md#навигация)
  - 🔗 [Группировка по глубине (уровней: 2)](sections/functions.md#группировка-по-глубине-уровней-2)
  - 🔗 [api/agnostic](sections/functions.md#apiagnostic)
  - 🔗 [api/atproto](sections/functions.md#apiatproto)
  - 🔗 [api/bsky](sections/functions.md#apibsky)
  - 🔗 [api/chat](sections/functions.md#apichat)
  - 🔗 [api/ozone](sections/functions.md#apiozone)
  - 🔗 [atproto/atclient](sections/functions.md#atprotoatclient)
  - 🔗 [atproto/atcrypto](sections/functions.md#atprotoatcrypto)
  - 🔗 [atproto/atdata](sections/functions.md#atprotoatdata)
  - 🔗 [atproto/auth](sections/functions.md#atprotoauth)
  - 🔗 [atproto/identity](sections/functions.md#atprotoidentity)
  - 🔗 [atproto/labeling](sections/functions.md#atprotolabeling)
  - 🔗 [atproto/lexicon](sections/functions.md#atprotolexicon)
  - 🔗 [atproto/repo](sections/functions.md#atprotorepo)
  - 🔗 [atproto/syntax](sections/functions.md#atprotosyntax)
  - 🔗 [automod/cachestore](sections/functions.md#automodcachestore)
  - 🔗 [automod/capture](sections/functions.md#automodcapture)
  - 🔗 [automod/consumer](sections/functions.md#automodconsumer)
  - 🔗 [automod/countstore](sections/functions.md#automodcountstore)
  - 🔗 [automod/engine](sections/functions.md#automodengine)
  - 🔗 [automod/flagstore](sections/functions.md#automodflagstore)
  - 🔗 [automod/helpers](sections/functions.md#automodhelpers)
  - 🔗 [automod/keyword](sections/functions.md#automodkeyword)
  - 🔗 [automod/rules](sections/functions.md#automodrules)
  - 🔗 [automod/setstore](sections/functions.md#automodsetstore)
  - 🔗 [automod/visual](sections/functions.md#automodvisual)
  - 🔗 [backfill](sections/functions.md#backfill)
  - 🔗 [carstore](sections/functions.md#carstore)
  - 🔗 [cmd/beemo](sections/functions.md#cmdbeemo)
  - 🔗 [cmd/bluepages](sections/functions.md#cmdbluepages)
  - 🔗 [cmd/collectiondir](sections/functions.md#cmdcollectiondir)
  - 🔗 [cmd/fakermaker](sections/functions.md#cmdfakermaker)
  - 🔗 [cmd/gosky](sections/functions.md#cmdgosky)
  - 🔗 [cmd/hepa](sections/functions.md#cmdhepa)
  - 🔗 [cmd/lexgen](sections/functions.md#cmdlexgen)
  - 🔗 [cmd/netsync](sections/functions.md#cmdnetsync)
  - 🔗 [cmd/palomar](sections/functions.md#cmdpalomar)
  - 🔗 [cmd/rainbow](sections/functions.md#cmdrainbow)
  - 🔗 [cmd/relay](sections/functions.md#cmdrelay)
  - 🔗 [cmd/sonar](sections/functions.md#cmdsonar)
  - 🔗 [cmd/stress](sections/functions.md#cmdstress)
  - 🔗 [cmd/tap](sections/functions.md#cmdtap)
  - 🔗 [events](sections/functions.md#events)
  - 🔗 [events/dbpersist](sections/functions.md#eventsdbpersist)
  - 🔗 [events/diskpersist](sections/functions.md#eventsdiskpersist)
  - 🔗 [events/pebblepersist](sections/functions.md#eventspebblepersist)
  - 🔗 [events/schedulers](sections/functions.md#eventsschedulers)
  - 🔗 [events/yolopersist](sections/functions.md#eventsyolopersist)
  - 🔗 [fakedata](sections/functions.md#fakedata)
  - 🔗 [gen](sections/functions.md#gen)
  - 🔗 [lex](sections/functions.md#lex)
  - 🔗 [lex/lexgen](sections/functions.md#lexlexgen)
  - 🔗 [lex/lexlint](sections/functions.md#lexlexlint)
  - 🔗 [lex/util](sections/functions.md#lexutil)
  - 🔗 [models](sections/functions.md#models)
  - 🔗 [mst](sections/functions.md#mst)
  - 🔗 [repo](sections/functions.md#repo)
  - 🔗 [repo/carutil](sections/functions.md#repocarutil)
  - 🔗 [repomgr](sections/functions.md#repomgr)
  - 🔗 [repomgr/keymgr](sections/functions.md#repomgrkeymgr)
  - 🔗 [search](sections/functions.md#search)
  - 🔗 [splitter](sections/functions.md#splitter)
  - 🔗 [testing](sections/functions.md#testing)
  - 🔗 [util](sections/functions.md#util)
  - 🔗 [util/cliutil](sections/functions.md#utilcliutil)
  - 🔗 [util/labels](sections/functions.md#utillabels)
  - 🔗 [util/ssrf](sections/functions.md#utilssrf)
  - 🔗 [util/svcutil](sections/functions.md#utilsvcutil)
  - 🔗 [util/tracing](sections/functions.md#utiltracing)
  - 🔗 [xrpc](sections/functions.md#xrpc)
  - 🔗 [Навигация](sections/functions.md#навигация)


---

## Спецификация API

- 📄 Подробнее: [sections/api.md](sections/api.md)
- 📚 Меню:
  - 🔗 [Навигация](sections/api.md#навигация)
  - 🔗 [Меню по файлам](sections/api.md#меню-по-файлам)
  - 🔗 [gRPC методы](sections/api.md#grpc-методы)
  - 🔗 [REST эндпоинты](sections/api.md#rest-эндпоинты)
  - 🔗 [Навигация](sections/api.md#навигация)


---

## Тестирование

- 📄 Подробнее: [sections/tests.md](sections/tests.md)
- 📚 Меню:
  - 🔗 [Навигация](sections/tests.md#навигация)
  - 🔗 [Меню по файлам](sections/tests.md#меню-по-файлам)
  - 🔗 [Тесты](sections/tests.md#тесты)
  - 🔗 [Бенчмарки](sections/tests.md#бенчмарки)
  - 🔗 [Примеры](sections/tests.md#примеры)
  - 🔗 [Навигация](sections/tests.md#навигация)


---

