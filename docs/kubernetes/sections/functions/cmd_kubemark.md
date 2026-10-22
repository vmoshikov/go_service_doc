---
title: "Функции: cmd/kubemark"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/kubemark
---


# Функции: cmd/kubemark


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kubelet.md)

- [Следующая директория](cmd_preferredimports.md)


---


## Меню по файлам


- 📄 [cmd/kubemark/app/hollow_node.go](#cmdkubemarkapphollow_nodego)

- 📄 [cmd/kubemark/hollow-node.go](#cmdkubemarkhollow-nodego)


---


## cmd/kubemark/app/hollow_node.go


📄 Исходный файл: `cmd/kubemark/app/hollow_node.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [NewHollowNodeCommand](#newhollownodecommand-cmdkubemarkapphollow_nodego153) `:153`

- 🔗 [addFlags](#addflags-cmdkubemarkapphollow_nodego89) `:89`

- 🔗 [bootstrapClientConfig](#bootstrapclientconfig-cmdkubemarkapphollow_nodego133) `:133`

- 🔗 [createClientConfigFromFile](#createclientconfigfromfile-cmdkubemarkapphollow_nodego118) `:118`

- 🔗 [createHollowKubeletOptions](#createhollowkubeletoptions-cmdkubemarkapphollow_nodego140) `:140`

- 🔗 [run](#run-cmdkubemarkapphollow_nodego184) `:184`


</details>


[function] name: NewHollowNodeCommand file: cmd/kubemark/app/hollow_node.go:153 returns_error: нет description: NewHollowNodeCommand creates a *cobra.Command object with default parameters


### NewHollowNodeCommand (cmd/kubemark/app/hollow_node.go:153)


NewHollowNodeCommand creates a *cobra.Command object with default parameters


```go
func NewHollowNodeCommand(()) ()
```


📍 *Расположение:* `cmd/kubemark/app/hollow_node.go:153`



---


[function] name: addFlags file: cmd/kubemark/app/hollow_node.go:89 returns_error: нет description: —


### addFlags (cmd/kubemark/app/hollow_node.go:89)


addFlags is a method that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func (c *hollowNodeConfig) addFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kubemark/app/hollow_node.go:89`



---


[function] name: bootstrapClientConfig file: cmd/kubemark/app/hollow_node.go:133 returns_error: нет description: —


### bootstrapClientConfig (cmd/kubemark/app/hollow_node.go:133)


bootstrapClientConfig is a method that performs operations based on the provided parameters and returns ().


```go
func (c *hollowNodeConfig) bootstrapClientConfig(()) ()
```


📍 *Расположение:* `cmd/kubemark/app/hollow_node.go:133`



---


[function] name: createClientConfigFromFile file: cmd/kubemark/app/hollow_node.go:118 returns_error: да description: —


### createClientConfigFromFile (cmd/kubemark/app/hollow_node.go:118)


createClientConfigFromFile is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *hollowNodeConfig) createClientConfigFromFile((*restclient.Config, error)) (*restclient.Config, error)
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


📍 *Расположение:* `cmd/kubemark/app/hollow_node.go:118`



---


[function] name: createHollowKubeletOptions file: cmd/kubemark/app/hollow_node.go:140 returns_error: нет description: —


### createHollowKubeletOptions (cmd/kubemark/app/hollow_node.go:140)


createHollowKubeletOptions is a method that performs operations based on the provided parameters and returns ().


```go
func (c *hollowNodeConfig) createHollowKubeletOptions(()) ()
```


📍 *Расположение:* `cmd/kubemark/app/hollow_node.go:140`



---


[function] name: run file: cmd/kubemark/app/hollow_node.go:184 returns_error: нет description: —


### run (cmd/kubemark/app/hollow_node.go:184)


run is a function that performs operations based on the provided parameters and returns (ctx context.Context, config *hollowNodeConfig).


```go
func run((ctx context.Context, config *hollowNodeConfig)) (ctx context.Context, config *hollowNodeConfig)
```


**Тип запроса:** hollowNodeConfig


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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** hollowNodeConfig


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


📍 *Расположение:* `cmd/kubemark/app/hollow_node.go:184`




## cmd/kubemark/hollow-node.go


📄 Исходный файл: `cmd/kubemark/hollow-node.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdkubemarkhollow-nodego26) `:26`


</details>


[function] name: main file: cmd/kubemark/hollow-node.go:26 returns_error: нет description: —


### main (cmd/kubemark/hollow-node.go:26)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/kubemark/hollow-node.go:26`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kubelet.md)

- [Следующая директория](cmd_preferredimports.md)


---

