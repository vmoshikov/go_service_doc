---
title: "Функции: cmd/genfeaturegates"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/genfeaturegates
---


# Функции: cmd/genfeaturegates


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_gendocs.md)

- [Следующая директория](cmd_genkubedocs.md)


---


## Меню по файлам


- 📄 [cmd/genfeaturegates/genfeaturegates.go](#cmdgenfeaturegatesgenfeaturegatesgo)


---


## cmd/genfeaturegates/genfeaturegates.go


📄 Исходный файл: `cmd/genfeaturegates/genfeaturegates.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [compareVersions](#compareversions-cmdgenfeaturegatesgenfeaturegatesgo584) `:584`

- 🔗 [deduplicateStages](#deduplicatestages-cmdgenfeaturegatesgenfeaturegatesgo269) `:269`

- 🔗 [formatEnabledColumn](#formatenabledcolumn-cmdgenfeaturegatesgenfeaturegatesgo501) `:501`

- 🔗 [formatLockedColumn](#formatlockedcolumn-cmdgenfeaturegatesgenfeaturegatesgo509) `:509`

- 🔗 [formatStageRanges](#formatstageranges-cmdgenfeaturegatesgenfeaturegatesgo518) `:518`

- 🔗 [generateJSON](#generatejson-cmdgenfeaturegatesgenfeaturegatesgo132) `:132`

- 🔗 [generateMarkdown](#generatemarkdown-cmdgenfeaturegatesgenfeaturegatesgo295) `:295`

- 🔗 [getPreviousMinorVersion](#getpreviousminorversion-cmdgenfeaturegatesgenfeaturegatesgo254) `:254`

- 🔗 [main](#main-cmdgenfeaturegatesgenfeaturegatesgo87) `:87`

- 🔗 [sortFeatures](#sortfeatures-cmdgenfeaturegatesgenfeaturegatesgo541) `:541`


</details>


[function] name: compareVersions file: cmd/genfeaturegates/genfeaturegates.go:584 returns_error: нет description: compareVersions compares two versions, putting nil versions last


### compareVersions (cmd/genfeaturegates/genfeaturegates.go:584)


compareVersions compares two versions, putting nil versions last


```go
func compareVersions((v1, v2 *version.Version, name1, name2 string)) (v1, v2 *version.Version, name1, name2 string)
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


**Тип ответа:** v1


```json
{
  "podsProvider": {},
  "devicesProvider": {}
}
```


*Определено в:* `pkg/kubelet/apis/podresources/server_v1alpha1.go`


**Тип ответа:** v2


```json
{
  "state": {},
  "name": "string",
  "ttl": {},
  "service": {},
  "lastResponse": null,
  "l": null,
  "apiServerID": "string",
  "version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/options/encryptionconfig/config.go`


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


**Тип ответа:** name1


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** name2


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:584`



---


[function] name: deduplicateStages file: cmd/genfeaturegates/genfeaturegates.go:269 returns_error: нет description: deduplicateStages merges consecutive entries with the same stage, default, and locked values.
If defaultValue or locked 


### deduplicateStages (cmd/genfeaturegates/genfeaturegates.go:269)


deduplicateStages merges consecutive entries with the same stage, default, and locked values.
If defaultValue or locked changes within the same stage, we keep separate entries to preserve
the full lifecycle history (e.g., beta disabled in 1.23, beta enabled in 1.24).


```go
func deduplicateStages((stages []StageJSON)) (stages []StageJSON)
```


**Тип ответа:** stages


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** StageJSON


```json
{
  "Stage": "string",
  "FromVersion": "string",
  "ToVersion": "string",
  "Default": false,
  "Locked": false
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:269`



---


[function] name: formatEnabledColumn file: cmd/genfeaturegates/genfeaturegates.go:501 returns_error: нет description: formatEnabledColumn formats the Enabled column showing when a feature was first enabled by default


### formatEnabledColumn (cmd/genfeaturegates/genfeaturegates.go:501)


formatEnabledColumn formats the Enabled column showing when a feature was first enabled by default


```go
func formatEnabledColumn((enabledFromVersion string)) (enabledFromVersion string)
```


**Тип ответа:** enabledFromVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:501`



---


[function] name: formatLockedColumn file: cmd/genfeaturegates/genfeaturegates.go:509 returns_error: нет description: formatLockedColumn formats the Locked column showing when a feature was first locked


### formatLockedColumn (cmd/genfeaturegates/genfeaturegates.go:509)


formatLockedColumn formats the Locked column showing when a feature was first locked


```go
func formatLockedColumn((lockedFromVersion string)) (lockedFromVersion string)
```


**Тип ответа:** lockedFromVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:509`



---


[function] name: formatStageRanges file: cmd/genfeaturegates/genfeaturegates.go:518 returns_error: нет description: formatStageRanges formats a list of stage ranges for markdown display
Each range shows "fromVersion–toVersion" (with en-


### formatStageRanges (cmd/genfeaturegates/genfeaturegates.go:518)


formatStageRanges formats a list of stage ranges for markdown display
Each range shows "fromVersion–toVersion" (with en-dash) or "fromVersion–" for open-ended ranges


```go
func formatStageRanges((stages []stageInfo)) (stages []stageInfo)
```


**Тип ответа:** stages


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stageInfo


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:518`



---


[function] name: generateJSON file: cmd/genfeaturegates/genfeaturegates.go:132 returns_error: нет description: —


### generateJSON (cmd/genfeaturegates/genfeaturegates.go:132)


generateJSON is a function that performs operations based on the provided parameters and returns (filterStage string).


```go
func generateJSON((filterStage string)) (filterStage string)
```


**Тип ответа:** filterStage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:132`



---


[function] name: generateMarkdown file: cmd/genfeaturegates/genfeaturegates.go:295 returns_error: нет description: —


### generateMarkdown (cmd/genfeaturegates/genfeaturegates.go:295)


generateMarkdown is a function that performs operations based on the provided parameters and returns (sortBy string, reverseSort bool, filterStage string).


```go
func generateMarkdown((sortBy string, reverseSort bool, filterStage string)) (sortBy string, reverseSort bool, filterStage string)
```


**Тип ответа:** sortBy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reverseSort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** filterStage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:295`



---


[function] name: getPreviousMinorVersion file: cmd/genfeaturegates/genfeaturegates.go:254 returns_error: нет description: getPreviousMinorVersion returns the previous minor version (e.g., "1.30" -> "1.29")


### getPreviousMinorVersion (cmd/genfeaturegates/genfeaturegates.go:254)


getPreviousMinorVersion returns the previous minor version (e.g., "1.30" -> "1.29")


```go
func getPreviousMinorVersion((ver string)) (ver string)
```


**Тип ответа:** ver


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


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:254`



---


[function] name: main file: cmd/genfeaturegates/genfeaturegates.go:87 returns_error: нет description: —


### main (cmd/genfeaturegates/genfeaturegates.go:87)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:87`



---


[function] name: sortFeatures file: cmd/genfeaturegates/genfeaturegates.go:541 returns_error: нет description: —


### sortFeatures (cmd/genfeaturegates/genfeaturegates.go:541)


sortFeatures is a function that performs operations based on the provided parameters and returns (features []featureInfo, sortBy string, reverseSort bool).


```go
func sortFeatures((features []featureInfo, sortBy string, reverseSort bool)) (features []featureInfo, sortBy string, reverseSort bool)
```


**Тип ответа:** features


```json
{
  "cpuHardcapping": false
}
```


*Определено в:* `pkg/kubelet/cm/container_manager_linux.go`


**Тип ответа:** featureInfo


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Тип ответа:** sortBy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reverseSort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genfeaturegates/genfeaturegates.go:541`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_gendocs.md)

- [Следующая директория](cmd_genkubedocs.md)


---

