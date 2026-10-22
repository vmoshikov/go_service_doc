---
title: "Функции: search"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: search
---


# Функции: search


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repomgr_keymgr.md)

- [Следующая директория](splitter.md)


---


## Меню по файлам


- 📄 [search/bulk.go](#searchbulkgo)

- 📄 [search/firehose.go](#searchfirehosego)

- 📄 [search/handlers.go](#searchhandlersgo)

- 📄 [search/indexing.go](#searchindexinggo)

- 📄 [search/japanese.go](#searchjapanesego)

- 📄 [search/metrics.go](#searchmetricsgo)

- 📄 [search/parse_query.go](#searchparse_querygo)

- 📄 [search/query.go](#searchquerygo)

- 📄 [search/server.go](#searchservergo)

- 📄 [search/transform.go](#searchtransformgo)

- 📄 [search/url.go](#searchurlgo)


---


## search/bulk.go


📄 Исходный файл: `search/bulk.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [BulkIndexPageranks](#bulkindexpageranks-searchbulkgo27) `:27`

- 🔗 [BulkIndexPosts](#bulkindexposts-searchbulkgo90) `:90`

- 🔗 [BulkIndexProfiles](#bulkindexprofiles-searchbulkgo153) `:153`

- 🔗 [processPagerankCSVLine](#processpagerankcsvline-searchbulkgo214) `:214`

- 🔗 [processPostCSVLine](#processpostcsvline-searchbulkgo242) `:242`

- 🔗 [processProfileCSVLine](#processprofilecsvline-searchbulkgo306) `:306`


</details>


[function] name: BulkIndexPageranks file: search/bulk.go:27 returns_error: нет description: BulkIndexPageranks updates the pageranks for the DIDs in the Search Index from a CSV file.


### BulkIndexPageranks (search/bulk.go:27)


BulkIndexPageranks updates the pageranks for the DIDs in the Search Index from a CSV file.


```go
func (idx *Indexer) BulkIndexPageranks((ctx context.Context, pagerankFile string)) (ctx context.Context, pagerankFile string)
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


**Тип ответа:** pagerankFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/bulk.go:27`



---


[function] name: BulkIndexPosts file: search/bulk.go:90 returns_error: нет description: BulkIndexPosts indexes posts from a CSV file.


### BulkIndexPosts (search/bulk.go:90)


BulkIndexPosts indexes posts from a CSV file.


```go
func (idx *Indexer) BulkIndexPosts((ctx context.Context, postsFile string)) (ctx context.Context, postsFile string)
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


**Тип ответа:** postsFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/bulk.go:90`



---


[function] name: BulkIndexProfiles file: search/bulk.go:153 returns_error: нет description: BulkIndexProfiles indexes profiles from a CSV file.


### BulkIndexProfiles (search/bulk.go:153)


BulkIndexProfiles indexes profiles from a CSV file.


```go
func (idx *Indexer) BulkIndexProfiles((ctx context.Context, profilesFile string)) (ctx context.Context, profilesFile string)
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


**Тип ответа:** profilesFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/bulk.go:153`



---


[function] name: processPagerankCSVLine file: search/bulk.go:214 returns_error: нет description: —


### processPagerankCSVLine (search/bulk.go:214)


processPagerankCSVLine is a method that performs operations based on the provided parameters and returns (line string).


```go
func (idx *Indexer) processPagerankCSVLine((line string)) (line string)
```


**Тип ответа:** line


```json
{
  "timeline": []
}
```


*Определено в:* `api/ozone/moderationgetAccountTimeline.go`


📍 *Расположение:* `search/bulk.go:214`



---


[function] name: processPostCSVLine file: search/bulk.go:242 returns_error: нет description: —


### processPostCSVLine (search/bulk.go:242)


processPostCSVLine is a method that performs operations based on the provided parameters and returns (line string).


```go
func (idx *Indexer) processPostCSVLine((line string)) (line string)
```


**Тип ответа:** line


```json
{
  "timeline": []
}
```


*Определено в:* `api/ozone/moderationgetAccountTimeline.go`


📍 *Расположение:* `search/bulk.go:242`



---


[function] name: processProfileCSVLine file: search/bulk.go:306 returns_error: нет description: —


### processProfileCSVLine (search/bulk.go:306)


processProfileCSVLine is a method that performs operations based on the provided parameters and returns (line string).


```go
func (idx *Indexer) processProfileCSVLine((line string)) (line string)
```


**Тип ответа:** line


```json
{
  "timeline": []
}
```


*Определено в:* `api/ozone/moderationgetAccountTimeline.go`


📍 *Расположение:* `search/bulk.go:306`




## search/firehose.go


📄 Исходный файл: `search/firehose.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [RunIndexer](#runindexer-searchfirehosego44) `:44`

- 🔗 [discoverRepos](#discoverrepos-searchfirehosego152) `:152`

- 🔗 [getLastCursor](#getlastcursor-searchfirehosego27) `:27`

- 🔗 [handleCreateOrUpdate](#handlecreateorupdate-searchfirehosego192) `:192`

- 🔗 [handleDelete](#handledelete-searchfirehosego266) `:266`

- 🔗 [processTooBigCommit](#processtoobigcommit-searchfirehosego291) `:291`

- 🔗 [updateLastCursor](#updatelastcursor-searchfirehosego40) `:40`


</details>


[function] name: RunIndexer file: search/firehose.go:44 returns_error: нет description: —


### RunIndexer (search/firehose.go:44)


RunIndexer is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (idx *Indexer) RunIndexer((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `search/firehose.go:44`



---


[function] name: discoverRepos file: search/firehose.go:152 returns_error: нет description: —


### discoverRepos (search/firehose.go:152)


discoverRepos is a method that performs operations based on the provided parameters and returns ().


```go
func (idx *Indexer) discoverRepos(()) ()
```


📍 *Расположение:* `search/firehose.go:152`



---


[function] name: getLastCursor file: search/firehose.go:27 returns_error: да description: —


### getLastCursor (search/firehose.go:27)


getLastCursor is a method that performs operations based on the provided parameters and may return an error.


```go
func (idx *Indexer) getLastCursor((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/firehose.go:27`



---


[function] name: handleCreateOrUpdate file: search/firehose.go:192 returns_error: нет description: —


### handleCreateOrUpdate (search/firehose.go:192)


handleCreateOrUpdate is a method that performs operations based on the provided parameters and returns (ctx context.Context, rawDID string, rev string, path string, recB *[]byte, rcid *cid.Cid).


```go
func (idx *Indexer) handleCreateOrUpdate((ctx context.Context, rawDID string, rev string, path string, recB *[]byte, rcid *cid.Cid)) (ctx context.Context, rawDID string, rev string, path string, recB *[]byte, rcid *cid.Cid)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


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


**Тип ответа:** rawDID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** recB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rcid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `search/firehose.go:192`



---


[function] name: handleDelete file: search/firehose.go:266 returns_error: нет description: —


### handleDelete (search/firehose.go:266)


handleDelete is a method that performs operations based on the provided parameters and returns (ctx context.Context, rawDID, rev, path string).


```go
func (idx *Indexer) handleDelete((ctx context.Context, rawDID, rev, path string)) (ctx context.Context, rawDID, rev, path string)
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


**Тип ответа:** rawDID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/firehose.go:266`



---


[function] name: processTooBigCommit file: search/firehose.go:291 returns_error: нет description: —


### processTooBigCommit (search/firehose.go:291)


processTooBigCommit is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit).


```go
func (idx *Indexer) processTooBigCommit((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)
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


📍 *Расположение:* `search/firehose.go:291`



---


[function] name: updateLastCursor file: search/firehose.go:40 returns_error: нет description: —


### updateLastCursor (search/firehose.go:40)


updateLastCursor is a method that performs operations based on the provided parameters and returns (curs int64).


```go
func (idx *Indexer) updateLastCursor((curs int64)) (curs int64)
```


**Тип ответа:** curs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/firehose.go:40`




## search/handlers.go


📄 Исходный файл: `search/handlers.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [SearchPosts](#searchposts-searchhandlersgo281) `:281`

- 🔗 [SearchProfiles](#searchprofiles-searchhandlersgo319) `:319`

- 🔗 [handleSearchActorsSkeleton](#handlesearchactorsskeleton-searchhandlersgo218) `:218`

- 🔗 [handleSearchPostsSkeleton](#handlesearchpostsskeleton-searchhandlersgo68) `:68`

- 🔗 [parseCursorLimit](#parsecursorlimit-searchhandlersgo23) `:23`


</details>


[function] name: SearchPosts file: search/handlers.go:281 returns_error: да description: —


### SearchPosts (search/handlers.go:281)


SearchPosts is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Server) SearchPosts((*appbsky.UnspeccedSearchPostsSkeleton_Output, error)) (*appbsky.UnspeccedSearchPostsSkeleton_Output, error)
```


**Тип запроса:** appbsky.UnspeccedSearchPostsSkeleton_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "posts": []
}
```


*Определено в:* `api/bsky/unspeccedsearchPostsSkeleton.go`


**Тип ответа:** appbsky.UnspeccedSearchPostsSkeleton_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "posts": []
}
```


*Определено в:* `api/bsky/unspeccedsearchPostsSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*appbsky.UnspeccedSearchPostsSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/handlers.go:281`



---


[function] name: SearchProfiles file: search/handlers.go:319 returns_error: да description: —


### SearchProfiles (search/handlers.go:319)


SearchProfiles is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Server) SearchProfiles((*appbsky.UnspeccedSearchActorsSkeleton_Output, error)) (*appbsky.UnspeccedSearchActorsSkeleton_Output, error)
```


**Тип запроса:** appbsky.UnspeccedSearchActorsSkeleton_Output


```json
{
  "actors": [],
  "cursor": "string",
  "hitsTotal": 0
}
```


*Определено в:* `api/bsky/unspeccedsearchActorsSkeleton.go`


**Тип ответа:** appbsky.UnspeccedSearchActorsSkeleton_Output


```json
{
  "actors": [],
  "cursor": "string",
  "hitsTotal": 0
}
```


*Определено в:* `api/bsky/unspeccedsearchActorsSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*appbsky.UnspeccedSearchActorsSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/handlers.go:319`



---


[function] name: handleSearchActorsSkeleton file: search/handlers.go:218 returns_error: нет description: —


### handleSearchActorsSkeleton (search/handlers.go:218)


handleSearchActorsSkeleton is a method that performs operations based on the provided parameters and returns (e echo.Context).


```go
func (s *Server) handleSearchActorsSkeleton((e echo.Context)) (e echo.Context)
```


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
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


📍 *Расположение:* `search/handlers.go:218`



---


[function] name: handleSearchPostsSkeleton file: search/handlers.go:68 returns_error: нет description: —


### handleSearchPostsSkeleton (search/handlers.go:68)


handleSearchPostsSkeleton is a method that performs operations based on the provided parameters and returns (e echo.Context).


```go
func (s *Server) handleSearchPostsSkeleton((e echo.Context)) (e echo.Context)
```


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
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


📍 *Расположение:* `search/handlers.go:68`



---


[function] name: parseCursorLimit file: search/handlers.go:23 returns_error: да description: —


### parseCursorLimit (search/handlers.go:23)


parseCursorLimit is a function that performs operations based on the provided parameters and may return an error.


```go
func parseCursorLimit((int, int, error)) (int, int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/handlers.go:23`




## search/indexing.go


📄 Исходный файл: `search/indexing.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [EnsureIndices](#ensureindices-searchindexinggo163) `:163`

- 🔗 [NewIndexer](#newindexer-searchindexinggo81) `:81`

- 🔗 [deletePost](#deletepost-searchindexinggo335) `:335`

- 🔗 [indexPageranks](#indexpageranks-searchindexinggo484) `:484`

- 🔗 [indexPosts](#indexposts-searchindexinggo382) `:382`

- 🔗 [indexProfiles](#indexprofiles-searchindexinggo432) `:432`

- 🔗 [runPagerankIndexer](#runpagerankindexer-searchindexinggo291) `:291`

- 🔗 [runPostIndexer](#runpostindexer-searchindexinggo203) `:203`

- 🔗 [runProfileIndexer](#runprofileindexer-searchindexinggo247) `:247`

- 🔗 [updateUserHandle](#updateuserhandle-searchindexinggo538) `:538`


</details>


[function] name: EnsureIndices file: search/indexing.go:163 returns_error: нет description: —


### EnsureIndices (search/indexing.go:163)


EnsureIndices is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (idx *Indexer) EnsureIndices((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `search/indexing.go:163`



---


[function] name: NewIndexer file: search/indexing.go:81 returns_error: да description: —


### NewIndexer (search/indexing.go:81)


NewIndexer is a function that performs operations based on the provided parameters and may return an error.


```go
func NewIndexer((*Indexer, error)) (*Indexer, error)
```


**Тип запроса:** Indexer


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "db": null,
  "relayhost": "string",
  "relayXRPC": null,
  "dir": {},
  "echo": null,
  "logger": null,
  "bfs": null,
  "bf": null,
  "enableRepoDiscovery": false,
  "indexLimiter": null,
  "profileQueue": {},
  "postQueue": {},
  "pagerankQueue": {}
}
```


*Определено в:* `search/indexing.go`


**Тип ответа:** Indexer


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "db": null,
  "relayhost": "string",
  "relayXRPC": null,
  "dir": {},
  "echo": null,
  "logger": null,
  "bfs": null,
  "bf": null,
  "enableRepoDiscovery": false,
  "indexLimiter": null,
  "profileQueue": {},
  "postQueue": {},
  "pagerankQueue": {}
}
```


*Определено в:* `search/indexing.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Indexer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/indexing.go:81`



---


[function] name: deletePost file: search/indexing.go:335 returns_error: нет description: —


### deletePost (search/indexing.go:335)


deletePost is a method that performs operations based on the provided parameters and returns (ctx context.Context, did syntax.DID, recordPath string).


```go
func (idx *Indexer) deletePost((ctx context.Context, did syntax.DID, recordPath string)) (ctx context.Context, did syntax.DID, recordPath string)
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


**Тип ответа:** syntax.DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


**Тип ответа:** recordPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/indexing.go:335`



---


[function] name: indexPageranks file: search/indexing.go:484 returns_error: нет description: indexPageranks uses the OpenSearch bulk API to update the pageranks for the given DIDs


### indexPageranks (search/indexing.go:484)


indexPageranks uses the OpenSearch bulk API to update the pageranks for the given DIDs


```go
func (idx *Indexer) indexPageranks((ctx context.Context, pageranks []*PagerankIndexJob)) (ctx context.Context, pageranks []*PagerankIndexJob)
```


**Тип запроса:** PagerankIndexJob


```json
{
  "did": {},
  "rank": 0.0
}
```


*Определено в:* `search/indexing.go`


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


**Тип ответа:** pageranks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PagerankIndexJob


```json
{
  "did": {},
  "rank": 0.0
}
```


*Определено в:* `search/indexing.go`


📍 *Расположение:* `search/indexing.go:484`



---


[function] name: indexPosts file: search/indexing.go:382 returns_error: нет description: —


### indexPosts (search/indexing.go:382)


indexPosts is a method that performs operations based on the provided parameters and returns (ctx context.Context, jobs []*PostIndexJob).


```go
func (idx *Indexer) indexPosts((ctx context.Context, jobs []*PostIndexJob)) (ctx context.Context, jobs []*PostIndexJob)
```


**Тип запроса:** PostIndexJob


```json
{
  "did": {},
  "record": null,
  "rcid": {},
  "rkey": "string"
}
```


*Определено в:* `search/indexing.go`


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


**Тип ответа:** jobs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PostIndexJob


```json
{
  "did": {},
  "record": null,
  "rcid": {},
  "rkey": "string"
}
```


*Определено в:* `search/indexing.go`


📍 *Расположение:* `search/indexing.go:382`



---


[function] name: indexProfiles file: search/indexing.go:432 returns_error: нет description: —


### indexProfiles (search/indexing.go:432)


indexProfiles is a method that performs operations based on the provided parameters and returns (ctx context.Context, jobs []*ProfileIndexJob).


```go
func (idx *Indexer) indexProfiles((ctx context.Context, jobs []*ProfileIndexJob)) (ctx context.Context, jobs []*ProfileIndexJob)
```


**Тип запроса:** ProfileIndexJob


```json
{
  "ident": null,
  "record": null,
  "rcid": {}
}
```


*Определено в:* `search/indexing.go`


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


**Тип ответа:** jobs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ProfileIndexJob


```json
{
  "ident": null,
  "record": null,
  "rcid": {}
}
```


*Определено в:* `search/indexing.go`


📍 *Расположение:* `search/indexing.go:432`



---


[function] name: runPagerankIndexer file: search/indexing.go:291 returns_error: нет description: —


### runPagerankIndexer (search/indexing.go:291)


runPagerankIndexer is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (idx *Indexer) runPagerankIndexer((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `search/indexing.go:291`



---


[function] name: runPostIndexer file: search/indexing.go:203 returns_error: нет description: —


### runPostIndexer (search/indexing.go:203)


runPostIndexer is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (idx *Indexer) runPostIndexer((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `search/indexing.go:203`



---


[function] name: runProfileIndexer file: search/indexing.go:247 returns_error: нет description: —


### runProfileIndexer (search/indexing.go:247)


runProfileIndexer is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (idx *Indexer) runProfileIndexer((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `search/indexing.go:247`



---


[function] name: updateUserHandle file: search/indexing.go:538 returns_error: нет description: —


### updateUserHandle (search/indexing.go:538)


updateUserHandle is a method that performs operations based on the provided parameters and returns (ctx context.Context, did syntax.DID, handle string).


```go
func (idx *Indexer) updateUserHandle((ctx context.Context, did syntax.DID, handle string)) (ctx context.Context, did syntax.DID, handle string)
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


**Тип ответа:** syntax.DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


**Тип ответа:** handle


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


📍 *Расположение:* `search/indexing.go:538`




## search/japanese.go


📄 Исходный файл: `search/japanese.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [containsJapanese](#containsjapanese-searchjapanesego12) `:12`


</details>


[function] name: containsJapanese file: search/japanese.go:12 returns_error: нет description: helper to check if an input string contains any Japanese-specific characters (hiragana or katakana). will not trigger on


### containsJapanese (search/japanese.go:12)


helper to check if an input string contains any Japanese-specific characters (hiragana or katakana). will not trigger on CJK characters which are not specific to Japanese


```go
func containsJapanese((text string)) (text string)
```


**Тип ответа:** text


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


📍 *Расположение:* `search/japanese.go:12`




## search/metrics.go


📄 Исходный файл: `search/metrics.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MetricsMiddleware](#metricsmiddleware-searchmetricsgo84) `:84`

- 🔗 [computeApproximateRequestSize](#computeapproximaterequestsize-searchmetricsgo136) `:136`


</details>


[function] name: MetricsMiddleware file: search/metrics.go:84 returns_error: нет description: MetricsMiddleware defines handler function for metrics middleware


### MetricsMiddleware (search/metrics.go:84)


MetricsMiddleware defines handler function for metrics middleware


```go
func MetricsMiddleware((next echo.HandlerFunc)) (next echo.HandlerFunc)
```


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** echo.HandlerFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/metrics.go:84`



---


[function] name: computeApproximateRequestSize file: search/metrics.go:136 returns_error: нет description: —


### computeApproximateRequestSize (search/metrics.go:136)


computeApproximateRequestSize is a function that performs operations based on the provided parameters and returns (r *http.Request).


```go
func computeApproximateRequestSize((r *http.Request)) (r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `search/metrics.go:136`




## search/parse_query.go


📄 Исходный файл: `search/parse_query.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ParsePostQuery](#parsepostquery-searchparse_querygo14) `:14`


</details>


[function] name: ParsePostQuery file: search/parse_query.go:14 returns_error: нет description: ParsePostQuery takes a query string and pulls out some facet patterns ("from:handle.net") as filters


### ParsePostQuery (search/parse_query.go:14)


ParsePostQuery takes a query string and pulls out some facet patterns ("from:handle.net") as filters


```go
func ParsePostQuery((ctx context.Context, dir identity.Directory, raw string, viewer *syntax.DID)) (ctx context.Context, dir identity.Directory, raw string, viewer *syntax.DID)
```


**Тип запроса:** syntax.DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


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


**Тип ответа:** dir


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


**Тип ответа:** raw


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


**Тип ответа:** viewer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


📍 *Расположение:* `search/parse_query.go:14`




## search/query.go


📄 Исходный файл: `search/query.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [DoSearchGeneric](#dosearchgeneric-searchquerygo379) `:379`

- 🔗 [DoSearchPosts](#dosearchposts-searchquerygo217) `:217`

- 🔗 [DoSearchProfiles](#dosearchprofiles-searchquerygo269) `:269`

- 🔗 [DoSearchProfilesTypeahead](#dosearchprofilestypeahead-searchquerygo340) `:340`

- 🔗 [Filters](#filters-searchquerygo108) `:108`

- 🔗 [Filters](#filters-searchquerygo192) `:192`

- 🔗 [Update](#update-searchquerygo79) `:79`

- 🔗 [checkParams](#checkparams-searchquerygo210) `:210`

- 🔗 [doSearch](#dosearch-searchquerygo399) `:399`


</details>


[function] name: DoSearchGeneric file: search/query.go:379 returns_error: да description: helper to do a full-featured Lucene query parser (query_string) search, with all possible facets. Not safe to expose pub


### DoSearchGeneric (search/query.go:379)


helper to do a full-featured Lucene query parser (query_string) search, with all possible facets. Not safe to expose publicly.


```go
func DoSearchGeneric((*EsSearchResponse, error)) (*EsSearchResponse, error)
```


**Тип запроса:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Тип ответа:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*EsSearchResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/query.go:379`



---


[function] name: DoSearchPosts file: search/query.go:217 returns_error: да description: —


### DoSearchPosts (search/query.go:217)


DoSearchPosts is a function that performs operations based on the provided parameters and may return an error.


```go
func DoSearchPosts((*EsSearchResponse, error)) (*EsSearchResponse, error)
```


**Тип запроса:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Тип ответа:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*EsSearchResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/query.go:217`



---


[function] name: DoSearchProfiles file: search/query.go:269 returns_error: да description: —


### DoSearchProfiles (search/query.go:269)


DoSearchProfiles is a function that performs operations based on the provided parameters and may return an error.


```go
func DoSearchProfiles((*EsSearchResponse, error)) (*EsSearchResponse, error)
```


**Тип запроса:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Тип ответа:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*EsSearchResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/query.go:269`



---


[function] name: DoSearchProfilesTypeahead file: search/query.go:340 returns_error: да description: —


### DoSearchProfilesTypeahead (search/query.go:340)


DoSearchProfilesTypeahead is a function that performs operations based on the provided parameters and may return an error.


```go
func DoSearchProfilesTypeahead((*EsSearchResponse, error)) (*EsSearchResponse, error)
```


**Тип запроса:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Тип ответа:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*EsSearchResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/query.go:340`



---


[function] name: Filters file: search/query.go:108 returns_error: нет description: Filters turns search params in to actual elasticsearch/opensearch filter DSL


### Filters (search/query.go:108)


Filters turns search params in to actual elasticsearch/opensearch filter DSL


```go
func (p *PostSearchParams) Filters(()) ()
```


📍 *Расположение:* `search/query.go:108`



---


[function] name: Filters file: search/query.go:192 returns_error: нет description: Filters turns search params in to actual elasticsearch/opensearch filter DSL


### Filters (search/query.go:192)


Filters turns search params in to actual elasticsearch/opensearch filter DSL


```go
func (p *ActorSearchParams) Filters(()) ()
```


📍 *Расположение:* `search/query.go:192`



---


[function] name: Update file: search/query.go:79 returns_error: нет description: Merges params from another param object in to this one. Intended to meld parsed query with HTTP query params, so not all


### Update (search/query.go:79)


Merges params from another param object in to this one. Intended to meld parsed query with HTTP query params, so not all functionality is supported, and priority is with the "current" object


```go
func (p *PostSearchParams) Update((other *PostSearchParams)) (other *PostSearchParams)
```


**Тип запроса:** PostSearchParams


```json
{
  "Query": "string",
  "Sort": "string",
  "Author": null,
  "Since": null,
  "Until": null,
  "Mentions": null,
  "Lang": null,
  "Domain": "string",
  "URL": "string",
  "Tags": [],
  "Viewer": null,
  "Offset": 0,
  "Size": 0
}
```


*Определено в:* `search/query.go`


**Тип ответа:** other


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PostSearchParams


```json
{
  "Query": "string",
  "Sort": "string",
  "Author": null,
  "Since": null,
  "Until": null,
  "Mentions": null,
  "Lang": null,
  "Domain": "string",
  "URL": "string",
  "Tags": [],
  "Viewer": null,
  "Offset": 0,
  "Size": 0
}
```


*Определено в:* `search/query.go`


📍 *Расположение:* `search/query.go:79`



---


[function] name: checkParams file: search/query.go:210 returns_error: нет description: —


### checkParams (search/query.go:210)


checkParams is a function that performs operations based on the provided parameters and returns (offset, size int).


```go
func checkParams((offset, size int)) (offset, size int)
```


**Тип ответа:** offset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** size


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/query.go:210`



---


[function] name: doSearch file: search/query.go:399 returns_error: да description: —


### doSearch (search/query.go:399)


doSearch is a function that performs operations based on the provided parameters and may return an error.


```go
func doSearch((*EsSearchResponse, error)) (*EsSearchResponse, error)
```


**Тип запроса:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Тип ответа:** EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*EsSearchResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/query.go:399`




## search/server.go


📄 Исходный файл: `search/server.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [EnsureIndices](#ensureindices-searchservergo67) `:67`

- 🔗 [NewServer](#newserver-searchservergo48) `:48`

- 🔗 [RunAPI](#runapi-searchservergo129) `:129`

- 🔗 [RunMetrics](#runmetrics-searchservergo161) `:161`

- 🔗 [Shutdown](#shutdown-searchservergo166) `:166`

- 🔗 [handleHealthCheck](#handlehealthcheck-searchservergo119) `:119`


</details>


[function] name: EnsureIndices file: search/server.go:67 returns_error: нет description: —


### EnsureIndices (search/server.go:67)


EnsureIndices is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (s *Server) EnsureIndices((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `search/server.go:67`



---


[function] name: NewServer file: search/server.go:48 returns_error: да description: —


### NewServer (search/server.go:48)


NewServer is a function that performs operations based on the provided parameters and may return an error.


```go
func NewServer((*Server, error)) (*Server, error)
```


**Тип запроса:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Тип ответа:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Server`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `search/server.go:48`



---


[function] name: RunAPI file: search/server.go:129 returns_error: нет description: —


### RunAPI (search/server.go:129)


RunAPI is a method that performs operations based on the provided parameters and returns (listen string).


```go
func (s *Server) RunAPI((listen string)) (listen string)
```


**Тип ответа:** listen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/server.go:129`



---


[function] name: RunMetrics file: search/server.go:161 returns_error: нет description: —


### RunMetrics (search/server.go:161)


RunMetrics is a method that performs operations based on the provided parameters and returns (listen string).


```go
func (s *Server) RunMetrics((listen string)) (listen string)
```


**Тип ответа:** listen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/server.go:161`



---


[function] name: Shutdown file: search/server.go:166 returns_error: нет description: —


### Shutdown (search/server.go:166)


Shutdown is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (s *Server) Shutdown((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `search/server.go:166`



---


[function] name: handleHealthCheck file: search/server.go:119 returns_error: нет description: —


### handleHealthCheck (search/server.go:119)


handleHealthCheck is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (a *Server) handleHealthCheck((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `search/server.go:119`




## search/transform.go


📄 Исходный файл: `search/transform.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [DocId](#docid-searchtransformgo59) `:59`

- 🔗 [DocId](#docid-searchtransformgo66) `:66`

- 🔗 [TransformPost](#transformpost-searchtransformgo105) `:105`

- 🔗 [TransformProfile](#transformprofile-searchtransformgo70) `:70`

- 🔗 [dedupeStrings](#dedupestrings-searchtransformgo240) `:240`

- 🔗 [parseEmojis](#parseemojis-searchtransformgo277) `:277`

- 🔗 [parsePostTags](#parseposttags-searchtransformgo261) `:261`

- 🔗 [parseProfileTags](#parseprofiletags-searchtransformgo252) `:252`


</details>


[function] name: DocId file: search/transform.go:59 returns_error: нет description: Returns the search index document ID (`_id`) for this document.

This identifier should be URL safe and not contain a sl


### DocId (search/transform.go:59)


Returns the search index document ID (`_id`) for this document.

This identifier should be URL safe and not contain a slash ("/").


```go
func (d *ProfileDoc) DocId(()) ()
```


📍 *Расположение:* `search/transform.go:59`



---


[function] name: DocId file: search/transform.go:66 returns_error: нет description: Returns the search index document ID (`_id`) for this document.

This identifier should be URL safe and not contain a sl


### DocId (search/transform.go:66)


Returns the search index document ID (`_id`) for this document.

This identifier should be URL safe and not contain a slash ("/").


```go
func (d *PostDoc) DocId(()) ()
```


📍 *Расположение:* `search/transform.go:66`



---


[function] name: TransformPost file: search/transform.go:105 returns_error: нет description: —


### TransformPost (search/transform.go:105)


TransformPost is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost, did syntax.DID, rkey, cid string).


```go
func TransformPost((post *appbsky.FeedPost, did syntax.DID, rkey, cid string)) (post *appbsky.FeedPost, did syntax.DID, rkey, cid string)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** syntax.DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


**Тип ответа:** rkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/transform.go:105`



---


[function] name: TransformProfile file: search/transform.go:70 returns_error: нет description: —


### TransformProfile (search/transform.go:70)


TransformProfile is a function that performs operations based on the provided parameters and returns (profile *appbsky.ActorProfile, ident *identity.Identity, cid string).


```go
func TransformProfile((profile *appbsky.ActorProfile, ident *identity.Identity, cid string)) (profile *appbsky.ActorProfile, ident *identity.Identity, cid string)
```


**Тип запроса:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


**Тип запроса:** identity.Identity


```json
{
  "DID": {},
  "Handle": {},
  "AlsoKnownAs": [],
  "Services": {},
  "Keys": {}
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** profile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


**Тип ответа:** ident


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** identity.Identity


```json
{
  "DID": {},
  "Handle": {},
  "AlsoKnownAs": [],
  "Services": {},
  "Keys": {}
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `search/transform.go:70`



---


[function] name: dedupeStrings file: search/transform.go:240 returns_error: нет description: —


### dedupeStrings (search/transform.go:240)


dedupeStrings is a function that performs operations based on the provided parameters and returns (in []string).


```go
func dedupeStrings((in []string)) (in []string)
```


**Тип ответа:** in


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


📍 *Расположение:* `search/transform.go:240`



---


[function] name: parseEmojis file: search/transform.go:277 returns_error: нет description: —


### parseEmojis (search/transform.go:277)


parseEmojis is a function that performs operations based on the provided parameters and returns (s string).


```go
func parseEmojis((s string)) (s string)
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


📍 *Расположение:* `search/transform.go:277`



---


[function] name: parsePostTags file: search/transform.go:261 returns_error: нет description: —


### parsePostTags (search/transform.go:261)


parsePostTags is a function that performs operations based on the provided parameters and returns (p *appbsky.FeedPost).


```go
func parsePostTags((p *appbsky.FeedPost)) (p *appbsky.FeedPost)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** p


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


📍 *Расположение:* `search/transform.go:261`



---


[function] name: parseProfileTags file: search/transform.go:252 returns_error: нет description: —


### parseProfileTags (search/transform.go:252)


parseProfileTags is a function that performs operations based on the provided parameters and returns (p *appbsky.ActorProfile).


```go
func parseProfileTags((p *appbsky.ActorProfile)) (p *appbsky.ActorProfile)
```


**Тип запроса:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


**Тип ответа:** p


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


📍 *Расположение:* `search/transform.go:252`




## search/url.go


📄 Исходный файл: `search/url.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NormalizeLossyURL](#normalizelossyurl-searchurlgo37) `:37`


</details>


[function] name: NormalizeLossyURL file: search/url.go:37 returns_error: нет description: aggressively normalizes URL, for search indexing and matching. it is possible the URL won't be directly functional after


### NormalizeLossyURL (search/url.go:37)


aggressively normalizes URL, for search indexing and matching. it is possible the URL won't be directly functional after this normalization


```go
func NormalizeLossyURL((raw string)) (raw string)
```


**Тип ответа:** raw


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


📍 *Расположение:* `search/url.go:37`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repomgr_keymgr.md)

- [Следующая директория](splitter.md)


---

