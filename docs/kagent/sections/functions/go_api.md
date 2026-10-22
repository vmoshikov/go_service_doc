---
title: "Функции: go/api"
type: functions
repo: kagent
language: ru
chunk_boundary: h3
group: go/api
---


# Функции: go/api


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](contrib_go-adk.md)

- [Следующая директория](go_cli.md)


---


## Меню по файлам


- 📄 [go/api/v1alpha1/agent_types.go](#goapiv1alpha1agent_typesgo)

- 📄 [go/api/v1alpha1/memory_types.go](#goapiv1alpha1memory_typesgo)

- 📄 [go/api/v1alpha1/modelconfig_types.go](#goapiv1alpha1modelconfig_typesgo)

- 📄 [go/api/v1alpha1/toolserver_types.go](#goapiv1alpha1toolserver_typesgo)

- 📄 [go/api/v1alpha1/zz_generated.deepcopy.go](#goapiv1alpha1zz_generateddeepcopygo)

- 📄 [go/api/v1alpha2/agent_types.go](#goapiv1alpha2agent_typesgo)

- 📄 [go/api/v1alpha2/common_types.go](#goapiv1alpha2common_typesgo)

- 📄 [go/api/v1alpha2/modelconfig_types.go](#goapiv1alpha2modelconfig_typesgo)

- 📄 [go/api/v1alpha2/modelproviderconfig_types.go](#goapiv1alpha2modelproviderconfig_typesgo)

- 📄 [go/api/v1alpha2/remotemcpserver_types.go](#goapiv1alpha2remotemcpserver_typesgo)

- 📄 [go/api/v1alpha2/zz_generated.deepcopy.go](#goapiv1alpha2zz_generateddeepcopygo)


---


## go/api/v1alpha1/agent_types.go


📄 Исходный файл: `go/api/v1alpha1/agent_types.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-goapiv1alpha1agent_typesgo165) `:165`


</details>


[function] name: init file: go/api/v1alpha1/agent_types.go:165 returns_error: нет description: —


### init (go/api/v1alpha1/agent_types.go:165)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/agent_types.go:165`




## go/api/v1alpha1/memory_types.go


📄 Исходный файл: `go/api/v1alpha1/memory_types.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-goapiv1alpha1memory_typesgo103) `:103`


</details>


[function] name: init file: go/api/v1alpha1/memory_types.go:103 returns_error: нет description: —


### init (go/api/v1alpha1/memory_types.go:103)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/memory_types.go:103`




## go/api/v1alpha1/modelconfig_types.go


📄 Исходный файл: `go/api/v1alpha1/modelconfig_types.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-goapiv1alpha1modelconfig_typesgo315) `:315`


</details>


[function] name: init file: go/api/v1alpha1/modelconfig_types.go:315 returns_error: нет description: —


### init (go/api/v1alpha1/modelconfig_types.go:315)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/modelconfig_types.go:315`




## go/api/v1alpha1/toolserver_types.go


📄 Исходный файл: `go/api/v1alpha1/toolserver_types.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Scan](#scan-goapiv1alpha1toolserver_typesgo53) `:53`

- 🔗 [Value](#value-goapiv1alpha1toolserver_typesgo63) `:63`

- 🔗 [init](#init-goapiv1alpha1toolserver_typesgo178) `:178`


</details>


[function] name: Scan file: go/api/v1alpha1/toolserver_types.go:53 returns_error: нет description: —


### Scan (go/api/v1alpha1/toolserver_types.go:53)


Scan is a method that performs operations based on the provided parameters and returns (src any).


```go
func (t *ToolServerConfig) Scan((src any)) (src any)
```


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha1/toolserver_types.go:53`



---


[function] name: Value file: go/api/v1alpha1/toolserver_types.go:63 returns_error: да description: —


### Value (go/api/v1alpha1/toolserver_types.go:63)


Value is a method that performs operations based on the provided parameters and may return an error.


```go
func (t ToolServerConfig) Value((driver.Value, error)) (driver.Value, error)
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


📍 *Расположение:* `go/api/v1alpha1/toolserver_types.go:63`



---


[function] name: init file: go/api/v1alpha1/toolserver_types.go:178 returns_error: нет description: —


### init (go/api/v1alpha1/toolserver_types.go:178)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/toolserver_types.go:178`




## go/api/v1alpha1/zz_generated.deepcopy.go


📄 Исходный файл: `go/api/v1alpha1/zz_generated.deepcopy.go`


<details open>
<summary><b>Функции в этом файле (92)</b></summary>


- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo43) `:43`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo62) `:62`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo94) `:94`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo142) `:142`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo188) `:188`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo215) `:215`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo230) `:230`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo245) `:245`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo261) `:261`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo281) `:281`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo301) `:301`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo321) `:321`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo343) `:343`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo396) `:396`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo411) `:411`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo427) `:427`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo466) `:466`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo486) `:486`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo506) `:506`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo525) `:525`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo557) `:557`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo585) `:585`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo607) `:607`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo626) `:626`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo658) `:658`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo728) `:728`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo750) `:750`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo765) `:765`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo787) `:787`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo817) `:817`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo837) `:837`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo853) `:853`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo887) `:887`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo908) `:908`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo933) `:933`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo952) `:952`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo990) `:990`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo1014) `:1014`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo1038) `:1038`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo1071) `:1071`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo1091) `:1091`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha1zz_generateddeepcopygo1106) `:1106`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo31) `:31`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo53) `:53`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo80) `:80`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo112) `:112`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo152) `:152`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo198) `:198`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo225) `:225`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo240) `:240`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo255) `:255`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo271) `:271`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo291) `:291`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo311) `:311`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo331) `:331`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo353) `:353`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo406) `:406`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo421) `:421`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo437) `:437`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo476) `:476`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo496) `:496`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo516) `:516`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo543) `:543`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo575) `:575`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo595) `:595`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo617) `:617`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo644) `:644`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo676) `:676`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo738) `:738`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo760) `:760`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo775) `:775`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo797) `:797`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo827) `:827`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo847) `:847`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo863) `:863`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo897) `:897`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo918) `:918`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo943) `:943`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo970) `:970`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo1000) `:1000`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo1032) `:1032`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo1048) `:1048`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo1081) `:1081`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha1zz_generateddeepcopygo1101) `:1101`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo72) `:72`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo104) `:104`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo535) `:535`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo567) `:567`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo636) `:636`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo668) `:668`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo962) `:962`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha1zz_generateddeepcopygo1024) `:1024`


</details>


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:43 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new A2AConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:43)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new A2AConfig.


```go
func (in *A2AConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:43`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:62 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Agent.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:62)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Agent.


```go
func (in *Agent) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:62`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:94 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentList.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:94)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentList.


```go
func (in *AgentList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:94`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:142 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSkill.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:142)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSkill.


```go
func (in *AgentSkill) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:142`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:188 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSpec.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:188)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSpec.


```go
func (in *AgentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:188`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:215 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentStatus.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:215)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentStatus.


```go
func (in *AgentStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:215`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:230 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentTool.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:230)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentTool.


```go
func (in *AgentTool) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:230`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:245 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:245)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicConfig.


```go
func (in *AnthropicConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:245`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:261 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicVertexAIConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:261)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicVertexAIConfig.


```go
func (in *AnthropicVertexAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:261`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:281 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnyType.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:281)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnyType.


```go
func (in *AnyType) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:281`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:301 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AzureOpenAIConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:301)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AzureOpenAIConfig.


```go
func (in *AzureOpenAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:301`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:321 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BaseVertexAIConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:321)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BaseVertexAIConfig.


```go
func (in *BaseVertexAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:321`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:343 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Component.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:343)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Component.


```go
func (in *Component) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:343`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:396 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DeploymentSpec.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:396)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DeploymentSpec.


