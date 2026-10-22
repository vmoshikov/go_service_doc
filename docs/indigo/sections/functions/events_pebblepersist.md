---
title: "Функции: events/pebblepersist"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: events/pebblepersist
---


# Функции: events/pebblepersist


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_diskpersist.md)

- [Следующая директория](events_schedulers.md)


---


## Меню по файлам


- 📄 [events/pebblepersist/pebblepersist.go](#eventspebblepersistpebblepersistgo)


---


## events/pebblepersist/pebblepersist.go


📄 Исходный файл: `events/pebblepersist/pebblepersist.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [Flush](#flush-eventspebblepersistpebblepersistgo151) `:151`

- 🔗 [GCThread](#gcthread-eventspebblepersistpebblepersistgo190) `:190`

- 🔗 [GarbageCollect](#garbagecollect-eventspebblepersistpebblepersistgo218) `:218`

- 🔗 [GetLast](#getlast-eventspebblepersistpebblepersistgo169) `:169`

- 🔗 [NewPebblePersistance](#newpebblepersistance-eventspebblepersistpebblepersistgo54) `:54`

- 🔗 [Persist](#persist-eventspebblepersistpebblepersistgo73) `:73`

- 🔗 [Playback](#playback-eventspebblepersistpebblepersistgo123) `:123`

- 🔗 [SetEventBroadcaster](#seteventbroadcaster-eventspebblepersistpebblepersistgo163) `:163`

- 🔗 [Shutdown](#shutdown-eventspebblepersistpebblepersistgo154) `:154`

- 🔗 [TakeDownRepo](#takedownrepo-eventspebblepersistpebblepersistgo147) `:147`

- 🔗 [eventFromPebbleIter](#eventfrompebbleiter-eventspebblepersistpebblepersistgo108) `:108`

- 🔗 [init](#init-eventspebblepersistpebblepersistgo211) `:211`

- 🔗 [setKeySeqMillis](#setkeyseqmillis-eventspebblepersistpebblepersistgo68) `:68`


</details>


[function] name: Flush file: events/pebblepersist/pebblepersist.go:151 returns_error: нет description: —


### Flush (events/pebblepersist/pebblepersist.go:151)


Flush is a method that performs operations based on the provided parameters and returns (context.Context).


```go
func (pp *PebblePersist) Flush((context.Context)) (context.Context)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:151`



---


[function] name: GCThread file: events/pebblepersist/pebblepersist.go:190 returns_error: нет description: example;
```
pp := NewPebblePersistance("/tmp/foo.pebble")
go pp.GCThread(context.Background(), 48 * time.Hour, 5 * time


### GCThread (events/pebblepersist/pebblepersist.go:190)


example;
```
pp := NewPebblePersistance("/tmp/foo.pebble")
go pp.GCThread(context.Background(), 48 * time.Hour, 5 * time.Minute)
```


```go
func (pp *PebblePersist) GCThread((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:190`



---


[function] name: GarbageCollect file: events/pebblepersist/pebblepersist.go:218 returns_error: нет description: —


### GarbageCollect (events/pebblepersist/pebblepersist.go:218)


GarbageCollect is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (pp *PebblePersist) GarbageCollect((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:218`



---


[function] name: GetLast file: events/pebblepersist/pebblepersist.go:169 returns_error: да description: —


### GetLast (events/pebblepersist/pebblepersist.go:169)


GetLast is a method that retrieves data based on the provided parameters and may return an error.


```go
func (pp *PebblePersist) GetLast((seq, millis int64, evt *events.XRPCStreamEvent, err error)) (seq, millis int64, evt *events.XRPCStreamEvent, err error)
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


**Тип ответа:** seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** millis


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `seq`, `millis int64`, `evt *events.XRPCStreamEvent`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:169`



---


[function] name: NewPebblePersistance file: events/pebblepersist/pebblepersist.go:54 returns_error: да description: Create a new EventPersistence which stores data in pebbledb
nil opts is ok


### NewPebblePersistance (events/pebblepersist/pebblepersist.go:54)


Create a new EventPersistence which stores data in pebbledb
nil opts is ok


```go
func NewPebblePersistance((*PebblePersist, error)) (*PebblePersist, error)
```


**Тип запроса:** PebblePersist


```json
{
  "broadcast": {},
  "db": null,
  "prevSeq": 0,
  "prevSeqExtra": 0,
  "cancel": {},
  "options": {}
}
```


*Определено в:* `events/pebblepersist/pebblepersist.go`


**Тип ответа:** PebblePersist


```json
{
  "broadcast": {},
  "db": null,
  "prevSeq": 0,
  "prevSeqExtra": 0,
  "cancel": {},
  "options": {}
}
```


*Определено в:* `events/pebblepersist/pebblepersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PebblePersist`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:54`



---


[function] name: Persist file: events/pebblepersist/pebblepersist.go:73 returns_error: нет description: —


### Persist (events/pebblepersist/pebblepersist.go:73)


Persist is a method that performs operations based on the provided parameters and returns (ctx context.Context, e *events.XRPCStreamEvent).


```go
func (pp *PebblePersist) Persist((ctx context.Context, e *events.XRPCStreamEvent)) (ctx context.Context, e *events.XRPCStreamEvent)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:73`



---


[function] name: Playback file: events/pebblepersist/pebblepersist.go:123 returns_error: да description: —


### Playback (events/pebblepersist/pebblepersist.go:123)


Playback is a method that performs operations based on the provided parameters and may return an error.


```go
func (pp *PebblePersist) Playback((ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)) (ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:123`



---


[function] name: SetEventBroadcaster file: events/pebblepersist/pebblepersist.go:163 returns_error: нет description: —


### SetEventBroadcaster (events/pebblepersist/pebblepersist.go:163)


SetEventBroadcaster is a method that updates data based on the provided parameters and returns (broadcast func(*events.XRPCStreamEvent)).


```go
func (pp *PebblePersist) SetEventBroadcaster((broadcast func(*events.XRPCStreamEvent))) (broadcast func(*events.XRPCStreamEvent))
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


**Тип ответа:** broadcast


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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:163`



---


[function] name: Shutdown file: events/pebblepersist/pebblepersist.go:154 returns_error: нет description: —


### Shutdown (events/pebblepersist/pebblepersist.go:154)


Shutdown is a method that performs operations based on the provided parameters and returns (context.Context).


```go
func (pp *PebblePersist) Shutdown((context.Context)) (context.Context)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:154`



---


[function] name: TakeDownRepo file: events/pebblepersist/pebblepersist.go:147 returns_error: нет description: —


### TakeDownRepo (events/pebblepersist/pebblepersist.go:147)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, usr models.Uid).


```go
func (pp *PebblePersist) TakeDownRepo((ctx context.Context, usr models.Uid)) (ctx context.Context, usr models.Uid)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:147`



---


[function] name: eventFromPebbleIter file: events/pebblepersist/pebblepersist.go:108 returns_error: да description: —


### eventFromPebbleIter (events/pebblepersist/pebblepersist.go:108)


eventFromPebbleIter is a function that performs operations based on the provided parameters and may return an error.


```go
func eventFromPebbleIter((*events.XRPCStreamEvent, error)) (*events.XRPCStreamEvent, error)
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


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:108`



---


[function] name: init file: events/pebblepersist/pebblepersist.go:211 returns_error: нет description: —


### init (events/pebblepersist/pebblepersist.go:211)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:211`



---


[function] name: setKeySeqMillis file: events/pebblepersist/pebblepersist.go:68 returns_error: нет description: —


### setKeySeqMillis (events/pebblepersist/pebblepersist.go:68)


setKeySeqMillis is a function that performs operations based on the provided parameters and returns (key []byte, seq, millis int64).


```go
func setKeySeqMillis((key []byte, seq, millis int64)) (key []byte, seq, millis int64)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** millis


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/pebblepersist/pebblepersist.go:68`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_diskpersist.md)

- [Следующая директория](events_schedulers.md)


---

