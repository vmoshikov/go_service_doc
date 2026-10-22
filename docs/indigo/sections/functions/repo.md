---
title: "Функции: repo"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: repo
---


# Функции: repo


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](mst.md)

- [Следующая директория](repo_carutil.md)


---


## Меню по файлам


- 📄 [repo/cbor_gen.go](#repocbor_gengo)

- 📄 [repo/repo.go](#reporepogo)

- 📄 [repo/stream.go](#repostreamgo)


---


## repo/cbor_gen.go


📄 Исходный файл: `repo/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-repocbor_gengo21) `:21`

- 🔗 [MarshalCBOR](#marshalcbor-repocbor_gengo333) `:333`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-repocbor_gengo174) `:174`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-repocbor_gengo462) `:462`


</details>


[function] name: MarshalCBOR file: repo/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (repo/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *SignedCommit) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `repo/cbor_gen.go:21`



---


[function] name: MarshalCBOR file: repo/cbor_gen.go:333 returns_error: нет description: —


### MarshalCBOR (repo/cbor_gen.go:333)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *UnsignedCommit) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `repo/cbor_gen.go:333`



---


[function] name: UnmarshalCBOR file: repo/cbor_gen.go:174 returns_error: да description: —


### UnmarshalCBOR (repo/cbor_gen.go:174)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *SignedCommit) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `repo/cbor_gen.go:174`



---


[function] name: UnmarshalCBOR file: repo/cbor_gen.go:462 returns_error: да description: —


### UnmarshalCBOR (repo/cbor_gen.go:462)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *UnsignedCommit) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `repo/cbor_gen.go:462`




## repo/repo.go


📄 Исходный файл: `repo/repo.go`


<details open>
<summary><b>Функции в этом файле (24)</b></summary>


- 🔗 [Blockstore](#blockstore-reporepogo195) `:195`

- 🔗 [BytesForSigning](#bytesforsigning-reporepogo73) `:73`

- 🔗 [Commit](#commit-reporepogo299) `:299`

- 🔗 [CopyDataTo](#copydatato-reporepogo457) `:457`

- 🔗 [CreateRecord](#createrecord-reporepogo199) `:199`

- 🔗 [DataCid](#datacid-reporepogo187) `:187`

- 🔗 [DeleteRecord](#deleterecord-reporepogo273) `:273`

- 🔗 [DiffSince](#diffsince-reporepogo421) `:421`

- 🔗 [ForEach](#foreach-reporepogo361) `:361`

- 🔗 [GetRecord](#getrecord-reporepogo376) `:376`

- 🔗 [GetRecordBytes](#getrecordbytes-reporepogo397) `:397`

- 🔗 [IngestRepo](#ingestrepo-reporepogo87) `:87`

- 🔗 [NewRepo](#newrepo-reporepogo128) `:128`

- 🔗 [OpenRepo](#openrepo-reporepogo148) `:148`

- 🔗 [PrevCommit](#prevcommit-reporepogo183) `:183`

- 🔗 [PutRecord](#putrecord-reporepogo225) `:225`

- 🔗 [ReadRepoFromCar](#readrepofromcar-reporepogo118) `:118`

- 🔗 [RepoDid](#repodid-reporepogo174) `:174`

- 🔗 [SignedCommit](#signedcommit-reporepogo191) `:191`

- 🔗 [Truncate](#truncate-reporepogo293) `:293`

- 🔗 [Unsigned](#unsigned-reporepogo60) `:60`

- 🔗 [UpdateRecord](#updaterecord-reporepogo249) `:249`

- 🔗 [copyRecCbor](#copyreccbor-reporepogo461) `:461`

- 🔗 [getMst](#getmst-reporepogo349) `:349`


</details>


[function] name: Blockstore file: repo/repo.go:195 returns_error: нет description: —


### Blockstore (repo/repo.go:195)


Blockstore is a method that performs operations based on the provided parameters and returns ().


```go
func (r *Repo) Blockstore(()) ()
```


📍 *Расположение:* `repo/repo.go:195`



---


[function] name: BytesForSigning file: repo/repo.go:73 returns_error: да description: returns bytes of the DAG-CBOR representation of object. This is what gets
signed; the `go-did` library will take the SHA


### BytesForSigning (repo/repo.go:73)


returns bytes of the DAG-CBOR representation of object. This is what gets
signed; the `go-did` library will take the SHA-256 of the bytes and sign
that.


```go
func (uc *UnsignedCommit) BytesForSigning(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:73`



---


[function] name: Commit file: repo/repo.go:299 returns_error: да description: creates and writes a new SignedCommit for this repo, with `prev` pointing to old value


### Commit (repo/repo.go:299)


creates and writes a new SignedCommit for this repo, with `prev` pointing to old value


```go
func (r *Repo) Commit((cid.Cid, string, error)) (cid.Cid, string, error)
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


*Типы возврата:* `cid.Cid`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:299`



---


[function] name: CopyDataTo file: repo/repo.go:457 returns_error: нет description: —


### CopyDataTo (repo/repo.go:457)


CopyDataTo is a method that performs operations based on the provided parameters and returns (ctx context.Context, bs cbor.IpldBlockstore).


```go
func (r *Repo) CopyDataTo((ctx context.Context, bs cbor.IpldBlockstore)) (ctx context.Context, bs cbor.IpldBlockstore)
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


**Тип ответа:** cbor.IpldBlockstore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repo/repo.go:457`



---


[function] name: CreateRecord file: repo/repo.go:199 returns_error: да description: —


### CreateRecord (repo/repo.go:199)


CreateRecord is a method that creates new data based on the provided parameters and may return an error.


```go
func (r *Repo) CreateRecord((cid.Cid, string, error)) (cid.Cid, string, error)
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


*Типы возврата:* `cid.Cid`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:199`



---


[function] name: DataCid file: repo/repo.go:187 returns_error: нет description: —


### DataCid (repo/repo.go:187)


DataCid is a method that performs operations based on the provided parameters and returns ().


```go
func (r *Repo) DataCid(()) ()
```


📍 *Расположение:* `repo/repo.go:187`



---


[function] name: DeleteRecord file: repo/repo.go:273 returns_error: нет description: —


### DeleteRecord (repo/repo.go:273)


DeleteRecord is a method that deletes data based on the provided parameters and returns (ctx context.Context, rpath string).


```go
func (r *Repo) DeleteRecord((ctx context.Context, rpath string)) (ctx context.Context, rpath string)
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


**Тип ответа:** rpath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repo/repo.go:273`



---


[function] name: DiffSince file: repo/repo.go:421 returns_error: да description: —


### DiffSince (repo/repo.go:421)


DiffSince is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Repo) DiffSince(([]*mst.DiffOp, error)) ([]*mst.DiffOp, error)
```


**Тип запроса:** mst.DiffOp


```json
{
  "Depth": 0,
  "Op": "string",
  "Rpath": "string",
  "OldCid": {},
  "NewCid": {}
}
```


*Определено в:* `mst/diff.go`


**Тип ответа:** mst.DiffOp


```json
{
  "Depth": 0,
  "Op": "string",
  "Rpath": "string",
  "OldCid": {},
  "NewCid": {}
}
```


*Определено в:* `mst/diff.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*mst.DiffOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:421`



---


[function] name: ForEach file: repo/repo.go:361 returns_error: да description: —


### ForEach (repo/repo.go:361)


ForEach is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Repo) ForEach((ctx context.Context, prefix string, cb func(k string, v cid.Cid) error)) (ctx context.Context, prefix string, cb func(k string, v cid.Cid) error)
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


**Тип ответа:** prefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** v


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


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `prefix string`, `cb func(k string`, `v cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:361`



---


[function] name: GetRecord file: repo/repo.go:376 returns_error: да description: —


### GetRecord (repo/repo.go:376)


GetRecord is a method that retrieves data based on the provided parameters and may return an error.


```go
func (r *Repo) GetRecord((cid.Cid, cbg.CBORMarshaler, error)) (cid.Cid, cbg.CBORMarshaler, error)
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


📍 *Расположение:* `repo/repo.go:376`



---


[function] name: GetRecordBytes file: repo/repo.go:397 returns_error: да description: —


### GetRecordBytes (repo/repo.go:397)


GetRecordBytes is a method that retrieves data based on the provided parameters and may return an error.


```go
func (r *Repo) GetRecordBytes((cid.Cid, *[]byte, error)) (cid.Cid, *[]byte, error)
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


📍 *Расположение:* `repo/repo.go:397`



---


[function] name: IngestRepo file: repo/repo.go:87 returns_error: да description: —


### IngestRepo (repo/repo.go:87)


IngestRepo is a function that performs operations based on the provided parameters and may return an error.


```go
func IngestRepo((cid.Cid, error)) (cid.Cid, error)
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


📍 *Расположение:* `repo/repo.go:87`



---


[function] name: NewRepo file: repo/repo.go:128 returns_error: нет description: —


### NewRepo (repo/repo.go:128)


NewRepo is a function that performs operations based on the provided parameters and returns (ctx context.Context, did string, bs cbor.IpldBlockstore).


```go
func NewRepo((ctx context.Context, did string, bs cbor.IpldBlockstore)) (ctx context.Context, did string, bs cbor.IpldBlockstore)
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


**Тип ответа:** cbor.IpldBlockstore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repo/repo.go:128`



---


[function] name: OpenRepo file: repo/repo.go:148 returns_error: да description: —


### OpenRepo (repo/repo.go:148)


OpenRepo is a function that performs operations based on the provided parameters and may return an error.


```go
func OpenRepo((*Repo, error)) (*Repo, error)
```


**Тип запроса:** Repo


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


**Тип ответа:** Repo


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


*Типы возврата:* `*Repo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:148`



---


[function] name: PrevCommit file: repo/repo.go:183 returns_error: да description: TODO(bnewbold): this could return just *cid.Cid


### PrevCommit (repo/repo.go:183)


TODO(bnewbold): this could return just *cid.Cid


```go
func (r *Repo) PrevCommit((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:183`



---


[function] name: PutRecord file: repo/repo.go:225 returns_error: да description: —


### PutRecord (repo/repo.go:225)


PutRecord is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Repo) PutRecord((cid.Cid, error)) (cid.Cid, error)
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


📍 *Расположение:* `repo/repo.go:225`



---


[function] name: ReadRepoFromCar file: repo/repo.go:118 returns_error: да description: —


### ReadRepoFromCar (repo/repo.go:118)


ReadRepoFromCar is a function that performs operations based on the provided parameters and may return an error.


```go
func ReadRepoFromCar((*Repo, error)) (*Repo, error)
```


**Тип запроса:** Repo


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


**Тип ответа:** Repo


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


*Типы возврата:* `*Repo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:118`



---


[function] name: RepoDid file: repo/repo.go:174 returns_error: нет description: —


### RepoDid (repo/repo.go:174)


RepoDid is a method that performs operations based on the provided parameters and returns ().


```go
func (r *Repo) RepoDid(()) ()
```


📍 *Расположение:* `repo/repo.go:174`



---


[function] name: SignedCommit file: repo/repo.go:191 returns_error: нет description: —


### SignedCommit (repo/repo.go:191)


SignedCommit is a method that performs operations based on the provided parameters and returns ().


```go
func (r *Repo) SignedCommit(()) ()
```


📍 *Расположение:* `repo/repo.go:191`



---


[function] name: Truncate file: repo/repo.go:293 returns_error: нет description: truncates history while retaining the same data root


### Truncate (repo/repo.go:293)


truncates history while retaining the same data root


```go
func (r *Repo) Truncate(()) ()
```


📍 *Расположение:* `repo/repo.go:293`



---


[function] name: Unsigned file: repo/repo.go:60 returns_error: нет description: Returns a copy of commit without the Sig field. Helpful when verifying signature.


### Unsigned (repo/repo.go:60)


Returns a copy of commit without the Sig field. Helpful when verifying signature.


```go
func (sc *SignedCommit) Unsigned(()) ()
```


📍 *Расположение:* `repo/repo.go:60`



---


[function] name: UpdateRecord file: repo/repo.go:249 returns_error: да description: —


### UpdateRecord (repo/repo.go:249)


UpdateRecord is a method that updates data based on the provided parameters and may return an error.


```go
func (r *Repo) UpdateRecord((cid.Cid, error)) (cid.Cid, error)
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


📍 *Расположение:* `repo/repo.go:249`



---


[function] name: copyRecCbor file: repo/repo.go:461 returns_error: нет description: —


### copyRecCbor (repo/repo.go:461)


copyRecCbor is a function that performs operations based on the provided parameters and returns (ctx context.Context, from, to cbor.IpldBlockstore, c cid.Cid, seen map[cid.Cid]struct{}).


```go
func copyRecCbor((ctx context.Context, from, to cbor.IpldBlockstore, c cid.Cid, seen map[cid.Cid]struct{})) (ctx context.Context, from, to cbor.IpldBlockstore, c cid.Cid, seen map[cid.Cid]struct{})
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


**Тип ответа:** from


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** to


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


**Тип ответа:** cbor.IpldBlockstore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** seen


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


**Тип ответа:** struct


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repo/repo.go:461`



---


[function] name: getMst file: repo/repo.go:349 returns_error: да description: —


### getMst (repo/repo.go:349)


getMst is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Repo) getMst((*mst.MerkleSearchTree, error)) (*mst.MerkleSearchTree, error)
```


**Тип запроса:** mst.MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** mst.MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*mst.MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/repo.go:349`




## repo/stream.go


📄 Исходный файл: `repo/stream.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Get](#get-repostreamgo69) `:69`

- 🔗 [Put](#put-repostreamgo110) `:110`

- 🔗 [StreamRepoRecords](#streamreporecords-repostreamgo134) `:134`

- 🔗 [View](#view-repostreamgo91) `:91`

- 🔗 [get](#get-repostreamgo73) `:73`

- 🔗 [newStreamingBlockstore](#newstreamingblockstore-repostreamgo34) `:34`

- 🔗 [readUntilBlock](#readuntilblock-repostreamgo41) `:41`


</details>


[function] name: Get file: repo/stream.go:69 returns_error: да description: —


### Get (repo/stream.go:69)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (bs *readStreamBlockstore) Get((block.Block, error)) (block.Block, error)
```


**Тип ответа:** block.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `block.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/stream.go:69`



---


[function] name: Put file: repo/stream.go:110 returns_error: нет description: —


### Put (repo/stream.go:110)


Put is a method that performs operations based on the provided parameters and returns (ctx context.Context, blk block.Block).


```go
func (bs *readStreamBlockstore) Put((ctx context.Context, blk block.Block)) (ctx context.Context, blk block.Block)
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


**Тип ответа:** block.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `repo/stream.go:110`



---


[function] name: StreamRepoRecords file: repo/stream.go:134 returns_error: да description: StreamRepoRecords parses a CAR-encoded repository from the given reader and
iterates over its records.

The prefix param


### StreamRepoRecords (repo/stream.go:134)


StreamRepoRecords parses a CAR-encoded repository from the given reader and
iterates over its records.

The prefix parameter specifies the starting point for iteration. Records are
visited in lexicographic order starting from the first key >= prefix. If
prefix exactly matches a full record path, that record will be included.
Note that this does not filter to only keys with that prefix; all records
from that point onward are visited.

The onCommit callback receives the signed commit after it is loaded. It may
be nil, in which case it is ignored. The callback can be used to extract
the revision string (sc.Rev), or in the future to verify the commit
signature. If the callback returns an error, StreamRepoRecords returns
immediately with that error.

The cb parameter is the visitor function called for each record with the
record's key, CID, and raw data. If cb returns an error, the error is logged
and iteration continues; errors from cb do not stop the walk and are not
returned from this function. To signal intentional early termination, cb can
return ErrDoneIterating, which is handled silently without logging.


```go
func StreamRepoRecords((ctx context.Context, r io.Reader, prefix string, onCommit func(*SignedCommit) error, cb func(k string, c cid.Cid, v []byte) error)) (ctx context.Context, r io.Reader, prefix string, onCommit func(*SignedCommit) error, cb func(k string, c cid.Cid, v []byte) error)
```


**Тип запроса:** SignedCommit


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


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** prefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** onCommit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SignedCommit


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


*Определено в:* `repo/repo.go`


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** v


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


*Типы возврата:* `ctx context.Context`, `r io.Reader`, `prefix string`, `onCommit func(*SignedCommit) error`, `cb func(k string`, `c cid.Cid`, `v []byte) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/stream.go:134`



---


[function] name: View file: repo/stream.go:91 returns_error: да description: —


### View (repo/stream.go:91)


View is a method that performs operations based on the provided parameters and may return an error.


```go
func (bs *readStreamBlockstore) View((cc cid.Cid, cb func([]byte) error)) (cc cid.Cid, cb func([]byte) error)
```


**Тип ответа:** cc


```json
{
  "Identity": {},
  "Status": "string"
}
```


*Определено в:* `cmd/relay/testing/scenario.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cc cid.Cid`, `cb func([]byte) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/stream.go:91`



---


[function] name: get file: repo/stream.go:73 returns_error: да description: —


### get (repo/stream.go:73)


get is a method that performs operations based on the provided parameters and may return an error.


```go
func (bs *readStreamBlockstore) get((*carutil.BasicBlock, error)) (*carutil.BasicBlock, error)
```


**Тип запроса:** carutil.BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** carutil.BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*carutil.BasicBlock`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/stream.go:73`



---


[function] name: newStreamingBlockstore file: repo/stream.go:34 returns_error: нет description: —


### newStreamingBlockstore (repo/stream.go:34)


newStreamingBlockstore is a function that performs operations based on the provided parameters and returns (r *carutil.Reader).


```go
func newStreamingBlockstore((r *carutil.Reader)) (r *carutil.Reader)
```


**Тип запроса:** carutil.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** carutil.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `repo/stream.go:34`



---


[function] name: readUntilBlock file: repo/stream.go:41 returns_error: да description: —


### readUntilBlock (repo/stream.go:41)


readUntilBlock is a method that performs operations based on the provided parameters and may return an error.


```go
func (bs *readStreamBlockstore) readUntilBlock((*carutil.BasicBlock, error)) (*carutil.BasicBlock, error)
```


**Тип запроса:** carutil.BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** carutil.BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*carutil.BasicBlock`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/stream.go:41`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](mst.md)

- [Следующая директория](repo_carutil.md)


---