```go
func (in *DeploymentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:396`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:411 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:411)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiConfig.


```go
func (in *GeminiConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:411`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:427 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiVertexAIConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:427)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiVertexAIConfig.


```go
func (in *GeminiVertexAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:427`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:466 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new HttpToolServerConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:466)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new HttpToolServerConfig.


```go
func (in *HttpToolServerConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:466`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:486 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MCPTool.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:486)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MCPTool.


```go
func (in *MCPTool) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:486`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:506 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new McpServerTool.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:506)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new McpServerTool.


```go
func (in *McpServerTool) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:506`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:525 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Memory.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:525)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Memory.


```go
func (in *Memory) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:525`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:557 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemoryList.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:557)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemoryList.


```go
func (in *MemoryList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:557`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:585 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemorySpec.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:585)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemorySpec.


```go
func (in *MemorySpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:585`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:607 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemoryStatus.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:607)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemoryStatus.


```go
func (in *MemoryStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:607`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:626 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:626)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfig.


```go
func (in *ModelConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:626`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:658 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigList.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:658)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigList.


```go
func (in *ModelConfigList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:658`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:728 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigSpec.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:728)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigSpec.


```go
func (in *ModelConfigSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:728`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:750 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigStatus.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:750)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigStatus.


```go
func (in *ModelConfigStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:750`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:765 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelInfo.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:765)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelInfo.


```go
func (in *ModelInfo) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:765`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:787 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OllamaConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:787)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OllamaConfig.


```go
func (in *OllamaConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:787`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:817 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OpenAIConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:817)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OpenAIConfig.


```go
func (in *OpenAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:817`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:837 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new PineconeConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:837)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new PineconeConfig.


```go
func (in *PineconeConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:837`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:853 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SseMcpServerConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:853)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SseMcpServerConfig.


```go
func (in *SseMcpServerConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:853`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:887 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new StdioMcpServerConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:887)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new StdioMcpServerConfig.


```go
func (in *StdioMcpServerConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:887`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:908 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new StreamableHttpServerConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:908)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new StreamableHttpServerConfig.


```go
func (in *StreamableHttpServerConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:908`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:933 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Tool.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:933)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Tool.


```go
func (in *Tool) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:933`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:952 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServer.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:952)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServer.


```go
func (in *ToolServer) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:952`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:990 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerConfig.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:990)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerConfig.


```go
func (in *ToolServerConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:990`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:1014 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerList.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:1014)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerList.


```go
func (in *ToolServerList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1014`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:1038 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerSpec.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:1038)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerSpec.


```go
func (in *ToolServerSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1038`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:1071 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerStatus.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:1071)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ToolServerStatus.


```go
func (in *ToolServerStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1071`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:1091 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueRef.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:1091)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueRef.


```go
func (in *ValueRef) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1091`



---


[function] name: DeepCopy file: go/api/v1alpha1/zz_generated.deepcopy.go:1106 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueSource.


### DeepCopy (go/api/v1alpha1/zz_generated.deepcopy.go:1106)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueSource.


```go
func (in *ValueSource) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1106`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:31 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:31)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *A2AConfig) DeepCopyInto((out *A2AConfig)) (out *A2AConfig)
```


**Тип запроса:** A2AConfig


```json
{
  "Skills": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** A2AConfig


```json
{
  "Skills": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:31`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:53 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:53)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Agent) DeepCopyInto((out *Agent)) (out *Agent)
```


**Тип запроса:** Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:53`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:80 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:80)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentList) DeepCopyInto((out *AgentList)) (out *AgentList)
```


**Тип запроса:** AgentList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:80`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:112 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:112)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentSkill) DeepCopyInto((out *AgentSkill)) (out *AgentSkill)
```


**Тип запроса:** AgentSkill


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentSkill


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:112`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:152 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:152)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentSpec) DeepCopyInto((out *AgentSpec)) (out *AgentSpec)
```


**Тип запроса:** AgentSpec


```json
{
  "Description": "string",
  "SystemMessage": "string",
  "ModelConfig": "string",
  "Stream": false,
  "Tools": [],
  "Memory": [],
  "A2AConfig": null,
  "Deployment": null
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentSpec


```json
{
  "Description": "string",
  "SystemMessage": "string",
  "ModelConfig": "string",
  "Stream": false,
  "Tools": [],
  "Memory": [],
  "A2AConfig": null,
  "Deployment": null
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:152`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:198 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:198)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentStatus) DeepCopyInto((out *AgentStatus)) (out *AgentStatus)
```


**Тип запроса:** AgentStatus


```json
{
  "ObservedGeneration": 0,
  "ConfigHash": [],
  "Conditions": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentStatus


```json
{
  "ObservedGeneration": 0,
  "ConfigHash": [],
  "Conditions": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:198`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:225 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:225)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentTool) DeepCopyInto((out *AgentTool)) (out *AgentTool)
```


**Тип запроса:** AgentTool


```json
{
  "Ref": "string"
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentTool


```json
{
  "Ref": "string"
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:225`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:240 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:240)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AnthropicConfig) DeepCopyInto((out *AnthropicConfig)) (out *AnthropicConfig)
```


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


**Тип ответа:** out


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


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:240`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:255 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:255)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AnthropicVertexAIConfig) DeepCopyInto((out *AnthropicVertexAIConfig)) (out *AnthropicVertexAIConfig)
```


**Тип запроса:** AnthropicVertexAIConfig


```json
{
  "MaxTokens": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AnthropicVertexAIConfig


```json
{
  "MaxTokens": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:255`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:271 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:271)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AnyType) DeepCopyInto((out *AnyType)) (out *AnyType)
```


**Тип запроса:** AnyType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AnyType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:271`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:291 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:291)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AzureOpenAIConfig) DeepCopyInto((out *AzureOpenAIConfig)) (out *AzureOpenAIConfig)
```


**Тип запроса:** AzureOpenAIConfig


```json
{
  "Model": "string",
  "Headers": {},
  "Timeout": 0
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AzureOpenAIConfig


```json
{
  "Model": "string",
  "Headers": {},
  "Timeout": 0
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:291`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:311 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:311)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *BaseVertexAIConfig) DeepCopyInto((out *BaseVertexAIConfig)) (out *BaseVertexAIConfig)
```


**Тип запроса:** BaseVertexAIConfig


```json
{
  "ProjectID": "string",
  "Location": "string",
  "Temperature": "string",
  "TopP": "string",
  "TopK": "string",
  "StopSequences": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BaseVertexAIConfig


```json
{
  "ProjectID": "string",
  "Location": "string",
  "Temperature": "string",
  "TopP": "string",
  "TopK": "string",
  "StopSequences": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:311`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:331 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:331)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Component) DeepCopyInto((out *Component)) (out *Component)
```


**Тип запроса:** Component


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


**Тип ответа:** out


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


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:331`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:353 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:353)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *DeploymentSpec) DeepCopyInto((out *DeploymentSpec)) (out *DeploymentSpec)
```


**Тип запроса:** DeploymentSpec


```json
{
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "Labels": {},
  "Annotations": {},
  "Env": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeploymentSpec


```json
{
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "Labels": {},
  "Annotations": {},
  "Env": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:353`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:406 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:406)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *GeminiConfig) DeepCopyInto((out *GeminiConfig)) (out *GeminiConfig)
