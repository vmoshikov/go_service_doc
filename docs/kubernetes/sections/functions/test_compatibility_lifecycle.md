---
title: "Функции: test/compatibility_lifecycle"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/compatibility_lifecycle
---


# Функции: test/compatibility_lifecycle


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](staging_src.md)

- [Следующая директория](test_conformance.md)


---


## Меню по файлам


- 📄 [test/compatibility_lifecycle/cmd/feature_gates.go](#testcompatibility_lifecyclecmdfeature_gatesgo)

- 📄 [test/compatibility_lifecycle/cmd/root.go](#testcompatibility_lifecyclecmdrootgo)

- 📄 [test/compatibility_lifecycle/cmd/util.go](#testcompatibility_lifecyclecmdutilgo)

- 📄 [test/compatibility_lifecycle/main.go](#testcompatibility_lifecyclemaingo)


---


## test/compatibility_lifecycle/cmd/feature_gates.go


📄 Исходный файл: `test/compatibility_lifecycle/cmd/feature_gates.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [NewFeatureGatesCommand](#newfeaturegatescommand-testcompatibility_lifecyclecmdfeature_gatesgo69) `:69`

- 🔗 [NewUpdateFeatureListCommand](#newupdatefeaturelistcommand-testcompatibility_lifecyclecmdfeature_gatesgo95) `:95`

- 🔗 [NewVerifyFeatureListCommand](#newverifyfeaturelistcommand-testcompatibility_lifecyclecmdfeature_gatesgo85) `:85`

- 🔗 [dedupeFeatureList](#dedupefeaturelist-testcompatibility_lifecyclecmdfeature_gatesgo181) `:181`

- 🔗 [extractFeatureInfoList](#extractfeatureinfolist-testcompatibility_lifecyclecmdfeature_gatesgo393) `:393`

- 🔗 [extractFeatureInfoListFromFile](#extractfeatureinfolistfromfile-testcompatibility_lifecyclecmdfeature_gatesgo311) `:311`

- 🔗 [getPkgPrefix](#getpkgprefix-testcompatibility_lifecyclecmdfeature_gatesgo367) `:367`

- 🔗 [isFeatureSpecType](#isfeaturespectype-testcompatibility_lifecyclecmdfeature_gatesgo428) `:428`

- 🔗 [parseFeatureInfo](#parsefeatureinfo-testcompatibility_lifecyclecmdfeature_gatesgo437) `:437`

- 🔗 [parseFeatureSpec](#parsefeaturespec-testcompatibility_lifecyclecmdfeature_gatesgo470) `:470`

- 🔗 [parseVersion](#parseversion-testcompatibility_lifecyclecmdfeature_gatesgo514) `:514`

- 🔗 [searchPathForFeatures](#searchpathforfeatures-testcompatibility_lifecyclecmdfeature_gatesgo280) `:280`

- 🔗 [updateFeatureListFunc](#updatefeaturelistfunc-testcompatibility_lifecyclecmdfeature_gatesgo112) `:112`

- 🔗 [verifyAlphaFeatures](#verifyalphafeatures-testcompatibility_lifecyclecmdfeature_gatesgo269) `:269`

- 🔗 [verifyAlphabeticOrder](#verifyalphabeticorder-testcompatibility_lifecyclecmdfeature_gatesgo374) `:374`

- 🔗 [verifyFeatureListFunc](#verifyfeaturelistfunc-testcompatibility_lifecyclecmdfeature_gatesgo104) `:104`

- 🔗 [verifyFeatureRemoval](#verifyfeatureremoval-testcompatibility_lifecyclecmdfeature_gatesgo213) `:213`

- 🔗 [verifyOrUpdateFeatureList](#verifyorupdatefeaturelist-testcompatibility_lifecyclecmdfeature_gatesgo123) `:123`


</details>


[function] name: NewFeatureGatesCommand file: test/compatibility_lifecycle/cmd/feature_gates.go:69 returns_error: нет description: NewFeatureGatesCommand returns the cobra command for "feature-gates".


### NewFeatureGatesCommand (test/compatibility_lifecycle/cmd/feature_gates.go:69)


NewFeatureGatesCommand returns the cobra command for "feature-gates".


```go
func NewFeatureGatesCommand(()) ()
```


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:69`



---


[function] name: NewUpdateFeatureListCommand file: test/compatibility_lifecycle/cmd/feature_gates.go:95 returns_error: нет description: —


### NewUpdateFeatureListCommand (test/compatibility_lifecycle/cmd/feature_gates.go:95)


NewUpdateFeatureListCommand is a function that performs operations based on the provided parameters and returns ().


```go
func NewUpdateFeatureListCommand(()) ()
```


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:95`



---


[function] name: NewVerifyFeatureListCommand file: test/compatibility_lifecycle/cmd/feature_gates.go:85 returns_error: нет description: —


### NewVerifyFeatureListCommand (test/compatibility_lifecycle/cmd/feature_gates.go:85)


NewVerifyFeatureListCommand is a function that performs operations based on the provided parameters and returns ().


```go
func NewVerifyFeatureListCommand(()) ()
```


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:85`



---


[function] name: dedupeFeatureList file: test/compatibility_lifecycle/cmd/feature_gates.go:181 returns_error: да description: —


### dedupeFeatureList (test/compatibility_lifecycle/cmd/feature_gates.go:181)


dedupeFeatureList is a function that performs operations based on the provided parameters and may return an error.


```go
func dedupeFeatureList(([]featureInfo, error)) ([]featureInfo, error)
```


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]featureInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:181`



---


[function] name: extractFeatureInfoList file: test/compatibility_lifecycle/cmd/feature_gates.go:393 returns_error: да description: extractFeatureInfoList extracts the info all the the features from
map[featuregate.Feature]featuregate.VersionedSpecs.


### extractFeatureInfoList (test/compatibility_lifecycle/cmd/feature_gates.go:393)


extractFeatureInfoList extracts the info all the the features from
map[featuregate.Feature]featuregate.VersionedSpecs.


```go
func extractFeatureInfoList(([]featureInfo, error)) ([]featureInfo, error)
```


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]featureInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:393`



---


[function] name: extractFeatureInfoListFromFile file: test/compatibility_lifecycle/cmd/feature_gates.go:311 returns_error: да description: extractFeatureInfoListFromFile extracts info of all the features from
map[featuregate.Feature]featuregate.VersionedSpecs


### extractFeatureInfoListFromFile (test/compatibility_lifecycle/cmd/feature_gates.go:311)


extractFeatureInfoListFromFile extracts info of all the features from
map[featuregate.Feature]featuregate.VersionedSpecs in the given file.


```go
func extractFeatureInfoListFromFile((allFeatures []featureInfo, err error)) (allFeatures []featureInfo, err error)
```


**Тип ответа:** allFeatures


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Тип ответа:** err


```json
{
  "msg": {},
  "cause": {},
  "stack": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/errors/errors.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `allFeatures []featureInfo`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:311`



---


[function] name: getPkgPrefix file: test/compatibility_lifecycle/cmd/feature_gates.go:367 returns_error: нет description: —


### getPkgPrefix (test/compatibility_lifecycle/cmd/feature_gates.go:367)


getPkgPrefix is a function that performs operations based on the provided parameters and returns (s string).


```go
func getPkgPrefix((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:367`



---


[function] name: isFeatureSpecType file: test/compatibility_lifecycle/cmd/feature_gates.go:428 returns_error: нет description: —


### isFeatureSpecType (test/compatibility_lifecycle/cmd/feature_gates.go:428)


isFeatureSpecType is a function that performs operations based on the provided parameters and returns (v ast.Expr, aliasMap map[string]string).


```go
func isFeatureSpecType((v ast.Expr, aliasMap map[string]string)) (v ast.Expr, aliasMap map[string]string)
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


**Тип ответа:** ast.Expr


```json
{
  "FieldRef": "string",
  "Warning": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/admissionregistration/v1alpha1/expressionwarning.go`


**Тип ответа:** aliasMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:428`



---


[function] name: parseFeatureInfo file: test/compatibility_lifecycle/cmd/feature_gates.go:437 returns_error: да description: —


### parseFeatureInfo (test/compatibility_lifecycle/cmd/feature_gates.go:437)


parseFeatureInfo is a function that performs operations based on the provided parameters and may return an error.


```go
func parseFeatureInfo((featureInfo, error)) (featureInfo, error)
```


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `featureInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:437`



---


[function] name: parseFeatureSpec file: test/compatibility_lifecycle/cmd/feature_gates.go:470 returns_error: да description: —


### parseFeatureSpec (test/compatibility_lifecycle/cmd/feature_gates.go:470)


parseFeatureSpec is a function that performs operations based on the provided parameters and may return an error.


```go
func parseFeatureSpec((featureSpec, error)) (featureSpec, error)
```


**Тип ответа:** featureSpec


```json
{
  "Default": false,
  "LockToDefault": false,
  "PreRelease": "string",
  "Version": "string"
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `featureSpec`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:470`



---


[function] name: parseVersion file: test/compatibility_lifecycle/cmd/feature_gates.go:514 returns_error: да description: —


### parseVersion (test/compatibility_lifecycle/cmd/feature_gates.go:514)


parseVersion is a function that performs operations based on the provided parameters and may return an error.


```go
func parseVersion((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:514`



---


[function] name: searchPathForFeatures file: test/compatibility_lifecycle/cmd/feature_gates.go:280 returns_error: да description: —


### searchPathForFeatures (test/compatibility_lifecycle/cmd/feature_gates.go:280)


searchPathForFeatures is a function that performs operations based on the provided parameters and may return an error.


```go
func searchPathForFeatures(([]featureInfo, error)) ([]featureInfo, error)
```


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]featureInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:280`



---


[function] name: updateFeatureListFunc file: test/compatibility_lifecycle/cmd/feature_gates.go:112 returns_error: нет description: —


### updateFeatureListFunc (test/compatibility_lifecycle/cmd/feature_gates.go:112)


updateFeatureListFunc is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func updateFeatureListFunc((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** cmd


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:112`



---


[function] name: verifyAlphaFeatures file: test/compatibility_lifecycle/cmd/feature_gates.go:269 returns_error: нет description: —


### verifyAlphaFeatures (test/compatibility_lifecycle/cmd/feature_gates.go:269)


verifyAlphaFeatures is a function that performs operations based on the provided parameters and returns (featureList []featureInfo).


```go
func verifyAlphaFeatures((featureList []featureInfo)) (featureList []featureInfo)
```


**Тип ответа:** featureList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:269`



---


[function] name: verifyAlphabeticOrder file: test/compatibility_lifecycle/cmd/feature_gates.go:374 returns_error: нет description: —


### verifyAlphabeticOrder (test/compatibility_lifecycle/cmd/feature_gates.go:374)


verifyAlphabeticOrder is a function that performs operations based on the provided parameters and returns (keys []string, path string).


```go
func verifyAlphabeticOrder((keys []string, path string)) (keys []string, path string)
```


**Тип ответа:** keys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** path


```json
{
  "muxName": "string",
  "pathToHandler": {},
  "prefixHandlers": [],
  "notFoundHandler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:374`



---


[function] name: verifyFeatureListFunc file: test/compatibility_lifecycle/cmd/feature_gates.go:104 returns_error: нет description: —


### verifyFeatureListFunc (test/compatibility_lifecycle/cmd/feature_gates.go:104)


verifyFeatureListFunc is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func verifyFeatureListFunc((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** cmd


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:104`



---


[function] name: verifyFeatureRemoval file: test/compatibility_lifecycle/cmd/feature_gates.go:213 returns_error: нет description: verifyFeatureRemoval checks if removed features are allowed to be removed based on their lifecycle.
Alpha features can b


### verifyFeatureRemoval (test/compatibility_lifecycle/cmd/feature_gates.go:213)


verifyFeatureRemoval checks if removed features are allowed to be removed based on their lifecycle.
Alpha features can be removed anytime without error.
Returns error if:
- Beta features are removed (not allowed)
- GA/Deprecated features are removed without being locked to default
- GA/Deprecated features locked after v1.31 are removed before 3 minor versions
have passed (required for emulation support)


```go
func verifyFeatureRemoval((featureList []featureInfo, baseFeatureList []featureInfo,
	currentVersion *version.Version, thresholdVersion *version.Version)) (featureList []featureInfo, baseFeatureList []featureInfo,
	currentVersion *version.Version, thresholdVersion *version.Version)
```


**Тип запроса:** version.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип запроса:** version.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** featureList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Тип ответа:** baseFeatureList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Тип ответа:** currentVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** version.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** thresholdVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** version.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:213`



---


[function] name: verifyOrUpdateFeatureList file: test/compatibility_lifecycle/cmd/feature_gates.go:123 returns_error: нет description: verifyOrUpdateFeatureList walks all the files under pkg/ and staging/ to find the list of all the features in
map[featur


### verifyOrUpdateFeatureList (test/compatibility_lifecycle/cmd/feature_gates.go:123)


verifyOrUpdateFeatureList walks all the files under pkg/ and staging/ to find the list of all the features in
map[featuregate.Feature]featuregate.VersionedSpecs.
It will then update the feature list in featureListFile, or verifies there is no change from the existing list.


```go
func verifyOrUpdateFeatureList((rootPath, featureListFile string, currentVersion *version.Version, update bool)) (rootPath, featureListFile string, currentVersion *version.Version, update bool)
```


**Тип запроса:** version.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** rootPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featureListFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** currentVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** version.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** update


```json
{
  "oldObj": {},
  "newObj": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/shared_informer.go`


📍 *Расположение:* `test/compatibility_lifecycle/cmd/feature_gates.go:123`




## test/compatibility_lifecycle/cmd/root.go


📄 Исходный файл: `test/compatibility_lifecycle/cmd/root.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Execute](#execute-testcompatibility_lifecyclecmdrootgo31) `:31`

- 🔗 [init](#init-testcompatibility_lifecyclecmdrootgo38) `:38`


</details>


[function] name: Execute file: test/compatibility_lifecycle/cmd/root.go:31 returns_error: нет description: —


### Execute (test/compatibility_lifecycle/cmd/root.go:31)


Execute is a function that performs operations based on the provided parameters and returns ().


```go
func Execute(()) ()
```


📍 *Расположение:* `test/compatibility_lifecycle/cmd/root.go:31`



---


[function] name: init file: test/compatibility_lifecycle/cmd/root.go:38 returns_error: нет description: —


### init (test/compatibility_lifecycle/cmd/root.go:38)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/compatibility_lifecycle/cmd/root.go:38`




## test/compatibility_lifecycle/cmd/util.go


📄 Исходный файл: `test/compatibility_lifecycle/cmd/util.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [basicIntLiteral](#basicintliteral-testcompatibility_lifecyclecmdutilgo88) `:88`

- 🔗 [basicStringLiteral](#basicstringliteral-testcompatibility_lifecyclecmdutilgo76) `:76`

- 🔗 [findGOOS](#findgoos-testcompatibility_lifecyclecmdutilgo33) `:33`

- 🔗 [globalVariableDeclarations](#globalvariabledeclarations-testcompatibility_lifecyclecmdutilgo119) `:119`

- 🔗 [identifierName](#identifiername-testcompatibility_lifecyclecmdutilgo47) `:47`

- 🔗 [importAliasMap](#importaliasmap-testcompatibility_lifecyclecmdutilgo61) `:61`

- 🔗 [parseBool](#parsebool-testcompatibility_lifecyclecmdutilgo104) `:104`


</details>


[function] name: basicIntLiteral file: test/compatibility_lifecycle/cmd/util.go:88 returns_error: да description: —


### basicIntLiteral (test/compatibility_lifecycle/cmd/util.go:88)


basicIntLiteral is a function that performs operations based on the provided parameters and may return an error.


```go
func basicIntLiteral((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/util.go:88`



---


[function] name: basicStringLiteral file: test/compatibility_lifecycle/cmd/util.go:76 returns_error: да description: —


### basicStringLiteral (test/compatibility_lifecycle/cmd/util.go:76)


basicStringLiteral is a function that performs operations based on the provided parameters and may return an error.


```go
func basicStringLiteral((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/util.go:76`



---


[function] name: findGOOS file: test/compatibility_lifecycle/cmd/util.go:33 returns_error: нет description: —


### findGOOS (test/compatibility_lifecycle/cmd/util.go:33)


findGOOS is a function that performs operations based on the provided parameters and returns ().


```go
func findGOOS(()) ()
```


📍 *Расположение:* `test/compatibility_lifecycle/cmd/util.go:33`



---


[function] name: globalVariableDeclarations file: test/compatibility_lifecycle/cmd/util.go:119 returns_error: нет description: —


### globalVariableDeclarations (test/compatibility_lifecycle/cmd/util.go:119)


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


📍 *Расположение:* `test/compatibility_lifecycle/cmd/util.go:119`



---


[function] name: identifierName file: test/compatibility_lifecycle/cmd/util.go:47 returns_error: нет description: identifierName returns the name of an identifier.
if ignorePkg, only return the last part of the identifierName.


### identifierName (test/compatibility_lifecycle/cmd/util.go:47)


identifierName returns the name of an identifier.
if ignorePkg, only return the last part of the identifierName.


```go
func identifierName((v ast.Expr, ignorePkg bool)) (v ast.Expr, ignorePkg bool)
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


**Тип ответа:** ast.Expr


```json
{
  "FieldRef": "string",
  "Warning": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/admissionregistration/v1alpha1/expressionwarning.go`


**Тип ответа:** ignorePkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/compatibility_lifecycle/cmd/util.go:47`



---


[function] name: importAliasMap file: test/compatibility_lifecycle/cmd/util.go:61 returns_error: нет description: importAliasMap returns the mapping from pkg path to import alias.


### importAliasMap (test/compatibility_lifecycle/cmd/util.go:61)


importAliasMap returns the mapping from pkg path to import alias.


```go
func importAliasMap((imports []*ast.ImportSpec)) (imports []*ast.ImportSpec)
```


**Тип запроса:** ast.ImportSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** imports


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ast.ImportSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/compatibility_lifecycle/cmd/util.go:61`



---


[function] name: parseBool file: test/compatibility_lifecycle/cmd/util.go:104 returns_error: да description: —


### parseBool (test/compatibility_lifecycle/cmd/util.go:104)


parseBool is a function that performs operations based on the provided parameters and may return an error.


```go
func parseBool((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/compatibility_lifecycle/cmd/util.go:104`




## test/compatibility_lifecycle/main.go


📄 Исходный файл: `test/compatibility_lifecycle/main.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testcompatibility_lifecyclemaingo21) `:21`


</details>


[function] name: main file: test/compatibility_lifecycle/main.go:21 returns_error: нет description: —


### main (test/compatibility_lifecycle/main.go:21)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/compatibility_lifecycle/main.go:21`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](staging_src.md)

- [Следующая директория](test_conformance.md)


---

