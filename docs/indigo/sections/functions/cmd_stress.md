---
title: "Функции: cmd/stress"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/stress
---


# Функции: cmd/stress


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_sonar.md)

- [Следующая директория](cmd_tap.md)


---


## Меню по файлам


- 📄 [cmd/stress/main.go](#cmdstressmaingo)


---


## cmd/stress/main.go


📄 Исходный файл: `cmd/stress/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [getXrpcClient](#getxrpcclient-cmdstressmaingo229) `:229`

- 🔗 [loadAuthFromEnv](#loadauthfromenv-cmdstressmaingo247) `:247`

- 🔗 [main](#main-cmdstressmaingo33) `:33`

- 🔗 [run](#run-cmdstressmaingo37) `:37`


</details>


[function] name: getXrpcClient file: cmd/stress/main.go:229 returns_error: да description: —


### getXrpcClient (cmd/stress/main.go:229)


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


📍 *Расположение:* `cmd/stress/main.go:229`



---


[function] name: loadAuthFromEnv file: cmd/stress/main.go:247 returns_error: да description: —


### loadAuthFromEnv (cmd/stress/main.go:247)


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


📍 *Расположение:* `cmd/stress/main.go:247`



---


[function] name: main file: cmd/stress/main.go:33 returns_error: нет description: —


### main (cmd/stress/main.go:33)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/stress/main.go:33`



---


[function] name: run file: cmd/stress/main.go:37 returns_error: нет description: —


### run (cmd/stress/main.go:37)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/stress/main.go:37`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_sonar.md)

- [Следующая директория](cmd_tap.md)


---

