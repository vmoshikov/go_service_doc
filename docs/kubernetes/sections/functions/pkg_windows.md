---
title: "Функции: pkg/windows"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/windows
---


# Функции: pkg/windows


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_volume.md)

- [Следующая директория](plugin_pkg.md)


---


## Меню по файлам


- 📄 [pkg/windows/service/service.go](#pkgwindowsserviceservicego)


---


## pkg/windows/service/service.go


📄 Исходный файл: `pkg/windows/service/service.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [Execute](#execute-pkgwindowsserviceservicego141) `:141`

- 🔗 [InitService](#initservice-pkgwindowsserviceservicego94) `:94`

- 🔗 [InitServiceWithShutdown](#initservicewithshutdown-pkgwindowsserviceservicego101) `:101`

- 🔗 [IsServiceInitialized](#isserviceinitialized-pkgwindowsserviceservicego137) `:137`

- 🔗 [QueryPreShutdownInfo](#querypreshutdowninfo-pkgwindowsserviceservicego50) `:50`

- 🔗 [SetPreShutdownHandler](#setpreshutdownhandler-pkgwindowsserviceservicego133) `:133`

- 🔗 [UpdatePreShutdownInfo](#updatepreshutdowninfo-pkgwindowsserviceservicego75) `:75`

- 🔗 [initService](#initservice-pkgwindowsserviceservicego107) `:107`


</details>


[function] name: Execute file: pkg/windows/service/service.go:141 returns_error: нет description: —


### Execute (pkg/windows/service/service.go:141)


Execute is a method that performs operations based on the provided parameters and returns (bool, uint32).


```go
func (h *handler) Execute((bool, uint32)) (bool, uint32)
```


📍 *Расположение:* `pkg/windows/service/service.go:141`



---


[function] name: InitService file: pkg/windows/service/service.go:94 returns_error: нет description: InitService is the entry point for running the daemon as a Windows
service. It returns an indication of whether it is ru


### InitService (pkg/windows/service/service.go:94)


InitService is the entry point for running the daemon as a Windows
service. It returns an indication of whether it is running as a service;
and an error.


```go
func InitService((serviceName string)) (serviceName string)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


📍 *Расположение:* `pkg/windows/service/service.go:94`



---


[function] name: InitServiceWithShutdown file: pkg/windows/service/service.go:101 returns_error: нет description: InitService is the entry point for running the daemon as a Windows
service which will accept preshutdown event. It retur


### InitServiceWithShutdown (pkg/windows/service/service.go:101)


InitService is the entry point for running the daemon as a Windows
service which will accept preshutdown event. It returns an indication
of whether it is running as a service; and an error.


```go
func InitServiceWithShutdown((serviceName string)) (serviceName string)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


📍 *Расположение:* `pkg/windows/service/service.go:101`



---


[function] name: IsServiceInitialized file: pkg/windows/service/service.go:137 returns_error: нет description: —


### IsServiceInitialized (pkg/windows/service/service.go:137)


IsServiceInitialized is a function that performs operations based on the provided parameters and returns ().


```go
func IsServiceInitialized(()) ()
```


📍 *Расположение:* `pkg/windows/service/service.go:137`



---


[function] name: QueryPreShutdownInfo file: pkg/windows/service/service.go:50 returns_error: да description: —


### QueryPreShutdownInfo (pkg/windows/service/service.go:50)


QueryPreShutdownInfo is a function that performs operations based on the provided parameters and may return an error.


```go
func QueryPreShutdownInfo((*SERVICE_PRESHUTDOWN_INFO, error)) (*SERVICE_PRESHUTDOWN_INFO, error)
```


**Тип запроса:** SERVICE_PRESHUTDOWN_INFO


```json
{
  "PreshutdownTimeout": 0
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** SERVICE_PRESHUTDOWN_INFO


```json
{
  "PreshutdownTimeout": 0
}
```


*Определено в:* `pkg/windows/service/service.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SERVICE_PRESHUTDOWN_INFO`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/windows/service/service.go:50`



---


[function] name: SetPreShutdownHandler file: pkg/windows/service/service.go:133 returns_error: нет description: —


### SetPreShutdownHandler (pkg/windows/service/service.go:133)


SetPreShutdownHandler is a function that updates data based on the provided parameters and returns (preshutdownhandler PreshutdownHandler).


```go
func SetPreShutdownHandler((preshutdownhandler PreshutdownHandler)) (preshutdownhandler PreshutdownHandler)
```


**Тип ответа:** preshutdownhandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PreshutdownHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/windows/service/service.go:133`



---


[function] name: UpdatePreShutdownInfo file: pkg/windows/service/service.go:75 returns_error: нет description: —


### UpdatePreShutdownInfo (pkg/windows/service/service.go:75)


UpdatePreShutdownInfo is a function that updates data based on the provided parameters and returns (h windows.Handle, timeoutMilliSeconds uint32).


```go
func UpdatePreShutdownInfo((h windows.Handle, timeoutMilliSeconds uint32)) (h windows.Handle, timeoutMilliSeconds uint32)
```


**Тип ответа:** h


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


**Тип ответа:** timeoutMilliSeconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/windows/service/service.go:75`



---


[function] name: initService file: pkg/windows/service/service.go:107 returns_error: нет description: initService will try to run the daemon as a Windows
service, with an option to indicate if the service will accept the p


### initService (pkg/windows/service/service.go:107)


initService will try to run the daemon as a Windows
service, with an option to indicate if the service will accept the preshutdown event.


```go
func initService((serviceName string, acceptPreshutdown bool)) (serviceName string, acceptPreshutdown bool)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** acceptPreshutdown


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/windows/service/service.go:107`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_volume.md)

- [Следующая директория](plugin_pkg.md)


---

