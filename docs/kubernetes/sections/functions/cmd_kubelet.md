---
title: "Функции: cmd/kubelet"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/kubelet
---


# Функции: cmd/kubelet


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kubectl-convert.md)

- [Следующая директория](cmd_kubemark.md)


---


## Меню по файлам


- 📄 [cmd/kubelet/app/auth.go](#cmdkubeletappauthgo)

- 📄 [cmd/kubelet/app/init_others.go](#cmdkubeletappinit_othersgo)

- 📄 [cmd/kubelet/app/init_windows.go](#cmdkubeletappinit_windowsgo)

- 📄 [cmd/kubelet/app/options/globalflags.go](#cmdkubeletappoptionsglobalflagsgo)

- 📄 [cmd/kubelet/app/options/globalflags_linux.go](#cmdkubeletappoptionsglobalflags_linuxgo)

- 📄 [cmd/kubelet/app/options/globalflags_other.go](#cmdkubeletappoptionsglobalflags_othergo)

- 📄 [cmd/kubelet/app/options/options.go](#cmdkubeletappoptionsoptionsgo)

- 📄 [cmd/kubelet/app/options/osflags_others.go](#cmdkubeletappoptionsosflags_othersgo)

- 📄 [cmd/kubelet/app/options/osflags_windows.go](#cmdkubeletappoptionsosflags_windowsgo)

- 📄 [cmd/kubelet/app/plugins.go](#cmdkubeletapppluginsgo)

- 📄 [cmd/kubelet/app/server.go](#cmdkubeletappservergo)

- 📄 [cmd/kubelet/app/server_linux.go](#cmdkubeletappserver_linuxgo)

- 📄 [cmd/kubelet/app/server_others.go](#cmdkubeletappserver_othersgo)

- 📄 [cmd/kubelet/app/server_unsupported.go](#cmdkubeletappserver_unsupportedgo)

- 📄 [cmd/kubelet/app/server_windows.go](#cmdkubeletappserver_windowsgo)

- 📄 [cmd/kubelet/kubelet.go](#cmdkubeletkubeletgo)


---


## cmd/kubelet/app/auth.go


📄 Исходный файл: `cmd/kubelet/app/auth.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [BuildAuth](#buildauth-cmdkubeletappauthgo43) `:43`

- 🔗 [BuildAuthn](#buildauthn-cmdkubeletappauthgo70) `:70`

- 🔗 [BuildAuthz](#buildauthz-cmdkubeletappauthgo117) `:117`


</details>


[function] name: BuildAuth file: cmd/kubelet/app/auth.go:43 returns_error: да description: BuildAuth creates an authenticator, an authorizer, and a matching authorizer attributes getter compatible with the kubel


### BuildAuth (cmd/kubelet/app/auth.go:43)


BuildAuth creates an authenticator, an authorizer, and a matching authorizer attributes getter compatible with the kubelet's needs
It returns AuthInterface, a run method to start internal controllers (like cert reloading) and error.


```go
func BuildAuth((server.AuthInterface, func(<-chan struct{}), error)) (server.AuthInterface, func(<-chan struct{}), error)
```


**Тип ответа:** server.AuthInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `server.AuthInterface`, `func(<-chan struct{})`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/auth.go:43`



---


[function] name: BuildAuthn file: cmd/kubelet/app/auth.go:70 returns_error: да description: BuildAuthn creates an authenticator compatible with the kubelet's needs


### BuildAuthn (cmd/kubelet/app/auth.go:70)


BuildAuthn creates an authenticator compatible with the kubelet's needs


```go
func BuildAuthn((authenticator.Request, func(<-chan struct{}), error)) (authenticator.Request, func(<-chan struct{}), error)
```


**Тип ответа:** authenticator.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** func


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authenticator.Request`, `func(<-chan struct{})`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/auth.go:70`



---


[function] name: BuildAuthz file: cmd/kubelet/app/auth.go:117 returns_error: да description: BuildAuthz creates an authorizer compatible with the kubelet's needs


### BuildAuthz (cmd/kubelet/app/auth.go:117)


BuildAuthz creates an authorizer compatible with the kubelet's needs


```go
func BuildAuthz((authorizer.Authorizer, error)) (authorizer.Authorizer, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authorizer.Authorizer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/auth.go:117`




## cmd/kubelet/app/init_others.go


📄 Исходный файл: `cmd/kubelet/app/init_others.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [initForOS](#initforos-cmdkubeletappinit_othersgo23) `:23`


</details>


[function] name: initForOS file: cmd/kubelet/app/init_others.go:23 returns_error: нет description: —


### initForOS (cmd/kubelet/app/init_others.go:23)


initForOS is a function that performs operations based on the provided parameters and returns (ctx context.Context, service bool, priorityClass string).


```go
func initForOS((ctx context.Context, service bool, priorityClass string)) (ctx context.Context, service bool, priorityClass string)
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


**Тип ответа:** priorityClass


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/scheduling/v1alpha1/priorityclass.go`


📍 *Расположение:* `cmd/kubelet/app/init_others.go:23`




## cmd/kubelet/app/init_windows.go


📄 Исходный файл: `cmd/kubelet/app/init_windows.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [createWindowsJobObject](#createwindowsjobobject-cmdkubeletappinit_windowsgo57) `:57`

- 🔗 [getPriorityValue](#getpriorityvalue-cmdkubeletappinit_windowsgo38) `:38`

- 🔗 [initForOS](#initforos-cmdkubeletappinit_windowsgo76) `:76`


</details>


[function] name: createWindowsJobObject file: cmd/kubelet/app/init_windows.go:57 returns_error: да description: createWindowsJobObject creates a new Job Object
(https://docs.microsoft.com/en-us/windows/win32/procthread/job-objects),


### createWindowsJobObject (cmd/kubelet/app/init_windows.go:57)


createWindowsJobObject creates a new Job Object
(https://docs.microsoft.com/en-us/windows/win32/procthread/job-objects),
and specifies the priority class for the job object to the specified value.
A job object is used here so that any spawned processes such as powershell or
wmic are created at the specified thread priority class.
Running kubelet with above normal / high priority  can help improve
responsiveness on machines with high CPU utilization.


```go
func createWindowsJobObject((windows.Handle, error)) (windows.Handle, error)
```


**Тип ответа:** windows.Handle


```json
{
  "Name": "string",
  "LongName": "string",
  "FileName": "string",
  "CAName": "string",
  "CABaseName": "string",
  "readwriter": {},
  "certConfigMutators": []
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `windows.Handle`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/init_windows.go:57`



---


[function] name: getPriorityValue file: cmd/kubelet/app/init_windows.go:38 returns_error: нет description: getPriorityValue returns the value associated with a Windows process priorityClass
Ref: https://docs.microsoft.com/en-us


### getPriorityValue (cmd/kubelet/app/init_windows.go:38)


getPriorityValue returns the value associated with a Windows process priorityClass
Ref: https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/setpriority-method-in-class-win32-process


```go
func getPriorityValue((priorityClassName string)) (priorityClassName string)
```


**Тип ответа:** priorityClassName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/init_windows.go:38`



---


[function] name: initForOS file: cmd/kubelet/app/init_windows.go:76 returns_error: нет description: —


### initForOS (cmd/kubelet/app/init_windows.go:76)


initForOS is a function that performs operations based on the provided parameters and returns (ctx context.Context, windowsService bool, windowsPriorityClass string).


```go
func initForOS((ctx context.Context, windowsService bool, windowsPriorityClass string)) (ctx context.Context, windowsService bool, windowsPriorityClass string)
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


**Тип ответа:** windowsService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** windowsPriorityClass


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/init_windows.go:76`




## cmd/kubelet/app/options/globalflags.go


📄 Исходный файл: `cmd/kubelet/app/options/globalflags.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AddGlobalFlags](#addglobalflags-cmdkubeletappoptionsglobalflagsgo35) `:35`

- 🔗 [addCredentialProviderFlags](#addcredentialproviderflags-cmdkubeletappoptionsglobalflagsgo66) `:66`

- 🔗 [normalize](#normalize-cmdkubeletappoptionsglobalflagsgo44) `:44`

- 🔗 [register](#register-cmdkubeletappoptionsglobalflagsgo49) `:49`

- 🔗 [registerDeprecated](#registerdeprecated-cmdkubeletappoptionsglobalflagsgo60) `:60`


</details>


[function] name: AddGlobalFlags file: cmd/kubelet/app/options/globalflags.go:35 returns_error: нет description: AddGlobalFlags explicitly registers flags that libraries (glog, verflag, etc.) register
against the global flagsets from


### AddGlobalFlags (cmd/kubelet/app/options/globalflags.go:35)


AddGlobalFlags explicitly registers flags that libraries (glog, verflag, etc.) register
against the global flagsets from "flag" and "github.com/spf13/pflag".
We do this in order to prevent unwanted flags from leaking into the Kubelet's flagset.


```go
func AddGlobalFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/options/globalflags.go:35`



---


[function] name: addCredentialProviderFlags file: cmd/kubelet/app/options/globalflags.go:66 returns_error: нет description: addCredentialProviderFlags adds flags from k8s.io/kubernetes/pkg/credentialprovider


### addCredentialProviderFlags (cmd/kubelet/app/options/globalflags.go:66)


addCredentialProviderFlags adds flags from k8s.io/kubernetes/pkg/credentialprovider


```go
func addCredentialProviderFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/options/globalflags.go:66`



---


[function] name: normalize file: cmd/kubelet/app/options/globalflags.go:44 returns_error: нет description: normalize replaces underscores with hyphens
we should always use hyphens instead of underscores when registering kubelet


### normalize (cmd/kubelet/app/options/globalflags.go:44)


normalize replaces underscores with hyphens
we should always use hyphens instead of underscores when registering kubelet flags


```go
func normalize((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `cmd/kubelet/app/options/globalflags.go:44`



---


[function] name: register file: cmd/kubelet/app/options/globalflags.go:49 returns_error: нет description: register adds a flag to local that targets the Value associated with the Flag named globalName in global


### register (cmd/kubelet/app/options/globalflags.go:49)


register adds a flag to local that targets the Value associated with the Flag named globalName in global


```go
func register((global *flag.FlagSet, local *pflag.FlagSet, globalName string)) (global *flag.FlagSet, local *pflag.FlagSet, globalName string)
```


**Тип запроса:** flag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** global


```json
{
  "volumeName": {},
  "volumeSpec": null,
  "devicePath": "string",
  "mounter": {},
  "deviceMounter": {},
  "blockVolumeMapper": {},
  "podVolumes": {}
}
```


*Определено в:* `pkg/kubelet/volumemanager/reconciler/reconstruct_common.go`


**Тип ответа:** flag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** local


```json
{
  "config": null,
  "testCase": null,
  "cs": {},
  "pvc": null,
  "sourcePVC": null,
  "sc": null,
  "migrationCheck": null
}
```


*Определено в:* `test/e2e/storage/testsuites/provisioning.go`


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** globalName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/options/globalflags.go:49`



---


[function] name: registerDeprecated file: cmd/kubelet/app/options/globalflags.go:60 returns_error: нет description: registerDeprecated registers the flag with register, and then marks it deprecated


### registerDeprecated (cmd/kubelet/app/options/globalflags.go:60)


registerDeprecated registers the flag with register, and then marks it deprecated


```go
func registerDeprecated((global *flag.FlagSet, local *pflag.FlagSet, globalName, deprecated string)) (global *flag.FlagSet, local *pflag.FlagSet, globalName, deprecated string)
```


**Тип запроса:** flag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** global


```json
{
  "volumeName": {},
  "volumeSpec": null,
  "devicePath": "string",
  "mounter": {},
  "deviceMounter": {},
  "blockVolumeMapper": {},
  "podVolumes": {}
}
```


*Определено в:* `pkg/kubelet/volumemanager/reconciler/reconstruct_common.go`


**Тип ответа:** flag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** local


```json
{
  "config": null,
  "testCase": null,
  "cs": {},
  "pvc": null,
  "sourcePVC": null,
  "sc": null,
  "migrationCheck": null
}
```


*Определено в:* `test/e2e/storage/testsuites/provisioning.go`


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** globalName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** deprecated


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/options/globalflags.go:60`




## cmd/kubelet/app/options/globalflags_linux.go


📄 Исходный файл: `cmd/kubelet/app/options/globalflags_linux.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [addCadvisorFlags](#addcadvisorflags-cmdkubeletappoptionsglobalflags_linuxgo37) `:37`


</details>


[function] name: addCadvisorFlags file: cmd/kubelet/app/options/globalflags_linux.go:37 returns_error: нет description: addCadvisorFlags adds flags from cadvisor


### addCadvisorFlags (cmd/kubelet/app/options/globalflags_linux.go:37)


addCadvisorFlags adds flags from cadvisor


```go
func addCadvisorFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/options/globalflags_linux.go:37`




## cmd/kubelet/app/options/globalflags_other.go


📄 Исходный файл: `cmd/kubelet/app/options/globalflags_other.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [addCadvisorFlags](#addcadvisorflags-cmdkubeletappoptionsglobalflags_othergo25) `:25`


</details>


[function] name: addCadvisorFlags file: cmd/kubelet/app/options/globalflags_other.go:25 returns_error: нет description: —


### addCadvisorFlags (cmd/kubelet/app/options/globalflags_other.go:25)


addCadvisorFlags is a function that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func addCadvisorFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/options/globalflags_other.go:25`




## cmd/kubelet/app/options/options.go


📄 Исходный файл: `cmd/kubelet/app/options/options.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkubeletappoptionsoptionsgo258) `:258`

- 🔗 [AddFlags](#addflags-cmdkubeletappoptionsoptionsgo264) `:264`

- 🔗 [AddKubeletConfigFlags](#addkubeletconfigflags-cmdkubeletappoptionsoptionsgo333) `:333`

- 🔗 [NewKubeletConfiguration](#newkubeletconfiguration-cmdkubeletappoptionsoptionsgo197) `:197`

- 🔗 [NewKubeletFlags](#newkubeletflags-cmdkubeletappoptionsoptionsgo137) `:137`

- 🔗 [NewKubeletServer](#newkubeletserver-cmdkubeletappoptionsoptionsgo234) `:234`

- 🔗 [ValidateKubeletFlags](#validatekubeletflags-cmdkubeletappoptionsoptionsgo150) `:150`

- 🔗 [ValidateKubeletServer](#validatekubeletserver-cmdkubeletappoptionsoptionsgo246) `:246`

- 🔗 [addContainerRuntimeFlags](#addcontainerruntimeflags-cmdkubeletappoptionsoptionsgo323) `:323`

- 🔗 [applyLegacyDefaults](#applylegacydefaults-cmdkubeletappoptionsoptionsgo215) `:215`

- 🔗 [getLabelNamespace](#getlabelnamespace-cmdkubeletappoptionsoptionsgo189) `:189`

- 🔗 [isKubernetesLabel](#iskuberneteslabel-cmdkubeletappoptionsoptionsgo178) `:178`


</details>


[function] name: AddFlags file: cmd/kubelet/app/options/options.go:258 returns_error: нет description: AddFlags adds flags for a specific KubeletServer to the specified FlagSet


### AddFlags (cmd/kubelet/app/options/options.go:258)


AddFlags adds flags for a specific KubeletServer to the specified FlagSet


```go
func (s *KubeletServer) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/options/options.go:258`



---


[function] name: AddFlags file: cmd/kubelet/app/options/options.go:264 returns_error: нет description: AddFlags adds flags for a specific KubeletFlags to the specified FlagSet


### AddFlags (cmd/kubelet/app/options/options.go:264)


AddFlags adds flags for a specific KubeletFlags to the specified FlagSet


```go
func (f *KubeletFlags) AddFlags((mainfs *pflag.FlagSet)) (mainfs *pflag.FlagSet)
```


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** mainfs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


📍 *Расположение:* `cmd/kubelet/app/options/options.go:264`



---


[function] name: AddKubeletConfigFlags file: cmd/kubelet/app/options/options.go:333 returns_error: нет description: AddKubeletConfigFlags adds flags for a specific kubeletconfig.KubeletConfiguration to the specified FlagSet


### AddKubeletConfigFlags (cmd/kubelet/app/options/options.go:333)


AddKubeletConfigFlags adds flags for a specific kubeletconfig.KubeletConfiguration to the specified FlagSet


```go
func AddKubeletConfigFlags((mainfs *pflag.FlagSet, c *kubeletconfigapi.KubeletConfiguration)) (mainfs *pflag.FlagSet, c *kubeletconfigapi.KubeletConfiguration)
```


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип запроса:** kubeletconfigapi.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** mainfs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


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


**Тип ответа:** kubeletconfigapi.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


📍 *Расположение:* `cmd/kubelet/app/options/options.go:333`



---


[function] name: NewKubeletConfiguration file: cmd/kubelet/app/options/options.go:197 returns_error: да description: NewKubeletConfiguration will create a new KubeletConfiguration with default values


### NewKubeletConfiguration (cmd/kubelet/app/options/options.go:197)


NewKubeletConfiguration will create a new KubeletConfiguration with default values


```go
func NewKubeletConfiguration((*kubeletconfigapi.KubeletConfiguration, error)) (*kubeletconfigapi.KubeletConfiguration, error)
```


**Тип запроса:** kubeletconfigapi.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfigapi.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfigapi.KubeletConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/options/options.go:197`



---


[function] name: NewKubeletFlags file: cmd/kubelet/app/options/options.go:137 returns_error: нет description: NewKubeletFlags will create a new KubeletFlags with default values


### NewKubeletFlags (cmd/kubelet/app/options/options.go:137)


NewKubeletFlags will create a new KubeletFlags with default values


```go
func NewKubeletFlags(()) ()
```


📍 *Расположение:* `cmd/kubelet/app/options/options.go:137`



---


[function] name: NewKubeletServer file: cmd/kubelet/app/options/options.go:234 returns_error: да description: NewKubeletServer will create a new KubeletServer with default values.


### NewKubeletServer (cmd/kubelet/app/options/options.go:234)


NewKubeletServer will create a new KubeletServer with default values.


```go
func NewKubeletServer((*KubeletServer, error)) (*KubeletServer, error)
```


**Тип запроса:** KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*KubeletServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/options/options.go:234`



---


[function] name: ValidateKubeletFlags file: cmd/kubelet/app/options/options.go:150 returns_error: нет description: ValidateKubeletFlags validates Kubelet's configuration flags and returns an error if they are invalid.


### ValidateKubeletFlags (cmd/kubelet/app/options/options.go:150)


ValidateKubeletFlags validates Kubelet's configuration flags and returns an error if they are invalid.


```go
func ValidateKubeletFlags((f *KubeletFlags)) (f *KubeletFlags)
```


**Тип запроса:** KubeletFlags


```json
{
  "KubeConfig": "string",
  "BootstrapKubeconfig": "string",
  "HostnameOverride": "string",
  "NodeIP": "string",
  "CertDirectory": "string",
  "CloudProvider": "string",
  "CloudConfigFile": "string",
  "RootDirectory": "string",
  "KubeletConfigFile": "string",
  "KubeletDropinConfigDirectory": "string",
  "WindowsService": false,
  "WindowsPriorityClass": "string",
  "ExperimentalMounterPath": "string",
  "ExperimentalNodeAllocatableIgnoreEvictionThreshold": false,
  "NodeLabels": {},
  "LockFilePath": "string",
  "ExitOnLockContention": false,
  "MinimumGCAge": {},
  "MaxPerPodContainerCount": 0,
  "MaxContainerCount": 0,
  "SeccompDefault": false
}
```


*Определено в:* `cmd/kubelet/app/options/options.go`


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


**Тип ответа:** KubeletFlags


```json
{
  "KubeConfig": "string",
  "BootstrapKubeconfig": "string",
  "HostnameOverride": "string",
  "NodeIP": "string",
  "CertDirectory": "string",
  "CloudProvider": "string",
  "CloudConfigFile": "string",
  "RootDirectory": "string",
  "KubeletConfigFile": "string",
  "KubeletDropinConfigDirectory": "string",
  "WindowsService": false,
  "WindowsPriorityClass": "string",
  "ExperimentalMounterPath": "string",
  "ExperimentalNodeAllocatableIgnoreEvictionThreshold": false,
  "NodeLabels": {},
  "LockFilePath": "string",
  "ExitOnLockContention": false,
  "MinimumGCAge": {},
  "MaxPerPodContainerCount": 0,
  "MaxContainerCount": 0,
  "SeccompDefault": false
}
```


*Определено в:* `cmd/kubelet/app/options/options.go`


📍 *Расположение:* `cmd/kubelet/app/options/options.go:150`



---


[function] name: ValidateKubeletServer file: cmd/kubelet/app/options/options.go:246 returns_error: нет description: ValidateKubeletServer validates configuration of KubeletServer and returns an error if the input configuration is invali


### ValidateKubeletServer (cmd/kubelet/app/options/options.go:246)


ValidateKubeletServer validates configuration of KubeletServer and returns an error if the input configuration is invalid.


```go
func ValidateKubeletServer((s *KubeletServer)) (s *KubeletServer)
```


**Тип запроса:** KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/options/options.go:246`



---


[function] name: addContainerRuntimeFlags file: cmd/kubelet/app/options/options.go:323 returns_error: нет description: addContainerRuntimeFlags adds flags to the container runtime, according to ContainerRuntimeOptions.


### addContainerRuntimeFlags (cmd/kubelet/app/options/options.go:323)


addContainerRuntimeFlags adds flags to the container runtime, according to ContainerRuntimeOptions.


```go
func addContainerRuntimeFlags((fs *pflag.FlagSet, o *kubeletconfig.ContainerRuntimeOptions)) (fs *pflag.FlagSet, o *kubeletconfig.ContainerRuntimeOptions)
```


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип запроса:** kubeletconfig.ContainerRuntimeOptions


```json
{
  "RuntimeCgroups": "string",
  "ImageCredentialProviderConfigPath": "string",
  "ImageCredentialProviderBinDir": "string"
}
```


*Определено в:* `pkg/kubelet/kubeletconfig/types.go`


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


**Тип ответа:** o


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


**Тип ответа:** kubeletconfig.ContainerRuntimeOptions


```json
{
  "RuntimeCgroups": "string",
  "ImageCredentialProviderConfigPath": "string",
  "ImageCredentialProviderBinDir": "string"
}
```


*Определено в:* `pkg/kubelet/kubeletconfig/types.go`


📍 *Расположение:* `cmd/kubelet/app/options/options.go:323`



---


[function] name: applyLegacyDefaults file: cmd/kubelet/app/options/options.go:215 returns_error: нет description: applyLegacyDefaults applies legacy default values to the KubeletConfiguration in order to
preserve the command line API.


### applyLegacyDefaults (cmd/kubelet/app/options/options.go:215)


applyLegacyDefaults applies legacy default values to the KubeletConfiguration in order to
preserve the command line API. This is used to construct the baseline default KubeletConfiguration
before the first round of flag parsing.


```go
func applyLegacyDefaults((kc *kubeletconfigapi.KubeletConfiguration)) (kc *kubeletconfigapi.KubeletConfiguration)
```


**Тип запроса:** kubeletconfigapi.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kc


```json
{
  "keyID": "string",
  "aead": {}
}
```


*Определено в:* `staging/src/k8s.io/kms/internal/plugins/_mock/pkcs11/pkcs11.go`


**Тип ответа:** kubeletconfigapi.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


📍 *Расположение:* `cmd/kubelet/app/options/options.go:215`



---


[function] name: getLabelNamespace file: cmd/kubelet/app/options/options.go:189 returns_error: нет description: —


### getLabelNamespace (cmd/kubelet/app/options/options.go:189)


getLabelNamespace is a function that performs operations based on the provided parameters and returns (key string).


```go
func getLabelNamespace((key string)) (key string)
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


📍 *Расположение:* `cmd/kubelet/app/options/options.go:189`



---


[function] name: isKubernetesLabel file: cmd/kubelet/app/options/options.go:178 returns_error: нет description: —


### isKubernetesLabel (cmd/kubelet/app/options/options.go:178)


isKubernetesLabel is a function that performs operations based on the provided parameters and returns (key string).


```go
func isKubernetesLabel((key string)) (key string)
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


📍 *Расположение:* `cmd/kubelet/app/options/options.go:178`




## cmd/kubelet/app/options/osflags_others.go


📄 Исходный файл: `cmd/kubelet/app/options/osflags_others.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [addOSFlags](#addosflags-cmdkubeletappoptionsosflags_othersgo25) `:25`


</details>


[function] name: addOSFlags file: cmd/kubelet/app/options/osflags_others.go:25 returns_error: нет description: —


### addOSFlags (cmd/kubelet/app/options/osflags_others.go:25)


addOSFlags is a method that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func (f *KubeletFlags) addOSFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/options/osflags_others.go:25`




## cmd/kubelet/app/options/osflags_windows.go


📄 Исходный файл: `cmd/kubelet/app/options/osflags_windows.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [addOSFlags](#addosflags-cmdkubeletappoptionsosflags_windowsgo25) `:25`


</details>


[function] name: addOSFlags file: cmd/kubelet/app/options/osflags_windows.go:25 returns_error: нет description: —


### addOSFlags (cmd/kubelet/app/options/osflags_windows.go:25)


addOSFlags is a method that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func (f *KubeletFlags) addOSFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/options/osflags_windows.go:25`




## cmd/kubelet/app/plugins.go


📄 Исходный файл: `cmd/kubelet/app/plugins.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetDynamicPluginProber](#getdynamicpluginprober-cmdkubeletapppluginsgo76) `:76`

- 🔗 [ProbeVolumePlugins](#probevolumeplugins-cmdkubeletapppluginsgo46) `:46`


</details>


[function] name: GetDynamicPluginProber file: cmd/kubelet/app/plugins.go:76 returns_error: нет description: GetDynamicPluginProber gets the probers of dynamically discoverable plugins
for kubelet.
Currently only Flexvolume plugi


### GetDynamicPluginProber (cmd/kubelet/app/plugins.go:76)


GetDynamicPluginProber gets the probers of dynamically discoverable plugins
for kubelet.
Currently only Flexvolume plugins are dynamically discoverable.


```go
func GetDynamicPluginProber((pluginDir string, runner exec.Interface)) (pluginDir string, runner exec.Interface)
```


**Тип ответа:** pluginDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** runner


```json
{
  "mu": {},
  "exec": {},
  "protocol": {},
  "hasCheck": false,
  "hasRandomFully": false,
  "waitFlag": [],
  "restoreWaitFlag": [],
  "lockfilePath14x": "string",
  "lockfilePath16x": "string"
}
```


*Определено в:* `pkg/util/iptables/iptables.go`


**Тип ответа:** exec.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `cmd/kubelet/app/plugins.go:76`



---


[function] name: ProbeVolumePlugins file: cmd/kubelet/app/plugins.go:46 returns_error: да description: ProbeVolumePlugins collects all volume plugins into an easy to use list.


### ProbeVolumePlugins (cmd/kubelet/app/plugins.go:46)


ProbeVolumePlugins collects all volume plugins into an easy to use list.


```go
func ProbeVolumePlugins(([]volume.VolumePlugin, error)) ([]volume.VolumePlugin, error)
```


**Тип ответа:** volume.VolumePlugin


```json
{
  "mutex": {},
  "plugins": {},
  "prober": {},
  "probedPlugins": {},
  "Host": {}
}
```


*Определено в:* `pkg/volume/plugins.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]volume.VolumePlugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/plugins.go:46`




## cmd/kubelet/app/server.go


📄 Исходный файл: `cmd/kubelet/app/server.go`


<details open>
<summary><b>Функции в этом файле (27)</b></summary>


- 🔗 [InitializeTLS](#initializetls-cmdkubeletappservergo1119) `:1119`

- 🔗 [NewKubeletCommand](#newkubeletcommand-cmdkubeletappservergo139) `:139`

- 🔗 [Run](#run-cmdkubeletappservergo539) `:539`

- 🔗 [RunKubelet](#runkubelet-cmdkubeletappservergo1223) `:1223`

- 🔗 [UnsecuredDependencies](#unsecureddependencies-cmdkubeletappservergo497) `:497`

- 🔗 [buildClientCertificateManager](#buildclientcertificatemanager-cmdkubeletappservergo1081) `:1081`

- 🔗 [buildKubeletClientConfig](#buildkubeletclientconfig-cmdkubeletappservergo948) `:948`

- 🔗 [createAndInitKubelet](#createandinitkubelet-cmdkubeletappservergo1293) `:1293`

- 🔗 [getCgroupDriverFromCRI](#getcgroupdriverfromcri-cmdkubeletappservergo1388) `:1388`

- 🔗 [getReservedCPUs](#getreservedcpus-cmdkubeletappservergo599) `:599`

- 🔗 [init](#init-cmdkubeletappservergo131) `:131`

- 🔗 [initConfigz](#initconfigz-cmdkubeletappservergo568) `:568`

- 🔗 [kubeClientConfigOverrides](#kubeclientconfigoverrides-cmdkubeletappservergo1110) `:1110`

- 🔗 [kubeletConfigFlagPrecedence](#kubeletconfigflagprecedence-cmdkubeletappservergo425) `:425`

- 🔗 [loadConfigFile](#loadconfigfile-cmdkubeletappservergo450) `:450`

- 🔗 [loadDropinConfigFileIntoJSON](#loaddropinconfigfileintojson-cmdkubeletappservergo481) `:481`

- 🔗 [makeEventRecorder](#makeeventrecorder-cmdkubeletappservergo583) `:583`

- 🔗 [mergeKubeletConfigurations](#mergekubeletconfigurations-cmdkubeletappservergo335) `:335`

- 🔗 [newFakeFlagSet](#newfakeflagset-cmdkubeletappservergo412) `:412`

- 🔗 [newFlagSetWithGlobals](#newflagsetwithglobals-cmdkubeletappservergo401) `:401`

- 🔗 [newTracerProvider](#newtracerprovider-cmdkubeletappservergo1367) `:1367`

- 🔗 [parseResourceList](#parseresourcelist-cmdkubeletappservergo1343) `:1343`

- 🔗 [run](#run-cmdkubeletappservergo621) `:621`

- 🔗 [setConfigz](#setconfigz-cmdkubeletappservergo555) `:555`

- 🔗 [setContentTypeForClient](#setcontenttypeforclient-cmdkubeletappservergo1203) `:1203`

- 🔗 [startKubelet](#startkubelet-cmdkubeletappservergo1279) `:1279`

- 🔗 [updateDialer](#updatedialer-cmdkubeletappservergo1069) `:1069`


</details>


[function] name: InitializeTLS file: cmd/kubelet/app/server.go:1119 returns_error: да description: InitializeTLS checks for a configured TLSCertFile and TLSPrivateKeyFile: if unspecified a new self-signed
certificate an


### InitializeTLS (cmd/kubelet/app/server.go:1119)


InitializeTLS checks for a configured TLSCertFile and TLSPrivateKeyFile: if unspecified a new self-signed
certificate and key file are generated. Returns a configured server.TLSOptions object.


```go
func InitializeTLS((*server.TLSOptions, error)) (*server.TLSOptions, error)
```


**Тип запроса:** server.TLSOptions


```json
{
  "Config": null,
  "CertFile": "string",
  "KeyFile": "string"
}
```


*Определено в:* `pkg/kubelet/server/server.go`


**Тип ответа:** server.TLSOptions


```json
{
  "Config": null,
  "CertFile": "string",
  "KeyFile": "string"
}
```


*Определено в:* `pkg/kubelet/server/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*server.TLSOptions`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:1119`



---


[function] name: NewKubeletCommand file: cmd/kubelet/app/server.go:139 returns_error: нет description: NewKubeletCommand creates a *cobra.Command object with default parameters


### NewKubeletCommand (cmd/kubelet/app/server.go:139)


NewKubeletCommand creates a *cobra.Command object with default parameters


```go
func NewKubeletCommand((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kubelet/app/server.go:139`



---


[function] name: Run file: cmd/kubelet/app/server.go:539 returns_error: нет description: Run runs the specified KubeletServer with the given Dependencies. This should never exit.
The kubeDeps argument may be n


### Run (cmd/kubelet/app/server.go:539)


Run runs the specified KubeletServer with the given Dependencies. This should never exit.
The kubeDeps argument may be nil - if so, it is initialized from the settings on KubeletServer.
Otherwise, the caller is assumed to have set up the Dependencies object and a default one will
not be generated.


```go
func Run((ctx context.Context, s *options.KubeletServer, kubeDeps *kubelet.Dependencies, featureGate featuregate.FeatureGate)) (ctx context.Context, s *options.KubeletServer, kubeDeps *kubelet.Dependencies, featureGate featuregate.FeatureGate)
```


**Тип запроса:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


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


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeDeps


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


**Тип ответа:** featureGate


```json
{
  "featureGateName": "string",
  "special": {},
  "lock": {},
  "known": {},
  "enabled": {},
  "dependencies": {},
  "enabledRaw": {},
  "closed": false,
  "queriedFeatures": {},
  "emulationVersion": {},
  "minCompatibilityVersion": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/featuregate/feature_gate.go`


**Тип ответа:** featuregate.FeatureGate


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `cmd/kubelet/app/server.go:539`



---


[function] name: RunKubelet file: cmd/kubelet/app/server.go:1223 returns_error: нет description: RunKubelet is responsible for setting up and running a kubelet.  It is used in three different applications:

1 Integrat


### RunKubelet (cmd/kubelet/app/server.go:1223)


RunKubelet is responsible for setting up and running a kubelet.  It is used in three different applications:

1 Integration tests
2 Kubelet binary
3 Standalone 'kubernetes' binary

Eventually, #2 will be replaced with instances of #3


```go
func RunKubelet((ctx context.Context, kubeServer *options.KubeletServer, kubeDeps *kubelet.Dependencies)) (ctx context.Context, kubeServer *options.KubeletServer, kubeDeps *kubelet.Dependencies)
```


**Тип запроса:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


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


**Тип ответа:** kubeServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeDeps


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


📍 *Расположение:* `cmd/kubelet/app/server.go:1223`



---


[function] name: UnsecuredDependencies file: cmd/kubelet/app/server.go:497 returns_error: да description: UnsecuredDependencies returns a Dependencies suitable for being run, or an error if the server setup
is not valid.  It w


### UnsecuredDependencies (cmd/kubelet/app/server.go:497)


UnsecuredDependencies returns a Dependencies suitable for being run, or an error if the server setup
is not valid.  It will not start any background processes, and does not include authentication/authorization


```go
func UnsecuredDependencies((*kubelet.Dependencies, error)) (*kubelet.Dependencies, error)
```


**Тип запроса:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


**Тип ответа:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubelet.Dependencies`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:497`



---


[function] name: buildClientCertificateManager file: cmd/kubelet/app/server.go:1081 returns_error: да description: buildClientCertificateManager creates a certificate manager that will use certConfig to request a client certificate
if 


### buildClientCertificateManager (cmd/kubelet/app/server.go:1081)


buildClientCertificateManager creates a certificate manager that will use certConfig to request a client certificate
if no certificate is available, or the most recent clientConfig (which is assumed to point to the cert that the manager will
write out).


```go
func buildClientCertificateManager((certificate.Manager, error)) (certificate.Manager, error)
```


**Тип ответа:** certificate.Manager


```json
{
  "draPlugins": null,
  "cache": null,
  "reconcilePeriod": {},
  "activePods": {},
  "sourcesReady": {},
  "kubeClient": {},
  "healthInfoCache": null,
  "update": {}
}
```


*Определено в:* `pkg/kubelet/cm/dra/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `certificate.Manager`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:1081`



---


[function] name: buildKubeletClientConfig file: cmd/kubelet/app/server.go:948 returns_error: да description: buildKubeletClientConfig constructs the appropriate client config for the kubelet depending on whether
bootstrapping is 


### buildKubeletClientConfig (cmd/kubelet/app/server.go:948)


buildKubeletClientConfig constructs the appropriate client config for the kubelet depending on whether
bootstrapping is enabled or client certificate rotation is enabled.


```go
func buildKubeletClientConfig((*restclient.Config, func(), error)) (*restclient.Config, func(), error)
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


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*restclient.Config`, `func()`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:948`



---


[function] name: createAndInitKubelet file: cmd/kubelet/app/server.go:1293 returns_error: да description: —


### createAndInitKubelet (cmd/kubelet/app/server.go:1293)


createAndInitKubelet is a function that performs operations based on the provided parameters and may return an error.


```go
func createAndInitKubelet((k kubelet.Bootstrap, err error)) (k kubelet.Bootstrap, err error)
```


**Тип ответа:** k


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


**Тип ответа:** kubelet.Bootstrap


```json
{
  "TokenStr": "string"
}
```


*Определено в:* `cmd/kubeadm/app/cmd/options/token.go`


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


*Типы возврата:* `k kubelet.Bootstrap`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:1293`



---


[function] name: getCgroupDriverFromCRI file: cmd/kubelet/app/server.go:1388 returns_error: нет description: —


### getCgroupDriverFromCRI (cmd/kubelet/app/server.go:1388)


getCgroupDriverFromCRI is a function that performs operations based on the provided parameters and returns (ctx context.Context, s *options.KubeletServer, kubeDeps *kubelet.Dependencies).


```go
func getCgroupDriverFromCRI((ctx context.Context, s *options.KubeletServer, kubeDeps *kubelet.Dependencies)) (ctx context.Context, s *options.KubeletServer, kubeDeps *kubelet.Dependencies)
```


**Тип запроса:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


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


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeDeps


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


📍 *Расположение:* `cmd/kubelet/app/server.go:1388`



---


[function] name: getReservedCPUs file: cmd/kubelet/app/server.go:599 returns_error: да description: —


### getReservedCPUs (cmd/kubelet/app/server.go:599)


getReservedCPUs is a function that performs operations based on the provided parameters and may return an error.


```go
func getReservedCPUs((cpuset.CPUSet, error)) (cpuset.CPUSet, error)
```


**Тип ответа:** cpuset.CPUSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cpuset.CPUSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:599`



---


[function] name: init file: cmd/kubelet/app/server.go:131 returns_error: нет description: —


### init (cmd/kubelet/app/server.go:131)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kubelet/app/server.go:131`



---


[function] name: initConfigz file: cmd/kubelet/app/server.go:568 returns_error: нет description: —


### initConfigz (cmd/kubelet/app/server.go:568)


initConfigz is a function that performs operations based on the provided parameters and returns (ctx context.Context, kc *kubeletconfiginternal.KubeletConfiguration).


```go
func initConfigz((ctx context.Context, kc *kubeletconfiginternal.KubeletConfiguration)) (ctx context.Context, kc *kubeletconfiginternal.KubeletConfiguration)
```


**Тип запроса:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


**Тип ответа:** kc


```json
{
  "keyID": "string",
  "aead": {}
}
```


*Определено в:* `staging/src/k8s.io/kms/internal/plugins/_mock/pkcs11/pkcs11.go`


**Тип ответа:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


📍 *Расположение:* `cmd/kubelet/app/server.go:568`



---


[function] name: kubeClientConfigOverrides file: cmd/kubelet/app/server.go:1110 returns_error: нет description: —


### kubeClientConfigOverrides (cmd/kubelet/app/server.go:1110)


kubeClientConfigOverrides is a function that performs operations based on the provided parameters and returns (s *options.KubeletServer, clientConfig *restclient.Config).


```go
func kubeClientConfigOverrides((s *options.KubeletServer, clientConfig *restclient.Config)) (s *options.KubeletServer, clientConfig *restclient.Config)
```


**Тип запроса:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** options.KubeletServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientConfig


```json
{
  "defaultClientConfig": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/genericclioptions/client_config.go`


**Тип ответа:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `cmd/kubelet/app/server.go:1110`



---


[function] name: kubeletConfigFlagPrecedence file: cmd/kubelet/app/server.go:425 returns_error: нет description: kubeletConfigFlagPrecedence re-parses flags over the KubeletConfiguration object.
We must enforce flag precedence by re-


### kubeletConfigFlagPrecedence (cmd/kubelet/app/server.go:425)


kubeletConfigFlagPrecedence re-parses flags over the KubeletConfiguration object.
We must enforce flag precedence by re-parsing the command line into the new object.
This is necessary to preserve backwards-compatibility across binary upgrades.
See issue #56171 for more details.


```go
func kubeletConfigFlagPrecedence((kc *kubeletconfiginternal.KubeletConfiguration, args []string)) (kc *kubeletconfiginternal.KubeletConfiguration, args []string)
```


**Тип запроса:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kc


```json
{
  "keyID": "string",
  "aead": {}
}
```


*Определено в:* `staging/src/k8s.io/kms/internal/plugins/_mock/pkcs11/pkcs11.go`


**Тип ответа:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/server.go:425`



---


[function] name: loadConfigFile file: cmd/kubelet/app/server.go:450 returns_error: да description: —


### loadConfigFile (cmd/kubelet/app/server.go:450)


loadConfigFile is a function that performs operations based on the provided parameters and may return an error.


```go
func loadConfigFile((*kubeletconfiginternal.KubeletConfiguration, error)) (*kubeletconfiginternal.KubeletConfiguration, error)
```


**Тип запроса:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfiginternal.KubeletConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:450`



---


[function] name: loadDropinConfigFileIntoJSON file: cmd/kubelet/app/server.go:481 returns_error: да description: —


### loadDropinConfigFileIntoJSON (cmd/kubelet/app/server.go:481)


loadDropinConfigFileIntoJSON is a function that performs operations based on the provided parameters and may return an error.


```go
func loadDropinConfigFileIntoJSON(([]byte, *schema.GroupVersionKind, error)) ([]byte, *schema.GroupVersionKind, error)
```


**Тип запроса:** schema.GroupVersionKind


```json
{
  "Group": "string",
  "Version": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** schema.GroupVersionKind


```json
{
  "Group": "string",
  "Version": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `*schema.GroupVersionKind`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:481`



---


[function] name: makeEventRecorder file: cmd/kubelet/app/server.go:583 returns_error: нет description: makeEventRecorder sets up kubeDeps.Recorder if it's nil. It's a no-op otherwise.


### makeEventRecorder (cmd/kubelet/app/server.go:583)


makeEventRecorder sets up kubeDeps.Recorder if it's nil. It's a no-op otherwise.


```go
func makeEventRecorder((ctx context.Context, kubeDeps *kubelet.Dependencies, nodeName types.NodeName)) (ctx context.Context, kubeDeps *kubelet.Dependencies, nodeName types.NodeName)
```


**Тип запроса:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


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


**Тип ответа:** kubeDeps


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NodeName


```json
{
  "enableSchedulingQueueHint": false
}
```


*Определено в:* `pkg/scheduler/framework/plugins/nodename/node_name.go`


📍 *Расположение:* `cmd/kubelet/app/server.go:583`



---


[function] name: mergeKubeletConfigurations file: cmd/kubelet/app/server.go:335 returns_error: да description: mergeKubeletConfigurations merges the provided drop-in configurations with the base kubelet configuration.
The drop-in c


### mergeKubeletConfigurations (cmd/kubelet/app/server.go:335)


mergeKubeletConfigurations merges the provided drop-in configurations with the base kubelet configuration.
The drop-in configurations are processed in lexical order based on the file names. This means that the
configurations in files with lower numeric prefixes are applied first, followed by higher numeric prefixes.
For example, if the drop-in directory contains files named "10-config.conf" and "20-config.conf",
the configurations in "10-config.conf" will be applied first, and then the configurations in "20-config.conf" will be applied,
potentially overriding the previous values. Files in subdirectories are also processed in lexical order.
Returns a list of skipped files and an error.


```go
func mergeKubeletConfigurations(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:335`



---


[function] name: newFakeFlagSet file: cmd/kubelet/app/server.go:412 returns_error: нет description: newFakeFlagSet constructs a pflag.FlagSet with the same flags as fs, but where
all values have noop Set implementations


### newFakeFlagSet (cmd/kubelet/app/server.go:412)


newFakeFlagSet constructs a pflag.FlagSet with the same flags as fs, but where
all values have noop Set implementations


```go
func newFakeFlagSet((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubelet/app/server.go:412`



---


[function] name: newFlagSetWithGlobals file: cmd/kubelet/app/server.go:401 returns_error: нет description: newFlagSetWithGlobals constructs a new pflag.FlagSet with global flags registered
on it.


### newFlagSetWithGlobals (cmd/kubelet/app/server.go:401)


newFlagSetWithGlobals constructs a new pflag.FlagSet with global flags registered
on it.


```go
func newFlagSetWithGlobals(()) ()
```


📍 *Расположение:* `cmd/kubelet/app/server.go:401`



---


[function] name: newTracerProvider file: cmd/kubelet/app/server.go:1367 returns_error: да description: —


### newTracerProvider (cmd/kubelet/app/server.go:1367)


newTracerProvider is a function that performs operations based on the provided parameters and may return an error.


```go
func newTracerProvider((oteltrace.TracerProvider, error)) (oteltrace.TracerProvider, error)
```


**Тип ответа:** oteltrace.TracerProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `oteltrace.TracerProvider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:1367`



---


[function] name: parseResourceList file: cmd/kubelet/app/server.go:1343 returns_error: да description: parseResourceList parses the given configuration map into an API
ResourceList or returns an error.


### parseResourceList (cmd/kubelet/app/server.go:1343)


parseResourceList parses the given configuration map into an API
ResourceList or returns an error.


```go
func parseResourceList((v1.ResourceList, error)) (v1.ResourceList, error)
```


**Тип ответа:** v1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `v1.ResourceList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:1343`



---


[function] name: run file: cmd/kubelet/app/server.go:621 returns_error: да description: —


### run (cmd/kubelet/app/server.go:621)


run is a function that performs operations based on the provided parameters and may return an error.


```go
func run((err error)) (err error)
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


📍 *Расположение:* `cmd/kubelet/app/server.go:621`



---


[function] name: setConfigz file: cmd/kubelet/app/server.go:555 returns_error: нет description: —


### setConfigz (cmd/kubelet/app/server.go:555)


setConfigz is a function that performs operations based on the provided parameters and returns (cz *configz.Config, kc *kubeletconfiginternal.KubeletConfiguration).


```go
func setConfigz((cz *configz.Config, kc *kubeletconfiginternal.KubeletConfiguration)) (cz *configz.Config, kc *kubeletconfiginternal.KubeletConfiguration)
```


**Тип запроса:** configz.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип запроса:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** cz


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** configz.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** kc


```json
{
  "keyID": "string",
  "aead": {}
}
```


*Определено в:* `staging/src/k8s.io/kms/internal/plugins/_mock/pkcs11/pkcs11.go`


**Тип ответа:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


📍 *Расположение:* `cmd/kubelet/app/server.go:555`



---


[function] name: setContentTypeForClient file: cmd/kubelet/app/server.go:1203 returns_error: нет description: setContentTypeForClient sets the appropriate content type into the rest config
and handles defaulting AcceptContentTypes


### setContentTypeForClient (cmd/kubelet/app/server.go:1203)


setContentTypeForClient sets the appropriate content type into the rest config
and handles defaulting AcceptContentTypes based on that input.


```go
func setContentTypeForClient((cfg *restclient.Config, contentType string)) (cfg *restclient.Config, contentType string)
```


**Тип запроса:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


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


**Тип ответа:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** contentType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/server.go:1203`



---


[function] name: startKubelet file: cmd/kubelet/app/server.go:1279 returns_error: нет description: —


### startKubelet (cmd/kubelet/app/server.go:1279)


startKubelet is a function that performs operations based on the provided parameters and returns (ctx context.Context, k kubelet.Bootstrap, podCfg *config.PodConfig, kubeCfg *kubeletconfiginternal.KubeletConfiguration, kubeDeps *kubelet.Dependencies, enableServer bool).


```go
func startKubelet((ctx context.Context, k kubelet.Bootstrap, podCfg *config.PodConfig, kubeCfg *kubeletconfiginternal.KubeletConfiguration, kubeDeps *kubelet.Dependencies, enableServer bool)) (ctx context.Context, k kubelet.Bootstrap, podCfg *config.PodConfig, kubeCfg *kubeletconfiginternal.KubeletConfiguration, kubeDeps *kubelet.Dependencies, enableServer bool)
```


**Тип запроса:** config.PodConfig


```json
{
  "pods": null,
  "mux": null,
  "updates": {},
  "sourcesLock": {},
  "sources": {}
}
```


*Определено в:* `pkg/kubelet/config/config.go`


**Тип запроса:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип запроса:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


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


**Тип ответа:** k


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


**Тип ответа:** kubelet.Bootstrap


```json
{
  "TokenStr": "string"
}
```


*Определено в:* `cmd/kubeadm/app/cmd/options/token.go`


**Тип ответа:** podCfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.PodConfig


```json
{
  "pods": null,
  "mux": null,
  "updates": {},
  "sourcesLock": {},
  "sources": {}
}
```


*Определено в:* `pkg/kubelet/config/config.go`


**Тип ответа:** kubeCfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeletconfiginternal.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeDeps


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubelet.Dependencies


```json
{
  "Options": [],
  "Flagz": {},
  "Auth": {},
  "CAdvisorInterface": {},
  "ContainerManager": {},
  "EventClient": {},
  "HeartbeatClient": {},
  "OnHeartbeatFailure": {},
  "KubeClient": {},
  "Mounter": {},
  "HostUtil": {},
  "OOMAdjuster": null,
  "OSInterface": {},
  "PodConfig": null,
  "ProbeManager": {},
  "Recorder": {},
  "Subpather": {},
  "TracerProvider": {},
  "VolumePlugins": [],
  "DynamicPluginProber": {},
  "TLSOptions": null,
  "RemoteRuntimeService": {},
  "RemoteImageService": {},
  "PodStartupLatencyTracker": {},
  "NodeStartupLatencyTracker": {},
  "HealthChecker": {},
  "useLegacyCadvisorStats": false
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


**Тип ответа:** enableServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kubelet/app/server.go:1279`



---


[function] name: updateDialer file: cmd/kubelet/app/server.go:1069 returns_error: да description: updateDialer instruments a restconfig with a dial. the returned function allows forcefully closing all active connection


### updateDialer (cmd/kubelet/app/server.go:1069)


updateDialer instruments a restconfig with a dial. the returned function allows forcefully closing all active connections.


```go
func updateDialer((func(), error)) (func(), error)
```


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `func()`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kubelet/app/server.go:1069`




## cmd/kubelet/app/server_linux.go


📄 Исходный файл: `cmd/kubelet/app/server_linux.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [watchForLockfileContention](#watchforlockfilecontention-cmdkubeletappserver_linuxgo26) `:26`


</details>


[function] name: watchForLockfileContention file: cmd/kubelet/app/server_linux.go:26 returns_error: нет description: —


### watchForLockfileContention (cmd/kubelet/app/server_linux.go:26)


watchForLockfileContention is a function that performs operations based on the provided parameters and returns (ctx context.Context, path string, done chan struct{}).


```go
func watchForLockfileContention((ctx context.Context, path string, done chan struct{})) (ctx context.Context, path string, done chan struct{})
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


**Тип ответа:** done


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


📍 *Расположение:* `cmd/kubelet/app/server_linux.go:26`




## cmd/kubelet/app/server_others.go


📄 Исходный файл: `cmd/kubelet/app/server_others.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [checkPermissions](#checkpermissions-cmdkubeletappserver_othersgo27) `:27`


</details>


[function] name: checkPermissions file: cmd/kubelet/app/server_others.go:27 returns_error: нет description: —


### checkPermissions (cmd/kubelet/app/server_others.go:27)


checkPermissions is a function that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func checkPermissions((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kubelet/app/server_others.go:27`




## cmd/kubelet/app/server_unsupported.go


📄 Исходный файл: `cmd/kubelet/app/server_unsupported.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [isCgroup2UnifiedMode](#iscgroup2unifiedmode-cmdkubeletappserver_unsupportedgo30) `:30`

- 🔗 [watchForLockfileContention](#watchforlockfilecontention-cmdkubeletappserver_unsupportedgo26) `:26`


</details>


[function] name: isCgroup2UnifiedMode file: cmd/kubelet/app/server_unsupported.go:30 returns_error: нет description: —


### isCgroup2UnifiedMode (cmd/kubelet/app/server_unsupported.go:30)


isCgroup2UnifiedMode is a function that performs operations based on the provided parameters and returns ().


```go
func isCgroup2UnifiedMode(()) ()
```


📍 *Расположение:* `cmd/kubelet/app/server_unsupported.go:30`



---


[function] name: watchForLockfileContention file: cmd/kubelet/app/server_unsupported.go:26 returns_error: нет description: —


### watchForLockfileContention (cmd/kubelet/app/server_unsupported.go:26)


watchForLockfileContention is a function that performs operations based on the provided parameters and returns (ctx context.Context, path string, done chan struct{}).


```go
func watchForLockfileContention((ctx context.Context, path string, done chan struct{})) (ctx context.Context, path string, done chan struct{})
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


**Тип ответа:** done


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


📍 *Расположение:* `cmd/kubelet/app/server_unsupported.go:26`




## cmd/kubelet/app/server_windows.go


📄 Исходный файл: `cmd/kubelet/app/server_windows.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [checkPermissions](#checkpermissions-cmdkubeletappserver_windowsgo30) `:30`


</details>


[function] name: checkPermissions file: cmd/kubelet/app/server_windows.go:30 returns_error: нет description: —


### checkPermissions (cmd/kubelet/app/server_windows.go:30)


checkPermissions is a function that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func checkPermissions((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kubelet/app/server_windows.go:30`




## cmd/kubelet/kubelet.go


📄 Исходный файл: `cmd/kubelet/kubelet.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdkubeletkubeletgo35) `:35`


</details>


[function] name: main file: cmd/kubelet/kubelet.go:35 returns_error: нет description: —


### main (cmd/kubelet/kubelet.go:35)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/kubelet/kubelet.go:35`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kubectl-convert.md)

- [Следующая директория](cmd_kubemark.md)


---

