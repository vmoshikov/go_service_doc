---
title: "Функции: cmd/kube-scheduler"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/kube-scheduler
---


# Функции: cmd/kube-scheduler


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kube-proxy.md)

- [Следующая директория](cmd_kubeadm.md)


---


## Меню по файлам


- 📄 [cmd/kube-scheduler/app/config/config.go](#cmdkube-schedulerappconfigconfiggo)

- 📄 [cmd/kube-scheduler/app/options/configfile.go](#cmdkube-schedulerappoptionsconfigfilego)

- 📄 [cmd/kube-scheduler/app/options/deprecated.go](#cmdkube-schedulerappoptionsdeprecatedgo)

- 📄 [cmd/kube-scheduler/app/options/options.go](#cmdkube-schedulerappoptionsoptionsgo)

- 📄 [cmd/kube-scheduler/app/server.go](#cmdkube-schedulerappservergo)

- 📄 [cmd/kube-scheduler/app/testing/testserver.go](#cmdkube-schedulerapptestingtestservergo)

- 📄 [cmd/kube-scheduler/scheduler.go](#cmdkube-schedulerschedulergo)


---


## cmd/kube-scheduler/app/config/config.go


📄 Исходный файл: `cmd/kube-scheduler/app/config/config.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Complete](#complete-cmdkube-schedulerappconfigconfiggo78) `:78`


</details>


[function] name: Complete file: cmd/kube-scheduler/app/config/config.go:78 returns_error: нет description: Complete fills in any fields not set that are required to have valid data. It's mutating the receiver.


### Complete (cmd/kube-scheduler/app/config/config.go:78)


Complete fills in any fields not set that are required to have valid data. It's mutating the receiver.


```go
func (c *Config) Complete(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/app/config/config.go:78`




## cmd/kube-scheduler/app/options/configfile.go


📄 Исходный файл: `cmd/kube-scheduler/app/options/configfile.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [LoadConfigFromFile](#loadconfigfromfile-cmdkube-schedulerappoptionsconfigfilego33) `:33`

- 🔗 [LogOrWriteConfig](#logorwriteconfig-cmdkube-schedulerappoptionsconfigfilego81) `:81`

- 🔗 [encodeConfig](#encodeconfig-cmdkube-schedulerappoptionsconfigfilego59) `:59`

- 🔗 [loadConfig](#loadconfig-cmdkube-schedulerappoptionsconfigfilego42) `:42`


</details>


[function] name: LoadConfigFromFile file: cmd/kube-scheduler/app/options/configfile.go:33 returns_error: да description: LoadConfigFromFile loads scheduler config from the specified file path


### LoadConfigFromFile (cmd/kube-scheduler/app/options/configfile.go:33)


LoadConfigFromFile loads scheduler config from the specified file path


```go
func LoadConfigFromFile((*config.KubeSchedulerConfiguration, error)) (*config.KubeSchedulerConfiguration, error)
```


**Тип запроса:** config.KubeSchedulerConfiguration


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


**Тип ответа:** config.KubeSchedulerConfiguration


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*config.KubeSchedulerConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/options/configfile.go:33`



---


[function] name: LogOrWriteConfig file: cmd/kube-scheduler/app/options/configfile.go:81 returns_error: нет description: LogOrWriteConfig logs the completed component config and writes it into the given file name as YAML, if either is enable


### LogOrWriteConfig (cmd/kube-scheduler/app/options/configfile.go:81)


LogOrWriteConfig logs the completed component config and writes it into the given file name as YAML, if either is enabled


```go
func LogOrWriteConfig((logger klog.Logger, fileName string, cfg *config.KubeSchedulerConfiguration, completedProfiles []config.KubeSchedulerProfile)) (logger klog.Logger, fileName string, cfg *config.KubeSchedulerConfiguration, completedProfiles []config.KubeSchedulerProfile)
```


**Тип запроса:** config.KubeSchedulerConfiguration


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


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** fileName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** config.KubeSchedulerConfiguration


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


**Тип ответа:** completedProfiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.KubeSchedulerProfile


```json
{
  "SchedulerName": "string",
  "PercentageOfNodesToScore": 0,
  "Plugins": null,
  "PluginConfig": []
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


📍 *Расположение:* `cmd/kube-scheduler/app/options/configfile.go:81`



---


[function] name: encodeConfig file: cmd/kube-scheduler/app/options/configfile.go:59 returns_error: да description: —


### encodeConfig (cmd/kube-scheduler/app/options/configfile.go:59)


encodeConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func encodeConfig((*bytes.Buffer, error)) (*bytes.Buffer, error)
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


**Тип ответа:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*bytes.Buffer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/options/configfile.go:59`



---


[function] name: loadConfig file: cmd/kube-scheduler/app/options/configfile.go:42 returns_error: да description: —


### loadConfig (cmd/kube-scheduler/app/options/configfile.go:42)


loadConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func loadConfig((*config.KubeSchedulerConfiguration, error)) (*config.KubeSchedulerConfiguration, error)
```


**Тип запроса:** config.KubeSchedulerConfiguration


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


**Тип ответа:** config.KubeSchedulerConfiguration


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*config.KubeSchedulerConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/options/configfile.go:42`




## cmd/kube-scheduler/app/options/deprecated.go


📄 Исходный файл: `cmd/kube-scheduler/app/options/deprecated.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-schedulerappoptionsdeprecatedgo39) `:39`


</details>


[function] name: AddFlags file: cmd/kube-scheduler/app/options/deprecated.go:39 returns_error: нет description: AddFlags adds flags for the deprecated options.


### AddFlags (cmd/kube-scheduler/app/options/deprecated.go:39)


AddFlags adds flags for the deprecated options.


```go
func (o *DeprecatedOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
```


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** fs


```json
{
  "EndpointsName": "string",
  "Path": "string",
  "ReadOnly": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/glusterfsvolumesource.go`


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


📍 *Расположение:* `cmd/kube-scheduler/app/options/deprecated.go:39`




## cmd/kube-scheduler/app/options/options.go


📄 Исходный файл: `cmd/kube-scheduler/app/options/options.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [ApplyDeprecated](#applydeprecated-cmdkube-schedulerappoptionsoptionsgo136) `:136`

- 🔗 [ApplyLeaderElectionTo](#applyleaderelectionto-cmdkube-schedulerappoptionsoptionsgo164) `:164`

- 🔗 [ApplyTo](#applyto-cmdkube-schedulerappoptionsoptionsgo220) `:220`

- 🔗 [Config](#config-cmdkube-schedulerappoptionsoptionsgo299) `:299`

- 🔗 [NewOptions](#newoptions-cmdkube-schedulerappoptionsoptionsgo88) `:88`

- 🔗 [NewOptionsWithComponentGlobalsRegistry](#newoptionswithcomponentglobalsregistry-cmdkube-schedulerappoptionsoptionsgo99) `:99`

- 🔗 [Validate](#validate-cmdkube-schedulerappoptionsoptionsgo280) `:280`

- 🔗 [createClients](#createclients-cmdkube-schedulerappoptionsoptionsgo397) `:397`

- 🔗 [createKubeConfig](#createkubeconfig-cmdkube-schedulerappoptionsoptionsgo381) `:381`

- 🔗 [initFlags](#initflags-cmdkube-schedulerappoptionsoptionsgo196) `:196`

- 🔗 [makeLeaderElectionConfig](#makeleaderelectionconfig-cmdkube-schedulerappoptionsoptionsgo347) `:347`


</details>


[function] name: ApplyDeprecated file: cmd/kube-scheduler/app/options/options.go:136 returns_error: нет description: ApplyDeprecated obtains the deprecated CLI args and set them to `o.ComponentConfig` if specified.


### ApplyDeprecated (cmd/kube-scheduler/app/options/options.go:136)


ApplyDeprecated obtains the deprecated CLI args and set them to `o.ComponentConfig` if specified.


```go
func (o *Options) ApplyDeprecated(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:136`



---


[function] name: ApplyLeaderElectionTo file: cmd/kube-scheduler/app/options/options.go:164 returns_error: нет description: ApplyLeaderElectionTo obtains the CLI args related with leaderelection, and override the values in `cfg`.
Then the `cfg`


### ApplyLeaderElectionTo (cmd/kube-scheduler/app/options/options.go:164)


ApplyLeaderElectionTo obtains the CLI args related with leaderelection, and override the values in `cfg`.
Then the `cfg` object is injected into the `options` object.


```go
func (o *Options) ApplyLeaderElectionTo((cfg *kubeschedulerconfig.KubeSchedulerConfiguration)) (cfg *kubeschedulerconfig.KubeSchedulerConfiguration)
```


**Тип запроса:** kubeschedulerconfig.KubeSchedulerConfiguration


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


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** kubeschedulerconfig.KubeSchedulerConfiguration


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


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:164`



---


[function] name: ApplyTo file: cmd/kube-scheduler/app/options/options.go:220 returns_error: нет description: ApplyTo applies the scheduler options to the given scheduler app configuration.


### ApplyTo (cmd/kube-scheduler/app/options/options.go:220)


ApplyTo applies the scheduler options to the given scheduler app configuration.


```go
func (o *Options) ApplyTo((logger klog.Logger, c *schedulerappconfig.Config)) (logger klog.Logger, c *schedulerappconfig.Config)
```


**Тип запроса:** schedulerappconfig.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** c


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


**Тип ответа:** schedulerappconfig.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:220`



---


[function] name: Config file: cmd/kube-scheduler/app/options/options.go:299 returns_error: да description: Config return a scheduler config object


### Config (cmd/kube-scheduler/app/options/options.go:299)


Config return a scheduler config object


```go
func (o *Options) Config((*schedulerappconfig.Config, error)) (*schedulerappconfig.Config, error)
```


**Тип запроса:** schedulerappconfig.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** schedulerappconfig.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*schedulerappconfig.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:299`



---


[function] name: NewOptions file: cmd/kube-scheduler/app/options/options.go:88 returns_error: нет description: NewOptions returns default scheduler app options.


### NewOptions (cmd/kube-scheduler/app/options/options.go:88)


NewOptions returns default scheduler app options.


```go
func NewOptions(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:88`



---


[function] name: NewOptionsWithComponentGlobalsRegistry file: cmd/kube-scheduler/app/options/options.go:99 returns_error: нет description: —


### NewOptionsWithComponentGlobalsRegistry (cmd/kube-scheduler/app/options/options.go:99)


NewOptionsWithComponentGlobalsRegistry is a function that performs operations based on the provided parameters and returns (componentGlobalsRegistry basecompatibility.ComponentGlobalsRegistry).


```go
func NewOptionsWithComponentGlobalsRegistry((componentGlobalsRegistry basecompatibility.ComponentGlobalsRegistry)) (componentGlobalsRegistry basecompatibility.ComponentGlobalsRegistry)
```


**Тип ответа:** componentGlobalsRegistry


```json
{
  "componentGlobals": {},
  "mutex": {},
  "emulationVersionConfig": [],
  "minCompatibilityVersionConfig": [],
  "featureGatesConfig": {},
  "featureGatesConfigFlags": null,
  "set": false
}
```


*Определено в:* `staging/src/k8s.io/component-base/compatibility/registry.go`


**Тип ответа:** basecompatibility.ComponentGlobalsRegistry


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:99`



---


[function] name: Validate file: cmd/kube-scheduler/app/options/options.go:280 returns_error: нет description: Validate validates all the required options.


### Validate (cmd/kube-scheduler/app/options/options.go:280)


Validate validates all the required options.


```go
func (o *Options) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:280`



---


[function] name: createClients file: cmd/kube-scheduler/app/options/options.go:397 returns_error: да description: createClients creates a kube client and an event client from the given kubeConfig


### createClients (cmd/kube-scheduler/app/options/options.go:397)


createClients creates a kube client and an event client from the given kubeConfig


```go
func createClients((clientset.Interface, clientset.Interface, error)) (clientset.Interface, clientset.Interface, error)
```


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `clientset.Interface`, `clientset.Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:397`



---


[function] name: createKubeConfig file: cmd/kube-scheduler/app/options/options.go:381 returns_error: да description: createKubeConfig creates a kubeConfig from the given config and masterOverride.
TODO remove masterOverride when CLI flag


### createKubeConfig (cmd/kube-scheduler/app/options/options.go:381)


createKubeConfig creates a kubeConfig from the given config and masterOverride.
TODO remove masterOverride when CLI flags are removed.


```go
func createKubeConfig((*restclient.Config, error)) (*restclient.Config, error)
```


**Тип запроса:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*restclient.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:381`



---


[function] name: initFlags file: cmd/kube-scheduler/app/options/options.go:196 returns_error: нет description: initFlags initializes flags by section name.


### initFlags (cmd/kube-scheduler/app/options/options.go:196)


initFlags initializes flags by section name.


```go
func (o *Options) initFlags(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:196`



---


[function] name: makeLeaderElectionConfig file: cmd/kube-scheduler/app/options/options.go:347 returns_error: да description: makeLeaderElectionConfig builds a leader election configuration. It will
create a new resource lock associated with the 


### makeLeaderElectionConfig (cmd/kube-scheduler/app/options/options.go:347)


makeLeaderElectionConfig builds a leader election configuration. It will
create a new resource lock associated with the configuration.


```go
func makeLeaderElectionConfig((*leaderelection.LeaderElectionConfig, error)) (*leaderelection.LeaderElectionConfig, error)
```


**Тип запроса:** leaderelection.LeaderElectionConfig


```json
{
  "Lock": {},
  "LeaseDuration": {},
  "RenewDeadline": {},
  "RetryPeriod": {},
  "Callbacks": {},
  "WatchDog": null,
  "ReleaseOnCancel": false,
  "Name": "string",
  "Coordinated": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/leaderelection/leaderelection.go`


**Тип ответа:** leaderelection.LeaderElectionConfig


```json
{
  "Lock": {},
  "LeaseDuration": {},
  "RenewDeadline": {},
  "RetryPeriod": {},
  "Callbacks": {},
  "WatchDog": null,
  "ReleaseOnCancel": false,
  "Name": "string",
  "Coordinated": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/leaderelection/leaderelection.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*leaderelection.LeaderElectionConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/options/options.go:347`




## cmd/kube-scheduler/app/server.go


📄 Исходный файл: `cmd/kube-scheduler/app/server.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [NewSchedulerCommand](#newschedulercommand-cmdkube-schedulerappservergo90) `:90`

- 🔗 [Run](#run-cmdkube-schedulerappservergo171) `:171`

- 🔗 [Setup](#setup-cmdkube-schedulerappservergo416) `:416`

- 🔗 [WithPlugin](#withplugin-cmdkube-schedulerappservergo409) `:409`

- 🔗 [buildHandlerChain](#buildhandlerchain-cmdkube-schedulerappservergo342) `:342`

- 🔗 [getRecorderFactory](#getrecorderfactory-cmdkube-schedulerappservergo401) `:401`

- 🔗 [init](#init-cmdkube-schedulerappservergo81) `:81`

- 🔗 [installMetricHandler](#installmetrichandler-cmdkube-schedulerappservergo356) `:356`

- 🔗 [newEndpointsHandler](#newendpointshandler-cmdkube-schedulerappservergo372) `:372`

- 🔗 [runCommand](#runcommand-cmdkube-schedulerappservergo139) `:139`


</details>


[function] name: NewSchedulerCommand file: cmd/kube-scheduler/app/server.go:90 returns_error: нет description: NewSchedulerCommand creates a *cobra.Command object with default parameters and registryOptions


### NewSchedulerCommand (cmd/kube-scheduler/app/server.go:90)


NewSchedulerCommand creates a *cobra.Command object with default parameters and registryOptions


```go
func NewSchedulerCommand((registryOptions ...Option)) (registryOptions ...Option)
```


**Тип ответа:** registryOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Option


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:90`



---


[function] name: Run file: cmd/kube-scheduler/app/server.go:171 returns_error: нет description: Run executes the scheduler based on the given configuration. It only returns on error or when context is done.


### Run (cmd/kube-scheduler/app/server.go:171)


Run executes the scheduler based on the given configuration. It only returns on error or when context is done.


```go
func Run((ctx context.Context, cc *schedulerserverconfig.CompletedConfig, sched *scheduler.Scheduler)) (ctx context.Context, cc *schedulerserverconfig.CompletedConfig, sched *scheduler.Scheduler)
```


**Тип запроса:** schedulerserverconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


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


**Тип ответа:** cc


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** schedulerserverconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sched


```json
{
  "prepareFn": {}
}
```


*Определено в:* `test/integration/scheduler_perf/options.go`


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:171`



---


[function] name: Setup file: cmd/kube-scheduler/app/server.go:416 returns_error: да description: Setup creates a completed config and a scheduler based on the command args and options


### Setup (cmd/kube-scheduler/app/server.go:416)


Setup creates a completed config and a scheduler based on the command args and options


```go
func Setup((*schedulerserverconfig.CompletedConfig, *scheduler.Scheduler, error)) (*schedulerserverconfig.CompletedConfig, *scheduler.Scheduler, error)
```


**Тип запроса:** schedulerserverconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Тип ответа:** schedulerserverconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*schedulerserverconfig.CompletedConfig`, `*scheduler.Scheduler`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:416`



---


[function] name: WithPlugin file: cmd/kube-scheduler/app/server.go:409 returns_error: нет description: WithPlugin creates an Option based on plugin name and factory. Please don't remove this function: it is used to register


### WithPlugin (cmd/kube-scheduler/app/server.go:409)


WithPlugin creates an Option based on plugin name and factory. Please don't remove this function: it is used to register out-of-tree plugins,
hence there are no references to it from the kubernetes scheduler code base.


```go
func WithPlugin((name string, factory runtime.PluginFactory)) (name string, factory runtime.PluginFactory)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** factory


```json
{
  "clientGetter": {},
  "openAPIParser": null,
  "oapi": null,
  "parser": {},
  "getter": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/util/factory_client_access.go`


**Тип ответа:** runtime.PluginFactory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:409`



---


[function] name: buildHandlerChain file: cmd/kube-scheduler/app/server.go:342 returns_error: нет description: buildHandlerChain wraps the given handler with the standard filters.


### buildHandlerChain (cmd/kube-scheduler/app/server.go:342)


buildHandlerChain wraps the given handler with the standard filters.


```go
func buildHandlerChain((handler http.Handler, authn authenticator.Request, authz authorizer.Authorizer)) (handler http.Handler, authn authenticator.Request, authz authorizer.Authorizer)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** http.Handler


```json
{
  "notify": [],
  "final": {},
  "once": {}
}
```


*Определено в:* `pkg/util/interrupt/interrupt.go`


**Тип ответа:** authn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authenticator.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** authz


```json
{
  "authorized": {},
  "reason": "string",
  "err": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/authorizer/caching_authorizer.go`


**Тип ответа:** authorizer.Authorizer


```json
{
  "subjectAccessReview": {},
  "responseCache": null,
  "authorizedTTL": {},
  "unauthorizedTTL": {},
  "retryBackoff": {},
  "decisionOnError": {},
  "metrics": {},
  "celMatcher": null,
  "name": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go`


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:342`



---


[function] name: getRecorderFactory file: cmd/kube-scheduler/app/server.go:401 returns_error: нет description: —


### getRecorderFactory (cmd/kube-scheduler/app/server.go:401)


getRecorderFactory is a function that performs operations based on the provided parameters and returns (cc *schedulerserverconfig.CompletedConfig).


```go
func getRecorderFactory((cc *schedulerserverconfig.CompletedConfig)) (cc *schedulerserverconfig.CompletedConfig)
```


**Тип запроса:** schedulerserverconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cc


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** schedulerserverconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:401`



---


[function] name: init file: cmd/kube-scheduler/app/server.go:81 returns_error: нет description: —


### init (cmd/kube-scheduler/app/server.go:81)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:81`



---


[function] name: installMetricHandler file: cmd/kube-scheduler/app/server.go:356 returns_error: нет description: —


### installMetricHandler (cmd/kube-scheduler/app/server.go:356)


installMetricHandler is a function that performs operations based on the provided parameters and returns (pathRecorderMux *mux.PathRecorderMux, informers informers.SharedInformerFactory, isLeader func() bool).


```go
func installMetricHandler((pathRecorderMux *mux.PathRecorderMux, informers informers.SharedInformerFactory, isLeader func() bool)) (pathRecorderMux *mux.PathRecorderMux, informers informers.SharedInformerFactory, isLeader func() bool)
```


**Тип запроса:** mux.PathRecorderMux


```json
{
  "name": "string",
  "lock": {},
  "notFoundHandler": {},
  "pathToHandler": {},
  "prefixToHandler": {},
  "mux": {},
  "exposedPaths": [],
  "pathStacks": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** pathRecorderMux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mux.PathRecorderMux


```json
{
  "name": "string",
  "lock": {},
  "notFoundHandler": {},
  "pathToHandler": {},
  "prefixToHandler": {},
  "mux": {},
  "exposedPaths": [],
  "pathStacks": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** informers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** informers.SharedInformerFactory


```json
{
  "client": {},
  "defaultResync": {},
  "namespace": "string",
  "lock": {},
  "informers": {},
  "startedInformers": {},
  "tweakListOptions": {},
  "wg": {},
  "shuttingDown": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/dynamicinformer/informer.go`


**Тип ответа:** isLeader


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:356`



---


[function] name: newEndpointsHandler file: cmd/kube-scheduler/app/server.go:372 returns_error: нет description: newEndpointsHandler creates an API health server from the config, and will also
embed the metrics handler and z-pages ha


### newEndpointsHandler (cmd/kube-scheduler/app/server.go:372)


newEndpointsHandler creates an API health server from the config, and will also
embed the metrics handler and z-pages handler.
TODO: healthz check is deprecated, please use livez and readyz instead. Will be removed in the future.


```go
func newEndpointsHandler((config *kubeschedulerconfig.KubeSchedulerConfiguration, informers informers.SharedInformerFactory, isLeader func() bool, healthzChecks, readyzChecks []healthz.HealthChecker, flagReader flagz.Reader)) (config *kubeschedulerconfig.KubeSchedulerConfiguration, informers informers.SharedInformerFactory, isLeader func() bool, healthzChecks, readyzChecks []healthz.HealthChecker, flagReader flagz.Reader)
```


**Тип запроса:** kubeschedulerconfig.KubeSchedulerConfiguration


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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeschedulerconfig.KubeSchedulerConfiguration


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


**Тип ответа:** informers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** informers.SharedInformerFactory


```json
{
  "client": {},
  "defaultResync": {},
  "namespace": "string",
  "lock": {},
  "informers": {},
  "startedInformers": {},
  "tweakListOptions": {},
  "wg": {},
  "shuttingDown": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/dynamicinformer/informer.go`


**Тип ответа:** isLeader


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** healthzChecks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** readyzChecks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** healthz.HealthChecker


```json
{
  "started": {}
}
```


*Определено в:* `test/images/agnhost/grpc-health-checking/grpc-health-checking.go`


**Тип ответа:** flagReader


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flagz.Reader


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


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:372`



---


[function] name: runCommand file: cmd/kube-scheduler/app/server.go:139 returns_error: нет description: runCommand runs the scheduler.


### runCommand (cmd/kube-scheduler/app/server.go:139)


runCommand runs the scheduler.


```go
func runCommand((cmd *cobra.Command, opts *options.Options, registryOptions ...Option)) (cmd *cobra.Command, opts *options.Options, registryOptions ...Option)
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


**Тип запроса:** options.Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


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


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options.Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


**Тип ответа:** registryOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Option


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `cmd/kube-scheduler/app/server.go:139`




## cmd/kube-scheduler/app/testing/testserver.go


📄 Исходный файл: `cmd/kube-scheduler/app/testing/testserver.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [StartTestServer](#starttestserver-cmdkube-schedulerapptestingtestservergo68) `:68`

- 🔗 [StartTestServerOrDie](#starttestserverordie-cmdkube-schedulerapptestingtestservergo202) `:202`

- 🔗 [createListenerOnFreePort](#createlisteneronfreeport-cmdkube-schedulerapptestingtestservergo210) `:210`

- 🔗 [init](#init-cmdkube-schedulerapptestingtestservergo43) `:43`


</details>


[function] name: StartTestServer file: cmd/kube-scheduler/app/testing/testserver.go:68 returns_error: да description: StartTestServer starts a kube-scheduler. A rest client config and a tear-down func,
and location of the tmpdir are retur


### StartTestServer (cmd/kube-scheduler/app/testing/testserver.go:68)


StartTestServer starts a kube-scheduler. A rest client config and a tear-down func,
and location of the tmpdir are returned.

Note: we return a tear-down func instead of a stop channel because the later will leak temporary

files that because Golang testing's call to os.Exit will not give a stop channel go routine
enough time to remove temporary files.


```go
func StartTestServer((result TestServer, err error)) (result TestServer, err error)
```


**Тип ответа:** result


```json
{
  "object": {},
  "err": {},
  "reason": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher.go`


**Тип ответа:** TestServer


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


*Типы возврата:* `result TestServer`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/testing/testserver.go:68`



---


[function] name: StartTestServerOrDie file: cmd/kube-scheduler/app/testing/testserver.go:202 returns_error: нет description: StartTestServerOrDie calls StartTestServer panic if it does not succeed.


### StartTestServerOrDie (cmd/kube-scheduler/app/testing/testserver.go:202)


StartTestServerOrDie calls StartTestServer panic if it does not succeed.


```go
func StartTestServerOrDie((t *testing.T, ctx context.Context, flags []string)) (t *testing.T, ctx context.Context, flags []string)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-scheduler/app/testing/testserver.go:202`



---


[function] name: createListenerOnFreePort file: cmd/kube-scheduler/app/testing/testserver.go:210 returns_error: да description: —


### createListenerOnFreePort (cmd/kube-scheduler/app/testing/testserver.go:210)


createListenerOnFreePort is a function that performs operations based on the provided parameters and may return an error.


```go
func createListenerOnFreePort((net.Listener, int, error)) (net.Listener, int, error)
```


**Тип ответа:** net.Listener


```json
{
  "logger": {},
  "nextCh": {},
  "addCh": {},
  "done": {},
  "handler": {},
  "syncTracker": null,
  "upstreamHasSynced": {},
  "pendingNotifications": {},
  "requestedResyncPeriod": {},
  "resyncPeriod": {},
  "nextResync": {},
  "resyncLock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/shared_informer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `net.Listener`, `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-scheduler/app/testing/testserver.go:210`



---


[function] name: init file: cmd/kube-scheduler/app/testing/testserver.go:43 returns_error: нет description: —


### init (cmd/kube-scheduler/app/testing/testserver.go:43)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/app/testing/testserver.go:43`




## cmd/kube-scheduler/scheduler.go


📄 Исходный файл: `cmd/kube-scheduler/scheduler.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdkube-schedulerschedulergo29) `:29`


</details>


[function] name: main file: cmd/kube-scheduler/scheduler.go:29 returns_error: нет description: —


### main (cmd/kube-scheduler/scheduler.go:29)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/kube-scheduler/scheduler.go:29`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kube-proxy.md)

- [Следующая директория](cmd_kubeadm.md)


---