```


**Тип запроса:** GeminiConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GeminiConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:406`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:421 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:421)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *GeminiVertexAIConfig) DeepCopyInto((out *GeminiVertexAIConfig)) (out *GeminiVertexAIConfig)
```


**Тип запроса:** GeminiVertexAIConfig


```json
{
  "MaxOutputTokens": 0,
  "CandidateCount": 0,
  "ResponseMimeType": "string"
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GeminiVertexAIConfig


```json
{
  "MaxOutputTokens": 0,
  "CandidateCount": 0,
  "ResponseMimeType": "string"
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:421`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:437 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:437)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *HttpToolServerConfig) DeepCopyInto((out *HttpToolServerConfig)) (out *HttpToolServerConfig)
```


**Тип запроса:** HttpToolServerConfig


```json
{
  "URL": "string",
  "Headers": {},
  "HeadersFrom": [],
  "Timeout": null,
  "SseReadTimeout": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** HttpToolServerConfig


```json
{
  "URL": "string",
  "Headers": {},
  "HeadersFrom": [],
  "Timeout": null,
  "SseReadTimeout": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:437`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:476 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:476)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *MCPTool) DeepCopyInto((out *MCPTool)) (out *MCPTool)
```


**Тип запроса:** MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:476`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:496 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:496)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *McpServerTool) DeepCopyInto((out *McpServerTool)) (out *McpServerTool)
```


**Тип запроса:** McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:496`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:516 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:516)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Memory) DeepCopyInto((out *Memory)) (out *Memory)
```


**Тип запроса:** Memory


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


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Memory


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


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:516`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:543 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:543)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *MemoryList) DeepCopyInto((out *MemoryList)) (out *MemoryList)
```


**Тип запроса:** MemoryList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MemoryList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:543`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:575 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:575)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *MemorySpec) DeepCopyInto((out *MemorySpec)) (out *MemorySpec)
```


**Тип запроса:** MemorySpec


```json
{
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "Pinecone": null
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MemorySpec


```json
{
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "Pinecone": null
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:575`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:595 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:595)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *MemoryStatus) DeepCopyInto((out *MemoryStatus)) (out *MemoryStatus)
```


**Тип запроса:** MemoryStatus


```json
{
  "Conditions": [],
  "ObservedGeneration": 0
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MemoryStatus


```json
{
  "Conditions": [],
  "ObservedGeneration": 0
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:595`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:617 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:617)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfig) DeepCopyInto((out *ModelConfig)) (out *ModelConfig)
```


**Тип запроса:** ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:617`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:644 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:644)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfigList) DeepCopyInto((out *ModelConfigList)) (out *ModelConfigList)
```


**Тип запроса:** ModelConfigList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfigList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:644`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:676 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:676)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfigSpec) DeepCopyInto((out *ModelConfigSpec)) (out *ModelConfigSpec)
```


**Тип запроса:** ModelConfigSpec


```json
{
  "Model": "string",
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "DefaultHeaders": {},
  "ModelInfo": null,
  "OpenAI": null,
  "Anthropic": null,
  "AzureOpenAI": null,
  "Ollama": null,
  "Gemini": null,
  "GeminiVertexAI": null,
  "AnthropicVertexAI": null
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfigSpec


```json
{
  "Model": "string",
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "DefaultHeaders": {},
  "ModelInfo": null,
  "OpenAI": null,
  "Anthropic": null,
  "AzureOpenAI": null,
  "Ollama": null,
  "Gemini": null,
  "GeminiVertexAI": null,
  "AnthropicVertexAI": null
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:676`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:738 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:738)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfigStatus) DeepCopyInto((out *ModelConfigStatus)) (out *ModelConfigStatus)
```


**Тип запроса:** ModelConfigStatus


```json
{
  "Conditions": [],
  "ObservedGeneration": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfigStatus


```json
{
  "Conditions": [],
  "ObservedGeneration": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:738`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:760 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:760)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelInfo) DeepCopyInto((out *ModelInfo)) (out *ModelInfo)
```


**Тип запроса:** ModelInfo


```json
{
  "Name": "string",
  "FunctionCalling": false
}
```


*Определено в:* `go/pkg/client/model.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelInfo


```json
{
  "Name": "string",
  "FunctionCalling": false
}
```


*Определено в:* `go/pkg/client/model.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:760`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:775 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:775)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *OllamaConfig) DeepCopyInto((out *OllamaConfig)) (out *OllamaConfig)
```


**Тип запроса:** OllamaConfig


```json
{
  "Host": "string",
  "Options": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** OllamaConfig


```json
{
  "Host": "string",
  "Options": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:775`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:797 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:797)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *OpenAIConfig) DeepCopyInto((out *OpenAIConfig)) (out *OpenAIConfig)
```


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


**Тип ответа:** out


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


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:797`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:827 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:827)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *PineconeConfig) DeepCopyInto((out *PineconeConfig)) (out *PineconeConfig)
```


**Тип запроса:** PineconeConfig


```json
{
  "IndexHost": "string",
  "TopK": 0,
  "Namespace": "string",
  "RecordFields": [],
  "ScoreThreshold": "string"
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PineconeConfig


```json
{
  "IndexHost": "string",
  "TopK": 0,
  "Namespace": "string",
  "RecordFields": [],
  "ScoreThreshold": "string"
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:827`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:847 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:847)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *SseMcpServerConfig) DeepCopyInto((out *SseMcpServerConfig)) (out *SseMcpServerConfig)
```


**Тип запроса:** SseMcpServerConfig


```json
{
  "Params": {},
  "Tools": []
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SseMcpServerConfig


```json
{
  "Params": {},
  "Tools": []
}
```


*Определено в:* `contrib/go-adk/pkg/config/types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:847`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:863 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:863)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *StdioMcpServerConfig) DeepCopyInto((out *StdioMcpServerConfig)) (out *StdioMcpServerConfig)
```


**Тип запроса:** StdioMcpServerConfig


```json
{
  "Command": "string",
  "Args": [],
  "Env": {},
  "EnvFrom": [],
  "ReadTimeoutSeconds": 0
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** StdioMcpServerConfig


```json
{
  "Command": "string",
  "Args": [],
  "Env": {},
  "EnvFrom": [],
  "ReadTimeoutSeconds": 0
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:863`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:897 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:897)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *StreamableHttpServerConfig) DeepCopyInto((out *StreamableHttpServerConfig)) (out *StreamableHttpServerConfig)
```


**Тип запроса:** StreamableHttpServerConfig


```json
{
  "TerminateOnClose": false
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** StreamableHttpServerConfig


```json
{
  "TerminateOnClose": false
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:897`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:918 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:918)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Tool) DeepCopyInto((out *Tool)) (out *Tool)
```


**Тип запроса:** Tool


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


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Tool


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


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:918`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:943 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:943)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ToolServer) DeepCopyInto((out *ToolServer)) (out *ToolServer)
```


**Тип запроса:** ToolServer


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


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolServer


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


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:943`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:970 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:970)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ToolServerConfig) DeepCopyInto((out *ToolServerConfig)) (out *ToolServerConfig)
```


**Тип запроса:** ToolServerConfig


```json
{
  "Type": {},
  "Stdio": null,
  "Sse": null,
  "StreamableHttp": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolServerConfig


```json
{
  "Type": {},
  "Stdio": null,
  "Sse": null,
  "StreamableHttp": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:970`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:1000 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:1000)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ToolServerList) DeepCopyInto((out *ToolServerList)) (out *ToolServerList)
