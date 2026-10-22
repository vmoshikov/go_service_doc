---
title: "Функции: cmd/tap"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/tap
---


# Функции: cmd/tap


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_stress.md)

- [Следующая директория](events.md)


---


## Меню по файлам


- 📄 [cmd/tap/crawler.go](#cmdtapcrawlergo)

- 📄 [cmd/tap/db_helpers.go](#cmdtapdb_helpersgo)

- 📄 [cmd/tap/event_manager.go](#cmdtapevent_managergo)

- 📄 [cmd/tap/firehose.go](#cmdtapfirehosego)

- 📄 [cmd/tap/main.go](#cmdtapmaingo)

- 📄 [cmd/tap/outbox.go](#cmdtapoutboxgo)

- 📄 [cmd/tap/repo_manager.go](#cmdtaprepo_managergo)

- 📄 [cmd/tap/resyncer.go](#cmdtapresyncergo)

- 📄 [cmd/tap/server.go](#cmdtapservergo)

- 📄 [cmd/tap/tap.go](#cmdtaptapgo)

- 📄 [cmd/tap/types.go](#cmdtaptypesgo)

- 📄 [cmd/tap/util.go](#cmdtaputilgo)

- 📄 [cmd/tap/webhook_client.go](#cmdtapwebhook_clientgo)


---


## cmd/tap/crawler.go


📄 Исходный файл: `cmd/tap/crawler.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [EnumerateNetwork](#enumeratenetwork-cmdtapcrawlergo72) `:72`

- 🔗 [EnumerateNetworkByCollection](#enumeratenetworkbycollection-cmdtapcrawlergo153) `:153`

- 🔗 [GetCursor](#getcursor-cmdtapcrawlergo62) `:62`

- 🔗 [NewCrawler](#newcrawler-cmdtapcrawlergo27) `:27`

- 🔗 [Run](#run-cmdtapcrawlergo37) `:37`

- 🔗 [getCollectionCursor](#getcollectioncursor-cmdtapcrawlergo220) `:220`

- 🔗 [getListReposCursor](#getlistreposcursor-cmdtapcrawlergo140) `:140`


</details>


[function] name: EnumerateNetwork file: cmd/tap/crawler.go:72 returns_error: нет description: EnumerateNetwork discovers and tracks all repositories on the network.


### EnumerateNetwork (cmd/tap/crawler.go:72)


EnumerateNetwork discovers and tracks all repositories on the network.


```go
func (c *Crawler) EnumerateNetwork((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/crawler.go:72`



---


[function] name: EnumerateNetworkByCollection file: cmd/tap/crawler.go:153 returns_error: нет description: EnumerateNetworkByCollection discovers repositories that have records in the specified collection.


### EnumerateNetworkByCollection (cmd/tap/crawler.go:153)


EnumerateNetworkByCollection discovers repositories that have records in the specified collection.


```go
func (c *Crawler) EnumerateNetworkByCollection((ctx context.Context, collection string)) (ctx context.Context, collection string)
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


📍 *Расположение:* `cmd/tap/crawler.go:153`



---


[function] name: GetCursor file: cmd/tap/crawler.go:62 returns_error: да description: —


### GetCursor (cmd/tap/crawler.go:62)


GetCursor is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c *Crawler) GetCursor((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/crawler.go:62`



---


[function] name: NewCrawler file: cmd/tap/crawler.go:27 returns_error: нет description: —


### NewCrawler (cmd/tap/crawler.go:27)


NewCrawler is a function that performs operations based on the provided parameters and returns (logger *slog.Logger, db *gorm.DB, config *TapConfig).


```go
func NewCrawler((logger *slog.Logger, db *gorm.DB, config *TapConfig)) (logger *slog.Logger, db *gorm.DB, config *TapConfig)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип запроса:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** db


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


📍 *Расположение:* `cmd/tap/crawler.go:27`



---


[function] name: Run file: cmd/tap/crawler.go:37 returns_error: нет description: —


### Run (cmd/tap/crawler.go:37)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Crawler) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/crawler.go:37`



---


[function] name: getCollectionCursor file: cmd/tap/crawler.go:220 returns_error: да description: —


### getCollectionCursor (cmd/tap/crawler.go:220)


getCollectionCursor is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *Crawler) getCollectionCursor((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/crawler.go:220`



---


[function] name: getListReposCursor file: cmd/tap/crawler.go:140 returns_error: да description: —


### getListReposCursor (cmd/tap/crawler.go:140)


getListReposCursor is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *Crawler) getListReposCursor((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/crawler.go:140`




## cmd/tap/db_helpers.go


📄 Исходный файл: `cmd/tap/db_helpers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [deleteRepo](#deleterepo-cmdtapdb_helpersgo8) `:8`


</details>


[function] name: deleteRepo file: cmd/tap/db_helpers.go:8 returns_error: нет description: —


### deleteRepo (cmd/tap/db_helpers.go:8)


deleteRepo is a function that performs operations based on the provided parameters and returns (tx *gorm.DB, did string).


```go
func deleteRepo((tx *gorm.DB, did string)) (tx *gorm.DB, did string)
```


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** tx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `cmd/tap/db_helpers.go:8`




## cmd/tap/event_manager.go


📄 Исходный файл: `cmd/tap/event_manager.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [AddCommit](#addcommit-cmdtapevent_managergo162) `:162`

- 🔗 [AddIdentityEvent](#addidentityevent-cmdtapevent_managergo296) `:296`

- 🔗 [AddRecordEvents](#addrecordevents-cmdtapevent_managergo201) `:201`

- 🔗 [DeleteEvents](#deleteevents-cmdtapevent_managergo78) `:78`

- 🔗 [GetEvent](#getevent-cmdtapevent_managergo71) `:71`

- 🔗 [IsFull](#isfull-cmdtapevent_managergo43) `:43`

- 🔗 [IsReady](#isready-cmdtapevent_managergo49) `:49`

- 🔗 [LoadEvents](#loadevents-cmdtapevent_managergo96) `:96`

- 🔗 [NewEventManager](#neweventmanager-cmdtapevent_managergo31) `:31`

- 🔗 [WaitForReady](#waitforready-cmdtapevent_managergo53) `:53`

- 🔗 [addToResyncBuffer](#addtoresyncbuffer-cmdtapevent_managergo332) `:332`

- 🔗 [loadEventPage](#loadeventpage-cmdtapevent_managergo123) `:123`

- 🔗 [updateRepoCommitMeta](#updaterepocommitmeta-cmdtapevent_managergo192) `:192`


</details>


[function] name: AddCommit file: cmd/tap/event_manager.go:162 returns_error: нет description: —


### AddCommit (cmd/tap/event_manager.go:162)


AddCommit is a method that creates new data based on the provided parameters and returns (ctx context.Context, commit *Commit, dbCallback DBCallback).


```go
func (em *EventManager) AddCommit((ctx context.Context, commit *Commit, dbCallback DBCallback)) (ctx context.Context, commit *Commit, dbCallback DBCallback)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


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


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** dbCallback


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DBCallback


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/event_manager.go:162`



---


[function] name: AddIdentityEvent file: cmd/tap/event_manager.go:296 returns_error: нет description: —


### AddIdentityEvent (cmd/tap/event_manager.go:296)


AddIdentityEvent is a method that creates new data based on the provided parameters and returns (ctx context.Context, evt *IdentityEvt, dbCallback DBCallback).


```go
func (em *EventManager) AddIdentityEvent((ctx context.Context, evt *IdentityEvt, dbCallback DBCallback)) (ctx context.Context, evt *IdentityEvt, dbCallback DBCallback)
```


**Тип запроса:** IdentityEvt


```json
{
  "Did": "string",
  "Handle": "string",
  "IsActive": false,
  "Status": {}
}
```


*Определено в:* `cmd/tap/types.go`


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


**Тип ответа:** IdentityEvt


```json
{
  "Did": "string",
  "Handle": "string",
  "IsActive": false,
  "Status": {}
}
```


*Определено в:* `cmd/tap/types.go`


**Тип ответа:** dbCallback


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DBCallback


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/event_manager.go:296`



---


[function] name: AddRecordEvents file: cmd/tap/event_manager.go:201 returns_error: нет description: —


### AddRecordEvents (cmd/tap/event_manager.go:201)


AddRecordEvents is a method that creates new data based on the provided parameters and returns (ctx context.Context, evts []*RecordEvt, live bool, dbCallback DBCallback).


```go
func (em *EventManager) AddRecordEvents((ctx context.Context, evts []*RecordEvt, live bool, dbCallback DBCallback)) (ctx context.Context, evts []*RecordEvt, live bool, dbCallback DBCallback)
```


**Тип запроса:** RecordEvt


```json
{
  "Live": false,
  "Did": "string",
  "Rev": "string",
  "Collection": "string",
  "Rkey": "string",
  "Action": "string",
  "Record": {},
  "Cid": "string"
}
```


*Определено в:* `cmd/tap/types.go`


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


**Тип ответа:** evts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RecordEvt


```json
{
  "Live": false,
  "Did": "string",
  "Rev": "string",
  "Collection": "string",
  "Rkey": "string",
  "Action": "string",
  "Record": {},
  "Cid": "string"
}
```


*Определено в:* `cmd/tap/types.go`


**Тип ответа:** live


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbCallback


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DBCallback


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/event_manager.go:201`



---


[function] name: DeleteEvents file: cmd/tap/event_manager.go:78 returns_error: нет description: —


### DeleteEvents (cmd/tap/event_manager.go:78)


DeleteEvents is a method that deletes data based on the provided parameters and returns (ctx context.Context, ids []uint).


```go
func (em *EventManager) DeleteEvents((ctx context.Context, ids []uint)) (ctx context.Context, ids []uint)
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


**Тип ответа:** ids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/event_manager.go:78`



---


[function] name: GetEvent file: cmd/tap/event_manager.go:71 returns_error: нет description: —


### GetEvent (cmd/tap/event_manager.go:71)


GetEvent is a method that retrieves data based on the provided parameters and returns (*OutboxEvt, bool).


```go
func (em *EventManager) GetEvent((*OutboxEvt, bool)) (*OutboxEvt, bool)
```


**Тип запроса:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


**Тип ответа:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


📍 *Расположение:* `cmd/tap/event_manager.go:71`



---


[function] name: IsFull file: cmd/tap/event_manager.go:43 returns_error: нет description: —


### IsFull (cmd/tap/event_manager.go:43)


IsFull is a method that performs operations based on the provided parameters and returns ().


```go
func (em *EventManager) IsFull(()) ()
```


📍 *Расположение:* `cmd/tap/event_manager.go:43`



---


[function] name: IsReady file: cmd/tap/event_manager.go:49 returns_error: нет description: —


### IsReady (cmd/tap/event_manager.go:49)


IsReady is a method that performs operations based on the provided parameters and returns ().


```go
func (em *EventManager) IsReady(()) ()
```


📍 *Расположение:* `cmd/tap/event_manager.go:49`



---


[function] name: LoadEvents file: cmd/tap/event_manager.go:96 returns_error: нет description: —


### LoadEvents (cmd/tap/event_manager.go:96)


LoadEvents is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (em *EventManager) LoadEvents((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/event_manager.go:96`



---


[function] name: NewEventManager file: cmd/tap/event_manager.go:31 returns_error: нет description: —


### NewEventManager (cmd/tap/event_manager.go:31)


NewEventManager is a function that performs operations based on the provided parameters and returns (logger *slog.Logger, db *gorm.DB, config *TapConfig).


```go
func NewEventManager((logger *slog.Logger, db *gorm.DB, config *TapConfig)) (logger *slog.Logger, db *gorm.DB, config *TapConfig)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип запроса:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** db


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


📍 *Расположение:* `cmd/tap/event_manager.go:31`



---


[function] name: WaitForReady file: cmd/tap/event_manager.go:53 returns_error: нет description: —


### WaitForReady (cmd/tap/event_manager.go:53)


WaitForReady is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (em *EventManager) WaitForReady((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/event_manager.go:53`



---


[function] name: addToResyncBuffer file: cmd/tap/event_manager.go:332 returns_error: нет description: —


### addToResyncBuffer (cmd/tap/event_manager.go:332)


addToResyncBuffer is a method that performs operations based on the provided parameters and returns (ctx context.Context, commit *Commit).


```go
func (em *EventManager) addToResyncBuffer((ctx context.Context, commit *Commit)) (ctx context.Context, commit *Commit)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


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


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


📍 *Расположение:* `cmd/tap/event_manager.go:332`



---


[function] name: loadEventPage file: cmd/tap/event_manager.go:123 returns_error: да description: —


### loadEventPage (cmd/tap/event_manager.go:123)


loadEventPage is a method that performs operations based on the provided parameters and may return an error.


```go
func (em *EventManager) loadEventPage((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/event_manager.go:123`



---


[function] name: updateRepoCommitMeta file: cmd/tap/event_manager.go:192 returns_error: нет description: —


### updateRepoCommitMeta (cmd/tap/event_manager.go:192)


updateRepoCommitMeta is a function that performs operations based on the provided parameters and returns (dbOrTx *gorm.DB, commit *Commit).


```go
func updateRepoCommitMeta((dbOrTx *gorm.DB, commit *Commit)) (dbOrTx *gorm.DB, commit *Commit)
```


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** dbOrTx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


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


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


📍 *Расположение:* `cmd/tap/event_manager.go:192`




## cmd/tap/firehose.go


📄 Исходный файл: `cmd/tap/firehose.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [GetCursor](#getcursor-cmdtapfirehosego384) `:384`

- 🔗 [NewFirehoseProcessor](#newfirehoseprocessor-cmdtapfirehosego43) `:43`

- 🔗 [ProcessAccount](#processaccount-cmdtapfirehosego292) `:292`

- 🔗 [ProcessCommit](#processcommit-cmdtapfirehosego71) `:71`

- 🔗 [ProcessIdentity](#processidentity-cmdtapfirehosego265) `:265`

- 🔗 [ProcessSync](#processsync-cmdtapfirehosego210) `:210`

- 🔗 [Run](#run-cmdtapfirehosego63) `:63`

- 🔗 [RunCursorSaver](#runcursorsaver-cmdtapfirehosego370) `:370`

- 🔗 [runConsumer](#runconsumer-cmdtapfirehosego398) `:398`

- 🔗 [saveCursor](#savecursor-cmdtapfirehosego357) `:357`

- 🔗 [updateLastSeq](#updatelastseq-cmdtapfirehosego58) `:58`

- 🔗 [validateCommitAndFilterOps](#validatecommitandfilterops-cmdtapfirehosego140) `:140`


</details>


[function] name: GetCursor file: cmd/tap/firehose.go:384 returns_error: да description: —


### GetCursor (cmd/tap/firehose.go:384)


GetCursor is a method that retrieves data based on the provided parameters and may return an error.


```go
func (fp *FirehoseProcessor) GetCursor((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/firehose.go:384`



---


[function] name: NewFirehoseProcessor file: cmd/tap/firehose.go:43 returns_error: нет description: —


### NewFirehoseProcessor (cmd/tap/firehose.go:43)


NewFirehoseProcessor is a function that performs operations based on the provided parameters and returns (logger *slog.Logger, db *gorm.DB, events *EventManager, repos *RepoManager, config *TapConfig).


```go
func NewFirehoseProcessor((logger *slog.Logger, db *gorm.DB, events *EventManager, repos *RepoManager, config *TapConfig)) (logger *slog.Logger, db *gorm.DB, events *EventManager, repos *RepoManager, config *TapConfig)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип запроса:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип запроса:** RepoManager


```json
{
  "cs": {},
  "kmgr": {},
  "lklk": {},
  "userLocks": {},
  "events": {},
  "hydrateRecords": false,
  "log": null,
  "noArchive": false,
  "clk": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип запроса:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** db


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** events


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** repos


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RepoManager


```json
{
  "cs": {},
  "kmgr": {},
  "lklk": {},
  "userLocks": {},
  "events": {},
  "hydrateRecords": false,
  "log": null,
  "noArchive": false,
  "clk": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


📍 *Расположение:* `cmd/tap/firehose.go:43`



---


[function] name: ProcessAccount file: cmd/tap/firehose.go:292 returns_error: нет description: —


### ProcessAccount (cmd/tap/firehose.go:292)


ProcessAccount is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Account).


```go
func (fp *FirehoseProcessor) ProcessAccount((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Account)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Account)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Account


```json
{
  "active": false,
  "did": "string",
  "seq": 0,
  "status": "string",
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** comatproto.SyncSubscribeRepos_Account


```json
{
  "active": false,
  "did": "string",
  "seq": 0,
  "status": "string",
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `cmd/tap/firehose.go:292`



---


[function] name: ProcessCommit file: cmd/tap/firehose.go:71 returns_error: нет description: ProcessCommit validates and applies a commit event from the firehose.


### ProcessCommit (cmd/tap/firehose.go:71)


ProcessCommit validates and applies a commit event from the firehose.


```go
func (fp *FirehoseProcessor) ProcessCommit((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)
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


📍 *Расположение:* `cmd/tap/firehose.go:71`



---


[function] name: ProcessIdentity file: cmd/tap/firehose.go:265 returns_error: нет description: —


### ProcessIdentity (cmd/tap/firehose.go:265)


ProcessIdentity is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Identity).


```go
func (fp *FirehoseProcessor) ProcessIdentity((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Identity)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Identity)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Identity


```json
{
  "did": "string",
  "handle": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** comatproto.SyncSubscribeRepos_Identity


```json
{
  "did": "string",
  "handle": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `cmd/tap/firehose.go:265`



---


[function] name: ProcessSync file: cmd/tap/firehose.go:210 returns_error: нет description: ProcessSync handles sync events and marks repos for resync if needed.


### ProcessSync (cmd/tap/firehose.go:210)


ProcessSync handles sync events and marks repos for resync if needed.


```go
func (fp *FirehoseProcessor) ProcessSync((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Sync)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Sync)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Sync


```json
{
  "blocks": {},
  "did": "string",
  "rev": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** comatproto.SyncSubscribeRepos_Sync


```json
{
  "blocks": {},
  "did": "string",
  "rev": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `cmd/tap/firehose.go:210`



---


[function] name: Run file: cmd/tap/firehose.go:63 returns_error: нет description: —


### Run (cmd/tap/firehose.go:63)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (fp *FirehoseProcessor) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/firehose.go:63`



---


[function] name: RunCursorSaver file: cmd/tap/firehose.go:370 returns_error: нет description: RunCursorSaver periodically saves the firehose cursor to the database.


### RunCursorSaver (cmd/tap/firehose.go:370)


RunCursorSaver periodically saves the firehose cursor to the database.


```go
func (fp *FirehoseProcessor) RunCursorSaver((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/firehose.go:370`



---


[function] name: runConsumer file: cmd/tap/firehose.go:398 returns_error: нет description: Connects to the firehose and processes events until context cancellation
On error, restarts the connection


### runConsumer (cmd/tap/firehose.go:398)


Connects to the firehose and processes events until context cancellation
On error, restarts the connection


```go
func (fp *FirehoseProcessor) runConsumer((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/firehose.go:398`



---


[function] name: saveCursor file: cmd/tap/firehose.go:357 returns_error: нет description: —


### saveCursor (cmd/tap/firehose.go:357)


saveCursor is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (fp *FirehoseProcessor) saveCursor((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/firehose.go:357`



---


[function] name: updateLastSeq file: cmd/tap/firehose.go:58 returns_error: нет description: —


### updateLastSeq (cmd/tap/firehose.go:58)


updateLastSeq is a method that performs operations based on the provided parameters and returns (seq int64).


```go
func (fp *FirehoseProcessor) updateLastSeq((seq int64)) (seq int64)
```


**Тип ответа:** seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/firehose.go:58`



---


[function] name: validateCommitAndFilterOps file: cmd/tap/firehose.go:140 returns_error: да description: —


### validateCommitAndFilterOps (cmd/tap/firehose.go:140)


validateCommitAndFilterOps is a method that performs operations based on the provided parameters and may return an error.


```go
func (fp *FirehoseProcessor) validateCommitAndFilterOps((*Commit, error)) (*Commit, error)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Commit`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/firehose.go:140`




## cmd/tap/main.go


📄 Исходный файл: `cmd/tap/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [configLogger](#configlogger-cmdtapmaingo289) `:289`

- 🔗 [main](#main-cmdtapmaingo23) `:23`

- 🔗 [run](#run-cmdtapmaingo30) `:30`

- 🔗 [runTap](#runtap-cmdtapmaingo182) `:182`


</details>


[function] name: configLogger file: cmd/tap/main.go:289 returns_error: нет description: —


### configLogger (cmd/tap/main.go:289)


configLogger is a function that performs operations based on the provided parameters and returns (cmd *cli.Command, writer *os.File).


```go
func configLogger((cmd *cli.Command, writer *os.File)) (cmd *cli.Command, writer *os.File)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


📍 *Расположение:* `cmd/tap/main.go:289`



---


[function] name: main file: cmd/tap/main.go:23 returns_error: нет description: —


### main (cmd/tap/main.go:23)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/tap/main.go:23`



---


[function] name: run file: cmd/tap/main.go:30 returns_error: нет description: —


### run (cmd/tap/main.go:30)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/main.go:30`



---


[function] name: runTap file: cmd/tap/main.go:182 returns_error: нет description: —


### runTap (cmd/tap/main.go:182)


runTap is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runTap((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/tap/main.go:182`




## cmd/tap/outbox.go


📄 Исходный файл: `cmd/tap/outbox.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [AckEvent](#ackevent-cmdtapoutboxgo133) `:133`

- 🔗 [NewOutbox](#newoutbox-cmdtapoutboxgo47) `:47`

- 🔗 [Run](#run-cmdtapoutboxgo69) `:69`

- 🔗 [ackEvent](#ackevent-cmdtapoutboxgo337) `:337`

- 🔗 [addEvent](#addevent-cmdtapoutboxgo307) `:307`

- 🔗 [checkTimeouts](#checktimeouts-cmdtapoutboxgo176) `:176`

- 🔗 [deliverEvent](#deliverevent-cmdtapoutboxgo99) `:99`

- 🔗 [processPendingEvts](#processpendingevts-cmdtapoutboxgo255) `:255`

- 🔗 [retryTimedOutEvents](#retrytimedoutevents-cmdtapoutboxgo184) `:184`

- 🔗 [run](#run-cmdtapoutboxgo216) `:216`

- 🔗 [runBatchedDeletes](#runbatcheddeletes-cmdtapoutboxgo146) `:146`

- 🔗 [runDelivery](#rundelivery-cmdtapoutboxgo88) `:88`

- 🔗 [sendEvent](#sendevent-cmdtapoutboxgo122) `:122`

- 🔗 [timedOutEvents](#timedoutevents-cmdtapoutboxgo350) `:350`

- 🔗 [workerFor](#workerfor-cmdtapoutboxgo109) `:109`


</details>


[function] name: AckEvent file: cmd/tap/outbox.go:133 returns_error: нет description: AckEvent marks an event as delivered and queues it for deletion.


### AckEvent (cmd/tap/outbox.go:133)


AckEvent marks an event as delivered and queues it for deletion.


```go
func (o *Outbox) AckEvent((eventID uint)) (eventID uint)
```


**Тип ответа:** eventID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/outbox.go:133`



---


[function] name: NewOutbox file: cmd/tap/outbox.go:47 returns_error: нет description: —


### NewOutbox (cmd/tap/outbox.go:47)


NewOutbox is a function that performs operations based on the provided parameters and returns (logger *slog.Logger, events *EventManager, config *TapConfig).


```go
func NewOutbox((logger *slog.Logger, events *EventManager, config *TapConfig)) (logger *slog.Logger, events *EventManager, config *TapConfig)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип запроса:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** events


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


📍 *Расположение:* `cmd/tap/outbox.go:47`



---


[function] name: Run file: cmd/tap/outbox.go:69 returns_error: нет description: Run starts the outbox workers for event delivery and cleanup.


### Run (cmd/tap/outbox.go:69)


Run starts the outbox workers for event delivery and cleanup.


```go
func (o *Outbox) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/outbox.go:69`



---


[function] name: ackEvent file: cmd/tap/outbox.go:337 returns_error: нет description: —


### ackEvent (cmd/tap/outbox.go:337)


ackEvent is a method that performs operations based on the provided parameters and returns (evtID uint).


```go
func (w *DIDWorker) ackEvent((evtID uint)) (evtID uint)
```


**Тип ответа:** evtID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/outbox.go:337`



---


[function] name: addEvent file: cmd/tap/outbox.go:307 returns_error: нет description: —


### addEvent (cmd/tap/outbox.go:307)


addEvent is a method that performs operations based on the provided parameters and returns (evt *OutboxEvt).


```go
func (w *DIDWorker) addEvent((evt *OutboxEvt)) (evt *OutboxEvt)
```


**Тип запроса:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


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


**Тип ответа:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


📍 *Расположение:* `cmd/tap/outbox.go:307`



---


[function] name: checkTimeouts file: cmd/tap/outbox.go:176 returns_error: нет description: —


### checkTimeouts (cmd/tap/outbox.go:176)


checkTimeouts is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (o *Outbox) checkTimeouts((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/outbox.go:176`



---


[function] name: deliverEvent file: cmd/tap/outbox.go:99 returns_error: нет description: —


### deliverEvent (cmd/tap/outbox.go:99)


deliverEvent is a method that performs operations based on the provided parameters and returns (eventID uint).


```go
func (o *Outbox) deliverEvent((eventID uint)) (eventID uint)
```


**Тип ответа:** eventID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/outbox.go:99`



---


[function] name: processPendingEvts file: cmd/tap/outbox.go:255 returns_error: нет description: get as many pending events in flight as we can
returns when it hits a blocking event


### processPendingEvts (cmd/tap/outbox.go:255)


get as many pending events in flight as we can
returns when it hits a blocking event


```go
func (w *DIDWorker) processPendingEvts(()) ()
```


📍 *Расположение:* `cmd/tap/outbox.go:255`



---


[function] name: retryTimedOutEvents file: cmd/tap/outbox.go:184 returns_error: нет description: retryTimedOutEvents iterates through all workers and re-queues timed out events


### retryTimedOutEvents (cmd/tap/outbox.go:184)


retryTimedOutEvents iterates through all workers and re-queues timed out events


```go
func (o *Outbox) retryTimedOutEvents(()) ()
```


📍 *Расположение:* `cmd/tap/outbox.go:184`



---


[function] name: run file: cmd/tap/outbox.go:216 returns_error: нет description: —


### run (cmd/tap/outbox.go:216)


run is a method that performs operations based on the provided parameters and returns ().


```go
func (w *DIDWorker) run(()) ()
```


📍 *Расположение:* `cmd/tap/outbox.go:216`



---


[function] name: runBatchedDeletes file: cmd/tap/outbox.go:146 returns_error: нет description: —


### runBatchedDeletes (cmd/tap/outbox.go:146)


runBatchedDeletes is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (o *Outbox) runBatchedDeletes((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/outbox.go:146`



---


[function] name: runDelivery file: cmd/tap/outbox.go:88 returns_error: нет description: runDelivery continuously pulls from pendingIDs and delivers events


### runDelivery (cmd/tap/outbox.go:88)


runDelivery continuously pulls from pendingIDs and delivers events


```go
func (o *Outbox) runDelivery((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/outbox.go:88`



---


[function] name: sendEvent file: cmd/tap/outbox.go:122 returns_error: нет description: —


### sendEvent (cmd/tap/outbox.go:122)


sendEvent is a method that performs operations based on the provided parameters and returns (evt *OutboxEvt).


```go
func (o *Outbox) sendEvent((evt *OutboxEvt)) (evt *OutboxEvt)
```


**Тип запроса:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


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


**Тип ответа:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


📍 *Расположение:* `cmd/tap/outbox.go:122`



---


[function] name: timedOutEvents file: cmd/tap/outbox.go:350 returns_error: нет description: checkAndRetryTimeouts checks for timed out events and returns their IDs
Must be called without holding w.mu


### timedOutEvents (cmd/tap/outbox.go:350)


checkAndRetryTimeouts checks for timed out events and returns their IDs
Must be called without holding w.mu


```go
func (w *DIDWorker) timedOutEvents(()) ()
```


📍 *Расположение:* `cmd/tap/outbox.go:350`



---


[function] name: workerFor file: cmd/tap/outbox.go:109 returns_error: нет description: workerFor gets or creates the DIDWorker for the given DID.


### workerFor (cmd/tap/outbox.go:109)


workerFor gets or creates the DIDWorker for the given DID.


```go
func (o *Outbox) workerFor((did string)) (did string)
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


📍 *Расположение:* `cmd/tap/outbox.go:109`




## cmd/tap/repo_manager.go


📄 Исходный файл: `cmd/tap/repo_manager.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [EnsureRepo](#ensurerepo-cmdtaprepo_managergo90) `:90`

- 🔗 [GetRepoState](#getrepostate-cmdtaprepo_managergo29) `:29`

- 🔗 [NewRepoManager](#newrepomanager-cmdtaprepo_managergo20) `:20`

- 🔗 [RefreshIdentity](#refreshidentity-cmdtaprepo_managergo47) `:47`

- 🔗 [UpdateRepoState](#updaterepostate-cmdtaprepo_managergo40) `:40`


</details>


[function] name: EnsureRepo file: cmd/tap/repo_manager.go:90 returns_error: нет description: —


### EnsureRepo (cmd/tap/repo_manager.go:90)


EnsureRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, did string).


```go
func (rm *RepoManager) EnsureRepo((ctx context.Context, did string)) (ctx context.Context, did string)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `cmd/tap/repo_manager.go:90`



---


[function] name: GetRepoState file: cmd/tap/repo_manager.go:29 returns_error: да description: —


### GetRepoState (cmd/tap/repo_manager.go:29)


GetRepoState is a method that retrieves data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) GetRepoState((*models.Repo, error)) (*models.Repo, error)
```


**Тип запроса:** models.Repo


```json
{
  "sc": {},
  "cst": {},
  "bs": {},
  "repoCid": {},
  "mst": null,
  "dirty": false,
  "clk": null
}
```


*Определено в:* `repo/repo.go`


**Тип ответа:** models.Repo


```json
{
  "sc": {},
  "cst": {},
  "bs": {},
  "repoCid": {},
  "mst": null,
  "dirty": false,
  "clk": null
}
```


*Определено в:* `repo/repo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.Repo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/repo_manager.go:29`



---


[function] name: NewRepoManager file: cmd/tap/repo_manager.go:20 returns_error: нет description: —


### NewRepoManager (cmd/tap/repo_manager.go:20)


NewRepoManager is a function that performs operations based on the provided parameters and returns (logger *slog.Logger, db *gorm.DB, events *EventManager, idDir identity.Directory).


```go
func NewRepoManager((logger *slog.Logger, db *gorm.DB, events *EventManager, idDir identity.Directory)) (logger *slog.Logger, db *gorm.DB, events *EventManager, idDir identity.Directory)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип запроса:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** db


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** events


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** idDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** identity.Directory


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


📍 *Расположение:* `cmd/tap/repo_manager.go:20`



---


[function] name: RefreshIdentity file: cmd/tap/repo_manager.go:47 returns_error: нет description: RefreshIdentity fetches the latest identity information for a DID.


### RefreshIdentity (cmd/tap/repo_manager.go:47)


RefreshIdentity fetches the latest identity information for a DID.


```go
func (rm *RepoManager) RefreshIdentity((ctx context.Context, did string)) (ctx context.Context, did string)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `cmd/tap/repo_manager.go:47`



---


[function] name: UpdateRepoState file: cmd/tap/repo_manager.go:40 returns_error: нет description: —


### UpdateRepoState (cmd/tap/repo_manager.go:40)


UpdateRepoState is a method that updates data based on the provided parameters and returns (ctx context.Context, did string, state models.RepoState).


```go
func (rm *RepoManager) UpdateRepoState((ctx context.Context, did string, state models.RepoState)) (ctx context.Context, did string, state models.RepoState)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.RepoState


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


📍 *Расположение:* `cmd/tap/repo_manager.go:40`




## cmd/tap/resyncer.go


📄 Исходный файл: `cmd/tap/resyncer.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [NewResyncer](#newresyncer-cmdtapresyncergo41) `:41`

- 🔗 [claimResyncJob](#claimresyncjob-cmdtapresyncergo97) `:97`

- 🔗 [claimResyncJobOfState](#claimresyncjobofstate-cmdtapresyncergo115) `:115`

- 🔗 [doResync](#doresync-cmdtapresyncergo172) `:172`

- 🔗 [drainResyncBuffer](#drainresyncbuffer-cmdtapresyncergo389) `:389`

- 🔗 [handleResyncError](#handleresyncerror-cmdtapresyncergo350) `:350`

- 🔗 [resetPartiallyResynced](#resetpartiallyresynced-cmdtapresyncergo383) `:383`

- 🔗 [resyncDid](#resyncdid-cmdtapresyncergo138) `:138`

- 🔗 [run](#run-cmdtapresyncergo54) `:54`

- 🔗 [runResyncWorker](#runresyncworker-cmdtapresyncergo60) `:60`


</details>


[function] name: NewResyncer file: cmd/tap/resyncer.go:41 returns_error: нет description: —


### NewResyncer (cmd/tap/resyncer.go:41)


NewResyncer is a function that performs operations based on the provided parameters and returns (logger *slog.Logger, db *gorm.DB, repos *RepoManager, events *EventManager, config *TapConfig).


```go
func NewResyncer((logger *slog.Logger, db *gorm.DB, repos *RepoManager, events *EventManager, config *TapConfig)) (logger *slog.Logger, db *gorm.DB, repos *RepoManager, events *EventManager, config *TapConfig)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип запроса:** RepoManager


```json
{
  "cs": {},
  "kmgr": {},
  "lklk": {},
  "userLocks": {},
  "events": {},
  "hydrateRecords": false,
  "log": null,
  "noArchive": false,
  "clk": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип запроса:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип запроса:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** db


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** repos


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RepoManager


```json
{
  "cs": {},
  "kmgr": {},
  "lklk": {},
  "userLocks": {},
  "events": {},
  "hydrateRecords": false,
  "log": null,
  "noArchive": false,
  "clk": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип ответа:** events


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** EventManager


```json
{
  "subs": [],
  "subsLk": {},
  "bufferSize": 0,
  "crossoverBufferSize": 0,
  "persister": {},
  "log": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


📍 *Расположение:* `cmd/tap/resyncer.go:41`



---


[function] name: claimResyncJob file: cmd/tap/resyncer.go:97 returns_error: да description: —


### claimResyncJob (cmd/tap/resyncer.go:97)


claimResyncJob is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Resyncer) claimResyncJob((string, bool, error)) (string, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/resyncer.go:97`



---


[function] name: claimResyncJobOfState file: cmd/tap/resyncer.go:115 returns_error: да description: —


### claimResyncJobOfState (cmd/tap/resyncer.go:115)


claimResyncJobOfState is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Resyncer) claimResyncJobOfState((string, bool, error)) (string, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/resyncer.go:115`



---


[function] name: doResync file: cmd/tap/resyncer.go:172 returns_error: да description: —


### doResync (cmd/tap/resyncer.go:172)


doResync is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Resyncer) doResync((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/resyncer.go:172`



---


[function] name: drainResyncBuffer file: cmd/tap/resyncer.go:389 returns_error: нет description: —


### drainResyncBuffer (cmd/tap/resyncer.go:389)


drainResyncBuffer is a method that performs operations based on the provided parameters and returns (ctx context.Context, did string).


```go
func (r *Resyncer) drainResyncBuffer((ctx context.Context, did string)) (ctx context.Context, did string)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `cmd/tap/resyncer.go:389`



---


[function] name: handleResyncError file: cmd/tap/resyncer.go:350 returns_error: да description: —


### handleResyncError (cmd/tap/resyncer.go:350)


handleResyncError is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Resyncer) handleResyncError((ctx context.Context, did string, resyncErr error)) (ctx context.Context, did string, resyncErr error)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** resyncErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `did string`, `resyncErr error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/resyncer.go:350`



---


[function] name: resetPartiallyResynced file: cmd/tap/resyncer.go:383 returns_error: нет description: —


### resetPartiallyResynced (cmd/tap/resyncer.go:383)


resetPartiallyResynced is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (r *Resyncer) resetPartiallyResynced((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/resyncer.go:383`



---


[function] name: resyncDid file: cmd/tap/resyncer.go:138 returns_error: нет description: —


### resyncDid (cmd/tap/resyncer.go:138)


resyncDid is a method that performs operations based on the provided parameters and returns (ctx context.Context, did string).


```go
func (r *Resyncer) resyncDid((ctx context.Context, did string)) (ctx context.Context, did string)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `cmd/tap/resyncer.go:138`



---


[function] name: run file: cmd/tap/resyncer.go:54 returns_error: нет description: —


### run (cmd/tap/resyncer.go:54)


run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (r *Resyncer) run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/resyncer.go:54`



---


[function] name: runResyncWorker file: cmd/tap/resyncer.go:60 returns_error: нет description: —


### runResyncWorker (cmd/tap/resyncer.go:60)


runResyncWorker is a method that performs operations based on the provided parameters and returns (ctx context.Context, workerID int).


```go
func (r *Resyncer) runResyncWorker((ctx context.Context, workerID int)) (ctx context.Context, workerID int)
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


**Тип ответа:** workerID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/resyncer.go:60`




## cmd/tap/server.go


📄 Исходный файл: `cmd/tap/server.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [NewTapServer](#newtapserver-cmdtapservergo30) `:30`

- 🔗 [Shutdown](#shutdown-cmdtapservergo70) `:70`

- 🔗 [Start](#start-cmdtapservergo42) `:42`

- 🔗 [handleAddRepos](#handleaddrepos-cmdtapservergo142) `:142`

- 🔗 [handleChannelWebsocket](#handlechannelwebsocket-cmdtapservergo86) `:86`

- 🔗 [handleHealthcheck](#handlehealthcheck-cmdtapservergo74) `:74`

- 🔗 [handleInfoRepo](#handleinforepo-cmdtapservergo208) `:208`

- 🔗 [handleRemoveRepos](#handleremoverepos-cmdtapservergo168) `:168`

- 🔗 [handleResolveDID](#handleresolvedid-cmdtapservergo189) `:189`

- 🔗 [handleStatsCursors](#handlestatscursors-cmdtapservergo275) `:275`

- 🔗 [handleStatsOutboxBuffer](#handlestatsoutboxbuffer-cmdtapservergo252) `:252`

- 🔗 [handleStatsRecordCount](#handlestatsrecordcount-cmdtapservergo243) `:243`

- 🔗 [handleStatsRepoCount](#handlestatsrepocount-cmdtapservergo234) `:234`

- 🔗 [handleStatsResyncBuffer](#handlestatsresyncbuffer-cmdtapservergo261) `:261`


</details>


[function] name: NewTapServer file: cmd/tap/server.go:30 returns_error: нет description: —


### NewTapServer (cmd/tap/server.go:30)


NewTapServer is a function that performs operations based on the provided parameters and returns (logger *slog.Logger, db *gorm.DB, outbox *Outbox, idDir identity.Directory, firehose *FirehoseProcessor, crawler *Crawler, config *TapConfig).


```go
func NewTapServer((logger *slog.Logger, db *gorm.DB, outbox *Outbox, idDir identity.Directory, firehose *FirehoseProcessor, crawler *Crawler, config *TapConfig)) (logger *slog.Logger, db *gorm.DB, outbox *Outbox, idDir identity.Directory, firehose *FirehoseProcessor, crawler *Crawler, config *TapConfig)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип запроса:** Outbox


```json
{
  "logger": null,
  "mode": {},
  "parallelism": 0,
  "retryTimeout": {},
  "webhook": null,
  "events": null,
  "didWorkers": null,
  "acks": {},
  "outgoing": {},
  "ctx": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


**Тип запроса:** FirehoseProcessor


```json
{
  "logger": null,
  "db": null,
  "events": null,
  "repos": null,
  "relayUrl": "string",
  "fullNetworkMode": false,
  "signalCollection": "string",
  "collectionFilters": [],
  "parallelism": 0,
  "cursorSaveInterval": {},
  "lastSeq": {}
}
```


*Определено в:* `cmd/tap/firehose.go`


**Тип запроса:** Crawler


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


**Тип запроса:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** db


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** outbox


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Outbox


```json
{
  "logger": null,
  "mode": {},
  "parallelism": 0,
  "retryTimeout": {},
  "webhook": null,
  "events": null,
  "didWorkers": null,
  "acks": {},
  "outgoing": {},
  "ctx": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


**Тип ответа:** idDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** identity.Directory


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


**Тип ответа:** firehose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FirehoseProcessor


```json
{
  "logger": null,
  "db": null,
  "events": null,
  "repos": null,
  "relayUrl": "string",
  "fullNetworkMode": false,
  "signalCollection": "string",
  "collectionFilters": [],
  "parallelism": 0,
  "cursorSaveInterval": {},
  "lastSeq": {}
}
```


*Определено в:* `cmd/tap/firehose.go`


**Тип ответа:** crawler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Crawler


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


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TapConfig


```json
{
  "DatabaseURL": "string",
  "DBMaxConns": 0,
  "PLCURL": "string",
  "RelayUrl": "string",
  "FirehoseParallelism": 0,
  "ResyncParallelism": 0,
  "OutboxParallelism": 0,
  "FirehoseCursorSaveInterval": {},
  "RepoFetchTimeout": {},
  "IdentityCacheSize": 0,
  "EventCacheSize": 0,
  "FullNetworkMode": false,
  "SignalCollection": "string",
  "DisableAcks": false,
  "WebhookURL": "string",
  "CollectionFilters": [],
  "OutboxOnly": false,
  "AdminPassword": "string",
  "RetryTimeout": {}
}
```


*Определено в:* `cmd/tap/tap.go`


📍 *Расположение:* `cmd/tap/server.go:30`



---


[function] name: Shutdown file: cmd/tap/server.go:70 returns_error: нет description: Shutdown gracefully shuts down the HTTP server.


### Shutdown (cmd/tap/server.go:70)


Shutdown gracefully shuts down the HTTP server.


```go
func (ts *TapServer) Shutdown((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/server.go:70`



---


[function] name: Start file: cmd/tap/server.go:42 returns_error: нет description: —


### Start (cmd/tap/server.go:42)


Start is a method that performs operations based on the provided parameters and returns (address string).


```go
func (ts *TapServer) Start((address string)) (address string)
```


**Тип ответа:** address


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/server.go:42`



---


[function] name: handleAddRepos file: cmd/tap/server.go:142 returns_error: нет description: —


### handleAddRepos (cmd/tap/server.go:142)


handleAddRepos is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleAddRepos((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:142`



---


[function] name: handleChannelWebsocket file: cmd/tap/server.go:86 returns_error: нет description: —


### handleChannelWebsocket (cmd/tap/server.go:86)


handleChannelWebsocket is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleChannelWebsocket((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:86`



---


[function] name: handleHealthcheck file: cmd/tap/server.go:74 returns_error: нет description: —


### handleHealthcheck (cmd/tap/server.go:74)


handleHealthcheck is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleHealthcheck((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:74`



---


[function] name: handleInfoRepo file: cmd/tap/server.go:208 returns_error: нет description: —


### handleInfoRepo (cmd/tap/server.go:208)


handleInfoRepo is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleInfoRepo((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:208`



---


[function] name: handleRemoveRepos file: cmd/tap/server.go:168 returns_error: нет description: —


### handleRemoveRepos (cmd/tap/server.go:168)


handleRemoveRepos is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleRemoveRepos((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:168`



---


[function] name: handleResolveDID file: cmd/tap/server.go:189 returns_error: нет description: —


### handleResolveDID (cmd/tap/server.go:189)


handleResolveDID is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleResolveDID((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:189`



---


[function] name: handleStatsCursors file: cmd/tap/server.go:275 returns_error: нет description: —


### handleStatsCursors (cmd/tap/server.go:275)


handleStatsCursors is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleStatsCursors((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:275`



---


[function] name: handleStatsOutboxBuffer file: cmd/tap/server.go:252 returns_error: нет description: —


### handleStatsOutboxBuffer (cmd/tap/server.go:252)


handleStatsOutboxBuffer is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleStatsOutboxBuffer((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:252`



---


[function] name: handleStatsRecordCount file: cmd/tap/server.go:243 returns_error: нет description: —


### handleStatsRecordCount (cmd/tap/server.go:243)


handleStatsRecordCount is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleStatsRecordCount((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:243`



---


[function] name: handleStatsRepoCount file: cmd/tap/server.go:234 returns_error: нет description: —


### handleStatsRepoCount (cmd/tap/server.go:234)


handleStatsRepoCount is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleStatsRepoCount((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:234`



---


[function] name: handleStatsResyncBuffer file: cmd/tap/server.go:261 returns_error: нет description: —


### handleStatsResyncBuffer (cmd/tap/server.go:261)


handleStatsResyncBuffer is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (ts *TapServer) handleStatsResyncBuffer((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/tap/server.go:261`




## cmd/tap/tap.go


📄 Исходный файл: `cmd/tap/tap.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [CloseDb](#closedb-cmdtaptapgo117) `:117`

- 🔗 [NewTap](#newtap-cmdtaptapgo56) `:56`

- 🔗 [Run](#run-cmdtaptapgo107) `:107`

- 🔗 [SetupDatabase](#setupdatabase-cmdtaptapgo134) `:134`


</details>


[function] name: CloseDb file: cmd/tap/tap.go:117 returns_error: нет description: —


### CloseDb (cmd/tap/tap.go:117)


CloseDb is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (t *Tap) CloseDb((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/tap.go:117`



---


[function] name: NewTap file: cmd/tap/tap.go:56 returns_error: да description: —


### NewTap (cmd/tap/tap.go:56)


NewTap is a function that performs operations based on the provided parameters and may return an error.


```go
func NewTap((*Tap, error)) (*Tap, error)
```


**Тип запроса:** Tap


```json
{
  "db": null,
  "logger": null,
  "firehose": null,
  "events": null,
  "repos": null,
  "resyncer": null,
  "crawler": null,
  "server": null,
  "outbox": null,
  "outboxOnly": false
}
```


*Определено в:* `cmd/tap/tap.go`


**Тип ответа:** Tap


```json
{
  "db": null,
  "logger": null,
  "firehose": null,
  "events": null,
  "repos": null,
  "resyncer": null,
  "crawler": null,
  "server": null,
  "outbox": null,
  "outboxOnly": false
}
```


*Определено в:* `cmd/tap/tap.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Tap`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/tap.go:56`



---


[function] name: Run file: cmd/tap/tap.go:107 returns_error: нет description: Run starts internal background workers for resync, cursor saving, and outbox delivery.


### Run (cmd/tap/tap.go:107)


Run starts internal background workers for resync, cursor saving, and outbox delivery.


```go
func (t *Tap) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/tap/tap.go:107`



---


[function] name: SetupDatabase file: cmd/tap/tap.go:134 returns_error: да description: —


### SetupDatabase (cmd/tap/tap.go:134)


SetupDatabase is a function that updates data based on the provided parameters and may return an error.


```go
func SetupDatabase((*gorm.DB, error)) (*gorm.DB, error)
```


**Тип запроса:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** gorm.DB


```json
{
  "Repo": "string",
  "State": "string",
  "Rev": "string",
  "RetryCount": 0,
  "RetryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*gorm.DB`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/tap.go:134`




## cmd/tap/types.go


📄 Исходный файл: `cmd/tap/types.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarshalWithId](#marshalwithid-cmdtaptypesgo44) `:44`

- 🔗 [MarshalWithId](#marshalwithid-cmdtaptypesgo59) `:59`


</details>


[function] name: MarshalWithId file: cmd/tap/types.go:44 returns_error: да description: —


### MarshalWithId (cmd/tap/types.go:44)


MarshalWithId is a method that performs operations based on the provided parameters and may return an error.


```go
func (e *RecordEvt) MarshalWithId(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/types.go:44`



---


[function] name: MarshalWithId file: cmd/tap/types.go:59 returns_error: да description: —


### MarshalWithId (cmd/tap/types.go:59)


MarshalWithId is a method that performs operations based on the provided parameters and may return an error.


```go
func (e *IdentityEvt) MarshalWithId(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/types.go:59`




## cmd/tap/util.go


📄 Исходный файл: `cmd/tap/util.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [backoff](#backoff-cmdtaputilgo24) `:24`

- 🔗 [evtHasSignalCollection](#evthassignalcollection-cmdtaputilgo54) `:54`

- 🔗 [isRateLimitError](#isratelimiterror-cmdtaputilgo67) `:67`

- 🔗 [matchesCollection](#matchescollection-cmdtaputilgo37) `:37`

- 🔗 [parseOutboxMode](#parseoutboxmode-cmdtaputilgo75) `:75`

- 🔗 [runPeriodically](#runperiodically-cmdtaputilgo86) `:86`

- 🔗 [userAgent](#useragent-cmdtaputilgo20) `:20`


</details>


[function] name: backoff file: cmd/tap/util.go:24 returns_error: нет description: —


### backoff (cmd/tap/util.go:24)


backoff is a function that performs operations based on the provided parameters and returns (retries int, max int).


```go
func backoff((retries int, max int)) (retries int, max int)
```


**Тип ответа:** retries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** max


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/util.go:24`



---


[function] name: evtHasSignalCollection file: cmd/tap/util.go:54 returns_error: нет description: —


### evtHasSignalCollection (cmd/tap/util.go:54)


evtHasSignalCollection is a function that performs operations based on the provided parameters and returns (evt *comatproto.SyncSubscribeRepos_Commit, signalColl string).


```go
func evtHasSignalCollection((evt *comatproto.SyncSubscribeRepos_Commit, signalColl string)) (evt *comatproto.SyncSubscribeRepos_Commit, signalColl string)
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


**Тип ответа:** signalColl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/util.go:54`



---


[function] name: isRateLimitError file: cmd/tap/util.go:67 returns_error: да description: —


### isRateLimitError (cmd/tap/util.go:67)


isRateLimitError is a function that performs operations based on the provided parameters and may return an error.


```go
func isRateLimitError((err error)) (err error)
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


📍 *Расположение:* `cmd/tap/util.go:67`



---


[function] name: matchesCollection file: cmd/tap/util.go:37 returns_error: нет description: matchesCollection checks if a collection matches any of the provided filters.
Filters support wildcards at the end (e.g.


### matchesCollection (cmd/tap/util.go:37)


matchesCollection checks if a collection matches any of the provided filters.
Filters support wildcards at the end (e.g., "app.bsky.*" & "app.bsky.feed.*" both match "app.bsky.feed.post").
If no filters are provided, all collections match.


```go
func matchesCollection((collection string, filters []string)) (collection string, filters []string)
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


**Тип ответа:** filters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/util.go:37`



---


[function] name: parseOutboxMode file: cmd/tap/util.go:75 returns_error: нет description: —


### parseOutboxMode (cmd/tap/util.go:75)


parseOutboxMode is a function that performs operations based on the provided parameters and returns (webhookURL string, disableAcks bool).


```go
func parseOutboxMode((webhookURL string, disableAcks bool)) (webhookURL string, disableAcks bool)
```


**Тип ответа:** webhookURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** disableAcks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/util.go:75`



---


[function] name: runPeriodically file: cmd/tap/util.go:86 returns_error: да description: runPeriodically runs the provided task function at the specified interval until the context is done or an error occurs.


### runPeriodically (cmd/tap/util.go:86)


runPeriodically runs the provided task function at the specified interval until the context is done or an error occurs.


```go
func runPeriodically((ctx context.Context, interval time.Duration, task func(context.Context) error)) (ctx context.Context, interval time.Duration, task func(context.Context) error)
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


**Тип ответа:** interval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** task


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


*Типы возврата:* `ctx context.Context`, `interval time.Duration`, `task func(context.Context) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/tap/util.go:86`



---


[function] name: userAgent file: cmd/tap/util.go:20 returns_error: нет description: —


### userAgent (cmd/tap/util.go:20)


userAgent is a function that performs operations based on the provided parameters and returns ().


```go
func userAgent(()) ()
```


📍 *Расположение:* `cmd/tap/util.go:20`




## cmd/tap/webhook_client.go


📄 Исходный файл: `cmd/tap/webhook_client.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Send](#send-cmdtapwebhook_clientgo18) `:18`

- 🔗 [post](#post-cmdtapwebhook_clientgo33) `:33`


</details>


[function] name: Send file: cmd/tap/webhook_client.go:18 returns_error: нет description: —


### Send (cmd/tap/webhook_client.go:18)


Send is a method that performs operations based on the provided parameters and returns (evt *OutboxEvt, ackFn func(uint)).


```go
func (w *WebhookClient) Send((evt *OutboxEvt, ackFn func(uint))) (evt *OutboxEvt, ackFn func(uint))
```


**Тип запроса:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


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


**Тип ответа:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


**Тип ответа:** ackFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/tap/webhook_client.go:18`



---


[function] name: post file: cmd/tap/webhook_client.go:33 returns_error: нет description: —


### post (cmd/tap/webhook_client.go:33)


post is a method that performs operations based on the provided parameters and returns (evt *OutboxEvt).


```go
func (w *WebhookClient) post((evt *OutboxEvt)) (evt *OutboxEvt)
```


**Тип запроса:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


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


**Тип ответа:** OutboxEvt


```json
{
  "ID": 0,
  "Did": "string",
  "Live": false,
  "Event": []
}
```


*Определено в:* `cmd/tap/types.go`


📍 *Расположение:* `cmd/tap/webhook_client.go:33`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_stress.md)

- [Следующая директория](events.md)


---

