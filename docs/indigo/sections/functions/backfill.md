---
title: "Функции: backfill"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: backfill
---


# Функции: backfill


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_visual.md)

- [Следующая директория](carstore.md)


---


## Меню по файлам


- 📄 [backfill/backfill.go](#backfillbackfillgo)

- 📄 [backfill/gormstore.go](#backfillgormstorego)

- 📄 [backfill/memstore.go](#backfillmemstorego)

- 📄 [backfill/util.go](#backfillutilgo)


---


## backfill/backfill.go


📄 Исходный файл: `backfill/backfill.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [BackfillRepo](#backfillrepo-backfillbackfillgo375) `:375`

- 🔗 [BufferOp](#bufferop-backfillbackfillgo601) `:601`

- 🔗 [BufferOps](#bufferops-backfillbackfillgo610) `:610`

- 🔗 [DefaultBackfillOptions](#defaultbackfilloptions-backfillbackfillgo124) `:124`

- 🔗 [Error](#error-backfillbackfillgo318) `:318`

- 🔗 [FlushBuffer](#flushbuffer-backfillbackfillgo249) `:249`

- 🔗 [HandleEvent](#handleevent-backfillbackfillgo527) `:527`

- 🔗 [NewBackfiller](#newbackfiller-backfillbackfillgo135) `:135`

- 🔗 [Start](#start-backfillbackfillgo171) `:171`

- 🔗 [Stop](#stop-backfillbackfillgo234) `:234`

- 🔗 [computeExponentialBackoff](#computeexponentialbackoff-backfillbackfillgo634) `:634`

- 🔗 [fetchRepo](#fetchrepo-backfillbackfillgo329) `:329`

- 🔗 [getRecord](#getrecord-backfillbackfillgo507) `:507`


</details>


[function] name: BackfillRepo file: backfill/backfill.go:375 returns_error: да description: BackfillRepo backfills a repo


### BackfillRepo (backfill/backfill.go:375)


BackfillRepo backfills a repo


```go
func (b *Backfiller) BackfillRepo((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/backfill.go:375`



---


[function] name: BufferOp file: backfill/backfill.go:601 returns_error: да description: —


### BufferOp (backfill/backfill.go:601)


BufferOp is a method that performs operations based on the provided parameters and may return an error.


```go
func (bf *Backfiller) BufferOp((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/backfill.go:601`



---


[function] name: BufferOps file: backfill/backfill.go:610 returns_error: да description: —


### BufferOps (backfill/backfill.go:610)


BufferOps is a method that performs operations based on the provided parameters and may return an error.


```go
func (bf *Backfiller) BufferOps((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/backfill.go:610`



---


[function] name: DefaultBackfillOptions file: backfill/backfill.go:124 returns_error: нет description: —


### DefaultBackfillOptions (backfill/backfill.go:124)


DefaultBackfillOptions is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultBackfillOptions(()) ()
```


📍 *Расположение:* `backfill/backfill.go:124`



---


[function] name: Error file: backfill/backfill.go:318 returns_error: нет description: —


### Error (backfill/backfill.go:318)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e *FetchRepoError) Error(()) ()
```


📍 *Расположение:* `backfill/backfill.go:318`



---


[function] name: FlushBuffer file: backfill/backfill.go:249 returns_error: нет description: FlushBuffer processes buffered operations for a job


### FlushBuffer (backfill/backfill.go:249)


FlushBuffer processes buffered operations for a job


```go
func (b *Backfiller) FlushBuffer((ctx context.Context, job Job)) (ctx context.Context, job Job)
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


**Тип ответа:** Job


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


📍 *Расположение:* `backfill/backfill.go:249`



---


[function] name: HandleEvent file: backfill/backfill.go:527 returns_error: нет description: —


### HandleEvent (backfill/backfill.go:527)


HandleEvent is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, evt *atproto.SyncSubscribeRepos_Commit).


```go
func (bf *Backfiller) HandleEvent((ctx context.Context, evt *atproto.SyncSubscribeRepos_Commit)) (ctx context.Context, evt *atproto.SyncSubscribeRepos_Commit)
```


**Тип запроса:** atproto.SyncSubscribeRepos_Commit


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


**Тип ответа:** atproto.SyncSubscribeRepos_Commit


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


📍 *Расположение:* `backfill/backfill.go:527`



---


[function] name: NewBackfiller file: backfill/backfill.go:135 returns_error: да description: NewBackfiller creates a new Backfiller


### NewBackfiller (backfill/backfill.go:135)


NewBackfiller creates a new Backfiller


```go
func NewBackfiller((
	name string,
	store Store,
	handleCreate func(ctx context.Context, repo string, rev string, path string, rec *[]byte, cid *cid.Cid) error,
	handleUpdate func(ctx context.Context, repo string, rev string, path string, rec *[]byte, cid *cid.Cid) error,
	handleDelete func(ctx context.Context, repo string, rev string, path string) error,
	opts *BackfillOptions,
)) (
	name string,
	store Store,
	handleCreate func(ctx context.Context, repo string, rev string, path string, rec *[]byte, cid *cid.Cid) error,
	handleUpdate func(ctx context.Context, repo string, rev string, path string, rec *[]byte, cid *cid.Cid) error,
	handleDelete func(ctx context.Context, repo string, rev string, path string) error,
	opts *BackfillOptions,
)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип запроса:** BackfillOptions


```json
{
  "ParallelBackfills": 0,
  "ParallelRecordCreates": 0,
  "NSIDFilter": "string",
  "SyncRequestsPerSecond": 0,
  "RelayHost": "string"
}
```


*Определено в:* `backfill/backfill.go`


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** store


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** Store


```json
{
  "dbPath": "string",
  "db": null,
  "log": null,
  "lastShardCache": {}
}
```


*Определено в:* `carstore/sqlite_store.go`


**Тип ответа:** handleCreate


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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** handleUpdate


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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** handleDelete


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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BackfillOptions


```json
{
  "ParallelBackfills": 0,
  "ParallelRecordCreates": 0,
  "NSIDFilter": "string",
  "SyncRequestsPerSecond": 0,
  "RelayHost": "string"
}
```


*Определено в:* `backfill/backfill.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `name string`, `store Store`, `handleCreate func(ctx context.Context`, `repo string`, `rev string`, `path string`, `rec *[]byte`, `cid *cid.Cid) error`, `handleUpdate func(ctx context.Context`, `repo string`, `rev string`, `path string`, `rec *[]byte`, `cid *cid.Cid) error`, `handleDelete func(ctx context.Context`, `repo string`, `rev string`, `path string) error`, `opts *BackfillOptions`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/backfill.go:135`



---


[function] name: Start file: backfill/backfill.go:171 returns_error: нет description: Start starts the backfill processor routine


### Start (backfill/backfill.go:171)


Start starts the backfill processor routine


```go
func (b *Backfiller) Start(()) ()
```


📍 *Расположение:* `backfill/backfill.go:171`



---


[function] name: Stop file: backfill/backfill.go:234 returns_error: нет description: Stop stops the backfill processor


### Stop (backfill/backfill.go:234)


Stop stops the backfill processor


```go
func (b *Backfiller) Stop((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `backfill/backfill.go:234`



---


[function] name: computeExponentialBackoff file: backfill/backfill.go:634 returns_error: нет description: —


### computeExponentialBackoff (backfill/backfill.go:634)


computeExponentialBackoff is a function that performs operations based on the provided parameters and returns (attempt int).


```go
func computeExponentialBackoff((attempt int)) (attempt int)
```


**Тип ответа:** attempt


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/backfill.go:634`



---


[function] name: fetchRepo file: backfill/backfill.go:329 returns_error: да description: Fetches a repo CAR file over HTTP from the indicated host.


### fetchRepo (backfill/backfill.go:329)


Fetches a repo CAR file over HTTP from the indicated host.


```go
func (b *Backfiller) fetchRepo((io.ReadCloser, error)) (io.ReadCloser, error)
```


**Тип ответа:** io.ReadCloser


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `io.ReadCloser`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/backfill.go:329`



---


[function] name: getRecord file: backfill/backfill.go:507 returns_error: да description: —


### getRecord (backfill/backfill.go:507)


getRecord is a method that performs operations based on the provided parameters and may return an error.


```go
func (bf *Backfiller) getRecord((cid.Cid, *[]byte, error)) (cid.Cid, *[]byte, error)
```


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `*[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/backfill.go:507`




## backfill/gormstore.go


📄 Исходный файл: `backfill/gormstore.go`


<details open>
<summary><b>Функции в этом файле (24)</b></summary>


- 🔗 [BufferOps](#bufferops-backfillgormstorego176) `:176`

- 🔗 [ClearBufferedOps](#clearbufferedops-backfillgormstorego401) `:401`

- 🔗 [EnqueueJob](#enqueuejob-backfillgormstorego115) `:115`

- 🔗 [EnqueueJobWithState](#enqueuejobwithstate-backfillgormstorego128) `:128`

- 🔗 [FlushBufferedOps](#flushbufferedops-backfillgormstorego357) `:357`

- 🔗 [GetJob](#getjob-backfillgormstorego214) `:214`

- 🔗 [GetNextEnqueuedJob](#getnextenqueuedjob-backfillgormstorego271) `:271`

- 🔗 [GetOrCreateJob](#getorcreatejob-backfillgormstorego98) `:98`

- 🔗 [LoadJobs](#loadjobs-backfillgormstorego61) `:61`

- 🔗 [NewGormstore](#newgormstore-backfillgormstorego54) `:54`

- 🔗 [PurgeRepo](#purgerepo-backfillgormstorego425) `:425`

- 🔗 [Repo](#repo-backfillgormstorego302) `:302`

- 🔗 [RetryCount](#retrycount-backfillgormstorego410) `:410`

- 🔗 [Rev](#rev-backfillgormstorego328) `:328`

- 🔗 [SetRev](#setrev-backfillgormstorego313) `:313`

- 🔗 [SetState](#setstate-backfillgormstorego335) `:335`

- 🔗 [State](#state-backfillgormstorego306) `:306`

- 🔗 [UpdateRev](#updaterev-backfillgormstorego416) `:416`

- 🔗 [bufferOps](#bufferops-backfillgormstorego209) `:209`

- 🔗 [checkJobCache](#checkjobcache-backfillgormstorego260) `:260`

- 🔗 [createJobForRepo](#createjobforrepo-backfillgormstorego141) `:141`

- 🔗 [getJob](#getjob-backfillgormstorego218) `:218`

- 🔗 [loadJob](#loadjob-backfillgormstorego227) `:227`

- 🔗 [loadJobs](#loadjobs-backfillgormstorego67) `:67`


</details>


[function] name: BufferOps file: backfill/gormstore.go:176 returns_error: да description: —


### BufferOps (backfill/gormstore.go:176)


BufferOps is a method that performs operations based on the provided parameters and may return an error.


```go
func (j *Gormjob) BufferOps((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/gormstore.go:176`



---


[function] name: ClearBufferedOps file: backfill/gormstore.go:401 returns_error: нет description: —


### ClearBufferedOps (backfill/gormstore.go:401)


ClearBufferedOps is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (j *Gormjob) ClearBufferedOps((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `backfill/gormstore.go:401`



---


[function] name: EnqueueJob file: backfill/gormstore.go:115 returns_error: нет description: —


### EnqueueJob (backfill/gormstore.go:115)


EnqueueJob is a method that performs operations based on the provided parameters and returns (ctx context.Context, repo string).


```go
func (s *Gormstore) EnqueueJob((ctx context.Context, repo string)) (ctx context.Context, repo string)
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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/gormstore.go:115`



---


[function] name: EnqueueJobWithState file: backfill/gormstore.go:128 returns_error: нет description: —


### EnqueueJobWithState (backfill/gormstore.go:128)


EnqueueJobWithState is a method that performs operations based on the provided parameters and returns (ctx context.Context, repo, state string).


```go
func (s *Gormstore) EnqueueJobWithState((ctx context.Context, repo, state string)) (ctx context.Context, repo, state string)
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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/gormstore.go:128`



---


[function] name: FlushBufferedOps file: backfill/gormstore.go:357 returns_error: да description: —


### FlushBufferedOps (backfill/gormstore.go:357)


FlushBufferedOps is a method that performs operations based on the provided parameters and may return an error.


```go
func (j *Gormjob) FlushBufferedOps((ctx context.Context, fn func(kind repomgr.EventKind, rev, path string, rec *[]byte, cid *cid.Cid) error)) (ctx context.Context, fn func(kind repomgr.EventKind, rev, path string, rec *[]byte, cid *cid.Cid) error)
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


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** repomgr.EventKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `fn func(kind repomgr.EventKind`, `rev`, `path string`, `rec *[]byte`, `cid *cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/gormstore.go:357`



---


[function] name: GetJob file: backfill/gormstore.go:214 returns_error: да description: —


### GetJob (backfill/gormstore.go:214)


GetJob is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *Gormstore) GetJob((Job, error)) (Job, error)
```


**Тип ответа:** Job


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Job`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/gormstore.go:214`



---


[function] name: GetNextEnqueuedJob file: backfill/gormstore.go:271 returns_error: да description: —


### GetNextEnqueuedJob (backfill/gormstore.go:271)


GetNextEnqueuedJob is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *Gormstore) GetNextEnqueuedJob((Job, error)) (Job, error)
```


**Тип ответа:** Job


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Job`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/gormstore.go:271`



---


[function] name: GetOrCreateJob file: backfill/gormstore.go:98 returns_error: да description: —


### GetOrCreateJob (backfill/gormstore.go:98)


GetOrCreateJob is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *Gormstore) GetOrCreateJob((Job, error)) (Job, error)
```


**Тип ответа:** Job


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Job`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/gormstore.go:98`



---


[function] name: LoadJobs file: backfill/gormstore.go:61 returns_error: нет description: —


### LoadJobs (backfill/gormstore.go:61)


LoadJobs is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (s *Gormstore) LoadJobs((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `backfill/gormstore.go:61`



---


[function] name: NewGormstore file: backfill/gormstore.go:54 returns_error: нет description: —


### NewGormstore (backfill/gormstore.go:54)


NewGormstore is a function that performs operations based on the provided parameters and returns (db *gorm.DB).


```go
func NewGormstore((db *gorm.DB)) (db *gorm.DB)
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


📍 *Расположение:* `backfill/gormstore.go:54`



---


[function] name: PurgeRepo file: backfill/gormstore.go:425 returns_error: нет description: —


### PurgeRepo (backfill/gormstore.go:425)


PurgeRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, repo string).


```go
func (s *Gormstore) PurgeRepo((ctx context.Context, repo string)) (ctx context.Context, repo string)
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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/gormstore.go:425`



---


[function] name: Repo file: backfill/gormstore.go:302 returns_error: нет description: —


### Repo (backfill/gormstore.go:302)


Repo is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Gormjob) Repo(()) ()
```


📍 *Расположение:* `backfill/gormstore.go:302`



---


[function] name: RetryCount file: backfill/gormstore.go:410 returns_error: нет description: —


### RetryCount (backfill/gormstore.go:410)


RetryCount is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Gormjob) RetryCount(()) ()
```


📍 *Расположение:* `backfill/gormstore.go:410`



---


[function] name: Rev file: backfill/gormstore.go:328 returns_error: нет description: —


### Rev (backfill/gormstore.go:328)


Rev is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Gormjob) Rev(()) ()
```


📍 *Расположение:* `backfill/gormstore.go:328`



---


[function] name: SetRev file: backfill/gormstore.go:313 returns_error: нет description: —


### SetRev (backfill/gormstore.go:313)


SetRev is a method that updates data based on the provided parameters and returns (ctx context.Context, r string).


```go
func (j *Gormjob) SetRev((ctx context.Context, r string)) (ctx context.Context, r string)
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


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


📍 *Расположение:* `backfill/gormstore.go:313`



---


[function] name: SetState file: backfill/gormstore.go:335 returns_error: нет description: —


### SetState (backfill/gormstore.go:335)


SetState is a method that updates data based on the provided parameters and returns (ctx context.Context, state string).


```go
func (j *Gormjob) SetState((ctx context.Context, state string)) (ctx context.Context, state string)
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


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/gormstore.go:335`



---


[function] name: State file: backfill/gormstore.go:306 returns_error: нет description: —


### State (backfill/gormstore.go:306)


State is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Gormjob) State(()) ()
```


📍 *Расположение:* `backfill/gormstore.go:306`



---


[function] name: UpdateRev file: backfill/gormstore.go:416 returns_error: нет description: —


### UpdateRev (backfill/gormstore.go:416)


UpdateRev is a method that updates data based on the provided parameters and returns (ctx context.Context, repo, rev string).


```go
func (s *Gormstore) UpdateRev((ctx context.Context, repo, rev string)) (ctx context.Context, repo, rev string)
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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/gormstore.go:416`



---


[function] name: bufferOps file: backfill/gormstore.go:209 returns_error: нет description: —


### bufferOps (backfill/gormstore.go:209)


bufferOps is a method that performs operations based on the provided parameters and returns (ops *opSet).


```go
func (j *Gormjob) bufferOps((ops *opSet)) (ops *opSet)
```


**Тип запроса:** opSet


```json
{
  "since": "string",
  "rev": "string",
  "ops": []
}
```


*Определено в:* `backfill/memstore.go`


**Тип ответа:** ops


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** opSet


```json
{
  "since": "string",
  "rev": "string",
  "ops": []
}
```


*Определено в:* `backfill/memstore.go`


📍 *Расположение:* `backfill/gormstore.go:209`



---


[function] name: checkJobCache file: backfill/gormstore.go:260 returns_error: нет description: —


### checkJobCache (backfill/gormstore.go:260)


checkJobCache is a method that performs operations based on the provided parameters and returns (ctx context.Context, repo string).


```go
func (s *Gormstore) checkJobCache((ctx context.Context, repo string)) (ctx context.Context, repo string)
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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/gormstore.go:260`



---


[function] name: createJobForRepo file: backfill/gormstore.go:141 returns_error: нет description: —


### createJobForRepo (backfill/gormstore.go:141)


createJobForRepo is a method that performs operations based on the provided parameters and returns (repo, state string).


```go
func (s *Gormstore) createJobForRepo((repo, state string)) (repo, state string)
```


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/gormstore.go:141`



---


[function] name: getJob file: backfill/gormstore.go:218 returns_error: да description: —


### getJob (backfill/gormstore.go:218)


getJob is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Gormstore) getJob((*Gormjob, error)) (*Gormjob, error)
```


**Тип запроса:** Gormjob


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


**Тип ответа:** Gormjob


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Gormjob`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/gormstore.go:218`



---


[function] name: loadJob file: backfill/gormstore.go:227 returns_error: да description: —


### loadJob (backfill/gormstore.go:227)


loadJob is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Gormstore) loadJob((*Gormjob, error)) (*Gormjob, error)
```


**Тип запроса:** Gormjob


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


**Тип ответа:** Gormjob


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Gormjob`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/gormstore.go:227`



---


[function] name: loadJobs file: backfill/gormstore.go:67 returns_error: нет description: —


### loadJobs (backfill/gormstore.go:67)


loadJobs is a method that performs operations based on the provided parameters and returns (ctx context.Context, limit int).


```go
func (s *Gormstore) loadJobs((ctx context.Context, limit int)) (ctx context.Context, limit int)
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


**Тип ответа:** limit


```json
{
  "Limit": 0,
  "Remaining": 0,
  "Policy": "string",
  "Reset": {}
}
```


*Определено в:* `xrpc/xrpc.go`


📍 *Расположение:* `backfill/gormstore.go:67`




## backfill/memstore.go


📄 Исходный файл: `backfill/memstore.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [BufferOp](#bufferop-backfillmemstorego90) `:90`

- 🔗 [BufferOps](#bufferops-backfillmemstorego126) `:126`

- 🔗 [ClearBufferedOps](#clearbufferedops-backfillmemstorego229) `:229`

- 🔗 [EnqueueJob](#enqueuejob-backfillmemstorego54) `:54`

- 🔗 [EnqueueJobWithState](#enqueuejobwithstate-backfillmemstorego72) `:72`

- 🔗 [FlushBufferedOps](#flushbufferedops-backfillmemstorego208) `:208`

- 🔗 [GetJob](#getjob-backfillmemstorego148) `:148`

- 🔗 [GetNextEnqueuedJob](#getnextenqueuedjob-backfillmemstorego159) `:159`

- 🔗 [NewMemstore](#newmemstore-backfillmemstorego48) `:48`

- 🔗 [PurgeRepo](#purgerepo-backfillmemstorego171) `:171`

- 🔗 [Repo](#repo-backfillmemstorego179) `:179`

- 🔗 [RetryCount](#retrycount-backfillmemstorego238) `:238`

- 🔗 [Rev](#rev-backfillmemstorego199) `:199`

- 🔗 [SetRev](#setrev-backfillmemstorego203) `:203`

- 🔗 [SetState](#setstate-backfillmemstorego190) `:190`

- 🔗 [State](#state-backfillmemstorego183) `:183`


</details>


[function] name: BufferOp file: backfill/memstore.go:90 returns_error: да description: —


### BufferOp (backfill/memstore.go:90)


BufferOp is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Memstore) BufferOp((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/memstore.go:90`



---


[function] name: BufferOps file: backfill/memstore.go:126 returns_error: да description: —


### BufferOps (backfill/memstore.go:126)


BufferOps is a method that performs operations based on the provided parameters and may return an error.


```go
func (j *Memjob) BufferOps((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/memstore.go:126`



---


[function] name: ClearBufferedOps file: backfill/memstore.go:229 returns_error: нет description: —


### ClearBufferedOps (backfill/memstore.go:229)


ClearBufferedOps is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (j *Memjob) ClearBufferedOps((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `backfill/memstore.go:229`



---


[function] name: EnqueueJob file: backfill/memstore.go:54 returns_error: нет description: —


### EnqueueJob (backfill/memstore.go:54)


EnqueueJob is a method that performs operations based on the provided parameters and returns (repo string).


```go
func (s *Memstore) EnqueueJob((repo string)) (repo string)
```


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/memstore.go:54`



---


[function] name: EnqueueJobWithState file: backfill/memstore.go:72 returns_error: нет description: —


### EnqueueJobWithState (backfill/memstore.go:72)


EnqueueJobWithState is a method that performs operations based on the provided parameters and returns (repo, state string).


```go
func (s *Memstore) EnqueueJobWithState((repo, state string)) (repo, state string)
```


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/memstore.go:72`



---


[function] name: FlushBufferedOps file: backfill/memstore.go:208 returns_error: да description: —


### FlushBufferedOps (backfill/memstore.go:208)


FlushBufferedOps is a method that performs operations based on the provided parameters and may return an error.


```go
func (j *Memjob) FlushBufferedOps((ctx context.Context, fn func(kind repomgr.EventKind, rev, path string, rec *[]byte, cid *cid.Cid) error)) (ctx context.Context, fn func(kind repomgr.EventKind, rev, path string, rec *[]byte, cid *cid.Cid) error)
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


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** repomgr.EventKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `fn func(kind repomgr.EventKind`, `rev`, `path string`, `rec *[]byte`, `cid *cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/memstore.go:208`



---


[function] name: GetJob file: backfill/memstore.go:148 returns_error: да description: —


### GetJob (backfill/memstore.go:148)


GetJob is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *Memstore) GetJob((Job, error)) (Job, error)
```


**Тип ответа:** Job


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Job`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/memstore.go:148`



---


[function] name: GetNextEnqueuedJob file: backfill/memstore.go:159 returns_error: да description: —


### GetNextEnqueuedJob (backfill/memstore.go:159)


GetNextEnqueuedJob is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *Memstore) GetNextEnqueuedJob((Job, error)) (Job, error)
```


**Тип ответа:** Job


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Job`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/memstore.go:159`



---


[function] name: NewMemstore file: backfill/memstore.go:48 returns_error: нет description: —


### NewMemstore (backfill/memstore.go:48)


NewMemstore is a function that performs operations based on the provided parameters and returns ().


```go
func NewMemstore(()) ()
```


📍 *Расположение:* `backfill/memstore.go:48`



---


[function] name: PurgeRepo file: backfill/memstore.go:171 returns_error: нет description: —


### PurgeRepo (backfill/memstore.go:171)


PurgeRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, repo string).


```go
func (s *Memstore) PurgeRepo((ctx context.Context, repo string)) (ctx context.Context, repo string)
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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/memstore.go:171`



---


[function] name: Repo file: backfill/memstore.go:179 returns_error: нет description: —


### Repo (backfill/memstore.go:179)


Repo is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Memjob) Repo(()) ()
```


📍 *Расположение:* `backfill/memstore.go:179`



---


[function] name: RetryCount file: backfill/memstore.go:238 returns_error: нет description: —


### RetryCount (backfill/memstore.go:238)


RetryCount is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Memjob) RetryCount(()) ()
```


📍 *Расположение:* `backfill/memstore.go:238`



---


[function] name: Rev file: backfill/memstore.go:199 returns_error: нет description: —


### Rev (backfill/memstore.go:199)


Rev is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Memjob) Rev(()) ()
```


📍 *Расположение:* `backfill/memstore.go:199`



---


[function] name: SetRev file: backfill/memstore.go:203 returns_error: нет description: —


### SetRev (backfill/memstore.go:203)


SetRev is a method that updates data based on the provided parameters and returns (ctx context.Context, rev string).


```go
func (j *Memjob) SetRev((ctx context.Context, rev string)) (ctx context.Context, rev string)
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


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/memstore.go:203`



---


[function] name: SetState file: backfill/memstore.go:190 returns_error: нет description: —


### SetState (backfill/memstore.go:190)


SetState is a method that updates data based on the provided parameters and returns (ctx context.Context, state string).


```go
func (j *Memjob) SetState((ctx context.Context, state string)) (ctx context.Context, state string)
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


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `backfill/memstore.go:190`



---


[function] name: State file: backfill/memstore.go:183 returns_error: нет description: —


### State (backfill/memstore.go:183)


State is a method that performs operations based on the provided parameters and returns ().


```go
func (j *Memjob) State(()) ()
```


📍 *Расположение:* `backfill/memstore.go:183`




## backfill/util.go


📄 Исходный файл: `backfill/util.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Close](#close-backfillutilgo20) `:20`

- 🔗 [Read](#read-backfillutilgo14) `:14`


</details>


[function] name: Close file: backfill/util.go:20 returns_error: нет description: —


### Close (backfill/util.go:20)


Close is a method that performs operations based on the provided parameters and returns ().


```go
func (r instrumentedReader) Close(()) ()
```


📍 *Расположение:* `backfill/util.go:20`



---


[function] name: Read file: backfill/util.go:14 returns_error: да description: —


### Read (backfill/util.go:14)


Read is a method that performs operations based on the provided parameters and may return an error.


```go
func (r instrumentedReader) Read((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `backfill/util.go:14`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_visual.md)

- [Следующая директория](carstore.md)


---

