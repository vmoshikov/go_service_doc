---
title: "Функции: cmd/genyaml"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/genyaml
---


# Функции: cmd/genyaml


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genutils.md)

- [Следующая директория](cmd_gotemplate.md)


---


## Меню по файлам


- 📄 [cmd/genyaml/gen_kubectl_yaml.go](#cmdgenyamlgen_kubectl_yamlgo)


---


## cmd/genyaml/gen_kubectl_yaml.go


📄 Исходный файл: `cmd/genyaml/gen_kubectl_yaml.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [forceMultiLine](#forcemultiline-cmdgenyamlgen_kubectl_yamlgo79) `:79`

- 🔗 [genFlagResult](#genflagresult-cmdgenyamlgen_kubectl_yamlgo86) `:86`

- 🔗 [genYaml](#genyaml-cmdgenyamlgen_kubectl_yamlgo114) `:114`

- 🔗 [main](#main-cmdgenyamlgen_kubectl_yamlgo52) `:52`


</details>


[function] name: forceMultiLine file: cmd/genyaml/gen_kubectl_yaml.go:79 returns_error: нет description: Temporary workaround for yaml lib generating incorrect yaml with long strings
that do not contain \n.


### forceMultiLine (cmd/genyaml/gen_kubectl_yaml.go:79)


Temporary workaround for yaml lib generating incorrect yaml with long strings
that do not contain \n.


```go
func forceMultiLine((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `cmd/genyaml/gen_kubectl_yaml.go:79`



---


[function] name: genFlagResult file: cmd/genyaml/gen_kubectl_yaml.go:86 returns_error: нет description: —


### genFlagResult (cmd/genyaml/gen_kubectl_yaml.go:86)


genFlagResult is a function that performs operations based on the provided parameters and returns (flags *pflag.FlagSet).


```go
func genFlagResult((flags *pflag.FlagSet)) (flags *pflag.FlagSet)
```


**Тип запроса:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pflag.FlagSet


```json
{
  "FlagSets": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/flagz/flagreader.go`


📍 *Расположение:* `cmd/genyaml/gen_kubectl_yaml.go:86`



---


[function] name: genYaml file: cmd/genyaml/gen_kubectl_yaml.go:114 returns_error: нет description: —


### genYaml (cmd/genyaml/gen_kubectl_yaml.go:114)


genYaml is a function that performs operations based on the provided parameters and returns (command *cobra.Command, parent, docsDir string).


```go
func genYaml((command *cobra.Command, parent, docsDir string)) (command *cobra.Command, parent, docsDir string)
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


📍 *Расположение:* `cmd/genyaml/gen_kubectl_yaml.go:114`



---


[function] name: main file: cmd/genyaml/gen_kubectl_yaml.go:52 returns_error: нет description: —


### main (cmd/genyaml/gen_kubectl_yaml.go:52)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/genyaml/gen_kubectl_yaml.go:52`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genutils.md)

- [Следующая директория](cmd_gotemplate.md)


---

