---
title: "Функции: automod/flagstore"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/flagstore
---


# Функции: automod/flagstore


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_engine.md)

- [Следующая директория](automod_helpers.md)


---


## Меню по файлам


- 📄 [automod/flagstore/flagstore_mem.go](#automodflagstoreflagstore_memgo)

- 📄 [automod/flagstore/flagstore_redis.go](#automodflagstoreflagstore_redisgo)

- 📄 [automod/flagstore/util.go](#automodflagstoreutilgo)


---


## automod/flagstore/flagstore_mem.go


📄 Исходный файл: `automod/flagstore/flagstore_mem.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Add](#add-automodflagstoreflagstore_memgo25) `:25`

- 🔗 [Get](#get-automodflagstoreflagstore_memgo17) `:17`

- 🔗 [NewMemFlagStore](#newmemflagstore-automodflagstoreflagstore_memgo11) `:11`

- 🔗 [Remove](#remove-automodflagstoreflagstore_memgo37) `:37`


</details>


[function] name: Add file: automod/flagstore/flagstore_mem.go:25 returns_error: нет description: —


### Add (automod/flagstore/flagstore_mem.go:25)


Add is a method that creates new data based on the provided parameters and returns (ctx context.Context, key string, flags []string).


```go
func (s MemFlagStore) Add((ctx context.Context, key string, flags []string)) (ctx context.Context, key string, flags []string)
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


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/flagstore/flagstore_mem.go:25`



---


[function] name: Get file: automod/flagstore/flagstore_mem.go:17 returns_error: да description: —


### Get (automod/flagstore/flagstore_mem.go:17)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s MemFlagStore) Get(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/flagstore/flagstore_mem.go:17`



---


[function] name: NewMemFlagStore file: automod/flagstore/flagstore_mem.go:11 returns_error: нет description: —


### NewMemFlagStore (automod/flagstore/flagstore_mem.go:11)


NewMemFlagStore is a function that performs operations based on the provided parameters and returns ().


```go
func NewMemFlagStore(()) ()
```


📍 *Расположение:* `automod/flagstore/flagstore_mem.go:11`



---


[function] name: Remove file: automod/flagstore/flagstore_mem.go:37 returns_error: нет description: does not error if flags not in set


### Remove (automod/flagstore/flagstore_mem.go:37)


does not error if flags not in set


```go
func (s MemFlagStore) Remove((ctx context.Context, key string, flags []string)) (ctx context.Context, key string, flags []string)
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


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/flagstore/flagstore_mem.go:37`




## automod/flagstore/flagstore_redis.go


📄 Исходный файл: `automod/flagstore/flagstore_redis.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Add](#add-automodflagstoreflagstore_redisgo44) `:44`

- 🔗 [Get](#get-automodflagstoreflagstore_redisgo33) `:33`

- 🔗 [NewRedisFlagStore](#newredisflagstore-automodflagstoreflagstore_redisgo15) `:15`

- 🔗 [Remove](#remove-automodflagstoreflagstore_redisgo56) `:56`


</details>


[function] name: Add file: automod/flagstore/flagstore_redis.go:44 returns_error: нет description: —


### Add (automod/flagstore/flagstore_redis.go:44)


Add is a method that creates new data based on the provided parameters and returns (ctx context.Context, key string, flags []string).


```go
func (s *RedisFlagStore) Add((ctx context.Context, key string, flags []string)) (ctx context.Context, key string, flags []string)
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


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/flagstore/flagstore_redis.go:44`



---


[function] name: Get file: automod/flagstore/flagstore_redis.go:33 returns_error: да description: —


### Get (automod/flagstore/flagstore_redis.go:33)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *RedisFlagStore) Get(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/flagstore/flagstore_redis.go:33`



---


[function] name: NewRedisFlagStore file: automod/flagstore/flagstore_redis.go:15 returns_error: да description: —


### NewRedisFlagStore (automod/flagstore/flagstore_redis.go:15)


NewRedisFlagStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewRedisFlagStore((*RedisFlagStore, error)) (*RedisFlagStore, error)
```


**Тип запроса:** RedisFlagStore


```json
{
  "Client": null
}
```


*Определено в:* `automod/flagstore/flagstore_redis.go`


**Тип ответа:** RedisFlagStore


```json
{
  "Client": null
}
```


*Определено в:* `automod/flagstore/flagstore_redis.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RedisFlagStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/flagstore/flagstore_redis.go:15`



---


[function] name: Remove file: automod/flagstore/flagstore_redis.go:56 returns_error: нет description: —


### Remove (automod/flagstore/flagstore_redis.go:56)


Remove is a method that deletes data based on the provided parameters and returns (ctx context.Context, key string, flags []string).


```go
func (s *RedisFlagStore) Remove((ctx context.Context, key string, flags []string)) (ctx context.Context, key string, flags []string)
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


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/flagstore/flagstore_redis.go:56`




## automod/flagstore/util.go


📄 Исходный файл: `automod/flagstore/util.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [dedupeStrings](#dedupestrings-automodflagstoreutilgo3) `:3`


</details>


[function] name: dedupeStrings file: automod/flagstore/util.go:3 returns_error: нет description: —


### dedupeStrings (automod/flagstore/util.go:3)


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


📍 *Расположение:* `automod/flagstore/util.go:3`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_engine.md)

- [Следующая директория](automod_helpers.md)


---

