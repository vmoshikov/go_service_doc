---
title: "Функции: test/typecheck"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/typecheck
---


# Функции: test/typecheck


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_soak.md)

- [Следующая директория](test_utils.md)


---


## Меню по файлам


- 📄 [test/typecheck/main.go](#testtypecheckmaingo)

- 📄 [test/typecheck/testdata/bad/bad.go](#testtypechecktestdatabadbadgo)

- 📄 [test/typecheck/testdata/good/_ignore/bad.go](#testtypechecktestdatagood_ignorebadgo)

- 📄 [test/typecheck/testdata/good/good.go](#testtypechecktestdatagoodgoodgo)

- 📄 [test/typecheck/testdata/good/testdata/bad.go](#testtypechecktestdatagoodtestdatabadgo)


---


## test/typecheck/main.go


📄 Исходный файл: `test/typecheck/main.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [accumulate](#accumulate-testtypecheckmaingo137) `:137`

- 🔗 [dedup](#dedup-testtypecheckmaingo150) `:150`

- 🔗 [main](#main-testtypecheckmaingo190) `:190`

- 🔗 [newConfig](#newconfig-testtypecheckmaingo58) `:58`

- 🔗 [resolvePkgs](#resolvepkgs-testtypecheckmaingo172) `:172`

- 🔗 [serialFprintf](#serialfprintf-testtypecheckmaingo166) `:166`

- 🔗 [verify](#verify-testtypecheckmaingo83) `:83`


</details>


[function] name: accumulate file: test/typecheck/main.go:137 returns_error: нет description: —


### accumulate (test/typecheck/main.go:137)


accumulate is a function that performs operations based on the provided parameters and returns (pkg *packages.Package, allMap map[string]*packages.Package).


```go
func accumulate((pkg *packages.Package, allMap map[string]*packages.Package)) (pkg *packages.Package, allMap map[string]*packages.Package)
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


**Тип ответа:** allMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


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


📍 *Расположение:* `test/typecheck/main.go:137`



---


[function] name: dedup file: test/typecheck/main.go:150 returns_error: нет description: —


### dedup (test/typecheck/main.go:150)


dedup is a function that performs operations based on the provided parameters and may return an error.


```go
func dedup((errors []packages.Error)) (errors []packages.Error)
```


**Тип ответа:** errors


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** packages.Error


```json
{
  "XMLName": {},
  "Message": "string",
  "Type": "string",
  "Value": "string"
}
```


*Определено в:* `test/utils/junit/junit.go`


📍 *Расположение:* `test/typecheck/main.go:150`



---


[function] name: main file: test/typecheck/main.go:190 returns_error: нет description: —


### main (test/typecheck/main.go:190)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/typecheck/main.go:190`



---


[function] name: newConfig file: test/typecheck/main.go:58 returns_error: нет description: —


### newConfig (test/typecheck/main.go:58)


newConfig is a function that performs operations based on the provided parameters and returns (platform string).


```go
func newConfig((platform string)) (platform string)
```


**Тип ответа:** platform


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/typecheck/main.go:58`



---


[function] name: resolvePkgs file: test/typecheck/main.go:172 returns_error: да description: —


### resolvePkgs (test/typecheck/main.go:172)


resolvePkgs is a function that performs operations based on the provided parameters and may return an error.


```go
func resolvePkgs((map[string]bool, error)) (map[string]bool, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/typecheck/main.go:172`



---


[function] name: serialFprintf file: test/typecheck/main.go:166 returns_error: нет description: —


### serialFprintf (test/typecheck/main.go:166)


serialFprintf is a function that performs operations based on the provided parameters and returns (w io.Writer, format string, a ...interface{}).


```go
func serialFprintf((w io.Writer, format string, a ...interface{})) (w io.Writer, format string, a ...interface{})
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


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


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


📍 *Расположение:* `test/typecheck/main.go:166`



---


[function] name: verify file: test/typecheck/main.go:83 returns_error: да description: —


### verify (test/typecheck/main.go:83)


verify is a function that performs operations based on the provided parameters and may return an error.


```go
func verify(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/typecheck/main.go:83`




## test/typecheck/testdata/bad/bad.go


📄 Исходный файл: `test/typecheck/testdata/bad/bad.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testtypechecktestdatabadbadgo50) `:50`


</details>


[function] name: main file: test/typecheck/testdata/bad/bad.go:50 returns_error: нет description: —


### main (test/typecheck/testdata/bad/bad.go:50)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/typecheck/testdata/bad/bad.go:50`




## test/typecheck/testdata/good/_ignore/bad.go


📄 Исходный файл: `test/typecheck/testdata/good/_ignore/bad.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testtypechecktestdatagood_ignorebadgo23) `:23`


</details>


[function] name: main file: test/typecheck/testdata/good/_ignore/bad.go:23 returns_error: нет description: —


### main (test/typecheck/testdata/good/_ignore/bad.go:23)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/typecheck/testdata/good/_ignore/bad.go:23`




## test/typecheck/testdata/good/good.go


📄 Исходный файл: `test/typecheck/testdata/good/good.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testtypechecktestdatagoodgoodgo50) `:50`


</details>


[function] name: main file: test/typecheck/testdata/good/good.go:50 returns_error: нет description: —


### main (test/typecheck/testdata/good/good.go:50)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/typecheck/testdata/good/good.go:50`




## test/typecheck/testdata/good/testdata/bad.go


📄 Исходный файл: `test/typecheck/testdata/good/testdata/bad.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testtypechecktestdatagoodtestdatabadgo23) `:23`


</details>


[function] name: main file: test/typecheck/testdata/good/testdata/bad.go:23 returns_error: нет description: —


### main (test/typecheck/testdata/good/testdata/bad.go:23)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/typecheck/testdata/good/testdata/bad.go:23`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_soak.md)

- [Следующая директория](test_utils.md)


---

