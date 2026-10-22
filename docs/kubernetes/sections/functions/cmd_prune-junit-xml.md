---
title: "Функции: cmd/prune-junit-xml"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/prune-junit-xml
---


# Функции: cmd/prune-junit-xml


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_preferredimports.md)

- [Следующая директория](hack_conformance.md)


---


## Меню по файлам


- 📄 [cmd/prune-junit-xml/logparse/logparse.go](#cmdprune-junit-xmllogparselogparsego)

- 📄 [cmd/prune-junit-xml/prunexml.go](#cmdprune-junit-xmlprunexmlgo)


---


## cmd/prune-junit-xml/logparse/logparse.go


📄 Исходный файл: `cmd/prune-junit-xml/logparse/logparse.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [All](#all-cmdprune-junit-xmllogparselogparsego73) `:73`

- 🔗 [LogData](#logdata-cmdprune-junit-xmllogparselogparsego98) `:98`

- 🔗 [LogData](#logdata-cmdprune-junit-xmllogparselogparsego109) `:109`

- 🔗 [LogData](#logdata-cmdprune-junit-xmllogparselogparsego130) `:130`

- 🔗 [Parse](#parse-cmdprune-junit-xmllogparselogparsego60) `:60`

- 🔗 [String](#string-cmdprune-junit-xmllogparselogparsego99) `:99`

- 🔗 [String](#string-cmdprune-junit-xmllogparselogparsego110) `:110`

- 🔗 [String](#string-cmdprune-junit-xmllogparselogparsego131) `:131`

- 🔗 [lookupSubmatch](#lookupsubmatch-cmdprune-junit-xmllogparselogparsego188) `:188`

- 🔗 [parse](#parse-cmdprune-junit-xmllogparselogparsego133) `:133`

- 🔗 [parseLine](#parseline-cmdprune-junit-xmllogparselogparsego201) `:201`


</details>


[function] name: All file: cmd/prune-junit-xml/logparse/logparse.go:73 returns_error: нет description: All is like Parse except that it can be used in a for/range loop:

for entry := range logparse.All(reader) {
// entry is


### All (cmd/prune-junit-xml/logparse/logparse.go:73)


All is like Parse except that it can be used in a for/range loop:

for entry := range logparse.All(reader) {
// entry is the next log entry.
}


```go
func All((in io.Reader)) (in io.Reader)
```


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** io.Reader


```json
{
  "logger": {},
  "err": {},
  "r": {},
  "ping": false,
  "timeout": {},
  "protocols": {},
  "selectedProtocol": "string",
  "handleCrash": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/stream.go`


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:73`



---


[function] name: LogData file: cmd/prune-junit-xml/logparse/logparse.go:98 returns_error: нет description: —


### LogData (cmd/prune-junit-xml/logparse/logparse.go:98)


LogData is a method that performs operations based on the provided parameters and returns ().


```go
func (e *ErrorEntry) LogData(()) ()
```


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:98`



---


[function] name: LogData file: cmd/prune-junit-xml/logparse/logparse.go:109 returns_error: нет description: —


### LogData (cmd/prune-junit-xml/logparse/logparse.go:109)


LogData is a method that performs operations based on the provided parameters and returns ().


```go
func (e *OtherEntry) LogData(()) ()
```


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:109`



---


[function] name: LogData file: cmd/prune-junit-xml/logparse/logparse.go:130 returns_error: нет description: —


### LogData (cmd/prune-junit-xml/logparse/logparse.go:130)


LogData is a method that performs operations based on the provided parameters and returns ().


```go
func (e *KlogEntry) LogData(()) ()
```


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:130`



---


[function] name: Parse file: cmd/prune-junit-xml/logparse/logparse.go:60 returns_error: нет description: Parse splits log output provided by the reader into individual log entries.
The original log can be reconstructed verbat


### Parse (cmd/prune-junit-xml/logparse/logparse.go:60)


Parse splits log output provided by the reader into individual log entries.
The original log can be reconstructed verbatim by concatenating these
entries. If the reader fails with an error, the last log entry will
capture that error.


```go
func Parse((in io.Reader)) (in io.Reader)
```


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** io.Reader


```json
{
  "logger": {},
  "err": {},
  "r": {},
  "ping": false,
  "timeout": {},
  "protocols": {},
  "selectedProtocol": "string",
  "handleCrash": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/stream.go`


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:60`



---


[function] name: String file: cmd/prune-junit-xml/logparse/logparse.go:99 returns_error: нет description: —


### String (cmd/prune-junit-xml/logparse/logparse.go:99)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (e *ErrorEntry) String(()) ()
```


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:99`



---


[function] name: String file: cmd/prune-junit-xml/logparse/logparse.go:110 returns_error: нет description: —


### String (cmd/prune-junit-xml/logparse/logparse.go:110)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (e *OtherEntry) String(()) ()
```


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:110`



---


[function] name: String file: cmd/prune-junit-xml/logparse/logparse.go:131 returns_error: нет description: —


### String (cmd/prune-junit-xml/logparse/logparse.go:131)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (e *KlogEntry) String(()) ()
```


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:131`



---


[function] name: lookupSubmatch file: cmd/prune-junit-xml/logparse/logparse.go:188 returns_error: нет description: —


### lookupSubmatch (cmd/prune-junit-xml/logparse/logparse.go:188)


lookupSubmatch is a function that performs operations based on the provided parameters and returns (name string).


```go
func lookupSubmatch((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:188`



---


[function] name: parse file: cmd/prune-junit-xml/logparse/logparse.go:133 returns_error: нет description: —


### parse (cmd/prune-junit-xml/logparse/logparse.go:133)


parse is a function that performs operations based on the provided parameters and returns (in io.Reader, yield func(Entry) bool).


```go
func parse((in io.Reader, yield func(Entry) bool)) (in io.Reader, yield func(Entry) bool)
```


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** io.Reader


```json
{
  "logger": {},
  "err": {},
  "r": {},
  "ping": false,
  "timeout": {},
  "protocols": {},
  "selectedProtocol": "string",
  "handleCrash": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/stream.go`


**Тип ответа:** yield


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Entry


```json
{
  "IP": "string",
  "Port": 0,
  "Protocol": "string",
  "Net": "string",
  "IP2": "string",
  "SetType": {}
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:133`



---


[function] name: parseLine file: cmd/prune-junit-xml/logparse/logparse.go:201 returns_error: да description: parseLine deals with one non-empty line. It returns the result of yield and
potentially the next line and/or a read erro


### parseLine (cmd/prune-junit-xml/logparse/logparse.go:201)


parseLine deals with one non-empty line. It returns the result of yield and
potentially the next line and/or a read error. If it doesn't have any new
data to process, it returns the empty string and a nil error.


```go
func parseLine((string, bool, error)) (string, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/prune-junit-xml/logparse/logparse.go:201`




## cmd/prune-junit-xml/prunexml.go


📄 Исходный файл: `cmd/prune-junit-xml/prunexml.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [fetchXML](#fetchxml-cmdprune-junit-xmlprunexmlgo188) `:188`

- 🔗 [joinTexts](#jointexts-cmdprune-junit-xmlprunexmlgo171) `:171`

- 🔗 [main](#main-cmdprune-junit-xmlprunexmlgo32) `:32`

- 🔗 [pruneStringIfNeeded](#prunestringifneeded-cmdprune-junit-xmlprunexmlgo112) `:112`

- 🔗 [pruneTESTS](#prunetests-cmdprune-junit-xmlprunexmlgo124) `:124`

- 🔗 [pruneXML](#prunexml-cmdprune-junit-xmlprunexmlgo67) `:67`

- 🔗 [streamXML](#streamxml-cmdprune-junit-xmlprunexmlgo198) `:198`


</details>


[function] name: fetchXML file: cmd/prune-junit-xml/prunexml.go:188 returns_error: да description: —


### fetchXML (cmd/prune-junit-xml/prunexml.go:188)


fetchXML is a function that performs operations based on the provided parameters and may return an error.


```go
func fetchXML((*junitxml.JUnitTestSuites, error)) (*junitxml.JUnitTestSuites, error)
```


**Тип запроса:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*junitxml.JUnitTestSuites`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/prune-junit-xml/prunexml.go:188`



---


[function] name: joinTexts file: cmd/prune-junit-xml/prunexml.go:171 returns_error: нет description: joinTexts returns "<a><empty line><b>" if both are non-empty,
otherwise just the non-empty string, if there is one.

If 


### joinTexts (cmd/prune-junit-xml/prunexml.go:171)


joinTexts returns "<a><empty line><b>" if both are non-empty,
otherwise just the non-empty string, if there is one.

If <b> is contained completely in <a>, <a> gets returned because repeating
exactly the same string again doesn't add any information. Typically
this occurs when joining the failure message because that is the fixed
string "Failed" for all tests, regardless of what the test logged.
The test log output is typically different because it cointains "=== RUN
<test name>" and thus doesn't get dropped.


```go
func joinTexts((a, b string)) (a, b string)
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


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `cmd/prune-junit-xml/prunexml.go:171`



---


[function] name: main file: cmd/prune-junit-xml/prunexml.go:32 returns_error: нет description: —


### main (cmd/prune-junit-xml/prunexml.go:32)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/prune-junit-xml/prunexml.go:32`



---


[function] name: pruneStringIfNeeded file: cmd/prune-junit-xml/prunexml.go:112 returns_error: нет description: —


### pruneStringIfNeeded (cmd/prune-junit-xml/prunexml.go:112)


pruneStringIfNeeded is a function that performs operations based on the provided parameters and returns (str *string, maxBytes int, msg string, args ...any).


```go
func pruneStringIfNeeded((str *string, maxBytes int, msg string, args ...any)) (str *string, maxBytes int, msg string, args ...any)
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


**Тип ответа:** maxBytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/prune-junit-xml/prunexml.go:112`



---


[function] name: pruneTESTS file: cmd/prune-junit-xml/prunexml.go:124 returns_error: нет description: This function condenses the junit xml to have package name as top level identifier
and nesting under that.


### pruneTESTS (cmd/prune-junit-xml/prunexml.go:124)


This function condenses the junit xml to have package name as top level identifier
and nesting under that.


```go
func pruneTESTS((suites *junitxml.JUnitTestSuites)) (suites *junitxml.JUnitTestSuites)
```


**Тип запроса:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** suites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/prune-junit-xml/prunexml.go:124`



---


[function] name: pruneXML file: cmd/prune-junit-xml/prunexml.go:67 returns_error: нет description: —


### pruneXML (cmd/prune-junit-xml/prunexml.go:67)


pruneXML is a function that performs operations based on the provided parameters and returns (suites *junitxml.JUnitTestSuites, maxBytes int).


```go
func pruneXML((suites *junitxml.JUnitTestSuites, maxBytes int)) (suites *junitxml.JUnitTestSuites, maxBytes int)
```


**Тип запроса:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** suites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxBytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/prune-junit-xml/prunexml.go:67`



---


[function] name: streamXML file: cmd/prune-junit-xml/prunexml.go:198 returns_error: нет description: —


### streamXML (cmd/prune-junit-xml/prunexml.go:198)


streamXML is a function that performs operations based on the provided parameters and returns (writer io.Writer, in *junitxml.JUnitTestSuites).


```go
func streamXML((writer io.Writer, in *junitxml.JUnitTestSuites)) (writer io.Writer, in *junitxml.JUnitTestSuites)
```


**Тип запроса:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** junitxml.JUnitTestSuites


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/prune-junit-xml/prunexml.go:198`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_preferredimports.md)

- [Следующая директория](hack_conformance.md)


---

