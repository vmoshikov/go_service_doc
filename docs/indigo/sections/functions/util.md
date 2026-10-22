---
title: "Функции: util"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: util
---


# Функции: util


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](testing.md)

- [Следующая директория](util_cliutil.md)


---


## Меню по файлам


- 📄 [util/cbor.go](#utilcborgo)

- 📄 [util/fakekey.go](#utilfakekeygo)

- 📄 [util/http.go](#utilhttpgo)

- 📄 [util/readrecordbs.go](#utilreadrecordbsgo)

- 📄 [util/uri.go](#utilurigo)


---


## util/cbor.go


📄 Исходный файл: `util/cbor.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CborStore](#cborstore-utilcborgo8) `:8`


</details>


[function] name: CborStore file: util/cbor.go:8 returns_error: нет description: —


### CborStore (util/cbor.go:8)


CborStore is a function that performs operations based on the provided parameters and returns (bs cbor.IpldBlockstore).


```go
func CborStore((bs cbor.IpldBlockstore)) (bs cbor.IpldBlockstore)
```


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


📍 *Расположение:* `util/cbor.go:8`




## util/fakekey.go


📄 Исходный файл: `util/fakekey.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [SignForUser](#signforuser-utilfakekeygo12) `:12`

- 🔗 [VerifyUserSignature](#verifyusersignature-utilfakekeygo8) `:8`


</details>


[function] name: SignForUser file: util/fakekey.go:12 returns_error: да description: —


### SignForUser (util/fakekey.go:12)


SignForUser is a method that performs operations based on the provided parameters and may return an error.


```go
func (km *FakeKeyManager) SignForUser(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/fakekey.go:12`



---


[function] name: VerifyUserSignature file: util/fakekey.go:8 returns_error: нет description: —


### VerifyUserSignature (util/fakekey.go:8)


VerifyUserSignature is a method that performs operations based on the provided parameters and returns (context.Context, string, []byte, []byte).


```go
func (km *FakeKeyManager) VerifyUserSignature((context.Context, string, []byte, []byte)) (context.Context, string, []byte, []byte)
```


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


📍 *Расположение:* `util/fakekey.go:8`




## util/http.go


📄 Исходный файл: `util/http.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Debug](#debug-utilhttpgo31) `:31`

- 🔗 [Error](#error-utilhttpgo19) `:19`

- 🔗 [Info](#info-utilhttpgo27) `:27`

- 🔗 [RobustHTTPClient](#robusthttpclient-utilhttpgo46) `:46`

- 🔗 [TestingHTTPClient](#testinghttpclient-utilhttpgo62) `:62`

- 🔗 [Warn](#warn-utilhttpgo23) `:23`

- 🔗 [XRPCRetryPolicy](#xrpcretrypolicy-utilhttpgo72) `:72`


</details>


[function] name: Debug file: util/http.go:31 returns_error: нет description: —


### Debug (util/http.go:31)


Debug is a method that performs operations based on the provided parameters and returns (msg string, keysAndValues ...interface{}).


```go
func (l LeveledSlog) Debug((msg string, keysAndValues ...interface{})) (msg string, keysAndValues ...interface{})
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** keysAndValues


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/http.go:31`



---


[function] name: Error file: util/http.go:19 returns_error: нет description: re-writes HTTP client ERROR to WARN level (because of retries)


### Error (util/http.go:19)


re-writes HTTP client ERROR to WARN level (because of retries)


```go
func (l LeveledSlog) Error((msg string, keysAndValues ...interface{})) (msg string, keysAndValues ...interface{})
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** keysAndValues


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/http.go:19`



---


[function] name: Info file: util/http.go:27 returns_error: нет description: —


### Info (util/http.go:27)


Info is a method that performs operations based on the provided parameters and returns (msg string, keysAndValues ...interface{}).


```go
func (l LeveledSlog) Info((msg string, keysAndValues ...interface{})) (msg string, keysAndValues ...interface{})
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** keysAndValues


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/http.go:27`



---


[function] name: RobustHTTPClient file: util/http.go:46 returns_error: нет description: Generates an HTTP client with decent general-purpose defaults around
timeouts and retries. The returned client has the s


### RobustHTTPClient (util/http.go:46)


Generates an HTTP client with decent general-purpose defaults around
timeouts and retries. The returned client has the stdlib http.Client
interface, but has Hashicorp retryablehttp logic internally.

This client will retry on connection errors, 5xx status (except 501).
It will log intermediate failures with WARN level. This does not start from
http.DefaultClient.

This should be usable for XRPC clients, and other general inter-service
client needs. CLI tools might want shorter timeouts and fewer retries by
default.


```go
func RobustHTTPClient(()) ()
```


📍 *Расположение:* `util/http.go:46`



---


[function] name: TestingHTTPClient file: util/http.go:62 returns_error: нет description: For use in local integration tests. Short timeouts, no retries, etc


### TestingHTTPClient (util/http.go:62)


For use in local integration tests. Short timeouts, no retries, etc


```go
func TestingHTTPClient(()) ()
```


📍 *Расположение:* `util/http.go:62`



---


[function] name: Warn file: util/http.go:23 returns_error: нет description: —


### Warn (util/http.go:23)


Warn is a method that performs operations based on the provided parameters and returns (msg string, keysAndValues ...interface{}).


```go
func (l LeveledSlog) Warn((msg string, keysAndValues ...interface{})) (msg string, keysAndValues ...interface{})
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** keysAndValues


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/http.go:23`



---


[function] name: XRPCRetryPolicy file: util/http.go:72 returns_error: да description: XRPCRetryPolicy is a custom wrapper around retryablehttp.DefaultRetryPolicy.
It treats `429 Too Many Requests` as non-re


### XRPCRetryPolicy (util/http.go:72)


XRPCRetryPolicy is a custom wrapper around retryablehttp.DefaultRetryPolicy.
It treats `429 Too Many Requests` as non-retryable, so the application can decide
how to deal with rate-limiting.


```go
func XRPCRetryPolicy((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/http.go:72`




## util/readrecordbs.go


📄 Исходный файл: `util/readrecordbs.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [AllKeysChan](#allkeyschan-utilreadrecordbsgo66) `:66`

- 🔗 [DeleteBlock](#deleteblock-utilreadrecordbsgo54) `:54`

- 🔗 [Get](#get-utilreadrecordbsgo39) `:39`

- 🔗 [GetLoggedBlocks](#getloggedblocks-utilreadrecordbsgo27) `:27`

- 🔗 [GetSize](#getsize-utilreadrecordbsgo50) `:50`

- 🔗 [Has](#has-utilreadrecordbsgo35) `:35`

- 🔗 [HashOnRead](#hashonread-utilreadrecordbsgo70) `:70`

- 🔗 [NewLoggingBstore](#newloggingbstore-utilreadrecordbsgo18) `:18`

- 🔗 [Put](#put-utilreadrecordbsgo58) `:58`

- 🔗 [PutMany](#putmany-utilreadrecordbsgo62) `:62`


</details>


[function] name: AllKeysChan file: util/readrecordbs.go:66 returns_error: да description: —


### AllKeysChan (util/readrecordbs.go:66)


AllKeysChan is a method that performs operations based on the provided parameters and may return an error.


```go
func (bs *LoggingBstore) AllKeysChan((<-chan cid.Cid, error)) (<-chan cid.Cid, error)
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


📍 *Расположение:* `util/readrecordbs.go:66`



---


[function] name: DeleteBlock file: util/readrecordbs.go:54 returns_error: нет description: —


### DeleteBlock (util/readrecordbs.go:54)


DeleteBlock is a method that deletes data based on the provided parameters and returns (ctx context.Context, c cid.Cid).


```go
func (bs *LoggingBstore) DeleteBlock((ctx context.Context, c cid.Cid)) (ctx context.Context, c cid.Cid)
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


📍 *Расположение:* `util/readrecordbs.go:54`



---


[function] name: Get file: util/readrecordbs.go:39 returns_error: да description: —


### Get (util/readrecordbs.go:39)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (bs *LoggingBstore) Get((blockformat.Block, error)) (blockformat.Block, error)
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


📍 *Расположение:* `util/readrecordbs.go:39`



---


[function] name: GetLoggedBlocks file: util/readrecordbs.go:27 returns_error: нет description: —


### GetLoggedBlocks (util/readrecordbs.go:27)


GetLoggedBlocks is a method that retrieves data based on the provided parameters and returns ().


```go
func (bs *LoggingBstore) GetLoggedBlocks(()) ()
```


📍 *Расположение:* `util/readrecordbs.go:27`



---


[function] name: GetSize file: util/readrecordbs.go:50 returns_error: да description: —


### GetSize (util/readrecordbs.go:50)


GetSize is a method that retrieves data based on the provided parameters and may return an error.


```go
func (bs *LoggingBstore) GetSize((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/readrecordbs.go:50`



---


[function] name: Has file: util/readrecordbs.go:35 returns_error: да description: —


### Has (util/readrecordbs.go:35)


Has is a method that performs operations based on the provided parameters and may return an error.


```go
func (bs *LoggingBstore) Has((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/readrecordbs.go:35`



---


[function] name: HashOnRead file: util/readrecordbs.go:70 returns_error: нет description: —


### HashOnRead (util/readrecordbs.go:70)


HashOnRead is a method that performs operations based on the provided parameters and returns (enabled bool).


```go
func (bs *LoggingBstore) HashOnRead((enabled bool)) (enabled bool)
```


**Тип ответа:** enabled


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/readrecordbs.go:70`



---


[function] name: NewLoggingBstore file: util/readrecordbs.go:18 returns_error: нет description: —


### NewLoggingBstore (util/readrecordbs.go:18)


NewLoggingBstore is a function that performs operations based on the provided parameters and returns (base blockstore.Blockstore).


```go
func NewLoggingBstore((base blockstore.Blockstore)) (base blockstore.Blockstore)
```


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** blockstore.Blockstore


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `util/readrecordbs.go:18`



---


[function] name: Put file: util/readrecordbs.go:58 returns_error: нет description: —


### Put (util/readrecordbs.go:58)


Put is a method that performs operations based on the provided parameters and returns (context.Context, blockformat.Block).


```go
func (bs *LoggingBstore) Put((context.Context, blockformat.Block)) (context.Context, blockformat.Block)
```


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


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `util/readrecordbs.go:58`



---


[function] name: PutMany file: util/readrecordbs.go:62 returns_error: нет description: —


### PutMany (util/readrecordbs.go:62)


PutMany is a method that performs operations based on the provided parameters and returns (context.Context, []blockformat.Block).


```go
func (bs *LoggingBstore) PutMany((context.Context, []blockformat.Block)) (context.Context, []blockformat.Block)
```


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


**Тип ответа:** blockformat.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `util/readrecordbs.go:62`




## util/uri.go


📄 Исходный файл: `util/uri.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ParseAtUri](#parseaturi-utilurigo14) `:14`


</details>


[function] name: ParseAtUri file: util/uri.go:14 returns_error: да description: —


### ParseAtUri (util/uri.go:14)


ParseAtUri is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseAtUri((*ParsedUri, error)) (*ParsedUri, error)
```


**Тип запроса:** ParsedUri


```json
{
  "Did": "string",
  "Collection": "string",
  "Rkey": "string"
}
```


*Определено в:* `util/uri.go`


**Тип ответа:** ParsedUri


```json
{
  "Did": "string",
  "Collection": "string",
  "Rkey": "string"
}
```


*Определено в:* `util/uri.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ParsedUri`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/uri.go:14`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](testing.md)

- [Следующая директория](util_cliutil.md)


---

