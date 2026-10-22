---
title: "Функции: contrib/go-adk"
type: functions
repo: kagent
language: ru
chunk_boundary: h3
group: contrib/go-adk
---


# Функции: contrib/go-adk


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Следующая директория](go_api.md)


---


## Меню по файлам


- 📄 [contrib/go-adk/cmd/main.go](#contribgo-adkcmdmaingo)

- 📄 [contrib/go-adk/examples/byo/main.go](#contribgo-adkexamplesbyomaingo)

- 📄 [contrib/go-adk/pkg/a2a/agentcard.go](#contribgo-adkpkga2aagentcardgo)

- 📄 [contrib/go-adk/pkg/a2a/eventqueue.go](#contribgo-adkpkga2aeventqueuego)

- 📄 [contrib/go-adk/pkg/a2a/executor.go](#contribgo-adkpkga2aexecutorgo)

- 📄 [contrib/go-adk/pkg/a2a/hitl.go](#contribgo-adkpkga2ahitlgo)

- 📄 [contrib/go-adk/pkg/a2a/server/health.go](#contribgo-adkpkga2aserverhealthgo)

- 📄 [contrib/go-adk/pkg/a2a/server/server.go](#contribgo-adkpkga2aserverservergo)

- 📄 [contrib/go-adk/pkg/agent/agent.go](#contribgo-adkpkgagentagentgo)

- 📄 [contrib/go-adk/pkg/app/app.go](#contribgo-adkpkgappappgo)

- 📄 [contrib/go-adk/pkg/auth/token.go](#contribgo-adkpkgauthtokengo)

- 📄 [contrib/go-adk/pkg/config/config_loader.go](#contribgo-adkpkgconfigconfig_loadergo)

- 📄 [contrib/go-adk/pkg/config/config_usage.go](#contribgo-adkpkgconfigconfig_usagego)

- 📄 [contrib/go-adk/pkg/config/types.go](#contribgo-adkpkgconfigtypesgo)

- 📄 [contrib/go-adk/pkg/mcp/registry.go](#contribgo-adkpkgmcpregistrygo)

- 📄 [contrib/go-adk/pkg/models/anthropic.go](#contribgo-adkpkgmodelsanthropicgo)

- 📄 [contrib/go-adk/pkg/models/anthropic_adk.go](#contribgo-adkpkgmodelsanthropic_adkgo)

- 📄 [contrib/go-adk/pkg/models/openai.go](#contribgo-adkpkgmodelsopenaigo)

- 📄 [contrib/go-adk/pkg/models/openai_adk.go](#contribgo-adkpkgmodelsopenai_adkgo)

- 📄 [contrib/go-adk/pkg/runner/adapter.go](#contribgo-adkpkgrunneradaptergo)

- 📄 [contrib/go-adk/pkg/session/adapter.go](#contribgo-adkpkgsessionadaptergo)

- 📄 [contrib/go-adk/pkg/session/local_session.go](#contribgo-adkpkgsessionlocal_sessiongo)

- 📄 [contrib/go-adk/pkg/session/session.go](#contribgo-adkpkgsessionsessiongo)

- 📄 [contrib/go-adk/pkg/skills/discovery.go](#contribgo-adkpkgskillsdiscoverygo)

- 📄 [contrib/go-adk/pkg/skills/shell.go](#contribgo-adkpkgskillsshellgo)

- 📄 [contrib/go-adk/pkg/skills/skills_tools.go](#contribgo-adkpkgskillsskills_toolsgo)

- 📄 [contrib/go-adk/pkg/taskstore/a2a_adapter.go](#contribgo-adkpkgtaskstorea2a_adaptergo)

- 📄 [contrib/go-adk/pkg/taskstore/store.go](#contribgo-adkpkgtaskstorestorego)

- 📄 [contrib/go-adk/pkg/telemetry/tracing.go](#contribgo-adkpkgtelemetrytracinggo)


---


## contrib/go-adk/cmd/main.go


📄 Исходный файл: `contrib/go-adk/cmd/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [deriveAppName](#deriveappname-contribgo-adkcmdmaingo176) `:176`

- 🔗 [main](#main-contribgo-adkcmdmaingo57) `:57`

- 🔗 [setupLogger](#setuplogger-contribgo-adkcmdmaingo26) `:26`


</details>


[function] name: deriveAppName file: contrib/go-adk/cmd/main.go:176 returns_error: нет description: —


### deriveAppName (contrib/go-adk/cmd/main.go:176)


deriveAppName is a function that performs operations based on the provided parameters and returns (agentCard *a2atype.AgentCard, logger logr.Logger).


```go
func deriveAppName((agentCard *a2atype.AgentCard, logger logr.Logger)) (agentCard *a2atype.AgentCard, logger logr.Logger)
```


**Тип запроса:** a2atype.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/cmd/main.go:176`



---


[function] name: main file: contrib/go-adk/cmd/main.go:57 returns_error: нет description: —


### main (contrib/go-adk/cmd/main.go:57)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `contrib/go-adk/cmd/main.go:57`



---


[function] name: setupLogger file: contrib/go-adk/cmd/main.go:26 returns_error: нет description: —


### setupLogger (contrib/go-adk/cmd/main.go:26)


setupLogger is a function that performs operations based on the provided parameters and returns (logr.Logger, *zap.Logger).


```go
func setupLogger((logr.Logger, *zap.Logger)) (logr.Logger, *zap.Logger)
```


**Тип запроса:** zap.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** zap.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/cmd/main.go:26`




## contrib/go-adk/examples/byo/main.go


📄 Исходный файл: `contrib/go-adk/examples/byo/main.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-contribgo-adkexamplesbyomaingo58) `:58`


</details>


[function] name: main file: contrib/go-adk/examples/byo/main.go:58 returns_error: нет description: —


### main (contrib/go-adk/examples/byo/main.go:58)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `contrib/go-adk/examples/byo/main.go:58`




## contrib/go-adk/pkg/a2a/agentcard.go


📄 Исходный файл: `contrib/go-adk/pkg/a2a/agentcard.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [EnrichAgentCard](#enrichagentcard-contribgo-adkpkga2aagentcardgo12) `:12`


</details>


[function] name: EnrichAgentCard file: contrib/go-adk/pkg/a2a/agentcard.go:12 returns_error: нет description: EnrichAgentCard populates the agent card with skills derived from the ADK
agent using adka2a.BuildAgentSkills. It also f


### EnrichAgentCard (contrib/go-adk/pkg/a2a/agentcard.go:12)


EnrichAgentCard populates the agent card with skills derived from the ADK
agent using adka2a.BuildAgentSkills. It also fills in the description from
the agent when the card has none.


```go
func EnrichAgentCard((card *a2atype.AgentCard, agent adkagent.Agent)) (card *a2atype.AgentCard, agent adkagent.Agent)
```


**Тип запроса:** a2atype.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** card


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** adkagent.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `contrib/go-adk/pkg/a2a/agentcard.go:12`




## contrib/go-adk/pkg/a2a/eventqueue.go


📄 Исходный файл: `contrib/go-adk/pkg/a2a/eventqueue.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Cancel](#cancel-contribgo-adkpkga2aeventqueuego68) `:68`

- 🔗 [Execute](#execute-contribgo-adkpkga2aeventqueuego61) `:61`

- 🔗 [NewEventQueue](#neweventqueue-contribgo-adkpkga2aeventqueuego44) `:44`

- 🔗 [WrapExecutorQueue](#wrapexecutorqueue-contribgo-adkpkga2aeventqueuego51) `:51`

- 🔗 [Write](#write-contribgo-adkpkga2aeventqueuego72) `:72`

- 🔗 [filterNonEmptyParts](#filternonemptyparts-contribgo-adkpkga2aeventqueuego141) `:141`

- 🔗 [filterTextParts](#filtertextparts-contribgo-adkpkga2aeventqueuego152) `:152`

- 🔗 [handleArtifactEvent](#handleartifactevent-contribgo-adkpkga2aeventqueuego83) `:83`

- 🔗 [handleStatusEvent](#handlestatusevent-contribgo-adkpkga2aeventqueuego118) `:118`

- 🔗 [isEmptyDataPart](#isemptydatapart-contribgo-adkpkga2aeventqueuego134) `:134`


</details>


[function] name: Cancel file: contrib/go-adk/pkg/a2a/eventqueue.go:68 returns_error: нет description: —


### Cancel (contrib/go-adk/pkg/a2a/eventqueue.go:68)


Cancel is a method that performs operations based on the provided parameters and returns (ctx context.Context, reqCtx *a2asrv.RequestContext, queue eventqueue.Queue).


```go
func (w *executorQueueWrapper) Cancel((ctx context.Context, reqCtx *a2asrv.RequestContext, queue eventqueue.Queue)) (ctx context.Context, reqCtx *a2asrv.RequestContext, queue eventqueue.Queue)
```


**Тип запроса:** a2asrv.RequestContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** reqCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2asrv.RequestContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** queue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** eventqueue.Queue


```json
{
  "reqCtx": null,
  "lastTextParts": {},
  "lastTextMeta": {}
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/eventqueue.go`


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:68`



---


[function] name: Execute file: contrib/go-adk/pkg/a2a/eventqueue.go:61 returns_error: нет description: —


### Execute (contrib/go-adk/pkg/a2a/eventqueue.go:61)


Execute is a method that performs operations based on the provided parameters and returns (ctx context.Context, reqCtx *a2asrv.RequestContext, queue eventqueue.Queue).


```go
func (w *executorQueueWrapper) Execute((ctx context.Context, reqCtx *a2asrv.RequestContext, queue eventqueue.Queue)) (ctx context.Context, reqCtx *a2asrv.RequestContext, queue eventqueue.Queue)
```


**Тип запроса:** a2asrv.RequestContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** reqCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2asrv.RequestContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** queue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** eventqueue.Queue


```json
{
  "reqCtx": null,
  "lastTextParts": {},
  "lastTextMeta": {}
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/eventqueue.go`


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:61`



---


[function] name: NewEventQueue file: contrib/go-adk/pkg/a2a/eventqueue.go:44 returns_error: нет description: NewEventQueue creates an EventQueue that wraps inner and mirrors artifact
events as status events for UI streaming and h


### NewEventQueue (contrib/go-adk/pkg/a2a/eventqueue.go:44)


NewEventQueue creates an EventQueue that wraps inner and mirrors artifact
events as status events for UI streaming and history population.


```go
func NewEventQueue((inner eventqueue.Queue, reqCtx *a2asrv.RequestContext)) (inner eventqueue.Queue, reqCtx *a2asrv.RequestContext)
```


**Тип запроса:** a2asrv.RequestContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** inner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** eventqueue.Queue


```json
{
  "reqCtx": null,
  "lastTextParts": {},
  "lastTextMeta": {}
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/eventqueue.go`


**Тип ответа:** reqCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2asrv.RequestContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:44`



---


[function] name: WrapExecutorQueue file: contrib/go-adk/pkg/a2a/eventqueue.go:51 returns_error: нет description: WrapExecutorQueue wraps an a2asrv.AgentExecutor so that each execution's
queue is automatically wrapped with an EventQue


### WrapExecutorQueue (contrib/go-adk/pkg/a2a/eventqueue.go:51)


WrapExecutorQueue wraps an a2asrv.AgentExecutor so that each execution's
queue is automatically wrapped with an EventQueue. Use this for opaque
executors where you cannot modify the Execute method.


```go
func WrapExecutorQueue((inner a2asrv.AgentExecutor)) (inner a2asrv.AgentExecutor)
```


**Тип ответа:** inner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2asrv.AgentExecutor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:51`



---


[function] name: Write file: contrib/go-adk/pkg/a2a/eventqueue.go:72 returns_error: нет description: —


### Write (contrib/go-adk/pkg/a2a/eventqueue.go:72)


Write is a method that performs operations based on the provided parameters and returns (ctx context.Context, event a2atype.Event).


```go
func (q *EventQueue) Write((ctx context.Context, event a2atype.Event)) (ctx context.Context, event a2atype.Event)
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


**Тип ответа:** event


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.Event


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


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:72`



---


[function] name: filterNonEmptyParts file: contrib/go-adk/pkg/a2a/eventqueue.go:141 returns_error: нет description: filterNonEmptyParts returns a2a parts with empty DataParts removed.
Returns nil when no parts pass the filter.


### filterNonEmptyParts (contrib/go-adk/pkg/a2a/eventqueue.go:141)


filterNonEmptyParts returns a2a parts with empty DataParts removed.
Returns nil when no parts pass the filter.


```go
func filterNonEmptyParts((parts a2atype.ContentParts)) (parts a2atype.ContentParts)
```


**Тип ответа:** parts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.ContentParts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:141`



---


[function] name: filterTextParts file: contrib/go-adk/pkg/a2a/eventqueue.go:152 returns_error: нет description: filterTextParts returns only TextParts from the given parts.


### filterTextParts (contrib/go-adk/pkg/a2a/eventqueue.go:152)


filterTextParts returns only TextParts from the given parts.


```go
func filterTextParts((parts a2atype.ContentParts)) (parts a2atype.ContentParts)
```


**Тип ответа:** parts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.ContentParts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:152`



---


[function] name: handleArtifactEvent file: contrib/go-adk/pkg/a2a/eventqueue.go:83 returns_error: нет description: —


### handleArtifactEvent (contrib/go-adk/pkg/a2a/eventqueue.go:83)


handleArtifactEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, ev *a2atype.TaskArtifactUpdateEvent).


```go
func (q *EventQueue) handleArtifactEvent((ctx context.Context, ev *a2atype.TaskArtifactUpdateEvent)) (ctx context.Context, ev *a2atype.TaskArtifactUpdateEvent)
```


**Тип запроса:** a2atype.TaskArtifactUpdateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** ev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.TaskArtifactUpdateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:83`



---


[function] name: handleStatusEvent file: contrib/go-adk/pkg/a2a/eventqueue.go:118 returns_error: нет description: —


### handleStatusEvent (contrib/go-adk/pkg/a2a/eventqueue.go:118)


handleStatusEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, ev *a2atype.TaskStatusUpdateEvent).


```go
func (q *EventQueue) handleStatusEvent((ctx context.Context, ev *a2atype.TaskStatusUpdateEvent)) (ctx context.Context, ev *a2atype.TaskStatusUpdateEvent)
```


**Тип запроса:** a2atype.TaskStatusUpdateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** ev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.TaskStatusUpdateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:118`



---


[function] name: isEmptyDataPart file: contrib/go-adk/pkg/a2a/eventqueue.go:134 returns_error: нет description: isEmptyDataPart returns true if the part is a DataPart with nil or empty Data.
The ADK processor emits such parts as cle


### isEmptyDataPart (contrib/go-adk/pkg/a2a/eventqueue.go:134)


isEmptyDataPart returns true if the part is a DataPart with nil or empty Data.
The ADK processor emits such parts as cleanup signals for streaming partial
artifacts and as a fallback for unrecognized GenAI part types.


```go
func isEmptyDataPart((part a2atype.Part)) (part a2atype.Part)
```


**Тип ответа:** part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.Part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/eventqueue.go:134`




## contrib/go-adk/pkg/a2a/executor.go


📄 Исходный файл: `contrib/go-adk/pkg/a2a/executor.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [NewExecutorConfig](#newexecutorconfig-contribgo-adkpkga2aexecutorgo30) `:30`

- 🔗 [a2aPartConverter](#a2apartconverter-contribgo-adkpkga2aexecutorgo170) `:170`

- 🔗 [afterExecute](#afterexecute-contribgo-adkpkga2aexecutorgo125) `:125`

- 🔗 [beforeExecute](#beforeexecute-contribgo-adkpkga2aexecutorgo74) `:74`

- 🔗 [convertDataPartToGenAI](#convertdataparttogenai-contribgo-adkpkga2aexecutorgo227) `:227`

- 🔗 [extractApprovalRequestsFromA2AParts](#extractapprovalrequestsfroma2aparts-contribgo-adkpkga2aexecutorgo185) `:185`

- 🔗 [extractSessionName](#extractsessionname-contribgo-adkpkga2aexecutorgo258) `:258`

- 🔗 [genAIPartConverter](#genaipartconverter-contribgo-adkpkga2aexecutorgo149) `:149`

- 🔗 [isLongRunningDataPart](#islongrunningdatapart-contribgo-adkpkga2aexecutorgo212) `:212`


</details>


[function] name: NewExecutorConfig file: contrib/go-adk/pkg/a2a/executor.go:30 returns_error: нет description: NewExecutorConfig builds an adka2a.ExecutorConfig with kagent-specific
callbacks wired in. The returned config can be pa


### NewExecutorConfig (contrib/go-adk/pkg/a2a/executor.go:30)


NewExecutorConfig builds an adka2a.ExecutorConfig with kagent-specific
callbacks wired in. The returned config can be passed directly to
adka2a.NewExecutor.


```go
func NewExecutorConfig((
	runnerConfig runner.Config,
	sessionService session.SessionService,
	stream bool,
	appName string,
	logger logr.Logger,
)) (
	runnerConfig runner.Config,
	sessionService session.SessionService,
	stream bool,
	appName string,
	logger logr.Logger,
)
```


**Тип ответа:** runnerConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** runner.Config


```json
{
  "Metrics": {},
  "Webhook": {},
  "Streaming": {},
  "Proxy": {},
  "LeaderElection": false,
  "ProbeAddr": "string",
  "SecureMetrics": false,
  "EnableHTTP2": false,
  "DefaultModelConfig": {},
  "HttpServerAddr": "string",
  "WatchNamespaces": "string",
  "A2ABaseUrl": "string",
  "Database": {}
}
```


*Определено в:* `go/pkg/app/app.go`


**Тип ответа:** sessionService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** session.SessionService


```json
{
  "BaseURL": "string",
  "Client": null
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


**Тип ответа:** stream


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:30`



---


[function] name: a2aPartConverter file: contrib/go-adk/pkg/a2a/executor.go:170 returns_error: да description: a2aPartConverter converts A2A parts to GenAI parts. DataParts with
kagent_type metadata (from older sessions) are handle


### a2aPartConverter (contrib/go-adk/pkg/a2a/executor.go:170)


a2aPartConverter converts A2A parts to GenAI parts. DataParts with
kagent_type metadata (from older sessions) are handled explicitly;
all other parts (including adk_type) fall through to the ADK default.


```go
func a2aPartConverter((*genai.Part, error)) (*genai.Part, error)
```


**Тип запроса:** genai.Part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genai.Part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*genai.Part`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:170`



---


[function] name: afterExecute file: contrib/go-adk/pkg/a2a/executor.go:125 returns_error: да description: afterExecute handles HITL enrichment for input_required states.
The ADK executor already populates adk_* metadata on the


### afterExecute (contrib/go-adk/pkg/a2a/executor.go:125)


afterExecute handles HITL enrichment for input_required states.
The ADK executor already populates adk_* metadata on the final event.


```go
func (cb *kagentCallbacks) afterExecute((ctx adka2a.ExecutorContext, finalEvent *a2atype.TaskStatusUpdateEvent, err error)) (ctx adka2a.ExecutorContext, finalEvent *a2atype.TaskStatusUpdateEvent, err error)
```


**Тип запроса:** a2atype.TaskStatusUpdateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adka2a.ExecutorContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** finalEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.TaskStatusUpdateEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx adka2a.ExecutorContext`, `finalEvent *a2atype.TaskStatusUpdateEvent`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:125`



---


[function] name: beforeExecute file: contrib/go-adk/pkg/a2a/executor.go:74 returns_error: да description: beforeExecute sets up tracing, creates the session with session_name if
needed, initializes skills, and appends the syst


### beforeExecute (contrib/go-adk/pkg/a2a/executor.go:74)


beforeExecute sets up tracing, creates the session with session_name if
needed, initializes skills, and appends the system header event.


```go
func (cb *kagentCallbacks) beforeExecute((context.Context, error)) (context.Context, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `context.Context`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:74`



---


[function] name: convertDataPartToGenAI file: contrib/go-adk/pkg/a2a/executor.go:227 returns_error: да description: convertDataPartToGenAI converts a DataPart with a type metadata key
(either adk_type or kagent_type) back to GenAI for i


### convertDataPartToGenAI (contrib/go-adk/pkg/a2a/executor.go:227)


convertDataPartToGenAI converts a DataPart with a type metadata key
(either adk_type or kagent_type) back to GenAI for inbound message processing.


```go
func convertDataPartToGenAI((*genai.Part, error)) (*genai.Part, error)
```


**Тип запроса:** genai.Part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genai.Part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*genai.Part`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:227`



---


[function] name: extractApprovalRequestsFromA2AParts file: contrib/go-adk/pkg/a2a/executor.go:185 returns_error: нет description: extractApprovalRequestsFromA2AParts extracts tool approval requests from
A2A data parts that represent long-running func


### extractApprovalRequestsFromA2AParts (contrib/go-adk/pkg/a2a/executor.go:185)


extractApprovalRequestsFromA2AParts extracts tool approval requests from
A2A data parts that represent long-running function calls.


```go
func extractApprovalRequestsFromA2AParts((parts a2atype.ContentParts)) (parts a2atype.ContentParts)
```


**Тип ответа:** parts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.ContentParts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:185`



---


[function] name: extractSessionName file: contrib/go-adk/pkg/a2a/executor.go:258 returns_error: нет description: extractSessionName extracts session name from the first text part of a message.


### extractSessionName (contrib/go-adk/pkg/a2a/executor.go:258)


extractSessionName extracts session name from the first text part of a message.


```go
func extractSessionName((message *a2atype.Message)) (message *a2atype.Message)
```


**Тип запроса:** a2atype.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:258`



---


[function] name: genAIPartConverter file: contrib/go-adk/pkg/a2a/executor.go:149 returns_error: да description: ---------------------------------------------------------------------------
Part converters
----------------------------


### genAIPartConverter (contrib/go-adk/pkg/a2a/executor.go:149)


---------------------------------------------------------------------------
Part converters
---------------------------------------------------------------------------
genAIPartConverter converts GenAI parts to A2A parts, filtering out
empty DataParts produced by the ADK for streaming cleanup signals.


```go
func genAIPartConverter((a2atype.Part, error)) (a2atype.Part, error)
```


**Тип ответа:** a2atype.Part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `a2atype.Part`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:149`



---


[function] name: isLongRunningDataPart file: contrib/go-adk/pkg/a2a/executor.go:212 returns_error: нет description: isLongRunningDataPart checks both kagent_is_long_running and adk_is_long_running
metadata keys for backward compatibilit


### isLongRunningDataPart (contrib/go-adk/pkg/a2a/executor.go:212)


isLongRunningDataPart checks both kagent_is_long_running and adk_is_long_running
metadata keys for backward compatibility.


```go
func isLongRunningDataPart((dp a2atype.DataPart)) (dp a2atype.DataPart)
```


**Тип ответа:** dp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.DataPart


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/executor.go:212`




## contrib/go-adk/pkg/a2a/hitl.go


📄 Исходный файл: `contrib/go-adk/pkg/a2a/hitl.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [BuildToolApprovalMessage](#buildtoolapprovalmessage-contribgo-adkpkga2ahitlgo137) `:137`

- 🔗 [ExtractDecisionFromMessage](#extractdecisionfrommessage-contribgo-adkpkga2ahitlgo79) `:79`

- 🔗 [ExtractDecisionFromText](#extractdecisionfromtext-contribgo-adkpkga2ahitlgo62) `:62`

- 🔗 [GetKAgentMetadataKey](#getkagentmetadatakey-contribgo-adkpkga2ahitlgo55) `:55`

- 🔗 [escapeMarkdownBackticks](#escapemarkdownbackticks-contribgo-adkpkga2ahitlgo109) `:109`

- 🔗 [formatToolApprovalTextParts](#formattoolapprovaltextparts-contribgo-adkpkga2ahitlgo115) `:115`

- 🔗 [init](#init-contribgo-adkpkga2ahitlgo16) `:16`


</details>


[function] name: BuildToolApprovalMessage file: contrib/go-adk/pkg/a2a/hitl.go:137 returns_error: нет description: BuildToolApprovalMessage creates an A2A message with human-readable text
describing the tool calls and a structured Data


### BuildToolApprovalMessage (contrib/go-adk/pkg/a2a/hitl.go:137)


BuildToolApprovalMessage creates an A2A message with human-readable text
describing the tool calls and a structured DataPart for machine processing
by the client.


```go
func BuildToolApprovalMessage((actionRequests []ToolApprovalRequest)) (actionRequests []ToolApprovalRequest)
```


**Тип ответа:** actionRequests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolApprovalRequest


```json
{
  "Name": "string",
  "Args": {},
  "ID": "string"
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/hitl.go`


📍 *Расположение:* `contrib/go-adk/pkg/a2a/hitl.go:137`



---


[function] name: ExtractDecisionFromMessage file: contrib/go-adk/pkg/a2a/hitl.go:79 returns_error: нет description: ExtractDecisionFromMessage extracts a decision from an A2A message.
Priority 1: DataPart with decision_type field.
Prior


### ExtractDecisionFromMessage (contrib/go-adk/pkg/a2a/hitl.go:79)


ExtractDecisionFromMessage extracts a decision from an A2A message.
Priority 1: DataPart with decision_type field.
Priority 2: TextPart keyword matching.


```go
func ExtractDecisionFromMessage((message *a2atype.Message)) (message *a2atype.Message)
```


**Тип запроса:** a2atype.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/hitl.go:79`



---


[function] name: ExtractDecisionFromText file: contrib/go-adk/pkg/a2a/hitl.go:62 returns_error: нет description: ExtractDecisionFromText extracts a decision from text using whole-word
keyword matching. Word boundaries prevent false p


### ExtractDecisionFromText (contrib/go-adk/pkg/a2a/hitl.go:62)


ExtractDecisionFromText extracts a decision from text using whole-word
keyword matching. Word boundaries prevent false positives from substrings
(e.g. "no" inside "know", "yes" inside "yesterday").


```go
func ExtractDecisionFromText((text string)) (text string)
```


**Тип ответа:** text


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


📍 *Расположение:* `contrib/go-adk/pkg/a2a/hitl.go:62`



---


[function] name: GetKAgentMetadataKey file: contrib/go-adk/pkg/a2a/hitl.go:55 returns_error: нет description: GetKAgentMetadataKey returns the prefixed metadata key.


### GetKAgentMetadataKey (contrib/go-adk/pkg/a2a/hitl.go:55)


GetKAgentMetadataKey returns the prefixed metadata key.


```go
func GetKAgentMetadataKey((key string)) (key string)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/hitl.go:55`



---


[function] name: escapeMarkdownBackticks file: contrib/go-adk/pkg/a2a/hitl.go:109 returns_error: нет description: escapeMarkdownBackticks escapes backticks to prevent markdown rendering issues.


### escapeMarkdownBackticks (contrib/go-adk/pkg/a2a/hitl.go:109)


escapeMarkdownBackticks escapes backticks to prevent markdown rendering issues.


```go
func escapeMarkdownBackticks((text string)) (text string)
```


**Тип ответа:** text


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


📍 *Расположение:* `contrib/go-adk/pkg/a2a/hitl.go:109`



---


[function] name: formatToolApprovalTextParts file: contrib/go-adk/pkg/a2a/hitl.go:115 returns_error: нет description: formatToolApprovalTextParts formats tool approval requests as a single
human-readable TextPart in markdown.


### formatToolApprovalTextParts (contrib/go-adk/pkg/a2a/hitl.go:115)


formatToolApprovalTextParts formats tool approval requests as a single
human-readable TextPart in markdown.


```go
func formatToolApprovalTextParts((actionRequests []ToolApprovalRequest)) (actionRequests []ToolApprovalRequest)
```


**Тип ответа:** actionRequests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolApprovalRequest


```json
{
  "Name": "string",
  "Args": {},
  "ID": "string"
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/hitl.go`


📍 *Расположение:* `contrib/go-adk/pkg/a2a/hitl.go:115`



---


[function] name: init file: contrib/go-adk/pkg/a2a/hitl.go:16 returns_error: нет description: —


### init (contrib/go-adk/pkg/a2a/hitl.go:16)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/a2a/hitl.go:16`




## contrib/go-adk/pkg/a2a/server/health.go


📄 Исходный файл: `contrib/go-adk/pkg/a2a/server/health.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RegisterHealthEndpoints](#registerhealthendpoints-contribgo-adkpkga2aserverhealthgo9) `:9`


</details>


[function] name: RegisterHealthEndpoints file: contrib/go-adk/pkg/a2a/server/health.go:9 returns_error: нет description: RegisterHealthEndpoints registers health check endpoints on the given mux.
These endpoints are used by Kubernetes for re


### RegisterHealthEndpoints (contrib/go-adk/pkg/a2a/server/health.go:9)


RegisterHealthEndpoints registers health check endpoints on the given mux.
These endpoints are used by Kubernetes for readiness/liveness probes.


```go
func RegisterHealthEndpoints((mux *http.ServeMux)) (mux *http.ServeMux)
```


**Тип запроса:** http.ServeMux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.ServeMux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/a2a/server/health.go:9`




## contrib/go-adk/pkg/a2a/server/server.go


📄 Исходный файл: `contrib/go-adk/pkg/a2a/server/server.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewA2AServer](#newa2aserver-contribgo-adkpkga2aserverservergo33) `:33`

- 🔗 [Run](#run-contribgo-adkpkga2aserverservergo95) `:95`

- 🔗 [Start](#start-contribgo-adkpkga2aserverservergo58) `:58`

- 🔗 [WaitForShutdown](#waitforshutdown-contribgo-adkpkga2aserverservergo73) `:73`


</details>


[function] name: NewA2AServer file: contrib/go-adk/pkg/a2a/server/server.go:33 returns_error: да description: NewA2AServer creates a new A2A server using a2asrv.


### NewA2AServer (contrib/go-adk/pkg/a2a/server/server.go:33)


NewA2AServer creates a new A2A server using a2asrv.


```go
func NewA2AServer((*A2AServer, error)) (*A2AServer, error)
```


**Тип запроса:** A2AServer


```json
{
  "httpServer": null,
  "logger": {},
  "config": {},
  "listenErr": {}
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/server/server.go`


**Тип ответа:** A2AServer


```json
{
  "httpServer": null,
  "logger": {},
  "config": {},
  "listenErr": {}
}
```


*Определено в:* `contrib/go-adk/pkg/a2a/server/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*A2AServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/a2a/server/server.go:33`



---


[function] name: Run file: contrib/go-adk/pkg/a2a/server/server.go:95 returns_error: нет description: Run starts the server and waits for shutdown.


### Run (contrib/go-adk/pkg/a2a/server/server.go:95)


Run starts the server and waits for shutdown.


```go
func (s *A2AServer) Run(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/a2a/server/server.go:95`



---


[function] name: Start file: contrib/go-adk/pkg/a2a/server/server.go:58 returns_error: нет description: Start initializes and starts the HTTP server.


### Start (contrib/go-adk/pkg/a2a/server/server.go:58)


Start initializes and starts the HTTP server.


```go
func (s *A2AServer) Start(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/a2a/server/server.go:58`



---


[function] name: WaitForShutdown file: contrib/go-adk/pkg/a2a/server/server.go:73 returns_error: нет description: WaitForShutdown blocks until a shutdown signal is received or the listener
fails, then gracefully shuts down.


### WaitForShutdown (contrib/go-adk/pkg/a2a/server/server.go:73)


WaitForShutdown blocks until a shutdown signal is received or the listener
fails, then gracefully shuts down.


```go
func (s *A2AServer) WaitForShutdown(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/a2a/server/server.go:73`




## contrib/go-adk/pkg/agent/agent.go


📄 Исходный файл: `contrib/go-adk/pkg/agent/agent.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [CreateGoogleADKAgent](#creategoogleadkagent-contribgo-adkpkgagentagentgo23) `:23`

- 🔗 [createLLM](#createllm-contribgo-adkpkgagentagentgo80) `:80`

- 🔗 [extractHeaders](#extractheaders-contribgo-adkpkgagentagentgo183) `:183`

- 🔗 [makeAfterToolCallback](#makeaftertoolcallback-contribgo-adkpkgagentagentgo205) `:205`

- 🔗 [makeBeforeToolCallback](#makebeforetoolcallback-contribgo-adkpkgagentagentgo191) `:191`

- 🔗 [makeOnToolErrorCallback](#makeontoolerrorcallback-contribgo-adkpkgagentagentgo228) `:228`

- 🔗 [mapKeys](#mapkeys-contribgo-adkpkgagentagentgo242) `:242`

- 🔗 [truncateArgs](#truncateargs-contribgo-adkpkgagentagentgo254) `:254`


</details>


[function] name: CreateGoogleADKAgent file: contrib/go-adk/pkg/agent/agent.go:23 returns_error: да description: CreateGoogleADKAgent creates a Google ADK agent from AgentConfig.
Toolsets are passed in directly (created by mcp.Create


### CreateGoogleADKAgent (contrib/go-adk/pkg/agent/agent.go:23)


CreateGoogleADKAgent creates a Google ADK agent from AgentConfig.
Toolsets are passed in directly (created by mcp.CreateToolsets).
agentName is used as the ADK agent identity (appears in event Author field).


```go
func CreateGoogleADKAgent((agent.Agent, error)) (agent.Agent, error)
```


**Тип ответа:** agent.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `agent.Agent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:23`



---


[function] name: createLLM file: contrib/go-adk/pkg/agent/agent.go:80 returns_error: да description: createLLM creates an adkmodel.LLM from the model configuration.


### createLLM (contrib/go-adk/pkg/agent/agent.go:80)


createLLM creates an adkmodel.LLM from the model configuration.


```go
func createLLM((adkmodel.LLM, error)) (adkmodel.LLM, error)
```


**Тип ответа:** adkmodel.LLM


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `adkmodel.LLM`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:80`



---


[function] name: extractHeaders file: contrib/go-adk/pkg/agent/agent.go:183 returns_error: нет description: extractHeaders returns an empty map if nil, the original map otherwise.


### extractHeaders (contrib/go-adk/pkg/agent/agent.go:183)


extractHeaders returns an empty map if nil, the original map otherwise.


```go
func extractHeaders((headers map[string]string)) (headers map[string]string)
```


**Тип ответа:** headers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:183`



---


[function] name: makeAfterToolCallback file: contrib/go-adk/pkg/agent/agent.go:205 returns_error: нет description: makeAfterToolCallback returns an AfterToolCallback that logs tool completion.


### makeAfterToolCallback (contrib/go-adk/pkg/agent/agent.go:205)


makeAfterToolCallback returns an AfterToolCallback that logs tool completion.


```go
func makeAfterToolCallback((logger logr.Logger)) (logger logr.Logger)
```


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:205`



---


[function] name: makeBeforeToolCallback file: contrib/go-adk/pkg/agent/agent.go:191 returns_error: нет description: makeBeforeToolCallback returns a BeforeToolCallback that logs tool invocations.


### makeBeforeToolCallback (contrib/go-adk/pkg/agent/agent.go:191)


makeBeforeToolCallback returns a BeforeToolCallback that logs tool invocations.


```go
func makeBeforeToolCallback((logger logr.Logger)) (logger logr.Logger)
```


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:191`



---


[function] name: makeOnToolErrorCallback file: contrib/go-adk/pkg/agent/agent.go:228 returns_error: нет description: makeOnToolErrorCallback returns an OnToolErrorCallback that logs tool errors.


### makeOnToolErrorCallback (contrib/go-adk/pkg/agent/agent.go:228)


makeOnToolErrorCallback returns an OnToolErrorCallback that logs tool errors.


```go
func makeOnToolErrorCallback((logger logr.Logger)) (logger logr.Logger)
```


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:228`



---


[function] name: mapKeys file: contrib/go-adk/pkg/agent/agent.go:242 returns_error: нет description: mapKeys returns the top-level keys of a map for logging without exposing values.


### mapKeys (contrib/go-adk/pkg/agent/agent.go:242)


mapKeys returns the top-level keys of a map for logging without exposing values.


```go
func mapKeys((m map[string]any)) (m map[string]any)
```


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:242`



---


[function] name: truncateArgs file: contrib/go-adk/pkg/agent/agent.go:254 returns_error: нет description: truncateArgs returns a JSON string of args truncated for safe logging.


### truncateArgs (contrib/go-adk/pkg/agent/agent.go:254)


truncateArgs returns a JSON string of args truncated for safe logging.


```go
func truncateArgs((args map[string]any)) (args map[string]any)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/agent/agent.go:254`




## contrib/go-adk/pkg/app/app.go


📄 Исходный файл: `contrib/go-adk/pkg/app/app.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [Logger](#logger-contribgo-adkpkgappappgo160) `:160`

- 🔗 [New](#new-contribgo-adkpkgappappgo84) `:84`

- 🔗 [Run](#run-contribgo-adkpkgappappgo148) `:148`

- 🔗 [SessionService](#sessionservice-contribgo-adkpkgappappgo155) `:155`

- 🔗 [applyDefaults](#applydefaults-contribgo-adkpkgappappgo172) `:172`

- 🔗 [buildAppName](#buildappname-contribgo-adkpkgappappgo201) `:201`

- 🔗 [newDefaultLogger](#newdefaultlogger-contribgo-adkpkgappappgo227) `:227`

- 🔗 [newHTTPClient](#newhttpclient-contribgo-adkpkgappappgo219) `:219`

- 🔗 [stop](#stop-contribgo-adkpkgappappgo165) `:165`


</details>


[function] name: Logger file: contrib/go-adk/pkg/app/app.go:160 returns_error: нет description: Logger returns the logger used by this app.


### Logger (contrib/go-adk/pkg/app/app.go:160)


Logger returns the logger used by this app.


```go
func (a *KAgentApp) Logger(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:160`



---


[function] name: New file: contrib/go-adk/pkg/app/app.go:84 returns_error: да description: New creates a KAgentApp by wiring the provided executor with kagent
infrastructure. The executor must implement a2asrv.A


### New (contrib/go-adk/pkg/app/app.go:84)


New creates a KAgentApp by wiring the provided executor with kagent
infrastructure. The executor must implement a2asrv.AgentExecutor.


```go
func New((*KAgentApp, error)) (*KAgentApp, error)
```


**Тип запроса:** KAgentApp


```json
{
  "server": null,
  "tokenService": null,
  "sessionService": {},
  "logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/app/app.go`


**Тип ответа:** KAgentApp


```json
{
  "server": null,
  "tokenService": null,
  "sessionService": {},
  "logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/app/app.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*KAgentApp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:84`



---


[function] name: Run file: contrib/go-adk/pkg/app/app.go:148 returns_error: нет description: Run starts the A2A server and blocks until a shutdown signal is received.


### Run (contrib/go-adk/pkg/app/app.go:148)


Run starts the A2A server and blocks until a shutdown signal is received.


```go
func (a *KAgentApp) Run(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:148`



---


[function] name: SessionService file: contrib/go-adk/pkg/app/app.go:155 returns_error: нет description: SessionService returns the wired session service. BYO executors that need
session persistence can use this. Returns nil 


### SessionService (contrib/go-adk/pkg/app/app.go:155)


SessionService returns the wired session service. BYO executors that need
session persistence can use this. Returns nil when KAgentURL is not configured.


```go
func (a *KAgentApp) SessionService(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:155`



---


[function] name: applyDefaults file: contrib/go-adk/pkg/app/app.go:172 returns_error: нет description: applyDefaults fills in zero-value fields with sensible defaults.


### applyDefaults (contrib/go-adk/pkg/app/app.go:172)


applyDefaults fills in zero-value fields with sensible defaults.


```go
func applyDefaults((cfg AppConfig)) (cfg AppConfig)
```


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AppConfig


```json
{
  "AgentCard": {},
  "Host": "string",
  "Port": "string",
  "KAgentURL": "string",
  "AppName": "string",
  "ShutdownTimeout": {},
  "Logger": {},
  "HTTPClient": null,
  "HandlerOpts": [],
  "Agent": {}
}
```


*Определено в:* `contrib/go-adk/pkg/app/app.go`


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:172`



---


[function] name: buildAppName file: contrib/go-adk/pkg/app/app.go:201 returns_error: нет description: buildAppName derives the app name from environment variables or agent card,
following the same convention as the Python 


### buildAppName (contrib/go-adk/pkg/app/app.go:201)


buildAppName derives the app name from environment variables or agent card,
following the same convention as the Python KAgentConfig.


```go
func buildAppName((agentCard *a2atype.AgentCard)) (agentCard *a2atype.AgentCard)
```


**Тип запроса:** a2atype.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:201`



---


[function] name: newDefaultLogger file: contrib/go-adk/pkg/app/app.go:227 returns_error: нет description: newDefaultLogger creates a production zap logger wrapped as logr.Logger.


### newDefaultLogger (contrib/go-adk/pkg/app/app.go:227)


newDefaultLogger creates a production zap logger wrapped as logr.Logger.


```go
func newDefaultLogger(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:227`



---


[function] name: newHTTPClient file: contrib/go-adk/pkg/app/app.go:219 returns_error: нет description: newHTTPClient creates an HTTP client with optional token injection.


### newHTTPClient (contrib/go-adk/pkg/app/app.go:219)


newHTTPClient creates an HTTP client with optional token injection.


```go
func newHTTPClient((tokenService *auth.KAgentTokenService)) (tokenService *auth.KAgentTokenService)
```


**Тип запроса:** auth.KAgentTokenService


```json
{
  "token": "string",
  "mu": {},
  "appName": "string",
  "stopChan": {},
  "stopOnce": {}
}
```


*Определено в:* `contrib/go-adk/pkg/auth/token.go`


**Тип ответа:** tokenService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** auth.KAgentTokenService


```json
{
  "token": "string",
  "mu": {},
  "appName": "string",
  "stopChan": {},
  "stopOnce": {}
}
```


*Определено в:* `contrib/go-adk/pkg/auth/token.go`


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:219`



---


[function] name: stop file: contrib/go-adk/pkg/app/app.go:165 returns_error: нет description: stop cleans up resources.


### stop (contrib/go-adk/pkg/app/app.go:165)


stop cleans up resources.


```go
func (a *KAgentApp) stop(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/app/app.go:165`




## contrib/go-adk/pkg/auth/token.go


📄 Исходный файл: `contrib/go-adk/pkg/auth/token.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [AddHeaders](#addheaders-contribgo-adkpkgauthtokengo59) `:59`

- 🔗 [GetToken](#gettoken-contribgo-adkpkgauthtokengo52) `:52`

- 🔗 [NewHTTPClientWithToken](#newhttpclientwithtoken-contribgo-adkpkgauthtokengo118) `:118`

- 🔗 [NewKAgentTokenService](#newkagenttokenservice-contribgo-adkpkgauthtokengo23) `:23`

- 🔗 [RoundTrip](#roundtrip-contribgo-adkpkgauthtokengo106) `:106`

- 🔗 [Start](#start-contribgo-adkpkgauthtokengo31) `:31`

- 🔗 [Stop](#stop-contribgo-adkpkgauthtokengo47) `:47`

- 🔗 [readToken](#readtoken-contribgo-adkpkgauthtokengo67) `:67`

- 🔗 [refreshTokenLoop](#refreshtokenloop-contribgo-adkpkgauthtokengo76) `:76`


</details>


[function] name: AddHeaders file: contrib/go-adk/pkg/auth/token.go:59 returns_error: нет description: AddHeaders adds authorization and agent headers to an HTTP request


### AddHeaders (contrib/go-adk/pkg/auth/token.go:59)


AddHeaders adds authorization and agent headers to an HTTP request


```go
func (s *KAgentTokenService) AddHeaders((req *http.Request)) (req *http.Request)
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


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:59`



---


[function] name: GetToken file: contrib/go-adk/pkg/auth/token.go:52 returns_error: нет description: GetToken returns the current token


### GetToken (contrib/go-adk/pkg/auth/token.go:52)


GetToken returns the current token


```go
func (s *KAgentTokenService) GetToken(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:52`



---


[function] name: NewHTTPClientWithToken file: contrib/go-adk/pkg/auth/token.go:118 returns_error: нет description: NewHTTPClientWithToken creates an HTTP client with token service integration


### NewHTTPClientWithToken (contrib/go-adk/pkg/auth/token.go:118)


NewHTTPClientWithToken creates an HTTP client with token service integration


```go
func NewHTTPClientWithToken((tokenService *KAgentTokenService)) (tokenService *KAgentTokenService)
```


**Тип запроса:** KAgentTokenService


```json
{
  "token": "string",
  "mu": {},
  "appName": "string",
  "stopChan": {},
  "stopOnce": {}
}
```


*Определено в:* `contrib/go-adk/pkg/auth/token.go`


**Тип ответа:** tokenService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** KAgentTokenService


```json
{
  "token": "string",
  "mu": {},
  "appName": "string",
  "stopChan": {},
  "stopOnce": {}
}
```


*Определено в:* `contrib/go-adk/pkg/auth/token.go`


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:118`



---


[function] name: NewKAgentTokenService file: contrib/go-adk/pkg/auth/token.go:23 returns_error: нет description: NewKAgentTokenService creates a new KAgentTokenService


### NewKAgentTokenService (contrib/go-adk/pkg/auth/token.go:23)


NewKAgentTokenService creates a new KAgentTokenService


```go
func NewKAgentTokenService((appName string)) (appName string)
```


**Тип ответа:** appName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:23`



---


[function] name: RoundTrip file: contrib/go-adk/pkg/auth/token.go:106 returns_error: да description: —


### RoundTrip (contrib/go-adk/pkg/auth/token.go:106)


RoundTrip is a method that performs operations based on the provided parameters and may return an error.


```go
func (rt *TokenRoundTripper) RoundTrip((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:106`



---


[function] name: Start file: contrib/go-adk/pkg/auth/token.go:31 returns_error: нет description: Start starts the token update loop


### Start (contrib/go-adk/pkg/auth/token.go:31)


Start starts the token update loop


```go
func (s *KAgentTokenService) Start((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:31`



---


[function] name: Stop file: contrib/go-adk/pkg/auth/token.go:47 returns_error: нет description: Stop stops the token refresh loop. Safe to call multiple times.


### Stop (contrib/go-adk/pkg/auth/token.go:47)


Stop stops the token refresh loop. Safe to call multiple times.


```go
func (s *KAgentTokenService) Stop(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:47`



---


[function] name: readToken file: contrib/go-adk/pkg/auth/token.go:67 returns_error: да description: readToken reads the token from the file


### readToken (contrib/go-adk/pkg/auth/token.go:67)


readToken reads the token from the file


```go
func (s *KAgentTokenService) readToken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:67`



---


[function] name: refreshTokenLoop file: contrib/go-adk/pkg/auth/token.go:76 returns_error: нет description: refreshTokenLoop periodically refreshes the token


### refreshTokenLoop (contrib/go-adk/pkg/auth/token.go:76)


refreshTokenLoop periodically refreshes the token


```go
func (s *KAgentTokenService) refreshTokenLoop((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `contrib/go-adk/pkg/auth/token.go:76`




## contrib/go-adk/pkg/config/config_loader.go


📄 Исходный файл: `contrib/go-adk/pkg/config/config_loader.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [LoadAgentCard](#loadagentcard-contribgo-adkpkgconfigconfig_loadergo28) `:28`

- 🔗 [LoadAgentConfig](#loadagentconfig-contribgo-adkpkgconfigconfig_loadergo13) `:13`

- 🔗 [LoadAgentConfigs](#loadagentconfigs-contribgo-adkpkgconfigconfig_loadergo43) `:43`


</details>


[function] name: LoadAgentCard file: contrib/go-adk/pkg/config/config_loader.go:28 returns_error: да description: LoadAgentCard loads agent card from agent-card.json file


### LoadAgentCard (contrib/go-adk/pkg/config/config_loader.go:28)


LoadAgentCard loads agent card from agent-card.json file


```go
func LoadAgentCard((*a2a.AgentCard, error)) (*a2a.AgentCard, error)
```


**Тип запроса:** a2a.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2a.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*a2a.AgentCard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/config/config_loader.go:28`



---


[function] name: LoadAgentConfig file: contrib/go-adk/pkg/config/config_loader.go:13 returns_error: да description: LoadAgentConfig loads agent configuration from config.json file


### LoadAgentConfig (contrib/go-adk/pkg/config/config_loader.go:13)


LoadAgentConfig loads agent configuration from config.json file


```go
func LoadAgentConfig((*AgentConfig, error)) (*AgentConfig, error)
```


**Тип запроса:** AgentConfig


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


**Тип ответа:** AgentConfig


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgentConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/config/config_loader.go:13`



---


[function] name: LoadAgentConfigs file: contrib/go-adk/pkg/config/config_loader.go:43 returns_error: да description: LoadAgentConfigs loads both config and agent card from the config directory


### LoadAgentConfigs (contrib/go-adk/pkg/config/config_loader.go:43)


LoadAgentConfigs loads both config and agent card from the config directory


```go
func LoadAgentConfigs((*AgentConfig, *a2a.AgentCard, error)) (*AgentConfig, *a2a.AgentCard, error)
```


**Тип запроса:** AgentConfig


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


**Тип запроса:** a2a.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentConfig


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


**Тип ответа:** a2a.AgentCard


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgentConfig`, `*a2a.AgentCard`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/config/config_loader.go:43`




## contrib/go-adk/pkg/config/config_usage.go


📄 Исходный файл: `contrib/go-adk/pkg/config/config_usage.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetAgentConfigSummary](#getagentconfigsummary-contribgo-adkpkgconfigconfig_usagego103) `:103`

- 🔗 [ValidateAgentConfigUsage](#validateagentconfigusage-contribgo-adkpkgconfigconfig_usagego43) `:43`

- 🔗 [ValidateAgentConfigUsageWithLogger](#validateagentconfigusagewithlogger-contribgo-adkpkgconfigconfig_usagego51) `:51`

- 🔗 [getModelName](#getmodelname-contribgo-adkpkgconfigconfig_usagego125) `:125`


</details>


[function] name: GetAgentConfigSummary file: contrib/go-adk/pkg/config/config_usage.go:103 returns_error: нет description: GetAgentConfigSummary returns a summary of the agent configuration


### GetAgentConfigSummary (contrib/go-adk/pkg/config/config_usage.go:103)


GetAgentConfigSummary returns a summary of the agent configuration


```go
func GetAgentConfigSummary((config *AgentConfig)) (config *AgentConfig)
```


**Тип запроса:** AgentConfig


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


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentConfig


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


📍 *Расположение:* `contrib/go-adk/pkg/config/config_usage.go:103`



---


[function] name: ValidateAgentConfigUsage file: contrib/go-adk/pkg/config/config_usage.go:43 returns_error: нет description: ValidateAgentConfigUsage validates that all AgentConfig fields are properly used
This is a helper function to ensure we'


### ValidateAgentConfigUsage (contrib/go-adk/pkg/config/config_usage.go:43)


ValidateAgentConfigUsage validates that all AgentConfig fields are properly used
This is a helper function to ensure we're using all fields correctly


```go
func ValidateAgentConfigUsage((config *AgentConfig)) (config *AgentConfig)
```


**Тип запроса:** AgentConfig


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


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentConfig


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


📍 *Расположение:* `contrib/go-adk/pkg/config/config_usage.go:43`



---


[function] name: ValidateAgentConfigUsageWithLogger file: contrib/go-adk/pkg/config/config_usage.go:51 returns_error: нет description: ValidateAgentConfigUsageWithLogger validates that all AgentConfig fields are properly used
This is a helper function to 


### ValidateAgentConfigUsageWithLogger (contrib/go-adk/pkg/config/config_usage.go:51)


ValidateAgentConfigUsageWithLogger validates that all AgentConfig fields are properly used
This is a helper function to ensure we're using all fields correctly
If logger is the zero value (no sink), validation will proceed without logging


```go
func ValidateAgentConfigUsageWithLogger((config *AgentConfig, logger logr.Logger)) (config *AgentConfig, logger logr.Logger)
```


**Тип запроса:** AgentConfig


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


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentConfig


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


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logr.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/config/config_usage.go:51`



---


[function] name: getModelName file: contrib/go-adk/pkg/config/config_usage.go:125 returns_error: нет description: —


### getModelName (contrib/go-adk/pkg/config/config_usage.go:125)


getModelName is a function that performs operations based on the provided parameters and returns (m Model).


```go
func getModelName((m Model)) (m Model)
```


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `contrib/go-adk/pkg/config/config_usage.go:125`




## contrib/go-adk/pkg/config/types.go


📄 Исходный файл: `contrib/go-adk/pkg/config/types.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [GetExecuteCode](#getexecutecode-contribgo-adkpkgconfigtypesgo165) `:165`

- 🔗 [GetStream](#getstream-contribgo-adkpkgconfigtypesgo157) `:157`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo45) `:45`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo51) `:51`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo63) `:63`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo69) `:69`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo75) `:75`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo81) `:81`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo87) `:87`

- 🔗 [GetType](#gettype-contribgo-adkpkgconfigtypesgo93) `:93`

- 🔗 [UnmarshalJSON](#unmarshaljson-contribgo-adkpkgconfigtypesgo172) `:172`


</details>


[function] name: GetExecuteCode file: contrib/go-adk/pkg/config/types.go:165 returns_error: нет description: GetExecuteCode returns the execute_code value or default if not set


### GetExecuteCode (contrib/go-adk/pkg/config/types.go:165)


GetExecuteCode returns the execute_code value or default if not set


```go
func (a *AgentConfig) GetExecuteCode(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:165`



---


[function] name: GetStream file: contrib/go-adk/pkg/config/types.go:157 returns_error: нет description: GetStream returns the stream value or default if not set


### GetStream (contrib/go-adk/pkg/config/types.go:157)


GetStream returns the stream value or default if not set


```go
func (a *AgentConfig) GetStream(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:157`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:45 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:45)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (o *OpenAI) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:45`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:51 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:51)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (a *AzureOpenAI) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:51`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:63 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:63)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (a *Anthropic) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:63`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:69 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:69)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (g *GeminiVertexAI) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:69`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:75 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:75)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (g *GeminiAnthropic) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:75`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:81 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:81)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (o *Ollama) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:81`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:87 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:87)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (g *Gemini) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:87`



---


[function] name: GetType file: contrib/go-adk/pkg/config/types.go:93 returns_error: нет description: —


### GetType (contrib/go-adk/pkg/config/types.go:93)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (g *GenericModel) GetType(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:93`



---


[function] name: UnmarshalJSON file: contrib/go-adk/pkg/config/types.go:172 returns_error: нет description: —


### UnmarshalJSON (contrib/go-adk/pkg/config/types.go:172)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (data []byte).


```go
func (a *AgentConfig) UnmarshalJSON((data []byte)) (data []byte)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/config/types.go:172`




## contrib/go-adk/pkg/mcp/registry.go


📄 Исходный файл: `contrib/go-adk/pkg/mcp/registry.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [CreateToolsets](#createtoolsets-contribgo-adkpkgmcpregistrygo40) `:40`

- 🔗 [RoundTrip](#roundtrip-contribgo-adkpkgmcpregistrygo202) `:202`

- 🔗 [addToolset](#addtoolset-contribgo-adkpkgmcpregistrygo86) `:86`

- 🔗 [createTransport](#createtransport-contribgo-adkpkgmcpregistrygo113) `:113`

- 🔗 [initializeToolSet](#initializetoolset-contribgo-adkpkgmcpregistrygo212) `:212`


</details>


[function] name: CreateToolsets file: contrib/go-adk/pkg/mcp/registry.go:40 returns_error: нет description: CreateToolsets creates toolsets from all configured HTTP and SSE MCP servers,
returning the accumulated toolsets. Errors


### CreateToolsets (contrib/go-adk/pkg/mcp/registry.go:40)


CreateToolsets creates toolsets from all configured HTTP and SSE MCP servers,
returning the accumulated toolsets. Errors on individual servers are logged
and skipped.


```go
func CreateToolsets((ctx context.Context, httpTools []config.HttpMcpServerConfig, sseTools []config.SseMcpServerConfig)) (ctx context.Context, httpTools []config.HttpMcpServerConfig, sseTools []config.SseMcpServerConfig)
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


**Тип ответа:** httpTools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.HttpMcpServerConfig


```json
{
  "Params": {},
  "Tools": []
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** sseTools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.SseMcpServerConfig


```json
{
  "Params": {},
  "Tools": []
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


📍 *Расположение:* `contrib/go-adk/pkg/mcp/registry.go:40`



---


[function] name: RoundTrip file: contrib/go-adk/pkg/mcp/registry.go:202 returns_error: да description: —


### RoundTrip (contrib/go-adk/pkg/mcp/registry.go:202)


RoundTrip is a method that performs operations based on the provided parameters and may return an error.


```go
func (rt *headerRoundTripper) RoundTrip((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `contrib/go-adk/pkg/mcp/registry.go:202`



---


[function] name: addToolset file: contrib/go-adk/pkg/mcp/registry.go:86 returns_error: да description: addToolset logs, initializes, and returns a single MCP toolset.


### addToolset (contrib/go-adk/pkg/mcp/registry.go:86)


addToolset logs, initializes, and returns a single MCP toolset.


```go
func addToolset((tool.Toolset, error)) (tool.Toolset, error)
```


**Тип ответа:** tool.Toolset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `tool.Toolset`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/mcp/registry.go:86`



---


[function] name: createTransport file: contrib/go-adk/pkg/mcp/registry.go:113 returns_error: да description: createTransport creates an MCP transport based on server type and configuration.
Uses the official MCP SDK (github.com/m


### createTransport (contrib/go-adk/pkg/mcp/registry.go:113)


createTransport creates an MCP transport based on server type and configuration.
Uses the official MCP SDK (github.com/modelcontextprotocol/go-sdk/mcp).


```go
func createTransport((mcpsdk.Transport, error)) (mcpsdk.Transport, error)
```


**Тип ответа:** mcpsdk.Transport


```json
{
  "base": {},
  "headers": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `mcpsdk.Transport`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/mcp/registry.go:113`



---


[function] name: initializeToolSet file: contrib/go-adk/pkg/mcp/registry.go:212 returns_error: да description: initializeToolSet fetches tools from an MCP server using Google ADK's mcptoolset.
Returns the created toolset on success


### initializeToolSet (contrib/go-adk/pkg/mcp/registry.go:212)


initializeToolSet fetches tools from an MCP server using Google ADK's mcptoolset.
Returns the created toolset on success.


```go
func initializeToolSet((tool.Toolset, error)) (tool.Toolset, error)
```


**Тип ответа:** tool.Toolset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `tool.Toolset`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/mcp/registry.go:212`




## contrib/go-adk/pkg/models/anthropic.go


📄 Исходный файл: `contrib/go-adk/pkg/models/anthropic.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [NewAnthropicModelWithLogger](#newanthropicmodelwithlogger-contribgo-adkpkgmodelsanthropicgo34) `:34`

- 🔗 [newAnthropicModelFromConfig](#newanthropicmodelfromconfig-contribgo-adkpkgmodelsanthropicgo42) `:42`


</details>


[function] name: NewAnthropicModelWithLogger file: contrib/go-adk/pkg/models/anthropic.go:34 returns_error: да description: NewAnthropicModelWithLogger creates a new Anthropic model instance with a logger


### NewAnthropicModelWithLogger (contrib/go-adk/pkg/models/anthropic.go:34)


NewAnthropicModelWithLogger creates a new Anthropic model instance with a logger


```go
func NewAnthropicModelWithLogger((*AnthropicModel, error)) (*AnthropicModel, error)
```


**Тип запроса:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Тип ответа:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AnthropicModel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic.go:34`



---


[function] name: newAnthropicModelFromConfig file: contrib/go-adk/pkg/models/anthropic.go:42 returns_error: да description: —


### newAnthropicModelFromConfig (contrib/go-adk/pkg/models/anthropic.go:42)


newAnthropicModelFromConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func newAnthropicModelFromConfig((*AnthropicModel, error)) (*AnthropicModel, error)
```


**Тип запроса:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Тип ответа:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AnthropicModel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic.go:42`




## contrib/go-adk/pkg/models/anthropic_adk.go


📄 Исходный файл: `contrib/go-adk/pkg/models/anthropic_adk.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [GenerateContent](#generatecontent-contribgo-adkpkgmodelsanthropic_adkgo40) `:40`

- 🔗 [Name](#name-contribgo-adkpkgmodelsanthropic_adkgo35) `:35`

- 🔗 [anthropicStopReasonToGenai](#anthropicstopreasontogenai-contribgo-adkpkgmodelsanthropic_adkgo21) `:21`

- 🔗 [applyAnthropicConfig](#applyanthropicconfig-contribgo-adkpkgmodelsanthropic_adkgo88) `:88`

- 🔗 [genaiContentsToAnthropicMessages](#genaicontentstoanthropicmessages-contribgo-adkpkgmodelsanthropic_adkgo103) `:103`

- 🔗 [genaiToolsToAnthropicTools](#genaitoolstoanthropictools-contribgo-adkpkgmodelsanthropic_adkgo222) `:222`

- 🔗 [runAnthropicNonStreaming](#runanthropicnonstreaming-contribgo-adkpkgmodelsanthropic_adkgo364) `:364`

- 🔗 [runAnthropicStreaming](#runanthropicstreaming-contribgo-adkpkgmodelsanthropic_adkgo264) `:264`


</details>


[function] name: GenerateContent file: contrib/go-adk/pkg/models/anthropic_adk.go:40 returns_error: нет description: GenerateContent implements model.LLM. Uses only ADK/genai types.


### GenerateContent (contrib/go-adk/pkg/models/anthropic_adk.go:40)


GenerateContent implements model.LLM. Uses only ADK/genai types.


```go
func (m *AnthropicModel) GenerateContent((ctx context.Context, req *model.LLMRequest, stream bool)) (ctx context.Context, req *model.LLMRequest, stream bool)
```


**Тип запроса:** model.LLMRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** model.LLMRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stream


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:40`



---


[function] name: Name file: contrib/go-adk/pkg/models/anthropic_adk.go:35 returns_error: нет description: Name implements model.LLM.


### Name (contrib/go-adk/pkg/models/anthropic_adk.go:35)


Name implements model.LLM.


```go
func (m *AnthropicModel) Name(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:35`



---


[function] name: anthropicStopReasonToGenai file: contrib/go-adk/pkg/models/anthropic_adk.go:21 returns_error: нет description: anthropicStopReasonToGenai maps Anthropic stop_reason to genai.FinishReason.


### anthropicStopReasonToGenai (contrib/go-adk/pkg/models/anthropic_adk.go:21)


anthropicStopReasonToGenai maps Anthropic stop_reason to genai.FinishReason.


```go
func anthropicStopReasonToGenai((reason anthropic.StopReason)) (reason anthropic.StopReason)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** anthropic.StopReason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:21`



---


[function] name: applyAnthropicConfig file: contrib/go-adk/pkg/models/anthropic_adk.go:88 returns_error: нет description: —


### applyAnthropicConfig (contrib/go-adk/pkg/models/anthropic_adk.go:88)


applyAnthropicConfig is a function that performs operations based on the provided parameters and returns (params *anthropic.MessageNewParams, cfg *AnthropicConfig).


```go
func applyAnthropicConfig((params *anthropic.MessageNewParams, cfg *AnthropicConfig)) (params *anthropic.MessageNewParams, cfg *AnthropicConfig)
```


**Тип запроса:** anthropic.MessageNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** AnthropicConfig


```json
{
  "Model": "string",
  "BaseUrl": "string",
  "Headers": {},
  "MaxTokens": 0,
  "Temperature": 0.0,
  "TopP": 0.0,
  "TopK": 0,
  "Timeout": 0
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** anthropic.MessageNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AnthropicConfig


```json
{
  "Model": "string",
  "BaseUrl": "string",
  "Headers": {},
  "MaxTokens": 0,
  "Temperature": 0.0,
  "TopP": 0.0,
  "TopK": 0,
  "Timeout": 0
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:88`



---


[function] name: genaiContentsToAnthropicMessages file: contrib/go-adk/pkg/models/anthropic_adk.go:103 returns_error: нет description: —


### genaiContentsToAnthropicMessages (contrib/go-adk/pkg/models/anthropic_adk.go:103)


genaiContentsToAnthropicMessages is a function that performs operations based on the provided parameters and returns ([]anthropic.MessageParam, string).


```go
func genaiContentsToAnthropicMessages(([]anthropic.MessageParam, string)) ([]anthropic.MessageParam, string)
```


**Тип ответа:** anthropic.MessageParam


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:103`



---


[function] name: genaiToolsToAnthropicTools file: contrib/go-adk/pkg/models/anthropic_adk.go:222 returns_error: нет description: —


### genaiToolsToAnthropicTools (contrib/go-adk/pkg/models/anthropic_adk.go:222)


genaiToolsToAnthropicTools is a function that performs operations based on the provided parameters and returns (tools []*genai.Tool).


```go
func genaiToolsToAnthropicTools((tools []*genai.Tool)) (tools []*genai.Tool)
```


**Тип запроса:** genai.Tool


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


**Тип ответа:** tools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genai.Tool


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


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:222`



---


[function] name: runAnthropicNonStreaming file: contrib/go-adk/pkg/models/anthropic_adk.go:364 returns_error: да description: —


### runAnthropicNonStreaming (contrib/go-adk/pkg/models/anthropic_adk.go:364)


runAnthropicNonStreaming is a function that performs operations based on the provided parameters and may return an error.


```go
func runAnthropicNonStreaming((ctx context.Context, m *AnthropicModel, params anthropic.MessageNewParams, yield func(*model.LLMResponse, error) bool)) (ctx context.Context, m *AnthropicModel, params anthropic.MessageNewParams, yield func(*model.LLMResponse, error) bool)
```


**Тип запроса:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Тип запроса:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** anthropic.MessageNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** yield


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `m *AnthropicModel`, `params anthropic.MessageNewParams`, `yield func(*model.LLMResponse`, `error) bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:364`



---


[function] name: runAnthropicStreaming file: contrib/go-adk/pkg/models/anthropic_adk.go:264 returns_error: да description: —


### runAnthropicStreaming (contrib/go-adk/pkg/models/anthropic_adk.go:264)


runAnthropicStreaming is a function that performs operations based on the provided parameters and may return an error.


```go
func runAnthropicStreaming((ctx context.Context, m *AnthropicModel, params anthropic.MessageNewParams, yield func(*model.LLMResponse, error) bool)) (ctx context.Context, m *AnthropicModel, params anthropic.MessageNewParams, yield func(*model.LLMResponse, error) bool)
```


**Тип запроса:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Тип запроса:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** AnthropicModel


```json
{
  "Config": null,
  "Client": {},
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/anthropic.go`


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** anthropic.MessageNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** yield


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `m *AnthropicModel`, `params anthropic.MessageNewParams`, `yield func(*model.LLMResponse`, `error) bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/anthropic_adk.go:264`




## contrib/go-adk/pkg/models/openai.go


📄 Исходный файл: `contrib/go-adk/pkg/models/openai.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [NewAzureOpenAIModelWithLogger](#newazureopenaimodelwithlogger-contribgo-adkpkgmodelsopenaigo116) `:116`

- 🔗 [NewOpenAICompatibleModelWithLogger](#newopenaicompatiblemodelwithlogger-contribgo-adkpkgmodelsopenaigo62) `:62`

- 🔗 [NewOpenAIModelWithLogger](#newopenaimodelwithlogger-contribgo-adkpkgmodelsopenaigo51) `:51`

- 🔗 [RoundTrip](#roundtrip-contribgo-adkpkgmodelsopenaigo211) `:211`

- 🔗 [azurePathRewriteMiddleware](#azurepathrewritemiddleware-contribgo-adkpkgmodelsopenaigo166) `:166`

- 🔗 [newOpenAIModelFromConfig](#newopenaimodelfromconfig-contribgo-adkpkgmodelsopenaigo79) `:79`


</details>


[function] name: NewAzureOpenAIModelWithLogger file: contrib/go-adk/pkg/models/openai.go:116 returns_error: да description: NewAzureOpenAIModelWithLogger creates a new Azure OpenAI model instance with a logger.
Uses Azure-style base URL, Api-Ke


### NewAzureOpenAIModelWithLogger (contrib/go-adk/pkg/models/openai.go:116)


NewAzureOpenAIModelWithLogger creates a new Azure OpenAI model instance with a logger.
Uses Azure-style base URL, Api-Key header, and path rewriting so we do not depend on the azure package.


```go
func NewAzureOpenAIModelWithLogger((*OpenAIModel, error)) (*OpenAIModel, error)
```


**Тип запроса:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*OpenAIModel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/openai.go:116`



---


[function] name: NewOpenAICompatibleModelWithLogger file: contrib/go-adk/pkg/models/openai.go:62 returns_error: да description: NewOpenAICompatibleModelWithLogger creates an OpenAI-compatible model (e.g. LiteLLM, Ollama).
baseURL is the API base (e


### NewOpenAICompatibleModelWithLogger (contrib/go-adk/pkg/models/openai.go:62)


NewOpenAICompatibleModelWithLogger creates an OpenAI-compatible model (e.g. LiteLLM, Ollama).
baseURL is the API base (e.g. http://localhost:11434/v1 for Ollama). apiKey is optional; if empty,
OPENAI_API_KEY is used, then a placeholder for endpoints that do not require a key.


```go
func NewOpenAICompatibleModelWithLogger((*OpenAIModel, error)) (*OpenAIModel, error)
```


**Тип запроса:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*OpenAIModel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/openai.go:62`



---


[function] name: NewOpenAIModelWithLogger file: contrib/go-adk/pkg/models/openai.go:51 returns_error: да description: NewOpenAIModelWithLogger creates a new OpenAI model instance with a logger


### NewOpenAIModelWithLogger (contrib/go-adk/pkg/models/openai.go:51)


NewOpenAIModelWithLogger creates a new OpenAI model instance with a logger


```go
func NewOpenAIModelWithLogger((*OpenAIModel, error)) (*OpenAIModel, error)
```


**Тип запроса:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*OpenAIModel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/openai.go:51`



---


[function] name: RoundTrip file: contrib/go-adk/pkg/models/openai.go:211 returns_error: да description: —


### RoundTrip (contrib/go-adk/pkg/models/openai.go:211)


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


📍 *Расположение:* `contrib/go-adk/pkg/models/openai.go:211`



---


[function] name: azurePathRewriteMiddleware file: contrib/go-adk/pkg/models/openai.go:166 returns_error: нет description: azurePathRewriteMiddleware rewrites .../chat/completions to .../openai/deployments/{model}/chat/completions
by reading t


### azurePathRewriteMiddleware (contrib/go-adk/pkg/models/openai.go:166)


azurePathRewriteMiddleware rewrites .../chat/completions to .../openai/deployments/{model}/chat/completions
by reading the request body for the model field (Azure deployment name).
Preserves the path prefix (e.g. /api/v1/proxy/) so proxies with a base path still work.


```go
func azurePathRewriteMiddleware(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/models/openai.go:166`



---


[function] name: newOpenAIModelFromConfig file: contrib/go-adk/pkg/models/openai.go:79 returns_error: да description: TODO: consider support for Azure OpenAI, when used from NewOpenAICompatibleModelWithLogger,
Anthropic and Gemini might u


### newOpenAIModelFromConfig (contrib/go-adk/pkg/models/openai.go:79)


TODO: consider support for Azure OpenAI, when used from NewOpenAICompatibleModelWithLogger,
Anthropic and Gemini might use Azure OpenAI, so we need to support it.


```go
func newOpenAIModelFromConfig((*OpenAIModel, error)) (*OpenAIModel, error)
```


**Тип запроса:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*OpenAIModel`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/openai.go:79`




## contrib/go-adk/pkg/models/openai_adk.go


📄 Исходный файл: `contrib/go-adk/pkg/models/openai_adk.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [GenerateContent](#generatecontent-contribgo-adkpkgmodelsopenai_adkgo49) `:49`

- 🔗 [Name](#name-contribgo-adkpkgmodelsopenai_adkgo44) `:44`

- 🔗 [applyOpenAIConfig](#applyopenaiconfig-contribgo-adkpkgmodelsopenai_adkgo86) `:86`

- 🔗 [functionResponseContentString](#functionresponsecontentstring-contribgo-adkpkgmodelsopenai_adkgo211) `:211`

- 🔗 [genaiContentsToOpenAIMessages](#genaicontentstoopenaimessages-contribgo-adkpkgmodelsopenai_adkgo113) `:113`

- 🔗 [genaiToolsToOpenAITools](#genaitoolstoopenaitools-contribgo-adkpkgmodelsopenai_adkgo234) `:234`

- 🔗 [openAIFinishReasonToGenai](#openaifinishreasontogenai-contribgo-adkpkgmodelsopenai_adkgo32) `:32`

- 🔗 [runNonStreaming](#runnonstreaming-contribgo-adkpkgmodelsopenai_adkgo368) `:368`

- 🔗 [runStreaming](#runstreaming-contribgo-adkpkgmodelsopenai_adkgo263) `:263`


</details>


[function] name: GenerateContent file: contrib/go-adk/pkg/models/openai_adk.go:49 returns_error: нет description: GenerateContent implements model.LLM. Uses only ADK/genai types.


### GenerateContent (contrib/go-adk/pkg/models/openai_adk.go:49)


GenerateContent implements model.LLM. Uses only ADK/genai types.


```go
func (m *OpenAIModel) GenerateContent((ctx context.Context, req *model.LLMRequest, stream bool)) (ctx context.Context, req *model.LLMRequest, stream bool)
```


**Тип запроса:** model.LLMRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** model.LLMRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stream


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:49`



---


[function] name: Name file: contrib/go-adk/pkg/models/openai_adk.go:44 returns_error: нет description: Name implements model.LLM.


### Name (contrib/go-adk/pkg/models/openai_adk.go:44)


Name implements model.LLM.


```go
func (m *OpenAIModel) Name(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:44`



---


[function] name: applyOpenAIConfig file: contrib/go-adk/pkg/models/openai_adk.go:86 returns_error: нет description: —


### applyOpenAIConfig (contrib/go-adk/pkg/models/openai_adk.go:86)


applyOpenAIConfig is a function that performs operations based on the provided parameters and returns (params *openai.ChatCompletionNewParams, cfg *OpenAIConfig).


```go
func applyOpenAIConfig((params *openai.ChatCompletionNewParams, cfg *OpenAIConfig)) (params *openai.ChatCompletionNewParams, cfg *OpenAIConfig)
```


**Тип запроса:** openai.ChatCompletionNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** OpenAIConfig


```json
{
  "Model": "string",
  "BaseUrl": "string",
  "Headers": {},
  "FrequencyPenalty": 0.0,
  "MaxTokens": 0,
  "N": 0,
  "PresencePenalty": 0.0,
  "ReasoningEffort": "string",
  "Seed": 0,
  "Temperature": 0.0,
  "Timeout": 0,
  "TopP": 0.0
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** openai.ChatCompletionNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** OpenAIConfig


```json
{
  "Model": "string",
  "BaseUrl": "string",
  "Headers": {},
  "FrequencyPenalty": 0.0,
  "MaxTokens": 0,
  "N": 0,
  "PresencePenalty": 0.0,
  "ReasoningEffort": "string",
  "Seed": 0,
  "Temperature": 0.0,
  "Timeout": 0,
  "TopP": 0.0
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:86`



---


[function] name: functionResponseContentString file: contrib/go-adk/pkg/models/openai_adk.go:211 returns_error: нет description: —


### functionResponseContentString (contrib/go-adk/pkg/models/openai_adk.go:211)


functionResponseContentString is a function that performs operations based on the provided parameters and returns (resp any).


```go
func functionResponseContentString((resp any)) (resp any)
```


**Тип ответа:** resp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:211`



---


[function] name: genaiContentsToOpenAIMessages file: contrib/go-adk/pkg/models/openai_adk.go:113 returns_error: нет description: —


### genaiContentsToOpenAIMessages (contrib/go-adk/pkg/models/openai_adk.go:113)


genaiContentsToOpenAIMessages is a function that performs operations based on the provided parameters and returns ([]openai.ChatCompletionMessageParamUnion, string).


```go
func genaiContentsToOpenAIMessages(([]openai.ChatCompletionMessageParamUnion, string)) ([]openai.ChatCompletionMessageParamUnion, string)
```


**Тип ответа:** openai.ChatCompletionMessageParamUnion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:113`



---


[function] name: genaiToolsToOpenAITools file: contrib/go-adk/pkg/models/openai_adk.go:234 returns_error: нет description: —


### genaiToolsToOpenAITools (contrib/go-adk/pkg/models/openai_adk.go:234)


genaiToolsToOpenAITools is a function that performs operations based on the provided parameters and returns (tools []*genai.Tool).


```go
func genaiToolsToOpenAITools((tools []*genai.Tool)) (tools []*genai.Tool)
```


**Тип запроса:** genai.Tool


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


**Тип ответа:** tools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genai.Tool


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


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:234`



---


[function] name: openAIFinishReasonToGenai file: contrib/go-adk/pkg/models/openai_adk.go:32 returns_error: нет description: openAIFinishReasonToGenai maps OpenAI finish_reason to genai.FinishReason.


### openAIFinishReasonToGenai (contrib/go-adk/pkg/models/openai_adk.go:32)


openAIFinishReasonToGenai maps OpenAI finish_reason to genai.FinishReason.


```go
func openAIFinishReasonToGenai((reason string)) (reason string)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:32`



---


[function] name: runNonStreaming file: contrib/go-adk/pkg/models/openai_adk.go:368 returns_error: да description: —


### runNonStreaming (contrib/go-adk/pkg/models/openai_adk.go:368)


runNonStreaming is a function that performs operations based on the provided parameters and may return an error.


```go
func runNonStreaming((ctx context.Context, m *OpenAIModel, params openai.ChatCompletionNewParams, yield func(*model.LLMResponse, error) bool)) (ctx context.Context, m *OpenAIModel, params openai.ChatCompletionNewParams, yield func(*model.LLMResponse, error) bool)
```


**Тип запроса:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип запроса:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** openai.ChatCompletionNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** yield


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `m *OpenAIModel`, `params openai.ChatCompletionNewParams`, `yield func(*model.LLMResponse`, `error) bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:368`



---


[function] name: runStreaming file: contrib/go-adk/pkg/models/openai_adk.go:263 returns_error: да description: —


### runStreaming (contrib/go-adk/pkg/models/openai_adk.go:263)


runStreaming is a function that performs operations based on the provided parameters and may return an error.


```go
func runStreaming((ctx context.Context, m *OpenAIModel, params openai.ChatCompletionNewParams, yield func(*model.LLMResponse, error) bool)) (ctx context.Context, m *OpenAIModel, params openai.ChatCompletionNewParams, yield func(*model.LLMResponse, error) bool)
```


**Тип запроса:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип запроса:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** OpenAIModel


```json
{
  "Config": null,
  "Client": {},
  "IsAzure": false,
  "Logger": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** openai.ChatCompletionNewParams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** yield


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** model.LLMResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `m *OpenAIModel`, `params openai.ChatCompletionNewParams`, `yield func(*model.LLMResponse`, `error) bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/models/openai_adk.go:263`




## contrib/go-adk/pkg/runner/adapter.go


📄 Исходный файл: `contrib/go-adk/pkg/runner/adapter.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [CreateRunnerConfig](#createrunnerconfig-contribgo-adkpkgrunneradaptergo24) `:24`

- 🔗 [agentNameFromAppName](#agentnamefromappname-contribgo-adkpkgrunneradaptergo16) `:16`


</details>


[function] name: CreateRunnerConfig file: contrib/go-adk/pkg/runner/adapter.go:24 returns_error: да description: CreateRunnerConfig creates a runner.Config suitable for use with adka2a.Executor.


### CreateRunnerConfig (contrib/go-adk/pkg/runner/adapter.go:24)


CreateRunnerConfig creates a runner.Config suitable for use with adka2a.Executor.


```go
func CreateRunnerConfig((runner.Config, error)) (runner.Config, error)
```


**Тип ответа:** runner.Config


```json
{
  "Metrics": {},
  "Webhook": {},
  "Streaming": {},
  "Proxy": {},
  "LeaderElection": false,
  "ProbeAddr": "string",
  "SecureMetrics": false,
  "EnableHTTP2": false,
  "DefaultModelConfig": {},
  "HttpServerAddr": "string",
  "WatchNamespaces": "string",
  "A2ABaseUrl": "string",
  "Database": {}
}
```


*Определено в:* `go/pkg/app/app.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `runner.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/runner/adapter.go:24`



---


[function] name: agentNameFromAppName file: contrib/go-adk/pkg/runner/adapter.go:16 returns_error: нет description: —


### agentNameFromAppName (contrib/go-adk/pkg/runner/adapter.go:16)


agentNameFromAppName is a function that performs operations based on the provided parameters and returns (appName string).


```go
func agentNameFromAppName((appName string)) (appName string)
```


**Тип ответа:** appName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/runner/adapter.go:16`




## contrib/go-adk/pkg/session/adapter.go


📄 Исходный файл: `contrib/go-adk/pkg/session/adapter.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [AppendEvent](#appendevent-contribgo-adkpkgsessionadaptergo107) `:107`

- 🔗 [Create](#create-contribgo-adkpkgsessionadaptergo32) `:32`

- 🔗 [Delete](#delete-contribgo-adkpkgsessionadaptergo96) `:96`

- 🔗 [Get](#get-contribgo-adkpkgsessionadaptergo53) `:53`

- 🔗 [List](#list-contribgo-adkpkgsessionadaptergo87) `:87`

- 🔗 [NewSessionServiceAdapter](#newsessionserviceadapter-contribgo-adkpkgsessionadaptergo27) `:27`

- 🔗 [convertADKSessionToOurs](#convertadksessiontoours-contribgo-adkpkgsessionadaptergo155) `:155`

- 🔗 [convertSessionToADK](#convertsessiontoadk-contribgo-adkpkgsessionadaptergo134) `:134`

- 🔗 [parseEventsToADK](#parseeventstoadk-contribgo-adkpkgsessionadaptergo170) `:170`

- 🔗 [parseRawToADKEvent](#parserawtoadkevent-contribgo-adkpkgsessionadaptergo220) `:220`


</details>


[function] name: AppendEvent file: contrib/go-adk/pkg/session/adapter.go:107 returns_error: нет description: AppendEvent implements session.Service.


### AppendEvent (contrib/go-adk/pkg/session/adapter.go:107)


AppendEvent implements session.Service.


```go
func (a *SessionServiceAdapter) AppendEvent((ctx context.Context, session adksession.Session, event *adksession.Event)) (ctx context.Context, session adksession.Session, event *adksession.Event)
```


**Тип запроса:** adksession.Event


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


**Тип ответа:** session


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** adksession.Session


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


**Тип ответа:** event


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adksession.Event


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


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:107`



---


[function] name: Create file: contrib/go-adk/pkg/session/adapter.go:32 returns_error: да description: Create implements session.Service.


### Create (contrib/go-adk/pkg/session/adapter.go:32)


Create implements session.Service.


```go
func (a *SessionServiceAdapter) Create((*adksession.CreateResponse, error)) (*adksession.CreateResponse, error)
```


**Тип запроса:** adksession.CreateResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adksession.CreateResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*adksession.CreateResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:32`



---


[function] name: Delete file: contrib/go-adk/pkg/session/adapter.go:96 returns_error: нет description: Delete implements session.Service.


### Delete (contrib/go-adk/pkg/session/adapter.go:96)


Delete implements session.Service.


```go
func (a *SessionServiceAdapter) Delete((ctx context.Context, req *adksession.DeleteRequest)) (ctx context.Context, req *adksession.DeleteRequest)
```


**Тип запроса:** adksession.DeleteRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** adksession.DeleteRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:96`



---


[function] name: Get file: contrib/go-adk/pkg/session/adapter.go:53 returns_error: да description: Get implements session.Service.


### Get (contrib/go-adk/pkg/session/adapter.go:53)


Get implements session.Service.


```go
func (a *SessionServiceAdapter) Get((*adksession.GetResponse, error)) (*adksession.GetResponse, error)
```


**Тип запроса:** adksession.GetResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adksession.GetResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*adksession.GetResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:53`



---


[function] name: List file: contrib/go-adk/pkg/session/adapter.go:87 returns_error: да description: List implements session.Service.


### List (contrib/go-adk/pkg/session/adapter.go:87)


List implements session.Service.


```go
func (a *SessionServiceAdapter) List((*adksession.ListResponse, error)) (*adksession.ListResponse, error)
```


**Тип запроса:** adksession.ListResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adksession.ListResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*adksession.ListResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:87`



---


[function] name: NewSessionServiceAdapter file: contrib/go-adk/pkg/session/adapter.go:27 returns_error: нет description: NewSessionServiceAdapter creates a new adapter.


### NewSessionServiceAdapter (contrib/go-adk/pkg/session/adapter.go:27)


NewSessionServiceAdapter creates a new adapter.


```go
func NewSessionServiceAdapter((service SessionService)) (service SessionService)
```


**Тип ответа:** service


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SessionService


```json
{
  "BaseURL": "string",
  "Client": null
}
```


*Определено в:* `contrib/go-adk/pkg/session/session.go`


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:27`



---


[function] name: convertADKSessionToOurs file: contrib/go-adk/pkg/session/adapter.go:155 returns_error: нет description: convertADKSessionToOurs converts an adksession.Session back to our Session.


### convertADKSessionToOurs (contrib/go-adk/pkg/session/adapter.go:155)


convertADKSessionToOurs converts an adksession.Session back to our Session.


```go
func convertADKSessionToOurs((s adksession.Session)) (s adksession.Session)
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


**Тип ответа:** adksession.Session


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


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:155`



---


[function] name: convertSessionToADK file: contrib/go-adk/pkg/session/adapter.go:134 returns_error: нет description: convertSessionToADK converts our Session to a localSession implementing adksession.Session.


### convertSessionToADK (contrib/go-adk/pkg/session/adapter.go:134)


convertSessionToADK converts our Session to a localSession implementing adksession.Session.


```go
func convertSessionToADK((sess *Session)) (sess *Session)
```


**Тип запроса:** Session


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


**Тип ответа:** sess


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** Session


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


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:134`



---


[function] name: parseEventsToADK file: contrib/go-adk/pkg/session/adapter.go:170 returns_error: нет description: parseEventsToADK converts backend event payloads to *adksession.Event.


### parseEventsToADK (contrib/go-adk/pkg/session/adapter.go:170)


parseEventsToADK converts backend event payloads to *adksession.Event.


```go
func parseEventsToADK((ctx context.Context, events []any)) (ctx context.Context, events []any)
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


**Тип ответа:** events


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:170`



---


[function] name: parseRawToADKEvent file: contrib/go-adk/pkg/session/adapter.go:220 returns_error: нет description: parseRawToADKEvent unmarshals JSON bytes into *adksession.Event.


### parseRawToADKEvent (contrib/go-adk/pkg/session/adapter.go:220)


parseRawToADKEvent unmarshals JSON bytes into *adksession.Event.


```go
func parseRawToADKEvent((ctx context.Context, data []byte)) (ctx context.Context, data []byte)
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


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/adapter.go:220`




## contrib/go-adk/pkg/session/local_session.go


📄 Исходный файл: `contrib/go-adk/pkg/session/local_session.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [All](#all-contribgo-adkpkgsessionlocal_sessiongo68) `:68`

- 🔗 [All](#all-contribgo-adkpkgsessionlocal_sessiongo110) `:110`

- 🔗 [AppName](#appname-contribgo-adkpkgsessionlocal_sessiongo26) `:26`

- 🔗 [At](#at-contribgo-adkpkgsessionlocal_sessiongo80) `:80`

- 🔗 [Events](#events-contribgo-adkpkgsessionlocal_sessiongo33) `:33`

- 🔗 [Get](#get-contribgo-adkpkgsessionlocal_sessiongo93) `:93`

- 🔗 [ID](#id-contribgo-adkpkgsessionlocal_sessiongo25) `:25`

- 🔗 [LastUpdateTime](#lastupdatetime-contribgo-adkpkgsessionlocal_sessiongo41) `:41`

- 🔗 [Len](#len-contribgo-adkpkgsessionlocal_sessiongo78) `:78`

- 🔗 [Set](#set-contribgo-adkpkgsessionlocal_sessiongo103) `:103`

- 🔗 [State](#state-contribgo-adkpkgsessionlocal_sessiongo29) `:29`

- 🔗 [UserID](#userid-contribgo-adkpkgsessionlocal_sessiongo27) `:27`

- 🔗 [appendEvent](#appendevent-contribgo-adkpkgsessionlocal_sessiongo47) `:47`

- 🔗 [trimTempDeltaState](#trimtempdeltastate-contribgo-adkpkgsessionlocal_sessiongo129) `:129`

- 🔗 [updateSessionState](#updatesessionstate-contribgo-adkpkgsessionlocal_sessiongo145) `:145`


</details>


[function] name: All file: contrib/go-adk/pkg/session/local_session.go:68 returns_error: нет description: —


### All (contrib/go-adk/pkg/session/local_session.go:68)


All is a method that performs operations based on the provided parameters and returns ().


```go
func (e events) All(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:68`



---


[function] name: All file: contrib/go-adk/pkg/session/local_session.go:110 returns_error: нет description: —


### All (contrib/go-adk/pkg/session/local_session.go:110)


All is a method that performs operations based on the provided parameters and returns ().


```go
func (s *sessionState) All(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:110`



---


[function] name: AppName file: contrib/go-adk/pkg/session/local_session.go:26 returns_error: нет description: —


### AppName (contrib/go-adk/pkg/session/local_session.go:26)


AppName is a method that performs operations based on the provided parameters and returns ().


```go
func (s *localSession) AppName(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:26`



---


[function] name: At file: contrib/go-adk/pkg/session/local_session.go:80 returns_error: нет description: —


### At (contrib/go-adk/pkg/session/local_session.go:80)


At is a method that performs operations based on the provided parameters and returns (i int).


```go
func (e events) At((i int)) (i int)
```


**Тип ответа:** i


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:80`



---


[function] name: Events file: contrib/go-adk/pkg/session/local_session.go:33 returns_error: нет description: —


### Events (contrib/go-adk/pkg/session/local_session.go:33)


Events is a method that performs operations based on the provided parameters and returns ().


```go
func (s *localSession) Events(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:33`



---


[function] name: Get file: contrib/go-adk/pkg/session/local_session.go:93 returns_error: да description: —


### Get (contrib/go-adk/pkg/session/local_session.go:93)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *sessionState) Get((any, error)) (any, error)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:93`



---


[function] name: ID file: contrib/go-adk/pkg/session/local_session.go:25 returns_error: нет description: —


### ID (contrib/go-adk/pkg/session/local_session.go:25)


ID is a method that performs operations based on the provided parameters and returns ().


```go
func (s *localSession) ID(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:25`



---


[function] name: LastUpdateTime file: contrib/go-adk/pkg/session/local_session.go:41 returns_error: нет description: —


### LastUpdateTime (contrib/go-adk/pkg/session/local_session.go:41)


LastUpdateTime is a method that performs operations based on the provided parameters and returns ().


```go
func (s *localSession) LastUpdateTime(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:41`



---


[function] name: Len file: contrib/go-adk/pkg/session/local_session.go:78 returns_error: нет description: —


### Len (contrib/go-adk/pkg/session/local_session.go:78)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (e events) Len(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:78`



---


[function] name: Set file: contrib/go-adk/pkg/session/local_session.go:103 returns_error: нет description: —


### Set (contrib/go-adk/pkg/session/local_session.go:103)


Set is a method that updates data based on the provided parameters and returns (key string, value any).


```go
func (s *sessionState) Set((key string, value any)) (key string, value any)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:103`



---


[function] name: State file: contrib/go-adk/pkg/session/local_session.go:29 returns_error: нет description: —


### State (contrib/go-adk/pkg/session/local_session.go:29)


State is a method that performs operations based on the provided parameters and returns ().


```go
func (s *localSession) State(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:29`



---


[function] name: UserID file: contrib/go-adk/pkg/session/local_session.go:27 returns_error: нет description: —


### UserID (contrib/go-adk/pkg/session/local_session.go:27)


UserID is a method that performs operations based on the provided parameters and returns ().


```go
func (s *localSession) UserID(()) ()
```


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:27`



---


[function] name: appendEvent file: contrib/go-adk/pkg/session/local_session.go:47 returns_error: нет description: —


### appendEvent (contrib/go-adk/pkg/session/local_session.go:47)


appendEvent is a method that performs operations based on the provided parameters and returns (event *adksession.Event).


```go
func (s *localSession) appendEvent((event *adksession.Event)) (event *adksession.Event)
```


**Тип запроса:** adksession.Event


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


**Тип ответа:** event


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adksession.Event


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


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:47`



---


[function] name: trimTempDeltaState file: contrib/go-adk/pkg/session/local_session.go:129 returns_error: нет description: trimTempDeltaState returns an event with temporary state delta keys removed.
It creates a shallow copy of the event to a


### trimTempDeltaState (contrib/go-adk/pkg/session/local_session.go:129)


trimTempDeltaState returns an event with temporary state delta keys removed.
It creates a shallow copy of the event to avoid mutating the original.


```go
func trimTempDeltaState((event *adksession.Event)) (event *adksession.Event)
```


**Тип запроса:** adksession.Event


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


**Тип ответа:** event


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adksession.Event


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


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:129`



---


[function] name: updateSessionState file: contrib/go-adk/pkg/session/local_session.go:145 returns_error: нет description: updateSessionState applies event state delta to the session.


### updateSessionState (contrib/go-adk/pkg/session/local_session.go:145)


updateSessionState applies event state delta to the session.


```go
func updateSessionState((sess *localSession, event *adksession.Event)) (sess *localSession, event *adksession.Event)
```


**Тип запроса:** localSession


```json
{
  "appName": "string",
  "userID": "string",
  "sessionID": "string",
  "mu": {},
  "events": [],
  "state": {},
  "updatedAt": {}
}
```


*Определено в:* `contrib/go-adk/pkg/session/local_session.go`


**Тип запроса:** adksession.Event


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


**Тип ответа:** sess


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** localSession


```json
{
  "appName": "string",
  "userID": "string",
  "sessionID": "string",
  "mu": {},
  "events": [],
  "state": {},
  "updatedAt": {}
}
```


*Определено в:* `contrib/go-adk/pkg/session/local_session.go`


**Тип ответа:** event


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adksession.Event


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


📍 *Расположение:* `contrib/go-adk/pkg/session/local_session.go:145`




## contrib/go-adk/pkg/session/session.go


📄 Исходный файл: `contrib/go-adk/pkg/session/session.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [AppendEvent](#appendevent-contribgo-adkpkgsessionsessiongo227) `:227`

- 🔗 [CreateSession](#createsession-contribgo-adkpkgsessionsessiongo55) `:55`

- 🔗 [DeleteSession](#deletesession-contribgo-adkpkgsessionsessiongo201) `:201`

- 🔗 [GetSession](#getsession-contribgo-adkpkgsessionsessiongo117) `:117`

- 🔗 [NewKAgentSessionService](#newkagentsessionservice-contribgo-adkpkgsessionsessiongo45) `:45`

- 🔗 [extractEventID](#extracteventid-contribgo-adkpkgsessionsessiongo276) `:276`

- 🔗 [extractStringFromField](#extractstringfromfield-contribgo-adkpkgsessionsessiongo352) `:352`

- 🔗 [getIDFromMap](#getidfrommap-contribgo-adkpkgsessionsessiongo309) `:309`

- 🔗 [getIDFromStruct](#getidfromstruct-contribgo-adkpkgsessionsessiongo329) `:329`

- 🔗 [getMapKeys](#getmapkeys-contribgo-adkpkgsessionsessiongo364) `:364`


</details>


[function] name: AppendEvent file: contrib/go-adk/pkg/session/session.go:227 returns_error: нет description: —


### AppendEvent (contrib/go-adk/pkg/session/session.go:227)


AppendEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, session *Session, event any).


```go
func (s *KAgentSessionService) AppendEvent((ctx context.Context, session *Session, event any)) (ctx context.Context, session *Session, event any)
```


**Тип запроса:** Session


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


**Тип ответа:** session


```json
{
  "session": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** Session


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


**Тип ответа:** event


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:227`



---


[function] name: CreateSession file: contrib/go-adk/pkg/session/session.go:55 returns_error: да description: —


### CreateSession (contrib/go-adk/pkg/session/session.go:55)


CreateSession is a method that creates new data based on the provided parameters and may return an error.


```go
func (s *KAgentSessionService) CreateSession((*Session, error)) (*Session, error)
```


**Тип запроса:** Session


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


**Тип ответа:** Session


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


*Типы возврата:* `*Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:55`



---


[function] name: DeleteSession file: contrib/go-adk/pkg/session/session.go:201 returns_error: нет description: —


### DeleteSession (contrib/go-adk/pkg/session/session.go:201)


DeleteSession is a method that deletes data based on the provided parameters and returns (ctx context.Context, appName, userID, sessionID string).


```go
func (s *KAgentSessionService) DeleteSession((ctx context.Context, appName, userID, sessionID string)) (ctx context.Context, appName, userID, sessionID string)
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


**Тип ответа:** appName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:201`



---


[function] name: GetSession file: contrib/go-adk/pkg/session/session.go:117 returns_error: да description: —


### GetSession (contrib/go-adk/pkg/session/session.go:117)


GetSession is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *KAgentSessionService) GetSession((*Session, error)) (*Session, error)
```


**Тип запроса:** Session


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


**Тип ответа:** Session


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


*Типы возврата:* `*Session`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:117`



---


[function] name: NewKAgentSessionService file: contrib/go-adk/pkg/session/session.go:45 returns_error: нет description: NewKAgentSessionService creates a new KAgentSessionService.
If client is nil, http.DefaultClient is used.


### NewKAgentSessionService (contrib/go-adk/pkg/session/session.go:45)


NewKAgentSessionService creates a new KAgentSessionService.
If client is nil, http.DefaultClient is used.


```go
func NewKAgentSessionService((baseURL string, client *http.Client)) (baseURL string, client *http.Client)
```


**Тип запроса:** http.Client


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


**Тип ответа:** baseURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** http.Client


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


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:45`



---


[function] name: extractEventID file: contrib/go-adk/pkg/session/session.go:276 returns_error: нет description: —


### extractEventID (contrib/go-adk/pkg/session/session.go:276)


extractEventID is a function that performs operations based on the provided parameters and returns (ctx context.Context, event any, eventData []byte).


```go
func extractEventID((ctx context.Context, event any, eventData []byte)) (ctx context.Context, event any, eventData []byte)
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


**Тип ответа:** event


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** eventData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:276`



---


[function] name: extractStringFromField file: contrib/go-adk/pkg/session/session.go:352 returns_error: нет description: —


### extractStringFromField (contrib/go-adk/pkg/session/session.go:352)


extractStringFromField is a function that performs operations based on the provided parameters and returns (field reflect.Value).


```go
func extractStringFromField((field reflect.Value)) (field reflect.Value)
```


**Тип ответа:** field


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reflect.Value


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:352`



---


[function] name: getIDFromMap file: contrib/go-adk/pkg/session/session.go:309 returns_error: нет description: —


### getIDFromMap (contrib/go-adk/pkg/session/session.go:309)


getIDFromMap is a function that performs operations based on the provided parameters and returns (m map[string]any).


```go
func getIDFromMap((m map[string]any)) (m map[string]any)
```


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:309`



---


[function] name: getIDFromStruct file: contrib/go-adk/pkg/session/session.go:329 returns_error: нет description: —


### getIDFromStruct (contrib/go-adk/pkg/session/session.go:329)


getIDFromStruct is a function that performs operations based on the provided parameters and returns (v reflect.Value).


```go
func getIDFromStruct((v reflect.Value)) (v reflect.Value)
```


**Тип ответа:** v


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** reflect.Value


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:329`



---


[function] name: getMapKeys file: contrib/go-adk/pkg/session/session.go:364 returns_error: нет description: —


### getMapKeys (contrib/go-adk/pkg/session/session.go:364)


getMapKeys is a function that performs operations based on the provided parameters and returns (m map[string]any).


```go
func getMapKeys((m map[string]any)) (m map[string]any)
```


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/session/session.go:364`




## contrib/go-adk/pkg/skills/discovery.go


📄 Исходный файл: `contrib/go-adk/pkg/skills/discovery.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [DiscoverSkills](#discoverskills-contribgo-adkpkgskillsdiscoverygo17) `:17`

- 🔗 [GenerateSkillsToolDescription](#generateskillstooldescription-contribgo-adkpkgskillsdiscoverygo118) `:118`

- 🔗 [GetSessionPath](#getsessionpath-contribgo-adkpkgskillsdiscoverygo135) `:135`

- 🔗 [LoadSkillContent](#loadskillcontent-contribgo-adkpkgskillsdiscoverygo60) `:60`

- 🔗 [parseSkillMetadata](#parseskillmetadata-contribgo-adkpkgskillsdiscoverygo77) `:77`


</details>


[function] name: DiscoverSkills file: contrib/go-adk/pkg/skills/discovery.go:17 returns_error: да description: DiscoverSkills discovers available skills in the skills directory


### DiscoverSkills (contrib/go-adk/pkg/skills/discovery.go:17)


DiscoverSkills discovers available skills in the skills directory


```go
func DiscoverSkills(([]Skill, error)) ([]Skill, error)
```


**Тип ответа:** Skill


```json
{
  "Name": "string",
  "Description": "string"
}
```


*Определено в:* `contrib/go-adk/pkg/skills/discovery.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]Skill`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/discovery.go:17`



---


[function] name: GenerateSkillsToolDescription file: contrib/go-adk/pkg/skills/discovery.go:118 returns_error: нет description: GenerateSkillsToolDescription generates a tool description with available skills


### GenerateSkillsToolDescription (contrib/go-adk/pkg/skills/discovery.go:118)


GenerateSkillsToolDescription generates a tool description with available skills


```go
func GenerateSkillsToolDescription((skills []Skill)) (skills []Skill)
```


**Тип ответа:** skills


```json
{
  "AuthMountPath": "string",
  "GitRefs": [],
  "OCIRefs": [],
  "InsecureOCI": false
}
```


*Определено в:* `go/internal/controller/translator/agent/adk_api_translator.go`


**Тип ответа:** Skill


```json
{
  "Name": "string",
  "Description": "string"
}
```


*Определено в:* `contrib/go-adk/pkg/skills/discovery.go`


📍 *Расположение:* `contrib/go-adk/pkg/skills/discovery.go:118`



---


[function] name: GetSessionPath file: contrib/go-adk/pkg/skills/discovery.go:135 returns_error: да description: GetSessionPath returns the working directory path for a session


### GetSessionPath (contrib/go-adk/pkg/skills/discovery.go:135)


GetSessionPath returns the working directory path for a session


```go
func GetSessionPath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/discovery.go:135`



---


[function] name: LoadSkillContent file: contrib/go-adk/pkg/skills/discovery.go:60 returns_error: да description: LoadSkillContent loads the full content of a skill's SKILL.md file


### LoadSkillContent (contrib/go-adk/pkg/skills/discovery.go:60)


LoadSkillContent loads the full content of a skill's SKILL.md file


```go
func LoadSkillContent((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/discovery.go:60`



---


[function] name: parseSkillMetadata file: contrib/go-adk/pkg/skills/discovery.go:77 returns_error: да description: parseSkillMetadata parses YAML frontmatter from SKILL.md


### parseSkillMetadata (contrib/go-adk/pkg/skills/discovery.go:77)


parseSkillMetadata parses YAML frontmatter from SKILL.md


```go
func parseSkillMetadata((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/discovery.go:77`




## contrib/go-adk/pkg/skills/shell.go


📄 Исходный файл: `contrib/go-adk/pkg/skills/shell.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [EditFileContent](#editfilecontent-contribgo-adkpkgskillsshellgo68) `:68`

- 🔗 [ExecuteCommand](#executecommand-contribgo-adkpkgskillsshellgo109) `:109`

- 🔗 [ReadFileContent](#readfilecontent-contribgo-adkpkgskillsshellgo16) `:16`

- 🔗 [WriteFileContent](#writefilecontent-contribgo-adkpkgskillsshellgo59) `:59`


</details>


[function] name: EditFileContent file: contrib/go-adk/pkg/skills/shell.go:68 returns_error: нет description: EditFileContent performs an exact string replacement in a file.


### EditFileContent (contrib/go-adk/pkg/skills/shell.go:68)


EditFileContent performs an exact string replacement in a file.


```go
func EditFileContent((path string, oldString, newString string, replaceAll bool)) (path string, oldString, newString string, replaceAll bool)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** replaceAll


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/skills/shell.go:68`



---


[function] name: ExecuteCommand file: contrib/go-adk/pkg/skills/shell.go:109 returns_error: да description: ExecuteCommand executes a shell command.


### ExecuteCommand (contrib/go-adk/pkg/skills/shell.go:109)


ExecuteCommand executes a shell command.


```go
func ExecuteCommand((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/shell.go:109`



---


[function] name: ReadFileContent file: contrib/go-adk/pkg/skills/shell.go:16 returns_error: да description: ReadFileContent reads a file with line numbers.


### ReadFileContent (contrib/go-adk/pkg/skills/shell.go:16)


ReadFileContent reads a file with line numbers.


```go
func ReadFileContent((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/shell.go:16`



---


[function] name: WriteFileContent file: contrib/go-adk/pkg/skills/shell.go:59 returns_error: нет description: WriteFileContent writes content to a file.


### WriteFileContent (contrib/go-adk/pkg/skills/shell.go:59)


WriteFileContent writes content to a file.


```go
func WriteFileContent((path string, content string)) (path string, content string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/skills/shell.go:59`




## contrib/go-adk/pkg/skills/skills_tools.go


📄 Исходный файл: `contrib/go-adk/pkg/skills/skills_tools.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [EditFile](#editfile-contribgo-adkpkgskillsskills_toolsgo72) `:72`

- 🔗 [Execute](#execute-contribgo-adkpkgskillsskills_toolsgo19) `:19`

- 🔗 [Execute](#execute-contribgo-adkpkgskillsskills_toolsgo48) `:48`

- 🔗 [InitializeSessionPath](#initializesessionpath-contribgo-adkpkgskillsskills_toolsgo77) `:77`

- 🔗 [NewBashTool](#newbashtool-contribgo-adkpkgskillsskills_toolsgo43) `:43`

- 🔗 [NewSkillsTool](#newskillstool-contribgo-adkpkgskillsskills_toolsgo14) `:14`

- 🔗 [ReadFile](#readfile-contribgo-adkpkgskillsskills_toolsgo62) `:62`

- 🔗 [WriteFile](#writefile-contribgo-adkpkgskillsskills_toolsgo67) `:67`


</details>


[function] name: EditFile file: contrib/go-adk/pkg/skills/skills_tools.go:72 returns_error: нет description: EditFile performs an exact string replacement in a file


### EditFile (contrib/go-adk/pkg/skills/skills_tools.go:72)


EditFile performs an exact string replacement in a file


```go
func (ft *FileTools) EditFile((path string, oldString, newString string, replaceAll bool)) (path string, oldString, newString string, replaceAll bool)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** replaceAll


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:72`



---


[function] name: Execute file: contrib/go-adk/pkg/skills/skills_tools.go:19 returns_error: да description: Execute executes the skills tool command


### Execute (contrib/go-adk/pkg/skills/skills_tools.go:19)


Execute executes the skills tool command


```go
func (t *SkillsTool) Execute((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:19`



---


[function] name: Execute file: contrib/go-adk/pkg/skills/skills_tools.go:48 returns_error: да description: Execute executes a bash command in the skills context


### Execute (contrib/go-adk/pkg/skills/skills_tools.go:48)


Execute executes a bash command in the skills context


```go
func (t *BashTool) Execute((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:48`



---


[function] name: InitializeSessionPath file: contrib/go-adk/pkg/skills/skills_tools.go:77 returns_error: да description: InitializeSessionPath initializes a session's working directory with skills symlink


### InitializeSessionPath (contrib/go-adk/pkg/skills/skills_tools.go:77)


InitializeSessionPath initializes a session's working directory with skills symlink


```go
func InitializeSessionPath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:77`



---


[function] name: NewBashTool file: contrib/go-adk/pkg/skills/skills_tools.go:43 returns_error: нет description: NewBashTool creates a new BashTool


### NewBashTool (contrib/go-adk/pkg/skills/skills_tools.go:43)


NewBashTool creates a new BashTool


```go
func NewBashTool((skillsDirectory string)) (skillsDirectory string)
```


**Тип ответа:** skillsDirectory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:43`



---


[function] name: NewSkillsTool file: contrib/go-adk/pkg/skills/skills_tools.go:14 returns_error: нет description: NewSkillsTool creates a new SkillsTool


### NewSkillsTool (contrib/go-adk/pkg/skills/skills_tools.go:14)


NewSkillsTool creates a new SkillsTool


```go
func NewSkillsTool((skillsDirectory string)) (skillsDirectory string)
```


**Тип ответа:** skillsDirectory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:14`



---


[function] name: ReadFile file: contrib/go-adk/pkg/skills/skills_tools.go:62 returns_error: да description: ReadFile reads a file with line numbers


### ReadFile (contrib/go-adk/pkg/skills/skills_tools.go:62)


ReadFile reads a file with line numbers


```go
func (ft *FileTools) ReadFile((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:62`



---


[function] name: WriteFile file: contrib/go-adk/pkg/skills/skills_tools.go:67 returns_error: нет description: WriteFile writes content to a file


### WriteFile (contrib/go-adk/pkg/skills/skills_tools.go:67)


WriteFile writes content to a file


```go
func (ft *FileTools) WriteFile((path string, content string)) (path string, content string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/skills/skills_tools.go:67`




## contrib/go-adk/pkg/taskstore/a2a_adapter.go


📄 Исходный файл: `contrib/go-adk/pkg/taskstore/a2a_adapter.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Get](#get-contribgo-adkpkgtaskstorea2a_adaptergo31) `:31`

- 🔗 [List](#list-contribgo-adkpkgtaskstorea2a_adaptergo45) `:45`

- 🔗 [NewA2ATaskStoreAdapter](#newa2ataskstoreadapter-contribgo-adkpkgtaskstorea2a_adaptergo18) `:18`

- 🔗 [Save](#save-contribgo-adkpkgtaskstorea2a_adaptergo23) `:23`


</details>


[function] name: Get file: contrib/go-adk/pkg/taskstore/a2a_adapter.go:31 returns_error: да description: Get implements a2asrv.TaskStore.


### Get (contrib/go-adk/pkg/taskstore/a2a_adapter.go:31)


Get implements a2asrv.TaskStore.


```go
func (a *A2ATaskStoreAdapter) Get((*a2atype.Task, a2atype.TaskVersion, error)) (*a2atype.Task, a2atype.TaskVersion, error)
```


**Тип запроса:** a2atype.Task


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


**Тип ответа:** a2atype.Task


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


**Тип ответа:** a2atype.TaskVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*a2atype.Task`, `a2atype.TaskVersion`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/a2a_adapter.go:31`



---


[function] name: List file: contrib/go-adk/pkg/taskstore/a2a_adapter.go:45 returns_error: да description: List implements a2asrv.TaskStore.
The underlying KAgentTaskStore does not support listing tasks, so this
returns an erro


### List (contrib/go-adk/pkg/taskstore/a2a_adapter.go:45)


List implements a2asrv.TaskStore.
The underlying KAgentTaskStore does not support listing tasks, so this
returns an error to signal callers that the operation is unsupported.


```go
func (a *A2ATaskStoreAdapter) List((*a2atype.ListTasksResponse, error)) (*a2atype.ListTasksResponse, error)
```


**Тип запроса:** a2atype.ListTasksResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.ListTasksResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*a2atype.ListTasksResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/a2a_adapter.go:45`



---


[function] name: NewA2ATaskStoreAdapter file: contrib/go-adk/pkg/taskstore/a2a_adapter.go:18 returns_error: нет description: NewA2ATaskStoreAdapter creates an adapter that implements a2asrv.TaskStore
by delegating to KAgentTaskStore.


### NewA2ATaskStoreAdapter (contrib/go-adk/pkg/taskstore/a2a_adapter.go:18)


NewA2ATaskStoreAdapter creates an adapter that implements a2asrv.TaskStore
by delegating to KAgentTaskStore.


```go
func NewA2ATaskStoreAdapter((store *KAgentTaskStore)) (store *KAgentTaskStore)
```


**Тип запроса:** KAgentTaskStore


```json
{
  "BaseURL": "string",
  "Client": null
}
```


*Определено в:* `contrib/go-adk/pkg/taskstore/store.go`


**Тип ответа:** store


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** KAgentTaskStore


```json
{
  "BaseURL": "string",
  "Client": null
}
```


*Определено в:* `contrib/go-adk/pkg/taskstore/store.go`


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/a2a_adapter.go:18`



---


[function] name: Save file: contrib/go-adk/pkg/taskstore/a2a_adapter.go:23 returns_error: да description: Save implements a2asrv.TaskStore.


### Save (contrib/go-adk/pkg/taskstore/a2a_adapter.go:23)


Save implements a2asrv.TaskStore.


```go
func (a *A2ATaskStoreAdapter) Save((a2atype.TaskVersion, error)) (a2atype.TaskVersion, error)
```


**Тип ответа:** a2atype.TaskVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `a2atype.TaskVersion`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/a2a_adapter.go:23`




## contrib/go-adk/pkg/taskstore/store.go


📄 Исходный файл: `contrib/go-adk/pkg/taskstore/store.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Get](#get-contribgo-adkpkgtaskstorestorego129) `:129`

- 🔗 [NewKAgentTaskStoreWithClient](#newkagenttaskstorewithclient-contribgo-adkpkgtaskstorestorego31) `:31`

- 🔗 [Save](#save-contribgo-adkpkgtaskstorestorego89) `:89`

- 🔗 [cleanPartialArtifacts](#cleanpartialartifacts-contribgo-adkpkgtaskstorestorego77) `:77`

- 🔗 [cleanPartialEvents](#cleanpartialevents-contribgo-adkpkgtaskstorestorego65) `:65`

- 🔗 [isPartialMeta](#ispartialmeta-contribgo-adkpkgtaskstorestorego51) `:51`


</details>


[function] name: Get file: contrib/go-adk/pkg/taskstore/store.go:129 returns_error: да description: Get retrieves a task from KAgent


### Get (contrib/go-adk/pkg/taskstore/store.go:129)


Get retrieves a task from KAgent


```go
func (s *KAgentTaskStore) Get((*a2atype.Task, error)) (*a2atype.Task, error)
```


**Тип запроса:** a2atype.Task


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


**Тип ответа:** a2atype.Task


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


*Типы возврата:* `*a2atype.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/store.go:129`



---


[function] name: NewKAgentTaskStoreWithClient file: contrib/go-adk/pkg/taskstore/store.go:31 returns_error: нет description: NewKAgentTaskStoreWithClient creates a new KAgentTaskStore with a custom HTTP client.
If client is nil, http.DefaultClie


### NewKAgentTaskStoreWithClient (contrib/go-adk/pkg/taskstore/store.go:31)


NewKAgentTaskStoreWithClient creates a new KAgentTaskStore with a custom HTTP client.
If client is nil, http.DefaultClient is used.


```go
func NewKAgentTaskStoreWithClient((baseURL string, client *http.Client)) (baseURL string, client *http.Client)
```


**Тип запроса:** http.Client


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


**Тип ответа:** baseURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** http.Client


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


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/store.go:31`



---


[function] name: Save file: contrib/go-adk/pkg/taskstore/store.go:89 returns_error: нет description: Save saves a task to KAgent


### Save (contrib/go-adk/pkg/taskstore/store.go:89)


Save saves a task to KAgent


```go
func (s *KAgentTaskStore) Save((ctx context.Context, task *a2atype.Task)) (ctx context.Context, task *a2atype.Task)
```


**Тип запроса:** a2atype.Task


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


**Тип ответа:** task


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.Task


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


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/store.go:89`



---


[function] name: cleanPartialArtifacts file: contrib/go-adk/pkg/taskstore/store.go:77 returns_error: нет description: cleanPartialArtifacts removes partial streaming artifacts.


### cleanPartialArtifacts (contrib/go-adk/pkg/taskstore/store.go:77)


cleanPartialArtifacts removes partial streaming artifacts.


```go
func cleanPartialArtifacts((artifacts []*a2atype.Artifact)) (artifacts []*a2atype.Artifact)
```


**Тип запроса:** a2atype.Artifact


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** artifacts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.Artifact


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/store.go:77`



---


[function] name: cleanPartialEvents file: contrib/go-adk/pkg/taskstore/store.go:65 returns_error: нет description: cleanPartialEvents removes partial streaming events from history.


### cleanPartialEvents (contrib/go-adk/pkg/taskstore/store.go:65)


cleanPartialEvents removes partial streaming events from history.


```go
func cleanPartialEvents((history []*a2atype.Message)) (history []*a2atype.Message)
```


**Тип запроса:** a2atype.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** history


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** a2atype.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/store.go:65`



---


[function] name: isPartialMeta file: contrib/go-adk/pkg/taskstore/store.go:51 returns_error: нет description: isPartialMeta checks if a metadata map has a partial flag set to true.
It checks both the upstream ADK key (adk_partial)


### isPartialMeta (contrib/go-adk/pkg/taskstore/store.go:51)


isPartialMeta checks if a metadata map has a partial flag set to true.
It checks both the upstream ADK key (adk_partial) and the kagent key
(kagent_adk_partial) so that events from either prefix are recognised.


```go
func isPartialMeta((meta map[string]any)) (meta map[string]any)
```


**Тип ответа:** meta


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/taskstore/store.go:51`




## contrib/go-adk/pkg/telemetry/tracing.go


📄 Исходный файл: `contrib/go-adk/pkg/telemetry/tracing.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetKAgentSpanAttributes](#setkagentspanattributes-contribgo-adkpkgtelemetrytracinggo11) `:11`


</details>


[function] name: SetKAgentSpanAttributes file: contrib/go-adk/pkg/telemetry/tracing.go:11 returns_error: нет description: SetKAgentSpanAttributes sets kagent span attributes in the OpenTelemetry context


### SetKAgentSpanAttributes (contrib/go-adk/pkg/telemetry/tracing.go:11)


SetKAgentSpanAttributes sets kagent span attributes in the OpenTelemetry context


```go
func SetKAgentSpanAttributes((ctx context.Context, attributes map[string]string)) (ctx context.Context, attributes map[string]string)
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


**Тип ответа:** attributes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `contrib/go-adk/pkg/telemetry/tracing.go:11`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Следующая директория](go_api.md)


---

