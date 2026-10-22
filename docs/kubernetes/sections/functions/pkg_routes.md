---
title: "Функции: pkg/routes"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/routes
---


# Функции: pkg/routes


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_registry.md)

- [Следующая директория](pkg_scheduler.md)


---


## Меню по файлам


- 📄 [pkg/routes/logs.go](#pkgrouteslogsgo)

- 📄 [pkg/routes/openidmetadata.go](#pkgroutesopenidmetadatago)


---


## pkg/routes/logs.go


📄 Исходный файл: `pkg/routes/logs.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Install](#install-pkgrouteslogsgo31) `:31`

- 🔗 [logFileHandler](#logfilehandler-pkgrouteslogsgo43) `:43`

- 🔗 [logFileListHandler](#logfilelisthandler-pkgrouteslogsgo55) `:55`

- 🔗 [logFileNameIsTooLong](#logfilenameistoolong-pkgrouteslogsgo62) `:62`


</details>


[function] name: Install file: pkg/routes/logs.go:31 returns_error: нет description: Install func registers the logs handler.


### Install (pkg/routes/logs.go:31)


Install func registers the logs handler.


```go
func (l Logs) Install((c *restful.Container)) (c *restful.Container)
```


**Тип запроса:** restful.Container


```json
{
  "ID": {},
  "Name": "string",
  "Image": "string",
  "ImageID": "string",
  "ImageRef": "string",
  "ImageRuntimeHandler": "string",
  "Hash": 0,
  "State": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


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


**Тип ответа:** restful.Container


```json
{
  "ID": {},
  "Name": "string",
  "Image": "string",
  "ImageID": "string",
  "ImageRef": "string",
  "ImageRuntimeHandler": "string",
  "Hash": 0,
  "State": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/routes/logs.go:31`



---


[function] name: logFileHandler file: pkg/routes/logs.go:43 returns_error: нет description: —


### logFileHandler (pkg/routes/logs.go:43)


logFileHandler is a function that performs operations based on the provided parameters and returns (req *restful.Request, resp *restful.Response).


```go
func logFileHandler((req *restful.Request, resp *restful.Response)) (req *restful.Request, resp *restful.Response)
```


**Тип запроса:** restful.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип запроса:** restful.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Тип ответа:** req


```json
{
  "RequestHeaders": {},
  "RequestVerb": "string",
  "RequestURL": "string",
  "ResponseStatus": "string",
  "ResponseHeaders": {},
  "ResponseErr": {},
  "muTrace": {},
  "DNSLookup": {},
  "Dialing": {},
  "GetConnection": {},
  "TLSHandshake": {},
  "ServerProcessing": {},
  "ConnectionReused": false,
  "Duration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


**Тип ответа:** restful.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** resp


```json
{
  "w": {},
  "ctx": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/peerproxy/peerproxy_handler.go`


**Тип ответа:** restful.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


📍 *Расположение:* `pkg/routes/logs.go:43`



---


[function] name: logFileListHandler file: pkg/routes/logs.go:55 returns_error: нет description: —


### logFileListHandler (pkg/routes/logs.go:55)


logFileListHandler is a function that performs operations based on the provided parameters and returns (req *restful.Request, resp *restful.Response).


```go
func logFileListHandler((req *restful.Request, resp *restful.Response)) (req *restful.Request, resp *restful.Response)
```


**Тип запроса:** restful.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип запроса:** restful.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Тип ответа:** req


```json
{
  "RequestHeaders": {},
  "RequestVerb": "string",
  "RequestURL": "string",
  "ResponseStatus": "string",
  "ResponseHeaders": {},
  "ResponseErr": {},
  "muTrace": {},
  "DNSLookup": {},
  "Dialing": {},
  "GetConnection": {},
  "TLSHandshake": {},
  "ServerProcessing": {},
  "ConnectionReused": false,
  "Duration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


**Тип ответа:** restful.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** resp


```json
{
  "w": {},
  "ctx": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/peerproxy/peerproxy_handler.go`


**Тип ответа:** restful.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


📍 *Расположение:* `pkg/routes/logs.go:55`



---


[function] name: logFileNameIsTooLong file: pkg/routes/logs.go:62 returns_error: нет description: logFileNameIsTooLong checks filename length, returns true if it's longer than 255.
cause http.ServeFile returns default 


### logFileNameIsTooLong (pkg/routes/logs.go:62)


logFileNameIsTooLong checks filename length, returns true if it's longer than 255.
cause http.ServeFile returns default error code 500 except for NotExist and Forbidden, but we need to separate the real 500 from oversize filename here.


```go
func logFileNameIsTooLong((filePath string)) (filePath string)
```


**Тип ответа:** filePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/routes/logs.go:62`




## pkg/routes/openidmetadata.go


📄 Исходный файл: `pkg/routes/openidmetadata.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Install](#install-pkgroutesopenidmetadatago58) `:58`

- 🔗 [NewOpenIDMetadataServer](#newopenidmetadataserver-pkgroutesopenidmetadatago53) `:53`

- 🔗 [fromStandard](#fromstandard-pkgroutesopenidmetadatago89) `:89`

- 🔗 [serveConfiguration](#serveconfiguration-pkgroutesopenidmetadatago95) `:95`

- 🔗 [serveKeys](#servekeys-pkgroutesopenidmetadatago105) `:105`


</details>


[function] name: Install file: pkg/routes/openidmetadata.go:58 returns_error: нет description: Install adds this server to the request router c.


### Install (pkg/routes/openidmetadata.go:58)


Install adds this server to the request router c.


```go
func (s *OpenIDMetadataServer) Install((c *restful.Container)) (c *restful.Container)
```


**Тип запроса:** restful.Container


```json
{
  "ID": {},
  "Name": "string",
  "Image": "string",
  "ImageID": "string",
  "ImageRef": "string",
  "ImageRuntimeHandler": "string",
  "Hash": 0,
  "State": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


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


**Тип ответа:** restful.Container


```json
{
  "ID": {},
  "Name": "string",
  "Image": "string",
  "ImageID": "string",
  "ImageRef": "string",
  "ImageRuntimeHandler": "string",
  "Hash": 0,
  "State": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/routes/openidmetadata.go:58`



---


[function] name: NewOpenIDMetadataServer file: pkg/routes/openidmetadata.go:53 returns_error: нет description: NewOpenIDMetadataServer creates a new OpenIDMetadataServer.
The issuer is the OIDC issuer; keys are the keys that may be


### NewOpenIDMetadataServer (pkg/routes/openidmetadata.go:53)


NewOpenIDMetadataServer creates a new OpenIDMetadataServer.
The issuer is the OIDC issuer; keys are the keys that may be used to sign
KSA tokens.


```go
func NewOpenIDMetadataServer((provider serviceaccount.OpenIDMetadataProvider)) (provider serviceaccount.OpenIDMetadataProvider)
```


**Тип ответа:** provider


```json
{
  "name": "string",
  "impl": null
}
```


*Определено в:* `pkg/credentialprovider/plugin/plugins.go`


**Тип ответа:** serviceaccount.OpenIDMetadataProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/routes/openidmetadata.go:53`



---


[function] name: fromStandard file: pkg/routes/openidmetadata.go:89 returns_error: нет description: fromStandard provides compatibility between the standard (net/http) handler signature and the restful signature.


### fromStandard (pkg/routes/openidmetadata.go:89)


fromStandard provides compatibility between the standard (net/http) handler signature and the restful signature.


```go
func fromStandard((h http.HandlerFunc)) (h http.HandlerFunc)
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


**Тип ответа:** http.HandlerFunc


```json
{
  "AddFunc": {},
  "UpdateFunc": {},
  "DeleteFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/controller.go`


📍 *Расположение:* `pkg/routes/openidmetadata.go:89`



---


[function] name: serveConfiguration file: pkg/routes/openidmetadata.go:95 returns_error: нет description: —


### serveConfiguration (pkg/routes/openidmetadata.go:95)


serveConfiguration is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, req *http.Request).


```go
func (s *OpenIDMetadataServer) serveConfiguration((w http.ResponseWriter, req *http.Request)) (w http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


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


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** req


```json
{
  "RequestHeaders": {},
  "RequestVerb": "string",
  "RequestURL": "string",
  "ResponseStatus": "string",
  "ResponseHeaders": {},
  "ResponseErr": {},
  "muTrace": {},
  "DNSLookup": {},
  "Dialing": {},
  "GetConnection": {},
  "TLSHandshake": {},
  "ServerProcessing": {},
  "ConnectionReused": false,
  "Duration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `pkg/routes/openidmetadata.go:95`



---


[function] name: serveKeys file: pkg/routes/openidmetadata.go:105 returns_error: нет description: —


### serveKeys (pkg/routes/openidmetadata.go:105)


serveKeys is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, req *http.Request).


```go
func (s *OpenIDMetadataServer) serveKeys((w http.ResponseWriter, req *http.Request)) (w http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


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


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** req


```json
{
  "RequestHeaders": {},
  "RequestVerb": "string",
  "RequestURL": "string",
  "ResponseStatus": "string",
  "ResponseHeaders": {},
  "ResponseErr": {},
  "muTrace": {},
  "DNSLookup": {},
  "Dialing": {},
  "GetConnection": {},
  "TLSHandshake": {},
  "ServerProcessing": {},
  "ConnectionReused": false,
  "Duration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `pkg/routes/openidmetadata.go:105`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_registry.md)

- [Следующая директория](pkg_scheduler.md)


---