```


**Тип запроса:** ToolServerList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolServerList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1000`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:1032 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:1032)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ToolServerSpec) DeepCopyInto((out *ToolServerSpec)) (out *ToolServerSpec)
```


**Тип запроса:** ToolServerSpec


```json
{
  "Description": "string",
  "Config": {}
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolServerSpec


```json
{
  "Description": "string",
  "Config": {}
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1032`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:1048 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:1048)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ToolServerStatus) DeepCopyInto((out *ToolServerStatus)) (out *ToolServerStatus)
```


**Тип запроса:** ToolServerStatus


```json
{
  "ObservedGeneration": 0,
  "Conditions": [],
  "DiscoveredTools": []
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolServerStatus


```json
{
  "ObservedGeneration": 0,
  "Conditions": [],
  "DiscoveredTools": []
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1048`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:1081 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:1081)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ValueRef) DeepCopyInto((out *ValueRef)) (out *ValueRef)
```


**Тип запроса:** ValueRef


```json
{
  "Name": "string",
  "Value": "string",
  "ValueFrom": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValueRef


```json
{
  "Name": "string",
  "Value": "string",
  "ValueFrom": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1081`



---


[function] name: DeepCopyInto file: go/api/v1alpha1/zz_generated.deepcopy.go:1101 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha1/zz_generated.deepcopy.go:1101)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ValueSource) DeepCopyInto((out *ValueSource)) (out *ValueSource)
```


**Тип запроса:** ValueSource


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValueSource


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1101`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:72 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:72)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *Agent) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:72`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:104 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:104)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *AgentList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:104`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:535 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:535)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *Memory) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:535`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:567 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:567)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *MemoryList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:567`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:636 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:636)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ModelConfig) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:636`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:668 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:668)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ModelConfigList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:668`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:962 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:962)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ToolServer) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:962`



---


[function] name: DeepCopyObject file: go/api/v1alpha1/zz_generated.deepcopy.go:1024 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha1/zz_generated.deepcopy.go:1024)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ToolServerList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha1/zz_generated.deepcopy.go:1024`




## go/api/v1alpha2/agent_types.go


📄 Исходный файл: `go/api/v1alpha2/agent_types.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GroupKind](#groupkind-goapiv1alpha2agent_typesgo423) `:423`

- 🔗 [NamespacedName](#namespacedname-goapiv1alpha2agent_typesgo430) `:430`

- 🔗 [ResolveHeaders](#resolveheaders-goapiv1alpha2agent_typesgo365) `:365`

- 🔗 [init](#init-goapiv1alpha2agent_typesgo485) `:485`


</details>


[function] name: GroupKind file: go/api/v1alpha2/agent_types.go:423 returns_error: нет description: —


### GroupKind (go/api/v1alpha2/agent_types.go:423)


GroupKind is a method that performs operations based on the provided parameters and returns ().


```go
func (t *TypedReference) GroupKind(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/agent_types.go:423`



---


[function] name: NamespacedName file: go/api/v1alpha2/agent_types.go:430 returns_error: нет description: —


### NamespacedName (go/api/v1alpha2/agent_types.go:430)


NamespacedName is a method that performs operations based on the provided parameters and returns (defaultNamespace string).


```go
func (t *TypedReference) NamespacedName((defaultNamespace string)) (defaultNamespace string)
```


**Тип ответа:** defaultNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha2/agent_types.go:430`



---


[function] name: ResolveHeaders file: go/api/v1alpha2/agent_types.go:365 returns_error: да description: —


### ResolveHeaders (go/api/v1alpha2/agent_types.go:365)


ResolveHeaders is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Tool) ResolveHeaders((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/api/v1alpha2/agent_types.go:365`



---


[function] name: init file: go/api/v1alpha2/agent_types.go:485 returns_error: нет description: —


### init (go/api/v1alpha2/agent_types.go:485)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/agent_types.go:485`




## go/api/v1alpha2/common_types.go


📄 Исходный файл: `go/api/v1alpha2/common_types.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AllowsNamespace](#allowsnamespace-goapiv1alpha2common_typesgo71) `:71`

- 🔗 [Resolve](#resolve-goapiv1alpha2common_typesgo121) `:121`

- 🔗 [Resolve](#resolve-goapiv1alpha2common_typesgo146) `:146`


</details>


[function] name: AllowsNamespace file: go/api/v1alpha2/common_types.go:71 returns_error: да description: AllowsNamespace checks if a reference from the given namespace is allowed.
The targetNamespace is the namespace where th


### AllowsNamespace (go/api/v1alpha2/common_types.go:71)


AllowsNamespace checks if a reference from the given namespace is allowed.
The targetNamespace is the namespace where the resource being referenced lives.
The sourceNamespace is the namespace where the referencing resource lives.


```go
func (a *AllowedNamespaces) AllowsNamespace((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/api/v1alpha2/common_types.go:71`



---


[function] name: Resolve file: go/api/v1alpha2/common_types.go:121 returns_error: да description: —


### Resolve (go/api/v1alpha2/common_types.go:121)


Resolve is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *ValueSource) Resolve((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/api/v1alpha2/common_types.go:121`



---


[function] name: Resolve file: go/api/v1alpha2/common_types.go:146 returns_error: да description: —


### Resolve (go/api/v1alpha2/common_types.go:146)


Resolve is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *ValueRef) Resolve((string, string, error)) (string, string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/api/v1alpha2/common_types.go:146`




## go/api/v1alpha2/modelconfig_types.go


📄 Исходный файл: `go/api/v1alpha2/modelconfig_types.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-goapiv1alpha2modelconfig_typesgo371) `:371`


</details>


[function] name: init file: go/api/v1alpha2/modelconfig_types.go:371 returns_error: нет description: —


### init (go/api/v1alpha2/modelconfig_types.go:371)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/modelconfig_types.go:371`




## go/api/v1alpha2/modelproviderconfig_types.go


📄 Исходный файл: `go/api/v1alpha2/modelproviderconfig_types.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [DefaultModelProviderEndpoint](#defaultmodelproviderendpoint-goapiv1alpha2modelproviderconfig_typesgo36) `:36`

- 🔗 [GetEndpoint](#getendpoint-goapiv1alpha2modelproviderconfig_typesgo83) `:83`

- 🔗 [RequiresSecret](#requiressecret-goapiv1alpha2modelproviderconfig_typesgo91) `:91`

- 🔗 [init](#init-goapiv1alpha2modelproviderconfig_typesgo153) `:153`


</details>


[function] name: DefaultModelProviderEndpoint file: go/api/v1alpha2/modelproviderconfig_types.go:36 returns_error: нет description: DefaultModelProviderEndpoint returns the default API endpoint for a given model provider type.
Returns empty string if n


### DefaultModelProviderEndpoint (go/api/v1alpha2/modelproviderconfig_types.go:36)


DefaultModelProviderEndpoint returns the default API endpoint for a given model provider type.
Returns empty string if no default is defined.


```go
func DefaultModelProviderEndpoint((providerType ModelProvider)) (providerType ModelProvider)
```


**Тип ответа:** providerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/api/v1alpha2/modelproviderconfig_types.go:36`



---


[function] name: GetEndpoint file: go/api/v1alpha2/modelproviderconfig_types.go:83 returns_error: нет description: GetEndpoint returns the endpoint, or the default endpoint if not specified.


### GetEndpoint (go/api/v1alpha2/modelproviderconfig_types.go:83)


GetEndpoint returns the endpoint, or the default endpoint if not specified.


```go
func (p *ModelProviderConfigSpec) GetEndpoint(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/modelproviderconfig_types.go:83`



---


[function] name: RequiresSecret file: go/api/v1alpha2/modelproviderconfig_types.go:91 returns_error: нет description: RequiresSecret returns true if this model provider type requires a secret for authentication.


### RequiresSecret (go/api/v1alpha2/modelproviderconfig_types.go:91)


RequiresSecret returns true if this model provider type requires a secret for authentication.


```go
func (p *ModelProviderConfigSpec) RequiresSecret(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/modelproviderconfig_types.go:91`



---


[function] name: init file: go/api/v1alpha2/modelproviderconfig_types.go:153 returns_error: нет description: —


### init (go/api/v1alpha2/modelproviderconfig_types.go:153)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/modelproviderconfig_types.go:153`




## go/api/v1alpha2/remotemcpserver_types.go


📄 Исходный файл: `go/api/v1alpha2/remotemcpserver_types.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [ResolveHeaders](#resolveheaders-goapiv1alpha2remotemcpserver_typesgo112) `:112`

- 🔗 [Scan](#scan-goapiv1alpha2remotemcpserver_typesgo66) `:66`

- 🔗 [Value](#value-goapiv1alpha2remotemcpserver_typesgo76) `:76`

- 🔗 [init](#init-goapiv1alpha2remotemcpserver_typesgo135) `:135`


</details>


[function] name: ResolveHeaders file: go/api/v1alpha2/remotemcpserver_types.go:112 returns_error: да description: ResolveHeaders resolves all HeadersFrom entries using the object's namespace.


### ResolveHeaders (go/api/v1alpha2/remotemcpserver_types.go:112)


ResolveHeaders resolves all HeadersFrom entries using the object's namespace.


```go
func (r *RemoteMCPServer) ResolveHeaders((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/api/v1alpha2/remotemcpserver_types.go:112`



---


[function] name: Scan file: go/api/v1alpha2/remotemcpserver_types.go:66 returns_error: нет description: —


### Scan (go/api/v1alpha2/remotemcpserver_types.go:66)


Scan is a method that performs operations based on the provided parameters and returns (src any).


```go
func (t *RemoteMCPServerSpec) Scan((src any)) (src any)
```


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha2/remotemcpserver_types.go:66`



---


[function] name: Value file: go/api/v1alpha2/remotemcpserver_types.go:76 returns_error: да description: —


### Value (go/api/v1alpha2/remotemcpserver_types.go:76)


Value is a method that performs operations based on the provided parameters and may return an error.


```go
func (t RemoteMCPServerSpec) Value((driver.Value, error)) (driver.Value, error)
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


📍 *Расположение:* `go/api/v1alpha2/remotemcpserver_types.go:76`



---


[function] name: init file: go/api/v1alpha2/remotemcpserver_types.go:135 returns_error: нет description: —


### init (go/api/v1alpha2/remotemcpserver_types.go:135)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/remotemcpserver_types.go:135`




## go/api/v1alpha2/zz_generated.deepcopy.go


📄 Исходный файл: `go/api/v1alpha2/zz_generated.deepcopy.go`


<details open>
<summary><b>Функции в этом файле (110)</b></summary>


- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo42) `:42`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo61) `:61`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo93) `:93`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo141) `:141`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo176) `:176`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo198) `:198`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo218) `:218`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo233) `:233`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo249) `:249`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo269) `:269`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo289) `:289`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo309) `:309`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo324) `:324`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo350) `:350`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo390) `:390`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo410) `:410`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo435) `:435`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo496) `:496`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo512) `:512`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo527) `:527`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo543) `:543`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo558) `:558`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo573) `:573`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo599) `:599`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo614) `:614`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo633) `:633`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo665) `:665`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo740) `:740`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo762) `:762`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo781) `:781`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo813) `:813`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo841) `:841`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo872) `:872`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo894) `:894`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo929) `:929`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo945) `:945`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo965) `:965`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo984) `:984`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1016) `:1016`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1066) `:1066`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1099) `:1099`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1114) `:1114`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1143) `:1143`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1247) `:1247`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1277) `:1277`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1292) `:1292`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1324) `:1324`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1339) `:1339`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1354) `:1354`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1374) `:1374`

