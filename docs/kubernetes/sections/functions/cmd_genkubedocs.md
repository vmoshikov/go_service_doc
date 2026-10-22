---
title: "Функции: cmd/genkubedocs"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/genkubedocs
---


# Функции: cmd/genkubedocs


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genfeaturegates.md)

- [Следующая директория](cmd_genman.md)


---


## Меню по файлам


- 📄 [cmd/genkubedocs/gen_kube_docs.go](#cmdgenkubedocsgen_kube_docsgo)

- 📄 [cmd/genkubedocs/postprocessing.go](#cmdgenkubedocspostprocessinggo)


---


## cmd/genkubedocs/gen_kube_docs.go


📄 Исходный файл: `cmd/genkubedocs/gen_kube_docs.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdgenkubedocsgen_kube_docsgo37) `:37`


</details>


[function] name: main file: cmd/genkubedocs/gen_kube_docs.go:37 returns_error: нет description: —


### main (cmd/genkubedocs/gen_kube_docs.go:37)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/genkubedocs/gen_kube_docs.go:37`




## cmd/genkubedocs/postprocessing.go


📄 Исходный файл: `cmd/genkubedocs/postprocessing.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarkdownPostProcessing](#markdownpostprocessing-cmdgenkubedocspostprocessinggo28) `:28`

- 🔗 [cleanupForInclude](#cleanupforinclude-cmdgenkubedocspostprocessinggo54) `:54`


</details>


[function] name: MarkdownPostProcessing file: cmd/genkubedocs/postprocessing.go:28 returns_error: нет description: MarkdownPostProcessing goes though the generated files


### MarkdownPostProcessing (cmd/genkubedocs/postprocessing.go:28)


MarkdownPostProcessing goes though the generated files


```go
func MarkdownPostProcessing((cmd *cobra.Command, dir string, processor func(string) string)) (cmd *cobra.Command, dir string, processor func(string) string)
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


**Тип ответа:** cmd


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


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


**Тип ответа:** dir


```json
{
  "name": "string",
  "goRestfulContainer": null,
  "nonGoRestfulMux": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/handler.go`


**Тип ответа:** processor


```json
{
  "CoreID": 0,
  "SocketID": 0,
  "NodeID": 0
}
```


*Определено в:* `pkg/kubelet/winstats/cpu_topology.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/genkubedocs/postprocessing.go:28`



---


[function] name: cleanupForInclude file: cmd/genkubedocs/postprocessing.go:54 returns_error: нет description: cleanupForInclude parts of markdown that will make difficult to use it as include in the website:
- The title of the doc


### cleanupForInclude (cmd/genkubedocs/postprocessing.go:54)


cleanupForInclude parts of markdown that will make difficult to use it as include in the website:
- The title of the document (this allow more flexibility for include, e.g. include in tabs)
- The sections see also, that assumes file will be used as a main page


```go
func cleanupForInclude((md string)) (md string)
```


**Тип ответа:** md


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `cmd/genkubedocs/postprocessing.go:54`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genfeaturegates.md)

- [Следующая директория](cmd_genman.md)


---

