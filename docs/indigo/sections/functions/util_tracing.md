---
title: "Функции: util/tracing"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: util/tracing
---


# Функции: util/tracing


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_svcutil.md)

- [Следующая директория](xrpc.md)


---


## Меню по файлам


- 📄 [util/tracing/tracing.go](#utiltracingtracinggo)


---


## util/tracing/tracing.go


📄 Исходный файл: `util/tracing/tracing.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [InstallExportPipeline](#installexportpipeline-utiltracingtracinggo15) `:15`

- 🔗 [newTraceProvider](#newtraceprovider-utiltracingtracinggo28) `:28`


</details>


[function] name: InstallExportPipeline file: util/tracing/tracing.go:15 returns_error: да description: —


### InstallExportPipeline (util/tracing/tracing.go:15)


InstallExportPipeline is a function that performs operations based on the provided parameters and may return an error.


```go
func InstallExportPipeline((func(context.Context) error, error)) (func(context.Context) error, error)
```


**Тип ответа:** func


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `func(context.Context) error`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/tracing/tracing.go:15`



---


[function] name: newTraceProvider file: util/tracing/tracing.go:28 returns_error: нет description: —


### newTraceProvider (util/tracing/tracing.go:28)


newTraceProvider is a function that performs operations based on the provided parameters and returns (exp sdktrace.SpanExporter, serviceName string, sampleRatio float64).


```go
func newTraceProvider((exp sdktrace.SpanExporter, serviceName string, sampleRatio float64)) (exp sdktrace.SpanExporter, serviceName string, sampleRatio float64)
```


**Тип ответа:** exp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sdktrace.SpanExporter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** serviceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sampleRatio


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/tracing/tracing.go:28`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_svcutil.md)

- [Следующая директория](xrpc.md)


---

