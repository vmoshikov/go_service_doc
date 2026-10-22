---
title: "Функции: cmd/kube-proxy"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/kube-proxy
---


# Функции: cmd/kube-proxy


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kube-controller-manager.md)

- [Следующая директория](cmd_kube-scheduler.md)


---


## Меню по файлам


- 📄 [cmd/kube-proxy/app/init_linux.go](#cmdkube-proxyappinit_linuxgo)

- 📄 [cmd/kube-proxy/app/init_other.go](#cmdkube-proxyappinit_othergo)

- 📄 [cmd/kube-proxy/app/init_windows.go](#cmdkube-proxyappinit_windowsgo)

- 📄 [cmd/kube-proxy/app/options.go](#cmdkube-proxyappoptionsgo)

- 📄 [cmd/kube-proxy/app/server.go](#cmdkube-proxyappservergo)

- 📄 [cmd/kube-proxy/app/server_linux.go](#cmdkube-proxyappserver_linuxgo)

- 📄 [cmd/kube-proxy/app/server_other.go](#cmdkube-proxyappserver_othergo)

- 📄 [cmd/kube-proxy/app/server_windows.go](#cmdkube-proxyappserver_windowsgo)

- 📄 [cmd/kube-proxy/proxy.go](#cmdkube-proxyproxygo)


---


## cmd/kube-proxy/app/init_linux.go


📄 Исходный файл: `cmd/kube-proxy/app/init_linux.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [addOSFlags](#addosflags-cmdkube-proxyappinit_linuxgo29) `:29`

- 🔗 [initForOS](#initforos-cmdkube-proxyappinit_linuxgo25) `:25`


</details>


[function] name: addOSFlags file: cmd/kube-proxy/app/init_linux.go:29 returns_error: нет description: —


### addOSFlags (cmd/kube-proxy/app/init_linux.go:29)


addOSFlags is a method that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func (o *Options) addOSFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-proxy/app/init_linux.go:29`



---


[function] name: initForOS file: cmd/kube-proxy/app/init_linux.go:25 returns_error: нет description: —


### initForOS (cmd/kube-proxy/app/init_linux.go:25)


initForOS is a function that performs operations based on the provided parameters and returns (service bool).


```go
func initForOS((service bool)) (service bool)
```


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


📍 *Расположение:* `cmd/kube-proxy/app/init_linux.go:25`




## cmd/kube-proxy/app/init_other.go


📄 Исходный файл: `cmd/kube-proxy/app/init_other.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [addOSFlags](#addosflags-cmdkube-proxyappinit_othergo32) `:32`

- 🔗 [initForOS](#initforos-cmdkube-proxyappinit_othergo28) `:28`


</details>


[function] name: addOSFlags file: cmd/kube-proxy/app/init_other.go:32 returns_error: нет description: —


### addOSFlags (cmd/kube-proxy/app/init_other.go:32)


addOSFlags is a method that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func (o *Options) addOSFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-proxy/app/init_other.go:32`



---


[function] name: initForOS file: cmd/kube-proxy/app/init_other.go:28 returns_error: нет description: —


### initForOS (cmd/kube-proxy/app/init_other.go:28)


initForOS is a function that performs operations based on the provided parameters and returns (windowsService bool).


```go
func initForOS((windowsService bool)) (windowsService bool)
```


**Тип ответа:** windowsService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/init_other.go:28`




## cmd/kube-proxy/app/init_windows.go


📄 Исходный файл: `cmd/kube-proxy/app/init_windows.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [addOSFlags](#addosflags-cmdkube-proxyappinit_windowsgo38) `:38`

- 🔗 [initForOS](#initforos-cmdkube-proxyappinit_windowsgo31) `:31`


</details>


[function] name: addOSFlags file: cmd/kube-proxy/app/init_windows.go:38 returns_error: нет description: —


### addOSFlags (cmd/kube-proxy/app/init_windows.go:38)


addOSFlags is a method that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func (o *Options) addOSFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-proxy/app/init_windows.go:38`



---


[function] name: initForOS file: cmd/kube-proxy/app/init_windows.go:31 returns_error: нет description: —


### initForOS (cmd/kube-proxy/app/init_windows.go:31)


initForOS is a function that performs operations based on the provided parameters and returns (windowsService bool).


```go
func initForOS((windowsService bool)) (windowsService bool)
```


**Тип ответа:** windowsService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/init_windows.go:31`




## cmd/kube-proxy/app/options.go


📄 Исходный файл: `cmd/kube-proxy/app/options.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-proxyappoptionsgo98) `:98`

- 🔗 [Complete](#complete-cmdkube-proxyappoptionsgo205) `:205`

- 🔗 [NewOptions](#newoptions-cmdkube-proxyappoptionsgo194) `:194`

- 🔗 [Run](#run-cmdkube-proxyappoptionsgo361) `:361`

- 🔗 [Validate](#validate-cmdkube-proxyappoptionsgo352) `:352`

- 🔗 [addressFromDeprecatedFlags](#addressfromdeprecatedflags-cmdkube-proxyappoptionsgo441) `:441`

- 🔗 [copyLogsFromFlags](#copylogsfromflags-cmdkube-proxyappoptionsgo263) `:263`

- 🔗 [errorHandler](#errorhandler-cmdkube-proxyappoptionsgo314) `:314`

- 🔗 [eventHandler](#eventhandler-cmdkube-proxyappoptionsgo305) `:305`

- 🔗 [initWatcher](#initwatcher-cmdkube-proxyappoptionsgo291) `:291`

- 🔗 [loadConfig](#loadconfig-cmdkube-proxyappoptionsgo474) `:474`

- 🔗 [loadConfigFromFile](#loadconfigfromfile-cmdkube-proxyappoptionsgo464) `:464`

- 🔗 [newKubeProxyConfiguration](#newkubeproxyconfiguration-cmdkube-proxyappoptionsgo182) `:182`

- 🔗 [newLenientSchemeAndCodecs](#newlenientschemeandcodecs-cmdkube-proxyappoptionsgo450) `:450`

- 🔗 [processHostnameOverrideFlag](#processhostnameoverrideflag-cmdkube-proxyappoptionsgo319) `:319`

- 🔗 [processV1Alpha1Flags](#processv1alpha1flags-cmdkube-proxyappoptionsgo333) `:333`

- 🔗 [runLoop](#runloop-cmdkube-proxyappoptionsgo388) `:388`

- 🔗 [writeConfigFile](#writeconfigfile-cmdkube-proxyappoptionsgo407) `:407`


</details>


[function] name: AddFlags file: cmd/kube-proxy/app/options.go:98 returns_error: нет description: AddFlags adds flags to fs and binds them to options.


### AddFlags (cmd/kube-proxy/app/options.go:98)


AddFlags adds flags to fs and binds them to options.


```go
func (o *Options) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-proxy/app/options.go:98`



---


[function] name: Complete file: cmd/kube-proxy/app/options.go:205 returns_error: нет description: Complete completes all the required options.


### Complete (cmd/kube-proxy/app/options.go:205)


Complete completes all the required options.


```go
func (o *Options) Complete((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-proxy/app/options.go:205`



---


[function] name: NewOptions file: cmd/kube-proxy/app/options.go:194 returns_error: нет description: NewOptions returns initialized Options


### NewOptions (cmd/kube-proxy/app/options.go:194)


NewOptions returns initialized Options


```go
func NewOptions(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/options.go:194`



---


[function] name: Run file: cmd/kube-proxy/app/options.go:361 returns_error: нет description: Run runs the specified ProxyServer.


### Run (cmd/kube-proxy/app/options.go:361)


Run runs the specified ProxyServer.


```go
func (o *Options) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-proxy/app/options.go:361`



---


[function] name: Validate file: cmd/kube-proxy/app/options.go:352 returns_error: нет description: Validate validates all the required options.


### Validate (cmd/kube-proxy/app/options.go:352)


Validate validates all the required options.


```go
func (o *Options) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/options.go:352`



---


[function] name: addressFromDeprecatedFlags file: cmd/kube-proxy/app/options.go:441 returns_error: нет description: addressFromDeprecatedFlags returns server address from flags
passed on the command line based on the following rules:
1.


### addressFromDeprecatedFlags (cmd/kube-proxy/app/options.go:441)


addressFromDeprecatedFlags returns server address from flags
passed on the command line based on the following rules:
1. If port is 0, disable the server (e.g. set address to empty).
2. Otherwise, set the port portion of the config accordingly.


```go
func addressFromDeprecatedFlags((addr string, port int32)) (addr string, port int32)
```


**Тип ответа:** addr


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** port


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/kube-proxy/app/options.go:441`



---


[function] name: copyLogsFromFlags file: cmd/kube-proxy/app/options.go:263 returns_error: нет description: copyLogsFromFlags applies the logging flags from the given flag set to the given
configuration. Fields for which the cor


### copyLogsFromFlags (cmd/kube-proxy/app/options.go:263)


copyLogsFromFlags applies the logging flags from the given flag set to the given
configuration. Fields for which the corresponding flag was not used are left
unmodified. For fields that have multiple values (like vmodule), the values from
the flags get joined so that the command line flags have priority.

TODO (pohly): move this to logsapi


```go
func copyLogsFromFlags((from *pflag.FlagSet, to *logsapi.LoggingConfiguration)) (from *pflag.FlagSet, to *logsapi.LoggingConfiguration)
```


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип запроса:** logsapi.LoggingConfiguration


```json
{
  "Format": "string",
  "FlushFrequency": "1s",
  "Verbosity": {},
  "VModule": {},
  "Options": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/types.go`


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


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** to


```json
{
  "cache": {},
  "logger": {}
}
```


*Определено в:* `pkg/controller/volume/selinuxwarning/metrics.go`


**Тип ответа:** logsapi.LoggingConfiguration


```json
{
  "Format": "string",
  "FlushFrequency": "1s",
  "Verbosity": {},
  "VModule": {},
  "Options": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/types.go`


📍 *Расположение:* `cmd/kube-proxy/app/options.go:263`



---


[function] name: errorHandler file: cmd/kube-proxy/app/options.go:314 returns_error: да description: —


### errorHandler (cmd/kube-proxy/app/options.go:314)


errorHandler is a method that performs operations based on the provided parameters and may return an error.


```go
func (o *Options) errorHandler((err error)) (err error)
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


📍 *Расположение:* `cmd/kube-proxy/app/options.go:314`



---


[function] name: eventHandler file: cmd/kube-proxy/app/options.go:305 returns_error: нет description: —


### eventHandler (cmd/kube-proxy/app/options.go:305)


eventHandler is a method that performs operations based on the provided parameters and returns (ent fsnotify.Event).


```go
func (o *Options) eventHandler((ent fsnotify.Event)) (ent fsnotify.Event)
```


**Тип ответа:** ent


```json
{
  "Name": "string",
  "CurrentVersion": "string",
  "NewVersion": "string",
  "NodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/output/v1alpha3/types.go`


**Тип ответа:** fsnotify.Event


```json
{
  "InvolvedObject": {},
  "Reason": "string",
  "Message": "string",
  "Source": {},
  "FirstTimestamp": {},
  "LastTimestamp": {},
  "Count": 0,
  "Type": "string",
  "EventTime": {},
  "Series": null,
  "Action": "string",
  "Related": null,
  "ReportingController": "string",
  "ReportingInstance": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `cmd/kube-proxy/app/options.go:305`



---


[function] name: initWatcher file: cmd/kube-proxy/app/options.go:291 returns_error: нет description: Creates a new filesystem watcher and adds watches for the config file.


### initWatcher (cmd/kube-proxy/app/options.go:291)


Creates a new filesystem watcher and adds watches for the config file.


```go
func (o *Options) initWatcher(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/options.go:291`



---


[function] name: loadConfig file: cmd/kube-proxy/app/options.go:474 returns_error: да description: loadConfig decodes a serialized KubeProxyConfiguration to the internal type.


### loadConfig (cmd/kube-proxy/app/options.go:474)


loadConfig decodes a serialized KubeProxyConfiguration to the internal type.


```go
func (o *Options) loadConfig((*kubeproxyconfig.KubeProxyConfiguration, error)) (*kubeproxyconfig.KubeProxyConfiguration, error)
```


**Тип запроса:** kubeproxyconfig.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** kubeproxyconfig.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeproxyconfig.KubeProxyConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/options.go:474`



---


[function] name: loadConfigFromFile file: cmd/kube-proxy/app/options.go:464 returns_error: да description: loadConfigFromFile loads the contents of file and decodes it as a
KubeProxyConfiguration object.


### loadConfigFromFile (cmd/kube-proxy/app/options.go:464)


loadConfigFromFile loads the contents of file and decodes it as a
KubeProxyConfiguration object.


```go
func (o *Options) loadConfigFromFile((*kubeproxyconfig.KubeProxyConfiguration, error)) (*kubeproxyconfig.KubeProxyConfiguration, error)
```


**Тип запроса:** kubeproxyconfig.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** kubeproxyconfig.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeproxyconfig.KubeProxyConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/options.go:464`



---


[function] name: newKubeProxyConfiguration file: cmd/kube-proxy/app/options.go:182 returns_error: нет description: newKubeProxyConfiguration returns a KubeProxyConfiguration with default values


### newKubeProxyConfiguration (cmd/kube-proxy/app/options.go:182)


newKubeProxyConfiguration returns a KubeProxyConfiguration with default values


```go
func newKubeProxyConfiguration(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/options.go:182`



---


[function] name: newLenientSchemeAndCodecs file: cmd/kube-proxy/app/options.go:450 returns_error: да description: newLenientSchemeAndCodecs returns a scheme that has only v1alpha1 registered into
it and a CodecFactory with strict deco


### newLenientSchemeAndCodecs (cmd/kube-proxy/app/options.go:450)


newLenientSchemeAndCodecs returns a scheme that has only v1alpha1 registered into
it and a CodecFactory with strict decoding disabled.


```go
func newLenientSchemeAndCodecs((*runtime.Scheme, *serializer.CodecFactory, error)) (*runtime.Scheme, *serializer.CodecFactory, error)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип запроса:** serializer.CodecFactory


```json
{
  "scheme": null,
  "universal": {},
  "accepts": [],
  "legacySerializer": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/codec_factory.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** serializer.CodecFactory


```json
{
  "scheme": null,
  "universal": {},
  "accepts": [],
  "legacySerializer": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/codec_factory.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtime.Scheme`, `*serializer.CodecFactory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/options.go:450`



---


[function] name: processHostnameOverrideFlag file: cmd/kube-proxy/app/options.go:319 returns_error: нет description: processHostnameOverrideFlag processes hostname-override flag


### processHostnameOverrideFlag (cmd/kube-proxy/app/options.go:319)


processHostnameOverrideFlag processes hostname-override flag


```go
func (o *Options) processHostnameOverrideFlag(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/options.go:319`



---


[function] name: processV1Alpha1Flags file: cmd/kube-proxy/app/options.go:333 returns_error: нет description: processV1Alpha1Flags processes v1alpha1 flags which can't be directly mapped to internal config.


### processV1Alpha1Flags (cmd/kube-proxy/app/options.go:333)


processV1Alpha1Flags processes v1alpha1 flags which can't be directly mapped to internal config.


```go
func (o *Options) processV1Alpha1Flags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-proxy/app/options.go:333`



---


[function] name: runLoop file: cmd/kube-proxy/app/options.go:388 returns_error: нет description: runLoop will watch on the update change of the proxy server's configuration file.
Return an error when updated


### runLoop (cmd/kube-proxy/app/options.go:388)


runLoop will watch on the update change of the proxy server's configuration file.
Return an error when updated


```go
func (o *Options) runLoop((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-proxy/app/options.go:388`



---


[function] name: writeConfigFile file: cmd/kube-proxy/app/options.go:407 returns_error: да description: —


### writeConfigFile (cmd/kube-proxy/app/options.go:407)


writeConfigFile is a method that performs operations based on the provided parameters and may return an error.


```go
func (o *Options) writeConfigFile((err error)) (err error)
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


📍 *Расположение:* `cmd/kube-proxy/app/options.go:407`




## cmd/kube-proxy/app/server.go


📄 Исходный файл: `cmd/kube-proxy/app/server.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [NewProxyCommand](#newproxycommand-cmdkube-proxyappservergo98) `:98`

- 🔗 [Run](#run-cmdkube-proxyappservergo526) `:526`

- 🔗 [badBindAddress](#badbindaddress-cmdkube-proxyappservergo392) `:392`

- 🔗 [badCIDRs](#badcidrs-cmdkube-proxyappservergo378) `:378`

- 🔗 [birthCry](#birthcry-cmdkube-proxyappservergo638) `:638`

- 🔗 [checkBadConfig](#checkbadconfig-cmdkube-proxyappservergo286) `:286`

- 🔗 [checkBadIPConfig](#checkbadipconfig-cmdkube-proxyappservergo319) `:319`

- 🔗 [createClient](#createclient-cmdkube-proxyappservergo404) `:404`

- 🔗 [detectNodeIPs](#detectnodeips-cmdkube-proxyappservergo655) `:655`

- 🔗 [init](#init-cmdkube-proxyappservergo87) `:87`

- 🔗 [newProxyServer](#newproxyserver-cmdkube-proxyappservergo181) `:181`

- 🔗 [serveHealthz](#servehealthz-cmdkube-proxyappservergo436) `:436`

- 🔗 [serveMetrics](#servemetrics-cmdkube-proxyappservergo459) `:459`


</details>


[function] name: NewProxyCommand file: cmd/kube-proxy/app/server.go:98 returns_error: нет description: NewProxyCommand creates a *cobra.Command object with default parameters


### NewProxyCommand (cmd/kube-proxy/app/server.go:98)


NewProxyCommand creates a *cobra.Command object with default parameters


```go
func NewProxyCommand(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/server.go:98`



---


[function] name: Run file: cmd/kube-proxy/app/server.go:526 returns_error: нет description: Run runs the specified ProxyServer.  This should never exit (unless CleanupAndExit is set).
TODO: At the moment, Run() c


### Run (cmd/kube-proxy/app/server.go:526)


Run runs the specified ProxyServer.  This should never exit (unless CleanupAndExit is set).
TODO: At the moment, Run() cannot return a nil error, otherwise it's caller will never exit. Update callers of Run to handle nil errors.


```go
func (s *ProxyServer) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-proxy/app/server.go:526`



---


[function] name: badBindAddress file: cmd/kube-proxy/app/server.go:392 returns_error: нет description: badBindAddress returns true if bindAddress is an "IP:port" string where IP is a
non-zero IP of wrongFamily.


### badBindAddress (cmd/kube-proxy/app/server.go:392)


badBindAddress returns true if bindAddress is an "IP:port" string where IP is a
non-zero IP of wrongFamily.


```go
func badBindAddress((bindAddress string, wrongFamily netutils.IPFamily)) (bindAddress string, wrongFamily netutils.IPFamily)
```


**Тип ответа:** bindAddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** wrongFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** netutils.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/server.go:392`



---


[function] name: badCIDRs file: cmd/kube-proxy/app/server.go:378 returns_error: нет description: badCIDRs returns true if cidrs is a non-empty list of CIDRs, all of wrongFamily.


### badCIDRs (cmd/kube-proxy/app/server.go:378)


badCIDRs returns true if cidrs is a non-empty list of CIDRs, all of wrongFamily.


```go
func badCIDRs((cidrs []string, wrongFamily netutils.IPFamily)) (cidrs []string, wrongFamily netutils.IPFamily)
```


**Тип ответа:** cidrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** wrongFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** netutils.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/server.go:378`



---


[function] name: birthCry file: cmd/kube-proxy/app/server.go:638 returns_error: нет description: —


### birthCry (cmd/kube-proxy/app/server.go:638)


birthCry is a method that performs operations based on the provided parameters and returns ().


```go
func (s *ProxyServer) birthCry(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/server.go:638`



---


[function] name: checkBadConfig file: cmd/kube-proxy/app/server.go:286 returns_error: нет description: checkBadConfig checks for bad/deprecated configuation


### checkBadConfig (cmd/kube-proxy/app/server.go:286)


checkBadConfig checks for bad/deprecated configuation


```go
func checkBadConfig((s *ProxyServer)) (s *ProxyServer)
```


**Тип запроса:** ProxyServer


```json
{
  "Config": null,
  "Client": {},
  "Broadcaster": {},
  "Recorder": {},
  "NodeRef": null,
  "HealthzServer": null,
  "NodeName": "string",
  "PrimaryIPFamily": {},
  "NodeIPs": {},
  "flagz": {},
  "podCIDRs": [],
  "NodeManager": null,
  "Proxier": {}
}
```


*Определено в:* `cmd/kube-proxy/app/server.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** ProxyServer


```json
{
  "Config": null,
  "Client": {},
  "Broadcaster": {},
  "Recorder": {},
  "NodeRef": null,
  "HealthzServer": null,
  "NodeName": "string",
  "PrimaryIPFamily": {},
  "NodeIPs": {},
  "flagz": {},
  "podCIDRs": [],
  "NodeManager": null,
  "Proxier": {}
}
```


*Определено в:* `cmd/kube-proxy/app/server.go`


📍 *Расположение:* `cmd/kube-proxy/app/server.go:286`



---


[function] name: checkBadIPConfig file: cmd/kube-proxy/app/server.go:319 returns_error: да description: checkBadIPConfig checks for bad configuration relative to s.PrimaryIPFamily.
Historically, we did not check most of the 


### checkBadIPConfig (cmd/kube-proxy/app/server.go:319)


checkBadIPConfig checks for bad configuration relative to s.PrimaryIPFamily.
Historically, we did not check most of the config options, so we cannot retroactively
make IP family mismatches in those options be fatal. When we add new options to check
here, we should make problems with those options be fatal.


```go
func checkBadIPConfig((err error, fatal bool)) (err error, fatal bool)
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


**Тип ответа:** fatal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`, `fatal bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server.go:319`



---


[function] name: createClient file: cmd/kube-proxy/app/server.go:404 returns_error: да description: createClient creates a kube client from the given config and masterOverride.
TODO remove masterOverride when CLI flags a


### createClient (cmd/kube-proxy/app/server.go:404)


createClient creates a kube client from the given config and masterOverride.
TODO remove masterOverride when CLI flags are removed.


```go
func createClient((clientset.Interface, error)) (clientset.Interface, error)
```


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `clientset.Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server.go:404`



---


[function] name: detectNodeIPs file: cmd/kube-proxy/app/server.go:655 returns_error: нет description: (Note that on Linux, the node IPs are used only to determine whether a given
LoadBalancerSourceRanges value matches the 


### detectNodeIPs (cmd/kube-proxy/app/server.go:655)


(Note that on Linux, the node IPs are used only to determine whether a given
LoadBalancerSourceRanges value matches the node or not. In particular, they are *not*
used for NodePort handling.)

The order of precedence is:
1. if bindAddress is not 0.0.0.0 or ::, then it is used as the primary IP.
2. if rawNodeIPs is not empty, then its address(es) is/are used
3. otherwise the node IPs are 127.0.0.1 and ::1


```go
func detectNodeIPs((v1.IPFamily, map[v1.IPFamily]net.IP)) (v1.IPFamily, map[v1.IPFamily]net.IP)
```


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `cmd/kube-proxy/app/server.go:655`



---


[function] name: init file: cmd/kube-proxy/app/server.go:87 returns_error: нет description: —


### init (cmd/kube-proxy/app/server.go:87)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/app/server.go:87`



---


[function] name: newProxyServer file: cmd/kube-proxy/app/server.go:181 returns_error: да description: newProxyServer creates a ProxyServer based on the given config


### newProxyServer (cmd/kube-proxy/app/server.go:181)


newProxyServer creates a ProxyServer based on the given config


```go
func newProxyServer((*ProxyServer, error)) (*ProxyServer, error)
```


**Тип запроса:** ProxyServer


```json
{
  "Config": null,
  "Client": {},
  "Broadcaster": {},
  "Recorder": {},
  "NodeRef": null,
  "HealthzServer": null,
  "NodeName": "string",
  "PrimaryIPFamily": {},
  "NodeIPs": {},
  "flagz": {},
  "podCIDRs": [],
  "NodeManager": null,
  "Proxier": {}
}
```


*Определено в:* `cmd/kube-proxy/app/server.go`


**Тип ответа:** ProxyServer


```json
{
  "Config": null,
  "Client": {},
  "Broadcaster": {},
  "Recorder": {},
  "NodeRef": null,
  "HealthzServer": null,
  "NodeName": "string",
  "PrimaryIPFamily": {},
  "NodeIPs": {},
  "flagz": {},
  "podCIDRs": [],
  "NodeManager": null,
  "Proxier": {}
}
```


*Определено в:* `cmd/kube-proxy/app/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ProxyServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server.go:181`



---


[function] name: serveHealthz file: cmd/kube-proxy/app/server.go:436 returns_error: да description: —


### serveHealthz (cmd/kube-proxy/app/server.go:436)


serveHealthz is a function that performs operations based on the provided parameters and may return an error.


```go
func serveHealthz((ctx context.Context, hz *healthcheck.ProxyHealthServer, errCh chan error)) (ctx context.Context, hz *healthcheck.ProxyHealthServer, errCh chan error)
```


**Тип запроса:** healthcheck.ProxyHealthServer


```json
{
  "listener": {},
  "httpFactory": {},
  "clock": {},
  "nodeManager": {},
  "addr": "string",
  "healthTimeout": {},
  "lock": {},
  "lastUpdatedMap": {},
  "oldestPendingQueuedMap": {}
}
```


*Определено в:* `pkg/proxy/healthcheck/proxy_health.go`


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


**Тип ответа:** hz


```json
{
  "pointerLock": {},
  "le": null,
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/leaderelection/healthzadaptor.go`


**Тип ответа:** healthcheck.ProxyHealthServer


```json
{
  "listener": {},
  "httpFactory": {},
  "clock": {},
  "nodeManager": {},
  "addr": "string",
  "healthTimeout": {},
  "lock": {},
  "lastUpdatedMap": {},
  "oldestPendingQueuedMap": {}
}
```


*Определено в:* `pkg/proxy/healthcheck/proxy_health.go`


**Тип ответа:** errCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `hz *healthcheck.ProxyHealthServer`, `errCh chan error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server.go:436`



---


[function] name: serveMetrics file: cmd/kube-proxy/app/server.go:459 returns_error: да description: —


### serveMetrics (cmd/kube-proxy/app/server.go:459)


serveMetrics is a function that performs operations based on the provided parameters and may return an error.


```go
func serveMetrics((ctx context.Context, bindAddress string, proxyMode kubeproxyconfig.ProxyMode, enableProfiling bool, flagzReader flagz.Reader, errCh chan error)) (ctx context.Context, bindAddress string, proxyMode kubeproxyconfig.ProxyMode, enableProfiling bool, flagzReader flagz.Reader, errCh chan error)
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


**Тип ответа:** bindAddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeproxyconfig.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** enableProfiling


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flagzReader


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


**Тип ответа:** errCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `bindAddress string`, `proxyMode kubeproxyconfig.ProxyMode`, `enableProfiling bool`, `flagzReader flagz.Reader`, `errCh chan error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server.go:459`




## cmd/kube-proxy/app/server_linux.go


📄 Исходный файл: `cmd/kube-proxy/app/server_linux.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [createProxier](#createproxier-cmdkube-proxyappserver_linuxgo121) `:121`

- 🔗 [getLocalDetectors](#getlocaldetectors-cmdkube-proxyappserver_linuxgo292) `:292`

- 🔗 [isIPTablesBased](#isiptablesbased-cmdkube-proxyappserver_linuxgo75) `:75`

- 🔗 [platformApplyDefaults](#platformapplydefaults-cmdkube-proxyappserver_linuxgo46) `:46`

- 🔗 [platformCheckSupported](#platformchecksupported-cmdkube-proxyappserver_linuxgo81) `:81`

- 🔗 [platformCleanup](#platformcleanup-cmdkube-proxyappserver_linuxgo336) `:336`

- 🔗 [platformSetup](#platformsetup-cmdkube-proxyappserver_linuxgo66) `:66`


</details>


[function] name: createProxier file: cmd/kube-proxy/app/server_linux.go:121 returns_error: да description: createProxier creates the proxy.Provider


### createProxier (cmd/kube-proxy/app/server_linux.go:121)


createProxier creates the proxy.Provider


```go
func (s *ProxyServer) createProxier((proxy.Provider, error)) (proxy.Provider, error)
```


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy.Provider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server_linux.go:121`



---


[function] name: getLocalDetectors file: cmd/kube-proxy/app/server_linux.go:292 returns_error: нет description: —


### getLocalDetectors (cmd/kube-proxy/app/server_linux.go:292)


getLocalDetectors is a function that performs operations based on the provided parameters and returns (logger klog.Logger, primaryIPFamily v1.IPFamily, config *proxyconfigapi.KubeProxyConfiguration, nodePodCIDRs []string).


```go
func getLocalDetectors((logger klog.Logger, primaryIPFamily v1.IPFamily, config *proxyconfigapi.KubeProxyConfiguration, nodePodCIDRs []string)) (logger klog.Logger, primaryIPFamily v1.IPFamily, config *proxyconfigapi.KubeProxyConfiguration, nodePodCIDRs []string)
```


**Тип запроса:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** primaryIPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** nodePodCIDRs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/server_linux.go:292`



---


[function] name: isIPTablesBased file: cmd/kube-proxy/app/server_linux.go:75 returns_error: нет description: isIPTablesBased checks whether mode is based on iptables rather than nftables


### isIPTablesBased (cmd/kube-proxy/app/server_linux.go:75)


isIPTablesBased checks whether mode is based on iptables rather than nftables


```go
func isIPTablesBased((mode proxyconfigapi.ProxyMode)) (mode proxyconfigapi.ProxyMode)
```


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** proxyconfigapi.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/server_linux.go:75`



---


[function] name: platformApplyDefaults file: cmd/kube-proxy/app/server_linux.go:46 returns_error: нет description: platformApplyDefaults is called after parsing command-line flags and/or reading the
config file, to apply platform-speci


### platformApplyDefaults (cmd/kube-proxy/app/server_linux.go:46)


platformApplyDefaults is called after parsing command-line flags and/or reading the
config file, to apply platform-specific default values to config.


```go
func (o *Options) platformApplyDefaults((config *proxyconfigapi.KubeProxyConfiguration)) (config *proxyconfigapi.KubeProxyConfiguration)
```


**Тип запроса:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `cmd/kube-proxy/app/server_linux.go:46`



---


[function] name: platformCheckSupported file: cmd/kube-proxy/app/server_linux.go:81 returns_error: да description: platformCheckSupported is called immediately before creating the Proxier, to check
what IP families are supported (and w


### platformCheckSupported (cmd/kube-proxy/app/server_linux.go:81)


platformCheckSupported is called immediately before creating the Proxier, to check
what IP families are supported (and whether the configuration is usable at all).


```go
func (s *ProxyServer) platformCheckSupported((ipv4Supported, ipv6Supported, dualStackSupported bool, err error)) (ipv4Supported, ipv6Supported, dualStackSupported bool, err error)
```


**Тип ответа:** ipv4Supported


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ipv6Supported


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dualStackSupported


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


*Типы возврата:* `ipv4Supported`, `ipv6Supported`, `dualStackSupported bool`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server_linux.go:81`



---


[function] name: platformCleanup file: cmd/kube-proxy/app/server_linux.go:336 returns_error: нет description: platformCleanup removes stale kube-proxy rules that can be safely removed. If
cleanupAndExit is true, it will attempt to


### platformCleanup (cmd/kube-proxy/app/server_linux.go:336)


platformCleanup removes stale kube-proxy rules that can be safely removed. If
cleanupAndExit is true, it will attempt to remove rules from all known kube-proxy
modes. If it is false, it will only remove rules that are definitely not in use by the
currently-configured mode.


```go
func platformCleanup((ctx context.Context, mode proxyconfigapi.ProxyMode, cleanupAndExit bool)) (ctx context.Context, mode proxyconfigapi.ProxyMode, cleanupAndExit bool)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** proxyconfigapi.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cleanupAndExit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/server_linux.go:336`



---


[function] name: platformSetup file: cmd/kube-proxy/app/server_linux.go:66 returns_error: нет description: platformSetup is called after setting up the ProxyServer, but before creating the
Proxier. It should fill in any platfor


### platformSetup (cmd/kube-proxy/app/server_linux.go:66)


platformSetup is called after setting up the ProxyServer, but before creating the
Proxier. It should fill in any platform-specific fields and perform other
platform-specific setup.


```go
func (s *ProxyServer) platformSetup((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-proxy/app/server_linux.go:66`




## cmd/kube-proxy/app/server_other.go


📄 Исходный файл: `cmd/kube-proxy/app/server_other.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [createProxier](#createproxier-cmdkube-proxyappserver_othergo53) `:53`

- 🔗 [platformApplyDefaults](#platformapplydefaults-cmdkube-proxyappserver_othergo34) `:34`

- 🔗 [platformCheckSupported](#platformchecksupported-cmdkube-proxyappserver_othergo48) `:48`

- 🔗 [platformCleanup](#platformcleanup-cmdkube-proxyappserver_othergo58) `:58`

- 🔗 [platformSetup](#platformsetup-cmdkube-proxyappserver_othergo42) `:42`


</details>


[function] name: createProxier file: cmd/kube-proxy/app/server_other.go:53 returns_error: да description: createProxier creates the proxy.Provider


### createProxier (cmd/kube-proxy/app/server_other.go:53)


createProxier creates the proxy.Provider


```go
func (s *ProxyServer) createProxier((proxy.Provider, error)) (proxy.Provider, error)
```


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy.Provider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server_other.go:53`



---


[function] name: platformApplyDefaults file: cmd/kube-proxy/app/server_other.go:34 returns_error: нет description: platformApplyDefaults is called after parsing command-line flags and/or reading the
config file, to apply platform-speci


### platformApplyDefaults (cmd/kube-proxy/app/server_other.go:34)


platformApplyDefaults is called after parsing command-line flags and/or reading the
config file, to apply platform-specific default values to config.


```go
func (o *Options) platformApplyDefaults((config *proxyconfigapi.KubeProxyConfiguration)) (config *proxyconfigapi.KubeProxyConfiguration)
```


**Тип запроса:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `cmd/kube-proxy/app/server_other.go:34`



---


[function] name: platformCheckSupported file: cmd/kube-proxy/app/server_other.go:48 returns_error: да description: platformCheckSupported is called immediately before creating the Proxier, to check
what IP families are supported (and w


### platformCheckSupported (cmd/kube-proxy/app/server_other.go:48)


platformCheckSupported is called immediately before creating the Proxier, to check
what IP families are supported (and whether the configuration is usable at all).


```go
func (s *ProxyServer) platformCheckSupported((ipv4Supported, ipv6Supported, dualStackSupported bool, err error)) (ipv4Supported, ipv6Supported, dualStackSupported bool, err error)
```


**Тип ответа:** ipv4Supported


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ipv6Supported


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dualStackSupported


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


*Типы возврата:* `ipv4Supported`, `ipv6Supported`, `dualStackSupported bool`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server_other.go:48`



---


[function] name: platformCleanup file: cmd/kube-proxy/app/server_other.go:58 returns_error: нет description: platformCleanup removes stale kube-proxy rules that can be safely removed.


### platformCleanup (cmd/kube-proxy/app/server_other.go:58)


platformCleanup removes stale kube-proxy rules that can be safely removed.


```go
func platformCleanup((ctx context.Context, mode proxyconfigapi.ProxyMode, cleanupAndExit bool)) (ctx context.Context, mode proxyconfigapi.ProxyMode, cleanupAndExit bool)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** proxyconfigapi.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cleanupAndExit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/server_other.go:58`



---


[function] name: platformSetup file: cmd/kube-proxy/app/server_other.go:42 returns_error: нет description: platformSetup is called after setting up the ProxyServer, but before creating the
Proxier. It should fill in any platfor


### platformSetup (cmd/kube-proxy/app/server_other.go:42)


platformSetup is called after setting up the ProxyServer, but before creating the
Proxier. It should fill in any platform-specific fields and perform other
platform-specific setup.


```go
func (s *ProxyServer) platformSetup((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-proxy/app/server_other.go:42`




## cmd/kube-proxy/app/server_windows.go


📄 Исходный файл: `cmd/kube-proxy/app/server_windows.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [createProxier](#createproxier-cmdkube-proxyappserver_windowsgo83) `:83`

- 🔗 [platformApplyDefaults](#platformapplydefaults-cmdkube-proxyappserver_windowsgo40) `:40`

- 🔗 [platformCheckSupported](#platformchecksupported-cmdkube-proxyappserver_windowsgo64) `:64`

- 🔗 [platformCleanup](#platformcleanup-cmdkube-proxyappserver_windowsgo123) `:123`

- 🔗 [platformSetup](#platformsetup-cmdkube-proxyappserver_windowsgo52) `:52`


</details>


[function] name: createProxier file: cmd/kube-proxy/app/server_windows.go:83 returns_error: да description: createProxier creates the proxy.Provider


### createProxier (cmd/kube-proxy/app/server_windows.go:83)


createProxier creates the proxy.Provider


```go
func (s *ProxyServer) createProxier((proxy.Provider, error)) (proxy.Provider, error)
```


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy.Provider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server_windows.go:83`



---


[function] name: platformApplyDefaults file: cmd/kube-proxy/app/server_windows.go:40 returns_error: нет description: platformApplyDefaults is called after parsing command-line flags and/or reading the
config file, to apply platform-speci


### platformApplyDefaults (cmd/kube-proxy/app/server_windows.go:40)


platformApplyDefaults is called after parsing command-line flags and/or reading the
config file, to apply platform-specific default values to config.


```go
func (o *Options) platformApplyDefaults((config *proxyconfigapi.KubeProxyConfiguration)) (config *proxyconfigapi.KubeProxyConfiguration)
```


**Тип запроса:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** proxyconfigapi.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `cmd/kube-proxy/app/server_windows.go:40`



---


[function] name: platformCheckSupported file: cmd/kube-proxy/app/server_windows.go:64 returns_error: да description: platformCheckSupported is called immediately before creating the Proxier, to check
what IP families are supported (and w


### platformCheckSupported (cmd/kube-proxy/app/server_windows.go:64)


platformCheckSupported is called immediately before creating the Proxier, to check
what IP families are supported (and whether the configuration is usable at all).


```go
func (s *ProxyServer) platformCheckSupported((ipv4Supported, ipv6Supported, dualStackSupported bool, err error)) (ipv4Supported, ipv6Supported, dualStackSupported bool, err error)
```


**Тип ответа:** ipv4Supported


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ipv6Supported


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dualStackSupported


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


*Типы возврата:* `ipv4Supported`, `ipv6Supported`, `dualStackSupported bool`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-proxy/app/server_windows.go:64`



---


[function] name: platformCleanup file: cmd/kube-proxy/app/server_windows.go:123 returns_error: нет description: platformCleanup removes stale kube-proxy rules that can be safely removed.


### platformCleanup (cmd/kube-proxy/app/server_windows.go:123)


platformCleanup removes stale kube-proxy rules that can be safely removed.


```go
func platformCleanup((ctx context.Context, mode proxyconfigapi.ProxyMode, cleanupAndExit bool)) (ctx context.Context, mode proxyconfigapi.ProxyMode, cleanupAndExit bool)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** proxyconfigapi.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cleanupAndExit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-proxy/app/server_windows.go:123`



---


[function] name: platformSetup file: cmd/kube-proxy/app/server_windows.go:52 returns_error: нет description: platformSetup is called after setting up the ProxyServer, but before creating the
Proxier. It should fill in any platfor


### platformSetup (cmd/kube-proxy/app/server_windows.go:52)


platformSetup is called after setting up the ProxyServer, but before creating the
Proxier. It should fill in any platform-specific fields and perform other
platform-specific setup.


```go
func (s *ProxyServer) platformSetup((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-proxy/app/server_windows.go:52`




## cmd/kube-proxy/proxy.go


📄 Исходный файл: `cmd/kube-proxy/proxy.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdkube-proxyproxygo29) `:29`


</details>


[function] name: main file: cmd/kube-proxy/proxy.go:29 returns_error: нет description: —


### main (cmd/kube-proxy/proxy.go:29)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/kube-proxy/proxy.go:29`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kube-controller-manager.md)

- [Следующая директория](cmd_kube-scheduler.md)


---

