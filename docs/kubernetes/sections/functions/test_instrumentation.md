---
title: "Функции: test/instrumentation"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/instrumentation
---


# Функции: test/instrumentation


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_images.md)

- [Следующая директория](test_integration.md)


---


## Меню по файлам


- 📄 [test/instrumentation/decode_metric.go](#testinstrumentationdecode_metricgo)

- 📄 [test/instrumentation/documentation/main.go](#testinstrumentationdocumentationmaingo)

- 📄 [test/instrumentation/endpoint_mapping.go](#testinstrumentationendpoint_mappinggo)

- 📄 [test/instrumentation/error.go](#testinstrumentationerrorgo)

- 📄 [test/instrumentation/find_stable_metric.go](#testinstrumentationfind_stable_metricgo)

- 📄 [test/instrumentation/internal/metric/metric.go](#testinstrumentationinternalmetricmetricgo)

- 📄 [test/instrumentation/main.go](#testinstrumentationmaingo)

- 📄 [test/instrumentation/sort/main.go](#testinstrumentationsortmaingo)

- 📄 [test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go](#testinstrumentationtestdatapkgkubeletmetricsmetricsgo)


---


## test/instrumentation/decode_metric.go


📄 Исходный файл: `test/instrumentation/decode_metric.go`


<details open>
<summary><b>Функции в этом файле (24)</b></summary>


- 🔗 [decodeBucketArguments](#decodebucketarguments-testinstrumentationdecode_metricgo737) `:737`

- 🔗 [decodeBucketFunctionCall](#decodebucketfunctioncall-testinstrumentationdecode_metricgo459) `:459`

- 🔗 [decodeBuckets](#decodebuckets-testinstrumentationdecode_metricgo423) `:423`

- 🔗 [decodeBuildFQNameArguments](#decodebuildfqnamearguments-testinstrumentationdecode_metricgo767) `:767`

- 🔗 [decodeConstLabels](#decodeconstlabels-testinstrumentationdecode_metricgo799) `:799`

- 🔗 [decodeDesc](#decodedesc-testinstrumentationdecode_metricgo126) `:126`

- 🔗 [decodeFloatMap](#decodefloatmap-testinstrumentationdecode_metricgo690) `:690`

- 🔗 [decodeInt64](#decodeint64-testinstrumentationdecode_metricgo612) `:612`

- 🔗 [decodeLabels](#decodelabels-testinstrumentationdecode_metricgo301) `:301`

- 🔗 [decodeLabelsFromArray](#decodelabelsfromarray-testinstrumentationdecode_metricgo288) `:288`

- 🔗 [decodeListOfFloats](#decodelistoffloats-testinstrumentationdecode_metricgo718) `:718`

- 🔗 [decodeMetric](#decodemetric-testinstrumentationdecode_metricgo119) `:119`

- 🔗 [decodeMetricCalls](#decodemetriccalls-testinstrumentationdecode_metricgo32) `:32`

- 🔗 [decodeMetricVec](#decodemetricvec-testinstrumentationdecode_metricgo257) `:257`

- 🔗 [decodeMetricVecForTimingRatioHistogram](#decodemetricvecfortimingratiohistogram-testinstrumentationdecode_metricgo274) `:274`

- 🔗 [decodeNewMetricCall](#decodenewmetriccall-testinstrumentationdecode_metricgo57) `:57`

- 🔗 [decodeObjectives](#decodeobjectives-testinstrumentationdecode_metricgo564) `:564`

- 🔗 [decodeOpts](#decodeopts-testinstrumentationdecode_metricgo323) `:323`

- 🔗 [decodeStabilityLevel](#decodestabilitylevel-testinstrumentationdecode_metricgo782) `:782`

- 🔗 [decodeString](#decodestring-testinstrumentationdecode_metricgo165) `:165`

- 🔗 [decodeUint32](#decodeuint32-testinstrumentationdecode_metricgo578) `:578`

- 🔗 [extractTimeExpression](#extracttimeexpression-testinstrumentationdecode_metricgo660) `:660`

- 🔗 [getMetricType](#getmetrictype-testinstrumentationdecode_metricgo100) `:100`

- 🔗 [stringValue](#stringvalue-testinstrumentationdecode_metricgo416) `:416`


</details>


[function] name: decodeBucketArguments file: test/instrumentation/decode_metric.go:737 returns_error: да description: —


### decodeBucketArguments (test/instrumentation/decode_metric.go:737)


decodeBucketArguments is a function that performs operations based on the provided parameters and may return an error.


```go
func decodeBucketArguments((float64, float64, int, error)) (float64, float64, int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `float64`, `float64`, `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:737`



---


[function] name: decodeBucketFunctionCall file: test/instrumentation/decode_metric.go:459 returns_error: да description: —


### decodeBucketFunctionCall (test/instrumentation/decode_metric.go:459)


decodeBucketFunctionCall is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeBucketFunctionCall(([]float64, error, bool)) ([]float64, error, bool)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]float64`, `error`, `bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:459`



---


[function] name: decodeBuckets file: test/instrumentation/decode_metric.go:423 returns_error: да description: —


### decodeBuckets (test/instrumentation/decode_metric.go:423)


decodeBuckets is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeBuckets(([]float64, error)) ([]float64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]float64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:423`



---


[function] name: decodeBuildFQNameArguments file: test/instrumentation/decode_metric.go:767 returns_error: да description: —


### decodeBuildFQNameArguments (test/instrumentation/decode_metric.go:767)


decodeBuildFQNameArguments is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeBuildFQNameArguments((string, string, string, error)) (string, string, string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `string`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:767`



---


[function] name: decodeConstLabels file: test/instrumentation/decode_metric.go:799 returns_error: да description: —


### decodeConstLabels (test/instrumentation/decode_metric.go:799)


decodeConstLabels is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeConstLabels((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:799`



---


[function] name: decodeDesc file: test/instrumentation/decode_metric.go:126 returns_error: да description: —


### decodeDesc (test/instrumentation/decode_metric.go:126)


decodeDesc is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeDesc((metric.Metric, error)) (metric.Metric, error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metric.Metric`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:126`



---


[function] name: decodeFloatMap file: test/instrumentation/decode_metric.go:690 returns_error: да description: —


### decodeFloatMap (test/instrumentation/decode_metric.go:690)


decodeFloatMap is a function that performs operations based on the provided parameters and may return an error.


```go
func decodeFloatMap((map[float64]float64, error)) (map[float64]float64, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[float64]float64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:690`



---


[function] name: decodeInt64 file: test/instrumentation/decode_metric.go:612 returns_error: да description: —


### decodeInt64 (test/instrumentation/decode_metric.go:612)


decodeInt64 is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeInt64((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:612`



---


[function] name: decodeLabels file: test/instrumentation/decode_metric.go:301 returns_error: да description: —


### decodeLabels (test/instrumentation/decode_metric.go:301)


decodeLabels is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeLabels(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:301`



---


[function] name: decodeLabelsFromArray file: test/instrumentation/decode_metric.go:288 returns_error: да description: —


### decodeLabelsFromArray (test/instrumentation/decode_metric.go:288)


decodeLabelsFromArray is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeLabelsFromArray(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:288`



---


[function] name: decodeListOfFloats file: test/instrumentation/decode_metric.go:718 returns_error: да description: —


### decodeListOfFloats (test/instrumentation/decode_metric.go:718)


decodeListOfFloats is a function that performs operations based on the provided parameters and may return an error.


```go
func decodeListOfFloats(([]float64, error)) ([]float64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]float64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:718`



---


[function] name: decodeMetric file: test/instrumentation/decode_metric.go:119 returns_error: да description: —


### decodeMetric (test/instrumentation/decode_metric.go:119)


decodeMetric is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeMetric((metric.Metric, error)) (metric.Metric, error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metric.Metric`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:119`



---


[function] name: decodeMetricCalls file: test/instrumentation/decode_metric.go:32 returns_error: да description: —


### decodeMetricCalls (test/instrumentation/decode_metric.go:32)


decodeMetricCalls is a function that performs operations based on the provided parameters and may return an error.


```go
func decodeMetricCalls(([]metric.Metric, []error)) ([]metric.Metric, []error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metric.Metric`, `[]error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:32`



---


[function] name: decodeMetricVec file: test/instrumentation/decode_metric.go:257 returns_error: да description: —


### decodeMetricVec (test/instrumentation/decode_metric.go:257)


decodeMetricVec is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeMetricVec((metric.Metric, error)) (metric.Metric, error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metric.Metric`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:257`



---


[function] name: decodeMetricVecForTimingRatioHistogram file: test/instrumentation/decode_metric.go:274 returns_error: да description: —


### decodeMetricVecForTimingRatioHistogram (test/instrumentation/decode_metric.go:274)


decodeMetricVecForTimingRatioHistogram is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeMetricVecForTimingRatioHistogram((metric.Metric, error)) (metric.Metric, error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metric.Metric`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:274`



---


[function] name: decodeNewMetricCall file: test/instrumentation/decode_metric.go:57 returns_error: да description: —


### decodeNewMetricCall (test/instrumentation/decode_metric.go:57)


decodeNewMetricCall is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeNewMetricCall((*metric.Metric, error)) (*metric.Metric, error)
```


**Тип запроса:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*metric.Metric`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:57`



---


[function] name: decodeObjectives file: test/instrumentation/decode_metric.go:564 returns_error: да description: —


### decodeObjectives (test/instrumentation/decode_metric.go:564)


decodeObjectives is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeObjectives((map[float64]float64, error)) (map[float64]float64, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[float64]float64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:564`



---


[function] name: decodeOpts file: test/instrumentation/decode_metric.go:323 returns_error: да description: —


### decodeOpts (test/instrumentation/decode_metric.go:323)


decodeOpts is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeOpts((metric.Metric, error)) (metric.Metric, error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metric.Metric`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:323`



---


[function] name: decodeStabilityLevel file: test/instrumentation/decode_metric.go:782 returns_error: да description: —


### decodeStabilityLevel (test/instrumentation/decode_metric.go:782)


decodeStabilityLevel is a function that performs operations based on the provided parameters and may return an error.


```go
func decodeStabilityLevel((*metrics.StabilityLevel, error)) (*metrics.StabilityLevel, error)
```


**Тип запроса:** metrics.StabilityLevel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metrics.StabilityLevel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*metrics.StabilityLevel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:782`



---


[function] name: decodeString file: test/instrumentation/decode_metric.go:165 returns_error: да description: —


### decodeString (test/instrumentation/decode_metric.go:165)


decodeString is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeString((*string, error)) (*string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:165`



---


[function] name: decodeUint32 file: test/instrumentation/decode_metric.go:578 returns_error: да description: —


### decodeUint32 (test/instrumentation/decode_metric.go:578)


decodeUint32 is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) decodeUint32((uint32, error)) (uint32, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `uint32`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:578`



---


[function] name: extractTimeExpression file: test/instrumentation/decode_metric.go:660 returns_error: да description: —


### extractTimeExpression (test/instrumentation/decode_metric.go:660)


extractTimeExpression is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *metricDecoder) extractTimeExpression((int64, error, bool)) (int64, error, bool)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`, `bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:660`



---


[function] name: getMetricType file: test/instrumentation/decode_metric.go:100 returns_error: нет description: —


### getMetricType (test/instrumentation/decode_metric.go:100)


getMetricType is a function that performs operations based on the provided parameters and returns (functionName string).


```go
func getMetricType((functionName string)) (functionName string)
```


**Тип ответа:** functionName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/instrumentation/decode_metric.go:100`



---


[function] name: stringValue file: test/instrumentation/decode_metric.go:416 returns_error: да description: —


### stringValue (test/instrumentation/decode_metric.go:416)


stringValue is a function that performs operations based on the provided parameters and may return an error.


```go
func stringValue((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/decode_metric.go:416`




## test/instrumentation/documentation/main.go


📄 Исходный файл: `test/instrumentation/documentation/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [byStabilityLevel](#bystabilitylevel-testinstrumentationdocumentationmaingo175) `:175`

- 🔗 [main](#main-testinstrumentationdocumentationmaingo130) `:130`

- 🔗 [parseMinor](#parseminor-testinstrumentationdocumentationmaingo186) `:186`


</details>


[function] name: byStabilityLevel file: test/instrumentation/documentation/main.go:175 returns_error: нет description: —


### byStabilityLevel (test/instrumentation/documentation/main.go:175)


byStabilityLevel is a function that performs operations based on the provided parameters and returns (ms []metric.Metric).


```go
func byStabilityLevel((ms []metric.Metric)) (ms []metric.Metric)
```


**Тип ответа:** ms


```json
{
  "terms": []
}
```


*Определено в:* `staging/src/k8s.io/component-helpers/scheduling/corev1/nodeaffinity/nodeaffinity.go`


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


📍 *Расположение:* `test/instrumentation/documentation/main.go:175`



---


[function] name: main file: test/instrumentation/documentation/main.go:130 returns_error: нет description: —


### main (test/instrumentation/documentation/main.go:130)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/instrumentation/documentation/main.go:130`



---


[function] name: parseMinor file: test/instrumentation/documentation/main.go:186 returns_error: нет description: —


### parseMinor (test/instrumentation/documentation/main.go:186)


parseMinor is a function that performs operations based on the provided parameters and returns (m string).


```go
func parseMinor((m string)) (m string)
```


**Тип ответа:** m


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `test/instrumentation/documentation/main.go:186`




## test/instrumentation/endpoint_mapping.go


📄 Исходный файл: `test/instrumentation/endpoint_mapping.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [allCoreComponentEndpoints](#allcorecomponentendpoints-testinstrumentationendpoint_mappinggo122) `:122`

- 🔗 [inferComponent](#infercomponent-testinstrumentationendpoint_mappinggo93) `:93`

- 🔗 [inferComponentEndpoints](#infercomponentendpoints-testinstrumentationendpoint_mappinggo58) `:58`

- 🔗 [inferEndpoint](#inferendpoint-testinstrumentationendpoint_mappinggo112) `:112`

- 🔗 [isSharedPath](#issharedpath-testinstrumentationendpoint_mappinggo84) `:84`

- 🔗 [loadEndpointMappingConfig](#loadendpointmappingconfig-testinstrumentationendpoint_mappinggo42) `:42`


</details>


[function] name: allCoreComponentEndpoints file: test/instrumentation/endpoint_mapping.go:122 returns_error: нет description: allCoreComponentEndpoints returns a ComponentEndpoint for each core component with the given endpoint.


### allCoreComponentEndpoints (test/instrumentation/endpoint_mapping.go:122)


allCoreComponentEndpoints returns a ComponentEndpoint for each core component with the given endpoint.


```go
func (c *endpointMappingConfig) allCoreComponentEndpoints((endpoint string)) (endpoint string)
```


**Тип ответа:** endpoint


```json
{
  "URL": "string",
  "AccessToken": "string",
  "JWT": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


📍 *Расположение:* `test/instrumentation/endpoint_mapping.go:122`



---


[function] name: inferComponent file: test/instrumentation/endpoint_mapping.go:93 returns_error: нет description: —


### inferComponent (test/instrumentation/endpoint_mapping.go:93)


inferComponent is a method that performs operations based on the provided parameters and returns (filePath string, components map[string][]string).


```go
func (c *endpointMappingConfig) inferComponent((filePath string, components map[string][]string)) (filePath string, components map[string][]string)
```


**Тип ответа:** filePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** components


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/instrumentation/endpoint_mapping.go:93`



---


[function] name: inferComponentEndpoints file: test/instrumentation/endpoint_mapping.go:58 returns_error: нет description: inferComponentEndpoints determines the component(s) and endpoint for a metric based on its source file path.


### inferComponentEndpoints (test/instrumentation/endpoint_mapping.go:58)


inferComponentEndpoints determines the component(s) and endpoint for a metric based on its source file path.


```go
func (c *endpointMappingConfig) inferComponentEndpoints((filePath string)) (filePath string)
```


**Тип ответа:** filePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/instrumentation/endpoint_mapping.go:58`



---


[function] name: inferEndpoint file: test/instrumentation/endpoint_mapping.go:112 returns_error: нет description: —


### inferEndpoint (test/instrumentation/endpoint_mapping.go:112)


inferEndpoint is a method that performs operations based on the provided parameters and returns (filePath string).


```go
func (c *endpointMappingConfig) inferEndpoint((filePath string)) (filePath string)
```


**Тип ответа:** filePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/instrumentation/endpoint_mapping.go:112`



---


[function] name: isSharedPath file: test/instrumentation/endpoint_mapping.go:84 returns_error: нет description: —


### isSharedPath (test/instrumentation/endpoint_mapping.go:84)


isSharedPath is a method that performs operations based on the provided parameters and returns (filePath string).


```go
func (c *endpointMappingConfig) isSharedPath((filePath string)) (filePath string)
```


**Тип ответа:** filePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/instrumentation/endpoint_mapping.go:84`



---


[function] name: loadEndpointMappingConfig file: test/instrumentation/endpoint_mapping.go:42 returns_error: да description: —


### loadEndpointMappingConfig (test/instrumentation/endpoint_mapping.go:42)


loadEndpointMappingConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func loadEndpointMappingConfig((*endpointMappingConfig, error)) (*endpointMappingConfig, error)
```


**Тип запроса:** endpointMappingConfig


```json
{
  "CoreComponents": {},
  "StandaloneComponents": {},
  "SharedPaths": [],
  "EndpointMappings": [],
  "DefaultEndpoint": "string"
}
```


*Определено в:* `test/instrumentation/endpoint_mapping.go`


**Тип ответа:** endpointMappingConfig


```json
{
  "CoreComponents": {},
  "StandaloneComponents": {},
  "SharedPaths": [],
  "EndpointMappings": [],
  "DefaultEndpoint": "string"
}
```


*Определено в:* `test/instrumentation/endpoint_mapping.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*endpointMappingConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/endpoint_mapping.go:42`




## test/instrumentation/error.go


📄 Исходный файл: `test/instrumentation/error.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Error](#error-testinstrumentationerrorgo65) `:65`

- 🔗 [errorWithFileInformation](#errorwithfileinformation-testinstrumentationerrorgo69) `:69`

- 🔗 [newDecodeErrorf](#newdecodeerrorf-testinstrumentationerrorgo56) `:56`


</details>


[function] name: Error file: test/instrumentation/error.go:65 returns_error: нет description: —


### Error (test/instrumentation/error.go:65)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e decodeError) Error(()) ()
```


📍 *Расположение:* `test/instrumentation/error.go:65`



---


[function] name: errorWithFileInformation file: test/instrumentation/error.go:69 returns_error: нет description: —


### errorWithFileInformation (test/instrumentation/error.go:69)


errorWithFileInformation is a method that performs operations based on the provided parameters and returns (fileset *token.FileSet).


```go
func (e decodeError) errorWithFileInformation((fileset *token.FileSet)) (fileset *token.FileSet)
```


**Тип запроса:** token.FileSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fileset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** token.FileSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/instrumentation/error.go:69`



---


[function] name: newDecodeErrorf file: test/instrumentation/error.go:56 returns_error: нет description: —


### newDecodeErrorf (test/instrumentation/error.go:56)


newDecodeErrorf is a function that performs operations based on the provided parameters and returns (node ast.Node, format string, a ...interface{}).


```go
func newDecodeErrorf((node ast.Node, format string, a ...interface{})) (node ast.Node, format string, a ...interface{})
```


**Тип ответа:** node


```json
{
  "identity": {},
  "dependentsLock": {},
  "dependents": {},
  "deletingDependents": false,
  "deletingDependentsLock": {},
  "beingDeleted": false,
  "beingDeletedLock": {},
  "virtual": false,
  "virtualLock": {},
  "owners": [],
  "ownersLock": {}
}
```


*Определено в:* `pkg/controller/garbagecollector/graph.go`


**Тип ответа:** ast.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** format


```json
{
  "availableOnNodes": null,
  "allocation": null
}
```


*Определено в:* `pkg/scheduler/framework/plugins/dynamicresources/dynamicresources.go`


**Тип ответа:** a


```json
{
  "Name": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/dependencycheck/dependencycheck.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/instrumentation/error.go:56`




## test/instrumentation/find_stable_metric.go


📄 Исходный файл: `test/instrumentation/find_stable_metric.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Visit](#visit-testinstrumentationfind_stable_metricgo64) `:64`

- 🔗 [contains](#contains-testinstrumentationfind_stable_metricgo55) `:55`

- 🔗 [findStableMetricDeclaration](#findstablemetricdeclaration-testinstrumentationfind_stable_metricgo35) `:35`

- 🔗 [getStabilityLevel](#getstabilitylevel-testinstrumentationfind_stable_metricgo145) `:145`

- 🔗 [isMetricOps](#ismetricops-testinstrumentationfind_stable_metricgo134) `:134`


</details>


[function] name: Visit file: test/instrumentation/find_stable_metric.go:64 returns_error: нет description: —


### Visit (test/instrumentation/find_stable_metric.go:64)


Visit is a method that performs operations based on the provided parameters and returns (w ast.Visitor).


```go
func (f *stableMetricFinder) Visit((w ast.Visitor)) (w ast.Visitor)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** ast.Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `test/instrumentation/find_stable_metric.go:64`



---


[function] name: contains file: test/instrumentation/find_stable_metric.go:55 returns_error: нет description: —


### contains (test/instrumentation/find_stable_metric.go:55)


contains is a function that performs operations based on the provided parameters and returns (v metrics.StabilityLevel, a []metrics.StabilityLevel).


```go
func contains((v metrics.StabilityLevel, a []metrics.StabilityLevel)) (v metrics.StabilityLevel, a []metrics.StabilityLevel)
```


**Тип ответа:** v


```json
{
  "ClientConfig": null,
  "ServerOpts": null,
  "TearDownFn": {},
  "TmpDir": "string",
  "EtcdClient": null,
  "EtcdStoragePrefix": "string"
}
```


*Определено в:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go`


**Тип ответа:** metrics.StabilityLevel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a


```json
{
  "Name": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/dependencycheck/dependencycheck.go`


**Тип ответа:** metrics.StabilityLevel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/instrumentation/find_stable_metric.go:55`



---


[function] name: findStableMetricDeclaration file: test/instrumentation/find_stable_metric.go:35 returns_error: да description: —


### findStableMetricDeclaration (test/instrumentation/find_stable_metric.go:35)


findStableMetricDeclaration is a function that performs operations based on the provided parameters and may return an error.


```go
func findStableMetricDeclaration(([]*ast.CallExpr, []error)) ([]*ast.CallExpr, []error)
```


**Тип запроса:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*ast.CallExpr`, `[]error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/find_stable_metric.go:35`



---


[function] name: getStabilityLevel file: test/instrumentation/find_stable_metric.go:145 returns_error: да description: —


### getStabilityLevel (test/instrumentation/find_stable_metric.go:145)


getStabilityLevel is a function that performs operations based on the provided parameters and may return an error.


```go
func getStabilityLevel((*metrics.StabilityLevel, error)) (*metrics.StabilityLevel, error)
```


**Тип запроса:** metrics.StabilityLevel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metrics.StabilityLevel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*metrics.StabilityLevel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/find_stable_metric.go:145`



---


[function] name: isMetricOps file: test/instrumentation/find_stable_metric.go:134 returns_error: нет description: —


### isMetricOps (test/instrumentation/find_stable_metric.go:134)


isMetricOps is a function that performs operations based on the provided parameters and returns (name string).


```go
func isMetricOps((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/instrumentation/find_stable_metric.go:134`




## test/instrumentation/internal/metric/metric.go


📄 Исходный файл: `test/instrumentation/internal/metric/metric.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [BuildFQName](#buildfqname-testinstrumentationinternalmetricmetricgo59) `:59`

- 🔗 [Len](#len-testinstrumentationinternalmetricmetricgo66) `:66`

- 🔗 [Less](#less-testinstrumentationinternalmetricmetricgo67) `:67`

- 🔗 [Swap](#swap-testinstrumentationinternalmetricmetricgo75) `:75`


</details>


[function] name: BuildFQName file: test/instrumentation/internal/metric/metric.go:59 returns_error: нет description: BuildFQName returns the fully qualified metric name.


### BuildFQName (test/instrumentation/internal/metric/metric.go:59)


BuildFQName returns the fully qualified metric name.


```go
func (m Metric) BuildFQName(()) ()
```


📍 *Расположение:* `test/instrumentation/internal/metric/metric.go:59`



---


[function] name: Len file: test/instrumentation/internal/metric/metric.go:66 returns_error: нет description: —


### Len (test/instrumentation/internal/metric/metric.go:66)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (ms ByFQName) Len(()) ()
```


📍 *Расположение:* `test/instrumentation/internal/metric/metric.go:66`



---


[function] name: Less file: test/instrumentation/internal/metric/metric.go:67 returns_error: нет description: —


### Less (test/instrumentation/internal/metric/metric.go:67)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (ms ByFQName) Less((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `test/instrumentation/internal/metric/metric.go:67`



---


[function] name: Swap file: test/instrumentation/internal/metric/metric.go:75 returns_error: нет description: —


### Swap (test/instrumentation/internal/metric/metric.go:75)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (ms ByFQName) Swap((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `test/instrumentation/internal/metric/metric.go:75`




## test/instrumentation/main.go


📄 Исходный файл: `test/instrumentation/main.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [addFileInformationToErrors](#addfileinformationtoerrors-testinstrumentationmaingo220) `:220`

- 🔗 [findGOOS](#findgoos-testinstrumentationmaingo52) `:52`

- 🔗 [findPkgDir](#findpkgdir-testinstrumentationmaingo247) `:247`

- 🔗 [getLocalNameOfImportedPackage](#getlocalnameofimportedpackage-testinstrumentationmaingo203) `:203`

- 🔗 [globalVariableDeclarations](#globalvariabledeclarations-testinstrumentationmaingo229) `:229`

- 🔗 [importedGlobalVariableDeclaration](#importedglobalvariabledeclaration-testinstrumentationmaingo267) `:267`

- 🔗 [main](#main-testinstrumentationmaingo64) `:64`

- 🔗 [searchFileForStableMetrics](#searchfileforstablemetrics-testinstrumentationmaingo163) `:163`

- 🔗 [searchPathForStableMetrics](#searchpathforstablemetrics-testinstrumentationmaingo141) `:141`


</details>


[function] name: addFileInformationToErrors file: test/instrumentation/main.go:220 returns_error: да description: —


### addFileInformationToErrors (test/instrumentation/main.go:220)


addFileInformationToErrors is a function that performs operations based on the provided parameters and may return an error.


```go
func addFileInformationToErrors((es []error, fileset *token.FileSet)) (es []error, fileset *token.FileSet)
```


**Тип запроса:** token.FileSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** es


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** fileset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** token.FileSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `es []error`, `fileset *token.FileSet`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/main.go:220`



---


[function] name: findGOOS file: test/instrumentation/main.go:52 returns_error: нет description: —


### findGOOS (test/instrumentation/main.go:52)


findGOOS is a function that performs operations based on the provided parameters and returns ().


```go
func findGOOS(()) ()
```


📍 *Расположение:* `test/instrumentation/main.go:52`



---


[function] name: findPkgDir file: test/instrumentation/main.go:247 returns_error: да description: —


### findPkgDir (test/instrumentation/main.go:247)


findPkgDir is a function that performs operations based on the provided parameters and may return an error.


```go
func findPkgDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/main.go:247`



---


[function] name: getLocalNameOfImportedPackage file: test/instrumentation/main.go:203 returns_error: да description: —


### getLocalNameOfImportedPackage (test/instrumentation/main.go:203)


getLocalNameOfImportedPackage is a function that performs operations based on the provided parameters and may return an error.


```go
func getLocalNameOfImportedPackage((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/main.go:203`



---


[function] name: globalVariableDeclarations file: test/instrumentation/main.go:229 returns_error: нет description: —


### globalVariableDeclarations (test/instrumentation/main.go:229)


globalVariableDeclarations is a function that performs operations based on the provided parameters and returns (tree *ast.File).


```go
func globalVariableDeclarations((tree *ast.File)) (tree *ast.File)
```


**Тип запроса:** ast.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** tree


```json
{
  "tree": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/store/store_btree.go`


**Тип ответа:** ast.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


📍 *Расположение:* `test/instrumentation/main.go:229`



---


[function] name: importedGlobalVariableDeclaration file: test/instrumentation/main.go:267 returns_error: да description: —


### importedGlobalVariableDeclaration (test/instrumentation/main.go:267)


importedGlobalVariableDeclaration is a function that performs operations based on the provided parameters and may return an error.


```go
func importedGlobalVariableDeclaration((map[string]ast.Expr, error)) (map[string]ast.Expr, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ast.Expr


```json
{
  "FieldRef": "string",
  "Warning": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/admissionregistration/v1alpha1/expressionwarning.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]ast.Expr`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/main.go:267`



---


[function] name: main file: test/instrumentation/main.go:64 returns_error: нет description: —


### main (test/instrumentation/main.go:64)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/instrumentation/main.go:64`



---


[function] name: searchFileForStableMetrics file: test/instrumentation/main.go:163 returns_error: да description: Pass either only filename of existing file or src including source code in any format and a filename that it comes from


### searchFileForStableMetrics (test/instrumentation/main.go:163)


Pass either only filename of existing file or src including source code in any format and a filename that it comes from


```go
func searchFileForStableMetrics(([]metric.Metric, []error)) ([]metric.Metric, []error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metric.Metric`, `[]error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/main.go:163`



---


[function] name: searchPathForStableMetrics file: test/instrumentation/main.go:141 returns_error: да description: —


### searchPathForStableMetrics (test/instrumentation/main.go:141)


searchPathForStableMetrics is a function that performs operations based on the provided parameters and may return an error.


```go
func searchPathForStableMetrics(([]metric.Metric, []error)) ([]metric.Metric, []error)
```


**Тип ответа:** metric.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metric.Metric`, `[]error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/instrumentation/main.go:141`




## test/instrumentation/sort/main.go


📄 Исходный файл: `test/instrumentation/sort/main.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testinstrumentationsortmaingo30) `:30`


</details>


[function] name: main file: test/instrumentation/sort/main.go:30 returns_error: нет description: —


### main (test/instrumentation/sort/main.go:30)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/instrumentation/sort/main.go:30`




## test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go


📄 Исходный файл: `test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Blah](#blah-testinstrumentationtestdatapkgkubeletmetricsmetricsgo654) `:654`

- 🔗 [GetGather](#getgather-testinstrumentationtestdatapkgkubeletmetricsmetricsgo640) `:640`

- 🔗 [Register](#register-testinstrumentationtestdatapkgkubeletmetricsmetricsgo585) `:585`

- 🔗 [SetNodeName](#setnodename-testinstrumentationtestdatapkgkubeletmetricsmetricsgo650) `:650`

- 🔗 [SinceInSeconds](#sinceinseconds-testinstrumentationtestdatapkgkubeletmetricsmetricsgo645) `:645`

- 🔗 [merge](#merge-testinstrumentationtestdatapkgkubeletmetricsmetricsgo658) `:658`


</details>


[function] name: Blah file: test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:654 returns_error: нет description: —


### Blah (test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:654)


Blah is a function that performs operations based on the provided parameters and returns ().


```go
func Blah(()) ()
```


📍 *Расположение:* `test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:654`



---


[function] name: GetGather file: test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:640 returns_error: нет description: GetGather returns the gatherer. It used by test case outside current package.


### GetGather (test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:640)


GetGather returns the gatherer. It used by test case outside current package.


```go
func GetGather(()) ()
```


📍 *Расположение:* `test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:640`



---


[function] name: Register file: test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:585 returns_error: нет description: Register registers all metrics.


### Register (test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:585)


Register registers all metrics.


```go
func Register((collectors ...metrics.StableCollector)) (collectors ...metrics.StableCollector)
```


**Тип ответа:** collectors


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metrics.StableCollector


```json
{
  "descriptors": {},
  "registerable": {},
  "hidden": {},
  "self": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/collector.go`


📍 *Расположение:* `test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:585`



---


[function] name: SetNodeName file: test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:650 returns_error: нет description: SetNodeName sets the NodeName Gauge to 1.


### SetNodeName (test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:650)


SetNodeName sets the NodeName Gauge to 1.


```go
func SetNodeName((name types.NodeName)) (name types.NodeName)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** types.NodeName


```json
{
  "enableSchedulingQueueHint": false
}
```


*Определено в:* `pkg/scheduler/framework/plugins/nodename/node_name.go`


📍 *Расположение:* `test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:650`



---


[function] name: SinceInSeconds file: test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:645 returns_error: нет description: SinceInSeconds gets the time since the specified start in seconds.


### SinceInSeconds (test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:645)


SinceInSeconds gets the time since the specified start in seconds.


```go
func SinceInSeconds((start time.Time)) (start time.Time)
```


**Тип ответа:** start


```json
{
  "Action": null,
  "ExitCodes": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/containerrestartrule.go`


**Тип ответа:** time.Time


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


📍 *Расположение:* `test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:645`



---


[function] name: merge file: test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:658 returns_error: нет description: —


### merge (test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:658)


merge is a function that performs operations based on the provided parameters and returns (slices ...[]float64).


```go
func merge((slices ...[]float64)) (slices ...[]float64)
```


**Тип ответа:** slices


```json
{
  "toCreate": []
}
```


*Определено в:* `pkg/controller/endpointslicemirroring/reconciler_helpers.go`


📍 *Расположение:* `test/instrumentation/testdata/pkg/kubelet/metrics/metrics.go:658`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_images.md)

- [Следующая директория](test_integration.md)


---