- 🔗 [DeepCopy](#deepcopy-goapiv1alpha2zz_generateddeepcopygo1389) `:1389`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo30) `:30`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo52) `:52`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo79) `:79`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo111) `:111`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo151) `:151`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo186) `:186`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo208) `:208`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo228) `:228`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo243) `:243`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo259) `:259`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo279) `:279`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo299) `:299`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo319) `:319`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo334) `:334`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo360) `:360`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo400) `:400`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo420) `:420`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo445) `:445`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo506) `:506`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo522) `:522`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo537) `:537`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo553) `:553`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo568) `:568`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo583) `:583`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo609) `:609`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo624) `:624`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo651) `:651`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo683) `:683`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo750) `:750`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo772) `:772`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo799) `:799`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo831) `:831`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo851) `:851`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo882) `:882`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo904) `:904`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo939) `:939`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo955) `:955`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo975) `:975`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1002) `:1002`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1034) `:1034`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1076) `:1076`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1109) `:1109`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1124) `:1124`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1153) `:1153`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1257) `:1257`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1287) `:1287`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1302) `:1302`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1334) `:1334`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1349) `:1349`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1364) `:1364`

- 🔗 [DeepCopyInto](#deepcopyinto-goapiv1alpha2zz_generateddeepcopygo1384) `:1384`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo71) `:71`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo103) `:103`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo643) `:643`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo675) `:675`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo791) `:791`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo823) `:823`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo994) `:994`

- 🔗 [DeepCopyObject](#deepcopyobject-goapiv1alpha2zz_generateddeepcopygo1026) `:1026`


</details>


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:42 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new A2AConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:42)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new A2AConfig.


```go
func (in *A2AConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:42`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:61 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Agent.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:61)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Agent.


```go
func (in *Agent) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:61`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:93 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentList.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:93)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentList.


```go
func (in *AgentList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:93`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:141 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSkill.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:141)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSkill.


```go
func (in *AgentSkill) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:141`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:176 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:176)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentSpec.


```go
func (in *AgentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:176`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:198 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentStatus.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:198)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AgentStatus.


```go
func (in *AgentStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:198`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:218 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AllowedNamespaces.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:218)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AllowedNamespaces.


```go
func (in *AllowedNamespaces) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:218`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:233 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:233)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicConfig.


```go
func (in *AnthropicConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:233`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:249 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicVertexAIConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:249)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AnthropicVertexAIConfig.


```go
func (in *AnthropicVertexAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:249`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:269 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AzureOpenAIConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:269)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new AzureOpenAIConfig.


```go
func (in *AzureOpenAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:269`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:289 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BYOAgentSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:289)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BYOAgentSpec.


```go
func (in *BYOAgentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:289`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:309 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BaseVertexAIConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:309)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BaseVertexAIConfig.


```go
func (in *BaseVertexAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:309`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:324 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BedrockConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:324)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new BedrockConfig.


```go
func (in *BedrockConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:324`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:350 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ByoDeploymentSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:350)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ByoDeploymentSpec.


```go
func (in *ByoDeploymentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:350`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:390 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ContextCompressionConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:390)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ContextCompressionConfig.


```go
func (in *ContextCompressionConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:390`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:410 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ContextConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:410)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ContextConfig.


```go
func (in *ContextConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:410`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:435 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ContextSummarizerConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:435)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ContextSummarizerConfig.


```go
func (in *ContextSummarizerConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:435`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:496 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DeclarativeAgentSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:496)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DeclarativeAgentSpec.


```go
func (in *DeclarativeAgentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:496`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:512 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DeclarativeDeploymentSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:512)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DeclarativeDeploymentSpec.


```go
func (in *DeclarativeDeploymentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:512`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:527 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:527)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiConfig.


```go
func (in *GeminiConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:527`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:543 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiVertexAIConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:543)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GeminiVertexAIConfig.


```go
func (in *GeminiVertexAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:543`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:558 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GitRepo.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:558)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new GitRepo.


```go
func (in *GitRepo) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:558`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:573 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MCPTool.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:573)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MCPTool.


```go
func (in *MCPTool) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:573`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:599 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new McpServerTool.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:599)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new McpServerTool.


```go
func (in *McpServerTool) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:599`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:614 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemorySpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:614)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new MemorySpec.


```go
func (in *MemorySpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:614`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:633 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:633)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfig.


```go
func (in *ModelConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:633`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:665 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigList.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:665)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigList.


```go
func (in *ModelConfigList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:665`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:740 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:740)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigSpec.


