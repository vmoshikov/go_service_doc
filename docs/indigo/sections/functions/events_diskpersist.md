---
title: "Функции: events/diskpersist"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: events/diskpersist
---


# Функции: events/diskpersist


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_dbpersist.md)

- [Следующая директория](events_pebblepersist.md)


---


## Меню по файлам


- 📄 [events/diskpersist/diskpersist.go](#eventsdiskpersistdiskpersistgo)


---


## events/diskpersist/diskpersist.go


📄 Исходный файл: `events/diskpersist/diskpersist.go`


<details open>
<summary><b>Функции в этом файле (30)</b></summary>


- 🔗 [DefaultDiskPersistOptions](#defaultdiskpersistoptions-eventsdiskpersistdiskpersistgo85) `:85`

- 🔗 [Flush](#flush-eventsdiskpersistdiskpersistgo903) `:903`

- 🔗 [Len64](#len64-eventsdiskpersistdiskpersistgo565) `:565`

- 🔗 [NewDiskPersistence](#newdiskpersistence-eventsdiskpersistdiskpersistgo95) `:95`

- 🔗 [Persist](#persist-eventsdiskpersistdiskpersistgo493) `:493`

- 🔗 [Playback](#playback-eventsdiskpersistdiskpersistgo631) `:631`

- 🔗 [PlaybackLogfiles](#playbacklogfiles-eventsdiskpersistdiskpersistgo658) `:658`

- 🔗 [Read](#read-eventsdiskpersistdiskpersistgo838) `:838`

- 🔗 [SetEventBroadcaster](#seteventbroadcaster-eventsdiskpersistdiskpersistgo922) `:922`

- 🔗 [Shutdown](#shutdown-eventsdiskpersistdiskpersistgo912) `:912`

- 🔗 [TakeDownRepo](#takedownrepo-eventsdiskpersistdiskpersistgo783) `:783`

- 🔗 [addJobToQueue](#addjobtoqueue-eventsdiskpersistdiskpersistgo290) `:290`

- 🔗 [deleteEventsForUser](#deleteeventsforuser-eventsdiskpersistdiskpersistgo845) `:845`

- 🔗 [doPersist](#dopersist-eventsdiskpersistdiskpersistgo447) `:447`

- 🔗 [flushLog](#flushlog-eventsdiskpersistdiskpersistgo327) `:327`

- 🔗 [flushRoutine](#flushroutine-eventsdiskpersistdiskpersistgo308) `:308`

- 🔗 [forEachShardWithUserEvents](#foreachshardwithuserevents-eventsdiskpersistdiskpersistgo802) `:802`

- 🔗 [garbageCollect](#garbagecollect-eventsdiskpersistdiskpersistgo389) `:389`

- 🔗 [garbageCollectRoutine](#garbagecollectroutine-eventsdiskpersistdiskpersistgo350) `:350`

- 🔗 [initLogFile](#initlogfile-eventsdiskpersistdiskpersistgo186) `:186`

- 🔗 [mutateUserEventsInLog](#mutateusereventsinlog-eventsdiskpersistdiskpersistgo849) `:849`

- 🔗 [postDoNotEmit](#postdonotemit-eventsdiskpersistdiskpersistgo676) `:676`

- 🔗 [readEventsFrom](#readeventsfrom-eventsdiskpersistdiskpersistgo684) `:684`

- 🔗 [readHeader](#readheader-eventsdiskpersistdiskpersistgo571) `:571`

- 🔗 [refMaybeHasUserEvents](#refmaybehasuserevents-eventsdiskpersistdiskpersistgo831) `:831`

- 🔗 [resumeLog](#resumelog-eventsdiskpersistdiskpersistgo158) `:158`

- 🔗 [scanForLastSeq](#scanforlastseq-eventsdiskpersistdiskpersistgo235) `:235`

- 🔗 [swapLog](#swaplog-eventsdiskpersistdiskpersistgo211) `:211`

- 🔗 [uidForDid](#uidfordid-eventsdiskpersistdiskpersistgo616) `:616`

- 🔗 [writeHeader](#writeheader-eventsdiskpersistdiskpersistgo597) `:597`


</details>


[function] name: DefaultDiskPersistOptions file: events/diskpersist/diskpersist.go:85 returns_error: нет description: —


### DefaultDiskPersistOptions (events/diskpersist/diskpersist.go:85)


DefaultDiskPersistOptions is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultDiskPersistOptions(()) ()
```


📍 *Расположение:* `events/diskpersist/diskpersist.go:85`



---


[function] name: Flush file: events/diskpersist/diskpersist.go:903 returns_error: нет description: —


### Flush (events/diskpersist/diskpersist.go:903)


Flush is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) Flush((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:903`



---


[function] name: Len64 file: events/diskpersist/diskpersist.go:565 returns_error: нет description: —


### Len64 (events/diskpersist/diskpersist.go:565)


Len64 is a method that performs operations based on the provided parameters and returns ().


```go
func (eh *evtHeader) Len64(()) ()
```


📍 *Расположение:* `events/diskpersist/diskpersist.go:565`



---


[function] name: NewDiskPersistence file: events/diskpersist/diskpersist.go:95 returns_error: да description: —


### NewDiskPersistence (events/diskpersist/diskpersist.go:95)


NewDiskPersistence is a function that performs operations based on the provided parameters and may return an error.


```go
func NewDiskPersistence((*DiskPersistence, error)) (*DiskPersistence, error)
```


**Тип запроса:** DiskPersistence


```json
{
  "primaryDir": "string",
  "archiveDir": "string",
  "eventsPerFile": 0,
  "writeBufferSize": 0,
  "retention": {},
  "meta": null,
  "broadcast": {},
  "logfi": null,
  "curSeq": 0,
  "uidCache": null,
  "didCache": null,
  "writers": null,
  "buffers": null,
  "scratch": [],
  "outbuf": null,
  "evtbuf": [],
  "shutdown": {},
  "lk": {}
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** DiskPersistence


```json
{
  "primaryDir": "string",
  "archiveDir": "string",
  "eventsPerFile": 0,
  "writeBufferSize": 0,
  "retention": {},
  "meta": null,
  "broadcast": {},
  "logfi": null,
  "curSeq": 0,
  "uidCache": null,
  "didCache": null,
  "writers": null,
  "buffers": null,
  "scratch": [],
  "outbuf": null,
  "evtbuf": [],
  "shutdown": {},
  "lk": {}
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DiskPersistence`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:95`



---


[function] name: Persist file: events/diskpersist/diskpersist.go:493 returns_error: нет description: —


### Persist (events/diskpersist/diskpersist.go:493)


Persist is a method that performs operations based on the provided parameters and returns (ctx context.Context, e *events.XRPCStreamEvent).


```go
func (dp *DiskPersistence) Persist((ctx context.Context, e *events.XRPCStreamEvent)) (ctx context.Context, e *events.XRPCStreamEvent)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:493`



---


[function] name: Playback file: events/diskpersist/diskpersist.go:631 returns_error: да description: —


### Playback (events/diskpersist/diskpersist.go:631)


Playback is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) Playback((ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)) (ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:631`



---


[function] name: PlaybackLogfiles file: events/diskpersist/diskpersist.go:658 returns_error: да description: —


### PlaybackLogfiles (events/diskpersist/diskpersist.go:658)


PlaybackLogfiles is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) PlaybackLogfiles((*int64, error)) (*int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:658`



---


[function] name: Read file: events/diskpersist/diskpersist.go:838 returns_error: да description: —


### Read (events/diskpersist/diskpersist.go:838)


Read is a method that performs operations based on the provided parameters and may return an error.


```go
func (zr *zeroReader) Read((n int, err error)) (n int, err error)
```


**Тип ответа:** n


```json
{
  "EnqueuedRepos": {},
  "FinishedRepos": {},
  "StatePath": "string",
  "CheckoutPath": "string",
  "outDir": "string",
  "magicHeaderKey": "string",
  "magicHeaderVal": "string",
  "logger": null,
  "lk": {},
  "wg": {},
  "exit": {},
  "limiter": null,
  "workerCount": 0,
  "client": null
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `n int`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:838`



---


[function] name: SetEventBroadcaster file: events/diskpersist/diskpersist.go:922 returns_error: нет description: —


### SetEventBroadcaster (events/diskpersist/diskpersist.go:922)


SetEventBroadcaster is a method that updates data based on the provided parameters and returns (f func(*events.XRPCStreamEvent)).


```go
func (dp *DiskPersistence) SetEventBroadcaster((f func(*events.XRPCStreamEvent))) (f func(*events.XRPCStreamEvent))
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


**Тип ответа:** f


```json
{
  "Logger": null,
  "PLCHost": "string",
  "PLCRateLimit": 0,
  "RedisURL": "string",
  "Bind": "string",
  "DisableRefresh": false
}
```


*Определено в:* `cmd/bluepages/server.go`


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


📍 *Расположение:* `events/diskpersist/diskpersist.go:922`



---


[function] name: Shutdown file: events/diskpersist/diskpersist.go:912 returns_error: нет description: —


### Shutdown (events/diskpersist/diskpersist.go:912)


Shutdown is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) Shutdown((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:912`



---


[function] name: TakeDownRepo file: events/diskpersist/diskpersist.go:783 returns_error: нет description: —


### TakeDownRepo (events/diskpersist/diskpersist.go:783)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, usr models.Uid).


```go
func (dp *DiskPersistence) TakeDownRepo((ctx context.Context, usr models.Uid)) (ctx context.Context, usr models.Uid)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:783`



---


[function] name: addJobToQueue file: events/diskpersist/diskpersist.go:290 returns_error: нет description: —


### addJobToQueue (events/diskpersist/diskpersist.go:290)


addJobToQueue is a method that performs operations based on the provided parameters and returns (ctx context.Context, job persistJob).


```go
func (dp *DiskPersistence) addJobToQueue((ctx context.Context, job persistJob)) (ctx context.Context, job persistJob)
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


**Тип ответа:** job


```json
{
  "repo": "string",
  "state": "string",
  "rev": "string",
  "lk": {},
  "bufferedOps": [],
  "dbj": null,
  "db": null,
  "createdAt": {},
  "updatedAt": {},
  "retryCount": 0,
  "retryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** persistJob


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


📍 *Расположение:* `events/diskpersist/diskpersist.go:290`



---


[function] name: deleteEventsForUser file: events/diskpersist/diskpersist.go:845 returns_error: нет description: —


### deleteEventsForUser (events/diskpersist/diskpersist.go:845)


deleteEventsForUser is a method that performs operations based on the provided parameters and returns (ctx context.Context, usr models.Uid, fn string).


```go
func (dp *DiskPersistence) deleteEventsForUser((ctx context.Context, usr models.Uid, fn string)) (ctx context.Context, usr models.Uid, fn string)
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


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/diskpersist/diskpersist.go:845`



---


[function] name: doPersist file: events/diskpersist/diskpersist.go:447 returns_error: нет description: —


### doPersist (events/diskpersist/diskpersist.go:447)


doPersist is a method that performs operations based on the provided parameters and returns (ctx context.Context, j persistJob).


```go
func (dp *DiskPersistence) doPersist((ctx context.Context, j persistJob)) (ctx context.Context, j persistJob)
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


**Тип ответа:** j


```json
{
  "Link": "string"
}
```


*Определено в:* `atproto/atdata/cidlink.go`


**Тип ответа:** persistJob


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


📍 *Расположение:* `events/diskpersist/diskpersist.go:447`



---


[function] name: flushLog file: events/diskpersist/diskpersist.go:327 returns_error: нет description: —


### flushLog (events/diskpersist/diskpersist.go:327)


flushLog is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) flushLog((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:327`



---


[function] name: flushRoutine file: events/diskpersist/diskpersist.go:308 returns_error: нет description: —


### flushRoutine (events/diskpersist/diskpersist.go:308)


flushRoutine is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) flushRoutine(()) ()
```


📍 *Расположение:* `events/diskpersist/diskpersist.go:308`



---


[function] name: forEachShardWithUserEvents file: events/diskpersist/diskpersist.go:802 returns_error: да description: —


### forEachShardWithUserEvents (events/diskpersist/diskpersist.go:802)


forEachShardWithUserEvents is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) forEachShardWithUserEvents((ctx context.Context, usr models.Uid, cb func(context.Context, string) error)) (ctx context.Context, usr models.Uid, cb func(context.Context, string) error)
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


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `usr models.Uid`, `cb func(context.Context`, `string) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:802`



---


[function] name: garbageCollect file: events/diskpersist/diskpersist.go:389 returns_error: нет description: —


### garbageCollect (events/diskpersist/diskpersist.go:389)


garbageCollect is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) garbageCollect((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:389`



---


[function] name: garbageCollectRoutine file: events/diskpersist/diskpersist.go:350 returns_error: нет description: —


### garbageCollectRoutine (events/diskpersist/diskpersist.go:350)


garbageCollectRoutine is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) garbageCollectRoutine(()) ()
```


📍 *Расположение:* `events/diskpersist/diskpersist.go:350`



---


[function] name: initLogFile file: events/diskpersist/diskpersist.go:186 returns_error: нет description: —


### initLogFile (events/diskpersist/diskpersist.go:186)


initLogFile is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) initLogFile(()) ()
```


📍 *Расположение:* `events/diskpersist/diskpersist.go:186`



---


[function] name: mutateUserEventsInLog file: events/diskpersist/diskpersist.go:849 returns_error: нет description: —


### mutateUserEventsInLog (events/diskpersist/diskpersist.go:849)


mutateUserEventsInLog is a method that performs operations based on the provided parameters and returns (ctx context.Context, usr models.Uid, fn string, flag uint32, zeroEvts bool).


```go
func (dp *DiskPersistence) mutateUserEventsInLog((ctx context.Context, usr models.Uid, fn string, flag uint32, zeroEvts bool)) (ctx context.Context, usr models.Uid, fn string, flag uint32, zeroEvts bool)
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


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** zeroEvts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/diskpersist/diskpersist.go:849`



---


[function] name: postDoNotEmit file: events/diskpersist/diskpersist.go:676 returns_error: нет description: —


### postDoNotEmit (events/diskpersist/diskpersist.go:676)


postDoNotEmit is a function that performs operations based on the provided parameters and returns (flags uint32).


```go
func postDoNotEmit((flags uint32)) (flags uint32)
```


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/diskpersist/diskpersist.go:676`



---


[function] name: readEventsFrom file: events/diskpersist/diskpersist.go:684 returns_error: да description: —


### readEventsFrom (events/diskpersist/diskpersist.go:684)


readEventsFrom is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) readEventsFrom((*int64, error)) (*int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:684`



---


[function] name: readHeader file: events/diskpersist/diskpersist.go:571 returns_error: да description: —


### readHeader (events/diskpersist/diskpersist.go:571)


readHeader is a function that performs operations based on the provided parameters and may return an error.


```go
func readHeader((*evtHeader, error)) (*evtHeader, error)
```


**Тип запроса:** evtHeader


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


**Тип ответа:** evtHeader


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*evtHeader`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:571`



---


[function] name: refMaybeHasUserEvents file: events/diskpersist/diskpersist.go:831 returns_error: да description: —


### refMaybeHasUserEvents (events/diskpersist/diskpersist.go:831)


refMaybeHasUserEvents is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) refMaybeHasUserEvents((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:831`



---


[function] name: resumeLog file: events/diskpersist/diskpersist.go:158 returns_error: нет description: —


### resumeLog (events/diskpersist/diskpersist.go:158)


resumeLog is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) resumeLog(()) ()
```


📍 *Расположение:* `events/diskpersist/diskpersist.go:158`



---


[function] name: scanForLastSeq file: events/diskpersist/diskpersist.go:235 returns_error: да description: —


### scanForLastSeq (events/diskpersist/diskpersist.go:235)


scanForLastSeq is a function that performs operations based on the provided parameters and may return an error.


```go
func scanForLastSeq((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:235`



---


[function] name: swapLog file: events/diskpersist/diskpersist.go:211 returns_error: нет description: swapLog swaps the current log file out for a new empty one
must only be called while holding dp.lk


### swapLog (events/diskpersist/diskpersist.go:211)


swapLog swaps the current log file out for a new empty one
must only be called while holding dp.lk


```go
func (dp *DiskPersistence) swapLog((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/diskpersist/diskpersist.go:211`



---


[function] name: uidForDid file: events/diskpersist/diskpersist.go:616 returns_error: да description: —


### uidForDid (events/diskpersist/diskpersist.go:616)


uidForDid is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) uidForDid((models.Uid, error)) (models.Uid, error)
```


**Тип ответа:** models.Uid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `models.Uid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/diskpersist/diskpersist.go:616`



---


[function] name: writeHeader file: events/diskpersist/diskpersist.go:597 returns_error: нет description: —


### writeHeader (events/diskpersist/diskpersist.go:597)


writeHeader is a method that performs operations based on the provided parameters and returns (ctx context.Context, flags uint32, kind uint32, l uint32, usr uint64, seq int64).


```go
func (dp *DiskPersistence) writeHeader((ctx context.Context, flags uint32, kind uint32, l uint32, usr uint64, seq int64)) (ctx context.Context, flags uint32, kind uint32, l uint32, usr uint64, seq int64)
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


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** l


```json
{
  "Inner": {},
  "ErrTTL": {},
  "HitTTL": {},
  "InvalidHandleTTL": {},
  "Logger": null,
  "handleCache": null,
  "didCache": null,
  "didResolveChans": {},
  "handleResolveChans": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** usr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/diskpersist/diskpersist.go:597`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_dbpersist.md)

- [Следующая директория](events_pebblepersist.md)


---

