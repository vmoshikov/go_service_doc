---
title: "Функции: api/agnostic"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: api/agnostic
---


# Функции: api/agnostic


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Следующая директория](api_atproto.md)


---


## Меню по файлам


- 📄 [api/agnostic/actorgetPreferences.go](#apiagnosticactorgetpreferencesgo)

- 📄 [api/agnostic/actorputPreferences.go](#apiagnosticactorputpreferencesgo)

- 📄 [api/agnostic/identitygetRecommendedDidCredentials.go](#apiagnosticidentitygetrecommendeddidcredentialsgo)

- 📄 [api/agnostic/identitysignPlcOperation.go](#apiagnosticidentitysignplcoperationgo)

- 📄 [api/agnostic/identitysubmitPlcOperation.go](#apiagnosticidentitysubmitplcoperationgo)

- 📄 [api/agnostic/repoapplyWrites.go](#apiagnosticrepoapplywritesgo)

- 📄 [api/agnostic/repocreateRecord.go](#apiagnosticrepocreaterecordgo)

- 📄 [api/agnostic/repogetRecord.go](#apiagnosticrepogetrecordgo)

- 📄 [api/agnostic/repolistRecords.go](#apiagnosticrepolistrecordsgo)

- 📄 [api/agnostic/repoputRecord.go](#apiagnosticrepoputrecordgo)


---


## api/agnostic/actorgetPreferences.go


📄 Исходный файл: `api/agnostic/actorgetPreferences.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorGetPreferences](#actorgetpreferences-apiagnosticactorgetpreferencesgo19) `:19`


</details>


[function] name: ActorGetPreferences file: api/agnostic/actorgetPreferences.go:19 returns_error: да description: ActorGetPreferences calls the XRPC method "app.bsky.actor.getPreferences".


### ActorGetPreferences (api/agnostic/actorgetPreferences.go:19)


ActorGetPreferences calls the XRPC method "app.bsky.actor.getPreferences".


```go
func ActorGetPreferences((*ActorGetPreferences_Output, error)) (*ActorGetPreferences_Output, error)
```


**Тип запроса:** ActorGetPreferences_Output


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorgetPreferences.go`


**Тип ответа:** ActorGetPreferences_Output


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorgetPreferences.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorGetPreferences_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/actorgetPreferences.go:19`




## api/agnostic/actorputPreferences.go


📄 Исходный файл: `api/agnostic/actorputPreferences.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorPutPreferences](#actorputpreferences-apiagnosticactorputpreferencesgo19) `:19`


</details>


[function] name: ActorPutPreferences file: api/agnostic/actorputPreferences.go:19 returns_error: нет description: ActorPutPreferences calls the XRPC method "app.bsky.actor.putPreferences".


### ActorPutPreferences (api/agnostic/actorputPreferences.go:19)


ActorPutPreferences calls the XRPC method "app.bsky.actor.putPreferences".


```go
func ActorPutPreferences((ctx context.Context, c util.LexClient, input *ActorPutPreferences_Input)) (ctx context.Context, c util.LexClient, input *ActorPutPreferences_Input)
```


**Тип запроса:** ActorPutPreferences_Input


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorputPreferences.go`


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


**Тип ответа:** util.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ActorPutPreferences_Input


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorputPreferences.go`


📍 *Расположение:* `api/agnostic/actorputPreferences.go:19`




## api/agnostic/identitygetRecommendedDidCredentials.go


📄 Исходный файл: `api/agnostic/identitygetRecommendedDidCredentials.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityGetRecommendedDidCredentials](#identitygetrecommendeddidcredentials-apiagnosticidentitygetrecommendeddidcredentialsgo15) `:15`


</details>


[function] name: IdentityGetRecommendedDidCredentials file: api/agnostic/identitygetRecommendedDidCredentials.go:15 returns_error: да description: IdentityGetRecommendedDidCredentials calls the XRPC method "com.atproto.identity.getRecommendedDidCredentials".


### IdentityGetRecommendedDidCredentials (api/agnostic/identitygetRecommendedDidCredentials.go:15)


IdentityGetRecommendedDidCredentials calls the XRPC method "com.atproto.identity.getRecommendedDidCredentials".


```go
func IdentityGetRecommendedDidCredentials((*json.RawMessage, error)) (*json.RawMessage, error)
```


**Тип запроса:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*json.RawMessage`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/identitygetRecommendedDidCredentials.go:15`




## api/agnostic/identitysignPlcOperation.go


📄 Исходный файл: `api/agnostic/identitysignPlcOperation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentitySignPlcOperation](#identitysignplcoperation-apiagnosticidentitysignplcoperationgo31) `:31`


</details>


[function] name: IdentitySignPlcOperation file: api/agnostic/identitysignPlcOperation.go:31 returns_error: да description: IdentitySignPlcOperation calls the XRPC method "com.atproto.identity.signPlcOperation".


### IdentitySignPlcOperation (api/agnostic/identitysignPlcOperation.go:31)


IdentitySignPlcOperation calls the XRPC method "com.atproto.identity.signPlcOperation".


```go
func IdentitySignPlcOperation((*IdentitySignPlcOperation_Output, error)) (*IdentitySignPlcOperation_Output, error)
```


**Тип запроса:** IdentitySignPlcOperation_Output


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysignPlcOperation.go`


**Тип ответа:** IdentitySignPlcOperation_Output


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysignPlcOperation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IdentitySignPlcOperation_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/identitysignPlcOperation.go:31`




## api/agnostic/identitysubmitPlcOperation.go


📄 Исходный файл: `api/agnostic/identitysubmitPlcOperation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentitySubmitPlcOperation](#identitysubmitplcoperation-apiagnosticidentitysubmitplcoperationgo20) `:20`


</details>


[function] name: IdentitySubmitPlcOperation file: api/agnostic/identitysubmitPlcOperation.go:20 returns_error: нет description: IdentitySubmitPlcOperation calls the XRPC method "com.atproto.identity.submitPlcOperation".


### IdentitySubmitPlcOperation (api/agnostic/identitysubmitPlcOperation.go:20)


IdentitySubmitPlcOperation calls the XRPC method "com.atproto.identity.submitPlcOperation".


```go
func IdentitySubmitPlcOperation((ctx context.Context, c util.LexClient, input *IdentitySubmitPlcOperation_Input)) (ctx context.Context, c util.LexClient, input *IdentitySubmitPlcOperation_Input)
```


**Тип запроса:** IdentitySubmitPlcOperation_Input


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysubmitPlcOperation.go`


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


**Тип ответа:** util.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** IdentitySubmitPlcOperation_Input


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysubmitPlcOperation.go`


📍 *Расположение:* `api/agnostic/identitysubmitPlcOperation.go:20`




## api/agnostic/repoapplyWrites.go


📄 Исходный файл: `api/agnostic/repoapplyWrites.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiagnosticrepoapplywritesgo72) `:72`

- 🔗 [MarshalJSON](#marshaljson-apiagnosticrepoapplywritesgo121) `:121`

- 🔗 [RepoApplyWrites](#repoapplywrites-apiagnosticrepoapplywritesgo181) `:181`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiagnosticrepoapplywritesgo87) `:87`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiagnosticrepoapplywritesgo136) `:136`


</details>


[function] name: MarshalJSON file: api/agnostic/repoapplyWrites.go:72 returns_error: да description: —


### MarshalJSON (api/agnostic/repoapplyWrites.go:72)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RepoApplyWrites_Input_Writes_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/repoapplyWrites.go:72`



---


[function] name: MarshalJSON file: api/agnostic/repoapplyWrites.go:121 returns_error: да description: —


### MarshalJSON (api/agnostic/repoapplyWrites.go:121)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RepoApplyWrites_Output_Results_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/repoapplyWrites.go:121`



---


[function] name: RepoApplyWrites file: api/agnostic/repoapplyWrites.go:181 returns_error: да description: RepoApplyWrites calls the XRPC method "com.atproto.repo.applyWrites".


### RepoApplyWrites (api/agnostic/repoapplyWrites.go:181)


RepoApplyWrites calls the XRPC method "com.atproto.repo.applyWrites".


```go
func RepoApplyWrites((*RepoApplyWrites_Output, error)) (*RepoApplyWrites_Output, error)
```


**Тип запроса:** RepoApplyWrites_Output


```json
{
  "commit": null,
  "results": []
}
```


*Определено в:* `api/agnostic/repoapplyWrites.go`


**Тип ответа:** RepoApplyWrites_Output


```json
{
  "commit": null,
  "results": []
}
```


*Определено в:* `api/agnostic/repoapplyWrites.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoApplyWrites_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/repoapplyWrites.go:181`



---


[function] name: UnmarshalJSON file: api/agnostic/repoapplyWrites.go:87 returns_error: нет description: —


### UnmarshalJSON (api/agnostic/repoapplyWrites.go:87)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *RepoApplyWrites_Input_Writes_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/agnostic/repoapplyWrites.go:87`



---


[function] name: UnmarshalJSON file: api/agnostic/repoapplyWrites.go:136 returns_error: нет description: —


### UnmarshalJSON (api/agnostic/repoapplyWrites.go:136)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *RepoApplyWrites_Output_Results_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/agnostic/repoapplyWrites.go:136`




## api/agnostic/repocreateRecord.go


📄 Исходный файл: `api/agnostic/repocreateRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoCreateRecord](#repocreaterecord-apiagnosticrepocreaterecordgo44) `:44`


</details>


[function] name: RepoCreateRecord file: api/agnostic/repocreateRecord.go:44 returns_error: да description: RepoCreateRecord calls the XRPC method "com.atproto.repo.createRecord".


### RepoCreateRecord (api/agnostic/repocreateRecord.go:44)


RepoCreateRecord calls the XRPC method "com.atproto.repo.createRecord".


```go
func RepoCreateRecord((*RepoCreateRecord_Output, error)) (*RepoCreateRecord_Output, error)
```


**Тип запроса:** RepoCreateRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repocreateRecord.go`


**Тип ответа:** RepoCreateRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repocreateRecord.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoCreateRecord_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/repocreateRecord.go:44`




## api/agnostic/repogetRecord.go


📄 Исходный файл: `api/agnostic/repogetRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoGetRecord](#repogetrecord-apiagnosticrepogetrecordgo28) `:28`


</details>


[function] name: RepoGetRecord file: api/agnostic/repogetRecord.go:28 returns_error: да description: RepoGetRecord calls the XRPC method "com.atproto.repo.getRecord".

cid: The CID of the version of the record. If not spe


### RepoGetRecord (api/agnostic/repogetRecord.go:28)


RepoGetRecord calls the XRPC method "com.atproto.repo.getRecord".

cid: The CID of the version of the record. If not specified, then return the most recent version.
collection: The NSID of the record collection.
repo: The handle or DID of the repo.
rkey: The Record Key.


```go
func RepoGetRecord((*RepoGetRecord_Output, error)) (*RepoGetRecord_Output, error)
```


**Тип запроса:** RepoGetRecord_Output


```json
{
  "cid": "string",
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/agnostic/repogetRecord.go`


**Тип ответа:** RepoGetRecord_Output


```json
{
  "cid": "string",
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/agnostic/repogetRecord.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoGetRecord_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/repogetRecord.go:28`




## api/agnostic/repolistRecords.go


📄 Исходный файл: `api/agnostic/repolistRecords.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoListRecords](#repolistrecords-apiagnosticrepolistrecordsgo34) `:34`


</details>


[function] name: RepoListRecords file: api/agnostic/repolistRecords.go:34 returns_error: да description: RepoListRecords calls the XRPC method "com.atproto.repo.listRecords".

collection: The NSID of the record type.
limit: T


### RepoListRecords (api/agnostic/repolistRecords.go:34)


RepoListRecords calls the XRPC method "com.atproto.repo.listRecords".

collection: The NSID of the record type.
limit: The number of records to return.
repo: The handle or DID of the repo.
reverse: Flag to reverse the order of the returned records.


```go
func RepoListRecords((*RepoListRecords_Output, error)) (*RepoListRecords_Output, error)
```


**Тип запроса:** RepoListRecords_Output


```json
{
  "cursor": "string",
  "records": []
}
```


*Определено в:* `api/agnostic/repolistRecords.go`


**Тип ответа:** RepoListRecords_Output


```json
{
  "cursor": "string",
  "records": []
}
```


*Определено в:* `api/agnostic/repolistRecords.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoListRecords_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/repolistRecords.go:34`




## api/agnostic/repoputRecord.go


📄 Исходный файл: `api/agnostic/repoputRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoPutRecord](#repoputrecord-apiagnosticrepoputrecordgo40) `:40`


</details>


[function] name: RepoPutRecord file: api/agnostic/repoputRecord.go:40 returns_error: да description: RepoPutRecord calls the XRPC method "com.atproto.repo.putRecord".


### RepoPutRecord (api/agnostic/repoputRecord.go:40)


RepoPutRecord calls the XRPC method "com.atproto.repo.putRecord".


```go
func RepoPutRecord((*RepoPutRecord_Output, error)) (*RepoPutRecord_Output, error)
```


**Тип запроса:** RepoPutRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repoputRecord.go`


**Тип ответа:** RepoPutRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repoputRecord.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoPutRecord_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/agnostic/repoputRecord.go:40`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Следующая директория](api_atproto.md)


---

