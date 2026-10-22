---
title: "Функции: go/pkg"
type: functions
repo: kagent
language: ru
chunk_boundary: h3
group: go/pkg
---


# Функции: go/pkg


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_internal.md)

- [Следующая директория](go_test.md)


---


## Меню по файлам


- 📄 [go/pkg/adk/types.go](#gopkgadktypesgo)

- 📄 [go/pkg/app/app.go](#gopkgappappgo)

- 📄 [go/pkg/auth/auth.go](#gopkgauthauthgo)

- 📄 [go/pkg/client/agent.go](#gopkgclientagentgo)

- 📄 [go/pkg/client/api/types.go](#gopkgclientapitypesgo)

- 📄 [go/pkg/client/base.go](#gopkgclientbasego)

- 📄 [go/pkg/client/clientset.go](#gopkgclientclientsetgo)

- 📄 [go/pkg/client/feedback.go](#gopkgclientfeedbackgo)

- 📄 [go/pkg/client/health.go](#gopkgclienthealthgo)

- 📄 [go/pkg/client/memory.go](#gopkgclientmemorygo)

- 📄 [go/pkg/client/model.go](#gopkgclientmodelgo)

- 📄 [go/pkg/client/modelconfig.go](#gopkgclientmodelconfiggo)

- 📄 [go/pkg/client/modelproviderconfig.go](#gopkgclientmodelproviderconfiggo)

- 📄 [go/pkg/client/namespace.go](#gopkgclientnamespacego)

- 📄 [go/pkg/client/session.go](#gopkgclientsessiongo)

- 📄 [go/pkg/client/tool.go](#gopkgclienttoolgo)

- 📄 [go/pkg/client/toolserver.go](#gopkgclienttoolservergo)

- 📄 [go/pkg/client/version.go](#gopkgclientversiongo)

- 📄 [go/pkg/database/models.go](#gopkgdatabasemodelsgo)

- 📄 [go/pkg/env/var.go](#gopkgenvvargo)

- 📄 [go/pkg/utils/utils.go](#gopkgutilsutilsgo)


---


## go/pkg/adk/types.go


📄 Исходный файл: `go/pkg/adk/types.go`


<details open>
<summary><b>Функции в этом файле (23)</b></summary>


- 🔗 [GetType](#gettype-gopkgadktypesgo93) `:93`

- 🔗 [GetType](#gettype-gopkgadktypesgo101) `:101`

- 🔗 [GetType](#gettype-gopkgadktypesgo132) `:132`

- 🔗 [GetType](#gettype-gopkgadktypesgo151) `:151`

- 🔗 [GetType](#gettype-gopkgadktypesgo170) `:170`

- 🔗 [GetType](#gettype-gopkgadktypesgo190) `:190`

- 🔗 [GetType](#gettype-gopkgadktypesgo209) `:209`

- 🔗 [GetType](#gettype-gopkgadktypesgo230) `:230`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo81) `:81`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo105) `:105`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo121) `:121`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo140) `:140`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo159) `:159`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo179) `:179`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo198) `:198`

- 🔗 [MarshalJSON](#marshaljson-gopkgadktypesgo219) `:219`

- 🔗 [ModelToEmbeddingConfig](#modeltoembeddingconfig-gopkgadktypesgo329) `:329`

- 🔗 [ParseModel](#parsemodel-gopkgadktypesgo234) `:234`

- 🔗 [Scan](#scan-gopkgadktypesgo466) `:466`

- 🔗 [UnmarshalJSON](#unmarshaljson-gopkgadktypesgo307) `:307`

- 🔗 [UnmarshalJSON](#unmarshaljson-gopkgadktypesgo380) `:380`

- 🔗 [UnmarshalJSON](#unmarshaljson-gopkgadktypesgo421) `:421`

- 🔗 [Value](#value-gopkgadktypesgo472) `:472`


</details>


[function] name: GetType file: go/pkg/adk/types.go:93 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:93)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (o *OpenAI) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:93`



---


[function] name: GetType file: go/pkg/adk/types.go:101 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:101)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (a *AzureOpenAI) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:101`



---


[function] name: GetType file: go/pkg/adk/types.go:132 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:132)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (a *Anthropic) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:132`



---


[function] name: GetType file: go/pkg/adk/types.go:151 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:151)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (g *GeminiVertexAI) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:151`



---


[function] name: GetType file: go/pkg/adk/types.go:170 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:170)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (g *GeminiAnthropic) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:170`



---


[function] name: GetType file: go/pkg/adk/types.go:190 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:190)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (o *Ollama) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:190`



---


[function] name: GetType file: go/pkg/adk/types.go:209 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:209)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (g *Gemini) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:209`



---


[function] name: GetType file: go/pkg/adk/types.go:230 returns_error: нет description: —


### GetType (go/pkg/adk/types.go:230)


GetType is a method that retrieves data based on the provided parameters and returns ().


```go
func (b *Bedrock) GetType(()) ()
```


📍 *Расположение:* `go/pkg/adk/types.go:230`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:81 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:81)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (o *OpenAI) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:81`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:105 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:105)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *AzureOpenAI) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:105`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:121 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:121)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *Anthropic) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:121`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:140 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:140)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (g *GeminiVertexAI) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:140`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:159 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:159)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (g *GeminiAnthropic) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:159`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:179 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:179)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (o *Ollama) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:179`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:198 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:198)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (g *Gemini) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:198`



---


[function] name: MarshalJSON file: go/pkg/adk/types.go:219 returns_error: да description: —


### MarshalJSON (go/pkg/adk/types.go:219)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (b *Bedrock) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:219`



---


[function] name: ModelToEmbeddingConfig file: go/pkg/adk/types.go:329 returns_error: нет description: ModelToEmbeddingConfig converts a Model (e.g. from translateModel) to EmbeddingConfig
so serialized AgentConfig has embe


### ModelToEmbeddingConfig (go/pkg/adk/types.go:329)


ModelToEmbeddingConfig converts a Model (e.g. from translateModel) to EmbeddingConfig
so serialized AgentConfig has embedding.provider for Python EmbeddingConfig validation.


```go
func ModelToEmbeddingConfig((m Model)) (m Model)
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


📍 *Расположение:* `go/pkg/adk/types.go:329`



---


[function] name: ParseModel file: go/pkg/adk/types.go:234 returns_error: да description: —


### ParseModel (go/pkg/adk/types.go:234)


ParseModel is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseModel((Model, error)) (Model, error)
```


**Тип ответа:** Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Model`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:234`



---


[function] name: Scan file: go/pkg/adk/types.go:466 returns_error: нет description: —


### Scan (go/pkg/adk/types.go:466)


Scan is a method that performs operations based on the provided parameters and returns (value any).


```go
func (a *AgentConfig) Scan((value any)) (value any)
```


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/adk/types.go:466`



---


[function] name: UnmarshalJSON file: go/pkg/adk/types.go:307 returns_error: нет description: —


### UnmarshalJSON (go/pkg/adk/types.go:307)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (data []byte).


```go
func (e *EmbeddingConfig) UnmarshalJSON((data []byte)) (data []byte)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/adk/types.go:307`



---


[function] name: UnmarshalJSON file: go/pkg/adk/types.go:380 returns_error: нет description: —


### UnmarshalJSON (go/pkg/adk/types.go:380)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (data []byte).


```go
func (c *AgentCompressionConfig) UnmarshalJSON((data []byte)) (data []byte)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/adk/types.go:380`



---


[function] name: UnmarshalJSON file: go/pkg/adk/types.go:421 returns_error: нет description: —


### UnmarshalJSON (go/pkg/adk/types.go:421)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (data []byte).


```go
func (a *AgentConfig) UnmarshalJSON((data []byte)) (data []byte)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/adk/types.go:421`



---


[function] name: Value file: go/pkg/adk/types.go:472 returns_error: да description: —


### Value (go/pkg/adk/types.go:472)


Value is a method that performs operations based on the provided parameters and may return an error.


```go
func (a AgentConfig) Value((driver.Value, error)) (driver.Value, error)
```


**Тип ответа:** driver.Value


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `driver.Value`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/adk/types.go:472`




## go/pkg/app/app.go


📄 Исходный файл: `go/pkg/app/app.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [LoadFromEnv](#loadfromenv-gopkgappappgo185) `:185`

- 🔗 [SetFlags](#setflags-gopkgappappgo134) `:134`

- 🔗 [Start](#start-gopkgappappgo219) `:219`

- 🔗 [Start](#start-gopkgappappgo600) `:600`

- 🔗 [configureNamespaceWatching](#configurenamespacewatching-gopkgappappgo557) `:557`

- 🔗 [filterValidNamespaces](#filtervalidnamespaces-gopkgappappgo574) `:574`

- 🔗 [init](#init-gopkgappappgo89) `:89`


</details>


[function] name: LoadFromEnv file: go/pkg/app/app.go:185 returns_error: нет description: LoadFromEnv loads configuration values from environment variables.
Flag names are converted to uppercase with underscore


### LoadFromEnv (go/pkg/app/app.go:185)


LoadFromEnv loads configuration values from environment variables.
Flag names are converted to uppercase with underscores (e.g., metrics-bind-address -> METRICS_BIND_ADDRESS).


```go
func LoadFromEnv((fs *flag.FlagSet)) (fs *flag.FlagSet)
```


**Тип запроса:** flag.FlagSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flag.FlagSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/app/app.go:185`



---


[function] name: SetFlags file: go/pkg/app/app.go:134 returns_error: нет description: —


### SetFlags (go/pkg/app/app.go:134)


SetFlags is a method that updates data based on the provided parameters and returns (commandLine *flag.FlagSet).


```go
func (cfg *Config) SetFlags((commandLine *flag.FlagSet)) (commandLine *flag.FlagSet)
```


**Тип запроса:** flag.FlagSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** commandLine


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flag.FlagSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/app/app.go:134`



---


[function] name: Start file: go/pkg/app/app.go:219 returns_error: нет description: —


### Start (go/pkg/app/app.go:219)


Start is a function that performs operations based on the provided parameters and returns (getExtensionConfig GetExtensionConfig).


```go
func Start((getExtensionConfig GetExtensionConfig)) (getExtensionConfig GetExtensionConfig)
```


**Тип ответа:** getExtensionConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GetExtensionConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/app/app.go:219`



---


[function] name: Start file: go/pkg/app/app.go:600 returns_error: нет description: —


### Start (go/pkg/app/app.go:600)


Start is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (a *adminServer) Start((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `go/pkg/app/app.go:600`



---


[function] name: configureNamespaceWatching file: go/pkg/app/app.go:557 returns_error: нет description: configureNamespaceWatching sets up the controller manager to watch specific namespaces
based on the provided configurati


### configureNamespaceWatching (go/pkg/app/app.go:557)


configureNamespaceWatching sets up the controller manager to watch specific namespaces
based on the provided configuration. It returns the list of namespaces being watched,
or nil if watching all namespaces.


```go
func configureNamespaceWatching((watchNamespacesList []string)) (watchNamespacesList []string)
```


**Тип ответа:** watchNamespacesList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/app/app.go:557`



---


[function] name: filterValidNamespaces file: go/pkg/app/app.go:574 returns_error: нет description: filterValidNamespaces removes invalid namespace names from the provided list.
A valid namespace must be a valid DNS-1123


### filterValidNamespaces (go/pkg/app/app.go:574)


filterValidNamespaces removes invalid namespace names from the provided list.
A valid namespace must be a valid DNS-1123 label.


```go
func filterValidNamespaces((namespaces []string)) (namespaces []string)
```


**Тип ответа:** namespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/app/app.go:574`



---


[function] name: init file: go/pkg/app/app.go:89 returns_error: нет description: —


### init (go/pkg/app/app.go:89)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/pkg/app/app.go:89`




## go/pkg/auth/auth.go


📄 Исходный файл: `go/pkg/auth/auth.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AuthSessionFrom](#authsessionfrom-gopkgauthauthgo66) `:66`

- 🔗 [AuthSessionTo](#authsessionto-gopkgauthauthgo71) `:71`

- 🔗 [AuthnMiddleware](#authnmiddleware-gopkgauthauthgo75) `:75`


</details>


[function] name: AuthSessionFrom file: go/pkg/auth/auth.go:66 returns_error: нет description: —


### AuthSessionFrom (go/pkg/auth/auth.go:66)


AuthSessionFrom is a function that performs operations based on the provided parameters and returns (Session, bool).


```go
func AuthSessionFrom((Session, bool)) (Session, bool)
```


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


📍 *Расположение:* `go/pkg/auth/auth.go:66`



---


[function] name: AuthSessionTo file: go/pkg/auth/auth.go:71 returns_error: нет description: —


### AuthSessionTo (go/pkg/auth/auth.go:71)


AuthSessionTo is a function that performs operations based on the provided parameters and returns (ctx context.Context, session Session).


```go
func AuthSessionTo((ctx context.Context, session Session)) (ctx context.Context, session Session)
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


📍 *Расположение:* `go/pkg/auth/auth.go:71`



---


[function] name: AuthnMiddleware file: go/pkg/auth/auth.go:75 returns_error: нет description: —


### AuthnMiddleware (go/pkg/auth/auth.go:75)


AuthnMiddleware is a function that performs operations based on the provided parameters and returns (authn AuthProvider).


```go
func AuthnMiddleware((authn AuthProvider)) (authn AuthProvider)
```


**Тип ответа:** authn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AuthProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/auth/auth.go:75`




## go/pkg/client/agent.go


📄 Исходный файл: `go/pkg/client/agent.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [CreateAgent](#createagent-gopkgclientagentgo51) `:51`

- 🔗 [DeleteAgent](#deleteagent-gopkgclientagentgo98) `:98`

- 🔗 [GetAgent](#getagent-gopkgclientagentgo66) `:66`

- 🔗 [ListAgents](#listagents-gopkgclientagentgo31) `:31`

- 🔗 [NewAgentClient](#newagentclient-gopkgclientagentgo26) `:26`

- 🔗 [UpdateAgent](#updateagent-gopkgclientagentgo82) `:82`


</details>


[function] name: CreateAgent file: go/pkg/client/agent.go:51 returns_error: да description: CreateAgent creates a new agent


### CreateAgent (go/pkg/client/agent.go:51)


CreateAgent creates a new agent


```go
func (c *agentClient) CreateAgent((*api.StandardResponse[*v1alpha2.Agent], error)) (*api.StandardResponse[*v1alpha2.Agent], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[*v1alpha2.Agent]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/agent.go:51`



---


[function] name: DeleteAgent file: go/pkg/client/agent.go:98 returns_error: нет description: DeleteAgent deletes a agent


### DeleteAgent (go/pkg/client/agent.go:98)


DeleteAgent deletes a agent


```go
func (c *agentClient) DeleteAgent((ctx context.Context, agentRef string)) (ctx context.Context, agentRef string)
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


**Тип ответа:** agentRef


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/agent.go:98`



---


[function] name: GetAgent file: go/pkg/client/agent.go:66 returns_error: да description: GetAgent retrieves a specific agent


### GetAgent (go/pkg/client/agent.go:66)


GetAgent retrieves a specific agent


```go
func (c *agentClient) GetAgent((*api.StandardResponse[*api.AgentResponse], error)) (*api.StandardResponse[*api.AgentResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.AgentResponse


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


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


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


*Типы возврата:* `*api.StandardResponse[*api.AgentResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/agent.go:66`



---


[function] name: ListAgents file: go/pkg/client/agent.go:31 returns_error: да description: ListAgents lists all agents for a user


### ListAgents (go/pkg/client/agent.go:31)


ListAgents lists all agents for a user


```go
func (c *agentClient) ListAgents((*api.StandardResponse[[]api.AgentResponse], error)) (*api.StandardResponse[[]api.AgentResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


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


*Типы возврата:* `*api.StandardResponse[[]api.AgentResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/agent.go:31`



---


[function] name: NewAgentClient file: go/pkg/client/agent.go:26 returns_error: нет description: NewAgentClient creates a new agent client


### NewAgentClient (go/pkg/client/agent.go:26)


NewAgentClient creates a new agent client


```go
func NewAgentClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/agent.go:26`



---


[function] name: UpdateAgent file: go/pkg/client/agent.go:82 returns_error: да description: UpdateAgent updates an existing agent


### UpdateAgent (go/pkg/client/agent.go:82)


UpdateAgent updates an existing agent


```go
func (c *agentClient) UpdateAgent((*api.StandardResponse[*v1alpha2.Agent], error)) (*api.StandardResponse[*v1alpha2.Agent], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** v1alpha2.Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[*v1alpha2.Agent]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/agent.go:82`




## go/pkg/client/api/types.go


📄 Исходный файл: `go/pkg/client/api/types.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewResponse](#newresponse-gopkgclientapitypesgo16) `:16`


</details>


[function] name: NewResponse file: go/pkg/client/api/types.go:16 returns_error: да description: —


### NewResponse (go/pkg/client/api/types.go:16)


NewResponse is a function that performs operations based on the provided parameters and may return an error.


```go
func NewResponse((data T, message string, error bool)) (data T, message string, error bool)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `data T`, `message string`, `error bool`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/api/types.go:16`




## go/pkg/client/base.go


📄 Исходный файл: `go/pkg/client/base.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [DecodeResponse](#decoderesponse-gopkgclientbasego153) `:153`

- 🔗 [Delete](#delete-gopkgclientbasego149) `:149`

- 🔗 [Error](#error-gopkgclientbasego23) `:23`

- 🔗 [Get](#get-gopkgclientbasego137) `:137`

- 🔗 [GetUserIDOrDefault](#getuseridordefault-gopkgclientbasego159) `:159`

- 🔗 [NewBaseClient](#newbaseclient-gopkgclientbasego52) `:52`

- 🔗 [Post](#post-gopkgclientbasego141) `:141`

- 🔗 [Put](#put-gopkgclientbasego145) `:145`

- 🔗 [WithHTTPClient](#withhttpclient-gopkgclientbasego31) `:31`

- 🔗 [WithUserID](#withuserid-gopkgclientbasego38) `:38`

- 🔗 [addUserID](#adduserid-gopkgclientbasego74) `:74`

- 🔗 [buildURL](#buildurl-gopkgclientbasego70) `:70`

- 🔗 [doRequest](#dorequest-gopkgclientbasego86) `:86`


</details>


[function] name: DecodeResponse file: go/pkg/client/base.go:153 returns_error: нет description: —


### DecodeResponse (go/pkg/client/base.go:153)


DecodeResponse is a function that performs operations based on the provided parameters and returns (resp *http.Response, target any).


```go
func DecodeResponse((resp *http.Response, target any)) (resp *http.Response, target any)
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


**Тип ответа:** resp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** target


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/base.go:153`



---


[function] name: Delete file: go/pkg/client/base.go:149 returns_error: да description: —


### Delete (go/pkg/client/base.go:149)


Delete is a method that deletes data based on the provided parameters and may return an error.


```go
func (c *BaseClient) Delete((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `go/pkg/client/base.go:149`



---


[function] name: Error file: go/pkg/client/base.go:23 returns_error: нет description: —


### Error (go/pkg/client/base.go:23)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e *ClientError) Error(()) ()
```


📍 *Расположение:* `go/pkg/client/base.go:23`



---


[function] name: Get file: go/pkg/client/base.go:137 returns_error: да description: —


### Get (go/pkg/client/base.go:137)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c *BaseClient) Get((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `go/pkg/client/base.go:137`



---


[function] name: GetUserIDOrDefault file: go/pkg/client/base.go:159 returns_error: нет description: GetUserIDOrDefault returns the provided userID or falls back to the client's default


### GetUserIDOrDefault (go/pkg/client/base.go:159)


GetUserIDOrDefault returns the provided userID or falls back to the client's default


```go
func (c *BaseClient) GetUserIDOrDefault((userID string)) (userID string)
```


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/base.go:159`



---


[function] name: NewBaseClient file: go/pkg/client/base.go:52 returns_error: нет description: NewBaseClient creates a new base client with the given configuration


### NewBaseClient (go/pkg/client/base.go:52)


NewBaseClient creates a new base client with the given configuration


```go
func NewBaseClient((baseURL string, options ...ClientOption)) (baseURL string, options ...ClientOption)
```


**Тип ответа:** baseURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ClientOption


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/base.go:52`



---


[function] name: Post file: go/pkg/client/base.go:141 returns_error: да description: —


### Post (go/pkg/client/base.go:141)


Post is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *BaseClient) Post((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `go/pkg/client/base.go:141`



---


[function] name: Put file: go/pkg/client/base.go:145 returns_error: да description: —


### Put (go/pkg/client/base.go:145)


Put is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *BaseClient) Put((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `go/pkg/client/base.go:145`



---


[function] name: WithHTTPClient file: go/pkg/client/base.go:31 returns_error: нет description: WithHTTPClient sets a custom HTTP client


### WithHTTPClient (go/pkg/client/base.go:31)


WithHTTPClient sets a custom HTTP client


```go
func WithHTTPClient((httpClient *http.Client)) (httpClient *http.Client)
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


**Тип ответа:** httpClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `go/pkg/client/base.go:31`



---


[function] name: WithUserID file: go/pkg/client/base.go:38 returns_error: нет description: WithUserID sets a default user ID for requests


### WithUserID (go/pkg/client/base.go:38)


WithUserID sets a default user ID for requests


```go
func WithUserID((userID string)) (userID string)
```


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/base.go:38`



---


[function] name: addUserID file: go/pkg/client/base.go:74 returns_error: нет description: —


### addUserID (go/pkg/client/base.go:74)


addUserID is a method that performs operations based on the provided parameters and returns (req *http.Request, userID string).


```go
func (c *BaseClient) addUserID((req *http.Request, userID string)) (req *http.Request, userID string)
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


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/base.go:74`



---


[function] name: buildURL file: go/pkg/client/base.go:70 returns_error: нет description: HTTP helper methods


### buildURL (go/pkg/client/base.go:70)


HTTP helper methods


```go
func (c *BaseClient) buildURL((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/base.go:70`



---


[function] name: doRequest file: go/pkg/client/base.go:86 returns_error: да description: —


### doRequest (go/pkg/client/base.go:86)


doRequest is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *BaseClient) doRequest((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `go/pkg/client/base.go:86`




## go/pkg/client/clientset.go


📄 Исходный файл: `go/pkg/client/clientset.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [New](#new-gopkgclientclientsetgo22) `:22`


</details>


[function] name: New file: go/pkg/client/clientset.go:22 returns_error: нет description: New creates a new KAgent client set


### New (go/pkg/client/clientset.go:22)


New creates a new KAgent client set


```go
func New((baseURL string, options ...ClientOption)) (baseURL string, options ...ClientOption)
```


**Тип ответа:** baseURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ClientOption


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/clientset.go:22`




## go/pkg/client/feedback.go


📄 Исходный файл: `go/pkg/client/feedback.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [CreateFeedback](#createfeedback-gopkgclientfeedbackgo27) `:27`

- 🔗 [ListFeedback](#listfeedback-gopkgclientfeedbackgo39) `:39`

- 🔗 [NewFeedbackClient](#newfeedbackclient-gopkgclientfeedbackgo22) `:22`


</details>


[function] name: CreateFeedback file: go/pkg/client/feedback.go:27 returns_error: нет description: CreateFeedback creates new feedback


### CreateFeedback (go/pkg/client/feedback.go:27)


CreateFeedback creates new feedback


```go
func (c *feedbackClient) CreateFeedback((ctx context.Context, feedback *api.Feedback, userID string)) (ctx context.Context, feedback *api.Feedback, userID string)
```


**Тип запроса:** api.Feedback


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


**Тип ответа:** feedback


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/feedback.go`


**Тип ответа:** api.Feedback


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


**Тип ответа:** userID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/feedback.go:27`



---


[function] name: ListFeedback file: go/pkg/client/feedback.go:39 returns_error: да description: ListFeedback lists all feedback for a user


### ListFeedback (go/pkg/client/feedback.go:39)


ListFeedback lists all feedback for a user


```go
func (c *feedbackClient) ListFeedback((*api.StandardResponse[[]api.Feedback], error)) (*api.StandardResponse[[]api.Feedback], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.Feedback


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


*Типы возврата:* `*api.StandardResponse[[]api.Feedback]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/feedback.go:39`



---


[function] name: NewFeedbackClient file: go/pkg/client/feedback.go:22 returns_error: нет description: NewFeedbackClient creates a new feedback client


### NewFeedbackClient (go/pkg/client/feedback.go:22)


NewFeedbackClient creates a new feedback client


```go
func NewFeedbackClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/feedback.go:22`




## go/pkg/client/health.go


📄 Исходный файл: `go/pkg/client/health.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Get](#get-gopkgclienthealthgo23) `:23`

- 🔗 [NewHealthClient](#newhealthclient-gopkgclienthealthgo18) `:18`


</details>


[function] name: Get file: go/pkg/client/health.go:23 returns_error: нет description: Health checks if the server is healthy


### Get (go/pkg/client/health.go:23)


Health checks if the server is healthy


```go
func (c *healthClient) Get((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `go/pkg/client/health.go:23`



---


[function] name: NewHealthClient file: go/pkg/client/health.go:18 returns_error: нет description: NewHealthClient creates a new health client


### NewHealthClient (go/pkg/client/health.go:18)


NewHealthClient creates a new health client


```go
func NewHealthClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/health.go:18`




## go/pkg/client/memory.go


📄 Исходный файл: `go/pkg/client/memory.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [CreateMemory](#creatememory-gopkgclientmemorygo46) `:46`

- 🔗 [DeleteMemory](#deletememory-gopkgclientmemorygo93) `:93`

- 🔗 [GetMemory](#getmemory-gopkgclientmemorygo61) `:61`

- 🔗 [ListMemories](#listmemories-gopkgclientmemorygo31) `:31`

- 🔗 [NewMemoryClient](#newmemoryclient-gopkgclientmemorygo26) `:26`

- 🔗 [UpdateMemory](#updatememory-gopkgclientmemorygo77) `:77`


</details>


[function] name: CreateMemory file: go/pkg/client/memory.go:46 returns_error: да description: CreateMemory creates a new memory


### CreateMemory (go/pkg/client/memory.go:46)


CreateMemory creates a new memory


```go
func (c *memoryClient) CreateMemory((*api.StandardResponse[*v1alpha1.Memory], error)) (*api.StandardResponse[*v1alpha1.Memory], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** v1alpha1.Memory


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


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** v1alpha1.Memory


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


*Типы возврата:* `*api.StandardResponse[*v1alpha1.Memory]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/memory.go:46`



---


[function] name: DeleteMemory file: go/pkg/client/memory.go:93 returns_error: нет description: DeleteMemory deletes a memory


### DeleteMemory (go/pkg/client/memory.go:93)


DeleteMemory deletes a memory


```go
func (c *memoryClient) DeleteMemory((ctx context.Context, namespace, memoryName string)) (ctx context.Context, namespace, memoryName string)
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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** memoryName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/memory.go:93`



---


[function] name: GetMemory file: go/pkg/client/memory.go:61 returns_error: да description: GetMemory retrieves a specific memory


### GetMemory (go/pkg/client/memory.go:61)


GetMemory retrieves a specific memory


```go
func (c *memoryClient) GetMemory((*api.StandardResponse[*api.MemoryResponse], error)) (*api.StandardResponse[*api.MemoryResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.MemoryResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "MemoryParams": {}
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.MemoryResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "MemoryParams": {}
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[*api.MemoryResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/memory.go:61`



---


[function] name: ListMemories file: go/pkg/client/memory.go:31 returns_error: да description: ListMemories lists all memories


### ListMemories (go/pkg/client/memory.go:31)


ListMemories lists all memories


```go
func (c *memoryClient) ListMemories((*api.StandardResponse[[]api.MemoryResponse], error)) (*api.StandardResponse[[]api.MemoryResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.MemoryResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "MemoryParams": {}
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[[]api.MemoryResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/memory.go:31`



---


[function] name: NewMemoryClient file: go/pkg/client/memory.go:26 returns_error: нет description: NewMemoryClient creates a new memory client


### NewMemoryClient (go/pkg/client/memory.go:26)


NewMemoryClient creates a new memory client


```go
func NewMemoryClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/memory.go:26`



---


[function] name: UpdateMemory file: go/pkg/client/memory.go:77 returns_error: да description: UpdateMemory updates an existing memory


### UpdateMemory (go/pkg/client/memory.go:77)


UpdateMemory updates an existing memory


```go
func (c *memoryClient) UpdateMemory((*api.StandardResponse[*v1alpha1.Memory], error)) (*api.StandardResponse[*v1alpha1.Memory], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** v1alpha1.Memory


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


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** v1alpha1.Memory


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


*Типы возврата:* `*api.StandardResponse[*v1alpha1.Memory]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/memory.go:77`




## go/pkg/client/model.go


📄 Исходный файл: `go/pkg/client/model.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ListSupportedModels](#listsupportedmodels-gopkgclientmodelgo35) `:35`

- 🔗 [NewModelClient](#newmodelclient-gopkgclientmodelgo30) `:30`


</details>


[function] name: ListSupportedModels file: go/pkg/client/model.go:35 returns_error: да description: ListSupportedModels lists all supported models


### ListSupportedModels (go/pkg/client/model.go:35)


ListSupportedModels lists all supported models


```go
func (c *modelClient) ListSupportedModels((*api.StandardResponse[ProviderModels], error)) (*api.StandardResponse[ProviderModels], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** ProviderModels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[ProviderModels]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/model.go:35`



---


[function] name: NewModelClient file: go/pkg/client/model.go:30 returns_error: нет description: NewModelClient creates a new model client


### NewModelClient (go/pkg/client/model.go:30)


NewModelClient creates a new model client


```go
func NewModelClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/model.go:30`




## go/pkg/client/modelconfig.go


📄 Исходный файл: `go/pkg/client/modelconfig.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [CreateModelConfig](#createmodelconfig-gopkgclientmodelconfiggo62) `:62`

- 🔗 [DeleteModelConfig](#deletemodelconfig-gopkgclientmodelconfiggo93) `:93`

- 🔗 [GetModelConfig](#getmodelconfig-gopkgclientmodelconfiggo46) `:46`

- 🔗 [ListModelConfigs](#listmodelconfigs-gopkgclientmodelconfiggo31) `:31`

- 🔗 [NewModelConfigClient](#newmodelconfigclient-gopkgclientmodelconfiggo26) `:26`

- 🔗 [UpdateModelConfig](#updatemodelconfig-gopkgclientmodelconfiggo77) `:77`


</details>


[function] name: CreateModelConfig file: go/pkg/client/modelconfig.go:62 returns_error: да description: CreateModelConfig creates a new model configuration


### CreateModelConfig (go/pkg/client/modelconfig.go:62)


CreateModelConfig creates a new model configuration


```go
func (c *ModelConfigClient) CreateModelConfig((*api.StandardResponse[*v1alpha2.ModelConfig], error)) (*api.StandardResponse[*v1alpha2.ModelConfig], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** v1alpha2.ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** v1alpha2.ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[*v1alpha2.ModelConfig]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/modelconfig.go:62`



---


[function] name: DeleteModelConfig file: go/pkg/client/modelconfig.go:93 returns_error: нет description: DeleteModelConfig deletes a model configuration


### DeleteModelConfig (go/pkg/client/modelconfig.go:93)


DeleteModelConfig deletes a model configuration


```go
func (c *ModelConfigClient) DeleteModelConfig((ctx context.Context, namespace, configName string)) (ctx context.Context, namespace, configName string)
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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** configName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/modelconfig.go:93`



---


[function] name: GetModelConfig file: go/pkg/client/modelconfig.go:46 returns_error: да description: GetModelConfig retrieves a specific model configuration


### GetModelConfig (go/pkg/client/modelconfig.go:46)


GetModelConfig retrieves a specific model configuration


```go
func (c *ModelConfigClient) GetModelConfig((*api.StandardResponse[*api.ModelConfigResponse], error)) (*api.StandardResponse[*api.ModelConfigResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.ModelConfigResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "Model": "string",
  "APIKeySecret": "string",
  "APIKeySecretKey": "string",
  "ModelParams": {},
  "TLS": null
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.ModelConfigResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "Model": "string",
  "APIKeySecret": "string",
  "APIKeySecretKey": "string",
  "ModelParams": {},
  "TLS": null
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[*api.ModelConfigResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/modelconfig.go:46`



---


[function] name: ListModelConfigs file: go/pkg/client/modelconfig.go:31 returns_error: да description: ListModelConfigs lists all model configurations


### ListModelConfigs (go/pkg/client/modelconfig.go:31)


ListModelConfigs lists all model configurations


```go
func (c *ModelConfigClient) ListModelConfigs((*api.StandardResponse[[]api.ModelConfigResponse], error)) (*api.StandardResponse[[]api.ModelConfigResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.ModelConfigResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "Model": "string",
  "APIKeySecret": "string",
  "APIKeySecretKey": "string",
  "ModelParams": {},
  "TLS": null
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[[]api.ModelConfigResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/modelconfig.go:31`



---


[function] name: NewModelConfigClient file: go/pkg/client/modelconfig.go:26 returns_error: нет description: NewModelConfigClient creates a new model config client


### NewModelConfigClient (go/pkg/client/modelconfig.go:26)


NewModelConfigClient creates a new model config client


```go
func NewModelConfigClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/modelconfig.go:26`



---


[function] name: UpdateModelConfig file: go/pkg/client/modelconfig.go:77 returns_error: да description: UpdateModelConfig updates an existing model configuration


### UpdateModelConfig (go/pkg/client/modelconfig.go:77)


UpdateModelConfig updates an existing model configuration


```go
func (c *ModelConfigClient) UpdateModelConfig((*api.StandardResponse[*api.ModelConfigResponse], error)) (*api.StandardResponse[*api.ModelConfigResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.ModelConfigResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "Model": "string",
  "APIKeySecret": "string",
  "APIKeySecretKey": "string",
  "ModelParams": {},
  "TLS": null
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.ModelConfigResponse


```json
{
  "Ref": "string",
  "ProviderName": "string",
  "Model": "string",
  "APIKeySecret": "string",
  "APIKeySecretKey": "string",
  "ModelParams": {},
  "TLS": null
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[*api.ModelConfigResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/modelconfig.go:77`




## go/pkg/client/modelproviderconfig.go


📄 Исходный файл: `go/pkg/client/modelproviderconfig.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [ListSupportedMemoryProviders](#listsupportedmemoryproviders-gopkgclientmodelproviderconfiggo41) `:41`

- 🔗 [ListSupportedModelProviders](#listsupportedmodelproviders-gopkgclientmodelproviderconfiggo26) `:26`

- 🔗 [NewModelProviderConfigClient](#newmodelproviderconfigclient-gopkgclientmodelproviderconfiggo21) `:21`


</details>


[function] name: ListSupportedMemoryProviders file: go/pkg/client/modelproviderconfig.go:41 returns_error: да description: ListSupportedMemoryProviders lists all supported memory providers


### ListSupportedMemoryProviders (go/pkg/client/modelproviderconfig.go:41)


ListSupportedMemoryProviders lists all supported memory providers


```go
func (c *modelProviderConfigClient) ListSupportedMemoryProviders((*api.StandardResponse[[]api.ProviderInfo], error)) (*api.StandardResponse[[]api.ProviderInfo], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.ProviderInfo


```json
{
  "Name": "string",
  "Type": "string",
  "RequiredParams": [],
  "OptionalParams": []
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[[]api.ProviderInfo]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/modelproviderconfig.go:41`



---


[function] name: ListSupportedModelProviders file: go/pkg/client/modelproviderconfig.go:26 returns_error: да description: ListSupportedModelProviders lists all supported model providers


### ListSupportedModelProviders (go/pkg/client/modelproviderconfig.go:26)


ListSupportedModelProviders lists all supported model providers


```go
func (c *modelProviderConfigClient) ListSupportedModelProviders((*api.StandardResponse[[]api.ProviderInfo], error)) (*api.StandardResponse[[]api.ProviderInfo], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.ProviderInfo


```json
{
  "Name": "string",
  "Type": "string",
  "RequiredParams": [],
  "OptionalParams": []
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[[]api.ProviderInfo]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/modelproviderconfig.go:26`



---


[function] name: NewModelProviderConfigClient file: go/pkg/client/modelproviderconfig.go:21 returns_error: нет description: NewModelProviderConfigClient creates a new model provider config client


### NewModelProviderConfigClient (go/pkg/client/modelproviderconfig.go:21)


NewModelProviderConfigClient creates a new model provider config client


```go
func NewModelProviderConfigClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/modelproviderconfig.go:21`




## go/pkg/client/namespace.go


📄 Исходный файл: `go/pkg/client/namespace.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ListNamespaces](#listnamespaces-gopkgclientnamespacego25) `:25`

- 🔗 [NewNamespaceClient](#newnamespaceclient-gopkgclientnamespacego20) `:20`


</details>


[function] name: ListNamespaces file: go/pkg/client/namespace.go:25 returns_error: да description: ListNamespaces lists all namespaces


### ListNamespaces (go/pkg/client/namespace.go:25)


ListNamespaces lists all namespaces


```go
func (c *namespaceClient) ListNamespaces((*api.StandardResponse[[]api.NamespaceResponse], error)) (*api.StandardResponse[[]api.NamespaceResponse], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.NamespaceResponse


```json
{
  "Name": "string",
  "Status": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[[]api.NamespaceResponse]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/namespace.go:25`



---


[function] name: NewNamespaceClient file: go/pkg/client/namespace.go:20 returns_error: нет description: NewNamespaceClient creates a new namespace client


### NewNamespaceClient (go/pkg/client/namespace.go:20)


NewNamespaceClient creates a new namespace client


```go
func NewNamespaceClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/namespace.go:20`




## go/pkg/client/session.go


📄 Исходный файл: `go/pkg/client/session.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [CreateSession](#createsession-gopkgclientsessiongo51) `:51`

- 🔗 [DeleteSession](#deletesession-gopkgclientsessiongo111) `:111`

- 🔗 [GetSession](#getsession-gopkgclientsessiongo70) `:70`

- 🔗 [ListSessionRuns](#listsessionruns-gopkgclientsessiongo126) `:126`

- 🔗 [ListSessions](#listsessions-gopkgclientsessiongo31) `:31`

- 🔗 [NewSessionClient](#newsessionclient-gopkgclientsessiongo26) `:26`

- 🔗 [UpdateSession](#updatesession-gopkgclientsessiongo91) `:91`


</details>


[function] name: CreateSession file: go/pkg/client/session.go:51 returns_error: да description: CreateSession creates a new session


### CreateSession (go/pkg/client/session.go:51)


CreateSession creates a new session


```go
func (c *sessionClient) CreateSession((*api.StandardResponse[*api.Session], error)) (*api.StandardResponse[*api.Session], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.Session


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


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.Session


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


*Типы возврата:* `*api.StandardResponse[*api.Session]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/session.go:51`



---


[function] name: DeleteSession file: go/pkg/client/session.go:111 returns_error: нет description: DeleteSession deletes a session


### DeleteSession (go/pkg/client/session.go:111)


DeleteSession deletes a session


```go
func (c *sessionClient) DeleteSession((ctx context.Context, sessionName string)) (ctx context.Context, sessionName string)
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


**Тип ответа:** sessionName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/session.go:111`



---


[function] name: GetSession file: go/pkg/client/session.go:70 returns_error: да description: GetSession retrieves a specific session


### GetSession (go/pkg/client/session.go:70)


GetSession retrieves a specific session


```go
func (c *sessionClient) GetSession((*api.StandardResponse[*api.Session], error)) (*api.StandardResponse[*api.Session], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.Session


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


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.Session


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


*Типы возврата:* `*api.StandardResponse[*api.Session]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/session.go:70`



---


[function] name: ListSessionRuns file: go/pkg/client/session.go:126 returns_error: да description: ListSessionRuns lists all runs for a specific session


### ListSessionRuns (go/pkg/client/session.go:126)


ListSessionRuns lists all runs for a specific session


```go
func (c *sessionClient) ListSessionRuns((*api.StandardResponse[any], error)) (*api.StandardResponse[any], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.StandardResponse[any]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/session.go:126`



---


[function] name: ListSessions file: go/pkg/client/session.go:31 returns_error: да description: ListSessions lists all sessions for a user


### ListSessions (go/pkg/client/session.go:31)


ListSessions lists all sessions for a user


```go
func (c *sessionClient) ListSessions((*api.StandardResponse[[]*api.Session], error)) (*api.StandardResponse[[]*api.Session], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.Session


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


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.Session


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


*Типы возврата:* `*api.StandardResponse[[]*api.Session]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/session.go:31`



---


[function] name: NewSessionClient file: go/pkg/client/session.go:26 returns_error: нет description: NewSessionClient creates a new session client


### NewSessionClient (go/pkg/client/session.go:26)


NewSessionClient creates a new session client


```go
func NewSessionClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/session.go:26`



---


[function] name: UpdateSession file: go/pkg/client/session.go:91 returns_error: да description: UpdateSession updates an existing session


### UpdateSession (go/pkg/client/session.go:91)


UpdateSession updates an existing session


```go
func (c *sessionClient) UpdateSession((*api.StandardResponse[*api.Session], error)) (*api.StandardResponse[*api.Session], error)
```


**Тип запроса:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип запроса:** api.Session


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


**Тип ответа:** api.StandardResponse


```json
{
  "Error": false,
  "Data": {},
  "Message": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.Session


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


*Типы возврата:* `*api.StandardResponse[*api.Session]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/session.go:91`




## go/pkg/client/tool.go


📄 Исходный файл: `go/pkg/client/tool.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ListTools](#listtools-gopkgclienttoolgo26) `:26`

- 🔗 [NewToolClient](#newtoolclient-gopkgclienttoolgo21) `:21`


</details>


[function] name: ListTools file: go/pkg/client/tool.go:26 returns_error: да description: ListTools lists all tools for a user


### ListTools (go/pkg/client/tool.go:26)


ListTools lists all tools for a user


```go
func (c *toolClient) ListTools(([]api.Tool, error)) ([]api.Tool, error)
```


**Тип ответа:** api.Tool


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


*Типы возврата:* `[]api.Tool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/tool.go:26`



---


[function] name: NewToolClient file: go/pkg/client/tool.go:21 returns_error: нет description: NewToolClient creates a new tool client


### NewToolClient (go/pkg/client/tool.go:21)


NewToolClient creates a new tool client


```go
func NewToolClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/tool.go:21`




## go/pkg/client/toolserver.go


📄 Исходный файл: `go/pkg/client/toolserver.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [CreateToolServer](#createtoolserver-gopkgclienttoolservergo44) `:44`

- 🔗 [DeleteToolServer](#deletetoolserver-gopkgclienttoolservergo59) `:59`

- 🔗 [ListToolServers](#listtoolservers-gopkgclienttoolservergo29) `:29`

- 🔗 [NewToolServerClient](#newtoolserverclient-gopkgclienttoolservergo24) `:24`


</details>


[function] name: CreateToolServer file: go/pkg/client/toolserver.go:44 returns_error: да description: CreateToolServer creates a new tool server


### CreateToolServer (go/pkg/client/toolserver.go:44)


CreateToolServer creates a new tool server


```go
func (c *ToolServerClient) CreateToolServer((*v1alpha1.ToolServer, error)) (*v1alpha1.ToolServer, error)
```


**Тип запроса:** v1alpha1.ToolServer


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


**Тип ответа:** v1alpha1.ToolServer


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


*Типы возврата:* `*v1alpha1.ToolServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/toolserver.go:44`



---


[function] name: DeleteToolServer file: go/pkg/client/toolserver.go:59 returns_error: нет description: DeleteToolServer deletes a tool server


### DeleteToolServer (go/pkg/client/toolserver.go:59)


DeleteToolServer deletes a tool server


```go
func (c *ToolServerClient) DeleteToolServer((ctx context.Context, namespace, toolServerName string)) (ctx context.Context, namespace, toolServerName string)
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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** toolServerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/client/toolserver.go:59`



---


[function] name: ListToolServers file: go/pkg/client/toolserver.go:29 returns_error: да description: ListToolServers lists all tool servers


### ListToolServers (go/pkg/client/toolserver.go:29)


ListToolServers lists all tool servers


```go
func (c *ToolServerClient) ListToolServers(([]api.ToolServerResponse, error)) ([]api.ToolServerResponse, error)
```


**Тип ответа:** api.ToolServerResponse


```json
{
  "Ref": "string",
  "GroupKind": "string",
  "DiscoveredTools": []
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]api.ToolServerResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/toolserver.go:29`



---


[function] name: NewToolServerClient file: go/pkg/client/toolserver.go:24 returns_error: нет description: NewToolServerClient creates a new tool server client


### NewToolServerClient (go/pkg/client/toolserver.go:24)


NewToolServerClient creates a new tool server client


```go
func NewToolServerClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/toolserver.go:24`




## go/pkg/client/version.go


📄 Исходный файл: `go/pkg/client/version.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetVersion](#getversion-gopkgclientversiongo25) `:25`

- 🔗 [NewVersionClient](#newversionclient-gopkgclientversiongo20) `:20`


</details>


[function] name: GetVersion file: go/pkg/client/version.go:25 returns_error: да description: GetVersion retrieves version information


### GetVersion (go/pkg/client/version.go:25)


GetVersion retrieves version information


```go
func (c *versionClient) GetVersion((*api.VersionResponse, error)) (*api.VersionResponse, error)
```


**Тип запроса:** api.VersionResponse


```json
{
  "KAgentVersion": "string",
  "GitCommit": "string",
  "BuildDate": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Тип ответа:** api.VersionResponse


```json
{
  "KAgentVersion": "string",
  "GitCommit": "string",
  "BuildDate": "string"
}
```


*Определено в:* `go/pkg/client/api/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*api.VersionResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/client/version.go:25`



---


[function] name: NewVersionClient file: go/pkg/client/version.go:20 returns_error: нет description: NewVersionClient creates a new version client


### NewVersionClient (go/pkg/client/version.go:20)


NewVersionClient creates a new version client


```go
func NewVersionClient((client *BaseClient)) (client *BaseClient)
```


**Тип запроса:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** BaseClient


```json
{
  "BaseURL": "string",
  "HTTPClient": null,
  "UserID": "string"
}
```


*Определено в:* `go/pkg/client/base.go`


📍 *Расположение:* `go/pkg/client/version.go:20`




## go/pkg/database/models.go


📄 Исходный файл: `go/pkg/database/models.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [BeforeCreate](#beforecreate-gopkgdatabasemodelsgo224) `:224`

- 🔗 [Parse](#parse-gopkgdatabasemodelsgo39) `:39`

- 🔗 [Parse](#parse-gopkgdatabasemodelsgo80) `:80`

- 🔗 [ParseMessages](#parsemessages-gopkgdatabasemodelsgo48) `:48`

- 🔗 [ParseTasks](#parsetasks-gopkgdatabasemodelsgo89) `:89`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo238) `:238`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo239) `:239`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo240) `:240`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo241) `:241`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo242) `:242`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo243) `:243`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo244) `:244`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo245) `:245`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo246) `:246`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo247) `:247`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo248) `:248`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo249) `:249`

- 🔗 [TableName](#tablename-gopkgdatabasemodelsgo250) `:250`


</details>


[function] name: BeforeCreate file: go/pkg/database/models.go:224 returns_error: нет description: BeforeCreate generates a UUID for the Memory ID if one has not been set,
making ID generation database-agnostic (works f


### BeforeCreate (go/pkg/database/models.go:224)


BeforeCreate generates a UUID for the Memory ID if one has not been set,
making ID generation database-agnostic (works for both Postgres and SQLite).


```go
func (m *Memory) BeforeCreate((tx *gorm.DB)) (tx *gorm.DB)
```


**Тип запроса:** gorm.DB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gorm.DB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/database/models.go:224`



---


[function] name: Parse file: go/pkg/database/models.go:39 returns_error: да description: —


### Parse (go/pkg/database/models.go:39)


Parse is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *Event) Parse((protocol.Message, error)) (protocol.Message, error)
```


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `protocol.Message`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/database/models.go:39`



---


[function] name: Parse file: go/pkg/database/models.go:80 returns_error: да description: —


### Parse (go/pkg/database/models.go:80)


Parse is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *Task) Parse((protocol.Task, error)) (protocol.Task, error)
```


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


*Типы возврата:* `protocol.Task`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/database/models.go:80`



---


[function] name: ParseMessages file: go/pkg/database/models.go:48 returns_error: да description: —


### ParseMessages (go/pkg/database/models.go:48)


ParseMessages is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseMessages(([]*protocol.Message, error)) ([]*protocol.Message, error)
```


**Тип запроса:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*protocol.Message`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/database/models.go:48`



---


[function] name: ParseTasks file: go/pkg/database/models.go:89 returns_error: да description: —


### ParseTasks (go/pkg/database/models.go:89)


ParseTasks is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseTasks(([]*protocol.Task, error)) ([]*protocol.Task, error)
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


📍 *Расположение:* `go/pkg/database/models.go:89`



---


[function] name: TableName file: go/pkg/database/models.go:238 returns_error: нет description: TableName methods to match Python table names


### TableName (go/pkg/database/models.go:238)


TableName methods to match Python table names


```go
func (Agent) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:238`



---


[function] name: TableName file: go/pkg/database/models.go:239 returns_error: нет description: —


### TableName (go/pkg/database/models.go:239)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Event) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:239`



---


[function] name: TableName file: go/pkg/database/models.go:240 returns_error: нет description: —


### TableName (go/pkg/database/models.go:240)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Session) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:240`



---


[function] name: TableName file: go/pkg/database/models.go:241 returns_error: нет description: —


### TableName (go/pkg/database/models.go:241)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Task) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:241`



---


[function] name: TableName file: go/pkg/database/models.go:242 returns_error: нет description: —


### TableName (go/pkg/database/models.go:242)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (PushNotification) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:242`



---


[function] name: TableName file: go/pkg/database/models.go:243 returns_error: нет description: —


### TableName (go/pkg/database/models.go:243)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Feedback) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:243`



---


[function] name: TableName file: go/pkg/database/models.go:244 returns_error: нет description: —


### TableName (go/pkg/database/models.go:244)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Tool) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:244`



---


[function] name: TableName file: go/pkg/database/models.go:245 returns_error: нет description: —


### TableName (go/pkg/database/models.go:245)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (ToolServer) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:245`



---


[function] name: TableName file: go/pkg/database/models.go:246 returns_error: нет description: —


### TableName (go/pkg/database/models.go:246)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (LangGraphCheckpoint) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:246`



---


[function] name: TableName file: go/pkg/database/models.go:247 returns_error: нет description: —


### TableName (go/pkg/database/models.go:247)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (LangGraphCheckpointWrite) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:247`



---


[function] name: TableName file: go/pkg/database/models.go:248 returns_error: нет description: —


### TableName (go/pkg/database/models.go:248)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (CrewAIAgentMemory) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:248`



---


[function] name: TableName file: go/pkg/database/models.go:249 returns_error: нет description: —


### TableName (go/pkg/database/models.go:249)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (CrewAIFlowState) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:249`



---


[function] name: TableName file: go/pkg/database/models.go:250 returns_error: нет description: —


### TableName (go/pkg/database/models.go:250)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Memory) TableName(()) ()
```


📍 *Расположение:* `go/pkg/database/models.go:250`




## go/pkg/env/var.go


📄 Исходный файл: `go/pkg/env/var.go`


<details open>
<summary><b>Функции в этом файле (24)</b></summary>


- 🔗 [DefaultValue](#defaultvalue-gopkgenvvargo160) `:160`

- 🔗 [ExportJSON](#exportjson-gopkgenvvargo360) `:360`

- 🔗 [ExportMarkdown](#exportmarkdown-gopkgenvvargo309) `:309`

- 🔗 [Get](#get-gopkgenvvargo140) `:140`

- 🔗 [Get](#get-gopkgenvvargo184) `:184`

- 🔗 [Get](#get-gopkgenvvargo232) `:232`

- 🔗 [Get](#get-gopkgenvvargo280) `:280`

- 🔗 [Lookup](#lookup-gopkgenvvargo148) `:148`

- 🔗 [Lookup](#lookup-gopkgenvvargo195) `:195`

- 🔗 [Lookup](#lookup-gopkgenvvargo243) `:243`

- 🔗 [Lookup](#lookup-gopkgenvvargo291) `:291`

- 🔗 [MarshalJSON](#marshaljson-gopkgenvvargo52) `:52`

- 🔗 [Name](#name-gopkgenvvargo157) `:157`

- 🔗 [Name](#name-gopkgenvvargo208) `:208`

- 🔗 [Name](#name-gopkgenvvargo256) `:256`

- 🔗 [Name](#name-gopkgenvvargo304) `:304`

- 🔗 [RegisterBoolVar](#registerboolvar-gopkgenvvargo171) `:171`

- 🔗 [RegisterDurationVar](#registerdurationvar-gopkgenvvargo267) `:267`

- 🔗 [RegisterIntVar](#registerintvar-gopkgenvvargo219) `:219`

- 🔗 [RegisterStringVar](#registerstringvar-gopkgenvvargo127) `:127`

- 🔗 [String](#string-gopkgenvvargo34) `:34`

- 🔗 [VarByName](#varbyname-gopkgenvvargo112) `:112`

- 🔗 [VarDescriptions](#vardescriptions-gopkgenvvargo97) `:97`

- 🔗 [register](#register-gopkgenvvargo90) `:90`


</details>


[function] name: DefaultValue file: go/pkg/env/var.go:160 returns_error: нет description: DefaultValue returns the default value.


### DefaultValue (go/pkg/env/var.go:160)


DefaultValue returns the default value.


```go
func (s StringVar) DefaultValue(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:160`



---


[function] name: ExportJSON file: go/pkg/env/var.go:360 returns_error: нет description: ExportJSON generates a JSON array of all registered variables.


### ExportJSON (go/pkg/env/var.go:360)


ExportJSON generates a JSON array of all registered variables.


```go
func ExportJSON((component string)) (component string)
```


**Тип ответа:** component


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/env/var.go:360`



---


[function] name: ExportMarkdown file: go/pkg/env/var.go:309 returns_error: нет description: ExportMarkdown generates a markdown document listing all registered variables.


### ExportMarkdown (go/pkg/env/var.go:309)


ExportMarkdown generates a markdown document listing all registered variables.


```go
func ExportMarkdown((component string)) (component string)
```


**Тип ответа:** component


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/env/var.go:309`



---


[function] name: Get file: go/pkg/env/var.go:140 returns_error: нет description: Get returns the current value of the environment variable, or the default.


### Get (go/pkg/env/var.go:140)


Get returns the current value of the environment variable, or the default.


```go
func (s StringVar) Get(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:140`



---


[function] name: Get file: go/pkg/env/var.go:184 returns_error: нет description: Get returns the current value of the environment variable, or the default.


### Get (go/pkg/env/var.go:184)


Get returns the current value of the environment variable, or the default.


```go
func (b BoolVar) Get(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:184`



---


[function] name: Get file: go/pkg/env/var.go:232 returns_error: нет description: Get returns the current value of the environment variable, or the default.


### Get (go/pkg/env/var.go:232)


Get returns the current value of the environment variable, or the default.


```go
func (i IntVar) Get(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:232`



---


[function] name: Get file: go/pkg/env/var.go:280 returns_error: нет description: Get returns the current value of the environment variable, or the default.


### Get (go/pkg/env/var.go:280)


Get returns the current value of the environment variable, or the default.


```go
func (d DurationVar) Get(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:280`



---


[function] name: Lookup file: go/pkg/env/var.go:148 returns_error: нет description: Lookup returns the value and whether the variable was set.


### Lookup (go/pkg/env/var.go:148)


Lookup returns the value and whether the variable was set.


```go
func (s StringVar) Lookup((string, bool)) (string, bool)
```


📍 *Расположение:* `go/pkg/env/var.go:148`



---


[function] name: Lookup file: go/pkg/env/var.go:195 returns_error: нет description: Lookup returns the value and whether the variable was set.


### Lookup (go/pkg/env/var.go:195)


Lookup returns the value and whether the variable was set.


```go
func (b BoolVar) Lookup((bool, bool)) (bool, bool)
```


📍 *Расположение:* `go/pkg/env/var.go:195`



---


[function] name: Lookup file: go/pkg/env/var.go:243 returns_error: нет description: Lookup returns the value and whether the variable was set.


### Lookup (go/pkg/env/var.go:243)


Lookup returns the value and whether the variable was set.


```go
func (i IntVar) Lookup((int, bool)) (int, bool)
```


📍 *Расположение:* `go/pkg/env/var.go:243`



---


[function] name: Lookup file: go/pkg/env/var.go:291 returns_error: нет description: Lookup returns the value and whether the variable was set.


### Lookup (go/pkg/env/var.go:291)


Lookup returns the value and whether the variable was set.


```go
func (d DurationVar) Lookup((time.Duration, bool)) (time.Duration, bool)
```


**Тип ответа:** time.Duration


```json
{
  "v": {},
  "defaultValue": {}
}
```


*Определено в:* `go/pkg/env/var.go`


📍 *Расположение:* `go/pkg/env/var.go:291`



---


[function] name: MarshalJSON file: go/pkg/env/var.go:52 returns_error: да description: MarshalJSON serializes VarType as its string representation.


### MarshalJSON (go/pkg/env/var.go:52)


MarshalJSON serializes VarType as its string representation.


```go
func (v VarType) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/pkg/env/var.go:52`



---


[function] name: Name file: go/pkg/env/var.go:157 returns_error: нет description: Name returns the environment variable name.


### Name (go/pkg/env/var.go:157)


Name returns the environment variable name.


```go
func (s StringVar) Name(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:157`



---


[function] name: Name file: go/pkg/env/var.go:208 returns_error: нет description: Name returns the environment variable name.


### Name (go/pkg/env/var.go:208)


Name returns the environment variable name.


```go
func (b BoolVar) Name(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:208`



---


[function] name: Name file: go/pkg/env/var.go:256 returns_error: нет description: Name returns the environment variable name.


### Name (go/pkg/env/var.go:256)


Name returns the environment variable name.


```go
func (i IntVar) Name(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:256`



---


[function] name: Name file: go/pkg/env/var.go:304 returns_error: нет description: Name returns the environment variable name.


### Name (go/pkg/env/var.go:304)


Name returns the environment variable name.


```go
func (d DurationVar) Name(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:304`



---


[function] name: RegisterBoolVar file: go/pkg/env/var.go:171 returns_error: нет description: RegisterBoolVar registers a boolean environment variable and returns a typed accessor.


### RegisterBoolVar (go/pkg/env/var.go:171)


RegisterBoolVar registers a boolean environment variable and returns a typed accessor.


```go
func RegisterBoolVar((name string, defaultValue bool, description string, component Component)) (name string, defaultValue bool, description string, component Component)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** defaultValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** component


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Component


```json
{
  "Provider": "string",
  "ComponentType": "string",
  "Version": 0,
  "ComponentVersion": 0,
  "Description": "string",
  "Label": "string",
  "Config": {}
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/pkg/env/var.go:171`



---


[function] name: RegisterDurationVar file: go/pkg/env/var.go:267 returns_error: нет description: RegisterDurationVar registers a duration environment variable and returns a typed accessor.


### RegisterDurationVar (go/pkg/env/var.go:267)


RegisterDurationVar registers a duration environment variable and returns a typed accessor.


```go
func RegisterDurationVar((name string, defaultValue time.Duration, description string, component Component)) (name string, defaultValue time.Duration, description string, component Component)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** defaultValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "v": {},
  "defaultValue": {}
}
```


*Определено в:* `go/pkg/env/var.go`


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** component


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Component


```json
{
  "Provider": "string",
  "ComponentType": "string",
  "Version": 0,
  "ComponentVersion": 0,
  "Description": "string",
  "Label": "string",
  "Config": {}
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/pkg/env/var.go:267`



---


[function] name: RegisterIntVar file: go/pkg/env/var.go:219 returns_error: нет description: RegisterIntVar registers an integer environment variable and returns a typed accessor.


### RegisterIntVar (go/pkg/env/var.go:219)


RegisterIntVar registers an integer environment variable and returns a typed accessor.


```go
func RegisterIntVar((name string, defaultValue int, description string, component Component)) (name string, defaultValue int, description string, component Component)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** defaultValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** component


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Component


```json
{
  "Provider": "string",
  "ComponentType": "string",
  "Version": 0,
  "ComponentVersion": 0,
  "Description": "string",
  "Label": "string",
  "Config": {}
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/pkg/env/var.go:219`



---


[function] name: RegisterStringVar file: go/pkg/env/var.go:127 returns_error: нет description: RegisterStringVar registers a string environment variable and returns a typed accessor.


### RegisterStringVar (go/pkg/env/var.go:127)


RegisterStringVar registers a string environment variable and returns a typed accessor.


```go
func RegisterStringVar((name, defaultValue, description string, component Component)) (name, defaultValue, description string, component Component)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** defaultValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** component


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Component


```json
{
  "Provider": "string",
  "ComponentType": "string",
  "Version": 0,
  "ComponentVersion": 0,
  "Description": "string",
  "Label": "string",
  "Config": {}
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/pkg/env/var.go:127`



---


[function] name: String file: go/pkg/env/var.go:34 returns_error: нет description: String returns the human-readable name of a VarType.


### String (go/pkg/env/var.go:34)


String returns the human-readable name of a VarType.


```go
func (v VarType) String(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:34`



---


[function] name: VarByName file: go/pkg/env/var.go:112 returns_error: нет description: VarByName returns the metadata for a registered variable, or false if not found.


### VarByName (go/pkg/env/var.go:112)


VarByName returns the metadata for a registered variable, or false if not found.


```go
func VarByName((Var, bool)) (Var, bool)
```


**Тип ответа:** Var


```json
{
  "Name": "string",
  "DefaultValue": "string",
  "Description": "string",
  "Type": {},
  "Component": {},
  "Hidden": false,
  "Deprecated": false
}
```


*Определено в:* `go/pkg/env/var.go`


📍 *Расположение:* `go/pkg/env/var.go:112`



---


[function] name: VarDescriptions file: go/pkg/env/var.go:97 returns_error: нет description: VarDescriptions returns all registered variables sorted by name.


### VarDescriptions (go/pkg/env/var.go:97)


VarDescriptions returns all registered variables sorted by name.


```go
func VarDescriptions(()) ()
```


📍 *Расположение:* `go/pkg/env/var.go:97`



---


[function] name: register file: go/pkg/env/var.go:90 returns_error: нет description: —


### register (go/pkg/env/var.go:90)


register is a function that performs operations based on the provided parameters and returns (v Var).


```go
func register((v Var)) (v Var)
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


**Тип ответа:** Var


```json
{
  "Name": "string",
  "DefaultValue": "string",
  "Description": "string",
  "Type": {},
  "Component": {},
  "Hidden": false,
  "Deprecated": false
}
```


*Определено в:* `go/pkg/env/var.go`


📍 *Расположение:* `go/pkg/env/var.go:90`




## go/pkg/utils/utils.go


📄 Исходный файл: `go/pkg/utils/utils.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetMetadataValue](#getmetadatavalue-gopkgutilsutilsgo7) `:7`


</details>


[function] name: GetMetadataValue file: go/pkg/utils/utils.go:7 returns_error: нет description: GetMetadataValue looks up an unprefixed key in A2A metadata, checking
"adk_<key>" first then falling back to "kagent_<ke


### GetMetadataValue (go/pkg/utils/utils.go:7)


GetMetadataValue looks up an unprefixed key in A2A metadata, checking
"adk_<key>" first then falling back to "kagent_<key>".  This allows
interoperability with upstream ADK (adk_ prefix) while preserving
backward-compatibility with kagent's own kagent_ prefix.


```go
func GetMetadataValue((any, bool)) (any, bool)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/pkg/utils/utils.go:7`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_internal.md)

- [Следующая директория](go_test.md)


---

