---
title: "Функции: cmd/fakermaker"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/fakermaker
---


# Функции: cmd/fakermaker


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_collectiondir.md)

- [Следующая директория](cmd_gosky.md)


---


## Меню по файлам


- 📄 [cmd/fakermaker/main.go](#cmdfakermakermaingo)


---


## cmd/fakermaker/main.go


📄 Исходный файл: `cmd/fakermaker/main.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [genAccounts](#genaccounts-cmdfakermakermaingo208) `:208`

- 🔗 [genGraph](#gengraph-cmdfakermakermaingo310) `:310`

- 🔗 [genInteractions](#geninteractions-cmdfakermakermaingo381) `:381`

- 🔗 [genPosts](#genposts-cmdfakermakermaingo345) `:345`

- 🔗 [genProfiles](#genprofiles-cmdfakermakermaingo275) `:275`

- 🔗 [getXrpcClient](#getxrpcclient-cmdfakermakermaingo452) `:452`

- 🔗 [loadAuthFromEnv](#loadauthfromenv-cmdfakermakermaingo470) `:470`

- 🔗 [main](#main-cmdfakermakermaingo27) `:27`

- 🔗 [run](#run-cmdfakermakermaingo31) `:31`

- 🔗 [runBrowsing](#runbrowsing-cmdfakermakermaingo419) `:419`


</details>


[function] name: genAccounts file: cmd/fakermaker/main.go:208 returns_error: нет description: registers fake accounts with PDS, and spits out JSON-lines to stdout with auth info


### genAccounts (cmd/fakermaker/main.go:208)


registers fake accounts with PDS, and spits out JSON-lines to stdout with auth info


```go
func genAccounts((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/fakermaker/main.go:208`



---


[function] name: genGraph file: cmd/fakermaker/main.go:310 returns_error: нет description: —


### genGraph (cmd/fakermaker/main.go:310)


genGraph is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func genGraph((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/fakermaker/main.go:310`



---


[function] name: genInteractions file: cmd/fakermaker/main.go:381 returns_error: нет description: —


### genInteractions (cmd/fakermaker/main.go:381)


genInteractions is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func genInteractions((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/fakermaker/main.go:381`



---


[function] name: genPosts file: cmd/fakermaker/main.go:345 returns_error: нет description: —


### genPosts (cmd/fakermaker/main.go:345)


genPosts is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func genPosts((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/fakermaker/main.go:345`



---


[function] name: genProfiles file: cmd/fakermaker/main.go:275 returns_error: нет description: —


### genProfiles (cmd/fakermaker/main.go:275)


genProfiles is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func genProfiles((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/fakermaker/main.go:275`



---


[function] name: getXrpcClient file: cmd/fakermaker/main.go:452 returns_error: да description: —


### getXrpcClient (cmd/fakermaker/main.go:452)


getXrpcClient is a function that performs operations based on the provided parameters and may return an error.


```go
func getXrpcClient((*xrpc.Client, error)) (*xrpc.Client, error)
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


📍 *Расположение:* `cmd/fakermaker/main.go:452`



---


[function] name: loadAuthFromEnv file: cmd/fakermaker/main.go:470 returns_error: да description: —


### loadAuthFromEnv (cmd/fakermaker/main.go:470)


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


📍 *Расположение:* `cmd/fakermaker/main.go:470`



---


[function] name: main file: cmd/fakermaker/main.go:27 returns_error: нет description: —


### main (cmd/fakermaker/main.go:27)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/fakermaker/main.go:27`



---


[function] name: run file: cmd/fakermaker/main.go:31 returns_error: нет description: —


### run (cmd/fakermaker/main.go:31)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/fakermaker/main.go:31`



---


[function] name: runBrowsing file: cmd/fakermaker/main.go:419 returns_error: нет description: —


### runBrowsing (cmd/fakermaker/main.go:419)


runBrowsing is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runBrowsing((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/fakermaker/main.go:419`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_collectiondir.md)

- [Следующая директория](cmd_gosky.md)


---

