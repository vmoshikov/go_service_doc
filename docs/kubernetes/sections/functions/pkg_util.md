---
title: "Функции: pkg/util"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/util
---


# Функции: pkg/util


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_serviceaccount.md)

- [Следующая директория](pkg_volume.md)


---


## Меню по файлам


- 📄 [pkg/util/async/runner.go](#pkgutilasyncrunnergo)

- 📄 [pkg/util/coverage/coverage.go](#pkgutilcoveragecoveragego)

- 📄 [pkg/util/coverage/coverage_disabled.go](#pkgutilcoveragecoverage_disabledgo)

- 📄 [pkg/util/coverage/fake_test_deps.go](#pkgutilcoveragefake_test_depsgo)

- 📄 [pkg/util/env/env.go](#pkgutilenvenvgo)

- 📄 [pkg/util/filesystem/defaultfs.go](#pkgutilfilesystemdefaultfsgo)

- 📄 [pkg/util/filesystem/util.go](#pkgutilfilesystemutilgo)

- 📄 [pkg/util/filesystem/util_unix.go](#pkgutilfilesystemutil_unixgo)

- 📄 [pkg/util/filesystem/util_windows.go](#pkgutilfilesystemutil_windowsgo)

- 📄 [pkg/util/filesystem/watcher.go](#pkgutilfilesystemwatchergo)

- 📄 [pkg/util/flag/flags.go](#pkgutilflagflagsgo)

- 📄 [pkg/util/flock/flock_other.go](#pkgutilflockflock_othergo)

- 📄 [pkg/util/flock/flock_unix.go](#pkgutilflockflock_unixgo)

- 📄 [pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go](#pkgutilgoroutinemapexponentialbackoffexponential_backoffgo)

- 📄 [pkg/util/goroutinemap/goroutinemap.go](#pkgutilgoroutinemapgoroutinemapgo)

- 📄 [pkg/util/hash/hash.go](#pkgutilhashhashgo)

- 📄 [pkg/util/interrupt/interrupt.go](#pkgutilinterruptinterruptgo)

- 📄 [pkg/util/iptables/iptables.go](#pkgutiliptablesiptablesgo)

- 📄 [pkg/util/iptables/iptables_linux.go](#pkgutiliptablesiptables_linuxgo)

- 📄 [pkg/util/iptables/save_restore.go](#pkgutiliptablessave_restorego)

- 📄 [pkg/util/iptables/testing/fake.go](#pkgutiliptablestestingfakego)

- 📄 [pkg/util/iptables/testing/parse.go](#pkgutiliptablestestingparsego)

- 📄 [pkg/util/kernel/version.go](#pkgutilkernelversiongo)

- 📄 [pkg/util/labels/labels.go](#pkgutillabelslabelsgo)

- 📄 [pkg/util/node/node.go](#pkgutilnodenodego)

- 📄 [pkg/util/oom/oom_fake.go](#pkgutiloomoom_fakego)

- 📄 [pkg/util/oom/oom_linux.go](#pkgutiloomoom_linuxgo)

- 📄 [pkg/util/oom/oom_unsupported.go](#pkgutiloomoom_unsupportedgo)

- 📄 [pkg/util/parsers/parsers.go](#pkgutilparsersparsersgo)

- 📄 [pkg/util/pod/pod.go](#pkgutilpodpodgo)

- 📄 [pkg/util/procfs/procfs_fake.go](#pkgutilprocfsprocfs_fakego)

- 📄 [pkg/util/procfs/procfs_linux.go](#pkgutilprocfsprocfs_linuxgo)

- 📄 [pkg/util/procfs/procfs_unsupported.go](#pkgutilprocfsprocfs_unsupportedgo)

- 📄 [pkg/util/removeall/removeall.go](#pkgutilremoveallremoveallgo)

- 📄 [pkg/util/rlimit/rlimit_linux.go](#pkgutilrlimitrlimit_linuxgo)

- 📄 [pkg/util/rlimit/rlimit_unsupported.go](#pkgutilrlimitrlimit_unsupportedgo)

- 📄 [pkg/util/slice/slice.go](#pkgutilsliceslicego)

- 📄 [pkg/util/tail/tail.go](#pkgutiltailtailgo)

- 📄 [pkg/util/taints/taints.go](#pkgutiltaintstaintsgo)

- 📄 [pkg/util/tolerations/tolerations.go](#pkgutiltolerationstolerationsgo)


---


## pkg/util/async/runner.go


📄 Исходный файл: `pkg/util/async/runner.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [NewRunner](#newrunner-pkgutilasyncrunnergo33) `:33`

- 🔗 [Start](#start-pkgutilasyncrunnergo38) `:38`

- 🔗 [Stop](#stop-pkgutilasyncrunnergo51) `:51`


</details>


[function] name: NewRunner file: pkg/util/async/runner.go:33 returns_error: нет description: NewRunner makes a runner for the given function(s). The function(s) should loop until
the channel is closed.


### NewRunner (pkg/util/async/runner.go:33)


NewRunner makes a runner for the given function(s). The function(s) should loop until
the channel is closed.


```go
func NewRunner((f ...func(stop chan struct{}))) (f ...func(stop chan struct{}))
```


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


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stop


```json
{
  "Opcode": {}
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/util/async/runner.go:33`



---


[function] name: Start file: pkg/util/async/runner.go:38 returns_error: нет description: Start begins running.


### Start (pkg/util/async/runner.go:38)


Start begins running.


```go
func (r *Runner) Start(()) ()
```


📍 *Расположение:* `pkg/util/async/runner.go:38`



---


[function] name: Stop file: pkg/util/async/runner.go:51 returns_error: нет description: Stop stops running.


### Stop (pkg/util/async/runner.go:51)


Stop stops running.


```go
func (r *Runner) Stop(()) ()
```


📍 *Расположение:* `pkg/util/async/runner.go:51`




## pkg/util/coverage/coverage.go


📄 Исходный файл: `pkg/util/coverage/coverage.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [FlushCoverage](#flushcoverage-pkgutilcoveragecoveragego73) `:73`

- 🔗 [InitCoverage](#initcoverage-pkgutilcoveragecoveragego44) `:44`

- 🔗 [tempCoveragePath](#tempcoveragepath-pkgutilcoveragecoveragego38) `:38`


</details>


[function] name: FlushCoverage file: pkg/util/coverage/coverage.go:73 returns_error: нет description: FlushCoverage flushes collected coverage information to disk.
The destination file is configured at startup and cannot b


### FlushCoverage (pkg/util/coverage/coverage.go:73)


FlushCoverage flushes collected coverage information to disk.
The destination file is configured at startup and cannot be changed.
Calling this function also sends a line like "coverage: 5% of statements" to stdout.


```go
func FlushCoverage(()) ()
```


📍 *Расположение:* `pkg/util/coverage/coverage.go:73`



---


[function] name: InitCoverage file: pkg/util/coverage/coverage.go:44 returns_error: нет description: InitCoverage is called from the dummy unit test to prepare Go's coverage framework.
Clients should never need to call it


### InitCoverage (pkg/util/coverage/coverage.go:44)


InitCoverage is called from the dummy unit test to prepare Go's coverage framework.
Clients should never need to call it.


```go
func InitCoverage((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/util/coverage/coverage.go:44`



---


[function] name: tempCoveragePath file: pkg/util/coverage/coverage.go:38 returns_error: нет description: tempCoveragePath returns a temporary file to write coverage information to.
The file is in the same directory as the des


### tempCoveragePath (pkg/util/coverage/coverage.go:38)


tempCoveragePath returns a temporary file to write coverage information to.
The file is in the same directory as the destination, ensuring os.Rename will work.


```go
func tempCoveragePath(()) ()
```


📍 *Расположение:* `pkg/util/coverage/coverage.go:38`




## pkg/util/coverage/coverage_disabled.go


📄 Исходный файл: `pkg/util/coverage/coverage_disabled.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [FlushCoverage](#flushcoverage-pkgutilcoveragecoverage_disabledgo27) `:27`

- 🔗 [InitCoverage](#initcoverage-pkgutilcoveragecoverage_disabledgo22) `:22`


</details>


[function] name: FlushCoverage file: pkg/util/coverage/coverage_disabled.go:27 returns_error: нет description: FlushCoverage is a no-op when not running with coverage.


### FlushCoverage (pkg/util/coverage/coverage_disabled.go:27)


FlushCoverage is a no-op when not running with coverage.


```go
func FlushCoverage(()) ()
```


📍 *Расположение:* `pkg/util/coverage/coverage_disabled.go:27`



---


[function] name: InitCoverage file: pkg/util/coverage/coverage_disabled.go:22 returns_error: нет description: InitCoverage is illegal when not running with coverage.


### InitCoverage (pkg/util/coverage/coverage_disabled.go:22)


InitCoverage is illegal when not running with coverage.


```go
func InitCoverage((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/util/coverage/coverage_disabled.go:22`




## pkg/util/coverage/fake_test_deps.go


📄 Исходный файл: `pkg/util/coverage/fake_test_deps.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [CheckCorpus](#checkcorpus-pkgutilcoveragefake_test_depsgo99) `:99`

- 🔗 [CoordinateFuzzing](#coordinatefuzzing-pkgutilcoveragefake_test_depsgo84) `:84`

- 🔗 [ImportPath](#importpath-pkgutilcoveragefake_test_depsgo45) `:45`

- 🔗 [InitRuntimeCoverage](#initruntimecoverage-pkgutilcoveragefake_test_depsgo110) `:110`

- 🔗 [MatchString](#matchstring-pkgutilcoveragefake_test_depsgo50) `:50`

- 🔗 [ReadCorpus](#readcorpus-pkgutilcoveragefake_test_depsgo94) `:94`

- 🔗 [ResetCoverage](#resetcoverage-pkgutilcoveragefake_test_depsgo104) `:104`

- 🔗 [RunFuzzWorker](#runfuzzworker-pkgutilcoveragefake_test_depsgo89) `:89`

- 🔗 [SetPanicOnExit0](#setpaniconexit0-pkgutilcoveragefake_test_depsgo55) `:55`

- 🔗 [SnapshotCoverage](#snapshotcoverage-pkgutilcoveragefake_test_depsgo107) `:107`

- 🔗 [StartCPUProfile](#startcpuprofile-pkgutilcoveragefake_test_depsgo58) `:58`

- 🔗 [StartTestLog](#starttestlog-pkgutilcoveragefake_test_depsgo66) `:66`

- 🔗 [StopCPUProfile](#stopcpuprofile-pkgutilcoveragefake_test_depsgo63) `:63`

- 🔗 [StopTestLog](#stoptestlog-pkgutilcoveragefake_test_depsgo69) `:69`

- 🔗 [WriteHeapProfile](#writeheapprofile-pkgutilcoveragefake_test_depsgo74) `:74`

- 🔗 [WriteProfileTo](#writeprofileto-pkgutilcoveragefake_test_depsgo79) `:79`


</details>


[function] name: CheckCorpus file: pkg/util/coverage/fake_test_deps.go:99 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### CheckCorpus (pkg/util/coverage/fake_test_deps.go:99)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) CheckCorpus(([]any, []reflect.Type)) ([]any, []reflect.Type)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reflect.Type


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:99`



---


[function] name: CoordinateFuzzing file: pkg/util/coverage/fake_test_deps.go:84 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### CoordinateFuzzing (pkg/util/coverage/fake_test_deps.go:84)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) CoordinateFuzzing((time.Duration, int64, time.Duration, int64, int, []corpusEntry, []reflect.Type, string, string)) (time.Duration, int64, time.Duration, int64, int, []corpusEntry, []reflect.Type, string, string)
```


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** corpusEntry


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reflect.Type


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:84`



---


[function] name: ImportPath file: pkg/util/coverage/fake_test_deps.go:45 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### ImportPath (pkg/util/coverage/fake_test_deps.go:45)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) ImportPath(()) ()
```


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:45`



---


[function] name: InitRuntimeCoverage file: pkg/util/coverage/fake_test_deps.go:110 returns_error: да description: nolint:unused // U1000 see comment above, we know it's unused normally.


### InitRuntimeCoverage (pkg/util/coverage/fake_test_deps.go:110)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) InitRuntimeCoverage((mode string, tearDown func(string, string) (string, error), snapcov func() float64)) (mode string, tearDown func(string, string) (string, error), snapcov func() float64)
```


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** tearDown


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** snapcov


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `mode string`, `tearDown func(string`, `string) (string`, `error)`, `snapcov func() float64`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:110`



---


[function] name: MatchString file: pkg/util/coverage/fake_test_deps.go:50 returns_error: да description: nolint:unused // U1000 see comment above, we know it's unused normally.


### MatchString (pkg/util/coverage/fake_test_deps.go:50)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) MatchString((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:50`



---


[function] name: ReadCorpus file: pkg/util/coverage/fake_test_deps.go:94 returns_error: да description: nolint:unused // U1000 see comment above, we know it's unused normally.


### ReadCorpus (pkg/util/coverage/fake_test_deps.go:94)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) ReadCorpus(([]corpusEntry, error)) ([]corpusEntry, error)
```


**Тип ответа:** corpusEntry


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corpusEntry`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:94`



---


[function] name: ResetCoverage file: pkg/util/coverage/fake_test_deps.go:104 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### ResetCoverage (pkg/util/coverage/fake_test_deps.go:104)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) ResetCoverage(()) ()
```


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:104`



---


[function] name: RunFuzzWorker file: pkg/util/coverage/fake_test_deps.go:89 returns_error: да description: nolint:unused // U1000 see comment above, we know it's unused normally.


### RunFuzzWorker (pkg/util/coverage/fake_test_deps.go:89)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) RunFuzzWorker((func(corpusEntry) error)) (func(corpusEntry) error)
```


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corpusEntry


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `func(corpusEntry) error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:89`



---


[function] name: SetPanicOnExit0 file: pkg/util/coverage/fake_test_deps.go:55 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### SetPanicOnExit0 (pkg/util/coverage/fake_test_deps.go:55)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) SetPanicOnExit0((bool)) (bool)
```


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:55`



---


[function] name: SnapshotCoverage file: pkg/util/coverage/fake_test_deps.go:107 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### SnapshotCoverage (pkg/util/coverage/fake_test_deps.go:107)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) SnapshotCoverage(()) ()
```


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:107`



---


[function] name: StartCPUProfile file: pkg/util/coverage/fake_test_deps.go:58 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### StartCPUProfile (pkg/util/coverage/fake_test_deps.go:58)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) StartCPUProfile((io.Writer)) (io.Writer)
```


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:58`



---


[function] name: StartTestLog file: pkg/util/coverage/fake_test_deps.go:66 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### StartTestLog (pkg/util/coverage/fake_test_deps.go:66)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) StartTestLog((io.Writer)) (io.Writer)
```


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:66`



---


[function] name: StopCPUProfile file: pkg/util/coverage/fake_test_deps.go:63 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### StopCPUProfile (pkg/util/coverage/fake_test_deps.go:63)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) StopCPUProfile(()) ()
```


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:63`



---


[function] name: StopTestLog file: pkg/util/coverage/fake_test_deps.go:69 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### StopTestLog (pkg/util/coverage/fake_test_deps.go:69)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) StopTestLog(()) ()
```


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:69`



---


[function] name: WriteHeapProfile file: pkg/util/coverage/fake_test_deps.go:74 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### WriteHeapProfile (pkg/util/coverage/fake_test_deps.go:74)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) WriteHeapProfile((io.Writer)) (io.Writer)
```


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:74`



---


[function] name: WriteProfileTo file: pkg/util/coverage/fake_test_deps.go:79 returns_error: нет description: nolint:unused // U1000 see comment above, we know it's unused normally.


### WriteProfileTo (pkg/util/coverage/fake_test_deps.go:79)


nolint:unused // U1000 see comment above, we know it's unused normally.


```go
func (fakeTestDeps) WriteProfileTo((string, io.Writer, int)) (string, io.Writer, int)
```


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


📍 *Расположение:* `pkg/util/coverage/fake_test_deps.go:79`




## pkg/util/env/env.go


📄 Исходный файл: `pkg/util/env/env.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [GetEnvAsFloat64OrFallback](#getenvasfloat64orfallback-pkgutilenvenvgo48) `:48`

- 🔗 [GetEnvAsIntOrFallback](#getenvasintorfallback-pkgutilenvenvgo35) `:35`

- 🔗 [GetEnvAsStringOrFallback](#getenvasstringorfallback-pkgutilenvenvgo26) `:26`


</details>


[function] name: GetEnvAsFloat64OrFallback file: pkg/util/env/env.go:48 returns_error: да description: GetEnvAsFloat64OrFallback returns the env variable (parsed as float64) for
the given key and falls back to the given def


### GetEnvAsFloat64OrFallback (pkg/util/env/env.go:48)


GetEnvAsFloat64OrFallback returns the env variable (parsed as float64) for
the given key and falls back to the given defaultValue if not set


```go
func GetEnvAsFloat64OrFallback((float64, error)) (float64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `float64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/env/env.go:48`



---


[function] name: GetEnvAsIntOrFallback file: pkg/util/env/env.go:35 returns_error: да description: GetEnvAsIntOrFallback returns the env variable (parsed as integer) for
the given key and falls back to the given default


### GetEnvAsIntOrFallback (pkg/util/env/env.go:35)


GetEnvAsIntOrFallback returns the env variable (parsed as integer) for
the given key and falls back to the given defaultValue if not set


```go
func GetEnvAsIntOrFallback((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/env/env.go:35`



---


[function] name: GetEnvAsStringOrFallback file: pkg/util/env/env.go:26 returns_error: нет description: GetEnvAsStringOrFallback returns the env variable for the given key
and falls back to the given defaultValue if not set


### GetEnvAsStringOrFallback (pkg/util/env/env.go:26)


GetEnvAsStringOrFallback returns the env variable for the given key
and falls back to the given defaultValue if not set


```go
func GetEnvAsStringOrFallback((key, defaultValue string)) (key, defaultValue string)
```


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


**Тип ответа:** defaultValue


```json
{
  "InlineConstant": "string",
  "SymbolReference": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/defaulter-gen/generators/defaulter.go`


📍 *Расположение:* `pkg/util/env/env.go:26`




## pkg/util/filesystem/defaultfs.go


📄 Исходный файл: `pkg/util/filesystem/defaultfs.go`


<details open>
<summary><b>Функции в этом файле (19)</b></summary>


- 🔗 [Chtimes](#chtimes-pkgutilfilesystemdefaultfsgo106) `:106`

- 🔗 [Close](#close-pkgutilfilesystemdefaultfsgo170) `:170`

- 🔗 [Create](#create-pkgutilfilesystemdefaultfsgo56) `:56`

- 🔗 [MkdirAll](#mkdirall-pkgutilfilesystemdefaultfsgo75) `:75`

- 🔗 [MkdirAllWithPathCheck](#mkdirallwithpathcheck-pkgutilfilesystemdefaultfsgo87) `:87`

- 🔗 [Name](#name-pkgutilfilesystemdefaultfsgo155) `:155`

- 🔗 [NewTempFs](#newtempfs-pkgutilfilesystemdefaultfsgo36) `:36`

- 🔗 [ReadDir](#readdir-pkgutilfilesystemdefaultfsgo140) `:140`

- 🔗 [ReadFile](#readfile-pkgutilfilesystemdefaultfsgo121) `:121`

- 🔗 [Remove](#remove-pkgutilfilesystemdefaultfsgo116) `:116`

- 🔗 [RemoveAll](#removeall-pkgutilfilesystemdefaultfsgo111) `:111`

- 🔗 [Rename](#rename-pkgutilfilesystemdefaultfsgo65) `:65`

- 🔗 [Stat](#stat-pkgutilfilesystemdefaultfsgo51) `:51`

- 🔗 [Sync](#sync-pkgutilfilesystemdefaultfsgo165) `:165`

- 🔗 [TempDir](#tempdir-pkgutilfilesystemdefaultfsgo126) `:126`

- 🔗 [TempFile](#tempfile-pkgutilfilesystemdefaultfsgo131) `:131`

- 🔗 [Walk](#walk-pkgutilfilesystemdefaultfsgo145) `:145`

- 🔗 [Write](#write-pkgutilfilesystemdefaultfsgo160) `:160`

- 🔗 [prefix](#prefix-pkgutilfilesystemdefaultfsgo43) `:43`


</details>


[function] name: Chtimes file: pkg/util/filesystem/defaultfs.go:106 returns_error: нет description: Chtimes via os.Chtimes


### Chtimes (pkg/util/filesystem/defaultfs.go:106)


Chtimes via os.Chtimes


```go
func (fs *DefaultFs) Chtimes((name string, atime time.Time, mtime time.Time)) (name string, atime time.Time, mtime time.Time)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** atime


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Time


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** mtime


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Time


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:106`



---


[function] name: Close file: pkg/util/filesystem/defaultfs.go:170 returns_error: нет description: Close via os.File.Close


### Close (pkg/util/filesystem/defaultfs.go:170)


Close via os.File.Close


```go
func (file *defaultFile) Close(()) ()
```


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:170`



---


[function] name: Create file: pkg/util/filesystem/defaultfs.go:56 returns_error: да description: Create via os.Create


### Create (pkg/util/filesystem/defaultfs.go:56)


Create via os.Create


```go
func (fs *DefaultFs) Create((File, error)) (File, error)
```


**Тип ответа:** File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `File`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:56`



---


[function] name: MkdirAll file: pkg/util/filesystem/defaultfs.go:75 returns_error: нет description: —


### MkdirAll (pkg/util/filesystem/defaultfs.go:75)


MkdirAll is a method that performs operations based on the provided parameters and returns (path string, perm os.FileMode).


```go
func (fs *DefaultFs) MkdirAll((path string, perm os.FileMode)) (path string, perm os.FileMode)
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


**Тип ответа:** perm


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:75`



---


[function] name: MkdirAllWithPathCheck file: pkg/util/filesystem/defaultfs.go:87 returns_error: нет description: MkdirAllWithPathCheck checks if path exists already. If not, it creates a directory
named path, along with any necessary


### MkdirAllWithPathCheck (pkg/util/filesystem/defaultfs.go:87)


MkdirAllWithPathCheck checks if path exists already. If not, it creates a directory
named path, along with any necessary parents, and returns nil, or else returns an error.
Permission bits perm (before umask) are used for all directories that
MkdirAllWithPathCheck creates.
If path is already a directory, MkdirAllWithPathCheck does nothing and returns nil.
NOTE: In case of Windows NTFS, mount points are implemented as reparse-point
(similar to symlink) and do not represent actual directory. Hence Directory existence
check for windows NTFS will NOT check for dir, but for symlink presence.


```go
func MkdirAllWithPathCheck((path string, perm os.FileMode)) (path string, perm os.FileMode)
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


**Тип ответа:** perm


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:87`



---


[function] name: Name file: pkg/util/filesystem/defaultfs.go:155 returns_error: нет description: Name via os.File.Name


### Name (pkg/util/filesystem/defaultfs.go:155)


Name via os.File.Name


```go
func (file *defaultFile) Name(()) ()
```


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:155`



---


[function] name: NewTempFs file: pkg/util/filesystem/defaultfs.go:36 returns_error: нет description: NewTempFs returns a fake Filesystem in temporary directory, useful for unit tests


### NewTempFs (pkg/util/filesystem/defaultfs.go:36)


NewTempFs returns a fake Filesystem in temporary directory, useful for unit tests


```go
func NewTempFs(()) ()
```


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:36`



---


[function] name: ReadDir file: pkg/util/filesystem/defaultfs.go:140 returns_error: да description: ReadDir via os.ReadDir


### ReadDir (pkg/util/filesystem/defaultfs.go:140)


ReadDir via os.ReadDir


```go
func (fs *DefaultFs) ReadDir(([]os.DirEntry, error)) ([]os.DirEntry, error)
```


**Тип ответа:** os.DirEntry


```json
{
  "mock": null
}
```


*Определено в:* `pkg/kubelet/container/testing/mockdirentry.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]os.DirEntry`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:140`



---


[function] name: ReadFile file: pkg/util/filesystem/defaultfs.go:121 returns_error: да description: ReadFile via os.ReadFile


### ReadFile (pkg/util/filesystem/defaultfs.go:121)


ReadFile via os.ReadFile


```go
func (fs *DefaultFs) ReadFile(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:121`



---


[function] name: Remove file: pkg/util/filesystem/defaultfs.go:116 returns_error: нет description: Remove via os.Remove


### Remove (pkg/util/filesystem/defaultfs.go:116)


Remove via os.Remove


```go
func (fs *DefaultFs) Remove((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:116`



---


[function] name: RemoveAll file: pkg/util/filesystem/defaultfs.go:111 returns_error: нет description: RemoveAll via os.RemoveAll


### RemoveAll (pkg/util/filesystem/defaultfs.go:111)


RemoveAll via os.RemoveAll


```go
func (fs *DefaultFs) RemoveAll((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:111`



---


[function] name: Rename file: pkg/util/filesystem/defaultfs.go:65 returns_error: нет description: Rename via os.Rename


### Rename (pkg/util/filesystem/defaultfs.go:65)


Rename via os.Rename


```go
func (fs *DefaultFs) Rename((oldpath, newpath string)) (oldpath, newpath string)
```


**Тип ответа:** oldpath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newpath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:65`



---


[function] name: Stat file: pkg/util/filesystem/defaultfs.go:51 returns_error: да description: Stat via os.Stat


### Stat (pkg/util/filesystem/defaultfs.go:51)


Stat via os.Stat


```go
func (fs *DefaultFs) Stat((os.FileInfo, error)) (os.FileInfo, error)
```


**Тип ответа:** os.FileInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `os.FileInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:51`



---


[function] name: Sync file: pkg/util/filesystem/defaultfs.go:165 returns_error: нет description: Sync via os.File.Sync


### Sync (pkg/util/filesystem/defaultfs.go:165)


Sync via os.File.Sync


```go
func (file *defaultFile) Sync(()) ()
```


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:165`



---


[function] name: TempDir file: pkg/util/filesystem/defaultfs.go:126 returns_error: да description: TempDir via os.MkdirTemp


### TempDir (pkg/util/filesystem/defaultfs.go:126)


TempDir via os.MkdirTemp


```go
func (fs *DefaultFs) TempDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:126`



---


[function] name: TempFile file: pkg/util/filesystem/defaultfs.go:131 returns_error: да description: TempFile via os.CreateTemp


### TempFile (pkg/util/filesystem/defaultfs.go:131)


TempFile via os.CreateTemp


```go
func (fs *DefaultFs) TempFile((File, error)) (File, error)
```


**Тип ответа:** File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `File`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:131`



---


[function] name: Walk file: pkg/util/filesystem/defaultfs.go:145 returns_error: нет description: Walk via filepath.Walk


### Walk (pkg/util/filesystem/defaultfs.go:145)


Walk via filepath.Walk


```go
func (fs *DefaultFs) Walk((root string, walkFn filepath.WalkFunc)) (root string, walkFn filepath.WalkFunc)
```


**Тип ответа:** root


```json
{
  "client": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/openapi3/root.go`


**Тип ответа:** walkFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** filepath.WalkFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:145`



---


[function] name: Write file: pkg/util/filesystem/defaultfs.go:160 returns_error: да description: Write via os.File.Write


### Write (pkg/util/filesystem/defaultfs.go:160)


Write via os.File.Write


```go
func (file *defaultFile) Write((n int, err error)) (n int, err error)
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


*Типы возврата:* `n int`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:160`



---


[function] name: prefix file: pkg/util/filesystem/defaultfs.go:43 returns_error: нет description: —


### prefix (pkg/util/filesystem/defaultfs.go:43)


prefix is a method that performs operations based on the provided parameters and returns (path string).


```go
func (fs *DefaultFs) prefix((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/defaultfs.go:43`




## pkg/util/filesystem/util.go


📄 Исходный файл: `pkg/util/filesystem/util.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IsPathClean](#ispathclean-pkgutilfilesystemutilgo25) `:25`


</details>


[function] name: IsPathClean file: pkg/util/filesystem/util.go:25 returns_error: нет description: IsPathClean will replace slashes to Separator (which is OS-specific).
This will make sure that all slashes are the same 


### IsPathClean (pkg/util/filesystem/util.go:25)


IsPathClean will replace slashes to Separator (which is OS-specific).
This will make sure that all slashes are the same before comparing.


```go
func IsPathClean((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/util.go:25`




## pkg/util/filesystem/util_unix.go


📄 Исходный файл: `pkg/util/filesystem/util_unix.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Chmod](#chmod-pkgutilfilesystemutil_unixgo40) `:40`

- 🔗 [IsAbs](#isabs-pkgutilfilesystemutil_unixgo50) `:50`

- 🔗 [IsUnixDomainSocket](#isunixdomainsocket-pkgutilfilesystemutil_unixgo28) `:28`

- 🔗 [MkdirAll](#mkdirall-pkgutilfilesystemutil_unixgo45) `:45`


</details>


[function] name: Chmod file: pkg/util/filesystem/util_unix.go:40 returns_error: нет description: Chmod is the same as os.Chmod on Unix.


### Chmod (pkg/util/filesystem/util_unix.go:40)


Chmod is the same as os.Chmod on Unix.


```go
func Chmod((name string, mode os.FileMode)) (name string, mode os.FileMode)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/util_unix.go:40`



---


[function] name: IsAbs file: pkg/util/filesystem/util_unix.go:50 returns_error: нет description: IsAbs is same as filepath.IsAbs on Unix.


### IsAbs (pkg/util/filesystem/util_unix.go:50)


IsAbs is same as filepath.IsAbs on Unix.


```go
func IsAbs((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/util_unix.go:50`



---


[function] name: IsUnixDomainSocket file: pkg/util/filesystem/util_unix.go:28 returns_error: да description: IsUnixDomainSocket returns whether a given file is a AF_UNIX socket file


### IsUnixDomainSocket (pkg/util/filesystem/util_unix.go:28)


IsUnixDomainSocket returns whether a given file is a AF_UNIX socket file


```go
func IsUnixDomainSocket((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/util_unix.go:28`



---


[function] name: MkdirAll file: pkg/util/filesystem/util_unix.go:45 returns_error: нет description: MkdirAll is same as os.MkdirAll on Unix.


### MkdirAll (pkg/util/filesystem/util_unix.go:45)


MkdirAll is same as os.MkdirAll on Unix.


```go
func MkdirAll((path string, perm os.FileMode)) (path string, perm os.FileMode)
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


**Тип ответа:** perm


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/util_unix.go:45`




## pkg/util/filesystem/util_windows.go


📄 Исходный файл: `pkg/util/filesystem/util_windows.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Chmod](#chmod-pkgutilfilesystemutil_windowsgo141) `:141`

- 🔗 [IsAbs](#isabs-pkgutilfilesystemutil_windowsgo260) `:260`

- 🔗 [IsUnixDomainSocket](#isunixdomainsocket-pkgutilfilesystemutil_windowsgo47) `:47`

- 🔗 [MkdirAll](#mkdirall-pkgutilfilesystemutil_windowsgo95) `:95`


</details>


[function] name: Chmod file: pkg/util/filesystem/util_windows.go:141 returns_error: нет description: On Windows os.Chmod only sets the read-only flag on files, so we need to use Windows APIs to set the desired access on f


### Chmod (pkg/util/filesystem/util_windows.go:141)


On Windows os.Chmod only sets the read-only flag on files, so we need to use Windows APIs to set the desired access on files / directories.
The OWNER mode will set file permissions for the file owner SID, the GROUP mode will set file permissions for the file group SID,
and the OTHERS mode will set file permissions for BUILTIN\Users.
Please note that Windows containers can be run as one of two user accounts; ContainerUser or ContainerAdministrator.
Containers run as ContainerAdministrator will inherit permissions from BUILTIN\Administrators,
while containers run as ContainerUser will inherit permissions from BUILTIN\Users.
Windows containers do not have the ability to run as a custom user account that is known to the host so the OTHERS group mode
is used to grant / deny permissions of files on the hosts to the ContainerUser account.


```go
func Chmod((path string, filemode os.FileMode)) (path string, filemode os.FileMode)
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


**Тип ответа:** filemode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/util_windows.go:141`



---


[function] name: IsAbs file: pkg/util/filesystem/util_windows.go:260 returns_error: нет description: IsAbs returns whether the given path is absolute or not.
On Windows, filepath.IsAbs will not return True for paths prefi


### IsAbs (pkg/util/filesystem/util_windows.go:260)


IsAbs returns whether the given path is absolute or not.
On Windows, filepath.IsAbs will not return True for paths prefixed with a slash, even
though they can be used as absolute paths (https://docs.microsoft.com/en-us/dotnet/standard/io/file-path-formats).

WARN: It isn't safe to use this for API values which will propagate across systems (e.g. REST API values
that get validated on Unix, persisted, then consumed by Windows, etc).


```go
func IsAbs((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/util_windows.go:260`



---


[function] name: IsUnixDomainSocket file: pkg/util/filesystem/util_windows.go:47 returns_error: да description: IsUnixDomainSocket returns whether a given file is a AF_UNIX socket file
Note that due to the retry logic inside, it cou


### IsUnixDomainSocket (pkg/util/filesystem/util_windows.go:47)


IsUnixDomainSocket returns whether a given file is a AF_UNIX socket file
Note that due to the retry logic inside, it could take up to 4 seconds
to determine whether or not the file path supplied is a Unix domain socket


```go
func IsUnixDomainSocket((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/util_windows.go:47`



---


[function] name: MkdirAll file: pkg/util/filesystem/util_windows.go:95 returns_error: нет description: On Windows os.Mkdir all doesn't set any permissions so call the Chown function below to set
permissions once the directo


### MkdirAll (pkg/util/filesystem/util_windows.go:95)


On Windows os.Mkdir all doesn't set any permissions so call the Chown function below to set
permissions once the directory is created.


```go
func MkdirAll((path string, perm os.FileMode)) (path string, perm os.FileMode)
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


**Тип ответа:** perm


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/util_windows.go:95`




## pkg/util/filesystem/watcher.go


📄 Исходный файл: `pkg/util/filesystem/watcher.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Add](#add-pkgutilfilesystemwatchergo101) `:101`

- 🔗 [AddWatch](#addwatch-pkgutilfilesystemwatchergo61) `:61`

- 🔗 [Init](#init-pkgutilfilesystemwatchergo65) `:65`

- 🔗 [NewFsnotifyWatcher](#newfsnotifywatcher-pkgutilfilesystemwatchergo57) `:57`

- 🔗 [Remove](#remove-pkgutilfilesystemwatchergo102) `:102`

- 🔗 [Run](#run-pkgutilfilesystemwatchergo77) `:77`

- 🔗 [WatchUntil](#watchuntil-pkgutilfilesystemwatchergo117) `:117`


</details>


[function] name: Add file: pkg/util/filesystem/watcher.go:101 returns_error: нет description: —


### Add (pkg/util/filesystem/watcher.go:101)


Add is a method that creates new data based on the provided parameters and returns (path string).


```go
func (noopWatcher) Add((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/watcher.go:101`



---


[function] name: AddWatch file: pkg/util/filesystem/watcher.go:61 returns_error: нет description: —


### AddWatch (pkg/util/filesystem/watcher.go:61)


AddWatch is a method that creates new data based on the provided parameters and returns (path string).


```go
func (w *fsnotifyWatcher) AddWatch((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/watcher.go:61`



---


[function] name: Init file: pkg/util/filesystem/watcher.go:65 returns_error: нет description: —


### Init (pkg/util/filesystem/watcher.go:65)


Init is a method that performs operations based on the provided parameters and may return an error.


```go
func (w *fsnotifyWatcher) Init((eventHandler FSEventHandler, errorHandler FSErrorHandler)) (eventHandler FSEventHandler, errorHandler FSErrorHandler)
```


**Тип ответа:** eventHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FSEventHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errorHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FSErrorHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/filesystem/watcher.go:65`



---


[function] name: NewFsnotifyWatcher file: pkg/util/filesystem/watcher.go:57 returns_error: нет description: NewFsnotifyWatcher returns an implementation of FSWatcher that continuously listens for
fsnotify events and calls the ev


### NewFsnotifyWatcher (pkg/util/filesystem/watcher.go:57)


NewFsnotifyWatcher returns an implementation of FSWatcher that continuously listens for
fsnotify events and calls the event handler as soon as an event is received.


```go
func NewFsnotifyWatcher(()) ()
```


📍 *Расположение:* `pkg/util/filesystem/watcher.go:57`



---


[function] name: Remove file: pkg/util/filesystem/watcher.go:102 returns_error: нет description: —


### Remove (pkg/util/filesystem/watcher.go:102)


Remove is a method that deletes data based on the provided parameters and returns (path string).


```go
func (noopWatcher) Remove((path string)) (path string)
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


📍 *Расположение:* `pkg/util/filesystem/watcher.go:102`



---


[function] name: Run file: pkg/util/filesystem/watcher.go:77 returns_error: нет description: —


### Run (pkg/util/filesystem/watcher.go:77)


Run is a method that performs operations based on the provided parameters and returns ().


```go
func (w *fsnotifyWatcher) Run(()) ()
```


📍 *Расположение:* `pkg/util/filesystem/watcher.go:77`



---


[function] name: WatchUntil file: pkg/util/filesystem/watcher.go:117 returns_error: да description: WatchUntil watches the specified path for changes and blocks until ctx is canceled.
eventHandler() must be non-nil, and 


### WatchUntil (pkg/util/filesystem/watcher.go:117)


WatchUntil watches the specified path for changes and blocks until ctx is canceled.
eventHandler() must be non-nil, and pollInterval must be greater than 0.
eventHandler() is invoked whenever a change event is observed or pollInterval elapses.
errorHandler() is invoked (if non-nil) whenever an error occurs initializing or watching the specified path.

If path is a directory, only the directory and immediate children are watched.

If path does not exist or cannot be watched, an error is passed to errorHandler() and eventHandler() is called at pollInterval.

Multiple observed events may collapse to a single invocation of eventHandler().

eventHandler() is invoked immediately after successful initialization of the filesystem watch,
in case the path changed concurrent with calling WatchUntil().


```go
func WatchUntil((ctx context.Context, pollInterval time.Duration, path string, eventHandler func(), errorHandler func(err error))) (ctx context.Context, pollInterval time.Duration, path string, eventHandler func(), errorHandler func(err error))
```


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


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


**Тип ответа:** eventHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errorHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


*Типы возврата:* `ctx context.Context`, `pollInterval time.Duration`, `path string`, `eventHandler func()`, `errorHandler func(err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/filesystem/watcher.go:117`




## pkg/util/flag/flags.go


📄 Исходный файл: `pkg/util/flag/flags.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [Set](#set-pkgutilflagflagsgo53) `:53`

- 🔗 [Set](#set-pkgutilflagflagsgo88) `:88`

- 🔗 [Set](#set-pkgutilflagflagsgo140) `:140`

- 🔗 [Set](#set-pkgutilflagflagsgo172) `:172`

- 🔗 [Set](#set-pkgutilflagflagsgo266) `:266`

- 🔗 [String](#string-pkgutilflagflagsgo70) `:70`

- 🔗 [String](#string-pkgutilflagflagsgo122) `:122`

- 🔗 [String](#string-pkgutilflagflagsgo153) `:153`

- 🔗 [String](#string-pkgutilflagflagsgo235) `:235`

- 🔗 [String](#string-pkgutilflagflagsgo289) `:289`

- 🔗 [Type](#type-pkgutilflagflagsgo78) `:78`

- 🔗 [Type](#type-pkgutilflagflagsgo130) `:130`

- 🔗 [Type](#type-pkgutilflagflagsgo161) `:161`

- 🔗 [Type](#type-pkgutilflagflagsgo256) `:256`

- 🔗 [Type](#type-pkgutilflagflagsgo301) `:301`


</details>


[function] name: Set file: pkg/util/flag/flags.go:53 returns_error: нет description: Set sets the flag value


### Set (pkg/util/flag/flags.go:53)


Set sets the flag value


```go
func (v *IPVar) Set((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/flag/flags.go:53`



---


[function] name: Set file: pkg/util/flag/flags.go:88 returns_error: нет description: Set sets the flag value


### Set (pkg/util/flag/flags.go:88)


Set sets the flag value


```go
func (v *IPPortVar) Set((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/flag/flags.go:88`



---


[function] name: Set file: pkg/util/flag/flags.go:140 returns_error: нет description: Set sets the flag value


### Set (pkg/util/flag/flags.go:140)


Set sets the flag value


```go
func (v PortRangeVar) Set((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/flag/flags.go:140`



---


[function] name: Set file: pkg/util/flag/flags.go:172 returns_error: нет description: Set sets the flag value


### Set (pkg/util/flag/flags.go:172)


Set sets the flag value


```go
func (v *ReservedMemoryVar) Set((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/flag/flags.go:172`



---


[function] name: Set file: pkg/util/flag/flags.go:266 returns_error: нет description: Set sets the flag value


### Set (pkg/util/flag/flags.go:266)


Set sets the flag value


```go
func (t RegisterWithTaintsVar) Set((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/flag/flags.go:266`



---


[function] name: String file: pkg/util/flag/flags.go:70 returns_error: нет description: String returns the flag value


### String (pkg/util/flag/flags.go:70)


String returns the flag value


```go
func (v *IPVar) String(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:70`



---


[function] name: String file: pkg/util/flag/flags.go:122 returns_error: нет description: String returns the flag value


### String (pkg/util/flag/flags.go:122)


String returns the flag value


```go
func (v *IPPortVar) String(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:122`



---


[function] name: String file: pkg/util/flag/flags.go:153 returns_error: нет description: String returns the flag value


### String (pkg/util/flag/flags.go:153)


String returns the flag value


```go
func (v PortRangeVar) String(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:153`



---


[function] name: String file: pkg/util/flag/flags.go:235 returns_error: нет description: String returns the flag value


### String (pkg/util/flag/flags.go:235)


String returns the flag value


```go
func (v *ReservedMemoryVar) String(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:235`



---


[function] name: String file: pkg/util/flag/flags.go:289 returns_error: нет description: String returns the flag value


### String (pkg/util/flag/flags.go:289)


String returns the flag value


```go
func (t RegisterWithTaintsVar) String(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:289`



---


[function] name: Type file: pkg/util/flag/flags.go:78 returns_error: нет description: Type gets the flag type


### Type (pkg/util/flag/flags.go:78)


Type gets the flag type


```go
func (v *IPVar) Type(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:78`



---


[function] name: Type file: pkg/util/flag/flags.go:130 returns_error: нет description: Type gets the flag type


### Type (pkg/util/flag/flags.go:130)


Type gets the flag type


```go
func (v *IPPortVar) Type(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:130`



---


[function] name: Type file: pkg/util/flag/flags.go:161 returns_error: нет description: Type gets the flag type


### Type (pkg/util/flag/flags.go:161)


Type gets the flag type


```go
func (v PortRangeVar) Type(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:161`



---


[function] name: Type file: pkg/util/flag/flags.go:256 returns_error: нет description: Type gets the flag type


### Type (pkg/util/flag/flags.go:256)


Type gets the flag type


```go
func (v *ReservedMemoryVar) Type(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:256`



---


[function] name: Type file: pkg/util/flag/flags.go:301 returns_error: нет description: Type gets the flag type


### Type (pkg/util/flag/flags.go:301)


Type gets the flag type


```go
func (t RegisterWithTaintsVar) Type(()) ()
```


📍 *Расположение:* `pkg/util/flag/flags.go:301`




## pkg/util/flock/flock_other.go


📄 Исходный файл: `pkg/util/flock/flock_other.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Acquire](#acquire-pkgutilflockflock_othergo22) `:22`


</details>


[function] name: Acquire file: pkg/util/flock/flock_other.go:22 returns_error: нет description: Acquire is not implemented on non-unix systems.


### Acquire (pkg/util/flock/flock_other.go:22)


Acquire is not implemented on non-unix systems.


```go
func Acquire((path string)) (path string)
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


📍 *Расположение:* `pkg/util/flock/flock_other.go:22`




## pkg/util/flock/flock_unix.go


📄 Исходный файл: `pkg/util/flock/flock_unix.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Acquire](#acquire-pkgutilflockflock_unixgo25) `:25`


</details>


[function] name: Acquire file: pkg/util/flock/flock_unix.go:25 returns_error: нет description: Acquire acquires a lock on a file for the duration of the process. This method
is reentrant.


### Acquire (pkg/util/flock/flock_unix.go:25)


Acquire acquires a lock on a file for the duration of the process. This method
is reentrant.


```go
func Acquire((path string)) (path string)
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


📍 *Расположение:* `pkg/util/flock/flock_unix.go:25`




## pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go


📄 Исходный файл: `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Error](#error-pkgutilgoroutinemapexponentialbackoffexponential_backoffgo113) `:113`

- 🔗 [GenerateNoRetriesPermittedMsg](#generatenoretriespermittedmsg-pkgutilgoroutinemapexponentialbackoffexponential_backoffgo72) `:72`

- 🔗 [IsExponentialBackoff](#isexponentialbackoff-pkgutilgoroutinemapexponentialbackoffexponential_backoffgo93) `:93`

- 🔗 [NewExponentialBackoffError](#newexponentialbackofferror-pkgutilgoroutinemapexponentialbackoffexponential_backoffgo81) `:81`

- 🔗 [SafeToRetry](#safetoretry-pkgutilgoroutinemapexponentialbackoffexponential_backoffgo50) `:50`

- 🔗 [Update](#update-pkgutilgoroutinemapexponentialbackoffexponential_backoffgo58) `:58`


</details>


[function] name: Error file: pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:113 returns_error: нет description: —


### Error (pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:113)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (err exponentialBackoffError) Error(()) ()
```


📍 *Расположение:* `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:113`



---


[function] name: GenerateNoRetriesPermittedMsg file: pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:72 returns_error: нет description: —


### GenerateNoRetriesPermittedMsg (pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:72)


GenerateNoRetriesPermittedMsg is a method that performs operations based on the provided parameters and returns (operationName string).


```go
func (expBackoff *ExponentialBackoff) GenerateNoRetriesPermittedMsg((operationName string)) (operationName string)
```


**Тип ответа:** operationName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:72`



---


[function] name: IsExponentialBackoff file: pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:93 returns_error: да description: IsExponentialBackoff returns true if an error returned from GoroutineMap
indicates that a new operation can not be start


### IsExponentialBackoff (pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:93)


IsExponentialBackoff returns true if an error returned from GoroutineMap
indicates that a new operation can not be started because
exponentialBackOffOnError is enabled and a previous operation with the same
operation failed within the durationBeforeRetry period.


```go
func IsExponentialBackoff((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:93`



---


[function] name: NewExponentialBackoffError file: pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:81 returns_error: нет description: NewExponentialBackoffError returns a new instance of ExponentialBackoff error.


### NewExponentialBackoffError (pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:81)


NewExponentialBackoffError returns a new instance of ExponentialBackoff error.


```go
func NewExponentialBackoffError((
	operationName string, expBackoff ExponentialBackoff)) (
	operationName string, expBackoff ExponentialBackoff)
```


**Тип ответа:** operationName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** expBackoff


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ExponentialBackoff


```json
{
  "lastError": {},
  "lastErrorTime": {},
  "durationBeforeRetry": {}
}
```


*Определено в:* `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go`


📍 *Расположение:* `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:81`



---


[function] name: SafeToRetry file: pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:50 returns_error: нет description: SafeToRetry returns an error if the durationBeforeRetry period for the given
lastErrorTime has not yet expired. Otherwis


### SafeToRetry (pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:50)


SafeToRetry returns an error if the durationBeforeRetry period for the given
lastErrorTime has not yet expired. Otherwise it returns nil.


```go
func (expBackoff *ExponentialBackoff) SafeToRetry((operationName string)) (operationName string)
```


**Тип ответа:** operationName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:50`



---


[function] name: Update file: pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:58 returns_error: да description: —


### Update (pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:58)


Update is a method that updates data based on the provided parameters and may return an error.


```go
func (expBackoff *ExponentialBackoff) Update((err *error)) (err *error)
```


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


*Типы возврата:* `err *error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/util/goroutinemap/exponentialbackoff/exponential_backoff.go:58`




## pkg/util/goroutinemap/goroutinemap.go


📄 Исходный файл: `pkg/util/goroutinemap/goroutinemap.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Error](#error-pkgutilgoroutinemapgoroutinemapgo226) `:226`

- 🔗 [IsAlreadyExists](#isalreadyexists-pkgutilgoroutinemapgoroutinemapgo208) `:208`

- 🔗 [IsOperationPending](#isoperationpending-pkgutilgoroutinemapgoroutinemapgo155) `:155`

- 🔗 [NewAlreadyExistsError](#newalreadyexistserror-pkgutilgoroutinemapgoroutinemapgo201) `:201`

- 🔗 [NewGoRoutineMap](#newgoroutinemap-pkgutilgoroutinemapgoroutinemapgo63) `:63`

- 🔗 [Run](#run-pkgutilgoroutinemapgoroutinemapgo86) `:86`

- 🔗 [Wait](#wait-pkgutilgoroutinemapgoroutinemapgo165) `:165`

- 🔗 [WaitForCompletion](#waitforcompletion-pkgutilgoroutinemapgoroutinemapgo174) `:174`

- 🔗 [nothingPending](#nothingpending-pkgutilgoroutinemapgoroutinemapgo189) `:189`

- 🔗 [operationComplete](#operationcomplete-pkgutilgoroutinemapgoroutinemapgo123) `:123`


</details>


[function] name: Error file: pkg/util/goroutinemap/goroutinemap.go:226 returns_error: нет description: —


### Error (pkg/util/goroutinemap/goroutinemap.go:226)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (err alreadyExistsError) Error(()) ()
```


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:226`



---


[function] name: IsAlreadyExists file: pkg/util/goroutinemap/goroutinemap.go:208 returns_error: да description: IsAlreadyExists returns true if an error returned from GoRoutineMap indicates
a new operation can not be started because


### IsAlreadyExists (pkg/util/goroutinemap/goroutinemap.go:208)


IsAlreadyExists returns true if an error returned from GoRoutineMap indicates
a new operation can not be started because an operation with the same
operation name is already executing.


```go
func IsAlreadyExists((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:208`



---


[function] name: IsOperationPending file: pkg/util/goroutinemap/goroutinemap.go:155 returns_error: нет description: —


### IsOperationPending (pkg/util/goroutinemap/goroutinemap.go:155)


IsOperationPending is a method that performs operations based on the provided parameters and returns (operationName string).


```go
func (grm *goRoutineMap) IsOperationPending((operationName string)) (operationName string)
```


**Тип ответа:** operationName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:155`



---


[function] name: NewAlreadyExistsError file: pkg/util/goroutinemap/goroutinemap.go:201 returns_error: нет description: NewAlreadyExistsError returns a new instance of AlreadyExists error.


### NewAlreadyExistsError (pkg/util/goroutinemap/goroutinemap.go:201)


NewAlreadyExistsError returns a new instance of AlreadyExists error.


```go
func NewAlreadyExistsError((operationName string)) (operationName string)
```


**Тип ответа:** operationName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:201`



---


[function] name: NewGoRoutineMap file: pkg/util/goroutinemap/goroutinemap.go:63 returns_error: нет description: NewGoRoutineMap returns a new instance of GoRoutineMap.


### NewGoRoutineMap (pkg/util/goroutinemap/goroutinemap.go:63)


NewGoRoutineMap returns a new instance of GoRoutineMap.


```go
func NewGoRoutineMap((exponentialBackOffOnError bool)) (exponentialBackOffOnError bool)
```


**Тип ответа:** exponentialBackOffOnError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:63`



---


[function] name: Run file: pkg/util/goroutinemap/goroutinemap.go:86 returns_error: да description: —


### Run (pkg/util/goroutinemap/goroutinemap.go:86)


Run is a method that performs operations based on the provided parameters and may return an error.


```go
func (grm *goRoutineMap) Run((
	operationName string,
	operationFunc func() error)) (
	operationName string,
	operationFunc func() error)
```


**Тип ответа:** operationName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** operationFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `operationName string`, `operationFunc func() error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:86`



---


[function] name: Wait file: pkg/util/goroutinemap/goroutinemap.go:165 returns_error: нет description: —


### Wait (pkg/util/goroutinemap/goroutinemap.go:165)


Wait is a method that performs operations based on the provided parameters and returns ().


```go
func (grm *goRoutineMap) Wait(()) ()
```


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:165`



---


[function] name: WaitForCompletion file: pkg/util/goroutinemap/goroutinemap.go:174 returns_error: нет description: —


### WaitForCompletion (pkg/util/goroutinemap/goroutinemap.go:174)


WaitForCompletion is a method that performs operations based on the provided parameters and returns ().


```go
func (grm *goRoutineMap) WaitForCompletion(()) ()
```


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:174`



---


[function] name: nothingPending file: pkg/util/goroutinemap/goroutinemap.go:189 returns_error: нет description: Check if any operation is pending. Already assumes caller has the
necessary locks


### nothingPending (pkg/util/goroutinemap/goroutinemap.go:189)


Check if any operation is pending. Already assumes caller has the
necessary locks


```go
func (grm *goRoutineMap) nothingPending(()) ()
```


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:189`



---


[function] name: operationComplete file: pkg/util/goroutinemap/goroutinemap.go:123 returns_error: да description: operationComplete handles the completion of a goroutine run in the
goRoutineMap.


### operationComplete (pkg/util/goroutinemap/goroutinemap.go:123)


operationComplete handles the completion of a goroutine run in the
goRoutineMap.


```go
func (grm *goRoutineMap) operationComplete((
	operationName string, err *error)) (
	operationName string, err *error)
```


**Тип ответа:** operationName


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


*Типы возврата:* `operationName string`, `err *error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/goroutinemap/goroutinemap.go:123`




## pkg/util/hash/hash.go


📄 Исходный файл: `pkg/util/hash/hash.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DeepHashObject](#deephashobject-pkgutilhashhashgo29) `:29`


</details>


[function] name: DeepHashObject file: pkg/util/hash/hash.go:29 returns_error: нет description: DeepHashObject writes specified object to hash using the spew library
which follows pointers and prints actual values of


### DeepHashObject (pkg/util/hash/hash.go:29)


DeepHashObject writes specified object to hash using the spew library
which follows pointers and prints actual values of the nested objects
ensuring the hash does not change when a pointer changes.


```go
func DeepHashObject((hasher hash.Hash, objectToWrite interface{})) (hasher hash.Hash, objectToWrite interface{})
```


**Тип ответа:** hasher


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hash.Hash


```json
{
  "jwtIssuerHash": "string",
  "apiServerIDHash": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/metrics.go`


**Тип ответа:** objectToWrite


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/util/hash/hash.go:29`




## pkg/util/interrupt/interrupt.go


📄 Исходный файл: `pkg/util/interrupt/interrupt.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Close](#close-pkgutilinterruptinterruptgo51) `:51`

- 🔗 [New](#new-pkgutilinterruptinterruptgo43) `:43`

- 🔗 [Run](#run-pkgutilinterruptinterruptgo77) `:77`

- 🔗 [Signal](#signal-pkgutilinterruptinterruptgo62) `:62`


</details>


[function] name: Close file: pkg/util/interrupt/interrupt.go:51 returns_error: нет description: Close executes all the notification handlers if they have not yet been executed.


### Close (pkg/util/interrupt/interrupt.go:51)


Close executes all the notification handlers if they have not yet been executed.


```go
func (h *Handler) Close(()) ()
```


📍 *Расположение:* `pkg/util/interrupt/interrupt.go:51`



---


[function] name: New file: pkg/util/interrupt/interrupt.go:43 returns_error: нет description: New creates a new handler that guarantees all notify functions are run after the critical
section exits (or is interrupt


### New (pkg/util/interrupt/interrupt.go:43)


New creates a new handler that guarantees all notify functions are run after the critical
section exits (or is interrupted by the OS), then invokes the final handler. If no final
handler is specified, the default final is `os.Exit(1)`. A handler can only be used for
one critical section.


```go
func New((final func(os.Signal), notify ...func())) (final func(os.Signal), notify ...func())
```


**Тип ответа:** final


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** os.Signal


```json
{
  "once": {},
  "done": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_context.go`


**Тип ответа:** notify


```json
{
  "watcher": null,
  "eventHandler": {},
  "errorHandler": {}
}
```


*Определено в:* `pkg/util/filesystem/watcher.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/interrupt/interrupt.go:43`



---


[function] name: Run file: pkg/util/interrupt/interrupt.go:77 returns_error: да description: Run ensures that any notifications are invoked after the provided fn exits (even if the
process is interrupted by an OS 


### Run (pkg/util/interrupt/interrupt.go:77)


Run ensures that any notifications are invoked after the provided fn exits (even if the
process is interrupted by an OS termination signal). Notifications are only invoked once
per Handler instance, so calling Run more than once will not behave as the user expects.


```go
func (h *Handler) Run((fn func() error)) (fn func() error)
```


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `fn func() error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/util/interrupt/interrupt.go:77`



---


[function] name: Signal file: pkg/util/interrupt/interrupt.go:62 returns_error: нет description: Signal is called when an os.Signal is received, and guarantees that all notifications
are executed, then the final handl


### Signal (pkg/util/interrupt/interrupt.go:62)


Signal is called when an os.Signal is received, and guarantees that all notifications
are executed, then the final handler is executed. This function should only be called once
per Handler instance.


```go
func (h *Handler) Signal((s os.Signal)) (s os.Signal)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** os.Signal


```json
{
  "once": {},
  "done": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_context.go`


📍 *Расположение:* `pkg/util/interrupt/interrupt.go:62`




## pkg/util/iptables/iptables.go


📄 Исходный файл: `pkg/util/iptables/iptables.go`


<details open>
<summary><b>Функции в этом файле (39)</b></summary>


- 🔗 [ChainExists](#chainexists-pkgutiliptablesiptablesgo640) `:640`

- 🔗 [DeleteChain](#deletechain-pkgutiliptablesiptablesgo305) `:305`

- 🔗 [DeleteRule](#deleterule-pkgutiliptablesiptablesgo340) `:340`

- 🔗 [EnsureChain](#ensurechain-pkgutiliptablesiptablesgo272) `:272`

- 🔗 [EnsureRule](#ensurerule-pkgutiliptablesiptablesgo319) `:319`

- 🔗 [Error](#error-pkgutiliptablesiptablesgo829) `:829`

- 🔗 [ExtractLines](#extractlines-pkgutiliptablesiptablesgo868) `:868`

- 🔗 [FlushChain](#flushchain-pkgutiliptablesiptablesgo291) `:291`

- 🔗 [HasRandomFully](#hasrandomfully-pkgutiliptablesiptablesgo749) `:749`

- 🔗 [IsIPv6](#isipv6-pkgutiliptablesiptablesgo360) `:360`

- 🔗 [IsNotFoundError](#isnotfounderror-pkgutiliptablesiptablesgo789) `:789`

- 🔗 [Line](#line-pkgutiliptablesiptablesgo825) `:825`

- 🔗 [Monitor](#monitor-pkgutiliptablesiptablesgo590) `:590`

- 🔗 [New](#new-pkgutiliptablesiptablesgo245) `:245`

- 🔗 [NewBestEffort](#newbesteffort-pkgutiliptablesiptablesgo267) `:267`

- 🔗 [Present](#present-pkgutiliptablesiptablesgo755) `:755`

- 🔗 [Protocol](#protocol-pkgutiliptablesiptablesgo364) `:364`

- 🔗 [Restore](#restore-pkgutiliptablesiptablesgo393) `:393`

- 🔗 [RestoreAll](#restoreall-pkgutiliptablesiptablesgo400) `:400`

- 🔗 [SaveInto](#saveinto-pkgutiliptablesiptablesgo369) `:369`

- 🔗 [checkRule](#checkrule-pkgutiliptablesiptablesgo497) `:497`

- 🔗 [checkRuleUsingCheck](#checkruleusingcheck-pkgutiliptablesiptablesgo561) `:561`

- 🔗 [checkRuleWithoutCheck](#checkrulewithoutcheck-pkgutiliptablesiptablesgo513) `:513`

- 🔗 [getIPTablesRestoreVersionString](#getiptablesrestoreversionstring-pkgutiliptablesiptablesgo728) `:728`

- 🔗 [getIPTablesRestoreWaitFlag](#getiptablesrestorewaitflag-pkgutiliptablesiptablesgo707) `:707`

- 🔗 [getIPTablesVersion](#getiptablesversion-pkgutiliptablesiptablesgo674) `:674`

- 🔗 [getIPTablesWaitFlag](#getiptableswaitflag-pkgutiliptablesiptablesgo695) `:695`

- 🔗 [iptablesCommand](#iptablescommand-pkgutiliptablesiptablesgo472) `:472`

- 🔗 [iptablesRestoreCommand](#iptablesrestorecommand-pkgutiliptablesiptablesgo465) `:465`

- 🔗 [iptablesSaveCommand](#iptablessavecommand-pkgutiliptablesiptablesgo458) `:458`

- 🔗 [isResourceError](#isresourceerror-pkgutiliptablesiptablesgo804) `:804`

- 🔗 [makeFullArgs](#makefullargs-pkgutiliptablesiptablesgo667) `:667`

- 🔗 [newDualStackInternal](#newdualstackinternal-pkgutiliptablesiptablesgo249) `:249`

- 🔗 [newInternal](#newinternal-pkgutiliptablesiptablesgo212) `:212`

- 🔗 [parseRestoreError](#parserestoreerror-pkgutiliptablesiptablesgo849) `:849`

- 🔗 [restoreInternal](#restoreinternal-pkgutiliptablesiptablesgo411) `:411`

- 🔗 [run](#run-pkgutiliptablesiptablesgo479) `:479`

- 🔗 [runContext](#runcontext-pkgutiliptablesiptablesgo483) `:483`

- 🔗 [trimhex](#trimhex-pkgutiliptablesiptablesgo506) `:506`


</details>


[function] name: ChainExists file: pkg/util/iptables/iptables.go:640 returns_error: да description: ChainExists is part of Interface


### ChainExists (pkg/util/iptables/iptables.go:640)


ChainExists is part of Interface


```go
func (runner *runner) ChainExists((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:640`



---


[function] name: DeleteChain file: pkg/util/iptables/iptables.go:305 returns_error: нет description: DeleteChain is part of Interface.


### DeleteChain (pkg/util/iptables/iptables.go:305)


DeleteChain is part of Interface.


```go
func (runner *runner) DeleteChain((table Table, chain Chain)) (table Table, chain Chain)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:305`



---


[function] name: DeleteRule file: pkg/util/iptables/iptables.go:340 returns_error: нет description: DeleteRule is part of Interface.


### DeleteRule (pkg/util/iptables/iptables.go:340)


DeleteRule is part of Interface.


```go
func (runner *runner) DeleteRule((table Table, chain Chain, args ...string)) (table Table, chain Chain, args ...string)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/iptables.go:340`



---


[function] name: EnsureChain file: pkg/util/iptables/iptables.go:272 returns_error: да description: EnsureChain is part of Interface.


### EnsureChain (pkg/util/iptables/iptables.go:272)


EnsureChain is part of Interface.


```go
func (runner *runner) EnsureChain((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:272`



---


[function] name: EnsureRule file: pkg/util/iptables/iptables.go:319 returns_error: да description: EnsureRule is part of Interface.


### EnsureRule (pkg/util/iptables/iptables.go:319)


EnsureRule is part of Interface.


```go
func (runner *runner) EnsureRule((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:319`



---


[function] name: Error file: pkg/util/iptables/iptables.go:829 returns_error: нет description: —


### Error (pkg/util/iptables/iptables.go:829)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e parseError) Error(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables.go:829`



---


[function] name: ExtractLines file: pkg/util/iptables/iptables.go:868 returns_error: нет description: ExtractLines extracts the -count and +count data from the lineNum row of lines and return
NOTE: lines start from line 1


### ExtractLines (pkg/util/iptables/iptables.go:868)


ExtractLines extracts the -count and +count data from the lineNum row of lines and return
NOTE: lines start from line 1


```go
func ExtractLines((lines []byte, line, count int)) (lines []byte, line, count int)
```


**Тип ответа:** lines


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** line


```json
{
  "wrap": 0,
  "words": []
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/explain/formatter.go`


**Тип ответа:** count


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:868`



---


[function] name: FlushChain file: pkg/util/iptables/iptables.go:291 returns_error: нет description: FlushChain is part of Interface.


### FlushChain (pkg/util/iptables/iptables.go:291)


FlushChain is part of Interface.


```go
func (runner *runner) FlushChain((table Table, chain Chain)) (table Table, chain Chain)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:291`



---


[function] name: HasRandomFully file: pkg/util/iptables/iptables.go:749 returns_error: нет description: —


### HasRandomFully (pkg/util/iptables/iptables.go:749)


HasRandomFully is a method that performs operations based on the provided parameters and returns ().


```go
func (runner *runner) HasRandomFully(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables.go:749`



---


[function] name: IsIPv6 file: pkg/util/iptables/iptables.go:360 returns_error: нет description: —


### IsIPv6 (pkg/util/iptables/iptables.go:360)


IsIPv6 is a method that performs operations based on the provided parameters and returns ().


```go
func (runner *runner) IsIPv6(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables.go:360`



---


[function] name: IsNotFoundError file: pkg/util/iptables/iptables.go:789 returns_error: да description: IsNotFoundError returns true if the error indicates "not found".  It parses
the error string looking for known values, w


### IsNotFoundError (pkg/util/iptables/iptables.go:789)


IsNotFoundError returns true if the error indicates "not found".  It parses
the error string looking for known values, which is imperfect; beware using
this function for anything beyond deciding between logging or ignoring an
error.


```go
func IsNotFoundError((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/util/iptables/iptables.go:789`



---


[function] name: Line file: pkg/util/iptables/iptables.go:825 returns_error: нет description: —


### Line (pkg/util/iptables/iptables.go:825)


Line is a method that performs operations based on the provided parameters and returns ().


```go
func (e parseError) Line(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables.go:825`



---


[function] name: Monitor file: pkg/util/iptables/iptables.go:590 returns_error: нет description: Monitor is part of Interface


### Monitor (pkg/util/iptables/iptables.go:590)


Monitor is part of Interface


```go
func (runner *runner) Monitor((canary Chain, tables []Table, reloadFunc func(), interval time.Duration, stopCh <-chan struct{})) (canary Chain, tables []Table, reloadFunc func(), interval time.Duration, stopCh <-chan struct{})
```


**Тип ответа:** canary


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** tables


```json
{
  "name": "string",
  "chainType": {},
  "hook": {},
  "priority": {}
}
```


*Определено в:* `pkg/proxy/nftables/proxier.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** reloadFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interval


```json
{
  "First": 0,
  "Last": 0
}
```


*Определено в:* `pkg/controller/job/indexed_job_utils.go`


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:590`



---


[function] name: New file: pkg/util/iptables/iptables.go:245 returns_error: нет description: New returns a new Interface which will exec iptables.
Note that this function will return a single iptables Interface *a


### New (pkg/util/iptables/iptables.go:245)


New returns a new Interface which will exec iptables.
Note that this function will return a single iptables Interface *and* an error, if only
a single family is supported.


```go
func New((protocol Protocol)) (protocol Protocol)
```


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:245`



---


[function] name: NewBestEffort file: pkg/util/iptables/iptables.go:267 returns_error: нет description: NewBestEffort returns a map containing an IPv4 Interface (if IPv4 iptables is
supported) and an IPv6 Interface (if IPv6 


### NewBestEffort (pkg/util/iptables/iptables.go:267)


NewBestEffort returns a map containing an IPv4 Interface (if IPv4 iptables is
supported) and an IPv6 Interface (if IPv6 iptables is supported). If iptables is not
supported, then it just returns an empty map. This function is intended to make things
simple for callers that just want "best-effort" iptables support, where neither partial
nor complete lack of iptables support is considered an error.


```go
func NewBestEffort(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables.go:267`



---


[function] name: Present file: pkg/util/iptables/iptables.go:755 returns_error: нет description: Present tests if iptable is supported on current kernel by checking the existence
of default table and chain


### Present (pkg/util/iptables/iptables.go:755)


Present tests if iptable is supported on current kernel by checking the existence
of default table and chain


```go
func (runner *runner) Present(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables.go:755`



---


[function] name: Protocol file: pkg/util/iptables/iptables.go:364 returns_error: нет description: —


### Protocol (pkg/util/iptables/iptables.go:364)


Protocol is a method that performs operations based on the provided parameters and returns ().


```go
func (runner *runner) Protocol(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables.go:364`



---


[function] name: Restore file: pkg/util/iptables/iptables.go:393 returns_error: нет description: Restore is part of Interface.


### Restore (pkg/util/iptables/iptables.go:393)


Restore is part of Interface.


```go
func (runner *runner) Restore((table Table, data []byte, flush FlushFlag, counters RestoreCountersFlag)) (table Table, data []byte, flush FlushFlag, counters RestoreCountersFlag)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


**Тип ответа:** flush


```json
{
  "flusher": {},
  "writer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flushwriter/writer.go`


**Тип ответа:** FlushFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** counters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RestoreCountersFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/iptables.go:393`



---


[function] name: RestoreAll file: pkg/util/iptables/iptables.go:400 returns_error: нет description: RestoreAll is part of Interface.


### RestoreAll (pkg/util/iptables/iptables.go:400)


RestoreAll is part of Interface.


```go
func (runner *runner) RestoreAll((data []byte, flush FlushFlag, counters RestoreCountersFlag)) (data []byte, flush FlushFlag, counters RestoreCountersFlag)
```


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


**Тип ответа:** flush


```json
{
  "flusher": {},
  "writer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flushwriter/writer.go`


**Тип ответа:** FlushFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** counters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RestoreCountersFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/iptables.go:400`



---


[function] name: SaveInto file: pkg/util/iptables/iptables.go:369 returns_error: нет description: SaveInto is part of Interface.


### SaveInto (pkg/util/iptables/iptables.go:369)


SaveInto is part of Interface.


```go
func (runner *runner) SaveInto((table Table, buffer *bytes.Buffer)) (table Table, buffer *bytes.Buffer)
```


**Тип запроса:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** buffer


```json
{
  "lines": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/swagger_doc_generator.go`


**Тип ответа:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:369`



---


[function] name: checkRule file: pkg/util/iptables/iptables.go:497 returns_error: да description: Returns (bool, nil) if it was able to check the existence of the rule, or
(<undefined>, error) if the process of checkin


### checkRule (pkg/util/iptables/iptables.go:497)


Returns (bool, nil) if it was able to check the existence of the rule, or
(<undefined>, error) if the process of checking failed.


```go
func (runner *runner) checkRule((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:497`



---


[function] name: checkRuleUsingCheck file: pkg/util/iptables/iptables.go:561 returns_error: да description: Executes the rule check using the "-C" flag


### checkRuleUsingCheck (pkg/util/iptables/iptables.go:561)


Executes the rule check using the "-C" flag


```go
func (runner *runner) checkRuleUsingCheck((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:561`



---


[function] name: checkRuleWithoutCheck file: pkg/util/iptables/iptables.go:513 returns_error: да description: Executes the rule check without using the "-C" flag, instead parsing iptables-save.
Present for compatibility with <1.4.


### checkRuleWithoutCheck (pkg/util/iptables/iptables.go:513)


Executes the rule check without using the "-C" flag, instead parsing iptables-save.
Present for compatibility with <1.4.11 versions of iptables.  This is full
of hack and half-measures.  We should nix this ASAP.


```go
func (runner *runner) checkRuleWithoutCheck((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:513`



---


[function] name: getIPTablesRestoreVersionString file: pkg/util/iptables/iptables.go:728 returns_error: да description: getIPTablesRestoreVersionString runs "iptables-restore --version" to get the version string
in the form "X.X.X"


### getIPTablesRestoreVersionString (pkg/util/iptables/iptables.go:728)


getIPTablesRestoreVersionString runs "iptables-restore --version" to get the version string
in the form "X.X.X"


```go
func getIPTablesRestoreVersionString((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:728`



---


[function] name: getIPTablesRestoreWaitFlag file: pkg/util/iptables/iptables.go:707 returns_error: нет description: Checks if iptables-restore has a "wait" flag


### getIPTablesRestoreWaitFlag (pkg/util/iptables/iptables.go:707)


Checks if iptables-restore has a "wait" flag


```go
func getIPTablesRestoreWaitFlag((version *utilversion.Version, exec utilexec.Interface, protocol Protocol)) (version *utilversion.Version, exec utilexec.Interface, protocol Protocol)
```


**Тип запроса:** utilversion.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


**Тип ответа:** utilversion.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** exec


```json
{
  "ExitCode": 0,
  "StartDelay": 0,
  "Delay": 0,
  "LoopForever": false,
  "TerminationSeconds": 0,
  "ContainerName": "string",
  "LoopPeriod": 0.0
}
```


*Определено в:* `test/e2e_node/container_lifecycle_pod_construction.go`


**Тип ответа:** utilexec.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:707`



---


[function] name: getIPTablesVersion file: pkg/util/iptables/iptables.go:674 returns_error: да description: getIPTablesVersion runs "iptables --version" and parses the returned version


### getIPTablesVersion (pkg/util/iptables/iptables.go:674)


getIPTablesVersion runs "iptables --version" and parses the returned version


```go
func getIPTablesVersion((*utilversion.Version, error)) (*utilversion.Version, error)
```


**Тип запроса:** utilversion.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** utilversion.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*utilversion.Version`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:674`



---


[function] name: getIPTablesWaitFlag file: pkg/util/iptables/iptables.go:695 returns_error: нет description: Checks if iptables version has a "wait" flag


### getIPTablesWaitFlag (pkg/util/iptables/iptables.go:695)


Checks if iptables version has a "wait" flag


```go
func getIPTablesWaitFlag((version *utilversion.Version)) (version *utilversion.Version)
```


**Тип запроса:** utilversion.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


**Тип ответа:** utilversion.Version


```json
{
  "components": [],
  "semver": false,
  "preRelease": "string",
  "buildMetadata": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/version/version.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:695`



---


[function] name: iptablesCommand file: pkg/util/iptables/iptables.go:472 returns_error: нет description: —


### iptablesCommand (pkg/util/iptables/iptables.go:472)


iptablesCommand is a function that performs operations based on the provided parameters and returns (protocol Protocol).


```go
func iptablesCommand((protocol Protocol)) (protocol Protocol)
```


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:472`



---


[function] name: iptablesRestoreCommand file: pkg/util/iptables/iptables.go:465 returns_error: нет description: —


### iptablesRestoreCommand (pkg/util/iptables/iptables.go:465)


iptablesRestoreCommand is a function that performs operations based on the provided parameters and returns (protocol Protocol).


```go
func iptablesRestoreCommand((protocol Protocol)) (protocol Protocol)
```


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:465`



---


[function] name: iptablesSaveCommand file: pkg/util/iptables/iptables.go:458 returns_error: нет description: —


### iptablesSaveCommand (pkg/util/iptables/iptables.go:458)


iptablesSaveCommand is a function that performs operations based on the provided parameters and returns (protocol Protocol).


```go
func iptablesSaveCommand((protocol Protocol)) (protocol Protocol)
```


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:458`



---


[function] name: isResourceError file: pkg/util/iptables/iptables.go:804 returns_error: да description: isResourceError returns true if the error indicates that iptables ran into a "resource
problem" and was unable to attemp


### isResourceError (pkg/util/iptables/iptables.go:804)


isResourceError returns true if the error indicates that iptables ran into a "resource
problem" and was unable to attempt the request. In particular, this will be true if it
times out trying to get the iptables lock.


```go
func isResourceError((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/util/iptables/iptables.go:804`



---


[function] name: makeFullArgs file: pkg/util/iptables/iptables.go:667 returns_error: нет description: —


### makeFullArgs (pkg/util/iptables/iptables.go:667)


makeFullArgs is a function that performs operations based on the provided parameters and returns (table Table, chain Chain, args ...string).


```go
func makeFullArgs((table Table, chain Chain, args ...string)) (table Table, chain Chain, args ...string)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/iptables.go:667`



---


[function] name: newDualStackInternal file: pkg/util/iptables/iptables.go:249 returns_error: нет description: —


### newDualStackInternal (pkg/util/iptables/iptables.go:249)


newDualStackInternal is a function that performs operations based on the provided parameters and returns (exec utilexec.Interface).


```go
func newDualStackInternal((exec utilexec.Interface)) (exec utilexec.Interface)
```


**Тип ответа:** exec


```json
{
  "ExitCode": 0,
  "StartDelay": 0,
  "Delay": 0,
  "LoopForever": false,
  "TerminationSeconds": 0,
  "ContainerName": "string",
  "LoopPeriod": 0.0
}
```


*Определено в:* `test/e2e_node/container_lifecycle_pod_construction.go`


**Тип ответа:** utilexec.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:249`



---


[function] name: newInternal file: pkg/util/iptables/iptables.go:212 returns_error: нет description: newInternal returns a new Interface which will exec iptables, and allows the
caller to change the iptables-restore lockf


### newInternal (pkg/util/iptables/iptables.go:212)


newInternal returns a new Interface which will exec iptables, and allows the
caller to change the iptables-restore lockfile path


```go
func newInternal((exec utilexec.Interface, protocol Protocol, lockfilePath14x, lockfilePath16x string)) (exec utilexec.Interface, protocol Protocol, lockfilePath14x, lockfilePath16x string)
```


**Тип ответа:** exec


```json
{
  "ExitCode": 0,
  "StartDelay": 0,
  "Delay": 0,
  "LoopForever": false,
  "TerminationSeconds": 0,
  "ContainerName": "string",
  "LoopPeriod": 0.0
}
```


*Определено в:* `test/e2e_node/container_lifecycle_pod_construction.go`


**Тип ответа:** utilexec.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


**Тип ответа:** lockfilePath14x


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lockfilePath16x


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/iptables.go:212`



---


[function] name: parseRestoreError file: pkg/util/iptables/iptables.go:849 returns_error: нет description: parseRestoreError extracts the line from the error, if it matches returns parseError
for example:
input: iptables-restor


### parseRestoreError (pkg/util/iptables/iptables.go:849)


parseRestoreError extracts the line from the error, if it matches returns parseError
for example:
input: iptables-restore: line 51 failed
output: parseError:  cmd = iptables-restore, line = 51
NOTE: parseRestoreError depends on the error format of iptables, if it ever changes
we need to update this function


```go
func parseRestoreError((ParseError, bool)) (ParseError, bool)
```


**Тип ответа:** ParseError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/iptables.go:849`



---


[function] name: restoreInternal file: pkg/util/iptables/iptables.go:411 returns_error: нет description: restoreInternal is the shared part of Restore/RestoreAll


### restoreInternal (pkg/util/iptables/iptables.go:411)


restoreInternal is the shared part of Restore/RestoreAll


```go
func (runner *runner) restoreInternal((args []string, data []byte, flush FlushFlag, counters RestoreCountersFlag)) (args []string, data []byte, flush FlushFlag, counters RestoreCountersFlag)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


**Тип ответа:** flush


```json
{
  "flusher": {},
  "writer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flushwriter/writer.go`


**Тип ответа:** FlushFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** counters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RestoreCountersFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/iptables.go:411`



---


[function] name: run file: pkg/util/iptables/iptables.go:479 returns_error: да description: —


### run (pkg/util/iptables/iptables.go:479)


run is a method that performs operations based on the provided parameters and may return an error.


```go
func (runner *runner) run(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:479`



---


[function] name: runContext file: pkg/util/iptables/iptables.go:483 returns_error: да description: —


### runContext (pkg/util/iptables/iptables.go:483)


runContext is a method that performs operations based on the provided parameters and may return an error.


```go
func (runner *runner) runContext(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables.go:483`



---


[function] name: trimhex file: pkg/util/iptables/iptables.go:506 returns_error: нет description: —


### trimhex (pkg/util/iptables/iptables.go:506)


trimhex is a function that performs operations based on the provided parameters and returns (s string).


```go
func trimhex((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/iptables/iptables.go:506`




## pkg/util/iptables/iptables_linux.go


📄 Исходный файл: `pkg/util/iptables/iptables_linux.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Close](#close-pkgutiliptablesiptables_linuxgo37) `:37`

- 🔗 [grabIptablesFileLock](#grabiptablesfilelock-pkgutiliptablesiptables_linuxgo98) `:98`

- 🔗 [grabIptablesLocks](#grabiptableslocks-pkgutiliptablesiptables_linuxgo52) `:52`


</details>


[function] name: Close file: pkg/util/iptables/iptables_linux.go:37 returns_error: нет description: —


### Close (pkg/util/iptables/iptables_linux.go:37)


Close is a method that performs operations based on the provided parameters and returns ().


```go
func (l *locker) Close(()) ()
```


📍 *Расположение:* `pkg/util/iptables/iptables_linux.go:37`



---


[function] name: grabIptablesFileLock file: pkg/util/iptables/iptables_linux.go:98 returns_error: нет description: —


### grabIptablesFileLock (pkg/util/iptables/iptables_linux.go:98)


grabIptablesFileLock is a function that performs operations based on the provided parameters and returns (f *os.File).


```go
func grabIptablesFileLock((f *os.File)) (f *os.File)
```


**Тип запроса:** os.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


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


**Тип ответа:** os.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


📍 *Расположение:* `pkg/util/iptables/iptables_linux.go:98`



---


[function] name: grabIptablesLocks file: pkg/util/iptables/iptables_linux.go:52 returns_error: да description: —


### grabIptablesLocks (pkg/util/iptables/iptables_linux.go:52)


grabIptablesLocks is a function that performs operations based on the provided parameters and may return an error.


```go
func grabIptablesLocks((iptablesLocker, error)) (iptablesLocker, error)
```


**Тип ответа:** iptablesLocker


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `iptablesLocker`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/iptables_linux.go:52`




## pkg/util/iptables/save_restore.go


📄 Исходный файл: `pkg/util/iptables/save_restore.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetChainsFromTable](#getchainsfromtable-pkgutiliptablessave_restorego36) `:36`

- 🔗 [MakeChainLine](#makechainline-pkgutiliptablessave_restorego29) `:29`


</details>


[function] name: GetChainsFromTable file: pkg/util/iptables/save_restore.go:36 returns_error: нет description: GetChainsFromTable parses iptables-save data to find the chains that are defined. It
assumes that save contains a single


### GetChainsFromTable (pkg/util/iptables/save_restore.go:36)


GetChainsFromTable parses iptables-save data to find the chains that are defined. It
assumes that save contains a single table's data, and returns a set with keys for every
chain defined in that table.


```go
func GetChainsFromTable((save []byte)) (save []byte)
```


**Тип ответа:** save


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/save_restore.go:36`



---


[function] name: MakeChainLine file: pkg/util/iptables/save_restore.go:29 returns_error: нет description: MakeChainLine return an iptables-save/restore formatted chain line given a Chain


### MakeChainLine (pkg/util/iptables/save_restore.go:29)


MakeChainLine return an iptables-save/restore formatted chain line given a Chain


```go
func MakeChainLine((chain Chain)) (chain Chain)
```


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


📍 *Расположение:* `pkg/util/iptables/save_restore.go:29`




## pkg/util/iptables/testing/fake.go


📄 Исходный файл: `pkg/util/iptables/testing/fake.go`


<details open>
<summary><b>Функции в этом файле (19)</b></summary>


- 🔗 [ChainExists](#chainexists-pkgutiliptablestestingfakego123) `:123`

- 🔗 [DeleteChain](#deletechain-pkgutiliptablestestingfakego108) `:108`

- 🔗 [DeleteRule](#deleterule-pkgutiliptablestestingfakego161) `:161`

- 🔗 [EnsureChain](#ensurechain-pkgutiliptablestestingfakego87) `:87`

- 🔗 [EnsureRule](#ensurerule-pkgutiliptablestestingfakego134) `:134`

- 🔗 [FlushChain](#flushchain-pkgutiliptablestestingfakego100) `:100`

- 🔗 [HasRandomFully](#hasrandomfully-pkgutiliptablestestingfakego325) `:325`

- 🔗 [IsIPv6](#isipv6-pkgutiliptablestestingfakego178) `:178`

- 🔗 [Monitor](#monitor-pkgutiliptablestestingfakego321) `:321`

- 🔗 [NewFake](#newfake-pkgutiliptablestestingfakego40) `:40`

- 🔗 [NewIPv6Fake](#newipv6fake-pkgutiliptablestestingfakego74) `:74`

- 🔗 [Present](#present-pkgutiliptablestestingfakego329) `:329`

- 🔗 [Protocol](#protocol-pkgutiliptablestestingfakego183) `:183`

- 🔗 [Restore](#restore-pkgutiliptablestestingfakego290) `:290`

- 🔗 [RestoreAll](#restoreall-pkgutiliptablestestingfakego305) `:305`

- 🔗 [SaveInto](#saveinto-pkgutiliptablestestingfakego207) `:207`

- 🔗 [SetHasRandomFully](#sethasrandomfully-pkgutiliptablestestingfakego81) `:81`

- 🔗 [restoreTable](#restoretable-pkgutiliptablestestingfakego226) `:226`

- 🔗 [saveTable](#savetable-pkgutiliptablestestingfakego187) `:187`


</details>


[function] name: ChainExists file: pkg/util/iptables/testing/fake.go:123 returns_error: да description: ChainExists is part of iptables.Interface


### ChainExists (pkg/util/iptables/testing/fake.go:123)


ChainExists is part of iptables.Interface


```go
func (f *FakeIPTables) ChainExists((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:123`



---


[function] name: DeleteChain file: pkg/util/iptables/testing/fake.go:108 returns_error: нет description: DeleteChain is part of iptables.Interface


### DeleteChain (pkg/util/iptables/testing/fake.go:108)


DeleteChain is part of iptables.Interface


```go
func (f *FakeIPTables) DeleteChain((table iptables.Table, chain iptables.Chain)) (table iptables.Table, chain iptables.Chain)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** iptables.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** iptables.Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:108`



---


[function] name: DeleteRule file: pkg/util/iptables/testing/fake.go:161 returns_error: нет description: DeleteRule is part of iptables.Interface


### DeleteRule (pkg/util/iptables/testing/fake.go:161)


DeleteRule is part of iptables.Interface


```go
func (f *FakeIPTables) DeleteRule((table iptables.Table, chain iptables.Chain, args ...string)) (table iptables.Table, chain iptables.Chain, args ...string)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** iptables.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** iptables.Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:161`



---


[function] name: EnsureChain file: pkg/util/iptables/testing/fake.go:87 returns_error: да description: EnsureChain is part of iptables.Interface


### EnsureChain (pkg/util/iptables/testing/fake.go:87)


EnsureChain is part of iptables.Interface


```go
func (f *FakeIPTables) EnsureChain((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:87`



---


[function] name: EnsureRule file: pkg/util/iptables/testing/fake.go:134 returns_error: да description: EnsureRule is part of iptables.Interface


### EnsureRule (pkg/util/iptables/testing/fake.go:134)


EnsureRule is part of iptables.Interface


```go
func (f *FakeIPTables) EnsureRule((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:134`



---


[function] name: FlushChain file: pkg/util/iptables/testing/fake.go:100 returns_error: нет description: FlushChain is part of iptables.Interface


### FlushChain (pkg/util/iptables/testing/fake.go:100)


FlushChain is part of iptables.Interface


```go
func (f *FakeIPTables) FlushChain((table iptables.Table, chain iptables.Chain)) (table iptables.Table, chain iptables.Chain)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** iptables.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** iptables.Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:100`



---


[function] name: HasRandomFully file: pkg/util/iptables/testing/fake.go:325 returns_error: нет description: HasRandomFully is part of iptables.Interface


### HasRandomFully (pkg/util/iptables/testing/fake.go:325)


HasRandomFully is part of iptables.Interface


```go
func (f *FakeIPTables) HasRandomFully(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:325`



---


[function] name: IsIPv6 file: pkg/util/iptables/testing/fake.go:178 returns_error: нет description: IsIPv6 is part of iptables.Interface


### IsIPv6 (pkg/util/iptables/testing/fake.go:178)


IsIPv6 is part of iptables.Interface


```go
func (f *FakeIPTables) IsIPv6(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:178`



---


[function] name: Monitor file: pkg/util/iptables/testing/fake.go:321 returns_error: нет description: Monitor is part of iptables.Interface


### Monitor (pkg/util/iptables/testing/fake.go:321)


Monitor is part of iptables.Interface


```go
func (f *FakeIPTables) Monitor((canary iptables.Chain, tables []iptables.Table, reloadFunc func(), interval time.Duration, stopCh <-chan struct{})) (canary iptables.Chain, tables []iptables.Table, reloadFunc func(), interval time.Duration, stopCh <-chan struct{})
```


**Тип ответа:** canary


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** iptables.Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** tables


```json
{
  "name": "string",
  "chainType": {},
  "hook": {},
  "priority": {}
}
```


*Определено в:* `pkg/proxy/nftables/proxier.go`


**Тип ответа:** iptables.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** reloadFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interval


```json
{
  "First": 0,
  "Last": 0
}
```


*Определено в:* `pkg/controller/job/indexed_job_utils.go`


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:321`



---


[function] name: NewFake file: pkg/util/iptables/testing/fake.go:40 returns_error: нет description: NewFake returns a no-op iptables.Interface


### NewFake (pkg/util/iptables/testing/fake.go:40)


NewFake returns a no-op iptables.Interface


```go
func NewFake(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:40`



---


[function] name: NewIPv6Fake file: pkg/util/iptables/testing/fake.go:74 returns_error: нет description: NewIPv6Fake returns a no-op iptables.Interface with IsIPv6() == true


### NewIPv6Fake (pkg/util/iptables/testing/fake.go:74)


NewIPv6Fake returns a no-op iptables.Interface with IsIPv6() == true


```go
func NewIPv6Fake(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:74`



---


[function] name: Present file: pkg/util/iptables/testing/fake.go:329 returns_error: нет description: —


### Present (pkg/util/iptables/testing/fake.go:329)


Present is a method that performs operations based on the provided parameters and returns ().


```go
func (f *FakeIPTables) Present(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:329`



---


[function] name: Protocol file: pkg/util/iptables/testing/fake.go:183 returns_error: нет description: Protocol is part of iptables.Interface


### Protocol (pkg/util/iptables/testing/fake.go:183)


Protocol is part of iptables.Interface


```go
func (f *FakeIPTables) Protocol(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:183`



---


[function] name: Restore file: pkg/util/iptables/testing/fake.go:290 returns_error: нет description: Restore is part of iptables.Interface


### Restore (pkg/util/iptables/testing/fake.go:290)


Restore is part of iptables.Interface


```go
func (f *FakeIPTables) Restore((table iptables.Table, data []byte, flush iptables.FlushFlag, counters iptables.RestoreCountersFlag)) (table iptables.Table, data []byte, flush iptables.FlushFlag, counters iptables.RestoreCountersFlag)
```


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** iptables.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


**Тип ответа:** flush


```json
{
  "flusher": {},
  "writer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flushwriter/writer.go`


**Тип ответа:** iptables.FlushFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** counters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** iptables.RestoreCountersFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:290`



---


[function] name: RestoreAll file: pkg/util/iptables/testing/fake.go:305 returns_error: нет description: RestoreAll is part of iptables.Interface


### RestoreAll (pkg/util/iptables/testing/fake.go:305)


RestoreAll is part of iptables.Interface


```go
func (f *FakeIPTables) RestoreAll((data []byte, flush iptables.FlushFlag, counters iptables.RestoreCountersFlag)) (data []byte, flush iptables.FlushFlag, counters iptables.RestoreCountersFlag)
```


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


**Тип ответа:** flush


```json
{
  "flusher": {},
  "writer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flushwriter/writer.go`


**Тип ответа:** iptables.FlushFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** counters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** iptables.RestoreCountersFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:305`



---


[function] name: SaveInto file: pkg/util/iptables/testing/fake.go:207 returns_error: нет description: SaveInto is part of iptables.Interface


### SaveInto (pkg/util/iptables/testing/fake.go:207)


SaveInto is part of iptables.Interface


```go
func (f *FakeIPTables) SaveInto((table iptables.Table, buffer *bytes.Buffer)) (table iptables.Table, buffer *bytes.Buffer)
```


**Тип запроса:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** iptables.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** buffer


```json
{
  "lines": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/swagger_doc_generator.go`


**Тип ответа:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:207`



---


[function] name: SetHasRandomFully file: pkg/util/iptables/testing/fake.go:81 returns_error: нет description: SetHasRandomFully sets f's return value for HasRandomFully()


### SetHasRandomFully (pkg/util/iptables/testing/fake.go:81)


SetHasRandomFully sets f's return value for HasRandomFully()


```go
func (f *FakeIPTables) SetHasRandomFully((can bool)) (can bool)
```


**Тип ответа:** can


```json
{
  "tok": {},
  "literal": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/labels/selector.go`


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:81`



---


[function] name: restoreTable file: pkg/util/iptables/testing/fake.go:226 returns_error: нет description: —


### restoreTable (pkg/util/iptables/testing/fake.go:226)


restoreTable is a method that performs operations based on the provided parameters and returns (newDump *IPTablesDump, newTable *Table, flush iptables.FlushFlag, counters iptables.RestoreCountersFlag).


```go
func (f *FakeIPTables) restoreTable((newDump *IPTablesDump, newTable *Table, flush iptables.FlushFlag, counters iptables.RestoreCountersFlag)) (newDump *IPTablesDump, newTable *Table, flush iptables.FlushFlag, counters iptables.RestoreCountersFlag)
```


**Тип запроса:** IPTablesDump


```json
{
  "Tables": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип запроса:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** newDump


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** IPTablesDump


```json
{
  "Tables": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** newTable


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** flush


```json
{
  "flusher": {},
  "writer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flushwriter/writer.go`


**Тип ответа:** iptables.FlushFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** counters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** iptables.RestoreCountersFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:226`



---


[function] name: saveTable file: pkg/util/iptables/testing/fake.go:187 returns_error: нет description: —


### saveTable (pkg/util/iptables/testing/fake.go:187)


saveTable is a method that performs operations based on the provided parameters and returns (table iptables.Table, buffer *bytes.Buffer).


```go
func (f *FakeIPTables) saveTable((table iptables.Table, buffer *bytes.Buffer)) (table iptables.Table, buffer *bytes.Buffer)
```


**Тип запроса:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип ответа:** table


```json
{
  "jsonPath": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** iptables.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** buffer


```json
{
  "lines": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/swagger_doc_generator.go`


**Тип ответа:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


📍 *Расположение:* `pkg/util/iptables/testing/fake.go:187`




## pkg/util/iptables/testing/parse.go


📄 Исходный файл: `pkg/util/iptables/testing/parse.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [GetChain](#getchain-pkgutiliptablestestingparsego186) `:186`

- 🔗 [GetTable](#gettable-pkgutiliptablestestingparsego177) `:177`

- 🔗 [Matches](#matches-pkgutiliptablestestingparsego277) `:277`

- 🔗 [ParseIPTablesDump](#parseiptablesdump-pkgutiliptablestestingparsego69) `:69`

- 🔗 [ParseRule](#parserule-pkgutiliptablestestingparsego310) `:310`

- 🔗 [String](#string-pkgutiliptablestestingparsego155) `:155`

- 🔗 [String](#string-pkgutiliptablestestingparsego267) `:267`

- 🔗 [findParamField](#findparamfield-pkgutiliptablestestingparsego287) `:287`


</details>


[function] name: GetChain file: pkg/util/iptables/testing/parse.go:186 returns_error: да description: —


### GetChain (pkg/util/iptables/testing/parse.go:186)


GetChain is a method that retrieves data based on the provided parameters and may return an error.


```go
func (dump *IPTablesDump) GetChain((*Chain, error)) (*Chain, error)
```


**Тип запроса:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Chain`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:186`



---


[function] name: GetTable file: pkg/util/iptables/testing/parse.go:177 returns_error: да description: —


### GetTable (pkg/util/iptables/testing/parse.go:177)


GetTable is a method that retrieves data based on the provided parameters and may return an error.


```go
func (dump *IPTablesDump) GetTable((*Table, error)) (*Table, error)
```


**Тип запроса:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Table`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:177`



---


[function] name: Matches file: pkg/util/iptables/testing/parse.go:277 returns_error: нет description: Matches returns true if cmp equals / doesn't equal v.Value (depending on
v.Negated).


### Matches (pkg/util/iptables/testing/parse.go:277)


Matches returns true if cmp equals / doesn't equal v.Value (depending on
v.Negated).


```go
func (v *IPTablesValue) Matches((cmp string)) (cmp string)
```


**Тип ответа:** cmp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:277`



---


[function] name: ParseIPTablesDump file: pkg/util/iptables/testing/parse.go:69 returns_error: да description: ParseIPTablesDump parses an IPTables rules dump. Note: this may ignore some bad data.


### ParseIPTablesDump (pkg/util/iptables/testing/parse.go:69)


ParseIPTablesDump parses an IPTables rules dump. Note: this may ignore some bad data.


```go
func ParseIPTablesDump((*IPTablesDump, error)) (*IPTablesDump, error)
```


**Тип запроса:** IPTablesDump


```json
{
  "Tables": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** IPTablesDump


```json
{
  "Tables": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IPTablesDump`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:69`



---


[function] name: ParseRule file: pkg/util/iptables/testing/parse.go:310 returns_error: да description: ParseRule parses rule. If strict is false, it will parse the recognized
parameters and ignore unrecognized ones. If it i


### ParseRule (pkg/util/iptables/testing/parse.go:310)


ParseRule parses rule. If strict is false, it will parse the recognized
parameters and ignore unrecognized ones. If it is true, parsing will fail if there are
unrecognized parameters.


```go
func ParseRule((*Rule, error)) (*Rule, error)
```


**Тип запроса:** Rule


```json
{
  "Raw": "string",
  "Chain": {},
  "Comment": null,
  "Protocol": null,
  "SourceAddress": null,
  "SourceType": null,
  "SourcePort": null,
  "DestinationAddress": null,
  "DestinationType": null,
  "DestinationPort": null,
  "MatchSet": null,
  "Jump": null,
  "RandomFully": false,
  "Probability": null,
  "DNATDestination": null,
  "AffinityCheck": false,
  "MarkCheck": null,
  "CTStateCheck": null,
  "AffinityName": null,
  "AffinitySeconds": null,
  "AffinitySet": false,
  "AffinityReap": false,
  "StatisticMode": null
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** Rule


```json
{
  "Raw": "string",
  "Chain": {},
  "Comment": null,
  "Protocol": null,
  "SourceAddress": null,
  "SourceType": null,
  "SourcePort": null,
  "DestinationAddress": null,
  "DestinationType": null,
  "DestinationPort": null,
  "MatchSet": null,
  "Jump": null,
  "RandomFully": false,
  "Probability": null,
  "DNATDestination": null,
  "AffinityCheck": false,
  "MarkCheck": null,
  "CTStateCheck": null,
  "AffinityName": null,
  "AffinitySeconds": null,
  "AffinitySet": false,
  "AffinityReap": false,
  "StatisticMode": null
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Rule`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:310`



---


[function] name: String file: pkg/util/iptables/testing/parse.go:155 returns_error: нет description: —


### String (pkg/util/iptables/testing/parse.go:155)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (dump *IPTablesDump) String(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:155`



---


[function] name: String file: pkg/util/iptables/testing/parse.go:267 returns_error: нет description: for debugging; otherwise %v will just print the pointer value


### String (pkg/util/iptables/testing/parse.go:267)


for debugging; otherwise %v will just print the pointer value


```go
func (v *IPTablesValue) String(()) ()
```


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:267`



---


[function] name: findParamField file: pkg/util/iptables/testing/parse.go:287 returns_error: нет description: findParamField finds a field in value with the struct tag "param:${param}" and if found,
returns a pointer to the Value 


### findParamField (pkg/util/iptables/testing/parse.go:287)


findParamField finds a field in value with the struct tag "param:${param}" and if found,
returns a pointer to the Value of that field, and the value of its "negatable" tag.


```go
func findParamField((*reflect.Value, bool)) (*reflect.Value, bool)
```


**Тип запроса:** reflect.Value


```json
{
  "items": []
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/custom_metrics/v1beta1/types.go`


**Тип ответа:** reflect.Value


```json
{
  "items": []
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/custom_metrics/v1beta1/types.go`


📍 *Расположение:* `pkg/util/iptables/testing/parse.go:287`




## pkg/util/kernel/version.go


📄 Исходный файл: `pkg/util/kernel/version.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetVersion](#getversion-pkgutilkernelversiongo30) `:30`

- 🔗 [getVersion](#getversion-pkgutilkernelversiongo35) `:35`


</details>


[function] name: GetVersion file: pkg/util/kernel/version.go:30 returns_error: да description: GetVersion returns currently running kernel version.


### GetVersion (pkg/util/kernel/version.go:30)


GetVersion returns currently running kernel version.


```go
func GetVersion((*version.Version, error)) (*version.Version, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*version.Version`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/kernel/version.go:30`



---


[function] name: getVersion file: pkg/util/kernel/version.go:35 returns_error: да description: getVersion reads os release file from the give readFile function.


### getVersion (pkg/util/kernel/version.go:35)


getVersion reads os release file from the give readFile function.


```go
func getVersion((*version.Version, error)) (*version.Version, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*version.Version`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/kernel/version.go:35`




## pkg/util/labels/labels.go


📄 Исходный файл: `pkg/util/labels/labels.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [AddLabel](#addlabel-pkgutillabelslabelsgo56) `:56`

- 🔗 [AddLabelToSelector](#addlabeltoselector-pkgutillabelslabelsgo109) `:109`

- 🔗 [CloneAndAddLabel](#cloneandaddlabel-pkgutillabelslabelsgo25) `:25`

- 🔗 [CloneAndRemoveLabel](#cloneandremovelabel-pkgutillabelslabelsgo41) `:41`

- 🔗 [CloneSelectorAndAddLabel](#cloneselectorandaddlabel-pkgutillabelslabelsgo70) `:70`

- 🔗 [SelectorHasLabel](#selectorhaslabel-pkgutillabelslabelsgo122) `:122`


</details>


[function] name: AddLabel file: pkg/util/labels/labels.go:56 returns_error: нет description: AddLabel returns a map with the given key and value added to the given map.


### AddLabel (pkg/util/labels/labels.go:56)


AddLabel returns a map with the given key and value added to the given map.


```go
func AddLabel((labels map[string]string, labelKey, labelValue string)) (labels map[string]string, labelKey, labelValue string)
```


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelValue


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `pkg/util/labels/labels.go:56`



---


[function] name: AddLabelToSelector file: pkg/util/labels/labels.go:109 returns_error: нет description: AddLabelToSelector returns a selector with the given key and value added to the given selector's MatchLabels.


### AddLabelToSelector (pkg/util/labels/labels.go:109)


AddLabelToSelector returns a selector with the given key and value added to the given selector's MatchLabels.


```go
func AddLabelToSelector((selector *metav1.LabelSelector, labelKey, labelValue string)) (selector *metav1.LabelSelector, labelKey, labelValue string)
```


**Тип запроса:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** selector


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelValue


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `pkg/util/labels/labels.go:109`



---


[function] name: CloneAndAddLabel file: pkg/util/labels/labels.go:25 returns_error: нет description: Clones the given map and returns a new map with the given key and value added.
Returns the given map, if labelKey is emp


### CloneAndAddLabel (pkg/util/labels/labels.go:25)


Clones the given map and returns a new map with the given key and value added.
Returns the given map, if labelKey is empty.


```go
func CloneAndAddLabel((labels map[string]string, labelKey, labelValue string)) (labels map[string]string, labelKey, labelValue string)
```


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelValue


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `pkg/util/labels/labels.go:25`



---


[function] name: CloneAndRemoveLabel file: pkg/util/labels/labels.go:41 returns_error: нет description: CloneAndRemoveLabel clones the given map and returns a new map with the given key removed.
Returns the given map, if lab


### CloneAndRemoveLabel (pkg/util/labels/labels.go:41)


CloneAndRemoveLabel clones the given map and returns a new map with the given key removed.
Returns the given map, if labelKey is empty.


```go
func CloneAndRemoveLabel((labels map[string]string, labelKey string)) (labels map[string]string, labelKey string)
```


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/labels/labels.go:41`



---


[function] name: CloneSelectorAndAddLabel file: pkg/util/labels/labels.go:70 returns_error: нет description: Clones the given selector and returns a new selector with the given key and value added.
Returns the given selector, if 


### CloneSelectorAndAddLabel (pkg/util/labels/labels.go:70)


Clones the given selector and returns a new selector with the given key and value added.
Returns the given selector, if labelKey is empty.


```go
func CloneSelectorAndAddLabel((selector *metav1.LabelSelector, labelKey, labelValue string)) (selector *metav1.LabelSelector, labelKey, labelValue string)
```


**Тип запроса:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** selector


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelValue


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `pkg/util/labels/labels.go:70`



---


[function] name: SelectorHasLabel file: pkg/util/labels/labels.go:122 returns_error: нет description: SelectorHasLabel checks if the given selector contains the given label key in its MatchLabels


### SelectorHasLabel (pkg/util/labels/labels.go:122)


SelectorHasLabel checks if the given selector contains the given label key in its MatchLabels


```go
func SelectorHasLabel((selector *metav1.LabelSelector, labelKey string)) (selector *metav1.LabelSelector, labelKey string)
```


**Тип запроса:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** selector


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/labels/labels.go:122`




## pkg/util/node/node.go


📄 Исходный файл: `pkg/util/node/node.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Error](#error-pkgutilnodenodego43) `:43`

- 🔗 [GetNodeHostIPs](#getnodehostips-pkgutilnodenodego65) `:65`

- 🔗 [GetPreferredNodeAddress](#getpreferrednodeaddress-pkgutilnodenodego49) `:49`

- 🔗 [IsNodeReady](#isnodeready-pkgutilnodenodego100) `:100`


</details>


[function] name: Error file: pkg/util/node/node.go:43 returns_error: нет description: Error is the implementation of the conventional interface for
representing an error condition, with the nil value repres


### Error (pkg/util/node/node.go:43)


Error is the implementation of the conventional interface for
representing an error condition, with the nil value representing no error.


```go
func (e *NoMatchError) Error(()) ()
```


📍 *Расположение:* `pkg/util/node/node.go:43`



---


[function] name: GetNodeHostIPs file: pkg/util/node/node.go:65 returns_error: да description: GetNodeHostIPs returns the provided node's IP(s); either a single "primary IP" for the
node in a single-stack cluster, o


### GetNodeHostIPs (pkg/util/node/node.go:65)


GetNodeHostIPs returns the provided node's IP(s); either a single "primary IP" for the
node in a single-stack cluster, or a dual-stack pair of IPs in a dual-stack cluster
(for nodes that actually have dual-stack IPs). Among other things, the IPs returned
from this function are used as the `.status.PodIPs` values for host-network pods on the
node, and the first IP is used as the `.status.HostIP` for all pods on the node.


```go
func GetNodeHostIPs(([]net.IP, error)) ([]net.IP, error)
```


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]net.IP`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/node/node.go:65`



---


[function] name: GetPreferredNodeAddress file: pkg/util/node/node.go:49 returns_error: да description: GetPreferredNodeAddress returns the address of the provided node, using the provided preference order.
If none of the pr


### GetPreferredNodeAddress (pkg/util/node/node.go:49)


GetPreferredNodeAddress returns the address of the provided node, using the provided preference order.
If none of the preferred address types are found, an error is returned.


```go
func GetPreferredNodeAddress((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/node/node.go:49`



---


[function] name: IsNodeReady file: pkg/util/node/node.go:100 returns_error: нет description: IsNodeReady returns true if a node is ready; false otherwise.


### IsNodeReady (pkg/util/node/node.go:100)


IsNodeReady returns true if a node is ready; false otherwise.


```go
func IsNodeReady((node *v1.Node)) (node *v1.Node)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** node


```json
{
  "identity": {},
  "dependentsLock": {},
  "dependents": {},
  "deletingDependents": false,
  "deletingDependentsLock": {},
  "beingDeleted": false,
  "beingDeletedLock": {},
  "virtual": false,
  "virtualLock": {},
  "owners": [],
  "ownersLock": {}
}
```


*Определено в:* `pkg/controller/garbagecollector/graph.go`


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/node/node.go:100`




## pkg/util/oom/oom_fake.go


📄 Исходный файл: `pkg/util/oom/oom_fake.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [NewFakeOOMAdjuster](#newfakeoomadjuster-pkgutiloomoom_fakego21) `:21`

- 🔗 [fakeApplyOOMScoreAdj](#fakeapplyoomscoreadj-pkgutiloomoom_fakego29) `:29`

- 🔗 [fakeApplyOOMScoreAdjContainer](#fakeapplyoomscoreadjcontainer-pkgutiloomoom_fakego33) `:33`


</details>


[function] name: NewFakeOOMAdjuster file: pkg/util/oom/oom_fake.go:21 returns_error: нет description: —


### NewFakeOOMAdjuster (pkg/util/oom/oom_fake.go:21)


NewFakeOOMAdjuster is a function that performs operations based on the provided parameters and returns ().


```go
func NewFakeOOMAdjuster(()) ()
```


📍 *Расположение:* `pkg/util/oom/oom_fake.go:21`



---


[function] name: fakeApplyOOMScoreAdj file: pkg/util/oom/oom_fake.go:29 returns_error: нет description: —


### fakeApplyOOMScoreAdj (pkg/util/oom/oom_fake.go:29)


fakeApplyOOMScoreAdj is a function that performs operations based on the provided parameters and returns (pid int, oomScoreAdj int).


```go
func fakeApplyOOMScoreAdj((pid int, oomScoreAdj int)) (pid int, oomScoreAdj int)
```


**Тип ответа:** pid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oomScoreAdj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/oom/oom_fake.go:29`



---


[function] name: fakeApplyOOMScoreAdjContainer file: pkg/util/oom/oom_fake.go:33 returns_error: нет description: —


### fakeApplyOOMScoreAdjContainer (pkg/util/oom/oom_fake.go:33)


fakeApplyOOMScoreAdjContainer is a function that performs operations based on the provided parameters and returns (cgroupName string, oomScoreAdj, maxTries int).


```go
func fakeApplyOOMScoreAdjContainer((cgroupName string, oomScoreAdj, maxTries int)) (cgroupName string, oomScoreAdj, maxTries int)
```


**Тип ответа:** cgroupName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oomScoreAdj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxTries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/oom/oom_fake.go:33`




## pkg/util/oom/oom_linux.go


📄 Исходный файл: `pkg/util/oom/oom_linux.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewOOMAdjuster](#newoomadjuster-pkgutiloomoom_linuxgo34) `:34`

- 🔗 [applyOOMScoreAdj](#applyoomscoreadj-pkgutiloomoom_linuxgo49) `:49`

- 🔗 [applyOOMScoreAdjContainer](#applyoomscoreadjcontainer-pkgutiloomoom_linuxgo88) `:88`

- 🔗 [getPids](#getpids-pkgutiloomoom_linuxgo43) `:43`


</details>


[function] name: NewOOMAdjuster file: pkg/util/oom/oom_linux.go:34 returns_error: нет description: —


### NewOOMAdjuster (pkg/util/oom/oom_linux.go:34)


NewOOMAdjuster is a function that performs operations based on the provided parameters and returns ().


```go
func NewOOMAdjuster(()) ()
```


📍 *Расположение:* `pkg/util/oom/oom_linux.go:34`



---


[function] name: applyOOMScoreAdj file: pkg/util/oom/oom_linux.go:49 returns_error: нет description: Writes 'value' to /proc/<pid>/oom_score_adj. PID = 0 means self
Returns os.ErrNotExist if the `pid` does not exist.


### applyOOMScoreAdj (pkg/util/oom/oom_linux.go:49)


Writes 'value' to /proc/<pid>/oom_score_adj. PID = 0 means self
Returns os.ErrNotExist if the `pid` does not exist.


```go
func applyOOMScoreAdj((pid int, oomScoreAdj int)) (pid int, oomScoreAdj int)
```


**Тип ответа:** pid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oomScoreAdj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/oom/oom_linux.go:49`



---


[function] name: applyOOMScoreAdjContainer file: pkg/util/oom/oom_linux.go:88 returns_error: нет description: Writes 'value' to /proc/<pid>/oom_score_adj for all processes in cgroup cgroupName.
Keeps trying to write until the proc


### applyOOMScoreAdjContainer (pkg/util/oom/oom_linux.go:88)


Writes 'value' to /proc/<pid>/oom_score_adj for all processes in cgroup cgroupName.
Keeps trying to write until the process list of the cgroup stabilizes, or until maxTries tries.


```go
func (oomAdjuster *OOMAdjuster) applyOOMScoreAdjContainer((cgroupName string, oomScoreAdj, maxTries int)) (cgroupName string, oomScoreAdj, maxTries int)
```


**Тип ответа:** cgroupName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oomScoreAdj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxTries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/oom/oom_linux.go:88`



---


[function] name: getPids file: pkg/util/oom/oom_linux.go:43 returns_error: да description: —


### getPids (pkg/util/oom/oom_linux.go:43)


getPids is a function that performs operations based on the provided parameters and may return an error.


```go
func getPids(([]int, error)) ([]int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/oom/oom_linux.go:43`




## pkg/util/oom/oom_unsupported.go


📄 Исходный файл: `pkg/util/oom/oom_unsupported.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [NewOOMAdjuster](#newoomadjuster-pkgutiloomoom_unsupportedgo27) `:27`

- 🔗 [unsupportedApplyOOMScoreAdj](#unsupportedapplyoomscoreadj-pkgutiloomoom_unsupportedgo34) `:34`

- 🔗 [unsupportedApplyOOMScoreAdjContainer](#unsupportedapplyoomscoreadjcontainer-pkgutiloomoom_unsupportedgo38) `:38`


</details>


[function] name: NewOOMAdjuster file: pkg/util/oom/oom_unsupported.go:27 returns_error: нет description: —


### NewOOMAdjuster (pkg/util/oom/oom_unsupported.go:27)


NewOOMAdjuster is a function that performs operations based on the provided parameters and returns ().


```go
func NewOOMAdjuster(()) ()
```


📍 *Расположение:* `pkg/util/oom/oom_unsupported.go:27`



---


[function] name: unsupportedApplyOOMScoreAdj file: pkg/util/oom/oom_unsupported.go:34 returns_error: нет description: —


### unsupportedApplyOOMScoreAdj (pkg/util/oom/oom_unsupported.go:34)


unsupportedApplyOOMScoreAdj is a function that performs operations based on the provided parameters and returns (pid int, oomScoreAdj int).


```go
func unsupportedApplyOOMScoreAdj((pid int, oomScoreAdj int)) (pid int, oomScoreAdj int)
```


**Тип ответа:** pid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oomScoreAdj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/oom/oom_unsupported.go:34`



---


[function] name: unsupportedApplyOOMScoreAdjContainer file: pkg/util/oom/oom_unsupported.go:38 returns_error: нет description: —


### unsupportedApplyOOMScoreAdjContainer (pkg/util/oom/oom_unsupported.go:38)


unsupportedApplyOOMScoreAdjContainer is a function that performs operations based on the provided parameters and returns (cgroupName string, oomScoreAdj, maxTries int).


```go
func unsupportedApplyOOMScoreAdjContainer((cgroupName string, oomScoreAdj, maxTries int)) (cgroupName string, oomScoreAdj, maxTries int)
```


**Тип ответа:** cgroupName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oomScoreAdj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxTries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/oom/oom_unsupported.go:38`




## pkg/util/parsers/parsers.go


📄 Исходный файл: `pkg/util/parsers/parsers.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ParseCronScheduleWithPanicRecovery](#parsecronschedulewithpanicrecovery-pkgutilparsersparsersgo59) `:59`

- 🔗 [ParseImageName](#parseimagename-pkgutilparsersparsersgo32) `:32`


</details>


[function] name: ParseCronScheduleWithPanicRecovery file: pkg/util/parsers/parsers.go:59 returns_error: да description: ParseCronScheduleWithPanicRecovery safely parses a cron schedule, recovering from panics
that can occur in cron.ParseSta


### ParseCronScheduleWithPanicRecovery (pkg/util/parsers/parsers.go:59)


ParseCronScheduleWithPanicRecovery safely parses a cron schedule, recovering from panics
that can occur in cron.ParseStandard for malformed schedules like "TZ=0".


```go
func ParseCronScheduleWithPanicRecovery((sched cron.Schedule, err error)) (sched cron.Schedule, err error)
```


**Тип ответа:** sched


```json
{
  "prepareFn": {}
}
```


*Определено в:* `test/integration/scheduler_perf/options.go`


**Тип ответа:** cron.Schedule


```json
{
  "Parallelism": 0,
  "LeaderElection": {},
  "ClientConnection": {},
  "PercentageOfNodesToScore": 0,
  "PodInitialBackoffSeconds": 0,
  "PodMaxBackoffSeconds": 0,
  "Profiles": [],
  "Extenders": [],
  "DelayCacheUntilActive": false
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


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


*Типы возврата:* `sched cron.Schedule`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/parsers/parsers.go:59`



---


[function] name: ParseImageName file: pkg/util/parsers/parsers.go:32 returns_error: да description: ParseImageName parses a docker image string into three parts: repo, tag and digest.
If both tag and digest are empty, a 


### ParseImageName (pkg/util/parsers/parsers.go:32)


ParseImageName parses a docker image string into three parts: repo, tag and digest.
If both tag and digest are empty, a default image tag will be returned.


```go
func ParseImageName((string, string, string, error)) (string, string, string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `string`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/parsers/parsers.go:32`




## pkg/util/pod/pod.go


📄 Исходный файл: `pkg/util/pod/pod.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [PatchPodStatus](#patchpodstatus-pkgutilpodpodgo34) `:34`

- 🔗 [ReplaceOrAppendPodCondition](#replaceorappendpodcondition-pkgutilpodpodgo74) `:74`

- 🔗 [preparePatchBytesForPodStatus](#preparepatchbytesforpodstatus-pkgutilpodpodgo50) `:50`


</details>


[function] name: PatchPodStatus file: pkg/util/pod/pod.go:34 returns_error: да description: PatchPodStatus patches pod status. It returns true and avoids an update if the patch contains no changes.


### PatchPodStatus (pkg/util/pod/pod.go:34)


PatchPodStatus patches pod status. It returns true and avoids an update if the patch contains no changes.


```go
func PatchPodStatus((*v1.Pod, []byte, bool, error)) (*v1.Pod, []byte, bool, error)
```


**Тип запроса:** v1.Pod


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "CreatedAt": 0,
  "Containers": [],
  "Sandboxes": []
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** v1.Pod


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "CreatedAt": 0,
  "Containers": [],
  "Sandboxes": []
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.Pod`, `[]byte`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/pod/pod.go:34`



---


[function] name: ReplaceOrAppendPodCondition file: pkg/util/pod/pod.go:74 returns_error: нет description: ReplaceOrAppendPodCondition replaces the first pod condition with equal type or appends if there is none


### ReplaceOrAppendPodCondition (pkg/util/pod/pod.go:74)


ReplaceOrAppendPodCondition replaces the first pod condition with equal type or appends if there is none


```go
func ReplaceOrAppendPodCondition((conditions []v1.PodCondition, condition *v1.PodCondition)) (conditions []v1.PodCondition, condition *v1.PodCondition)
```


**Тип запроса:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** conditions


```json
{
  "UID": null,
  "ResourceVersion": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/preconditions.go`


**Тип ответа:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/pod/pod.go:74`



---


[function] name: preparePatchBytesForPodStatus file: pkg/util/pod/pod.go:50 returns_error: да description: —


### preparePatchBytesForPodStatus (pkg/util/pod/pod.go:50)


preparePatchBytesForPodStatus is a function that performs operations based on the provided parameters and may return an error.


```go
func preparePatchBytesForPodStatus(([]byte, bool, error)) ([]byte, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/pod/pod.go:50`




## pkg/util/procfs/procfs_fake.go


📄 Исходный файл: `pkg/util/procfs/procfs_fake.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetFullContainerName](#getfullcontainername-pkgutilprocfsprocfs_fakego24) `:24`


</details>


[function] name: GetFullContainerName file: pkg/util/procfs/procfs_fake.go:24 returns_error: да description: GetFullContainerName gets the container name given the root process id of the container.
E.g. if the devices cgroup for 


### GetFullContainerName (pkg/util/procfs/procfs_fake.go:24)


GetFullContainerName gets the container name given the root process id of the container.
E.g. if the devices cgroup for the container is stored in /sys/fs/cgroup/devices/docker/nginx,
return docker/nginx. Assumes that the process is part of exactly one cgroup hierarchy.


```go
func (fakePfs *FakeProcFS) GetFullContainerName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/procfs/procfs_fake.go:24`




## pkg/util/procfs/procfs_linux.go


📄 Исходный файл: `pkg/util/procfs/procfs_linux.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GetFullContainerName](#getfullcontainername-pkgutilprocfsprocfs_linuxgo55) `:55`

- 🔗 [PKill](#pkill-pkgutilprocfsprocfs_linuxgo69) `:69`

- 🔗 [PidOf](#pidof-pkgutilprocfsprocfs_linuxgo92) `:92`

- 🔗 [containerNameFromProcCgroup](#containernamefromproccgroup-pkgutilprocfsprocfs_linuxgo41) `:41`

- 🔗 [getPids](#getpids-pkgutilprocfsprocfs_linuxgo103) `:103`


</details>


[function] name: GetFullContainerName file: pkg/util/procfs/procfs_linux.go:55 returns_error: да description: GetFullContainerName gets the container name given the root process id of the container.
E.g. if the devices cgroup for 


### GetFullContainerName (pkg/util/procfs/procfs_linux.go:55)


GetFullContainerName gets the container name given the root process id of the container.
E.g. if the devices cgroup for the container is stored in /sys/fs/cgroup/devices/docker/nginx,
return docker/nginx. Assumes that the process is part of exactly one cgroup hierarchy.


```go
func (pfs *ProcFS) GetFullContainerName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/procfs/procfs_linux.go:55`



---


[function] name: PKill file: pkg/util/procfs/procfs_linux.go:69 returns_error: нет description: PKill finds process(es) using a regular expression and send a specified
signal to each process.


### PKill (pkg/util/procfs/procfs_linux.go:69)


PKill finds process(es) using a regular expression and send a specified
signal to each process.


```go
func PKill((name string, sig syscall.Signal)) (name string, sig syscall.Signal)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** sig


```json
{
  "fn": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/go-to-protobuf/protobuf/parser.go`


**Тип ответа:** syscall.Signal


```json
{
  "once": {},
  "done": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_context.go`


📍 *Расположение:* `pkg/util/procfs/procfs_linux.go:69`



---


[function] name: PidOf file: pkg/util/procfs/procfs_linux.go:92 returns_error: да description: PidOf finds process(es) with a specified name (regexp match)
and return their pid(s).


### PidOf (pkg/util/procfs/procfs_linux.go:92)


PidOf finds process(es) with a specified name (regexp match)
and return their pid(s).


```go
func PidOf(([]int, error)) ([]int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/procfs/procfs_linux.go:92`



---


[function] name: containerNameFromProcCgroup file: pkg/util/procfs/procfs_linux.go:41 returns_error: да description: —


### containerNameFromProcCgroup (pkg/util/procfs/procfs_linux.go:41)


containerNameFromProcCgroup is a function that performs operations based on the provided parameters and may return an error.


```go
func containerNameFromProcCgroup((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/procfs/procfs_linux.go:41`



---


[function] name: getPids file: pkg/util/procfs/procfs_linux.go:103 returns_error: нет description: —


### getPids (pkg/util/procfs/procfs_linux.go:103)


getPids is a function that performs operations based on the provided parameters and returns (re *regexp.Regexp).


```go
func getPids((re *regexp.Regexp)) (re *regexp.Regexp)
```


**Тип запроса:** regexp.Regexp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** re


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** regexp.Regexp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/procfs/procfs_linux.go:103`




## pkg/util/procfs/procfs_unsupported.go


📄 Исходный файл: `pkg/util/procfs/procfs_unsupported.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetFullContainerName](#getfullcontainername-pkgutilprocfsprocfs_unsupportedgo33) `:33`

- 🔗 [NewProcFS](#newprocfs-pkgutilprocfsprocfs_unsupportedgo28) `:28`

- 🔗 [PKill](#pkill-pkgutilprocfsprocfs_unsupportedgo39) `:39`

- 🔗 [PidOf](#pidof-pkgutilprocfsprocfs_unsupportedgo45) `:45`


</details>


[function] name: GetFullContainerName file: pkg/util/procfs/procfs_unsupported.go:33 returns_error: да description: GetFullContainerName gets the container name given the root process id of the container.


### GetFullContainerName (pkg/util/procfs/procfs_unsupported.go:33)


GetFullContainerName gets the container name given the root process id of the container.


```go
func (pfs *ProcFS) GetFullContainerName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/procfs/procfs_unsupported.go:33`



---


[function] name: NewProcFS file: pkg/util/procfs/procfs_unsupported.go:28 returns_error: нет description: —


### NewProcFS (pkg/util/procfs/procfs_unsupported.go:28)


NewProcFS is a function that performs operations based on the provided parameters and returns ().


```go
func NewProcFS(()) ()
```


📍 *Расположение:* `pkg/util/procfs/procfs_unsupported.go:28`



---


[function] name: PKill file: pkg/util/procfs/procfs_unsupported.go:39 returns_error: нет description: Find process(es) using a regular expression and send a specified
signal to each process


### PKill (pkg/util/procfs/procfs_unsupported.go:39)


Find process(es) using a regular expression and send a specified
signal to each process


```go
func PKill((name string, sig syscall.Signal)) (name string, sig syscall.Signal)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** sig


```json
{
  "fn": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/go-to-protobuf/protobuf/parser.go`


**Тип ответа:** syscall.Signal


```json
{
  "once": {},
  "done": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_context.go`


📍 *Расположение:* `pkg/util/procfs/procfs_unsupported.go:39`



---


[function] name: PidOf file: pkg/util/procfs/procfs_unsupported.go:45 returns_error: да description: Find process(es) with a specified name (exact match)
and return their pid(s)


### PidOf (pkg/util/procfs/procfs_unsupported.go:45)


Find process(es) with a specified name (exact match)
and return their pid(s)


```go
func PidOf(([]int, error)) ([]int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/procfs/procfs_unsupported.go:45`




## pkg/util/removeall/removeall.go


📄 Исходный файл: `pkg/util/removeall/removeall.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [RemoveAllOneFilesystem](#removeallonefilesystem-pkgutilremoveallremoveallgo115) `:115`

- 🔗 [RemoveAllOneFilesystemCommon](#removeallonefilesystemcommon-pkgutilremoveallremoveallgo35) `:35`

- 🔗 [RemoveDirsOneFilesystem](#removedirsonefilesystem-pkgutilremoveallremoveallgo126) `:126`


</details>


[function] name: RemoveAllOneFilesystem file: pkg/util/removeall/removeall.go:115 returns_error: нет description: RemoveAllOneFilesystem removes the path and any children it contains, using
the os.Remove function. It makes sure it doe


### RemoveAllOneFilesystem (pkg/util/removeall/removeall.go:115)


RemoveAllOneFilesystem removes the path and any children it contains, using
the os.Remove function. It makes sure it does not cross mount boundaries,
i.e. it returns an error rather than remove files from another filesystem.
It removes everything it can but returns the first error it encounters.
If the path does not exist, it returns nil (no error).


```go
func RemoveAllOneFilesystem((mounter mount.Interface, path string)) (mounter mount.Interface, path string)
```


**Тип ответа:** mounter


```json
{
  "mounter": {},
  "exec": {},
  "deviceUtil": {}
}
```


*Определено в:* `pkg/volume/iscsi/iscsi.go`


**Тип ответа:** mount.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `pkg/util/removeall/removeall.go:115`



---


[function] name: RemoveAllOneFilesystemCommon file: pkg/util/removeall/removeall.go:35 returns_error: да description: RemoveAllOneFilesystemCommon removes the path and any children it contains,
using the provided remove function. It remov


### RemoveAllOneFilesystemCommon (pkg/util/removeall/removeall.go:35)


RemoveAllOneFilesystemCommon removes the path and any children it contains,
using the provided remove function. It removes everything it can but returns
the first error it encounters. If the path does not exist, RemoveAll
returns nil (no error).
It makes sure it does not cross mount boundary, i.e. it does *not* remove
files from another filesystems. Like 'rm -rf --one-file-system'.
It is copied from RemoveAll() sources, with IsLikelyNotMountPoint


```go
func RemoveAllOneFilesystemCommon((mounter mount.Interface, path string, remove func(string) error)) (mounter mount.Interface, path string, remove func(string) error)
```


**Тип ответа:** mounter


```json
{
  "mounter": {},
  "exec": {},
  "deviceUtil": {}
}
```


*Определено в:* `pkg/volume/iscsi/iscsi.go`


**Тип ответа:** mount.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** remove


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `mounter mount.Interface`, `path string`, `remove func(string) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/removeall/removeall.go:35`



---


[function] name: RemoveDirsOneFilesystem file: pkg/util/removeall/removeall.go:126 returns_error: нет description: RemoveDirsOneFilesystem removes the path and any empty subdirectories it
contains, using the syscall.Rmdir function. Unl


### RemoveDirsOneFilesystem (pkg/util/removeall/removeall.go:126)


RemoveDirsOneFilesystem removes the path and any empty subdirectories it
contains, using the syscall.Rmdir function. Unlike RemoveAllOneFilesystem,
RemoveDirsOneFilesystem will remove only directories and returns an error if
it encounters any files in the directory tree. It makes sure it does not
cross mount boundaries, i.e. it returns an error rather than remove dirs
from another filesystem. It removes everything it can but returns the first
error it encounters. If the path does not exist, it returns nil (no error).


```go
func RemoveDirsOneFilesystem((mounter mount.Interface, path string)) (mounter mount.Interface, path string)
```


**Тип ответа:** mounter


```json
{
  "mounter": {},
  "exec": {},
  "deviceUtil": {}
}
```


*Определено в:* `pkg/volume/iscsi/iscsi.go`


**Тип ответа:** mount.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `pkg/util/removeall/removeall.go:126`




## pkg/util/rlimit/rlimit_linux.go


📄 Исходный файл: `pkg/util/rlimit/rlimit_linux.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetNumFiles](#setnumfiles-pkgutilrlimitrlimit_linuxgo26) `:26`


</details>


[function] name: SetNumFiles file: pkg/util/rlimit/rlimit_linux.go:26 returns_error: нет description: SetNumFiles sets the linux rlimit for the maximum open files.


### SetNumFiles (pkg/util/rlimit/rlimit_linux.go:26)


SetNumFiles sets the linux rlimit for the maximum open files.


```go
func SetNumFiles((maxOpenFiles uint64)) (maxOpenFiles uint64)
```


**Тип ответа:** maxOpenFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/rlimit/rlimit_linux.go:26`




## pkg/util/rlimit/rlimit_unsupported.go


📄 Исходный файл: `pkg/util/rlimit/rlimit_unsupported.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetNumFiles](#setnumfiles-pkgutilrlimitrlimit_unsupportedgo26) `:26`


</details>


[function] name: SetNumFiles file: pkg/util/rlimit/rlimit_unsupported.go:26 returns_error: нет description: SetNumFiles sets the rlimit for the maximum open files.


### SetNumFiles (pkg/util/rlimit/rlimit_unsupported.go:26)


SetNumFiles sets the rlimit for the maximum open files.


```go
func SetNumFiles((maxOpenFiles uint64)) (maxOpenFiles uint64)
```


**Тип ответа:** maxOpenFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/rlimit/rlimit_unsupported.go:26`




## pkg/util/slice/slice.go


📄 Исходный файл: `pkg/util/slice/slice.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [ContainsString](#containsstring-pkgutilsliceslicego47) `:47`

- 🔗 [CopyStrings](#copystrings-pkgutilsliceslicego30) `:30`

- 🔗 [RemoveString](#removestring-pkgutilsliceslicego59) `:59`

- 🔗 [SortStrings](#sortstrings-pkgutilsliceslicego38) `:38`


</details>


[function] name: ContainsString file: pkg/util/slice/slice.go:47 returns_error: нет description: ContainsString checks if a given slice of strings contains the provided string.
If a modifier func is provided, it is ca


### ContainsString (pkg/util/slice/slice.go:47)


ContainsString checks if a given slice of strings contains the provided string.
If a modifier func is provided, it is called with the slice item before the comparation.

Deprecated: Use slices.ContainsFunc or slices.Contains instead.


```go
func ContainsString((slice []string, s string, modifier func(s string) string)) (slice []string, s string, modifier func(s string) string)
```


**Тип ответа:** slice


```json
{
  "elements": [],
  "idx": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/common/valuesreflect.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** modifier


```json
{
  "allTypes": false,
  "output": false,
  "name": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/go-to-protobuf/protobuf/cmd.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/slice/slice.go:47`



---


[function] name: CopyStrings file: pkg/util/slice/slice.go:30 returns_error: нет description: CopyStrings copies the contents of the specified string slice
into a new slice.

Deprecated: Use slices.Clone instead.




### CopyStrings (pkg/util/slice/slice.go:30)


CopyStrings copies the contents of the specified string slice
into a new slice.

Deprecated: Use slices.Clone instead.

go:fix inline


```go
func CopyStrings((s []string)) (s []string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/slice/slice.go:30`



---


[function] name: RemoveString file: pkg/util/slice/slice.go:59 returns_error: нет description: RemoveString returns a newly created []string that contains all items from slice that
are not equal to s and modifier(s)


### RemoveString (pkg/util/slice/slice.go:59)


RemoveString returns a newly created []string that contains all items from slice that
are not equal to s and modifier(s) in case modifier func is provided.


```go
func RemoveString((slice []string, s string, modifier func(s string) string)) (slice []string, s string, modifier func(s string) string)
```


**Тип ответа:** slice


```json
{
  "elements": [],
  "idx": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/common/valuesreflect.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** modifier


```json
{
  "allTypes": false,
  "output": false,
  "name": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/go-to-protobuf/protobuf/cmd.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/slice/slice.go:59`



---


[function] name: SortStrings file: pkg/util/slice/slice.go:38 returns_error: нет description: SortStrings sorts the specified string slice in place. It returns the same
slice that was provided in order to facilitat


### SortStrings (pkg/util/slice/slice.go:38)


SortStrings sorts the specified string slice in place. It returns the same
slice that was provided in order to facilitate method chaining.

Deprecated: Use slices.Sort instead.


```go
func SortStrings((s []string)) (s []string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/util/slice/slice.go:38`




## pkg/util/tail/tail.go


📄 Исходный файл: `pkg/util/tail/tail.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ReadAtMost](#readatmost-pkgutiltailtailgo32) `:32`


</details>


[function] name: ReadAtMost file: pkg/util/tail/tail.go:32 returns_error: да description: ReadAtMost reads at most max bytes from the end of the file identified by path or
returns an error. It returns true if t


### ReadAtMost (pkg/util/tail/tail.go:32)


ReadAtMost reads at most max bytes from the end of the file identified by path or
returns an error. It returns true if the file was longer than max. It will
allocate up to max bytes.


```go
func ReadAtMost(([]byte, bool, error)) ([]byte, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/tail/tail.go:32`




## pkg/util/taints/taints.go


📄 Исходный файл: `pkg/util/taints/taints.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [AddOrUpdateTaint](#addorupdatetaint-pkgutiltaintstaintsgo188) `:188`

- 🔗 [CheckIfTaintsAlreadyExists](#checkiftaintsalreadyexists-pkgutiltaintstaintsgo128) `:128`

- 🔗 [CheckTaintValidation](#checktaintvalidation-pkgutiltaintstaintsgo273) `:273`

- 🔗 [DeleteTaint](#deletetaint-pkgutiltaintstaintsgo155) `:155`

- 🔗 [DeleteTaintsByKey](#deletetaintsbykey-pkgutiltaintstaintsgo141) `:141`

- 🔗 [ParseTaints](#parsetaints-pkgutiltaintstaintsgo91) `:91`

- 🔗 [RemoveTaint](#removetaint-pkgutiltaintstaintsgo170) `:170`

- 🔗 [TaintExists](#taintexists-pkgutiltaintstaintsgo216) `:216`

- 🔗 [TaintKeyExists](#taintkeyexists-pkgutiltaintstaintsgo226) `:226`

- 🔗 [TaintSetDiff](#taintsetdiff-pkgutiltaintstaintsgo240) `:240`

- 🔗 [TaintSetFilter](#taintsetfilter-pkgutiltaintstaintsgo259) `:259`

- 🔗 [parseTaint](#parsetaint-pkgutiltaintstaintsgo38) `:38`

- 🔗 [validateTaintEffect](#validatetainteffect-pkgutiltaintstaintsgo81) `:81`


</details>


[function] name: AddOrUpdateTaint file: pkg/util/taints/taints.go:188 returns_error: да description: AddOrUpdateTaint tries to add a taint to annotations list. Returns a new copy of updated Node and true if something was 


### AddOrUpdateTaint (pkg/util/taints/taints.go:188)


AddOrUpdateTaint tries to add a taint to annotations list. Returns a new copy of updated Node and true if something was updated
false otherwise.


```go
func AddOrUpdateTaint((*v1.Node, bool, error)) (*v1.Node, bool, error)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.Node`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/taints/taints.go:188`



---


[function] name: CheckIfTaintsAlreadyExists file: pkg/util/taints/taints.go:128 returns_error: нет description: CheckIfTaintsAlreadyExists checks if the node already has taints that we want to add and returns a string with taint key


### CheckIfTaintsAlreadyExists (pkg/util/taints/taints.go:128)


CheckIfTaintsAlreadyExists checks if the node already has taints that we want to add and returns a string with taint keys.


```go
func CheckIfTaintsAlreadyExists((oldTaints []v1.Taint, taints []v1.Taint)) (oldTaints []v1.Taint, taints []v1.Taint)
```


**Тип ответа:** oldTaints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/taints/taints.go:128`



---


[function] name: CheckTaintValidation file: pkg/util/taints/taints.go:273 returns_error: нет description: CheckTaintValidation checks if the given taint is valid.
Returns error if the given taint is invalid.


### CheckTaintValidation (pkg/util/taints/taints.go:273)


CheckTaintValidation checks if the given taint is valid.
Returns error if the given taint is invalid.


```go
func CheckTaintValidation((taint v1.Taint)) (taint v1.Taint)
```


**Тип ответа:** taint


```json
{
  "numEvictedPods": 0
}
```


*Определено в:* `pkg/controller/devicetainteviction/device_taint_eviction.go`


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/taints/taints.go:273`



---


[function] name: DeleteTaint file: pkg/util/taints/taints.go:155 returns_error: нет description: DeleteTaint removes all the taints that have the same key and effect to given taintToDelete.


### DeleteTaint (pkg/util/taints/taints.go:155)


DeleteTaint removes all the taints that have the same key and effect to given taintToDelete.


```go
func DeleteTaint(([]v1.Taint, bool)) ([]v1.Taint, bool)
```


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/taints/taints.go:155`



---


[function] name: DeleteTaintsByKey file: pkg/util/taints/taints.go:141 returns_error: нет description: DeleteTaintsByKey removes all the taints that have the same key to given taintKey


### DeleteTaintsByKey (pkg/util/taints/taints.go:141)


DeleteTaintsByKey removes all the taints that have the same key to given taintKey


```go
func DeleteTaintsByKey(([]v1.Taint, bool)) ([]v1.Taint, bool)
```


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/taints/taints.go:141`



---


[function] name: ParseTaints file: pkg/util/taints/taints.go:91 returns_error: да description: ParseTaints takes a spec which is an array and creates slices for new taints to be added, taints to be deleted.
It also 


### ParseTaints (pkg/util/taints/taints.go:91)


ParseTaints takes a spec which is an array and creates slices for new taints to be added, taints to be deleted.
It also validates the spec. For example, the form `<key>` may be used to remove a taint, but not to add one.


```go
func ParseTaints(([]v1.Taint, []v1.Taint, error)) ([]v1.Taint, []v1.Taint, error)
```


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]v1.Taint`, `[]v1.Taint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/taints/taints.go:91`



---


[function] name: RemoveTaint file: pkg/util/taints/taints.go:170 returns_error: да description: RemoveTaint tries to remove a taint from annotations list. Returns a new copy of updated Node and true if something was 


### RemoveTaint (pkg/util/taints/taints.go:170)


RemoveTaint tries to remove a taint from annotations list. Returns a new copy of updated Node and true if something was updated
false otherwise.


```go
func RemoveTaint((*v1.Node, bool, error)) (*v1.Node, bool, error)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.Node`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/taints/taints.go:170`



---


[function] name: TaintExists file: pkg/util/taints/taints.go:216 returns_error: нет description: TaintExists checks if the given taint exists in list of taints. Returns true if exists false otherwise.


### TaintExists (pkg/util/taints/taints.go:216)


TaintExists checks if the given taint exists in list of taints. Returns true if exists false otherwise.


```go
func TaintExists((taints []v1.Taint, taintToFind *v1.Taint)) (taints []v1.Taint, taintToFind *v1.Taint)
```


**Тип запроса:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taintToFind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/taints/taints.go:216`



---


[function] name: TaintKeyExists file: pkg/util/taints/taints.go:226 returns_error: нет description: TaintKeyExists checks if the given taint key exists in list of taints. Returns true if exists false otherwise.


### TaintKeyExists (pkg/util/taints/taints.go:226)


TaintKeyExists checks if the given taint key exists in list of taints. Returns true if exists false otherwise.


```go
func TaintKeyExists((taints []v1.Taint, taintKeyToMatch string)) (taints []v1.Taint, taintKeyToMatch string)
```


**Тип ответа:** taints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taintKeyToMatch


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/taints/taints.go:226`



---


[function] name: TaintSetDiff file: pkg/util/taints/taints.go:240 returns_error: нет description: TaintSetDiff finds the difference between two taint slices and
returns all new and removed elements of the new slice rel


### TaintSetDiff (pkg/util/taints/taints.go:240)


TaintSetDiff finds the difference between two taint slices and
returns all new and removed elements of the new slice relative to the old slice.
for example:
input: taintsNew=[a b] taintsOld=[a c]
output: taintsToAdd=[b] taintsToRemove=[c]


```go
func TaintSetDiff((taintsToAdd []*v1.Taint, taintsToRemove []*v1.Taint)) (taintsToAdd []*v1.Taint, taintsToRemove []*v1.Taint)
```


**Тип запроса:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taintsToAdd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taintsToRemove


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/taints/taints.go:240`



---


[function] name: TaintSetFilter file: pkg/util/taints/taints.go:259 returns_error: нет description: TaintSetFilter filters from the taint slice according to the passed fn function to get the filtered taint slice.


### TaintSetFilter (pkg/util/taints/taints.go:259)


TaintSetFilter filters from the taint slice according to the passed fn function to get the filtered taint slice.


```go
func TaintSetFilter((taints []v1.Taint, fn func(*v1.Taint) bool)) (taints []v1.Taint, fn func(*v1.Taint) bool)
```


**Тип запроса:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/taints/taints.go:259`



---


[function] name: parseTaint file: pkg/util/taints/taints.go:38 returns_error: да description: parseTaint parses a taint from a string, whose form must be either
'<key>=<value>:<effect>', '<key>:<effect>', or '<key>


### parseTaint (pkg/util/taints/taints.go:38)


parseTaint parses a taint from a string, whose form must be either
'<key>=<value>:<effect>', '<key>:<effect>', or '<key>'.


```go
func parseTaint((v1.Taint, error)) (v1.Taint, error)
```


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `v1.Taint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/util/taints/taints.go:38`



---


[function] name: validateTaintEffect file: pkg/util/taints/taints.go:81 returns_error: нет description: —


### validateTaintEffect (pkg/util/taints/taints.go:81)


validateTaintEffect is a function that performs operations based on the provided parameters and returns (effect v1.TaintEffect).


```go
func validateTaintEffect((effect v1.TaintEffect)) (effect v1.TaintEffect)
```


**Тип ответа:** effect


```json
{
  "useDefaultBuildBinaryVersion": {},
  "binaryVersion": {},
  "emulationVersion": {},
  "minCompatibilityVersion": {},
  "emulationVersionFloor": null,
  "minCompatibilityVersionFloor": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/compatibility/version.go`


**Тип ответа:** v1.TaintEffect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/util/taints/taints.go:81`




## pkg/util/tolerations/tolerations.go


📄 Исходный файл: `pkg/util/tolerations/tolerations.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MergeTolerations](#mergetolerations-pkgutiltolerationstolerationsgo47) `:47`

- 🔗 [VerifyAgainstWhitelist](#verifyagainstwhitelist-pkgutiltolerationstolerationsgo27) `:27`

- 🔗 [isSuperset](#issuperset-pkgutiltolerationstolerationsgo73) `:73`


</details>


[function] name: MergeTolerations file: pkg/util/tolerations/tolerations.go:47 returns_error: нет description: MergeTolerations merges two sets of tolerations into one. If one toleration is a superset of
another, only the superset 


### MergeTolerations (pkg/util/tolerations/tolerations.go:47)


MergeTolerations merges two sets of tolerations into one. If one toleration is a superset of
another, only the superset is kept.


```go
func MergeTolerations((first, second []api.Toleration)) (first, second []api.Toleration)
```


**Тип ответа:** first


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** second


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Toleration


```json
{
  "Key": "string",
  "Operator": {},
  "Value": "string",
  "Effect": {},
  "TolerationSeconds": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/tolerations/tolerations.go:47`



---


[function] name: VerifyAgainstWhitelist file: pkg/util/tolerations/tolerations.go:27 returns_error: нет description: VerifyAgainstWhitelist checks if the provided tolerations
satisfy the provided whitelist and returns true, otherwise ret


### VerifyAgainstWhitelist (pkg/util/tolerations/tolerations.go:27)


VerifyAgainstWhitelist checks if the provided tolerations
satisfy the provided whitelist and returns true, otherwise returns false


```go
func VerifyAgainstWhitelist((tolerations, whitelist []api.Toleration)) (tolerations, whitelist []api.Toleration)
```


**Тип ответа:** tolerations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** whitelist


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Toleration


```json
{
  "Key": "string",
  "Operator": {},
  "Value": "string",
  "Effect": {},
  "TolerationSeconds": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/tolerations/tolerations.go:27`



---


[function] name: isSuperset file: pkg/util/tolerations/tolerations.go:73 returns_error: нет description: isSuperset checks whether ss tolerates a superset of t.


### isSuperset (pkg/util/tolerations/tolerations.go:73)


isSuperset checks whether ss tolerates a superset of t.


```go
func isSuperset((ss, t api.Toleration)) (ss, t api.Toleration)
```


**Тип ответа:** ss


```json
{
  "incomingImports": {},
  "transitiveIncomingImports": {}
}
```


*Определено в:* `cmd/import-boss/main.go`


**Тип ответа:** t


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** api.Toleration


```json
{
  "Key": "string",
  "Operator": {},
  "Value": "string",
  "Effect": {},
  "TolerationSeconds": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/util/tolerations/tolerations.go:73`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_serviceaccount.md)

- [Следующая директория](pkg_volume.md)


---

