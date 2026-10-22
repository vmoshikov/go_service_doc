---
title: "Функции: hack/tools"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: hack/tools
---


# Функции: hack/tools


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](hack_conformance.md)

- [Следующая директория](pkg_api.md)


---


## Меню по файлам


- 📄 [hack/tools/golangci-lint/sorted/main.go](#hacktoolsgolangci-lintsortedmaingo)

- 📄 [hack/tools/golangci-lint/sorted/pkg/sorted.go](#hacktoolsgolangci-lintsortedpkgsortedgo)

- 📄 [hack/tools/golangci-lint/sorted/plugin/plugin.go](#hacktoolsgolangci-lintsortedpluginplugingo)

- 📄 [hack/tools/publishing-verifier/publishing-verifier.go](#hacktoolspublishing-verifierpublishing-verifiergo)


---


## hack/tools/golangci-lint/sorted/main.go


📄 Исходный файл: `hack/tools/golangci-lint/sorted/main.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-hacktoolsgolangci-lintsortedmaingo25) `:25`


</details>


[function] name: main file: hack/tools/golangci-lint/sorted/main.go:25 returns_error: нет description: —


### main (hack/tools/golangci-lint/sorted/main.go:25)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `hack/tools/golangci-lint/sorted/main.go:25`




## hack/tools/golangci-lint/sorted/pkg/sorted.go


📄 Исходный файл: `hack/tools/golangci-lint/sorted/pkg/sorted.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [NewAnalyzer](#newanalyzer-hacktoolsgolangci-lintsortedpkgsortedgo41) `:41`

- 🔗 [NewAnalyzerWithConfig](#newanalyzerwithconfig-hacktoolsgolangci-lintsortedpkgsortedgo46) `:46`

- 🔗 [checkFeatureGateMaps](#checkfeaturegatemaps-hacktoolsgolangci-lintsortedpkgsortedgo113) `:113`

- 🔗 [extractFeatures](#extractfeatures-hacktoolsgolangci-lintsortedpkgsortedgo211) `:211`

- 🔗 [generateMapSourceCode](#generatemapsourcecode-hacktoolsgolangci-lintsortedpkgsortedgo348) `:348`

- 🔗 [generateSourceCode](#generatesourcecode-hacktoolsgolangci-lintsortedpkgsortedgo366) `:366`

- 🔗 [hasOrderChanged](#hasorderchanged-hacktoolsgolangci-lintsortedpkgsortedgo264) `:264`

- 🔗 [isTargetFile](#istargetfile-hacktoolsgolangci-lintsortedpkgsortedgo59) `:59`

- 🔗 [reportMapSortingIssue](#reportmapsortingissue-hacktoolsgolangci-lintsortedpkgsortedgo321) `:321`

- 🔗 [reportSortingIssue](#reportsortingissue-hacktoolsgolangci-lintsortedpkgsortedgo279) `:279`

- 🔗 [run](#run-hacktoolsgolangci-lintsortedpkgsortedgo68) `:68`

- 🔗 [sortFeatures](#sortfeatures-hacktoolsgolangci-lintsortedpkgsortedgo252) `:252`

- 🔗 [stripHeader](#stripheader-hacktoolsgolangci-lintsortedpkgsortedgo305) `:305`


</details>


[function] name: NewAnalyzer file: hack/tools/golangci-lint/sorted/pkg/sorted.go:41 returns_error: нет description: NewAnalyzer returns a new sorted analyzer.


### NewAnalyzer (hack/tools/golangci-lint/sorted/pkg/sorted.go:41)


NewAnalyzer returns a new sorted analyzer.


```go
func NewAnalyzer(()) ()
```


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:41`



---


[function] name: NewAnalyzerWithConfig file: hack/tools/golangci-lint/sorted/pkg/sorted.go:46 returns_error: нет description: NewAnalyzerWithConfig returns a new sorted analyzer with the given configuration.


### NewAnalyzerWithConfig (hack/tools/golangci-lint/sorted/pkg/sorted.go:46)


NewAnalyzerWithConfig returns a new sorted analyzer with the given configuration.


```go
func NewAnalyzerWithConfig((config Config)) (config Config)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:46`



---


[function] name: checkFeatureGateMaps file: hack/tools/golangci-lint/sorted/pkg/sorted.go:113 returns_error: нет description: checkFeatureGateMaps checks if maps with feature gates as keys have their keys sorted alphabetically


### checkFeatureGateMaps (hack/tools/golangci-lint/sorted/pkg/sorted.go:113)


checkFeatureGateMaps checks if maps with feature gates as keys have their keys sorted alphabetically


```go
func checkFeatureGateMaps((pass *analysis.Pass, genDecl *ast.GenDecl)) (pass *analysis.Pass, genDecl *ast.GenDecl)
```


**Тип запроса:** analysis.Pass


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


**Тип запроса:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pass


```json
{
  "logger": {},
  "gr": {},
  "rwMutex": {},
  "store": {},
  "assumed": {}
}
```


*Определено в:* `pkg/scheduler/framework/plugins/volumebinding/passive_assume_cache.go`


**Тип ответа:** analysis.Pass


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


**Тип ответа:** genDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:113`



---


[function] name: extractFeatures file: hack/tools/golangci-lint/sorted/pkg/sorted.go:211 returns_error: нет description: extractFeatures extracts features from a GenDecl


### extractFeatures (hack/tools/golangci-lint/sorted/pkg/sorted.go:211)


extractFeatures extracts features from a GenDecl


```go
func extractFeatures((decl *ast.GenDecl, comments []*ast.CommentGroup)) (decl *ast.GenDecl, comments []*ast.CommentGroup)
```


**Тип запроса:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** ast.CommentGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** decl


```json
{
  "ndfFramework": null,
  "ndfSet": {},
  "version": null
}
```


*Определено в:* `pkg/kubelet/lifecycle/handlers.go`


**Тип ответа:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comments


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ast.CommentGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:211`



---


[function] name: generateMapSourceCode file: hack/tools/golangci-lint/sorted/pkg/sorted.go:348 returns_error: нет description: generateMapSourceCode recreates the source code for map keys


### generateMapSourceCode (hack/tools/golangci-lint/sorted/pkg/sorted.go:348)


generateMapSourceCode recreates the source code for map keys


```go
func generateMapSourceCode((features []Feature)) (features []Feature)
```


**Тип ответа:** features


```json
{
  "cpuHardcapping": false
}
```


*Определено в:* `pkg/kubelet/cm/container_manager_linux.go`


**Тип ответа:** Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:348`



---


[function] name: generateSourceCode file: hack/tools/golangci-lint/sorted/pkg/sorted.go:366 returns_error: нет description: generateSourceCode recreates the source code from features


### generateSourceCode (hack/tools/golangci-lint/sorted/pkg/sorted.go:366)


generateSourceCode recreates the source code from features


```go
func generateSourceCode((tokenType token.Token, features []Feature)) (tokenType token.Token, features []Feature)
```


**Тип ответа:** tokenType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** token.Token


```json
{
  "IDToken": "string",
  "AccessToken": "string",
  "TokenType": "string",
  "RefreshToken": "string",
  "ExpiresIn": 0
}
```


*Определено в:* `test/utils/oidc/handlers/handlers.go`


**Тип ответа:** features


```json
{
  "cpuHardcapping": false
}
```


*Определено в:* `pkg/kubelet/cm/container_manager_linux.go`


**Тип ответа:** Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:366`



---


[function] name: hasOrderChanged file: hack/tools/golangci-lint/sorted/pkg/sorted.go:264 returns_error: нет description: hasOrderChanged checks if the order of features has changed


### hasOrderChanged (hack/tools/golangci-lint/sorted/pkg/sorted.go:264)


hasOrderChanged checks if the order of features has changed


```go
func hasOrderChanged((original, sorted []Feature)) (original, sorted []Feature)
```


**Тип ответа:** original


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sorted


```json
{
  "nodes": {}
}
```


*Определено в:* `pkg/scheduler/schedule_one.go`


**Тип ответа:** Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:264`



---


[function] name: isTargetFile file: hack/tools/golangci-lint/sorted/pkg/sorted.go:59 returns_error: нет description: —


### isTargetFile (hack/tools/golangci-lint/sorted/pkg/sorted.go:59)


isTargetFile is a function that performs operations based on the provided parameters and returns (configFiles []string, filename string).


```go
func isTargetFile((configFiles []string, filename string)) (configFiles []string, filename string)
```


**Тип ответа:** configFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:59`



---


[function] name: reportMapSortingIssue file: hack/tools/golangci-lint/sorted/pkg/sorted.go:321 returns_error: нет description: reportMapSortingIssue reports a linting issue for unsorted map keys


### reportMapSortingIssue (hack/tools/golangci-lint/sorted/pkg/sorted.go:321)


reportMapSortingIssue reports a linting issue for unsorted map keys


```go
func reportMapSortingIssue((pass *analysis.Pass, decl *ast.GenDecl, mapName string, current, sorted []Feature)) (pass *analysis.Pass, decl *ast.GenDecl, mapName string, current, sorted []Feature)
```


**Тип запроса:** analysis.Pass


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


**Тип запроса:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pass


```json
{
  "logger": {},
  "gr": {},
  "rwMutex": {},
  "store": {},
  "assumed": {}
}
```


*Определено в:* `pkg/scheduler/framework/plugins/volumebinding/passive_assume_cache.go`


**Тип ответа:** analysis.Pass


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


**Тип ответа:** decl


```json
{
  "ndfFramework": null,
  "ndfSet": {},
  "version": null
}
```


*Определено в:* `pkg/kubelet/lifecycle/handlers.go`


**Тип ответа:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mapName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** current


```json
{
  "visitors": [],
  "concurrency": 0
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/visitor.go`


**Тип ответа:** sorted


```json
{
  "nodes": {}
}
```


*Определено в:* `pkg/scheduler/schedule_one.go`


**Тип ответа:** Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:321`



---


[function] name: reportSortingIssue file: hack/tools/golangci-lint/sorted/pkg/sorted.go:279 returns_error: нет description: reportSortingIssue reports a linting issue with a diff showing the correct order


### reportSortingIssue (hack/tools/golangci-lint/sorted/pkg/sorted.go:279)


reportSortingIssue reports a linting issue with a diff showing the correct order


```go
func reportSortingIssue((pass *analysis.Pass, decl *ast.GenDecl, current, sorted []Feature)) (pass *analysis.Pass, decl *ast.GenDecl, current, sorted []Feature)
```


**Тип запроса:** analysis.Pass


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


**Тип запроса:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pass


```json
{
  "logger": {},
  "gr": {},
  "rwMutex": {},
  "store": {},
  "assumed": {}
}
```


*Определено в:* `pkg/scheduler/framework/plugins/volumebinding/passive_assume_cache.go`


**Тип ответа:** analysis.Pass


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


**Тип ответа:** decl


```json
{
  "ndfFramework": null,
  "ndfSet": {},
  "version": null
}
```


*Определено в:* `pkg/kubelet/lifecycle/handlers.go`


**Тип ответа:** ast.GenDecl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** current


```json
{
  "visitors": [],
  "concurrency": 0
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/visitor.go`


**Тип ответа:** sorted


```json
{
  "nodes": {}
}
```


*Определено в:* `pkg/scheduler/schedule_one.go`


**Тип ответа:** Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:279`



---


[function] name: run file: hack/tools/golangci-lint/sorted/pkg/sorted.go:68 returns_error: да description: —


### run (hack/tools/golangci-lint/sorted/pkg/sorted.go:68)


run is a function that performs operations based on the provided parameters and may return an error.


```go
func run((interface{}, error)) (interface{}, error)
```


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `interface{}`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:68`



---


[function] name: sortFeatures file: hack/tools/golangci-lint/sorted/pkg/sorted.go:252 returns_error: нет description: sortFeatures sorts features alphabetically by name


### sortFeatures (hack/tools/golangci-lint/sorted/pkg/sorted.go:252)


sortFeatures sorts features alphabetically by name


```go
func sortFeatures((features []Feature)) (features []Feature)
```


**Тип ответа:** features


```json
{
  "cpuHardcapping": false
}
```


*Определено в:* `pkg/kubelet/cm/container_manager_linux.go`


**Тип ответа:** Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:252`



---


[function] name: stripHeader file: hack/tools/golangci-lint/sorted/pkg/sorted.go:305 returns_error: нет description: —


### stripHeader (hack/tools/golangci-lint/sorted/pkg/sorted.go:305)


stripHeader is a function that performs operations based on the provided parameters and returns (input string, n int).


```go
func stripHeader((input string, n int)) (input string, n int)
```


**Тип ответа:** input


```json
{
  "builder": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/client-gen/args/gvpackages.go`


**Тип ответа:** n


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `hack/tools/golangci-lint/sorted/pkg/sorted.go:305`




## hack/tools/golangci-lint/sorted/plugin/plugin.go


📄 Исходный файл: `hack/tools/golangci-lint/sorted/plugin/plugin.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetAnalyzers](#getanalyzers-hacktoolsgolangci-lintsortedpluginplugingo31) `:31`

- 🔗 [New](#new-hacktoolsgolangci-lintsortedpluginplugingo58) `:58`


</details>


[function] name: GetAnalyzers file: hack/tools/golangci-lint/sorted/plugin/plugin.go:31 returns_error: нет description: —


### GetAnalyzers (hack/tools/golangci-lint/sorted/plugin/plugin.go:31)


GetAnalyzers is a method that retrieves data based on the provided parameters and returns ().


```go
func (*analyzerPlugin) GetAnalyzers(()) ()
```


📍 *Расположение:* `hack/tools/golangci-lint/sorted/plugin/plugin.go:31`



---


[function] name: New file: hack/tools/golangci-lint/sorted/plugin/plugin.go:58 returns_error: да description: New is the entry point for golangci-lint plugin system


### New (hack/tools/golangci-lint/sorted/plugin/plugin.go:58)


New is the entry point for golangci-lint plugin system


```go
func New(([]*analysis.Analyzer, error)) ([]*analysis.Analyzer, error)
```


**Тип запроса:** analysis.Analyzer


```json
{
  "statsProvider": {},
  "calcPeriod": {},
  "cachedVolumeStats": {},
  "startOnce": {},
  "eventRecorder": {}
}
```


*Определено в:* `pkg/kubelet/server/stats/fs_resource_analyzer.go`


**Тип ответа:** analysis.Analyzer


```json
{
  "statsProvider": {},
  "calcPeriod": {},
  "cachedVolumeStats": {},
  "startOnce": {},
  "eventRecorder": {}
}
```


*Определено в:* `pkg/kubelet/server/stats/fs_resource_analyzer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*analysis.Analyzer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `hack/tools/golangci-lint/sorted/plugin/plugin.go:58`




## hack/tools/publishing-verifier/publishing-verifier.go


📄 Исходный файл: `hack/tools/publishing-verifier/publishing-verifier.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [checkDependencies](#checkdependencies-hacktoolspublishing-verifierpublishing-verifiergo134) `:134`

- 🔗 [checkMasterBranch](#checkmasterbranch-hacktoolspublishing-verifierpublishing-verifiergo122) `:122`

- 🔗 [checkValidSourceDirectory](#checkvalidsourcedirectory-hacktoolspublishing-verifierpublishing-verifiergo101) `:101`

- 🔗 [diffSlice](#diffslice-hacktoolspublishing-verifierpublishing-verifiergo77) `:77`

- 🔗 [getGoModDependencies](#getgomoddependencies-hacktoolspublishing-verifierpublishing-verifiergo36) `:36`

- 🔗 [getKeys](#getkeys-hacktoolspublishing-verifierpublishing-verifiergo92) `:92`

- 🔗 [main](#main-hacktoolspublishing-verifierpublishing-verifiergo227) `:227`

- 🔗 [verifyPublishingBotRules](#verifypublishingbotrules-hacktoolspublishing-verifierpublishing-verifiergo166) `:166`


</details>


[function] name: checkDependencies file: hack/tools/publishing-verifier/publishing-verifier.go:134 returns_error: нет description: —


### checkDependencies (hack/tools/publishing-verifier/publishing-verifier.go:134)


checkDependencies is a function that performs operations based on the provided parameters and returns (rule config.RepositoryRule, gomodDependencies map[string][]string).


```go
func checkDependencies((rule config.RepositoryRule, gomodDependencies map[string][]string)) (rule config.RepositoryRule, gomodDependencies map[string][]string)
```


**Тип ответа:** rule


```json
{
  "rules": [],
  "errors": []
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Тип ответа:** config.RepositoryRule


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gomodDependencies


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:134`



---


[function] name: checkMasterBranch file: hack/tools/publishing-verifier/publishing-verifier.go:122 returns_error: нет description: checkMasterBranch checks if the master branch of destination repository refers to the master
of the source


### checkMasterBranch (hack/tools/publishing-verifier/publishing-verifier.go:122)


checkMasterBranch checks if the master branch of destination repository refers to the master
of the source


```go
func checkMasterBranch((rule config.RepositoryRule)) (rule config.RepositoryRule)
```


**Тип ответа:** rule


```json
{
  "rules": [],
  "errors": []
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Тип ответа:** config.RepositoryRule


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:122`



---


[function] name: checkValidSourceDirectory file: hack/tools/publishing-verifier/publishing-verifier.go:101 returns_error: нет description: checkValidSourceDirectory checks if proper source directory fields are used in rules


### checkValidSourceDirectory (hack/tools/publishing-verifier/publishing-verifier.go:101)


checkValidSourceDirectory checks if proper source directory fields are used in rules


```go
func checkValidSourceDirectory((rule config.RepositoryRule)) (rule config.RepositoryRule)
```


**Тип ответа:** rule


```json
{
  "rules": [],
  "errors": []
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Тип ответа:** config.RepositoryRule


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:101`



---


[function] name: diffSlice file: hack/tools/publishing-verifier/publishing-verifier.go:77 returns_error: нет description: diffSlice returns the difference of s1-s2


### diffSlice (hack/tools/publishing-verifier/publishing-verifier.go:77)


diffSlice returns the difference of s1-s2


```go
func diffSlice((s1, s2 []string)) (s1, s2 []string)
```


**Тип ответа:** s1


```json
{
  "keyID": "string",
  "aead": {}
}
```


*Определено в:* `staging/src/k8s.io/kms/internal/plugins/_mock/pkcs11/pkcs11.go`


**Тип ответа:** s2


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:77`



---


[function] name: getGoModDependencies file: hack/tools/publishing-verifier/publishing-verifier.go:36 returns_error: да description: getGoModDependencies gets all the staging dependencies for all the modules
in the given directory


### getGoModDependencies (hack/tools/publishing-verifier/publishing-verifier.go:36)


getGoModDependencies gets all the staging dependencies for all the modules
in the given directory


```go
func getGoModDependencies((map[string][]string, error)) (map[string][]string, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string][]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:36`



---


[function] name: getKeys file: hack/tools/publishing-verifier/publishing-verifier.go:92 returns_error: нет description: getKeys returns a slice with only the keys of the given map


### getKeys (hack/tools/publishing-verifier/publishing-verifier.go:92)


getKeys returns a slice with only the keys of the given map


```go
func getKeys((m map[K]V)) (m map[K]V)
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


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** K


```json
{
  "Generic": null,
  "KubeCloudShared": null,
  "ServiceController": null,
  "AttachDetachController": null,
  "CSRSigningController": null,
  "DaemonSetController": null,
  "DeploymentController": null,
  "DeviceTaintEvictionController": null,
  "ResourceClaimController": null,
  "StatefulSetController": null,
  "DeprecatedFlags": null,
  "EndpointController": null,
  "EndpointSliceController": null,
  "EndpointSliceMirroringController": null,
  "EphemeralVolumeController": null,
  "GarbageCollectorController": null,
  "HPAController": null,
  "JobController": null,
  "CronJobController": null,
  "LegacySATokenCleaner": null,
  "NamespaceController": null,
  "NodeIPAMController": null,
  "NodeLifecycleController": null,
  "PersistentVolumeBinderController": null,
  "PodGCController": null,
  "ReplicaSetController": null,
  "ReplicationController": null,
  "ResourceQuotaController": null,
  "SAController": null,
  "TTLAfterFinishedController": null,
  "ValidatingAdmissionPolicyStatusController": null,
  "SecureServing": null,
  "Authentication": null,
  "Authorization": null,
  "Metrics": null,
  "Logs": null,
  "Master": "string",
  "ShowHiddenMetricsForVersion": "string",
  "ControllerShutdownTimeout": {},
  "ComponentGlobalsRegistry": {},
  "ParsedFlags": null
}
```


*Определено в:* `cmd/kube-controller-manager/app/options/options.go`


**Тип ответа:** V


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:92`



---


[function] name: main file: hack/tools/publishing-verifier/publishing-verifier.go:227 returns_error: нет description: —


### main (hack/tools/publishing-verifier/publishing-verifier.go:227)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:227`



---


[function] name: verifyPublishingBotRules file: hack/tools/publishing-verifier/publishing-verifier.go:166 returns_error: нет description: —


### verifyPublishingBotRules (hack/tools/publishing-verifier/publishing-verifier.go:166)


verifyPublishingBotRules is a function that performs operations based on the provided parameters and returns ().


```go
func verifyPublishingBotRules(()) ()
```


📍 *Расположение:* `hack/tools/publishing-verifier/publishing-verifier.go:166`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](hack_conformance.md)

- [Следующая директория](pkg_api.md)


---

