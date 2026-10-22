---
title: "Функции: pkg/features"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/features
---


# Функции: pkg/features


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_credentialprovider.md)

- [Следующая директория](pkg_fieldpath.md)


---


## Меню по файлам


- 📄 [pkg/features/client_adapter.go](#pkgfeaturesclient_adaptergo)

- 📄 [pkg/features/kube_features.go](#pkgfeatureskube_featuresgo)


---


## pkg/features/client_adapter.go


📄 Исходный файл: `pkg/features/client_adapter.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Add](#add-pkgfeaturesclient_adaptergo44) `:44`

- 🔗 [AddVersioned](#addversioned-pkgfeaturesclient_adaptergo72) `:72`

- 🔗 [Enabled](#enabled-pkgfeaturesclient_adaptergo38) `:38`

- 🔗 [Set](#set-pkgfeaturesclient_adaptergo112) `:112`


</details>


[function] name: Add file: pkg/features/client_adapter.go:44 returns_error: нет description: —


### Add (pkg/features/client_adapter.go:44)


Add is a method that creates new data based on the provided parameters and returns (in map[clientfeatures.Feature]clientfeatures.FeatureSpec).


```go
func (a *clientAdapter) Add((in map[clientfeatures.Feature]clientfeatures.FeatureSpec)) (in map[clientfeatures.Feature]clientfeatures.FeatureSpec)
```


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** clientfeatures.Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


**Тип ответа:** clientfeatures.FeatureSpec


```json
{
  "Default": false,
  "LockToDefault": false,
  "PreRelease": {},
  "Version": null,
  "MinCompatibilityVersion": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/featuregate/feature_gate.go`


📍 *Расположение:* `pkg/features/client_adapter.go:44`



---


[function] name: AddVersioned file: pkg/features/client_adapter.go:72 returns_error: нет description: AddVersioned adds the provided versioned feature gates.


### AddVersioned (pkg/features/client_adapter.go:72)


AddVersioned adds the provided versioned feature gates.


```go
func (a *clientAdapter) AddVersioned((in map[clientfeatures.Feature]clientfeatures.VersionedSpecs)) (in map[clientfeatures.Feature]clientfeatures.VersionedSpecs)
```


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** clientfeatures.Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


**Тип ответа:** clientfeatures.VersionedSpecs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/features/client_adapter.go:72`



---


[function] name: Enabled file: pkg/features/client_adapter.go:38 returns_error: нет description: —


### Enabled (pkg/features/client_adapter.go:38)


Enabled is a method that performs operations based on the provided parameters and returns (name clientfeatures.Feature).


```go
func (a *clientAdapter) Enabled((name clientfeatures.Feature)) (name clientfeatures.Feature)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** clientfeatures.Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `pkg/features/client_adapter.go:38`



---


[function] name: Set file: pkg/features/client_adapter.go:112 returns_error: нет description: Set implements the unexported interface that client-go feature gate testing expects for
ek8s.io/client-go/features/testi


### Set (pkg/features/client_adapter.go:112)


Set implements the unexported interface that client-go feature gate testing expects for
ek8s.io/client-go/features/testing.SetFeatureDuringTest. This is necessary for integration tests
to set test overrides for client-go feature gates.


```go
func (a *clientAdapter) Set((name clientfeatures.Feature, enabled bool)) (name clientfeatures.Feature, enabled bool)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** clientfeatures.Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


**Тип ответа:** enabled


```json
{
  "value": "string",
  "register": false
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/generators/deepcopy.go`


📍 *Расположение:* `pkg/features/client_adapter.go:112`




## pkg/features/kube_features.go


📄 Исходный файл: `pkg/features/kube_features.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-pkgfeatureskube_featuresgo2586) `:2586`


</details>


[function] name: init file: pkg/features/kube_features.go:2586 returns_error: нет description: —


### init (pkg/features/kube_features.go:2586)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/features/kube_features.go:2586`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_credentialprovider.md)

- [Следующая директория](pkg_fieldpath.md)


---

