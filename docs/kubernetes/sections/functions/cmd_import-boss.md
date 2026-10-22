---
title: "Функции: cmd/import-boss"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/import-boss
---


# Функции: cmd/import-boss


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_gotemplate.md)

- [Следующая директория](cmd_importverifier.md)


---


## Меню по файлам


- 📄 [cmd/import-boss/main.go](#cmdimport-bossmaingo)


---


## cmd/import-boss/main.go


📄 Исходный файл: `cmd/import-boss/main.go`


<details open>
<summary><b>Функции в этом файле (20)</b></summary>


- 🔗 [Evaluate](#evaluate-cmdimport-bossmaingo253) `:253`

- 🔗 [Verify](#verify-cmdimport-bossmaingo187) `:187`

- 🔗 [dfsImports](#dfsimports-cmdimport-bossmaingo450) `:450`

- 🔗 [hasPathPrefix](#haspathprefix-cmdimport-bossmaingo427) `:427`

- 🔗 [hasTestFiles](#hastestfiles-cmdimport-bossmaingo178) `:178`

- 🔗 [isGoModRoot](#isgomodroot-cmdimport-bossmaingo316) `:316`

- 🔗 [loadPkgs](#loadpkgs-cmdimport-bossmaingo82) `:82`

- 🔗 [main](#main-cmdimport-bossmaingo43) `:43`

- 🔗 [massage](#massage-cmdimport-bossmaingo116) `:116`

- 🔗 [newBoss](#newboss-cmdimport-bossmaingo160) `:160`

- 🔗 [packageDir](#packagedir-cmdimport-bossmaingo211) `:211`

- 🔗 [readFile](#readfile-cmdimport-bossmaingo299) `:299`

- 🔗 [recursiveRead](#recursiveread-cmdimport-bossmaingo275) `:275`

- 🔗 [removeLastDir](#removelastdir-cmdimport-bossmaingo324) `:324`

- 🔗 [transitiveClosure](#transitiveclosure-cmdimport-bossmaingo543) `:543`

- 🔗 [transitiveImports](#transitiveimports-cmdimport-bossmaingo439) `:439`

- 🔗 [uniq](#uniq-cmdimport-bossmaingo412) `:412`

- 🔗 [unmassage](#unmassage-cmdimport-bossmaingo143) `:143`

- 🔗 [verifyInverseRules](#verifyinverserules-cmdimport-bossmaingo462) `:462`

- 🔗 [verifyRules](#verifyrules-cmdimport-bossmaingo330) `:330`


</details>


[function] name: Evaluate file: cmd/import-boss/main.go:253 returns_error: нет description: Evaluate considers this rule and decides if this dependency is allowed.


### Evaluate (cmd/import-boss/main.go:253)


Evaluate considers this rule and decides if this dependency is allowed.


```go
func (r Rule) Evaluate((imp string)) (imp string)
```


**Тип ответа:** imp


```json
{
  "impersonate": {},
  "delegate": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


📍 *Расположение:* `cmd/import-boss/main.go:253`



---


[function] name: Verify file: cmd/import-boss/main.go:187 returns_error: нет description: —


### Verify (cmd/import-boss/main.go:187)


Verify is a method that performs operations based on the provided parameters and returns (pkg *packages.Package).


```go
func (boss *ImportBoss) Verify((pkg *packages.Package)) (pkg *packages.Package)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/import-boss/main.go:187`



---


[function] name: dfsImports file: cmd/import-boss/main.go:450 returns_error: нет description: —


### dfsImports (cmd/import-boss/main.go:450)


dfsImports is a function that performs operations based on the provided parameters and returns (dest *[]string, seen map[string]bool, p *packages.Package).


```go
func dfsImports((dest *[]string, seen map[string]bool, p *packages.Package)) (dest *[]string, seen map[string]bool, p *packages.Package)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** seen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/import-boss/main.go:450`



---


[function] name: hasPathPrefix file: cmd/import-boss/main.go:427 returns_error: нет description: —


### hasPathPrefix (cmd/import-boss/main.go:427)


hasPathPrefix is a function that performs operations based on the provided parameters and returns (path, prefix string).


```go
func hasPathPrefix((path, prefix string)) (path, prefix string)
```


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


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


📍 *Расположение:* `cmd/import-boss/main.go:427`



---


[function] name: hasTestFiles file: cmd/import-boss/main.go:178 returns_error: нет description: —


### hasTestFiles (cmd/import-boss/main.go:178)


hasTestFiles is a function that performs operations based on the provided parameters and returns (files []string).


```go
func hasTestFiles((files []string)) (files []string)
```


**Тип ответа:** files


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/import-boss/main.go:178`



---


[function] name: isGoModRoot file: cmd/import-boss/main.go:316 returns_error: нет description: isGoModRoot checks if a directory is the root directory for a package
by checking for the existence of a 'go.mod' file i


### isGoModRoot (cmd/import-boss/main.go:316)


isGoModRoot checks if a directory is the root directory for a package
by checking for the existence of a 'go.mod' file in that directory.


```go
func isGoModRoot((path string)) (path string)
```


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


📍 *Расположение:* `cmd/import-boss/main.go:316`



---


[function] name: loadPkgs file: cmd/import-boss/main.go:82 returns_error: да description: —


### loadPkgs (cmd/import-boss/main.go:82)


loadPkgs is a function that performs operations based on the provided parameters and may return an error.


```go
func loadPkgs(([]*packages.Package, error)) ([]*packages.Package, error)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*packages.Package`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/import-boss/main.go:82`



---


[function] name: main file: cmd/import-boss/main.go:43 returns_error: нет description: —


### main (cmd/import-boss/main.go:43)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/import-boss/main.go:43`



---


[function] name: massage file: cmd/import-boss/main.go:116 returns_error: нет description: —


### massage (cmd/import-boss/main.go:116)


massage is a function that performs operations based on the provided parameters and returns (in []*packages.Package).


```go
func massage((in []*packages.Package)) (in []*packages.Package)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/import-boss/main.go:116`



---


[function] name: newBoss file: cmd/import-boss/main.go:160 returns_error: нет description: —


### newBoss (cmd/import-boss/main.go:160)


newBoss is a function that performs operations based on the provided parameters and returns (pkgs []*packages.Package).


```go
func newBoss((pkgs []*packages.Package)) (pkgs []*packages.Package)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** pkgs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/import-boss/main.go:160`



---


[function] name: packageDir file: cmd/import-boss/main.go:211 returns_error: нет description: packageDir tries to figure out the directory of the specified package.


### packageDir (cmd/import-boss/main.go:211)


packageDir tries to figure out the directory of the specified package.


```go
func packageDir((pkg *packages.Package)) (pkg *packages.Package)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/import-boss/main.go:211`



---


[function] name: readFile file: cmd/import-boss/main.go:299 returns_error: да description: —


### readFile (cmd/import-boss/main.go:299)


readFile is a function that performs operations based on the provided parameters and may return an error.


```go
func readFile((*FileFormat, error)) (*FileFormat, error)
```


**Тип запроса:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


**Тип ответа:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FileFormat`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/import-boss/main.go:299`



---


[function] name: recursiveRead file: cmd/import-boss/main.go:275 returns_error: да description: recursiveRead collects all '.import-restriction' files, between the current directory,
and the module root.


### recursiveRead (cmd/import-boss/main.go:275)


recursiveRead collects all '.import-restriction' files, between the current directory,
and the module root.


```go
func recursiveRead(([]*FileFormat, error)) ([]*FileFormat, error)
```


**Тип запроса:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


**Тип ответа:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*FileFormat`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/import-boss/main.go:275`



---


[function] name: removeLastDir file: cmd/import-boss/main.go:324 returns_error: нет description: removeLastDir removes the last directory, but leaves the file name
unchanged. It returns the new path and the removed di


### removeLastDir (cmd/import-boss/main.go:324)


removeLastDir removes the last directory, but leaves the file name
unchanged. It returns the new path and the removed directory. So:
"a/b/c/file" -> ("a/b/file", "c")


```go
func removeLastDir((newPath, removedDir string)) (newPath, removedDir string)
```


**Тип ответа:** newPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** removedDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/import-boss/main.go:324`



---


[function] name: transitiveClosure file: cmd/import-boss/main.go:543 returns_error: нет description: —


### transitiveClosure (cmd/import-boss/main.go:543)


transitiveClosure is a function that performs operations based on the provided parameters and returns (in map[string][]string).


```go
func transitiveClosure((in map[string][]string)) (in map[string][]string)
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


📍 *Расположение:* `cmd/import-boss/main.go:543`



---


[function] name: transitiveImports file: cmd/import-boss/main.go:439 returns_error: нет description: —


### transitiveImports (cmd/import-boss/main.go:439)


transitiveImports is a function that performs operations based on the provided parameters and returns ([]string, []string).


```go
func transitiveImports(([]string, []string)) ([]string, []string)
```


📍 *Расположение:* `cmd/import-boss/main.go:439`



---


[function] name: uniq file: cmd/import-boss/main.go:412 returns_error: нет description: —


### uniq (cmd/import-boss/main.go:412)


uniq is a function that performs operations based on the provided parameters and returns (slices ...[]string).


```go
func uniq((slices ...[]string)) (slices ...[]string)
```


**Тип ответа:** slices


```json
{
  "toCreate": []
}
```


*Определено в:* `pkg/controller/endpointslicemirroring/reconciler_helpers.go`


📍 *Расположение:* `cmd/import-boss/main.go:412`



---


[function] name: unmassage file: cmd/import-boss/main.go:143 returns_error: нет description: —


### unmassage (cmd/import-boss/main.go:143)


unmassage is a function that performs operations based on the provided parameters and returns (str string).


```go
func unmassage((str string)) (str string)
```


**Тип ответа:** str


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/import-boss/main.go:143`



---


[function] name: verifyInverseRules file: cmd/import-boss/main.go:462 returns_error: нет description: verifyInverseRules checks that all packages that import a package are allowed to import it.


### verifyInverseRules (cmd/import-boss/main.go:462)


verifyInverseRules checks that all packages that import a package are allowed to import it.


```go
func (boss *ImportBoss) verifyInverseRules((pkg *packages.Package, restrictionFiles []*FileFormat)) (pkg *packages.Package, restrictionFiles []*FileFormat)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип запроса:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** restrictionFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


📍 *Расположение:* `cmd/import-boss/main.go:462`



---


[function] name: verifyRules file: cmd/import-boss/main.go:330 returns_error: нет description: —


### verifyRules (cmd/import-boss/main.go:330)


verifyRules is a method that performs operations based on the provided parameters and returns (pkg *packages.Package, restrictionFiles []*FileFormat).


```go
func (boss *ImportBoss) verifyRules((pkg *packages.Package, restrictionFiles []*FileFormat)) (pkg *packages.Package, restrictionFiles []*FileFormat)
```


**Тип запроса:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип запроса:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** packages.Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** restrictionFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FileFormat


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


📍 *Расположение:* `cmd/import-boss/main.go:330`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_gotemplate.md)

- [Следующая директория](cmd_importverifier.md)


---

