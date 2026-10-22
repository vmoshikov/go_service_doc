---
title: "Функции: automod/capture"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/capture
---


# Функции: automod/capture


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_cachestore.md)

- [Следующая директория](automod_consumer.md)


---


## Меню по файлам


- 📄 [automod/capture/capture.go](#automodcapturecapturego)

- 📄 [automod/capture/fetch.go](#automodcapturefetchgo)

- 📄 [automod/capture/testing.go](#automodcapturetestinggo)


---


## automod/capture/capture.go


📄 Исходный файл: `automod/capture/capture.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CaptureRecent](#capturerecent-automodcapturecapturego17) `:17`


</details>


[function] name: CaptureRecent file: automod/capture/capture.go:17 returns_error: да description: —


### CaptureRecent (automod/capture/capture.go:17)


CaptureRecent is a function that performs operations based on the provided parameters and may return an error.


```go
func CaptureRecent((*AccountCapture, error)) (*AccountCapture, error)
```


**Тип запроса:** AccountCapture


```json
{
  "CapturedAt": {},
  "AccountMeta": {},
  "PostRecords": []
}
```


*Определено в:* `automod/capture/capture.go`


**Тип ответа:** AccountCapture


```json
{
  "CapturedAt": {},
  "AccountMeta": {},
  "PostRecords": []
}
```


*Определено в:* `automod/capture/capture.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AccountCapture`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/capture/capture.go:17`




## automod/capture/fetch.go


📄 Исходный файл: `automod/capture/fetch.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [FetchAndProcessRecent](#fetchandprocessrecent-automodcapturefetchgo74) `:74`

- 🔗 [FetchAndProcessRecord](#fetchandprocessrecord-automodcapturefetchgo15) `:15`

- 🔗 [FetchRecent](#fetchrecent-automodcapturefetchgo55) `:55`


</details>


[function] name: FetchAndProcessRecent file: automod/capture/fetch.go:74 returns_error: нет description: —


### FetchAndProcessRecent (automod/capture/fetch.go:74)


FetchAndProcessRecent is a function that retrieves data based on the provided parameters and returns (ctx context.Context, eng *automod.Engine, atid syntax.AtIdentifier, limit int).


```go
func FetchAndProcessRecent((ctx context.Context, eng *automod.Engine, atid syntax.AtIdentifier, limit int)) (ctx context.Context, eng *automod.Engine, atid syntax.AtIdentifier, limit int)
```


**Тип запроса:** automod.Engine


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


**Тип ответа:** automod.Engine


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


**Тип ответа:** atid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.AtIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `automod/capture/fetch.go:74`



---


[function] name: FetchAndProcessRecord file: automod/capture/fetch.go:15 returns_error: нет description: —


### FetchAndProcessRecord (automod/capture/fetch.go:15)


FetchAndProcessRecord is a function that retrieves data based on the provided parameters and returns (ctx context.Context, eng *automod.Engine, aturi syntax.ATURI).


```go
func FetchAndProcessRecord((ctx context.Context, eng *automod.Engine, aturi syntax.ATURI)) (ctx context.Context, eng *automod.Engine, aturi syntax.ATURI)
```


**Тип запроса:** automod.Engine


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


**Тип ответа:** automod.Engine


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


**Тип ответа:** aturi


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.ATURI


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/capture/fetch.go:15`



---


[function] name: FetchRecent file: automod/capture/fetch.go:55 returns_error: да description: —


### FetchRecent (automod/capture/fetch.go:55)


FetchRecent is a function that retrieves data based on the provided parameters and may return an error.


```go
func FetchRecent((*identity.Identity, []*comatproto.RepoListRecords_Record, error)) (*identity.Identity, []*comatproto.RepoListRecords_Record, error)
```


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


**Тип запроса:** comatproto.RepoListRecords_Record


```json
{
  "cid": "string",
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/agnostic/repolistRecords.go`


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


**Тип ответа:** comatproto.RepoListRecords_Record


```json
{
  "cid": "string",
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/agnostic/repolistRecords.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `[]*comatproto.RepoListRecords_Record`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/capture/fetch.go:55`




## automod/capture/testing.go


📄 Исходный файл: `automod/capture/testing.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MustLoadCapture](#mustloadcapture-automodcapturetestinggo16) `:16`

- 🔗 [ProcessCaptureRules](#processcapturerules-automodcapturetestinggo38) `:38`


</details>


[function] name: MustLoadCapture file: automod/capture/testing.go:16 returns_error: нет description: —


### MustLoadCapture (automod/capture/testing.go:16)


MustLoadCapture is a function that performs operations based on the provided parameters and returns (capPath string).


```go
func MustLoadCapture((capPath string)) (capPath string)
```


**Тип ответа:** capPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/capture/testing.go:16`



---


[function] name: ProcessCaptureRules file: automod/capture/testing.go:38 returns_error: нет description: Test helper which processes all the records from a capture. Intentionally exported, for use in other packages.

This met


### ProcessCaptureRules (automod/capture/testing.go:38)


Test helper which processes all the records from a capture. Intentionally exported, for use in other packages.

This method replaces any pre-existing directory on the engine with a mock directory.


```go
func ProcessCaptureRules((eng *automod.Engine, capture AccountCapture)) (eng *automod.Engine, capture AccountCapture)
```


**Тип запроса:** automod.Engine


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


**Тип ответа:** eng


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** automod.Engine


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


**Тип ответа:** capture


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountCapture


```json
{
  "CapturedAt": {},
  "AccountMeta": {},
  "PostRecords": []
}
```


*Определено в:* `automod/capture/capture.go`


📍 *Расположение:* `automod/capture/testing.go:38`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_cachestore.md)

- [Следующая директория](automod_consumer.md)


---

