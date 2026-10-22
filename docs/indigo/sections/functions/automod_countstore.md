---
title: "Функции: automod/countstore"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/countstore
---


# Функции: automod/countstore


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_consumer.md)

- [Следующая директория](automod_engine.md)


---


## Меню по файлам


- 📄 [automod/countstore/countstore.go](#automodcountstorecountstorego)

- 📄 [automod/countstore/countstore_mem.go](#automodcountstorecountstore_memgo)

- 📄 [automod/countstore/countstore_redis.go](#automodcountstorecountstore_redisgo)


---


## automod/countstore/countstore.go


📄 Исходный файл: `automod/countstore/countstore.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [periodBucket](#periodbucket-automodcountstorecountstorego53) `:53`


</details>


[function] name: periodBucket file: automod/countstore/countstore.go:53 returns_error: нет description: —


### periodBucket (automod/countstore/countstore.go:53)


periodBucket is a function that performs operations based on the provided parameters and returns (name, val, period string).


```go
func periodBucket((name, val, period string)) (name, val, period string)
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


📍 *Расположение:* `automod/countstore/countstore.go:53`




## automod/countstore/countstore_mem.go


📄 Исходный файл: `automod/countstore/countstore_mem.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [GetCount](#getcount-automodcountstorecountstore_memgo26) `:26`

- 🔗 [GetCountDistinct](#getcountdistinct-automodcountstorecountstore_memgo51) `:51`

- 🔗 [Increment](#increment-automodcountstorecountstore_memgo34) `:34`

- 🔗 [IncrementDistinct](#incrementdistinct-automodcountstorecountstore_memgo59) `:59`

- 🔗 [IncrementPeriod](#incrementperiod-automodcountstorecountstore_memgo43) `:43`

- 🔗 [NewMemCountStore](#newmemcountstore-automodcountstorecountstore_memgo19) `:19`


</details>


[function] name: GetCount file: automod/countstore/countstore_mem.go:26 returns_error: да description: —


### GetCount (automod/countstore/countstore_mem.go:26)


GetCount is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s MemCountStore) GetCount((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/countstore/countstore_mem.go:26`



---


[function] name: GetCountDistinct file: automod/countstore/countstore_mem.go:51 returns_error: да description: —


### GetCountDistinct (automod/countstore/countstore_mem.go:51)


GetCountDistinct is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s MemCountStore) GetCountDistinct((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/countstore/countstore_mem.go:51`



---


[function] name: Increment file: automod/countstore/countstore_mem.go:34 returns_error: нет description: —


### Increment (automod/countstore/countstore_mem.go:34)


Increment is a method that performs operations based on the provided parameters and returns (ctx context.Context, name, val string).


```go
func (s MemCountStore) Increment((ctx context.Context, name, val string)) (ctx context.Context, name, val string)
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


📍 *Расположение:* `automod/countstore/countstore_mem.go:34`



---


[function] name: IncrementDistinct file: automod/countstore/countstore_mem.go:59 returns_error: нет description: —


### IncrementDistinct (automod/countstore/countstore_mem.go:59)


IncrementDistinct is a method that performs operations based on the provided parameters and returns (ctx context.Context, name, bucket, val string).


```go
func (s MemCountStore) IncrementDistinct((ctx context.Context, name, bucket, val string)) (ctx context.Context, name, bucket, val string)
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


📍 *Расположение:* `automod/countstore/countstore_mem.go:59`



---


[function] name: IncrementPeriod file: automod/countstore/countstore_mem.go:43 returns_error: нет description: —


### IncrementPeriod (automod/countstore/countstore_mem.go:43)


IncrementPeriod is a method that performs operations based on the provided parameters and returns (ctx context.Context, name, val, period string).


```go
func (s MemCountStore) IncrementPeriod((ctx context.Context, name, val, period string)) (ctx context.Context, name, val, period string)
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


📍 *Расположение:* `automod/countstore/countstore_mem.go:43`



---


[function] name: NewMemCountStore file: automod/countstore/countstore_mem.go:19 returns_error: нет description: —


### NewMemCountStore (automod/countstore/countstore_mem.go:19)


NewMemCountStore is a function that performs operations based on the provided parameters and returns ().


```go
func NewMemCountStore(()) ()
```


📍 *Расположение:* `automod/countstore/countstore_mem.go:19`




## automod/countstore/countstore_redis.go


📄 Исходный файл: `automod/countstore/countstore_redis.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [GetCount](#getcount-automodcountstorecountstore_redisgo35) `:35`

- 🔗 [GetCountDistinct](#getcountdistinct-automodcountstorecountstore_redisgo89) `:89`

- 🔗 [Increment](#increment-automodcountstorecountstore_redisgo46) `:46`

- 🔗 [IncrementDistinct](#incrementdistinct-automodcountstorecountstore_redisgo100) `:100`

- 🔗 [IncrementPeriod](#incrementperiod-automodcountstorecountstore_redisgo70) `:70`

- 🔗 [NewRedisCountStore](#newrediscountstore-automodcountstorecountstore_redisgo17) `:17`


</details>


[function] name: GetCount file: automod/countstore/countstore_redis.go:35 returns_error: да description: —


### GetCount (automod/countstore/countstore_redis.go:35)


GetCount is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *RedisCountStore) GetCount((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/countstore/countstore_redis.go:35`



---


[function] name: GetCountDistinct file: automod/countstore/countstore_redis.go:89 returns_error: да description: —


### GetCountDistinct (automod/countstore/countstore_redis.go:89)


GetCountDistinct is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *RedisCountStore) GetCountDistinct((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/countstore/countstore_redis.go:89`



---


[function] name: Increment file: automod/countstore/countstore_redis.go:46 returns_error: нет description: —


### Increment (automod/countstore/countstore_redis.go:46)


Increment is a method that performs operations based on the provided parameters and returns (ctx context.Context, name, val string).


```go
func (s *RedisCountStore) Increment((ctx context.Context, name, val string)) (ctx context.Context, name, val string)
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


📍 *Расположение:* `automod/countstore/countstore_redis.go:46`



---


[function] name: IncrementDistinct file: automod/countstore/countstore_redis.go:100 returns_error: нет description: —


### IncrementDistinct (automod/countstore/countstore_redis.go:100)


IncrementDistinct is a method that performs operations based on the provided parameters and returns (ctx context.Context, name, bucket, val string).


```go
func (s *RedisCountStore) IncrementDistinct((ctx context.Context, name, bucket, val string)) (ctx context.Context, name, bucket, val string)
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


📍 *Расположение:* `automod/countstore/countstore_redis.go:100`



---


[function] name: IncrementPeriod file: automod/countstore/countstore_redis.go:70 returns_error: нет description: Variant of Increment() which only acts on a single specified time period. The intended us of this variant is to control 


### IncrementPeriod (automod/countstore/countstore_redis.go:70)


Variant of Increment() which only acts on a single specified time period. The intended us of this variant is to control the total number of counters persisted, by using a relatively short time period, for which the counters will expire.


```go
func (s *RedisCountStore) IncrementPeriod((ctx context.Context, name, val, period string)) (ctx context.Context, name, val, period string)
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


📍 *Расположение:* `automod/countstore/countstore_redis.go:70`



---


[function] name: NewRedisCountStore file: automod/countstore/countstore_redis.go:17 returns_error: да description: —


### NewRedisCountStore (automod/countstore/countstore_redis.go:17)


NewRedisCountStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewRedisCountStore((*RedisCountStore, error)) (*RedisCountStore, error)
```


**Тип запроса:** RedisCountStore


```json
{
  "Client": null
}
```


*Определено в:* `automod/countstore/countstore_redis.go`


**Тип ответа:** RedisCountStore


```json
{
  "Client": null
}
```


*Определено в:* `automod/countstore/countstore_redis.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RedisCountStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/countstore/countstore_redis.go:17`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_consumer.md)

- [Следующая директория](automod_engine.md)


---

