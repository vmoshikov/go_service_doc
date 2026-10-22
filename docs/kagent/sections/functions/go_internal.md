---
title: "Функции: go/internal"
type: functions
repo: kagent
language: ru
chunk_boundary: h3
group: go/internal
---


# Функции: go/internal


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_hack.md)

- [Следующая директория](go_pkg.md)


---


## Меню по файлам


- 📄 [go/internal/a2a/a2a_handler_mux.go](#gointernala2aa2a_handler_muxgo)

- 📄 [go/internal/a2a/a2a_registrar.go](#gointernala2aa2a_registrargo)

- 📄 [go/internal/a2a/a2a_utils.go](#gointernala2aa2a_utilsgo)

- 📄 [go/internal/a2a/manager.go](#gointernala2amanagergo)

- 📄 [go/internal/controller/agent_controller.go](#gointernalcontrolleragent_controllergo)

- 📄 [go/internal/controller/mcp_server_tool_controller.go](#gointernalcontrollermcp_server_tool_controllergo)

- 📄 [go/internal/controller/modelconfig_controller.go](#gointernalcontrollermodelconfig_controllergo)

- 📄 [go/internal/controller/modelproviderconfig_controller.go](#gointernalcontrollermodelproviderconfig_controllergo)

- 📄 [go/internal/controller/predicates/discovery_disabled.go](#gointernalcontrollerpredicatesdiscovery_disabledgo)

- 📄 [go/internal/controller/provider/discoverer.go](#gointernalcontrollerproviderdiscoverergo)

- 📄 [go/internal/controller/reconciler/reconciler.go](#gointernalcontrollerreconcilerreconcilergo)

- 📄 [go/internal/controller/reconciler/status/mcp_server.go](#gointernalcontrollerreconcilerstatusmcp_servergo)

- 📄 [go/internal/controller/reconciler/utils/reconciler_utils.go](#gointernalcontrollerreconcilerutilsreconciler_utilsgo)

- 📄 [go/internal/controller/remote_mcp_server_controller.go](#gointernalcontrollerremote_mcp_server_controllergo)

- 📄 [go/internal/controller/service_controller.go](#gointernalcontrollerservice_controllergo)

- 📄 [go/internal/controller/translator/agent/adk_api_translator.go](#gointernalcontrollertranslatoragentadk_api_translatorgo)

- 📄 [go/internal/controller/translator/agent/conversion.go](#gointernalcontrollertranslatoragentconversiongo)

- 📄 [go/internal/controller/translator/agent/deployments.go](#gointernalcontrollertranslatoragentdeploymentsgo)

- 📄 [go/internal/controller/translator/agent/template.go](#gointernalcontrollertranslatoragenttemplatego)

- 📄 [go/internal/controller/translator/agent/utils.go](#gointernalcontrollertranslatoragentutilsgo)

- 📄 [go/internal/controller/translator/mutate.go](#gointernalcontrollertranslatormutatego)

- 📄 [go/internal/database/client.go](#gointernaldatabaseclientgo)

- 📄 [go/internal/database/fake/client.go](#gointernaldatabasefakeclientgo)

- 📄 [go/internal/database/manager.go](#gointernaldatabasemanagergo)

- 📄 [go/internal/database/service.go](#gointernaldatabaseservicego)

- 📄 [go/internal/goruntime/cpu.go](#gointernalgoruntimecpugo)

- 📄 [go/internal/httpserver/auth/authn.go](#gointernalhttpserverauthauthngo)

- 📄 [go/internal/httpserver/auth/authz.go](#gointernalhttpserverauthauthzgo)

- 📄 [go/internal/httpserver/errors/errors.go](#gointernalhttpservererrorserrorsgo)

- 📄 [go/internal/httpserver/handlers/agents.go](#gointernalhttpserverhandlersagentsgo)

- 📄 [go/internal/httpserver/handlers/checkpoints.go](#gointernalhttpserverhandlerscheckpointsgo)

- 📄 [go/internal/httpserver/handlers/crewai.go](#gointernalhttpserverhandlerscrewaigo)

- 📄 [go/internal/httpserver/handlers/feedback.go](#gointernalhttpserverhandlersfeedbackgo)

- 📄 [go/internal/httpserver/handlers/handlers.go](#gointernalhttpserverhandlershandlersgo)

- 📄 [go/internal/httpserver/handlers/health.go](#gointernalhttpserverhandlershealthgo)

- 📄 [go/internal/httpserver/handlers/helpers.go](#gointernalhttpserverhandlershelpersgo)

- 📄 [go/internal/httpserver/handlers/memory.go](#gointernalhttpserverhandlersmemorygo)

- 📄 [go/internal/httpserver/handlers/modelconfig.go](#gointernalhttpserverhandlersmodelconfiggo)

- 📄 [go/internal/httpserver/handlers/modelproviderconfig.go](#gointernalhttpserverhandlersmodelproviderconfiggo)

- 📄 [go/internal/httpserver/handlers/models.go](#gointernalhttpserverhandlersmodelsgo)

- 📄 [go/internal/httpserver/handlers/namespaces.go](#gointernalhttpserverhandlersnamespacesgo)

- 📄 [go/internal/httpserver/handlers/sessions.go](#gointernalhttpserverhandlerssessionsgo)

- 📄 [go/internal/httpserver/handlers/tasks.go](#gointernalhttpserverhandlerstasksgo)

- 📄 [go/internal/httpserver/handlers/tools.go](#gointernalhttpserverhandlerstoolsgo)

- 📄 [go/internal/httpserver/handlers/toolservers.go](#gointernalhttpserverhandlerstoolserversgo)

- 📄 [go/internal/httpserver/handlers/toolservertypes.go](#gointernalhttpserverhandlerstoolservertypesgo)

- 📄 [go/internal/httpserver/handlers/utils.go](#gointernalhttpserverhandlersutilsgo)

- 📄 [go/internal/httpserver/middleware.go](#gointernalhttpservermiddlewarego)

- 📄 [go/internal/httpserver/middleware_error.go](#gointernalhttpservermiddleware_errorgo)

- 📄 [go/internal/httpserver/server.go](#gointernalhttpserverservergo)

- 📄 [go/internal/mcp/mcp_handler.go](#gointernalmcpmcp_handlergo)

- 📄 [go/internal/metrics/version.go](#gointernalmetricsversiongo)

- 📄 [go/internal/utils/client_wrapper.go](#gointernalutilsclient_wrappergo)

- 📄 [go/internal/utils/common.go](#gointernalutilscommongo)

- 📄 [go/internal/utils/config_map.go](#gointernalutilsconfig_mapgo)

- 📄 [go/internal/utils/iter.go](#gointernalutilsitergo)

- 📄 [go/internal/utils/secret.go](#gointernalutilssecretgo)

- 📄 [go/internal/version/version.go](#gointernalversionversiongo)


---


## go/internal/a2a/a2a_handler_mux.go


📄 Исходный файл: `go/internal/a2a/a2a_handler_mux.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NewA2AHttpMux](#newa2ahttpmux-gointernala2aa2a_handler_muxgo38) `:38`

- 🔗 [RemoveAgentHandler](#removeagenthandler-gointernala2aa2a_handler_muxgo64) `:64`

- 🔗 [ServeHTTP](#servehttp-gointernala2aa2a_handler_muxgo79) `:79`

- 🔗 [SetAgentHandler](#setagenthandler-gointernala2aa2a_handler_muxgo46) `:46`

- 🔗 [getHandler](#gethandler-gointernala2aa2a_handler_muxgo72) `:72`


</details>


[function] name: NewA2AHttpMux file: go/internal/a2a/a2a_handler_mux.go:38 returns_error: нет description: —


### NewA2AHttpMux (go/internal/a2a/a2a_handler_mux.go:38)


NewA2AHttpMux is a function that performs operations based on the provided parameters and returns (pathPrefix string, authenticator auth.AuthProvider).


```go
func NewA2AHttpMux((pathPrefix string, authenticator auth.AuthProvider)) (pathPrefix string, authenticator auth.AuthProvider)
```


**Тип ответа:** pathPrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authenticator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.AuthProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/a2a/a2a_handler_mux.go:38`



---


[function] name: RemoveAgentHandler file: go/internal/a2a/a2a_handler_mux.go:64 returns_error: нет description: —


### RemoveAgentHandler (go/internal/a2a/a2a_handler_mux.go:64)


RemoveAgentHandler is a method that deletes data based on the provided parameters and returns (
	agentRef string,
).


```go
func (a *handlerMux) RemoveAgentHandler((
	agentRef string,
)) (
	agentRef string,
)
```


**Тип ответа:** agentRef


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/a2a/a2a_handler_mux.go:64`



---


[function] name: ServeHTTP file: go/internal/a2a/a2a_handler_mux.go:79 returns_error: нет description: —


### ServeHTTP (go/internal/a2a/a2a_handler_mux.go:79)


ServeHTTP is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (a *handlerMux) ServeHTTP((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/a2a/a2a_handler_mux.go:79`



---


[function] name: SetAgentHandler file: go/internal/a2a/a2a_handler_mux.go:46 returns_error: нет description: —


### SetAgentHandler (go/internal/a2a/a2a_handler_mux.go:46)


SetAgentHandler is a method that updates data based on the provided parameters and returns (
	agentRef string,
	client *client.A2AClient,
	card server.AgentCard,
).


```go
func (a *handlerMux) SetAgentHandler((
	agentRef string,
	client *client.A2AClient,
	card server.AgentCard,
)) (
	agentRef string,
	client *client.A2AClient,
	card server.AgentCard,
)
```


**Тип запроса:** client.A2AClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agentRef


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.A2AClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** card


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** server.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/a2a/a2a_handler_mux.go:46`



---


[function] name: getHandler file: go/internal/a2a/a2a_handler_mux.go:72 returns_error: нет description: —


### getHandler (go/internal/a2a/a2a_handler_mux.go:72)


getHandler is a method that performs operations based on the provided parameters and returns (http.Handler, bool).


```go
func (a *handlerMux) getHandler((http.Handler, bool)) (http.Handler, bool)
```


**Тип ответа:** http.Handler


```json
{
  "kubeClient": {},
  "a2aBaseURL": "string",
  "authenticator": {},
  "httpHandler": null,
  "server": null,
  "a2aClients": {}
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


📍 *Расположение:* `go/internal/a2a/a2a_handler_mux.go:72`




## go/internal/a2a/a2a_registrar.go


📄 Исходный файл: `go/internal/a2a/a2a_registrar.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NeedLeaderElection](#needleaderelection-gointernala2aa2a_registrargo63) `:63`

- 🔗 [NewA2ARegistrar](#newa2aregistrar-gointernala2aa2a_registrargo37) `:37`

- 🔗 [Start](#start-gointernala2aa2a_registrargo67) `:67`

- 🔗 [debugOpt](#debugopt-gointernala2aa2a_registrargo154) `:154`

- 🔗 [upsertAgentHandler](#upsertagenthandler-gointernala2aa2a_registrargo123) `:123`


</details>


[function] name: NeedLeaderElection file: go/internal/a2a/a2a_registrar.go:63 returns_error: нет description: —


### NeedLeaderElection (go/internal/a2a/a2a_registrar.go:63)


NeedLeaderElection is a method that performs operations based on the provided parameters and returns ().


```go
func (a *A2ARegistrar) NeedLeaderElection(()) ()
```


📍 *Расположение:* `go/internal/a2a/a2a_registrar.go:63`



---


[function] name: NewA2ARegistrar file: go/internal/a2a/a2a_registrar.go:37 returns_error: нет description: —


### NewA2ARegistrar (go/internal/a2a/a2a_registrar.go:37)


NewA2ARegistrar is a function that performs operations based on the provided parameters and returns (
	cache crcache.Cache,
	translator agent_translator.AdkApiTranslator,
	mux A2AHandlerMux,
	a2aBaseUrl string,
	authenticator auth.AuthProvider,
	streamingMaxBuf int,
	streamingInitialBuf int,
	streamingTimeout time.Duration,
).


```go
func NewA2ARegistrar((
	cache crcache.Cache,
	translator agent_translator.AdkApiTranslator,
	mux A2AHandlerMux,
	a2aBaseUrl string,
	authenticator auth.AuthProvider,
	streamingMaxBuf int,
	streamingInitialBuf int,
	streamingTimeout time.Duration,
)) (
	cache crcache.Cache,
	translator agent_translator.AdkApiTranslator,
	mux A2AHandlerMux,
	a2aBaseUrl string,
	authenticator auth.AuthProvider,
	streamingMaxBuf int,
	streamingInitialBuf int,
	streamingTimeout time.Duration,
)
```


**Тип ответа:** cache


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** crcache.Cache


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** translator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agent_translator.AdkApiTranslator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** A2AHandlerMux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2aBaseUrl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authenticator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.AuthProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** streamingMaxBuf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** streamingInitialBuf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** streamingTimeout


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "v": {},
  "defaultValue": {}
}
```


*Определено в:* `go/pkg/env/var.go`


📍 *Расположение:* `go/internal/a2a/a2a_registrar.go:37`



---


[function] name: Start file: go/internal/a2a/a2a_registrar.go:67 returns_error: нет description: —


### Start (go/internal/a2a/a2a_registrar.go:67)


Start is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (a *A2ARegistrar) Start((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


📍 *Расположение:* `go/internal/a2a/a2a_registrar.go:67`



---


[function] name: debugOpt file: go/internal/a2a/a2a_registrar.go:154 returns_error: нет description: —


### debugOpt (go/internal/a2a/a2a_registrar.go:154)


debugOpt is a function that performs operations based on the provided parameters and returns ().


```go
func debugOpt(()) ()
```


📍 *Расположение:* `go/internal/a2a/a2a_registrar.go:154`



---


[function] name: upsertAgentHandler file: go/internal/a2a/a2a_registrar.go:123 returns_error: нет description: —


### upsertAgentHandler (go/internal/a2a/a2a_registrar.go:123)


upsertAgentHandler is a method that performs operations based on the provided parameters and returns (ctx context.Context, agent *v1alpha2.Agent, log logr.Logger).


```go
func (a *A2ARegistrar) upsertAgentHandler((ctx context.Context, agent *v1alpha2.Agent, log logr.Logger)) (ctx context.Context, agent *v1alpha2.Agent, log logr.Logger)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** log


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/a2a/a2a_registrar.go:123`




## go/internal/a2a/a2a_utils.go


📄 Исходный файл: `go/internal/a2a/a2a_utils.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ExtractText](#extracttext-gointernala2aa2a_utilsgo10) `:10`


</details>


[function] name: ExtractText file: go/internal/a2a/a2a_utils.go:10 returns_error: нет description: ExtractText extracts the text content from a message.


### ExtractText (go/internal/a2a/a2a_utils.go:10)


ExtractText extracts the text content from a message.


```go
func ExtractText((message protocol.Message)) (message protocol.Message)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/a2a/a2a_utils.go:10`




## go/internal/a2a/manager.go


📄 Исходный файл: `go/internal/a2a/manager.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [NewPassthroughManager](#newpassthroughmanager-gointernala2amanagergo15) `:15`

- 🔗 [OnCancelTask](#oncanceltask-gointernala2amanagergo45) `:45`

- 🔗 [OnGetTask](#ongettask-gointernala2amanagergo41) `:41`

- 🔗 [OnPushNotificationGet](#onpushnotificationget-gointernala2amanagergo53) `:53`

- 🔗 [OnPushNotificationSet](#onpushnotificationset-gointernala2amanagergo49) `:49`

- 🔗 [OnResubscribe](#onresubscribe-gointernala2amanagergo57) `:57`

- 🔗 [OnSendMessage](#onsendmessage-gointernala2amanagergo21) `:21`

- 🔗 [OnSendMessageStream](#onsendmessagestream-gointernala2amanagergo31) `:31`


</details>


[function] name: NewPassthroughManager file: go/internal/a2a/manager.go:15 returns_error: нет description: —


### NewPassthroughManager (go/internal/a2a/manager.go:15)


NewPassthroughManager is a function that performs operations based on the provided parameters and returns (client *client.A2AClient).


```go
func NewPassthroughManager((client *client.A2AClient)) (client *client.A2AClient)
```


**Тип запроса:** client.A2AClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.A2AClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/a2a/manager.go:15`



---


[function] name: OnCancelTask file: go/internal/a2a/manager.go:45 returns_error: да description: —


### OnCancelTask (go/internal/a2a/manager.go:45)


OnCancelTask is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *PassthroughManager) OnCancelTask((*protocol.Task, error)) (*protocol.Task, error)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/a2a/manager.go:45`



---


[function] name: OnGetTask file: go/internal/a2a/manager.go:41 returns_error: да description: —


### OnGetTask (go/internal/a2a/manager.go:41)


OnGetTask is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *PassthroughManager) OnGetTask((*protocol.Task, error)) (*protocol.Task, error)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/a2a/manager.go:41`



---


[function] name: OnPushNotificationGet file: go/internal/a2a/manager.go:53 returns_error: да description: —


### OnPushNotificationGet (go/internal/a2a/manager.go:53)


OnPushNotificationGet is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *PassthroughManager) OnPushNotificationGet((*protocol.TaskPushNotificationConfig, error)) (*protocol.TaskPushNotificationConfig, error)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.TaskPushNotificationConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/a2a/manager.go:53`



---


[function] name: OnPushNotificationSet file: go/internal/a2a/manager.go:49 returns_error: да description: —


### OnPushNotificationSet (go/internal/a2a/manager.go:49)


OnPushNotificationSet is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *PassthroughManager) OnPushNotificationSet((*protocol.TaskPushNotificationConfig, error)) (*protocol.TaskPushNotificationConfig, error)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.TaskPushNotificationConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/a2a/manager.go:49`



---


[function] name: OnResubscribe file: go/internal/a2a/manager.go:57 returns_error: да description: —


### OnResubscribe (go/internal/a2a/manager.go:57)


OnResubscribe is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *PassthroughManager) OnResubscribe((<-chan protocol.StreamingMessageEvent, error)) (<-chan protocol.StreamingMessageEvent, error)
```


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.StreamingMessageEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `<-chan protocol.StreamingMessageEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/a2a/manager.go:57`



---


[function] name: OnSendMessage file: go/internal/a2a/manager.go:21 returns_error: да description: —


### OnSendMessage (go/internal/a2a/manager.go:21)


OnSendMessage is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *PassthroughManager) OnSendMessage((*protocol.MessageResult, error)) (*protocol.MessageResult, error)
```


**Тип запроса:** protocol.MessageResult


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.MessageResult


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.MessageResult`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/a2a/manager.go:21`



---


[function] name: OnSendMessageStream file: go/internal/a2a/manager.go:31 returns_error: да description: —


### OnSendMessageStream (go/internal/a2a/manager.go:31)


OnSendMessageStream is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *PassthroughManager) OnSendMessageStream((<-chan protocol.StreamingMessageEvent, error)) (<-chan protocol.StreamingMessageEvent, error)
```


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.StreamingMessageEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `<-chan protocol.StreamingMessageEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/a2a/manager.go:31`




## go/internal/controller/agent_controller.go


📄 Исходный файл: `go/internal/controller/agent_controller.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [Create](#create-gointernalcontrolleragent_controllergo383) `:383`

- 🔗 [Reconcile](#reconcile-gointernalcontrolleragent_controllergo62) `:62`

- 🔗 [SetupWithManager](#setupwithmanager-gointernalcontrolleragent_controllergo68) `:68`

- 🔗 [findAgentsReferencingConfigMap](#findagentsreferencingconfigmap-gointernalcontrolleragent_controllergo335) `:335`

- 🔗 [findAgentsUsingMCPServer](#findagentsusingmcpserver-gointernalcontrolleragent_controllergo196) `:196`

- 🔗 [findAgentsUsingMCPService](#findagentsusingmcpservice-gointernalcontrolleragent_controllergo268) `:268`

- 🔗 [findAgentsUsingModelConfig](#findagentsusingmodelconfig-gointernalcontrolleragent_controllergo304) `:304`

- 🔗 [findAgentsUsingRemoteMCPServer](#findagentsusingremotemcpserver-gointernalcontrolleragent_controllergo231) `:231`


</details>


[function] name: Create file: go/internal/controller/agent_controller.go:383 returns_error: нет description: Create implements default CreateEvent filter to ignore creation events for
owned objects as this controller most likely 


### Create (go/internal/controller/agent_controller.go:383)


Create implements default CreateEvent filter to ignore creation events for
owned objects as this controller most likely created it and does not need to
re-reconcile.


```go
func (typedOwnedObjectPredicate[object]) Create((e event.TypedCreateEvent[object])) (e event.TypedCreateEvent[object])
```


**Тип ответа:** e


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** event.TypedCreateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** object


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/agent_controller.go:383`



---


[function] name: Reconcile file: go/internal/controller/agent_controller.go:62 returns_error: да description: +kubebuilder:rbac:groups=kagent.dev,resources=agents,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:g


### Reconcile (go/internal/controller/agent_controller.go:62)


+kubebuilder:rbac:groups=kagent.dev,resources=agents,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:groups=kagent.dev,resources=agents/status,verbs=get;update;patch
+kubebuilder:rbac:groups=kagent.dev,resources=agents/finalizers,verbs=update
+kubebuilder:rbac:groups=core,resources=secrets,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:groups=core,resources=serviceaccounts,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:groups=core,resources=configmaps,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:groups=apps,resources=deployments,verbs=get;list;watch;create;update;patch;delete


```go
func (r *AgentController) Reconcile((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/agent_controller.go:62`



---


[function] name: SetupWithManager file: go/internal/controller/agent_controller.go:68 returns_error: нет description: SetupWithManager sets up the controller with the Manager.


### SetupWithManager (go/internal/controller/agent_controller.go:68)


SetupWithManager sets up the controller with the Manager.


```go
func (r *AgentController) SetupWithManager((mgr ctrl.Manager)) (mgr ctrl.Manager)
```


**Тип ответа:** mgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


📍 *Расположение:* `go/internal/controller/agent_controller.go:68`



---


[function] name: findAgentsReferencingConfigMap file: go/internal/controller/agent_controller.go:335 returns_error: нет description: —


### findAgentsReferencingConfigMap (go/internal/controller/agent_controller.go:335)


findAgentsReferencingConfigMap is a method that performs operations based on the provided parameters and returns (ctx context.Context, cl client.Client, obj types.NamespacedName).


```go
func (r *AgentController) findAgentsReferencingConfigMap((ctx context.Context, cl client.Client, obj types.NamespacedName)) (ctx context.Context, cl client.Client, obj types.NamespacedName)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** cl


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/agent_controller.go:335`



---


[function] name: findAgentsUsingMCPServer file: go/internal/controller/agent_controller.go:196 returns_error: нет description: —


### findAgentsUsingMCPServer (go/internal/controller/agent_controller.go:196)


findAgentsUsingMCPServer is a method that performs operations based on the provided parameters and returns (ctx context.Context, cl client.Client, obj types.NamespacedName).


```go
func (r *AgentController) findAgentsUsingMCPServer((ctx context.Context, cl client.Client, obj types.NamespacedName)) (ctx context.Context, cl client.Client, obj types.NamespacedName)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** cl


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/agent_controller.go:196`



---


[function] name: findAgentsUsingMCPService file: go/internal/controller/agent_controller.go:268 returns_error: нет description: —


### findAgentsUsingMCPService (go/internal/controller/agent_controller.go:268)


findAgentsUsingMCPService is a method that performs operations based on the provided parameters and returns (ctx context.Context, cl client.Client, obj types.NamespacedName).


```go
func (r *AgentController) findAgentsUsingMCPService((ctx context.Context, cl client.Client, obj types.NamespacedName)) (ctx context.Context, cl client.Client, obj types.NamespacedName)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** cl


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/agent_controller.go:268`



---


[function] name: findAgentsUsingModelConfig file: go/internal/controller/agent_controller.go:304 returns_error: нет description: —


### findAgentsUsingModelConfig (go/internal/controller/agent_controller.go:304)


findAgentsUsingModelConfig is a method that performs operations based on the provided parameters and returns (ctx context.Context, cl client.Client, obj types.NamespacedName).


```go
func (r *AgentController) findAgentsUsingModelConfig((ctx context.Context, cl client.Client, obj types.NamespacedName)) (ctx context.Context, cl client.Client, obj types.NamespacedName)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** cl


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/agent_controller.go:304`



---


[function] name: findAgentsUsingRemoteMCPServer file: go/internal/controller/agent_controller.go:231 returns_error: нет description: —


### findAgentsUsingRemoteMCPServer (go/internal/controller/agent_controller.go:231)


findAgentsUsingRemoteMCPServer is a method that performs operations based on the provided parameters and returns (ctx context.Context, cl client.Client, obj types.NamespacedName).


```go
func (r *AgentController) findAgentsUsingRemoteMCPServer((ctx context.Context, cl client.Client, obj types.NamespacedName)) (ctx context.Context, cl client.Client, obj types.NamespacedName)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** cl


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/agent_controller.go:231`




## go/internal/controller/mcp_server_tool_controller.go


📄 Исходный файл: `go/internal/controller/mcp_server_tool_controller.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Reconcile](#reconcile-gointernalcontrollermcp_server_tool_controllergo49) `:49`

- 🔗 [SetupWithManager](#setupwithmanager-gointernalcontrollermcp_server_tool_controllergo71) `:71`


</details>


[function] name: Reconcile file: go/internal/controller/mcp_server_tool_controller.go:49 returns_error: да description: +kubebuilder:rbac:groups=kagent.dev,resources=mcpservers,verbs=get;list;watch


### Reconcile (go/internal/controller/mcp_server_tool_controller.go:49)


+kubebuilder:rbac:groups=kagent.dev,resources=mcpservers,verbs=get;list;watch


```go
func (r *MCPServerToolController) Reconcile((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/mcp_server_tool_controller.go:49`



---


[function] name: SetupWithManager file: go/internal/controller/mcp_server_tool_controller.go:71 returns_error: нет description: SetupWithManager sets up the controller with the Manager.


### SetupWithManager (go/internal/controller/mcp_server_tool_controller.go:71)


SetupWithManager sets up the controller with the Manager.


```go
func (r *MCPServerToolController) SetupWithManager((mgr ctrl.Manager)) (mgr ctrl.Manager)
```


**Тип ответа:** mgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


📍 *Расположение:* `go/internal/controller/mcp_server_tool_controller.go:71`




## go/internal/controller/modelconfig_controller.go


📄 Исходный файл: `go/internal/controller/modelconfig_controller.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Reconcile](#reconcile-gointernalcontrollermodelconfig_controllergo55) `:55`

- 🔗 [SetupWithManager](#setupwithmanager-gointernalcontrollermodelconfig_controllergo61) `:61`

- 🔗 [findModelsUsingSecret](#findmodelsusingsecret-gointernalcontrollermodelconfig_controllergo92) `:92`

- 🔗 [modelReferencesSecret](#modelreferencessecret-gointernalcontrollermodelconfig_controllergo115) `:115`


</details>


[function] name: Reconcile file: go/internal/controller/modelconfig_controller.go:55 returns_error: да description: +kubebuilder:rbac:groups=kagent.dev,resources=modelconfigs,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:


### Reconcile (go/internal/controller/modelconfig_controller.go:55)


+kubebuilder:rbac:groups=kagent.dev,resources=modelconfigs,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:groups=kagent.dev,resources=modelconfigs/status,verbs=get;update;patch
+kubebuilder:rbac:groups=kagent.dev,resources=modelconfigs/finalizers,verbs=update
+kubebuilder:rbac:groups=core,resources=secrets,verbs=get;list;watch


```go
func (r *ModelConfigController) Reconcile((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/modelconfig_controller.go:55`



---


[function] name: SetupWithManager file: go/internal/controller/modelconfig_controller.go:61 returns_error: нет description: SetupWithManager sets up the controller with the Manager.


### SetupWithManager (go/internal/controller/modelconfig_controller.go:61)


SetupWithManager sets up the controller with the Manager.


```go
func (r *ModelConfigController) SetupWithManager((mgr ctrl.Manager)) (mgr ctrl.Manager)
```


**Тип ответа:** mgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


📍 *Расположение:* `go/internal/controller/modelconfig_controller.go:61`



---


[function] name: findModelsUsingSecret file: go/internal/controller/modelconfig_controller.go:92 returns_error: нет description: —


### findModelsUsingSecret (go/internal/controller/modelconfig_controller.go:92)


findModelsUsingSecret is a method that performs operations based on the provided parameters and returns (ctx context.Context, cl client.Client, obj types.NamespacedName).


```go
func (r *ModelConfigController) findModelsUsingSecret((ctx context.Context, cl client.Client, obj types.NamespacedName)) (ctx context.Context, cl client.Client, obj types.NamespacedName)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** cl


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/modelconfig_controller.go:92`



---


[function] name: modelReferencesSecret file: go/internal/controller/modelconfig_controller.go:115 returns_error: нет description: —


### modelReferencesSecret (go/internal/controller/modelconfig_controller.go:115)


modelReferencesSecret is a function that performs operations based on the provided parameters and returns (model *v1alpha2.ModelConfig, secretObj types.NamespacedName).


```go
func modelReferencesSecret((model *v1alpha2.ModelConfig, secretObj types.NamespacedName)) (model *v1alpha2.ModelConfig, secretObj types.NamespacedName)
```


**Тип запроса:** v1alpha2.ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** model


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** v1alpha2.ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** secretObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/modelconfig_controller.go:115`




## go/internal/controller/modelproviderconfig_controller.go


📄 Исходный файл: `go/internal/controller/modelproviderconfig_controller.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Reconcile](#reconcile-gointernalcontrollermodelproviderconfig_controllergo53) `:53`

- 🔗 [SetupWithManager](#setupwithmanager-gointernalcontrollermodelproviderconfig_controllergo59) `:59`

- 🔗 [findModelProviderConfigsUsingSecret](#findmodelproviderconfigsusingsecret-gointernalcontrollermodelproviderconfig_controllergo90) `:90`

- 🔗 [modelProviderConfigReferencesSecret](#modelproviderconfigreferencessecret-gointernalcontrollermodelproviderconfig_controllergo113) `:113`


</details>


[function] name: Reconcile file: go/internal/controller/modelproviderconfig_controller.go:53 returns_error: да description: +kubebuilder:rbac:groups=kagent.dev,resources=modelproviderconfigs,verbs=get;list;watch;create;update;patch;delete
+kube


### Reconcile (go/internal/controller/modelproviderconfig_controller.go:53)


+kubebuilder:rbac:groups=kagent.dev,resources=modelproviderconfigs,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:groups=kagent.dev,resources=modelproviderconfigs/status,verbs=get;update;patch
+kubebuilder:rbac:groups=kagent.dev,resources=modelproviderconfigs/finalizers,verbs=update
+kubebuilder:rbac:groups=core,resources=secrets,verbs=get;list;watch


```go
func (r *ModelProviderConfigController) Reconcile((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/modelproviderconfig_controller.go:53`



---


[function] name: SetupWithManager file: go/internal/controller/modelproviderconfig_controller.go:59 returns_error: нет description: SetupWithManager sets up the controller with the Manager.


### SetupWithManager (go/internal/controller/modelproviderconfig_controller.go:59)


SetupWithManager sets up the controller with the Manager.


```go
func (r *ModelProviderConfigController) SetupWithManager((mgr ctrl.Manager)) (mgr ctrl.Manager)
```


**Тип ответа:** mgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


📍 *Расположение:* `go/internal/controller/modelproviderconfig_controller.go:59`



---


[function] name: findModelProviderConfigsUsingSecret file: go/internal/controller/modelproviderconfig_controller.go:90 returns_error: нет description: —


### findModelProviderConfigsUsingSecret (go/internal/controller/modelproviderconfig_controller.go:90)


findModelProviderConfigsUsingSecret is a method that performs operations based on the provided parameters and returns (ctx context.Context, cl client.Client, obj types.NamespacedName).


```go
func (r *ModelProviderConfigController) findModelProviderConfigsUsingSecret((ctx context.Context, cl client.Client, obj types.NamespacedName)) (ctx context.Context, cl client.Client, obj types.NamespacedName)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** cl


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/modelproviderconfig_controller.go:90`



---


[function] name: modelProviderConfigReferencesSecret file: go/internal/controller/modelproviderconfig_controller.go:113 returns_error: нет description: —


### modelProviderConfigReferencesSecret (go/internal/controller/modelproviderconfig_controller.go:113)


modelProviderConfigReferencesSecret is a function that performs operations based on the provided parameters and returns (mpc *v1alpha2.ModelProviderConfig, secretObj types.NamespacedName).


```go
func modelProviderConfigReferencesSecret((mpc *v1alpha2.ModelProviderConfig, secretObj types.NamespacedName)) (mpc *v1alpha2.ModelProviderConfig, secretObj types.NamespacedName)
```


**Тип запроса:** v1alpha2.ModelProviderConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** mpc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelProviderConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** secretObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/modelproviderconfig_controller.go:113`




## go/internal/controller/predicates/discovery_disabled.go


📄 Исходный файл: `go/internal/controller/predicates/discovery_disabled.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Create](#create-gointernalcontrollerpredicatesdiscovery_disabledgo32) `:32`

- 🔗 [Delete](#delete-gointernalcontrollerpredicatesdiscovery_disabledgo40) `:40`

- 🔗 [Generic](#generic-gointernalcontrollerpredicatesdiscovery_disabledgo44) `:44`

- 🔗 [Update](#update-gointernalcontrollerpredicatesdiscovery_disabledgo36) `:36`

- 🔗 [isDiscoveryDisabled](#isdiscoverydisabled-gointernalcontrollerpredicatesdiscovery_disabledgo48) `:48`


</details>


[function] name: Create file: go/internal/controller/predicates/discovery_disabled.go:32 returns_error: нет description: —


### Create (go/internal/controller/predicates/discovery_disabled.go:32)


Create is a method that creates new data based on the provided parameters and returns (e event.CreateEvent).


```go
func (DiscoveryDisabledPredicate) Create((e event.CreateEvent)) (e event.CreateEvent)
```


**Тип ответа:** e


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** event.CreateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/predicates/discovery_disabled.go:32`



---


[function] name: Delete file: go/internal/controller/predicates/discovery_disabled.go:40 returns_error: нет description: —


### Delete (go/internal/controller/predicates/discovery_disabled.go:40)


Delete is a method that deletes data based on the provided parameters and returns (e event.DeleteEvent).


```go
func (DiscoveryDisabledPredicate) Delete((e event.DeleteEvent)) (e event.DeleteEvent)
```


**Тип ответа:** e


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** event.DeleteEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/predicates/discovery_disabled.go:40`



---


[function] name: Generic file: go/internal/controller/predicates/discovery_disabled.go:44 returns_error: нет description: —


### Generic (go/internal/controller/predicates/discovery_disabled.go:44)


Generic is a method that performs operations based on the provided parameters and returns (e event.GenericEvent).


```go
func (DiscoveryDisabledPredicate) Generic((e event.GenericEvent)) (e event.GenericEvent)
```


**Тип ответа:** e


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** event.GenericEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/predicates/discovery_disabled.go:44`



---


[function] name: Update file: go/internal/controller/predicates/discovery_disabled.go:36 returns_error: нет description: —


### Update (go/internal/controller/predicates/discovery_disabled.go:36)


Update is a method that updates data based on the provided parameters and returns (e event.UpdateEvent).


```go
func (DiscoveryDisabledPredicate) Update((e event.UpdateEvent)) (e event.UpdateEvent)
```


**Тип ответа:** e


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** event.UpdateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/predicates/discovery_disabled.go:36`



---


[function] name: isDiscoveryDisabled file: go/internal/controller/predicates/discovery_disabled.go:48 returns_error: нет description: —


### isDiscoveryDisabled (go/internal/controller/predicates/discovery_disabled.go:48)


isDiscoveryDisabled is a function that performs operations based on the provided parameters and returns (obj client.Object).


```go
func isDiscoveryDisabled((obj client.Object)) (obj client.Object)
```


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/predicates/discovery_disabled.go:48`




## go/internal/controller/provider/discoverer.go


📄 Исходный файл: `go/internal/controller/provider/discoverer.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [DiscoverModels](#discovermodels-gointernalcontrollerproviderdiscoverergo62) `:62`

- 🔗 [NewModelDiscoverer](#newmodeldiscoverer-gointernalcontrollerproviderdiscoverergo44) `:44`

- 🔗 [buildModelsURL](#buildmodelsurl-gointernalcontrollerproviderdiscoverergo146) `:146`

- 🔗 [discoverOllamaModels](#discoverollamamodels-gointernalcontrollerproviderdiscoverergo185) `:185`

- 🔗 [parseModelsResponse](#parsemodelsresponse-gointernalcontrollerproviderdiscoverergo123) `:123`

- 🔗 [setAuthHeaders](#setauthheaders-gointernalcontrollerproviderdiscoverergo106) `:106`


</details>


[function] name: DiscoverModels file: go/internal/controller/provider/discoverer.go:62 returns_error: да description: DiscoverModels calls the provider's models endpoint and returns available model IDs.
Most providers use OpenAI-compatibl


### DiscoverModels (go/internal/controller/provider/discoverer.go:62)


DiscoverModels calls the provider's models endpoint and returns available model IDs.
Most providers use OpenAI-compatible /v1/models, but auth headers vary by provider.


```go
func (d *ModelDiscoverer) DiscoverModels(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/provider/discoverer.go:62`



---


[function] name: NewModelDiscoverer file: go/internal/controller/provider/discoverer.go:44 returns_error: нет description: NewModelDiscoverer creates a new ModelDiscoverer instance.


### NewModelDiscoverer (go/internal/controller/provider/discoverer.go:44)


NewModelDiscoverer creates a new ModelDiscoverer instance.


```go
func NewModelDiscoverer(()) ()
```


📍 *Расположение:* `go/internal/controller/provider/discoverer.go:44`



---


[function] name: buildModelsURL file: go/internal/controller/provider/discoverer.go:146 returns_error: нет description: buildModelsURL constructs the models endpoint URL based on provider type.
Note: Ollama is handled separately via Discove


### buildModelsURL (go/internal/controller/provider/discoverer.go:146)


buildModelsURL constructs the models endpoint URL based on provider type.
Note: Ollama is handled separately via DiscoverOllamaModels.


```go
func buildModelsURL((endpoint string, providerType v1alpha2.ModelProvider)) (endpoint string, providerType v1alpha2.ModelProvider)
```


**Тип ответа:** endpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** providerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/internal/controller/provider/discoverer.go:146`



---


[function] name: discoverOllamaModels file: go/internal/controller/provider/discoverer.go:185 returns_error: да description: discoverOllamaModels handles Ollama's different response format.


### discoverOllamaModels (go/internal/controller/provider/discoverer.go:185)


discoverOllamaModels handles Ollama's different response format.


```go
func (d *ModelDiscoverer) discoverOllamaModels(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/provider/discoverer.go:185`



---


[function] name: parseModelsResponse file: go/internal/controller/provider/discoverer.go:123 returns_error: да description: parseModelsResponse parses OpenAI-compatible response and extracts model IDs.
Format: {"data": [{"id": "model-name"}, ..


### parseModelsResponse (go/internal/controller/provider/discoverer.go:123)


parseModelsResponse parses OpenAI-compatible response and extracts model IDs.
Format: {"data": [{"id": "model-name"}, ...]}


```go
func (d *ModelDiscoverer) parseModelsResponse(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/provider/discoverer.go:123`



---


[function] name: setAuthHeaders file: go/internal/controller/provider/discoverer.go:106 returns_error: нет description: setAuthHeaders sets the appropriate authentication headers based on provider type.


### setAuthHeaders (go/internal/controller/provider/discoverer.go:106)


setAuthHeaders sets the appropriate authentication headers based on provider type.


```go
func (d *ModelDiscoverer) setAuthHeaders((req *http.Request, providerType v1alpha2.ModelProvider, apiKey string)) (req *http.Request, providerType v1alpha2.ModelProvider, apiKey string)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** providerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** apiKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/provider/discoverer.go:106`




## go/internal/controller/reconciler/reconciler.go


📄 Исходный файл: `go/internal/controller/reconciler/reconciler.go`


<details open>
<summary><b>Функции в этом файле (39)</b></summary>


- 🔗 [GetOwnedResourceTypes](#getownedresourcetypes-gointernalcontrollerreconcilerreconcilergo653) `:653`

- 🔗 [NewKagentReconciler](#newkagentreconciler-gointernalcontrollerreconcilerreconcilergo67) `:67`

- 🔗 [ReconcileKagentAgent](#reconcilekagentagent-gointernalcontrollerreconcilerreconcilergo83) `:83`

- 🔗 [ReconcileKagentMCPServer](#reconcilekagentmcpserver-gointernalcontrollerreconcilerreconcilergo351) `:351`

- 🔗 [ReconcileKagentMCPService](#reconcilekagentmcpservice-gointernalcontrollerreconcilerreconcilergo178) `:178`

- 🔗 [ReconcileKagentModelConfig](#reconcilekagentmodelconfig-gointernalcontrollerreconcilerreconcilergo227) `:227`

- 🔗 [ReconcileKagentModelProviderConfig](#reconcilekagentmodelproviderconfig-gointernalcontrollerreconcilerreconcilergo921) `:921`

- 🔗 [ReconcileKagentRemoteMCPServer](#reconcilekagentremotemcpserver-gointernalcontrollerreconcilerreconcilergo395) `:395`

- 🔗 [RefreshModelProviderConfigModels](#refreshmodelproviderconfigmodels-gointernalcontrollerreconcilerreconcilergo1133) `:1133`

- 🔗 [RoundTrip](#roundtrip-gointernalcontrollerreconcilerreconcilergo854) `:854`

- 🔗 [computeModelProviderSecretHash](#computemodelprovidersecrethash-gointernalcontrollerreconcilerreconcilergo996) `:996`

- 🔗 [computeStatusSecretHash](#computestatussecrethash-gointernalcontrollerreconcilerreconcilergo283) `:283`

- 🔗 [conditionMessage](#conditionmessage-gointernalcontrollerreconcilerreconcilergo1123) `:1123`

- 🔗 [conditionReason](#conditionreason-gointernalcontrollerreconcilerreconcilergo1116) `:1116`

- 🔗 [conditionStatus](#conditionstatus-gointernalcontrollerreconcilerreconcilergo1109) `:1109`

- 🔗 [convertTool](#converttool-gointernalcontrollerreconcilerreconcilergo913) `:913`

- 🔗 [createMcpTransport](#createmcptransport-gointernalcontrollerreconcilerreconcilergo812) `:812`

- 🔗 [createOrUpdate](#createorupdate-gointernalcontrollerreconcilerreconcilergo698) `:698`

- 🔗 [deleteObjects](#deleteobjects-gointernalcontrollerreconcilerreconcilergo746) `:746`

- 🔗 [discoverModelProviderConfigModels](#discovermodelproviderconfigmodels-gointernalcontrollerreconcilerreconcilergo1024) `:1024`

- 🔗 [getDiscoveredMCPTools](#getdiscoveredmcptools-gointernalcontrollerreconcilerreconcilergo894) `:894`

- 🔗 [handleAgentDeletion](#handleagentdeletion-gointernalcontrollerreconcilerreconcilergo102) `:102`

- 🔗 [isNamespaceWatched](#isnamespacewatched-gointernalcontrollerreconcilerreconcilergo805) `:805`

- 🔗 [listTools](#listtools-gointernalcontrollerreconcilerreconcilergo865) `:865`

- 🔗 [mutate](#mutate-gointernalcontrollerreconcilerreconcilergo736) `:736`

- 🔗 [newHTTPClient](#newhttpclient-gointernalcontrollerreconcilerreconcilergo836) `:836`

- 🔗 [reconcileAgent](#reconcileagent-gointernalcontrollerreconcilerreconcilergo620) `:620`

- 🔗 [reconcileAgentStatus](#reconcileagentstatus-gointernalcontrollerreconcilerreconcilergo113) `:113`

- 🔗 [reconcileDesiredObjects](#reconciledesiredobjects-gointernalcontrollerreconcilerreconcilergo658) `:658`

- 🔗 [reconcileModelConfigStatus](#reconcilemodelconfigstatus-gointernalcontrollerreconcilerreconcilergo310) `:310`

- 🔗 [reconcileRemoteMCPServerStatus](#reconcileremotemcpserverstatus-gointernalcontrollerreconcilerreconcilergo455) `:455`

- 🔗 [resolveModelProviderConfigSecret](#resolvemodelproviderconfigsecret-gointernalcontrollerreconcilerreconcilergo949) `:949`

- 🔗 [shouldDiscoverModels](#shoulddiscovermodels-gointernalcontrollerreconcilerreconcilergo1008) `:1008`

- 🔗 [updateModelProviderConfigStatus](#updatemodelproviderconfigstatus-gointernalcontrollerreconcilerreconcilergo1037) `:1037`

- 🔗 [upsertAgent](#upsertagent-gointernalcontrollerreconcilerreconcilergo767) `:767`

- 🔗 [upsertToolServerForRemoteMCPServer](#upserttoolserverforremotemcpserver-gointernalcontrollerreconcilerreconcilergo782) `:782`

- 🔗 [validateAgentToolReference](#validateagenttoolreference-gointernalcontrollerreconcilerreconcilergo529) `:529`

- 🔗 [validateCrossNamespaceReferences](#validatecrossnamespacereferences-gointernalcontrollerreconcilerreconcilergo504) `:504`

- 🔗 [validateMcpServerReference](#validatemcpserverreference-gointernalcontrollerreconcilerreconcilergo565) `:565`


</details>


[function] name: GetOwnedResourceTypes file: go/internal/controller/reconciler/reconciler.go:653 returns_error: нет description: GetOwnedResourceTypes returns all the resource types that may be owned by
controllers that are reconciled herein. At pre


### GetOwnedResourceTypes (go/internal/controller/reconciler/reconciler.go:653)


GetOwnedResourceTypes returns all the resource types that may be owned by
controllers that are reconciled herein. At present only the agents controller
owns resources so this simply wraps a call to the ADK translator as that is
responsible for creating the manifests for an agent. If in future other
controllers start owning resources then this method should be updated to
return the distinct union of all owned resource types.


```go
func (r *kagentReconciler) GetOwnedResourceTypes(()) ()
```


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:653`



---


[function] name: NewKagentReconciler file: go/internal/controller/reconciler/reconciler.go:67 returns_error: нет description: —


### NewKagentReconciler (go/internal/controller/reconciler/reconciler.go:67)


NewKagentReconciler is a function that performs operations based on the provided parameters and returns (
	translator agent_translator.AdkApiTranslator,
	kube client.Client,
	dbClient database.Client,
	defaultModelConfig types.NamespacedName,
	watchedNamespaces []string,
).


```go
func NewKagentReconciler((
	translator agent_translator.AdkApiTranslator,
	kube client.Client,
	dbClient database.Client,
	defaultModelConfig types.NamespacedName,
	watchedNamespaces []string,
)) (
	translator agent_translator.AdkApiTranslator,
	kube client.Client,
	dbClient database.Client,
	defaultModelConfig types.NamespacedName,
	watchedNamespaces []string,
)
```


**Тип ответа:** translator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agent_translator.AdkApiTranslator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kube


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** dbClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** defaultModelConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** watchedNamespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:67`



---


[function] name: ReconcileKagentAgent file: go/internal/controller/reconciler/reconciler.go:83 returns_error: нет description: —


### ReconcileKagentAgent (go/internal/controller/reconciler/reconciler.go:83)


ReconcileKagentAgent is a method that performs operations based on the provided parameters and returns (ctx context.Context, req ctrl.Request).


```go
func (a *kagentReconciler) ReconcileKagentAgent((ctx context.Context, req ctrl.Request)) (ctx context.Context, req ctrl.Request)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:83`



---


[function] name: ReconcileKagentMCPServer file: go/internal/controller/reconciler/reconciler.go:351 returns_error: нет description: —


### ReconcileKagentMCPServer (go/internal/controller/reconciler/reconciler.go:351)


ReconcileKagentMCPServer is a method that performs operations based on the provided parameters and returns (ctx context.Context, req ctrl.Request).


```go
func (a *kagentReconciler) ReconcileKagentMCPServer((ctx context.Context, req ctrl.Request)) (ctx context.Context, req ctrl.Request)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:351`



---


[function] name: ReconcileKagentMCPService file: go/internal/controller/reconciler/reconciler.go:178 returns_error: нет description: —


### ReconcileKagentMCPService (go/internal/controller/reconciler/reconciler.go:178)


ReconcileKagentMCPService is a method that performs operations based on the provided parameters and returns (ctx context.Context, req ctrl.Request).


```go
func (a *kagentReconciler) ReconcileKagentMCPService((ctx context.Context, req ctrl.Request)) (ctx context.Context, req ctrl.Request)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:178`



---


[function] name: ReconcileKagentModelConfig file: go/internal/controller/reconciler/reconciler.go:227 returns_error: нет description: —


### ReconcileKagentModelConfig (go/internal/controller/reconciler/reconciler.go:227)


ReconcileKagentModelConfig is a method that performs operations based on the provided parameters and returns (ctx context.Context, req ctrl.Request).


```go
func (a *kagentReconciler) ReconcileKagentModelConfig((ctx context.Context, req ctrl.Request)) (ctx context.Context, req ctrl.Request)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:227`



---


[function] name: ReconcileKagentModelProviderConfig file: go/internal/controller/reconciler/reconciler.go:921 returns_error: да description: ReconcileKagentModelProviderConfig reconciles a ModelProviderConfig object


### ReconcileKagentModelProviderConfig (go/internal/controller/reconciler/reconciler.go:921)


ReconcileKagentModelProviderConfig reconciles a ModelProviderConfig object


```go
func (a *kagentReconciler) ReconcileKagentModelProviderConfig((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:921`



---


[function] name: ReconcileKagentRemoteMCPServer file: go/internal/controller/reconciler/reconciler.go:395 returns_error: нет description: —


### ReconcileKagentRemoteMCPServer (go/internal/controller/reconciler/reconciler.go:395)


ReconcileKagentRemoteMCPServer is a method that performs operations based on the provided parameters and returns (ctx context.Context, req ctrl.Request).


```go
func (a *kagentReconciler) ReconcileKagentRemoteMCPServer((ctx context.Context, req ctrl.Request)) (ctx context.Context, req ctrl.Request)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:395`



---


[function] name: RefreshModelProviderConfigModels file: go/internal/controller/reconciler/reconciler.go:1133 returns_error: да description: RefreshModelProviderConfigModels forces a fresh model discovery for a model provider config and updates its status.
This


### RefreshModelProviderConfigModels (go/internal/controller/reconciler/reconciler.go:1133)


RefreshModelProviderConfigModels forces a fresh model discovery for a model provider config and updates its status.
This is called by the HTTP API when refresh=true is requested.
It reuses all existing internal reconciler methods - no code duplication.


```go
func (a *kagentReconciler) RefreshModelProviderConfigModels(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:1133`



---


[function] name: RoundTrip file: go/internal/controller/reconciler/reconciler.go:854 returns_error: да description: —


### RoundTrip (go/internal/controller/reconciler/reconciler.go:854)


RoundTrip is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *headerTransport) RoundTrip((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "AccessToken": "string",
  "TokenType": "string",
  "ExpiresIn": 0,
  "Scope": "string",
  "IssuedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Response


```json
{
  "AccessToken": "string",
  "TokenType": "string",
  "ExpiresIn": 0,
  "Scope": "string",
  "IssuedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:854`



---


[function] name: computeModelProviderSecretHash file: go/internal/controller/reconciler/reconciler.go:996 returns_error: нет description: computeModelProviderSecretHash computes a hash of the secret's identity and data for change detection.
The secret must c


### computeModelProviderSecretHash (go/internal/controller/reconciler/reconciler.go:996)


computeModelProviderSecretHash computes a hash of the secret's identity and data for change detection.
The secret must contain exactly one data key (caller is responsible for validation).


```go
func computeModelProviderSecretHash((secret *corev1.Secret)) (secret *corev1.Secret)
```


**Тип запроса:** corev1.Secret


```json
{
  "Enabled": false,
  "Provider": "string",
  "File": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** secret


```json
{
  "NamespacedName": {},
  "Secret": null
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** corev1.Secret


```json
{
  "Enabled": false,
  "Provider": "string",
  "File": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:996`



---


[function] name: computeStatusSecretHash file: go/internal/controller/reconciler/reconciler.go:283 returns_error: нет description: computeStatusSecretHash computes a deterministic singular hash of the secrets the model config references for the status


### computeStatusSecretHash (go/internal/controller/reconciler/reconciler.go:283)


computeStatusSecretHash computes a deterministic singular hash of the secrets the model config references for the status
this loses per-secret context (i.e. versioning/hash status per-secret), but simplifies the number of statuses tracked


```go
func computeStatusSecretHash((secrets []secretRef)) (secrets []secretRef)
```


**Тип ответа:** secrets


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** secretRef


```json
{
  "NamespacedName": {},
  "Secret": null
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:283`



---


[function] name: conditionMessage file: go/internal/controller/reconciler/reconciler.go:1123 returns_error: да description: —


### conditionMessage (go/internal/controller/reconciler/reconciler.go:1123)


conditionMessage is a function that performs operations based on the provided parameters and may return an error.


```go
func conditionMessage((err error, successMessage string)) (err error, successMessage string)
```


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** successMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`, `successMessage string`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:1123`



---


[function] name: conditionReason file: go/internal/controller/reconciler/reconciler.go:1116 returns_error: да description: —


### conditionReason (go/internal/controller/reconciler/reconciler.go:1116)


conditionReason is a function that performs operations based on the provided parameters and may return an error.


```go
func conditionReason((err error, successReason, failureReason string)) (err error, successReason, failureReason string)
```


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** successReason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** failureReason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`, `successReason`, `failureReason string`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:1116`



---


[function] name: conditionStatus file: go/internal/controller/reconciler/reconciler.go:1109 returns_error: нет description: Helper functions for condition status


### conditionStatus (go/internal/controller/reconciler/reconciler.go:1109)


Helper functions for condition status


```go
func conditionStatus((isTrue bool)) (isTrue bool)
```


**Тип ответа:** isTrue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:1109`



---


[function] name: convertTool file: go/internal/controller/reconciler/reconciler.go:913 returns_error: да description: —


### convertTool (go/internal/controller/reconciler/reconciler.go:913)


convertTool is a function that performs operations based on the provided parameters and may return an error.


```go
func convertTool((*v1alpha2.MCPTool, error)) (*v1alpha2.MCPTool, error)
```


**Тип запроса:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1alpha2.MCPTool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:913`



---


[function] name: createMcpTransport file: go/internal/controller/reconciler/reconciler.go:812 returns_error: да description: —


### createMcpTransport (go/internal/controller/reconciler/reconciler.go:812)


createMcpTransport is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *kagentReconciler) createMcpTransport((mcp.Transport, error)) (mcp.Transport, error)
```


**Тип ответа:** mcp.Transport


```json
{
  "base": {},
  "headers": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `mcp.Transport`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:812`



---


[function] name: createOrUpdate file: go/internal/controller/reconciler/reconciler.go:698 returns_error: да description: modified version of controllerutil.CreateOrUpdate to support proto based objects like istio


### createOrUpdate (go/internal/controller/reconciler/reconciler.go:698)


modified version of controllerutil.CreateOrUpdate to support proto based objects like istio


```go
func createOrUpdate((controllerutil.OperationResult, error)) (controllerutil.OperationResult, error)
```


**Тип ответа:** controllerutil.OperationResult


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `controllerutil.OperationResult`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:698`



---


[function] name: deleteObjects file: go/internal/controller/reconciler/reconciler.go:746 returns_error: нет description: —


### deleteObjects (go/internal/controller/reconciler/reconciler.go:746)


deleteObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, objects map[types.UID]client.Object).


```go
func (a *kagentReconciler) deleteObjects((ctx context.Context, objects map[types.UID]client.Object)) (ctx context.Context, objects map[types.UID]client.Object)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** objects


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.UID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:746`



---


[function] name: discoverModelProviderConfigModels file: go/internal/controller/reconciler/reconciler.go:1024 returns_error: да description: discoverModelProviderConfigModels calls the model discoverer to fetch models


### discoverModelProviderConfigModels (go/internal/controller/reconciler/reconciler.go:1024)


discoverModelProviderConfigModels calls the model discoverer to fetch models


```go
func (a *kagentReconciler) discoverModelProviderConfigModels(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:1024`



---


[function] name: getDiscoveredMCPTools file: go/internal/controller/reconciler/reconciler.go:894 returns_error: да description: —


### getDiscoveredMCPTools (go/internal/controller/reconciler/reconciler.go:894)


getDiscoveredMCPTools is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *kagentReconciler) getDiscoveredMCPTools(([]*v1alpha2.MCPTool, error)) ([]*v1alpha2.MCPTool, error)
```


**Тип запроса:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*v1alpha2.MCPTool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:894`



---


[function] name: handleAgentDeletion file: go/internal/controller/reconciler/reconciler.go:102 returns_error: нет description: —


### handleAgentDeletion (go/internal/controller/reconciler/reconciler.go:102)


handleAgentDeletion is a method that performs operations based on the provided parameters and returns (req ctrl.Request).


```go
func (a *kagentReconciler) handleAgentDeletion((req ctrl.Request)) (req ctrl.Request)
```


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:102`



---


[function] name: isNamespaceWatched file: go/internal/controller/reconciler/reconciler.go:805 returns_error: нет description: —


### isNamespaceWatched (go/internal/controller/reconciler/reconciler.go:805)


isNamespaceWatched is a method that performs operations based on the provided parameters and returns (namespace string).


```go
func (a *kagentReconciler) isNamespaceWatched((namespace string)) (namespace string)
```


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:805`



---


[function] name: listTools file: go/internal/controller/reconciler/reconciler.go:865 returns_error: да description: —


### listTools (go/internal/controller/reconciler/reconciler.go:865)


listTools is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *kagentReconciler) listTools(([]*v1alpha2.MCPTool, error)) ([]*v1alpha2.MCPTool, error)
```


**Тип запроса:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*v1alpha2.MCPTool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:865`



---


[function] name: mutate file: go/internal/controller/reconciler/reconciler.go:736 returns_error: нет description: mutate wraps a MutateFn and applies validation to its result.


### mutate (go/internal/controller/reconciler/reconciler.go:736)


mutate wraps a MutateFn and applies validation to its result.


```go
func mutate((f controllerutil.MutateFn, key client.ObjectKey, obj client.Object)) (f controllerutil.MutateFn, key client.ObjectKey, obj client.Object)
```


**Тип ответа:** f


```json
{
  "DatabasePath": "string",
  "VectorEnabled": false
}
```


*Определено в:* `go/internal/database/manager.go`


**Тип ответа:** controllerutil.MutateFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.ObjectKey


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:736`



---


[function] name: newHTTPClient file: go/internal/controller/reconciler/reconciler.go:836 returns_error: нет description: go-sdk does not have a WithHeaders option when initializing transport
so we need to create a custom HTTP client that add


### newHTTPClient (go/internal/controller/reconciler/reconciler.go:836)


go-sdk does not have a WithHeaders option when initializing transport
so we need to create a custom HTTP client that adds headers to all requests.


```go
func newHTTPClient((headers map[string]string)) (headers map[string]string)
```


**Тип ответа:** headers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:836`



---


[function] name: reconcileAgent file: go/internal/controller/reconciler/reconciler.go:620 returns_error: нет description: —


### reconcileAgent (go/internal/controller/reconciler/reconciler.go:620)


reconcileAgent is a method that performs operations based on the provided parameters and returns (ctx context.Context, agent *v1alpha2.Agent).


```go
func (a *kagentReconciler) reconcileAgent((ctx context.Context, agent *v1alpha2.Agent)) (ctx context.Context, agent *v1alpha2.Agent)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:620`



---


[function] name: reconcileAgentStatus file: go/internal/controller/reconciler/reconciler.go:113 returns_error: да description: —


### reconcileAgentStatus (go/internal/controller/reconciler/reconciler.go:113)


reconcileAgentStatus is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *kagentReconciler) reconcileAgentStatus((ctx context.Context, agent *v1alpha2.Agent, err error)) (ctx context.Context, agent *v1alpha2.Agent, err error)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `agent *v1alpha2.Agent`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:113`



---


[function] name: reconcileDesiredObjects file: go/internal/controller/reconciler/reconciler.go:658 returns_error: нет description: Function initially copied from https://github.com/open-telemetry/opentelemetry-operator/blob/e6d96f006f05cff0bc3808da1af


### reconcileDesiredObjects (go/internal/controller/reconciler/reconciler.go:658)


Function initially copied from https://github.com/open-telemetry/opentelemetry-operator/blob/e6d96f006f05cff0bc3808da1af69b6b636fbe88/internal/controllers/common.go#L141-L192


```go
func (a *kagentReconciler) reconcileDesiredObjects((ctx context.Context, owner metav1.Object, desiredObjects []client.Object, ownedObjects map[types.UID]client.Object)) (ctx context.Context, owner metav1.Object, desiredObjects []client.Object, ownedObjects map[types.UID]client.Object)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** owner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** desiredObjects


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** ownedObjects


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.UID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:658`



---


[function] name: reconcileModelConfigStatus file: go/internal/controller/reconciler/reconciler.go:310 returns_error: да description: —


### reconcileModelConfigStatus (go/internal/controller/reconciler/reconciler.go:310)


reconcileModelConfigStatus is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *kagentReconciler) reconcileModelConfigStatus((ctx context.Context, modelConfig *v1alpha2.ModelConfig, err error, secretHash string)) (ctx context.Context, modelConfig *v1alpha2.ModelConfig, err error, secretHash string)
```


**Тип запроса:** v1alpha2.ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** modelConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** secretHash


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `modelConfig *v1alpha2.ModelConfig`, `err error`, `secretHash string`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:310`



---


[function] name: reconcileRemoteMCPServerStatus file: go/internal/controller/reconciler/reconciler.go:455 returns_error: да description: —


### reconcileRemoteMCPServerStatus (go/internal/controller/reconciler/reconciler.go:455)


reconcileRemoteMCPServerStatus is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *kagentReconciler) reconcileRemoteMCPServerStatus((
	ctx context.Context,
	server *v1alpha2.RemoteMCPServer,
	discoveredTools []*v1alpha2.MCPTool,
	err error,
)) (
	ctx context.Context,
	server *v1alpha2.RemoteMCPServer,
	discoveredTools []*v1alpha2.MCPTool,
	err error,
)
```


**Тип запроса:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип запроса:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** server


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** discoveredTools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `server *v1alpha2.RemoteMCPServer`, `discoveredTools []*v1alpha2.MCPTool`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:455`



---


[function] name: resolveModelProviderConfigSecret file: go/internal/controller/reconciler/reconciler.go:949 returns_error: да description: resolveModelProviderConfigSecret fetches the Secret, validates it, and returns the API key and hash.
For model provider 


### resolveModelProviderConfigSecret (go/internal/controller/reconciler/reconciler.go:949)


resolveModelProviderConfigSecret fetches the Secret, validates it, and returns the API key and hash.
For model provider configs that don't require authentication (e.g., Ollama), returns empty apiKey with no error.


```go
func (a *kagentReconciler) resolveModelProviderConfigSecret((string, string, error)) (string, string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:949`



---


[function] name: shouldDiscoverModels file: go/internal/controller/reconciler/reconciler.go:1008 returns_error: нет description: shouldDiscoverModels checks if model discovery is needed


### shouldDiscoverModels (go/internal/controller/reconciler/reconciler.go:1008)


shouldDiscoverModels checks if model discovery is needed


```go
func (a *kagentReconciler) shouldDiscoverModels((mpc *v1alpha2.ModelProviderConfig)) (mpc *v1alpha2.ModelProviderConfig)
```


**Тип запроса:** v1alpha2.ModelProviderConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** mpc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelProviderConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:1008`



---


[function] name: updateModelProviderConfigStatus file: go/internal/controller/reconciler/reconciler.go:1037 returns_error: да description: updateModelProviderConfigStatus updates the ModelProviderConfig status based on reconciliation results.
Only modifies th


### updateModelProviderConfigStatus (go/internal/controller/reconciler/reconciler.go:1037)


updateModelProviderConfigStatus updates the ModelProviderConfig status based on reconciliation results.
Only modifies the status subresource - never modifies the ModelProviderConfig object itself.


```go
func (a *kagentReconciler) updateModelProviderConfigStatus((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:1037`



---


[function] name: upsertAgent file: go/internal/controller/reconciler/reconciler.go:767 returns_error: нет description: —


### upsertAgent (go/internal/controller/reconciler/reconciler.go:767)


upsertAgent is a method that performs operations based on the provided parameters and returns (ctx context.Context, agent *v1alpha2.Agent, agentOutputs *agent_translator.AgentOutputs).


```go
func (a *kagentReconciler) upsertAgent((ctx context.Context, agent *v1alpha2.Agent, agentOutputs *agent_translator.AgentOutputs)) (ctx context.Context, agent *v1alpha2.Agent, agentOutputs *agent_translator.AgentOutputs)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип запроса:** agent_translator.AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** agentOutputs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agent_translator.AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:767`



---


[function] name: upsertToolServerForRemoteMCPServer file: go/internal/controller/reconciler/reconciler.go:782 returns_error: да description: —


### upsertToolServerForRemoteMCPServer (go/internal/controller/reconciler/reconciler.go:782)


upsertToolServerForRemoteMCPServer is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *kagentReconciler) upsertToolServerForRemoteMCPServer(([]*v1alpha2.MCPTool, error)) ([]*v1alpha2.MCPTool, error)
```


**Тип запроса:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*v1alpha2.MCPTool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:782`



---


[function] name: validateAgentToolReference file: go/internal/controller/reconciler/reconciler.go:529 returns_error: нет description: validateAgentToolReference validates a reference to an Agent as a tool.
This includes:
1. Checking that target namespace


### validateAgentToolReference (go/internal/controller/reconciler/reconciler.go:529)


validateAgentToolReference validates a reference to an Agent as a tool.
This includes:
1. Checking that target namespaces are watched by the controller
2. Checking that the target Agent allows references from the agent's namespace


```go
func (a *kagentReconciler) validateAgentToolReference((ctx context.Context, sourceNamespace string, ref *v1alpha2.TypedReference)) (ctx context.Context, sourceNamespace string, ref *v1alpha2.TypedReference)
```


**Тип запроса:** v1alpha2.TypedReference


```json
{
  "Kind": "string",
  "ApiGroup": "string",
  "Name": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** sourceNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ref


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.TypedReference


```json
{
  "Kind": "string",
  "ApiGroup": "string",
  "Name": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:529`



---


[function] name: validateCrossNamespaceReferences file: go/internal/controller/reconciler/reconciler.go:504 returns_error: нет description: validateCrossNamespaceReferences validates that any cross-namespace
references in the agent's tools target namespaces th


### validateCrossNamespaceReferences (go/internal/controller/reconciler/reconciler.go:504)


validateCrossNamespaceReferences validates that any cross-namespace
references in the agent's tools target namespaces that are watched by the
controller. This prevents agents from referencing tools or agents in
namespaces that the controller cannot access.


```go
func (a *kagentReconciler) validateCrossNamespaceReferences((ctx context.Context, agent *v1alpha2.Agent)) (ctx context.Context, agent *v1alpha2.Agent)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:504`



---


[function] name: validateMcpServerReference file: go/internal/controller/reconciler/reconciler.go:565 returns_error: нет description: validateMcpServerReference validates a reference to an MCP server tool. This
includes:
1. Enforcing same-namespace-only 


### validateMcpServerReference (go/internal/controller/reconciler/reconciler.go:565)


validateMcpServerReference validates a reference to an MCP server tool. This
includes:
1. Enforcing same-namespace-only for MCPServer and Service (external types)
2. Checking that target namespaces are watched by the controller
3. Checking that the target resource allows references from the agent's namespace


```go
func (a *kagentReconciler) validateMcpServerReference((ctx context.Context, sourceNamespace string, ref *v1alpha2.McpServerTool)) (ctx context.Context, sourceNamespace string, ref *v1alpha2.McpServerTool)
```


**Тип запроса:** v1alpha2.McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** sourceNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ref


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/internal/controller/reconciler/reconciler.go:565`




## go/internal/controller/reconciler/status/mcp_server.go


📄 Исходный файл: `go/internal/controller/reconciler/status/mcp_server.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [ReconcileMCPServerStatus](#reconcilemcpserverstatus-gointernalcontrollerreconcilerstatusmcp_servergo15) `:15`

- 🔗 [checkReadyCondition](#checkreadycondition-gointernalcontrollerreconcilerstatusmcp_servergo73) `:73`

- 🔗 [setAcceptedCondition](#setacceptedcondition-gointernalcontrollerreconcilerstatusmcp_servergo33) `:33`

- 🔗 [setCondition](#setcondition-gointernalcontrollerreconcilerstatusmcp_servergo116) `:116`

- 🔗 [setProgrammedCondition](#setprogrammedcondition-gointernalcontrollerreconcilerstatusmcp_servergo57) `:57`

- 🔗 [setReadyCondition](#setreadycondition-gointernalcontrollerreconcilerstatusmcp_servergo107) `:107`

- 🔗 [setResolvedRefsCondition](#setresolvedrefscondition-gointernalcontrollerreconcilerstatusmcp_servergo48) `:48`

- 🔗 [updateMCPServerStatus](#updatemcpserverstatus-gointernalcontrollerreconcilerstatusmcp_servergo153) `:153`


</details>


[function] name: ReconcileMCPServerStatus file: go/internal/controller/reconciler/status/mcp_server.go:15 returns_error: да description: ReconcileMCPServerStatus reconciles the status of an MCPServer based on the deployment state


### ReconcileMCPServerStatus (go/internal/controller/reconciler/status/mcp_server.go:15)


ReconcileMCPServerStatus reconciles the status of an MCPServer based on the deployment state


```go
func ReconcileMCPServerStatus((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:15`



---


[function] name: checkReadyCondition file: go/internal/controller/reconciler/status/mcp_server.go:73 returns_error: нет description: checkReadyCondition checks if the MCPServer is ready by examining the deployment status
returns true if the deployment i


### checkReadyCondition (go/internal/controller/reconciler/status/mcp_server.go:73)


checkReadyCondition checks if the MCPServer is ready by examining the deployment status
returns true if the deployment is not ready and request should be requeued


```go
func checkReadyCondition((ctx context.Context, kube client.Client, mcpServer *v1alpha1.MCPServer)) (ctx context.Context, kube client.Client, mcpServer *v1alpha1.MCPServer)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** kube


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** mcpServer


```json
{
  "URL": "string",
  "Headers": {},
  "ServerType": "string",
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/mcp/registry.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:73`



---


[function] name: setAcceptedCondition file: go/internal/controller/reconciler/status/mcp_server.go:33 returns_error: да description: setAcceptedCondition sets the Accepted condition on the MCPServer


### setAcceptedCondition (go/internal/controller/reconciler/status/mcp_server.go:33)


setAcceptedCondition sets the Accepted condition on the MCPServer


```go
func setAcceptedCondition((mcpServer *v1alpha1.MCPServer, err error)) (mcpServer *v1alpha1.MCPServer, err error)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** mcpServer


```json
{
  "URL": "string",
  "Headers": {},
  "ServerType": "string",
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/mcp/registry.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `mcpServer *v1alpha1.MCPServer`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:33`



---


[function] name: setCondition file: go/internal/controller/reconciler/status/mcp_server.go:116 returns_error: нет description: setCondition sets the given condition on the MCPServer status


### setCondition (go/internal/controller/reconciler/status/mcp_server.go:116)


setCondition sets the given condition on the MCPServer status


```go
func setCondition((
	mcpServer *v1alpha1.MCPServer,
	conditionType v1alpha1.MCPServerConditionType,
	status metav1.ConditionStatus,
	reason v1alpha1.MCPServerConditionReason,
	message string,
)) (
	mcpServer *v1alpha1.MCPServer,
	conditionType v1alpha1.MCPServerConditionType,
	status metav1.ConditionStatus,
	reason v1alpha1.MCPServerConditionReason,
	message string,
)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** mcpServer


```json
{
  "URL": "string",
  "Headers": {},
  "ServerType": "string",
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/mcp/registry.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** conditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.MCPServerConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** status


```json
{
  "status": 0
}
```


*Определено в:* `go/internal/httpserver/middleware.go`


**Тип ответа:** metav1.ConditionStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.MCPServerConditionReason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:116`



---


[function] name: setProgrammedCondition file: go/internal/controller/reconciler/status/mcp_server.go:57 returns_error: нет description: setProgrammedCondition sets the Programmed condition on the MCPServer


### setProgrammedCondition (go/internal/controller/reconciler/status/mcp_server.go:57)


setProgrammedCondition sets the Programmed condition on the MCPServer


```go
func setProgrammedCondition((mcpServer *v1alpha1.MCPServer, programmed bool)) (mcpServer *v1alpha1.MCPServer, programmed bool)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** mcpServer


```json
{
  "URL": "string",
  "Headers": {},
  "ServerType": "string",
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/mcp/registry.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** programmed


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:57`



---


[function] name: setReadyCondition file: go/internal/controller/reconciler/status/mcp_server.go:107 returns_error: нет description: setReadyCondition sets the Ready condition on the MCPServer


### setReadyCondition (go/internal/controller/reconciler/status/mcp_server.go:107)


setReadyCondition sets the Ready condition on the MCPServer


```go
func setReadyCondition((mcpServer *v1alpha1.MCPServer, ready bool, reason v1alpha1.MCPServerConditionReason, message string)) (mcpServer *v1alpha1.MCPServer, ready bool, reason v1alpha1.MCPServerConditionReason, message string)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** mcpServer


```json
{
  "URL": "string",
  "Headers": {},
  "ServerType": "string",
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/mcp/registry.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** ready


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.MCPServerConditionReason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:107`



---


[function] name: setResolvedRefsCondition file: go/internal/controller/reconciler/status/mcp_server.go:48 returns_error: нет description: setResolvedRefsCondition sets the ResolvedRefs condition on the MCPServer


### setResolvedRefsCondition (go/internal/controller/reconciler/status/mcp_server.go:48)


setResolvedRefsCondition sets the ResolvedRefs condition on the MCPServer


```go
func setResolvedRefsCondition((mcpServer *v1alpha1.MCPServer, resolved bool, reason v1alpha1.MCPServerConditionReason, message string)) (mcpServer *v1alpha1.MCPServer, resolved bool, reason v1alpha1.MCPServerConditionReason, message string)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** mcpServer


```json
{
  "URL": "string",
  "Headers": {},
  "ServerType": "string",
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/mcp/registry.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** resolved


```json
{
  "Image": "string",
  "Cmd": "string",
  "Args": [],
  "Port": 0,
  "ImagePullPolicy": {},
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "VolumeMounts": [],
  "Labels": {},
  "Annotations": {},
  "Env": [],
  "Resources": {},
  "Tolerations": [],
  "Affinity": null,
  "NodeSelector": {},
  "SecurityContext": null,
  "PodSecurityContext": null,
  "ServiceAccountName": "string",
  "ServiceAccountConfig": null
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.MCPServerConditionReason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:48`



---


[function] name: updateMCPServerStatus file: go/internal/controller/reconciler/status/mcp_server.go:153 returns_error: нет description: updateMCPServerStatus updates the MCPServer status if it has changed


### updateMCPServerStatus (go/internal/controller/reconciler/status/mcp_server.go:153)


updateMCPServerStatus updates the MCPServer status if it has changed


```go
func updateMCPServerStatus((ctx context.Context, kube client.Client, mcpServer *v1alpha1.MCPServer)) (ctx context.Context, kube client.Client, mcpServer *v1alpha1.MCPServer)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** kube


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** mcpServer


```json
{
  "URL": "string",
  "Headers": {},
  "ServerType": "string",
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/mcp/registry.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


📍 *Расположение:* `go/internal/controller/reconciler/status/mcp_server.go:153`




## go/internal/controller/reconciler/utils/reconciler_utils.go


📄 Исходный файл: `go/internal/controller/reconciler/utils/reconciler_utils.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [DeepEqual](#deepequal-gointernalcontrollerreconcilerutilsreconciler_utilsgo130) `:130`

- 🔗 [FindOwnedObjects](#findownedobjects-gointernalcontrollerreconcilerutilsreconciler_utilsgo170) `:170`

- 🔗 [GetList](#getlist-gointernalcontrollerreconcilerutilsreconciler_utilsgo190) `:190`

- 🔗 [ObjectMetasEqual](#objectmetasequal-gointernalcontrollerreconcilerutilsreconciler_utilsgo81) `:81`

- 🔗 [ObjectsEqual](#objectsequal-gointernalcontrollerreconcilerutilsreconciler_utilsgo30) `:30`

- 🔗 [SetupOwnerIndexes](#setupownerindexes-gointernalcontrollerreconcilerutilsreconciler_utilsgo143) `:143`

- 🔗 [UpsertOutput](#upsertoutput-gointernalcontrollerreconcilerutilsreconciler_utilsgo222) `:222`

- 🔗 [mapStringEqual](#mapstringequal-gointernalcontrollerreconcilerutilsreconciler_utilsgo88) `:88`

- 🔗 [mkPointer](#mkpointer-gointernalcontrollerreconcilerutilsreconciler_utilsgo113) `:113`


</details>


[function] name: DeepEqual file: go/internal/controller/reconciler/utils/reconciler_utils.go:130 returns_error: нет description: DeepEqual should be used in place of reflect.DeepEqual when the type of an object is unknown and may be a proto message.


### DeepEqual (go/internal/controller/reconciler/utils/reconciler_utils.go:130)


DeepEqual should be used in place of reflect.DeepEqual when the type of an object is unknown and may be a proto message.
see https://github.com/golang/protobuf/issues/1173 for details on why reflect.DeepEqual no longer works for proto messages


```go
func DeepEqual((val1, val2 any)) (val1, val2 any)
```


**Тип ответа:** val1


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** val2


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:130`



---


[function] name: FindOwnedObjects file: go/internal/controller/reconciler/utils/reconciler_utils.go:170 returns_error: да description: FindOwnedObjects looks for objects in the given namespace that have an owner
reference. Note: this method assumes that a


### FindOwnedObjects (go/internal/controller/reconciler/utils/reconciler_utils.go:170)


FindOwnedObjects looks for objects in the given namespace that have an owner
reference. Note: this method assumes that an index has been setup for the
owner reference using `SetupOwnerIndexes`.


```go
func FindOwnedObjects((map[types.UID]client.Object, error)) (map[types.UID]client.Object, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.UID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[types.UID]client.Object`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:170`



---


[function] name: GetList file: go/internal/controller/reconciler/utils/reconciler_utils.go:190 returns_error: да description: GetList queries the Kubernetes API to list the requested resource, setting
the list l of type T.


### GetList (go/internal/controller/reconciler/utils/reconciler_utils.go:190)


GetList queries the Kubernetes API to list the requested resource, setting
the list l of type T.


```go
func GetList((map[types.UID]client.Object, error)) (map[types.UID]client.Object, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.UID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[types.UID]client.Object`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:190`



---


[function] name: ObjectMetasEqual file: go/internal/controller/reconciler/utils/reconciler_utils.go:81 returns_error: нет description: returns true if "relevant" parts of obj1 and obj2 have equal:
-labels
-annotations
-namespace+name
or if the objects are


### ObjectMetasEqual (go/internal/controller/reconciler/utils/reconciler_utils.go:81)


returns true if "relevant" parts of obj1 and obj2 have equal:
-labels
-annotations
-namespace+name
or if the objects are not metav1.Objects


```go
func ObjectMetasEqual((obj1, obj2 metav1.Object)) (obj1, obj2 metav1.Object)
```


**Тип ответа:** obj1


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** obj2


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:81`



---


[function] name: ObjectsEqual file: go/internal/controller/reconciler/utils/reconciler_utils.go:30 returns_error: нет description: returns true if "relevant" parts of obj1 and obj2 have equal:
- labels,
- annotations,
- namespace+name,
- non-metadata,


### ObjectsEqual (go/internal/controller/reconciler/utils/reconciler_utils.go:30)


returns true if "relevant" parts of obj1 and obj2 have equal:
- labels,
- annotations,
- namespace+name,
- non-metadata, non-status fields
Note that Status fields are not compared.
To compare status fields, use ObjectStatusesEqual


```go
func ObjectsEqual((obj1, obj2 runtime.Object)) (obj1, obj2 runtime.Object)
```


**Тип ответа:** obj1


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** obj2


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** runtime.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:30`



---


[function] name: SetupOwnerIndexes file: go/internal/controller/reconciler/utils/reconciler_utils.go:143 returns_error: нет description: SetupOwnerIndexes sets up caching and indexing of owned resources.


### SetupOwnerIndexes (go/internal/controller/reconciler/utils/reconciler_utils.go:143)


SetupOwnerIndexes sets up caching and indexing of owned resources.


```go
func SetupOwnerIndexes((mgr ctrl.Manager, ownedTypes []client.Object)) (mgr ctrl.Manager, ownedTypes []client.Object)
```


**Тип ответа:** mgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


**Тип ответа:** ownedTypes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:143`



---


[function] name: UpsertOutput file: go/internal/controller/reconciler/utils/reconciler_utils.go:222 returns_error: нет description: —


### UpsertOutput (go/internal/controller/reconciler/utils/reconciler_utils.go:222)


UpsertOutput is a function that performs operations based on the provided parameters and returns (ctx context.Context, kube client.Client, output client.Object).


```go
func UpsertOutput((ctx context.Context, kube client.Client, output client.Object)) (ctx context.Context, kube client.Client, output client.Object)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** kube


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:222`



---


[function] name: mapStringEqual file: go/internal/controller/reconciler/utils/reconciler_utils.go:88 returns_error: нет description: —


### mapStringEqual (go/internal/controller/reconciler/utils/reconciler_utils.go:88)


mapStringEqual is a function that performs operations based on the provided parameters and returns (map1, map2 map[string]string).


```go
func mapStringEqual((map1, map2 map[string]string)) (map1, map2 map[string]string)
```


**Тип ответа:** map1


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map2


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:88`



---


[function] name: mkPointer file: go/internal/controller/reconciler/utils/reconciler_utils.go:113 returns_error: нет description: if i is a pointer, just return the value.
if i is addressable, return that.
if i is a struct passed in by value, make a 


### mkPointer (go/internal/controller/reconciler/utils/reconciler_utils.go:113)


if i is a pointer, just return the value.
if i is addressable, return that.
if i is a struct passed in by value, make a new instance of the type and copy the contents to that and return
the pointer to that.


```go
func mkPointer((val reflect.Value)) (val reflect.Value)
```


**Тип ответа:** val


```json
{
  "Name": "string",
  "Args": {},
  "ID": "string"
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/hitl.go`


**Тип ответа:** reflect.Value


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/internal/controller/reconciler/utils/reconciler_utils.go:113`




## go/internal/controller/remote_mcp_server_controller.go


📄 Исходный файл: `go/internal/controller/remote_mcp_server_controller.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Reconcile](#reconcile-gointernalcontrollerremote_mcp_server_controllergo43) `:43`

- 🔗 [SetupWithManager](#setupwithmanager-gointernalcontrollerremote_mcp_server_controllergo58) `:58`


</details>


[function] name: Reconcile file: go/internal/controller/remote_mcp_server_controller.go:43 returns_error: да description: +kubebuilder:rbac:groups=kagent.dev,resources=remotemcpservers,verbs=get;list;watch;create;update;patch;delete
+kubebuil


### Reconcile (go/internal/controller/remote_mcp_server_controller.go:43)


+kubebuilder:rbac:groups=kagent.dev,resources=remotemcpservers,verbs=get;list;watch;create;update;patch;delete
+kubebuilder:rbac:groups=kagent.dev,resources=remotemcpservers/status,verbs=get;update;patch
+kubebuilder:rbac:groups=kagent.dev,resources=remotemcpservers/finalizers,verbs=update


```go
func (r *RemoteMCPServerController) Reconcile((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/remote_mcp_server_controller.go:43`



---


[function] name: SetupWithManager file: go/internal/controller/remote_mcp_server_controller.go:58 returns_error: нет description: SetupWithManager sets up the controller with the Manager.


### SetupWithManager (go/internal/controller/remote_mcp_server_controller.go:58)


SetupWithManager sets up the controller with the Manager.


```go
func (r *RemoteMCPServerController) SetupWithManager((mgr ctrl.Manager)) (mgr ctrl.Manager)
```


**Тип ответа:** mgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


📍 *Расположение:* `go/internal/controller/remote_mcp_server_controller.go:58`




## go/internal/controller/service_controller.go


📄 Исходный файл: `go/internal/controller/service_controller.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Reconcile](#reconcile-gointernalcontrollerservice_controllergo45) `:45`

- 🔗 [SetupWithManager](#setupwithmanager-gointernalcontrollerservice_controllergo65) `:65`


</details>


[function] name: Reconcile file: go/internal/controller/service_controller.go:45 returns_error: да description: +kubebuilder:rbac:groups=core,resources=services,verbs=get;list;watch


### Reconcile (go/internal/controller/service_controller.go:45)


+kubebuilder:rbac:groups=core,resources=services,verbs=get;list;watch


```go
func (r *ServiceController) Reconcile((ctrl.Result, error)) (ctrl.Result, error)
```


**Тип ответа:** ctrl.Result


```json
{
  "Name": "string",
  "ID": "string",
  "Response": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctrl.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/service_controller.go:45`



---


[function] name: SetupWithManager file: go/internal/controller/service_controller.go:65 returns_error: нет description: SetupWithManager sets up the controller with the Manager.


### SetupWithManager (go/internal/controller/service_controller.go:65)


SetupWithManager sets up the controller with the Manager.


```go
func (r *ServiceController) SetupWithManager((mgr ctrl.Manager)) (mgr ctrl.Manager)
```


**Тип ответа:** mgr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctrl.Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


📍 *Расположение:* `go/internal/controller/service_controller.go:65`




## go/internal/controller/translator/agent/adk_api_translator.go


📄 Исходный файл: `go/internal/controller/translator/agent/adk_api_translator.go`


<details open>
<summary><b>Функции в этом файле (34)</b></summary>


- 🔗 [Error](#error-gointernalcontrollertranslatoragentadk_api_translatorgo67) `:67`

- 🔗 [GetOwnedResourceTypes](#getownedresourcetypes-gointernalcontrollertranslatoragentadk_api_translatorgo208) `:208`

- 🔗 [Image](#image-gointernalcontrollertranslatoragentadk_api_translatorgo89) `:89`

- 🔗 [NewAdkApiTranslator](#newadkapitranslator-gointernalcontrollertranslatoragentadk_api_translatorgo123) `:123`

- 🔗 [NewValidationError](#newvalidationerror-gointernalcontrollertranslatoragentadk_api_translatorgo76) `:76`

- 🔗 [TranslateAgent](#translateagent-gointernalcontrollertranslatoragentadk_api_translatorgo164) `:164`

- 🔗 [Unwrap](#unwrap-gointernalcontrollertranslatoragentadk_api_translatorgo71) `:71`

- 🔗 [addTLSConfiguration](#addtlsconfiguration-gointernalcontrollertranslatoragentadk_api_translatorgo768) `:768`

- 🔗 [applyProxyURL](#applyproxyurl-gointernalcontrollertranslatoragentadk_api_translatorgo1399) `:1399`

- 🔗 [buildManifest](#buildmanifest-gointernalcontrollertranslatoragentadk_api_translatorgo269) `:269`

- 🔗 [buildSkillsInitContainer](#buildskillsinitcontainer-gointernalcontrollertranslatoragentadk_api_translatorgo1659) `:1659`

- 🔗 [buildSkillsScript](#buildskillsscript-gointernalcontrollertranslatoragentadk_api_translatorgo1570) `:1570`

- 🔗 [collectOtelEnvFromProcess](#collectotelenvfromprocess-gointernalcontrollertranslatoragentadk_api_translatorgo1473) `:1473`

- 🔗 [computeConfigHash](#computeconfighash-gointernalcontrollertranslatoragentadk_api_translatorgo1423) `:1423`

- 🔗 [gitSkillName](#gitskillname-gointernalcontrollertranslatoragentadk_api_translatorgo1509) `:1509`

- 🔗 [isCommitSHA](#iscommitsha-gointernalcontrollertranslatoragentadk_api_translatorgo1501) `:1501`

- 🔗 [isInternalK8sURL](#isinternalk8surl-gointernalcontrollertranslatoragentadk_api_translatorgo1364) `:1364`

- 🔗 [isVisited](#isvisited-gointernalcontrollertranslatoragentadk_api_translatorgo160) `:160`

- 🔗 [mergeDeploymentData](#mergedeploymentdata-gointernalcontrollertranslatoragentadk_api_translatorgo1434) `:1434`

- 🔗 [ociSkillName](#ociskillname-gointernalcontrollertranslatoragentadk_api_translatorgo1580) `:1580`

- 🔗 [populateTLSFields](#populatetlsfields-gointernalcontrollertranslatoragentadk_api_translatorgo748) `:748`

- 🔗 [prepareSkillsInitData](#prepareskillsinitdata-gointernalcontrollertranslatoragentadk_api_translatorgo1597) `:1597`

- 🔗 [resolveRawSystemMessage](#resolverawsystemmessage-gointernalcontrollertranslatoragentadk_api_translatorgo730) `:730`

- 🔗 [runPlugins](#runplugins-gointernalcontrollertranslatoragentadk_api_translatorgo1712) `:1712`

- 🔗 [translateEmbeddingConfig](#translateembeddingconfig-gointernalcontrollertranslatoragentadk_api_translatorgo800) `:800`

- 🔗 [translateInlineAgent](#translateinlineagent-gointernalcontrollertranslatoragentadk_api_translatorgo571) `:571`

- 🔗 [translateMCPServerTarget](#translatemcpservertarget-gointernalcontrollertranslatoragentadk_api_translatorgo1246) `:1246`

- 🔗 [translateModel](#translatemodel-gointernalcontrollertranslatoragentadk_api_translatorgo809) `:809`

- 🔗 [translateRemoteMCPServerTarget](#translateremotemcpservertarget-gointernalcontrollertranslatoragentadk_api_translatorgo1332) `:1332`

- 🔗 [translateSseHttpTool](#translatessehttptool-gointernalcontrollertranslatoragentadk_api_translatorgo1216) `:1216`

- 🔗 [translateStreamableHttpTool](#translatestreamablehttptool-gointernalcontrollertranslatoragentadk_api_translatorgo1182) `:1182`

- 🔗 [validateAgent](#validateagent-gointernalcontrollertranslatoragentadk_api_translatorgo224) `:224`

- 🔗 [validateSubPath](#validatesubpath-gointernalcontrollertranslatoragentadk_api_translatorgo1527) `:1527`

- 🔗 [with](#with-gointernalcontrollertranslatoragentadk_api_translatorgo150) `:150`


</details>


[function] name: Error file: go/internal/controller/translator/agent/adk_api_translator.go:67 returns_error: нет description: —


### Error (go/internal/controller/translator/agent/adk_api_translator.go:67)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e *ValidationError) Error(()) ()
```


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:67`



---


[function] name: GetOwnedResourceTypes file: go/internal/controller/translator/agent/adk_api_translator.go:208 returns_error: нет description: GetOwnedResourceTypes returns all the resource types that may be created for an agent.
Even though this method returns a


### GetOwnedResourceTypes (go/internal/controller/translator/agent/adk_api_translator.go:208)


GetOwnedResourceTypes returns all the resource types that may be created for an agent.
Even though this method returns an array of client.Object, these are (empty)
example structs rather than actual resources.


```go
func (r *adkApiTranslator) GetOwnedResourceTypes(()) ()
```


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:208`



---


[function] name: Image file: go/internal/controller/translator/agent/adk_api_translator.go:89 returns_error: нет description: Image returns the fully qualified image reference (registry/repository:tag).


### Image (go/internal/controller/translator/agent/adk_api_translator.go:89)


Image returns the fully qualified image reference (registry/repository:tag).


```go
func (c ImageConfig) Image(()) ()
```


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:89`



---


[function] name: NewAdkApiTranslator file: go/internal/controller/translator/agent/adk_api_translator.go:123 returns_error: нет description: —


### NewAdkApiTranslator (go/internal/controller/translator/agent/adk_api_translator.go:123)


NewAdkApiTranslator is a function that performs operations based on the provided parameters and returns (kube client.Client, defaultModelConfig types.NamespacedName, plugins []TranslatorPlugin, globalProxyURL string).


```go
func NewAdkApiTranslator((kube client.Client, defaultModelConfig types.NamespacedName, plugins []TranslatorPlugin, globalProxyURL string)) (kube client.Client, defaultModelConfig types.NamespacedName, plugins []TranslatorPlugin, globalProxyURL string)
```


**Тип ответа:** kube


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** defaultModelConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** plugins


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TranslatorPlugin


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** globalProxyURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:123`



---


[function] name: NewValidationError file: go/internal/controller/translator/agent/adk_api_translator.go:76 returns_error: нет description: NewValidationError creates a new ValidationError


### NewValidationError (go/internal/controller/translator/agent/adk_api_translator.go:76)


NewValidationError creates a new ValidationError


```go
func NewValidationError((format string, args ...any)) (format string, args ...any)
```


**Тип ответа:** format


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:76`



---


[function] name: TranslateAgent file: go/internal/controller/translator/agent/adk_api_translator.go:164 returns_error: да description: —


### TranslateAgent (go/internal/controller/translator/agent/adk_api_translator.go:164)


TranslateAgent is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *adkApiTranslator) TranslateAgent((*AgentOutputs, error)) (*AgentOutputs, error)
```


**Тип запроса:** AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


**Тип ответа:** AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgentOutputs`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:164`



---


[function] name: Unwrap file: go/internal/controller/translator/agent/adk_api_translator.go:71 returns_error: нет description: —


### Unwrap (go/internal/controller/translator/agent/adk_api_translator.go:71)


Unwrap is a method that performs operations based on the provided parameters and returns ().


```go
func (e *ValidationError) Unwrap(()) ()
```


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:71`



---


[function] name: addTLSConfiguration file: go/internal/controller/translator/agent/adk_api_translator.go:768 returns_error: нет description: addTLSConfiguration adds TLS certificate volume mounts to modelDeploymentData
when TLS configuration is present in the M


### addTLSConfiguration (go/internal/controller/translator/agent/adk_api_translator.go:768)


addTLSConfiguration adds TLS certificate volume mounts to modelDeploymentData
when TLS configuration is present in the ModelConfig.
Note: TLS configuration fields are now included in agent config JSON via BaseModel,
so this function only handles volume mounting.


```go
func addTLSConfiguration((modelDeploymentData *modelDeploymentData, tlsConfig *v1alpha2.TLSConfig)) (modelDeploymentData *modelDeploymentData, tlsConfig *v1alpha2.TLSConfig)
```


**Тип запроса:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип запроса:** v1alpha2.TLSConfig


```json
{
  "DisableVerify": false,
  "CACertSecretRef": "string",
  "CACertSecretKey": "string",
  "DisableSystemCAs": false
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


**Тип ответа:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** tlsConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.TLSConfig


```json
{
  "DisableVerify": false,
  "CACertSecretRef": "string",
  "CACertSecretKey": "string",
  "DisableSystemCAs": false
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:768`



---


[function] name: applyProxyURL file: go/internal/controller/translator/agent/adk_api_translator.go:1399 returns_error: да description: —


### applyProxyURL (go/internal/controller/translator/agent/adk_api_translator.go:1399)


applyProxyURL is a function that performs operations based on the provided parameters and may return an error.


```go
func applyProxyURL((targetURL string, updatedHeaders map[string]string, err error)) (targetURL string, updatedHeaders map[string]string, err error)
```


**Тип ответа:** targetURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updatedHeaders


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `targetURL string`, `updatedHeaders map[string]string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1399`



---


[function] name: buildManifest file: go/internal/controller/translator/agent/adk_api_translator.go:269 returns_error: да description: —


### buildManifest (go/internal/controller/translator/agent/adk_api_translator.go:269)


buildManifest is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *adkApiTranslator) buildManifest((*AgentOutputs, error)) (*AgentOutputs, error)
```


**Тип запроса:** AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


**Тип ответа:** AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgentOutputs`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:269`



---


[function] name: buildSkillsInitContainer file: go/internal/controller/translator/agent/adk_api_translator.go:1659 returns_error: да description: buildSkillsInitContainer creates the unified init container and associated volumes
for fetching skills from both Git rep


### buildSkillsInitContainer (go/internal/controller/translator/agent/adk_api_translator.go:1659)


buildSkillsInitContainer creates the unified init container and associated volumes
for fetching skills from both Git repositories and OCI registries.
If authSecretRef is non-nil a single Secret volume is created and mounted at /git-auth.


```go
func buildSkillsInitContainer((container corev1.Container, volumes []corev1.Volume, err error)) (container corev1.Container, volumes []corev1.Volume, err error)
```


**Тип ответа:** container


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.Container


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** volumes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.Volume


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `container corev1.Container`, `volumes []corev1.Volume`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1659`



---


[function] name: buildSkillsScript file: go/internal/controller/translator/agent/adk_api_translator.go:1570 returns_error: да description: buildSkillsScript renders the unified skills-init shell script.


### buildSkillsScript (go/internal/controller/translator/agent/adk_api_translator.go:1570)


buildSkillsScript renders the unified skills-init shell script.


```go
func buildSkillsScript((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1570`



---


[function] name: collectOtelEnvFromProcess file: go/internal/controller/translator/agent/adk_api_translator.go:1473 returns_error: нет description: —


### collectOtelEnvFromProcess (go/internal/controller/translator/agent/adk_api_translator.go:1473)


collectOtelEnvFromProcess is a function that performs operations based on the provided parameters and returns ().


```go
func collectOtelEnvFromProcess(()) ()
```


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1473`



---


[function] name: computeConfigHash file: go/internal/controller/translator/agent/adk_api_translator.go:1423 returns_error: нет description: —


### computeConfigHash (go/internal/controller/translator/agent/adk_api_translator.go:1423)


computeConfigHash is a function that performs operations based on the provided parameters and returns (agentCfg, agentCard, secretData []byte).


```go
func computeConfigHash((agentCfg, agentCard, secretData []byte)) (agentCfg, agentCard, secretData []byte)
```


**Тип ответа:** agentCfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** secretData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1423`



---


[function] name: gitSkillName file: go/internal/controller/translator/agent/adk_api_translator.go:1509 returns_error: нет description: gitSkillName returns the directory name for a git skill ref.
If Name is set, it is used; otherwise the last path segment


### gitSkillName (go/internal/controller/translator/agent/adk_api_translator.go:1509)


gitSkillName returns the directory name for a git skill ref.
If Name is set, it is used; otherwise the last path segment of the repo URL
(with any .git suffix stripped) is used.
Query parameters and fragments are stripped before extracting the base name.


```go
func gitSkillName((ref v1alpha2.GitRepo)) (ref v1alpha2.GitRepo)
```


**Тип ответа:** ref


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.GitRepo


```json
{
  "URL": "string",
  "Ref": "string",
  "Path": "string",
  "Name": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1509`



---


[function] name: isCommitSHA file: go/internal/controller/translator/agent/adk_api_translator.go:1501 returns_error: нет description: —


### isCommitSHA (go/internal/controller/translator/agent/adk_api_translator.go:1501)


isCommitSHA is a function that performs operations based on the provided parameters and returns (ref string).


```go
func isCommitSHA((ref string)) (ref string)
```


**Тип ответа:** ref


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1501`



---


[function] name: isInternalK8sURL file: go/internal/controller/translator/agent/adk_api_translator.go:1364 returns_error: нет description: isInternalK8sURL checks if a URL points to an internal Kubernetes service.
Internal k8s URLs follow the pattern: http://


### isInternalK8sURL (go/internal/controller/translator/agent/adk_api_translator.go:1364)


isInternalK8sURL checks if a URL points to an internal Kubernetes service.
Internal k8s URLs follow the pattern: http://{name}.{namespace}:{port} or
http://{name}.{namespace}.svc.cluster.local:{port}
This method checks if the namespace exists in the cluster to determine if it's internal.


```go
func (a *adkApiTranslator) isInternalK8sURL((ctx context.Context, urlStr, namespace string)) (ctx context.Context, urlStr, namespace string)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** urlStr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1364`



---


[function] name: isVisited file: go/internal/controller/translator/agent/adk_api_translator.go:160 returns_error: нет description: —


### isVisited (go/internal/controller/translator/agent/adk_api_translator.go:160)


isVisited is a method that performs operations based on the provided parameters and returns (agentName string).


```go
func (t *tState) isVisited((agentName string)) (agentName string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:160`



---


[function] name: mergeDeploymentData file: go/internal/controller/translator/agent/adk_api_translator.go:1434 returns_error: нет description: mergeDeploymentData adds env vars, volumes, and volume mounts from src into dst,
skipping any that already exist in dst 


### mergeDeploymentData (go/internal/controller/translator/agent/adk_api_translator.go:1434)


mergeDeploymentData adds env vars, volumes, and volume mounts from src into dst,
skipping any that already exist in dst (by name for env/volumes, by mount path for mounts).


```go
func mergeDeploymentData((dst, src *modelDeploymentData)) (dst, src *modelDeploymentData)
```


**Тип запроса:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** dst


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1434`



---


[function] name: ociSkillName file: go/internal/controller/translator/agent/adk_api_translator.go:1580 returns_error: нет description: ociSkillName extracts a skill directory name from an OCI image reference.
It takes the last path component of the repo (


### ociSkillName (go/internal/controller/translator/agent/adk_api_translator.go:1580)


ociSkillName extracts a skill directory name from an OCI image reference.
It takes the last path component of the repo (stripped of tag/digest).


```go
func ociSkillName((imageRef string)) (imageRef string)
```


**Тип ответа:** imageRef


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1580`



---


[function] name: populateTLSFields file: go/internal/controller/translator/agent/adk_api_translator.go:748 returns_error: нет description: populateTLSFields populates TLS configuration fields in the BaseModel
from the ModelConfig TLS spec.


### populateTLSFields (go/internal/controller/translator/agent/adk_api_translator.go:748)


populateTLSFields populates TLS configuration fields in the BaseModel
from the ModelConfig TLS spec.


```go
func populateTLSFields((baseModel *adk.BaseModel, tlsConfig *v1alpha2.TLSConfig)) (baseModel *adk.BaseModel, tlsConfig *v1alpha2.TLSConfig)
```


**Тип запроса:** adk.BaseModel


```json
{
  "Type": "string",
  "Model": "string",
  "Headers": {},
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип запроса:** v1alpha2.TLSConfig


```json
{
  "DisableVerify": false,
  "CACertSecretRef": "string",
  "CACertSecretKey": "string",
  "DisableSystemCAs": false
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


**Тип ответа:** baseModel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adk.BaseModel


```json
{
  "Type": "string",
  "Model": "string",
  "Headers": {},
  "TLSDisableVerify": false,
  "TLSCACertPath": "string",
  "TLSDisableSystemCAs": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** tlsConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.TLSConfig


```json
{
  "DisableVerify": false,
  "CACertSecretRef": "string",
  "CACertSecretKey": "string",
  "DisableSystemCAs": false
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:748`



---


[function] name: prepareSkillsInitData file: go/internal/controller/translator/agent/adk_api_translator.go:1597 returns_error: да description: prepareSkillsInitData converts CRD values to the template-ready data struct.
It validates subPaths and detects duplicate


### prepareSkillsInitData (go/internal/controller/translator/agent/adk_api_translator.go:1597)


prepareSkillsInitData converts CRD values to the template-ready data struct.
It validates subPaths and detects duplicate skill directory names.


```go
func prepareSkillsInitData((skillsInitData, error)) (skillsInitData, error)
```


**Тип ответа:** skillsInitData


```json
{
  "AuthMountPath": "string",
  "GitRefs": [],
  "OCIRefs": [],
  "InsecureOCI": false
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `skillsInitData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1597`



---


[function] name: resolveRawSystemMessage file: go/internal/controller/translator/agent/adk_api_translator.go:730 returns_error: да description: resolveRawSystemMessage gets the raw system message string from the agent spec
without applying any template processing.


### resolveRawSystemMessage (go/internal/controller/translator/agent/adk_api_translator.go:730)


resolveRawSystemMessage gets the raw system message string from the agent spec
without applying any template processing.


```go
func (a *adkApiTranslator) resolveRawSystemMessage((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:730`



---


[function] name: runPlugins file: go/internal/controller/translator/agent/adk_api_translator.go:1712 returns_error: нет description: —


### runPlugins (go/internal/controller/translator/agent/adk_api_translator.go:1712)


runPlugins is a method that performs operations based on the provided parameters and returns (ctx context.Context, agent *v1alpha2.Agent, outputs *AgentOutputs).


```go
func (a *adkApiTranslator) runPlugins((ctx context.Context, agent *v1alpha2.Agent, outputs *AgentOutputs)) (ctx context.Context, agent *v1alpha2.Agent, outputs *AgentOutputs)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип запроса:** AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** outputs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentOutputs


```json
{
  "Manifest": [],
  "Config": null,
  "AgentCard": {}
}
```


*Определено в:* `go/pkg/translator/adk_api_translator_types.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1712`



---


[function] name: translateEmbeddingConfig file: go/internal/controller/translator/agent/adk_api_translator.go:800 returns_error: да description: translateEmbeddingConfig resolves the embedding ModelConfig and returns the
EmbeddingConfig for the Python config JSON, 


### translateEmbeddingConfig (go/internal/controller/translator/agent/adk_api_translator.go:800)


translateEmbeddingConfig resolves the embedding ModelConfig and returns the
EmbeddingConfig for the Python config JSON, the deployment data for the
embedding model, and the raw secret hash bytes (caller decides whether to
include them). The caller should use mergeDeploymentData to combine the
returned deployment data with the existing deployment data.


```go
func (a *adkApiTranslator) translateEmbeddingConfig((*adk.EmbeddingConfig, *modelDeploymentData, []byte, error)) (*adk.EmbeddingConfig, *modelDeploymentData, []byte, error)
```


**Тип запроса:** adk.EmbeddingConfig


```json
{
  "Provider": "string",
  "Model": "string",
  "BaseUrl": "string"
}
```


*Определено в:* `go/pkg/adk/types.go`


**Тип запроса:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** adk.EmbeddingConfig


```json
{
  "Provider": "string",
  "Model": "string",
  "BaseUrl": "string"
}
```


*Определено в:* `go/pkg/adk/types.go`


**Тип ответа:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*adk.EmbeddingConfig`, `*modelDeploymentData`, `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:800`



---


[function] name: translateInlineAgent file: go/internal/controller/translator/agent/adk_api_translator.go:571 returns_error: да description: —


### translateInlineAgent (go/internal/controller/translator/agent/adk_api_translator.go:571)


translateInlineAgent is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *adkApiTranslator) translateInlineAgent((*adk.AgentConfig, *modelDeploymentData, []byte, error)) (*adk.AgentConfig, *modelDeploymentData, []byte, error)
```


**Тип запроса:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип запроса:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*adk.AgentConfig`, `*modelDeploymentData`, `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:571`



---


[function] name: translateMCPServerTarget file: go/internal/controller/translator/agent/adk_api_translator.go:1246 returns_error: нет description: —


### translateMCPServerTarget (go/internal/controller/translator/agent/adk_api_translator.go:1246)


translateMCPServerTarget is a method that performs operations based on the provided parameters and returns (ctx context.Context, agent *adk.AgentConfig, agentNamespace string, toolServer *v1alpha2.McpServerTool, agentHeaders map[string]string, proxyURL string).


```go
func (a *adkApiTranslator) translateMCPServerTarget((ctx context.Context, agent *adk.AgentConfig, agentNamespace string, toolServer *v1alpha2.McpServerTool, agentHeaders map[string]string, proxyURL string)) (ctx context.Context, agent *adk.AgentConfig, agentNamespace string, toolServer *v1alpha2.McpServerTool, agentHeaders map[string]string, proxyURL string)
```


**Тип запроса:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип запроса:** v1alpha2.McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** agentNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** toolServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** agentHeaders


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1246`



---


[function] name: translateModel file: go/internal/controller/translator/agent/adk_api_translator.go:809 returns_error: да description: —


### translateModel (go/internal/controller/translator/agent/adk_api_translator.go:809)


translateModel is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *adkApiTranslator) translateModel((adk.Model, *modelDeploymentData, []byte, error)) (adk.Model, *modelDeploymentData, []byte, error)
```


**Тип запроса:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** adk.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** modelDeploymentData


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `adk.Model`, `*modelDeploymentData`, `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:809`



---


[function] name: translateRemoteMCPServerTarget file: go/internal/controller/translator/agent/adk_api_translator.go:1332 returns_error: нет description: —


### translateRemoteMCPServerTarget (go/internal/controller/translator/agent/adk_api_translator.go:1332)


translateRemoteMCPServerTarget is a method that performs operations based on the provided parameters and returns (ctx context.Context, agent *adk.AgentConfig, remoteMcpServer *v1alpha2.RemoteMCPServer, mcpServerTool *v1alpha2.McpServerTool, agentHeaders map[string]string, proxyURL string).


```go
func (a *adkApiTranslator) translateRemoteMCPServerTarget((ctx context.Context, agent *adk.AgentConfig, remoteMcpServer *v1alpha2.RemoteMCPServer, mcpServerTool *v1alpha2.McpServerTool, agentHeaders map[string]string, proxyURL string)) (ctx context.Context, agent *adk.AgentConfig, remoteMcpServer *v1alpha2.RemoteMCPServer, mcpServerTool *v1alpha2.McpServerTool, agentHeaders map[string]string, proxyURL string)
```


**Тип запроса:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип запроса:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип запроса:** v1alpha2.McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** remoteMcpServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** mcpServerTool


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** agentHeaders


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1332`



---


[function] name: translateSseHttpTool file: go/internal/controller/translator/agent/adk_api_translator.go:1216 returns_error: да description: —


### translateSseHttpTool (go/internal/controller/translator/agent/adk_api_translator.go:1216)


translateSseHttpTool is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *adkApiTranslator) translateSseHttpTool((*adk.SseConnectionParams, error)) (*adk.SseConnectionParams, error)
```


**Тип запроса:** adk.SseConnectionParams


```json
{
  "Url": "string",
  "Headers": {},
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TlsDisableVerify": false,
  "TlsCaCertPath": "string",
  "TlsDisableSystemCas": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** adk.SseConnectionParams


```json
{
  "Url": "string",
  "Headers": {},
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TlsDisableVerify": false,
  "TlsCaCertPath": "string",
  "TlsDisableSystemCas": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*adk.SseConnectionParams`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1216`



---


[function] name: translateStreamableHttpTool file: go/internal/controller/translator/agent/adk_api_translator.go:1182 returns_error: да description: —


### translateStreamableHttpTool (go/internal/controller/translator/agent/adk_api_translator.go:1182)


translateStreamableHttpTool is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *adkApiTranslator) translateStreamableHttpTool((*adk.StreamableHTTPConnectionParams, error)) (*adk.StreamableHTTPConnectionParams, error)
```


**Тип запроса:** adk.StreamableHTTPConnectionParams


```json
{
  "Url": "string",
  "Headers": {},
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TerminateOnClose": false,
  "TlsDisableVerify": false,
  "TlsCaCertPath": "string",
  "TlsDisableSystemCas": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** adk.StreamableHTTPConnectionParams


```json
{
  "Url": "string",
  "Headers": {},
  "Timeout": 0.0,
  "SseReadTimeout": 0.0,
  "TerminateOnClose": false,
  "TlsDisableVerify": false,
  "TlsCaCertPath": "string",
  "TlsDisableSystemCas": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*adk.StreamableHTTPConnectionParams`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1182`



---


[function] name: validateAgent file: go/internal/controller/translator/agent/adk_api_translator.go:224 returns_error: нет description: —


### validateAgent (go/internal/controller/translator/agent/adk_api_translator.go:224)


validateAgent is a method that performs operations based on the provided parameters and returns (ctx context.Context, agent *v1alpha2.Agent, state *tState).


```go
func (a *adkApiTranslator) validateAgent((ctx context.Context, agent *v1alpha2.Agent, state *tState)) (ctx context.Context, agent *v1alpha2.Agent, state *tState)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип запроса:** tState


```json
{
  "depth": 0,
  "visitedAgents": []
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tState


```json
{
  "depth": 0,
  "visitedAgents": []
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:224`



---


[function] name: validateSubPath file: go/internal/controller/translator/agent/adk_api_translator.go:1527 returns_error: нет description: validateSubPath rejects subPath values that are absolute or contain ".." traversal segments.


### validateSubPath (go/internal/controller/translator/agent/adk_api_translator.go:1527)


validateSubPath rejects subPath values that are absolute or contain ".." traversal segments.


```go
func validateSubPath((p string)) (p string)
```


**Тип ответа:** p


```json
{
  "AccessToken": "string",
  "TokenType": "string",
  "ExpiresIn": 0,
  "Scope": "string",
  "IssuedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:1527`



---


[function] name: with file: go/internal/controller/translator/agent/adk_api_translator.go:150 returns_error: нет description: —


### with (go/internal/controller/translator/agent/adk_api_translator.go:150)


with is a method that performs operations based on the provided parameters and returns (agent *v1alpha2.Agent).


```go
func (s *tState) with((agent *v1alpha2.Agent)) (agent *v1alpha2.Agent)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/controller/translator/agent/adk_api_translator.go:150`




## go/internal/controller/translator/agent/conversion.go


📄 Исходный файл: `go/internal/controller/translator/agent/conversion.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ConvertMCPServerToRemoteMCPServer](#convertmcpservertoremotemcpserver-gointernalcontrollertranslatoragentconversiongo67) `:67`

- 🔗 [ConvertServiceToRemoteMCPServer](#convertservicetoremotemcpserver-gointernalcontrollertranslatoragentconversiongo14) `:14`


</details>


[function] name: ConvertMCPServerToRemoteMCPServer file: go/internal/controller/translator/agent/conversion.go:67 returns_error: да description: —


### ConvertMCPServerToRemoteMCPServer (go/internal/controller/translator/agent/conversion.go:67)


ConvertMCPServerToRemoteMCPServer is a function that performs operations based on the provided parameters and may return an error.


```go
func ConvertMCPServerToRemoteMCPServer((*v1alpha2.RemoteMCPServer, error)) (*v1alpha2.RemoteMCPServer, error)
```


**Тип запроса:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1alpha2.RemoteMCPServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/conversion.go:67`



---


[function] name: ConvertServiceToRemoteMCPServer file: go/internal/controller/translator/agent/conversion.go:14 returns_error: да description: —


### ConvertServiceToRemoteMCPServer (go/internal/controller/translator/agent/conversion.go:14)


ConvertServiceToRemoteMCPServer is a function that performs operations based on the provided parameters and may return an error.


```go
func ConvertServiceToRemoteMCPServer((*v1alpha2.RemoteMCPServer, error)) (*v1alpha2.RemoteMCPServer, error)
```


**Тип запроса:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1alpha2.RemoteMCPServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/conversion.go:14`




## go/internal/controller/translator/agent/deployments.go


📄 Исходный файл: `go/internal/controller/translator/agent/deployments.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [checkPullSecretAlreadyPresent](#checkpullsecretalreadypresent-gointernalcontrollertranslatoragentdeploymentsgo147) `:147`

- 🔗 [getDefaultLabels](#getdefaultlabels-gointernalcontrollertranslatoragentdeploymentsgo68) `:68`

- 🔗 [getDefaultResources](#getdefaultresources-gointernalcontrollertranslatoragentdeploymentsgo52) `:52`

- 🔗 [resolveByoDeployment](#resolvebyodeployment-gointernalcontrollertranslatoragentdeploymentsgo158) `:158`

- 🔗 [resolveInlineDeployment](#resolveinlinedeployment-gointernalcontrollertranslatoragentdeploymentsgo78) `:78`


</details>


[function] name: checkPullSecretAlreadyPresent file: go/internal/controller/translator/agent/deployments.go:147 returns_error: нет description: —


### checkPullSecretAlreadyPresent (go/internal/controller/translator/agent/deployments.go:147)


checkPullSecretAlreadyPresent is a function that performs operations based on the provided parameters and returns (spec v1alpha2.DeclarativeDeploymentSpec).


```go
func checkPullSecretAlreadyPresent((spec v1alpha2.DeclarativeDeploymentSpec)) (spec v1alpha2.DeclarativeDeploymentSpec)
```


**Тип ответа:** spec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.DeclarativeDeploymentSpec


```json
{
  "ImageRegistry": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/internal/controller/translator/agent/deployments.go:147`



---


[function] name: getDefaultLabels file: go/internal/controller/translator/agent/deployments.go:68 returns_error: нет description: —


### getDefaultLabels (go/internal/controller/translator/agent/deployments.go:68)


getDefaultLabels is a function that performs operations based on the provided parameters and returns (agentName string, incoming map[string]string).


```go
func getDefaultLabels((agentName string, incoming map[string]string)) (agentName string, incoming map[string]string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** incoming


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/deployments.go:68`



---


[function] name: getDefaultResources file: go/internal/controller/translator/agent/deployments.go:52 returns_error: нет description: getDefaultResources sets default resource requirements if not specified


### getDefaultResources (go/internal/controller/translator/agent/deployments.go:52)


getDefaultResources sets default resource requirements if not specified


```go
func getDefaultResources((spec *corev1.ResourceRequirements)) (spec *corev1.ResourceRequirements)
```


**Тип запроса:** corev1.ResourceRequirements


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** spec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ResourceRequirements


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/agent/deployments.go:52`



---


[function] name: resolveByoDeployment file: go/internal/controller/translator/agent/deployments.go:158 returns_error: да description: —


### resolveByoDeployment (go/internal/controller/translator/agent/deployments.go:158)


resolveByoDeployment is a function that performs operations based on the provided parameters and may return an error.


```go
func resolveByoDeployment((*resolvedDeployment, error)) (*resolvedDeployment, error)
```


**Тип запроса:** resolvedDeployment


```json
{
  "Image": "string",
  "Cmd": "string",
  "Args": [],
  "Port": 0,
  "ImagePullPolicy": {},
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "VolumeMounts": [],
  "Labels": {},
  "Annotations": {},
  "Env": [],
  "Resources": {},
  "Tolerations": [],
  "Affinity": null,
  "NodeSelector": {},
  "SecurityContext": null,
  "PodSecurityContext": null,
  "ServiceAccountName": "string",
  "ServiceAccountConfig": null
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** resolvedDeployment


```json
{
  "Image": "string",
  "Cmd": "string",
  "Args": [],
  "Port": 0,
  "ImagePullPolicy": {},
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "VolumeMounts": [],
  "Labels": {},
  "Annotations": {},
  "Env": [],
  "Resources": {},
  "Tolerations": [],
  "Affinity": null,
  "NodeSelector": {},
  "SecurityContext": null,
  "PodSecurityContext": null,
  "ServiceAccountName": "string",
  "ServiceAccountConfig": null
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*resolvedDeployment`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/deployments.go:158`



---


[function] name: resolveInlineDeployment file: go/internal/controller/translator/agent/deployments.go:78 returns_error: да description: —


### resolveInlineDeployment (go/internal/controller/translator/agent/deployments.go:78)


resolveInlineDeployment is a function that performs operations based on the provided parameters and may return an error.


```go
func resolveInlineDeployment((*resolvedDeployment, error)) (*resolvedDeployment, error)
```


**Тип запроса:** resolvedDeployment


```json
{
  "Image": "string",
  "Cmd": "string",
  "Args": [],
  "Port": 0,
  "ImagePullPolicy": {},
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "VolumeMounts": [],
  "Labels": {},
  "Annotations": {},
  "Env": [],
  "Resources": {},
  "Tolerations": [],
  "Affinity": null,
  "NodeSelector": {},
  "SecurityContext": null,
  "PodSecurityContext": null,
  "ServiceAccountName": "string",
  "ServiceAccountConfig": null
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** resolvedDeployment


```json
{
  "Image": "string",
  "Cmd": "string",
  "Args": [],
  "Port": 0,
  "ImagePullPolicy": {},
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "VolumeMounts": [],
  "Labels": {},
  "Annotations": {},
  "Env": [],
  "Resources": {},
  "Tolerations": [],
  "Affinity": null,
  "NodeSelector": {},
  "SecurityContext": null,
  "PodSecurityContext": null,
  "ServiceAccountName": "string",
  "ServiceAccountConfig": null
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*resolvedDeployment`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/deployments.go:78`




## go/internal/controller/translator/agent/template.go


📄 Исходный файл: `go/internal/controller/translator/agent/template.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [buildTemplateContext](#buildtemplatecontext-gointernalcontrollertranslatoragenttemplatego64) `:64`

- 🔗 [executeSystemMessageTemplate](#executesystemmessagetemplate-gointernalcontrollertranslatoragenttemplatego99) `:99`

- 🔗 [resolvePromptSources](#resolvepromptsources-gointernalcontrollertranslatoragenttemplatego33) `:33`


</details>


[function] name: buildTemplateContext file: go/internal/controller/translator/agent/template.go:64 returns_error: нет description: buildTemplateContext constructs the template context from an Agent resource and its
already-translated AgentConfig. Tool


### buildTemplateContext (go/internal/controller/translator/agent/template.go:64)


buildTemplateContext constructs the template context from an Agent resource and its
already-translated AgentConfig. Tool names are extracted from the config rather than
recomputed from the spec.


```go
func buildTemplateContext((agent *v1alpha2.Agent, cfg *adk.AgentConfig)) (agent *v1alpha2.Agent, cfg *adk.AgentConfig)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип запроса:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adk.AgentConfig


```json
{
  "Model": {},
  "Description": "string",
  "Instruction": "string",
  "HttpTools": [],
  "SseTools": [],
  "RemoteAgents": [],
  "ExecuteCode": false,
  "Stream": false
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


📍 *Расположение:* `go/internal/controller/translator/agent/template.go:64`



---


[function] name: executeSystemMessageTemplate file: go/internal/controller/translator/agent/template.go:99 returns_error: да description: executeSystemMessageTemplate parses and executes the system message as a Go text/template.
The include function resolves


### executeSystemMessageTemplate (go/internal/controller/translator/agent/template.go:99)


executeSystemMessageTemplate parses and executes the system message as a Go text/template.
The include function resolves "source/key" paths from the provided lookup map.
Included content is treated as plain text (no nested template execution).


```go
func executeSystemMessageTemplate((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/template.go:99`



---


[function] name: resolvePromptSources file: go/internal/controller/translator/agent/template.go:33 returns_error: да description: resolvePromptSources fetches all data from the referenced ConfigMaps and builds
a lookup map keyed by "identifier/key" w


### resolvePromptSources (go/internal/controller/translator/agent/template.go:33)


resolvePromptSources fetches all data from the referenced ConfigMaps and builds
a lookup map keyed by "identifier/key" where identifier is the alias (if set) or resource name.


```go
func resolvePromptSources((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/controller/translator/agent/template.go:33`




## go/internal/controller/translator/agent/utils.go


📄 Исходный файл: `go/internal/controller/translator/agent/utils.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetA2AAgentCard](#geta2aagentcard-gointernalcontrollertranslatoragentutilsgo14) `:14`


</details>


[function] name: GetA2AAgentCard file: go/internal/controller/translator/agent/utils.go:14 returns_error: нет description: —


### GetA2AAgentCard (go/internal/controller/translator/agent/utils.go:14)


GetA2AAgentCard is a function that retrieves data based on the provided parameters and returns (agent *v1alpha2.Agent).


```go
func GetA2AAgentCard((agent *v1alpha2.Agent)) (agent *v1alpha2.Agent)
```


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/controller/translator/agent/utils.go:14`




## go/internal/controller/translator/mutate.go


📄 Исходный файл: `go/internal/controller/translator/mutate.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [MutateFuncFor](#mutatefuncfor-gointernalcontrollertranslatormutatego13) `:13`

- 🔗 [mergeWithOverride](#mergewithoverride-gointernalcontrollertranslatormutatego68) `:68`

- 🔗 [mutateConfigMap](#mutateconfigmap-gointernalcontrollertranslatormutatego72) `:72`

- 🔗 [mutateDeployment](#mutatedeployment-gointernalcontrollertranslatormutatego91) `:91`

- 🔗 [mutatePodTemplate](#mutatepodtemplate-gointernalcontrollertranslatormutatego109) `:109`

- 🔗 [mutateSecret](#mutatesecret-gointernalcontrollertranslatormutatego77) `:77`

- 🔗 [mutateService](#mutateservice-gointernalcontrollertranslatormutatego86) `:86`

- 🔗 [mutateServiceAccount](#mutateserviceaccount-gointernalcontrollertranslatormutatego82) `:82`


</details>


[function] name: MutateFuncFor file: go/internal/controller/translator/mutate.go:13 returns_error: нет description: —


### MutateFuncFor (go/internal/controller/translator/mutate.go:13)


MutateFuncFor is a function that performs operations based on the provided parameters and returns (existing, desired client.Object).


```go
func MutateFuncFor((existing, desired client.Object)) (existing, desired client.Object)
```


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desired


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/controller/translator/mutate.go:13`



---


[function] name: mergeWithOverride file: go/internal/controller/translator/mutate.go:68 returns_error: нет description: —


### mergeWithOverride (go/internal/controller/translator/mutate.go:68)


mergeWithOverride is a function that performs operations based on the provided parameters and returns (dst, src any).


```go
func mergeWithOverride((dst, src any)) (dst, src any)
```


**Тип ответа:** dst


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/mutate.go:68`



---


[function] name: mutateConfigMap file: go/internal/controller/translator/mutate.go:72 returns_error: нет description: —


### mutateConfigMap (go/internal/controller/translator/mutate.go:72)


mutateConfigMap is a function that performs operations based on the provided parameters and returns (existing, desired *corev1.ConfigMap).


```go
func mutateConfigMap((existing, desired *corev1.ConfigMap)) (existing, desired *corev1.ConfigMap)
```


**Тип запроса:** corev1.ConfigMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desired


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ConfigMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/mutate.go:72`



---


[function] name: mutateDeployment file: go/internal/controller/translator/mutate.go:91 returns_error: нет description: —


### mutateDeployment (go/internal/controller/translator/mutate.go:91)


mutateDeployment is a function that performs operations based on the provided parameters and returns (existing, desired *appsv1.Deployment).


```go
func mutateDeployment((existing, desired *appsv1.Deployment)) (existing, desired *appsv1.Deployment)
```


**Тип запроса:** appsv1.Deployment


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desired


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appsv1.Deployment


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


📍 *Расположение:* `go/internal/controller/translator/mutate.go:91`



---


[function] name: mutatePodTemplate file: go/internal/controller/translator/mutate.go:109 returns_error: нет description: —


### mutatePodTemplate (go/internal/controller/translator/mutate.go:109)


mutatePodTemplate is a function that performs operations based on the provided parameters and returns (existing, desired *corev1.PodTemplateSpec).


```go
func mutatePodTemplate((existing, desired *corev1.PodTemplateSpec)) (existing, desired *corev1.PodTemplateSpec)
```


**Тип запроса:** corev1.PodTemplateSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desired


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.PodTemplateSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/controller/translator/mutate.go:109`



---


[function] name: mutateSecret file: go/internal/controller/translator/mutate.go:77 returns_error: нет description: —


### mutateSecret (go/internal/controller/translator/mutate.go:77)


mutateSecret is a function that performs operations based on the provided parameters and returns (existing, desired *corev1.Secret).


```go
func mutateSecret((existing, desired *corev1.Secret)) (existing, desired *corev1.Secret)
```


**Тип запроса:** corev1.Secret


```json
{
  "Enabled": false,
  "Provider": "string",
  "File": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desired


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.Secret


```json
{
  "Enabled": false,
  "Provider": "string",
  "File": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/internal/controller/translator/mutate.go:77`



---


[function] name: mutateService file: go/internal/controller/translator/mutate.go:86 returns_error: нет description: —


### mutateService (go/internal/controller/translator/mutate.go:86)


mutateService is a function that performs operations based on the provided parameters and returns (existing, desired *corev1.Service).


```go
func mutateService((existing, desired *corev1.Service)) (existing, desired *corev1.Service)
```


**Тип запроса:** corev1.Service


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/service_controller.go`


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desired


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.Service


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/service_controller.go`


📍 *Расположение:* `go/internal/controller/translator/mutate.go:86`



---


[function] name: mutateServiceAccount file: go/internal/controller/translator/mutate.go:82 returns_error: нет description: —


### mutateServiceAccount (go/internal/controller/translator/mutate.go:82)


mutateServiceAccount is a function that performs operations based on the provided parameters and returns (existing, desired *corev1.ServiceAccount).


```go
func mutateServiceAccount((existing, desired *corev1.ServiceAccount)) (existing, desired *corev1.ServiceAccount)
```


**Тип запроса:** corev1.ServiceAccount


```json
{
  "Labels": {},
  "Annotations": {}
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** existing


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desired


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ServiceAccount


```json
{
  "Labels": {},
  "Annotations": {}
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/internal/controller/translator/mutate.go:82`




## go/internal/database/client.go


📄 Исходный файл: `go/internal/database/client.go`


<details open>
<summary><b>Функции в этом файле (54)</b></summary>


- 🔗 [DeleteAgent](#deleteagent-gointernaldatabaseclientgo73) `:73`

- 🔗 [DeleteAgentMemory](#deleteagentmemory-gointernaldatabaseclientgo692) `:692`

- 🔗 [DeleteCheckpoint](#deletecheckpoint-gointernaldatabaseclientgo482) `:482`

- 🔗 [DeleteMessage](#deletemessage-gointernaldatabaseclientgo290) `:290`

- 🔗 [DeletePushNotification](#deletepushnotification-gointernaldatabaseclientgo410) `:410`

- 🔗 [DeleteSession](#deletesession-gointernaldatabaseclientgo66) `:66`

- 🔗 [DeleteTask](#deletetask-gointernaldatabaseclientgo61) `:61`

- 🔗 [DeleteToolServer](#deletetoolserver-gointernaldatabaseclientgo78) `:78`

- 🔗 [DeleteToolsForServer](#deletetoolsforserver-gointernaldatabaseclientgo84) `:84`

- 🔗 [GetAgent](#getagent-gointernaldatabaseclientgo117) `:117`

- 🔗 [GetCrewAIFlowState](#getcrewaiflowstate-gointernaldatabaseclientgo558) `:558`

- 🔗 [GetMessage](#getmessage-gointernaldatabaseclientgo275) `:275`

- 🔗 [GetPushNotification](#getpushnotification-gointernaldatabaseclientgo375) `:375`

- 🔗 [GetSession](#getsession-gointernaldatabaseclientgo110) `:110`

- 🔗 [GetTask](#gettask-gointernaldatabaseclientgo337) `:337`

- 🔗 [GetTaskMessages](#gettaskmessages-gointernaldatabaseclientgo91) `:91`

- 🔗 [GetTool](#gettool-gointernaldatabaseclientgo122) `:122`

- 🔗 [GetToolServer](#gettoolserver-gointernaldatabaseclientgo127) `:127`

- 🔗 [ListAgentMemories](#listagentmemories-gointernaldatabaseclientgo679) `:679`

- 🔗 [ListAgents](#listagents-gointernaldatabaseclientgo175) `:175`

- 🔗 [ListCheckpoints](#listcheckpoints-gointernaldatabaseclientgo436) `:436`

- 🔗 [ListEventsForSession](#listeventsforsession-gointernaldatabaseclientgo242) `:242`

- 🔗 [ListFeedback](#listfeedback-gointernaldatabaseclientgo132) `:132`

- 🔗 [ListMessagesByContextID](#listmessagesbycontextid-gointernaldatabaseclientgo295) `:295`

- 🔗 [ListMessagesForTask](#listmessagesfortask-gointernaldatabaseclientgo229) `:229`

- 🔗 [ListPushNotifications](#listpushnotifications-gointernaldatabaseclientgo391) `:391`

- 🔗 [ListSessions](#listsessions-gointernaldatabaseclientgo170) `:170`

- 🔗 [ListSessionsForAgent](#listsessionsforagent-gointernaldatabaseclientgo163) `:163`

- 🔗 [ListTasksForSession](#listtasksforsession-gointernaldatabaseclientgo152) `:152`

- 🔗 [ListToolServers](#listtoolservers-gointernaldatabaseclientgo180) `:180`

- 🔗 [ListTools](#listtools-gointernaldatabaseclientgo185) `:185`

- 🔗 [ListToolsForServer](#listtoolsforserver-gointernaldatabaseclientgo190) `:190`

- 🔗 [NewClient](#newclient-gointernaldatabaseclientgo22) `:22`

- 🔗 [PruneExpiredMemories](#pruneexpiredmemories-gointernaldatabaseclientgo651) `:651`

- 🔗 [RefreshToolsForServer](#refreshtoolsforserver-gointernaldatabaseclientgo203) `:203`

- 🔗 [ResetCrewAIMemory](#resetcrewaimemory-gointernaldatabaseclientgo535) `:535`

- 🔗 [SearchAgentMemory](#searchagentmemory-gointernaldatabaseclientgo595) `:595`

- 🔗 [SearchCrewAIMemoryByTask](#searchcrewaimemorybytask-gointernaldatabaseclientgo510) `:510`

- 🔗 [StoreAgent](#storeagent-gointernaldatabaseclientgo42) `:42`

- 🔗 [StoreAgentMemories](#storeagentmemories-gointernaldatabaseclientgo584) `:584`

- 🔗 [StoreAgentMemory](#storeagentmemory-gointernaldatabaseclientgo580) `:580`

- 🔗 [StoreCheckpoint](#storecheckpoint-gointernaldatabaseclientgo415) `:415`

- 🔗 [StoreCheckpointWrites](#storecheckpointwrites-gointernaldatabaseclientgo424) `:424`

- 🔗 [StoreCrewAIFlowState](#storecrewaiflowstate-gointernaldatabaseclientgo549) `:549`

- 🔗 [StoreCrewAIMemory](#storecrewaimemory-gointernaldatabaseclientgo501) `:501`

- 🔗 [StoreEvents](#storeevents-gointernaldatabaseclientgo141) `:141`

- 🔗 [StoreFeedback](#storefeedback-gointernaldatabaseclientgo29) `:29`

- 🔗 [StorePushNotification](#storepushnotification-gointernaldatabaseclientgo359) `:359`

- 🔗 [StoreSession](#storesession-gointernaldatabaseclientgo37) `:37`

- 🔗 [StoreTask](#storetask-gointernaldatabaseclientgo321) `:321`

- 🔗 [StoreTool](#storetool-gointernaldatabaseclientgo56) `:56`

- 🔗 [StoreToolServer](#storetoolserver-gointernaldatabaseclientgo47) `:47`

- 🔗 [TaskExists](#taskexists-gointernaldatabaseclientgo352) `:352`

- 🔗 [deleteAgentMemoryByQuery](#deleteagentmemorybyquery-gointernaldatabaseclientgo703) `:703`


</details>


[function] name: DeleteAgent file: go/internal/database/client.go:73 returns_error: нет description: DeleteAgent deletes an agent by name and user ID


### DeleteAgent (go/internal/database/client.go:73)


DeleteAgent deletes an agent by name and user ID


```go
func (c *clientImpl) DeleteAgent((agentID string)) (agentID string)
```


**Тип ответа:** agentID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:73`



---


[function] name: DeleteAgentMemory file: go/internal/database/client.go:692 returns_error: нет description: —


### DeleteAgentMemory (go/internal/database/client.go:692)


DeleteAgentMemory is a method that deletes data based on the provided parameters and returns (agentName, userID string).


```go
func (c *clientImpl) DeleteAgentMemory((agentName, userID string)) (agentName, userID string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:692`



---


[function] name: DeleteCheckpoint file: go/internal/database/client.go:482 returns_error: нет description: DeleteCheckpoint deletes a checkpoint and its writes atomically


### DeleteCheckpoint (go/internal/database/client.go:482)


DeleteCheckpoint deletes a checkpoint and its writes atomically


```go
func (c *clientImpl) DeleteCheckpoint((userID, threadID string)) (userID, threadID string)
```


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** threadID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:482`



---


[function] name: DeleteMessage file: go/internal/database/client.go:290 returns_error: нет description: DeleteMessage deletes a protocol message from the database


### DeleteMessage (go/internal/database/client.go:290)


DeleteMessage deletes a protocol message from the database


```go
func (c *clientImpl) DeleteMessage((messageID string)) (messageID string)
```


**Тип ответа:** messageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:290`



---


[function] name: DeletePushNotification file: go/internal/database/client.go:410 returns_error: нет description: DeletePushNotification deletes a push notification configuration from the database


### DeletePushNotification (go/internal/database/client.go:410)


DeletePushNotification deletes a push notification configuration from the database


```go
func (c *clientImpl) DeletePushNotification((taskID string)) (taskID string)
```


**Тип ответа:** taskID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:410`



---


[function] name: DeleteSession file: go/internal/database/client.go:66 returns_error: нет description: DeleteSession deletes a session by id and user ID


### DeleteSession (go/internal/database/client.go:66)


DeleteSession deletes a session by id and user ID


```go
func (c *clientImpl) DeleteSession((sessionName string, userID string)) (sessionName string, userID string)
```


**Тип ответа:** sessionName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:66`



---


[function] name: DeleteTask file: go/internal/database/client.go:61 returns_error: нет description: DeleteTask deletes a task by ID


### DeleteTask (go/internal/database/client.go:61)


DeleteTask deletes a task by ID


```go
func (c *clientImpl) DeleteTask((taskID string)) (taskID string)
```


**Тип ответа:** taskID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:61`



---


[function] name: DeleteToolServer file: go/internal/database/client.go:78 returns_error: нет description: DeleteToolServer deletes a tool server by name and user ID


### DeleteToolServer (go/internal/database/client.go:78)


DeleteToolServer deletes a tool server by name and user ID


```go
func (c *clientImpl) DeleteToolServer((serverName string, groupKind string)) (serverName string, groupKind string)
```


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groupKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:78`



---


[function] name: DeleteToolsForServer file: go/internal/database/client.go:84 returns_error: нет description: —


### DeleteToolsForServer (go/internal/database/client.go:84)


DeleteToolsForServer is a method that deletes data based on the provided parameters and returns (serverName string, groupKind string).


```go
func (c *clientImpl) DeleteToolsForServer((serverName string, groupKind string)) (serverName string, groupKind string)
```


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groupKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:84`



---


[function] name: GetAgent file: go/internal/database/client.go:117 returns_error: да description: GetAgent retrieves an agent by name and user ID


### GetAgent (go/internal/database/client.go:117)


GetAgent retrieves an agent by name and user ID


```go
func (c *clientImpl) GetAgent((*dbpkg.Agent, error)) (*dbpkg.Agent, error)
```


**Тип запроса:** dbpkg.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** dbpkg.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*dbpkg.Agent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:117`



---


[function] name: GetCrewAIFlowState file: go/internal/database/client.go:558 returns_error: да description: GetCrewAIFlowState retrieves the most recent CrewAI flow state


### GetCrewAIFlowState (go/internal/database/client.go:558)


GetCrewAIFlowState retrieves the most recent CrewAI flow state


```go
func (c *clientImpl) GetCrewAIFlowState((*dbpkg.CrewAIFlowState, error)) (*dbpkg.CrewAIFlowState, error)
```


**Тип запроса:** dbpkg.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** dbpkg.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*dbpkg.CrewAIFlowState`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:558`



---


[function] name: GetMessage file: go/internal/database/client.go:275 returns_error: да description: GetMessage retrieves a protocol message from the database


### GetMessage (go/internal/database/client.go:275)


GetMessage retrieves a protocol message from the database


```go
func (c *clientImpl) GetMessage((*protocol.Message, error)) (*protocol.Message, error)
```


**Тип запроса:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.Message`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:275`



---


[function] name: GetPushNotification file: go/internal/database/client.go:375 returns_error: да description: GetPushNotification retrieves a push notification configuration from the database


### GetPushNotification (go/internal/database/client.go:375)


GetPushNotification retrieves a push notification configuration from the database


```go
func (c *clientImpl) GetPushNotification((*protocol.TaskPushNotificationConfig, error)) (*protocol.TaskPushNotificationConfig, error)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.TaskPushNotificationConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:375`



---


[function] name: GetSession file: go/internal/database/client.go:110 returns_error: да description: GetSession retrieves a session by name and user ID


### GetSession (go/internal/database/client.go:110)


GetSession retrieves a session by name and user ID


```go
func (c *clientImpl) GetSession((*dbpkg.Session, error)) (*dbpkg.Session, error)
```


**Тип запроса:** dbpkg.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Тип ответа:** dbpkg.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*dbpkg.Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:110`



---


[function] name: GetTask file: go/internal/database/client.go:337 returns_error: да description: GetTask retrieves a MemoryCancellableTask from the database


### GetTask (go/internal/database/client.go:337)


GetTask retrieves a MemoryCancellableTask from the database


```go
func (c *clientImpl) GetTask((*protocol.Task, error)) (*protocol.Task, error)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:337`



---


[function] name: GetTaskMessages file: go/internal/database/client.go:91 returns_error: да description: GetTaskMessages retrieves messages for a specific task


### GetTaskMessages (go/internal/database/client.go:91)


GetTaskMessages retrieves messages for a specific task


```go
func (c *clientImpl) GetTaskMessages(([]*protocol.Message, error)) ([]*protocol.Message, error)
```


**Тип запроса:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*protocol.Message`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:91`



---


[function] name: GetTool file: go/internal/database/client.go:122 returns_error: да description: GetTool retrieves a tool by provider (name) and user ID


### GetTool (go/internal/database/client.go:122)


GetTool retrieves a tool by provider (name) and user ID


```go
func (c *clientImpl) GetTool((*dbpkg.Tool, error)) (*dbpkg.Tool, error)
```


**Тип запроса:** dbpkg.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** dbpkg.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*dbpkg.Tool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:122`



---


[function] name: GetToolServer file: go/internal/database/client.go:127 returns_error: да description: GetToolServer retrieves a tool server by name and user ID


### GetToolServer (go/internal/database/client.go:127)


GetToolServer retrieves a tool server by name and user ID


```go
func (c *clientImpl) GetToolServer((*dbpkg.ToolServer, error)) (*dbpkg.ToolServer, error)
```


**Тип запроса:** dbpkg.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** dbpkg.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*dbpkg.ToolServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:127`



---


[function] name: ListAgentMemories file: go/internal/database/client.go:679 returns_error: да description: —


### ListAgentMemories (go/internal/database/client.go:679)


ListAgentMemories is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (c *clientImpl) ListAgentMemories(([]dbpkg.Memory, error)) ([]dbpkg.Memory, error)
```


**Тип ответа:** dbpkg.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.Memory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:679`



---


[function] name: ListAgents file: go/internal/database/client.go:175 returns_error: да description: ListAgents lists all agents


### ListAgents (go/internal/database/client.go:175)


ListAgents lists all agents


```go
func (c *clientImpl) ListAgents(([]dbpkg.Agent, error)) ([]dbpkg.Agent, error)
```


**Тип ответа:** dbpkg.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.Agent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:175`



---


[function] name: ListCheckpoints file: go/internal/database/client.go:436 returns_error: да description: ListCheckpoints lists checkpoints for a thread, optionally filtered by beforeCheckpointID


### ListCheckpoints (go/internal/database/client.go:436)


ListCheckpoints lists checkpoints for a thread, optionally filtered by beforeCheckpointID


```go
func (c *clientImpl) ListCheckpoints(([]*dbpkg.LangGraphCheckpointTuple, error)) ([]*dbpkg.LangGraphCheckpointTuple, error)
```


**Тип запроса:** dbpkg.LangGraphCheckpointTuple


```json
{
  "Checkpoint": null,
  "Writes": []
}
```


*Определено в:* `go/pkg/database/client.go`


**Тип ответа:** dbpkg.LangGraphCheckpointTuple


```json
{
  "Checkpoint": null,
  "Writes": []
}
```


*Определено в:* `go/pkg/database/client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*dbpkg.LangGraphCheckpointTuple`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:436`



---


[function] name: ListEventsForSession file: go/internal/database/client.go:242 returns_error: да description: ListEventsForSession retrieves events for a specific session
Use Limit with DESC for getting latest events, ASC with no 


### ListEventsForSession (go/internal/database/client.go:242)


ListEventsForSession retrieves events for a specific session
Use Limit with DESC for getting latest events, ASC with no limit for chronological order


```go
func (c *clientImpl) ListEventsForSession(([]*dbpkg.Event, error)) ([]*dbpkg.Event, error)
```


**Тип запроса:** dbpkg.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** dbpkg.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*dbpkg.Event`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:242`



---


[function] name: ListFeedback file: go/internal/database/client.go:132 returns_error: да description: ListFeedback lists all feedback for a user


### ListFeedback (go/internal/database/client.go:132)


ListFeedback lists all feedback for a user


```go
func (c *clientImpl) ListFeedback(([]dbpkg.Feedback, error)) ([]dbpkg.Feedback, error)
```


**Тип ответа:** dbpkg.Feedback


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.Feedback`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:132`



---


[function] name: ListMessagesByContextID file: go/internal/database/client.go:295 returns_error: да description: ListMessagesByContextID retrieves messages by context ID with optional limit


### ListMessagesByContextID (go/internal/database/client.go:295)


ListMessagesByContextID retrieves messages by context ID with optional limit


```go
func (c *clientImpl) ListMessagesByContextID(([]protocol.Message, error)) ([]protocol.Message, error)
```


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]protocol.Message`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:295`



---


[function] name: ListMessagesForTask file: go/internal/database/client.go:229 returns_error: да description: ListMessagesForRun retrieves messages for a specific run (helper method)


### ListMessagesForTask (go/internal/database/client.go:229)


ListMessagesForRun retrieves messages for a specific run (helper method)


```go
func (c *clientImpl) ListMessagesForTask(([]*protocol.Message, error)) ([]*protocol.Message, error)
```


**Тип запроса:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*protocol.Message`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:229`



---


[function] name: ListPushNotifications file: go/internal/database/client.go:391 returns_error: да description: —


### ListPushNotifications (go/internal/database/client.go:391)


ListPushNotifications is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (c *clientImpl) ListPushNotifications(([]*protocol.TaskPushNotificationConfig, error)) ([]*protocol.TaskPushNotificationConfig, error)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*protocol.TaskPushNotificationConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:391`



---


[function] name: ListSessions file: go/internal/database/client.go:170 returns_error: да description: ListSessions lists all sessions for a user


### ListSessions (go/internal/database/client.go:170)


ListSessions lists all sessions for a user


```go
func (c *clientImpl) ListSessions(([]dbpkg.Session, error)) ([]dbpkg.Session, error)
```


**Тип ответа:** dbpkg.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:170`



---


[function] name: ListSessionsForAgent file: go/internal/database/client.go:163 returns_error: да description: —


### ListSessionsForAgent (go/internal/database/client.go:163)


ListSessionsForAgent is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (c *clientImpl) ListSessionsForAgent(([]dbpkg.Session, error)) ([]dbpkg.Session, error)
```


**Тип ответа:** dbpkg.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:163`



---


[function] name: ListTasksForSession file: go/internal/database/client.go:152 returns_error: да description: ListSessionRuns lists all runs for a specific session


### ListTasksForSession (go/internal/database/client.go:152)


ListSessionRuns lists all runs for a specific session


```go
func (c *clientImpl) ListTasksForSession(([]*protocol.Task, error)) ([]*protocol.Task, error)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*protocol.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:152`



---


[function] name: ListToolServers file: go/internal/database/client.go:180 returns_error: да description: ListToolServers lists all tool servers for a user


### ListToolServers (go/internal/database/client.go:180)


ListToolServers lists all tool servers for a user


```go
func (c *clientImpl) ListToolServers(([]dbpkg.ToolServer, error)) ([]dbpkg.ToolServer, error)
```


**Тип ответа:** dbpkg.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.ToolServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:180`



---


[function] name: ListTools file: go/internal/database/client.go:185 returns_error: да description: ListTools lists all tools for a user


### ListTools (go/internal/database/client.go:185)


ListTools lists all tools for a user


```go
func (c *clientImpl) ListTools(([]dbpkg.Tool, error)) ([]dbpkg.Tool, error)
```


**Тип ответа:** dbpkg.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.Tool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:185`



---


[function] name: ListToolsForServer file: go/internal/database/client.go:190 returns_error: да description: ListToolsForServer lists all tools for a specific server and group kind


### ListToolsForServer (go/internal/database/client.go:190)


ListToolsForServer lists all tools for a specific server and group kind


```go
func (c *clientImpl) ListToolsForServer(([]dbpkg.Tool, error)) ([]dbpkg.Tool, error)
```


**Тип ответа:** dbpkg.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.Tool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:190`



---


[function] name: NewClient file: go/internal/database/client.go:22 returns_error: нет description: —


### NewClient (go/internal/database/client.go:22)


NewClient is a function that performs operations based on the provided parameters and returns (dbManager *Manager).


```go
func NewClient((dbManager *Manager)) (dbManager *Manager)
```


**Тип запроса:** Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


**Тип ответа:** dbManager


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


📍 *Расположение:* `go/internal/database/client.go:22`



---


[function] name: PruneExpiredMemories file: go/internal/database/client.go:651 returns_error: нет description: PruneExpiredMemories deletes expired memories if they haven't been accessed enough,
otherwise extends their TTL.


### PruneExpiredMemories (go/internal/database/client.go:651)


PruneExpiredMemories deletes expired memories if they haven't been accessed enough,
otherwise extends their TTL.


```go
func (c *clientImpl) PruneExpiredMemories(()) ()
```


📍 *Расположение:* `go/internal/database/client.go:651`



---


[function] name: RefreshToolsForServer file: go/internal/database/client.go:203 returns_error: нет description: RefreshToolsForServer atomically replaces all tools for a server.
Uses a database transaction to ensure consistency unde


### RefreshToolsForServer (go/internal/database/client.go:203)


RefreshToolsForServer atomically replaces all tools for a server.
Uses a database transaction to ensure consistency under concurrent access.

IMPORTANT: This function should only contain fast database operations.
Network I/O (e.g., fetching tools from remote MCP servers) must happen
BEFORE calling this function, not inside it. Holding a database transaction
during slow operations can cause contention and degrade performance.


```go
func (c *clientImpl) RefreshToolsForServer((serverName string, groupKind string, tools ...*v1alpha2.MCPTool)) (serverName string, groupKind string, tools ...*v1alpha2.MCPTool)
```


**Тип запроса:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groupKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/internal/database/client.go:203`



---


[function] name: ResetCrewAIMemory file: go/internal/database/client.go:535 returns_error: нет description: ResetCrewAIMemory deletes all CrewAI agent memory for a session


### ResetCrewAIMemory (go/internal/database/client.go:535)


ResetCrewAIMemory deletes all CrewAI agent memory for a session


```go
func (c *clientImpl) ResetCrewAIMemory((userID, threadID string)) (userID, threadID string)
```


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** threadID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:535`



---


[function] name: SearchAgentMemory file: go/internal/database/client.go:595 returns_error: да description: —


### SearchAgentMemory (go/internal/database/client.go:595)


SearchAgentMemory is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *clientImpl) SearchAgentMemory(([]dbpkg.AgentMemorySearchResult, error)) ([]dbpkg.AgentMemorySearchResult, error)
```


**Тип ответа:** dbpkg.AgentMemorySearchResult


```json
{
  "Score": 0.0
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]dbpkg.AgentMemorySearchResult`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:595`



---


[function] name: SearchCrewAIMemoryByTask file: go/internal/database/client.go:510 returns_error: да description: SearchCrewAIMemoryByTask searches CrewAI agent memory by task description across all agents for a session


### SearchCrewAIMemoryByTask (go/internal/database/client.go:510)


SearchCrewAIMemoryByTask searches CrewAI agent memory by task description across all agents for a session


```go
func (c *clientImpl) SearchCrewAIMemoryByTask(([]*dbpkg.CrewAIAgentMemory, error)) ([]*dbpkg.CrewAIAgentMemory, error)
```


**Тип запроса:** dbpkg.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** dbpkg.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*dbpkg.CrewAIAgentMemory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:510`



---


[function] name: StoreAgent file: go/internal/database/client.go:42 returns_error: нет description: CreateAgent creates a new agent record


### StoreAgent (go/internal/database/client.go:42)


CreateAgent creates a new agent record


```go
func (c *clientImpl) StoreAgent((agent *dbpkg.Agent)) (agent *dbpkg.Agent)
```


**Тип запроса:** dbpkg.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** dbpkg.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/database/client.go:42`



---


[function] name: StoreAgentMemories file: go/internal/database/client.go:584 returns_error: нет description: —


### StoreAgentMemories (go/internal/database/client.go:584)


StoreAgentMemories is a method that performs operations based on the provided parameters and returns (memories []*dbpkg.Memory).


```go
func (c *clientImpl) StoreAgentMemories((memories []*dbpkg.Memory)) (memories []*dbpkg.Memory)
```


**Тип запроса:** dbpkg.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** memories


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbpkg.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:584`



---


[function] name: StoreAgentMemory file: go/internal/database/client.go:580 returns_error: нет description: AgentMemory methods


### StoreAgentMemory (go/internal/database/client.go:580)


AgentMemory methods


```go
func (c *clientImpl) StoreAgentMemory((memory *dbpkg.Memory)) (memory *dbpkg.Memory)
```


**Тип запроса:** dbpkg.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** memory


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/memory.go`


**Тип ответа:** dbpkg.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:580`



---


[function] name: StoreCheckpoint file: go/internal/database/client.go:415 returns_error: нет description: StoreCheckpoint stores a LangGraph checkpoint and its writes atomically


### StoreCheckpoint (go/internal/database/client.go:415)


StoreCheckpoint stores a LangGraph checkpoint and its writes atomically


```go
func (c *clientImpl) StoreCheckpoint((checkpoint *dbpkg.LangGraphCheckpoint)) (checkpoint *dbpkg.LangGraphCheckpoint)
```


**Тип запроса:** dbpkg.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** checkpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbpkg.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:415`



---


[function] name: StoreCheckpointWrites file: go/internal/database/client.go:424 returns_error: нет description: —


### StoreCheckpointWrites (go/internal/database/client.go:424)


StoreCheckpointWrites is a method that performs operations based on the provided parameters and returns (writes []*dbpkg.LangGraphCheckpointWrite).


```go
func (c *clientImpl) StoreCheckpointWrites((writes []*dbpkg.LangGraphCheckpointWrite)) (writes []*dbpkg.LangGraphCheckpointWrite)
```


**Тип запроса:** dbpkg.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** writes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbpkg.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:424`



---


[function] name: StoreCrewAIFlowState file: go/internal/database/client.go:549 returns_error: нет description: StoreCrewAIFlowState stores CrewAI flow state


### StoreCrewAIFlowState (go/internal/database/client.go:549)


StoreCrewAIFlowState stores CrewAI flow state


```go
func (c *clientImpl) StoreCrewAIFlowState((state *dbpkg.CrewAIFlowState)) (state *dbpkg.CrewAIFlowState)
```


**Тип запроса:** dbpkg.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbpkg.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:549`



---


[function] name: StoreCrewAIMemory file: go/internal/database/client.go:501 returns_error: нет description: StoreCrewAIMemory stores CrewAI agent memory


### StoreCrewAIMemory (go/internal/database/client.go:501)


StoreCrewAIMemory stores CrewAI agent memory


```go
func (c *clientImpl) StoreCrewAIMemory((memory *dbpkg.CrewAIAgentMemory)) (memory *dbpkg.CrewAIAgentMemory)
```


**Тип запроса:** dbpkg.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** memory


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/memory.go`


**Тип ответа:** dbpkg.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:501`



---


[function] name: StoreEvents file: go/internal/database/client.go:141 returns_error: нет description: —


### StoreEvents (go/internal/database/client.go:141)


StoreEvents is a method that performs operations based on the provided parameters and returns (events ...*dbpkg.Event).


```go
func (c *clientImpl) StoreEvents((events ...*dbpkg.Event)) (events ...*dbpkg.Event)
```


**Тип запроса:** dbpkg.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** events


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbpkg.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:141`



---


[function] name: StoreFeedback file: go/internal/database/client.go:29 returns_error: нет description: CreateFeedback creates a new feedback record


### StoreFeedback (go/internal/database/client.go:29)


CreateFeedback creates a new feedback record


```go
func (c *clientImpl) StoreFeedback((feedback *dbpkg.Feedback)) (feedback *dbpkg.Feedback)
```


**Тип запроса:** dbpkg.Feedback


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** feedback


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/feedback.go`


**Тип ответа:** dbpkg.Feedback


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:29`



---


[function] name: StorePushNotification file: go/internal/database/client.go:359 returns_error: нет description: StorePushNotification stores a push notification configuration in the database


### StorePushNotification (go/internal/database/client.go:359)


StorePushNotification stores a push notification configuration in the database


```go
func (c *clientImpl) StorePushNotification((config *protocol.TaskPushNotificationConfig)) (config *protocol.TaskPushNotificationConfig)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:359`



---


[function] name: StoreSession file: go/internal/database/client.go:37 returns_error: нет description: CreateSession creates a new session record


### StoreSession (go/internal/database/client.go:37)


CreateSession creates a new session record


```go
func (c *clientImpl) StoreSession((session *dbpkg.Session)) (session *dbpkg.Session)
```


**Тип запроса:** dbpkg.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Тип ответа:** session


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** dbpkg.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


📍 *Расположение:* `go/internal/database/client.go:37`



---


[function] name: StoreTask file: go/internal/database/client.go:321 returns_error: нет description: StoreTask stores a MemoryCancellableTask in the database


### StoreTask (go/internal/database/client.go:321)


StoreTask stores a MemoryCancellableTask in the database


```go
func (c *clientImpl) StoreTask((task *protocol.Task)) (task *protocol.Task)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** task


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:321`



---


[function] name: StoreTool file: go/internal/database/client.go:56 returns_error: нет description: CreateTool creates a new tool record


### StoreTool (go/internal/database/client.go:56)


CreateTool creates a new tool record


```go
func (c *clientImpl) StoreTool((tool *dbpkg.Tool)) (tool *dbpkg.Tool)
```


**Тип запроса:** dbpkg.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** tool


```json
{
  "Name": "string",
  "ID": "string",
  "Args": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Тип ответа:** dbpkg.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/client.go:56`



---


[function] name: StoreToolServer file: go/internal/database/client.go:47 returns_error: да description: CreateToolServer creates a new tool server record


### StoreToolServer (go/internal/database/client.go:47)


CreateToolServer creates a new tool server record


```go
func (c *clientImpl) StoreToolServer((*dbpkg.ToolServer, error)) (*dbpkg.ToolServer, error)
```


**Тип запроса:** dbpkg.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** dbpkg.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*dbpkg.ToolServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/client.go:47`



---


[function] name: TaskExists file: go/internal/database/client.go:352 returns_error: нет description: TaskExists checks if a task exists in the database


### TaskExists (go/internal/database/client.go:352)


TaskExists checks if a task exists in the database


```go
func (c *clientImpl) TaskExists((taskID string)) (taskID string)
```


**Тип ответа:** taskID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:352`



---


[function] name: deleteAgentMemoryByQuery file: go/internal/database/client.go:703 returns_error: нет description: —


### deleteAgentMemoryByQuery (go/internal/database/client.go:703)


deleteAgentMemoryByQuery is a method that performs operations based on the provided parameters and returns (agentName, userID string).


```go
func (c *clientImpl) deleteAgentMemoryByQuery((agentName, userID string)) (agentName, userID string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/client.go:703`




## go/internal/database/fake/client.go


📄 Исходный файл: `go/internal/database/fake/client.go`


<details open>
<summary><b>Функции в этом файле (62)</b></summary>


- 🔗 [AddTask](#addtask-gointernaldatabasefakeclientgo530) `:530`

- 🔗 [AddTool](#addtool-gointernaldatabasefakeclientgo522) `:522`

- 🔗 [Clear](#clear-gointernaldatabasefakeclientgo538) `:538`

- 🔗 [CreateTool](#createtool-gointernaldatabasefakeclientgo185) `:185`

- 🔗 [DeleteAgent](#deleteagent-gointernaldatabasefakeclientgo204) `:204`

- 🔗 [DeleteAgentMemory](#deleteagentmemory-gointernaldatabasefakeclientgo1020) `:1020`

- 🔗 [DeleteCheckpoint](#deletecheckpoint-gointernaldatabasefakeclientgo703) `:703`

- 🔗 [DeletePushNotification](#deletepushnotification-gointernaldatabasefakeclientgo64) `:64`

- 🔗 [DeleteSession](#deletesession-gointernaldatabasefakeclientgo194) `:194`

- 🔗 [DeleteTask](#deletetask-gointernaldatabasefakeclientgo95) `:95`

- 🔗 [DeleteToolServer](#deletetoolserver-gointernaldatabasefakeclientgo219) `:219`

- 🔗 [DeleteToolsForServer](#deletetoolsforserver-gointernaldatabasefakeclientgo228) `:228`

- 🔗 [GetAgent](#getagent-gointernaldatabasefakeclientgo255) `:255`

- 🔗 [GetCheckpoint](#getcheckpoint-gointernaldatabasefakeclientgo641) `:641`

- 🔗 [GetCrewAIFlowState](#getcrewaiflowstate-gointernaldatabasefakeclientgo886) `:886`

- 🔗 [GetLatestCheckpoint](#getlatestcheckpoint-gointernaldatabasefakeclientgo613) `:613`

- 🔗 [GetPushNotification](#getpushnotification-gointernaldatabasefakeclientgo72) `:72`

- 🔗 [GetSession](#getsession-gointernaldatabasefakeclientgo242) `:242`

- 🔗 [GetTask](#gettask-gointernaldatabasefakeclientgo79) `:79`

- 🔗 [GetTool](#gettool-gointernaldatabasefakeclientgo267) `:267`

- 🔗 [GetToolServer](#gettoolserver-gointernaldatabasefakeclientgo279) `:279`

- 🔗 [ListAgentMemories](#listagentmemories-gointernaldatabasefakeclientgo995) `:995`

- 🔗 [ListAgents](#listagents-gointernaldatabasefakeclientgo356) `:356`

- 🔗 [ListCheckpoints](#listcheckpoints-gointernaldatabasefakeclientgo658) `:658`

- 🔗 [ListEventsForSession](#listeventsforsession-gointernaldatabasefakeclientgo436) `:436`

- 🔗 [ListFeedback](#listfeedback-gointernaldatabasefakeclientgo291) `:291`

- 🔗 [ListPushNotifications](#listpushnotifications-gointernaldatabasefakeclientgo423) `:423`

- 🔗 [ListSessions](#listsessions-gointernaldatabasefakeclientgo322) `:322`

- 🔗 [ListSessionsForAgent](#listsessionsforagent-gointernaldatabasefakeclientgo339) `:339`

- 🔗 [ListTasksForSession](#listtasksforsession-gointernaldatabasefakeclientgo304) `:304`

- 🔗 [ListToolServers](#listtoolservers-gointernaldatabasefakeclientgo371) `:371`

- 🔗 [ListTools](#listtools-gointernaldatabasefakeclientgo386) `:386`

- 🔗 [ListToolsForServer](#listtoolsforserver-gointernaldatabasefakeclientgo401) `:401`

- 🔗 [ListWrites](#listwrites-gointernaldatabasefakeclientgo725) `:725`

- 🔗 [NewClient](#newclient-gointernaldatabasefakeclientgo40) `:40`

- 🔗 [PruneExpiredMemories](#pruneexpiredmemories-gointernaldatabasefakeclientgo1033) `:1033`

- 🔗 [RefreshToolsForServer](#refreshtoolsforserver-gointernaldatabasefakeclientgo460) `:460`

- 🔗 [ResetCrewAIMemory](#resetcrewaimemory-gointernaldatabasefakeclientgo845) `:845`

- 🔗 [SearchAgentMemory](#searchagentmemory-gointernaldatabasefakeclientgo954) `:954`

- 🔗 [SearchCrewAIMemoryByTask](#searchcrewaimemorybytask-gointernaldatabasefakeclientgo768) `:768`

- 🔗 [StoreAgent](#storeagent-gointernaldatabasefakeclientgo142) `:142`

- 🔗 [StoreAgentMemories](#storeagentmemories-gointernaldatabasefakeclientgo919) `:919`

- 🔗 [StoreAgentMemory](#storeagentmemory-gointernaldatabasefakeclientgo906) `:906`

- 🔗 [StoreCheckpoint](#storecheckpoint-gointernaldatabasefakeclientgo572) `:572`

- 🔗 [StoreCheckpointWrites](#storecheckpointwrites-gointernaldatabasefakeclientgo593) `:593`

- 🔗 [StoreCrewAIFlowState](#storecrewaiflowstate-gointernaldatabasefakeclientgo871) `:871`

- 🔗 [StoreCrewAIMemory](#storecrewaimemory-gointernaldatabasefakeclientgo753) `:753`

- 🔗 [StoreEvents](#storeevents-gointernaldatabasefakeclientgo119) `:119`

- 🔗 [StoreFeedback](#storefeedback-gointernaldatabasefakeclientgo104) `:104`

- 🔗 [StorePushNotification](#storepushnotification-gointernaldatabasefakeclientgo167) `:167`

- 🔗 [StoreSession](#storesession-gointernaldatabasefakeclientgo132) `:132`

- 🔗 [StoreTask](#storetask-gointernaldatabasefakeclientgo151) `:151`

- 🔗 [StoreToolServer](#storetoolserver-gointernaldatabasefakeclientgo176) `:176`

- 🔗 [UpdateAgent](#updateagent-gointernaldatabasefakeclientgo504) `:504`

- 🔗 [UpdateSession](#updatesession-gointernaldatabasefakeclientgo485) `:485`

- 🔗 [UpdateTask](#updatetask-gointernaldatabasefakeclientgo513) `:513`

- 🔗 [UpdateToolServer](#updatetoolserver-gointernaldatabasefakeclientgo495) `:495`

- 🔗 [UpsertAgent](#upsertagent-gointernaldatabasefakeclientgo558) `:558`

- 🔗 [checkpointKey](#checkpointkey-gointernaldatabasefakeclientgo567) `:567`

- 🔗 [cosineSimilarity](#cosinesimilarity-gointernaldatabasefakeclientgo935) `:935`

- 🔗 [memoryKey](#memorykey-gointernaldatabasefakeclientgo901) `:901`

- 🔗 [sessionKey](#sessionkey-gointernaldatabasefakeclientgo60) `:60`


</details>


[function] name: AddTask file: go/internal/database/fake/client.go:530 returns_error: нет description: AddTask adds a task for testing purposes


### AddTask (go/internal/database/fake/client.go:530)


AddTask adds a task for testing purposes


```go
func (c *InMemoryFakeClient) AddTask((task *database.Task)) (task *database.Task)
```


**Тип запроса:** database.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** task


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:530`



---


[function] name: AddTool file: go/internal/database/fake/client.go:522 returns_error: нет description: AddTool adds a tool for testing purposes


### AddTool (go/internal/database/fake/client.go:522)


AddTool adds a tool for testing purposes


```go
func (c *InMemoryFakeClient) AddTool((tool *database.Tool)) (tool *database.Tool)
```


**Тип запроса:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** tool


```json
{
  "Name": "string",
  "ID": "string",
  "Args": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Тип ответа:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:522`



---


[function] name: Clear file: go/internal/database/fake/client.go:538 returns_error: нет description: Clear clears all data for testing purposes


### Clear (go/internal/database/fake/client.go:538)


Clear clears all data for testing purposes


```go
func (c *InMemoryFakeClient) Clear(()) ()
```


📍 *Расположение:* `go/internal/database/fake/client.go:538`



---


[function] name: CreateTool file: go/internal/database/fake/client.go:185 returns_error: нет description: CreateTool creates a new tool record


### CreateTool (go/internal/database/fake/client.go:185)


CreateTool creates a new tool record


```go
func (c *InMemoryFakeClient) CreateTool((tool *database.Tool)) (tool *database.Tool)
```


**Тип запроса:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** tool


```json
{
  "Name": "string",
  "ID": "string",
  "Args": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Тип ответа:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:185`



---


[function] name: DeleteAgent file: go/internal/database/fake/client.go:204 returns_error: нет description: DeleteAgent deletes an agent by name


### DeleteAgent (go/internal/database/fake/client.go:204)


DeleteAgent deletes an agent by name


```go
func (c *InMemoryFakeClient) DeleteAgent((agentName string)) (agentName string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:204`



---


[function] name: DeleteAgentMemory file: go/internal/database/fake/client.go:1020 returns_error: нет description: DeleteAgentMemory deletes all agent memory for a given agent and user


### DeleteAgentMemory (go/internal/database/fake/client.go:1020)


DeleteAgentMemory deletes all agent memory for a given agent and user


```go
func (c *InMemoryFakeClient) DeleteAgentMemory((agentName, userID string)) (agentName, userID string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:1020`



---


[function] name: DeleteCheckpoint file: go/internal/database/fake/client.go:703 returns_error: нет description: DeleteCheckpoint deletes a checkpoint and its writes atomically


### DeleteCheckpoint (go/internal/database/fake/client.go:703)


DeleteCheckpoint deletes a checkpoint and its writes atomically


```go
func (c *InMemoryFakeClient) DeleteCheckpoint((userID, threadID string)) (userID, threadID string)
```


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** threadID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:703`



---


[function] name: DeletePushNotification file: go/internal/database/fake/client.go:64 returns_error: нет description: —


### DeletePushNotification (go/internal/database/fake/client.go:64)


DeletePushNotification is a method that deletes data based on the provided parameters and returns (taskID string).


```go
func (c *InMemoryFakeClient) DeletePushNotification((taskID string)) (taskID string)
```


**Тип ответа:** taskID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:64`



---


[function] name: DeleteSession file: go/internal/database/fake/client.go:194 returns_error: нет description: DeleteSession deletes a session by ID and user ID


### DeleteSession (go/internal/database/fake/client.go:194)


DeleteSession deletes a session by ID and user ID


```go
func (c *InMemoryFakeClient) DeleteSession((sessionID string, userID string)) (sessionID string, userID string)
```


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:194`



---


[function] name: DeleteTask file: go/internal/database/fake/client.go:95 returns_error: нет description: —


### DeleteTask (go/internal/database/fake/client.go:95)


DeleteTask is a method that deletes data based on the provided parameters and returns (taskID string).


```go
func (c *InMemoryFakeClient) DeleteTask((taskID string)) (taskID string)
```


**Тип ответа:** taskID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:95`



---


[function] name: DeleteToolServer file: go/internal/database/fake/client.go:219 returns_error: нет description: DeleteToolServer deletes a tool server by name


### DeleteToolServer (go/internal/database/fake/client.go:219)


DeleteToolServer deletes a tool server by name


```go
func (c *InMemoryFakeClient) DeleteToolServer((serverName string, groupKind string)) (serverName string, groupKind string)
```


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groupKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:219`



---


[function] name: DeleteToolsForServer file: go/internal/database/fake/client.go:228 returns_error: нет description: DeleteToolsForServer deletes tools for a tool server by name


### DeleteToolsForServer (go/internal/database/fake/client.go:228)


DeleteToolsForServer deletes tools for a tool server by name


```go
func (c *InMemoryFakeClient) DeleteToolsForServer((serverName string, groupKind string)) (serverName string, groupKind string)
```


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groupKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:228`



---


[function] name: GetAgent file: go/internal/database/fake/client.go:255 returns_error: да description: GetAgent retrieves an agent by name


### GetAgent (go/internal/database/fake/client.go:255)


GetAgent retrieves an agent by name


```go
func (c *InMemoryFakeClient) GetAgent((*database.Agent, error)) (*database.Agent, error)
```


**Тип запроса:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.Agent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:255`



---


[function] name: GetCheckpoint file: go/internal/database/fake/client.go:641 returns_error: да description: GetCheckpoint retrieves a specific checkpoint by ID


### GetCheckpoint (go/internal/database/fake/client.go:641)


GetCheckpoint retrieves a specific checkpoint by ID


```go
func (c *InMemoryFakeClient) GetCheckpoint((*database.LangGraphCheckpoint, []*database.LangGraphCheckpointWrite, error)) (*database.LangGraphCheckpoint, []*database.LangGraphCheckpointWrite, error)
```


**Тип запроса:** database.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип запроса:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.LangGraphCheckpoint`, `[]*database.LangGraphCheckpointWrite`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:641`



---


[function] name: GetCrewAIFlowState file: go/internal/database/fake/client.go:886 returns_error: да description: GetCrewAIFlowState retrieves CrewAI flow state


### GetCrewAIFlowState (go/internal/database/fake/client.go:886)


GetCrewAIFlowState retrieves CrewAI flow state


```go
func (c *InMemoryFakeClient) GetCrewAIFlowState((*database.CrewAIFlowState, error)) (*database.CrewAIFlowState, error)
```


**Тип запроса:** database.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.CrewAIFlowState`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:886`



---


[function] name: GetLatestCheckpoint file: go/internal/database/fake/client.go:613 returns_error: да description: GetLatestCheckpoint retrieves the most recent checkpoint for a thread


### GetLatestCheckpoint (go/internal/database/fake/client.go:613)


GetLatestCheckpoint retrieves the most recent checkpoint for a thread


```go
func (c *InMemoryFakeClient) GetLatestCheckpoint((*database.LangGraphCheckpoint, []*database.LangGraphCheckpointWrite, error)) (*database.LangGraphCheckpoint, []*database.LangGraphCheckpointWrite, error)
```


**Тип запроса:** database.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип запроса:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.LangGraphCheckpoint`, `[]*database.LangGraphCheckpointWrite`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:613`



---


[function] name: GetPushNotification file: go/internal/database/fake/client.go:72 returns_error: да description: —


### GetPushNotification (go/internal/database/fake/client.go:72)


GetPushNotification is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c *InMemoryFakeClient) GetPushNotification((*protocol.TaskPushNotificationConfig, error)) (*protocol.TaskPushNotificationConfig, error)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.TaskPushNotificationConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:72`



---


[function] name: GetSession file: go/internal/database/fake/client.go:242 returns_error: да description: GetSession retrieves a session by ID and user ID


### GetSession (go/internal/database/fake/client.go:242)


GetSession retrieves a session by ID and user ID


```go
func (c *InMemoryFakeClient) GetSession((*database.Session, error)) (*database.Session, error)
```


**Тип запроса:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Тип ответа:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:242`



---


[function] name: GetTask file: go/internal/database/fake/client.go:79 returns_error: да description: —


### GetTask (go/internal/database/fake/client.go:79)


GetTask is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c *InMemoryFakeClient) GetTask((*protocol.Task, error)) (*protocol.Task, error)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*protocol.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:79`



---


[function] name: GetTool file: go/internal/database/fake/client.go:267 returns_error: да description: GetTool retrieves a tool by name


### GetTool (go/internal/database/fake/client.go:267)


GetTool retrieves a tool by name


```go
func (c *InMemoryFakeClient) GetTool((*database.Tool, error)) (*database.Tool, error)
```


**Тип запроса:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.Tool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:267`



---


[function] name: GetToolServer file: go/internal/database/fake/client.go:279 returns_error: да description: GetToolServer retrieves a tool server by name


### GetToolServer (go/internal/database/fake/client.go:279)


GetToolServer retrieves a tool server by name


```go
func (c *InMemoryFakeClient) GetToolServer((*database.ToolServer, error)) (*database.ToolServer, error)
```


**Тип запроса:** database.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.ToolServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:279`



---


[function] name: ListAgentMemories file: go/internal/database/fake/client.go:995 returns_error: да description: ListAgentMemories lists agent memories ordered by access count descending


### ListAgentMemories (go/internal/database/fake/client.go:995)


ListAgentMemories lists agent memories ordered by access count descending


```go
func (c *InMemoryFakeClient) ListAgentMemories(([]database.Memory, error)) ([]database.Memory, error)
```


**Тип ответа:** database.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.Memory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:995`



---


[function] name: ListAgents file: go/internal/database/fake/client.go:356 returns_error: да description: ListAgents lists all agents


### ListAgents (go/internal/database/fake/client.go:356)


ListAgents lists all agents


```go
func (c *InMemoryFakeClient) ListAgents(([]database.Agent, error)) ([]database.Agent, error)
```


**Тип ответа:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.Agent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:356`



---


[function] name: ListCheckpoints file: go/internal/database/fake/client.go:658 returns_error: да description: ListCheckpoints lists checkpoints for a thread, optionally filtered by checkpointID


### ListCheckpoints (go/internal/database/fake/client.go:658)


ListCheckpoints lists checkpoints for a thread, optionally filtered by checkpointID


```go
func (c *InMemoryFakeClient) ListCheckpoints(([]*database.LangGraphCheckpointTuple, error)) ([]*database.LangGraphCheckpointTuple, error)
```


**Тип запроса:** database.LangGraphCheckpointTuple


```json
{
  "Checkpoint": null,
  "Writes": []
}
```


*Определено в:* `go/pkg/database/client.go`


**Тип ответа:** database.LangGraphCheckpointTuple


```json
{
  "Checkpoint": null,
  "Writes": []
}
```


*Определено в:* `go/pkg/database/client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*database.LangGraphCheckpointTuple`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:658`



---


[function] name: ListEventsForSession file: go/internal/database/fake/client.go:436 returns_error: да description: ListEventsForSession retrieves events for a specific session


### ListEventsForSession (go/internal/database/fake/client.go:436)


ListEventsForSession retrieves events for a specific session


```go
func (c *InMemoryFakeClient) ListEventsForSession(([]*database.Event, error)) ([]*database.Event, error)
```


**Тип запроса:** database.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*database.Event`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:436`



---


[function] name: ListFeedback file: go/internal/database/fake/client.go:291 returns_error: да description: ListFeedback lists all feedback for a user


### ListFeedback (go/internal/database/fake/client.go:291)


ListFeedback lists all feedback for a user


```go
func (c *InMemoryFakeClient) ListFeedback(([]database.Feedback, error)) ([]database.Feedback, error)
```


**Тип ответа:** database.Feedback


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.Feedback`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:291`



---


[function] name: ListPushNotifications file: go/internal/database/fake/client.go:423 returns_error: да description: —


### ListPushNotifications (go/internal/database/fake/client.go:423)


ListPushNotifications is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (c *InMemoryFakeClient) ListPushNotifications(([]*protocol.TaskPushNotificationConfig, error)) ([]*protocol.TaskPushNotificationConfig, error)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*protocol.TaskPushNotificationConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:423`



---


[function] name: ListSessions file: go/internal/database/fake/client.go:322 returns_error: да description: ListSessions lists all sessions for a user


### ListSessions (go/internal/database/fake/client.go:322)


ListSessions lists all sessions for a user


```go
func (c *InMemoryFakeClient) ListSessions(([]database.Session, error)) ([]database.Session, error)
```


**Тип ответа:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:322`



---


[function] name: ListSessionsForAgent file: go/internal/database/fake/client.go:339 returns_error: да description: ListSessionsForAgent lists all sessions for an agent


### ListSessionsForAgent (go/internal/database/fake/client.go:339)


ListSessionsForAgent lists all sessions for an agent


```go
func (c *InMemoryFakeClient) ListSessionsForAgent(([]database.Session, error)) ([]database.Session, error)
```


**Тип ответа:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:339`



---


[function] name: ListTasksForSession file: go/internal/database/fake/client.go:304 returns_error: да description: —


### ListTasksForSession (go/internal/database/fake/client.go:304)


ListTasksForSession is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (c *InMemoryFakeClient) ListTasksForSession(([]*protocol.Task, error)) ([]*protocol.Task, error)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*protocol.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:304`



---


[function] name: ListToolServers file: go/internal/database/fake/client.go:371 returns_error: да description: ListToolServers lists all tool servers


### ListToolServers (go/internal/database/fake/client.go:371)


ListToolServers lists all tool servers


```go
func (c *InMemoryFakeClient) ListToolServers(([]database.ToolServer, error)) ([]database.ToolServer, error)
```


**Тип ответа:** database.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.ToolServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:371`



---


[function] name: ListTools file: go/internal/database/fake/client.go:386 returns_error: да description: ListTools lists all tools for a user


### ListTools (go/internal/database/fake/client.go:386)


ListTools lists all tools for a user


```go
func (c *InMemoryFakeClient) ListTools(([]database.Tool, error)) ([]database.Tool, error)
```


**Тип ответа:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.Tool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:386`



---


[function] name: ListToolsForServer file: go/internal/database/fake/client.go:401 returns_error: да description: ListToolsForServer lists all tools for a specific server and toolserver type


### ListToolsForServer (go/internal/database/fake/client.go:401)


ListToolsForServer lists all tools for a specific server and toolserver type


```go
func (c *InMemoryFakeClient) ListToolsForServer(([]database.Tool, error)) ([]database.Tool, error)
```


**Тип ответа:** database.Tool


```json
{
  "ID": "string",
  "ServerName": "string",
  "GroupKind": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Description": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.Tool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:401`



---


[function] name: ListWrites file: go/internal/database/fake/client.go:725 returns_error: да description: ListWrites retrieves writes for a specific checkpoint


### ListWrites (go/internal/database/fake/client.go:725)


ListWrites retrieves writes for a specific checkpoint


```go
func (c *InMemoryFakeClient) ListWrites(([]*database.LangGraphCheckpointWrite, error)) ([]*database.LangGraphCheckpointWrite, error)
```


**Тип запроса:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*database.LangGraphCheckpointWrite`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:725`



---


[function] name: NewClient file: go/internal/database/fake/client.go:40 returns_error: нет description: NewClient creates a new fake database client


### NewClient (go/internal/database/fake/client.go:40)


NewClient creates a new fake database client


```go
func NewClient(()) ()
```


📍 *Расположение:* `go/internal/database/fake/client.go:40`



---


[function] name: PruneExpiredMemories file: go/internal/database/fake/client.go:1033 returns_error: нет description: PruneExpiredMemories removes all memories whose ExpiresAt is in the past


### PruneExpiredMemories (go/internal/database/fake/client.go:1033)


PruneExpiredMemories removes all memories whose ExpiresAt is in the past


```go
func (c *InMemoryFakeClient) PruneExpiredMemories(()) ()
```


📍 *Расположение:* `go/internal/database/fake/client.go:1033`



---


[function] name: RefreshToolsForServer file: go/internal/database/fake/client.go:460 returns_error: нет description: RefreshToolsForServer refreshes a tool server


### RefreshToolsForServer (go/internal/database/fake/client.go:460)


RefreshToolsForServer refreshes a tool server


```go
func (c *InMemoryFakeClient) RefreshToolsForServer((serverName string, groupKind string, tools ...*v1alpha2.MCPTool)) (serverName string, groupKind string, tools ...*v1alpha2.MCPTool)
```


**Тип запроса:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groupKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/internal/database/fake/client.go:460`



---


[function] name: ResetCrewAIMemory file: go/internal/database/fake/client.go:845 returns_error: нет description: ResetCrewAIMemory deletes all CrewAI agent memory for a session


### ResetCrewAIMemory (go/internal/database/fake/client.go:845)


ResetCrewAIMemory deletes all CrewAI agent memory for a session


```go
func (c *InMemoryFakeClient) ResetCrewAIMemory((userID, threadID string)) (userID, threadID string)
```


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** threadID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:845`



---


[function] name: SearchAgentMemory file: go/internal/database/fake/client.go:954 returns_error: да description: SearchAgentMemory searches agent memory by vector similarity


### SearchAgentMemory (go/internal/database/fake/client.go:954)


SearchAgentMemory searches agent memory by vector similarity


```go
func (c *InMemoryFakeClient) SearchAgentMemory(([]database.AgentMemorySearchResult, error)) ([]database.AgentMemorySearchResult, error)
```


**Тип ответа:** database.AgentMemorySearchResult


```json
{
  "Score": 0.0
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]database.AgentMemorySearchResult`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:954`



---


[function] name: SearchCrewAIMemoryByTask file: go/internal/database/fake/client.go:768 returns_error: да description: SearchCrewAIMemoryByTask searches CrewAI agent memory by task description across all agents for a session


### SearchCrewAIMemoryByTask (go/internal/database/fake/client.go:768)


SearchCrewAIMemoryByTask searches CrewAI agent memory by task description across all agents for a session


```go
func (c *InMemoryFakeClient) SearchCrewAIMemoryByTask(([]*database.CrewAIAgentMemory, error)) ([]*database.CrewAIAgentMemory, error)
```


**Тип запроса:** database.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*database.CrewAIAgentMemory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:768`



---


[function] name: StoreAgent file: go/internal/database/fake/client.go:142 returns_error: нет description: StoreAgent creates a new agent record


### StoreAgent (go/internal/database/fake/client.go:142)


StoreAgent creates a new agent record


```go
func (c *InMemoryFakeClient) StoreAgent((agent *database.Agent)) (agent *database.Agent)
```


**Тип запроса:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/database/fake/client.go:142`



---


[function] name: StoreAgentMemories file: go/internal/database/fake/client.go:919 returns_error: нет description: StoreAgentMemories stores multiple agent memories


### StoreAgentMemories (go/internal/database/fake/client.go:919)


StoreAgentMemories stores multiple agent memories


```go
func (c *InMemoryFakeClient) StoreAgentMemories((memories []*database.Memory)) (memories []*database.Memory)
```


**Тип запроса:** database.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** memories


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:919`



---


[function] name: StoreAgentMemory file: go/internal/database/fake/client.go:906 returns_error: нет description: StoreAgentMemory stores agent memory


### StoreAgentMemory (go/internal/database/fake/client.go:906)


StoreAgentMemory stores agent memory


```go
func (c *InMemoryFakeClient) StoreAgentMemory((memory *database.Memory)) (memory *database.Memory)
```


**Тип запроса:** database.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** memory


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/memory.go`


**Тип ответа:** database.Memory


```json
{
  "ID": "string",
  "AgentName": "string",
  "UserID": "string",
  "Content": "string",
  "Embedding": {},
  "Metadata": "string",
  "CreatedAt": {},
  "ExpiresAt": "2023-01-01T00:00:00Z",
  "AccessCount": 0
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:906`



---


[function] name: StoreCheckpoint file: go/internal/database/fake/client.go:572 returns_error: нет description: StoreCheckpoint stores a LangGraph checkpoint


### StoreCheckpoint (go/internal/database/fake/client.go:572)


StoreCheckpoint stores a LangGraph checkpoint


```go
func (c *InMemoryFakeClient) StoreCheckpoint((checkpoint *database.LangGraphCheckpoint)) (checkpoint *database.LangGraphCheckpoint)
```


**Тип запроса:** database.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** checkpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.LangGraphCheckpoint


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "ParentCheckpointID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Metadata": "string",
  "Checkpoint": "string",
  "CheckpointType": "string",
  "Version": 0
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:572`



---


[function] name: StoreCheckpointWrites file: go/internal/database/fake/client.go:593 returns_error: нет description: StoreCheckpointWrites stores checkpoint writes


### StoreCheckpointWrites (go/internal/database/fake/client.go:593)


StoreCheckpointWrites stores checkpoint writes


```go
func (c *InMemoryFakeClient) StoreCheckpointWrites((writes []*database.LangGraphCheckpointWrite)) (writes []*database.LangGraphCheckpointWrite)
```


**Тип запроса:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** writes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.LangGraphCheckpointWrite


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CheckpointNS": "string",
  "CheckpointID": "string",
  "WriteIdx": 0,
  "Value": "string",
  "ValueType": "string",
  "Channel": "string",
  "TaskID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {}
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:593`



---


[function] name: StoreCrewAIFlowState file: go/internal/database/fake/client.go:871 returns_error: нет description: StoreCrewAIFlowState stores CrewAI flow state


### StoreCrewAIFlowState (go/internal/database/fake/client.go:871)


StoreCrewAIFlowState stores CrewAI flow state


```go
func (c *InMemoryFakeClient) StoreCrewAIFlowState((state *database.CrewAIFlowState)) (state *database.CrewAIFlowState)
```


**Тип запроса:** database.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.CrewAIFlowState


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "MethodName": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "StateData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:871`



---


[function] name: StoreCrewAIMemory file: go/internal/database/fake/client.go:753 returns_error: нет description: StoreCrewAIMemory stores CrewAI agent memory


### StoreCrewAIMemory (go/internal/database/fake/client.go:753)


StoreCrewAIMemory stores CrewAI agent memory


```go
func (c *InMemoryFakeClient) StoreCrewAIMemory((memory *database.CrewAIAgentMemory)) (memory *database.CrewAIAgentMemory)
```


**Тип запроса:** database.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** memory


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/memory.go`


**Тип ответа:** database.CrewAIAgentMemory


```json
{
  "UserID": "string",
  "ThreadID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "MemoryData": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:753`



---


[function] name: StoreEvents file: go/internal/database/fake/client.go:119 returns_error: нет description: StoreEvents creates a new event record


### StoreEvents (go/internal/database/fake/client.go:119)


StoreEvents creates a new event record


```go
func (c *InMemoryFakeClient) StoreEvents((events ...*database.Event)) (events ...*database.Event)
```


**Тип запроса:** database.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** events


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.Event


```json
{
  "ID": "string",
  "SessionID": "string",
  "UserID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:119`



---


[function] name: StoreFeedback file: go/internal/database/fake/client.go:104 returns_error: нет description: StoreFeedback creates a new feedback record


### StoreFeedback (go/internal/database/fake/client.go:104)


StoreFeedback creates a new feedback record


```go
func (c *InMemoryFakeClient) StoreFeedback((feedback *database.Feedback)) (feedback *database.Feedback)
```


**Тип запроса:** database.Feedback


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** feedback


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/feedback.go`


**Тип ответа:** database.Feedback


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:104`



---


[function] name: StorePushNotification file: go/internal/database/fake/client.go:167 returns_error: нет description: StorePushNotification creates a new push notification record


### StorePushNotification (go/internal/database/fake/client.go:167)


StorePushNotification creates a new push notification record


```go
func (c *InMemoryFakeClient) StorePushNotification((config *protocol.TaskPushNotificationConfig)) (config *protocol.TaskPushNotificationConfig)
```


**Тип запроса:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.TaskPushNotificationConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:167`



---


[function] name: StoreSession file: go/internal/database/fake/client.go:132 returns_error: нет description: StoreSession creates a new session record


### StoreSession (go/internal/database/fake/client.go:132)


StoreSession creates a new session record


```go
func (c *InMemoryFakeClient) StoreSession((session *database.Session)) (session *database.Session)
```


**Тип запроса:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Тип ответа:** session


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


📍 *Расположение:* `go/internal/database/fake/client.go:132`



---


[function] name: StoreTask file: go/internal/database/fake/client.go:151 returns_error: нет description: StoreTask creates a new task record


### StoreTask (go/internal/database/fake/client.go:151)


StoreTask creates a new task record


```go
func (c *InMemoryFakeClient) StoreTask((task *protocol.Task)) (task *protocol.Task)
```


**Тип запроса:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** task


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:151`



---


[function] name: StoreToolServer file: go/internal/database/fake/client.go:176 returns_error: да description: StoreToolServer creates a new tool server record


### StoreToolServer (go/internal/database/fake/client.go:176)


StoreToolServer creates a new tool server record


```go
func (c *InMemoryFakeClient) StoreToolServer((*database.ToolServer, error)) (*database.ToolServer, error)
```


**Тип запроса:** database.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** database.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*database.ToolServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/fake/client.go:176`



---


[function] name: UpdateAgent file: go/internal/database/fake/client.go:504 returns_error: нет description: UpdateAgent updates an agent record


### UpdateAgent (go/internal/database/fake/client.go:504)


UpdateAgent updates an agent record


```go
func (c *InMemoryFakeClient) UpdateAgent((agent *database.Agent)) (agent *database.Agent)
```


**Тип запроса:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/database/fake/client.go:504`



---


[function] name: UpdateSession file: go/internal/database/fake/client.go:485 returns_error: нет description: UpdateSession updates a session


### UpdateSession (go/internal/database/fake/client.go:485)


UpdateSession updates a session


```go
func (c *InMemoryFakeClient) UpdateSession((session *database.Session)) (session *database.Session)
```


**Тип запроса:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Тип ответа:** session


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** database.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


📍 *Расположение:* `go/internal/database/fake/client.go:485`



---


[function] name: UpdateTask file: go/internal/database/fake/client.go:513 returns_error: нет description: UpdateTask updates a task record


### UpdateTask (go/internal/database/fake/client.go:513)


UpdateTask updates a task record


```go
func (c *InMemoryFakeClient) UpdateTask((task *database.Task)) (task *database.Task)
```


**Тип запроса:** database.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** task


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.Task


```json
{
  "ID": "string",
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Data": "string",
  "SessionID": "string"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:513`



---


[function] name: UpdateToolServer file: go/internal/database/fake/client.go:495 returns_error: нет description: UpdateToolServer updates a tool server


### UpdateToolServer (go/internal/database/fake/client.go:495)


UpdateToolServer updates a tool server


```go
func (c *InMemoryFakeClient) UpdateToolServer((server *database.ToolServer)) (server *database.ToolServer)
```


**Тип запроса:** database.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** server


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.ToolServer


```json
{
  "CreatedAt": {},
  "UpdatedAt": {},
  "DeletedAt": {},
  "Name": "string",
  "GroupKind": "string",
  "Description": "string",
  "LastConnected": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `go/pkg/database/models.go`


📍 *Расположение:* `go/internal/database/fake/client.go:495`



---


[function] name: UpsertAgent file: go/internal/database/fake/client.go:558 returns_error: нет description: UpsertAgent upserts an agent record


### UpsertAgent (go/internal/database/fake/client.go:558)


UpsertAgent upserts an agent record


```go
func (c *InMemoryFakeClient) UpsertAgent((agent *database.Agent)) (agent *database.Agent)
```


**Тип запроса:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** agent


```json
{
  "adkTranslator": {},
  "kube": {},
  "dbClient": {},
  "defaultModelConfig": {},
  "watchedNamespaces": []
}
```


*Определено в:* `go/internal/controller/reconciler/reconciler.go`


**Тип ответа:** database.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/database/fake/client.go:558`



---


[function] name: checkpointKey file: go/internal/database/fake/client.go:567 returns_error: нет description: checkpointKey creates a key for checkpoint storage


### checkpointKey (go/internal/database/fake/client.go:567)


checkpointKey creates a key for checkpoint storage


```go
func (c *InMemoryFakeClient) checkpointKey((userID, threadID, checkpointNS, checkpointID string)) (userID, threadID, checkpointNS, checkpointID string)
```


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** threadID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** checkpointNS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** checkpointID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:567`



---


[function] name: cosineSimilarity file: go/internal/database/fake/client.go:935 returns_error: нет description: cosineSimilarity computes the cosine similarity between two float32 slices.
Returns 0 if either vector has zero magnitud


### cosineSimilarity (go/internal/database/fake/client.go:935)


cosineSimilarity computes the cosine similarity between two float32 slices.
Returns 0 if either vector has zero magnitude.


```go
func cosineSimilarity((a, b []float32)) (a, b []float32)
```


**Тип ответа:** a


```json
{
  "Key": "string",
  "Value": {}
}
```


*Определено в:* `go/internal/database/service.go`


**Тип ответа:** b


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/database/fake/client.go:935`



---


[function] name: memoryKey file: go/internal/database/fake/client.go:901 returns_error: нет description: memoryKey creates a unique key for a memory record


### memoryKey (go/internal/database/fake/client.go:901)


memoryKey creates a unique key for a memory record


```go
func (c *InMemoryFakeClient) memoryKey((agentName, userID, id string)) (agentName, userID, id string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** id


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/internal/database/fake/client.go:901`



---


[function] name: sessionKey file: go/internal/database/fake/client.go:60 returns_error: нет description: —


### sessionKey (go/internal/database/fake/client.go:60)


sessionKey is a method that performs operations based on the provided parameters and returns (sessionID, userID string).


```go
func (c *InMemoryFakeClient) sessionKey((sessionID, userID string)) (sessionID, userID string)
```


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/fake/client.go:60`




## go/internal/database/manager.go


📄 Исходный файл: `go/internal/database/manager.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Close](#close-gointernaldatabasemanagergo227) `:227`

- 🔗 [Initialize](#initialize-gointernaldatabasemanagergo106) `:106`

- 🔗 [NewManager](#newmanager-gointernaldatabasemanagergo52) `:52`

- 🔗 [Reset](#reset-gointernaldatabasemanagergo178) `:178`

- 🔗 [resolveURLFile](#resolveurlfile-gointernaldatabasemanagergo214) `:214`


</details>


[function] name: Close file: go/internal/database/manager.go:227 returns_error: нет description: Close closes the database connection


### Close (go/internal/database/manager.go:227)


Close closes the database connection


```go
func (m *Manager) Close(()) ()
```


📍 *Расположение:* `go/internal/database/manager.go:227`



---


[function] name: Initialize file: go/internal/database/manager.go:106 returns_error: нет description: Initialize sets up the database tables


### Initialize (go/internal/database/manager.go:106)


Initialize sets up the database tables


```go
func (m *Manager) Initialize(()) ()
```


📍 *Расположение:* `go/internal/database/manager.go:106`



---


[function] name: NewManager file: go/internal/database/manager.go:52 returns_error: да description: NewManager creates a new database manager


### NewManager (go/internal/database/manager.go:52)


NewManager creates a new database manager


```go
func NewManager((*Manager, error)) (*Manager, error)
```


**Тип запроса:** Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


**Тип ответа:** Manager


```json
{
  "projectRoot": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Manager`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/manager.go:52`



---


[function] name: Reset file: go/internal/database/manager.go:178 returns_error: нет description: Reset drops all tables and optionally recreates them


### Reset (go/internal/database/manager.go:178)


Reset drops all tables and optionally recreates them


```go
func (m *Manager) Reset((recreateTables bool)) (recreateTables bool)
```


**Тип ответа:** recreateTables


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/database/manager.go:178`



---


[function] name: resolveURLFile file: go/internal/database/manager.go:214 returns_error: да description: resolveURLFile reads a database connection URL from a file and returns the
trimmed contents. Returns an error if the fil


### resolveURLFile (go/internal/database/manager.go:214)


resolveURLFile reads a database connection URL from a file and returns the
trimmed contents. Returns an error if the file cannot be read or is empty.


```go
func resolveURLFile((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/manager.go:214`




## go/internal/database/service.go


📄 Исходный файл: `go/internal/database/service.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [BuildWhereClause](#buildwhereclause-gointernaldatabaseservicego79) `:79`

- 🔗 [delete](#delete-gointernaldatabaseservicego63) `:63`

- 🔗 [get](#get-gointernaldatabaseservicego35) `:35`

- 🔗 [list](#list-gointernaldatabaseservicego20) `:20`

- 🔗 [save](#save-gointernaldatabaseservicego54) `:54`


</details>


[function] name: BuildWhereClause file: go/internal/database/service.go:79 returns_error: нет description: BuildWhereClause is deprecated, use individual Where clauses instead


### BuildWhereClause (go/internal/database/service.go:79)


BuildWhereClause is deprecated, use individual Where clauses instead


```go
func BuildWhereClause((clauses ...Clause)) (clauses ...Clause)
```


**Тип ответа:** clauses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Clause


```json
{
  "Key": "string",
  "Value": {}
}
```


*Определено в:* `go/internal/database/service.go`


📍 *Расположение:* `go/internal/database/service.go:79`



---


[function] name: delete file: go/internal/database/service.go:63 returns_error: нет description: —


### delete (go/internal/database/service.go:63)


delete is a function that performs operations based on the provided parameters and returns (db *gorm.DB, clauses ...Clause).


```go
func delete((db *gorm.DB, clauses ...Clause)) (db *gorm.DB, clauses ...Clause)
```


**Тип запроса:** gorm.DB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** db


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** gorm.DB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clauses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Clause


```json
{
  "Key": "string",
  "Value": {}
}
```


*Определено в:* `go/internal/database/service.go`


📍 *Расположение:* `go/internal/database/service.go:63`



---


[function] name: get file: go/internal/database/service.go:35 returns_error: да description: —


### get (go/internal/database/service.go:35)


get is a function that performs operations based on the provided parameters and may return an error.


```go
func get((*T, error)) (*T, error)
```


**Тип запроса:** T


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** T


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*T`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/service.go:35`



---


[function] name: list file: go/internal/database/service.go:20 returns_error: да description: —


### list (go/internal/database/service.go:20)


list is a function that performs operations based on the provided parameters and may return an error.


```go
func list(([]T, error)) ([]T, error)
```


**Тип ответа:** T


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]T`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/database/service.go:20`



---


[function] name: save file: go/internal/database/service.go:54 returns_error: нет description: save performs an upsert operation (INSERT ON CONFLICT DO UPDATE)
args:
- db: the database connection
- model: the model 


### save (go/internal/database/service.go:54)


save performs an upsert operation (INSERT ON CONFLICT DO UPDATE)
args:
- db: the database connection
- model: the model to save


```go
func save((db *gorm.DB, model *T)) (db *gorm.DB, model *T)
```


**Тип запроса:** gorm.DB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** T


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** db


```json
{
  "UserID": "string",
  "MessageID": 0,
  "IsPositive": false,
  "FeedbackText": "string",
  "IssueType": null
}
```


*Определено в:* `go/pkg/database/models.go`


**Тип ответа:** gorm.DB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** model


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Тип ответа:** T


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/database/service.go:54`




## go/internal/goruntime/cpu.go


📄 Исходный файл: `go/internal/goruntime/cpu.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetMaxProcs](#setmaxprocs-gointernalgoruntimecpugo11) `:11`


</details>


[function] name: SetMaxProcs file: go/internal/goruntime/cpu.go:11 returns_error: нет description: —


### SetMaxProcs (go/internal/goruntime/cpu.go:11)


SetMaxProcs is a function that updates data based on the provided parameters and returns (logger logr.Logger).


```go
func SetMaxProcs((logger logr.Logger)) (logger logr.Logger)
```


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/goruntime/cpu.go:11`




## go/internal/httpserver/auth/authn.go


📄 Исходный файл: `go/internal/httpserver/auth/authn.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [A2ARequestHandler](#a2arequesthandler-gointernalhttpserverauthauthngo82) `:82`

- 🔗 [Authenticate](#authenticate-gointernalhttpserverauthauthngo24) `:24`

- 🔗 [Handle](#handle-gointernalhttpserverauthauthngo78) `:78`

- 🔗 [NewA2AAuthenticator](#newa2aauthenticator-gointernalhttpserverauthauthngo62) `:62`

- 🔗 [Principal](#principal-gointernalhttpserverauthauthngo18) `:18`

- 🔗 [UpstreamAuth](#upstreamauth-gointernalhttpserverauthauthngo48) `:48`

- 🔗 [Wrap](#wrap-gointernalhttpserverauthauthngo72) `:72`


</details>


[function] name: A2ARequestHandler file: go/internal/httpserver/auth/authn.go:82 returns_error: нет description: —


### A2ARequestHandler (go/internal/httpserver/auth/authn.go:82)


A2ARequestHandler is a function that performs operations based on the provided parameters and returns (authProvider auth.AuthProvider, agentNns types.NamespacedName).


```go
func A2ARequestHandler((authProvider auth.AuthProvider, agentNns types.NamespacedName)) (authProvider auth.AuthProvider, agentNns types.NamespacedName)
```


**Тип ответа:** authProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.AuthProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agentNns


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/auth/authn.go:82`



---


[function] name: Authenticate file: go/internal/httpserver/auth/authn.go:24 returns_error: да description: —


### Authenticate (go/internal/httpserver/auth/authn.go:24)


Authenticate is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *UnsecureAuthenticator) Authenticate((auth.Session, error)) (auth.Session, error)
```


**Тип ответа:** auth.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `auth.Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/auth/authn.go:24`



---


[function] name: Handle file: go/internal/httpserver/auth/authn.go:78 returns_error: да description: —


### Handle (go/internal/httpserver/auth/authn.go:78)


Handle is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h handler) Handle((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "AccessToken": "string",
  "TokenType": "string",
  "ExpiresIn": 0,
  "Scope": "string",
  "IssuedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Response


```json
{
  "AccessToken": "string",
  "TokenType": "string",
  "ExpiresIn": 0,
  "Scope": "string",
  "IssuedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/auth/authn.go:78`



---


[function] name: NewA2AAuthenticator file: go/internal/httpserver/auth/authn.go:62 returns_error: нет description: —


### NewA2AAuthenticator (go/internal/httpserver/auth/authn.go:62)


NewA2AAuthenticator is a function that performs operations based on the provided parameters and returns (provider auth.AuthProvider).


```go
func NewA2AAuthenticator((provider auth.AuthProvider)) (provider auth.AuthProvider)
```


**Тип ответа:** provider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.AuthProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/auth/authn.go:62`



---


[function] name: Principal file: go/internal/httpserver/auth/authn.go:18 returns_error: нет description: —


### Principal (go/internal/httpserver/auth/authn.go:18)


Principal is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SimpleSession) Principal(()) ()
```


📍 *Расположение:* `go/internal/httpserver/auth/authn.go:18`



---


[function] name: UpstreamAuth file: go/internal/httpserver/auth/authn.go:48 returns_error: нет description: —


### UpstreamAuth (go/internal/httpserver/auth/authn.go:48)


UpstreamAuth is a method that performs operations based on the provided parameters and returns (r *http.Request, session auth.Session, upstreamPrincipal auth.Principal).


```go
func (a *UnsecureAuthenticator) UpstreamAuth((r *http.Request, session auth.Session, upstreamPrincipal auth.Principal)) (r *http.Request, session auth.Session, upstreamPrincipal auth.Principal)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** session


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** auth.Session


```json
{
  "ID": "string",
  "UserID": "string",
  "AppName": "string",
  "State": {},
  "Events": []
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Тип ответа:** upstreamPrincipal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.Principal


```json
{
  "User": {},
  "Agent": {}
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/httpserver/auth/authn.go:48`



---


[function] name: Wrap file: go/internal/httpserver/auth/authn.go:72 returns_error: нет description: —


### Wrap (go/internal/httpserver/auth/authn.go:72)


Wrap is a method that performs operations based on the provided parameters and returns (next http.Handler).


```go
func (p *A2AAuthenticator) Wrap((next http.Handler)) (next http.Handler)
```


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Handler


```json
{
  "kubeClient": {},
  "a2aBaseURL": "string",
  "authenticator": {},
  "httpHandler": null,
  "server": null,
  "a2aClients": {}
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


📍 *Расположение:* `go/internal/httpserver/auth/authn.go:72`




## go/internal/httpserver/auth/authz.go


📄 Исходный файл: `go/internal/httpserver/auth/authz.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Check](#check-gointernalhttpserverauthauthzgo11) `:11`


</details>


[function] name: Check file: go/internal/httpserver/auth/authz.go:11 returns_error: нет description: —


### Check (go/internal/httpserver/auth/authz.go:11)


Check is a method that performs operations based on the provided parameters and returns (ctx context.Context, principal auth.Principal, verb auth.Verb, resource auth.Resource).


```go
func (a *NoopAuthorizer) Check((ctx context.Context, principal auth.Principal, verb auth.Verb, resource auth.Resource)) (ctx context.Context, principal auth.Principal, verb auth.Verb, resource auth.Resource)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** principal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.Principal


```json
{
  "User": {},
  "Agent": {}
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** verb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.Verb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resource


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.Resource


```json
{
  "Name": "string",
  "Type": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/httpserver/auth/authz.go:11`




## go/internal/httpserver/errors/errors.go


📄 Исходный файл: `go/internal/httpserver/errors/errors.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Error](#error-gointernalhttpservererrorserrorsgo16) `:16`

- 🔗 [NewBadRequestError](#newbadrequesterror-gointernalhttpservererrorserrorsgo34) `:34`

- 🔗 [NewConflictError](#newconflicterror-gointernalhttpservererrorserrorsgo69) `:69`

- 🔗 [NewForbiddenError](#newforbiddenerror-gointernalhttpservererrorserrorsgo85) `:85`

- 🔗 [NewInternalServerError](#newinternalservererror-gointernalhttpservererrorserrorsgo52) `:52`

- 🔗 [NewNotFoundError](#newnotfounderror-gointernalhttpservererrorserrorsgo43) `:43`

- 🔗 [NewNotImplementedError](#newnotimplementederror-gointernalhttpservererrorserrorsgo77) `:77`

- 🔗 [NewValidationError](#newvalidationerror-gointernalhttpservererrorserrorsgo61) `:61`

- 🔗 [StatusCode](#statuscode-gointernalhttpservererrorserrorsgo29) `:29`

- 🔗 [Unwrap](#unwrap-gointernalhttpservererrorserrorsgo24) `:24`


</details>


[function] name: Error file: go/internal/httpserver/errors/errors.go:16 returns_error: нет description: Error implements the error interface


### Error (go/internal/httpserver/errors/errors.go:16)


Error implements the error interface


```go
func (e *APIError) Error(()) ()
```


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:16`



---


[function] name: NewBadRequestError file: go/internal/httpserver/errors/errors.go:34 returns_error: да description: NewBadRequestError creates a new bad request error


### NewBadRequestError (go/internal/httpserver/errors/errors.go:34)


NewBadRequestError creates a new bad request error


```go
func NewBadRequestError((message string, err error)) (message string, err error)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `message string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:34`



---


[function] name: NewConflictError file: go/internal/httpserver/errors/errors.go:69 returns_error: да description: —


### NewConflictError (go/internal/httpserver/errors/errors.go:69)


NewConflictError is a function that performs operations based on the provided parameters and may return an error.


```go
func NewConflictError((message string, err error)) (message string, err error)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `message string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:69`



---


[function] name: NewForbiddenError file: go/internal/httpserver/errors/errors.go:85 returns_error: да description: —


### NewForbiddenError (go/internal/httpserver/errors/errors.go:85)


NewForbiddenError is a function that performs operations based on the provided parameters and may return an error.


```go
func NewForbiddenError((message string, err error)) (message string, err error)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `message string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:85`



---


[function] name: NewInternalServerError file: go/internal/httpserver/errors/errors.go:52 returns_error: да description: NewInternalServerError creates a new internal server error


### NewInternalServerError (go/internal/httpserver/errors/errors.go:52)


NewInternalServerError creates a new internal server error


```go
func NewInternalServerError((message string, err error)) (message string, err error)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `message string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:52`



---


[function] name: NewNotFoundError file: go/internal/httpserver/errors/errors.go:43 returns_error: да description: NewNotFoundError creates a new not found error


### NewNotFoundError (go/internal/httpserver/errors/errors.go:43)


NewNotFoundError creates a new not found error


```go
func NewNotFoundError((message string, err error)) (message string, err error)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `message string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:43`



---


[function] name: NewNotImplementedError file: go/internal/httpserver/errors/errors.go:77 returns_error: да description: —


### NewNotImplementedError (go/internal/httpserver/errors/errors.go:77)


NewNotImplementedError is a function that performs operations based on the provided parameters and may return an error.


```go
func NewNotImplementedError((message string, err error)) (message string, err error)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `message string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:77`



---


[function] name: NewValidationError file: go/internal/httpserver/errors/errors.go:61 returns_error: да description: NewValidationError creates a new validation error


### NewValidationError (go/internal/httpserver/errors/errors.go:61)


NewValidationError creates a new validation error


```go
func NewValidationError((message string, err error)) (message string, err error)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `message string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:61`



---


[function] name: StatusCode file: go/internal/httpserver/errors/errors.go:29 returns_error: нет description: StatusCode returns the HTTP status code


### StatusCode (go/internal/httpserver/errors/errors.go:29)


StatusCode returns the HTTP status code


```go
func (e *APIError) StatusCode(()) ()
```


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:29`



---


[function] name: Unwrap file: go/internal/httpserver/errors/errors.go:24 returns_error: нет description: Unwrap returns the wrapped error


### Unwrap (go/internal/httpserver/errors/errors.go:24)


Unwrap returns the wrapped error


```go
func (e *APIError) Unwrap(()) ()
```


📍 *Расположение:* `go/internal/httpserver/errors/errors.go:24`




## go/internal/httpserver/handlers/agents.go


📄 Исходный файл: `go/internal/httpserver/handlers/agents.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [HandleCreateAgent](#handlecreateagent-gointernalhttpserverhandlersagentsgo165) `:165`

- 🔗 [HandleDeleteAgent](#handledeleteagent-gointernalhttpserverhandlersagentsgo288) `:288`

- 🔗 [HandleGetAgent](#handlegetagent-gointernalhttpserverhandlersagentsgo119) `:119`

- 🔗 [HandleListAgents](#handlelistagents-gointernalhttpserverhandlersagentsgo31) `:31`

- 🔗 [HandleUpdateAgent](#handleupdateagent-gointernalhttpserverhandlersagentsgo226) `:226`

- 🔗 [NewAgentsHandler](#newagentshandler-gointernalhttpserverhandlersagentsgo26) `:26`

- 🔗 [getAgentResponse](#getagentresponse-gointernalhttpserverhandlersagentsgo62) `:62`


</details>


[function] name: HandleCreateAgent file: go/internal/httpserver/handlers/agents.go:165 returns_error: нет description: HandleCreateAgent handles POST /api/agents requests using database


### HandleCreateAgent (go/internal/httpserver/handlers/agents.go:165)


HandleCreateAgent handles POST /api/agents requests using database


```go
func (h *AgentsHandler) HandleCreateAgent((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/agents.go:165`



---


[function] name: HandleDeleteAgent file: go/internal/httpserver/handlers/agents.go:288 returns_error: нет description: HandleDeleteAgent handles DELETE /api/agents/{namespace}/{name} requests using database


### HandleDeleteAgent (go/internal/httpserver/handlers/agents.go:288)


HandleDeleteAgent handles DELETE /api/agents/{namespace}/{name} requests using database


```go
func (h *AgentsHandler) HandleDeleteAgent((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/agents.go:288`



---


[function] name: HandleGetAgent file: go/internal/httpserver/handlers/agents.go:119 returns_error: нет description: HandleGetAgent handles GET /api/agents/{namespace}/{name} requests using database


### HandleGetAgent (go/internal/httpserver/handlers/agents.go:119)


HandleGetAgent handles GET /api/agents/{namespace}/{name} requests using database


```go
func (h *AgentsHandler) HandleGetAgent((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/agents.go:119`



---


[function] name: HandleListAgents file: go/internal/httpserver/handlers/agents.go:31 returns_error: нет description: HandleListAgents handles GET /api/agents requests using database


### HandleListAgents (go/internal/httpserver/handlers/agents.go:31)


HandleListAgents handles GET /api/agents requests using database


```go
func (h *AgentsHandler) HandleListAgents((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/agents.go:31`



---


[function] name: HandleUpdateAgent file: go/internal/httpserver/handlers/agents.go:226 returns_error: нет description: HandleUpdateAgent handles PUT /api/agents/{namespace}/{name} requests using database


### HandleUpdateAgent (go/internal/httpserver/handlers/agents.go:226)


HandleUpdateAgent handles PUT /api/agents/{namespace}/{name} requests using database


```go
func (h *AgentsHandler) HandleUpdateAgent((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/agents.go:226`



---


[function] name: NewAgentsHandler file: go/internal/httpserver/handlers/agents.go:26 returns_error: нет description: NewAgentsHandler creates a new AgentsHandler


### NewAgentsHandler (go/internal/httpserver/handlers/agents.go:26)


NewAgentsHandler creates a new AgentsHandler


```go
func NewAgentsHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/agents.go:26`



---


[function] name: getAgentResponse file: go/internal/httpserver/handlers/agents.go:62 returns_error: да description: —


### getAgentResponse (go/internal/httpserver/handlers/agents.go:62)


getAgentResponse is a method that performs operations based on the provided parameters and may return an error.


```go
func (h *AgentsHandler) getAgentResponse((api.AgentResponse, error)) (api.AgentResponse, error)
```


**Тип ответа:** api.AgentResponse


```json
{
  "ID": "string",
  "Agent": null,
  "ModelProvider": {},
  "Model": "string",
  "ModelConfigRef": "string",
  "MemoryRefs": [],
  "Tools": [],
  "DeploymentReady": false,
  "Accepted": false
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `api.AgentResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/agents.go:62`




## go/internal/httpserver/handlers/checkpoints.go


📄 Исходный файл: `go/internal/httpserver/handlers/checkpoints.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [HandleDeleteThread](#handledeletethread-gointernalhttpserverhandlerscheckpointsgo257) `:257`

- 🔗 [HandleListCheckpoints](#handlelistcheckpoints-gointernalhttpserverhandlerscheckpointsgo128) `:128`

- 🔗 [HandlePutCheckpoint](#handleputcheckpoint-gointernalhttpserverhandlerscheckpointsgo72) `:72`

- 🔗 [HandlePutWrites](#handleputwrites-gointernalhttpserverhandlerscheckpointsgo204) `:204`

- 🔗 [NewCheckpointsHandler](#newcheckpointshandler-gointernalhttpserverhandlerscheckpointsgo19) `:19`


</details>


[function] name: HandleDeleteThread file: go/internal/httpserver/handlers/checkpoints.go:257 returns_error: нет description: HandleDeleteThread handles DELETE /api/langgraph/checkpoints/{thread_id} requests


### HandleDeleteThread (go/internal/httpserver/handlers/checkpoints.go:257)


HandleDeleteThread handles DELETE /api/langgraph/checkpoints/{thread_id} requests


```go
func (h *CheckpointsHandler) HandleDeleteThread((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/checkpoints.go:257`



---


[function] name: HandleListCheckpoints file: go/internal/httpserver/handlers/checkpoints.go:128 returns_error: нет description: HandleListCheckpoints handles GET /api/langgraph/checkpoints requests


### HandleListCheckpoints (go/internal/httpserver/handlers/checkpoints.go:128)


HandleListCheckpoints handles GET /api/langgraph/checkpoints requests


```go
func (h *CheckpointsHandler) HandleListCheckpoints((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/checkpoints.go:128`



---


[function] name: HandlePutCheckpoint file: go/internal/httpserver/handlers/checkpoints.go:72 returns_error: нет description: HandlePutCheckpoint handles POST /api/langgraph/checkpoints requests


### HandlePutCheckpoint (go/internal/httpserver/handlers/checkpoints.go:72)


HandlePutCheckpoint handles POST /api/langgraph/checkpoints requests


```go
func (h *CheckpointsHandler) HandlePutCheckpoint((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/checkpoints.go:72`



---


[function] name: HandlePutWrites file: go/internal/httpserver/handlers/checkpoints.go:204 returns_error: нет description: HandlePutWrites handles POST /api/langgraph/checkpoints/writes requests


### HandlePutWrites (go/internal/httpserver/handlers/checkpoints.go:204)


HandlePutWrites handles POST /api/langgraph/checkpoints/writes requests


```go
func (h *CheckpointsHandler) HandlePutWrites((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/checkpoints.go:204`



---


[function] name: NewCheckpointsHandler file: go/internal/httpserver/handlers/checkpoints.go:19 returns_error: нет description: NewCheckpointsHandler creates a new CheckpointsHandler


### NewCheckpointsHandler (go/internal/httpserver/handlers/checkpoints.go:19)


NewCheckpointsHandler creates a new CheckpointsHandler


```go
func NewCheckpointsHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/checkpoints.go:19`




## go/internal/httpserver/handlers/crewai.go


📄 Исходный файл: `go/internal/httpserver/handlers/crewai.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [HandleGetFlowState](#handlegetflowstate-gointernalhttpserverhandlerscrewaigo255) `:255`

- 🔗 [HandleGetMemory](#handlegetmemory-gointernalhttpserverhandlerscrewaigo104) `:104`

- 🔗 [HandleResetMemory](#handleresetmemory-gointernalhttpserverhandlerscrewaigo167) `:167`

- 🔗 [HandleStoreFlowState](#handlestoreflowstate-gointernalhttpserverhandlerscrewaigo197) `:197`

- 🔗 [HandleStoreMemory](#handlestorememory-gointernalhttpserverhandlerscrewaigo51) `:51`

- 🔗 [NewCrewAIHandler](#newcrewaihandler-gointernalhttpserverhandlerscrewaigo20) `:20`


</details>


[function] name: HandleGetFlowState file: go/internal/httpserver/handlers/crewai.go:255 returns_error: нет description: HandleGetFlowState handles GET /api/crewai/flows/state requests


### HandleGetFlowState (go/internal/httpserver/handlers/crewai.go:255)


HandleGetFlowState handles GET /api/crewai/flows/state requests


```go
func (h *CrewAIHandler) HandleGetFlowState((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/crewai.go:255`



---


[function] name: HandleGetMemory file: go/internal/httpserver/handlers/crewai.go:104 returns_error: нет description: HandleGetMemory handles GET /api/crewai/memory requests


### HandleGetMemory (go/internal/httpserver/handlers/crewai.go:104)


HandleGetMemory handles GET /api/crewai/memory requests


```go
func (h *CrewAIHandler) HandleGetMemory((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/crewai.go:104`



---


[function] name: HandleResetMemory file: go/internal/httpserver/handlers/crewai.go:167 returns_error: нет description: HandleResetMemory handles DELETE /api/crewai/memory requests


### HandleResetMemory (go/internal/httpserver/handlers/crewai.go:167)


HandleResetMemory handles DELETE /api/crewai/memory requests


```go
func (h *CrewAIHandler) HandleResetMemory((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/crewai.go:167`



---


[function] name: HandleStoreFlowState file: go/internal/httpserver/handlers/crewai.go:197 returns_error: нет description: HandleStoreFlowState handles POST /api/crewai/flows/state requests


### HandleStoreFlowState (go/internal/httpserver/handlers/crewai.go:197)


HandleStoreFlowState handles POST /api/crewai/flows/state requests


```go
func (h *CrewAIHandler) HandleStoreFlowState((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/crewai.go:197`



---


[function] name: HandleStoreMemory file: go/internal/httpserver/handlers/crewai.go:51 returns_error: нет description: HandleStoreMemory handles POST /api/crewai/memory requests


### HandleStoreMemory (go/internal/httpserver/handlers/crewai.go:51)


HandleStoreMemory handles POST /api/crewai/memory requests


```go
func (h *CrewAIHandler) HandleStoreMemory((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/crewai.go:51`



---


[function] name: NewCrewAIHandler file: go/internal/httpserver/handlers/crewai.go:20 returns_error: нет description: NewCrewAIHandler creates a new CrewAIHandler


### NewCrewAIHandler (go/internal/httpserver/handlers/crewai.go:20)


NewCrewAIHandler creates a new CrewAIHandler


```go
func NewCrewAIHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/crewai.go:20`




## go/internal/httpserver/handlers/feedback.go


📄 Исходный файл: `go/internal/httpserver/handlers/feedback.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [HandleCreateFeedback](#handlecreatefeedback-gointernalhttpserverhandlersfeedbackgo25) `:25`

- 🔗 [HandleListFeedback](#handlelistfeedback-gointernalhttpserverhandlersfeedbackgo65) `:65`

- 🔗 [NewFeedbackHandler](#newfeedbackhandler-gointernalhttpserverhandlersfeedbackgo20) `:20`


</details>


[function] name: HandleCreateFeedback file: go/internal/httpserver/handlers/feedback.go:25 returns_error: нет description: HandleCreateFeedback handles the submission of user feedback and forwards it to the Python backend


### HandleCreateFeedback (go/internal/httpserver/handlers/feedback.go:25)


HandleCreateFeedback handles the submission of user feedback and forwards it to the Python backend


```go
func (h *FeedbackHandler) HandleCreateFeedback((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/feedback.go:25`



---


[function] name: HandleListFeedback file: go/internal/httpserver/handlers/feedback.go:65 returns_error: нет description: —


### HandleListFeedback (go/internal/httpserver/handlers/feedback.go:65)


HandleListFeedback is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *FeedbackHandler) HandleListFeedback((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/feedback.go:65`



---


[function] name: NewFeedbackHandler file: go/internal/httpserver/handlers/feedback.go:20 returns_error: нет description: NewFeedbackHandler creates a new feedback handler


### NewFeedbackHandler (go/internal/httpserver/handlers/feedback.go:20)


NewFeedbackHandler creates a new feedback handler


```go
func NewFeedbackHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/feedback.go:20`




## go/internal/httpserver/handlers/handlers.go


📄 Исходный файл: `go/internal/httpserver/handlers/handlers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewHandlers](#newhandlers-gointernalhttpserverhandlershandlersgo41) `:41`


</details>


[function] name: NewHandlers file: go/internal/httpserver/handlers/handlers.go:41 returns_error: нет description: NewHandlers creates a new Handlers instance with all handler components.


### NewHandlers (go/internal/httpserver/handlers/handlers.go:41)


NewHandlers creates a new Handlers instance with all handler components.


```go
func NewHandlers((kubeClient client.Client, defaultModelConfig types.NamespacedName, dbService database.Client, watchedNamespaces []string, authorizer auth.Authorizer, proxyURL string, rcnclr reconciler.KagentReconciler)) (kubeClient client.Client, defaultModelConfig types.NamespacedName, dbService database.Client, watchedNamespaces []string, authorizer auth.Authorizer, proxyURL string, rcnclr reconciler.KagentReconciler)
```


**Тип ответа:** kubeClient


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** defaultModelConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** database.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** watchedNamespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authorizer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.Authorizer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rcnclr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reconciler.KagentReconciler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/handlers.go:41`




## go/internal/httpserver/handlers/health.go


📄 Исходный файл: `go/internal/httpserver/handlers/health.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [HandleHealth](#handlehealth-gointernalhttpserverhandlershealthgo19) `:19`

- 🔗 [NewHealthHandler](#newhealthhandler-gointernalhttpserverhandlershealthgo14) `:14`


</details>


[function] name: HandleHealth file: go/internal/httpserver/handlers/health.go:19 returns_error: нет description: HandleHealth handles GET /health requests


### HandleHealth (go/internal/httpserver/handlers/health.go:19)


HandleHealth handles GET /health requests


```go
func (h *HealthHandler) HandleHealth((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/health.go:19`



---


[function] name: NewHealthHandler file: go/internal/httpserver/handlers/health.go:14 returns_error: нет description: NewHealthHandler creates a new HealthHandler


### NewHealthHandler (go/internal/httpserver/handlers/health.go:14)


NewHealthHandler creates a new HealthHandler


```go
func NewHealthHandler(()) ()
```


📍 *Расположение:* `go/internal/httpserver/handlers/health.go:14`




## go/internal/httpserver/handlers/helpers.go


📄 Исходный файл: `go/internal/httpserver/handlers/helpers.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Check](#check-gointernalhttpserverhandlershelpersgo56) `:56`

- 🔗 [CreateSecret](#createsecret-gointernalhttpserverhandlershelpersgo180) `:180`

- 🔗 [DecodeJSONBody](#decodejsonbody-gointernalhttpserverhandlershelpersgo129) `:129`

- 🔗 [FlattenStructToMap](#flattenstructtomap-gointernalhttpserverhandlershelpersgo144) `:144`

- 🔗 [GetIntPathParam](#getintpathparam-gointernalhttpserverhandlershelpersgo110) `:110`

- 🔗 [GetPathParam](#getpathparam-gointernalhttpserverhandlershelpersgo95) `:95`

- 🔗 [GetPrincipal](#getprincipal-gointernalhttpserverhandlershelpersgo82) `:82`

- 🔗 [GetUserID](#getuserid-gointernalhttpserverhandlershelpersgo51) `:51`

- 🔗 [RespondWithError](#respondwitherror-gointernalhttpserverhandlershelpersgo44) `:44`

- 🔗 [RespondWithJSON](#respondwithjson-gointernalhttpserverhandlershelpersgo27) `:27`


</details>


[function] name: Check file: go/internal/httpserver/handlers/helpers.go:56 returns_error: нет description: —


### Check (go/internal/httpserver/handlers/helpers.go:56)


Check is a function that performs operations based on the provided parameters and returns (authorizer auth.Authorizer, r *http.Request, res auth.Resource).


```go
func Check((authorizer auth.Authorizer, r *http.Request, res auth.Resource)) (authorizer auth.Authorizer, r *http.Request, res auth.Resource)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** authorizer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.Authorizer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** res


```json
{
  "URL": "string",
  "URLFile": "string",
  "VectorEnabled": false
}
```


*Определено в:* `go/internal/database/manager.go`


**Тип ответа:** auth.Resource


```json
{
  "Name": "string",
  "Type": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:56`



---


[function] name: CreateSecret file: go/internal/httpserver/handlers/helpers.go:180 returns_error: да description: —


### CreateSecret (go/internal/httpserver/handlers/helpers.go:180)


CreateSecret is a function that creates new data based on the provided parameters and may return an error.


```go
func CreateSecret((*corev1.Secret, error)) (*corev1.Secret, error)
```


**Тип запроса:** corev1.Secret


```json
{
  "Enabled": false,
  "Provider": "string",
  "File": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** corev1.Secret


```json
{
  "Enabled": false,
  "Provider": "string",
  "File": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Secret`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:180`



---


[function] name: DecodeJSONBody file: go/internal/httpserver/handlers/helpers.go:129 returns_error: нет description: DecodeJSONBody decodes a JSON request body into the provided struct


### DecodeJSONBody (go/internal/httpserver/handlers/helpers.go:129)


DecodeJSONBody decodes a JSON request body into the provided struct


```go
func DecodeJSONBody((r *http.Request, target any)) (r *http.Request, target any)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** target


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:129`



---


[function] name: FlattenStructToMap file: go/internal/httpserver/handlers/helpers.go:144 returns_error: нет description: flattenStructToMap uses reflection to add fields of a struct to a map,
using json tags as keys.


### FlattenStructToMap (go/internal/httpserver/handlers/helpers.go:144)


flattenStructToMap uses reflection to add fields of a struct to a map,
using json tags as keys.


```go
func FlattenStructToMap((data any, targetMap map[string]any)) (data any, targetMap map[string]any)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** targetMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:144`



---


[function] name: GetIntPathParam file: go/internal/httpserver/handlers/helpers.go:110 returns_error: да description: GetIntPathParam gets an integer path parameter from the request


### GetIntPathParam (go/internal/httpserver/handlers/helpers.go:110)


GetIntPathParam gets an integer path parameter from the request


```go
func GetIntPathParam((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:110`



---


[function] name: GetPathParam file: go/internal/httpserver/handlers/helpers.go:95 returns_error: да description: GetPathParam gets a path parameter from the request


### GetPathParam (go/internal/httpserver/handlers/helpers.go:95)


GetPathParam gets a path parameter from the request


```go
func GetPathParam((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:95`



---


[function] name: GetPrincipal file: go/internal/httpserver/handlers/helpers.go:82 returns_error: да description: —


### GetPrincipal (go/internal/httpserver/handlers/helpers.go:82)


GetPrincipal is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetPrincipal((auth.Principal, error)) (auth.Principal, error)
```


**Тип ответа:** auth.Principal


```json
{
  "User": {},
  "Agent": {}
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `auth.Principal`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:82`



---


[function] name: GetUserID file: go/internal/httpserver/handlers/helpers.go:51 returns_error: да description: —


### GetUserID (go/internal/httpserver/handlers/helpers.go:51)


GetUserID is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetUserID((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:51`



---


[function] name: RespondWithError file: go/internal/httpserver/handlers/helpers.go:44 returns_error: нет description: —


### RespondWithError (go/internal/httpserver/handlers/helpers.go:44)


RespondWithError is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, code int, message string).


```go
func RespondWithError((w http.ResponseWriter, code int, message string)) (w http.ResponseWriter, code int, message string)
```


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** code


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:44`



---


[function] name: RespondWithJSON file: go/internal/httpserver/handlers/helpers.go:27 returns_error: нет description: —


### RespondWithJSON (go/internal/httpserver/handlers/helpers.go:27)


RespondWithJSON is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, code int, payload any).


```go
func RespondWithJSON((w http.ResponseWriter, code int, payload any)) (w http.ResponseWriter, code int, payload any)
```


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** code


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** payload


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/helpers.go:27`




## go/internal/httpserver/handlers/memory.go


📄 Исходный файл: `go/internal/httpserver/handlers/memory.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [AddSession](#addsession-gointernalhttpserverhandlersmemorygo71) `:71`

- 🔗 [AddSessionBatch](#addsessionbatch-gointernalhttpserverhandlersmemorygo125) `:125`

- 🔗 [Delete](#delete-gointernalhttpserverhandlersmemorygo278) `:278`

- 🔗 [List](#list-gointernalhttpserverhandlersmemorygo244) `:244`

- 🔗 [NewMemoryHandler](#newmemoryhandler-gointernalhttpserverhandlersmemorygo29) `:29`

- 🔗 [Search](#search-gointernalhttpserverhandlersmemorygo187) `:187`


</details>


[function] name: AddSession file: go/internal/httpserver/handlers/memory.go:71 returns_error: нет description: AddSession handles POST /api/memories/sessions


### AddSession (go/internal/httpserver/handlers/memory.go:71)


AddSession handles POST /api/memories/sessions


```go
func (h *MemoryHandler) AddSession((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/memory.go:71`



---


[function] name: AddSessionBatch file: go/internal/httpserver/handlers/memory.go:125 returns_error: нет description: AddSessionBatch handles POST /api/memories/sessions/batch


### AddSessionBatch (go/internal/httpserver/handlers/memory.go:125)


AddSessionBatch handles POST /api/memories/sessions/batch


```go
func (h *MemoryHandler) AddSessionBatch((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/memory.go:125`



---


[function] name: Delete file: go/internal/httpserver/handlers/memory.go:278 returns_error: нет description: Delete handles DELETE /api/memories


### Delete (go/internal/httpserver/handlers/memory.go:278)


Delete handles DELETE /api/memories


```go
func (h *MemoryHandler) Delete((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/memory.go:278`



---


[function] name: List file: go/internal/httpserver/handlers/memory.go:244 returns_error: нет description: List handles GET /api/memories and returns all memories for an agent+user, ranked by access frequency


### List (go/internal/httpserver/handlers/memory.go:244)


List handles GET /api/memories and returns all memories for an agent+user, ranked by access frequency


```go
func (h *MemoryHandler) List((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/memory.go:244`



---


[function] name: NewMemoryHandler file: go/internal/httpserver/handlers/memory.go:29 returns_error: нет description: NewMemoryHandler creates a new MemoryHandler


### NewMemoryHandler (go/internal/httpserver/handlers/memory.go:29)


NewMemoryHandler creates a new MemoryHandler


```go
func NewMemoryHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/memory.go:29`



---


[function] name: Search file: go/internal/httpserver/handlers/memory.go:187 returns_error: нет description: Search handles POST /api/memories/search


### Search (go/internal/httpserver/handlers/memory.go:187)


Search handles POST /api/memories/search


```go
func (h *MemoryHandler) Search((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/memory.go:187`




## go/internal/httpserver/handlers/modelconfig.go


📄 Исходный файл: `go/internal/httpserver/handlers/modelconfig.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [HandleCreateModelConfig](#handlecreatemodelconfig-gointernalhttpserverhandlersmodelconfiggo185) `:185`

- 🔗 [HandleDeleteModelConfig](#handledeletemodelconfig-gointernalhttpserverhandlersmodelconfiggo557) `:557`

- 🔗 [HandleGetModelConfig](#handlegetmodelconfig-gointernalhttpserverhandlersmodelconfiggo82) `:82`

- 🔗 [HandleListModelConfigs](#handlelistmodelconfigs-gointernalhttpserverhandlersmodelconfiggo33) `:33`

- 🔗 [HandleUpdateModelConfig](#handleupdatemodelconfig-gointernalhttpserverhandlersmodelconfiggo365) `:365`

- 🔗 [NewModelConfigHandler](#newmodelconfighandler-gointernalhttpserverhandlersmodelconfiggo28) `:28`

- 🔗 [getStructJSONKeys](#getstructjsonkeys-gointernalhttpserverhandlersmodelconfiggo163) `:163`


</details>


[function] name: HandleCreateModelConfig file: go/internal/httpserver/handlers/modelconfig.go:185 returns_error: нет description: HandleCreateToolServer handles POST /api/modelconfigs requests


### HandleCreateModelConfig (go/internal/httpserver/handlers/modelconfig.go:185)


HandleCreateToolServer handles POST /api/modelconfigs requests


```go
func (h *ModelConfigHandler) HandleCreateModelConfig((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelconfig.go:185`



---


[function] name: HandleDeleteModelConfig file: go/internal/httpserver/handlers/modelconfig.go:557 returns_error: нет description: HandleDeleteModelConfig handles DELETE /api/modelconfigs/{namespace}/{name} requests


### HandleDeleteModelConfig (go/internal/httpserver/handlers/modelconfig.go:557)


HandleDeleteModelConfig handles DELETE /api/modelconfigs/{namespace}/{name} requests


```go
func (h *ModelConfigHandler) HandleDeleteModelConfig((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelconfig.go:557`



---


[function] name: HandleGetModelConfig file: go/internal/httpserver/handlers/modelconfig.go:82 returns_error: нет description: HandleGetModelConfig handles GET /api/modelconfigs/{namespace}/{name} requests


### HandleGetModelConfig (go/internal/httpserver/handlers/modelconfig.go:82)


HandleGetModelConfig handles GET /api/modelconfigs/{namespace}/{name} requests


```go
func (h *ModelConfigHandler) HandleGetModelConfig((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelconfig.go:82`



---


[function] name: HandleListModelConfigs file: go/internal/httpserver/handlers/modelconfig.go:33 returns_error: нет description: HandleListModelConfigs handles GET /api/modelconfigs requests


### HandleListModelConfigs (go/internal/httpserver/handlers/modelconfig.go:33)


HandleListModelConfigs handles GET /api/modelconfigs requests


```go
func (h *ModelConfigHandler) HandleListModelConfigs((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelconfig.go:33`



---


[function] name: HandleUpdateModelConfig file: go/internal/httpserver/handlers/modelconfig.go:365 returns_error: нет description: HandleUpdateModelConfig handles POST /api/modelconfigs/{namespace}/{name} requests


### HandleUpdateModelConfig (go/internal/httpserver/handlers/modelconfig.go:365)


HandleUpdateModelConfig handles POST /api/modelconfigs/{namespace}/{name} requests


```go
func (h *ModelConfigHandler) HandleUpdateModelConfig((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelconfig.go:365`



---


[function] name: NewModelConfigHandler file: go/internal/httpserver/handlers/modelconfig.go:28 returns_error: нет description: NewModelConfigHandler creates a new ModelConfigHandler


### NewModelConfigHandler (go/internal/httpserver/handlers/modelconfig.go:28)


NewModelConfigHandler creates a new ModelConfigHandler


```go
func NewModelConfigHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelconfig.go:28`



---


[function] name: getStructJSONKeys file: go/internal/httpserver/handlers/modelconfig.go:163 returns_error: нет description: Helper function to get all JSON keys from a struct type


### getStructJSONKeys (go/internal/httpserver/handlers/modelconfig.go:163)


Helper function to get all JSON keys from a struct type


```go
func getStructJSONKeys((structType reflect.Type)) (structType reflect.Type)
```


**Тип ответа:** structType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reflect.Type


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelconfig.go:163`




## go/internal/httpserver/handlers/modelproviderconfig.go


📄 Исходный файл: `go/internal/httpserver/handlers/modelproviderconfig.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [HandleGetProviderModels](#handlegetprovidermodels-gointernalhttpserverhandlersmodelproviderconfiggo196) `:196`

- 🔗 [HandleListConfiguredProviders](#handlelistconfiguredproviders-gointernalhttpserverhandlersmodelproviderconfiggo162) `:162`

- 🔗 [HandleListSupportedMemoryProviders](#handlelistsupportedmemoryproviders-gointernalhttpserverhandlersmodelproviderconfiggo71) `:71`

- 🔗 [HandleListSupportedModelProviders](#handlelistsupportedmodelproviders-gointernalhttpserverhandlersmodelproviderconfiggo112) `:112`

- 🔗 [NewModelProviderConfigHandler](#newmodelproviderconfighandler-gointernalhttpserverhandlersmodelproviderconfiggo37) `:37`

- 🔗 [getRequiredKeysForMemoryProvider](#getrequiredkeysformemoryprovider-gointernalhttpserverhandlersmodelproviderconfiggo62) `:62`

- 🔗 [getRequiredKeysForModelProvider](#getrequiredkeysformodelprovider-gointernalhttpserverhandlersmodelproviderconfiggo45) `:45`


</details>


[function] name: HandleGetProviderModels file: go/internal/httpserver/handlers/modelproviderconfig.go:196 returns_error: нет description: HandleGetProviderModels discovers and returns available models for a specific model provider.
GET /api/modelproviderconf


### HandleGetProviderModels (go/internal/httpserver/handlers/modelproviderconfig.go:196)


HandleGetProviderModels discovers and returns available models for a specific model provider.
GET /api/modelproviderconfigs/configured/{name}/models?refresh=true


```go
func (h *ModelProviderConfigHandler) HandleGetProviderModels((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelproviderconfig.go:196`



---


[function] name: HandleListConfiguredProviders file: go/internal/httpserver/handlers/modelproviderconfig.go:162 returns_error: нет description: HandleListConfiguredProviders returns the list of model providers configured via ModelProviderConfig CRDs.
GET /api/mode


### HandleListConfiguredProviders (go/internal/httpserver/handlers/modelproviderconfig.go:162)


HandleListConfiguredProviders returns the list of model providers configured via ModelProviderConfig CRDs.
GET /api/modelproviderconfigs/configured


```go
func (h *ModelProviderConfigHandler) HandleListConfiguredProviders((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelproviderconfig.go:162`



---


[function] name: HandleListSupportedMemoryProviders file: go/internal/httpserver/handlers/modelproviderconfig.go:71 returns_error: нет description: —


### HandleListSupportedMemoryProviders (go/internal/httpserver/handlers/modelproviderconfig.go:71)


HandleListSupportedMemoryProviders is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *ModelProviderConfigHandler) HandleListSupportedMemoryProviders((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelproviderconfig.go:71`



---


[function] name: HandleListSupportedModelProviders file: go/internal/httpserver/handlers/modelproviderconfig.go:112 returns_error: нет description: —


### HandleListSupportedModelProviders (go/internal/httpserver/handlers/modelproviderconfig.go:112)


HandleListSupportedModelProviders is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *ModelProviderConfigHandler) HandleListSupportedModelProviders((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelproviderconfig.go:112`



---


[function] name: NewModelProviderConfigHandler file: go/internal/httpserver/handlers/modelproviderconfig.go:37 returns_error: нет description: NewModelProviderConfigHandler creates a new ModelProviderConfigHandler


### NewModelProviderConfigHandler (go/internal/httpserver/handlers/modelproviderconfig.go:37)


NewModelProviderConfigHandler creates a new ModelProviderConfigHandler


```go
func NewModelProviderConfigHandler((base *Base, rcnclr reconciler.KagentReconciler)) (base *Base, rcnclr reconciler.KagentReconciler)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** rcnclr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reconciler.KagentReconciler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/modelproviderconfig.go:37`



---


[function] name: getRequiredKeysForMemoryProvider file: go/internal/httpserver/handlers/modelproviderconfig.go:62 returns_error: нет description: —


### getRequiredKeysForMemoryProvider (go/internal/httpserver/handlers/modelproviderconfig.go:62)


getRequiredKeysForMemoryProvider is a function that performs operations based on the provided parameters and returns (providerType v1alpha1.MemoryProvider).


```go
func getRequiredKeysForMemoryProvider((providerType v1alpha1.MemoryProvider)) (providerType v1alpha1.MemoryProvider)
```


**Тип ответа:** providerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.MemoryProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/modelproviderconfig.go:62`



---


[function] name: getRequiredKeysForModelProvider file: go/internal/httpserver/handlers/modelproviderconfig.go:45 returns_error: нет description: Helper function to get JSON keys specifically marked as required


### getRequiredKeysForModelProvider (go/internal/httpserver/handlers/modelproviderconfig.go:45)


Helper function to get JSON keys specifically marked as required


```go
func getRequiredKeysForModelProvider((providerType v1alpha2.ModelProvider)) (providerType v1alpha2.ModelProvider)
```


**Тип ответа:** providerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/internal/httpserver/handlers/modelproviderconfig.go:45`




## go/internal/httpserver/handlers/models.go


📄 Исходный файл: `go/internal/httpserver/handlers/models.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [HandleListSupportedModels](#handlelistsupportedmodels-gointernalhttpserverhandlersmodelsgo22) `:22`

- 🔗 [NewModelHandler](#newmodelhandler-gointernalhttpserverhandlersmodelsgo18) `:18`


</details>


[function] name: HandleListSupportedModels file: go/internal/httpserver/handlers/models.go:22 returns_error: нет description: —


### HandleListSupportedModels (go/internal/httpserver/handlers/models.go:22)


HandleListSupportedModels is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *ModelHandler) HandleListSupportedModels((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/models.go:22`



---


[function] name: NewModelHandler file: go/internal/httpserver/handlers/models.go:18 returns_error: нет description: NewModelHandler creates a new ModelHandler


### NewModelHandler (go/internal/httpserver/handlers/models.go:18)


NewModelHandler creates a new ModelHandler


```go
func NewModelHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/models.go:18`




## go/internal/httpserver/handlers/namespaces.go


📄 Исходный файл: `go/internal/httpserver/handlers/namespaces.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [HandleListNamespaces](#handlelistnamespaces-gointernalhttpserverhandlersnamespacesgo32) `:32`

- 🔗 [NewNamespacesHandler](#newnamespaceshandler-gointernalhttpserverhandlersnamespacesgo24) `:24`


</details>


[function] name: HandleListNamespaces file: go/internal/httpserver/handlers/namespaces.go:32 returns_error: нет description: HandleListNamespaces returns a list of namespaces based on the watch configuration


### HandleListNamespaces (go/internal/httpserver/handlers/namespaces.go:32)


HandleListNamespaces returns a list of namespaces based on the watch configuration


```go
func (h *NamespacesHandler) HandleListNamespaces((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/namespaces.go:32`



---


[function] name: NewNamespacesHandler file: go/internal/httpserver/handlers/namespaces.go:24 returns_error: нет description: NewNamespacesHandler creates a new NamespacesHandler


### NewNamespacesHandler (go/internal/httpserver/handlers/namespaces.go:24)


NewNamespacesHandler creates a new NamespacesHandler


```go
func NewNamespacesHandler((base *Base, watchedNamespaces []string)) (base *Base, watchedNamespaces []string)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** watchedNamespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/namespaces.go:24`




## go/internal/httpserver/handlers/sessions.go


📄 Исходный файл: `go/internal/httpserver/handlers/sessions.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [HandleAddEventToSession](#handleaddeventtosession-gointernalhttpserverhandlerssessionsgo341) `:341`

- 🔗 [HandleCreateSession](#handlecreatesession-gointernalhttpserverhandlerssessionsgo98) `:98`

- 🔗 [HandleDeleteSession](#handledeletesession-gointernalhttpserverhandlerssessionsgo277) `:277`

- 🔗 [HandleGetSession](#handlegetsession-gointernalhttpserverhandlerssessionsgo161) `:161`

- 🔗 [HandleGetSessionsForAgent](#handlegetsessionsforagent-gointernalhttpserverhandlerssessionsgo32) `:32`

- 🔗 [HandleListSessions](#handlelistsessions-gointernalhttpserverhandlerssessionsgo75) `:75`

- 🔗 [HandleListTasksForSession](#handlelisttasksforsession-gointernalhttpserverhandlerssessionsgo305) `:305`

- 🔗 [HandleUpdateSession](#handleupdatesession-gointernalhttpserverhandlerssessionsgo225) `:225`

- 🔗 [NewSessionsHandler](#newsessionshandler-gointernalhttpserverhandlerssessionsgo23) `:23`

- 🔗 [getUserID](#getuserid-gointernalhttpserverhandlerssessionsgo398) `:398`

- 🔗 [getUserIDOrAgentUser](#getuseridoragentuser-gointernalhttpserverhandlerssessionsgo419) `:419`


</details>


[function] name: HandleAddEventToSession file: go/internal/httpserver/handlers/sessions.go:341 returns_error: нет description: —


### HandleAddEventToSession (go/internal/httpserver/handlers/sessions.go:341)


HandleAddEventToSession is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *SessionsHandler) HandleAddEventToSession((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:341`



---


[function] name: HandleCreateSession file: go/internal/httpserver/handlers/sessions.go:98 returns_error: нет description: HandleCreateSession handles POST /api/sessions requests using database


### HandleCreateSession (go/internal/httpserver/handlers/sessions.go:98)


HandleCreateSession handles POST /api/sessions requests using database


```go
func (h *SessionsHandler) HandleCreateSession((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:98`



---


[function] name: HandleDeleteSession file: go/internal/httpserver/handlers/sessions.go:277 returns_error: нет description: HandleDeleteSession handles DELETE /api/sessions/{session_id} requests using database


### HandleDeleteSession (go/internal/httpserver/handlers/sessions.go:277)


HandleDeleteSession handles DELETE /api/sessions/{session_id} requests using database


```go
func (h *SessionsHandler) HandleDeleteSession((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:277`



---


[function] name: HandleGetSession file: go/internal/httpserver/handlers/sessions.go:161 returns_error: нет description: HandleGetSession handles GET /api/sessions/{session_id} requests using database


### HandleGetSession (go/internal/httpserver/handlers/sessions.go:161)


HandleGetSession handles GET /api/sessions/{session_id} requests using database


```go
func (h *SessionsHandler) HandleGetSession((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:161`



---


[function] name: HandleGetSessionsForAgent file: go/internal/httpserver/handlers/sessions.go:32 returns_error: нет description: —


### HandleGetSessionsForAgent (go/internal/httpserver/handlers/sessions.go:32)


HandleGetSessionsForAgent is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *SessionsHandler) HandleGetSessionsForAgent((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:32`



---


[function] name: HandleListSessions file: go/internal/httpserver/handlers/sessions.go:75 returns_error: нет description: HandleListSessions handles GET /api/sessions requests using database


### HandleListSessions (go/internal/httpserver/handlers/sessions.go:75)


HandleListSessions handles GET /api/sessions requests using database


```go
func (h *SessionsHandler) HandleListSessions((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:75`



---


[function] name: HandleListTasksForSession file: go/internal/httpserver/handlers/sessions.go:305 returns_error: нет description: HandleListSessionRuns handles GET /api/sessions/{session_id}/tasks requests using database


### HandleListTasksForSession (go/internal/httpserver/handlers/sessions.go:305)


HandleListSessionRuns handles GET /api/sessions/{session_id}/tasks requests using database


```go
func (h *SessionsHandler) HandleListTasksForSession((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:305`



---


[function] name: HandleUpdateSession file: go/internal/httpserver/handlers/sessions.go:225 returns_error: нет description: HandleUpdateSession handles PUT /api/sessions requests using database


### HandleUpdateSession (go/internal/httpserver/handlers/sessions.go:225)


HandleUpdateSession handles PUT /api/sessions requests using database


```go
func (h *SessionsHandler) HandleUpdateSession((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:225`



---


[function] name: NewSessionsHandler file: go/internal/httpserver/handlers/sessions.go:23 returns_error: нет description: NewSessionsHandler creates a new SessionsHandler


### NewSessionsHandler (go/internal/httpserver/handlers/sessions.go:23)


NewSessionsHandler creates a new SessionsHandler


```go
func NewSessionsHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:23`



---


[function] name: getUserID file: go/internal/httpserver/handlers/sessions.go:398 returns_error: да description: —


### getUserID (go/internal/httpserver/handlers/sessions.go:398)


getUserID is a function that performs operations based on the provided parameters and may return an error.


```go
func getUserID((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:398`



---


[function] name: getUserIDOrAgentUser file: go/internal/httpserver/handlers/sessions.go:419 returns_error: да description: —


### getUserIDOrAgentUser (go/internal/httpserver/handlers/sessions.go:419)


getUserIDOrAgentUser is a function that performs operations based on the provided parameters and may return an error.


```go
func getUserIDOrAgentUser((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/sessions.go:419`




## go/internal/httpserver/handlers/tasks.go


📄 Исходный файл: `go/internal/httpserver/handlers/tasks.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [HandleCreateTask](#handlecreatetask-gointernalhttpserverhandlerstasksgo43) `:43`

- 🔗 [HandleDeleteTask](#handledeletetask-gointernalhttpserverhandlerstasksgo66) `:66`

- 🔗 [HandleGetTask](#handlegettask-gointernalhttpserverhandlerstasksgo22) `:22`

- 🔗 [NewTasksHandler](#newtaskshandler-gointernalhttpserverhandlerstasksgo18) `:18`


</details>


[function] name: HandleCreateTask file: go/internal/httpserver/handlers/tasks.go:43 returns_error: нет description: —


### HandleCreateTask (go/internal/httpserver/handlers/tasks.go:43)


HandleCreateTask is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *TasksHandler) HandleCreateTask((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/tasks.go:43`



---


[function] name: HandleDeleteTask file: go/internal/httpserver/handlers/tasks.go:66 returns_error: нет description: —


### HandleDeleteTask (go/internal/httpserver/handlers/tasks.go:66)


HandleDeleteTask is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *TasksHandler) HandleDeleteTask((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/tasks.go:66`



---


[function] name: HandleGetTask file: go/internal/httpserver/handlers/tasks.go:22 returns_error: нет description: —


### HandleGetTask (go/internal/httpserver/handlers/tasks.go:22)


HandleGetTask is a method that handles or processes requests based on the provided parameters and may return an error.


```go
func (h *TasksHandler) HandleGetTask((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/tasks.go:22`



---


[function] name: NewTasksHandler file: go/internal/httpserver/handlers/tasks.go:18 returns_error: нет description: NewTasksHandler creates a new TasksHandler


### NewTasksHandler (go/internal/httpserver/handlers/tasks.go:18)


NewTasksHandler creates a new TasksHandler


```go
func NewTasksHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/tasks.go:18`




## go/internal/httpserver/handlers/tools.go


📄 Исходный файл: `go/internal/httpserver/handlers/tools.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [HandleListTools](#handlelisttools-gointernalhttpserverhandlerstoolsgo22) `:22`

- 🔗 [NewToolsHandler](#newtoolshandler-gointernalhttpserverhandlerstoolsgo17) `:17`


</details>


[function] name: HandleListTools file: go/internal/httpserver/handlers/tools.go:22 returns_error: нет description: HandleListTools handles GET /api/tools requests using database


### HandleListTools (go/internal/httpserver/handlers/tools.go:22)


HandleListTools handles GET /api/tools requests using database


```go
func (h *ToolsHandler) HandleListTools((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/tools.go:22`



---


[function] name: NewToolsHandler file: go/internal/httpserver/handlers/tools.go:17 returns_error: нет description: NewToolsHandler creates a new ToolsHandler


### NewToolsHandler (go/internal/httpserver/handlers/tools.go:17)


NewToolsHandler creates a new ToolsHandler


```go
func NewToolsHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/tools.go:17`




## go/internal/httpserver/handlers/toolservers.go


📄 Исходный файл: `go/internal/httpserver/handlers/toolservers.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [HandleCreateToolServer](#handlecreatetoolserver-gointernalhttpserverhandlerstoolserversgo88) `:88`

- 🔗 [HandleDeleteToolServer](#handledeletetoolserver-gointernalhttpserverhandlerstoolserversgo193) `:193`

- 🔗 [HandleListToolServers](#handlelisttoolservers-gointernalhttpserverhandlerstoolserversgo45) `:45`

- 🔗 [NewToolServersHandler](#newtoolservershandler-gointernalhttpserverhandlerstoolserversgo28) `:28`

- 🔗 [handleCreateMCPServer](#handlecreatemcpserver-gointernalhttpserverhandlerstoolserversgo159) `:159`

- 🔗 [handleCreateRemoteMCPServer](#handlecreateremotemcpserver-gointernalhttpserverhandlerstoolserversgo129) `:129`


</details>


[function] name: HandleCreateToolServer file: go/internal/httpserver/handlers/toolservers.go:88 returns_error: нет description: HandleCreateToolServer handles POST /api/toolservers requests


### HandleCreateToolServer (go/internal/httpserver/handlers/toolservers.go:88)


HandleCreateToolServer handles POST /api/toolservers requests


```go
func (h *ToolServersHandler) HandleCreateToolServer((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/toolservers.go:88`



---


[function] name: HandleDeleteToolServer file: go/internal/httpserver/handlers/toolservers.go:193 returns_error: нет description: HandleDeleteToolServer handles DELETE /api/toolservers/{namespace}/{name} requests


### HandleDeleteToolServer (go/internal/httpserver/handlers/toolservers.go:193)


HandleDeleteToolServer handles DELETE /api/toolservers/{namespace}/{name} requests


```go
func (h *ToolServersHandler) HandleDeleteToolServer((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/toolservers.go:193`



---


[function] name: HandleListToolServers file: go/internal/httpserver/handlers/toolservers.go:45 returns_error: нет description: HandleListToolServers handles GET /api/toolservers requests


### HandleListToolServers (go/internal/httpserver/handlers/toolservers.go:45)


HandleListToolServers handles GET /api/toolservers requests


```go
func (h *ToolServersHandler) HandleListToolServers((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/toolservers.go:45`



---


[function] name: NewToolServersHandler file: go/internal/httpserver/handlers/toolservers.go:28 returns_error: нет description: NewToolServersHandler creates a new ToolServersHandler


### NewToolServersHandler (go/internal/httpserver/handlers/toolservers.go:28)


NewToolServersHandler creates a new ToolServersHandler


```go
func NewToolServersHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/toolservers.go:28`



---


[function] name: handleCreateMCPServer file: go/internal/httpserver/handlers/toolservers.go:159 returns_error: нет description: handleCreateMCPServer handles the creation of an MCPServer (stdio-based)


### handleCreateMCPServer (go/internal/httpserver/handlers/toolservers.go:159)


handleCreateMCPServer handles the creation of an MCPServer (stdio-based)


```go
func (h *ToolServersHandler) handleCreateMCPServer((w ErrorResponseWriter, r *http.Request, toolServerRequest *v1alpha1.MCPServer, log logr.Logger)) (w ErrorResponseWriter, r *http.Request, toolServerRequest *v1alpha1.MCPServer, log logr.Logger)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** toolServerRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** log


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/toolservers.go:159`



---


[function] name: handleCreateRemoteMCPServer file: go/internal/httpserver/handlers/toolservers.go:129 returns_error: нет description: handleCreateRemoteMCPServer handles the creation of a RemoteMCPServer


### handleCreateRemoteMCPServer (go/internal/httpserver/handlers/toolservers.go:129)


handleCreateRemoteMCPServer handles the creation of a RemoteMCPServer


```go
func (h *ToolServersHandler) handleCreateRemoteMCPServer((w ErrorResponseWriter, r *http.Request, toolServerRequest *v1alpha2.RemoteMCPServer, log logr.Logger)) (w ErrorResponseWriter, r *http.Request, toolServerRequest *v1alpha2.RemoteMCPServer, log logr.Logger)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип запроса:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** toolServerRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** log


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/toolservers.go:129`




## go/internal/httpserver/handlers/toolservertypes.go


📄 Исходный файл: `go/internal/httpserver/handlers/toolservertypes.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetSupportedToolServerTypes](#getsupportedtoolservertypes-gointernalhttpserverhandlerstoolservertypesgo58) `:58`

- 🔗 [HandleListToolServerTypes](#handlelisttoolservertypes-gointernalhttpserverhandlerstoolservertypesgo71) `:71`

- 🔗 [Join](#join-gointernalhttpserverhandlerstoolservertypesgo35) `:35`

- 🔗 [NewToolServerTypesHandler](#newtoolservertypeshandler-gointernalhttpserverhandlerstoolservertypesgo21) `:21`


</details>


[function] name: GetSupportedToolServerTypes file: go/internal/httpserver/handlers/toolservertypes.go:58 returns_error: да description: —


### GetSupportedToolServerTypes (go/internal/httpserver/handlers/toolservertypes.go:58)


GetSupportedToolServerTypes is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetSupportedToolServerTypes((ToolServerTypes, error)) (ToolServerTypes, error)
```


**Тип ответа:** ToolServerTypes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ToolServerTypes`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/handlers/toolservertypes.go:58`



---


[function] name: HandleListToolServerTypes file: go/internal/httpserver/handlers/toolservertypes.go:71 returns_error: нет description: HandleListToolServerTypes handles GET /api/toolservertypes requests


### HandleListToolServerTypes (go/internal/httpserver/handlers/toolservertypes.go:71)


HandleListToolServerTypes handles GET /api/toolservertypes requests


```go
func (h *ToolServerTypesHandler) HandleListToolServerTypes((w ErrorResponseWriter, r *http.Request)) (w ErrorResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/handlers/toolservertypes.go:71`



---


[function] name: Join file: go/internal/httpserver/handlers/toolservertypes.go:35 returns_error: нет description: —


### Join (go/internal/httpserver/handlers/toolservertypes.go:35)


Join is a method that performs operations based on the provided parameters and returns (sep string).


```go
func (t ToolServerTypes) Join((sep string)) (sep string)
```


**Тип ответа:** sep


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/handlers/toolservertypes.go:35`



---


[function] name: NewToolServerTypesHandler file: go/internal/httpserver/handlers/toolservertypes.go:21 returns_error: нет description: NewToolServerTypesHandler creates a new ToolServerTypesHandler


### NewToolServerTypesHandler (go/internal/httpserver/handlers/toolservertypes.go:21)


NewToolServerTypesHandler creates a new ToolServerTypesHandler


```go
func NewToolServerTypesHandler((base *Base)) (base *Base)
```


**Тип запроса:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Base


```json
{
  "KubeClient": {},
  "DefaultModelConfig": {},
  "DatabaseService": {},
  "Authorizer": {},
  "ProxyURL": "string"
}
```


*Определено в:* `go/internal/httpserver/handlers/handlers.go`


📍 *Расположение:* `go/internal/httpserver/handlers/toolservertypes.go:21`




## go/internal/httpserver/handlers/utils.go


📄 Исходный файл: `go/internal/httpserver/handlers/utils.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [createOrUpdateSecretWithOwnerReference](#createorupdatesecretwithownerreference-gointernalhttpserverhandlersutilsgo55) `:55`

- 🔗 [createSecretWithOwnerReference](#createsecretwithownerreference-gointernalhttpserverhandlersutilsgo19) `:19`


</details>


[function] name: createOrUpdateSecretWithOwnerReference file: go/internal/httpserver/handlers/utils.go:55 returns_error: нет description: createOrUpdateSecretWithOwnerReference creates or updates a Kubernetes secret with owner reference.
Secret will have the


### createOrUpdateSecretWithOwnerReference (go/internal/httpserver/handlers/utils.go:55)


createOrUpdateSecretWithOwnerReference creates or updates a Kubernetes secret with owner reference.
Secret will have the same name and namespace as the owner object.


```go
func createOrUpdateSecretWithOwnerReference((
	ctx context.Context,
	kubeClient client.Client,
	data map[string]string,
	owner client.Object,
)) (
	ctx context.Context,
	kubeClient client.Client,
	data map[string]string,
	owner client.Object,
)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** kubeClient


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** owner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/httpserver/handlers/utils.go:55`



---


[function] name: createSecretWithOwnerReference file: go/internal/httpserver/handlers/utils.go:19 returns_error: нет description: createSecretWithOwnerReference creates a Kubernetes secret with owner reference.
Secret will have the same name and name


### createSecretWithOwnerReference (go/internal/httpserver/handlers/utils.go:19)


createSecretWithOwnerReference creates a Kubernetes secret with owner reference.
Secret will have the same name and namespace as the owner object.


```go
func createSecretWithOwnerReference((
	ctx context.Context,
	kubeClient client.Client,
	data map[string]string,
	owner client.Object,
)) (
	ctx context.Context,
	kubeClient client.Client,
	data map[string]string,
	owner client.Object,
)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** kubeClient


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** owner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/httpserver/handlers/utils.go:19`




## go/internal/httpserver/middleware.go


📄 Исходный файл: `go/internal/httpserver/middleware.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Flush](#flush-gointernalhttpservermiddlewarego48) `:48`

- 🔗 [RespondWithError](#respondwitherror-gointernalhttpservermiddlewarego60) `:60`

- 🔗 [WriteHeader](#writeheader-gointernalhttpservermiddlewarego54) `:54`

- 🔗 [contentTypeMiddleware](#contenttypemiddleware-gointernalhttpservermiddlewarego69) `:69`

- 🔗 [loggingMiddleware](#loggingmiddleware-gointernalhttpservermiddlewarego11) `:11`

- 🔗 [newStatusResponseWriter](#newstatusresponsewriter-gointernalhttpservermiddlewarego44) `:44`


</details>


[function] name: Flush file: go/internal/httpserver/middleware.go:48 returns_error: нет description: —


### Flush (go/internal/httpserver/middleware.go:48)


Flush is a method that performs operations based on the provided parameters and returns ().


```go
func (w *statusResponseWriter) Flush(()) ()
```


📍 *Расположение:* `go/internal/httpserver/middleware.go:48`



---


[function] name: RespondWithError file: go/internal/httpserver/middleware.go:60 returns_error: да description: Forward RespondWithError to underlying writer if it implements ErrorResponseWriter


### RespondWithError (go/internal/httpserver/middleware.go:60)


Forward RespondWithError to underlying writer if it implements ErrorResponseWriter


```go
func (w *statusResponseWriter) RespondWithError((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `go/internal/httpserver/middleware.go:60`



---


[function] name: WriteHeader file: go/internal/httpserver/middleware.go:54 returns_error: нет description: —


### WriteHeader (go/internal/httpserver/middleware.go:54)


WriteHeader is a method that performs operations based on the provided parameters and returns (code int).


```go
func (w *statusResponseWriter) WriteHeader((code int)) (code int)
```


**Тип ответа:** code


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/httpserver/middleware.go:54`



---


[function] name: contentTypeMiddleware file: go/internal/httpserver/middleware.go:69 returns_error: нет description: —


### contentTypeMiddleware (go/internal/httpserver/middleware.go:69)


contentTypeMiddleware is a function that performs operations based on the provided parameters and returns (next http.Handler).


```go
func contentTypeMiddleware((next http.Handler)) (next http.Handler)
```


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Handler


```json
{
  "kubeClient": {},
  "a2aBaseURL": "string",
  "authenticator": {},
  "httpHandler": null,
  "server": null,
  "a2aClients": {}
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


📍 *Расположение:* `go/internal/httpserver/middleware.go:69`



---


[function] name: loggingMiddleware file: go/internal/httpserver/middleware.go:11 returns_error: нет description: —


### loggingMiddleware (go/internal/httpserver/middleware.go:11)


loggingMiddleware is a function that performs operations based on the provided parameters and returns (next http.Handler).


```go
func loggingMiddleware((next http.Handler)) (next http.Handler)
```


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Handler


```json
{
  "kubeClient": {},
  "a2aBaseURL": "string",
  "authenticator": {},
  "httpHandler": null,
  "server": null,
  "a2aClients": {}
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


📍 *Расположение:* `go/internal/httpserver/middleware.go:11`



---


[function] name: newStatusResponseWriter file: go/internal/httpserver/middleware.go:44 returns_error: нет description: —


### newStatusResponseWriter (go/internal/httpserver/middleware.go:44)


newStatusResponseWriter is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter).


```go
func newStatusResponseWriter((w http.ResponseWriter)) (w http.ResponseWriter)
```


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


📍 *Расположение:* `go/internal/httpserver/middleware.go:44`




## go/internal/httpserver/middleware_error.go


📄 Исходный файл: `go/internal/httpserver/middleware_error.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Flush](#flush-gointernalhttpservermiddleware_errorgo34) `:34`

- 🔗 [RespondWithError](#respondwitherror-gointernalhttpservermiddleware_errorgo40) `:40`

- 🔗 [errorHandlerMiddleware](#errorhandlermiddleware-gointernalhttpservermiddleware_errorgo14) `:14`


</details>


[function] name: Flush file: go/internal/httpserver/middleware_error.go:34 returns_error: нет description: —


### Flush (go/internal/httpserver/middleware_error.go:34)


Flush is a method that performs operations based on the provided parameters and returns ().


```go
func (w *errorResponseWriter) Flush(()) ()
```


📍 *Расположение:* `go/internal/httpserver/middleware_error.go:34`



---


[function] name: RespondWithError file: go/internal/httpserver/middleware_error.go:40 returns_error: да description: —


### RespondWithError (go/internal/httpserver/middleware_error.go:40)


RespondWithError is a method that performs operations based on the provided parameters and may return an error.


```go
func (w *errorResponseWriter) RespondWithError((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `go/internal/httpserver/middleware_error.go:40`



---


[function] name: errorHandlerMiddleware file: go/internal/httpserver/middleware_error.go:14 returns_error: нет description: —


### errorHandlerMiddleware (go/internal/httpserver/middleware_error.go:14)


errorHandlerMiddleware is a function that performs operations based on the provided parameters and returns (next http.Handler).


```go
func errorHandlerMiddleware((next http.Handler)) (next http.Handler)
```


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Handler


```json
{
  "kubeClient": {},
  "a2aBaseURL": "string",
  "authenticator": {},
  "httpHandler": null,
  "server": null,
  "a2aClients": {}
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


📍 *Расположение:* `go/internal/httpserver/middleware_error.go:14`




## go/internal/httpserver/server.go


📄 Исходный файл: `go/internal/httpserver/server.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [NeedLeaderElection](#needleaderelection-gointernalhttpserverservergo139) `:139`

- 🔗 [NeedLeaderElection](#needleaderelection-gointernalhttpserverservergo178) `:178`

- 🔗 [NewHTTPServer](#newhttpserver-gointernalhttpserverservergo78) `:78`

- 🔗 [NewMemoryCleanupRunnable](#newmemorycleanuprunnable-gointernalhttpserverservergo144) `:144`

- 🔗 [Start](#start-gointernalhttpserverservergo90) `:90`

- 🔗 [Start](#start-gointernalhttpserverservergo152) `:152`

- 🔗 [Stop](#stop-gointernalhttpserverservergo170) `:170`

- 🔗 [adaptHandler](#adapthandler-gointernalhttpserverservergo289) `:289`

- 🔗 [adaptHealthHandler](#adapthealthhandler-gointernalhttpserverservergo295) `:295`

- 🔗 [setupRoutes](#setuproutes-gointernalhttpserverservergo184) `:184`


</details>


[function] name: NeedLeaderElection file: go/internal/httpserver/server.go:139 returns_error: нет description: —


### NeedLeaderElection (go/internal/httpserver/server.go:139)


NeedLeaderElection is a method that performs operations based on the provided parameters and returns ().


```go
func (m *MemoryCleanupRunnable) NeedLeaderElection(()) ()
```


📍 *Расположение:* `go/internal/httpserver/server.go:139`



---


[function] name: NeedLeaderElection file: go/internal/httpserver/server.go:178 returns_error: нет description: NeedLeaderElection implements controller-runtime's LeaderElectionRunnable interface


### NeedLeaderElection (go/internal/httpserver/server.go:178)


NeedLeaderElection implements controller-runtime's LeaderElectionRunnable interface


```go
func (s *HTTPServer) NeedLeaderElection(()) ()
```


📍 *Расположение:* `go/internal/httpserver/server.go:178`



---


[function] name: NewHTTPServer file: go/internal/httpserver/server.go:78 returns_error: да description: NewHTTPServer creates a new HTTP server instance


### NewHTTPServer (go/internal/httpserver/server.go:78)


NewHTTPServer creates a new HTTP server instance


```go
func NewHTTPServer((*HTTPServer, error)) (*HTTPServer, error)
```


**Тип запроса:** HTTPServer


```json
{
  "httpServer": null,
  "config": {},
  "router": null,
  "handlers": null,
  "dbManager": null,
  "authenticator": {}
}
```


*Определено в:* `go/internal/httpserver/server.go`


**Тип ответа:** HTTPServer


```json
{
  "httpServer": null,
  "config": {},
  "router": null,
  "handlers": null,
  "dbManager": null,
  "authenticator": {}
}
```


*Определено в:* `go/internal/httpserver/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*HTTPServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/httpserver/server.go:78`



---


[function] name: NewMemoryCleanupRunnable file: go/internal/httpserver/server.go:144 returns_error: нет description: NewMemoryCleanupRunnable returns a MemoryCleanupRunnable with the given
database client. interval controls how often the


### NewMemoryCleanupRunnable (go/internal/httpserver/server.go:144)


NewMemoryCleanupRunnable returns a MemoryCleanupRunnable with the given
database client. interval controls how often the cleanup runs; pass 0 to
use the default of 24 hours.


```go
func NewMemoryCleanupRunnable((dbClient dbpkg.Client, interval time.Duration)) (dbClient dbpkg.Client, interval time.Duration)
```


**Тип ответа:** dbClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dbpkg.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


**Тип ответа:** interval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "v": {},
  "defaultValue": {}
}
```


*Определено в:* `go/pkg/env/var.go`


📍 *Расположение:* `go/internal/httpserver/server.go:144`



---


[function] name: Start file: go/internal/httpserver/server.go:90 returns_error: нет description: Start initializes and starts the HTTP server


### Start (go/internal/httpserver/server.go:90)


Start initializes and starts the HTTP server


```go
func (s *HTTPServer) Start((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


📍 *Расположение:* `go/internal/httpserver/server.go:90`



---


[function] name: Start file: go/internal/httpserver/server.go:152 returns_error: нет description: Start runs the periodic cleanup loop until ctx is cancelled.


### Start (go/internal/httpserver/server.go:152)


Start runs the periodic cleanup loop until ctx is cancelled.


```go
func (m *MemoryCleanupRunnable) Start((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


📍 *Расположение:* `go/internal/httpserver/server.go:152`



---


[function] name: Stop file: go/internal/httpserver/server.go:170 returns_error: нет description: Stop stops the HTTP server


### Stop (go/internal/httpserver/server.go:170)


Stop stops the HTTP server


```go
func (s *HTTPServer) Stop((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


📍 *Расположение:* `go/internal/httpserver/server.go:170`



---


[function] name: adaptHandler file: go/internal/httpserver/server.go:289 returns_error: нет description: —


### adaptHandler (go/internal/httpserver/server.go:289)


adaptHandler is a function that performs operations based on the provided parameters and may return an error.


```go
func adaptHandler((h func(handlers.ErrorResponseWriter, *http.Request))) (h func(handlers.ErrorResponseWriter, *http.Request))
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** h


```json
{
  "handlers": {},
  "lock": {},
  "basePathPrefix": "string",
  "authenticator": {}
}
```


*Определено в:* `go/internal/a2a/a2a_handler_mux.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** handlers.ErrorResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/server.go:289`



---


[function] name: adaptHealthHandler file: go/internal/httpserver/server.go:295 returns_error: нет description: —


### adaptHealthHandler (go/internal/httpserver/server.go:295)


adaptHealthHandler is a function that performs operations based on the provided parameters and returns (h func(http.ResponseWriter, *http.Request)).


```go
func adaptHealthHandler((h func(http.ResponseWriter, *http.Request))) (h func(http.ResponseWriter, *http.Request))
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** h


```json
{
  "handlers": {},
  "lock": {},
  "basePathPrefix": "string",
  "authenticator": {}
}
```


*Определено в:* `go/internal/a2a/a2a_handler_mux.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/httpserver/server.go:295`



---


[function] name: setupRoutes file: go/internal/httpserver/server.go:184 returns_error: нет description: setupRoutes configures all the routes for the server


### setupRoutes (go/internal/httpserver/server.go:184)


setupRoutes configures all the routes for the server


```go
func (s *HTTPServer) setupRoutes(()) ()
```


📍 *Расположение:* `go/internal/httpserver/server.go:184`




## go/internal/mcp/mcp_handler.go


📄 Исходный файл: `go/internal/mcp/mcp_handler.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NewMCPHandler](#newmcphandler-gointernalmcpmcp_handlergo60) `:60`

- 🔗 [ServeHTTP](#servehttp-gointernalmcpmcp_handlergo307) `:307`

- 🔗 [Shutdown](#shutdown-gointernalmcpmcp_handlergo313) `:313`

- 🔗 [handleInvokeAgent](#handleinvokeagent-gointernalmcpmcp_handlergo174) `:174`

- 🔗 [handleListAgents](#handlelistagents-gointernalmcpmcp_handlergo107) `:107`


</details>


[function] name: NewMCPHandler file: go/internal/mcp/mcp_handler.go:60 returns_error: да description: NewMCPHandler creates a new MCP handler
Wraps the StreamableHTTPHandler and adds A2A bridging and context management.


### NewMCPHandler (go/internal/mcp/mcp_handler.go:60)


NewMCPHandler creates a new MCP handler
Wraps the StreamableHTTPHandler and adds A2A bridging and context management.


```go
func NewMCPHandler((*MCPHandler, error)) (*MCPHandler, error)
```


**Тип запроса:** MCPHandler


```json
{
  "kubeClient": {},
  "a2aBaseURL": "string",
  "authenticator": {},
  "httpHandler": null,
  "server": null,
  "a2aClients": {}
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


**Тип ответа:** MCPHandler


```json
{
  "kubeClient": {},
  "a2aBaseURL": "string",
  "authenticator": {},
  "httpHandler": null,
  "server": null,
  "a2aClients": {}
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MCPHandler`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/mcp/mcp_handler.go:60`



---


[function] name: ServeHTTP file: go/internal/mcp/mcp_handler.go:307 returns_error: нет description: ServeHTTP implements http.Handler interface


### ServeHTTP (go/internal/mcp/mcp_handler.go:307)


ServeHTTP implements http.Handler interface


```go
func (h *MCPHandler) ServeHTTP((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/mcp/mcp_handler.go:307`



---


[function] name: Shutdown file: go/internal/mcp/mcp_handler.go:313 returns_error: нет description: Shutdown gracefully shuts down the MCP handler


### Shutdown (go/internal/mcp/mcp_handler.go:313)


Shutdown gracefully shuts down the MCP handler


```go
func (h *MCPHandler) Shutdown((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


📍 *Расположение:* `go/internal/mcp/mcp_handler.go:313`



---


[function] name: handleInvokeAgent file: go/internal/mcp/mcp_handler.go:174 returns_error: да description: handleInvokeAgent handles the invoke_agent MCP tool


### handleInvokeAgent (go/internal/mcp/mcp_handler.go:174)


handleInvokeAgent handles the invoke_agent MCP tool


```go
func (h *MCPHandler) handleInvokeAgent((*mcpsdk.CallToolResult, InvokeAgentOutput, error)) (*mcpsdk.CallToolResult, InvokeAgentOutput, error)
```


**Тип запроса:** mcpsdk.CallToolResult


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcpsdk.CallToolResult


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** InvokeAgentOutput


```json
{
  "Agent": "string",
  "Text": "string",
  "ContextID": "string"
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*mcpsdk.CallToolResult`, `InvokeAgentOutput`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/mcp/mcp_handler.go:174`



---


[function] name: handleListAgents file: go/internal/mcp/mcp_handler.go:107 returns_error: да description: handleListAgents handles the list_agents MCP tool


### handleListAgents (go/internal/mcp/mcp_handler.go:107)


handleListAgents handles the list_agents MCP tool


```go
func (h *MCPHandler) handleListAgents((*mcpsdk.CallToolResult, ListAgentsOutput, error)) (*mcpsdk.CallToolResult, ListAgentsOutput, error)
```


**Тип запроса:** mcpsdk.CallToolResult


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcpsdk.CallToolResult


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ListAgentsOutput


```json
{
  "Agents": []
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*mcpsdk.CallToolResult`, `ListAgentsOutput`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/mcp/mcp_handler.go:107`




## go/internal/metrics/version.go


📄 Исходный файл: `go/internal/metrics/version.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewBuildInfoCollector](#newbuildinfocollector-gointernalmetricsversiongo11) `:11`


</details>


[function] name: NewBuildInfoCollector file: go/internal/metrics/version.go:11 returns_error: нет description: NewBuildInfoCollector returns a collector that exports metrics about current version
information.


### NewBuildInfoCollector (go/internal/metrics/version.go:11)


NewBuildInfoCollector returns a collector that exports metrics about current version
information.


```go
func NewBuildInfoCollector(()) ()
```


📍 *Расположение:* `go/internal/metrics/version.go:11`




## go/internal/utils/client_wrapper.go


📄 Исходный файл: `go/internal/utils/client_wrapper.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AddInMemory](#addinmemory-gointernalutilsclient_wrappergo38) `:38`

- 🔗 [Get](#get-gointernalutilsclient_wrappergo52) `:52`

- 🔗 [NewKubeClientWrapper](#newkubeclientwrapper-gointernalutilsclient_wrappergo31) `:31`

- 🔗 [getInMemory](#getinmemory-gointernalutilsclient_wrappergo61) `:61`

- 🔗 [makeTypedObjectKey](#maketypedobjectkey-gointernalutilsclient_wrappergo90) `:90`


</details>


[function] name: AddInMemory file: go/internal/utils/client_wrapper.go:38 returns_error: нет description: —


### AddInMemory (go/internal/utils/client_wrapper.go:38)


AddInMemory is a method that creates new data based on the provided parameters and returns (obj client.Object).


```go
func (w *kubeClientWrapper) AddInMemory((obj client.Object)) (obj client.Object)
```


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/utils/client_wrapper.go:38`



---


[function] name: Get file: go/internal/utils/client_wrapper.go:52 returns_error: нет description: —


### Get (go/internal/utils/client_wrapper.go:52)


Get is a method that retrieves data based on the provided parameters and returns (ctx context.Context, key client.ObjectKey, obj client.Object, opts ...client.GetOption).


```go
func (w *kubeClientWrapper) Get((ctx context.Context, key client.ObjectKey, obj client.Object, opts ...client.GetOption)) (ctx context.Context, key client.ObjectKey, obj client.Object, opts ...client.GetOption)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "AgentName": "string",
  "AgentNamespace": "string",
  "Description": "string",
  "ToolNames": [],
  "SkillNames": []
}
```


*Определено в:* `go/internal/controller/translator/agent/template.go`


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.ObjectKey


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.GetOption


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/utils/client_wrapper.go:52`



---


[function] name: NewKubeClientWrapper file: go/internal/utils/client_wrapper.go:31 returns_error: нет description: —


### NewKubeClientWrapper (go/internal/utils/client_wrapper.go:31)


NewKubeClientWrapper is a function that performs operations based on the provided parameters and returns (kube client.Client).


```go
func NewKubeClientWrapper((kube client.Client)) (kube client.Client)
```


**Тип ответа:** kube


```json
{
  "inMemoryLock": {},
  "inMemory": {}
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Тип ответа:** client.Client


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


📍 *Расположение:* `go/internal/utils/client_wrapper.go:31`



---


[function] name: getInMemory file: go/internal/utils/client_wrapper.go:61 returns_error: да description: —


### getInMemory (go/internal/utils/client_wrapper.go:61)


getInMemory is a method that performs operations based on the provided parameters and may return an error.


```go
func (w *kubeClientWrapper) getInMemory((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/utils/client_wrapper.go:61`



---


[function] name: makeTypedObjectKey file: go/internal/utils/client_wrapper.go:90 returns_error: да description: —


### makeTypedObjectKey (go/internal/utils/client_wrapper.go:90)


makeTypedObjectKey is a function that performs operations based on the provided parameters and may return an error.


```go
func makeTypedObjectKey((typedObjectKey, error)) (typedObjectKey, error)
```


**Тип ответа:** typedObjectKey


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `typedObjectKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/utils/client_wrapper.go:90`




## go/internal/utils/common.go


📄 Исходный файл: `go/internal/utils/common.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [ConvertToKubernetesIdentifier](#converttokubernetesidentifier-gointernalutilscommongo151) `:151`

- 🔗 [ConvertToPythonIdentifier](#converttopythonidentifier-gointernalutilscommongo144) `:144`

- 🔗 [Error](#error-gointernalutilscommongo79) `:79`

- 🔗 [GetControllerName](#getcontrollername-gointernalutilscommongo35) `:35`

- 🔗 [GetObjectRef](#getobjectref-gointernalutilscommongo45) `:45`

- 🔗 [GetResourceNamespace](#getresourcenamespace-gointernalutilscommongo29) `:29`

- 🔗 [ParseRefString](#parserefstring-gointernalutilscommongo85) `:85`

- 🔗 [ParseStringToFloat64](#parsestringtofloat64-gointernalutilscommongo157) `:157`

- 🔗 [ResourceRefString](#resourcerefstring-gointernalutilscommongo40) `:40`

- 🔗 [containsWhitespace](#containswhitespace-gointernalutilscommongo50) `:50`

- 🔗 [validateDNS1123Subdomain](#validatedns1123subdomain-gointernalutilscommongo60) `:60`


</details>


[function] name: ConvertToKubernetesIdentifier file: go/internal/utils/common.go:151 returns_error: нет description: ConvertToKubernetesIdentifier converts Python identifiers back to Kubernetes format
by replacing "__NS__" with slashes a


### ConvertToKubernetesIdentifier (go/internal/utils/common.go:151)


ConvertToKubernetesIdentifier converts Python identifiers back to Kubernetes format
by replacing "__NS__" with slashes and underscores with hyphens.


```go
func ConvertToKubernetesIdentifier((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/internal/utils/common.go:151`



---


[function] name: ConvertToPythonIdentifier file: go/internal/utils/common.go:144 returns_error: нет description: ConvertToPythonIdentifier converts Kubernetes identifiers to Python-compatible format
by replacing hyphens with undersco


### ConvertToPythonIdentifier (go/internal/utils/common.go:144)


ConvertToPythonIdentifier converts Kubernetes identifiers to Python-compatible format
by replacing hyphens with underscores and slashes with "__NS__".


```go
func ConvertToPythonIdentifier((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/internal/utils/common.go:144`



---


[function] name: Error file: go/internal/utils/common.go:79 returns_error: нет description: —


### Error (go/internal/utils/common.go:79)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e *EmptyReferenceError) Error(()) ()
```


📍 *Расположение:* `go/internal/utils/common.go:79`



---


[function] name: GetControllerName file: go/internal/utils/common.go:35 returns_error: нет description: GetControllerName returns the name for the kagent controller,
using the KAGENT_CONTROLLER_NAME environment variable or d


### GetControllerName (go/internal/utils/common.go:35)


GetControllerName returns the name for the kagent controller,
using the KAGENT_CONTROLLER_NAME environment variable or defaulting to "kagent-controller".


```go
func GetControllerName(()) ()
```


📍 *Расположение:* `go/internal/utils/common.go:35`



---


[function] name: GetObjectRef file: go/internal/utils/common.go:45 returns_error: нет description: GetObjectRef formats a Kubernetes object reference as "namespace/name" string.


### GetObjectRef (go/internal/utils/common.go:45)


GetObjectRef formats a Kubernetes object reference as "namespace/name" string.


```go
func GetObjectRef((obj client.Object)) (obj client.Object)
```


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.Object


```json
{
  "gvk": {},
  "name": "string",
  "namespace": "string"
}
```


*Определено в:* `go/internal/utils/client_wrapper.go`


📍 *Расположение:* `go/internal/utils/common.go:45`



---


[function] name: GetResourceNamespace file: go/internal/utils/common.go:29 returns_error: нет description: GetResourceNamespace returns the namespace for resources,
using the KAGENT_NAMESPACE environment variable or defaulting 


### GetResourceNamespace (go/internal/utils/common.go:29)


GetResourceNamespace returns the namespace for resources,
using the KAGENT_NAMESPACE environment variable or defaulting to "kagent".


```go
func GetResourceNamespace(()) ()
```


📍 *Расположение:* `go/internal/utils/common.go:29`



---


[function] name: ParseRefString file: go/internal/utils/common.go:85 returns_error: да description: ParseRefString parses a string reference (either "namespace/name" or just "name")
into a NamespacedName object, using pa


### ParseRefString (go/internal/utils/common.go:85)


ParseRefString parses a string reference (either "namespace/name" or just "name")
into a NamespacedName object, using parentNamespace when namespace is not specified.


```go
func ParseRefString((types.NamespacedName, error)) (types.NamespacedName, error)
```


**Тип ответа:** types.NamespacedName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `types.NamespacedName`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/utils/common.go:85`



---


[function] name: ParseStringToFloat64 file: go/internal/utils/common.go:157 returns_error: нет description: ParseStringToFloat64 parses a string to float64, returns nil if empty or invalid


### ParseStringToFloat64 (go/internal/utils/common.go:157)


ParseStringToFloat64 parses a string to float64, returns nil if empty or invalid


```go
func ParseStringToFloat64((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/utils/common.go:157`



---


[function] name: ResourceRefString file: go/internal/utils/common.go:40 returns_error: нет description: ResourceRefString formats namespace and name as a string reference in "namespace/name" format.


### ResourceRefString (go/internal/utils/common.go:40)


ResourceRefString formats namespace and name as a string reference in "namespace/name" format.


```go
func ResourceRefString((namespace, name string)) (namespace, name string)
```


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/internal/utils/common.go:40`



---


[function] name: containsWhitespace file: go/internal/utils/common.go:50 returns_error: нет description: containsWhitespace reports whether s contains any Unicode whitespace characters.


### containsWhitespace (go/internal/utils/common.go:50)


containsWhitespace reports whether s contains any Unicode whitespace characters.


```go
func containsWhitespace((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/internal/utils/common.go:50`



---


[function] name: validateDNS1123Subdomain file: go/internal/utils/common.go:60 returns_error: нет description: validateDNS1123Subdomain validates a DNS1123 subdomain and returns a descriptive error


### validateDNS1123Subdomain (go/internal/utils/common.go:60)


validateDNS1123Subdomain validates a DNS1123 subdomain and returns a descriptive error


```go
func validateDNS1123Subdomain((value, fieldName string)) (value, fieldName string)
```


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fieldName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/internal/utils/common.go:60`




## go/internal/utils/config_map.go


📄 Исходный файл: `go/internal/utils/config_map.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetConfigMapData](#getconfigmapdata-gointernalutilsconfig_mapgo12) `:12`

- 🔗 [GetConfigMapValue](#getconfigmapvalue-gointernalutilsconfig_mapgo21) `:21`


</details>


[function] name: GetConfigMapData file: go/internal/utils/config_map.go:12 returns_error: да description: GetConfigMapData fetches all data from a ConfigMap.


### GetConfigMapData (go/internal/utils/config_map.go:12)


GetConfigMapData fetches all data from a ConfigMap.


```go
func GetConfigMapData((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/utils/config_map.go:12`



---


[function] name: GetConfigMapValue file: go/internal/utils/config_map.go:21 returns_error: да description: GetConfigMapValue fetches a value from a ConfigMap


### GetConfigMapValue (go/internal/utils/config_map.go:21)


GetConfigMapValue fetches a value from a ConfigMap


```go
func GetConfigMapValue((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/utils/config_map.go:21`




## go/internal/utils/iter.go


📄 Исходный файл: `go/internal/utils/iter.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Filter](#filter-gointernalutilsitergo16) `:16`

- 🔗 [Map](#map-gointernalutilsitergo6) `:6`


</details>


[function] name: Filter file: go/internal/utils/iter.go:16 returns_error: нет description: —


### Filter (go/internal/utils/iter.go:16)


Filter is a function that performs operations based on the provided parameters and returns (s iter.Seq[E], f func(E) bool).


```go
func Filter((s iter.Seq[E], f func(E) bool)) (s iter.Seq[E], f func(E) bool)
```


**Тип ответа:** s


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** iter.Seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** E


```json
{
  "Err": {}
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


**Тип ответа:** f


```json
{
  "DatabasePath": "string",
  "VectorEnabled": false
}
```


*Определено в:* `go/internal/database/manager.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** E


```json
{
  "Err": {}
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


📍 *Расположение:* `go/internal/utils/iter.go:16`



---


[function] name: Map file: go/internal/utils/iter.go:6 returns_error: нет description: Map returns an iterator over the slice, applying the function f to each element.


### Map (go/internal/utils/iter.go:6)


Map returns an iterator over the slice, applying the function f to each element.


```go
func Map((s iter.Seq[E], f func(E) F)) (s iter.Seq[E], f func(E) F)
```


**Тип ответа:** s


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** iter.Seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** E


```json
{
  "Err": {}
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


**Тип ответа:** f


```json
{
  "DatabasePath": "string",
  "VectorEnabled": false
}
```


*Определено в:* `go/internal/database/manager.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** E


```json
{
  "Err": {}
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


**Тип ответа:** F


```json
{
  "mu": {},
  "feedback": {},
  "tasks": {},
  "sessions": {},
  "agents": {},
  "toolServers": {},
  "tools": {},
  "eventsBySession": {},
  "events": {},
  "pushNotifications": {},
  "checkpoints": {},
  "checkpointWrites": {},
  "crewaiMemory": {},
  "crewaiFlowStates": {},
  "memories": {},
  "nextFeedbackID": 0
}
```


*Определено в:* `go/internal/database/fake/client.go`


📍 *Расположение:* `go/internal/utils/iter.go:6`




## go/internal/utils/secret.go


📄 Исходный файл: `go/internal/utils/secret.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetSecretValue](#getsecretvalue-gointernalutilssecretgo12) `:12`


</details>


[function] name: GetSecretValue file: go/internal/utils/secret.go:12 returns_error: да description: GetSecretValue fetches a value from a Secret


### GetSecretValue (go/internal/utils/secret.go:12)


GetSecretValue fetches a value from a Secret


```go
func GetSecretValue((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/internal/utils/secret.go:12`




## go/internal/version/version.go


📄 Исходный файл: `go/internal/version/version.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Get](#get-gointernalversionversiongo26) `:26`

- 🔗 [GetFull](#getfull-gointernalversionversiongo59) `:59`

- 🔗 [GetShort](#getshort-gointernalversionversiongo54) `:54`

- 🔗 [GetVersion](#getversion-gointernalversionversiongo49) `:49`

- 🔗 [Short](#short-gointernalversionversiongo44) `:44`

- 🔗 [String](#string-gointernalversionversiongo38) `:38`


</details>


[function] name: Get file: go/internal/version/version.go:26 returns_error: нет description: Get returns version information


### Get (go/internal/version/version.go:26)


Get returns version information


```go
func Get(()) ()
```


📍 *Расположение:* `go/internal/version/version.go:26`



---


[function] name: GetFull file: go/internal/version/version.go:59 returns_error: нет description: GetFull returns the full version information as a string


### GetFull (go/internal/version/version.go:59)


GetFull returns the full version information as a string


```go
func GetFull(()) ()
```


📍 *Расположение:* `go/internal/version/version.go:59`



---


[function] name: GetShort file: go/internal/version/version.go:54 returns_error: нет description: GetShort returns a short version string using the package variables


### GetShort (go/internal/version/version.go:54)


GetShort returns a short version string using the package variables


```go
func GetShort(()) ()
```


📍 *Расположение:* `go/internal/version/version.go:54`



---


[function] name: GetVersion file: go/internal/version/version.go:49 returns_error: нет description: GetVersion returns just the version string


### GetVersion (go/internal/version/version.go:49)


GetVersion returns just the version string


```go
func GetVersion(()) ()
```


📍 *Расположение:* `go/internal/version/version.go:49`



---


[function] name: Short file: go/internal/version/version.go:44 returns_error: нет description: Short returns a short version string


### Short (go/internal/version/version.go:44)


Short returns a short version string


```go
func (i Info) Short(()) ()
```


📍 *Расположение:* `go/internal/version/version.go:44`



---


[function] name: String file: go/internal/version/version.go:38 returns_error: нет description: String returns a human-readable version string


### String (go/internal/version/version.go:38)


String returns a human-readable version string


```go
func (i Info) String(()) ()
```


📍 *Расположение:* `go/internal/version/version.go:38`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_hack.md)

- [Следующая директория](go_pkg.md)


---

