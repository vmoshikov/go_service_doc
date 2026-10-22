---
title: "Функции: util/svcutil"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: util/svcutil
---


# Функции: util/svcutil


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_ssrf.md)

- [Следующая директория](util_tracing.md)


---


## Меню по файлам


- 📄 [util/svcutil/logger.go](#utilsvcutilloggergo)

- 📄 [util/svcutil/metrics_middleware.go](#utilsvcutilmetrics_middlewarego)


---


## util/svcutil/logger.go


📄 Исходный файл: `util/svcutil/logger.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConfigLogger](#configlogger-utilsvcutilloggergo11) `:11`


</details>


[function] name: ConfigLogger file: util/svcutil/logger.go:11 returns_error: нет description: —


### ConfigLogger (util/svcutil/logger.go:11)


ConfigLogger is a function that performs operations based on the provided parameters and returns (cmd *cli.Command, writer io.Writer).


```go
func ConfigLogger((cmd *cli.Command, writer io.Writer)) (cmd *cli.Command, writer io.Writer)
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


📍 *Расположение:* `util/svcutil/logger.go:11`




## util/svcutil/metrics_middleware.go


📄 Исходный файл: `util/svcutil/metrics_middleware.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MetricsMiddleware](#metricsmiddleware-utilsvcutilmetrics_middlewarego38) `:38`

- 🔗 [computeApproximateRequestSize](#computeapproximaterequestsize-utilsvcutilmetrics_middlewarego77) `:77`


</details>


[function] name: MetricsMiddleware file: util/svcutil/metrics_middleware.go:38 returns_error: нет description: MetricsMiddleware defines handler function for metrics middleware


### MetricsMiddleware (util/svcutil/metrics_middleware.go:38)


MetricsMiddleware defines handler function for metrics middleware


```go
func MetricsMiddleware((next echo.HandlerFunc)) (next echo.HandlerFunc)
```


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** echo.HandlerFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/svcutil/metrics_middleware.go:38`



---


[function] name: computeApproximateRequestSize file: util/svcutil/metrics_middleware.go:77 returns_error: нет description: —


### computeApproximateRequestSize (util/svcutil/metrics_middleware.go:77)


computeApproximateRequestSize is a function that performs operations based on the provided parameters and returns (r *http.Request).


```go
func computeApproximateRequestSize((r *http.Request)) (r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `util/svcutil/metrics_middleware.go:77`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_ssrf.md)

- [Следующая директория](util_tracing.md)


---

