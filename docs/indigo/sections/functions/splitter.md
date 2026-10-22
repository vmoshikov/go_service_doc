---
title: "Функции: splitter"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: splitter
---


# Функции: splitter


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](search.md)

- [Следующая директория](testing.md)


---


## Меню по файлам


- 📄 [splitter/firehose.go](#splitterfirehosego)

- 📄 [splitter/handlers.go](#splitterhandlersgo)

- 📄 [splitter/ringbuf.go](#splitterringbufgo)

- 📄 [splitter/splitter.go](#splittersplittergo)


---


## splitter/firehose.go


📄 Исходный файл: `splitter/firehose.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [HandleSubscribeRepos](#handlesubscriberepos-splitterfirehosego19) `:19`

- 🔗 [cleanupConsumer](#cleanupconsumer-splitterfirehosego182) `:182`

- 🔗 [registerConsumer](#registerconsumer-splitterfirehosego170) `:170`


</details>


[function] name: HandleSubscribeRepos file: splitter/firehose.go:19 returns_error: нет description: —


### HandleSubscribeRepos (splitter/firehose.go:19)


HandleSubscribeRepos is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Splitter) HandleSubscribeRepos((c echo.Context)) (c echo.Context)
```


**Тип ответа:** c


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `splitter/firehose.go:19`



---


[function] name: cleanupConsumer file: splitter/firehose.go:182 returns_error: нет description: —


### cleanupConsumer (splitter/firehose.go:182)


cleanupConsumer is a method that performs operations based on the provided parameters and returns (id uint64).


```go
func (s *Splitter) cleanupConsumer((id uint64)) (id uint64)
```


**Тип ответа:** id


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `splitter/firehose.go:182`



---


[function] name: registerConsumer file: splitter/firehose.go:170 returns_error: нет description: —


### registerConsumer (splitter/firehose.go:170)


registerConsumer is a method that performs operations based on the provided parameters and returns (c *SocketConsumer).


```go
func (s *Splitter) registerConsumer((c *SocketConsumer)) (c *SocketConsumer)
```


**Тип запроса:** SocketConsumer


```json
{
  "UserAgent": "string",
  "RemoteAddr": "string",
  "ConnectedAt": {},
  "EventsSent": {}
}
```


*Определено в:* `splitter/firehose.go`


**Тип ответа:** c


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


**Тип ответа:** SocketConsumer


```json
{
  "UserAgent": "string",
  "RemoteAddr": "string",
  "ConnectedAt": {},
  "EventsSent": {}
}
```


*Определено в:* `splitter/firehose.go`


📍 *Расположение:* `splitter/firehose.go:170`




## splitter/handlers.go


📄 Исходный файл: `splitter/handlers.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [HandleComAtprotoSyncRequestCrawl](#handlecomatprotosyncrequestcrawl-splitterhandlersgo41) `:41`

- 🔗 [HandleHealthCheck](#handlehealthcheck-splitterhandlersgo22) `:22`

- 🔗 [HandleHomeMessage](#handlehomemessage-splitterhandlersgo37) `:37`

- 🔗 [ProxyRequest](#proxyrequest-splitterhandlersgo107) `:107`

- 🔗 [ProxyRequestCollectionDir](#proxyrequestcollectiondir-splitterhandlersgo99) `:99`

- 🔗 [ProxyRequestUpstream](#proxyrequestupstream-splitterhandlersgo90) `:90`


</details>


[function] name: HandleComAtprotoSyncRequestCrawl file: splitter/handlers.go:41 returns_error: нет description: —


### HandleComAtprotoSyncRequestCrawl (splitter/handlers.go:41)


HandleComAtprotoSyncRequestCrawl is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Splitter) HandleComAtprotoSyncRequestCrawl((c echo.Context)) (c echo.Context)
```


**Тип ответа:** c


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `splitter/handlers.go:41`



---


[function] name: HandleHealthCheck file: splitter/handlers.go:22 returns_error: нет description: —


### HandleHealthCheck (splitter/handlers.go:22)


HandleHealthCheck is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Splitter) HandleHealthCheck((c echo.Context)) (c echo.Context)
```


**Тип ответа:** c


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `splitter/handlers.go:22`



---


[function] name: HandleHomeMessage file: splitter/handlers.go:37 returns_error: нет description: —


### HandleHomeMessage (splitter/handlers.go:37)


HandleHomeMessage is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Splitter) HandleHomeMessage((c echo.Context)) (c echo.Context)
```


**Тип ответа:** c


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `splitter/handlers.go:37`



---


[function] name: ProxyRequest file: splitter/handlers.go:107 returns_error: нет description: —


### ProxyRequest (splitter/handlers.go:107)


ProxyRequest is a method that performs operations based on the provided parameters and returns (c echo.Context, hostname, scheme string).


```go
func (s *Splitter) ProxyRequest((c echo.Context, hostname, scheme string)) (c echo.Context, hostname, scheme string)
```


**Тип ответа:** c


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


**Тип ответа:** echo.Context


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


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scheme


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/handlers.go:107`



---


[function] name: ProxyRequestCollectionDir file: splitter/handlers.go:99 returns_error: нет description: Proxies a request to the collectiondir


### ProxyRequestCollectionDir (splitter/handlers.go:99)


Proxies a request to the collectiondir


```go
func (s *Splitter) ProxyRequestCollectionDir((c echo.Context)) (c echo.Context)
```


**Тип ответа:** c


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `splitter/handlers.go:99`



---


[function] name: ProxyRequestUpstream file: splitter/handlers.go:90 returns_error: нет description: Proxies a request to the single upstream (relay)


### ProxyRequestUpstream (splitter/handlers.go:90)


Proxies a request to the single upstream (relay)


```go
func (s *Splitter) ProxyRequestUpstream((c echo.Context)) (c echo.Context)
```


**Тип ответа:** c


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `splitter/handlers.go:90`




## splitter/ringbuf.go


📄 Исходный файл: `splitter/ringbuf.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Flush](#flush-splitterringbufgo67) `:67`

- 🔗 [NewEventRingBuffer](#neweventringbuffer-splitterringbufgo11) `:11`

- 🔗 [Persist](#persist-splitterringbufgo44) `:44`

- 🔗 [Playback](#playback-splitterringbufgo71) `:71`

- 🔗 [SetEventBroadcaster](#seteventbroadcaster-splitterringbufgo134) `:134`

- 🔗 [Shutdown](#shutdown-splitterringbufgo138) `:138`

- 🔗 [TakeDownRepo](#takedownrepo-splitterringbufgo142) `:142`

- 🔗 [append](#append-splitterringbufgo32) `:32`

- 🔗 [events](#events-splitterringbufgo38) `:38`

- 🔗 [playbackRound](#playbackround-splitterringbufgo89) `:89`


</details>


[function] name: Flush file: splitter/ringbuf.go:67 returns_error: нет description: —


### Flush (splitter/ringbuf.go:67)


Flush is a method that performs operations based on the provided parameters and returns (context.Context).


```go
func (er *EventRingBuffer) Flush((context.Context)) (context.Context)
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


📍 *Расположение:* `splitter/ringbuf.go:67`



---


[function] name: NewEventRingBuffer file: splitter/ringbuf.go:11 returns_error: нет description: —


### NewEventRingBuffer (splitter/ringbuf.go:11)


NewEventRingBuffer is a function that performs operations based on the provided parameters and returns (chunkSize, nchunks int).


```go
func NewEventRingBuffer((chunkSize, nchunks int)) (chunkSize, nchunks int)
```


**Тип ответа:** chunkSize


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nchunks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/ringbuf.go:11`



---


[function] name: Persist file: splitter/ringbuf.go:44 returns_error: нет description: —


### Persist (splitter/ringbuf.go:44)


Persist is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *events.XRPCStreamEvent).


```go
func (er *EventRingBuffer) Persist((ctx context.Context, evt *events.XRPCStreamEvent)) (ctx context.Context, evt *events.XRPCStreamEvent)
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


📍 *Расположение:* `splitter/ringbuf.go:44`



---


[function] name: Playback file: splitter/ringbuf.go:71 returns_error: да description: —


### Playback (splitter/ringbuf.go:71)


Playback is a method that performs operations based on the provided parameters and may return an error.


```go
func (er *EventRingBuffer) Playback((ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)) (ctx context.Context, since int64, cb func(*events.XRPCStreamEvent) error)
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


📍 *Расположение:* `splitter/ringbuf.go:71`



---


[function] name: SetEventBroadcaster file: splitter/ringbuf.go:134 returns_error: нет description: —


### SetEventBroadcaster (splitter/ringbuf.go:134)


SetEventBroadcaster is a method that updates data based on the provided parameters and returns (brc func(*events.XRPCStreamEvent)).


```go
func (er *EventRingBuffer) SetEventBroadcaster((brc func(*events.XRPCStreamEvent))) (brc func(*events.XRPCStreamEvent))
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


📍 *Расположение:* `splitter/ringbuf.go:134`



---


[function] name: Shutdown file: splitter/ringbuf.go:138 returns_error: нет description: —


### Shutdown (splitter/ringbuf.go:138)


Shutdown is a method that performs operations based on the provided parameters and returns (context.Context).


```go
func (er *EventRingBuffer) Shutdown((context.Context)) (context.Context)
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


📍 *Расположение:* `splitter/ringbuf.go:138`



---


[function] name: TakeDownRepo file: splitter/ringbuf.go:142 returns_error: нет description: —


### TakeDownRepo (splitter/ringbuf.go:142)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (context.Context, models.Uid).


```go
func (er *EventRingBuffer) TakeDownRepo((context.Context, models.Uid)) (context.Context, models.Uid)
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


**Тип ответа:** models.Uid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/ringbuf.go:142`



---


[function] name: append file: splitter/ringbuf.go:32 returns_error: нет description: —


### append (splitter/ringbuf.go:32)


append is a method that performs operations based on the provided parameters and returns (evt *events.XRPCStreamEvent).


```go
func (rc *ringChunk) append((evt *events.XRPCStreamEvent)) (evt *events.XRPCStreamEvent)
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


📍 *Расположение:* `splitter/ringbuf.go:32`



---


[function] name: events file: splitter/ringbuf.go:38 returns_error: нет description: —


### events (splitter/ringbuf.go:38)


events is a method that performs operations based on the provided parameters and returns ().


```go
func (rc *ringChunk) events(()) ()
```


📍 *Расположение:* `splitter/ringbuf.go:38`



---


[function] name: playbackRound file: splitter/ringbuf.go:89 returns_error: да description: —


### playbackRound (splitter/ringbuf.go:89)


playbackRound is a method that performs operations based on the provided parameters and may return an error.


```go
func (er *EventRingBuffer) playbackRound((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `splitter/ringbuf.go:89`




## splitter/splitter.go


📄 Исходный файл: `splitter/splitter.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [NewSplitter](#newsplitter-splittersplittergo101) `:101`

- 🔗 [Shutdown](#shutdown-splittersplittergo190) `:190`

- 🔗 [StartAPI](#startapi-splittersplittergo166) `:166`

- 🔗 [StartMetrics](#startmetrics-splittersplittergo185) `:185`

- 🔗 [UpstreamHostHTTP](#upstreamhosthttp-splittersplittergo80) `:80`

- 🔗 [UpstreamHostWebsocket](#upstreamhostwebsocket-splittersplittergo59) `:59`

- 🔗 [errorHandler](#errorhandler-splittersplittergo275) `:275`

- 🔗 [getLastCursor](#getlastcursor-splittersplittergo304) `:304`

- 🔗 [handleUpstreamConnection](#handleupstreamconnection-splittersplittergo400) `:400`

- 🔗 [sleepForBackoff](#sleepforbackoff-splittersplittergo342) `:342`

- 🔗 [startWithListener](#startwithlistener-splittersplittergo194) `:194`

- 🔗 [subscribeWithRedialer](#subscribewithredialer-splittersplittergo354) `:354`

- 🔗 [writeCursor](#writecursor-splittersplittergo338) `:338`


</details>


[function] name: NewSplitter file: splitter/splitter.go:101 returns_error: да description: —


### NewSplitter (splitter/splitter.go:101)


NewSplitter is a function that performs operations based on the provided parameters and may return an error.


```go
func NewSplitter((*Splitter, error)) (*Splitter, error)
```


**Тип запроса:** Splitter


```json
{
  "erb": null,
  "pp": null,
  "events": null,
  "consumersLk": {},
  "nextConsumerID": 0,
  "consumers": {},
  "conf": {},
  "logger": null,
  "upstreamClient": null,
  "peerClient": null,
  "nextCrawlers": []
}
```


*Определено в:* `splitter/splitter.go`


**Тип ответа:** Splitter


```json
{
  "erb": null,
  "pp": null,
  "events": null,
  "consumersLk": {},
  "nextConsumerID": 0,
  "consumers": {},
  "conf": {},
  "logger": null,
  "upstreamClient": null,
  "peerClient": null,
  "nextCrawlers": []
}
```


*Определено в:* `splitter/splitter.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Splitter`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `splitter/splitter.go:101`



---


[function] name: Shutdown file: splitter/splitter.go:190 returns_error: нет description: —


### Shutdown (splitter/splitter.go:190)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (s *Splitter) Shutdown(()) ()
```


📍 *Расположение:* `splitter/splitter.go:190`



---


[function] name: StartAPI file: splitter/splitter.go:166 returns_error: нет description: —


### StartAPI (splitter/splitter.go:166)


StartAPI is a method that performs operations based on the provided parameters and returns (addr string).


```go
func (s *Splitter) StartAPI((addr string)) (addr string)
```


**Тип ответа:** addr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/splitter.go:166`



---


[function] name: StartMetrics file: splitter/splitter.go:185 returns_error: нет description: —


### StartMetrics (splitter/splitter.go:185)


StartMetrics is a method that performs operations based on the provided parameters and returns (listen string).


```go
func (s *Splitter) StartMetrics((listen string)) (listen string)
```


**Тип ответа:** listen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/splitter.go:185`



---


[function] name: UpstreamHostHTTP file: splitter/splitter.go:80 returns_error: нет description: —


### UpstreamHostHTTP (splitter/splitter.go:80)


UpstreamHostHTTP is a method that performs operations based on the provided parameters and returns ().


```go
func (sc *SplitterConfig) UpstreamHostHTTP(()) ()
```


📍 *Расположение:* `splitter/splitter.go:80`



---


[function] name: UpstreamHostWebsocket file: splitter/splitter.go:59 returns_error: нет description: —


### UpstreamHostWebsocket (splitter/splitter.go:59)


UpstreamHostWebsocket is a method that performs operations based on the provided parameters and returns ().


```go
func (sc *SplitterConfig) UpstreamHostWebsocket(()) ()
```


📍 *Расположение:* `splitter/splitter.go:59`



---


[function] name: errorHandler file: splitter/splitter.go:275 returns_error: да description: —


### errorHandler (splitter/splitter.go:275)


errorHandler is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Splitter) errorHandler((err error, ctx echo.Context)) (err error, ctx echo.Context)
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


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** echo.Context


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


*Типы возврата:* `err error`, `ctx echo.Context`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `splitter/splitter.go:275`



---


[function] name: getLastCursor file: splitter/splitter.go:304 returns_error: да description: —


### getLastCursor (splitter/splitter.go:304)


getLastCursor is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Splitter) getLastCursor((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `splitter/splitter.go:304`



---


[function] name: handleUpstreamConnection file: splitter/splitter.go:400 returns_error: нет description: —


### handleUpstreamConnection (splitter/splitter.go:400)


handleUpstreamConnection is a method that performs operations based on the provided parameters and returns (ctx context.Context, con *websocket.Conn, lastCursor *int64).


```go
func (s *Splitter) handleUpstreamConnection((ctx context.Context, con *websocket.Conn, lastCursor *int64)) (ctx context.Context, con *websocket.Conn, lastCursor *int64)
```


**Тип запроса:** websocket.Conn


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


**Тип ответа:** lastCursor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/splitter.go:400`



---


[function] name: sleepForBackoff file: splitter/splitter.go:342 returns_error: нет description: —


### sleepForBackoff (splitter/splitter.go:342)


sleepForBackoff is a function that performs operations based on the provided parameters and returns (b int).


```go
func sleepForBackoff((b int)) (b int)
```


**Тип ответа:** b


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


📍 *Расположение:* `splitter/splitter.go:342`



---


[function] name: startWithListener file: splitter/splitter.go:194 returns_error: нет description: —


### startWithListener (splitter/splitter.go:194)


startWithListener is a method that performs operations based on the provided parameters and returns (listen net.Listener).


```go
func (s *Splitter) startWithListener((listen net.Listener)) (listen net.Listener)
```


**Тип ответа:** listen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.Listener


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/splitter.go:194`



---


[function] name: subscribeWithRedialer file: splitter/splitter.go:354 returns_error: нет description: —


### subscribeWithRedialer (splitter/splitter.go:354)


subscribeWithRedialer is a method that performs operations based on the provided parameters and returns (ctx context.Context, cursor int64).


```go
func (s *Splitter) subscribeWithRedialer((ctx context.Context, cursor int64)) (ctx context.Context, cursor int64)
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


**Тип ответа:** cursor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/splitter.go:354`



---


[function] name: writeCursor file: splitter/splitter.go:338 returns_error: нет description: —


### writeCursor (splitter/splitter.go:338)


writeCursor is a method that performs operations based on the provided parameters and returns (curs int64).


```go
func (s *Splitter) writeCursor((curs int64)) (curs int64)
```


**Тип ответа:** curs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `splitter/splitter.go:338`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](search.md)

- [Следующая директория](testing.md)


---

