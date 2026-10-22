---
title: "Функции: carstore"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: carstore
---


# Функции: carstore


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](backfill.md)

- [Следующая директория](cmd_beemo.md)


---


## Меню по файлам


- 📄 [carstore/bs.go](#carstorebsgo)

- 📄 [carstore/last_shard_cache.go](#carstorelast_shard_cachego)

- 📄 [carstore/meta_gorm.go](#carstoremeta_gormgo)

- 📄 [carstore/nonarchive.go](#carstorenonarchivego)

- 📄 [carstore/scylla.go](#carstorescyllago)

- 📄 [carstore/scylla_stub.go](#carstorescylla_stubgo)

- 📄 [carstore/sqlite_store.go](#carstoresqlite_storego)

- 📄 [carstore/util.go](#carstoreutilgo)


---


## carstore/bs.go


📄 Исходный файл: `carstore/bs.go`


<details open>
<summary><b>Функции в этом файле (60)</b></summary>


- 🔗 [AllKeysChan](#allkeyschan-carstorebsgo258) `:258`

- 🔗 [AllKeysChan](#allkeyschan-carstorebsgo490) `:490`

- 🔗 [BaseCid](#basecid-carstorebsgo467) `:467`

- 🔗 [BlockDiff](#blockdiff-carstorebsgo707) `:707`

- 🔗 [CalcDiff](#calcdiff-carstorebsgo809) `:809`

- 🔗 [CloseWithRoot](#closewithroot-carstorebsgo576) `:576`

- 🔗 [CompactUserShards](#compactusershards-carstorebsgo1073) `:1073`

- 🔗 [DeleteBlock](#deleteblock-carstorebsgo270) `:270`

- 🔗 [DeleteBlock](#deleteblock-carstorebsgo494) `:494`

- 🔗 [Get](#get-carstorebsgo137) `:137`

- 🔗 [Get](#get-carstorebsgo507) `:507`

- 🔗 [GetCompactionTargets](#getcompactiontargets-carstorebsgo1027) `:1027`

- 🔗 [GetSize](#getsize-carstorebsgo274) `:274`

- 🔗 [GetSize](#getsize-carstorebsgo529) `:529`

- 🔗 [GetUserRepoHead](#getuserrepohead-carstorebsgo819) `:819`

- 🔗 [GetUserRepoRev](#getuserreporev-carstorebsgo831) `:831`

- 🔗 [Has](#has-carstorebsgo126) `:126`

- 🔗 [Has](#has-carstorebsgo516) `:516`

- 🔗 [HashOnRead](#hashonread-carstorebsgo122) `:122`

- 🔗 [HashOnRead](#hashonread-carstorebsgo525) `:525`

- 🔗 [ImportSlice](#importslice-carstorebsgo771) `:771`

- 🔗 [NewCarStore](#newcarstore-carstorebsgo72) `:72`

- 🔗 [NewDeltaSession](#newdeltasession-carstorebsgo321) `:321`

- 🔗 [Put](#put-carstorebsgo262) `:262`

- 🔗 [Put](#put-carstorebsgo471) `:471`

- 🔗 [PutMany](#putmany-carstorebsgo266) `:266`

- 🔗 [PutMany](#putmany-carstorebsgo479) `:479`

- 🔗 [ReadOnlySession](#readonlysession-carstorebsgo352) `:352`

- 🔗 [ReadUserCar](#readusercar-carstorebsgo367) `:367`

- 🔗 [Stat](#stat-carstorebsgo849) `:849`

- 🔗 [WipeUserData](#wipeuserdata-carstorebsgo867) `:867`

- 🔗 [WriteCarHeader](#writecarheader-carstorebsgo587) `:587`

- 🔗 [addShardStat](#addshardstat-carstorebsgo1001) `:1001`

- 🔗 [aggrRefs](#aggrrefs-carstorebsgo939) `:939`

- 🔗 [blocksToCar](#blockstocar-carstorebsgo611) `:611`

- 🔗 [checkLastShardCache](#checklastshardcache-carstorebsgo303) `:303`

- 🔗 [compactBucket](#compactbucket-carstorebsgo1322) `:1322`

- 🔗 [deleteShardFile](#deleteshardfile-carstorebsgo570) `:570`

- 🔗 [deleteShards](#deleteshards-carstorebsgo884) `:884`

- 🔗 [deleteStaleRefs](#deletestalerefs-carstorebsgo1287) `:1287`

- 🔗 [dirForUser](#dirforuser-carstorebsgo542) `:542`

- 🔗 [dirtyFrac](#dirtyfrac-carstorebsgo935) `:935`

- 🔗 [doBlockRead](#doblockread-carstorebsgo235) `:235`

- 🔗 [fnameForShard](#fnameforshard-carstorebsgo538) `:538`

- 🔗 [getBlockRefsForShards](#getblockrefsforshards-carstorebsgo1035) `:1035`

- 🔗 [getLastShard](#getlastshard-carstorebsgo315) `:315`

- 🔗 [isEmpty](#isempty-carstorebsgo1006) `:1006`

- 🔗 [iterateShardBlocks](#iterateshardblocks-carstorebsgo438) `:438`

- 🔗 [openNewCompactedShardFile](#opennewcompactedshardfile-carstorebsgo1010) `:1010`

- 🔗 [openNewShardFile](#opennewshardfile-carstorebsgo546) `:546`

- 🔗 [prefetchRead](#prefetchread-carstorebsgo178) `:178`

- 🔗 [putLastShardCache](#putlastshardcache-carstorebsgo311) `:311`

- 🔗 [putShard](#putshard-carstorebsgo691) `:691`

- 🔗 [removeLastShardCache](#removelastshardcache-carstorebsgo307) `:307`

- 🔗 [shardSize](#shardsize-carstorebsgo1051) `:1051`

- 🔗 [shouldCompact](#shouldcompact-carstorebsgo979) `:979`

- 🔗 [singleRead](#singleread-carstorebsgo225) `:225`

- 🔗 [writeNewShard](#writenewshard-carstorebsgo628) `:628`

- 🔗 [writeNewShardFile](#writenewshardfile-carstorebsgo557) `:557`

- 🔗 [writeShardBlocks](#writeshardblocks-carstorebsgo414) `:414`


</details>


[function] name: AllKeysChan file: carstore/bs.go:258 returns_error: да description: —


### AllKeysChan (carstore/bs.go:258)


AllKeysChan is a method that performs operations based on the provided parameters and may return an error.


```go
func (uv *userView) AllKeysChan((<-chan cid.Cid, error)) (<-chan cid.Cid, error)
```


**Тип ответа:** chan


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


*Типы возврата:* `<-chan cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:258`



---


[function] name: AllKeysChan file: carstore/bs.go:490 returns_error: да description: —


### AllKeysChan (carstore/bs.go:490)


AllKeysChan is a method that performs operations based on the provided parameters and may return an error.


```go
func (ds *DeltaSession) AllKeysChan((<-chan cid.Cid, error)) (<-chan cid.Cid, error)
```


**Тип ответа:** chan


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


*Типы возврата:* `<-chan cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:490`



---


[function] name: BaseCid file: carstore/bs.go:467 returns_error: нет description: —


### BaseCid (carstore/bs.go:467)


BaseCid is a method that performs operations based on the provided parameters and returns ().


```go
func (ds *DeltaSession) BaseCid(()) ()
```


📍 *Расположение:* `carstore/bs.go:467`



---


[function] name: BlockDiff file: carstore/bs.go:707 returns_error: да description: —


### BlockDiff (carstore/bs.go:707)


BlockDiff is a function that performs operations based on the provided parameters and may return an error.


```go
func BlockDiff((map[cid.Cid]bool, error)) (map[cid.Cid]bool, error)
```


**Тип ответа:** map


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


*Типы возврата:* `map[cid.Cid]bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:707`



---


[function] name: CalcDiff file: carstore/bs.go:809 returns_error: нет description: —


### CalcDiff (carstore/bs.go:809)


CalcDiff is a method that performs operations based on the provided parameters and returns (ctx context.Context, skipcids map[cid.Cid]bool).


```go
func (ds *DeltaSession) CalcDiff((ctx context.Context, skipcids map[cid.Cid]bool)) (ctx context.Context, skipcids map[cid.Cid]bool)
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


**Тип ответа:** skipcids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/bs.go:809`



---


[function] name: CloseWithRoot file: carstore/bs.go:576 returns_error: да description: CloseWithRoot writes all new blocks in a car file to the writer with the
given cid as the 'root'


### CloseWithRoot (carstore/bs.go:576)


CloseWithRoot writes all new blocks in a car file to the writer with the
given cid as the 'root'


```go
func (ds *DeltaSession) CloseWithRoot(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:576`



---


[function] name: CompactUserShards file: carstore/bs.go:1073 returns_error: да description: —


### CompactUserShards (carstore/bs.go:1073)


CompactUserShards is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) CompactUserShards((*CompactionStats, error)) (*CompactionStats, error)
```


**Тип запроса:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CompactionStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:1073`



---


[function] name: DeleteBlock file: carstore/bs.go:270 returns_error: нет description: —


### DeleteBlock (carstore/bs.go:270)


DeleteBlock is a method that deletes data based on the provided parameters and returns (ctx context.Context, k cid.Cid).


```go
func (uv *userView) DeleteBlock((ctx context.Context, k cid.Cid)) (ctx context.Context, k cid.Cid)
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


**Тип ответа:** k


```json
{
  "logger": null,
  "webhookURL": "string",
  "adminPassword": "string",
  "httpClient": null
}
```


*Определено в:* `cmd/tap/webhook_client.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/bs.go:270`



---


[function] name: DeleteBlock file: carstore/bs.go:494 returns_error: нет description: —


### DeleteBlock (carstore/bs.go:494)


DeleteBlock is a method that deletes data based on the provided parameters and returns (ctx context.Context, c cid.Cid).


```go
func (ds *DeltaSession) DeleteBlock((ctx context.Context, c cid.Cid)) (ctx context.Context, c cid.Cid)
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


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/bs.go:494`



---


[function] name: Get file: carstore/bs.go:137 returns_error: да description: —


### Get (carstore/bs.go:137)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (uv *userView) Get((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:137`



---


[function] name: Get file: carstore/bs.go:507 returns_error: да description: —


### Get (carstore/bs.go:507)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (ds *DeltaSession) Get((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:507`



---


[function] name: GetCompactionTargets file: carstore/bs.go:1027 returns_error: да description: —


### GetCompactionTargets (carstore/bs.go:1027)


GetCompactionTargets is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) GetCompactionTargets(([]CompactionTarget, error)) ([]CompactionTarget, error)
```


**Тип ответа:** CompactionTarget


```json
{
  "Usr": {},
  "NumShards": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]CompactionTarget`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:1027`



---


[function] name: GetSize file: carstore/bs.go:274 returns_error: да description: —


### GetSize (carstore/bs.go:274)


GetSize is a method that retrieves data based on the provided parameters and may return an error.


```go
func (uv *userView) GetSize((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:274`



---


[function] name: GetSize file: carstore/bs.go:529 returns_error: да description: —


### GetSize (carstore/bs.go:529)


GetSize is a method that retrieves data based on the provided parameters and may return an error.


```go
func (ds *DeltaSession) GetSize((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:529`



---


[function] name: GetUserRepoHead file: carstore/bs.go:819 returns_error: да description: —


### GetUserRepoHead (carstore/bs.go:819)


GetUserRepoHead is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) GetUserRepoHead((cid.Cid, error)) (cid.Cid, error)
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


📍 *Расположение:* `carstore/bs.go:819`



---


[function] name: GetUserRepoRev file: carstore/bs.go:831 returns_error: да description: —


### GetUserRepoRev (carstore/bs.go:831)


GetUserRepoRev is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) GetUserRepoRev((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:831`



---


[function] name: Has file: carstore/bs.go:126 returns_error: да description: —


### Has (carstore/bs.go:126)


Has is a method that performs operations based on the provided parameters and may return an error.


```go
func (uv *userView) Has((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:126`



---


[function] name: Has file: carstore/bs.go:516 returns_error: да description: —


### Has (carstore/bs.go:516)


Has is a method that performs operations based on the provided parameters and may return an error.


```go
func (ds *DeltaSession) Has((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:516`



---


[function] name: HashOnRead file: carstore/bs.go:122 returns_error: нет description: —


### HashOnRead (carstore/bs.go:122)


HashOnRead is a method that performs operations based on the provided parameters and returns (hor bool).


```go
func (uv *userView) HashOnRead((hor bool)) (hor bool)
```


**Тип ответа:** hor


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetAuthorFeed.go`


📍 *Расположение:* `carstore/bs.go:122`



---


[function] name: HashOnRead file: carstore/bs.go:525 returns_error: нет description: —


### HashOnRead (carstore/bs.go:525)


HashOnRead is a method that performs operations based on the provided parameters and returns (hor bool).


```go
func (ds *DeltaSession) HashOnRead((hor bool)) (hor bool)
```


**Тип ответа:** hor


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetAuthorFeed.go`


📍 *Расположение:* `carstore/bs.go:525`



---


[function] name: ImportSlice file: carstore/bs.go:771 returns_error: да description: —


### ImportSlice (carstore/bs.go:771)


ImportSlice is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) ImportSlice((cid.Cid, *DeltaSession, error)) (cid.Cid, *DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:771`



---


[function] name: NewCarStore file: carstore/bs.go:72 returns_error: да description: —


### NewCarStore (carstore/bs.go:72)


NewCarStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewCarStore((CarStore, error)) (CarStore, error)
```


**Тип ответа:** CarStore


```json
{
  "meta": null,
  "rootDirs": [],
  "lastShardCache": {},
  "log": null
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CarStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:72`



---


[function] name: NewDeltaSession file: carstore/bs.go:321 returns_error: да description: —


### NewDeltaSession (carstore/bs.go:321)


NewDeltaSession is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) NewDeltaSession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:321`



---


[function] name: Put file: carstore/bs.go:262 returns_error: нет description: —


### Put (carstore/bs.go:262)


Put is a method that performs operations based on the provided parameters and returns (ctx context.Context, blk blockformat.Block).


```go
func (uv *userView) Put((ctx context.Context, blk blockformat.Block)) (ctx context.Context, blk blockformat.Block)
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


**Тип ответа:** blk


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `carstore/bs.go:262`



---


[function] name: Put file: carstore/bs.go:471 returns_error: нет description: —


### Put (carstore/bs.go:471)


Put is a method that performs operations based on the provided parameters and returns (ctx context.Context, b blockformat.Block).


```go
func (ds *DeltaSession) Put((ctx context.Context, b blockformat.Block)) (ctx context.Context, b blockformat.Block)
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


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `carstore/bs.go:471`



---


[function] name: PutMany file: carstore/bs.go:266 returns_error: нет description: —


### PutMany (carstore/bs.go:266)


PutMany is a method that performs operations based on the provided parameters and returns (ctx context.Context, blks []blockformat.Block).


```go
func (uv *userView) PutMany((ctx context.Context, blks []blockformat.Block)) (ctx context.Context, blks []blockformat.Block)
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


**Тип ответа:** blks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `carstore/bs.go:266`



---


[function] name: PutMany file: carstore/bs.go:479 returns_error: нет description: —


### PutMany (carstore/bs.go:479)


PutMany is a method that performs operations based on the provided parameters and returns (ctx context.Context, bs []blockformat.Block).


```go
func (ds *DeltaSession) PutMany((ctx context.Context, bs []blockformat.Block)) (ctx context.Context, bs []blockformat.Block)
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


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `carstore/bs.go:479`



---


[function] name: ReadOnlySession file: carstore/bs.go:352 returns_error: да description: —


### ReadOnlySession (carstore/bs.go:352)


ReadOnlySession is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) ReadOnlySession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:352`



---


[function] name: ReadUserCar file: carstore/bs.go:367 returns_error: нет description: TODO: incremental is only ever called true, remove the param


### ReadUserCar (carstore/bs.go:367)


TODO: incremental is only ever called true, remove the param


```go
func (cs *FileCarStore) ReadUserCar((ctx context.Context, user models.Uid, sinceRev string, incremental bool, shardOut io.Writer)) (ctx context.Context, user models.Uid, sinceRev string, incremental bool, shardOut io.Writer)
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


**Тип ответа:** sinceRev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** incremental


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shardOut


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/bs.go:367`



---


[function] name: Stat file: carstore/bs.go:849 returns_error: да description: —


### Stat (carstore/bs.go:849)


Stat is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) Stat(([]UserStat, error)) ([]UserStat, error)
```


**Тип ответа:** UserStat


```json
{
  "Seq": 0,
  "Root": "string",
  "Created": {}
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]UserStat`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:849`



---


[function] name: WipeUserData file: carstore/bs.go:867 returns_error: нет description: —


### WipeUserData (carstore/bs.go:867)


WipeUserData is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid).


```go
func (cs *FileCarStore) WipeUserData((ctx context.Context, user models.Uid)) (ctx context.Context, user models.Uid)
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


📍 *Расположение:* `carstore/bs.go:867`



---


[function] name: WriteCarHeader file: carstore/bs.go:587 returns_error: да description: —


### WriteCarHeader (carstore/bs.go:587)


WriteCarHeader is a function that performs operations based on the provided parameters and may return an error.


```go
func WriteCarHeader((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:587`



---


[function] name: addShardStat file: carstore/bs.go:1001 returns_error: нет description: —


### addShardStat (carstore/bs.go:1001)


addShardStat is a method that performs operations based on the provided parameters and returns (ss shardStat).


```go
func (cb *compBucket) addShardStat((ss shardStat)) (ss shardStat)
```


**Тип ответа:** ss


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


**Тип ответа:** shardStat


```json
{
  "ID": 0,
  "Dirty": 0,
  "Seq": 0,
  "Total": 0,
  "refs": []
}
```


*Определено в:* `carstore/bs.go`


📍 *Расположение:* `carstore/bs.go:1001`



---


[function] name: aggrRefs file: carstore/bs.go:939 returns_error: нет description: —


### aggrRefs (carstore/bs.go:939)


aggrRefs is a function that performs operations based on the provided parameters and returns (brefs []blockRef, shards map[uint]CarShard, staleCids map[cid.Cid]bool).


```go
func aggrRefs((brefs []blockRef, shards map[uint]CarShard, staleCids map[cid.Cid]bool)) (brefs []blockRef, shards map[uint]CarShard, staleCids map[cid.Cid]bool)
```


**Тип ответа:** brefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blockRef


```json
{
  "ID": 0,
  "Cid": {},
  "Shard": 0,
  "Offset": 0
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** shards


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** staleCids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/bs.go:939`



---


[function] name: blocksToCar file: carstore/bs.go:611 returns_error: да description: —


### blocksToCar (carstore/bs.go:611)


blocksToCar is a function that performs operations based on the provided parameters and may return an error.


```go
func blocksToCar(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:611`



---


[function] name: checkLastShardCache file: carstore/bs.go:303 returns_error: нет description: —


### checkLastShardCache (carstore/bs.go:303)


checkLastShardCache is a method that performs operations based on the provided parameters and returns (user models.Uid).


```go
func (cs *FileCarStore) checkLastShardCache((user models.Uid)) (user models.Uid)
```


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


📍 *Расположение:* `carstore/bs.go:303`



---


[function] name: compactBucket file: carstore/bs.go:1322 returns_error: нет description: —


### compactBucket (carstore/bs.go:1322)


compactBucket is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid, b *compBucket, shardsById map[uint]CarShard, keep map[cid.Cid]bool).


```go
func (cs *FileCarStore) compactBucket((ctx context.Context, user models.Uid, b *compBucket, shardsById map[uint]CarShard, keep map[cid.Cid]bool)) (ctx context.Context, user models.Uid, b *compBucket, shardsById map[uint]CarShard, keep map[cid.Cid]bool)
```


**Тип запроса:** compBucket


```json
{
  "shards": [],
  "cleanBlocks": 0,
  "expSize": 0
}
```


*Определено в:* `carstore/bs.go`


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


**Тип ответа:** compBucket


```json
{
  "shards": [],
  "cleanBlocks": 0,
  "expSize": 0
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** shardsById


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** keep


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/bs.go:1322`



---


[function] name: deleteShardFile file: carstore/bs.go:570 returns_error: нет description: —


### deleteShardFile (carstore/bs.go:570)


deleteShardFile is a method that performs operations based on the provided parameters and returns (ctx context.Context, sh *CarShard).


```go
func (cs *FileCarStore) deleteShardFile((ctx context.Context, sh *CarShard)) (ctx context.Context, sh *CarShard)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


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


**Тип ответа:** sh


```json
{
  "cs": null,
  "l": {},
  "obsolete": false,
  "freshCache": {}
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


📍 *Расположение:* `carstore/bs.go:570`



---


[function] name: deleteShards file: carstore/bs.go:884 returns_error: нет description: —


### deleteShards (carstore/bs.go:884)


deleteShards is a method that performs operations based on the provided parameters and returns (ctx context.Context, shs []CarShard).


```go
func (cs *FileCarStore) deleteShards((ctx context.Context, shs []CarShard)) (ctx context.Context, shs []CarShard)
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


**Тип ответа:** shs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


📍 *Расположение:* `carstore/bs.go:884`



---


[function] name: deleteStaleRefs file: carstore/bs.go:1287 returns_error: нет description: —


### deleteStaleRefs (carstore/bs.go:1287)


deleteStaleRefs is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid models.Uid, brefs []blockRef, staleRefs []staleRef, removedShards map[uint]bool).


```go
func (cs *FileCarStore) deleteStaleRefs((ctx context.Context, uid models.Uid, brefs []blockRef, staleRefs []staleRef, removedShards map[uint]bool)) (ctx context.Context, uid models.Uid, brefs []blockRef, staleRefs []staleRef, removedShards map[uint]bool)
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


**Тип ответа:** brefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blockRef


```json
{
  "ID": 0,
  "Cid": {},
  "Shard": 0,
  "Offset": 0
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** staleRefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** staleRef


```json
{
  "ID": 0,
  "Cid": null,
  "Cids": [],
  "Usr": {}
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** removedShards


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/bs.go:1287`



---


[function] name: dirForUser file: carstore/bs.go:542 returns_error: нет description: —


### dirForUser (carstore/bs.go:542)


dirForUser is a method that performs operations based on the provided parameters and returns (user models.Uid).


```go
func (cs *FileCarStore) dirForUser((user models.Uid)) (user models.Uid)
```


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


📍 *Расположение:* `carstore/bs.go:542`



---


[function] name: dirtyFrac file: carstore/bs.go:935 returns_error: нет description: —


### dirtyFrac (carstore/bs.go:935)


dirtyFrac is a method that performs operations based on the provided parameters and returns ().


```go
func (s shardStat) dirtyFrac(()) ()
```


📍 *Расположение:* `carstore/bs.go:935`



---


[function] name: doBlockRead file: carstore/bs.go:235 returns_error: да description: —


### doBlockRead (carstore/bs.go:235)


doBlockRead is a function that performs operations based on the provided parameters and may return an error.


```go
func doBlockRead((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:235`



---


[function] name: fnameForShard file: carstore/bs.go:538 returns_error: нет description: —


### fnameForShard (carstore/bs.go:538)


fnameForShard is a function that performs operations based on the provided parameters and returns (user models.Uid, seq int).


```go
func fnameForShard((user models.Uid, seq int)) (user models.Uid, seq int)
```


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


**Тип ответа:** seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/bs.go:538`



---


[function] name: getBlockRefsForShards file: carstore/bs.go:1035 returns_error: да description: getBlockRefsForShards is a prep function for CompactUserShards


### getBlockRefsForShards (carstore/bs.go:1035)


getBlockRefsForShards is a prep function for CompactUserShards


```go
func (cs *FileCarStore) getBlockRefsForShards(([]blockRef, error)) ([]blockRef, error)
```


**Тип ответа:** blockRef


```json
{
  "ID": 0,
  "Cid": {},
  "Shard": 0,
  "Offset": 0
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]blockRef`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:1035`



---


[function] name: getLastShard file: carstore/bs.go:315 returns_error: да description: —


### getLastShard (carstore/bs.go:315)


getLastShard is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) getLastShard((*CarShard, error)) (*CarShard, error)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CarShard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:315`



---


[function] name: isEmpty file: carstore/bs.go:1006 returns_error: нет description: —


### isEmpty (carstore/bs.go:1006)


isEmpty is a method that performs operations based on the provided parameters and returns ().


```go
func (cb *compBucket) isEmpty(()) ()
```


📍 *Расположение:* `carstore/bs.go:1006`



---


[function] name: iterateShardBlocks file: carstore/bs.go:438 returns_error: да description: inner loop part of compactBucket


### iterateShardBlocks (carstore/bs.go:438)


inner loop part of compactBucket


```go
func (cs *FileCarStore) iterateShardBlocks((ctx context.Context, sh *CarShard, cb func(blk blockformat.Block) error)) (ctx context.Context, sh *CarShard, cb func(blk blockformat.Block) error)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


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


**Тип ответа:** sh


```json
{
  "cs": null,
  "l": {},
  "obsolete": false,
  "freshCache": {}
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blk


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `sh *CarShard`, `cb func(blk blockformat.Block) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:438`



---


[function] name: openNewCompactedShardFile file: carstore/bs.go:1010 returns_error: да description: —


### openNewCompactedShardFile (carstore/bs.go:1010)


openNewCompactedShardFile is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) openNewCompactedShardFile((*os.File, string, error)) (*os.File, string, error)
```


**Тип запроса:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*os.File`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:1010`



---


[function] name: openNewShardFile file: carstore/bs.go:546 returns_error: да description: —


### openNewShardFile (carstore/bs.go:546)


openNewShardFile is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) openNewShardFile((*os.File, string, error)) (*os.File, string, error)
```


**Тип запроса:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*os.File`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:546`



---


[function] name: prefetchRead file: carstore/bs.go:178 returns_error: да description: —


### prefetchRead (carstore/bs.go:178)


prefetchRead is a method that performs operations based on the provided parameters and may return an error.


```go
func (uv *userView) prefetchRead((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:178`



---


[function] name: putLastShardCache file: carstore/bs.go:311 returns_error: нет description: —


### putLastShardCache (carstore/bs.go:311)


putLastShardCache is a method that performs operations based on the provided parameters and returns (ls *CarShard).


```go
func (cs *FileCarStore) putLastShardCache((ls *CarShard)) (ls *CarShard)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** ls


```json
{
  "ModerationDefsImagedetails": null,
  "ModerationDefsVideodetails": null
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


📍 *Расположение:* `carstore/bs.go:311`



---


[function] name: putShard file: carstore/bs.go:691 returns_error: нет description: —


### putShard (carstore/bs.go:691)


putShard is a method that performs operations based on the provided parameters and returns (ctx context.Context, shard *CarShard, brefs []map[string]any, rmcids map[cid.Cid]bool, nocache bool).


```go
func (cs *FileCarStore) putShard((ctx context.Context, shard *CarShard, brefs []map[string]any, rmcids map[cid.Cid]bool, nocache bool)) (ctx context.Context, shard *CarShard, brefs []map[string]any, rmcids map[cid.Cid]bool, nocache bool)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


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


**Тип ответа:** shard


```json
{
  "ID": 0,
  "Dirty": 0,
  "Seq": 0,
  "Total": 0,
  "refs": []
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** brefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rmcids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** nocache


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/bs.go:691`



---


[function] name: removeLastShardCache file: carstore/bs.go:307 returns_error: нет description: —


### removeLastShardCache (carstore/bs.go:307)


removeLastShardCache is a method that performs operations based on the provided parameters and returns (user models.Uid).


```go
func (cs *FileCarStore) removeLastShardCache((user models.Uid)) (user models.Uid)
```


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


📍 *Расположение:* `carstore/bs.go:307`



---


[function] name: shardSize file: carstore/bs.go:1051 returns_error: да description: —


### shardSize (carstore/bs.go:1051)


shardSize is a function that performs operations based on the provided parameters and may return an error.


```go
func shardSize((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:1051`



---


[function] name: shouldCompact file: carstore/bs.go:979 returns_error: нет description: —


### shouldCompact (carstore/bs.go:979)


shouldCompact is a method that performs operations based on the provided parameters and returns ().


```go
func (cb *compBucket) shouldCompact(()) ()
```


📍 *Расположение:* `carstore/bs.go:979`



---


[function] name: singleRead file: carstore/bs.go:225 returns_error: да description: —


### singleRead (carstore/bs.go:225)


singleRead is a method that performs operations based on the provided parameters and may return an error.


```go
func (uv *userView) singleRead((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:225`



---


[function] name: writeNewShard file: carstore/bs.go:628 returns_error: да description: —


### writeNewShard (carstore/bs.go:628)


writeNewShard is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) writeNewShard(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:628`



---


[function] name: writeNewShardFile file: carstore/bs.go:557 returns_error: да description: —


### writeNewShardFile (carstore/bs.go:557)


writeNewShardFile is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *FileCarStore) writeNewShardFile((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/bs.go:557`



---


[function] name: writeShardBlocks file: carstore/bs.go:414 returns_error: нет description: inner loop part of ReadUserCar
copy shard blocks from disk to Writer


### writeShardBlocks (carstore/bs.go:414)


inner loop part of ReadUserCar
copy shard blocks from disk to Writer


```go
func (cs *FileCarStore) writeShardBlocks((ctx context.Context, sh *CarShard, shardOut io.Writer)) (ctx context.Context, sh *CarShard, shardOut io.Writer)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


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


**Тип ответа:** sh


```json
{
  "cs": null,
  "l": {},
  "obsolete": false,
  "freshCache": {}
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** shardOut


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/bs.go:414`




## carstore/last_shard_cache.go


📄 Исходный файл: `carstore/last_shard_cache.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Init](#init-carstorelast_shard_cachego21) `:21`

- 🔗 [check](#check-carstorelast_shard_cachego25) `:25`

- 🔗 [get](#get-carstorelast_shard_cachego54) `:54`

- 🔗 [put](#put-carstorelast_shard_cachego44) `:44`

- 🔗 [remove](#remove-carstorelast_shard_cachego37) `:37`


</details>


[function] name: Init file: carstore/last_shard_cache.go:21 returns_error: нет description: —


### Init (carstore/last_shard_cache.go:21)


Init is a method that performs operations based on the provided parameters and returns ().


```go
func (lsc *lastShardCache) Init(()) ()
```


📍 *Расположение:* `carstore/last_shard_cache.go:21`



---


[function] name: check file: carstore/last_shard_cache.go:25 returns_error: нет description: —


### check (carstore/last_shard_cache.go:25)


check is a method that performs operations based on the provided parameters and returns (user models.Uid).


```go
func (lsc *lastShardCache) check((user models.Uid)) (user models.Uid)
```


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


📍 *Расположение:* `carstore/last_shard_cache.go:25`



---


[function] name: get file: carstore/last_shard_cache.go:54 returns_error: да description: —


### get (carstore/last_shard_cache.go:54)


get is a method that performs operations based on the provided parameters and may return an error.


```go
func (lsc *lastShardCache) get((*CarShard, error)) (*CarShard, error)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CarShard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/last_shard_cache.go:54`



---


[function] name: put file: carstore/last_shard_cache.go:44 returns_error: нет description: —


### put (carstore/last_shard_cache.go:44)


put is a method that performs operations based on the provided parameters and returns (ls *CarShard).


```go
func (lsc *lastShardCache) put((ls *CarShard)) (ls *CarShard)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** ls


```json
{
  "ModerationDefsImagedetails": null,
  "ModerationDefsVideodetails": null
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


📍 *Расположение:* `carstore/last_shard_cache.go:44`



---


[function] name: remove file: carstore/last_shard_cache.go:37 returns_error: нет description: —


### remove (carstore/last_shard_cache.go:37)


remove is a method that performs operations based on the provided parameters and returns (user models.Uid).


```go
func (lsc *lastShardCache) remove((user models.Uid)) (user models.Uid)
```


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


📍 *Расположение:* `carstore/last_shard_cache.go:37`




## carstore/meta_gorm.go


📄 Исходный файл: `carstore/meta_gorm.go`


<details open>
<summary><b>Функции в этом файле (21)</b></summary>


- 🔗 [DeleteShardsAndRefs](#deleteshardsandrefs-carstoremeta_gormgo162) `:162`

- 🔗 [GetBlockRefsForShards](#getblockrefsforshards-carstoremeta_gormgo178) `:178`

- 🔗 [GetCompactionTargets](#getcompactiontargets-carstoremeta_gormgo115) `:115`

- 🔗 [GetLastShard](#getlastshard-carstoremeta_gormgo73) `:73`

- 🔗 [GetUserShards](#getusershards-carstoremeta_gormgo82) `:82`

- 🔗 [GetUserShardsDesc](#getusershardsdesc-carstoremeta_gormgo91) `:91`

- 🔗 [GetUserStaleRefs](#getuserstalerefs-carstoremeta_gormgo99) `:99`

- 🔗 [HasUidCid](#hasuidcid-carstoremeta_gormgo34) `:34`

- 🔗 [Init](#init-carstoremeta_gormgo23) `:23`

- 🔗 [LookupBlockRef](#lookupblockref-carstoremeta_gormgo50) `:50`

- 🔗 [PutShardAndRefs](#putshardandrefs-carstoremeta_gormgo124) `:124`

- 🔗 [SeqForRev](#seqforrev-carstoremeta_gormgo107) `:107`

- 🔗 [SetStaleRef](#setstaleref-carstoremeta_gormgo221) `:221`

- 🔗 [blockRefsForShards](#blockrefsforshards-carstoremeta_gormgo195) `:195`

- 🔗 [createBlockRefs](#createblockrefs-carstoremeta_gormgo306) `:306`

- 🔗 [createInBatches](#createinbatches-carstoremeta_gormgo318) `:318`

- 🔗 [generateInsertQuery](#generateinsertquery-carstoremeta_gormgo334) `:334`

- 🔗 [getCids](#getcids-carstoremeta_gormgo271) `:271`

- 🔗 [packCids](#packcids-carstoremeta_gormgo297) `:297`

- 🔗 [unpackCids](#unpackcids-carstoremeta_gormgo279) `:279`

- 🔗 [valuesStatementForShards](#valuesstatementforshards-carstoremeta_gormgo208) `:208`


</details>


[function] name: DeleteShardsAndRefs file: carstore/meta_gorm.go:162 returns_error: нет description: —


### DeleteShardsAndRefs (carstore/meta_gorm.go:162)


DeleteShardsAndRefs is a method that deletes data based on the provided parameters and returns (ctx context.Context, ids []uint).


```go
func (cs *CarStoreGormMeta) DeleteShardsAndRefs((ctx context.Context, ids []uint)) (ctx context.Context, ids []uint)
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


📍 *Расположение:* `carstore/meta_gorm.go:162`



---


[function] name: GetBlockRefsForShards file: carstore/meta_gorm.go:178 returns_error: да description: —


### GetBlockRefsForShards (carstore/meta_gorm.go:178)


GetBlockRefsForShards is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *CarStoreGormMeta) GetBlockRefsForShards(([]blockRef, error)) ([]blockRef, error)
```


**Тип ответа:** blockRef


```json
{
  "ID": 0,
  "Cid": {},
  "Shard": 0,
  "Offset": 0
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]blockRef`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:178`



---


[function] name: GetCompactionTargets file: carstore/meta_gorm.go:115 returns_error: да description: —


### GetCompactionTargets (carstore/meta_gorm.go:115)


GetCompactionTargets is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *CarStoreGormMeta) GetCompactionTargets(([]CompactionTarget, error)) ([]CompactionTarget, error)
```


**Тип ответа:** CompactionTarget


```json
{
  "Usr": {},
  "NumShards": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]CompactionTarget`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:115`



---


[function] name: GetLastShard file: carstore/meta_gorm.go:73 returns_error: да description: —


### GetLastShard (carstore/meta_gorm.go:73)


GetLastShard is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *CarStoreGormMeta) GetLastShard((*CarShard, error)) (*CarShard, error)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CarShard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:73`



---


[function] name: GetUserShards file: carstore/meta_gorm.go:82 returns_error: да description: return all of a users's shards, ascending by Seq


### GetUserShards (carstore/meta_gorm.go:82)


return all of a users's shards, ascending by Seq


```go
func (cs *CarStoreGormMeta) GetUserShards(([]CarShard, error)) ([]CarShard, error)
```


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]CarShard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:82`



---


[function] name: GetUserShardsDesc file: carstore/meta_gorm.go:91 returns_error: да description: return all of a users's shards, descending by Seq


### GetUserShardsDesc (carstore/meta_gorm.go:91)


return all of a users's shards, descending by Seq


```go
func (cs *CarStoreGormMeta) GetUserShardsDesc(([]CarShard, error)) ([]CarShard, error)
```


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]CarShard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:91`



---


[function] name: GetUserStaleRefs file: carstore/meta_gorm.go:99 returns_error: да description: —


### GetUserStaleRefs (carstore/meta_gorm.go:99)


GetUserStaleRefs is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *CarStoreGormMeta) GetUserStaleRefs(([]staleRef, error)) ([]staleRef, error)
```


**Тип ответа:** staleRef


```json
{
  "ID": 0,
  "Cid": null,
  "Cids": [],
  "Usr": {}
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]staleRef`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:99`



---


[function] name: HasUidCid file: carstore/meta_gorm.go:34 returns_error: да description: Return true if any known record matches (Uid, Cid)


### HasUidCid (carstore/meta_gorm.go:34)


Return true if any known record matches (Uid, Cid)


```go
func (cs *CarStoreGormMeta) HasUidCid((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:34`



---


[function] name: Init file: carstore/meta_gorm.go:23 returns_error: нет description: —


### Init (carstore/meta_gorm.go:23)


Init is a method that performs operations based on the provided parameters and returns ().


```go
func (cs *CarStoreGormMeta) Init(()) ()
```


📍 *Расположение:* `carstore/meta_gorm.go:23`



---


[function] name: LookupBlockRef file: carstore/meta_gorm.go:50 returns_error: да description: For some Cid, lookup the block ref.
Return the path of the file written, the offset within the file, and the user associ


### LookupBlockRef (carstore/meta_gorm.go:50)


For some Cid, lookup the block ref.
Return the path of the file written, the offset within the file, and the user associated with the Cid.


```go
func (cs *CarStoreGormMeta) LookupBlockRef((path string, offset int64, user models.Uid, err error)) (path string, offset int64, user models.Uid, err error)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** offset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `path string`, `offset int64`, `user models.Uid`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:50`



---


[function] name: PutShardAndRefs file: carstore/meta_gorm.go:124 returns_error: нет description: —


### PutShardAndRefs (carstore/meta_gorm.go:124)


PutShardAndRefs is a method that performs operations based on the provided parameters and returns (ctx context.Context, shard *CarShard, brefs []map[string]any, rmcids map[cid.Cid]bool).


```go
func (cs *CarStoreGormMeta) PutShardAndRefs((ctx context.Context, shard *CarShard, brefs []map[string]any, rmcids map[cid.Cid]bool)) (ctx context.Context, shard *CarShard, brefs []map[string]any, rmcids map[cid.Cid]bool)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


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


**Тип ответа:** shard


```json
{
  "ID": 0,
  "Dirty": 0,
  "Seq": 0,
  "Total": 0,
  "refs": []
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** brefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rmcids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/meta_gorm.go:124`



---


[function] name: SeqForRev file: carstore/meta_gorm.go:107 returns_error: да description: —


### SeqForRev (carstore/meta_gorm.go:107)


SeqForRev is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *CarStoreGormMeta) SeqForRev((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/meta_gorm.go:107`



---


[function] name: SetStaleRef file: carstore/meta_gorm.go:221 returns_error: нет description: —


### SetStaleRef (carstore/meta_gorm.go:221)


SetStaleRef is a method that updates data based on the provided parameters and returns (ctx context.Context, uid models.Uid, staleToKeep []cid.Cid).


```go
func (cs *CarStoreGormMeta) SetStaleRef((ctx context.Context, uid models.Uid, staleToKeep []cid.Cid)) (ctx context.Context, uid models.Uid, staleToKeep []cid.Cid)
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


**Тип ответа:** staleToKeep


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/meta_gorm.go:221`



---


[function] name: blockRefsForShards file: carstore/meta_gorm.go:195 returns_error: нет description: blockRefsForShards is an inner loop helper for GetBlockRefsForShards


### blockRefsForShards (carstore/meta_gorm.go:195)


blockRefsForShards is an inner loop helper for GetBlockRefsForShards


```go
func blockRefsForShards((ctx context.Context, db *gorm.DB, shards []uint, obuf *[]blockRef)) (ctx context.Context, db *gorm.DB, shards []uint, obuf *[]blockRef)
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


**Тип ответа:** shards


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** obuf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blockRef


```json
{
  "ID": 0,
  "Cid": {},
  "Shard": 0,
  "Offset": 0
}
```


*Определено в:* `carstore/meta_gorm.go`


📍 *Расположение:* `carstore/meta_gorm.go:195`



---


[function] name: createBlockRefs file: carstore/meta_gorm.go:306 returns_error: нет description: —


### createBlockRefs (carstore/meta_gorm.go:306)


createBlockRefs is a function that performs operations based on the provided parameters and returns (ctx context.Context, tx *gorm.DB, brefs []map[string]any).


```go
func createBlockRefs((ctx context.Context, tx *gorm.DB, brefs []map[string]any)) (ctx context.Context, tx *gorm.DB, brefs []map[string]any)
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


**Тип ответа:** brefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/meta_gorm.go:306`



---


[function] name: createInBatches file: carstore/meta_gorm.go:318 returns_error: нет description: Function to create in batches


### createInBatches (carstore/meta_gorm.go:318)


Function to create in batches


```go
func createInBatches((ctx context.Context, tx *gorm.DB, brefs []map[string]any, batchSize int)) (ctx context.Context, tx *gorm.DB, brefs []map[string]any, batchSize int)
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


**Тип ответа:** brefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** batchSize


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/meta_gorm.go:318`



---


[function] name: generateInsertQuery file: carstore/meta_gorm.go:334 returns_error: нет description: —


### generateInsertQuery (carstore/meta_gorm.go:334)


generateInsertQuery is a function that performs operations based on the provided parameters and returns (string, []any).


```go
func generateInsertQuery((string, []any)) (string, []any)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/meta_gorm.go:334`



---


[function] name: getCids file: carstore/meta_gorm.go:271 returns_error: да description: —


### getCids (carstore/meta_gorm.go:271)


getCids is a method that performs operations based on the provided parameters and may return an error.


```go
func (sr *staleRef) getCids(([]cid.Cid, error)) ([]cid.Cid, error)
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


📍 *Расположение:* `carstore/meta_gorm.go:271`



---


[function] name: packCids file: carstore/meta_gorm.go:297 returns_error: нет description: —


### packCids (carstore/meta_gorm.go:297)


packCids is a function that performs operations based on the provided parameters and returns (cids []cid.Cid).


```go
func packCids((cids []cid.Cid)) (cids []cid.Cid)
```


**Тип ответа:** cids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `carstore/meta_gorm.go:297`



---


[function] name: unpackCids file: carstore/meta_gorm.go:279 returns_error: да description: —


### unpackCids (carstore/meta_gorm.go:279)


unpackCids is a function that performs operations based on the provided parameters and may return an error.


```go
func unpackCids(([]cid.Cid, error)) ([]cid.Cid, error)
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


📍 *Расположение:* `carstore/meta_gorm.go:279`



---


[function] name: valuesStatementForShards file: carstore/meta_gorm.go:208 returns_error: нет description: valuesStatementForShards builds a postgres compatible statement string from int literals


### valuesStatementForShards (carstore/meta_gorm.go:208)


valuesStatementForShards builds a postgres compatible statement string from int literals


```go
func valuesStatementForShards((shards []uint)) (shards []uint)
```


**Тип ответа:** shards


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/meta_gorm.go:208`




## carstore/nonarchive.go


📄 Исходный файл: `carstore/nonarchive.go`


<details open>
<summary><b>Функции в этом файле (20)</b></summary>


- 🔗 [CompactUserShards](#compactusershards-carstorenonarchivego261) `:261`

- 🔗 [GetCompactionTargets](#getcompactiontargets-carstorenonarchivego257) `:257`

- 🔗 [GetUserRepoHead](#getuserrepohead-carstorenonarchivego220) `:220`

- 🔗 [GetUserRepoRev](#getuserreporev-carstorenonarchivego232) `:232`

- 🔗 [HasUidCid](#hasuidcid-carstorenonarchivego265) `:265`

- 🔗 [ImportSlice](#importslice-carstorenonarchivego182) `:182`

- 🔗 [LookupBlockRef](#lookupblockref-carstorenonarchivego269) `:269`

- 🔗 [NewDeltaSession](#newdeltasession-carstorenonarchivego129) `:129`

- 🔗 [NewNonArchivalCarstore](#newnonarchivalcarstore-carstorenonarchivego30) `:30`

- 🔗 [ReadOnlySession](#readonlysession-carstorenonarchivego163) `:163`

- 🔗 [ReadUserCar](#readusercar-carstorenonarchivego178) `:178`

- 🔗 [Stat](#stat-carstorenonarchivego244) `:244`

- 🔗 [WipeUserData](#wipeuserdata-carstorenonarchivego248) `:248`

- 🔗 [checkLastShardCache](#checklastshardcache-carstorenonarchivego49) `:49`

- 🔗 [getCommitRefInfo](#getcommitrefinfo-carstorenonarchivego87) `:87`

- 🔗 [loadCommitRefInfo](#loadcommitrefinfo-carstorenonarchivego75) `:75`

- 🔗 [putLastShardCache](#putlastshardcache-carstorenonarchivego68) `:68`

- 🔗 [removeLastShardCache](#removelastshardcache-carstorenonarchivego61) `:61`

- 🔗 [updateLastCommit](#updatelastcommit-carstorenonarchivego108) `:108`

- 🔗 [writeNewShard](#writenewshard-carstorenonarchivego273) `:273`


</details>


[function] name: CompactUserShards file: carstore/nonarchive.go:261 returns_error: да description: —


### CompactUserShards (carstore/nonarchive.go:261)


CompactUserShards is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) CompactUserShards((*CompactionStats, error)) (*CompactionStats, error)
```


**Тип запроса:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CompactionStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:261`



---


[function] name: GetCompactionTargets file: carstore/nonarchive.go:257 returns_error: да description: —


### GetCompactionTargets (carstore/nonarchive.go:257)


GetCompactionTargets is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) GetCompactionTargets(([]CompactionTarget, error)) ([]CompactionTarget, error)
```


**Тип ответа:** CompactionTarget


```json
{
  "Usr": {},
  "NumShards": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]CompactionTarget`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:257`



---


[function] name: GetUserRepoHead file: carstore/nonarchive.go:220 returns_error: да description: —


### GetUserRepoHead (carstore/nonarchive.go:220)


GetUserRepoHead is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) GetUserRepoHead((cid.Cid, error)) (cid.Cid, error)
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


📍 *Расположение:* `carstore/nonarchive.go:220`



---


[function] name: GetUserRepoRev file: carstore/nonarchive.go:232 returns_error: да description: —


### GetUserRepoRev (carstore/nonarchive.go:232)


GetUserRepoRev is a method that retrieves data based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) GetUserRepoRev((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:232`



---


[function] name: HasUidCid file: carstore/nonarchive.go:265 returns_error: да description: —


### HasUidCid (carstore/nonarchive.go:265)


HasUidCid is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) HasUidCid((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:265`



---


[function] name: ImportSlice file: carstore/nonarchive.go:182 returns_error: да description: —


### ImportSlice (carstore/nonarchive.go:182)


ImportSlice is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) ImportSlice((cid.Cid, *DeltaSession, error)) (cid.Cid, *DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:182`



---


[function] name: LookupBlockRef file: carstore/nonarchive.go:269 returns_error: да description: —


### LookupBlockRef (carstore/nonarchive.go:269)


LookupBlockRef is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) LookupBlockRef((path string, offset int64, user models.Uid, err error)) (path string, offset int64, user models.Uid, err error)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** offset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `path string`, `offset int64`, `user models.Uid`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:269`



---


[function] name: NewDeltaSession file: carstore/nonarchive.go:129 returns_error: да description: —


### NewDeltaSession (carstore/nonarchive.go:129)


NewDeltaSession is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) NewDeltaSession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:129`



---


[function] name: NewNonArchivalCarstore file: carstore/nonarchive.go:30 returns_error: да description: —


### NewNonArchivalCarstore (carstore/nonarchive.go:30)


NewNonArchivalCarstore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewNonArchivalCarstore((*NonArchivalCarstore, error)) (*NonArchivalCarstore, error)
```


**Тип запроса:** NonArchivalCarstore


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** NonArchivalCarstore


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NonArchivalCarstore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:30`



---


[function] name: ReadOnlySession file: carstore/nonarchive.go:163 returns_error: да description: —


### ReadOnlySession (carstore/nonarchive.go:163)


ReadOnlySession is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) ReadOnlySession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:163`



---


[function] name: ReadUserCar file: carstore/nonarchive.go:178 returns_error: нет description: TODO: incremental is only ever called true, remove the param


### ReadUserCar (carstore/nonarchive.go:178)


TODO: incremental is only ever called true, remove the param


```go
func (cs *NonArchivalCarstore) ReadUserCar((ctx context.Context, user models.Uid, sinceRev string, incremental bool, w io.Writer)) (ctx context.Context, user models.Uid, sinceRev string, incremental bool, w io.Writer)
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


**Тип ответа:** sinceRev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** incremental


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


📍 *Расположение:* `carstore/nonarchive.go:178`



---


[function] name: Stat file: carstore/nonarchive.go:244 returns_error: да description: —


### Stat (carstore/nonarchive.go:244)


Stat is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) Stat(([]UserStat, error)) ([]UserStat, error)
```


**Тип ответа:** UserStat


```json
{
  "Seq": 0,
  "Root": "string",
  "Created": {}
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]UserStat`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:244`



---


[function] name: WipeUserData file: carstore/nonarchive.go:248 returns_error: нет description: —


### WipeUserData (carstore/nonarchive.go:248)


WipeUserData is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid).


```go
func (cs *NonArchivalCarstore) WipeUserData((ctx context.Context, user models.Uid)) (ctx context.Context, user models.Uid)
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


📍 *Расположение:* `carstore/nonarchive.go:248`



---


[function] name: checkLastShardCache file: carstore/nonarchive.go:49 returns_error: нет description: —


### checkLastShardCache (carstore/nonarchive.go:49)


checkLastShardCache is a method that performs operations based on the provided parameters and returns (user models.Uid).


```go
func (cs *NonArchivalCarstore) checkLastShardCache((user models.Uid)) (user models.Uid)
```


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


📍 *Расположение:* `carstore/nonarchive.go:49`



---


[function] name: getCommitRefInfo file: carstore/nonarchive.go:87 returns_error: да description: —


### getCommitRefInfo (carstore/nonarchive.go:87)


getCommitRefInfo is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) getCommitRefInfo((*commitRefInfo, error)) (*commitRefInfo, error)
```


**Тип запроса:** commitRefInfo


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** commitRefInfo


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*commitRefInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:87`



---


[function] name: loadCommitRefInfo file: carstore/nonarchive.go:75 returns_error: да description: —


### loadCommitRefInfo (carstore/nonarchive.go:75)


loadCommitRefInfo is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) loadCommitRefInfo((*commitRefInfo, error)) (*commitRefInfo, error)
```


**Тип запроса:** commitRefInfo


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** commitRefInfo


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*commitRefInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:75`



---


[function] name: putLastShardCache file: carstore/nonarchive.go:68 returns_error: нет description: —


### putLastShardCache (carstore/nonarchive.go:68)


putLastShardCache is a method that performs operations based on the provided parameters and returns (ls *commitRefInfo).


```go
func (cs *NonArchivalCarstore) putLastShardCache((ls *commitRefInfo)) (ls *commitRefInfo)
```


**Тип запроса:** commitRefInfo


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** ls


```json
{
  "ModerationDefsImagedetails": null,
  "ModerationDefsVideodetails": null
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Тип ответа:** commitRefInfo


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


📍 *Расположение:* `carstore/nonarchive.go:68`



---


[function] name: removeLastShardCache file: carstore/nonarchive.go:61 returns_error: нет description: —


### removeLastShardCache (carstore/nonarchive.go:61)


removeLastShardCache is a method that performs operations based on the provided parameters and returns (user models.Uid).


```go
func (cs *NonArchivalCarstore) removeLastShardCache((user models.Uid)) (user models.Uid)
```


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


📍 *Расположение:* `carstore/nonarchive.go:61`



---


[function] name: updateLastCommit file: carstore/nonarchive.go:108 returns_error: нет description: —


### updateLastCommit (carstore/nonarchive.go:108)


updateLastCommit is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid models.Uid, rev string, cid cid.Cid).


```go
func (cs *NonArchivalCarstore) updateLastCommit((ctx context.Context, uid models.Uid, rev string, cid cid.Cid)) (ctx context.Context, uid models.Uid, rev string, cid cid.Cid)
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


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `carstore/nonarchive.go:108`



---


[function] name: writeNewShard file: carstore/nonarchive.go:273 returns_error: да description: —


### writeNewShard (carstore/nonarchive.go:273)


writeNewShard is a method that performs operations based on the provided parameters and may return an error.


```go
func (cs *NonArchivalCarstore) writeNewShard(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/nonarchive.go:273`




## carstore/scylla.go


📄 Исходный файл: `carstore/scylla.go`


<details open>
<summary><b>Функции в этом файле (26)</b></summary>


- 🔗 [Attempt](#attempt-carstorescyllago586) `:586`

- 🔗 [CarStore](#carstore-carstorescyllago473) `:473`

- 🔗 [Close](#close-carstorescyllago477) `:477`

- 🔗 [CompactUserShards](#compactusershards-carstorescyllago219) `:219`

- 🔗 [GetCompactionTargets](#getcompactiontargets-carstorescyllago224) `:224`

- 🔗 [GetLastShard](#getlastshard-carstorescyllago198) `:198`

- 🔗 [GetRetryType](#getretrytype-carstorescyllago613) `:613`

- 🔗 [GetUserRepoHead](#getuserrepohead-carstorescyllago229) `:229`

- 🔗 [GetUserRepoRev](#getuserreporev-carstorescyllago245) `:245`

- 🔗 [HasUidCid](#hasuidcid-carstorescyllago461) `:461`

- 🔗 [ImportSlice](#importslice-carstorescyllago261) `:261`

- 🔗 [NewDeltaSession](#newdeltasession-carstorescyllago300) `:300`

- 🔗 [NewScyllaStore](#newscyllastore-carstorescyllago42) `:42`

- 🔗 [Open](#open-carstorescyllago53) `:53`

- 🔗 [ReadOnlySession](#readonlysession-carstorescyllago333) `:333`

- 🔗 [ReadUserCar](#readusercar-carstorescyllago347) `:347`

- 🔗 [Stat](#stat-carstorescyllago410) `:410`

- 🔗 [WipeUserData](#wipeuserdata-carstorescyllago415) `:415`

- 🔗 [createTables](#createtables-carstorescyllago131) `:131`

- 🔗 [delayForAttempt](#delayforattempt-carstorescyllago632) `:632`

- 🔗 [getBlock](#getblock-carstorescyllago483) `:483`

- 🔗 [getBlockSize](#getblocksize-carstorescyllago497) `:497`

- 🔗 [getExponentialTime](#getexponentialtime-carstorescyllago595) `:595`

- 🔗 [init](#init-carstorescyllago553) `:553`

- 🔗 [napTime](#naptime-carstorescyllago582) `:582`

- 🔗 [writeNewShard](#writenewshard-carstorescyllago142) `:142`


</details>


[function] name: Attempt file: carstore/scylla.go:586 returns_error: нет description: —


### Attempt (carstore/scylla.go:586)


Attempt is a method that performs operations based on the provided parameters and returns (q gocql.RetryableQuery).


```go
func (e *ExponentialBackoffRetryPolicy) Attempt((q gocql.RetryableQuery)) (q gocql.RetryableQuery)
```


**Тип ответа:** q


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** gocql.RetryableQuery


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/scylla.go:586`



---


[function] name: CarStore file: carstore/scylla.go:473 returns_error: нет description: —


### CarStore (carstore/scylla.go:473)


CarStore is a method that performs operations based on the provided parameters and returns ().


```go
func (sqs *ScyllaStore) CarStore(()) ()
```


📍 *Расположение:* `carstore/scylla.go:473`



---


[function] name: Close file: carstore/scylla.go:477 returns_error: нет description: —


### Close (carstore/scylla.go:477)


Close is a method that performs operations based on the provided parameters and returns ().


```go
func (sqs *ScyllaStore) Close(()) ()
```


📍 *Расположение:* `carstore/scylla.go:477`



---


[function] name: CompactUserShards file: carstore/scylla.go:219 returns_error: да description: —


### CompactUserShards (carstore/scylla.go:219)


CompactUserShards is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) CompactUserShards((*CompactionStats, error)) (*CompactionStats, error)
```


**Тип запроса:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CompactionStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:219`



---


[function] name: GetCompactionTargets file: carstore/scylla.go:224 returns_error: да description: —


### GetCompactionTargets (carstore/scylla.go:224)


GetCompactionTargets is a method that retrieves data based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) GetCompactionTargets(([]CompactionTarget, error)) ([]CompactionTarget, error)
```


**Тип ответа:** CompactionTarget


```json
{
  "Usr": {},
  "NumShards": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]CompactionTarget`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:224`



---


[function] name: GetLastShard file: carstore/scylla.go:198 returns_error: да description: GetLastShard nedeed for NewDeltaSession indirectly through lastShardCache
What we actually seem to need from this: last 


### GetLastShard (carstore/scylla.go:198)


GetLastShard nedeed for NewDeltaSession indirectly through lastShardCache
What we actually seem to need from this: last {Rev, Root.CID}


```go
func (sqs *ScyllaStore) GetLastShard((*CarShard, error)) (*CarShard, error)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CarShard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:198`



---


[function] name: GetRetryType file: carstore/scylla.go:613 returns_error: да description: GetRetryType returns the retry type for the given error


### GetRetryType (carstore/scylla.go:613)


GetRetryType returns the retry type for the given error


```go
func (e *ExponentialBackoffRetryPolicy) GetRetryType((err error)) (err error)
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


📍 *Расположение:* `carstore/scylla.go:613`



---


[function] name: GetUserRepoHead file: carstore/scylla.go:229 returns_error: да description: —


### GetUserRepoHead (carstore/scylla.go:229)


GetUserRepoHead is a method that retrieves data based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) GetUserRepoHead((cid.Cid, error)) (cid.Cid, error)
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


📍 *Расположение:* `carstore/scylla.go:229`



---


[function] name: GetUserRepoRev file: carstore/scylla.go:245 returns_error: да description: —


### GetUserRepoRev (carstore/scylla.go:245)


GetUserRepoRev is a method that retrieves data based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) GetUserRepoRev((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:245`



---


[function] name: HasUidCid file: carstore/scylla.go:461 returns_error: да description: HasUidCid needed for NewDeltaSession userView


### HasUidCid (carstore/scylla.go:461)


HasUidCid needed for NewDeltaSession userView


```go
func (sqs *ScyllaStore) HasUidCid((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:461`



---


[function] name: ImportSlice file: carstore/scylla.go:261 returns_error: да description: —


### ImportSlice (carstore/scylla.go:261)


ImportSlice is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) ImportSlice((cid.Cid, *DeltaSession, error)) (cid.Cid, *DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:261`



---


[function] name: NewDeltaSession file: carstore/scylla.go:300 returns_error: да description: —


### NewDeltaSession (carstore/scylla.go:300)


NewDeltaSession is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) NewDeltaSession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:300`



---


[function] name: NewScyllaStore file: carstore/scylla.go:42 returns_error: да description: —


### NewScyllaStore (carstore/scylla.go:42)


NewScyllaStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewScyllaStore((*ScyllaStore, error)) (*ScyllaStore, error)
```


**Тип запроса:** ScyllaStore


```json
{
  "WriteSession": null,
  "ReadSession": null,
  "scyllaAddrs": [],
  "keyspace": "string",
  "log": null,
  "lastShardCache": {}
}
```


*Определено в:* `carstore/scylla.go`


**Тип ответа:** ScyllaStore


```json
{
  "WriteSession": null,
  "ReadSession": null,
  "scyllaAddrs": [],
  "keyspace": "string",
  "log": null,
  "lastShardCache": {}
}
```


*Определено в:* `carstore/scylla.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ScyllaStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:42`



---


[function] name: Open file: carstore/scylla.go:53 returns_error: нет description: —


### Open (carstore/scylla.go:53)


Open is a method that performs operations based on the provided parameters and returns ().


```go
func (sqs *ScyllaStore) Open(()) ()
```


📍 *Расположение:* `carstore/scylla.go:53`



---


[function] name: ReadOnlySession file: carstore/scylla.go:333 returns_error: да description: —


### ReadOnlySession (carstore/scylla.go:333)


ReadOnlySession is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) ReadOnlySession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:333`



---


[function] name: ReadUserCar file: carstore/scylla.go:347 returns_error: нет description: ReadUserCar
incremental is only ever called true


### ReadUserCar (carstore/scylla.go:347)


ReadUserCar
incremental is only ever called true


```go
func (sqs *ScyllaStore) ReadUserCar((ctx context.Context, user models.Uid, sinceRev string, incremental bool, shardOut io.Writer)) (ctx context.Context, user models.Uid, sinceRev string, incremental bool, shardOut io.Writer)
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


**Тип ответа:** sinceRev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** incremental


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shardOut


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/scylla.go:347`



---


[function] name: Stat file: carstore/scylla.go:410 returns_error: да description: Stat is only used in a debugging admin handler
don't bother implementing it (for now?)


### Stat (carstore/scylla.go:410)


Stat is only used in a debugging admin handler
don't bother implementing it (for now?)


```go
func (sqs *ScyllaStore) Stat(([]UserStat, error)) ([]UserStat, error)
```


**Тип ответа:** UserStat


```json
{
  "Seq": 0,
  "Root": "string",
  "Created": {}
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]UserStat`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:410`



---


[function] name: WipeUserData file: carstore/scylla.go:415 returns_error: нет description: —


### WipeUserData (carstore/scylla.go:415)


WipeUserData is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid).


```go
func (sqs *ScyllaStore) WipeUserData((ctx context.Context, user models.Uid)) (ctx context.Context, user models.Uid)
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


📍 *Расположение:* `carstore/scylla.go:415`



---


[function] name: createTables file: carstore/scylla.go:131 returns_error: нет description: —


### createTables (carstore/scylla.go:131)


createTables is a method that performs operations based on the provided parameters and returns ().


```go
func (sqs *ScyllaStore) createTables(()) ()
```


📍 *Расположение:* `carstore/scylla.go:131`



---


[function] name: delayForAttempt file: carstore/scylla.go:632 returns_error: нет description: —


### delayForAttempt (carstore/scylla.go:632)


delayForAttempt is a function that performs operations based on the provided parameters and returns (attempt int).


```go
func delayForAttempt((attempt int)) (attempt int)
```


**Тип ответа:** attempt


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/scylla.go:632`



---


[function] name: getBlock file: carstore/scylla.go:483 returns_error: да description: —


### getBlock (carstore/scylla.go:483)


getBlock is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) getBlock((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:483`



---


[function] name: getBlockSize file: carstore/scylla.go:497 returns_error: да description: —


### getBlockSize (carstore/scylla.go:497)


getBlockSize is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *ScyllaStore) getBlockSize((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:497`



---


[function] name: getExponentialTime file: carstore/scylla.go:595 returns_error: нет description: used to calculate exponentially growing time


### getExponentialTime (carstore/scylla.go:595)


used to calculate exponentially growing time


```go
func getExponentialTime((min time.Duration, max time.Duration, attempts int)) (min time.Duration, max time.Duration, attempts int)
```


**Тип ответа:** min


```json
{
  "Password": "string"
}
```


*Определено в:* `atproto/atclient/admin_auth.go`


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** max


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** attempts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/scylla.go:595`



---


[function] name: init file: carstore/scylla.go:553 returns_error: нет description: —


### init (carstore/scylla.go:553)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `carstore/scylla.go:553`



---


[function] name: napTime file: carstore/scylla.go:582 returns_error: нет description: —


### napTime (carstore/scylla.go:582)


napTime is a method that performs operations based on the provided parameters and returns (attempts int).


```go
func (e *ExponentialBackoffRetryPolicy) napTime((attempts int)) (attempts int)
```


**Тип ответа:** attempts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/scylla.go:582`



---


[function] name: writeNewShard file: carstore/scylla.go:142 returns_error: да description: writeNewShard needed for DeltaSession.CloseWithRoot


### writeNewShard (carstore/scylla.go:142)


writeNewShard needed for DeltaSession.CloseWithRoot


```go
func (sqs *ScyllaStore) writeNewShard(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla.go:142`




## carstore/scylla_stub.go


📄 Исходный файл: `carstore/scylla_stub.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewScyllaStore](#newscyllastore-carstorescylla_stubgo7) `:7`


</details>


[function] name: NewScyllaStore file: carstore/scylla_stub.go:7 returns_error: да description: —


### NewScyllaStore (carstore/scylla_stub.go:7)


NewScyllaStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewScyllaStore((CarStore, error)) (CarStore, error)
```


**Тип ответа:** CarStore


```json
{
  "meta": null,
  "rootDirs": [],
  "lastShardCache": {},
  "log": null
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CarStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/scylla_stub.go:7`




## carstore/sqlite_store.go


📄 Исходный файл: `carstore/sqlite_store.go`


<details open>
<summary><b>Функции в этом файле (24)</b></summary>


- 🔗 [CarStore](#carstore-carstoresqlite_storego441) `:441`

- 🔗 [Close](#close-carstoresqlite_storego445) `:445`

- 🔗 [CompactUserShards](#compactusershards-carstoresqlite_storego200) `:200`

- 🔗 [Get](#get-carstoresqlite_storego528) `:528`

- 🔗 [GetCompactionTargets](#getcompactiontargets-carstoresqlite_storego205) `:205`

- 🔗 [GetLastShard](#getlastshard-carstoresqlite_storego170) `:170`

- 🔗 [GetSize](#getsize-carstoresqlite_storego533) `:533`

- 🔗 [GetUserRepoHead](#getuserrepohead-carstoresqlite_storego210) `:210`

- 🔗 [GetUserRepoRev](#getuserreporev-carstoresqlite_storego223) `:223`

- 🔗 [Has](#has-carstoresqlite_storego523) `:523`

- 🔗 [HasUidCid](#hasuidcid-carstoresqlite_storego412) `:412`

- 🔗 [ImportSlice](#importslice-carstoresqlite_storego236) `:236`

- 🔗 [NewDeltaSession](#newdeltasession-carstoresqlite_storego277) `:277`

- 🔗 [NewSqliteStore](#newsqlitestore-carstoresqlite_storego52) `:52`

- 🔗 [Open](#open-carstoresqlite_storego65) `:65`

- 🔗 [ReadOnlySession](#readonlysession-carstoresqlite_storego310) `:310`

- 🔗 [ReadUserCar](#readusercar-carstoresqlite_storego331) `:331`

- 🔗 [Stat](#stat-carstoresqlite_storego382) `:382`

- 🔗 [WipeUserData](#wipeuserdata-carstoresqlite_storego387) `:387`

- 🔗 [createTables](#createtables-carstoresqlite_storego85) `:85`

- 🔗 [ensureDir](#ensuredir-carstoresqlite_storego38) `:38`

- 🔗 [getBlock](#getblock-carstoresqlite_storego449) `:449`

- 🔗 [getBlockSize](#getblocksize-carstoresqlite_storego483) `:483`

- 🔗 [writeNewShard](#writenewshard-carstoresqlite_storego103) `:103`


</details>


[function] name: CarStore file: carstore/sqlite_store.go:441 returns_error: нет description: —


### CarStore (carstore/sqlite_store.go:441)


CarStore is a method that performs operations based on the provided parameters and returns ().


```go
func (sqs *SQLiteStore) CarStore(()) ()
```


📍 *Расположение:* `carstore/sqlite_store.go:441`



---


[function] name: Close file: carstore/sqlite_store.go:445 returns_error: нет description: —


### Close (carstore/sqlite_store.go:445)


Close is a method that performs operations based on the provided parameters and returns ().


```go
func (sqs *SQLiteStore) Close(()) ()
```


📍 *Расположение:* `carstore/sqlite_store.go:445`



---


[function] name: CompactUserShards file: carstore/sqlite_store.go:200 returns_error: да description: —


### CompactUserShards (carstore/sqlite_store.go:200)


CompactUserShards is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) CompactUserShards((*CompactionStats, error)) (*CompactionStats, error)
```


**Тип запроса:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** CompactionStats


```json
{
  "TotalRefs": 0,
  "StartShards": 0,
  "NewShards": 0,
  "SkippedShards": 0,
  "ShardsDeleted": 0,
  "DupeCount": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CompactionStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:200`



---


[function] name: Get file: carstore/sqlite_store.go:528 returns_error: да description: —


### Get (carstore/sqlite_store.go:528)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s sqliteUserView) Get((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:528`



---


[function] name: GetCompactionTargets file: carstore/sqlite_store.go:205 returns_error: да description: —


### GetCompactionTargets (carstore/sqlite_store.go:205)


GetCompactionTargets is a method that retrieves data based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) GetCompactionTargets(([]CompactionTarget, error)) ([]CompactionTarget, error)
```


**Тип ответа:** CompactionTarget


```json
{
  "Usr": {},
  "NumShards": 0
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]CompactionTarget`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:205`



---


[function] name: GetLastShard file: carstore/sqlite_store.go:170 returns_error: да description: GetLastShard nedeed for NewDeltaSession indirectly through lastShardCache
What we actually seem to need from this: last 


### GetLastShard (carstore/sqlite_store.go:170)


GetLastShard nedeed for NewDeltaSession indirectly through lastShardCache
What we actually seem to need from this: last {Rev, Root.CID}


```go
func (sqs *SQLiteStore) GetLastShard((*CarShard, error)) (*CarShard, error)
```


**Тип запроса:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** CarShard


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Root": {},
  "DataStart": 0,
  "Seq": 0,
  "Path": "string",
  "Usr": {},
  "Rev": "string"
}
```


*Определено в:* `carstore/meta_gorm.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CarShard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:170`



---


[function] name: GetSize file: carstore/sqlite_store.go:533 returns_error: да description: —


### GetSize (carstore/sqlite_store.go:533)


GetSize is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s sqliteUserView) GetSize((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:533`



---


[function] name: GetUserRepoHead file: carstore/sqlite_store.go:210 returns_error: да description: —


### GetUserRepoHead (carstore/sqlite_store.go:210)


GetUserRepoHead is a method that retrieves data based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) GetUserRepoHead((cid.Cid, error)) (cid.Cid, error)
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


📍 *Расположение:* `carstore/sqlite_store.go:210`



---


[function] name: GetUserRepoRev file: carstore/sqlite_store.go:223 returns_error: да description: —


### GetUserRepoRev (carstore/sqlite_store.go:223)


GetUserRepoRev is a method that retrieves data based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) GetUserRepoRev((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:223`



---


[function] name: Has file: carstore/sqlite_store.go:523 returns_error: да description: —


### Has (carstore/sqlite_store.go:523)


Has is a method that performs operations based on the provided parameters and may return an error.


```go
func (s sqliteUserView) Has((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:523`



---


[function] name: HasUidCid file: carstore/sqlite_store.go:412 returns_error: да description: HasUidCid needed for NewDeltaSession userView


### HasUidCid (carstore/sqlite_store.go:412)


HasUidCid needed for NewDeltaSession userView


```go
func (sqs *SQLiteStore) HasUidCid((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:412`



---


[function] name: ImportSlice file: carstore/sqlite_store.go:236 returns_error: да description: —


### ImportSlice (carstore/sqlite_store.go:236)


ImportSlice is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) ImportSlice((cid.Cid, *DeltaSession, error)) (cid.Cid, *DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:236`



---


[function] name: NewDeltaSession file: carstore/sqlite_store.go:277 returns_error: да description: —


### NewDeltaSession (carstore/sqlite_store.go:277)


NewDeltaSession is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) NewDeltaSession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:277`



---


[function] name: NewSqliteStore file: carstore/sqlite_store.go:52 returns_error: да description: —


### NewSqliteStore (carstore/sqlite_store.go:52)


NewSqliteStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewSqliteStore((*SQLiteStore, error)) (*SQLiteStore, error)
```


**Тип запроса:** SQLiteStore


```json
{
  "dbPath": "string",
  "db": null,
  "log": null,
  "lastShardCache": {}
}
```


*Определено в:* `carstore/sqlite_store.go`


**Тип ответа:** SQLiteStore


```json
{
  "dbPath": "string",
  "db": null,
  "log": null,
  "lastShardCache": {}
}
```


*Определено в:* `carstore/sqlite_store.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SQLiteStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:52`



---


[function] name: Open file: carstore/sqlite_store.go:65 returns_error: нет description: —


### Open (carstore/sqlite_store.go:65)


Open is a method that performs operations based on the provided parameters and returns (path string).


```go
func (sqs *SQLiteStore) Open((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/sqlite_store.go:65`



---


[function] name: ReadOnlySession file: carstore/sqlite_store.go:310 returns_error: да description: —


### ReadOnlySession (carstore/sqlite_store.go:310)


ReadOnlySession is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) ReadOnlySession((*DeltaSession, error)) (*DeltaSession, error)
```


**Тип запроса:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Тип ответа:** DeltaSession


```json
{
  "blks": {},
  "rmcids": {},
  "base": {},
  "user": {},
  "baseCid": {},
  "seq": 0,
  "readonly": false,
  "cs": {},
  "lastRev": "string"
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DeltaSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:310`



---


[function] name: ReadUserCar file: carstore/sqlite_store.go:331 returns_error: нет description: ReadUserCar
incremental is only ever called true


### ReadUserCar (carstore/sqlite_store.go:331)


ReadUserCar
incremental is only ever called true


```go
func (sqs *SQLiteStore) ReadUserCar((ctx context.Context, user models.Uid, sinceRev string, incremental bool, shardOut io.Writer)) (ctx context.Context, user models.Uid, sinceRev string, incremental bool, shardOut io.Writer)
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


**Тип ответа:** sinceRev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** incremental


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shardOut


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/sqlite_store.go:331`



---


[function] name: Stat file: carstore/sqlite_store.go:382 returns_error: да description: Stat is only used in a debugging admin handler
don't bother implementing it (for now?)


### Stat (carstore/sqlite_store.go:382)


Stat is only used in a debugging admin handler
don't bother implementing it (for now?)


```go
func (sqs *SQLiteStore) Stat(([]UserStat, error)) ([]UserStat, error)
```


**Тип ответа:** UserStat


```json
{
  "Seq": 0,
  "Root": "string",
  "Created": {}
}
```


*Определено в:* `carstore/bs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]UserStat`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:382`



---


[function] name: WipeUserData file: carstore/sqlite_store.go:387 returns_error: нет description: —


### WipeUserData (carstore/sqlite_store.go:387)


WipeUserData is a method that performs operations based on the provided parameters and returns (ctx context.Context, user models.Uid).


```go
func (sqs *SQLiteStore) WipeUserData((ctx context.Context, user models.Uid)) (ctx context.Context, user models.Uid)
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


📍 *Расположение:* `carstore/sqlite_store.go:387`



---


[function] name: createTables file: carstore/sqlite_store.go:85 returns_error: нет description: —


### createTables (carstore/sqlite_store.go:85)


createTables is a method that performs operations based on the provided parameters and returns ().


```go
func (sqs *SQLiteStore) createTables(()) ()
```


📍 *Расположение:* `carstore/sqlite_store.go:85`



---


[function] name: ensureDir file: carstore/sqlite_store.go:38 returns_error: нет description: —


### ensureDir (carstore/sqlite_store.go:38)


ensureDir is a function that performs operations based on the provided parameters and returns (path string).


```go
func ensureDir((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `carstore/sqlite_store.go:38`



---


[function] name: getBlock file: carstore/sqlite_store.go:449 returns_error: да description: —


### getBlock (carstore/sqlite_store.go:449)


getBlock is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) getBlock((blockformat.Block, error)) (blockformat.Block, error)
```


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blockformat.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:449`



---


[function] name: getBlockSize file: carstore/sqlite_store.go:483 returns_error: да description: —


### getBlockSize (carstore/sqlite_store.go:483)


getBlockSize is a method that performs operations based on the provided parameters and may return an error.


```go
func (sqs *SQLiteStore) getBlockSize((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:483`



---


[function] name: writeNewShard file: carstore/sqlite_store.go:103 returns_error: да description: writeNewShard needed for DeltaSession.CloseWithRoot


### writeNewShard (carstore/sqlite_store.go:103)


writeNewShard needed for DeltaSession.CloseWithRoot


```go
func (sqs *SQLiteStore) writeNewShard(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/sqlite_store.go:103`




## carstore/util.go


📄 Исходный файл: `carstore/util.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [LdWrite](#ldwrite-carstoreutilgo10) `:10`


</details>


[function] name: LdWrite file: carstore/util.go:10 returns_error: да description: Length-delimited Write
Writer stream gets Uvarint length then concatenated data


### LdWrite (carstore/util.go:10)


Length-delimited Write
Writer stream gets Uvarint length then concatenated data


```go
func LdWrite((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `carstore/util.go:10`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](backfill.md)

- [Следующая директория](cmd_beemo.md)


---

