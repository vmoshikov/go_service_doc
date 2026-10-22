---
title: "Функции: repomgr"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: repomgr
---


# Функции: repomgr


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repo_carutil.md)

- [Следующая директория](repomgr_keymgr.md)


---


## Меню по файлам


- 📄 [repomgr/repomgr.go](#repomgrrepomgrgo)


---


## repomgr/repomgr.go


📄 Исходный файл: `repomgr/repomgr.go`


<details open>
<summary><b>Функции в этом файле (27)</b></summary>


- 🔗 [BatchWrite](#batchwrite-repomgrrepomgrgo780) `:780`

- 🔗 [CarStore](#carstore-repomgrrepomgrgo158) `:158`

- 🔗 [CheckRepoSig](#checkreposig-repomgrrepomgrgo522) `:522`

- 🔗 [CreateRecord](#createrecord-repomgrrepomgrgo162) `:162`

- 🔗 [DeleteRecord](#deleterecord-repomgrrepomgrgo297) `:297`

- 🔗 [GetProfile](#getprofile-repomgrrepomgrgo493) `:493`

- 🔗 [GetRecord](#getrecord-repomgrrepomgrgo439) `:439`

- 🔗 [GetRecordProof](#getrecordproof-repomgrrepomgrgo467) `:467`

- 🔗 [GetRepoRev](#getreporev-repomgrrepomgrgo428) `:428`

- 🔗 [GetRepoRoot](#getreporoot-repomgrrepomgrgo421) `:421`

- 🔗 [HandleExternalUserEvent](#handleexternaluserevent-repomgrrepomgrgo545) `:545`

- 🔗 [ImportNewRepo](#importnewrepo-repomgrrepomgrgo900) `:900`

- 🔗 [InitNewActor](#initnewactor-repomgrrepomgrgo360) `:360`

- 🔗 [NewRepoManager](#newrepomanager-repomgrrepomgrgo36) `:36`

- 🔗 [ReadRepo](#readrepo-repomgrrepomgrgo435) `:435`

- 🔗 [ResetRepo](#resetrepo-repomgrrepomgrgo1177) `:1177`

- 🔗 [SetEventHandler](#seteventhandler-repomgrrepomgrgo60) `:60`

- 🔗 [TakeDownRepo](#takedownrepo-repomgrrepomgrgo1169) `:1169`

- 🔗 [UpdateRecord](#updaterecord-repomgrrepomgrgo227) `:227`

- 🔗 [VerifyRepo](#verifyrepo-repomgrrepomgrgo1184) `:1184`

- 🔗 [handleExternalUserEventArchive](#handleexternalusereventarchive-repomgrrepomgrgo650) `:650`

- 🔗 [handleExternalUserEventNoArchive](#handleexternalusereventnoarchive-repomgrrepomgrgo553) `:553`

- 🔗 [lockUser](#lockuser-repomgrrepomgrgo127) `:127`

- 🔗 [processNewRepo](#processnewrepo-repomgrrepomgrgo1045) `:1045`

- 🔗 [processOp](#processop-repomgrrepomgrgo992) `:992`

- 🔗 [stringOrNil](#stringornil-repomgrrepomgrgo1113) `:1113`

- 🔗 [walkTree](#walktree-repomgrrepomgrgo1122) `:1122`


</details>


[function] name: BatchWrite file: repomgr/repomgr.go:780 returns_error: нет description: —


### BatchWrite (repomgr/repomgr.go:780)


BatchWrite is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid, writes []*atproto.RepoApplyWrites_Input_Writes_Elem).


```go
func (rm *RepoManager) BatchWrite((ctx context.Context, user models.Uid, writes []*atproto.RepoApplyWrites_Input_Writes_Elem)) (ctx context.Context, user models.Uid, writes []*atproto.RepoApplyWrites_Input_Writes_Elem)
```


**Тип запроса:** atproto.RepoApplyWrites_Input_Writes_Elem


```json
{
  "RepoApplyWritesCreate": null,
  "RepoApplyWritesUpdate": null,
  "RepoApplyWritesDelete": null
}
```


*Определено в:* `api/agnostic/repoapplyWrites.go`


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


**Тип ответа:** writes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atproto.RepoApplyWrites_Input_Writes_Elem


```json
{
  "RepoApplyWritesCreate": null,
  "RepoApplyWritesUpdate": null,
  "RepoApplyWritesDelete": null
}
```


*Определено в:* `api/agnostic/repoapplyWrites.go`


📍 *Расположение:* `repomgr/repomgr.go:780`



---


[function] name: CarStore file: repomgr/repomgr.go:158 returns_error: нет description: —


### CarStore (repomgr/repomgr.go:158)


CarStore is a method that performs operations based on the provided parameters and returns ().


```go
func (rm *RepoManager) CarStore(()) ()
```


📍 *Расположение:* `repomgr/repomgr.go:158`



---


[function] name: CheckRepoSig file: repomgr/repomgr.go:522 returns_error: нет description: —


### CheckRepoSig (repomgr/repomgr.go:522)


CheckRepoSig is a method that performs operations based on the provided parameters and returns (ctx context.Context, r *repo.Repo, expdid string).


```go
func (rm *RepoManager) CheckRepoSig((ctx context.Context, r *repo.Repo, expdid string)) (ctx context.Context, r *repo.Repo, expdid string)
```


**Тип запроса:** repo.Repo


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


**Тип ответа:** repo.Repo


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


**Тип ответа:** expdid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repomgr/repomgr.go:522`



---


[function] name: CreateRecord file: repomgr/repomgr.go:162 returns_error: да description: —


### CreateRecord (repomgr/repomgr.go:162)


CreateRecord is a method that creates new data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) CreateRecord((string, cid.Cid, error)) (string, cid.Cid, error)
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


*Типы возврата:* `string`, `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:162`



---


[function] name: DeleteRecord file: repomgr/repomgr.go:297 returns_error: нет description: —


### DeleteRecord (repomgr/repomgr.go:297)


DeleteRecord is a method that deletes data based on the provided parameters and returns (ctx context.Context, user models.Uid, collection, rkey string).


```go
func (rm *RepoManager) DeleteRecord((ctx context.Context, user models.Uid, collection, rkey string)) (ctx context.Context, user models.Uid, collection, rkey string)
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


**Тип ответа:** rkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repomgr/repomgr.go:297`



---


[function] name: GetProfile file: repomgr/repomgr.go:493 returns_error: да description: —


### GetProfile (repomgr/repomgr.go:493)


GetProfile is a method that retrieves data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) GetProfile((*bsky.ActorProfile, error)) (*bsky.ActorProfile, error)
```


**Тип запроса:** bsky.ActorProfile


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


**Тип ответа:** bsky.ActorProfile


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*bsky.ActorProfile`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:493`



---


[function] name: GetRecord file: repomgr/repomgr.go:439 returns_error: да description: —


### GetRecord (repomgr/repomgr.go:439)


GetRecord is a method that retrieves data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) GetRecord((cid.Cid, cbg.CBORMarshaler, error)) (cid.Cid, cbg.CBORMarshaler, error)
```


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cbg.CBORMarshaler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `cbg.CBORMarshaler`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:439`



---


[function] name: GetRecordProof file: repomgr/repomgr.go:467 returns_error: да description: —


### GetRecordProof (repomgr/repomgr.go:467)


GetRecordProof is a method that retrieves data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) GetRecordProof((cid.Cid, []blocks.Block, error)) (cid.Cid, []blocks.Block, error)
```


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** blocks.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `[]blocks.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:467`



---


[function] name: GetRepoRev file: repomgr/repomgr.go:428 returns_error: да description: —


### GetRepoRev (repomgr/repomgr.go:428)


GetRepoRev is a method that retrieves data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) GetRepoRev((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:428`



---


[function] name: GetRepoRoot file: repomgr/repomgr.go:421 returns_error: да description: —


### GetRepoRoot (repomgr/repomgr.go:421)


GetRepoRoot is a method that retrieves data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) GetRepoRoot((cid.Cid, error)) (cid.Cid, error)
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


*Типы возврата:* `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:421`



---


[function] name: HandleExternalUserEvent file: repomgr/repomgr.go:545 returns_error: нет description: —


### HandleExternalUserEvent (repomgr/repomgr.go:545)


HandleExternalUserEvent is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp).


```go
func (rm *RepoManager) HandleExternalUserEvent((ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp)) (ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp)
```


**Тип запроса:** atproto.SyncSubscribeRepos_RepoOp


```json
{
  "action": "string",
  "cid": null,
  "path": "string",
  "prev": null
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


**Тип ответа:** pdsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** models.Uid


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


**Тип ответа:** since


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nrev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** carslice


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ops


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atproto.SyncSubscribeRepos_RepoOp


```json
{
  "action": "string",
  "cid": null,
  "path": "string",
  "prev": null
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `repomgr/repomgr.go:545`



---


[function] name: ImportNewRepo file: repomgr/repomgr.go:900 returns_error: нет description: —


### ImportNewRepo (repomgr/repomgr.go:900)


ImportNewRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid, repoDid string, r io.Reader, rev *string).


```go
func (rm *RepoManager) ImportNewRepo((ctx context.Context, user models.Uid, repoDid string, r io.Reader, rev *string)) (ctx context.Context, user models.Uid, repoDid string, r io.Reader, rev *string)
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


**Тип ответа:** repoDid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repomgr/repomgr.go:900`



---


[function] name: InitNewActor file: repomgr/repomgr.go:360 returns_error: нет description: —


### InitNewActor (repomgr/repomgr.go:360)


InitNewActor is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid, handle, did, displayname string, declcid, actortype string).


```go
func (rm *RepoManager) InitNewActor((ctx context.Context, user models.Uid, handle, did, displayname string, declcid, actortype string)) (ctx context.Context, user models.Uid, handle, did, displayname string, declcid, actortype string)
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


**Тип ответа:** handle


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** displayname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** declcid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** actortype


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repomgr/repomgr.go:360`



---


[function] name: NewRepoManager file: repomgr/repomgr.go:36 returns_error: нет description: —


### NewRepoManager (repomgr/repomgr.go:36)


NewRepoManager is a function that performs operations based on the provided parameters and returns (cs carstore.CarStore, kmgr KeyManager).


```go
func NewRepoManager((cs carstore.CarStore, kmgr KeyManager)) (cs carstore.CarStore, kmgr KeyManager)
```


**Тип ответа:** cs


```json
{
  "suggested": [],
  "topics": []
}
```


*Определено в:* `api/bsky/unspeccedgetTrendingTopics.go`


**Тип ответа:** carstore.CarStore


```json
{
  "meta": null,
  "rootDirs": [],
  "lastShardCache": {},
  "log": null
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** kmgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** KeyManager


```json
{
  "didr": {},
  "signingKey": null,
  "log": null
}
```


*Определено в:* `repomgr/keymgr/keymgr.go`


📍 *Расположение:* `repomgr/repomgr.go:36`



---


[function] name: ReadRepo file: repomgr/repomgr.go:435 returns_error: нет description: —


### ReadRepo (repomgr/repomgr.go:435)


ReadRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid, since string, w io.Writer).


```go
func (rm *RepoManager) ReadRepo((ctx context.Context, user models.Uid, since string, w io.Writer)) (ctx context.Context, user models.Uid, since string, w io.Writer)
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


**Тип ответа:** since


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `repomgr/repomgr.go:435`



---


[function] name: ResetRepo file: repomgr/repomgr.go:1177 returns_error: нет description: technically identical to TakeDownRepo, for now


### ResetRepo (repomgr/repomgr.go:1177)


technically identical to TakeDownRepo, for now


```go
func (rm *RepoManager) ResetRepo((ctx context.Context, uid models.Uid)) (ctx context.Context, uid models.Uid)
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


📍 *Расположение:* `repomgr/repomgr.go:1177`



---


[function] name: SetEventHandler file: repomgr/repomgr.go:60 returns_error: нет description: —


### SetEventHandler (repomgr/repomgr.go:60)


SetEventHandler is a method that updates data based on the provided parameters and returns (cb func(context.Context, *RepoEvent), hydrateRecords bool).


```go
func (rm *RepoManager) SetEventHandler((cb func(context.Context, *RepoEvent), hydrateRecords bool)) (cb func(context.Context, *RepoEvent), hydrateRecords bool)
```


**Тип запроса:** RepoEvent


```json
{
  "User": {},
  "OldRoot": null,
  "NewRoot": {},
  "Since": "string",
  "Rev": "string",
  "RepoSlice": [],
  "PDS": 0,
  "Ops": []
}
```


*Определено в:* `repomgr/repomgr.go`


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


**Тип ответа:** RepoEvent


```json
{
  "User": {},
  "OldRoot": null,
  "NewRoot": {},
  "Since": "string",
  "Rev": "string",
  "RepoSlice": [],
  "PDS": 0,
  "Ops": []
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип ответа:** hydrateRecords


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repomgr/repomgr.go:60`



---


[function] name: TakeDownRepo file: repomgr/repomgr.go:1169 returns_error: нет description: —


### TakeDownRepo (repomgr/repomgr.go:1169)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid models.Uid).


```go
func (rm *RepoManager) TakeDownRepo((ctx context.Context, uid models.Uid)) (ctx context.Context, uid models.Uid)
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


📍 *Расположение:* `repomgr/repomgr.go:1169`



---


[function] name: UpdateRecord file: repomgr/repomgr.go:227 returns_error: да description: —


### UpdateRecord (repomgr/repomgr.go:227)


UpdateRecord is a method that updates data based on the provided parameters and may return an error.


```go
func (rm *RepoManager) UpdateRecord((cid.Cid, error)) (cid.Cid, error)
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


*Типы возврата:* `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:227`



---


[function] name: VerifyRepo file: repomgr/repomgr.go:1184 returns_error: нет description: —


### VerifyRepo (repomgr/repomgr.go:1184)


VerifyRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid models.Uid).


```go
func (rm *RepoManager) VerifyRepo((ctx context.Context, uid models.Uid)) (ctx context.Context, uid models.Uid)
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


📍 *Расположение:* `repomgr/repomgr.go:1184`



---


[function] name: handleExternalUserEventArchive file: repomgr/repomgr.go:650 returns_error: нет description: —


### handleExternalUserEventArchive (repomgr/repomgr.go:650)


handleExternalUserEventArchive is a method that performs operations based on the provided parameters and returns (ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp).


```go
func (rm *RepoManager) handleExternalUserEventArchive((ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp)) (ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp)
```


**Тип запроса:** atproto.SyncSubscribeRepos_RepoOp


```json
{
  "action": "string",
  "cid": null,
  "path": "string",
  "prev": null
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


**Тип ответа:** pdsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** models.Uid


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


**Тип ответа:** since


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nrev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** carslice


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ops


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atproto.SyncSubscribeRepos_RepoOp


```json
{
  "action": "string",
  "cid": null,
  "path": "string",
  "prev": null
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `repomgr/repomgr.go:650`



---


[function] name: handleExternalUserEventNoArchive file: repomgr/repomgr.go:553 returns_error: нет description: —


### handleExternalUserEventNoArchive (repomgr/repomgr.go:553)


handleExternalUserEventNoArchive is a method that performs operations based on the provided parameters and returns (ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp).


```go
func (rm *RepoManager) handleExternalUserEventNoArchive((ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp)) (ctx context.Context, pdsid uint, uid models.Uid, did string, since *string, nrev string, carslice []byte, ops []*atproto.SyncSubscribeRepos_RepoOp)
```


**Тип запроса:** atproto.SyncSubscribeRepos_RepoOp


```json
{
  "action": "string",
  "cid": null,
  "path": "string",
  "prev": null
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


**Тип ответа:** pdsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** models.Uid


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


**Тип ответа:** since


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nrev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** carslice


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ops


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atproto.SyncSubscribeRepos_RepoOp


```json
{
  "action": "string",
  "cid": null,
  "path": "string",
  "prev": null
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `repomgr/repomgr.go:553`



---


[function] name: lockUser file: repomgr/repomgr.go:127 returns_error: нет description: —


### lockUser (repomgr/repomgr.go:127)


lockUser is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid).


```go
func (rm *RepoManager) lockUser((ctx context.Context, user models.Uid)) (ctx context.Context, user models.Uid)
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


📍 *Расположение:* `repomgr/repomgr.go:127`



---


[function] name: processNewRepo file: repomgr/repomgr.go:1045 returns_error: да description: —


### processNewRepo (repomgr/repomgr.go:1045)


processNewRepo is a method that performs operations based on the provided parameters and may return an error.


```go
func (rm *RepoManager) processNewRepo((ctx context.Context, user models.Uid, r io.Reader, rev *string, cb func(ctx context.Context, root cid.Cid, finish func(context.Context, string) ([]byte, error), bs blockstore.Blockstore) error)) (ctx context.Context, user models.Uid, r io.Reader, rev *string, cb func(ctx context.Context, root cid.Cid, finish func(context.Context, string) ([]byte, error), bs blockstore.Blockstore) error)
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


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


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


**Тип ответа:** root


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** finish


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


**Тип ответа:** bs


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


**Тип ответа:** blockstore.Blockstore


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `user models.Uid`, `r io.Reader`, `rev *string`, `cb func(ctx context.Context`, `root cid.Cid`, `finish func(context.Context`, `string) ([]byte`, `error)`, `bs blockstore.Blockstore) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:1045`



---


[function] name: processOp file: repomgr/repomgr.go:992 returns_error: да description: —


### processOp (repomgr/repomgr.go:992)


processOp is a method that performs operations based on the provided parameters and may return an error.


```go
func (rm *RepoManager) processOp((*RepoOp, error)) (*RepoOp, error)
```


**Тип запроса:** RepoOp


```json
{
  "Kind": {},
  "Collection": "string",
  "Rkey": "string",
  "RecCid": null,
  "Record": {},
  "ActorInfo": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип ответа:** RepoOp


```json
{
  "Kind": {},
  "Collection": "string",
  "Rkey": "string",
  "RecCid": null,
  "Record": {},
  "ActorInfo": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:992`



---


[function] name: stringOrNil file: repomgr/repomgr.go:1113 returns_error: нет description: —


### stringOrNil (repomgr/repomgr.go:1113)


stringOrNil is a function that performs operations based on the provided parameters and returns (s *string).


```go
func stringOrNil((s *string)) (s *string)
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


📍 *Расположение:* `repomgr/repomgr.go:1113`



---


[function] name: walkTree file: repomgr/repomgr.go:1122 returns_error: да description: walkTree returns all cids linked recursively by the root, skipping any cids
in the 'skip' map, and not erroring on 'not 


### walkTree (repomgr/repomgr.go:1122)


walkTree returns all cids linked recursively by the root, skipping any cids
in the 'skip' map, and not erroring on 'not found' if prevMissing is set


```go
func (rm *RepoManager) walkTree(([]cid.Cid, error)) ([]cid.Cid, error)
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


*Типы возврата:* `[]cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/repomgr.go:1122`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repo_carutil.md)

- [Следующая директория](repomgr_keymgr.md)


---

