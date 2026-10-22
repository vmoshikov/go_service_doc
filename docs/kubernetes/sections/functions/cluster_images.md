---
title: "Функции: cluster/images"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cluster/images
---


# Функции: cluster/images


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cluster_gce.md)

- [Следующая директория](cmd_clicheck.md)


---


## Меню по файлам


- 📄 [cluster/images/etcd-version-monitor/etcd-version-monitor.go](#clusterimagesetcd-version-monitoretcd-version-monitorgo)


---


## cluster/images/etcd-version-monitor/etcd-version-monitor.go


📄 Исходный файл: `cluster/images/etcd-version-monitor/etcd-version-monitor.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [Gather](#gather-clusterimagesetcd-version-monitoretcd-version-monitorgo153) `:153`

- 🔗 [deepCopyLabelPair](#deepcopylabelpair-clusterimagesetcd-version-monitoretcd-version-monitorgo379) `:379`

- 🔗 [deepCopyMetric](#deepcopymetric-clusterimagesetcd-version-monitoretcd-version-monitorgo364) `:364`

- 🔗 [deepCopyMetricFamily](#deepcopymetricfamily-clusterimagesetcd-version-monitoretcd-version-monitorgo352) `:352`

- 🔗 [deleteLabels](#deletelabels-clusterimagesetcd-version-monitoretcd-version-monitorgo335) `:335`

- 🔗 [filterMetricsByLabels](#filtermetricsbylabels-clusterimagesetcd-version-monitoretcd-version-monitorgo292) `:292`

- 🔗 [getVersion](#getversion-clusterimagesetcd-version-monitoretcd-version-monitorgo203) `:203`

- 🔗 [getVersionPeriodically](#getversionperiodically-clusterimagesetcd-version-monitoretcd-version-monitorgo246) `:246`

- 🔗 [groupCounterMetricsByLabels](#groupcountermetricsbylabels-clusterimagesetcd-version-monitoretcd-version-monitorgo309) `:309`

- 🔗 [identity](#identity-clusterimagesetcd-version-monitoretcd-version-monitorgo348) `:348`

- 🔗 [labelsKey](#labelskey-clusterimagesetcd-version-monitoretcd-version-monitorgo324) `:324`

- 🔗 [main](#main-clusterimagesetcd-version-monitoretcd-version-monitorgo386) `:386`

- 🔗 [registerFlags](#registerflags-clusterimagesetcd-version-monitoretcd-version-monitorgo46) `:46`

- 🔗 [renameLabels](#renamelabels-clusterimagesetcd-version-monitoretcd-version-monitorgo282) `:282`

- 🔗 [renameMetric](#renamemetric-clusterimagesetcd-version-monitoretcd-version-monitorgo278) `:278`

- 🔗 [rewriteExportedMetrics](#rewriteexportedmetrics-clusterimagesetcd-version-monitoretcd-version-monitorgo172) `:172`

- 🔗 [scrapeMetrics](#scrapemetrics-clusterimagesetcd-version-monitoretcd-version-monitorgo261) `:261`


</details>


[function] name: Gather file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:153 returns_error: да description: —


### Gather (cluster/images/etcd-version-monitor/etcd-version-monitor.go:153)


Gather is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *monitorGatherer) Gather(([]*dto.MetricFamily, error)) ([]*dto.MetricFamily, error)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*dto.MetricFamily`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:153`



---


[function] name: deepCopyLabelPair file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:379 returns_error: нет description: —


### deepCopyLabelPair (cluster/images/etcd-version-monitor/etcd-version-monitor.go:379)


deepCopyLabelPair is a function that performs operations based on the provided parameters and returns (lp *dto.LabelPair).


```go
func deepCopyLabelPair((lp *dto.LabelPair)) (lp *dto.LabelPair)
```


**Тип запроса:** dto.LabelPair


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lp


```json
{
  "restClient": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/clientset/versioned/typed/metrics/v1alpha1/metrics_client.go`


**Тип ответа:** dto.LabelPair


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:379`



---


[function] name: deepCopyMetric file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:364 returns_error: нет description: —


### deepCopyMetric (cluster/images/etcd-version-monitor/etcd-version-monitor.go:364)


deepCopyMetric is a function that performs operations based on the provided parameters and returns (m *dto.Metric).


```go
func deepCopyMetric((m *dto.Metric)) (m *dto.Metric)
```


**Тип запроса:** dto.Metric


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


**Тип ответа:** dto.Metric


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


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:364`



---


[function] name: deepCopyMetricFamily file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:352 returns_error: нет description: —


### deepCopyMetricFamily (cluster/images/etcd-version-monitor/etcd-version-monitor.go:352)


deepCopyMetricFamily is a function that performs operations based on the provided parameters and returns (mf *dto.MetricFamily).


```go
func deepCopyMetricFamily((mf *dto.MetricFamily)) (mf *dto.MetricFamily)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:352`



---


[function] name: deleteLabels file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:335 returns_error: нет description: —


### deleteLabels (cluster/images/etcd-version-monitor/etcd-version-monitor.go:335)


deleteLabels is a function that performs operations based on the provided parameters and returns (mf *dto.MetricFamily, names map[string]bool).


```go
func deleteLabels((mf *dto.MetricFamily, names map[string]bool)) (mf *dto.MetricFamily, names map[string]bool)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** names


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:335`



---


[function] name: filterMetricsByLabels file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:292 returns_error: нет description: —


### filterMetricsByLabels (cluster/images/etcd-version-monitor/etcd-version-monitor.go:292)


filterMetricsByLabels is a function that performs operations based on the provided parameters and returns (mf *dto.MetricFamily, labelValues map[string]string).


```go
func filterMetricsByLabels((mf *dto.MetricFamily, labelValues map[string]string)) (mf *dto.MetricFamily, labelValues map[string]string)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelValues


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:292`



---


[function] name: getVersion file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:203 returns_error: нет description: Function for fetching etcd version info and feeding it to the prometheus metric.


### getVersion (cluster/images/etcd-version-monitor/etcd-version-monitor.go:203)


Function for fetching etcd version info and feeding it to the prometheus metric.


```go
func getVersion((lastSeenBinaryVersion *string)) (lastSeenBinaryVersion *string)
```


**Тип ответа:** lastSeenBinaryVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:203`



---


[function] name: getVersionPeriodically file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:246 returns_error: нет description: Periodically fetches etcd version info.


### getVersionPeriodically (cluster/images/etcd-version-monitor/etcd-version-monitor.go:246)


Periodically fetches etcd version info.


```go
func getVersionPeriodically((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:246`



---


[function] name: groupCounterMetricsByLabels file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:309 returns_error: нет description: —


### groupCounterMetricsByLabels (cluster/images/etcd-version-monitor/etcd-version-monitor.go:309)


groupCounterMetricsByLabels is a function that performs operations based on the provided parameters and returns (mf *dto.MetricFamily, names map[string]bool).


```go
func groupCounterMetricsByLabels((mf *dto.MetricFamily, names map[string]bool)) (mf *dto.MetricFamily, names map[string]bool)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** names


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:309`



---


[function] name: identity file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:348 returns_error: да description: —


### identity (cluster/images/etcd-version-monitor/etcd-version-monitor.go:348)


identity is a function that performs operations based on the provided parameters and may return an error.


```go
func identity((*dto.MetricFamily, error)) (*dto.MetricFamily, error)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*dto.MetricFamily`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:348`



---


[function] name: labelsKey file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:324 returns_error: нет description: —


### labelsKey (cluster/images/etcd-version-monitor/etcd-version-monitor.go:324)


labelsKey is a function that performs operations based on the provided parameters and returns (lbls []*dto.LabelPair).


```go
func labelsKey((lbls []*dto.LabelPair)) (lbls []*dto.LabelPair)
```


**Тип запроса:** dto.LabelPair


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lbls


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.LabelPair


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:324`



---


[function] name: main file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:386 returns_error: нет description: —


### main (cluster/images/etcd-version-monitor/etcd-version-monitor.go:386)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:386`



---


[function] name: registerFlags file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:46 returns_error: нет description: —


### registerFlags (cluster/images/etcd-version-monitor/etcd-version-monitor.go:46)


registerFlags is a function that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func registerFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
```


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** fs


```json
{
  "EndpointsName": "string",
  "Path": "string",
  "ReadOnly": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/glusterfsvolumesource.go`


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:46`



---


[function] name: renameLabels file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:282 returns_error: нет description: —


### renameLabels (cluster/images/etcd-version-monitor/etcd-version-monitor.go:282)


renameLabels is a function that performs operations based on the provided parameters and returns (mf *dto.MetricFamily, nameMapping map[string]string).


```go
func renameLabels((mf *dto.MetricFamily, nameMapping map[string]string)) (mf *dto.MetricFamily, nameMapping map[string]string)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nameMapping


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:282`



---


[function] name: renameMetric file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:278 returns_error: нет description: —


### renameMetric (cluster/images/etcd-version-monitor/etcd-version-monitor.go:278)


renameMetric is a function that performs operations based on the provided parameters and returns (mf *dto.MetricFamily, name string).


```go
func renameMetric((mf *dto.MetricFamily, name string)) (mf *dto.MetricFamily, name string)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:278`



---


[function] name: rewriteExportedMetrics file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:172 returns_error: да description: —


### rewriteExportedMetrics (cluster/images/etcd-version-monitor/etcd-version-monitor.go:172)


rewriteExportedMetrics is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *monitorGatherer) rewriteExportedMetrics(([]*dto.MetricFamily, error)) ([]*dto.MetricFamily, error)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*dto.MetricFamily`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:172`



---


[function] name: scrapeMetrics file: cluster/images/etcd-version-monitor/etcd-version-monitor.go:261 returns_error: да description: scrapeMetrics scrapes the prometheus metrics from the etcd metrics URI.


### scrapeMetrics (cluster/images/etcd-version-monitor/etcd-version-monitor.go:261)


scrapeMetrics scrapes the prometheus metrics from the etcd metrics URI.


```go
func scrapeMetrics((map[string]*dto.MetricFamily, error)) (map[string]*dto.MetricFamily, error)
```


**Тип запроса:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** dto.MetricFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]*dto.MetricFamily`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cluster/images/etcd-version-monitor/etcd-version-monitor.go:261`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cluster_gce.md)

- [Следующая директория](cmd_clicheck.md)


---

