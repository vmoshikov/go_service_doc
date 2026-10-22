---
title: "Функции: util/cliutil"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: util/cliutil
---


# Функции: util/cliutil


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util.md)

- [Следующая директория](util_labels.md)


---


## Меню по файлам


- 📄 [util/cliutil/key.go](#utilcliutilkeygo)

- 📄 [util/cliutil/util.go](#utilcliutilutilgo)


---


## util/cliutil/key.go


📄 Исходный файл: `util/cliutil/key.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GenerateKeyToFile](#generatekeytofile-utilcliutilkeygo57) `:57`

- 🔗 [LoadKeyFromFile](#loadkeyfromfile-utilcliutilkeygo21) `:21`


</details>


[function] name: GenerateKeyToFile file: util/cliutil/key.go:57 returns_error: нет description: Generates a P-256 secret key and saves it to disk as JWK.

Deprecated: use the indigo atcrypto package and multikey stri


### GenerateKeyToFile (util/cliutil/key.go:57)


Generates a P-256 secret key and saves it to disk as JWK.

Deprecated: use the indigo atcrypto package and multikey string serialization instead


```go
func GenerateKeyToFile((fname string)) (fname string)
```


**Тип ответа:** fname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/cliutil/key.go:57`



---


[function] name: LoadKeyFromFile file: util/cliutil/key.go:21 returns_error: да description: Loads a secret key from JWK JSON on disk. Only supports P-256 format.

Deprecated: use the indigo atcrypto package and m


### LoadKeyFromFile (util/cliutil/key.go:21)


Loads a secret key from JWK JSON on disk. Only supports P-256 format.

Deprecated: use the indigo atcrypto package and multikey string serialization instead


```go
func LoadKeyFromFile((*atcrypto.PrivateKeyP256, error)) (*atcrypto.PrivateKeyP256, error)
```


**Тип запроса:** atcrypto.PrivateKeyP256


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Тип ответа:** atcrypto.PrivateKeyP256


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*atcrypto.PrivateKeyP256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/cliutil/key.go:21`




## util/cliutil/util.go


📄 Исходный файл: `util/cliutil/util.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GetXrpcClient](#getxrpcclient-utilcliutilutilgo34) `:34`

- 🔗 [NewHttpClient](#newhttpclient-utilcliutilutilgo21) `:21`

- 🔗 [ReadAuth](#readauth-utilcliutilutilgo78) `:78`

- 🔗 [SetupDatabase](#setupdatabase-utilcliutilutilgo98) `:98`

- 🔗 [loadAuthFromEnv](#loadauthfromenv-utilcliutilutilgo52) `:52`


</details>


[function] name: GetXrpcClient file: util/cliutil/util.go:34 returns_error: да description: —


### GetXrpcClient (util/cliutil/util.go:34)


GetXrpcClient is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetXrpcClient((*xrpc.Client, error)) (*xrpc.Client, error)
```


**Тип запроса:** xrpc.Client


```json
{
  "Client": null,
  "Auth": null,
  "AdminToken": "string",
  "Host": "string",
  "UserAgent": "string",
  "Headers": {}
}
```


*Определено в:* `xrpc/xrpc.go`


**Тип ответа:** xrpc.Client


```json
{
  "Client": null,
  "Auth": null,
  "AdminToken": "string",
  "Host": "string",
  "UserAgent": "string",
  "Headers": {}
}
```


*Определено в:* `xrpc/xrpc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*xrpc.Client`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/cliutil/util.go:34`



---


[function] name: NewHttpClient file: util/cliutil/util.go:21 returns_error: нет description: —


### NewHttpClient (util/cliutil/util.go:21)


NewHttpClient is a function that performs operations based on the provided parameters and returns ().


```go
func NewHttpClient(()) ()
```


📍 *Расположение:* `util/cliutil/util.go:21`



---


[function] name: ReadAuth file: util/cliutil/util.go:78 returns_error: да description: —


### ReadAuth (util/cliutil/util.go:78)


ReadAuth is a function that performs operations based on the provided parameters and may return an error.


```go
func ReadAuth((*xrpc.AuthInfo, error)) (*xrpc.AuthInfo, error)
```


**Тип запроса:** xrpc.AuthInfo


```json
{
  "AccessJwt": "string",
  "RefreshJwt": "string",
  "Handle": "string",
  "Did": "string"
}
```


*Определено в:* `xrpc/xrpc.go`


**Тип ответа:** xrpc.AuthInfo


```json
{
  "AccessJwt": "string",
  "RefreshJwt": "string",
  "Handle": "string",
  "Did": "string"
}
```


*Определено в:* `xrpc/xrpc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*xrpc.AuthInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/cliutil/util.go:78`



---


[function] name: SetupDatabase file: util/cliutil/util.go:98 returns_error: да description: Supports both previous "dbtype=" prefixed DSNs, and URI-style database config strings, for both sqlite and postgresql.




### SetupDatabase (util/cliutil/util.go:98)


Supports both previous "dbtype=" prefixed DSNs, and URI-style database config strings, for both sqlite and postgresql.

Examples:
- "sqlite=dir/file.sqlite"
- "sqlite://file.sqlite"
- "postgres=host=localhost user=postgres password=password dbname=pdsdb port=5432 sslmode=disable"
- "postgresql://postgres:password@localhost:5432/pdsdb?sslmode=disable"


```go
func SetupDatabase((*gorm.DB, error)) (*gorm.DB, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*gorm.DB`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/cliutil/util.go:98`



---


[function] name: loadAuthFromEnv file: util/cliutil/util.go:52 returns_error: да description: —


### loadAuthFromEnv (util/cliutil/util.go:52)


loadAuthFromEnv is a function that performs operations based on the provided parameters and may return an error.


```go
func loadAuthFromEnv((*xrpc.AuthInfo, error)) (*xrpc.AuthInfo, error)
```


**Тип запроса:** xrpc.AuthInfo


```json
{
  "AccessJwt": "string",
  "RefreshJwt": "string",
  "Handle": "string",
  "Did": "string"
}
```


*Определено в:* `xrpc/xrpc.go`


**Тип ответа:** xrpc.AuthInfo


```json
{
  "AccessJwt": "string",
  "RefreshJwt": "string",
  "Handle": "string",
  "Did": "string"
}
```


*Определено в:* `xrpc/xrpc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*xrpc.AuthInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/cliutil/util.go:52`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util.md)

- [Следующая директория](util_labels.md)


---

