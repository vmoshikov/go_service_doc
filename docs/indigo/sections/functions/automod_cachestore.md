---
title: "Функции: automod/cachestore"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/cachestore
---


# Функции: automod/cachestore


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_syntax.md)

- [Следующая директория](automod_capture.md)


---


## Меню по файлам


- 📄 [automod/cachestore/cachestore_mem.go](#automodcachestorecachestore_memgo)

- 📄 [automod/cachestore/cachestore_redis.go](#automodcachestorecachestore_redisgo)


---


## automod/cachestore/cachestore_mem.go


📄 Исходный файл: `automod/cachestore/cachestore_mem.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Get](#get-automodcachestorecachestore_memgo20) `:20`

- 🔗 [NewMemCacheStore](#newmemcachestore-automodcachestorecachestore_memgo14) `:14`

- 🔗 [Purge](#purge-automodcachestorecachestore_memgo33) `:33`

- 🔗 [Set](#set-automodcachestorecachestore_memgo28) `:28`


</details>


[function] name: Get file: automod/cachestore/cachestore_mem.go:20 returns_error: да description: —


### Get (automod/cachestore/cachestore_mem.go:20)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s MemCacheStore) Get((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/cachestore/cachestore_mem.go:20`



---


[function] name: NewMemCacheStore file: automod/cachestore/cachestore_mem.go:14 returns_error: нет description: —


### NewMemCacheStore (automod/cachestore/cachestore_mem.go:14)


NewMemCacheStore is a function that performs operations based on the provided parameters and returns (capacity int, ttl time.Duration).


```go
func NewMemCacheStore((capacity int, ttl time.Duration)) (capacity int, ttl time.Duration)
```


**Тип ответа:** capacity


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ttl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/cachestore/cachestore_mem.go:14`



---


[function] name: Purge file: automod/cachestore/cachestore_mem.go:33 returns_error: нет description: —


### Purge (automod/cachestore/cachestore_mem.go:33)


Purge is a method that performs operations based on the provided parameters and returns (ctx context.Context, name, key string).


```go
func (s MemCacheStore) Purge((ctx context.Context, name, key string)) (ctx context.Context, name, key string)
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


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/cachestore/cachestore_mem.go:33`



---


[function] name: Set file: automod/cachestore/cachestore_mem.go:28 returns_error: нет description: —


### Set (automod/cachestore/cachestore_mem.go:28)


Set is a method that updates data based on the provided parameters and returns (ctx context.Context, name, key string, val string).


```go
func (s MemCacheStore) Set((ctx context.Context, name, key string, val string)) (ctx context.Context, name, key string, val string)
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


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


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


📍 *Расположение:* `automod/cachestore/cachestore_mem.go:28`




## automod/cachestore/cachestore_redis.go


📄 Исходный файл: `automod/cachestore/cachestore_redis.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Get](#get-automodcachestorecachestore_redisgo44) `:44`

- 🔗 [NewRedisCacheStore](#newrediscachestore-automodcachestorecachestore_redisgo18) `:18`

- 🔗 [Purge](#purge-automodcachestorecachestore_redisgo65) `:65`

- 🔗 [Set](#set-automodcachestorecachestore_redisgo56) `:56`

- 🔗 [redisCacheKey](#rediscachekey-automodcachestorecachestore_redisgo40) `:40`


</details>


[function] name: Get file: automod/cachestore/cachestore_redis.go:44 returns_error: да description: —


### Get (automod/cachestore/cachestore_redis.go:44)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s RedisCacheStore) Get((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/cachestore/cachestore_redis.go:44`



---


[function] name: NewRedisCacheStore file: automod/cachestore/cachestore_redis.go:18 returns_error: да description: —


### NewRedisCacheStore (automod/cachestore/cachestore_redis.go:18)


NewRedisCacheStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewRedisCacheStore((*RedisCacheStore, error)) (*RedisCacheStore, error)
```


**Тип запроса:** RedisCacheStore


```json
{
  "Data": null,
  "TTL": {}
}
```


*Определено в:* `automod/cachestore/cachestore_redis.go`


**Тип ответа:** RedisCacheStore


```json
{
  "Data": null,
  "TTL": {}
}
```


*Определено в:* `automod/cachestore/cachestore_redis.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RedisCacheStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/cachestore/cachestore_redis.go:18`



---


[function] name: Purge file: automod/cachestore/cachestore_redis.go:65 returns_error: нет description: —


### Purge (automod/cachestore/cachestore_redis.go:65)


Purge is a method that performs operations based on the provided parameters and returns (ctx context.Context, name, key string).


```go
func (s RedisCacheStore) Purge((ctx context.Context, name, key string)) (ctx context.Context, name, key string)
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


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/cachestore/cachestore_redis.go:65`



---


[function] name: Set file: automod/cachestore/cachestore_redis.go:56 returns_error: нет description: —


### Set (automod/cachestore/cachestore_redis.go:56)


Set is a method that updates data based on the provided parameters and returns (ctx context.Context, name, key string, val string).


```go
func (s RedisCacheStore) Set((ctx context.Context, name, key string, val string)) (ctx context.Context, name, key string, val string)
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


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


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


📍 *Расположение:* `automod/cachestore/cachestore_redis.go:56`



---


[function] name: redisCacheKey file: automod/cachestore/cachestore_redis.go:40 returns_error: нет description: —


### redisCacheKey (automod/cachestore/cachestore_redis.go:40)


redisCacheKey is a function that performs operations based on the provided parameters and returns (name, key string).


```go
func redisCacheKey((name, key string)) (name, key string)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/cachestore/cachestore_redis.go:40`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_syntax.md)

- [Следующая директория](automod_capture.md)


---

