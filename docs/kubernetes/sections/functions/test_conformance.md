---
title: "Функции: test/conformance"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/conformance
---


# Функции: test/conformance


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_compatibility_lifecycle.md)

- [Следующая директория](test_e2e.md)


---


## Меню по файлам


- 📄 [test/conformance/image/go-runner/cmd.go](#testconformanceimagego-runnercmdgo)

- 📄 [test/conformance/image/go-runner/env.go](#testconformanceimagego-runnerenvgo)

- 📄 [test/conformance/image/go-runner/main.go](#testconformanceimagego-runnermaingo)

- 📄 [test/conformance/image/go-runner/tar.go](#testconformanceimagego-runnertargo)

- 📄 [test/conformance/testdata/embed.go](#testconformancetestdataembedgo)

- 📄 [test/conformance/walk.go](#testconformancewalkgo)


---


## test/conformance/image/go-runner/cmd.go


📄 Исходный файл: `test/conformance/image/go-runner/cmd.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [cmdInfo](#cmdinfo-testconformanceimagego-runnercmdgo103) `:103`

- 🔗 [getCmd](#getcmd-testconformanceimagego-runnercmdgo28) `:28`


</details>


[function] name: cmdInfo file: test/conformance/image/go-runner/cmd.go:103 returns_error: нет description: cmdInfo generates a useful look at what the command is for printing/debug.


### cmdInfo (test/conformance/image/go-runner/cmd.go:103)


cmdInfo generates a useful look at what the command is for printing/debug.


```go
func cmdInfo((cmd *exec.Cmd)) (cmd *exec.Cmd)
```


**Тип запроса:** exec.Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


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


**Тип ответа:** exec.Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


📍 *Расположение:* `test/conformance/image/go-runner/cmd.go:103`



---


[function] name: getCmd file: test/conformance/image/go-runner/cmd.go:28 returns_error: нет description: getCmd uses the given environment to form the ginkgo command to run tests. It will
set the stdout/stderr to the given wr


### getCmd (test/conformance/image/go-runner/cmd.go:28)


getCmd uses the given environment to form the ginkgo command to run tests. It will
set the stdout/stderr to the given writer.


```go
func getCmd((env Getenver, w io.Writer)) (env Getenver, w io.Writer)
```


**Тип ответа:** env


```json
{
  "callSiteName": "string",
  "readEnvVarsOnce": {},
  "known": {},
  "enabledViaEnvVar": {},
  "lockEnabledViaSetMethod": {},
  "enabledViaSetMethod": {},
  "readEnvVars": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/features/envvar.go`


**Тип ответа:** Getenver


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/conformance/image/go-runner/cmd.go:28`




## test/conformance/image/go-runner/env.go


📄 Исходный файл: `test/conformance/image/go-runner/env.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Getenv](#getenv-testconformanceimagego-runnerenvgo33) `:33`

- 🔗 [Getenv](#getenv-testconformanceimagego-runnerenvgo44) `:44`

- 🔗 [Getenv](#getenv-testconformanceimagego-runnerenvgo56) `:56`

- 🔗 [envWithDefaults](#envwithdefaults-testconformanceimagego-runnerenvgo64) `:64`


</details>


[function] name: Getenv file: test/conformance/image/go-runner/env.go:33 returns_error: нет description: Getenv gets the value of the requested environment variable.


### Getenv (test/conformance/image/go-runner/env.go:33)


Getenv gets the value of the requested environment variable.


```go
func (*osEnv) Getenv((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/conformance/image/go-runner/env.go:33`



---


[function] name: Getenv file: test/conformance/image/go-runner/env.go:44 returns_error: нет description: Getenv returns the value of the requested environment variable (in this
implementation, really just a map lookup).


### Getenv (test/conformance/image/go-runner/env.go:44)


Getenv returns the value of the requested environment variable (in this
implementation, really just a map lookup).


```go
func (e *explicitEnv) Getenv((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/conformance/image/go-runner/env.go:44`



---


[function] name: Getenv file: test/conformance/image/go-runner/env.go:56 returns_error: нет description: Getenv returns the value of the environment variable or its default if unset.


### Getenv (test/conformance/image/go-runner/env.go:56)


Getenv returns the value of the environment variable or its default if unset.


```go
func (e *defaultEnver) Getenv((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/conformance/image/go-runner/env.go:56`



---


[function] name: envWithDefaults file: test/conformance/image/go-runner/env.go:64 returns_error: нет description: —


### envWithDefaults (test/conformance/image/go-runner/env.go:64)


envWithDefaults is a function that performs operations based on the provided parameters and returns (defaults map[string]string).


```go
func envWithDefaults((defaults map[string]string)) (defaults map[string]string)
```


**Тип ответа:** defaults


```json
{
  "object": null,
  "base": null,
  "additional": []
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/defaulter-gen/generators/defaulter.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/conformance/image/go-runner/env.go:64`




## test/conformance/image/go-runner/main.go


📄 Исходный файл: `test/conformance/image/go-runner/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [configureAndRunWithEnv](#configureandrunwithenv-testconformanceimagego-runnermaingo52) `:52`

- 🔗 [main](#main-testconformanceimagego-runnermaingo29) `:29`

- 🔗 [saveResults](#saveresults-testconformanceimagego-runnermaingo116) `:116`

- 🔗 [setupSigHandler](#setupsighandler-testconformanceimagego-runnermaingo94) `:94`


</details>


[function] name: configureAndRunWithEnv file: test/conformance/image/go-runner/main.go:52 returns_error: нет description: configureAndRunWithEnv uses the given environment to configure and then start the test run.
It will handle TERM signals 


### configureAndRunWithEnv (test/conformance/image/go-runner/main.go:52)


configureAndRunWithEnv uses the given environment to configure and then start the test run.
It will handle TERM signals gracefully and kill the test process and will
save the logs/results to the location specified via the RESULTS_DIR environment
variable.


```go
func configureAndRunWithEnv((env Getenver)) (env Getenver)
```


**Тип ответа:** env


```json
{
  "callSiteName": "string",
  "readEnvVarsOnce": {},
  "known": {},
  "enabledViaEnvVar": {},
  "lockEnabledViaSetMethod": {},
  "enabledViaSetMethod": {},
  "readEnvVars": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/features/envvar.go`


**Тип ответа:** Getenver


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/image/go-runner/main.go:52`



---


[function] name: main file: test/conformance/image/go-runner/main.go:29 returns_error: нет description: —


### main (test/conformance/image/go-runner/main.go:29)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/conformance/image/go-runner/main.go:29`



---


[function] name: saveResults file: test/conformance/image/go-runner/main.go:116 returns_error: нет description: saveResults will tar the results directory and write the resulting tarball path
into the donefile.


### saveResults (test/conformance/image/go-runner/main.go:116)


saveResults will tar the results directory and write the resulting tarball path
into the donefile.


```go
func saveResults((resultsDir string)) (resultsDir string)
```


**Тип ответа:** resultsDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/image/go-runner/main.go:116`



---


[function] name: setupSigHandler file: test/conformance/image/go-runner/main.go:94 returns_error: нет description: setupSigHandler will kill the process identified by the given PID if it
gets a TERM signal.


### setupSigHandler (test/conformance/image/go-runner/main.go:94)


setupSigHandler will kill the process identified by the given PID if it
gets a TERM signal.


```go
func setupSigHandler((pid int)) (pid int)
```


**Тип ответа:** pid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/image/go-runner/main.go:94`




## test/conformance/image/go-runner/tar.go


📄 Исходный файл: `test/conformance/image/go-runner/tar.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [tarDir](#tardir-testconformanceimagego-runnertargo31) `:31`


</details>


[function] name: tarDir file: test/conformance/image/go-runner/tar.go:31 returns_error: нет description: tarDir takes a source and variable writers and walks 'source' writing each file
found to the tar writer.


### tarDir (test/conformance/image/go-runner/tar.go:31)


tarDir takes a source and variable writers and walks 'source' writing each file
found to the tar writer.


```go
func tarDir((dir, outpath string)) (dir, outpath string)
```


**Тип ответа:** dir


```json
{
  "name": "string",
  "goRestfulContainer": null,
  "nonGoRestfulMux": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/handler.go`


**Тип ответа:** outpath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/image/go-runner/tar.go:31`




## test/conformance/testdata/embed.go


📄 Исходный файл: `test/conformance/testdata/embed.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetConformanceTestdataFS](#getconformancetestdatafs-testconformancetestdataembedgo28) `:28`


</details>


[function] name: GetConformanceTestdataFS file: test/conformance/testdata/embed.go:28 returns_error: нет description: —


### GetConformanceTestdataFS (test/conformance/testdata/embed.go:28)


GetConformanceTestdataFS is a function that retrieves data based on the provided parameters and returns ().


```go
func GetConformanceTestdataFS(()) ()
```


📍 *Расположение:* `test/conformance/testdata/embed.go:28`




## test/conformance/walk.go


📄 Исходный файл: `test/conformance/walk.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [commentToConformanceData](#commenttoconformancedata-testconformancewalkgo259) `:259`

- 🔗 [getConformanceData](#getconformancedata-testconformancewalkgo181) `:181`

- 🔗 [getTestInfo](#gettestinfo-testconformancewalkgo123) `:123`

- 🔗 [getTestName](#gettestname-testconformancewalkgo146) `:146`

- 🔗 [isConformance](#isconformance-testconformancewalkgo119) `:119`

- 🔗 [main](#main-testconformancewalkgo80) `:80`

- 🔗 [saveAllTestInfo](#savealltestinfo-testconformancewalkgo150) `:150`

- 🔗 [scanFileForFrame](#scanfileforframe-testconformancewalkgo209) `:209`

- 🔗 [shouldProcessCommentGroup](#shouldprocesscommentgroup-testconformancewalkgo254) `:254`

- 🔗 [tryCommentGroupAndFrame](#trycommentgroupandframe-testconformancewalkgo235) `:235`

- 🔗 [validateTestName](#validatetestname-testconformancewalkgo227) `:227`


</details>


[function] name: commentToConformanceData file: test/conformance/walk.go:259 returns_error: нет description: —


### commentToConformanceData (test/conformance/walk.go:259)


commentToConformanceData is a function that performs operations based on the provided parameters and returns (comment string).


```go
func commentToConformanceData((comment string)) (comment string)
```


**Тип ответа:** comment


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/walk.go:259`



---


[function] name: getConformanceData file: test/conformance/walk.go:181 returns_error: да description: —


### getConformanceData (test/conformance/walk.go:181)


getConformanceData is a function that performs operations based on the provided parameters and may return an error.


```go
func getConformanceData((*ConformanceData, error)) (*ConformanceData, error)
```


**Тип запроса:** ConformanceData


```json
{
  "URL": "string",
  "TestName": "string",
  "CodeName": "string",
  "Description": "string",
  "Release": "string",
  "File": "string"
}
```


*Определено в:* `test/conformance/walk.go`


**Тип ответа:** ConformanceData


```json
{
  "URL": "string",
  "TestName": "string",
  "CodeName": "string",
  "Description": "string",
  "Release": "string",
  "File": "string"
}
```


*Определено в:* `test/conformance/walk.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConformanceData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/conformance/walk.go:181`



---


[function] name: getTestInfo file: test/conformance/walk.go:123 returns_error: нет description: —


### getTestInfo (test/conformance/walk.go:123)


getTestInfo is a function that performs operations based on the provided parameters and returns (spec *types.SpecReport).


```go
func getTestInfo((spec *types.SpecReport)) (spec *types.SpecReport)
```


**Тип запроса:** types.SpecReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** types.SpecReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/walk.go:123`



---


[function] name: getTestName file: test/conformance/walk.go:146 returns_error: нет description: —


### getTestName (test/conformance/walk.go:146)


getTestName is a function that performs operations based on the provided parameters and returns (spec *types.SpecReport).


```go
func getTestName((spec *types.SpecReport)) (spec *types.SpecReport)
```


**Тип запроса:** types.SpecReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** types.SpecReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/walk.go:146`



---


[function] name: isConformance file: test/conformance/walk.go:119 returns_error: нет description: —


### isConformance (test/conformance/walk.go:119)


isConformance is a function that performs operations based on the provided parameters and returns (spec *types.SpecReport).


```go
func isConformance((spec *types.SpecReport)) (spec *types.SpecReport)
```


**Тип запроса:** types.SpecReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** types.SpecReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/conformance/walk.go:119`



---


[function] name: main file: test/conformance/walk.go:80 returns_error: нет description: —


### main (test/conformance/walk.go:80)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/conformance/walk.go:80`



---


[function] name: saveAllTestInfo file: test/conformance/walk.go:150 returns_error: нет description: —


### saveAllTestInfo (test/conformance/walk.go:150)


saveAllTestInfo is a function that performs operations based on the provided parameters and returns (dataSet []*ConformanceData).


```go
func saveAllTestInfo((dataSet []*ConformanceData)) (dataSet []*ConformanceData)
```


**Тип запроса:** ConformanceData


```json
{
  "URL": "string",
  "TestName": "string",
  "CodeName": "string",
  "Description": "string",
  "Release": "string",
  "File": "string"
}
```


*Определено в:* `test/conformance/walk.go`


**Тип ответа:** dataSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ConformanceData


```json
{
  "URL": "string",
  "TestName": "string",
  "CodeName": "string",
  "Description": "string",
  "Release": "string",
  "File": "string"
}
```


*Определено в:* `test/conformance/walk.go`


📍 *Расположение:* `test/conformance/walk.go:150`



---


[function] name: scanFileForFrame file: test/conformance/walk.go:209 returns_error: да description: scanFileForFrame will scan the target and look for a conformance comment attached to the function
described by the targe


### scanFileForFrame (test/conformance/walk.go:209)


scanFileForFrame will scan the target and look for a conformance comment attached to the function
described by the target frame. If the comment can't be found then nil, nil is returned.


```go
func scanFileForFrame((*ConformanceData, error)) (*ConformanceData, error)
```


**Тип запроса:** ConformanceData


```json
{
  "URL": "string",
  "TestName": "string",
  "CodeName": "string",
  "Description": "string",
  "Release": "string",
  "File": "string"
}
```


*Определено в:* `test/conformance/walk.go`


**Тип ответа:** ConformanceData


```json
{
  "URL": "string",
  "TestName": "string",
  "CodeName": "string",
  "Description": "string",
  "Release": "string",
  "File": "string"
}
```


*Определено в:* `test/conformance/walk.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConformanceData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/conformance/walk.go:209`



---


[function] name: shouldProcessCommentGroup file: test/conformance/walk.go:254 returns_error: нет description: —


### shouldProcessCommentGroup (test/conformance/walk.go:254)


shouldProcessCommentGroup is a function that performs operations based on the provided parameters and returns (fset *token.FileSet, cg *ast.CommentGroup, f frame).


```go
func shouldProcessCommentGroup((fset *token.FileSet, cg *ast.CommentGroup, f frame)) (fset *token.FileSet, cg *ast.CommentGroup, f frame)
```


**Тип запроса:** token.FileSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** ast.CommentGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cg


```json
{
  "subsystems": null,
  "useSystemd": false
}
```


*Определено в:* `pkg/kubelet/cm/cgroup_manager_linux.go`


**Тип ответа:** ast.CommentGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** f


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


**Тип ответа:** frame


```json
{
  "File": "string",
  "Line": 0
}
```


*Определено в:* `test/conformance/walk.go`


📍 *Расположение:* `test/conformance/walk.go:254`



---


[function] name: tryCommentGroupAndFrame file: test/conformance/walk.go:235 returns_error: нет description: —


### tryCommentGroupAndFrame (test/conformance/walk.go:235)


tryCommentGroupAndFrame is a function that performs operations based on the provided parameters and returns (fset *token.FileSet, cg *ast.CommentGroup, f frame).


```go
func tryCommentGroupAndFrame((fset *token.FileSet, cg *ast.CommentGroup, f frame)) (fset *token.FileSet, cg *ast.CommentGroup, f frame)
```


**Тип запроса:** token.FileSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** ast.CommentGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cg


```json
{
  "subsystems": null,
  "useSystemd": false
}
```


*Определено в:* `pkg/kubelet/cm/cgroup_manager_linux.go`


**Тип ответа:** ast.CommentGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** f


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


**Тип ответа:** frame


```json
{
  "File": "string",
  "Line": 0
}
```


*Определено в:* `test/conformance/walk.go`


📍 *Расположение:* `test/conformance/walk.go:235`



---


[function] name: validateTestName file: test/conformance/walk.go:227 returns_error: нет description: —


### validateTestName (test/conformance/walk.go:227)


validateTestName is a function that performs operations based on the provided parameters and returns (s string).


```go
func validateTestName((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/conformance/walk.go:227`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_compatibility_lifecycle.md)

- [Следующая директория](test_e2e.md)


---

