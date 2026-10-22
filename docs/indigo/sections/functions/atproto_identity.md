---
title: "Функции: atproto/identity"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/identity
---


# Функции: atproto/identity


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_auth.md)

- [Следующая директория](atproto_labeling.md)


---


## Меню по файлам


- 📄 [atproto/identity/apidir/apidir.go](#atprotoidentityapidirapidirgo)

- 📄 [atproto/identity/base_directory.go](#atprotoidentitybase_directorygo)

- 📄 [atproto/identity/cache_directory.go](#atprotoidentitycache_directorygo)

- 📄 [atproto/identity/cmd/atp-id/main.go](#atprotoidentitycmdatp-idmaingo)

- 📄 [atproto/identity/did.go](#atprotoidentitydidgo)

- 📄 [atproto/identity/directory.go](#atprotoidentitydirectorygo)

- 📄 [atproto/identity/handle.go](#atprotoidentityhandlego)

- 📄 [atproto/identity/identity.go](#atprotoidentityidentitygo)

- 📄 [atproto/identity/mock_directory.go](#atprotoidentitymock_directorygo)

- 📄 [atproto/identity/nsid.go](#atprotoidentitynsidgo)

- 📄 [atproto/identity/redisdir/redis_directory.go](#atprotoidentityredisdirredis_directorygo)


---


## atproto/identity/apidir/apidir.go


📄 Исходный файл: `atproto/identity/apidir/apidir.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Lookup](#lookup-atprotoidentityapidirapidirgo174) `:174`

- 🔗 [LookupDID](#lookupdid-atprotoidentityapidirapidirgo204) `:204`

- 🔗 [LookupHandle](#lookuphandle-atprotoidentityapidirapidirgo200) `:200`

- 🔗 [NewAPIDirectory](#newapidirectory-atprotoidentityapidirapidirgo43) `:43`

- 🔗 [Purge](#purge-atprotoidentityapidirapidirgo208) `:208`

- 🔗 [ResolveDID](#resolvedid-atprotoidentityapidirapidirgo143) `:143`

- 🔗 [ResolveDIDRaw](#resolvedidraw-atprotoidentityapidirapidirgo126) `:126`

- 🔗 [ResolveHandle](#resolvehandle-atprotoidentityapidirapidirgo156) `:156`

- 🔗 [apiGet](#apiget-atprotoidentityapidirapidirgo59) `:59`

- 🔗 [apiPost](#apipost-atprotoidentityapidirapidirgo93) `:93`


</details>


[function] name: Lookup file: atproto/identity/apidir/apidir.go:174 returns_error: да description: —


### Lookup (atproto/identity/apidir/apidir.go:174)


Lookup is a method that performs operations based on the provided parameters and may return an error.


```go
func (dir *APIDirectory) Lookup((*identity.Identity, error)) (*identity.Identity, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:174`



---


[function] name: LookupDID file: atproto/identity/apidir/apidir.go:204 returns_error: да description: —


### LookupDID (atproto/identity/apidir/apidir.go:204)


LookupDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (dir *APIDirectory) LookupDID((*identity.Identity, error)) (*identity.Identity, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:204`



---


[function] name: LookupHandle file: atproto/identity/apidir/apidir.go:200 returns_error: да description: —


### LookupHandle (atproto/identity/apidir/apidir.go:200)


LookupHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (dir *APIDirectory) LookupHandle((*identity.Identity, error)) (*identity.Identity, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:200`



---


[function] name: NewAPIDirectory file: atproto/identity/apidir/apidir.go:43 returns_error: нет description: —


### NewAPIDirectory (atproto/identity/apidir/apidir.go:43)


NewAPIDirectory is a function that performs operations based on the provided parameters and returns (host string).


```go
func NewAPIDirectory((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


📍 *Расположение:* `atproto/identity/apidir/apidir.go:43`



---


[function] name: Purge file: atproto/identity/apidir/apidir.go:208 returns_error: нет description: —


### Purge (atproto/identity/apidir/apidir.go:208)


Purge is a method that performs operations based on the provided parameters and returns (ctx context.Context, atid syntax.AtIdentifier).


```go
func (dir *APIDirectory) Purge((ctx context.Context, atid syntax.AtIdentifier)) (ctx context.Context, atid syntax.AtIdentifier)
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


**Тип ответа:** atid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.AtIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/identity/apidir/apidir.go:208`



---


[function] name: ResolveDID file: atproto/identity/apidir/apidir.go:143 returns_error: да description: —


### ResolveDID (atproto/identity/apidir/apidir.go:143)


ResolveDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (dir *APIDirectory) ResolveDID((*identity.DIDDocument, error)) (*identity.DIDDocument, error)
```


**Тип запроса:** identity.DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Тип ответа:** identity.DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.DIDDocument`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:143`



---


[function] name: ResolveDIDRaw file: atproto/identity/apidir/apidir.go:126 returns_error: да description: —


### ResolveDIDRaw (atproto/identity/apidir/apidir.go:126)


ResolveDIDRaw is a method that performs operations based on the provided parameters and may return an error.


```go
func (dir *APIDirectory) ResolveDIDRaw((json.RawMessage, error)) (json.RawMessage, error)
```


**Тип ответа:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `json.RawMessage`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:126`



---


[function] name: ResolveHandle file: atproto/identity/apidir/apidir.go:156 returns_error: да description: —


### ResolveHandle (atproto/identity/apidir/apidir.go:156)


ResolveHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (dir *APIDirectory) ResolveHandle((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:156`



---


[function] name: apiGet file: atproto/identity/apidir/apidir.go:59 returns_error: да description: body: struct pointer which can be `json.Unmarshal()`


### apiGet (atproto/identity/apidir/apidir.go:59)


body: struct pointer which can be `json.Unmarshal()`


```go
func (dir *APIDirectory) apiGet((ctx context.Context, u string, body any, errFail error, errNotFound error)) (ctx context.Context, u string, body any, errFail error, errNotFound error)
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


**Тип ответа:** u


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** body


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errFail


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errNotFound


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `u string`, `body any`, `errFail error`, `errNotFound error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:59`



---


[function] name: apiPost file: atproto/identity/apidir/apidir.go:93 returns_error: да description: body: struct pointer which can be `json.Unmarshal()`


### apiPost (atproto/identity/apidir/apidir.go:93)


body: struct pointer which can be `json.Unmarshal()`


```go
func (dir *APIDirectory) apiPost((ctx context.Context, u string, reqBody []byte, body any, errFail error, errNotFound error)) (ctx context.Context, u string, reqBody []byte, body any, errFail error, errNotFound error)
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


**Тип ответа:** u


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** reqBody


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** body


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errFail


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errNotFound


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `u string`, `reqBody []byte`, `body any`, `errFail error`, `errNotFound error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/apidir/apidir.go:93`




## atproto/identity/base_directory.go


📄 Исходный файл: `atproto/identity/base_directory.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Lookup](#lookup-atprotoidentitybase_directorygo101) `:101`

- 🔗 [LookupDID](#lookupdid-atprotoidentitybase_directorygo67) `:67`

- 🔗 [LookupHandle](#lookuphandle-atprotoidentitybase_directorygo43) `:43`

- 🔗 [Purge](#purge-atprotoidentitybase_directorygo113) `:113`


</details>


[function] name: Lookup file: atproto/identity/base_directory.go:101 returns_error: да description: —


### Lookup (atproto/identity/base_directory.go:101)


Lookup is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) Lookup((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/base_directory.go:101`



---


[function] name: LookupDID file: atproto/identity/base_directory.go:67 returns_error: да description: —


### LookupDID (atproto/identity/base_directory.go:67)


LookupDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) LookupDID((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/base_directory.go:67`



---


[function] name: LookupHandle file: atproto/identity/base_directory.go:43 returns_error: да description: —


### LookupHandle (atproto/identity/base_directory.go:43)


LookupHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) LookupHandle((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/base_directory.go:43`



---


[function] name: Purge file: atproto/identity/base_directory.go:113 returns_error: нет description: —


### Purge (atproto/identity/base_directory.go:113)


Purge is a method that performs operations based on the provided parameters and returns (ctx context.Context, atid syntax.AtIdentifier).


```go
func (d *BaseDirectory) Purge((ctx context.Context, atid syntax.AtIdentifier)) (ctx context.Context, atid syntax.AtIdentifier)
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


**Тип ответа:** atid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.AtIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/identity/base_directory.go:113`




## atproto/identity/cache_directory.go


📄 Исходный файл: `atproto/identity/cache_directory.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Lookup](#lookup-atprotoidentitycache_directorygo262) `:262`

- 🔗 [LookupDID](#lookupdid-atprotoidentitycache_directorygo177) `:177`

- 🔗 [LookupDIDWithCacheState](#lookupdidwithcachestate-atprotoidentitycache_directorygo182) `:182`

- 🔗 [LookupHandle](#lookuphandle-atprotoidentitycache_directorygo235) `:235`

- 🔗 [LookupHandleWithCacheState](#lookuphandlewithcachestate-atprotoidentitycache_directorygo240) `:240`

- 🔗 [NewCacheDirectory](#newcachedirectory-atprotoidentitycache_directorygo40) `:40`

- 🔗 [Purge](#purge-atprotoidentitycache_directorygo274) `:274`

- 🔗 [ResolveHandle](#resolvehandle-atprotoidentitycache_directorygo95) `:95`

- 🔗 [isHandleStale](#ishandlestale-atprotoidentitycache_directorygo50) `:50`

- 🔗 [isIdentityStale](#isidentitystale-atprotoidentitycache_directorygo57) `:57`

- 🔗 [updateDID](#updatedid-atprotoidentitycache_directorygo152) `:152`

- 🔗 [updateHandle](#updatehandle-atprotoidentitycache_directorygo67) `:67`


</details>


[function] name: Lookup file: atproto/identity/cache_directory.go:262 returns_error: да description: —


### Lookup (atproto/identity/cache_directory.go:262)


Lookup is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *CacheDirectory) Lookup((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/cache_directory.go:262`



---


[function] name: LookupDID file: atproto/identity/cache_directory.go:177 returns_error: да description: —


### LookupDID (atproto/identity/cache_directory.go:177)


LookupDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *CacheDirectory) LookupDID((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/cache_directory.go:177`



---


[function] name: LookupDIDWithCacheState file: atproto/identity/cache_directory.go:182 returns_error: да description: —


### LookupDIDWithCacheState (atproto/identity/cache_directory.go:182)


LookupDIDWithCacheState is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *CacheDirectory) LookupDIDWithCacheState((*Identity, bool, error)) (*Identity, bool, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/cache_directory.go:182`



---


[function] name: LookupHandle file: atproto/identity/cache_directory.go:235 returns_error: да description: —


### LookupHandle (atproto/identity/cache_directory.go:235)


LookupHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *CacheDirectory) LookupHandle((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/cache_directory.go:235`



---


[function] name: LookupHandleWithCacheState file: atproto/identity/cache_directory.go:240 returns_error: да description: —


### LookupHandleWithCacheState (atproto/identity/cache_directory.go:240)


LookupHandleWithCacheState is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *CacheDirectory) LookupHandleWithCacheState((*Identity, bool, error)) (*Identity, bool, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/cache_directory.go:240`



---


[function] name: NewCacheDirectory file: atproto/identity/cache_directory.go:40 returns_error: нет description: Capacity of zero means unlimited size. Similarly, ttl of zero means unlimited duration.


### NewCacheDirectory (atproto/identity/cache_directory.go:40)


Capacity of zero means unlimited size. Similarly, ttl of zero means unlimited duration.


```go
func NewCacheDirectory((inner Directory, capacity int, hitTTL, errTTL, invalidHandleTTL time.Duration)) (inner Directory, capacity int, hitTTL, errTTL, invalidHandleTTL time.Duration)
```


**Тип ответа:** inner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Directory


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


**Тип ответа:** capacity


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hitTTL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errTTL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** invalidHandleTTL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/identity/cache_directory.go:40`



---


[function] name: Purge file: atproto/identity/cache_directory.go:274 returns_error: нет description: —


### Purge (atproto/identity/cache_directory.go:274)


Purge is a method that performs operations based on the provided parameters and returns (ctx context.Context, atid syntax.AtIdentifier).


```go
func (d *CacheDirectory) Purge((ctx context.Context, atid syntax.AtIdentifier)) (ctx context.Context, atid syntax.AtIdentifier)
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


**Тип ответа:** atid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.AtIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/identity/cache_directory.go:274`



---


[function] name: ResolveHandle file: atproto/identity/cache_directory.go:95 returns_error: да description: —


### ResolveHandle (atproto/identity/cache_directory.go:95)


ResolveHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *CacheDirectory) ResolveHandle((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/cache_directory.go:95`



---


[function] name: isHandleStale file: atproto/identity/cache_directory.go:50 returns_error: нет description: —


### isHandleStale (atproto/identity/cache_directory.go:50)


isHandleStale is a method that performs operations based on the provided parameters and returns (e *handleEntry).


```go
func (d *CacheDirectory) isHandleStale((e *handleEntry)) (e *handleEntry)
```


**Тип запроса:** handleEntry


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** handleEntry


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


📍 *Расположение:* `atproto/identity/cache_directory.go:50`



---


[function] name: isIdentityStale file: atproto/identity/cache_directory.go:57 returns_error: нет description: —


### isIdentityStale (atproto/identity/cache_directory.go:57)


isIdentityStale is a method that performs operations based on the provided parameters and returns (e *identityEntry).


```go
func (d *CacheDirectory) isIdentityStale((e *identityEntry)) (e *identityEntry)
```


**Тип запроса:** identityEntry


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** identityEntry


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


📍 *Расположение:* `atproto/identity/cache_directory.go:57`



---


[function] name: updateDID file: atproto/identity/cache_directory.go:152 returns_error: нет description: —


### updateDID (atproto/identity/cache_directory.go:152)


updateDID is a method that performs operations based on the provided parameters and returns (ctx context.Context, did syntax.DID).


```go
func (d *CacheDirectory) updateDID((ctx context.Context, did syntax.DID)) (ctx context.Context, did syntax.DID)
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


📍 *Расположение:* `atproto/identity/cache_directory.go:152`



---


[function] name: updateHandle file: atproto/identity/cache_directory.go:67 returns_error: нет description: —


### updateHandle (atproto/identity/cache_directory.go:67)


updateHandle is a method that performs operations based on the provided parameters and returns (ctx context.Context, h syntax.Handle).


```go
func (d *CacheDirectory) updateHandle((ctx context.Context, h syntax.Handle)) (ctx context.Context, h syntax.Handle)
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


**Тип ответа:** h


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** syntax.Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


📍 *Расположение:* `atproto/identity/cache_directory.go:67`




## atproto/identity/cmd/atp-id/main.go


📄 Исходный файл: `atproto/identity/cmd/atp-id/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [main](#main-atprotoidentitycmdatp-idmaingo16) `:16`

- 🔗 [runLookup](#runlookup-atprotoidentitycmdatp-idmaingo49) `:49`

- 🔗 [runResolveDID](#runresolvedid-atprotoidentitycmdatp-idmaingo91) `:91`

- 🔗 [runResolveHandle](#runresolvehandle-atprotoidentitycmdatp-idmaingo70) `:70`


</details>


[function] name: main file: atproto/identity/cmd/atp-id/main.go:16 returns_error: нет description: —


### main (atproto/identity/cmd/atp-id/main.go:16)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `atproto/identity/cmd/atp-id/main.go:16`



---


[function] name: runLookup file: atproto/identity/cmd/atp-id/main.go:49 returns_error: нет description: —


### runLookup (atproto/identity/cmd/atp-id/main.go:49)


runLookup is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runLookup((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/identity/cmd/atp-id/main.go:49`



---


[function] name: runResolveDID file: atproto/identity/cmd/atp-id/main.go:91 returns_error: нет description: —


### runResolveDID (atproto/identity/cmd/atp-id/main.go:91)


runResolveDID is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runResolveDID((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/identity/cmd/atp-id/main.go:91`



---


[function] name: runResolveHandle file: atproto/identity/cmd/atp-id/main.go:70 returns_error: нет description: —


### runResolveHandle (atproto/identity/cmd/atp-id/main.go:70)


runResolveHandle is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runResolveHandle((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/identity/cmd/atp-id/main.go:70`




## atproto/identity/did.go


📄 Исходный файл: `atproto/identity/did.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [ResolveDID](#resolvedid-atprotoidentitydidgo22) `:22`

- 🔗 [ResolveDIDRaw](#resolvedidraw-atprotoidentitydidgo41) `:41`

- 🔗 [resolveDIDBytes](#resolvedidbytes-atprotoidentitydidgo59) `:59`

- 🔗 [resolveDIDPLC](#resolvedidplc-atprotoidentitydidgo130) `:130`

- 🔗 [resolveDIDWeb](#resolvedidweb-atprotoidentitydidgo76) `:76`


</details>


[function] name: ResolveDID file: atproto/identity/did.go:22 returns_error: да description: Resolves a DID to a parsed `DIDDocument` struct.

This method does not bi-directionally verify handles. Most atproto-spe


### ResolveDID (atproto/identity/did.go:22)


Resolves a DID to a parsed `DIDDocument` struct.

This method does not bi-directionally verify handles. Most atproto-specific code should use the `identity.Directory` interface ("Lookup" methods), which implement that check by default, and provide more ergonomic helpers for working with atproto-relevant information in DID documents.

Note that the `DIDDocument` might not include all the information in the original document. Use `ResolveDIDRaw()` to get the full original JSON.


```go
func (d *BaseDirectory) ResolveDID((*DIDDocument, error)) (*DIDDocument, error)
```


**Тип запроса:** DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Тип ответа:** DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DIDDocument`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/did.go:22`



---


[function] name: ResolveDIDRaw file: atproto/identity/did.go:41 returns_error: да description: Low-level method for resolving a DID to a raw JSON document.

This method does not parse the DID document into an atprot


### ResolveDIDRaw (atproto/identity/did.go:41)


Low-level method for resolving a DID to a raw JSON document.

This method does not parse the DID document into an atproto-specific format, and does not bi-directionally verify handles. Most atproto-specific code should use the "Lookup*" methods, which do implement that functionality.


```go
func (d *BaseDirectory) ResolveDIDRaw((json.RawMessage, error)) (json.RawMessage, error)
```


**Тип ответа:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `json.RawMessage`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/did.go:41`



---


[function] name: resolveDIDBytes file: atproto/identity/did.go:59 returns_error: да description: —


### resolveDIDBytes (atproto/identity/did.go:59)


resolveDIDBytes is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) resolveDIDBytes(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/did.go:59`



---


[function] name: resolveDIDPLC file: atproto/identity/did.go:130 returns_error: да description: —


### resolveDIDPLC (atproto/identity/did.go:130)


resolveDIDPLC is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) resolveDIDPLC(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/did.go:130`



---


[function] name: resolveDIDWeb file: atproto/identity/did.go:76 returns_error: да description: —


### resolveDIDWeb (atproto/identity/did.go:76)


resolveDIDWeb is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) resolveDIDWeb(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/did.go:76`




## atproto/identity/directory.go


📄 Исходный файл: `atproto/identity/directory.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DefaultDirectory](#defaultdirectory-atprotoidentitydirectorygo65) `:65`


</details>


[function] name: DefaultDirectory file: atproto/identity/directory.go:65 returns_error: нет description: Returns a reasonable Directory implementation for applications


### DefaultDirectory (atproto/identity/directory.go:65)


Returns a reasonable Directory implementation for applications


```go
func DefaultDirectory(()) ()
```


📍 *Расположение:* `atproto/identity/directory.go:65`




## atproto/identity/handle.go


📄 Исходный файл: `atproto/identity/handle.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [ResolveHandle](#resolvehandle-atprotoidentityhandlego175) `:175`

- 🔗 [ResolveHandleDNS](#resolvehandledns-atprotoidentityhandlego32) `:32`

- 🔗 [ResolveHandleDNSAuthoritative](#resolvehandlednsauthoritative-atprotoidentityhandlego48) `:48`

- 🔗 [ResolveHandleDNSFallback](#resolvehandlednsfallback-atprotoidentityhandlego93) `:93`

- 🔗 [ResolveHandleWellKnown](#resolvehandlewellknown-atprotoidentityhandlego129) `:129`

- 🔗 [parseTXTResp](#parsetxtresp-atprotoidentityhandlego17) `:17`


</details>


[function] name: ResolveHandle file: atproto/identity/handle.go:175 returns_error: да description: —


### ResolveHandle (atproto/identity/handle.go:175)


ResolveHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) ResolveHandle((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/handle.go:175`



---


[function] name: ResolveHandleDNS file: atproto/identity/handle.go:32 returns_error: да description: Does not cross-verify, only does the handle resolution step.


### ResolveHandleDNS (atproto/identity/handle.go:32)


Does not cross-verify, only does the handle resolution step.


```go
func (d *BaseDirectory) ResolveHandleDNS((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/handle.go:32`



---


[function] name: ResolveHandleDNSAuthoritative file: atproto/identity/handle.go:48 returns_error: да description: this is a variant of ResolveHandleDNS which first does an authoritative nameserver lookup, then queries there


### ResolveHandleDNSAuthoritative (atproto/identity/handle.go:48)


this is a variant of ResolveHandleDNS which first does an authoritative nameserver lookup, then queries there


```go
func (d *BaseDirectory) ResolveHandleDNSAuthoritative((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/handle.go:48`



---


[function] name: ResolveHandleDNSFallback file: atproto/identity/handle.go:93 returns_error: да description: variant of ResolveHandleDNS which uses any configured fallback DNS servers


### ResolveHandleDNSFallback (atproto/identity/handle.go:93)


variant of ResolveHandleDNS which uses any configured fallback DNS servers


```go
func (d *BaseDirectory) ResolveHandleDNSFallback((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/handle.go:93`



---


[function] name: ResolveHandleWellKnown file: atproto/identity/handle.go:129 returns_error: да description: —


### ResolveHandleWellKnown (atproto/identity/handle.go:129)


ResolveHandleWellKnown is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *BaseDirectory) ResolveHandleWellKnown((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/handle.go:129`



---


[function] name: parseTXTResp file: atproto/identity/handle.go:17 returns_error: да description: —


### parseTXTResp (atproto/identity/handle.go:17)


parseTXTResp is a function that performs operations based on the provided parameters and may return an error.


```go
func parseTXTResp((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/handle.go:17`




## atproto/identity/identity.go


📄 Исходный файл: `atproto/identity/identity.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [DIDDocument](#diddocument-atprotoidentityidentitygo89) `:89`

- 🔗 [DeclaredHandle](#declaredhandle-atprotoidentityidentitygo198) `:198`

- 🔗 [GetPublicKey](#getpublickey-atprotoidentityidentitygo132) `:132`

- 🔗 [GetServiceEndpoint](#getserviceendpoint-atprotoidentityidentitygo180) `:180`

- 🔗 [PDSEndpoint](#pdsendpoint-atprotoidentityidentitygo171) `:171`

- 🔗 [ParseIdentity](#parseidentity-atprotoidentityidentitygo42) `:42`

- 🔗 [PublicKey](#publickey-atprotoidentityidentitygo123) `:123`


</details>


[function] name: DIDDocument file: atproto/identity/identity.go:89 returns_error: нет description: Helper to generate a DID document based on an identity. Note that there is flexibility around parsing, and this won't ne


### DIDDocument (atproto/identity/identity.go:89)


Helper to generate a DID document based on an identity. Note that there is flexibility around parsing, and this won't necessarily "round-trip" for every valid DID document.


```go
func (ident *Identity) DIDDocument(()) ()
```


📍 *Расположение:* `atproto/identity/identity.go:89`



---


[function] name: DeclaredHandle file: atproto/identity/identity.go:198 returns_error: да description: Returns an atproto handle from the alsoKnownAs URI list for this identifier. Returns an error if there is no handle, or 


### DeclaredHandle (atproto/identity/identity.go:198)


Returns an atproto handle from the alsoKnownAs URI list for this identifier. Returns an error if there is no handle, or if an at:// URI fails to parse as a handle.

Note that this handle is *not* necessarily to be trusted, as it may not have been bi-directionally verified. The 'Handle' field on the 'Identity' should contain either a verified handle, or the special 'handle.invalid' indicator value.


```go
func (i *Identity) DeclaredHandle((syntax.Handle, error)) (syntax.Handle, error)
```


**Тип ответа:** syntax.Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.Handle`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/identity.go:198`



---


[function] name: GetPublicKey file: atproto/identity/identity.go:132 returns_error: да description: Identifies and parses a specified service signing public key out of any keys in this identity's DID document.

Returns [


### GetPublicKey (atproto/identity/identity.go:132)


Identifies and parses a specified service signing public key out of any keys in this identity's DID document.

Returns [ErrKeyNotFound] if there is no such key.

Note that [atcrypto.PublicKey] is an interface, not a concrete type.


```go
func (i *Identity) GetPublicKey((atcrypto.PublicKey, error)) (atcrypto.PublicKey, error)
```


**Тип ответа:** atcrypto.PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `atcrypto.PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/identity.go:132`



---


[function] name: GetServiceEndpoint file: atproto/identity/identity.go:180 returns_error: нет description: Returns the service endpoint URL for specified service ID (the fragment part of identifier, not including the hash symbo


### GetServiceEndpoint (atproto/identity/identity.go:180)


Returns the service endpoint URL for specified service ID (the fragment part of identifier, not including the hash symbol).

The endpoint should be an HTTP URL with method, hostname, and optional port. It may or may not include path segments.

Returns an empty string if the service isn't found, or if the URL fails to parse.


```go
func (i *Identity) GetServiceEndpoint((id string)) (id string)
```


**Тип ответа:** id


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `atproto/identity/identity.go:180`



---


[function] name: PDSEndpoint file: atproto/identity/identity.go:171 returns_error: нет description: The home PDS endpoint for this identity, if one is included in the DID document.

The endpoint should be an HTTP URL wit


### PDSEndpoint (atproto/identity/identity.go:171)


The home PDS endpoint for this identity, if one is included in the DID document.

The endpoint should be an HTTP URL with method, hostname, and optional port. It may or may not include path segments.

Returns an empty string if the service isn't found, or if the URL fails to parse.


```go
func (i *Identity) PDSEndpoint(()) ()
```


📍 *Расположение:* `atproto/identity/identity.go:171`



---


[function] name: ParseIdentity file: atproto/identity/identity.go:42 returns_error: нет description: Extracts the information relevant to atproto from an arbitrary DID document.

Always returns an invalid Handle field; ca


### ParseIdentity (atproto/identity/identity.go:42)


Extracts the information relevant to atproto from an arbitrary DID document.

Always returns an invalid Handle field; calling code should only populate that field if it has been bi-directionally verified.


```go
func ParseIdentity((doc *DIDDocument)) (doc *DIDDocument)
```


**Тип запроса:** DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Тип ответа:** doc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


📍 *Расположение:* `atproto/identity/identity.go:42`



---


[function] name: PublicKey file: atproto/identity/identity.go:123 returns_error: да description: Identifies and parses the atproto repo signing public key, specifically, out of any keys in this identity's DID document


### PublicKey (atproto/identity/identity.go:123)


Identifies and parses the atproto repo signing public key, specifically, out of any keys in this identity's DID document.

Returns [ErrKeyNotFound] if there is no such key.

Note that [atcrypto.PublicKey] is an interface, not a concrete type.


```go
func (i *Identity) PublicKey((atcrypto.PublicKey, error)) (atcrypto.PublicKey, error)
```


**Тип ответа:** atcrypto.PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `atcrypto.PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/identity.go:123`




## atproto/identity/mock_directory.go


📄 Исходный файл: `atproto/identity/mock_directory.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [Insert](#insert-atprotoidentitymock_directorygo29) `:29`

- 🔗 [Lookup](#lookup-atprotoidentitymock_directorygo66) `:66`

- 🔗 [LookupDID](#lookupdid-atprotoidentitymock_directorygo55) `:55`

- 🔗 [LookupHandle](#lookuphandle-atprotoidentitymock_directorygo39) `:39`

- 🔗 [NewMockDirectory](#newmockdirectory-atprotoidentitymock_directorygo22) `:22`

- 🔗 [Purge](#purge-atprotoidentitymock_directorygo117) `:117`

- 🔗 [ResolveDID](#resolvedid-atprotoidentitymock_directorygo93) `:93`

- 🔗 [ResolveDIDRaw](#resolvedidraw-atprotoidentitymock_directorygo105) `:105`

- 🔗 [ResolveHandle](#resolvehandle-atprotoidentitymock_directorygo81) `:81`


</details>


[function] name: Insert file: atproto/identity/mock_directory.go:29 returns_error: нет description: —


### Insert (atproto/identity/mock_directory.go:29)


Insert is a method that performs operations based on the provided parameters and returns (ident Identity).


```go
func (d *MockDirectory) Insert((ident Identity)) (ident Identity)
```


**Тип ответа:** ident


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** Identity


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


📍 *Расположение:* `atproto/identity/mock_directory.go:29`



---


[function] name: Lookup file: atproto/identity/mock_directory.go:66 returns_error: да description: —


### Lookup (atproto/identity/mock_directory.go:66)


Lookup is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *MockDirectory) Lookup((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/mock_directory.go:66`



---


[function] name: LookupDID file: atproto/identity/mock_directory.go:55 returns_error: да description: —


### LookupDID (atproto/identity/mock_directory.go:55)


LookupDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *MockDirectory) LookupDID((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/mock_directory.go:55`



---


[function] name: LookupHandle file: atproto/identity/mock_directory.go:39 returns_error: да description: —


### LookupHandle (atproto/identity/mock_directory.go:39)


LookupHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *MockDirectory) LookupHandle((*Identity, error)) (*Identity, error)
```


**Тип запроса:** Identity


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


**Тип ответа:** Identity


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/mock_directory.go:39`



---


[function] name: NewMockDirectory file: atproto/identity/mock_directory.go:22 returns_error: нет description: —


### NewMockDirectory (atproto/identity/mock_directory.go:22)


NewMockDirectory is a function that performs operations based on the provided parameters and returns ().


```go
func NewMockDirectory(()) ()
```


📍 *Расположение:* `atproto/identity/mock_directory.go:22`



---


[function] name: Purge file: atproto/identity/mock_directory.go:117 returns_error: нет description: —


### Purge (atproto/identity/mock_directory.go:117)


Purge is a method that performs operations based on the provided parameters and returns (ctx context.Context, a syntax.AtIdentifier).


```go
func (d *MockDirectory) Purge((ctx context.Context, a syntax.AtIdentifier)) (ctx context.Context, a syntax.AtIdentifier)
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


**Тип ответа:** a


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** syntax.AtIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/identity/mock_directory.go:117`



---


[function] name: ResolveDID file: atproto/identity/mock_directory.go:93 returns_error: да description: —


### ResolveDID (atproto/identity/mock_directory.go:93)


ResolveDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *MockDirectory) ResolveDID((*DIDDocument, error)) (*DIDDocument, error)
```


**Тип запроса:** DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Тип ответа:** DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DIDDocument`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/mock_directory.go:93`



---


[function] name: ResolveDIDRaw file: atproto/identity/mock_directory.go:105 returns_error: да description: —


### ResolveDIDRaw (atproto/identity/mock_directory.go:105)


ResolveDIDRaw is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *MockDirectory) ResolveDIDRaw((json.RawMessage, error)) (json.RawMessage, error)
```


**Тип ответа:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `json.RawMessage`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/mock_directory.go:105`



---


[function] name: ResolveHandle file: atproto/identity/mock_directory.go:81 returns_error: да description: —


### ResolveHandle (atproto/identity/mock_directory.go:81)


ResolveHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *MockDirectory) ResolveHandle((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/mock_directory.go:81`




## atproto/identity/nsid.go


📄 Исходный файл: `atproto/identity/nsid.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ResolveNSID](#resolvensid-atprotoidentitynsidgo18) `:18`


</details>


[function] name: ResolveNSID file: atproto/identity/nsid.go:18 returns_error: да description: Resolves an NSID to a DID, as used for Lexicon resolution (using "_lexicon" DNS TXT record)


### ResolveNSID (atproto/identity/nsid.go:18)


Resolves an NSID to a DID, as used for Lexicon resolution (using "_lexicon" DNS TXT record)


```go
func (d *BaseDirectory) ResolveNSID((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/nsid.go:18`




## atproto/identity/redisdir/redis_directory.go


📄 Исходный файл: `atproto/identity/redisdir/redis_directory.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Lookup](#lookup-atprotoidentityredisdirredis_directorygo370) `:370`

- 🔗 [LookupDID](#lookupdid-atprotoidentityredisdirredis_directorygo276) `:276`

- 🔗 [LookupDIDWithCacheState](#lookupdidwithcachestate-atprotoidentityredisdirredis_directorygo281) `:281`

- 🔗 [LookupHandle](#lookuphandle-atprotoidentityredisdirredis_directorygo343) `:343`

- 🔗 [LookupHandleWithCacheState](#lookuphandlewithcachestate-atprotoidentityredisdirredis_directorygo348) `:348`

- 🔗 [NewRedisDirectory](#newredisdirectory-atprotoidentityredisdirredis_directorygo58) `:58`

- 🔗 [Purge](#purge-atprotoidentityredisdirredis_directorygo382) `:382`

- 🔗 [ResolveHandle](#resolvehandle-atprotoidentityredisdirredis_directorygo157) `:157`

- 🔗 [isHandleStale](#ishandlestale-atprotoidentityredisdirredis_directorygo87) `:87`

- 🔗 [isIdentityStale](#isidentitystale-atprotoidentityredisdirredis_directorygo94) `:94`

- 🔗 [updateDID](#updatedid-atprotoidentityredisdirredis_directorygo235) `:235`

- 🔗 [updateHandle](#updatehandle-atprotoidentityredisdirredis_directorygo104) `:104`


</details>


[function] name: Lookup file: atproto/identity/redisdir/redis_directory.go:370 returns_error: да description: —


### Lookup (atproto/identity/redisdir/redis_directory.go:370)


Lookup is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisDirectory) Lookup((*identity.Identity, error)) (*identity.Identity, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:370`



---


[function] name: LookupDID file: atproto/identity/redisdir/redis_directory.go:276 returns_error: да description: —


### LookupDID (atproto/identity/redisdir/redis_directory.go:276)


LookupDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisDirectory) LookupDID((*identity.Identity, error)) (*identity.Identity, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:276`



---


[function] name: LookupDIDWithCacheState file: atproto/identity/redisdir/redis_directory.go:281 returns_error: да description: —


### LookupDIDWithCacheState (atproto/identity/redisdir/redis_directory.go:281)


LookupDIDWithCacheState is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisDirectory) LookupDIDWithCacheState((*identity.Identity, bool, error)) (*identity.Identity, bool, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:281`



---


[function] name: LookupHandle file: atproto/identity/redisdir/redis_directory.go:343 returns_error: да description: —


### LookupHandle (atproto/identity/redisdir/redis_directory.go:343)


LookupHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisDirectory) LookupHandle((*identity.Identity, error)) (*identity.Identity, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:343`



---


[function] name: LookupHandleWithCacheState file: atproto/identity/redisdir/redis_directory.go:348 returns_error: да description: —


### LookupHandleWithCacheState (atproto/identity/redisdir/redis_directory.go:348)


LookupHandleWithCacheState is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisDirectory) LookupHandleWithCacheState((*identity.Identity, bool, error)) (*identity.Identity, bool, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.Identity`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:348`



---


[function] name: NewRedisDirectory file: atproto/identity/redisdir/redis_directory.go:58 returns_error: да description: Creates a new caching `identity.Directory` wrapper around an existing directory, using Redis and in-process LRU for cach


### NewRedisDirectory (atproto/identity/redisdir/redis_directory.go:58)


Creates a new caching `identity.Directory` wrapper around an existing directory, using Redis and in-process LRU for caching.

`redisURL` contains all the redis connection config options.
`hitTTL` and `errTTL` define how long successful and errored identity metadata should be cached (respectively). errTTL is expected to be shorted than hitTTL.
`lruSize` is the size of the in-process cache, for each of the handle and identity caches. 10000 is a reasonable default.

NOTE: Errors returned may be inconsistent with the base directory, or between calls. This is because cached errors are serialized/deserialized and that may break equality checks.


```go
func NewRedisDirectory((*RedisDirectory, error)) (*RedisDirectory, error)
```


**Тип запроса:** RedisDirectory


```json
{
  "Inner": {},
  "ErrTTL": {},
  "HitTTL": {},
  "InvalidHandleTTL": {},
  "handleCache": null,
  "identityCache": null,
  "didLookupChans": {},
  "handleLookupChans": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** RedisDirectory


```json
{
  "Inner": {},
  "ErrTTL": {},
  "HitTTL": {},
  "InvalidHandleTTL": {},
  "handleCache": null,
  "identityCache": null,
  "didLookupChans": {},
  "handleLookupChans": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RedisDirectory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:58`



---


[function] name: Purge file: atproto/identity/redisdir/redis_directory.go:382 returns_error: нет description: —


### Purge (atproto/identity/redisdir/redis_directory.go:382)


Purge is a method that performs operations based on the provided parameters and returns (ctx context.Context, a syntax.AtIdentifier).


```go
func (d *RedisDirectory) Purge((ctx context.Context, a syntax.AtIdentifier)) (ctx context.Context, a syntax.AtIdentifier)
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


**Тип ответа:** a


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** syntax.AtIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:382`



---


[function] name: ResolveHandle file: atproto/identity/redisdir/redis_directory.go:157 returns_error: да description: —


### ResolveHandle (atproto/identity/redisdir/redis_directory.go:157)


ResolveHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisDirectory) ResolveHandle((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:157`



---


[function] name: isHandleStale file: atproto/identity/redisdir/redis_directory.go:87 returns_error: нет description: —


### isHandleStale (atproto/identity/redisdir/redis_directory.go:87)


isHandleStale is a method that performs operations based on the provided parameters and returns (e *handleEntry).


```go
func (d *RedisDirectory) isHandleStale((e *handleEntry)) (e *handleEntry)
```


**Тип запроса:** handleEntry


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** handleEntry


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:87`



---


[function] name: isIdentityStale file: atproto/identity/redisdir/redis_directory.go:94 returns_error: нет description: —


### isIdentityStale (atproto/identity/redisdir/redis_directory.go:94)


isIdentityStale is a method that performs operations based on the provided parameters and returns (e *identityEntry).


```go
func (d *RedisDirectory) isIdentityStale((e *identityEntry)) (e *identityEntry)
```


**Тип запроса:** identityEntry


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** identityEntry


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:94`



---


[function] name: updateDID file: atproto/identity/redisdir/redis_directory.go:235 returns_error: нет description: —


### updateDID (atproto/identity/redisdir/redis_directory.go:235)


updateDID is a method that performs operations based on the provided parameters and returns (ctx context.Context, did syntax.DID).


```go
func (d *RedisDirectory) updateDID((ctx context.Context, did syntax.DID)) (ctx context.Context, did syntax.DID)
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


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:235`



---


[function] name: updateHandle file: atproto/identity/redisdir/redis_directory.go:104 returns_error: нет description: —


### updateHandle (atproto/identity/redisdir/redis_directory.go:104)


updateHandle is a method that performs operations based on the provided parameters and returns (ctx context.Context, h syntax.Handle).


```go
func (d *RedisDirectory) updateHandle((ctx context.Context, h syntax.Handle)) (ctx context.Context, h syntax.Handle)
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


**Тип ответа:** h


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** syntax.Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


📍 *Расположение:* `atproto/identity/redisdir/redis_directory.go:104`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_auth.md)

- [Следующая директория](atproto_labeling.md)


---

