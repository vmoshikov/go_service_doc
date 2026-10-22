---
title: "Функции: cmd/dependencyverifier"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/dependencyverifier
---


# Функции: cmd/dependencyverifier


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_dependencycheck.md)

- [Следующая директория](cmd_fieldnamedocscheck.md)


---


## Меню по файлам


- 📄 [cmd/dependencyverifier/dependencyverifier.go](#cmddependencyverifierdependencyverifiergo)


---


## cmd/dependencyverifier/dependencyverifier.go


📄 Исходный файл: `cmd/dependencyverifier/dependencyverifier.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [String](#string-cmddependencyverifierdependencyverifiergo156) `:156`

- 🔗 [convertToMap](#converttomap-cmddependencyverifierdependencyverifiergo94) `:94`

- 🔗 [difference](#difference-cmddependencyverifierdependencyverifiergo125) `:125`

- 🔗 [doVisit](#dovisit-cmddependencyverifierdependencyverifiergo412) `:412`

- 🔗 [main](#main-cmddependencyverifierdependencyverifiergo173) `:173`

- 🔗 [moduleInSlice](#moduleinslice-cmddependencyverifierdependencyverifiergo81) `:81`

- 🔗 [parseModule](#parsemodule-cmddependencyverifierdependencyverifiergo163) `:163`

- 🔗 [readFile](#readfile-cmddependencyverifierdependencyverifiergo75) `:75`

- 🔗 [runCommand](#runcommand-cmddependencyverifierdependencyverifiergo61) `:61`

- 🔗 [runCommandInDir](#runcommandindir-cmddependencyverifierdependencyverifiergo65) `:65`

- 🔗 [visit](#visit-cmddependencyverifierdependencyverifiergo408) `:408`


</details>


[function] name: String file: cmd/dependencyverifier/dependencyverifier.go:156 returns_error: нет description: —


### String (cmd/dependencyverifier/dependencyverifier.go:156)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (m module) String(()) ()
```


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:156`



---


[function] name: convertToMap file: cmd/dependencyverifier/dependencyverifier.go:94 returns_error: нет description: converts `go mod graph` output modStr into a map of from->[]to references and the main module


### convertToMap (cmd/dependencyverifier/dependencyverifier.go:94)


converts `go mod graph` output modStr into a map of from->[]to references and the main module


```go
func convertToMap(([]module, map[module][]module)) ([]module, map[module][]module)
```


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:94`



---


[function] name: difference file: cmd/dependencyverifier/dependencyverifier.go:125 returns_error: нет description: difference returns a-b and b-a as sorted lists


### difference (cmd/dependencyverifier/dependencyverifier.go:125)


difference returns a-b and b-a as sorted lists


```go
func difference(([]string, []string)) ([]string, []string)
```


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:125`



---


[function] name: doVisit file: cmd/dependencyverifier/dependencyverifier.go:412 returns_error: нет description: —


### doVisit (cmd/dependencyverifier/dependencyverifier.go:412)


doVisit is a function that performs operations based on the provided parameters and returns (visitor func(m module, via []module), from module, via []module, visited map[module]bool, references map[module][]module, effectiveVersions map[string]module).


```go
func doVisit((visitor func(m module, via []module), from module, via []module, visited map[module]bool, references map[module][]module, effectiveVersions map[string]module)) (visitor func(m module, via []module), from module, via []module, visited map[module]bool, references map[module][]module, effectiveVersions map[string]module)
```


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** via


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** from


```json
{
  "isInlined": false,
  "matchedKeys": [],
  "parentPath": [],
  "returnUnknownFields": false,
  "unknownFieldErrors": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/converter.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** via


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** visited


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** references


```json
{
  "getPreferencesFunc": {},
  "aliases": {},
  "policy": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/kuberc/kuberc.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** effectiveVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:412`



---


[function] name: main file: cmd/dependencyverifier/dependencyverifier.go:173 returns_error: нет description: option1: dependencyverifier dependencies.json
it will run `go mod graph` and check it.


### main (cmd/dependencyverifier/dependencyverifier.go:173)


option1: dependencyverifier dependencies.json
it will run `go mod graph` and check it.


```go
func main(()) ()
```


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:173`



---


[function] name: moduleInSlice file: cmd/dependencyverifier/dependencyverifier.go:81 returns_error: нет description: —


### moduleInSlice (cmd/dependencyverifier/dependencyverifier.go:81)


moduleInSlice is a function that performs operations based on the provided parameters and returns (a module, list []module, matchVersion bool).


```go
func moduleInSlice((a module, list []module, matchVersion bool)) (a module, list []module, matchVersion bool)
```


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


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** list


```json
{
  "parent": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/listwatch.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** matchVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:81`



---


[function] name: parseModule file: cmd/dependencyverifier/dependencyverifier.go:163 returns_error: нет description: —


### parseModule (cmd/dependencyverifier/dependencyverifier.go:163)


parseModule is a function that performs operations based on the provided parameters and returns (s string).


```go
func parseModule((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:163`



---


[function] name: readFile file: cmd/dependencyverifier/dependencyverifier.go:75 returns_error: да description: —


### readFile (cmd/dependencyverifier/dependencyverifier.go:75)


readFile is a function that performs operations based on the provided parameters and may return an error.


```go
func readFile((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:75`



---


[function] name: runCommand file: cmd/dependencyverifier/dependencyverifier.go:61 returns_error: да description: runCommand runs the cmd and returns the combined stdout and stderr, or an
error if the command failed.


### runCommand (cmd/dependencyverifier/dependencyverifier.go:61)


runCommand runs the cmd and returns the combined stdout and stderr, or an
error if the command failed.


```go
func runCommand((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:61`



---


[function] name: runCommandInDir file: cmd/dependencyverifier/dependencyverifier.go:65 returns_error: да description: —


### runCommandInDir (cmd/dependencyverifier/dependencyverifier.go:65)


runCommandInDir is a function that performs operations based on the provided parameters and may return an error.


```go
func runCommandInDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:65`



---


[function] name: visit file: cmd/dependencyverifier/dependencyverifier.go:408 returns_error: нет description: —


### visit (cmd/dependencyverifier/dependencyverifier.go:408)


visit is a function that performs operations based on the provided parameters and returns (visitor func(m module, via []module), main module, references map[module][]module, effectiveVersions map[string]module).


```go
func visit((visitor func(m module, via []module), main module, references map[module][]module, effectiveVersions map[string]module)) (visitor func(m module, via []module), main module, references map[module][]module, effectiveVersions map[string]module)
```


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** via


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** main


```json
{
  "Estimate": 0
}
```


*Определено в:* `pkg/controller/namespace/deletion/namespaced_resources_deleter.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** references


```json
{
  "getPreferencesFunc": {},
  "aliases": {},
  "policy": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/kuberc/kuberc.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


**Тип ответа:** effectiveVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** module


```json
{
  "name": "string",
  "version": "string"
}
```


*Определено в:* `cmd/dependencyverifier/dependencyverifier.go`


📍 *Расположение:* `cmd/dependencyverifier/dependencyverifier.go:408`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_dependencycheck.md)

- [Следующая директория](cmd_fieldnamedocscheck.md)


---

