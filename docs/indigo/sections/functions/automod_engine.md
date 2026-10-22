---
title: "Функции: automod/engine"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/engine
---


# Функции: automod/engine


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_countstore.md)

- [Следующая директория](automod_flagstore.md)


---


## Меню по файлам


- 📄 [automod/engine/blobs.go](#automodengineblobsgo)

- 📄 [automod/engine/context.go](#automodenginecontextgo)

- 📄 [automod/engine/effects.go](#automodengineeffectsgo)

- 📄 [automod/engine/engine.go](#automodengineenginego)

- 📄 [automod/engine/engine_ozone.go](#automodengineengine_ozonego)

- 📄 [automod/engine/fetch_account_meta.go](#automodenginefetch_account_metago)

- 📄 [automod/engine/fetch_relationship.go](#automodenginefetch_relationshipgo)

- 📄 [automod/engine/persist.go](#automodenginepersistgo)

- 📄 [automod/engine/persisthelpers.go](#automodenginepersisthelpersgo)

- 📄 [automod/engine/report.go](#automodenginereportgo)

- 📄 [automod/engine/ruleset.go](#automodenginerulesetgo)

- 📄 [automod/engine/slack.go](#automodengineslackgo)

- 📄 [automod/engine/testing.go](#automodenginetestinggo)

- 📄 [automod/engine/util.go](#automodengineutilgo)


---


## automod/engine/blobs.go


📄 Исходный файл: `automod/engine/blobs.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Blobs](#blobs-automodengineblobsgo19) `:19`

- 🔗 [fetchBlob](#fetchblob-automodengineblobsgo44) `:44`


</details>


[function] name: Blobs file: automod/engine/blobs.go:19 returns_error: да description: Parses out any blobs from the enclosed record.

NOTE: for consistency with other RecordContext methods, which don't usua


### Blobs (automod/engine/blobs.go:19)


Parses out any blobs from the enclosed record.

NOTE: for consistency with other RecordContext methods, which don't usually return errors, maybe the error-returning version of this function should be a helper function, or defined on RecordOp, and the RecordContext version should return an empty array on error?


```go
func (c *RecordContext) Blobs(([]lexutil.LexBlob, error)) ([]lexutil.LexBlob, error)
```


**Тип ответа:** lexutil.LexBlob


```json
{
  "Ref": {},
  "MimeType": "string",
  "Size": 0
}
```


*Определено в:* `lex/util/lex_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]lexutil.LexBlob`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/blobs.go:19`



---


[function] name: fetchBlob file: automod/engine/blobs.go:44 returns_error: да description: —


### fetchBlob (automod/engine/blobs.go:44)


fetchBlob is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *RecordContext) fetchBlob(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/blobs.go:44`




## automod/engine/context.go


📄 Исходный файл: `automod/engine/context.go`


<details open>
<summary><b>Функции в этом файле (32)</b></summary>


- 🔗 [ATURI](#aturi-automodenginecontextgo111) `:111`

- 🔗 [AcknowledgeAccount](#acknowledgeaccount-automodenginecontextgo265) `:265`

- 🔗 [AcknowledgeRecord](#acknowledgerecord-automodenginecontextgo297) `:297`

- 🔗 [AddAccountFlag](#addaccountflag-automodenginecontextgo237) `:237`

- 🔗 [AddAccountLabel](#addaccountlabel-automodenginecontextgo241) `:241`

- 🔗 [AddAccountTag](#addaccounttag-automodenginecontextgo249) `:249`

- 🔗 [AddRecordFlag](#addrecordflag-automodenginecontextgo269) `:269`

- 🔗 [AddRecordLabel](#addrecordlabel-automodenginecontextgo273) `:273`

- 🔗 [AddRecordTag](#addrecordtag-automodenginecontextgo281) `:281`

- 🔗 [Directory](#directory-automodenginecontextgo118) `:118`

- 🔗 [EscalateAccount](#escalateaccount-automodenginecontextgo261) `:261`

- 🔗 [EscalateRecord](#escalaterecord-automodenginecontextgo293) `:293`

- 🔗 [GetAccountMeta](#getaccountmeta-automodenginecontextgo200) `:200`

- 🔗 [GetAccountRelationship](#getaccountrelationship-automodenginecontextgo186) `:186`

- 🔗 [GetCount](#getcount-automodenginecontextgo123) `:123`

- 🔗 [GetCountDistinct](#getcountdistinct-automodenginecontextgo134) `:134`

- 🔗 [InSet](#inset-automodenginecontextgo145) `:145`

- 🔗 [Increment](#increment-automodenginecontextgo221) `:221`

- 🔗 [IncrementDistinct](#incrementdistinct-automodenginecontextgo225) `:225`

- 🔗 [IncrementPeriod](#incrementperiod-automodenginecontextgo229) `:229`

- 🔗 [InternalEngine](#internalengine-automodenginecontextgo159) `:159`

- 🔗 [NewAccountContext](#newaccountcontext-automodenginecontextgo163) `:163`

- 🔗 [NewRecordContext](#newrecordcontext-automodenginecontextgo176) `:176`

- 🔗 [Notify](#notify-automodenginecontextgo233) `:233`

- 🔗 [RemoveAccountLabel](#removeaccountlabel-automodenginecontextgo245) `:245`

- 🔗 [RemoveRecordLabel](#removerecordlabel-automodenginecontextgo277) `:277`

- 🔗 [ReportAccount](#reportaccount-automodenginecontextgo253) `:253`

- 🔗 [ReportRecord](#reportrecord-automodenginecontextgo285) `:285`

- 🔗 [TakedownAccount](#takedownaccount-automodenginecontextgo257) `:257`

- 🔗 [TakedownBlob](#takedownblob-automodenginecontextgo301) `:301`

- 🔗 [TakedownRecord](#takedownrecord-automodenginecontextgo289) `:289`

- 🔗 [Validate](#validate-automodenginecontextgo95) `:95`


</details>


[function] name: ATURI file: automod/engine/context.go:111 returns_error: нет description: —


### ATURI (automod/engine/context.go:111)


ATURI is a method that performs operations based on the provided parameters and returns ().


```go
func (op *RecordOp) ATURI(()) ()
```


📍 *Расположение:* `automod/engine/context.go:111`



---


[function] name: AcknowledgeAccount file: automod/engine/context.go:265 returns_error: нет description: —


### AcknowledgeAccount (automod/engine/context.go:265)


AcknowledgeAccount is a method that performs operations based on the provided parameters and returns ().


```go
func (c *AccountContext) AcknowledgeAccount(()) ()
```


📍 *Расположение:* `automod/engine/context.go:265`



---


[function] name: AcknowledgeRecord file: automod/engine/context.go:297 returns_error: нет description: —


### AcknowledgeRecord (automod/engine/context.go:297)


AcknowledgeRecord is a method that performs operations based on the provided parameters and returns ().


```go
func (c *RecordContext) AcknowledgeRecord(()) ()
```


📍 *Расположение:* `automod/engine/context.go:297`



---


[function] name: AddAccountFlag file: automod/engine/context.go:237 returns_error: нет description: —


### AddAccountFlag (automod/engine/context.go:237)


AddAccountFlag is a method that creates new data based on the provided parameters and returns (val string).


```go
func (c *AccountContext) AddAccountFlag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:237`



---


[function] name: AddAccountLabel file: automod/engine/context.go:241 returns_error: нет description: —


### AddAccountLabel (automod/engine/context.go:241)


AddAccountLabel is a method that creates new data based on the provided parameters and returns (val string).


```go
func (c *AccountContext) AddAccountLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:241`



---


[function] name: AddAccountTag file: automod/engine/context.go:249 returns_error: нет description: —


### AddAccountTag (automod/engine/context.go:249)


AddAccountTag is a method that creates new data based on the provided parameters and returns (val string).


```go
func (c *AccountContext) AddAccountTag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:249`



---


[function] name: AddRecordFlag file: automod/engine/context.go:269 returns_error: нет description: —


### AddRecordFlag (automod/engine/context.go:269)


AddRecordFlag is a method that creates new data based on the provided parameters and returns (val string).


```go
func (c *RecordContext) AddRecordFlag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:269`



---


[function] name: AddRecordLabel file: automod/engine/context.go:273 returns_error: нет description: —


### AddRecordLabel (automod/engine/context.go:273)


AddRecordLabel is a method that creates new data based on the provided parameters and returns (val string).


```go
func (c *RecordContext) AddRecordLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:273`



---


[function] name: AddRecordTag file: automod/engine/context.go:281 returns_error: нет description: —


### AddRecordTag (automod/engine/context.go:281)


AddRecordTag is a method that creates new data based on the provided parameters and returns (val string).


```go
func (c *RecordContext) AddRecordTag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:281`



---


[function] name: Directory file: automod/engine/context.go:118 returns_error: нет description: Access to engine's identity directory (without access to other engine fields)


### Directory (automod/engine/context.go:118)


Access to engine's identity directory (without access to other engine fields)


```go
func (c *BaseContext) Directory(()) ()
```


📍 *Расположение:* `automod/engine/context.go:118`



---


[function] name: EscalateAccount file: automod/engine/context.go:261 returns_error: нет description: —


### EscalateAccount (automod/engine/context.go:261)


EscalateAccount is a method that performs operations based on the provided parameters and returns ().


```go
func (c *AccountContext) EscalateAccount(()) ()
```


📍 *Расположение:* `automod/engine/context.go:261`



---


[function] name: EscalateRecord file: automod/engine/context.go:293 returns_error: нет description: —


### EscalateRecord (automod/engine/context.go:293)


EscalateRecord is a method that performs operations based on the provided parameters and returns ().


```go
func (c *RecordContext) EscalateRecord(()) ()
```


📍 *Расположение:* `automod/engine/context.go:293`



---


[function] name: GetAccountMeta file: automod/engine/context.go:200 returns_error: нет description: fetch account metadata for the given DID. if there is any problem with lookup, returns nil.

TODO: should this take an A


### GetAccountMeta (automod/engine/context.go:200)


fetch account metadata for the given DID. if there is any problem with lookup, returns nil.

TODO: should this take an AtIdentifier instead?


```go
func (c *BaseContext) GetAccountMeta((did syntax.DID)) (did syntax.DID)
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


📍 *Расположение:* `automod/engine/context.go:200`



---


[function] name: GetAccountRelationship file: automod/engine/context.go:186 returns_error: нет description: fetch relationship metadata between this account and another account


### GetAccountRelationship (automod/engine/context.go:186)


fetch relationship metadata between this account and another account


```go
func (c *AccountContext) GetAccountRelationship((other syntax.DID)) (other syntax.DID)
```


**Тип ответа:** other


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


📍 *Расположение:* `automod/engine/context.go:186`



---


[function] name: GetCount file: automod/engine/context.go:123 returns_error: нет description: request external state via engine (indirect)


### GetCount (automod/engine/context.go:123)


request external state via engine (indirect)


```go
func (c *BaseContext) GetCount((name, val, period string)) (name, val, period string)
```


**Тип ответа:** name


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


**Тип ответа:** period


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/context.go:123`



---


[function] name: GetCountDistinct file: automod/engine/context.go:134 returns_error: нет description: —


### GetCountDistinct (automod/engine/context.go:134)


GetCountDistinct is a method that retrieves data based on the provided parameters and returns (name, bucket, period string).


```go
func (c *BaseContext) GetCountDistinct((name, bucket, period string)) (name, bucket, period string)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bucket


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** period


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/context.go:134`



---


[function] name: InSet file: automod/engine/context.go:145 returns_error: нет description: —


### InSet (automod/engine/context.go:145)


InSet is a method that performs operations based on the provided parameters and returns (name, val string).


```go
func (c *BaseContext) InSet((name, val string)) (name, val string)
```


**Тип ответа:** name


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


📍 *Расположение:* `automod/engine/context.go:145`



---


[function] name: Increment file: automod/engine/context.go:221 returns_error: нет description: update effects (indirect) ======


### Increment (automod/engine/context.go:221)


update effects (indirect) ======


```go
func (c *BaseContext) Increment((name, val string)) (name, val string)
```


**Тип ответа:** name


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


📍 *Расположение:* `automod/engine/context.go:221`



---


[function] name: IncrementDistinct file: automod/engine/context.go:225 returns_error: нет description: —


### IncrementDistinct (automod/engine/context.go:225)


IncrementDistinct is a method that performs operations based on the provided parameters and returns (name, bucket, val string).


```go
func (c *BaseContext) IncrementDistinct((name, bucket, val string)) (name, bucket, val string)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bucket


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


📍 *Расположение:* `automod/engine/context.go:225`



---


[function] name: IncrementPeriod file: automod/engine/context.go:229 returns_error: нет description: —


### IncrementPeriod (automod/engine/context.go:229)


IncrementPeriod is a method that performs operations based on the provided parameters and returns (name, val string, period string).


```go
func (c *BaseContext) IncrementPeriod((name, val string, period string)) (name, val string, period string)
```


**Тип ответа:** name


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


**Тип ответа:** period


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/context.go:229`



---


[function] name: InternalEngine file: automod/engine/context.go:159 returns_error: нет description: Returns a pointer to the underlying automod engine. This usually should NOT be used in rules.

This is an escape hatch f


### InternalEngine (automod/engine/context.go:159)


Returns a pointer to the underlying automod engine. This usually should NOT be used in rules.

This is an escape hatch for hacking on the system before features get fully integerated in to the content API surface. The Engine API is not stable.


```go
func (c *BaseContext) InternalEngine(()) ()
```


📍 *Расположение:* `automod/engine/context.go:159`



---


[function] name: NewAccountContext file: automod/engine/context.go:163 returns_error: нет description: —


### NewAccountContext (automod/engine/context.go:163)


NewAccountContext is a function that performs operations based on the provided parameters and returns (ctx context.Context, eng *Engine, meta AccountMeta).


```go
func NewAccountContext((ctx context.Context, eng *Engine, meta AccountMeta)) (ctx context.Context, eng *Engine, meta AccountMeta)
```


**Тип запроса:** Engine


```json
{
  "Logger": null,
  "Directory": {},
  "Rules": {},
  "Counters": {},
  "Sets": {},
  "Cache": {},
  "Flags": {},
  "Notifier": {},
  "BskyClient": null,
  "OzoneClient": null,
  "AdminClient": null,
  "BlobClient": null,
  "Config": {}
}
```


*Определено в:* `automod/engine/engine.go`


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


**Тип ответа:** eng


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Engine


```json
{
  "Logger": null,
  "Directory": {},
  "Rules": {},
  "Counters": {},
  "Sets": {},
  "Cache": {},
  "Flags": {},
  "Notifier": {},
  "BskyClient": null,
  "OzoneClient": null,
  "AdminClient": null,
  "BlobClient": null,
  "Config": {}
}
```


*Определено в:* `automod/engine/engine.go`


**Тип ответа:** meta


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountMeta


```json
{
  "Identity": null,
  "Profile": {},
  "Private": null,
  "AccountLabels": [],
  "AccountNegatedLabels": [],
  "AccountFlags": [],
  "FollowersCount": 0,
  "FollowsCount": 0,
  "PostsCount": 0,
  "Takendown": false,
  "Deactivated": false,
  "CreatedAt": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `automod/engine/account_meta.go`


📍 *Расположение:* `automod/engine/context.go:163`



---


[function] name: NewRecordContext file: automod/engine/context.go:176 returns_error: нет description: —


### NewRecordContext (automod/engine/context.go:176)


NewRecordContext is a function that performs operations based on the provided parameters and returns (ctx context.Context, eng *Engine, meta AccountMeta, op RecordOp).


```go
func NewRecordContext((ctx context.Context, eng *Engine, meta AccountMeta, op RecordOp)) (ctx context.Context, eng *Engine, meta AccountMeta, op RecordOp)
```


**Тип запроса:** Engine


```json
{
  "Logger": null,
  "Directory": {},
  "Rules": {},
  "Counters": {},
  "Sets": {},
  "Cache": {},
  "Flags": {},
  "Notifier": {},
  "BskyClient": null,
  "OzoneClient": null,
  "AdminClient": null,
  "BlobClient": null,
  "Config": {}
}
```


*Определено в:* `automod/engine/engine.go`


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


**Тип ответа:** eng


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Engine


```json
{
  "Logger": null,
  "Directory": {},
  "Rules": {},
  "Counters": {},
  "Sets": {},
  "Cache": {},
  "Flags": {},
  "Notifier": {},
  "BskyClient": null,
  "OzoneClient": null,
  "AdminClient": null,
  "BlobClient": null,
  "Config": {}
}
```


*Определено в:* `automod/engine/engine.go`


**Тип ответа:** meta


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountMeta


```json
{
  "Identity": null,
  "Profile": {},
  "Private": null,
  "AccountLabels": [],
  "AccountNegatedLabels": [],
  "AccountFlags": [],
  "FollowersCount": 0,
  "FollowsCount": 0,
  "PostsCount": 0,
  "Takendown": false,
  "Deactivated": false,
  "CreatedAt": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `automod/engine/account_meta.go`


**Тип ответа:** op


```json
{
  "HTTPMethod": "string",
  "TargetURI": "string",
  "AccessTokenHash": "string",
  "Nonce": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** RecordOp


```json
{
  "Action": "string",
  "DID": {},
  "Collection": {},
  "RecordKey": {},
  "CID": null,
  "RecordCBOR": []
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/context.go:176`



---


[function] name: Notify file: automod/engine/context.go:233 returns_error: нет description: —


### Notify (automod/engine/context.go:233)


Notify is a method that performs operations based on the provided parameters and returns (srv string).


```go
func (c *BaseContext) Notify((srv string)) (srv string)
```


**Тип ответа:** srv


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/context.go:233`



---


[function] name: RemoveAccountLabel file: automod/engine/context.go:245 returns_error: нет description: —


### RemoveAccountLabel (automod/engine/context.go:245)


RemoveAccountLabel is a method that deletes data based on the provided parameters and returns (val string).


```go
func (c *AccountContext) RemoveAccountLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:245`



---


[function] name: RemoveRecordLabel file: automod/engine/context.go:277 returns_error: нет description: —


### RemoveRecordLabel (automod/engine/context.go:277)


RemoveRecordLabel is a method that deletes data based on the provided parameters and returns (val string).


```go
func (c *RecordContext) RemoveRecordLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/context.go:277`



---


[function] name: ReportAccount file: automod/engine/context.go:253 returns_error: нет description: —


### ReportAccount (automod/engine/context.go:253)


ReportAccount is a method that performs operations based on the provided parameters and returns (reason, comment string).


```go
func (c *AccountContext) ReportAccount((reason, comment string)) (reason, comment string)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comment


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/context.go:253`



---


[function] name: ReportRecord file: automod/engine/context.go:285 returns_error: нет description: —


### ReportRecord (automod/engine/context.go:285)


ReportRecord is a method that performs operations based on the provided parameters and returns (reason, comment string).


```go
func (c *RecordContext) ReportRecord((reason, comment string)) (reason, comment string)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comment


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/context.go:285`



---


[function] name: TakedownAccount file: automod/engine/context.go:257 returns_error: нет description: —


### TakedownAccount (automod/engine/context.go:257)


TakedownAccount is a method that performs operations based on the provided parameters and returns ().


```go
func (c *AccountContext) TakedownAccount(()) ()
```


📍 *Расположение:* `automod/engine/context.go:257`



---


[function] name: TakedownBlob file: automod/engine/context.go:301 returns_error: нет description: —


### TakedownBlob (automod/engine/context.go:301)


TakedownBlob is a method that performs operations based on the provided parameters and returns (cid string).


```go
func (c *RecordContext) TakedownBlob((cid string)) (cid string)
```


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/context.go:301`



---


[function] name: TakedownRecord file: automod/engine/context.go:289 returns_error: нет description: —


### TakedownRecord (automod/engine/context.go:289)


TakedownRecord is a method that performs operations based on the provided parameters and returns ().


```go
func (c *RecordContext) TakedownRecord(()) ()
```


📍 *Расположение:* `automod/engine/context.go:289`



---


[function] name: Validate file: automod/engine/context.go:95 returns_error: нет description: Checks that op has expected fields, based on the action type


### Validate (automod/engine/context.go:95)


Checks that op has expected fields, based on the action type


```go
func (op *RecordOp) Validate(()) ()
```


📍 *Расположение:* `automod/engine/context.go:95`




## automod/engine/effects.go


📄 Исходный файл: `automod/engine/effects.go`


<details open>
<summary><b>Функции в этом файле (22)</b></summary>


- 🔗 [AcknowledgeAccount](#acknowledgeaccount-automodengineeffectsgo167) `:167`

- 🔗 [AcknowledgeRecord](#acknowledgerecord-automodengineeffectsgo245) `:245`

- 🔗 [AddAccountFlag](#addaccountflag-automodengineeffectsgo130) `:130`

- 🔗 [AddAccountLabel](#addaccountlabel-automodengineeffectsgo94) `:94`

- 🔗 [AddAccountTag](#addaccounttag-automodengineeffectsgo118) `:118`

- 🔗 [AddRecordFlag](#addrecordflag-automodengineeffectsgo208) `:208`

- 🔗 [AddRecordLabel](#addrecordlabel-automodengineeffectsgo172) `:172`

- 🔗 [AddRecordTag](#addrecordtag-automodengineeffectsgo196) `:196`

- 🔗 [EscalateAccount](#escalateaccount-automodengineeffectsgo162) `:162`

- 🔗 [EscalateRecord](#escalaterecord-automodengineeffectsgo240) `:240`

- 🔗 [Increment](#increment-automodengineeffectsgo73) `:73`

- 🔗 [IncrementDistinct](#incrementdistinct-automodengineeffectsgo87) `:87`

- 🔗 [IncrementPeriod](#incrementperiod-automodengineeffectsgo80) `:80`

- 🔗 [Notify](#notify-automodengineeffectsgo262) `:262`

- 🔗 [Reject](#reject-automodengineeffectsgo273) `:273`

- 🔗 [RemoveAccountLabel](#removeaccountlabel-automodengineeffectsgo106) `:106`

- 🔗 [RemoveRecordLabel](#removerecordlabel-automodengineeffectsgo184) `:184`

- 🔗 [ReportAccount](#reportaccount-automodengineeffectsgo142) `:142`

- 🔗 [ReportRecord](#reportrecord-automodengineeffectsgo220) `:220`

- 🔗 [TakedownAccount](#takedownaccount-automodengineeffectsgo157) `:157`

- 🔗 [TakedownBlob](#takedownblob-automodengineeffectsgo250) `:250`

- 🔗 [TakedownRecord](#takedownrecord-automodengineeffectsgo235) `:235`


</details>


[function] name: AcknowledgeAccount file: automod/engine/effects.go:167 returns_error: нет description: Enqueues reports on account to be "acknowledged" (closed) at the end of rule processing.


### AcknowledgeAccount (automod/engine/effects.go:167)


Enqueues reports on account to be "acknowledged" (closed) at the end of rule processing.


```go
func (e *Effects) AcknowledgeAccount(()) ()
```


📍 *Расположение:* `automod/engine/effects.go:167`



---


[function] name: AcknowledgeRecord file: automod/engine/effects.go:245 returns_error: нет description: Enqueues the record to be "escalated" for mod review at the end of rule processing.


### AcknowledgeRecord (automod/engine/effects.go:245)


Enqueues the record to be "escalated" for mod review at the end of rule processing.


```go
func (e *Effects) AcknowledgeRecord(()) ()
```


📍 *Расположение:* `automod/engine/effects.go:245`



---


[function] name: AddAccountFlag file: automod/engine/effects.go:130 returns_error: нет description: Enqueues the provided flag (string value) to be recorded (in the Engine's flagstore) at the end of rule processing.


### AddAccountFlag (automod/engine/effects.go:130)


Enqueues the provided flag (string value) to be recorded (in the Engine's flagstore) at the end of rule processing.


```go
func (e *Effects) AddAccountFlag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:130`



---


[function] name: AddAccountLabel file: automod/engine/effects.go:94 returns_error: нет description: Enqueues the provided label (string value) to be added to the account at the end of rule processing.


### AddAccountLabel (automod/engine/effects.go:94)


Enqueues the provided label (string value) to be added to the account at the end of rule processing.


```go
func (e *Effects) AddAccountLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:94`



---


[function] name: AddAccountTag file: automod/engine/effects.go:118 returns_error: нет description: Enqueues the provided label (string value) to be added to the account at the end of rule processing.


### AddAccountTag (automod/engine/effects.go:118)


Enqueues the provided label (string value) to be added to the account at the end of rule processing.


```go
func (e *Effects) AddAccountTag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:118`



---


[function] name: AddRecordFlag file: automod/engine/effects.go:208 returns_error: нет description: Enqueues the provided flag (string value) to be recorded (in the Engine's flagstore) at the end of rule processing.


### AddRecordFlag (automod/engine/effects.go:208)


Enqueues the provided flag (string value) to be recorded (in the Engine's flagstore) at the end of rule processing.


```go
func (e *Effects) AddRecordFlag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:208`



---


[function] name: AddRecordLabel file: automod/engine/effects.go:172 returns_error: нет description: Enqueues the provided label (string value) to be added to the record at the end of rule processing.


### AddRecordLabel (automod/engine/effects.go:172)


Enqueues the provided label (string value) to be added to the record at the end of rule processing.


```go
func (e *Effects) AddRecordLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:172`



---


[function] name: AddRecordTag file: automod/engine/effects.go:196 returns_error: нет description: Enqueues the provided tag (string value) to be added to the record at the end of rule processing.


### AddRecordTag (automod/engine/effects.go:196)


Enqueues the provided tag (string value) to be added to the record at the end of rule processing.


```go
func (e *Effects) AddRecordTag((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:196`



---


[function] name: EscalateAccount file: automod/engine/effects.go:162 returns_error: нет description: Enqueues the account to be "escalated" for mod review at the end of rule processing.


### EscalateAccount (automod/engine/effects.go:162)


Enqueues the account to be "escalated" for mod review at the end of rule processing.


```go
func (e *Effects) EscalateAccount(()) ()
```


📍 *Расположение:* `automod/engine/effects.go:162`



---


[function] name: EscalateRecord file: automod/engine/effects.go:240 returns_error: нет description: Enqueues the record to be "escalated" for mod review at the end of rule processing.


### EscalateRecord (automod/engine/effects.go:240)


Enqueues the record to be "escalated" for mod review at the end of rule processing.


```go
func (e *Effects) EscalateRecord(()) ()
```


📍 *Расположение:* `automod/engine/effects.go:240`



---


[function] name: Increment file: automod/engine/effects.go:73 returns_error: нет description: Enqueues the named counter to be incremented at the end of all rule processing. Will automatically increment for all tim


### Increment (automod/engine/effects.go:73)


Enqueues the named counter to be incremented at the end of all rule processing. Will automatically increment for all time periods.

"name" is the counter namespace.
"val" is the specific counter with that namespace.


```go
func (e *Effects) Increment((name, val string)) (name, val string)
```


**Тип ответа:** name


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


📍 *Расположение:* `automod/engine/effects.go:73`



---


[function] name: IncrementDistinct file: automod/engine/effects.go:87 returns_error: нет description: Enqueues the named "distinct value" counter based on the supplied string value ("val") to be incremented at the end of a


### IncrementDistinct (automod/engine/effects.go:87)


Enqueues the named "distinct value" counter based on the supplied string value ("val") to be incremented at the end of all rule processing. Will automatically increment for all time periods.


```go
func (e *Effects) IncrementDistinct((name, bucket, val string)) (name, bucket, val string)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bucket


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


📍 *Расположение:* `automod/engine/effects.go:87`



---


[function] name: IncrementPeriod file: automod/engine/effects.go:80 returns_error: нет description: Enqueues the named counter to be incremented at the end of all rule processing. Will only increment the indicated time p


### IncrementPeriod (automod/engine/effects.go:80)


Enqueues the named counter to be incremented at the end of all rule processing. Will only increment the indicated time period bucket.


```go
func (e *Effects) IncrementPeriod((name, val string, period string)) (name, val string, period string)
```


**Тип ответа:** name


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


**Тип ответа:** period


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/effects.go:80`



---


[function] name: Notify file: automod/engine/effects.go:262 returns_error: нет description: Records that the given service should be notified about this event


### Notify (automod/engine/effects.go:262)


Records that the given service should be notified about this event


```go
func (e *Effects) Notify((srv string)) (srv string)
```


**Тип ответа:** srv


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/effects.go:262`



---


[function] name: Reject file: automod/engine/effects.go:273 returns_error: нет description: —


### Reject (automod/engine/effects.go:273)


Reject is a method that performs operations based on the provided parameters and returns ().


```go
func (e *Effects) Reject(()) ()
```


📍 *Расположение:* `automod/engine/effects.go:273`



---


[function] name: RemoveAccountLabel file: automod/engine/effects.go:106 returns_error: нет description: Enqueues the provided label (string value) to be removed from the account at the end of rule processing.


### RemoveAccountLabel (automod/engine/effects.go:106)


Enqueues the provided label (string value) to be removed from the account at the end of rule processing.


```go
func (e *Effects) RemoveAccountLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:106`



---


[function] name: RemoveRecordLabel file: automod/engine/effects.go:184 returns_error: нет description: Enqueues the provided label (string value) to be removed from the record at the end of rule processing.


### RemoveRecordLabel (automod/engine/effects.go:184)


Enqueues the provided label (string value) to be removed from the record at the end of rule processing.


```go
func (e *Effects) RemoveRecordLabel((val string)) (val string)
```


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


📍 *Расположение:* `automod/engine/effects.go:184`



---


[function] name: ReportAccount file: automod/engine/effects.go:142 returns_error: нет description: Enqueues a moderation report to be filed against the account at the end of rule processing.


### ReportAccount (automod/engine/effects.go:142)


Enqueues a moderation report to be filed against the account at the end of rule processing.


```go
func (e *Effects) ReportAccount((reason, comment string)) (reason, comment string)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comment


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/effects.go:142`



---


[function] name: ReportRecord file: automod/engine/effects.go:220 returns_error: нет description: Enqueues a moderation report to be filed against the record at the end of rule processing.


### ReportRecord (automod/engine/effects.go:220)


Enqueues a moderation report to be filed against the record at the end of rule processing.


```go
func (e *Effects) ReportRecord((reason, comment string)) (reason, comment string)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comment


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/effects.go:220`



---


[function] name: TakedownAccount file: automod/engine/effects.go:157 returns_error: нет description: Enqueues the entire account to be taken down at the end of rule processing.


### TakedownAccount (automod/engine/effects.go:157)


Enqueues the entire account to be taken down at the end of rule processing.


```go
func (e *Effects) TakedownAccount(()) ()
```


📍 *Расположение:* `automod/engine/effects.go:157`



---


[function] name: TakedownBlob file: automod/engine/effects.go:250 returns_error: нет description: Enqueues the blob CID to be taken down (aka, CDN purge) as part of any record takedown


### TakedownBlob (automod/engine/effects.go:250)


Enqueues the blob CID to be taken down (aka, CDN purge) as part of any record takedown


```go
func (e *Effects) TakedownBlob((cid string)) (cid string)
```


**Тип ответа:** cid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/effects.go:250`



---


[function] name: TakedownRecord file: automod/engine/effects.go:235 returns_error: нет description: Enqueues the record to be taken down at the end of rule processing.


### TakedownRecord (automod/engine/effects.go:235)


Enqueues the record to be taken down at the end of rule processing.


```go
func (e *Effects) TakedownRecord(()) ()
```


📍 *Расположение:* `automod/engine/effects.go:235`




## automod/engine/engine.go


📄 Исходный файл: `automod/engine/engine.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [CanonicalLogLineAccount](#canonicalloglineaccount-automodengineenginego310) `:310`

- 🔗 [CanonicalLogLineRecord](#canonicalloglinerecord-automodengineenginego320) `:320`

- 🔗 [ProcessAccountEvent](#processaccountevent-automodengineenginego143) `:143`

- 🔗 [ProcessIdentityEvent](#processidentityevent-automodengineenginego69) `:69`

- 🔗 [ProcessRecordOp](#processrecordop-automodengineenginego217) `:217`

- 🔗 [PurgeAccountCaches](#purgeaccountcaches-automodengineenginego300) `:300`


</details>


[function] name: CanonicalLogLineAccount file: automod/engine/engine.go:310 returns_error: нет description: —


### CanonicalLogLineAccount (automod/engine/engine.go:310)


CanonicalLogLineAccount is a method that performs operations based on the provided parameters and returns (c *AccountContext).


```go
func (e *Engine) CanonicalLogLineAccount((c *AccountContext)) (c *AccountContext)
```


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


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


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


📍 *Расположение:* `automod/engine/engine.go:310`



---


[function] name: CanonicalLogLineRecord file: automod/engine/engine.go:320 returns_error: нет description: —


### CanonicalLogLineRecord (automod/engine/engine.go:320)


CanonicalLogLineRecord is a method that performs operations based on the provided parameters and returns (c *RecordContext).


```go
func (e *Engine) CanonicalLogLineRecord((c *RecordContext)) (c *RecordContext)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/engine.go:320`



---


[function] name: ProcessAccountEvent file: automod/engine/engine.go:143 returns_error: нет description: Entrypoint for external code pushing #account events in to the engine.

This method can be called concurrently, though c


### ProcessAccountEvent (automod/engine/engine.go:143)


Entrypoint for external code pushing #account events in to the engine.

This method can be called concurrently, though cached state may end up inconsistent if multiple events for the same account (DID) are processed in parallel.


```go
func (eng *Engine) ProcessAccountEvent((ctx context.Context, evt comatproto.SyncSubscribeRepos_Account)) (ctx context.Context, evt comatproto.SyncSubscribeRepos_Account)
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


📍 *Расположение:* `automod/engine/engine.go:143`



---


[function] name: ProcessIdentityEvent file: automod/engine/engine.go:69 returns_error: нет description: Entrypoint for external code pushing #identity events in to the engine.

This method can be called concurrently, though 


### ProcessIdentityEvent (automod/engine/engine.go:69)


Entrypoint for external code pushing #identity events in to the engine.

This method can be called concurrently, though cached state may end up inconsistent if multiple events for the same account (DID) are processed in parallel.


```go
func (eng *Engine) ProcessIdentityEvent((ctx context.Context, evt comatproto.SyncSubscribeRepos_Identity)) (ctx context.Context, evt comatproto.SyncSubscribeRepos_Identity)
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


📍 *Расположение:* `automod/engine/engine.go:69`



---


[function] name: ProcessRecordOp file: automod/engine/engine.go:217 returns_error: нет description: Entrypoint for external code pushing repository updates. A simple repo commit results in multiple calls.

This method ca


### ProcessRecordOp (automod/engine/engine.go:217)


Entrypoint for external code pushing repository updates. A simple repo commit results in multiple calls.

This method can be called concurrently, though cached state may end up inconsistent if multiple events for the same account (DID) are processed in parallel.


```go
func (eng *Engine) ProcessRecordOp((ctx context.Context, op RecordOp)) (ctx context.Context, op RecordOp)
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


**Тип ответа:** op


```json
{
  "HTTPMethod": "string",
  "TargetURI": "string",
  "AccessTokenHash": "string",
  "Nonce": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** RecordOp


```json
{
  "Action": "string",
  "DID": {},
  "Collection": {},
  "RecordKey": {},
  "CID": null,
  "RecordCBOR": []
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/engine.go:217`



---


[function] name: PurgeAccountCaches file: automod/engine/engine.go:300 returns_error: нет description: Purge metadata caches for a specific account.


### PurgeAccountCaches (automod/engine/engine.go:300)


Purge metadata caches for a specific account.


```go
func (e *Engine) PurgeAccountCaches((ctx context.Context, did syntax.DID)) (ctx context.Context, did syntax.DID)
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


📍 *Расположение:* `automod/engine/engine.go:300`




## automod/engine/engine_ozone.go


📄 Исходный файл: `automod/engine/engine_ozone.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [CanonicalLogLineOzoneEvent](#canonicalloglineozoneevent-automodengineengine_ozonego212) `:212`

- 🔗 [NewOzoneEventContext](#newozoneeventcontext-automodengineengine_ozonego12) `:12`

- 🔗 [ProcessOzoneEvent](#processozoneevent-automodengineengine_ozonego154) `:154`


</details>


[function] name: CanonicalLogLineOzoneEvent file: automod/engine/engine_ozone.go:212 returns_error: нет description: —


### CanonicalLogLineOzoneEvent (automod/engine/engine_ozone.go:212)


CanonicalLogLineOzoneEvent is a method that performs operations based on the provided parameters and returns (c *OzoneEventContext).


```go
func (e *Engine) CanonicalLogLineOzoneEvent((c *OzoneEventContext)) (c *OzoneEventContext)
```


**Тип запроса:** OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
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


**Тип ответа:** OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/engine_ozone.go:212`



---


[function] name: NewOzoneEventContext file: automod/engine/engine_ozone.go:12 returns_error: да description: —


### NewOzoneEventContext (automod/engine/engine_ozone.go:12)


NewOzoneEventContext is a function that performs operations based on the provided parameters and may return an error.


```go
func NewOzoneEventContext((*OzoneEventContext, error)) (*OzoneEventContext, error)
```


**Тип запроса:** OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
}
```


*Определено в:* `automod/engine/context.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*OzoneEventContext`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/engine_ozone.go:12`



---


[function] name: ProcessOzoneEvent file: automod/engine/engine_ozone.go:154 returns_error: нет description: Entrypoint for external code pushing ozone events.

This method can be called concurrently, though cached state may end 


### ProcessOzoneEvent (automod/engine/engine_ozone.go:154)


Entrypoint for external code pushing ozone events.

This method can be called concurrently, though cached state may end up inconsistent if multiple events for the same account (DID) are processed in parallel.


```go
func (eng *Engine) ProcessOzoneEvent((ctx context.Context, eventView *toolsozone.ModerationDefs_ModEventView)) (ctx context.Context, eventView *toolsozone.ModerationDefs_ModEventView)
```


**Тип запроса:** toolsozone.ModerationDefs_ModEventView


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "creatorHandle": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobCids": [],
  "subjectHandle": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


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


**Тип ответа:** eventView


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** toolsozone.ModerationDefs_ModEventView


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "creatorHandle": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobCids": [],
  "subjectHandle": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


📍 *Расположение:* `automod/engine/engine_ozone.go:154`




## automod/engine/fetch_account_meta.go


📄 Исходный файл: `automod/engine/fetch_account_meta.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetAccountMeta](#getaccountmeta-automodenginefetch_account_metago21) `:21`


</details>


[function] name: GetAccountMeta file: automod/engine/fetch_account_meta.go:21 returns_error: да description: Helper to hydrate metadata about an account from several sources: PDS (if access), mod service (if access), public ident


### GetAccountMeta (automod/engine/fetch_account_meta.go:21)


Helper to hydrate metadata about an account from several sources: PDS (if access), mod service (if access), public identity resolution


```go
func (e *Engine) GetAccountMeta((*AccountMeta, error)) (*AccountMeta, error)
```


**Тип запроса:** AccountMeta


```json
{
  "Identity": null,
  "Profile": {},
  "Private": null,
  "AccountLabels": [],
  "AccountNegatedLabels": [],
  "AccountFlags": [],
  "FollowersCount": 0,
  "FollowsCount": 0,
  "PostsCount": 0,
  "Takendown": false,
  "Deactivated": false,
  "CreatedAt": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `automod/engine/account_meta.go`


**Тип ответа:** AccountMeta


```json
{
  "Identity": null,
  "Profile": {},
  "Private": null,
  "AccountLabels": [],
  "AccountNegatedLabels": [],
  "AccountFlags": [],
  "FollowersCount": 0,
  "FollowsCount": 0,
  "PostsCount": 0,
  "Takendown": false,
  "Deactivated": false,
  "CreatedAt": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `automod/engine/account_meta.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AccountMeta`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/fetch_account_meta.go:21`




## automod/engine/fetch_relationship.go


📄 Исходный файл: `automod/engine/fetch_relationship.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetAccountRelationship](#getaccountrelationship-automodenginefetch_relationshipgo23) `:23`


</details>


[function] name: GetAccountRelationship file: automod/engine/fetch_relationship.go:23 returns_error: да description: Helper to fetch social graph relationship metadata


### GetAccountRelationship (automod/engine/fetch_relationship.go:23)


Helper to fetch social graph relationship metadata


```go
func (eng *Engine) GetAccountRelationship((*AccountRelationship, error)) (*AccountRelationship, error)
```


**Тип запроса:** AccountRelationship


```json
{
  "DID": {},
  "FollowedBy": false,
  "Following": false
}
```


*Определено в:* `automod/engine/fetch_relationship.go`


**Тип ответа:** AccountRelationship


```json
{
  "DID": {},
  "FollowedBy": false,
  "Following": false
}
```


*Определено в:* `automod/engine/fetch_relationship.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AccountRelationship`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/fetch_relationship.go:23`




## automod/engine/persist.go


📄 Исходный файл: `automod/engine/persist.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [persistAccountModActions](#persistaccountmodactions-automodenginepersistgo41) `:41`

- 🔗 [persistCounters](#persistcounters-automodenginepersistgo12) `:12`

- 🔗 [persistRecordModActions](#persistrecordmodactions-automodenginepersistgo270) `:270`


</details>


[function] name: persistAccountModActions file: automod/engine/persist.go:41 returns_error: нет description: Persists account-level moderation actions: new labels, new tags, new flags, new takedowns, and reports.

If necessary, w


### persistAccountModActions (automod/engine/persist.go:41)


Persists account-level moderation actions: new labels, new tags, new flags, new takedowns, and reports.

If necessary, will "purge" identity and account caches, so that state updates will be picked up for subsequent events.

Note that this method expects to run *before* counts are persisted (it accesses and updates some counts)


```go
func (eng *Engine) persistAccountModActions((c *AccountContext)) (c *AccountContext)
```


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


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


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


📍 *Расположение:* `automod/engine/persist.go:41`



---


[function] name: persistCounters file: automod/engine/persist.go:12 returns_error: нет description: —


### persistCounters (automod/engine/persist.go:12)


persistCounters is a method that performs operations based on the provided parameters and returns (ctx context.Context, eff *Effects).


```go
func (eng *Engine) persistCounters((ctx context.Context, eff *Effects)) (ctx context.Context, eff *Effects)
```


**Тип запроса:** Effects


```json
{
  "mu": {},
  "CounterIncrements": [],
  "CounterDistinctIncrements": [],
  "AccountLabels": [],
  "RemovedAccountLabels": [],
  "AccountTags": [],
  "AccountFlags": [],
  "AccountReports": [],
  "AccountTakedown": false,
  "AccountEscalate": false,
  "AccountAcknowledge": false,
  "RecordLabels": [],
  "RemovedRecordLabels": [],
  "RecordTags": [],
  "RecordFlags": [],
  "RecordReports": [],
  "RecordTakedown": false,
  "RecordEscalate": false,
  "RecordAcknowledge": false,
  "BlobTakedowns": [],
  "RejectEvent": false,
  "NotifyServices": []
}
```


*Определено в:* `automod/engine/effects.go`


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


**Тип ответа:** eff


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Effects


```json
{
  "mu": {},
  "CounterIncrements": [],
  "CounterDistinctIncrements": [],
  "AccountLabels": [],
  "RemovedAccountLabels": [],
  "AccountTags": [],
  "AccountFlags": [],
  "AccountReports": [],
  "AccountTakedown": false,
  "AccountEscalate": false,
  "AccountAcknowledge": false,
  "RecordLabels": [],
  "RemovedRecordLabels": [],
  "RecordTags": [],
  "RecordFlags": [],
  "RecordReports": [],
  "RecordTakedown": false,
  "RecordEscalate": false,
  "RecordAcknowledge": false,
  "BlobTakedowns": [],
  "RejectEvent": false,
  "NotifyServices": []
}
```


*Определено в:* `automod/engine/effects.go`


📍 *Расположение:* `automod/engine/persist.go:12`



---


[function] name: persistRecordModActions file: automod/engine/persist.go:270 returns_error: нет description: Persists some record-level state: labels, tags, takedowns, reports.

NOTE: this method currently does *not* persist reco


### persistRecordModActions (automod/engine/persist.go:270)


Persists some record-level state: labels, tags, takedowns, reports.

NOTE: this method currently does *not* persist record-level flags to any storage, and does not de-dupe most actions, on the assumption that the record is new (from firehose) and has no existing mod state.


```go
func (eng *Engine) persistRecordModActions((c *RecordContext)) (c *RecordContext)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/persist.go:270`




## automod/engine/persisthelpers.go


📄 Исходный файл: `automod/engine/persisthelpers.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [circuitBreakModAction](#circuitbreakmodaction-automodenginepersisthelpersgo141) `:141`

- 🔗 [circuitBreakReports](#circuitbreakreports-automodenginepersisthelpersgo93) `:93`

- 🔗 [circuitBreakTakedown](#circuitbreaktakedown-automodenginepersisthelpersgo117) `:117`

- 🔗 [createRecordReportIfFresh](#createrecordreportiffresh-automodenginepersisthelpersgo253) `:253`

- 🔗 [createReportIfFresh](#createreportiffresh-automodenginepersisthelpersgo167) `:167`

- 🔗 [dedupeFlagActions](#dedupeflagactions-automodenginepersisthelpersgo55) `:55`

- 🔗 [dedupeLabelActions](#dedupelabelactions-automodenginepersisthelpersgo15) `:15`

- 🔗 [dedupeReportActions](#dedupereportactions-automodenginepersisthelpersgo72) `:72`

- 🔗 [dedupeTagActions](#dedupetagactions-automodenginepersisthelpersgo38) `:38`


</details>


[function] name: circuitBreakModAction file: automod/engine/persisthelpers.go:141 returns_error: да description: Combined circuit breaker for miscellaneous mod actions like: escalate, acknowledge


### circuitBreakModAction (automod/engine/persisthelpers.go:141)


Combined circuit breaker for miscellaneous mod actions like: escalate, acknowledge


```go
func (eng *Engine) circuitBreakModAction((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/persisthelpers.go:141`



---


[function] name: circuitBreakReports file: automod/engine/persisthelpers.go:93 returns_error: да description: —


### circuitBreakReports (automod/engine/persisthelpers.go:93)


circuitBreakReports is a method that performs operations based on the provided parameters and may return an error.


```go
func (eng *Engine) circuitBreakReports(([]ModReport, error)) ([]ModReport, error)
```


**Тип ответа:** ModReport


```json
{
  "ReasonType": "string",
  "Comment": "string"
}
```


*Определено в:* `automod/engine/report.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]ModReport`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/persisthelpers.go:93`



---


[function] name: circuitBreakTakedown file: automod/engine/persisthelpers.go:117 returns_error: да description: —


### circuitBreakTakedown (automod/engine/persisthelpers.go:117)


circuitBreakTakedown is a method that performs operations based on the provided parameters and may return an error.


```go
func (eng *Engine) circuitBreakTakedown((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/persisthelpers.go:117`



---


[function] name: createRecordReportIfFresh file: automod/engine/persisthelpers.go:253 returns_error: да description: Create a moderation report, but checks first if there was a similar recent one, and skips if so.

Returns a bool indicat


### createRecordReportIfFresh (automod/engine/persisthelpers.go:253)


Create a moderation report, but checks first if there was a similar recent one, and skips if so.

Returns a bool indicating if a new report was created.

TODO: merge this with createReportIfFresh()


```go
func (eng *Engine) createRecordReportIfFresh((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/persisthelpers.go:253`



---


[function] name: createReportIfFresh file: automod/engine/persisthelpers.go:167 returns_error: да description: Creates a moderation report, but checks first if there was a similar recent one, and skips if so.

Returns a bool indica


### createReportIfFresh (automod/engine/persisthelpers.go:167)


Creates a moderation report, but checks first if there was a similar recent one, and skips if so.

Returns a bool indicating if a new report was created.


```go
func (eng *Engine) createReportIfFresh((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/persisthelpers.go:167`



---


[function] name: dedupeFlagActions file: automod/engine/persisthelpers.go:55 returns_error: нет description: —


### dedupeFlagActions (automod/engine/persisthelpers.go:55)


dedupeFlagActions is a function that performs operations based on the provided parameters and returns (flags, existing []string).


```go
func dedupeFlagActions((flags, existing []string)) (flags, existing []string)
```


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/persisthelpers.go:55`



---


[function] name: dedupeLabelActions file: automod/engine/persisthelpers.go:15 returns_error: нет description: —


### dedupeLabelActions (automod/engine/persisthelpers.go:15)


dedupeLabelActions is a function that performs operations based on the provided parameters and returns (labels, existing, existingNegated []string).


```go
func dedupeLabelActions((labels, existing, existingNegated []string)) (labels, existing, existingNegated []string)
```


**Тип ответа:** labels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** existingNegated


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/persisthelpers.go:15`



---


[function] name: dedupeReportActions file: automod/engine/persisthelpers.go:72 returns_error: да description: —


### dedupeReportActions (automod/engine/persisthelpers.go:72)


dedupeReportActions is a method that performs operations based on the provided parameters and may return an error.


```go
func (eng *Engine) dedupeReportActions(([]ModReport, error)) ([]ModReport, error)
```


**Тип ответа:** ModReport


```json
{
  "ReasonType": "string",
  "Comment": "string"
}
```


*Определено в:* `automod/engine/report.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]ModReport`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/engine/persisthelpers.go:72`



---


[function] name: dedupeTagActions file: automod/engine/persisthelpers.go:38 returns_error: нет description: —


### dedupeTagActions (automod/engine/persisthelpers.go:38)


dedupeTagActions is a function that performs operations based on the provided parameters and returns (tags, existing []string).


```go
func dedupeTagActions((tags, existing []string)) (tags, existing []string)
```


**Тип ответа:** tags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/persisthelpers.go:38`




## automod/engine/report.go


📄 Исходный файл: `automod/engine/report.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ReasonShortName](#reasonshortname-automodenginereportgo18) `:18`


</details>


[function] name: ReasonShortName file: automod/engine/report.go:18 returns_error: нет description: —


### ReasonShortName (automod/engine/report.go:18)


ReasonShortName is a function that performs operations based on the provided parameters and returns (reason string).


```go
func ReasonShortName((reason string)) (reason string)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/report.go:18`




## automod/engine/ruleset.go


📄 Исходный файл: `automod/engine/ruleset.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [CallAccountRules](#callaccountrules-automodenginerulesetgo93) `:93`

- 🔗 [CallIdentityRules](#callidentityrules-automodenginerulesetgo82) `:82`

- 🔗 [CallOzoneEventRules](#callozoneeventrules-automodenginerulesetgo103) `:103`

- 🔗 [CallRecordDeleteRules](#callrecorddeleterules-automodenginerulesetgo71) `:71`

- 🔗 [CallRecordRules](#callrecordrules-automodenginerulesetgo25) `:25`

- 🔗 [fetchAndProcessBlobs](#fetchandprocessblobs-automodenginerulesetgo114) `:114`

- 🔗 [processBlob](#processblob-automodenginerulesetgo155) `:155`


</details>


[function] name: CallAccountRules file: automod/engine/ruleset.go:93 returns_error: нет description: Executes rules for account update events.


### CallAccountRules (automod/engine/ruleset.go:93)


Executes rules for account update events.


```go
func (r *RuleSet) CallAccountRules((c *AccountContext)) (c *AccountContext)
```


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


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


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


📍 *Расположение:* `automod/engine/ruleset.go:93`



---


[function] name: CallIdentityRules file: automod/engine/ruleset.go:82 returns_error: нет description: Executes rules for identity update events.


### CallIdentityRules (automod/engine/ruleset.go:82)


Executes rules for identity update events.


```go
func (r *RuleSet) CallIdentityRules((c *AccountContext)) (c *AccountContext)
```


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


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


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


📍 *Расположение:* `automod/engine/ruleset.go:82`



---


[function] name: CallOzoneEventRules file: automod/engine/ruleset.go:103 returns_error: нет description: —


### CallOzoneEventRules (automod/engine/ruleset.go:103)


CallOzoneEventRules is a method that performs operations based on the provided parameters and returns (c *OzoneEventContext).


```go
func (r *RuleSet) CallOzoneEventRules((c *OzoneEventContext)) (c *OzoneEventContext)
```


**Тип запроса:** OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
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


**Тип ответа:** OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/ruleset.go:103`



---


[function] name: CallRecordDeleteRules file: automod/engine/ruleset.go:71 returns_error: нет description: NOTE: this will probably be removed and merged in to `CallRecordRules`


### CallRecordDeleteRules (automod/engine/ruleset.go:71)


NOTE: this will probably be removed and merged in to `CallRecordRules`


```go
func (r *RuleSet) CallRecordDeleteRules((c *RecordContext)) (c *RecordContext)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/ruleset.go:71`



---


[function] name: CallRecordRules file: automod/engine/ruleset.go:25 returns_error: нет description: Executes all the various record-related rules. Only dispatches execution, does no other de-dupe or pre/post processing.


### CallRecordRules (automod/engine/ruleset.go:25)


Executes all the various record-related rules. Only dispatches execution, does no other de-dupe or pre/post processing.


```go
func (r *RuleSet) CallRecordRules((c *RecordContext)) (c *RecordContext)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/ruleset.go:25`



---


[function] name: fetchAndProcessBlobs file: automod/engine/ruleset.go:114 returns_error: нет description: high-level helper for fetching and processing blobs concurrently


### fetchAndProcessBlobs (automod/engine/ruleset.go:114)


high-level helper for fetching and processing blobs concurrently


```go
func (r *RuleSet) fetchAndProcessBlobs((c *RecordContext)) (c *RecordContext)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/ruleset.go:114`



---


[function] name: processBlob file: automod/engine/ruleset.go:155 returns_error: нет description: —


### processBlob (automod/engine/ruleset.go:155)


processBlob is a method that performs operations based on the provided parameters and returns (c *RecordContext, blob lexutil.LexBlob, data []byte).


```go
func (r *RuleSet) processBlob((c *RecordContext, blob lexutil.LexBlob, data []byte)) (c *RecordContext, blob lexutil.LexBlob, data []byte)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** blob


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexutil.LexBlob


```json
{
  "Ref": {},
  "MimeType": "string",
  "Size": 0
}
```


*Определено в:* `lex/util/lex_types.go`


**Тип ответа:** data


```json
{
  "AuthorizationServers": []
}
```


*Определено в:* `atproto/auth/oauth/types.go`


📍 *Расположение:* `automod/engine/ruleset.go:155`




## automod/engine/slack.go


📄 Исходный файл: `automod/engine/slack.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [SendAccount](#sendaccount-automodengineslackgo16) `:16`

- 🔗 [SendRecord](#sendrecord-automodengineslackgo25) `:25`

- 🔗 [sendSlackMsg](#sendslackmsg-automodengineslackgo43) `:43`

- 🔗 [slackBody](#slackbody-automodengineslackgo71) `:71`


</details>


[function] name: SendAccount file: automod/engine/slack.go:16 returns_error: нет description: —


### SendAccount (automod/engine/slack.go:16)


SendAccount is a method that performs operations based on the provided parameters and returns (ctx context.Context, service string, c *AccountContext).


```go
func (n *SlackNotifier) SendAccount((ctx context.Context, service string, c *AccountContext)) (ctx context.Context, service string, c *AccountContext)
```


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


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


**Тип ответа:** service


```json
{
  "LexMethod": "string"
}
```


*Определено в:* `atproto/auth/jwt.go`


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


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


📍 *Расположение:* `automod/engine/slack.go:16`



---


[function] name: SendRecord file: automod/engine/slack.go:25 returns_error: нет description: —


### SendRecord (automod/engine/slack.go:25)


SendRecord is a method that performs operations based on the provided parameters and returns (ctx context.Context, service string, c *RecordContext).


```go
func (n *SlackNotifier) SendRecord((ctx context.Context, service string, c *RecordContext)) (ctx context.Context, service string, c *RecordContext)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


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


**Тип ответа:** service


```json
{
  "LexMethod": "string"
}
```


*Определено в:* `atproto/auth/jwt.go`


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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/engine/slack.go:25`



---


[function] name: sendSlackMsg file: automod/engine/slack.go:43 returns_error: нет description: Sends a simple slack message to a channel via "incoming webhook".

The slack incoming webhook must be already configured


### sendSlackMsg (automod/engine/slack.go:43)


Sends a simple slack message to a channel via "incoming webhook".

The slack incoming webhook must be already configured in the slack workplace.


```go
func (n *SlackNotifier) sendSlackMsg((ctx context.Context, msg string)) (ctx context.Context, msg string)
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


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/slack.go:43`



---


[function] name: slackBody file: automod/engine/slack.go:71 returns_error: нет description: —


### slackBody (automod/engine/slack.go:71)


slackBody is a function that performs operations based on the provided parameters and returns (header string, acct AccountMeta, newLabels, rmdLabels, newFlags []string, newReports []ModReport, newTakedown bool).


```go
func slackBody((header string, acct AccountMeta, newLabels, rmdLabels, newFlags []string, newReports []ModReport, newTakedown bool)) (header string, acct AccountMeta, newLabels, rmdLabels, newFlags []string, newReports []ModReport, newTakedown bool)
```


**Тип ответа:** header


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** acct


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountMeta


```json
{
  "Identity": null,
  "Profile": {},
  "Private": null,
  "AccountLabels": [],
  "AccountNegatedLabels": [],
  "AccountFlags": [],
  "FollowersCount": 0,
  "FollowsCount": 0,
  "PostsCount": 0,
  "Takendown": false,
  "Deactivated": false,
  "CreatedAt": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `automod/engine/account_meta.go`


**Тип ответа:** newLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rmdLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newReports


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModReport


```json
{
  "ReasonType": "string",
  "Comment": "string"
}
```


*Определено в:* `automod/engine/report.go`


**Тип ответа:** newTakedown


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/engine/slack.go:71`




## automod/engine/testing.go


📄 Исходный файл: `automod/engine/testing.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [EngineTestFixture](#enginetestfixture-automodenginetestinggo39) `:39`

- 🔗 [ExtractEffects](#extracteffects-automodenginetestinggo74) `:74`

- 🔗 [simpleRule](#simplerule-automodenginetestinggo18) `:18`


</details>


[function] name: EngineTestFixture file: automod/engine/testing.go:39 returns_error: нет description: —


### EngineTestFixture (automod/engine/testing.go:39)


EngineTestFixture is a function that performs operations based on the provided parameters and returns ().


```go
func EngineTestFixture(()) ()
```


📍 *Расположение:* `automod/engine/testing.go:39`



---


[function] name: ExtractEffects file: automod/engine/testing.go:74 returns_error: нет description: Helper to access the private effects field from a context. Intended for use in test code, *not* from rules.


### ExtractEffects (automod/engine/testing.go:74)


Helper to access the private effects field from a context. Intended for use in test code, *not* from rules.


```go
func ExtractEffects((c *BaseContext)) (c *BaseContext)
```


**Тип запроса:** BaseContext


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


**Тип ответа:** BaseContext


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


📍 *Расположение:* `automod/engine/testing.go:74`



---


[function] name: simpleRule file: automod/engine/testing.go:18 returns_error: нет description: —


### simpleRule (automod/engine/testing.go:18)


simpleRule is a function that performs operations based on the provided parameters and returns (c *RecordContext, post *appbsky.FeedPost).


```go
func simpleRule((c *RecordContext, post *appbsky.FeedPost)) (c *RecordContext, post *appbsky.FeedPost)
```


**Тип запроса:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


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


**Тип ответа:** RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


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


📍 *Расположение:* `automod/engine/testing.go:18`




## automod/engine/util.go


📄 Исходный файл: `automod/engine/util.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [cidFromCdnUrl](#cidfromcdnurl-automodengineutilgo21) `:21`

- 🔗 [dedupeStrings](#dedupestrings-automodengineutilgo8) `:8`


</details>


[function] name: cidFromCdnUrl file: automod/engine/util.go:21 returns_error: нет description: get the cid from a bluesky cdn url


### cidFromCdnUrl (automod/engine/util.go:21)


get the cid from a bluesky cdn url


```go
func cidFromCdnUrl((str *string)) (str *string)
```


**Тип ответа:** str


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


📍 *Расположение:* `automod/engine/util.go:21`



---


[function] name: dedupeStrings file: automod/engine/util.go:8 returns_error: нет description: —


### dedupeStrings (automod/engine/util.go:8)


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


📍 *Расположение:* `automod/engine/util.go:8`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_countstore.md)

- [Следующая директория](automod_flagstore.md)


---

