---
title: "Функции: events"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: events
---


# Функции: events


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_tap.md)

- [Следующая директория](events_dbpersist.md)


---


## Меню по файлам


- 📄 [events/cbor_gen.go](#eventscbor_gengo)

- 📄 [events/consumer.go](#eventsconsumergo)

- 📄 [events/events.go](#eventseventsgo)

- 📄 [events/persist.go](#eventspersistgo)


---


## events/cbor_gen.go


📄 Исходный файл: `events/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-eventscbor_gengo21) `:21`

- 🔗 [MarshalCBOR](#marshalcbor-eventscbor_gengo178) `:178`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-eventscbor_gengo89) `:89`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-eventscbor_gengo238) `:238`


</details>


[function] name: MarshalCBOR file: events/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (events/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EventHeader) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/cbor_gen.go:21`



---


[function] name: MarshalCBOR file: events/cbor_gen.go:178 returns_error: нет description: —


### MarshalCBOR (events/cbor_gen.go:178)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *ErrorFrame) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/cbor_gen.go:178`



---


[function] name: UnmarshalCBOR file: events/cbor_gen.go:89 returns_error: да description: —


### UnmarshalCBOR (events/cbor_gen.go:89)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EventHeader) UnmarshalCBOR((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `events/cbor_gen.go:89`



---


[function] name: UnmarshalCBOR file: events/cbor_gen.go:238 returns_error: да description: —


### UnmarshalCBOR (events/cbor_gen.go:238)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ErrorFrame) UnmarshalCBOR((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `events/cbor_gen.go:238`




## events/consumer.go


📄 Исходный файл: `events/consumer.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [EventHandler](#eventhandler-eventsconsumergo31) `:31`

- 🔗 [EventHandler](#eventhandler-eventsconsumergo86) `:86`

- 🔗 [HandleRepoStream](#handlerepostream-eventsconsumergo112) `:112`

- 🔗 [NewInstrumentedRepoStreamCallbacks](#newinstrumentedrepostreamcallbacks-eventsconsumergo59) `:59`

- 🔗 [Read](#read-eventsconsumergo102) `:102`

- 🔗 [waitForLimiter](#waitforlimiter-eventsconsumergo66) `:66`


</details>


[function] name: EventHandler file: events/consumer.go:31 returns_error: нет description: —


### EventHandler (events/consumer.go:31)


EventHandler is a method that performs operations based on the provided parameters and returns (ctx context.Context, xev *XRPCStreamEvent).


```go
func (rsc *RepoStreamCallbacks) EventHandler((ctx context.Context, xev *XRPCStreamEvent)) (ctx context.Context, xev *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** xev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/consumer.go:31`



---


[function] name: EventHandler file: events/consumer.go:86 returns_error: нет description: —


### EventHandler (events/consumer.go:86)


EventHandler is a method that performs operations based on the provided parameters and returns (ctx context.Context, xev *XRPCStreamEvent).


```go
func (rsc *InstrumentedRepoStreamCallbacks) EventHandler((ctx context.Context, xev *XRPCStreamEvent)) (ctx context.Context, xev *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** xev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/consumer.go:86`



---


[function] name: HandleRepoStream file: events/consumer.go:112 returns_error: нет description: HandleRepoStream
con is source of events
sched gets AddWork for each event
log may be nil for default logger


### HandleRepoStream (events/consumer.go:112)


HandleRepoStream
con is source of events
sched gets AddWork for each event
log may be nil for default logger


```go
func HandleRepoStream((ctx context.Context, con *websocket.Conn, sched Scheduler, log *slog.Logger)) (ctx context.Context, con *websocket.Conn, sched Scheduler, log *slog.Logger)
```


**Тип запроса:** websocket.Conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** con


```json
{
  "repo": "string",
  "val": null,
  "signal": "string",
  "wg": null
}
```


*Определено в:* `events/schedulers/autoscaling/autoscaling.go`


**Тип ответа:** websocket.Conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sched


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Scheduler


```json
{
  "concurrency": 0,
  "maxConcurrency": 0,
  "do": {},
  "feeder": {},
  "workerGroup": {},
  "lk": {},
  "active": {},
  "maxActive": 0,
  "ident": "string",
  "itemsAdded": {},
  "itemsProcessed": {},
  "itemsActive": {},
  "workersActive": {},
  "throughputManager": null,
  "autoscaleFrequency": {},
  "autoscalerIn": {},
  "autoscalerOut": {},
  "log": null
}
```


*Определено в:* `events/schedulers/autoscaling/autoscaling.go`


**Тип ответа:** log


```json
{
  "inner": null
}
```


*Определено в:* `util/http.go`


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/consumer.go:112`



---


[function] name: NewInstrumentedRepoStreamCallbacks file: events/consumer.go:59 returns_error: да description: —


### NewInstrumentedRepoStreamCallbacks (events/consumer.go:59)


NewInstrumentedRepoStreamCallbacks is a function that performs operations based on the provided parameters and may return an error.


```go
func NewInstrumentedRepoStreamCallbacks((limiters []*slidingwindow.Limiter, next func(ctx context.Context, xev *XRPCStreamEvent) error)) (limiters []*slidingwindow.Limiter, next func(ctx context.Context, xev *XRPCStreamEvent) error)
```


**Тип запроса:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** limiters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** xev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** XRPCStreamEvent


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


*Типы возврата:* `limiters []*slidingwindow.Limiter`, `next func(ctx context.Context`, `xev *XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/consumer.go:59`



---


[function] name: Read file: events/consumer.go:102 returns_error: да description: —


### Read (events/consumer.go:102)


Read is a method that performs operations based on the provided parameters and may return an error.


```go
func (sr *instrumentedReader) Read((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/consumer.go:102`



---


[function] name: waitForLimiter file: events/consumer.go:66 returns_error: нет description: —


### waitForLimiter (events/consumer.go:66)


waitForLimiter is a function that performs operations based on the provided parameters and returns (ctx context.Context, lim *slidingwindow.Limiter).


```go
func waitForLimiter((ctx context.Context, lim *slidingwindow.Limiter)) (ctx context.Context, lim *slidingwindow.Limiter)
```


**Тип запроса:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


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


**Тип ответа:** lim


```json
{
  "Limit": 0,
  "Remaining": 0,
  "Policy": "string",
  "Reset": {}
}
```


*Определено в:* `xrpc/xrpc.go`


**Тип ответа:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


📍 *Расположение:* `events/consumer.go:66`




## events/events.go


📄 Исходный файл: `events/events.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [AddEvent](#addevent-eventseventsgo325) `:325`

- 🔗 [Deserialize](#deserialize-eventseventsgo246) `:246`

- 🔗 [GetSequence](#getsequence-eventseventsgo465) `:465`

- 🔗 [NewEventManager](#neweventmanager-eventseventsgo41) `:41`

- 🔗 [Preserialize](#preserialize-eventseventsgo307) `:307`

- 🔗 [Sequence](#sequence-eventseventsgo444) `:444`

- 🔗 [SequenceForEvent](#sequenceforevent-eventseventsgo440) `:440`

- 🔗 [Serialize](#serialize-eventseventsgo212) `:212`

- 🔗 [Shutdown](#shutdown-eventseventsgo66) `:66`

- 🔗 [Subscribe](#subscribe-eventseventsgo338) `:338`

- 🔗 [TakeDownRepo](#takedownrepo-eventseventsgo506) `:506`

- 🔗 [addSubscriber](#addsubscriber-eventseventsgo499) `:499`

- 🔗 [broadcastEvent](#broadcastevent-eventseventsgo70) `:70`

- 🔗 [init](#init-eventseventsgo188) `:188`

- 🔗 [persistAndSendEvent](#persistandsendevent-eventseventsgo128) `:128`

- 🔗 [rmSubscriber](#rmsubscriber-eventseventsgo486) `:486`


</details>


[function] name: AddEvent file: events/events.go:325 returns_error: нет description: —


### AddEvent (events/events.go:325)


AddEvent is a method that creates new data based on the provided parameters and returns (ctx context.Context, ev *XRPCStreamEvent).


```go
func (em *EventManager) AddEvent((ctx context.Context, ev *XRPCStreamEvent)) (ctx context.Context, ev *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** ev


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


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/events.go:325`



---


[function] name: Deserialize file: events/events.go:246 returns_error: нет description: —


### Deserialize (events/events.go:246)


Deserialize is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (xevt *XRPCStreamEvent) Deserialize((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `events/events.go:246`



---


[function] name: GetSequence file: events/events.go:465 returns_error: нет description: —


### GetSequence (events/events.go:465)


GetSequence is a method that retrieves data based on the provided parameters and returns (int64, bool).


```go
func (evt *XRPCStreamEvent) GetSequence((int64, bool)) (int64, bool)
```


📍 *Расположение:* `events/events.go:465`



---


[function] name: NewEventManager file: events/events.go:41 returns_error: нет description: —


### NewEventManager (events/events.go:41)


NewEventManager is a function that performs operations based on the provided parameters and returns (persister EventPersistence).


```go
func NewEventManager((persister EventPersistence)) (persister EventPersistence)
```


**Тип ответа:** persister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** EventPersistence


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/events.go:41`



---


[function] name: Preserialize file: events/events.go:307 returns_error: нет description: serialize content into Preserialized cache


### Preserialize (events/events.go:307)


serialize content into Preserialized cache


```go
func (evt *XRPCStreamEvent) Preserialize(()) ()
```


📍 *Расположение:* `events/events.go:307`



---


[function] name: Sequence file: events/events.go:444 returns_error: нет description: —


### Sequence (events/events.go:444)


Sequence is a method that performs operations based on the provided parameters and returns ().


```go
func (evt *XRPCStreamEvent) Sequence(()) ()
```


📍 *Расположение:* `events/events.go:444`



---


[function] name: SequenceForEvent file: events/events.go:440 returns_error: нет description: —


### SequenceForEvent (events/events.go:440)


SequenceForEvent is a function that performs operations based on the provided parameters and returns (evt *XRPCStreamEvent).


```go
func SequenceForEvent((evt *XRPCStreamEvent)) (evt *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/events.go:440`



---


[function] name: Serialize file: events/events.go:212 returns_error: нет description: —


### Serialize (events/events.go:212)


Serialize is a method that performs operations based on the provided parameters and returns (wc io.Writer).


```go
func (evt *XRPCStreamEvent) Serialize((wc io.Writer)) (wc io.Writer)
```


**Тип ответа:** wc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/events.go:212`



---


[function] name: Shutdown file: events/events.go:66 returns_error: нет description: —


### Shutdown (events/events.go:66)


Shutdown is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (em *EventManager) Shutdown((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/events.go:66`



---


[function] name: Subscribe file: events/events.go:338 returns_error: да description: —


### Subscribe (events/events.go:338)


Subscribe is a method that performs operations based on the provided parameters and may return an error.


```go
func (em *EventManager) Subscribe((<-chan *XRPCStreamEvent, func(), error)) (<-chan *XRPCStreamEvent, func(), error)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** XRPCStreamEvent


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


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `<-chan *XRPCStreamEvent`, `func()`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/events.go:338`



---


[function] name: TakeDownRepo file: events/events.go:506 returns_error: нет description: —


### TakeDownRepo (events/events.go:506)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid).


```go
func (em *EventManager) TakeDownRepo((ctx context.Context, user models.Uid)) (ctx context.Context, user models.Uid)
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


**Тип ответа:** user


```json
{
  "CreatedAt": {},
  "Did": "string",
  "Handle": "string",
  "InvitedBy": "string",
  "InvitedByHandle": "string",
  "TotalInvites": 0,
  "Invited": [],
  "Email": "string"
}
```


*Определено в:* `cmd/gosky/admin.go`


**Тип ответа:** models.Uid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/events.go:506`



---


[function] name: addSubscriber file: events/events.go:499 returns_error: нет description: —


### addSubscriber (events/events.go:499)


addSubscriber is a method that performs operations based on the provided parameters and returns (sub *Subscriber).


```go
func (em *EventManager) addSubscriber((sub *Subscriber)) (sub *Subscriber)
```


**Тип запроса:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


**Тип ответа:** sub


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `events/events.go:499`



---


[function] name: broadcastEvent file: events/events.go:70 returns_error: нет description: —


### broadcastEvent (events/events.go:70)


broadcastEvent is a method that performs operations based on the provided parameters and returns (evt *XRPCStreamEvent).


```go
func (em *EventManager) broadcastEvent((evt *XRPCStreamEvent)) (evt *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/events.go:70`



---


[function] name: init file: events/events.go:188 returns_error: нет description: —


### init (events/events.go:188)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `events/events.go:188`



---


[function] name: persistAndSendEvent file: events/events.go:128 returns_error: нет description: —


### persistAndSendEvent (events/events.go:128)


persistAndSendEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *XRPCStreamEvent).


```go
func (em *EventManager) persistAndSendEvent((ctx context.Context, evt *XRPCStreamEvent)) (ctx context.Context, evt *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/events.go:128`



---


[function] name: rmSubscriber file: events/events.go:486 returns_error: нет description: —


### rmSubscriber (events/events.go:486)


rmSubscriber is a method that performs operations based on the provided parameters and returns (sub *Subscriber).


```go
func (em *EventManager) rmSubscriber((sub *Subscriber)) (sub *Subscriber)
```


**Тип запроса:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


**Тип ответа:** sub


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `events/events.go:486`




## events/persist.go


📄 Исходный файл: `events/persist.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Flush](#flush-eventspersistgo86) `:86`

- 🔗 [NewMemPersister](#newmempersister-eventspersistgo34) `:34`

- 🔗 [Persist](#persist-eventspersistgo38) `:38`

- 🔗 [Playback](#playback-eventspersistgo63) `:63`

- 🔗 [SetEventBroadcaster](#seteventbroadcaster-eventspersistgo90) `:90`

- 🔗 [Shutdown](#shutdown-eventspersistgo94) `:94`

- 🔗 [TakeDownRepo](#takedownrepo-eventspersistgo82) `:82`


</details>


[function] name: Flush file: events/persist.go:86 returns_error: нет description: —


### Flush (events/persist.go:86)


Flush is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (mp *MemPersister) Flush((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `events/persist.go:86`



---


[function] name: NewMemPersister file: events/persist.go:34 returns_error: нет description: —


### NewMemPersister (events/persist.go:34)


NewMemPersister is a function that performs operations based on the provided parameters and returns ().


```go
func NewMemPersister(()) ()
```


📍 *Расположение:* `events/persist.go:34`



---


[function] name: Persist file: events/persist.go:38 returns_error: нет description: —


### Persist (events/persist.go:38)


Persist is a method that performs operations based on the provided parameters and returns (ctx context.Context, e *XRPCStreamEvent).


```go
func (mp *MemPersister) Persist((ctx context.Context, e *XRPCStreamEvent)) (ctx context.Context, e *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/persist.go:38`



---


[function] name: Playback file: events/persist.go:63 returns_error: да description: —


### Playback (events/persist.go:63)


Playback is a method that performs operations based on the provided parameters and may return an error.


```go
func (mp *MemPersister) Playback((ctx context.Context, since int64, cb func(*XRPCStreamEvent) error)) (ctx context.Context, since int64, cb func(*XRPCStreamEvent) error)
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** XRPCStreamEvent


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


*Типы возврата:* `ctx context.Context`, `since int64`, `cb func(*XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/persist.go:63`



---


[function] name: SetEventBroadcaster file: events/persist.go:90 returns_error: нет description: —


### SetEventBroadcaster (events/persist.go:90)


SetEventBroadcaster is a method that updates data based on the provided parameters and returns (brc func(*XRPCStreamEvent)).


```go
func (mp *MemPersister) SetEventBroadcaster((brc func(*XRPCStreamEvent))) (brc func(*XRPCStreamEvent))
```


**Тип запроса:** XRPCStreamEvent


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


**Тип ответа:** XRPCStreamEvent


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


📍 *Расположение:* `events/persist.go:90`



---


[function] name: Shutdown file: events/persist.go:94 returns_error: нет description: —


### Shutdown (events/persist.go:94)


Shutdown is a method that performs operations based on the provided parameters and returns (context.Context).


```go
func (mp *MemPersister) Shutdown((context.Context)) (context.Context)
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


📍 *Расположение:* `events/persist.go:94`



---


[function] name: TakeDownRepo file: events/persist.go:82 returns_error: нет description: —


### TakeDownRepo (events/persist.go:82)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid models.Uid).


```go
func (mp *MemPersister) TakeDownRepo((ctx context.Context, uid models.Uid)) (ctx context.Context, uid models.Uid)
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


📍 *Расположение:* `events/persist.go:82`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_tap.md)

- [Следующая директория](events_dbpersist.md)


---

