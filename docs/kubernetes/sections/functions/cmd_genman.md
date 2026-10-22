---
title: "Функции: cmd/genman"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/genman
---


# Функции: cmd/genman


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genkubedocs.md)

- [Следующая директория](cmd_genswaggertypedocs.md)


---


## Меню по файлам


- 📄 [cmd/genman/gen_kube_man.go](#cmdgenmangen_kube_mango)


---


## cmd/genman/gen_kube_man.go


📄 Исходный файл: `cmd/genman/gen_kube_man.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [genMarkdown](#genmarkdown-cmdgenmangen_kube_mango168) `:168`

- 🔗 [main](#main-cmdgenmangen_kube_mango41) `:41`

- 🔗 [preamble](#preamble-cmdgenmangen_kube_mango120) `:120`

- 🔗 [printFlags](#printflags-cmdgenmangen_kube_mango133) `:133`

- 🔗 [printOptions](#printoptions-cmdgenmangen_kube_mango153) `:153`


</details>


[function] name: genMarkdown file: cmd/genman/gen_kube_man.go:168 returns_error: нет description: —


### genMarkdown (cmd/genman/gen_kube_man.go:168)


genMarkdown is a function that performs operations based on the provided parameters and returns (command *cobra.Command, parent, docsDir string).


```go
func genMarkdown((command *cobra.Command, parent, docsDir string)) (command *cobra.Command, parent, docsDir string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** parent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** docsDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genman/gen_kube_man.go:168`



---


[function] name: main file: cmd/genman/gen_kube_man.go:41 returns_error: нет description: —


### main (cmd/genman/gen_kube_man.go:41)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/genman/gen_kube_man.go:41`



---


[function] name: preamble file: cmd/genman/gen_kube_man.go:120 returns_error: нет description: —


### preamble (cmd/genman/gen_kube_man.go:120)


preamble is a function that performs operations based on the provided parameters and returns (out *bytes.Buffer, name, short, long string).


```go
func preamble((out *bytes.Buffer, name, short, long string)) (out *bytes.Buffer, name, short, long string)
```


**Тип запроса:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** short


```json
{
  "RESTMapper": {},
  "discoveryClient": {},
  "warningHandler": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/restmapper/shortcut.go`


**Тип ответа:** long


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genman/gen_kube_man.go:120`



---


[function] name: printFlags file: cmd/genman/gen_kube_man.go:133 returns_error: нет description: —


### printFlags (cmd/genman/gen_kube_man.go:133)


printFlags is a function that performs operations based on the provided parameters and returns (out *bytes.Buffer, flags *pflag.FlagSet).


```go
func printFlags((out *bytes.Buffer, flags *pflag.FlagSet)) (out *bytes.Buffer, flags *pflag.FlagSet)
```


**Тип запроса:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


📍 *Расположение:* `cmd/genman/gen_kube_man.go:133`



---


[function] name: printOptions file: cmd/genman/gen_kube_man.go:153 returns_error: нет description: —


### printOptions (cmd/genman/gen_kube_man.go:153)


printOptions is a function that performs operations based on the provided parameters and returns (out *bytes.Buffer, command *cobra.Command).


```go
func printOptions((out *bytes.Buffer, command *cobra.Command)) (out *bytes.Buffer, command *cobra.Command)
```


**Тип запроса:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** bytes.Buffer


```json
{
  "buffer": [],
  "startIndex": 0,
  "endIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval.go`


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


📍 *Расположение:* `cmd/genman/gen_kube_man.go:153`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genkubedocs.md)

- [Следующая директория](cmd_genswaggertypedocs.md)


---