```go
func (in *ModelConfigSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:740`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:762 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigStatus.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:762)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelConfigStatus.


```go
func (in *ModelConfigStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:762`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:781 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:781)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfig.


```go
func (in *ModelProviderConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:781`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:813 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfigList.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:813)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfigList.


```go
func (in *ModelProviderConfigList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:813`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:841 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfigSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:841)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfigSpec.


```go
func (in *ModelProviderConfigSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:841`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:872 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfigStatus.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:872)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ModelProviderConfigStatus.


```go
func (in *ModelProviderConfigStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:872`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:894 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OllamaConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:894)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OllamaConfig.


```go
func (in *OllamaConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:894`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:929 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OpenAIConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:929)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OpenAIConfig.


```go
func (in *OpenAIConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:929`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:945 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new PromptSource.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:945)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new PromptSource.


```go
func (in *PromptSource) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:945`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:965 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new PromptTemplateSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:965)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new PromptTemplateSpec.


```go
func (in *PromptTemplateSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:965`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:984 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServer.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:984)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServer.


```go
func (in *RemoteMCPServer) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:984`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1016 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServerList.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1016)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServerList.


```go
func (in *RemoteMCPServerList) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1016`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1066 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServerSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1066)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServerSpec.


```go
func (in *RemoteMCPServerSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1066`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1099 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServerStatus.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1099)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteMCPServerStatus.


```go
func (in *RemoteMCPServerStatus) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1099`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1114 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SecretReference.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1114)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SecretReference.


```go
func (in *SecretReference) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1114`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1143 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ServiceAccountConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1143)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ServiceAccountConfig.


```go
func (in *ServiceAccountConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1143`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1247 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SharedDeploymentSpec.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1247)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SharedDeploymentSpec.


```go
func (in *SharedDeploymentSpec) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1247`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1277 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SkillForAgent.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1277)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new SkillForAgent.


```go
func (in *SkillForAgent) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1277`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1292 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new TLSConfig.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1292)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new TLSConfig.


```go
func (in *TLSConfig) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1292`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1324 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Tool.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1324)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Tool.


```go
func (in *Tool) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1324`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1339 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new TypedLocalReference.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1339)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new TypedLocalReference.


```go
func (in *TypedLocalReference) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1339`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1354 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new TypedReference.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1354)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new TypedReference.


```go
func (in *TypedReference) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1354`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1374 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueRef.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1374)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueRef.


```go
func (in *ValueRef) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1374`



---


[function] name: DeepCopy file: go/api/v1alpha2/zz_generated.deepcopy.go:1389 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueSource.


### DeepCopy (go/api/v1alpha2/zz_generated.deepcopy.go:1389)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ValueSource.


```go
func (in *ValueSource) DeepCopy(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1389`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:30 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:30)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *A2AConfig) DeepCopyInto((out *A2AConfig)) (out *A2AConfig)
```


**Тип запроса:** A2AConfig


```json
{
  "Skills": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** A2AConfig


```json
{
  "Skills": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:30`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:52 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:52)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Agent) DeepCopyInto((out *Agent)) (out *Agent)
```


**Тип запроса:** Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Agent


```json
{
  "ID": "string"
}
```


*Определено в:* `go/pkg/auth/auth.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:52`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:79 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:79)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentList) DeepCopyInto((out *AgentList)) (out *AgentList)
```


**Тип запроса:** AgentList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:79`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:111 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:111)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentSkill) DeepCopyInto((out *AgentSkill)) (out *AgentSkill)
```


**Тип запроса:** AgentSkill


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentSkill


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:111`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:151 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:151)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentSpec) DeepCopyInto((out *AgentSpec)) (out *AgentSpec)
```


**Тип запроса:** AgentSpec


