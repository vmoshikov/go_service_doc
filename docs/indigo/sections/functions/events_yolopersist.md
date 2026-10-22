---
title: "Функции: events/yolopersist"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: events/yolopersist
---


# Функции: events/yolopersist


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_schedulers.md)

- [Следующая директория](fakedata.md)


---


## Меню по файлам


- 📄 [events/yolopersist/yolopersist.go](#eventsyolopersistyolopersistgo)


---


## events/yolopersist/yolopersist.go


📄 Исходный файл: `events/yolopersist/yolopersist.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Flush](#flush-eventsyolopersistyolopersistgo60) `:60`

- 🔗 [NewYoloPersister](#newyolopersister-eventsyolopersistyolopersistgo20) `:20`

- 🔗 [Persist](#persist-eventsyolopersistyolopersistgo24) `:24`

- 🔗 [Playback](#playback-eventsyolopersistyolopersistgo48) `:48`

- 🔗 [SetEventBroadcaster](#seteventbroadcaster-eventsyolopersistyolopersistgo56) `:56`

- 🔗 [Shutdown](#shutdown-eventsyolopersistyolopersistgo64) `:64`

- 🔗 [TakeDownRepo](#takedownrepo-eventsyolopersistyolopersistgo52) `:52`


</details>


[function] name: Flush file: events/yolopersist/yolopersist.go:60 returns_error: нет description: —


### Flush (events/yolopersist/yolopersist.go:60)


Flush is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (yp *YoloPersister) Flush((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "Ctx": {},
  "Err": {},
  "Logger": null,
  "engine": null,
  "effects": null
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `events/yolopersist/yolopersist.go:60`



---


[function] name: NewYoloPersister file: events/yolopersist/yolopersist.go:20 returns_error: нет description: —


### NewYoloPersister (events/yolopersist/yolopersist.go:20)


NewYoloPersister is a function that performs operations based on the provided parameters and returns ().


```go
func NewYoloPersister(()) ()
```


📍 *Расположение:* `events/yolopersist/yolopersist.go:20`



---


[function] name: Persist file: events/yolopersist/yolopersist.go:24 returns_error: нет description: —


### Persist (events/yolopersist/yolopersist.go:24)


Persist is a method that performs operations based on the provided parameters and returns (ctx context.Context, e *events.XRPCStreamEvent).


```go
func (yp *YoloPersister) Persist((ctx context.Context, e *events.XRPCStreamEvent)) (ctx context.Context, e *events.XRPCStreamEvent)
```


**Тип запроса:** events.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "Ctx": {},
  "Err": {},
  "Logger": null,
  "engine": null,
  "effects": null
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** events.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `events/yolopersist/yolopersist.go:24`



---


[function] name: Playback file: events/yolopersist/yolopersist.go:48 returns_error: да description: —


### Playback (events/yolopersist/yolopersist.go:48)


Playback is a method that performs operations based on the provided parameters and may return an error.


```go
func (mp *YoloPersister) Playback((ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)) (ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)
```


**Тип запроса:** events.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "Ctx": {},
  "Err": {},
  "Logger": null,
  "engine": null,
  "effects": null
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** since


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** events.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `since int64`, `cb func(*events.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/yolopersist/yolopersist.go:48`



---


[function] name: SetEventBroadcaster file: events/yolopersist/yolopersist.go:56 returns_error: нет description: —


### SetEventBroadcaster (events/yolopersist/yolopersist.go:56)


SetEventBroadcaster is a method that updates data based on the provided parameters and returns (brc func(*events.XRPCStreamEvent)).


```go
func (yp *YoloPersister) SetEventBroadcaster((brc func(*events.XRPCStreamEvent))) (brc func(*events.XRPCStreamEvent))
```


**Тип запроса:** events.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** brc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** events.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `events/yolopersist/yolopersist.go:56`



---


[function] name: Shutdown file: events/yolopersist/yolopersist.go:64 returns_error: нет description: —


### Shutdown (events/yolopersist/yolopersist.go:64)


Shutdown is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (yp *YoloPersister) Shutdown((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "Ctx": {},
  "Err": {},
  "Logger": null,
  "engine": null,
  "effects": null
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `events/yolopersist/yolopersist.go:64`



---


[function] name: TakeDownRepo file: events/yolopersist/yolopersist.go:52 returns_error: нет description: —


### TakeDownRepo (events/yolopersist/yolopersist.go:52)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid models.Uid).


```go
func (yp *YoloPersister) TakeDownRepo((ctx context.Context, uid models.Uid)) (ctx context.Context, uid models.Uid)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "Ctx": {},
  "Err": {},
  "Logger": null,
  "engine": null,
  "effects": null
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** models.Uid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/yolopersist/yolopersist.go:52`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_schedulers.md)

- [Следующая директория](fakedata.md)


---

