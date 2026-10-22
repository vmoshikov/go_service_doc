---
title: "Функции: events/dbpersist"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: events/dbpersist
---


# Функции: events/dbpersist


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events.md)

- [Следующая директория](events_diskpersist.md)


---


## Меню по файлам


- 📄 [events/dbpersist/dbpersist.go](#eventsdbpersistdbpersistgo)


---


## events/dbpersist/dbpersist.go


📄 Исходный файл: `events/dbpersist/dbpersist.go`


<details open>
<summary><b>Функции в этом файле (24)</b></summary>


- 🔗 [AddItemToBatch](#additemtobatch-eventsdbpersistdbpersistgo192) `:192`

- 🔗 [DefaultOptions](#defaultoptions-eventsdbpersistdbpersistgo42) `:42`

- 🔗 [Flush](#flush-eventsdbpersistdbpersistgo148) `:148`

- 🔗 [NewDbPersistence](#newdbpersistence-eventsdbpersistdbpersistgo93) `:93`

- 🔗 [Persist](#persist-eventsdbpersistdbpersistgo209) `:209`

- 🔗 [Playback](#playback-eventsdbpersistdbpersistgo352) `:352`

- 🔗 [RecordFromRepoAccount](#recordfromrepoaccount-eventsdbpersistdbpersistgo263) `:263`

- 🔗 [RecordFromRepoCommit](#recordfromrepocommit-eventsdbpersistdbpersistgo283) `:283`

- 🔗 [RecordFromRepoIdentity](#recordfromrepoidentity-eventsdbpersistdbpersistgo245) `:245`

- 🔗 [RecordFromRepoSync](#recordfromreposync-eventsdbpersistdbpersistgo330) `:330`

- 🔗 [SetEventBroadcaster](#seteventbroadcaster-eventsdbpersistdbpersistgo144) `:144`

- 🔗 [Shutdown](#shutdown-eventsdbpersistdbpersistgo630) `:630`

- 🔗 [TakeDownRepo](#takedownrepo-eventsdbpersistdbpersistgo618) `:618`

- 🔗 [batchFlusher](#batchflusher-eventsdbpersistdbpersistgo126) `:126`

- 🔗 [deleteAllEventsForUser](#deletealleventsforuser-eventsdbpersistdbpersistgo622) `:622`

- 🔗 [didForUid](#didforuid-eventsdbpersistdbpersistgo483) `:483`

- 🔗 [flushBatchLocked](#flushbatchlocked-eventsdbpersistdbpersistgo154) `:154`

- 🔗 [hydrateAccountEvent](#hydrateaccountevent-eventsdbpersistdbpersistgo512) `:512`

- 🔗 [hydrateBatch](#hydratebatch-eventsdbpersistdbpersistgo401) `:401`

- 🔗 [hydrateCommit](#hydratecommit-eventsdbpersistdbpersistgo528) `:528`

- 🔗 [hydrateIdentityEvent](#hydrateidentityevent-eventsdbpersistdbpersistgo498) `:498`

- 🔗 [hydrateSyncEvent](#hydratesyncevent-eventsdbpersistdbpersistgo585) `:585`

- 🔗 [readCarSlice](#readcarslice-eventsdbpersistdbpersistgo608) `:608`

- 🔗 [uidForDid](#uidfordid-eventsdbpersistdbpersistgo468) `:468`


</details>


[function] name: AddItemToBatch file: events/dbpersist/dbpersist.go:192 returns_error: нет description: —


### AddItemToBatch (events/dbpersist/dbpersist.go:192)


AddItemToBatch is a method that creates new data based on the provided parameters and returns (ctx context.Context, rec *RepoEventRecord, evt *events.XRPCStreamEvent).


```go
func (p *DbPersistence) AddItemToBatch((ctx context.Context, rec *RepoEventRecord, evt *events.XRPCStreamEvent)) (ctx context.Context, rec *RepoEventRecord, evt *events.XRPCStreamEvent)
```


**Тип запроса:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


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


**Тип ответа:** rec


```json
{
  "db": null,
  "collections": {},
  "collectionNames": {},
  "maxCollectionId": 0,
  "collectionsLock": {},
  "log": null
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


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


📍 *Расположение:* `events/dbpersist/dbpersist.go:192`



---


[function] name: DefaultOptions file: events/dbpersist/dbpersist.go:42 returns_error: нет description: —


### DefaultOptions (events/dbpersist/dbpersist.go:42)


DefaultOptions is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultOptions(()) ()
```


📍 *Расположение:* `events/dbpersist/dbpersist.go:42`



---


[function] name: Flush file: events/dbpersist/dbpersist.go:148 returns_error: нет description: —


### Flush (events/dbpersist/dbpersist.go:148)


Flush is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (p *DbPersistence) Flush((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/dbpersist/dbpersist.go:148`



---


[function] name: NewDbPersistence file: events/dbpersist/dbpersist.go:93 returns_error: да description: —


### NewDbPersistence (events/dbpersist/dbpersist.go:93)


NewDbPersistence is a function that performs operations based on the provided parameters and may return an error.


```go
func NewDbPersistence((*DbPersistence, error)) (*DbPersistence, error)
```


**Тип запроса:** DbPersistence


```json
{
  "db": null,
  "cs": {},
  "lk": {},
  "broadcast": {},
  "batch": [],
  "batchOptions": {},
  "lastFlush": {},
  "uidCache": null,
  "didCache": null
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Тип ответа:** DbPersistence


```json
{
  "db": null,
  "cs": {},
  "lk": {},
  "broadcast": {},
  "batch": [],
  "batchOptions": {},
  "lastFlush": {},
  "uidCache": null,
  "didCache": null
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DbPersistence`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:93`



---


[function] name: Persist file: events/dbpersist/dbpersist.go:209 returns_error: нет description: —


### Persist (events/dbpersist/dbpersist.go:209)


Persist is a method that performs operations based on the provided parameters and returns (ctx context.Context, e *events.XRPCStreamEvent).


```go
func (p *DbPersistence) Persist((ctx context.Context, e *events.XRPCStreamEvent)) (ctx context.Context, e *events.XRPCStreamEvent)
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


📍 *Расположение:* `events/dbpersist/dbpersist.go:209`



---


[function] name: Playback file: events/dbpersist/dbpersist.go:352 returns_error: да description: —


### Playback (events/dbpersist/dbpersist.go:352)


Playback is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) Playback((ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)) (ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)
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


📍 *Расположение:* `events/dbpersist/dbpersist.go:352`



---


[function] name: RecordFromRepoAccount file: events/dbpersist/dbpersist.go:263 returns_error: да description: —


### RecordFromRepoAccount (events/dbpersist/dbpersist.go:263)


RecordFromRepoAccount is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) RecordFromRepoAccount((*RepoEventRecord, error)) (*RepoEventRecord, error)
```


**Тип запроса:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Тип ответа:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoEventRecord`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:263`



---


[function] name: RecordFromRepoCommit file: events/dbpersist/dbpersist.go:283 returns_error: да description: —


### RecordFromRepoCommit (events/dbpersist/dbpersist.go:283)


RecordFromRepoCommit is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) RecordFromRepoCommit((*RepoEventRecord, error)) (*RepoEventRecord, error)
```


**Тип запроса:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Тип ответа:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoEventRecord`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:283`



---


[function] name: RecordFromRepoIdentity file: events/dbpersist/dbpersist.go:245 returns_error: да description: —


### RecordFromRepoIdentity (events/dbpersist/dbpersist.go:245)


RecordFromRepoIdentity is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) RecordFromRepoIdentity((*RepoEventRecord, error)) (*RepoEventRecord, error)
```


**Тип запроса:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Тип ответа:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoEventRecord`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:245`



---


[function] name: RecordFromRepoSync file: events/dbpersist/dbpersist.go:330 returns_error: да description: —


### RecordFromRepoSync (events/dbpersist/dbpersist.go:330)


RecordFromRepoSync is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) RecordFromRepoSync((*RepoEventRecord, error)) (*RepoEventRecord, error)
```


**Тип запроса:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Тип ответа:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoEventRecord`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:330`



---


[function] name: SetEventBroadcaster file: events/dbpersist/dbpersist.go:144 returns_error: нет description: —


### SetEventBroadcaster (events/dbpersist/dbpersist.go:144)


SetEventBroadcaster is a method that updates data based on the provided parameters and returns (brc func(*events.XRPCStreamEvent)).


```go
func (p *DbPersistence) SetEventBroadcaster((brc func(*events.XRPCStreamEvent))) (brc func(*events.XRPCStreamEvent))
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


📍 *Расположение:* `events/dbpersist/dbpersist.go:144`



---


[function] name: Shutdown file: events/dbpersist/dbpersist.go:630 returns_error: нет description: —


### Shutdown (events/dbpersist/dbpersist.go:630)


Shutdown is a method that performs operations based on the provided parameters and returns (context.Context).


```go
func (p *DbPersistence) Shutdown((context.Context)) (context.Context)
```


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


📍 *Расположение:* `events/dbpersist/dbpersist.go:630`



---


[function] name: TakeDownRepo file: events/dbpersist/dbpersist.go:618 returns_error: нет description: —


### TakeDownRepo (events/dbpersist/dbpersist.go:618)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, usr models.Uid).


```go
func (p *DbPersistence) TakeDownRepo((ctx context.Context, usr models.Uid)) (ctx context.Context, usr models.Uid)
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


**Тип ответа:** usr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.Uid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/dbpersist/dbpersist.go:618`



---


[function] name: batchFlusher file: events/dbpersist/dbpersist.go:126 returns_error: нет description: —


### batchFlusher (events/dbpersist/dbpersist.go:126)


batchFlusher is a method that performs operations based on the provided parameters and returns ().


```go
func (p *DbPersistence) batchFlusher(()) ()
```


📍 *Расположение:* `events/dbpersist/dbpersist.go:126`



---


[function] name: deleteAllEventsForUser file: events/dbpersist/dbpersist.go:622 returns_error: нет description: —


### deleteAllEventsForUser (events/dbpersist/dbpersist.go:622)


deleteAllEventsForUser is a method that performs operations based on the provided parameters and returns (ctx context.Context, usr models.Uid).


```go
func (p *DbPersistence) deleteAllEventsForUser((ctx context.Context, usr models.Uid)) (ctx context.Context, usr models.Uid)
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


**Тип ответа:** usr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.Uid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/dbpersist/dbpersist.go:622`



---


[function] name: didForUid file: events/dbpersist/dbpersist.go:483 returns_error: да description: —


### didForUid (events/dbpersist/dbpersist.go:483)


didForUid is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) didForUid((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:483`



---


[function] name: flushBatchLocked file: events/dbpersist/dbpersist.go:154 returns_error: нет description: —


### flushBatchLocked (events/dbpersist/dbpersist.go:154)


flushBatchLocked is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (p *DbPersistence) flushBatchLocked((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/dbpersist/dbpersist.go:154`



---


[function] name: hydrateAccountEvent file: events/dbpersist/dbpersist.go:512 returns_error: да description: —


### hydrateAccountEvent (events/dbpersist/dbpersist.go:512)


hydrateAccountEvent is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) hydrateAccountEvent((*events.XRPCStreamEvent, error)) (*events.XRPCStreamEvent, error)
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


*Типы возврата:* `*events.XRPCStreamEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:512`



---


[function] name: hydrateBatch file: events/dbpersist/dbpersist.go:401 returns_error: да description: —


### hydrateBatch (events/dbpersist/dbpersist.go:401)


hydrateBatch is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) hydrateBatch((ctx context.Context, batch []*RepoEventRecord, cb func(*events.XRPCStreamEvent) error)) (ctx context.Context, batch []*RepoEventRecord, cb func(*events.XRPCStreamEvent) error)
```


**Тип запроса:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


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


**Тип ответа:** batch


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RepoEventRecord


```json
{
  "Seq": 0,
  "Rev": "string",
  "Since": "string",
  "Commit": null,
  "Prev": null,
  "NewHandle": "string",
  "Time": {},
  "Blobs": [],
  "Repo": {},
  "Type": "string",
  "Rebase": false,
  "Active": false,
  "Status": "string",
  "Ops": []
}
```


*Определено в:* `events/dbpersist/dbpersist.go`


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


*Типы возврата:* `ctx context.Context`, `batch []*RepoEventRecord`, `cb func(*events.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:401`



---


[function] name: hydrateCommit file: events/dbpersist/dbpersist.go:528 returns_error: да description: —


### hydrateCommit (events/dbpersist/dbpersist.go:528)


hydrateCommit is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) hydrateCommit((*events.XRPCStreamEvent, error)) (*events.XRPCStreamEvent, error)
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


*Типы возврата:* `*events.XRPCStreamEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:528`



---


[function] name: hydrateIdentityEvent file: events/dbpersist/dbpersist.go:498 returns_error: да description: —


### hydrateIdentityEvent (events/dbpersist/dbpersist.go:498)


hydrateIdentityEvent is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) hydrateIdentityEvent((*events.XRPCStreamEvent, error)) (*events.XRPCStreamEvent, error)
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


*Типы возврата:* `*events.XRPCStreamEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:498`



---


[function] name: hydrateSyncEvent file: events/dbpersist/dbpersist.go:585 returns_error: да description: —


### hydrateSyncEvent (events/dbpersist/dbpersist.go:585)


hydrateSyncEvent is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) hydrateSyncEvent((*events.XRPCStreamEvent, error)) (*events.XRPCStreamEvent, error)
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


*Типы возврата:* `*events.XRPCStreamEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:585`



---


[function] name: readCarSlice file: events/dbpersist/dbpersist.go:608 returns_error: да description: —


### readCarSlice (events/dbpersist/dbpersist.go:608)


readCarSlice is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) readCarSlice(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:608`



---


[function] name: uidForDid file: events/dbpersist/dbpersist.go:468 returns_error: да description: —


### uidForDid (events/dbpersist/dbpersist.go:468)


uidForDid is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *DbPersistence) uidForDid((models.Uid, error)) (models.Uid, error)
```


**Тип ответа:** models.Uid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `models.Uid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/dbpersist/dbpersist.go:468`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events.md)

- [Следующая директория](events_diskpersist.md)


---

