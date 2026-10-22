---
title: "Функции: cmd/hepa"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/hepa
---


# Функции: cmd/hepa


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_gosky.md)

- [Следующая директория](cmd_lexgen.md)


---


## Меню по файлам


- 📄 [cmd/hepa/main.go](#cmdhepamaingo)

- 📄 [cmd/hepa/otel.go](#cmdhepaotelgo)

- 📄 [cmd/hepa/server.go](#cmdhepaservergo)


---


## cmd/hepa/main.go


📄 Исходный файл: `cmd/hepa/main.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [configDirectory](#configdirectory-cmdhepamaingo208) `:208`

- 🔗 [configEphemeralServer](#configephemeralserver-cmdhepamaingo370) `:370`

- 🔗 [configLogger](#configlogger-cmdhepamaingo231) `:231`

- 🔗 [main](#main-cmdhepamaingo30) `:30`

- 🔗 [run](#run-cmdhepamaingo37) `:37`


</details>


[function] name: configDirectory file: cmd/hepa/main.go:208 returns_error: да description: —


### configDirectory (cmd/hepa/main.go:208)


configDirectory is a function that performs operations based on the provided parameters and may return an error.


```go
func configDirectory((identity.Directory, error)) (identity.Directory, error)
```


**Тип ответа:** identity.Directory


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `identity.Directory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/hepa/main.go:208`



---


[function] name: configEphemeralServer file: cmd/hepa/main.go:370 returns_error: да description: for simple commands, not long-running daemons


### configEphemeralServer (cmd/hepa/main.go:370)


for simple commands, not long-running daemons


```go
func configEphemeralServer((*Server, error)) (*Server, error)
```


**Тип запроса:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Тип ответа:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Server`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/hepa/main.go:370`



---


[function] name: configLogger file: cmd/hepa/main.go:231 returns_error: нет description: —


### configLogger (cmd/hepa/main.go:231)


configLogger is a function that performs operations based on the provided parameters and returns (cmd *cli.Command, writer io.Writer).


```go
func configLogger((cmd *cli.Command, writer io.Writer)) (cmd *cli.Command, writer io.Writer)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/hepa/main.go:231`



---


[function] name: main file: cmd/hepa/main.go:30 returns_error: нет description: —


### main (cmd/hepa/main.go:30)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/hepa/main.go:30`



---


[function] name: run file: cmd/hepa/main.go:37 returns_error: нет description: —


### run (cmd/hepa/main.go:37)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/hepa/main.go:37`




## cmd/hepa/otel.go


📄 Исходный файл: `cmd/hepa/otel.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [configOTEL](#configotel-cmdhepaotelgo26) `:26`


</details>


[function] name: configOTEL file: cmd/hepa/otel.go:26 returns_error: нет description: Enable OTLP HTTP exporter
For relevant environment variables:
https://pkg.go.dev/go.opentelemetry.io/otel/exporters/otlp


### configOTEL (cmd/hepa/otel.go:26)


Enable OTLP HTTP exporter
For relevant environment variables:
https://pkg.go.dev/go.opentelemetry.io/otel/exporters/otlp/otlptrace#readme-environment-variables
At a minimum, you need to set
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
TODO: this should be in cliutil or something


```go
func configOTEL((serviceName string)) (serviceName string)
```


**Тип ответа:** serviceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/hepa/otel.go:26`




## cmd/hepa/server.go


📄 Исходный файл: `cmd/hepa/server.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [NewServer](#newserver-cmdhepaservergo62) `:62`

- 🔗 [RunMetrics](#runmetrics-cmdhepaservergo240) `:240`


</details>


[function] name: NewServer file: cmd/hepa/server.go:62 returns_error: да description: —


### NewServer (cmd/hepa/server.go:62)


NewServer is a function that performs operations based on the provided parameters and may return an error.


```go
func NewServer((*Server, error)) (*Server, error)
```


**Тип запроса:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Тип ответа:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Server`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/hepa/server.go:62`



---


[function] name: RunMetrics file: cmd/hepa/server.go:240 returns_error: нет description: —


### RunMetrics (cmd/hepa/server.go:240)


RunMetrics is a method that performs operations based on the provided parameters and returns (listen string).


```go
func (s *Server) RunMetrics((listen string)) (listen string)
```


**Тип ответа:** listen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/hepa/server.go:240`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_gosky.md)

- [Следующая директория](cmd_lexgen.md)


---

