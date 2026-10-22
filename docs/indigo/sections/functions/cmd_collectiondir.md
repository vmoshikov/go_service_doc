---
title: "Функции: cmd/collectiondir"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/collectiondir
---


# Функции: cmd/collectiondir


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_bluepages.md)

- [Следующая директория](cmd_fakermaker.md)


---


## Меню по файлам


- 📄 [cmd/collectiondir/collectiondir.go](#cmdcollectiondircollectiondirgo)

- 📄 [cmd/collectiondir/crawl.go](#cmdcollectiondircrawlgo)

- 📄 [cmd/collectiondir/firehose.go](#cmdcollectiondirfirehosego)

- 📄 [cmd/collectiondir/pebble.go](#cmdcollectiondirpebblego)

- 📄 [cmd/collectiondir/serve.go](#cmdcollectiondirservego)


---


## cmd/collectiondir/collectiondir.go


📄 Исходный файл: `cmd/collectiondir/collectiondir.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdcollectiondircollectiondirgo25) `:25`


</details>


[function] name: main file: cmd/collectiondir/collectiondir.go:25 returns_error: нет description: —


### main (cmd/collectiondir/collectiondir.go:25)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/collectiondir/collectiondir.go:25`




## cmd/collectiondir/crawl.go


📄 Исходный файл: `cmd/collectiondir/crawl.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [CrawlPDSRepoCollections](#crawlpdsrepocollections-cmdcollectiondircrawlgo129) `:129`

- 🔗 [DidCollectionsToCsv](#didcollectionstocsv-cmdcollectiondircrawlgo27) `:27`


</details>


[function] name: CrawlPDSRepoCollections file: cmd/collectiondir/crawl.go:129 returns_error: нет description: CrawlPDSRepoCollections
write results to chan
does _not_ close chan
(allow multiple threads of PDS queries running to on


### CrawlPDSRepoCollections (cmd/collectiondir/crawl.go:129)


CrawlPDSRepoCollections
write results to chan
does _not_ close chan
(allow multiple threads of PDS queries running to one output chan, e.g. feeding into SetFromResults() )


```go
func (cr *Crawler) CrawlPDSRepoCollections(()) ()
```


📍 *Расположение:* `cmd/collectiondir/crawl.go:129`



---


[function] name: DidCollectionsToCsv file: cmd/collectiondir/crawl.go:27 returns_error: нет description: —


### DidCollectionsToCsv (cmd/collectiondir/crawl.go:27)


DidCollectionsToCsv is a function that performs operations based on the provided parameters and returns (out io.Writer, sources <-chan DidCollection).


```go
func DidCollectionsToCsv((out io.Writer, sources <-chan DidCollection)) (out io.Writer, sources <-chan DidCollection)
```


**Тип ответа:** out


```json
{
  "Name": "string",
  "Type": null,
  "NeedsCbor": false,
  "NeedsType": false
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sources


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DidCollection


```json
{
  "Did": "string",
  "Collection": "string"
}
```


*Определено в:* `cmd/collectiondir/crawl.go`


📍 *Расположение:* `cmd/collectiondir/crawl.go:27`




## cmd/collectiondir/firehose.go


📄 Исходный файл: `cmd/collectiondir/firehose.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [AddWork](#addwork-cmdcollectiondirfirehosego95) `:95`

- 🔗 [Shutdown](#shutdown-cmdcollectiondirfirehosego105) `:105`

- 🔗 [handleConnection](#handleconnection-cmdcollectiondirfirehosego87) `:87`

- 🔗 [subscribeWithRedialer](#subscribewithredialer-cmdcollectiondirfirehosego25) `:25`


</details>


[function] name: AddWork file: cmd/collectiondir/firehose.go:95 returns_error: нет description: AddWork is part of events.Scheduler


### AddWork (cmd/collectiondir/firehose.go:95)


AddWork is part of events.Scheduler


```go
func (fh *Firehose) AddWork((ctx context.Context, repo string, val *events.XRPCStreamEvent)) (ctx context.Context, repo string, val *events.XRPCStreamEvent)
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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** val


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


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


📍 *Расположение:* `cmd/collectiondir/firehose.go:95`



---


[function] name: Shutdown file: cmd/collectiondir/firehose.go:105 returns_error: нет description: Shutdown is part of events.Scheduler


### Shutdown (cmd/collectiondir/firehose.go:105)


Shutdown is part of events.Scheduler


```go
func (fh *Firehose) Shutdown(()) ()
```


📍 *Расположение:* `cmd/collectiondir/firehose.go:105`



---


[function] name: handleConnection file: cmd/collectiondir/firehose.go:87 returns_error: нет description: —


### handleConnection (cmd/collectiondir/firehose.go:87)


handleConnection is a method that performs operations based on the provided parameters and returns (ctx context.Context, con *websocket.Conn).


```go
func (fh *Firehose) handleConnection((ctx context.Context, con *websocket.Conn)) (ctx context.Context, con *websocket.Conn)
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


📍 *Расположение:* `cmd/collectiondir/firehose.go:87`



---


[function] name: subscribeWithRedialer file: cmd/collectiondir/firehose.go:25 returns_error: нет description: —


### subscribeWithRedialer (cmd/collectiondir/firehose.go:25)


subscribeWithRedialer is a method that performs operations based on the provided parameters and returns (ctx context.Context, fhevents chan<- *events.XRPCStreamEvent).


```go
func (fh *Firehose) subscribeWithRedialer((ctx context.Context, fhevents chan<- *events.XRPCStreamEvent)) (ctx context.Context, fhevents chan<- *events.XRPCStreamEvent)
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


**Тип ответа:** fhevents


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


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


📍 *Расположение:* `cmd/collectiondir/firehose.go:25`




## cmd/collectiondir/pebble.go


📄 Исходный файл: `cmd/collectiondir/pebble.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [Close](#close-cmdcollectiondirpebblego103) `:103`

- 🔗 [CollectionToId](#collectiontoid-cmdcollectiondirpebblego261) `:261`

- 🔗 [CountDidCollections](#countdidcollections-cmdcollectiondirpebblego305) `:305`

- 🔗 [GetCollectionStats](#getcollectionstats-cmdcollectiondirpebblego388) `:388`

- 🔗 [GetSequence](#getsequence-cmdcollectiondirpebblego409) `:409`

- 🔗 [MaybeSetCollection](#maybesetcollection-cmdcollectiondirpebblego330) `:330`

- 🔗 [Open](#open-cmdcollectiondirpebblego89) `:89`

- 🔗 [ReadAllPrimary](#readallprimary-cmdcollectiondirpebblego154) `:154`

- 🔗 [ReadCollection](#readcollection-cmdcollectiondirpebblego188) `:188`

- 🔗 [SetFromResults](#setfromresults-cmdcollectiondirpebblego367) `:367`

- 🔗 [SetSequence](#setsequence-cmdcollectiondirpebblego404) `:404`

- 🔗 [makeByDidKey](#makebydidkey-cmdcollectiondirpebblego52) `:52`

- 🔗 [makeCollectionInternKey](#makecollectioninternkey-cmdcollectiondirpebblego17) `:17`

- 🔗 [makePrimaryPebbleRow](#makeprimarypebblerow-cmdcollectiondirpebblego31) `:31`

- 🔗 [parseByDidKey](#parsebydidkey-cmdcollectiondirpebblego61) `:61`

- 🔗 [parseCollectionInternKey](#parsecollectioninternkey-cmdcollectiondirpebblego24) `:24`

- 🔗 [parsePrimaryPebbleRow](#parseprimarypebblerow-cmdcollectiondirpebblego42) `:42`

- 🔗 [readAllCollectionInterns](#readallcollectioninterns-cmdcollectiondirpebblego116) `:116`


</details>


[function] name: Close file: cmd/collectiondir/pebble.go:103 returns_error: нет description: —


### Close (cmd/collectiondir/pebble.go:103)


Close is a method that performs operations based on the provided parameters and returns ().


```go
func (pcd *PebbleCollectionDirectory) Close(()) ()
```


📍 *Расположение:* `cmd/collectiondir/pebble.go:103`



---


[function] name: CollectionToId file: cmd/collectiondir/pebble.go:261 returns_error: да description: —


### CollectionToId (cmd/collectiondir/pebble.go:261)


CollectionToId is a method that performs operations based on the provided parameters and may return an error.


```go
func (pcd *PebbleCollectionDirectory) CollectionToId((uint32, error)) (uint32, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `uint32`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/pebble.go:261`



---


[function] name: CountDidCollections file: cmd/collectiondir/pebble.go:305 returns_error: да description: —


### CountDidCollections (cmd/collectiondir/pebble.go:305)


CountDidCollections is a method that performs operations based on the provided parameters and may return an error.


```go
func (pcd *PebbleCollectionDirectory) CountDidCollections((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/pebble.go:305`



---


[function] name: GetCollectionStats file: cmd/collectiondir/pebble.go:388 returns_error: да description: —


### GetCollectionStats (cmd/collectiondir/pebble.go:388)


GetCollectionStats is a method that retrieves data based on the provided parameters and may return an error.


```go
func (pcd *PebbleCollectionDirectory) GetCollectionStats((stats CollectionStats, err error)) (stats CollectionStats, err error)
```


**Тип ответа:** stats


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CollectionStats


```json
{
  "CollectionCounts": {}
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


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


*Типы возврата:* `stats CollectionStats`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/pebble.go:388`



---


[function] name: GetSequence file: cmd/collectiondir/pebble.go:409 returns_error: да description: —


### GetSequence (cmd/collectiondir/pebble.go:409)


GetSequence is a method that retrieves data based on the provided parameters and may return an error.


```go
func (pcd *PebbleCollectionDirectory) GetSequence((int64, bool, error)) (int64, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/pebble.go:409`



---


[function] name: MaybeSetCollection file: cmd/collectiondir/pebble.go:330 returns_error: нет description: —


### MaybeSetCollection (cmd/collectiondir/pebble.go:330)


MaybeSetCollection is a method that performs operations based on the provided parameters and returns (did, collection string).


```go
func (pcd *PebbleCollectionDirectory) MaybeSetCollection((did, collection string)) (did, collection string)
```


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** collection


```json
{
  "ctx": {},
  "pcd": null,
  "dauDirectory": null,
  "dauDirectoryPath": "string",
  "dauDay": {},
  "dauTomorrow": {},
  "dauDirectoryDir": "string",
  "statsCache": null,
  "statsCacheWhen": {},
  "statsCacheLock": {},
  "statsCacheFresh": {},
  "statsCachePending": false,
  "ingestFirehose": {},
  "ingestCrawl": {},
  "log": null,
  "AdminToken": "string",
  "ExepctedAuthHeader": "string",
  "PerPDSCrawlQPS": 0.0,
  "activeCrawls": {},
  "activeCrawlsLock": {},
  "shutdown": {},
  "wg": {},
  "ratelimitHeader": "string",
  "apiServer": null,
  "metricsServer": null,
  "MinDidsForCollectionList": 0,
  "MaxDidCollections": 0,
  "didCollectionCounts": null,
  "badwords": {}
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `cmd/collectiondir/pebble.go:330`



---


[function] name: Open file: cmd/collectiondir/pebble.go:89 returns_error: нет description: —


### Open (cmd/collectiondir/pebble.go:89)


Open is a method that performs operations based on the provided parameters and returns (pebblePath string).


```go
func (pcd *PebbleCollectionDirectory) Open((pebblePath string)) (pebblePath string)
```


**Тип ответа:** pebblePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/pebble.go:89`



---


[function] name: ReadAllPrimary file: cmd/collectiondir/pebble.go:154 returns_error: нет description: —


### ReadAllPrimary (cmd/collectiondir/pebble.go:154)


ReadAllPrimary is a method that performs operations based on the provided parameters and returns (ctx context.Context, out chan<- CollectionDidTime).


```go
func (pcd *PebbleCollectionDirectory) ReadAllPrimary((ctx context.Context, out chan<- CollectionDidTime)) (ctx context.Context, out chan<- CollectionDidTime)
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


**Тип ответа:** out


```json
{
  "Name": "string",
  "Type": null,
  "NeedsCbor": false,
  "NeedsType": false
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CollectionDidTime


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


📍 *Расположение:* `cmd/collectiondir/pebble.go:154`



---


[function] name: ReadCollection file: cmd/collectiondir/pebble.go:188 returns_error: да description: —


### ReadCollection (cmd/collectiondir/pebble.go:188)


ReadCollection is a method that performs operations based on the provided parameters and may return an error.


```go
func (pcd *PebbleCollectionDirectory) ReadCollection((result []CollectionDidTime, nextCursor string, err error)) (result []CollectionDidTime, nextCursor string, err error)
```


**Тип ответа:** result


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CollectionDidTime


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** nextCursor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `result []CollectionDidTime`, `nextCursor string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/pebble.go:188`



---


[function] name: SetFromResults file: cmd/collectiondir/pebble.go:367 returns_error: нет description: —


### SetFromResults (cmd/collectiondir/pebble.go:367)


SetFromResults is a method that updates data based on the provided parameters and returns (results <-chan DidCollection).


```go
func (pcd *PebbleCollectionDirectory) SetFromResults((results <-chan DidCollection)) (results <-chan DidCollection)
```


**Тип ответа:** results


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DidCollection


```json
{
  "Did": "string",
  "Collection": "string"
}
```


*Определено в:* `cmd/collectiondir/crawl.go`


📍 *Расположение:* `cmd/collectiondir/pebble.go:367`



---


[function] name: SetSequence file: cmd/collectiondir/pebble.go:404 returns_error: нет description: —


### SetSequence (cmd/collectiondir/pebble.go:404)


SetSequence is a method that updates data based on the provided parameters and returns (seq int64).


```go
func (pcd *PebbleCollectionDirectory) SetSequence((seq int64)) (seq int64)
```


**Тип ответа:** seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/pebble.go:404`



---


[function] name: makeByDidKey file: cmd/collectiondir/pebble.go:52 returns_error: нет description: —


### makeByDidKey (cmd/collectiondir/pebble.go:52)


makeByDidKey is a function that performs operations based on the provided parameters and returns (did string, collectionId uint32).


```go
func makeByDidKey((did string, collectionId uint32)) (did string, collectionId uint32)
```


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** collectionId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/pebble.go:52`



---


[function] name: makeCollectionInternKey file: cmd/collectiondir/pebble.go:17 returns_error: нет description: —


### makeCollectionInternKey (cmd/collectiondir/pebble.go:17)


makeCollectionInternKey is a function that performs operations based on the provided parameters and returns (collection string).


```go
func makeCollectionInternKey((collection string)) (collection string)
```


**Тип ответа:** collection


```json
{
  "ctx": {},
  "pcd": null,
  "dauDirectory": null,
  "dauDirectoryPath": "string",
  "dauDay": {},
  "dauTomorrow": {},
  "dauDirectoryDir": "string",
  "statsCache": null,
  "statsCacheWhen": {},
  "statsCacheLock": {},
  "statsCacheFresh": {},
  "statsCachePending": false,
  "ingestFirehose": {},
  "ingestCrawl": {},
  "log": null,
  "AdminToken": "string",
  "ExepctedAuthHeader": "string",
  "PerPDSCrawlQPS": 0.0,
  "activeCrawls": {},
  "activeCrawlsLock": {},
  "shutdown": {},
  "wg": {},
  "ratelimitHeader": "string",
  "apiServer": null,
  "metricsServer": null,
  "MinDidsForCollectionList": 0,
  "MaxDidCollections": 0,
  "didCollectionCounts": null,
  "badwords": {}
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `cmd/collectiondir/pebble.go:17`



---


[function] name: makePrimaryPebbleRow file: cmd/collectiondir/pebble.go:31 returns_error: нет description: —


### makePrimaryPebbleRow (cmd/collectiondir/pebble.go:31)


makePrimaryPebbleRow is a function that performs operations based on the provided parameters and returns (collectionId uint32, did string, seenMs int64).


```go
func makePrimaryPebbleRow((collectionId uint32, did string, seenMs int64)) (collectionId uint32, did string, seenMs int64)
```


**Тип ответа:** collectionId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** seenMs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/pebble.go:31`



---


[function] name: parseByDidKey file: cmd/collectiondir/pebble.go:61 returns_error: нет description: —


### parseByDidKey (cmd/collectiondir/pebble.go:61)


parseByDidKey is a function that performs operations based on the provided parameters and returns (did string, collectionId uint32).


```go
func parseByDidKey((did string, collectionId uint32)) (did string, collectionId uint32)
```


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** collectionId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/pebble.go:61`



---


[function] name: parseCollectionInternKey file: cmd/collectiondir/pebble.go:24 returns_error: нет description: —


### parseCollectionInternKey (cmd/collectiondir/pebble.go:24)


parseCollectionInternKey is a function that performs operations based on the provided parameters and returns (key []byte).


```go
func parseCollectionInternKey((key []byte)) (key []byte)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/pebble.go:24`



---


[function] name: parsePrimaryPebbleRow file: cmd/collectiondir/pebble.go:42 returns_error: нет description: —


### parsePrimaryPebbleRow (cmd/collectiondir/pebble.go:42)


parsePrimaryPebbleRow is a function that performs operations based on the provided parameters and returns (collectionId uint32, did string, seenMs int64).


```go
func parsePrimaryPebbleRow((collectionId uint32, did string, seenMs int64)) (collectionId uint32, did string, seenMs int64)
```


**Тип ответа:** collectionId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** seenMs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/pebble.go:42`



---


[function] name: readAllCollectionInterns file: cmd/collectiondir/pebble.go:116 returns_error: нет description: readAllCollectionInterns should only be run at setup time inside Open() when locking against threads is not needed


### readAllCollectionInterns (cmd/collectiondir/pebble.go:116)


readAllCollectionInterns should only be run at setup time inside Open() when locking against threads is not needed


```go
func (pcd *PebbleCollectionDirectory) readAllCollectionInterns((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/collectiondir/pebble.go:116`




## cmd/collectiondir/serve.go


📄 Исходный файл: `cmd/collectiondir/serve.go`


<details open>
<summary><b>Функции в этом файле (32)</b></summary>


- 🔗 [HasBadword](#hasbadword-cmdcollectiondirservego1032) `:1032`

- 🔗 [Shutdown](#shutdown-cmdcollectiondirservego277) `:277`

- 🔗 [StartApiServer](#startapiserver-cmdcollectiondirservego443) `:443`

- 🔗 [StartMetricsServer](#startmetricsserver-cmdcollectiondirservego395) `:395`

- 🔗 [clearActiveCrawl](#clearactivecrawl-cmdcollectiondirservego958) `:958`

- 🔗 [crawlPds](#crawlpds-cmdcollectiondirservego871) `:871`

- 🔗 [crawlStatus](#crawlstatus-cmdcollectiondirservego977) `:977`

- 🔗 [crawlThread](#crawlthread-cmdcollectiondirservego897) `:897`

- 🔗 [createApiServer](#createapiserver-cmdcollectiondirservego406) `:406`

- 🔗 [createMetricsServer](#createmetricsserver-cmdcollectiondirservego384) `:384`

- 🔗 [dauStats](#daustats-cmdcollectiondirservego778) `:778`

- 🔗 [firehoseThread](#firehosethread-cmdcollectiondirservego309) `:309`

- 🔗 [getDidsForCollection](#getdidsforcollection-cmdcollectiondirservego479) `:479`

- 🔗 [getLimit](#getlimit-cmdcollectiondirservego455) `:455`

- 🔗 [getStatsCache](#getstatscache-cmdcollectiondirservego510) `:510`

- 🔗 [handleCommit](#handlecommit-cmdcollectiondirservego365) `:365`

- 🔗 [handleFirehose](#handlefirehose-cmdcollectiondirservego330) `:330`

- 🔗 [hasBadword](#hasbadword-cmdcollectiondirservego620) `:620`

- 🔗 [healthz](#healthz-cmdcollectiondirservego997) `:997`

- 🔗 [hostOrUrlToUrl](#hostorurltourl-cmdcollectiondirservego837) `:837`

- 🔗 [ingestDidc](#ingestdidc-cmdcollectiondirservego735) `:735`

- 🔗 [ingestReceiver](#ingestreceiver-cmdcollectiondirservego700) `:700`

- 🔗 [isAdmin](#isadmin-cmdcollectiondirservego851) `:851`

- 🔗 [listCollections](#listcollections-cmdcollectiondirservego633) `:633`

- 🔗 [loadBadwords](#loadbadwords-cmdcollectiondirservego1002) `:1002`

- 🔗 [maybeDauWrite](#maybedauwrite-cmdcollectiondirservego764) `:764`

- 🔗 [openDau](#opendau-cmdcollectiondirservego257) `:257`

- 🔗 [pcdStatsToCsvGz](#pcdstatstocsvgz-cmdcollectiondirservego796) `:796`

- 🔗 [recordCrawlStart](#recordcrawlstart-cmdcollectiondirservego939) `:939`

- 🔗 [run](#run-cmdcollectiondirservego168) `:168`

- 🔗 [statsBuilder](#statsbuilder-cmdcollectiondirservego594) `:594`

- 🔗 [waiter](#waiter-cmdcollectiondirservego581) `:581`


</details>


[function] name: HasBadword file: cmd/collectiondir/serve.go:1032 returns_error: нет description: —


### HasBadword (cmd/collectiondir/serve.go:1032)


HasBadword is a method that performs operations based on the provided parameters and returns (s string).


```go
func (bw *BadwordsRE) HasBadword((s string)) (s string)
```


**Тип ответа:** s


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


📍 *Расположение:* `cmd/collectiondir/serve.go:1032`



---


[function] name: Shutdown file: cmd/collectiondir/serve.go:277 returns_error: нет description: —


### Shutdown (cmd/collectiondir/serve.go:277)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (cs *collectionServer) Shutdown(()) ()
```


📍 *Расположение:* `cmd/collectiondir/serve.go:277`



---


[function] name: StartApiServer file: cmd/collectiondir/serve.go:443 returns_error: нет description: —


### StartApiServer (cmd/collectiondir/serve.go:443)


StartApiServer is a method that performs operations based on the provided parameters and returns (ctx context.Context, e *echo.Echo).


```go
func (cs *collectionServer) StartApiServer((ctx context.Context, e *echo.Echo)) (ctx context.Context, e *echo.Echo)
```


**Тип запроса:** echo.Echo


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


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** echo.Echo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/serve.go:443`



---


[function] name: StartMetricsServer file: cmd/collectiondir/serve.go:395 returns_error: нет description: —


### StartMetricsServer (cmd/collectiondir/serve.go:395)


StartMetricsServer is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (cs *collectionServer) StartMetricsServer((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/collectiondir/serve.go:395`



---


[function] name: clearActiveCrawl file: cmd/collectiondir/serve.go:958 returns_error: нет description: —


### clearActiveCrawl (cmd/collectiondir/serve.go:958)


clearActiveCrawl is a method that performs operations based on the provided parameters and returns (host string).


```go
func (cs *collectionServer) clearActiveCrawl((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


📍 *Расположение:* `cmd/collectiondir/serve.go:958`



---


[function] name: crawlPds file: cmd/collectiondir/serve.go:871 returns_error: нет description: /admin/pds/requestCrawl
same API signature as relay admin requestCrawl
starts a crawl and returns. See /v1/crawlStatus
r


### crawlPds (cmd/collectiondir/serve.go:871)


/admin/pds/requestCrawl
same API signature as relay admin requestCrawl
starts a crawl and returns. See /v1/crawlStatus
requires header `Authorization: Bearer {admin token}`

POST {"hostname":"one hostname or URL", "hosts":["up to 1000 hosts", "..."]}
OR
POST /admin/pds/requestCrawl?hostname={one host}


```go
func (cs *collectionServer) crawlPds((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/collectiondir/serve.go:871`



---


[function] name: crawlStatus file: cmd/collectiondir/serve.go:977 returns_error: нет description: GET /v1/crawlStatus


### crawlStatus (cmd/collectiondir/serve.go:977)


GET /v1/crawlStatus


```go
func (cs *collectionServer) crawlStatus((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/collectiondir/serve.go:977`



---


[function] name: crawlThread file: cmd/collectiondir/serve.go:897 returns_error: нет description: —


### crawlThread (cmd/collectiondir/serve.go:897)


crawlThread is a method that performs operations based on the provided parameters and returns (hostIn string).


```go
func (cs *collectionServer) crawlThread((hostIn string)) (hostIn string)
```


**Тип ответа:** hostIn


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


📍 *Расположение:* `cmd/collectiondir/serve.go:897`



---


[function] name: createApiServer file: cmd/collectiondir/serve.go:406 returns_error: да description: —


### createApiServer (cmd/collectiondir/serve.go:406)


createApiServer is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *collectionServer) createApiServer((*echo.Echo, error)) (*echo.Echo, error)
```


**Тип запроса:** echo.Echo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** echo.Echo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*echo.Echo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/serve.go:406`



---


[function] name: createMetricsServer file: cmd/collectiondir/serve.go:384 returns_error: нет description: —


### createMetricsServer (cmd/collectiondir/serve.go:384)


createMetricsServer is a method that performs operations based on the provided parameters and returns (addr string).


```go
func (cs *collectionServer) createMetricsServer((addr string)) (addr string)
```


**Тип ответа:** addr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/serve.go:384`



---


[function] name: dauStats file: cmd/collectiondir/serve.go:778 returns_error: нет description: write {dauDirectoryDir}/d{YYYY-MM-DD}.pebble stats summary to {dauDirectoryDir}/d{YYYY-MM-DD}.csv.gz


### dauStats (cmd/collectiondir/serve.go:778)


write {dauDirectoryDir}/d{YYYY-MM-DD}.pebble stats summary to {dauDirectoryDir}/d{YYYY-MM-DD}.csv.gz


```go
func dauStats((oldDau *PebbleCollectionDirectory, dauDay time.Time, dauDir string, log *slog.Logger)) (oldDau *PebbleCollectionDirectory, dauDay time.Time, dauDir string, log *slog.Logger)
```


**Тип запроса:** PebbleCollectionDirectory


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


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldDau


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PebbleCollectionDirectory


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


**Тип ответа:** dauDay


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Time


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** dauDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** log


```json
{
  "inner": null
}
```


*Определено в:* `util/http.go`


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/serve.go:778`



---


[function] name: firehoseThread file: cmd/collectiondir/serve.go:309 returns_error: нет description: firehoseThreads is responsible for connecting to upstream firehose source


### firehoseThread (cmd/collectiondir/serve.go:309)


firehoseThreads is responsible for connecting to upstream firehose source


```go
func (cs *collectionServer) firehoseThread((fh *Firehose, fhevents chan<- *events.XRPCStreamEvent)) (fh *Firehose, fhevents chan<- *events.XRPCStreamEvent)
```


**Тип запроса:** Firehose


```json
{
  "Log": null,
  "Host": "string",
  "Seq": 0,
  "events": {}
}
```


*Определено в:* `cmd/collectiondir/firehose.go`


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


**Тип ответа:** fh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Firehose


```json
{
  "Log": null,
  "Host": "string",
  "Seq": 0,
  "events": {}
}
```


*Определено в:* `cmd/collectiondir/firehose.go`


**Тип ответа:** fhevents


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


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


📍 *Расположение:* `cmd/collectiondir/serve.go:309`



---


[function] name: getDidsForCollection file: cmd/collectiondir/serve.go:479 returns_error: нет description: /xrpc/com.atproto.sync.listReposByCollection?collection={}&cursor={}&limit={50<=N<=1000}
/v1/getDidsForCollection?collec


### getDidsForCollection (cmd/collectiondir/serve.go:479)


/xrpc/com.atproto.sync.listReposByCollection?collection={}&cursor={}&limit={50<=N<=1000}
/v1/getDidsForCollection?collection={}&cursor={}&limit={50<=N<=1000}

returns
{"dids":["did:A", "..."], "cursor":"opaque text"}


```go
func (cs *collectionServer) getDidsForCollection((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/collectiondir/serve.go:479`



---


[function] name: getLimit file: cmd/collectiondir/serve.go:455 returns_error: нет description: —


### getLimit (cmd/collectiondir/serve.go:455)


getLimit is a function that performs operations based on the provided parameters and returns (c echo.Context, min, defaultLim, max int).


```go
func getLimit((c echo.Context, min, defaultLim, max int)) (c echo.Context, min, defaultLim, max int)
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


**Тип ответа:** min


```json
{
  "Password": "string"
}
```


*Определено в:* `atproto/atclient/admin_auth.go`


**Тип ответа:** defaultLim


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** max


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/serve.go:455`



---


[function] name: getStatsCache file: cmd/collectiondir/serve.go:510 returns_error: да description: return cached collection stats if they're fresh
return new collection stats if they can be calculated quickly
return sta


### getStatsCache (cmd/collectiondir/serve.go:510)


return cached collection stats if they're fresh
return new collection stats if they can be calculated quickly
return stale cached collection stats if new stats take too long
just wait for fresh stats if there are no cached stats
stalenessAllowed is how old stats can be before we try to recalculate them, 0=default of 5 minutes


```go
func (cs *collectionServer) getStatsCache((*CollectionStats, error)) (*CollectionStats, error)
```


**Тип запроса:** CollectionStats


```json
{
  "CollectionCounts": {}
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** CollectionStats


```json
{
  "CollectionCounts": {}
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CollectionStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/serve.go:510`



---


[function] name: handleCommit file: cmd/collectiondir/serve.go:365 returns_error: нет description: —


### handleCommit (cmd/collectiondir/serve.go:365)


handleCommit is a method that performs operations based on the provided parameters and returns (commit *comatproto.SyncSubscribeRepos_Commit).


```go
func (cs *collectionServer) handleCommit((commit *comatproto.SyncSubscribeRepos_Commit)) (commit *comatproto.SyncSubscribeRepos_Commit)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


**Тип ответа:** commit


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `cmd/collectiondir/serve.go:365`



---


[function] name: handleFirehose file: cmd/collectiondir/serve.go:330 returns_error: нет description: handleFirehose consumes XRPCStreamEvent from firehoseThread(), further parses data and applies


### handleFirehose (cmd/collectiondir/serve.go:330)


handleFirehose consumes XRPCStreamEvent from firehoseThread(), further parses data and applies


```go
func (cs *collectionServer) handleFirehose((fhevents <-chan *events.XRPCStreamEvent)) (fhevents <-chan *events.XRPCStreamEvent)
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


**Тип ответа:** fhevents


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


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


📍 *Расположение:* `cmd/collectiondir/serve.go:330`



---


[function] name: hasBadword file: cmd/collectiondir/serve.go:620 returns_error: нет description: —


### hasBadword (cmd/collectiondir/serve.go:620)


hasBadword is a method that performs operations based on the provided parameters and returns (collection string).


```go
func (cs *collectionServer) hasBadword((collection string)) (collection string)
```


**Тип ответа:** collection


```json
{
  "ctx": {},
  "pcd": null,
  "dauDirectory": null,
  "dauDirectoryPath": "string",
  "dauDay": {},
  "dauTomorrow": {},
  "dauDirectoryDir": "string",
  "statsCache": null,
  "statsCacheWhen": {},
  "statsCacheLock": {},
  "statsCacheFresh": {},
  "statsCachePending": false,
  "ingestFirehose": {},
  "ingestCrawl": {},
  "log": null,
  "AdminToken": "string",
  "ExepctedAuthHeader": "string",
  "PerPDSCrawlQPS": 0.0,
  "activeCrawls": {},
  "activeCrawlsLock": {},
  "shutdown": {},
  "wg": {},
  "ratelimitHeader": "string",
  "apiServer": null,
  "metricsServer": null,
  "MinDidsForCollectionList": 0,
  "MaxDidCollections": 0,
  "didCollectionCounts": null,
  "badwords": {}
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `cmd/collectiondir/serve.go:620`



---


[function] name: healthz file: cmd/collectiondir/serve.go:997 returns_error: нет description: —


### healthz (cmd/collectiondir/serve.go:997)


healthz is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (cs *collectionServer) healthz((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/collectiondir/serve.go:997`



---


[function] name: hostOrUrlToUrl file: cmd/collectiondir/serve.go:837 returns_error: нет description: —


### hostOrUrlToUrl (cmd/collectiondir/serve.go:837)


hostOrUrlToUrl is a function that performs operations based on the provided parameters and returns (host string).


```go
func hostOrUrlToUrl((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


📍 *Расположение:* `cmd/collectiondir/serve.go:837`



---


[function] name: ingestDidc file: cmd/collectiondir/serve.go:735 returns_error: нет description: —


### ingestDidc (cmd/collectiondir/serve.go:735)


ingestDidc is a method that performs operations based on the provided parameters and returns (didc DidCollection, dau bool).


```go
func (cs *collectionServer) ingestDidc((didc DidCollection, dau bool)) (didc DidCollection, dau bool)
```


**Тип ответа:** didc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DidCollection


```json
{
  "Did": "string",
  "Collection": "string"
}
```


*Определено в:* `cmd/collectiondir/crawl.go`


**Тип ответа:** dau


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/serve.go:735`



---


[function] name: ingestReceiver file: cmd/collectiondir/serve.go:700 returns_error: нет description: —


### ingestReceiver (cmd/collectiondir/serve.go:700)


ingestReceiver is a method that performs operations based on the provided parameters and returns ().


```go
func (cs *collectionServer) ingestReceiver(()) ()
```


📍 *Расположение:* `cmd/collectiondir/serve.go:700`



---


[function] name: isAdmin file: cmd/collectiondir/serve.go:851 returns_error: нет description: —


### isAdmin (cmd/collectiondir/serve.go:851)


isAdmin is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (cs *collectionServer) isAdmin((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/collectiondir/serve.go:851`



---


[function] name: listCollections file: cmd/collectiondir/serve.go:633 returns_error: нет description: /v1/listCollections?c={}&cursor={}&limit={50<=limit<=1000}

admin may set ?stalesec={} for a maximum number of seconds s


### listCollections (cmd/collectiondir/serve.go:633)


/v1/listCollections?c={}&cursor={}&limit={50<=limit<=1000}

admin may set ?stalesec={} for a maximum number of seconds stale data is accepted

returns
{"collections":{"app.bsky.feed.post": 123456789, "some collection": 42}, "cursor":"opaque text"}


```go
func (cs *collectionServer) listCollections((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/collectiondir/serve.go:633`



---


[function] name: loadBadwords file: cmd/collectiondir/serve.go:1002 returns_error: да description: —


### loadBadwords (cmd/collectiondir/serve.go:1002)


loadBadwords is a function that performs operations based on the provided parameters and may return an error.


```go
func loadBadwords((*BadwordsRE, error)) (*BadwordsRE, error)
```


**Тип запроса:** BadwordsRE


```json
{
  "re": null
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** BadwordsRE


```json
{
  "re": null
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*BadwordsRE`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/collectiondir/serve.go:1002`



---


[function] name: maybeDauWrite file: cmd/collectiondir/serve.go:764 returns_error: нет description: —


### maybeDauWrite (cmd/collectiondir/serve.go:764)


maybeDauWrite is a method that performs operations based on the provided parameters and returns (didc DidCollection).


```go
func (cs *collectionServer) maybeDauWrite((didc DidCollection)) (didc DidCollection)
```


**Тип ответа:** didc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DidCollection


```json
{
  "Did": "string",
  "Collection": "string"
}
```


*Определено в:* `cmd/collectiondir/crawl.go`


📍 *Расположение:* `cmd/collectiondir/serve.go:764`



---


[function] name: openDau file: cmd/collectiondir/serve.go:257 returns_error: нет description: —


### openDau (cmd/collectiondir/serve.go:257)


openDau is a method that performs operations based on the provided parameters and returns ().


```go
func (cs *collectionServer) openDau(()) ()
```


📍 *Расположение:* `cmd/collectiondir/serve.go:257`



---


[function] name: pcdStatsToCsvGz file: cmd/collectiondir/serve.go:796 returns_error: нет description: —


### pcdStatsToCsvGz (cmd/collectiondir/serve.go:796)


pcdStatsToCsvGz is a function that performs operations based on the provided parameters and returns (stats CollectionStats, outpath string, log *slog.Logger).


```go
func pcdStatsToCsvGz((stats CollectionStats, outpath string, log *slog.Logger)) (stats CollectionStats, outpath string, log *slog.Logger)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stats


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CollectionStats


```json
{
  "CollectionCounts": {}
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** outpath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** log


```json
{
  "inner": null
}
```


*Определено в:* `util/http.go`


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/serve.go:796`



---


[function] name: recordCrawlStart file: cmd/collectiondir/serve.go:939 returns_error: нет description: recordCrawlStart returns true if ok, false if duplicate


### recordCrawlStart (cmd/collectiondir/serve.go:939)


recordCrawlStart returns true if ok, false if duplicate


```go
func (cs *collectionServer) recordCrawlStart((ok bool, stats *CrawlStats)) (ok bool, stats *CrawlStats)
```


**Тип запроса:** CrawlStats


```json
{
  "ReposDescribed": {}
}
```


*Определено в:* `cmd/collectiondir/crawl.go`


**Тип ответа:** ok


```json
{
  "logger": null,
  "webhookURL": "string",
  "adminPassword": "string",
  "httpClient": null
}
```


*Определено в:* `cmd/tap/webhook_client.go`


**Тип ответа:** stats


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CrawlStats


```json
{
  "ReposDescribed": {}
}
```


*Определено в:* `cmd/collectiondir/crawl.go`


📍 *Расположение:* `cmd/collectiondir/serve.go:939`



---


[function] name: run file: cmd/collectiondir/serve.go:168 returns_error: нет description: —


### run (cmd/collectiondir/serve.go:168)


run is a method that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func (cs *collectionServer) run((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
```


**Тип запроса:** cli.Command


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


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/collectiondir/serve.go:168`



---


[function] name: statsBuilder file: cmd/collectiondir/serve.go:594 returns_error: нет description: —


### statsBuilder (cmd/collectiondir/serve.go:594)


statsBuilder is a method that performs operations based on the provided parameters and returns ().


```go
func (cs *collectionServer) statsBuilder(()) ()
```


📍 *Расположение:* `cmd/collectiondir/serve.go:594`



---


[function] name: waiter file: cmd/collectiondir/serve.go:581 returns_error: нет description: —


### waiter (cmd/collectiondir/serve.go:581)


waiter is a method that performs operations based on the provided parameters and returns ().


```go
func (fsw *freshStatsWaiter) waiter(()) ()
```


📍 *Расположение:* `cmd/collectiondir/serve.go:581`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_bluepages.md)

- [Следующая директория](cmd_fakermaker.md)


---

