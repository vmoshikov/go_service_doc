---
title: "Функции: test/list"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/list
---


# Функции: test/list


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_integration.md)

- [Следующая директория](test_soak.md)


---


## Меню по файлам


- 📄 [test/list/main.go](#testlistmaingo)


---


## test/list/main.go


📄 Исходный файл: `test/list/main.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [Visit](#visit-testlistmaingo182) `:182`

- 🔗 [clone](#clone-testlistmaingo118) `:118`

- 🔗 [collect](#collect-testlistmaingo50) `:50`

- 🔗 [describeName](#describename-testlistmaingo160) `:160`

- 🔗 [firstArg](#firstarg-testlistmaingo125) `:125`

- 🔗 [funcName](#funcname-testlistmaingo91) `:91`

- 🔗 [handlePath](#handlepath-testlistmaingo232) `:232`

- 🔗 [isSprintf](#issprintf-testlistmaingo101) `:101`

- 🔗 [itName](#itname-testlistmaingo173) `:173`

- 🔗 [main](#main-testlistmaingo249) `:249`

- 🔗 [makeWalker](#makewalker-testlistmaingo113) `:113`


</details>


[function] name: Visit file: test/list/main.go:182 returns_error: нет description: Visit walks the AST, following Ginkgo context and collecting tests.
See the documentation for ast.Walk for more details.


### Visit (test/list/main.go:182)


Visit walks the AST, following Ginkgo context and collecting tests.
See the documentation for ast.Walk for more details.


```go
func (w *walker) Visit((n ast.Node)) (n ast.Node)
```


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


**Тип ответа:** ast.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/list/main.go:182`



---


[function] name: clone file: test/list/main.go:118 returns_error: нет description: clone creates a new walker with the given string extending the path.


### clone (test/list/main.go:118)


clone creates a new walker with the given string extending the path.


```go
func (w *walker) clone((ext string)) (ext string)
```


**Тип ответа:** ext


```json
{
  "ClientBuilder": {},
  "InformerFactory": {},
  "ObjectOrMetadataInformerFactory": {},
  "RESTMapper": null,
  "Stop": {},
  "InformersStarted": {},
  "ResyncPeriod": {},
  "ControllerManagerMetrics": null
}
```


*Определено в:* `staging/src/k8s.io/controller-manager/app/controllercontext.go`


📍 *Расположение:* `test/list/main.go:118`



---


[function] name: collect file: test/list/main.go:50 returns_error: нет description: collect extracts test metadata from a file.
If src is nil, it reads filename for the code, otherwise it
uses src (which 


### collect (test/list/main.go:50)


collect extracts test metadata from a file.
If src is nil, it reads filename for the code, otherwise it
uses src (which may be a string, byte[], or io.Reader).


```go
func collect((filename string, src interface{})) (filename string, src interface{})
```


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/list/main.go:50`



---


[function] name: describeName file: test/list/main.go:160 returns_error: нет description: describeName returns the first argument of a function if it's
a Ginkgo-relevant function (Describe/SIGDescribe/Context),


### describeName (test/list/main.go:160)


describeName returns the first argument of a function if it's
a Ginkgo-relevant function (Describe/SIGDescribe/Context),
and the empty string otherwise.


```go
func (w *walker) describeName((n *ast.CallExpr)) (n *ast.CallExpr)
```


**Тип запроса:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/list/main.go:160`



---


[function] name: firstArg file: test/list/main.go:125 returns_error: нет description: firstArg attempts to statically determine the value of the first
argument. It only handles strings, and converts any unk


### firstArg (test/list/main.go:125)


firstArg attempts to statically determine the value of the first
argument. It only handles strings, and converts any unknown values
(fmt.Sprintf interpolations) into *.


```go
func (w *walker) firstArg((n *ast.CallExpr)) (n *ast.CallExpr)
```


**Тип запроса:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/list/main.go:125`



---


[function] name: funcName file: test/list/main.go:91 returns_error: нет description: funcName converts a selectorExpr with two idents into a string,
x.y -> "x.y"


### funcName (test/list/main.go:91)


funcName converts a selectorExpr with two idents into a string,
x.y -> "x.y"


```go
func funcName((n ast.Expr)) (n ast.Expr)
```


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


**Тип ответа:** ast.Expr


```json
{
  "FieldRef": "string",
  "Warning": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/admissionregistration/v1alpha1/expressionwarning.go`


📍 *Расположение:* `test/list/main.go:91`



---


[function] name: handlePath file: test/list/main.go:232 returns_error: да description: handlePath walks the filesystem recursively, collecting tests
from files with paths *e2e*.go and *_test.go, ignoring thi


### handlePath (test/list/main.go:232)


handlePath walks the filesystem recursively, collecting tests
from files with paths *e2e*.go and *_test.go, ignoring third_party
and staging directories.


```go
func (t *testList) handlePath((path string, info os.FileInfo, err error)) (path string, info os.FileInfo, err error)
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


**Тип ответа:** info


```json
{
  "lister": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/pods.go`


**Тип ответа:** os.FileInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `path string`, `info os.FileInfo`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/list/main.go:232`



---


[function] name: isSprintf file: test/list/main.go:101 returns_error: нет description: isSprintf returns whether the given node is a call to fmt.Sprintf


### isSprintf (test/list/main.go:101)


isSprintf returns whether the given node is a call to fmt.Sprintf


```go
func isSprintf((n ast.Expr)) (n ast.Expr)
```


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


**Тип ответа:** ast.Expr


```json
{
  "FieldRef": "string",
  "Warning": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/admissionregistration/v1alpha1/expressionwarning.go`


📍 *Расположение:* `test/list/main.go:101`



---


[function] name: itName file: test/list/main.go:173 returns_error: нет description: itName returns the first argument if it's a call to It(), else "".


### itName (test/list/main.go:173)


itName returns the first argument if it's a call to It(), else "".


```go
func (w *walker) itName((n *ast.CallExpr)) (n *ast.CallExpr)
```


**Тип запроса:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** ast.CallExpr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/list/main.go:173`



---


[function] name: main file: test/list/main.go:249 returns_error: нет description: —


### main (test/list/main.go:249)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/list/main.go:249`



---


[function] name: makeWalker file: test/list/main.go:113 returns_error: нет description: —


### makeWalker (test/list/main.go:113)


makeWalker is a function that performs operations based on the provided parameters and returns (path string, fset *token.FileSet, tests *[]Test).


```go
func makeWalker((path string, fset *token.FileSet, tests *[]Test)) (path string, fset *token.FileSet, tests *[]Test)
```


**Тип запроса:** token.FileSet


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


**Тип ответа:** fset


```json
{
  "rand": null,
  "offset": 0
}
```


*Определено в:* `pkg/registry/core/service/allocator/bitmap.go`


**Тип ответа:** token.FileSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Test


```json
{
  "Volume": {},
  "Mode": {},
  "File": "string",
  "ExpectedContent": "string"
}
```


*Определено в:* `test/e2e/framework/volume/fixtures.go`


📍 *Расположение:* `test/list/main.go:113`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_integration.md)

- [Следующая директория](test_soak.md)


---

