---
title: "Функции: pkg/probe"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/probe
---


# Функции: pkg/probe


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_printers.md)

- [Следующая директория](pkg_proxy.md)


---


## Меню по файлам


- 📄 [pkg/probe/dialer_others.go](#pkgprobedialer_othersgo)

- 📄 [pkg/probe/dialer_windows.go](#pkgprobedialer_windowsgo)

- 📄 [pkg/probe/exec/exec.go](#pkgprobeexecexecgo)

- 📄 [pkg/probe/grpc/grpc.go](#pkgprobegrpcgrpcgo)

- 📄 [pkg/probe/http/http.go](#pkgprobehttphttpgo)

- 📄 [pkg/probe/http/request.go](#pkgprobehttprequestgo)

- 📄 [pkg/probe/tcp/tcp.go](#pkgprobetcptcpgo)

- 📄 [pkg/probe/util.go](#pkgprobeutilgo)


---


## pkg/probe/dialer_others.go


📄 Исходный файл: `pkg/probe/dialer_others.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ProbeDialer](#probedialer-pkgprobedialer_othersgo32) `:32`


</details>


[function] name: ProbeDialer file: pkg/probe/dialer_others.go:32 returns_error: нет description: ProbeDialer returns a dialer optimized for probes to avoid lingering sockets on TIME-WAIT state.
The dialer reduces the 


### ProbeDialer (pkg/probe/dialer_others.go:32)


ProbeDialer returns a dialer optimized for probes to avoid lingering sockets on TIME-WAIT state.
The dialer reduces the TIME-WAIT period to 1 seconds instead of the OS default of 60 seconds.
Using 1 second instead of 0 because SO_LINGER socket option to 0 causes pending data to be
discarded and the connection to be aborted with an RST rather than for the pending data to be
transmitted and the connection closed cleanly with a FIN.
Ref: https://issues.k8s.io/89898


```go
func ProbeDialer(()) ()
```


📍 *Расположение:* `pkg/probe/dialer_others.go:32`




## pkg/probe/dialer_windows.go


📄 Исходный файл: `pkg/probe/dialer_windows.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ProbeDialer](#probedialer-pkgprobedialer_windowsgo32) `:32`


</details>


[function] name: ProbeDialer file: pkg/probe/dialer_windows.go:32 returns_error: нет description: ProbeDialer returns a dialer optimized for probes to avoid lingering sockets on TIME-WAIT state.
The dialer reduces the 


### ProbeDialer (pkg/probe/dialer_windows.go:32)


ProbeDialer returns a dialer optimized for probes to avoid lingering sockets on TIME-WAIT state.
The dialer reduces the TIME-WAIT period to 1 seconds instead of the OS default of 60 seconds.
Using 1 second instead of 0 because SO_LINGER socket option to 0 causes pending data to be
discarded and the connection to be aborted with an RST rather than for the pending data to be
transmitted and the connection closed cleanly with a FIN.
Ref: https://issues.k8s.io/89898


```go
func ProbeDialer(()) ()
```


📍 *Расположение:* `pkg/probe/dialer_windows.go:32`




## pkg/probe/exec/exec.go


📄 Исходный файл: `pkg/probe/exec/exec.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [New](#new-pkgprobeexecexecgo36) `:36`

- 🔗 [Probe](#probe-pkgprobeexecexecgo50) `:50`


</details>


[function] name: New file: pkg/probe/exec/exec.go:36 returns_error: нет description: New creates a Prober.


### New (pkg/probe/exec/exec.go:36)


New creates a Prober.


```go
func New(()) ()
```


📍 *Расположение:* `pkg/probe/exec/exec.go:36`



---


[function] name: Probe file: pkg/probe/exec/exec.go:50 returns_error: да description: Probe executes a command to check the liveness/readiness of container
from executing a command. Returns the Result statu


### Probe (pkg/probe/exec/exec.go:50)


Probe executes a command to check the liveness/readiness of container
from executing a command. Returns the Result status, command output, and
errors if any.


```go
func (pr execProber) Probe((probe.Result, string, error)) (probe.Result, string, error)
```


**Тип ответа:** probe.Result


```json
{
  "Host": "string",
  "Cmd": "string",
  "Stdout": "string",
  "Stderr": "string",
  "Code": 0
}
```


*Определено в:* `test/e2e/storage/utils/host_exec.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `probe.Result`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/exec/exec.go:50`




## pkg/probe/grpc/grpc.go


📄 Исходный файл: `pkg/probe/grpc/grpc.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [New](#new-pkgprobegrpcgrpcgo45) `:45`

- 🔗 [Probe](#probe-pkgprobegrpcgrpcgo53) `:53`


</details>


[function] name: New file: pkg/probe/grpc/grpc.go:45 returns_error: нет description: New Prober for execute grpc probe


### New (pkg/probe/grpc/grpc.go:45)


New Prober for execute grpc probe


```go
func New(()) ()
```


📍 *Расположение:* `pkg/probe/grpc/grpc.go:45`



---


[function] name: Probe file: pkg/probe/grpc/grpc.go:53 returns_error: да description: Probe executes a grpc call to check the liveness/readiness/startup of container.
Returns the Result status, command outp


### Probe (pkg/probe/grpc/grpc.go:53)


Probe executes a grpc call to check the liveness/readiness/startup of container.
Returns the Result status, command output, and errors if any.
Any failure is considered as a probe failure to mimic grpc_health_probe tool behavior.
err is always nil


```go
func (p grpcProber) Probe((probe.Result, string, error)) (probe.Result, string, error)
```


**Тип ответа:** probe.Result


```json
{
  "Host": "string",
  "Cmd": "string",
  "Stdout": "string",
  "Stderr": "string",
  "Code": 0
}
```


*Определено в:* `test/e2e/storage/utils/host_exec.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `probe.Result`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/grpc/grpc.go:53`




## pkg/probe/http/http.go


📄 Исходный файл: `pkg/probe/http/http.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [DoHTTPProbe](#dohttpprobe-pkgprobehttphttpgo93) `:93`

- 🔗 [New](#new-pkgprobehttphttpgo40) `:40`

- 🔗 [NewWithTLSConfig](#newwithtlsconfig-pkgprobehttphttpgo48) `:48`

- 🔗 [Probe](#probe-pkgprobehttphttpgo75) `:75`

- 🔗 [RedirectChecker](#redirectchecker-pkgprobehttphttpgo126) `:126`


</details>


[function] name: DoHTTPProbe file: pkg/probe/http/http.go:93 returns_error: да description: DoHTTPProbe checks if a GET request to the url succeeds.
If the HTTP response code is successful (i.e. 400 > code >= 200


### DoHTTPProbe (pkg/probe/http/http.go:93)


DoHTTPProbe checks if a GET request to the url succeeds.
If the HTTP response code is successful (i.e. 400 > code >= 200), it returns Success.
If the HTTP response code is unsuccessful or HTTP communication fails, it returns Failure.
This is exported because some other packages may want to do direct HTTP probes.


```go
func DoHTTPProbe((probe.Result, string, error)) (probe.Result, string, error)
```


**Тип ответа:** probe.Result


```json
{
  "Host": "string",
  "Cmd": "string",
  "Stdout": "string",
  "Stderr": "string",
  "Code": 0
}
```


*Определено в:* `test/e2e/storage/utils/host_exec.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `probe.Result`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/http/http.go:93`



---


[function] name: New file: pkg/probe/http/http.go:40 returns_error: нет description: New creates Prober that will skip TLS verification while probing.
followNonLocalRedirects configures whether the prober 


### New (pkg/probe/http/http.go:40)


New creates Prober that will skip TLS verification while probing.
followNonLocalRedirects configures whether the prober should follow redirects to a different hostname.
If disabled, redirects to other hosts will trigger a warning result.


```go
func New((followNonLocalRedirects bool)) (followNonLocalRedirects bool)
```


**Тип ответа:** followNonLocalRedirects


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/probe/http/http.go:40`



---


[function] name: NewWithTLSConfig file: pkg/probe/http/http.go:48 returns_error: нет description: NewWithTLSConfig takes tls config as parameter.
followNonLocalRedirects configures whether the prober should follow redi


### NewWithTLSConfig (pkg/probe/http/http.go:48)


NewWithTLSConfig takes tls config as parameter.
followNonLocalRedirects configures whether the prober should follow redirects to a different hostname.
If disabled, redirects to other hosts will trigger a warning result.


```go
func NewWithTLSConfig((config *tls.Config, followNonLocalRedirects bool)) (config *tls.Config, followNonLocalRedirects bool)
```


**Тип запроса:** tls.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** tls.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** followNonLocalRedirects


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/probe/http/http.go:48`



---


[function] name: Probe file: pkg/probe/http/http.go:75 returns_error: да description: Probe returns a ProbeRunner capable of running an HTTP check.


### Probe (pkg/probe/http/http.go:75)


Probe returns a ProbeRunner capable of running an HTTP check.


```go
func (pr httpProber) Probe((probe.Result, string, error)) (probe.Result, string, error)
```


**Тип ответа:** probe.Result


```json
{
  "Host": "string",
  "Cmd": "string",
  "Stdout": "string",
  "Stderr": "string",
  "Code": 0
}
```


*Определено в:* `test/e2e/storage/utils/host_exec.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `probe.Result`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/http/http.go:75`



---


[function] name: RedirectChecker file: pkg/probe/http/http.go:126 returns_error: нет description: RedirectChecker returns a function that can be used to check HTTP redirects.


### RedirectChecker (pkg/probe/http/http.go:126)


RedirectChecker returns a function that can be used to check HTTP redirects.


```go
func RedirectChecker((followNonLocalRedirects bool)) (followNonLocalRedirects bool)
```


**Тип ответа:** followNonLocalRedirects


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/probe/http/http.go:126`




## pkg/probe/http/request.go


📄 Исходный файл: `pkg/probe/http/request.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [NewProbeRequest](#newproberequest-pkgprobehttprequestgo34) `:34`

- 🔗 [NewRequestForHTTPGetAction](#newrequestforhttpgetaction-pkgprobehttprequestgo40) `:40`

- 🔗 [formatURL](#formaturl-pkgprobehttprequestgo95) `:95`

- 🔗 [newProbeRequest](#newproberequest-pkgprobehttprequestgo63) `:63`

- 🔗 [userAgent](#useragent-pkgprobehttprequestgo89) `:89`

- 🔗 [v1HeaderToHTTPHeader](#v1headertohttpheader-pkgprobehttprequestgo113) `:113`


</details>


[function] name: NewProbeRequest file: pkg/probe/http/request.go:34 returns_error: да description: NewProbeRequest returns an http.Request suitable for use as a request for a
probe.


### NewProbeRequest (pkg/probe/http/request.go:34)


NewProbeRequest returns an http.Request suitable for use as a request for a
probe.


```go
func NewProbeRequest((*http.Request, error)) (*http.Request, error)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Request`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/http/request.go:34`



---


[function] name: NewRequestForHTTPGetAction file: pkg/probe/http/request.go:40 returns_error: да description: NewRequestForHTTPGetAction returns an http.Request derived from httpGet.
When httpGet.Host is empty, podIP will be used 


### NewRequestForHTTPGetAction (pkg/probe/http/request.go:40)


NewRequestForHTTPGetAction returns an http.Request derived from httpGet.
When httpGet.Host is empty, podIP will be used instead.


```go
func NewRequestForHTTPGetAction((*http.Request, error)) (*http.Request, error)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Request`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/http/request.go:40`



---


[function] name: formatURL file: pkg/probe/http/request.go:95 returns_error: нет description: formatURL formats a URL from args.  For testability.


### formatURL (pkg/probe/http/request.go:95)


formatURL formats a URL from args.  For testability.


```go
func formatURL((scheme string, host string, port int, path string)) (scheme string, host string, port int, path string)
```


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


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


📍 *Расположение:* `pkg/probe/http/request.go:95`



---


[function] name: newProbeRequest file: pkg/probe/http/request.go:63 returns_error: да description: —


### newProbeRequest (pkg/probe/http/request.go:63)


newProbeRequest is a function that performs operations based on the provided parameters and may return an error.


```go
func newProbeRequest((*http.Request, error)) (*http.Request, error)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Request`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/http/request.go:63`



---


[function] name: userAgent file: pkg/probe/http/request.go:89 returns_error: нет description: —


### userAgent (pkg/probe/http/request.go:89)


userAgent is a function that performs operations based on the provided parameters and returns (purpose string).


```go
func userAgent((purpose string)) (purpose string)
```


**Тип ответа:** purpose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/probe/http/request.go:89`



---


[function] name: v1HeaderToHTTPHeader file: pkg/probe/http/request.go:113 returns_error: нет description: v1HeaderToHTTPHeader takes a list of HTTPHeader <name, value> string pairs
and returns a populated string->[]string http


### v1HeaderToHTTPHeader (pkg/probe/http/request.go:113)


v1HeaderToHTTPHeader takes a list of HTTPHeader <name, value> string pairs
and returns a populated string->[]string http.Header map.


```go
func v1HeaderToHTTPHeader((headerList []v1.HTTPHeader)) (headerList []v1.HTTPHeader)
```


**Тип ответа:** headerList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.HTTPHeader


```json
{
  "Name": "string",
  "Value": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/probe/http/request.go:113`




## pkg/probe/tcp/tcp.go


📄 Исходный файл: `pkg/probe/tcp/tcp.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DoTCPProbe](#dotcpprobe-pkgprobetcptcpgo50) `:50`

- 🔗 [New](#new-pkgprobetcptcpgo30) `:30`

- 🔗 [Probe](#probe-pkgprobetcptcpgo42) `:42`


</details>


[function] name: DoTCPProbe file: pkg/probe/tcp/tcp.go:50 returns_error: да description: DoTCPProbe checks that a TCP socket to the address can be opened.
If the socket can be opened, it returns Success
If the


### DoTCPProbe (pkg/probe/tcp/tcp.go:50)


DoTCPProbe checks that a TCP socket to the address can be opened.
If the socket can be opened, it returns Success
If the socket fails to open, it returns Failure.
This is exported because some other packages may want to do direct TCP probes.


```go
func DoTCPProbe((probe.Result, string, error)) (probe.Result, string, error)
```


**Тип ответа:** probe.Result


```json
{
  "Host": "string",
  "Cmd": "string",
  "Stdout": "string",
  "Stderr": "string",
  "Code": 0
}
```


*Определено в:* `test/e2e/storage/utils/host_exec.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `probe.Result`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/tcp/tcp.go:50`



---


[function] name: New file: pkg/probe/tcp/tcp.go:30 returns_error: нет description: New creates Prober.


### New (pkg/probe/tcp/tcp.go:30)


New creates Prober.


```go
func New(()) ()
```


📍 *Расположение:* `pkg/probe/tcp/tcp.go:30`



---


[function] name: Probe file: pkg/probe/tcp/tcp.go:42 returns_error: да description: Probe checks that a TCP connection to the address can be opened.


### Probe (pkg/probe/tcp/tcp.go:42)


Probe checks that a TCP connection to the address can be opened.


```go
func (pr tcpProber) Probe((probe.Result, string, error)) (probe.Result, string, error)
```


**Тип ответа:** probe.Result


```json
{
  "Host": "string",
  "Cmd": "string",
  "Stdout": "string",
  "Stderr": "string",
  "Code": 0
}
```


*Определено в:* `test/e2e/storage/utils/host_exec.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `probe.Result`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/tcp/tcp.go:42`




## pkg/probe/util.go


📄 Исходный файл: `pkg/probe/util.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ResolveContainerPort](#resolvecontainerport-pkgprobeutilgo27) `:27`

- 🔗 [findPortByName](#findportbyname-pkgprobeutilgo50) `:50`


</details>


[function] name: ResolveContainerPort file: pkg/probe/util.go:27 returns_error: да description: —


### ResolveContainerPort (pkg/probe/util.go:27)


ResolveContainerPort is a function that performs operations based on the provided parameters and may return an error.


```go
func ResolveContainerPort((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/util.go:27`



---


[function] name: findPortByName file: pkg/probe/util.go:50 returns_error: да description: findPortByName is a helper function to look up a port in a container by name.


### findPortByName (pkg/probe/util.go:50)


findPortByName is a helper function to look up a port in a container by name.


```go
func findPortByName((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/probe/util.go:50`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_printers.md)

- [Следующая директория](pkg_proxy.md)


---

