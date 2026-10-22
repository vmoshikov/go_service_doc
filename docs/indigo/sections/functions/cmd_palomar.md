---
title: "Функции: cmd/palomar"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/palomar
---


# Функции: cmd/palomar


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_netsync.md)

- [Следующая директория](cmd_rainbow.md)


---


## Меню по файлам


- 📄 [cmd/palomar/main.go](#cmdpalomarmaingo)


---


## cmd/palomar/main.go


📄 Исходный файл: `cmd/palomar/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [createEsClient](#createesclient-cmdpalomarmaingo467) `:467`

- 🔗 [main](#main-cmdpalomarmaingo33) `:33`

- 🔗 [printHits](#printhits-cmdpalomarmaingo383) `:383`

- 🔗 [run](#run-cmdpalomarmaingo40) `:40`


</details>


[function] name: createEsClient file: cmd/palomar/main.go:467 returns_error: да description: —


### createEsClient (cmd/palomar/main.go:467)


createEsClient is a function that performs operations based on the provided parameters and may return an error.


```go
func createEsClient((*es.Client, error)) (*es.Client, error)
```


**Тип запроса:** es.Client


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


**Тип ответа:** es.Client


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


*Типы возврата:* `*es.Client`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/palomar/main.go:467`



---


[function] name: main file: cmd/palomar/main.go:33 returns_error: нет description: —


### main (cmd/palomar/main.go:33)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/palomar/main.go:33`



---


[function] name: printHits file: cmd/palomar/main.go:383 returns_error: нет description: —


### printHits (cmd/palomar/main.go:383)


printHits is a function that performs operations based on the provided parameters and returns (resp *search.EsSearchResponse).


```go
func printHits((resp *search.EsSearchResponse)) (resp *search.EsSearchResponse)
```


**Тип запроса:** search.EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


**Тип ответа:** resp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** search.EsSearchResponse


```json
{
  "Took": 0,
  "TimedOut": false,
  "Hits": {}
}
```


*Определено в:* `search/query.go`


📍 *Расположение:* `cmd/palomar/main.go:383`



---


[function] name: run file: cmd/palomar/main.go:40 returns_error: нет description: —


### run (cmd/palomar/main.go:40)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/palomar/main.go:40`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_netsync.md)

- [Следующая директория](cmd_rainbow.md)


---