```json
{
  "Description": "string",
  "SystemMessage": "string",
  "ModelConfig": "string",
  "Stream": false,
  "Tools": [],
  "Memory": [],
  "A2AConfig": null,
  "Deployment": null
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentSpec


```json
{
  "Description": "string",
  "SystemMessage": "string",
  "ModelConfig": "string",
  "Stream": false,
  "Tools": [],
  "Memory": [],
  "A2AConfig": null,
  "Deployment": null
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:151`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:186 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:186)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AgentStatus) DeepCopyInto((out *AgentStatus)) (out *AgentStatus)
```


**Тип запроса:** AgentStatus


```json
{
  "ObservedGeneration": 0,
  "ConfigHash": [],
  "Conditions": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentStatus


```json
{
  "ObservedGeneration": 0,
  "ConfigHash": [],
  "Conditions": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:186`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:208 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:208)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AllowedNamespaces) DeepCopyInto((out *AllowedNamespaces)) (out *AllowedNamespaces)
```


**Тип запроса:** AllowedNamespaces


```json
{
  "From": {},
  "Selector": null
}
```


*Определено в:* `go/api/v1alpha2/common_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AllowedNamespaces


```json
{
  "From": {},
  "Selector": null
}
```


*Определено в:* `go/api/v1alpha2/common_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:208`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:228 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:228)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AnthropicConfig) DeepCopyInto((out *AnthropicConfig)) (out *AnthropicConfig)
```


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


**Тип ответа:** out


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


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:228`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:243 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:243)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AnthropicVertexAIConfig) DeepCopyInto((out *AnthropicVertexAIConfig)) (out *AnthropicVertexAIConfig)
```


**Тип запроса:** AnthropicVertexAIConfig


```json
{
  "MaxTokens": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AnthropicVertexAIConfig


```json
{
  "MaxTokens": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:243`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:259 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:259)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *AzureOpenAIConfig) DeepCopyInto((out *AzureOpenAIConfig)) (out *AzureOpenAIConfig)
```


**Тип запроса:** AzureOpenAIConfig


```json
{
  "Model": "string",
  "Headers": {},
  "Timeout": 0
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AzureOpenAIConfig


```json
{
  "Model": "string",
  "Headers": {},
  "Timeout": 0
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:259`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:279 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:279)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *BYOAgentSpec) DeepCopyInto((out *BYOAgentSpec)) (out *BYOAgentSpec)
```


**Тип запроса:** BYOAgentSpec


```json
{
  "Deployment": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BYOAgentSpec


```json
{
  "Deployment": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:279`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:299 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:299)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *BaseVertexAIConfig) DeepCopyInto((out *BaseVertexAIConfig)) (out *BaseVertexAIConfig)
```


**Тип запроса:** BaseVertexAIConfig


```json
{
  "ProjectID": "string",
  "Location": "string",
  "Temperature": "string",
  "TopP": "string",
  "TopK": "string",
  "StopSequences": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BaseVertexAIConfig


```json
{
  "ProjectID": "string",
  "Location": "string",
  "Temperature": "string",
  "TopP": "string",
  "TopK": "string",
  "StopSequences": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:299`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:319 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:319)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *BedrockConfig) DeepCopyInto((out *BedrockConfig)) (out *BedrockConfig)
```


**Тип запроса:** BedrockConfig


```json
{
  "Region": "string"
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BedrockConfig


```json
{
  "Region": "string"
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:319`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:334 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:334)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ByoDeploymentSpec) DeepCopyInto((out *ByoDeploymentSpec)) (out *ByoDeploymentSpec)
```


**Тип запроса:** ByoDeploymentSpec


```json
{
  "Image": "string",
  "Cmd": "string",
  "Args": []
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ByoDeploymentSpec


```json
{
  "Image": "string",
  "Cmd": "string",
  "Args": []
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:334`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:360 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:360)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ContextCompressionConfig) DeepCopyInto((out *ContextCompressionConfig)) (out *ContextCompressionConfig)
```


**Тип запроса:** ContextCompressionConfig


```json
{
  "CompactionInterval": 0,
  "OverlapSize": 0,
  "Summarizer": null,
  "TokenThreshold": 0,
  "EventRetentionSize": 0
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContextCompressionConfig


```json
{
  "CompactionInterval": 0,
  "OverlapSize": 0,
  "Summarizer": null,
  "TokenThreshold": 0,
  "EventRetentionSize": 0
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:360`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:400 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:400)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ContextConfig) DeepCopyInto((out *ContextConfig)) (out *ContextConfig)
```


**Тип запроса:** ContextConfig


```json
{
  "Compaction": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContextConfig


```json
{
  "Compaction": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:400`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:420 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:420)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ContextSummarizerConfig) DeepCopyInto((out *ContextSummarizerConfig)) (out *ContextSummarizerConfig)
```


**Тип запроса:** ContextSummarizerConfig


```json
{
  "ModelConfig": "string",
  "PromptTemplate": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContextSummarizerConfig


```json
{
  "ModelConfig": "string",
  "PromptTemplate": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:420`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:445 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:445)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *DeclarativeAgentSpec) DeepCopyInto((out *DeclarativeAgentSpec)) (out *DeclarativeAgentSpec)
```


**Тип запроса:** DeclarativeAgentSpec


```json
{
  "SystemMessage": "string",
  "SystemMessageFrom": null,
  "PromptTemplate": null,
  "ModelConfig": "string",
  "Stream": false,
  "Tools": [],
  "A2AConfig": null,
  "Deployment": null,
  "ExecuteCodeBlocks": false,
  "Memory": null,
  "Context": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeclarativeAgentSpec


```json
{
  "SystemMessage": "string",
  "SystemMessageFrom": null,
  "PromptTemplate": null,
  "ModelConfig": "string",
  "Stream": false,
  "Tools": [],
  "A2AConfig": null,
  "Deployment": null,
  "ExecuteCodeBlocks": false,
  "Memory": null,
  "Context": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:445`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:506 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:506)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *DeclarativeDeploymentSpec) DeepCopyInto((out *DeclarativeDeploymentSpec)) (out *DeclarativeDeploymentSpec)
```


**Тип запроса:** DeclarativeDeploymentSpec


```json
{
  "ImageRegistry": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeclarativeDeploymentSpec


```json
{
  "ImageRegistry": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:506`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:522 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:522)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *GeminiConfig) DeepCopyInto((out *GeminiConfig)) (out *GeminiConfig)
```


**Тип запроса:** GeminiConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GeminiConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:522`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:537 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:537)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *GeminiVertexAIConfig) DeepCopyInto((out *GeminiVertexAIConfig)) (out *GeminiVertexAIConfig)
```


**Тип запроса:** GeminiVertexAIConfig


```json
{
  "MaxOutputTokens": 0,
  "CandidateCount": 0,
  "ResponseMimeType": "string"
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GeminiVertexAIConfig


```json
{
  "MaxOutputTokens": 0,
  "CandidateCount": 0,
  "ResponseMimeType": "string"
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:537`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:553 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:553)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *GitRepo) DeepCopyInto((out *GitRepo)) (out *GitRepo)
```


**Тип запроса:** GitRepo


```json
{
  "URL": "string",
  "Ref": "string",
  "Path": "string",
  "Name": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GitRepo


```json
{
  "URL": "string",
  "Ref": "string",
  "Path": "string",
  "Name": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:553`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:568 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:568)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *MCPTool) DeepCopyInto((out *MCPTool)) (out *MCPTool)
```


**Тип запроса:** MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MCPTool


```json
{
  "Name": "string",
  "Description": "string",
  "Component": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:568`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:583 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:583)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *McpServerTool) DeepCopyInto((out *McpServerTool)) (out *McpServerTool)
```


**Тип запроса:** McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** McpServerTool


```json
{
  "ToolServer": "string",
  "ToolNames": []
}
```


*Определено в:* `go/api/v1alpha1/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:583`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:609 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:609)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *MemorySpec) DeepCopyInto((out *MemorySpec)) (out *MemorySpec)
```


**Тип запроса:** MemorySpec


```json
{
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "Pinecone": null
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MemorySpec


```json
{
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "Pinecone": null
}
```


*Определено в:* `go/api/v1alpha1/memory_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:609`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:624 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:624)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfig) DeepCopyInto((out *ModelConfig)) (out *ModelConfig)
```


**Тип запроса:** ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:624`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:651 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:651)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfigList) DeepCopyInto((out *ModelConfigList)) (out *ModelConfigList)
```


**Тип запроса:** ModelConfigList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfigList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:651`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:683 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:683)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfigSpec) DeepCopyInto((out *ModelConfigSpec)) (out *ModelConfigSpec)
```


**Тип запроса:** ModelConfigSpec


```json
{
  "Model": "string",
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "DefaultHeaders": {},
  "ModelInfo": null,
  "OpenAI": null,
  "Anthropic": null,
  "AzureOpenAI": null,
  "Ollama": null,
  "Gemini": null,
  "GeminiVertexAI": null,
  "AnthropicVertexAI": null
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfigSpec


```json
{
  "Model": "string",
  "Provider": {},
  "APIKeySecretRef": "string",
  "APIKeySecretKey": "string",
  "DefaultHeaders": {},
  "ModelInfo": null,
  "OpenAI": null,
  "Anthropic": null,
  "AzureOpenAI": null,
  "Ollama": null,
  "Gemini": null,
  "GeminiVertexAI": null,
  "AnthropicVertexAI": null
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:683`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:750 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:750)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelConfigStatus) DeepCopyInto((out *ModelConfigStatus)) (out *ModelConfigStatus)
```


**Тип запроса:** ModelConfigStatus


```json
{
  "Conditions": [],
  "ObservedGeneration": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelConfigStatus


```json
{
  "Conditions": [],
  "ObservedGeneration": 0
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:750`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:772 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:772)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelProviderConfig) DeepCopyInto((out *ModelProviderConfig)) (out *ModelProviderConfig)
```


**Тип запроса:** ModelProviderConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelProviderConfig


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:772`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:799 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:799)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelProviderConfigList) DeepCopyInto((out *ModelProviderConfigList)) (out *ModelProviderConfigList)
```


**Тип запроса:** ModelProviderConfigList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelProviderConfigList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:799`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:831 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:831)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelProviderConfigSpec) DeepCopyInto((out *ModelProviderConfigSpec)) (out *ModelProviderConfigSpec)
```


**Тип запроса:** ModelProviderConfigSpec


```json
{
  "Type": {},
  "Endpoint": "string",
  "SecretRef": null
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelProviderConfigSpec


```json
{
  "Type": {},
  "Endpoint": "string",
  "SecretRef": null
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:831`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:851 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:851)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ModelProviderConfigStatus) DeepCopyInto((out *ModelProviderConfigStatus)) (out *ModelProviderConfigStatus)
```


**Тип запроса:** ModelProviderConfigStatus


```json
{
  "ObservedGeneration": 0,
  "Conditions": [],
  "DiscoveredModels": [],
  "ModelCount": 0,
  "LastDiscoveryTime": null,
  "SecretHash": "string"
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModelProviderConfigStatus


```json
{
  "ObservedGeneration": 0,
  "Conditions": [],
  "DiscoveredModels": [],
  "ModelCount": 0,
  "LastDiscoveryTime": null,
  "SecretHash": "string"
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:851`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:882 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:882)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *OllamaConfig) DeepCopyInto((out *OllamaConfig)) (out *OllamaConfig)
```


**Тип запроса:** OllamaConfig


```json
{
  "Host": "string",
  "Options": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** OllamaConfig


```json
{
  "Host": "string",
  "Options": {}
}
```


*Определено в:* `go/api/v1alpha1/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:882`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:904 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:904)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *OpenAIConfig) DeepCopyInto((out *OpenAIConfig)) (out *OpenAIConfig)
```


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


**Тип ответа:** out


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


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:904`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:939 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:939)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *PromptSource) DeepCopyInto((out *PromptSource)) (out *PromptSource)
```


**Тип запроса:** PromptSource


```json
{
  "Alias": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PromptSource


```json
{
  "Alias": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:939`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:955 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:955)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *PromptTemplateSpec) DeepCopyInto((out *PromptTemplateSpec)) (out *PromptTemplateSpec)
```


**Тип запроса:** PromptTemplateSpec


```json
{
  "DataSources": []
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PromptTemplateSpec


```json
{
  "DataSources": []
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:955`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:975 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:975)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *RemoteMCPServer) DeepCopyInto((out *RemoteMCPServer)) (out *RemoteMCPServer)
```


**Тип запроса:** RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:975`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1002 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1002)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *RemoteMCPServerList) DeepCopyInto((out *RemoteMCPServerList)) (out *RemoteMCPServerList)
```


**Тип запроса:** RemoteMCPServerList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RemoteMCPServerList


```json
{
  "Items": []
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1002`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1034 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1034)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *RemoteMCPServerSpec) DeepCopyInto((out *RemoteMCPServerSpec)) (out *RemoteMCPServerSpec)
```


**Тип запроса:** RemoteMCPServerSpec


```json
{
  "Description": "string",
  "Protocol": {},
  "URL": "string",
  "HeadersFrom": [],
  "Timeout": null,
  "SseReadTimeout": null,
  "TerminateOnClose": false,
  "AllowedNamespaces": null
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RemoteMCPServerSpec


```json
{
  "Description": "string",
  "Protocol": {},
  "URL": "string",
  "HeadersFrom": [],
  "Timeout": null,
  "SseReadTimeout": null,
  "TerminateOnClose": false,
  "AllowedNamespaces": null
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1034`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1076 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1076)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *RemoteMCPServerStatus) DeepCopyInto((out *RemoteMCPServerStatus)) (out *RemoteMCPServerStatus)
```


**Тип запроса:** RemoteMCPServerStatus


```json
{
  "ObservedGeneration": 0,
  "Conditions": [],
  "DiscoveredTools": []
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RemoteMCPServerStatus


```json
{
  "ObservedGeneration": 0,
  "Conditions": [],
  "DiscoveredTools": []
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1076`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1109 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1109)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *SecretReference) DeepCopyInto((out *SecretReference)) (out *SecretReference)
```


**Тип запроса:** SecretReference


```json
{
  "Name": "string"
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SecretReference


```json
{
  "Name": "string"
}
```


*Определено в:* `go/api/v1alpha2/modelproviderconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1109`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1124 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1124)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ServiceAccountConfig) DeepCopyInto((out *ServiceAccountConfig)) (out *ServiceAccountConfig)
```


**Тип запроса:** ServiceAccountConfig


```json
{
  "Labels": {},
  "Annotations": {}
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ServiceAccountConfig


```json
{
  "Labels": {},
  "Annotations": {}
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1124`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1153 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1153)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *SharedDeploymentSpec) DeepCopyInto((out *SharedDeploymentSpec)) (out *SharedDeploymentSpec)
```


**Тип запроса:** SharedDeploymentSpec


```json
{
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "VolumeMounts": [],
  "Labels": {},
  "Annotations": {},
  "Env": [],
  "ImagePullPolicy": {},
  "Resources": null,
  "Tolerations": [],
  "Affinity": null,
  "NodeSelector": {},
  "SecurityContext": null,
  "PodSecurityContext": null,
  "ServiceAccountName": "string",
  "ServiceAccountConfig": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SharedDeploymentSpec


```json
{
  "Replicas": 0,
  "ImagePullSecrets": [],
  "Volumes": [],
  "VolumeMounts": [],
  "Labels": {},
  "Annotations": {},
  "Env": [],
  "ImagePullPolicy": {},
  "Resources": null,
  "Tolerations": [],
  "Affinity": null,
  "NodeSelector": {},
  "SecurityContext": null,
  "PodSecurityContext": null,
  "ServiceAccountName": "string",
  "ServiceAccountConfig": null
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1153`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1257 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1257)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *SkillForAgent) DeepCopyInto((out *SkillForAgent)) (out *SkillForAgent)
```


**Тип запроса:** SkillForAgent


```json
{
  "InsecureSkipVerify": false,
  "Refs": [],
  "GitAuthSecretRef": null,
  "GitRefs": []
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SkillForAgent


```json
{
  "InsecureSkipVerify": false,
  "Refs": [],
  "GitAuthSecretRef": null,
  "GitRefs": []
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1257`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1287 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1287)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *TLSConfig) DeepCopyInto((out *TLSConfig)) (out *TLSConfig)
```


**Тип запроса:** TLSConfig


```json
{
  "DisableVerify": false,
  "CACertSecretRef": "string",
  "CACertSecretKey": "string",
  "DisableSystemCAs": false
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TLSConfig


```json
{
  "DisableVerify": false,
  "CACertSecretRef": "string",
  "CACertSecretKey": "string",
  "DisableSystemCAs": false
}
```


*Определено в:* `go/api/v1alpha2/modelconfig_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1287`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1302 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1302)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Tool) DeepCopyInto((out *Tool)) (out *Tool)
```


**Тип запроса:** Tool


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


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Tool


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


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1302`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1334 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1334)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *TypedLocalReference) DeepCopyInto((out *TypedLocalReference)) (out *TypedLocalReference)
```


**Тип запроса:** TypedLocalReference


```json
{
  "Kind": "string",
  "ApiGroup": "string",
  "Name": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TypedLocalReference


```json
{
  "Kind": "string",
  "ApiGroup": "string",
  "Name": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1334`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1349 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1349)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *TypedReference) DeepCopyInto((out *TypedReference)) (out *TypedReference)
```


**Тип запроса:** TypedReference


```json
{
  "Kind": "string",
  "ApiGroup": "string",
  "Name": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TypedReference


```json
{
  "Kind": "string",
  "ApiGroup": "string",
  "Name": "string",
  "Namespace": "string"
}
```


*Определено в:* `go/api/v1alpha2/agent_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1349`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1364 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1364)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ValueRef) DeepCopyInto((out *ValueRef)) (out *ValueRef)
```


**Тип запроса:** ValueRef


```json
{
  "Name": "string",
  "Value": "string",
  "ValueFrom": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValueRef


```json
{
  "Name": "string",
  "Value": "string",
  "ValueFrom": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1364`



---


[function] name: DeepCopyInto file: go/api/v1alpha2/zz_generated.deepcopy.go:1384 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (go/api/v1alpha2/zz_generated.deepcopy.go:1384)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *ValueSource) DeepCopyInto((out *ValueSource)) (out *ValueSource)
```


**Тип запроса:** ValueSource


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Тип ответа:** out


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValueSource


```json
{
  "Type": {},
  "ValueRef": "string",
  "Key": "string"
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1384`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:71 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:71)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *Agent) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:71`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:103 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:103)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *AgentList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:103`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:643 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:643)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ModelConfig) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:643`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:675 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:675)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ModelConfigList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:675`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:791 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:791)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ModelProviderConfig) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:791`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:823 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:823)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *ModelProviderConfigList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:823`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:994 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:994)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *RemoteMCPServer) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:994`



---


[function] name: DeepCopyObject file: go/api/v1alpha2/zz_generated.deepcopy.go:1026 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (go/api/v1alpha2/zz_generated.deepcopy.go:1026)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *RemoteMCPServerList) DeepCopyObject(()) ()
```


📍 *Расположение:* `go/api/v1alpha2/zz_generated.deepcopy.go:1026`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](contrib_go-adk.md)

- [Следующая директория](go_cli.md)


---

