---
title: "Функции: go/cli"
type: functions
repo: kagent
language: ru
chunk_boundary: h3
group: go/cli
---


# Функции: go/cli


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_api.md)

- [Следующая директория](go_cmd.md)


---


## Меню по файлам


- 📄 [go/cli/cmd/kagent/main.go](#goclicmdkagentmaingo)

- 📄 [go/cli/internal/agent/frameworks/adk/python/generator.go](#gocliinternalagentframeworksadkpythongeneratorgo)

- 📄 [go/cli/internal/agent/frameworks/common/base_generator.go](#gocliinternalagentframeworkscommonbase_generatorgo)

- 📄 [go/cli/internal/agent/frameworks/common/manifest_manager.go](#gocliinternalagentframeworkscommonmanifest_managergo)

- 📄 [go/cli/internal/agent/frameworks/frameworks.go](#gocliinternalagentframeworksframeworksgo)

- 📄 [go/cli/internal/cli/agent/add_mcp.go](#gocliinternalcliagentadd_mcpgo)

- 📄 [go/cli/internal/cli/agent/bug_report.go](#gocliinternalcliagentbug_reportgo)

- 📄 [go/cli/internal/cli/agent/build.go](#gocliinternalcliagentbuildgo)

- 📄 [go/cli/internal/cli/agent/const.go](#gocliinternalcliagentconstgo)

- 📄 [go/cli/internal/cli/agent/dashboard.go](#gocliinternalcliagentdashboardgo)

- 📄 [go/cli/internal/cli/agent/dashboard_darwin.go](#gocliinternalcliagentdashboard_darwingo)

- 📄 [go/cli/internal/cli/agent/deploy.go](#gocliinternalcliagentdeploygo)

- 📄 [go/cli/internal/cli/agent/format.go](#gocliinternalcliagentformatgo)

- 📄 [go/cli/internal/cli/agent/get.go](#gocliinternalcliagentgetgo)

- 📄 [go/cli/internal/cli/agent/init.go](#gocliinternalcliagentinitgo)

- 📄 [go/cli/internal/cli/agent/install.go](#gocliinternalcliagentinstallgo)

- 📄 [go/cli/internal/cli/agent/invoke.go](#gocliinternalcliagentinvokego)

- 📄 [go/cli/internal/cli/agent/run.go](#gocliinternalcliagentrungo)

- 📄 [go/cli/internal/cli/agent/utils.go](#gocliinternalcliagentutilsgo)

- 📄 [go/cli/internal/cli/agent/version.go](#gocliinternalcliagentversiongo)

- 📄 [go/cli/internal/cli/envdoc/envdoc.go](#gocliinternalclienvdocenvdocgo)

- 📄 [go/cli/internal/cli/mcp/add_tool.go](#gocliinternalclimcpadd_toolgo)

- 📄 [go/cli/internal/cli/mcp/build.go](#gocliinternalclimcpbuildgo)

- 📄 [go/cli/internal/cli/mcp/deploy.go](#gocliinternalclimcpdeploygo)

- 📄 [go/cli/internal/cli/mcp/init.go](#gocliinternalclimcpinitgo)

- 📄 [go/cli/internal/cli/mcp/init_go.go](#gocliinternalclimcpinit_gogo)

- 📄 [go/cli/internal/cli/mcp/init_java.go](#gocliinternalclimcpinit_javago)

- 📄 [go/cli/internal/cli/mcp/init_python.go](#gocliinternalclimcpinit_pythongo)

- 📄 [go/cli/internal/cli/mcp/init_typescript.go](#gocliinternalclimcpinit_typescriptgo)

- 📄 [go/cli/internal/cli/mcp/inspector.go](#gocliinternalclimcpinspectorgo)

- 📄 [go/cli/internal/cli/mcp/root.go](#gocliinternalclimcprootgo)

- 📄 [go/cli/internal/cli/mcp/run.go](#gocliinternalclimcprungo)

- 📄 [go/cli/internal/cli/mcp/secrets.go](#gocliinternalclimcpsecretsgo)

- 📄 [go/cli/internal/common/exec/docker.go](#gocliinternalcommonexecdockergo)

- 📄 [go/cli/internal/common/exec/kubectl.go](#gocliinternalcommonexeckubectlgo)

- 📄 [go/cli/internal/common/fs/project.go](#gocliinternalcommonfsprojectgo)

- 📄 [go/cli/internal/common/generator/base.go](#gocliinternalcommongeneratorbasego)

- 📄 [go/cli/internal/common/image/image.go](#gocliinternalcommonimageimagego)

- 📄 [go/cli/internal/common/k8s/config.go](#gocliinternalcommonk8sconfiggo)

- 📄 [go/cli/internal/common/prompt/input.go](#gocliinternalcommonpromptinputgo)

- 📄 [go/cli/internal/config/config.go](#gocliinternalconfigconfiggo)

- 📄 [go/cli/internal/config/utils.go](#gocliinternalconfigutilsgo)

- 📄 [go/cli/internal/mcp/builder/builder.go](#gocliinternalmcpbuilderbuildergo)

- 📄 [go/cli/internal/mcp/frameworks/common/base_generator.go](#gocliinternalmcpframeworkscommonbase_generatorgo)

- 📄 [go/cli/internal/mcp/frameworks/frameworks.go](#gocliinternalmcpframeworksframeworksgo)

- 📄 [go/cli/internal/mcp/frameworks/golang/generator.go](#gocliinternalmcpframeworksgolanggeneratorgo)

- 📄 [go/cli/internal/mcp/frameworks/java/generator.go](#gocliinternalmcpframeworksjavageneratorgo)

- 📄 [go/cli/internal/mcp/frameworks/python/generator.go](#gocliinternalmcpframeworkspythongeneratorgo)

- 📄 [go/cli/internal/mcp/frameworks/typescript/generator.go](#gocliinternalmcpframeworkstypescriptgeneratorgo)

- 📄 [go/cli/internal/mcp/manifests/manager.go](#gocliinternalmcpmanifestsmanagergo)

- 📄 [go/cli/internal/profiles/profiles.go](#gocliinternalprofilesprofilesgo)

- 📄 [go/cli/internal/tui/chat.go](#gocliinternaltuichatgo)

- 📄 [go/cli/internal/tui/dialogs/agent_chooser.go](#gocliinternaltuidialogsagent_choosergo)

- 📄 [go/cli/internal/tui/dialogs/manager.go](#gocliinternaltuidialogsmanagergo)

- 📄 [go/cli/internal/tui/dialogs/mcp_server_wizard.go](#gocliinternaltuidialogsmcp_server_wizardgo)

- 📄 [go/cli/internal/tui/keys/keys.go](#gocliinternaltuikeyskeysgo)

- 📄 [go/cli/internal/tui/theme/colors.go](#gocliinternaltuithemecolorsgo)

- 📄 [go/cli/internal/tui/workspace.go](#gocliinternaltuiworkspacego)


---


## go/cli/cmd/kagent/main.go


📄 Исходный файл: `go/cli/cmd/kagent/main.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [main](#main-goclicmdkagentmaingo20) `:20`

- 🔗 [runInteractive](#runinteractive-goclicmdkagentmaingo432) `:432`


</details>


[function] name: main file: go/cli/cmd/kagent/main.go:20 returns_error: нет description: —


### main (go/cli/cmd/kagent/main.go:20)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `go/cli/cmd/kagent/main.go:20`



---


[function] name: runInteractive file: go/cli/cmd/kagent/main.go:432 returns_error: нет description: —


### runInteractive (go/cli/cmd/kagent/main.go:432)


runInteractive is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func runInteractive((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/cmd/kagent/main.go:432`




## go/cli/internal/agent/frameworks/adk/python/generator.go


📄 Исходный файл: `go/cli/internal/agent/frameworks/adk/python/generator.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Generate](#generate-gocliinternalagentframeworksadkpythongeneratorgo28) `:28`

- 🔗 [NewPythonGenerator](#newpythongenerator-gocliinternalagentframeworksadkpythongeneratorgo21) `:21`


</details>


[function] name: Generate file: go/cli/internal/agent/frameworks/adk/python/generator.go:28 returns_error: нет description: Generate creates a new Python ADK project


### Generate (go/cli/internal/agent/frameworks/adk/python/generator.go:28)


Generate creates a new Python ADK project


```go
func (g *PythonGenerator) Generate((projectDir, agentName, instruction, modelProvider, modelName, description string, verbose bool, kagentVersion string)) (projectDir, agentName, instruction, modelProvider, modelName, description string, verbose bool, kagentVersion string)
```


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** instruction


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** modelProvider


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/modelproviderconfig.go`


**Тип ответа:** modelName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kagentVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/agent/frameworks/adk/python/generator.go:28`



---


[function] name: NewPythonGenerator file: go/cli/internal/agent/frameworks/adk/python/generator.go:21 returns_error: нет description: NewPythonGenerator creates a new ADK Python generator


### NewPythonGenerator (go/cli/internal/agent/frameworks/adk/python/generator.go:21)


NewPythonGenerator creates a new ADK Python generator


```go
func NewPythonGenerator(()) ()
```


📍 *Расположение:* `go/cli/internal/agent/frameworks/adk/python/generator.go:21`




## go/cli/internal/agent/frameworks/common/base_generator.go


📄 Исходный файл: `go/cli/internal/agent/frameworks/common/base_generator.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [GenerateProject](#generateproject-gocliinternalagentframeworkscommonbase_generatorgo57) `:57`

- 🔗 [GetDirectory](#getdirectory-gocliinternalagentframeworkscommonbase_generatorgo25) `:25`

- 🔗 [IsVerbose](#isverbose-gocliinternalagentframeworkscommonbase_generatorgo29) `:29`

- 🔗 [NewBaseGenerator](#newbasegenerator-gocliinternalagentframeworkscommonbase_generatorgo49) `:49`

- 🔗 [RenderTemplate](#rendertemplate-gocliinternalagentframeworkscommonbase_generatorgo63) `:63`

- 🔗 [ShouldInitGit](#shouldinitgit-gocliinternalagentframeworkscommonbase_generatorgo33) `:33`

- 🔗 [ShouldSkipPath](#shouldskippath-gocliinternalagentframeworkscommonbase_generatorgo37) `:37`


</details>


[function] name: GenerateProject file: go/cli/internal/agent/frameworks/common/base_generator.go:57 returns_error: нет description: GenerateProject generates a new project using the provided templates.
This delegates to the shared generator implementat


### GenerateProject (go/cli/internal/agent/frameworks/common/base_generator.go:57)


GenerateProject generates a new project using the provided templates.
This delegates to the shared generator implementation.


```go
func (g *BaseGenerator) GenerateProject((config AgentConfig)) (config AgentConfig)
```


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


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/base_generator.go:57`



---


[function] name: GetDirectory file: go/cli/internal/agent/frameworks/common/base_generator.go:25 returns_error: нет description: Implement ProjectConfig interface for AgentConfig


### GetDirectory (go/cli/internal/agent/frameworks/common/base_generator.go:25)


Implement ProjectConfig interface for AgentConfig


```go
func (c AgentConfig) GetDirectory(()) ()
```


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/base_generator.go:25`



---


[function] name: IsVerbose file: go/cli/internal/agent/frameworks/common/base_generator.go:29 returns_error: нет description: —


### IsVerbose (go/cli/internal/agent/frameworks/common/base_generator.go:29)


IsVerbose is a method that performs operations based on the provided parameters and returns ().


```go
func (c AgentConfig) IsVerbose(()) ()
```


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/base_generator.go:29`



---


[function] name: NewBaseGenerator file: go/cli/internal/agent/frameworks/common/base_generator.go:49 returns_error: нет description: NewBaseGenerator creates a new base generator that uses the shared generator


### NewBaseGenerator (go/cli/internal/agent/frameworks/common/base_generator.go:49)


NewBaseGenerator creates a new base generator that uses the shared generator


```go
func NewBaseGenerator((templateFiles fs.FS)) (templateFiles fs.FS)
```


**Тип ответа:** templateFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fs.FS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/base_generator.go:49`



---


[function] name: RenderTemplate file: go/cli/internal/agent/frameworks/common/base_generator.go:63 returns_error: да description: RenderTemplate renders a template string with the provided data.
This delegates to the shared generator implementation.


### RenderTemplate (go/cli/internal/agent/frameworks/common/base_generator.go:63)


RenderTemplate renders a template string with the provided data.
This delegates to the shared generator implementation.


```go
func (g *BaseGenerator) RenderTemplate((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/base_generator.go:63`



---


[function] name: ShouldInitGit file: go/cli/internal/agent/frameworks/common/base_generator.go:33 returns_error: нет description: —


### ShouldInitGit (go/cli/internal/agent/frameworks/common/base_generator.go:33)


ShouldInitGit is a method that performs operations based on the provided parameters and returns ().


```go
func (c AgentConfig) ShouldInitGit(()) ()
```


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/base_generator.go:33`



---


[function] name: ShouldSkipPath file: go/cli/internal/agent/frameworks/common/base_generator.go:37 returns_error: нет description: —


### ShouldSkipPath (go/cli/internal/agent/frameworks/common/base_generator.go:37)


ShouldSkipPath is a method that performs operations based on the provided parameters and returns (path string).


```go
func (c AgentConfig) ShouldSkipPath((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/base_generator.go:37`




## go/cli/internal/agent/frameworks/common/manifest_manager.go


📄 Исходный файл: `go/cli/internal/agent/frameworks/common/manifest_manager.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Load](#load-gocliinternalagentframeworkscommonmanifest_managergo53) `:53`

- 🔗 [NewManifestManager](#newmanifestmanager-gocliinternalagentframeworkscommonmanifest_managergo46) `:46`

- 🔗 [NewProjectManifest](#newprojectmanifest-gocliinternalagentframeworkscommonmanifest_managergo154) `:154`

- 🔗 [Save](#save-gocliinternalagentframeworkscommonmanifest_managergo78) `:78`

- 🔗 [Validate](#validate-gocliinternalagentframeworkscommonmanifest_managergo101) `:101`


</details>


[function] name: Load file: go/cli/internal/agent/frameworks/common/manifest_manager.go:53 returns_error: да description: Load reads and parses the kagent.yaml file


### Load (go/cli/internal/agent/frameworks/common/manifest_manager.go:53)


Load reads and parses the kagent.yaml file


```go
func (m *Manager) Load((*AgentManifest, error)) (*AgentManifest, error)
```


**Тип запроса:** AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgentManifest`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/manifest_manager.go:53`



---


[function] name: NewManifestManager file: go/cli/internal/agent/frameworks/common/manifest_manager.go:46 returns_error: нет description: NewManifestManager creates a new manifest manager for the given project root


### NewManifestManager (go/cli/internal/agent/frameworks/common/manifest_manager.go:46)


NewManifestManager creates a new manifest manager for the given project root


```go
func NewManifestManager((projectRoot string)) (projectRoot string)
```


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/manifest_manager.go:46`



---


[function] name: NewProjectManifest file: go/cli/internal/agent/frameworks/common/manifest_manager.go:154 returns_error: нет description: NewProjectManifest creates a new AgentManifest with the given values


### NewProjectManifest (go/cli/internal/agent/frameworks/common/manifest_manager.go:154)


NewProjectManifest creates a new AgentManifest with the given values


```go
func NewProjectManifest((agentName, language, framework, modelProvider, modelName, description string, mcpServers []McpServerType)) (agentName, language, framework, modelProvider, modelName, description string, mcpServers []McpServerType)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** language


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** modelProvider


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/modelproviderconfig.go`


**Тип ответа:** modelName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcpServers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/manifest_manager.go:154`



---


[function] name: Save file: go/cli/internal/agent/frameworks/common/manifest_manager.go:78 returns_error: нет description: Save writes the manifest to kagent.yaml


### Save (go/cli/internal/agent/frameworks/common/manifest_manager.go:78)


Save writes the manifest to kagent.yaml


```go
func (m *Manager) Save((manifest *AgentManifest)) (manifest *AgentManifest)
```


**Тип запроса:** AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/manifest_manager.go:78`



---


[function] name: Validate file: go/cli/internal/agent/frameworks/common/manifest_manager.go:101 returns_error: нет description: Validate checks if the manifest is valid


### Validate (go/cli/internal/agent/frameworks/common/manifest_manager.go:101)


Validate checks if the manifest is valid


```go
func (m *Manager) Validate((manifest *AgentManifest)) (manifest *AgentManifest)
```


**Тип запроса:** AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/agent/frameworks/common/manifest_manager.go:101`




## go/cli/internal/agent/frameworks/frameworks.go


📄 Исходный файл: `go/cli/internal/agent/frameworks/frameworks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewGenerator](#newgenerator-gocliinternalagentframeworksframeworksgo15) `:15`


</details>


[function] name: NewGenerator file: go/cli/internal/agent/frameworks/frameworks.go:15 returns_error: да description: NewGenerator creates a new generator for the specified framework and language


### NewGenerator (go/cli/internal/agent/frameworks/frameworks.go:15)


NewGenerator creates a new generator for the specified framework and language


```go
func NewGenerator((Generator, error)) (Generator, error)
```


**Тип ответа:** Generator


```json
{
  "TemplateFiles": {},
  "TemplateRoot": "string"
}
```


*Определено в:* `go/cli/internal/common/generator/base.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Generator`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/agent/frameworks/frameworks.go:15`




## go/cli/internal/cli/agent/add_mcp.go


📄 Исходный файл: `go/cli/internal/cli/agent/add_mcp.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddMcpCmd](#addmcpcmd-gocliinternalcliagentadd_mcpgo41) `:41`

- 🔗 [ensureMcpServerDirectories](#ensuremcpserverdirectories-gocliinternalcliagentadd_mcpgo139) `:139`

- 🔗 [parseKeyValuePairs](#parsekeyvaluepairs-gocliinternalcliagentadd_mcpgo196) `:196`


</details>


[function] name: AddMcpCmd file: go/cli/internal/cli/agent/add_mcp.go:41 returns_error: нет description: AddMcpCmd runs the interactive flow to append an MCP server to kagent.yaml


### AddMcpCmd (go/cli/internal/cli/agent/add_mcp.go:41)


AddMcpCmd runs the interactive flow to append an MCP server to kagent.yaml


```go
func AddMcpCmd((cfg *AddMcpCfg)) (cfg *AddMcpCfg)
```


**Тип запроса:** AddMcpCfg


```json
{
  "ProjectDir": "string",
  "Config": null,
  "Name": "string",
  "RemoteURL": "string",
  "Headers": [],
  "Command": "string",
  "Args": [],
  "Env": [],
  "Image": "string",
  "Build": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/add_mcp.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AddMcpCfg


```json
{
  "ProjectDir": "string",
  "Config": null,
  "Name": "string",
  "RemoteURL": "string",
  "Headers": [],
  "Command": "string",
  "Args": [],
  "Env": [],
  "Image": "string",
  "Build": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/add_mcp.go`


📍 *Расположение:* `go/cli/internal/cli/agent/add_mcp.go:41`



---


[function] name: ensureMcpServerDirectories file: go/cli/internal/cli/agent/add_mcp.go:139 returns_error: нет description: —


### ensureMcpServerDirectories (go/cli/internal/cli/agent/add_mcp.go:139)


ensureMcpServerDirectories is a function that performs operations based on the provided parameters and returns (projectDir string, manifest *common.AgentManifest, verbose bool).


```go
func ensureMcpServerDirectories((projectDir string, manifest *common.AgentManifest, verbose bool)) (projectDir string, manifest *common.AgentManifest, verbose bool)
```


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/add_mcp.go:139`



---


[function] name: parseKeyValuePairs file: go/cli/internal/cli/agent/add_mcp.go:196 returns_error: нет description: parseKeyValuePairs parses KEY=VALUE pairs from a string slice


### parseKeyValuePairs (go/cli/internal/cli/agent/add_mcp.go:196)


parseKeyValuePairs parses KEY=VALUE pairs from a string slice


```go
func parseKeyValuePairs((pairs []string)) (pairs []string)
```


**Тип ответа:** pairs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/add_mcp.go:196`




## go/cli/internal/cli/agent/bug_report.go


📄 Исходный файл: `go/cli/internal/cli/agent/bug_report.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [BugReportCmd](#bugreportcmd-gocliinternalcliagentbug_reportgo14) `:14`


</details>


[function] name: BugReportCmd file: go/cli/internal/cli/agent/bug_report.go:14 returns_error: нет description: —


### BugReportCmd (go/cli/internal/cli/agent/bug_report.go:14)


BugReportCmd is a function that performs operations based on the provided parameters and returns (cfg *config.Config).


```go
func BugReportCmd((cfg *config.Config)) (cfg *config.Config)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


📍 *Расположение:* `go/cli/internal/cli/agent/bug_report.go:14`




## go/cli/internal/cli/agent/build.go


📄 Исходный файл: `go/cli/internal/cli/agent/build.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [BuildCmd](#buildcmd-gocliinternalcliagentbuildgo24) `:24`

- 🔗 [buildMcpServerImages](#buildmcpserverimages-gocliinternalcliagentbuildgo127) `:127`

- 🔗 [constructImageName](#constructimagename-gocliinternalcliagentbuildgo90) `:90`

- 🔗 [constructMcpServerImageName](#constructmcpserverimagename-gocliinternalcliagentbuildgo197) `:197`

- 🔗 [getAgentNameFromManifest](#getagentnamefrommanifest-gocliinternalcliagentbuildgo103) `:103`

- 🔗 [getManifestFromProjectDir](#getmanifestfromprojectdir-gocliinternalcliagentbuildgo116) `:116`

- 🔗 [pushMcpServerImages](#pushmcpserverimages-gocliinternalcliagentbuildgo167) `:167`


</details>


[function] name: BuildCmd file: go/cli/internal/cli/agent/build.go:24 returns_error: нет description: BuildCmd builds a Docker image for an agent project


### BuildCmd (go/cli/internal/cli/agent/build.go:24)


BuildCmd builds a Docker image for an agent project


```go
func BuildCmd((cfg *BuildCfg)) (cfg *BuildCfg)
```


**Тип запроса:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


📍 *Расположение:* `go/cli/internal/cli/agent/build.go:24`



---


[function] name: buildMcpServerImages file: go/cli/internal/cli/agent/build.go:127 returns_error: нет description: buildMcpServerImages builds Docker images for each MCP server


### buildMcpServerImages (go/cli/internal/cli/agent/build.go:127)


buildMcpServerImages builds Docker images for each MCP server


```go
func buildMcpServerImages((cfg *BuildCfg, manifest *common.AgentManifest)) (cfg *BuildCfg, manifest *common.AgentManifest)
```


**Тип запроса:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/build.go:127`



---


[function] name: constructImageName file: go/cli/internal/cli/agent/build.go:90 returns_error: нет description: constructImageName constructs the full image name from the provided image or defaults


### constructImageName (go/cli/internal/cli/agent/build.go:90)


constructImageName constructs the full image name from the provided image or defaults


```go
func constructImageName((cfg *BuildCfg)) (cfg *BuildCfg)
```


**Тип запроса:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


📍 *Расположение:* `go/cli/internal/cli/agent/build.go:90`



---


[function] name: constructMcpServerImageName file: go/cli/internal/cli/agent/build.go:197 returns_error: нет description: constructMcpServerImageName constructs the MCP server image name


### constructMcpServerImageName (go/cli/internal/cli/agent/build.go:197)


constructMcpServerImageName constructs the MCP server image name


```go
func constructMcpServerImageName((cfg *BuildCfg, serverName string)) (cfg *BuildCfg, serverName string)
```


**Тип запроса:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/build.go:197`



---


[function] name: getAgentNameFromManifest file: go/cli/internal/cli/agent/build.go:103 returns_error: нет description: getAgentNameFromManifest attempts to load the agent name from kagent.yaml


### getAgentNameFromManifest (go/cli/internal/cli/agent/build.go:103)


getAgentNameFromManifest attempts to load the agent name from kagent.yaml


```go
func getAgentNameFromManifest((projectDir string)) (projectDir string)
```


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/build.go:103`



---


[function] name: getManifestFromProjectDir file: go/cli/internal/cli/agent/build.go:116 returns_error: нет description: getManifestFromProjectDir loads the agent manifest from the project directory


### getManifestFromProjectDir (go/cli/internal/cli/agent/build.go:116)


getManifestFromProjectDir loads the agent manifest from the project directory


```go
func getManifestFromProjectDir((projectDir string)) (projectDir string)
```


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/build.go:116`



---


[function] name: pushMcpServerImages file: go/cli/internal/cli/agent/build.go:167 returns_error: нет description: pushMcpServerImages pushes the MCP server Docker images to the specified registry


### pushMcpServerImages (go/cli/internal/cli/agent/build.go:167)


pushMcpServerImages pushes the MCP server Docker images to the specified registry


```go
func pushMcpServerImages((cfg *BuildCfg, manifest *common.AgentManifest)) (cfg *BuildCfg, manifest *common.AgentManifest)
```


**Тип запроса:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BuildCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "Push": false,
  "Platform": "string",
  "Config": null,
  "SkipMCPServers": false
}
```


*Определено в:* `go/cli/internal/cli/agent/build.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/build.go:167`




## go/cli/internal/cli/agent/const.go


📄 Исходный файл: `go/cli/internal/cli/agent/const.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetEnvVarWithDefault](#getenvvarwithdefault-gocliinternalcliagentconstgo60) `:60`

- 🔗 [GetModelProvider](#getmodelprovider-gocliinternalcliagentconstgo17) `:17`

- 🔗 [GetModelProviderHelmValuesKey](#getmodelproviderhelmvalueskey-gocliinternalcliagentconstgo37) `:37`

- 🔗 [GetProviderAPIKey](#getproviderapikey-gocliinternalcliagentconstgo46) `:46`


</details>


[function] name: GetEnvVarWithDefault file: go/cli/internal/cli/agent/const.go:60 returns_error: нет description: GetEnvVarWithDefault returns the value of the environment variable if it exists, otherwise returns the default value


### GetEnvVarWithDefault (go/cli/internal/cli/agent/const.go:60)


GetEnvVarWithDefault returns the value of the environment variable if it exists, otherwise returns the default value


```go
func GetEnvVarWithDefault((envVar, defaultValue string)) (envVar, defaultValue string)
```


**Тип ответа:** envVar


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** defaultValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/const.go:60`



---


[function] name: GetModelProvider file: go/cli/internal/cli/agent/const.go:17 returns_error: нет description: GetModelProvider returns the model provider from KAGENT_DEFAULT_MODEL_PROVIDER environment variable


### GetModelProvider (go/cli/internal/cli/agent/const.go:17)


GetModelProvider returns the model provider from KAGENT_DEFAULT_MODEL_PROVIDER environment variable


```go
func GetModelProvider(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/agent/const.go:17`



---


[function] name: GetModelProviderHelmValuesKey file: go/cli/internal/cli/agent/const.go:37 returns_error: нет description: GetModelProviderHelmValuesKey returns the helm values key for the model provider with lowercased name


### GetModelProviderHelmValuesKey (go/cli/internal/cli/agent/const.go:37)


GetModelProviderHelmValuesKey returns the helm values key for the model provider with lowercased name


```go
func GetModelProviderHelmValuesKey((provider v1alpha2.ModelProvider)) (provider v1alpha2.ModelProvider)
```


**Тип ответа:** provider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/cli/internal/cli/agent/const.go:37`



---


[function] name: GetProviderAPIKey file: go/cli/internal/cli/agent/const.go:46 returns_error: нет description: GetProviderAPIKey returns API_KEY env var name from provider type


### GetProviderAPIKey (go/cli/internal/cli/agent/const.go:46)


GetProviderAPIKey returns API_KEY env var name from provider type


```go
func GetProviderAPIKey((provider v1alpha2.ModelProvider)) (provider v1alpha2.ModelProvider)
```


**Тип ответа:** provider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/cli/internal/cli/agent/const.go:46`




## go/cli/internal/cli/agent/dashboard.go


📄 Исходный файл: `go/cli/internal/cli/agent/dashboard.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DashboardCmd](#dashboardcmd-gocliinternalcliagentdashboardgo13) `:13`


</details>


[function] name: DashboardCmd file: go/cli/internal/cli/agent/dashboard.go:13 returns_error: нет description: —


### DashboardCmd (go/cli/internal/cli/agent/dashboard.go:13)


DashboardCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cfg *config.Config).


```go
func DashboardCmd((ctx context.Context, cfg *config.Config)) (ctx context.Context, cfg *config.Config)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


📍 *Расположение:* `go/cli/internal/cli/agent/dashboard.go:13`




## go/cli/internal/cli/agent/dashboard_darwin.go


📄 Исходный файл: `go/cli/internal/cli/agent/dashboard_darwin.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DashboardCmd](#dashboardcmd-gocliinternalcliagentdashboard_darwingo16) `:16`


</details>


[function] name: DashboardCmd file: go/cli/internal/cli/agent/dashboard_darwin.go:16 returns_error: нет description: —


### DashboardCmd (go/cli/internal/cli/agent/dashboard_darwin.go:16)


DashboardCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cfg *config.Config).


```go
func DashboardCmd((ctx context.Context, cfg *config.Config)) (ctx context.Context, cfg *config.Config)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


📍 *Расположение:* `go/cli/internal/cli/agent/dashboard_darwin.go:16`




## go/cli/internal/cli/agent/deploy.go


📄 Исходный файл: `go/cli/internal/cli/agent/deploy.go`


<details open>
<summary><b>Функции в этом файле (43)</b></summary>


- 🔗 [DeployCmd](#deploycmd-gocliinternalcliagentdeploygo72) `:72`

- 🔗 [buildAgentCRD](#buildagentcrd-gocliinternalcliagentdeploygo667) `:667`

- 🔗 [buildAndPushImage](#buildandpushimage-gocliinternalcliagentdeploygo150) `:150`

- 🔗 [buildCommandMCPServer](#buildcommandmcpserver-gocliinternalcliagentdeploygo875) `:875`

- 🔗 [buildRemoteMCPServer](#buildremotemcpserver-gocliinternalcliagentdeploygo786) `:786`

- 🔗 [buildSecret](#buildsecret-gocliinternalcliagentdeploygo600) `:600`

- 🔗 [createAgentCRD](#createagentcrd-gocliinternalcliagentdeploygo648) `:648`

- 🔗 [createEnvFileSecret](#createenvfilesecret-gocliinternalcliagentdeploygo391) `:391`

- 🔗 [createKubernetesClient](#createkubernetesclient-gocliinternalcliagentdeploygo557) `:557`

- 🔗 [createOrUpdateAgent](#createorupdateagent-gocliinternalcliagentdeploygo712) `:712`

- 🔗 [createOrUpdateEnvSecret](#createorupdateenvsecret-gocliinternalcliagentdeploygo1085) `:1085`

- 🔗 [createOrUpdateMCPServer](#createorupdatemcpserver-gocliinternalcliagentdeploygo899) `:899`

- 🔗 [createOrUpdateRemoteMCPServer](#createorupdateremotemcpserver-gocliinternalcliagentdeploygo811) `:811`

- 🔗 [createOrUpdateSecret](#createorupdatesecret-gocliinternalcliagentdeploygo615) `:615`

- 🔗 [createSecret](#createsecret-gocliinternalcliagentdeploygo589) `:589`

- 🔗 [createSecretsForEnv](#createsecretsforenv-gocliinternalcliagentdeploygo1003) `:1003`

- 🔗 [createSecretsForHeaders](#createsecretsforheaders-gocliinternalcliagentdeploygo929) `:929`

- 🔗 [deployCommandMCPServer](#deploycommandmcpserver-gocliinternalcliagentdeploygo841) `:841`

- 🔗 [deployMCPServers](#deploymcpservers-gocliinternalcliagentdeploygo742) `:742`

- 🔗 [deployMCPServersIfNeeded](#deploymcpserversifneeded-gocliinternalcliagentdeploygo504) `:504`

- 🔗 [deployRemoteMCPServer](#deployremotemcpserver-gocliinternalcliagentdeploygo770) `:770`

- 🔗 [determineCommandMCPServerImage](#determinecommandmcpserverimage-gocliinternalcliagentdeploygo859) `:859`

- 🔗 [determineImageName](#determineimagename-gocliinternalcliagentdeploygo662) `:662`

- 🔗 [extractEnvVarName](#extractenvvarname-gocliinternalcliagentdeploygo985) `:985`

- 🔗 [extractEnvVarsFromManifest](#extractenvvarsfrommanifest-gocliinternalcliagentdeploygo208) `:208`

- 🔗 [getAPIKeyEnvVar](#getapikeyenvvar-gocliinternalcliagentdeploygo543) `:543`

- 🔗 [handleEnvFileSecret](#handleenvfilesecret-gocliinternalcliagentdeploygo317) `:317`

- 🔗 [outputEnvSecret](#outputenvsecret-gocliinternalcliagentdeploygo1069) `:1069`

- 🔗 [outputYAML](#outputyaml-gocliinternalcliagentdeploygo531) `:531`

- 🔗 [parseEnvFile](#parseenvfile-gocliinternalcliagentdeploygo344) `:344`

- 🔗 [parseEnvVar](#parseenvvar-gocliinternalcliagentdeploygo1050) `:1050`

- 🔗 [printDeploymentResult](#printdeploymentresult-gocliinternalcliagentdeploygo521) `:521`

- 🔗 [processHeaderValue](#processheadervalue-gocliinternalcliagentdeploygo945) `:945`

- 🔗 [promptUserConfirmation](#promptuserconfirmation-gocliinternalcliagentdeploygo256) `:256`

- 🔗 [resolveEnvVarReference](#resolveenvvarreference-gocliinternalcliagentdeploygo1059) `:1059`

- 🔗 [restartAgentDeployment](#restartagentdeployment-gocliinternalcliagentdeploygo473) `:473`

- 🔗 [sanitizeForSecretKey](#sanitizeforsecretkey-gocliinternalcliagentdeploygo998) `:998`

- 🔗 [sanitizeForSecretName](#sanitizeforsecretname-gocliinternalcliagentdeploygo993) `:993`

- 🔗 [setupKubernetesEnvironment](#setupkubernetesenvironment-gocliinternalcliagentdeploygo187) `:187`

- 🔗 [validateAndLoadProject](#validateandloadproject-gocliinternalcliagentdeploygo132) `:132`

- 🔗 [validateAndPromptEnvVars](#validateandpromptenvvars-gocliinternalcliagentdeploygo272) `:272`

- 🔗 [validateDeploymentRequirements](#validatedeploymentrequirements-gocliinternalcliagentdeploygo173) `:173`

- 🔗 [waitForDeployment](#waitfordeployment-gocliinternalcliagentdeploygo439) `:439`


</details>


[function] name: DeployCmd file: go/cli/internal/cli/agent/deploy.go:72 returns_error: нет description: DeployCmd deploys an agent to Kubernetes


### DeployCmd (go/cli/internal/cli/agent/deploy.go:72)


DeployCmd deploys an agent to Kubernetes


```go
func DeployCmd((ctx context.Context, cfg *DeployCfg)) (ctx context.Context, cfg *DeployCfg)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:72`



---


[function] name: buildAgentCRD file: go/cli/internal/cli/agent/deploy.go:667 returns_error: нет description: buildAgentCRD constructs an Agent CRD object


### buildAgentCRD (go/cli/internal/cli/agent/deploy.go:667)


buildAgentCRD constructs an Agent CRD object


```go
func buildAgentCRD((namespace string, manifest *common.AgentManifest, imageName string, envData *envFileData)) (namespace string, manifest *common.AgentManifest, imageName string, envData *envFileData)
```


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип запроса:** envFileData


```json
{
  "SecretName": "string",
  "EnvVarKeys": []
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** envData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** envFileData


```json
{
  "SecretName": "string",
  "EnvVarKeys": []
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:667`



---


[function] name: buildAndPushImage file: go/cli/internal/cli/agent/deploy.go:150 returns_error: нет description: buildAndPushImage builds and pushes the Docker image (skipped in dry-run mode)


### buildAndPushImage (go/cli/internal/cli/agent/deploy.go:150)


buildAndPushImage builds and pushes the Docker image (skipped in dry-run mode)


```go
func buildAndPushImage((cfg *DeployCfg)) (cfg *DeployCfg)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:150`



---


[function] name: buildCommandMCPServer file: go/cli/internal/cli/agent/deploy.go:875 returns_error: нет description: buildCommandMCPServer constructs an MCPServer CRD object


### buildCommandMCPServer (go/cli/internal/cli/agent/deploy.go:875)


buildCommandMCPServer constructs an MCPServer CRD object


```go
func buildCommandMCPServer((namespace string, mcpServer *common.McpServerType, image string, envMap map[string]string, secretRefs []corev1.LocalObjectReference)) (namespace string, mcpServer *common.McpServerType, image string, envMap map[string]string, secretRefs []corev1.LocalObjectReference)
```


**Тип запроса:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


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


**Тип ответа:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** image


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** envMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** secretRefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.LocalObjectReference


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:875`



---


[function] name: buildRemoteMCPServer file: go/cli/internal/cli/agent/deploy.go:786 returns_error: нет description: buildRemoteMCPServer constructs a RemoteMCPServer CRD object


### buildRemoteMCPServer (go/cli/internal/cli/agent/deploy.go:786)


buildRemoteMCPServer constructs a RemoteMCPServer CRD object


```go
func buildRemoteMCPServer((namespace string, mcpServer *common.McpServerType, headerRefs []v1alpha2.ValueRef)) (namespace string, mcpServer *common.McpServerType, headerRefs []v1alpha2.ValueRef)
```


**Тип запроса:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


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


**Тип ответа:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** headerRefs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.ValueRef


```json
{
  "Name": "string",
  "Value": "string",
  "ValueFrom": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:786`



---


[function] name: buildSecret file: go/cli/internal/cli/agent/deploy.go:600 returns_error: нет description: buildSecret constructs a Kubernetes Secret object


### buildSecret (go/cli/internal/cli/agent/deploy.go:600)


buildSecret constructs a Kubernetes Secret object


```go
func buildSecret((namespace, name, key, value string)) (namespace, name, key, value string)
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


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:600`



---


[function] name: createAgentCRD file: go/cli/internal/cli/agent/deploy.go:648 returns_error: нет description: createAgentCRD creates or updates the Agent CRD


### createAgentCRD (go/cli/internal/cli/agent/deploy.go:648)


createAgentCRD creates or updates the Agent CRD


```go
func createAgentCRD((ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest, envData *envFileData, verbose bool)) (ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest, envData *envFileData, verbose bool)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип запроса:** envFileData


```json
{
  "SecretName": "string",
  "EnvVarKeys": []
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** envData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** envFileData


```json
{
  "SecretName": "string",
  "EnvVarKeys": []
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:648`



---


[function] name: createEnvFileSecret file: go/cli/internal/cli/agent/deploy.go:391 returns_error: нет description: createEnvFileSecret creates a Kubernetes secret from env file variables


### createEnvFileSecret (go/cli/internal/cli/agent/deploy.go:391)


createEnvFileSecret creates a Kubernetes secret from env file variables


```go
func createEnvFileSecret((ctx context.Context, k8sClient client.Client, namespace, secretName string, envVars map[string]string, verbose bool, dryRun bool)) (ctx context.Context, k8sClient client.Client, namespace, secretName string, envVars map[string]string, verbose bool, dryRun bool)
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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** secretName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** envVars


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dryRun


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:391`



---


[function] name: createKubernetesClient file: go/cli/internal/cli/agent/deploy.go:557 returns_error: да description: createKubernetesClient creates a Kubernetes client


### createKubernetesClient (go/cli/internal/cli/agent/deploy.go:557)


createKubernetesClient creates a Kubernetes client


```go
func createKubernetesClient((client.Client, error)) (client.Client, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `client.Client`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:557`



---


[function] name: createOrUpdateAgent file: go/cli/internal/cli/agent/deploy.go:712 returns_error: нет description: createOrUpdateAgent creates a new agent or updates an existing one


### createOrUpdateAgent (go/cli/internal/cli/agent/deploy.go:712)


createOrUpdateAgent creates a new agent or updates an existing one


```go
func createOrUpdateAgent((ctx context.Context, k8sClient client.Client, agent *v1alpha2.Agent, namespace, name string, verbose bool)) (ctx context.Context, k8sClient client.Client, agent *v1alpha2.Agent, namespace, name string, verbose bool)
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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:712`



---


[function] name: createOrUpdateEnvSecret file: go/cli/internal/cli/agent/deploy.go:1085 returns_error: нет description: createOrUpdateEnvSecret creates or updates a secret containing multiple environment variables


### createOrUpdateEnvSecret (go/cli/internal/cli/agent/deploy.go:1085)


createOrUpdateEnvSecret creates or updates a secret containing multiple environment variables


```go
func createOrUpdateEnvSecret((ctx context.Context, k8sClient client.Client, namespace, secretName string, secretData map[string][]byte, verbose bool)) (ctx context.Context, k8sClient client.Client, namespace, secretName string, secretData map[string][]byte, verbose bool)
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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** secretName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** secretData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:1085`



---


[function] name: createOrUpdateMCPServer file: go/cli/internal/cli/agent/deploy.go:899 returns_error: нет description: createOrUpdateMCPServer creates a new MCPServer or updates an existing one


### createOrUpdateMCPServer (go/cli/internal/cli/agent/deploy.go:899)


createOrUpdateMCPServer creates a new MCPServer or updates an existing one


```go
func createOrUpdateMCPServer((ctx context.Context, k8sClient client.Client, mcpServerResource *v1alpha1.MCPServer, namespace, name string, verbose bool)) (ctx context.Context, k8sClient client.Client, mcpServerResource *v1alpha1.MCPServer, namespace, name string, verbose bool)
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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** mcpServerResource


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


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


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:899`



---


[function] name: createOrUpdateRemoteMCPServer file: go/cli/internal/cli/agent/deploy.go:811 returns_error: нет description: createOrUpdateRemoteMCPServer creates a new RemoteMCPServer or updates an existing one


### createOrUpdateRemoteMCPServer (go/cli/internal/cli/agent/deploy.go:811)


createOrUpdateRemoteMCPServer creates a new RemoteMCPServer or updates an existing one


```go
func createOrUpdateRemoteMCPServer((ctx context.Context, k8sClient client.Client, remoteMCPServer *v1alpha2.RemoteMCPServer, namespace, name string, verbose bool)) (ctx context.Context, k8sClient client.Client, remoteMCPServer *v1alpha2.RemoteMCPServer, namespace, name string, verbose bool)
```


**Тип запроса:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** remoteMCPServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha2.RemoteMCPServer


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `go/api/v1alpha2/remotemcpserver_types.go`


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


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:811`



---


[function] name: createOrUpdateSecret file: go/cli/internal/cli/agent/deploy.go:615 returns_error: нет description: createOrUpdateSecret creates a new secret or updates an existing one


### createOrUpdateSecret (go/cli/internal/cli/agent/deploy.go:615)


createOrUpdateSecret creates a new secret or updates an existing one


```go
func createOrUpdateSecret((ctx context.Context, k8sClient client.Client, secret *corev1.Secret, key, value string, verbose bool)) (ctx context.Context, k8sClient client.Client, secret *corev1.Secret, key, value string, verbose bool)
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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:615`



---


[function] name: createSecret file: go/cli/internal/cli/agent/deploy.go:589 returns_error: нет description: createSecret creates or updates a Kubernetes secret with the specified key-value pair


### createSecret (go/cli/internal/cli/agent/deploy.go:589)


createSecret creates or updates a Kubernetes secret with the specified key-value pair


```go
func createSecret((ctx context.Context, k8sClient client.Client, namespace, secretName, key, value string, verbose bool, dryRun bool)) (ctx context.Context, k8sClient client.Client, namespace, secretName, key, value string, verbose bool, dryRun bool)
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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** secretName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dryRun


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:589`



---


[function] name: createSecretsForEnv file: go/cli/internal/cli/agent/deploy.go:1003 returns_error: да description: createSecretsForEnv creates secrets for environment variables and returns env map and secret refs


### createSecretsForEnv (go/cli/internal/cli/agent/deploy.go:1003)


createSecretsForEnv creates secrets for environment variables and returns env map and secret refs


```go
func createSecretsForEnv((map[string]string, []corev1.LocalObjectReference, error)) (map[string]string, []corev1.LocalObjectReference, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.LocalObjectReference


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `[]corev1.LocalObjectReference`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:1003`



---


[function] name: createSecretsForHeaders file: go/cli/internal/cli/agent/deploy.go:929 returns_error: да description: createSecretsForHeaders creates secrets for header values that reference environment variables


### createSecretsForHeaders (go/cli/internal/cli/agent/deploy.go:929)


createSecretsForHeaders creates secrets for header values that reference environment variables


```go
func createSecretsForHeaders(([]v1alpha2.ValueRef, error)) ([]v1alpha2.ValueRef, error)
```


**Тип ответа:** v1alpha2.ValueRef


```json
{
  "Name": "string",
  "Value": "string",
  "ValueFrom": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]v1alpha2.ValueRef`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:929`



---


[function] name: deployCommandMCPServer file: go/cli/internal/cli/agent/deploy.go:841 returns_error: нет description: deployCommandMCPServer creates or updates an MCPServer resource for command/stdio type


### deployCommandMCPServer (go/cli/internal/cli/agent/deploy.go:841)


deployCommandMCPServer creates or updates an MCPServer resource for command/stdio type


```go
func deployCommandMCPServer((ctx context.Context, k8sClient client.Client, namespace string, mcpServer *common.McpServerType, verbose bool, dryRun bool)) (ctx context.Context, k8sClient client.Client, namespace string, mcpServer *common.McpServerType, verbose bool, dryRun bool)
```


**Тип запроса:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


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


**Тип ответа:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dryRun


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:841`



---


[function] name: deployMCPServers file: go/cli/internal/cli/agent/deploy.go:742 returns_error: нет description: deployMCPServers deploys all MCP servers defined in the manifest


### deployMCPServers (go/cli/internal/cli/agent/deploy.go:742)


deployMCPServers deploys all MCP servers defined in the manifest


```go
func deployMCPServers((ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest)) (ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:742`



---


[function] name: deployMCPServersIfNeeded file: go/cli/internal/cli/agent/deploy.go:504 returns_error: нет description: deployMCPServersIfNeeded deploys MCP servers if any are defined in the manifest


### deployMCPServersIfNeeded (go/cli/internal/cli/agent/deploy.go:504)


deployMCPServersIfNeeded deploys MCP servers if any are defined in the manifest


```go
func deployMCPServersIfNeeded((ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest)) (ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:504`



---


[function] name: deployRemoteMCPServer file: go/cli/internal/cli/agent/deploy.go:770 returns_error: нет description: deployRemoteMCPServer creates or updates a RemoteMCPServer resource


### deployRemoteMCPServer (go/cli/internal/cli/agent/deploy.go:770)


deployRemoteMCPServer creates or updates a RemoteMCPServer resource


```go
func deployRemoteMCPServer((ctx context.Context, k8sClient client.Client, namespace string, mcpServer *common.McpServerType, verbose bool, dryRun bool)) (ctx context.Context, k8sClient client.Client, namespace string, mcpServer *common.McpServerType, verbose bool, dryRun bool)
```


**Тип запроса:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


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


**Тип ответа:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dryRun


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:770`



---


[function] name: determineCommandMCPServerImage file: go/cli/internal/cli/agent/deploy.go:859 returns_error: нет description: determineCommandMCPServerImage returns the appropriate Docker image based on the command


### determineCommandMCPServerImage (go/cli/internal/cli/agent/deploy.go:859)


determineCommandMCPServerImage returns the appropriate Docker image based on the command


```go
func determineCommandMCPServerImage((mcpServer *common.McpServerType)) (mcpServer *common.McpServerType)
```


**Тип запроса:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


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


**Тип ответа:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:859`



---


[function] name: determineImageName file: go/cli/internal/cli/agent/deploy.go:662 returns_error: нет description: determineImageName returns the image name to use, either from config or default


### determineImageName (go/cli/internal/cli/agent/deploy.go:662)


determineImageName returns the image name to use, either from config or default


```go
func determineImageName((configImage, agentName string)) (configImage, agentName string)
```


**Тип ответа:** configImage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:662`



---


[function] name: extractEnvVarName file: go/cli/internal/cli/agent/deploy.go:985 returns_error: нет description: extractEnvVarName extracts the environment variable name from regex matches


### extractEnvVarName (go/cli/internal/cli/agent/deploy.go:985)


extractEnvVarName extracts the environment variable name from regex matches


```go
func extractEnvVarName((matches []string)) (matches []string)
```


**Тип ответа:** matches


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:985`



---


[function] name: extractEnvVarsFromManifest file: go/cli/internal/cli/agent/deploy.go:208 returns_error: нет description: extractEnvVarsFromManifest extracts all environment variable references from the manifest


### extractEnvVarsFromManifest (go/cli/internal/cli/agent/deploy.go:208)


extractEnvVarsFromManifest extracts all environment variable references from the manifest


```go
func extractEnvVarsFromManifest((manifest *common.AgentManifest)) (manifest *common.AgentManifest)
```


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:208`



---


[function] name: getAPIKeyEnvVar file: go/cli/internal/cli/agent/deploy.go:543 returns_error: нет description: getAPIKeyEnvVar returns the environment variable name for the given model provider


### getAPIKeyEnvVar (go/cli/internal/cli/agent/deploy.go:543)


getAPIKeyEnvVar returns the environment variable name for the given model provider


```go
func getAPIKeyEnvVar((modelProvider string)) (modelProvider string)
```


**Тип ответа:** modelProvider


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/modelproviderconfig.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:543`



---


[function] name: handleEnvFileSecret file: go/cli/internal/cli/agent/deploy.go:317 returns_error: да description: handleEnvFileSecret manages environment file secret creation


### handleEnvFileSecret (go/cli/internal/cli/agent/deploy.go:317)


handleEnvFileSecret manages environment file secret creation


```go
func handleEnvFileSecret((*envFileData, error)) (*envFileData, error)
```


**Тип запроса:** envFileData


```json
{
  "SecretName": "string",
  "EnvVarKeys": []
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** envFileData


```json
{
  "SecretName": "string",
  "EnvVarKeys": []
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*envFileData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:317`



---


[function] name: outputEnvSecret file: go/cli/internal/cli/agent/deploy.go:1069 returns_error: нет description: outputEnvSecret outputs a secret containing environment variables (for dry-run mode)


### outputEnvSecret (go/cli/internal/cli/agent/deploy.go:1069)


outputEnvSecret outputs a secret containing environment variables (for dry-run mode)


```go
func outputEnvSecret((namespace, secretName string, secretData map[string][]byte)) (namespace, secretName string, secretData map[string][]byte)
```


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** secretName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** secretData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:1069`



---


[function] name: outputYAML file: go/cli/internal/cli/agent/deploy.go:531 returns_error: нет description: outputYAML serializes a Kubernetes object to YAML and prints it (for dry-run mode)


### outputYAML (go/cli/internal/cli/agent/deploy.go:531)


outputYAML serializes a Kubernetes object to YAML and prints it (for dry-run mode)


```go
func outputYAML((obj client.Object)) (obj client.Object)
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


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:531`



---


[function] name: parseEnvFile file: go/cli/internal/cli/agent/deploy.go:344 returns_error: да description: parseEnvFile reads and parses a .env file, returning a map of environment variables


### parseEnvFile (go/cli/internal/cli/agent/deploy.go:344)


parseEnvFile reads and parses a .env file, returning a map of environment variables


```go
func parseEnvFile((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:344`



---


[function] name: parseEnvVar file: go/cli/internal/cli/agent/deploy.go:1050 returns_error: да description: parseEnvVar parses an environment variable in KEY=VALUE format


### parseEnvVar (go/cli/internal/cli/agent/deploy.go:1050)


parseEnvVar parses an environment variable in KEY=VALUE format


```go
func parseEnvVar((key, value string, err error)) (key, value string, err error)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `key`, `value string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:1050`



---


[function] name: printDeploymentResult file: go/cli/internal/cli/agent/deploy.go:521 returns_error: нет description: printDeploymentResult prints the appropriate success/dry-run message


### printDeploymentResult (go/cli/internal/cli/agent/deploy.go:521)


printDeploymentResult prints the appropriate success/dry-run message


```go
func printDeploymentResult((cfg *DeployCfg, manifest *common.AgentManifest)) (cfg *DeployCfg, manifest *common.AgentManifest)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:521`



---


[function] name: processHeaderValue file: go/cli/internal/cli/agent/deploy.go:945 returns_error: да description: processHeaderValue processes a single header value and creates a secret if needed


### processHeaderValue (go/cli/internal/cli/agent/deploy.go:945)


processHeaderValue processes a single header value and creates a secret if needed


```go
func processHeaderValue((v1alpha2.ValueRef, error)) (v1alpha2.ValueRef, error)
```


**Тип ответа:** v1alpha2.ValueRef


```json
{
  "Name": "string",
  "Value": "string",
  "ValueFrom": null
}
```


*Определено в:* `go/api/v1alpha1/toolserver_types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `v1alpha2.ValueRef`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:945`



---


[function] name: promptUserConfirmation file: go/cli/internal/cli/agent/deploy.go:256 returns_error: нет description: promptUserConfirmation prompts the user with a yes/no question and returns an error if they decline


### promptUserConfirmation (go/cli/internal/cli/agent/deploy.go:256)


promptUserConfirmation prompts the user with a yes/no question and returns an error if they decline


```go
func promptUserConfirmation((message string)) (message string)
```


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:256`



---


[function] name: resolveEnvVarReference file: go/cli/internal/cli/agent/deploy.go:1059 returns_error: да description: resolveEnvVarReference resolves an environment variable reference and returns its actual value


### resolveEnvVarReference (go/cli/internal/cli/agent/deploy.go:1059)


resolveEnvVarReference resolves an environment variable reference and returns its actual value


```go
func resolveEnvVarReference((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:1059`



---


[function] name: restartAgentDeployment file: go/cli/internal/cli/agent/deploy.go:473 returns_error: нет description: restartAgentDeployment restarts the agent deployment using kubectl rollout restart


### restartAgentDeployment (go/cli/internal/cli/agent/deploy.go:473)


restartAgentDeployment restarts the agent deployment using kubectl rollout restart


```go
func restartAgentDeployment((ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest)) (ctx context.Context, k8sClient client.Client, cfg *DeployCfg, manifest *common.AgentManifest)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


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


**Тип ответа:** k8sClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:473`



---


[function] name: sanitizeForSecretKey file: go/cli/internal/cli/agent/deploy.go:998 returns_error: нет description: sanitizeForSecretKey converts a header name to a valid secret key


### sanitizeForSecretKey (go/cli/internal/cli/agent/deploy.go:998)


sanitizeForSecretKey converts a header name to a valid secret key


```go
func sanitizeForSecretKey((headerName string)) (headerName string)
```


**Тип ответа:** headerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:998`



---


[function] name: sanitizeForSecretName file: go/cli/internal/cli/agent/deploy.go:993 returns_error: нет description: sanitizeForSecretName converts a header name to a valid Kubernetes secret name


### sanitizeForSecretName (go/cli/internal/cli/agent/deploy.go:993)


sanitizeForSecretName converts a header name to a valid Kubernetes secret name


```go
func sanitizeForSecretName((headerName string)) (headerName string)
```


**Тип ответа:** headerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:993`



---


[function] name: setupKubernetesEnvironment file: go/cli/internal/cli/agent/deploy.go:187 returns_error: да description: setupKubernetesEnvironment creates Kubernetes client and sets up namespace


### setupKubernetesEnvironment (go/cli/internal/cli/agent/deploy.go:187)


setupKubernetesEnvironment creates Kubernetes client and sets up namespace


```go
func setupKubernetesEnvironment((client.Client, error)) (client.Client, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `client.Client`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:187`



---


[function] name: validateAndLoadProject file: go/cli/internal/cli/agent/deploy.go:132 returns_error: да description: validateAndLoadProject validates the project directory and loads the manifest


### validateAndLoadProject (go/cli/internal/cli/agent/deploy.go:132)


validateAndLoadProject validates the project directory and loads the manifest


```go
func validateAndLoadProject((*common.AgentManifest, error)) (*common.AgentManifest, error)
```


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*common.AgentManifest`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:132`



---


[function] name: validateAndPromptEnvVars file: go/cli/internal/cli/agent/deploy.go:272 returns_error: нет description: validateAndPromptEnvVars validates environment variables and prompts user if needed


### validateAndPromptEnvVars (go/cli/internal/cli/agent/deploy.go:272)


validateAndPromptEnvVars validates environment variables and prompts user if needed


```go
func validateAndPromptEnvVars((cfg *DeployCfg, requiredEnvVars []string, apiKeyEnvVar string)) (cfg *DeployCfg, requiredEnvVars []string, apiKeyEnvVar string)
```


**Тип запроса:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DeployCfg


```json
{
  "ProjectDir": "string",
  "Image": "string",
  "EnvFile": "string",
  "Platform": "string",
  "Config": null,
  "DryRun": false
}
```


*Определено в:* `go/cli/internal/cli/agent/deploy.go`


**Тип ответа:** requiredEnvVars


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiKeyEnvVar


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:272`



---


[function] name: validateDeploymentRequirements file: go/cli/internal/cli/agent/deploy.go:173 returns_error: да description: validateDeploymentRequirements validates deployment-specific requirements


### validateDeploymentRequirements (go/cli/internal/cli/agent/deploy.go:173)


validateDeploymentRequirements validates deployment-specific requirements


```go
func validateDeploymentRequirements((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:173`



---


[function] name: waitForDeployment file: go/cli/internal/cli/agent/deploy.go:439 returns_error: да description: waitForDeployment polls for a deployment to be created, with a timeout


### waitForDeployment (go/cli/internal/cli/agent/deploy.go:439)


waitForDeployment polls for a deployment to be created, with a timeout


```go
func waitForDeployment((*appsv1.Deployment, error)) (*appsv1.Deployment, error)
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


**Тип ответа:** appsv1.Deployment


```json
{
  "EnvVars": [],
  "Volumes": [],
  "VolumeMounts": []
}
```


*Определено в:* `go/internal/controller/translator/agent/deployments.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*appsv1.Deployment`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/deploy.go:439`




## go/cli/internal/cli/agent/format.go


📄 Исходный файл: `go/cli/internal/cli/agent/format.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [printJSON](#printjson-gocliinternalcliagentformatgo46) `:46`

- 🔗 [printOutput](#printoutput-gocliinternalcliagentformatgo20) `:20`


</details>


[function] name: printJSON file: go/cli/internal/cli/agent/format.go:46 returns_error: нет description: —


### printJSON (go/cli/internal/cli/agent/format.go:46)


printJSON is a function that performs operations based on the provided parameters and returns (data any).


```go
func printJSON((data any)) (data any)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/format.go:46`



---


[function] name: printOutput file: go/cli/internal/cli/agent/format.go:20 returns_error: нет description: —


### printOutput (go/cli/internal/cli/agent/format.go:20)


printOutput is a function that performs operations based on the provided parameters and returns (data any, tableHeaders []string, tableRows [][]string).


```go
func printOutput((data any, tableHeaders []string, tableRows [][]string)) (data any, tableHeaders []string, tableRows [][]string)
```


**Тип ответа:** data


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tableHeaders


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tableRows


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/format.go:20`




## go/cli/internal/cli/agent/get.go


📄 Исходный файл: `go/cli/internal/cli/agent/get.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [GetAgentCmd](#getagentcmd-gocliinternalcliagentgetgo17) `:17`

- 🔗 [GetSessionCmd](#getsessioncmd-gocliinternalcliagentgetgo47) `:47`

- 🔗 [GetToolCmd](#gettoolcmd-gocliinternalcliagentgetgo76) `:76`

- 🔗 [printAgents](#printagents-gocliinternalcliagentgetgo105) `:105`

- 🔗 [printSessions](#printsessions-gocliinternalcliagentgetgo122) `:122`

- 🔗 [printTools](#printtools-gocliinternalcliagentgetgo89) `:89`


</details>


[function] name: GetAgentCmd file: go/cli/internal/cli/agent/get.go:17 returns_error: нет description: —


### GetAgentCmd (go/cli/internal/cli/agent/get.go:17)


GetAgentCmd is a function that retrieves data based on the provided parameters and returns (cfg *config.Config, resourceName string).


```go
func GetAgentCmd((cfg *config.Config, resourceName string)) (cfg *config.Config, resourceName string)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/get.go:17`



---


[function] name: GetSessionCmd file: go/cli/internal/cli/agent/get.go:47 returns_error: нет description: —


### GetSessionCmd (go/cli/internal/cli/agent/get.go:47)


GetSessionCmd is a function that retrieves data based on the provided parameters and returns (cfg *config.Config, resourceName string).


```go
func GetSessionCmd((cfg *config.Config, resourceName string)) (cfg *config.Config, resourceName string)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/get.go:47`



---


[function] name: GetToolCmd file: go/cli/internal/cli/agent/get.go:76 returns_error: нет description: —


### GetToolCmd (go/cli/internal/cli/agent/get.go:76)


GetToolCmd is a function that retrieves data based on the provided parameters and returns (cfg *config.Config).


```go
func GetToolCmd((cfg *config.Config)) (cfg *config.Config)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


📍 *Расположение:* `go/cli/internal/cli/agent/get.go:76`



---


[function] name: printAgents file: go/cli/internal/cli/agent/get.go:105 returns_error: нет description: —


### printAgents (go/cli/internal/cli/agent/get.go:105)


printAgents is a function that performs operations based on the provided parameters and returns (agents []api.AgentResponse).


```go
func printAgents((agents []api.AgentResponse)) (agents []api.AgentResponse)
```


**Тип ответа:** agents


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `go/cli/internal/cli/agent/get.go:105`



---


[function] name: printSessions file: go/cli/internal/cli/agent/get.go:122 returns_error: нет description: —


### printSessions (go/cli/internal/cli/agent/get.go:122)


printSessions is a function that performs operations based on the provided parameters and returns (sessions []*database.Session).


```go
func printSessions((sessions []*database.Session)) (sessions []*database.Session)
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


**Тип ответа:** sessions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `go/cli/internal/cli/agent/get.go:122`



---


[function] name: printTools file: go/cli/internal/cli/agent/get.go:89 returns_error: нет description: —


### printTools (go/cli/internal/cli/agent/get.go:89)


printTools is a function that performs operations based on the provided parameters and returns (tools []database.Tool).


```go
func printTools((tools []database.Tool)) (tools []database.Tool)
```


**Тип ответа:** tools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `go/cli/internal/cli/agent/get.go:89`




## go/cli/internal/cli/agent/init.go


📄 Исходный файл: `go/cli/internal/cli/agent/init.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [InitCmd](#initcmd-gocliinternalcliagentinitgo28) `:28`

- 🔗 [validateAgentName](#validateagentname-gocliinternalcliagentinitgo111) `:111`

- 🔗 [validateModelProvider](#validatemodelprovider-gocliinternalcliagentinitgo97) `:97`


</details>


[function] name: InitCmd file: go/cli/internal/cli/agent/init.go:28 returns_error: нет description: —


### InitCmd (go/cli/internal/cli/agent/init.go:28)


InitCmd is a function that performs operations based on the provided parameters and returns (cfg *InitCfg).


```go
func InitCmd((cfg *InitCfg)) (cfg *InitCfg)
```


**Тип запроса:** InitCfg


```json
{
  "Framework": "string",
  "Language": "string",
  "AgentName": "string",
  "InstructionFile": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "Config": null
}
```


*Определено в:* `go/cli/internal/cli/agent/init.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** InitCfg


```json
{
  "Framework": "string",
  "Language": "string",
  "AgentName": "string",
  "InstructionFile": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "Config": null
}
```


*Определено в:* `go/cli/internal/cli/agent/init.go`


📍 *Расположение:* `go/cli/internal/cli/agent/init.go:28`



---


[function] name: validateAgentName file: go/cli/internal/cli/agent/init.go:111 returns_error: нет description: validateAgentName checks if the agent name is a valid identifier.
The name must start with a letter or underscore and co


### validateAgentName (go/cli/internal/cli/agent/init.go:111)


validateAgentName checks if the agent name is a valid identifier.
The name must start with a letter or underscore and contain only letters, digits,
and underscores. This matches the Python identifier rules enforced by the ADK at runtime.


```go
func validateAgentName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/cli/agent/init.go:111`



---


[function] name: validateModelProvider file: go/cli/internal/cli/agent/init.go:97 returns_error: нет description: validateModelProvider checks if the provided model provider is supported


### validateModelProvider (go/cli/internal/cli/agent/init.go:97)


validateModelProvider checks if the provided model provider is supported


```go
func validateModelProvider((provider string)) (provider string)
```


**Тип ответа:** provider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/init.go:97`




## go/cli/internal/cli/agent/install.go


📄 Исходный файл: `go/cli/internal/cli/agent/install.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [InstallCmd](#installcmd-gocliinternalcliagentinstallgo68) `:68`

- 🔗 [InteractiveInstallCmd](#interactiveinstallcmd-gocliinternalcliagentinstallgo107) `:107`

- 🔗 [UninstallCmd](#uninstallcmd-gocliinternalcliagentinstallgo271) `:271`

- 🔗 [checkHelmAvailable](#checkhelmavailable-gocliinternalcliagentinstallgo336) `:336`

- 🔗 [deleteCRDs](#deletecrds-gocliinternalcliagentinstallgo243) `:243`

- 🔗 [install](#install-gocliinternalcliagentinstallgo181) `:181`

- 🔗 [installChart](#installchart-gocliinternalcliagentinstallgo28) `:28`

- 🔗 [setupHelmConfig](#setuphelmconfig-gocliinternalcliagentinstallgo156) `:156`


</details>


[function] name: InstallCmd file: go/cli/internal/cli/agent/install.go:68 returns_error: нет description: —


### InstallCmd (go/cli/internal/cli/agent/install.go:68)


InstallCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cfg *InstallCfg).


```go
func InstallCmd((ctx context.Context, cfg *InstallCfg)) (ctx context.Context, cfg *InstallCfg)
```


**Тип запроса:** InstallCfg


```json
{
  "Config": null,
  "Profile": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/install.go`


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** InstallCfg


```json
{
  "Config": null,
  "Profile": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/install.go`


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:68`



---


[function] name: InteractiveInstallCmd file: go/cli/internal/cli/agent/install.go:107 returns_error: нет description: —


### InteractiveInstallCmd (go/cli/internal/cli/agent/install.go:107)


InteractiveInstallCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, c *ishell.Context).


```go
func InteractiveInstallCmd((ctx context.Context, c *ishell.Context)) (ctx context.Context, c *ishell.Context)
```


**Тип запроса:** ishell.Context


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


**Тип ответа:** c


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** ishell.Context


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


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:107`



---


[function] name: UninstallCmd file: go/cli/internal/cli/agent/install.go:271 returns_error: нет description: —


### UninstallCmd (go/cli/internal/cli/agent/install.go:271)


UninstallCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cfg *config.Config).


```go
func UninstallCmd((ctx context.Context, cfg *config.Config)) (ctx context.Context, cfg *config.Config)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:271`



---


[function] name: checkHelmAvailable file: go/cli/internal/cli/agent/install.go:336 returns_error: нет description: —


### checkHelmAvailable (go/cli/internal/cli/agent/install.go:336)


checkHelmAvailable is a function that performs operations based on the provided parameters and returns ().


```go
func checkHelmAvailable(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:336`



---


[function] name: deleteCRDs file: go/cli/internal/cli/agent/install.go:243 returns_error: нет description: deleteCRDs manually deletes Kubernetes CRDs for kagent
This is a workaround for the fact that helm doesn't delete CRDs a


### deleteCRDs (go/cli/internal/cli/agent/install.go:243)


deleteCRDs manually deletes Kubernetes CRDs for kagent
This is a workaround for the fact that helm doesn't delete CRDs automatically


```go
func deleteCRDs((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:243`



---


[function] name: install file: go/cli/internal/cli/agent/install.go:181 returns_error: нет description: install installs kagent and kagent-crds using the helm config


### install (go/cli/internal/cli/agent/install.go:181)


install installs kagent and kagent-crds using the helm config


```go
func install((ctx context.Context, cfg *config.Config, helmConfig helmConfig, modelProvider v1alpha2.ModelProvider)) (ctx context.Context, cfg *config.Config, helmConfig helmConfig, modelProvider v1alpha2.ModelProvider)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


**Тип ответа:** helmConfig


```json
{
  "registry": "string",
  "version": "string",
  "values": [],
  "inlineValues": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/install.go`


**Тип ответа:** helmConfig


```json
{
  "registry": "string",
  "version": "string",
  "values": [],
  "inlineValues": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/install.go`


**Тип ответа:** modelProvider


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/modelproviderconfig.go`


**Тип ответа:** v1alpha2.ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:181`



---


[function] name: installChart file: go/cli/internal/cli/agent/install.go:28 returns_error: да description: installChart installs or upgrades a Helm chart with the given parameters


### installChart (go/cli/internal/cli/agent/install.go:28)


installChart installs or upgrades a Helm chart with the given parameters


```go
func installChart((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:28`



---


[function] name: setupHelmConfig file: go/cli/internal/cli/agent/install.go:156 returns_error: нет description: setupHelmConfig sets up the helm config for the kagent chart
This sets up the general configuration for a helm installat


### setupHelmConfig (go/cli/internal/cli/agent/install.go:156)


setupHelmConfig sets up the helm config for the kagent chart
This sets up the general configuration for a helm installation without the profile, which is calculated later based on the installation type (interactive or non-interactive)


```go
func setupHelmConfig((modelProvider v1alpha2.ModelProvider, apiKeyValue string)) (modelProvider v1alpha2.ModelProvider, apiKeyValue string)
```


**Тип ответа:** modelProvider


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/modelproviderconfig.go`


**Тип ответа:** v1alpha2.ModelProvider


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** apiKeyValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/install.go:156`




## go/cli/internal/cli/agent/invoke.go


📄 Исходный файл: `go/cli/internal/cli/agent/invoke.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [InvokeCmd](#invokecmd-gocliinternalcliagentinvokego26) `:26`


</details>


[function] name: InvokeCmd file: go/cli/internal/cli/agent/invoke.go:26 returns_error: нет description: —


### InvokeCmd (go/cli/internal/cli/agent/invoke.go:26)


InvokeCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cfg *InvokeCfg).


```go
func InvokeCmd((ctx context.Context, cfg *InvokeCfg)) (ctx context.Context, cfg *InvokeCfg)
```


**Тип запроса:** InvokeCfg


```json
{
  "Config": null,
  "Task": "string",
  "File": "string",
  "Session": "string",
  "Agent": "string",
  "Stream": false,
  "URLOverride": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/invoke.go`


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** InvokeCfg


```json
{
  "Config": null,
  "Task": "string",
  "File": "string",
  "Session": "string",
  "Agent": "string",
  "Stream": false,
  "URLOverride": "string"
}
```


*Определено в:* `go/cli/internal/cli/agent/invoke.go`


📍 *Расположение:* `go/cli/internal/cli/agent/invoke.go:26`




## go/cli/internal/cli/agent/run.go


📄 Исходный файл: `go/cli/internal/cli/agent/run.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [RunCmd](#runcmd-gocliinternalcliagentrungo26) `:26`

- 🔗 [waitForAgent](#waitforagent-gocliinternalcliagentrungo151) `:151`


</details>


[function] name: RunCmd file: go/cli/internal/cli/agent/run.go:26 returns_error: нет description: RunCmd starts docker-compose in the background and launches a chat session with the local agent


### RunCmd (go/cli/internal/cli/agent/run.go:26)


RunCmd starts docker-compose in the background and launches a chat session with the local agent


```go
func RunCmd((ctx context.Context, cfg *RunCfg)) (ctx context.Context, cfg *RunCfg)
```


**Тип запроса:** RunCfg


```json
{
  "ProjectDir": "string",
  "Config": null,
  "Build": false
}
```


*Определено в:* `go/cli/internal/cli/agent/run.go`


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RunCfg


```json
{
  "ProjectDir": "string",
  "Config": null,
  "Build": false
}
```


*Определено в:* `go/cli/internal/cli/agent/run.go`


📍 *Расположение:* `go/cli/internal/cli/agent/run.go:26`



---


[function] name: waitForAgent file: go/cli/internal/cli/agent/run.go:151 returns_error: нет description: waitForAgent polls the agent's root endpoint until it's ready or timeout


### waitForAgent (go/cli/internal/cli/agent/run.go:151)


waitForAgent polls the agent's root endpoint until it's ready or timeout


```go
func waitForAgent((ctx context.Context, agentURL string, timeout time.Duration)) (ctx context.Context, agentURL string, timeout time.Duration)
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


**Тип ответа:** agentURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** timeout


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "v": {},
  "defaultValue": {}
}
```


*Определено в:* `go/pkg/env/var.go`


📍 *Расположение:* `go/cli/internal/cli/agent/run.go:151`




## go/cli/internal/cli/agent/utils.go


📄 Исходный файл: `go/cli/internal/cli/agent/utils.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [CheckServerConnection](#checkserverconnection-gocliinternalcliagentutilsgo31) `:31`

- 🔗 [CopyTemplateIfNotExists](#copytemplateifnotexists-gocliinternalcliagentutilsgo182) `:182`

- 🔗 [IsVerbose](#isverbose-gocliinternalcliagentutilsgo158) `:158`

- 🔗 [LoadManifest](#loadmanifest-gocliinternalcliagentutilsgo148) `:148`

- 🔗 [NewPortForward](#newportforward-gocliinternalcliagentutilsgo51) `:51`

- 🔗 [ReadTemplateFile](#readtemplatefile-gocliinternalcliagentutilsgo165) `:165`

- 🔗 [RegenerateDockerCompose](#regeneratedockercompose-gocliinternalcliagentutilsgo206) `:206`

- 🔗 [RenderTemplate](#rendertemplate-gocliinternalcliagentutilsgo171) `:171`

- 🔗 [ResolveProjectDir](#resolveprojectdir-gocliinternalcliagentutilsgo114) `:114`

- 🔗 [Stop](#stop-gocliinternalcliagentutilsgo81) `:81`

- 🔗 [StreamA2AEvents](#streama2aevents-gocliinternalcliagentutilsgo92) `:92`

- 🔗 [ValidateAPIKey](#validateapikey-gocliinternalcliagentutilsgo274) `:274`

- 🔗 [ValidateProjectDir](#validateprojectdir-gocliinternalcliagentutilsgo135) `:135`

- 🔗 [extractEnvVarsFromHeaders](#extractenvvarsfromheaders-gocliinternalcliagentutilsgo246) `:246`

- 🔗 [regenerateMcpToolsFile](#regeneratemcptoolsfile-gocliinternalcliagentutilsgo298) `:298`


</details>


[function] name: CheckServerConnection file: go/cli/internal/cli/agent/utils.go:31 returns_error: нет description: —


### CheckServerConnection (go/cli/internal/cli/agent/utils.go:31)


CheckServerConnection is a function that performs operations based on the provided parameters and returns (ctx context.Context, client *client.ClientSet).


```go
func CheckServerConnection((ctx context.Context, client *client.ClientSet)) (ctx context.Context, client *client.ClientSet)
```


**Тип запроса:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


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


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:31`



---


[function] name: CopyTemplateIfNotExists file: go/cli/internal/cli/agent/utils.go:182 returns_error: нет description: CopyTemplateIfNotExists copies a template file to the target directory if it doesn't exist


### CopyTemplateIfNotExists (go/cli/internal/cli/agent/utils.go:182)


CopyTemplateIfNotExists copies a template file to the target directory if it doesn't exist


```go
func CopyTemplateIfNotExists((targetDir, filename, templatePath string, verbose bool)) (targetDir, filename, templatePath string, verbose bool)
```


**Тип ответа:** targetDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** templatePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:182`



---


[function] name: IsVerbose file: go/cli/internal/cli/agent/utils.go:158 returns_error: нет description: IsVerbose checks if verbose mode is enabled


### IsVerbose (go/cli/internal/cli/agent/utils.go:158)


IsVerbose checks if verbose mode is enabled


```go
func IsVerbose((cfg *config.Config)) (cfg *config.Config)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:158`



---


[function] name: LoadManifest file: go/cli/internal/cli/agent/utils.go:148 returns_error: да description: LoadManifest loads the kagent.yaml file from the project directory


### LoadManifest (go/cli/internal/cli/agent/utils.go:148)


LoadManifest loads the kagent.yaml file from the project directory


```go
func LoadManifest((*common.AgentManifest, error)) (*common.AgentManifest, error)
```


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*common.AgentManifest`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:148`



---


[function] name: NewPortForward file: go/cli/internal/cli/agent/utils.go:51 returns_error: да description: —


### NewPortForward (go/cli/internal/cli/agent/utils.go:51)


NewPortForward is a function that performs operations based on the provided parameters and may return an error.


```go
func NewPortForward((*PortForward, error)) (*PortForward, error)
```


**Тип запроса:** PortForward


```json
{
  "cmd": null,
  "cancel": {}
}
```


*Определено в:* `go/cli/internal/cli/agent/utils.go`


**Тип ответа:** PortForward


```json
{
  "cmd": null,
  "cancel": {}
}
```


*Определено в:* `go/cli/internal/cli/agent/utils.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PortForward`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:51`



---


[function] name: ReadTemplateFile file: go/cli/internal/cli/agent/utils.go:165 returns_error: да description: ReadTemplateFile reads a template file from the embedded filesystem


### ReadTemplateFile (go/cli/internal/cli/agent/utils.go:165)


ReadTemplateFile reads a template file from the embedded filesystem


```go
func ReadTemplateFile(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:165`



---


[function] name: RegenerateDockerCompose file: go/cli/internal/cli/agent/utils.go:206 returns_error: нет description: RegenerateDockerCompose regenerates the docker-compose.yaml file with updated MCP server configuration


### RegenerateDockerCompose (go/cli/internal/cli/agent/utils.go:206)


RegenerateDockerCompose regenerates the docker-compose.yaml file with updated MCP server configuration


```go
func RegenerateDockerCompose((projectDir string, manifest *common.AgentManifest, verbose bool)) (projectDir string, manifest *common.AgentManifest, verbose bool)
```


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:206`



---


[function] name: RenderTemplate file: go/cli/internal/cli/agent/utils.go:171 returns_error: да description: RenderTemplate reads and renders a template file with the given data


### RenderTemplate (go/cli/internal/cli/agent/utils.go:171)


RenderTemplate reads and renders a template file with the given data


```go
func RenderTemplate((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:171`



---


[function] name: ResolveProjectDir file: go/cli/internal/cli/agent/utils.go:114 returns_error: да description: ResolveProjectDir resolves the project directory to an absolute path


### ResolveProjectDir (go/cli/internal/cli/agent/utils.go:114)


ResolveProjectDir resolves the project directory to an absolute path


```go
func ResolveProjectDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:114`



---


[function] name: Stop file: go/cli/internal/cli/agent/utils.go:81 returns_error: нет description: —


### Stop (go/cli/internal/cli/agent/utils.go:81)


Stop is a method that performs operations based on the provided parameters and returns ().


```go
func (p *PortForward) Stop(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:81`



---


[function] name: StreamA2AEvents file: go/cli/internal/cli/agent/utils.go:92 returns_error: нет description: —


### StreamA2AEvents (go/cli/internal/cli/agent/utils.go:92)


StreamA2AEvents is a function that performs operations based on the provided parameters and returns (ch <-chan protocol.StreamingMessageEvent, verbose bool).


```go
func StreamA2AEvents((ch <-chan protocol.StreamingMessageEvent, verbose bool)) (ch <-chan protocol.StreamingMessageEvent, verbose bool)
```


**Тип ответа:** ch


```json
{
  "AgentName": "string",
  "UserID": "string",
  "Vector": [],
  "Limit": 0,
  "MinScore": 0.0
}
```


*Определено в:* `go/internal/httpserver/handlers/memory.go`


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.StreamingMessageEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:92`



---


[function] name: ValidateAPIKey file: go/cli/internal/cli/agent/utils.go:274 returns_error: нет description: ValidateAPIKey checks if the required API key environment variable is set for the given model provider


### ValidateAPIKey (go/cli/internal/cli/agent/utils.go:274)


ValidateAPIKey checks if the required API key environment variable is set for the given model provider


```go
func ValidateAPIKey((modelProvider string)) (modelProvider string)
```


**Тип ответа:** modelProvider


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/modelproviderconfig.go`


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:274`



---


[function] name: ValidateProjectDir file: go/cli/internal/cli/agent/utils.go:135 returns_error: нет description: ValidateProjectDir checks if a project directory exists


### ValidateProjectDir (go/cli/internal/cli/agent/utils.go:135)


ValidateProjectDir checks if a project directory exists


```go
func ValidateProjectDir((projectDir string)) (projectDir string)
```


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:135`



---


[function] name: extractEnvVarsFromHeaders file: go/cli/internal/cli/agent/utils.go:246 returns_error: нет description: extractEnvVarsFromHeaders extracts environment variable names from MCP server headers
It looks for ${VAR_NAME} patterns 


### extractEnvVarsFromHeaders (go/cli/internal/cli/agent/utils.go:246)


extractEnvVarsFromHeaders extracts environment variable names from MCP server headers
It looks for ${VAR_NAME} patterns in header values


```go
func extractEnvVarsFromHeaders((mcpServers []common.McpServerType)) (mcpServers []common.McpServerType)
```


**Тип ответа:** mcpServers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.McpServerType


```json
{
  "Type": "string",
  "Name": "string",
  "Image": "string",
  "Build": "string",
  "Command": "string",
  "Args": [],
  "Env": [],
  "URL": "string",
  "Headers": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:246`



---


[function] name: regenerateMcpToolsFile file: go/cli/internal/cli/agent/utils.go:298 returns_error: нет description: regenerateMcpToolsFile regenerates mcp_tools.py with the current MCP servers from the manifest


### regenerateMcpToolsFile (go/cli/internal/cli/agent/utils.go:298)


regenerateMcpToolsFile regenerates mcp_tools.py with the current MCP servers from the manifest


```go
func regenerateMcpToolsFile((projectDir string, manifest *common.AgentManifest, verbose bool)) (projectDir string, manifest *common.AgentManifest, verbose bool)
```


**Тип запроса:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** common.AgentManifest


```json
{
  "Name": "string",
  "Language": "string",
  "Framework": "string",
  "ModelProvider": "string",
  "ModelName": "string",
  "Description": "string",
  "McpServers": [],
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/agent/frameworks/common/manifest_manager.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/agent/utils.go:298`




## go/cli/internal/cli/agent/version.go


📄 Исходный файл: `go/cli/internal/cli/agent/version.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [VersionCmd](#versioncmd-gocliinternalcliagentversiongo14) `:14`


</details>


[function] name: VersionCmd file: go/cli/internal/cli/agent/version.go:14 returns_error: нет description: —


### VersionCmd (go/cli/internal/cli/agent/version.go:14)


VersionCmd is a function that performs operations based on the provided parameters and returns (cfg *config.Config).


```go
func VersionCmd((cfg *config.Config)) (cfg *config.Config)
```


**Тип запроса:** config.Config


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


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


📍 *Расположение:* `go/cli/internal/cli/agent/version.go:14`




## go/cli/internal/cli/envdoc/envdoc.go


📄 Исходный файл: `go/cli/internal/cli/envdoc/envdoc.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewEnvCmd](#newenvcmd-gocliinternalclienvdocenvdocgo16) `:16`


</details>


[function] name: NewEnvCmd file: go/cli/internal/cli/envdoc/envdoc.go:16 returns_error: нет description: NewEnvCmd returns a cobra command that generates environment variable documentation.


### NewEnvCmd (go/cli/internal/cli/envdoc/envdoc.go:16)


NewEnvCmd returns a cobra command that generates environment variable documentation.


```go
func NewEnvCmd(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/envdoc/envdoc.go:16`




## go/cli/internal/cli/mcp/add_tool.go


📄 Исходный файл: `go/cli/internal/cli/mcp/add_tool.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [createTool](#createtool-gocliinternalclimcpadd_toolgo179) `:179`

- 🔗 [createToolInteractive](#createtoolinteractive-gocliinternalclimcpadd_toolgo162) `:162`

- 🔗 [generateTool](#generatetool-gocliinternalclimcpadd_toolgo191) `:191`

- 🔗 [init](#init-gocliinternalclimcpadd_toolgo45) `:45`

- 🔗 [isValidIdentifier](#isvalididentifier-gocliinternalclimcpadd_toolgo130) `:130`

- 🔗 [runAddTool](#runaddtool-gocliinternalclimcpadd_toolgo52) `:52`

- 🔗 [validateToolName](#validatetoolname-gocliinternalclimcpadd_toolgo111) `:111`


</details>


[function] name: createTool file: go/cli/internal/cli/mcp/add_tool.go:179 returns_error: нет description: —


### createTool (go/cli/internal/cli/mcp/add_tool.go:179)


createTool is a function that performs operations based on the provided parameters and returns (toolName, projectRoot, framework string).


```go
func createTool((toolName, projectRoot, framework string)) (toolName, projectRoot, framework string)
```


**Тип ответа:** toolName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/add_tool.go:179`



---


[function] name: createToolInteractive file: go/cli/internal/cli/mcp/add_tool.go:162 returns_error: нет description: —


### createToolInteractive (go/cli/internal/cli/mcp/add_tool.go:162)


createToolInteractive is a function that performs operations based on the provided parameters and returns (toolName, projectRoot, framework string).


```go
func createToolInteractive((toolName, projectRoot, framework string)) (toolName, projectRoot, framework string)
```


**Тип ответа:** toolName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/add_tool.go:162`



---


[function] name: generateTool file: go/cli/internal/cli/mcp/add_tool.go:191 returns_error: нет description: —


### generateTool (go/cli/internal/cli/mcp/add_tool.go:191)


generateTool is a function that performs operations based on the provided parameters and returns (toolName, projectRoot, framework string).


```go
func generateTool((toolName, projectRoot, framework string)) (toolName, projectRoot, framework string)
```


**Тип ответа:** toolName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/add_tool.go:191`



---


[function] name: init file: go/cli/internal/cli/mcp/add_tool.go:45 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/add_tool.go:45)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/add_tool.go:45`



---


[function] name: isValidIdentifier file: go/cli/internal/cli/mcp/add_tool.go:130 returns_error: нет description: —


### isValidIdentifier (go/cli/internal/cli/mcp/add_tool.go:130)


isValidIdentifier is a function that performs operations based on the provided parameters and returns (name string).


```go
func isValidIdentifier((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/cli/mcp/add_tool.go:130`



---


[function] name: runAddTool file: go/cli/internal/cli/mcp/add_tool.go:52 returns_error: нет description: —


### runAddTool (go/cli/internal/cli/mcp/add_tool.go:52)


runAddTool is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runAddTool((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/add_tool.go:52`



---


[function] name: validateToolName file: go/cli/internal/cli/mcp/add_tool.go:111 returns_error: нет description: —


### validateToolName (go/cli/internal/cli/mcp/add_tool.go:111)


validateToolName is a function that performs operations based on the provided parameters and returns (name string).


```go
func validateToolName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/cli/mcp/add_tool.go:111`




## go/cli/internal/cli/mcp/build.go


📄 Исходный файл: `go/cli/internal/cli/mcp/build.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [init](#init-gocliinternalclimcpbuildgo43) `:43`

- 🔗 [runBuild](#runbuild-gocliinternalclimcpbuildgo53) `:53`

- 🔗 [runKind](#runkind-gocliinternalclimcpbuildgo138) `:138`


</details>


[function] name: init file: go/cli/internal/cli/mcp/build.go:43 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/build.go:43)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/build.go:43`



---


[function] name: runBuild file: go/cli/internal/cli/mcp/build.go:53 returns_error: нет description: —


### runBuild (go/cli/internal/cli/mcp/build.go:53)


runBuild is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, _ []string).


```go
func runBuild((_ *cobra.Command, _ []string)) (_ *cobra.Command, _ []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/build.go:53`



---


[function] name: runKind file: go/cli/internal/cli/mcp/build.go:138 returns_error: нет description: —


### runKind (go/cli/internal/cli/mcp/build.go:138)


runKind is a function that performs operations based on the provided parameters and returns (args ...string).


```go
func runKind((args ...string)) (args ...string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/build.go:138`




## go/cli/internal/cli/mcp/deploy.go


📄 Исходный файл: `go/cli/internal/cli/mcp/deploy.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [applyToCluster](#applytocluster-gocliinternalclimcpdeploygo560) `:560`

- 🔗 [generateMCPServer](#generatemcpserver-gocliinternalclimcpdeploygo386) `:386`

- 🔗 [getDefaultArgs](#getdefaultargs-gocliinternalclimcpdeploygo528) `:528`

- 🔗 [getDefaultCommand](#getdefaultcommand-gocliinternalclimcpdeploygo513) `:513`

- 🔗 [getProjectDirFromFile](#getprojectdirfromfile-gocliinternalclimcpdeploygo368) `:368`

- 🔗 [getSecretRefFromManifest](#getsecretreffrommanifest-gocliinternalclimcpdeploygo482) `:482`

- 🔗 [getTransportType](#gettransporttype-gocliinternalclimcpdeploygo261) `:261`

- 🔗 [init](#init-gocliinternalclimcpdeploygo85) `:85`

- 🔗 [init](#init-gocliinternalclimcpdeploygo139) `:139`

- 🔗 [parseEnvVars](#parseenvvars-gocliinternalclimcpdeploygo549) `:549`

- 🔗 [runDeployMCP](#rundeploymcp-gocliinternalclimcpdeploygo277) `:277`

- 🔗 [runInspector](#runinspector-gocliinternalclimcpdeploygo616) `:616`

- 🔗 [runPackageDeploy](#runpackagedeploy-gocliinternalclimcpdeploygo162) `:162`

- 🔗 [runPortForward](#runportforward-gocliinternalclimcpdeploygo639) `:639`

- 🔗 [sanitizeLabelValue](#sanitizelabelvalue-gocliinternalclimcpdeploygo509) `:509`


</details>


[function] name: applyToCluster file: go/cli/internal/cli/mcp/deploy.go:560 returns_error: нет description: —


### applyToCluster (go/cli/internal/cli/mcp/deploy.go:560)


applyToCluster is a function that performs operations based on the provided parameters and returns (projectDir, yamlContent string, mcpServer *v1alpha1.MCPServer).


```go
func applyToCluster((projectDir, yamlContent string, mcpServer *v1alpha1.MCPServer)) (projectDir, yamlContent string, mcpServer *v1alpha1.MCPServer)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** yamlContent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:560`



---


[function] name: generateMCPServer file: go/cli/internal/cli/mcp/deploy.go:386 returns_error: да description: —


### generateMCPServer (go/cli/internal/cli/mcp/deploy.go:386)


generateMCPServer is a function that performs operations based on the provided parameters and may return an error.


```go
func generateMCPServer((*v1alpha1.MCPServer, error)) (*v1alpha1.MCPServer, error)
```


**Тип запроса:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Тип ответа:** v1alpha1.MCPServer


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/mcp_server_tool_controller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1alpha1.MCPServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:386`



---


[function] name: getDefaultArgs file: go/cli/internal/cli/mcp/deploy.go:528 returns_error: нет description: —


### getDefaultArgs (go/cli/internal/cli/mcp/deploy.go:528)


getDefaultArgs is a function that performs operations based on the provided parameters and returns (framework string, targetPort int).


```go
func getDefaultArgs((framework string, targetPort int)) (framework string, targetPort int)
```


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** targetPort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:528`



---


[function] name: getDefaultCommand file: go/cli/internal/cli/mcp/deploy.go:513 returns_error: нет description: —


### getDefaultCommand (go/cli/internal/cli/mcp/deploy.go:513)


getDefaultCommand is a function that performs operations based on the provided parameters and returns (framework string).


```go
func getDefaultCommand((framework string)) (framework string)
```


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:513`



---


[function] name: getProjectDirFromFile file: go/cli/internal/cli/mcp/deploy.go:368 returns_error: да description: getProjectDirFromFile extracts the project directory from a file path


### getProjectDirFromFile (go/cli/internal/cli/mcp/deploy.go:368)


getProjectDirFromFile extracts the project directory from a file path


```go
func getProjectDirFromFile((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:368`



---


[function] name: getSecretRefFromManifest file: go/cli/internal/cli/mcp/deploy.go:482 returns_error: да description: —


### getSecretRefFromManifest (go/cli/internal/cli/mcp/deploy.go:482)


getSecretRefFromManifest is a function that performs operations based on the provided parameters and may return an error.


```go
func getSecretRefFromManifest((*corev1.LocalObjectReference, error)) (*corev1.LocalObjectReference, error)
```


**Тип запроса:** corev1.LocalObjectReference


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.LocalObjectReference


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.LocalObjectReference`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:482`



---


[function] name: getTransportType file: go/cli/internal/cli/mcp/deploy.go:261 returns_error: нет description: getTransportType determines the transport type based on flags


### getTransportType (go/cli/internal/cli/mcp/deploy.go:261)


getTransportType determines the transport type based on flags


```go
func getTransportType(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:261`



---


[function] name: init file: go/cli/internal/cli/mcp/deploy.go:85 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/deploy.go:85)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:85`



---


[function] name: init file: go/cli/internal/cli/mcp/deploy.go:139 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/deploy.go:139)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:139`



---


[function] name: parseEnvVars file: go/cli/internal/cli/mcp/deploy.go:549 returns_error: нет description: —


### parseEnvVars (go/cli/internal/cli/mcp/deploy.go:549)


parseEnvVars is a function that performs operations based on the provided parameters and returns (envVars []string).


```go
func parseEnvVars((envVars []string)) (envVars []string)
```


**Тип ответа:** envVars


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:549`



---


[function] name: runDeployMCP file: go/cli/internal/cli/mcp/deploy.go:277 returns_error: нет description: —


### runDeployMCP (go/cli/internal/cli/mcp/deploy.go:277)


runDeployMCP is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runDeployMCP((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:277`



---


[function] name: runInspector file: go/cli/internal/cli/mcp/deploy.go:616 returns_error: нет description: —


### runInspector (go/cli/internal/cli/mcp/deploy.go:616)


runInspector is a function that performs operations based on the provided parameters and returns (mcpServer *v1alpha1.MCPServer, configPath string, projectDir string).


```go
func runInspector((mcpServer *v1alpha1.MCPServer, configPath string, projectDir string)) (mcpServer *v1alpha1.MCPServer, configPath string, projectDir string)
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


**Тип ответа:** configPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:616`



---


[function] name: runPackageDeploy file: go/cli/internal/cli/mcp/deploy.go:162 returns_error: нет description: —


### runPackageDeploy (go/cli/internal/cli/mcp/deploy.go:162)


runPackageDeploy is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runPackageDeploy((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:162`



---


[function] name: runPortForward file: go/cli/internal/cli/mcp/deploy.go:639 returns_error: да description: —


### runPortForward (go/cli/internal/cli/mcp/deploy.go:639)


runPortForward is a function that performs operations based on the provided parameters and may return an error.


```go
func runPortForward((*exec.Cmd, error)) (*exec.Cmd, error)
```


**Тип запроса:** exec.Cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** exec.Cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*exec.Cmd`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:639`



---


[function] name: sanitizeLabelValue file: go/cli/internal/cli/mcp/deploy.go:509 returns_error: нет description: —


### sanitizeLabelValue (go/cli/internal/cli/mcp/deploy.go:509)


sanitizeLabelValue is a function that performs operations based on the provided parameters and returns (value string).


```go
func sanitizeLabelValue((value string)) (value string)
```


**Тип ответа:** value


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/deploy.go:509`




## go/cli/internal/cli/mcp/init.go


📄 Исходный файл: `go/cli/internal/cli/mcp/init.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [init](#init-gocliinternalclimcpinitgo45) `:45`

- 🔗 [isValidEmail](#isvalidemail-gocliinternalclimcpinitgo192) `:192`

- 🔗 [promptForAuthor](#promptforauthor-gocliinternalclimcpinitgo147) `:147`

- 🔗 [promptForDescription](#promptfordescription-gocliinternalclimcpinitgo181) `:181`

- 🔗 [promptForEmail](#promptforemail-gocliinternalclimcpinitgo157) `:157`

- 🔗 [runInit](#runinit-gocliinternalclimcpinitgo55) `:55`

- 🔗 [runInitFramework](#runinitframework-gocliinternalclimcpinitgo62) `:62`

- 🔗 [validateProjectName](#validateprojectname-gocliinternalclimcpinitgo127) `:127`


</details>


[function] name: init file: go/cli/internal/cli/mcp/init.go:45 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/init.go:45)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:45`



---


[function] name: isValidEmail file: go/cli/internal/cli/mcp/init.go:192 returns_error: нет description: isValidEmail performs basic email validation


### isValidEmail (go/cli/internal/cli/mcp/init.go:192)


isValidEmail performs basic email validation


```go
func isValidEmail((email string)) (email string)
```


**Тип ответа:** email


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:192`



---


[function] name: promptForAuthor file: go/cli/internal/cli/mcp/init.go:147 returns_error: нет description: Prompts for user input


### promptForAuthor (go/cli/internal/cli/mcp/init.go:147)


Prompts for user input


```go
func promptForAuthor(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:147`



---


[function] name: promptForDescription file: go/cli/internal/cli/mcp/init.go:181 returns_error: нет description: —


### promptForDescription (go/cli/internal/cli/mcp/init.go:181)


promptForDescription is a function that performs operations based on the provided parameters and returns ().


```go
func promptForDescription(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:181`



---


[function] name: promptForEmail file: go/cli/internal/cli/mcp/init.go:157 returns_error: нет description: —


### promptForEmail (go/cli/internal/cli/mcp/init.go:157)


promptForEmail is a function that performs operations based on the provided parameters and returns ().


```go
func promptForEmail(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:157`



---


[function] name: runInit file: go/cli/internal/cli/mcp/init.go:55 returns_error: нет description: —


### runInit (go/cli/internal/cli/mcp/init.go:55)


runInit is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func runInit((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:55`



---


[function] name: runInitFramework file: go/cli/internal/cli/mcp/init.go:62 returns_error: да description: —


### runInitFramework (go/cli/internal/cli/mcp/init.go:62)


runInitFramework is a function that performs operations based on the provided parameters and may return an error.


```go
func runInitFramework((
	projectName, framework string,
	customizeProjectConfig func(*mcp.ProjectConfig) error,
)) (
	projectName, framework string,
	customizeProjectConfig func(*mcp.ProjectConfig) error,
)
```


**Тип запроса:** mcp.ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


**Тип ответа:** projectName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** customizeProjectConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `projectName`, `framework string`, `customizeProjectConfig func(*mcp.ProjectConfig) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:62`



---


[function] name: validateProjectName file: go/cli/internal/cli/mcp/init.go:127 returns_error: нет description: —


### validateProjectName (go/cli/internal/cli/mcp/init.go:127)


validateProjectName is a function that performs operations based on the provided parameters and returns (name string).


```go
func validateProjectName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/cli/mcp/init.go:127`




## go/cli/internal/cli/mcp/init_go.go


📄 Исходный файл: `go/cli/internal/cli/mcp/init_go.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-gocliinternalclimcpinit_gogo28) `:28`

- 🔗 [runInitGo](#runinitgo-gocliinternalclimcpinit_gogo38) `:38`


</details>


[function] name: init file: go/cli/internal/cli/mcp/init_go.go:28 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/init_go.go:28)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init_go.go:28`



---


[function] name: runInitGo file: go/cli/internal/cli/mcp/init_go.go:38 returns_error: нет description: —


### runInitGo (go/cli/internal/cli/mcp/init_go.go:38)


runInitGo is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runInitGo((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/init_go.go:38`




## go/cli/internal/cli/mcp/init_java.go


📄 Исходный файл: `go/cli/internal/cli/mcp/init_java.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-gocliinternalclimcpinit_javago20) `:20`

- 🔗 [runInitJava](#runinitjava-gocliinternalclimcpinit_javago24) `:24`


</details>


[function] name: init file: go/cli/internal/cli/mcp/init_java.go:20 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/init_java.go:20)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init_java.go:20`



---


[function] name: runInitJava file: go/cli/internal/cli/mcp/init_java.go:24 returns_error: нет description: —


### runInitJava (go/cli/internal/cli/mcp/init_java.go:24)


runInitJava is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runInitJava((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/init_java.go:24`




## go/cli/internal/cli/mcp/init_python.go


📄 Исходный файл: `go/cli/internal/cli/mcp/init_python.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-gocliinternalclimcpinit_pythongo20) `:20`

- 🔗 [runInitPython](#runinitpython-gocliinternalclimcpinit_pythongo24) `:24`


</details>


[function] name: init file: go/cli/internal/cli/mcp/init_python.go:20 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/init_python.go:20)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init_python.go:20`



---


[function] name: runInitPython file: go/cli/internal/cli/mcp/init_python.go:24 returns_error: нет description: —


### runInitPython (go/cli/internal/cli/mcp/init_python.go:24)


runInitPython is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runInitPython((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/init_python.go:24`




## go/cli/internal/cli/mcp/init_typescript.go


📄 Исходный файл: `go/cli/internal/cli/mcp/init_typescript.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-gocliinternalclimcpinit_typescriptgo20) `:20`

- 🔗 [runInitTypeScript](#runinittypescript-gocliinternalclimcpinit_typescriptgo24) `:24`


</details>


[function] name: init file: go/cli/internal/cli/mcp/init_typescript.go:20 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/init_typescript.go:20)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/init_typescript.go:20`



---


[function] name: runInitTypeScript file: go/cli/internal/cli/mcp/init_typescript.go:24 returns_error: нет description: —


### runInitTypeScript (go/cli/internal/cli/mcp/init_typescript.go:24)


runInitTypeScript is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runInitTypeScript((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/init_typescript.go:24`




## go/cli/internal/cli/mcp/inspector.go


📄 Исходный файл: `go/cli/internal/cli/mcp/inspector.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [checkNpxInstalled](#checknpxinstalled-gocliinternalclimcpinspectorgo12) `:12`

- 🔗 [createMCPInspectorConfig](#createmcpinspectorconfig-gocliinternalclimcpinspectorgo21) `:21`

- 🔗 [runMCPInspector](#runmcpinspector-gocliinternalclimcpinspectorgo61) `:61`


</details>


[function] name: checkNpxInstalled file: go/cli/internal/cli/mcp/inspector.go:12 returns_error: нет description: —


### checkNpxInstalled (go/cli/internal/cli/mcp/inspector.go:12)


checkNpxInstalled is a function that performs operations based on the provided parameters and returns ().


```go
func checkNpxInstalled(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/inspector.go:12`



---


[function] name: createMCPInspectorConfig file: go/cli/internal/cli/mcp/inspector.go:21 returns_error: нет description: createMCPInspectorConfig creates an MCP inspector configuration file


### createMCPInspectorConfig (go/cli/internal/cli/mcp/inspector.go:21)


createMCPInspectorConfig creates an MCP inspector configuration file


```go
func createMCPInspectorConfig((serverName string, serverConfig map[string]any, configPath string)) (serverName string, serverConfig map[string]any, configPath string)
```


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** serverConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** configPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/inspector.go:21`



---


[function] name: runMCPInspector file: go/cli/internal/cli/mcp/inspector.go:61 returns_error: нет description: runMCPInspector runs the MCP inspector with the given configuration


### runMCPInspector (go/cli/internal/cli/mcp/inspector.go:61)


runMCPInspector runs the MCP inspector with the given configuration


```go
func runMCPInspector((configPath, serverName string, workingDir string)) (configPath, serverName string, workingDir string)
```


**Тип ответа:** configPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** workingDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/inspector.go:61`




## go/cli/internal/cli/mcp/root.go


📄 Исходный файл: `go/cli/internal/cli/mcp/root.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewMCPCmd](#newmcpcmd-gocliinternalclimcprootgo8) `:8`


</details>


[function] name: NewMCPCmd file: go/cli/internal/cli/mcp/root.go:8 returns_error: нет description: NewMCPCmd creates the root MCP command


### NewMCPCmd (go/cli/internal/cli/mcp/root.go:8)


NewMCPCmd creates the root MCP command


```go
func NewMCPCmd(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/root.go:8`




## go/cli/internal/cli/mcp/run.go


📄 Исходный файл: `go/cli/internal/cli/mcp/run.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [executeRun](#executerun-gocliinternalclimcprungo66) `:66`

- 🔗 [getProjectDir](#getprojectdir-gocliinternalclimcprungo207) `:207`

- 🔗 [getProjectManifest](#getprojectmanifest-gocliinternalclimcprungo239) `:239`

- 🔗 [init](#init-gocliinternalclimcprungo44) `:44`

- 🔗 [runFastMCPPython](#runfastmcppython-gocliinternalclimcprungo99) `:99`

- 🔗 [runJava](#runjava-gocliinternalclimcprungo308) `:308`

- 🔗 [runMCPGo](#runmcpgo-gocliinternalclimcprungo154) `:154`

- 🔗 [runTypeScript](#runtypescript-gocliinternalclimcprungo255) `:255`


</details>


[function] name: executeRun file: go/cli/internal/cli/mcp/run.go:66 returns_error: нет description: —


### executeRun (go/cli/internal/cli/mcp/run.go:66)


executeRun is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, _ []string).


```go
func executeRun((_ *cobra.Command, _ []string)) (_ *cobra.Command, _ []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:66`



---


[function] name: getProjectDir file: go/cli/internal/cli/mcp/run.go:207 returns_error: да description: —


### getProjectDir (go/cli/internal/cli/mcp/run.go:207)


getProjectDir is a function that performs operations based on the provided parameters and may return an error.


```go
func getProjectDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:207`



---


[function] name: getProjectManifest file: go/cli/internal/cli/mcp/run.go:239 returns_error: да description: —


### getProjectManifest (go/cli/internal/cli/mcp/run.go:239)


getProjectManifest is a function that performs operations based on the provided parameters and may return an error.


```go
func getProjectManifest((*manifests.ProjectManifest, error)) (*manifests.ProjectManifest, error)
```


**Тип запроса:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*manifests.ProjectManifest`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:239`



---


[function] name: init file: go/cli/internal/cli/mcp/run.go:44 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/run.go:44)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:44`



---


[function] name: runFastMCPPython file: go/cli/internal/cli/mcp/run.go:99 returns_error: нет description: —


### runFastMCPPython (go/cli/internal/cli/mcp/run.go:99)


runFastMCPPython is a function that performs operations based on the provided parameters and returns (projectDir string, manifest *manifests.ProjectManifest).


```go
func runFastMCPPython((projectDir string, manifest *manifests.ProjectManifest)) (projectDir string, manifest *manifests.ProjectManifest)
```


**Тип запроса:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:99`



---


[function] name: runJava file: go/cli/internal/cli/mcp/run.go:308 returns_error: нет description: —


### runJava (go/cli/internal/cli/mcp/run.go:308)


runJava is a function that performs operations based on the provided parameters and returns (projectDir string, manifest *manifests.ProjectManifest).


```go
func runJava((projectDir string, manifest *manifests.ProjectManifest)) (projectDir string, manifest *manifests.ProjectManifest)
```


**Тип запроса:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:308`



---


[function] name: runMCPGo file: go/cli/internal/cli/mcp/run.go:154 returns_error: нет description: —


### runMCPGo (go/cli/internal/cli/mcp/run.go:154)


runMCPGo is a function that performs operations based on the provided parameters and returns (projectDir string, manifest *manifests.ProjectManifest).


```go
func runMCPGo((projectDir string, manifest *manifests.ProjectManifest)) (projectDir string, manifest *manifests.ProjectManifest)
```


**Тип запроса:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:154`



---


[function] name: runTypeScript file: go/cli/internal/cli/mcp/run.go:255 returns_error: нет description: —


### runTypeScript (go/cli/internal/cli/mcp/run.go:255)


runTypeScript is a function that performs operations based on the provided parameters and returns (projectDir string, manifest *manifests.ProjectManifest).


```go
func runTypeScript((projectDir string, manifest *manifests.ProjectManifest)) (projectDir string, manifest *manifests.ProjectManifest)
```


**Тип запроса:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** projectDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** manifests.ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/cli/mcp/run.go:255`




## go/cli/internal/cli/mcp/secrets.go


📄 Исходный файл: `go/cli/internal/cli/mcp/secrets.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [applySecretToCluster](#applysecrettocluster-gocliinternalclimcpsecretsgo163) `:163`

- 🔗 [init](#init-gocliinternalclimcpsecretsgo61) `:61`

- 🔗 [loadEnvFile](#loadenvfile-gocliinternalclimcpsecretsgo198) `:198`

- 🔗 [runSync](#runsync-gocliinternalclimcpsecretsgo71) `:71`


</details>


[function] name: applySecretToCluster file: go/cli/internal/cli/mcp/secrets.go:163 returns_error: нет description: —


### applySecretToCluster (go/cli/internal/cli/mcp/secrets.go:163)


applySecretToCluster is a function that performs operations based on the provided parameters and returns (secret *corev1.Secret).


```go
func applySecretToCluster((secret *corev1.Secret)) (secret *corev1.Secret)
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


📍 *Расположение:* `go/cli/internal/cli/mcp/secrets.go:163`



---


[function] name: init file: go/cli/internal/cli/mcp/secrets.go:61 returns_error: нет description: —


### init (go/cli/internal/cli/mcp/secrets.go:61)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `go/cli/internal/cli/mcp/secrets.go:61`



---


[function] name: loadEnvFile file: go/cli/internal/cli/mcp/secrets.go:198 returns_error: да description: loadEnvFile reads environment variables from a file and returns them as a map


### loadEnvFile (go/cli/internal/cli/mcp/secrets.go:198)


loadEnvFile reads environment variables from a file and returns them as a map


```go
func loadEnvFile((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/cli/mcp/secrets.go:198`



---


[function] name: runSync file: go/cli/internal/cli/mcp/secrets.go:71 returns_error: нет description: —


### runSync (go/cli/internal/cli/mcp/secrets.go:71)


runSync is a function that performs operations based on the provided parameters and returns (_ *cobra.Command, args []string).


```go
func runSync((_ *cobra.Command, args []string)) (_ *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cobra.Command


```json
{
  "ID": "string",
  "DisplayName": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/cli/mcp/secrets.go:71`




## go/cli/internal/common/exec/docker.go


📄 Исходный файл: `go/cli/internal/common/exec/docker.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Build](#build-gocliinternalcommonexecdockergo74) `:74`

- 🔗 [CheckAvailability](#checkavailability-gocliinternalcommonexecdockergo31) `:31`

- 🔗 [GetComposeCommand](#getcomposecommand-gocliinternalcommonexecdockergo99) `:99`

- 🔗 [NewDockerExecutor](#newdockerexecutor-gocliinternalcommonexecdockergo22) `:22`

- 🔗 [Push](#push-gocliinternalcommonexecdockergo88) `:88`

- 🔗 [Run](#run-gocliinternalcommonexecdockergo54) `:54`


</details>


[function] name: Build file: go/cli/internal/common/exec/docker.go:74 returns_error: нет description: Build builds a Docker image with the specified name and context.
Additional build arguments can be provided (e.g., "--pl


### Build (go/cli/internal/common/exec/docker.go:74)


Build builds a Docker image with the specified name and context.
Additional build arguments can be provided (e.g., "--platform", "linux/amd64").


```go
func (d *DockerExecutor) Build((imageName, context string, extraArgs ...string)) (imageName, context string, extraArgs ...string)
```


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** extraArgs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/exec/docker.go:74`



---


[function] name: CheckAvailability file: go/cli/internal/common/exec/docker.go:31 returns_error: нет description: CheckAvailability checks if Docker is installed and the daemon is running.
Returns an error if Docker is not available o


### CheckAvailability (go/cli/internal/common/exec/docker.go:31)


CheckAvailability checks if Docker is installed and the daemon is running.
Returns an error if Docker is not available or not properly configured.


```go
func (d *DockerExecutor) CheckAvailability(()) ()
```


📍 *Расположение:* `go/cli/internal/common/exec/docker.go:31`



---


[function] name: GetComposeCommand file: go/cli/internal/common/exec/docker.go:99 returns_error: нет description: GetComposeCommand returns the appropriate docker compose command for the system.
It tries "docker compose" (newer versio


### GetComposeCommand (go/cli/internal/common/exec/docker.go:99)


GetComposeCommand returns the appropriate docker compose command for the system.
It tries "docker compose" (newer version) first, then falls back to "docker-compose" (older version).


```go
func GetComposeCommand(()) ()
```


📍 *Расположение:* `go/cli/internal/common/exec/docker.go:99`



---


[function] name: NewDockerExecutor file: go/cli/internal/common/exec/docker.go:22 returns_error: нет description: NewDockerExecutor creates a new Docker executor with the specified configuration.


### NewDockerExecutor (go/cli/internal/common/exec/docker.go:22)


NewDockerExecutor creates a new Docker executor with the specified configuration.


```go
func NewDockerExecutor((verbose bool, workDir string)) (verbose bool, workDir string)
```


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** workDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/exec/docker.go:22`



---


[function] name: Push file: go/cli/internal/common/exec/docker.go:88 returns_error: нет description: Push pushes a Docker image to a registry.


### Push (go/cli/internal/common/exec/docker.go:88)


Push pushes a Docker image to a registry.


```go
func (d *DockerExecutor) Push((imageName string)) (imageName string)
```


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/exec/docker.go:88`



---


[function] name: Run file: go/cli/internal/common/exec/docker.go:54 returns_error: нет description: Run executes a docker command with the given arguments.
It automatically handles verbose logging and working directory c


### Run (go/cli/internal/common/exec/docker.go:54)


Run executes a docker command with the given arguments.
It automatically handles verbose logging and working directory configuration.


```go
func (d *DockerExecutor) Run((args ...string)) (args ...string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/exec/docker.go:54`




## go/cli/internal/common/exec/kubectl.go


📄 Исходный файл: `go/cli/internal/common/exec/kubectl.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Apply](#apply-gocliinternalcommonexeckubectlgo78) `:78`

- 🔗 [CheckAvailability](#checkavailability-gocliinternalcommonexeckubectlgo33) `:33`

- 🔗 [NewKubectlExecutor](#newkubectlexecutor-gocliinternalcommonexeckubectlgo25) `:25`

- 🔗 [RolloutRestart](#rolloutrestart-gocliinternalcommonexeckubectlgo124) `:124`

- 🔗 [Run](#run-gocliinternalcommonexeckubectlgo43) `:43`

- 🔗 [RunWithOutput](#runwithoutput-gocliinternalcommonexeckubectlgo62) `:62`

- 🔗 [WaitForDeployment](#waitfordeployment-gocliinternalcommonexeckubectlgo148) `:148`


</details>


[function] name: Apply file: go/cli/internal/common/exec/kubectl.go:78 returns_error: нет description: Apply applies YAML resources to the Kubernetes cluster.
Multiple YAML documents can be provided and will be combined wit


### Apply (go/cli/internal/common/exec/kubectl.go:78)


Apply applies YAML resources to the Kubernetes cluster.
Multiple YAML documents can be provided and will be combined with separators.


```go
func (k *KubectlExecutor) Apply((yamls ...[]byte)) (yamls ...[]byte)
```


**Тип ответа:** yamls


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/exec/kubectl.go:78`



---


[function] name: CheckAvailability file: go/cli/internal/common/exec/kubectl.go:33 returns_error: нет description: CheckAvailability checks if kubectl is installed and accessible.


### CheckAvailability (go/cli/internal/common/exec/kubectl.go:33)


CheckAvailability checks if kubectl is installed and accessible.


```go
func (k *KubectlExecutor) CheckAvailability(()) ()
```


📍 *Расположение:* `go/cli/internal/common/exec/kubectl.go:33`



---


[function] name: NewKubectlExecutor file: go/cli/internal/common/exec/kubectl.go:25 returns_error: нет description: NewKubectlExecutor creates a new kubectl executor with the specified configuration.


### NewKubectlExecutor (go/cli/internal/common/exec/kubectl.go:25)


NewKubectlExecutor creates a new kubectl executor with the specified configuration.


```go
func NewKubectlExecutor((verbose bool, namespace string)) (verbose bool, namespace string)
```


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/common/exec/kubectl.go:25`



---


[function] name: RolloutRestart file: go/cli/internal/common/exec/kubectl.go:124 returns_error: нет description: RolloutRestart restarts a Kubernetes deployment by triggering a rollout restart.
This causes the deployment to recreate 


### RolloutRestart (go/cli/internal/common/exec/kubectl.go:124)


RolloutRestart restarts a Kubernetes deployment by triggering a rollout restart.
This causes the deployment to recreate all pods with the latest configuration.


```go
func (k *KubectlExecutor) RolloutRestart((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/common/exec/kubectl.go:124`



---


[function] name: Run file: go/cli/internal/common/exec/kubectl.go:43 returns_error: нет description: Run executes a kubectl command with the given arguments.
It automatically handles verbose logging and captures stderr fo


### Run (go/cli/internal/common/exec/kubectl.go:43)


Run executes a kubectl command with the given arguments.
It automatically handles verbose logging and captures stderr for better error messages.


```go
func (k *KubectlExecutor) Run((args ...string)) (args ...string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/exec/kubectl.go:43`



---


[function] name: RunWithOutput file: go/cli/internal/common/exec/kubectl.go:62 returns_error: да description: RunWithOutput executes a kubectl command and returns the combined output.
This is useful for capturing command output fo


### RunWithOutput (go/cli/internal/common/exec/kubectl.go:62)


RunWithOutput executes a kubectl command and returns the combined output.
This is useful for capturing command output for further processing.


```go
func (k *KubectlExecutor) RunWithOutput(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/exec/kubectl.go:62`



---


[function] name: WaitForDeployment file: go/cli/internal/common/exec/kubectl.go:148 returns_error: нет description: WaitForDeployment waits for a Kubernetes deployment to be ready.
It uses kubectl rollout status to monitor the deploymen


### WaitForDeployment (go/cli/internal/common/exec/kubectl.go:148)


WaitForDeployment waits for a Kubernetes deployment to be ready.
It uses kubectl rollout status to monitor the deployment progress.


```go
func (k *KubectlExecutor) WaitForDeployment((name string, timeout time.Duration)) (name string, timeout time.Duration)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** timeout


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "v": {},
  "defaultValue": {}
}
```


*Определено в:* `go/pkg/env/var.go`


📍 *Расположение:* `go/cli/internal/common/exec/kubectl.go:148`




## go/cli/internal/common/fs/project.go


📄 Исходный файл: `go/cli/internal/common/fs/project.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [DirExists](#direxists-gocliinternalcommonfsprojectgo111) `:111`

- 🔗 [EnsureDir](#ensuredir-gocliinternalcommonfsprojectgo121) `:121`

- 🔗 [Exists](#exists-gocliinternalcommonfsprojectgo80) `:80`

- 🔗 [FileExists](#fileexists-gocliinternalcommonfsprojectgo93) `:93`

- 🔗 [FileExists](#fileexists-gocliinternalcommonfsprojectgo105) `:105`

- 🔗 [IsVerbose](#isverbose-gocliinternalcommonfsprojectgo99) `:99`

- 🔗 [Join](#join-gocliinternalcommonfsprojectgo87) `:87`

- 🔗 [NewProjectDir](#newprojectdir-gocliinternalcommonfsprojectgo20) `:20`

- 🔗 [Path](#path-gocliinternalcommonfsprojectgo60) `:60`

- 🔗 [Validate](#validate-gocliinternalcommonfsprojectgo66) `:66`

- 🔗 [resolvePath](#resolvepath-gocliinternalcommonfsprojectgo39) `:39`


</details>


[function] name: DirExists file: go/cli/internal/common/fs/project.go:111 returns_error: нет description: DirExists checks if a directory exists at the given path.


### DirExists (go/cli/internal/common/fs/project.go:111)


DirExists checks if a directory exists at the given path.


```go
func DirExists((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/fs/project.go:111`



---


[function] name: EnsureDir file: go/cli/internal/common/fs/project.go:121 returns_error: нет description: EnsureDir creates a directory if it doesn't exist.
It creates all necessary parent directories as well.


### EnsureDir (go/cli/internal/common/fs/project.go:121)


EnsureDir creates a directory if it doesn't exist.
It creates all necessary parent directories as well.


```go
func EnsureDir((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/fs/project.go:121`



---


[function] name: Exists file: go/cli/internal/common/fs/project.go:80 returns_error: нет description: Exists checks if the project directory exists.
Returns true if the directory exists, false otherwise.


### Exists (go/cli/internal/common/fs/project.go:80)


Exists checks if the project directory exists.
Returns true if the directory exists, false otherwise.


```go
func (p *ProjectDir) Exists(()) ()
```


📍 *Расположение:* `go/cli/internal/common/fs/project.go:80`



---


[function] name: FileExists file: go/cli/internal/common/fs/project.go:93 returns_error: нет description: FileExists checks if a file exists in the project directory.
The filename is relative to the project directory.


### FileExists (go/cli/internal/common/fs/project.go:93)


FileExists checks if a file exists in the project directory.
The filename is relative to the project directory.


```go
func (p *ProjectDir) FileExists((filename string)) (filename string)
```


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/fs/project.go:93`



---


[function] name: FileExists file: go/cli/internal/common/fs/project.go:105 returns_error: нет description: FileExists checks if a file exists at the given path.
This is a standalone utility function for checking file existence.


### FileExists (go/cli/internal/common/fs/project.go:105)


FileExists checks if a file exists at the given path.
This is a standalone utility function for checking file existence.


```go
func FileExists((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/fs/project.go:105`



---


[function] name: IsVerbose file: go/cli/internal/common/fs/project.go:99 returns_error: нет description: IsVerbose returns whether verbose mode is enabled for this project directory.


### IsVerbose (go/cli/internal/common/fs/project.go:99)


IsVerbose returns whether verbose mode is enabled for this project directory.


```go
func (p *ProjectDir) IsVerbose(()) ()
```


📍 *Расположение:* `go/cli/internal/common/fs/project.go:99`



---


[function] name: Join file: go/cli/internal/common/fs/project.go:87 returns_error: нет description: Join joins path elements with the project directory.
This is a convenience method for constructing paths within the proj


### Join (go/cli/internal/common/fs/project.go:87)


Join joins path elements with the project directory.
This is a convenience method for constructing paths within the project.


```go
func (p *ProjectDir) Join((elem ...string)) (elem ...string)
```


**Тип ответа:** elem


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/fs/project.go:87`



---


[function] name: NewProjectDir file: go/cli/internal/common/fs/project.go:20 returns_error: да description: NewProjectDir creates a new ProjectDir, resolving relative paths to absolute paths.
If path is empty, it uses the curren


### NewProjectDir (go/cli/internal/common/fs/project.go:20)


NewProjectDir creates a new ProjectDir, resolving relative paths to absolute paths.
If path is empty, it uses the current working directory.
If verbose is true, it logs the resolved directory path.


```go
func NewProjectDir((*ProjectDir, error)) (*ProjectDir, error)
```


**Тип запроса:** ProjectDir


```json
{
  "path": "string",
  "verbose": false
}
```


*Определено в:* `go/cli/internal/common/fs/project.go`


**Тип ответа:** ProjectDir


```json
{
  "path": "string",
  "verbose": false
}
```


*Определено в:* `go/cli/internal/common/fs/project.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ProjectDir`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/fs/project.go:20`



---


[function] name: Path file: go/cli/internal/common/fs/project.go:60 returns_error: нет description: Path returns the absolute path to the project directory.


### Path (go/cli/internal/common/fs/project.go:60)


Path returns the absolute path to the project directory.


```go
func (p *ProjectDir) Path(()) ()
```


📍 *Расположение:* `go/cli/internal/common/fs/project.go:60`



---


[function] name: Validate file: go/cli/internal/common/fs/project.go:66 returns_error: нет description: Validate checks if the project directory exists.
Returns an error if the directory doesn't exist or the path is empty.


### Validate (go/cli/internal/common/fs/project.go:66)


Validate checks if the project directory exists.
Returns an error if the directory doesn't exist or the path is empty.


```go
func (p *ProjectDir) Validate(()) ()
```


📍 *Расположение:* `go/cli/internal/common/fs/project.go:66`



---


[function] name: resolvePath file: go/cli/internal/common/fs/project.go:39 returns_error: да description: resolvePath resolves a path to an absolute path.
If the path is empty, it returns the current working directory.
If the 


### resolvePath (go/cli/internal/common/fs/project.go:39)


resolvePath resolves a path to an absolute path.
If the path is empty, it returns the current working directory.
If the path is relative, it converts it to an absolute path.


```go
func resolvePath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/fs/project.go:39`




## go/cli/internal/common/generator/base.go


📄 Исходный файл: `go/cli/internal/common/generator/base.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GenerateProject](#generateproject-gocliinternalcommongeneratorbasego55) `:55`

- 🔗 [NewBaseGenerator](#newbasegenerator-gocliinternalcommongeneratorbasego42) `:42`

- 🔗 [ReadTemplateFile](#readtemplatefile-gocliinternalcommongeneratorbasego160) `:160`

- 🔗 [RenderTemplate](#rendertemplate-gocliinternalcommongeneratorbasego128) `:128`

- 🔗 [initGitRepo](#initgitrepo-gocliinternalcommongeneratorbasego143) `:143`


</details>


[function] name: GenerateProject file: go/cli/internal/common/generator/base.go:55 returns_error: нет description: GenerateProject generates a new project using the provided templates.
It walks through all template files, renders them 


### GenerateProject (go/cli/internal/common/generator/base.go:55)


GenerateProject generates a new project using the provided templates.
It walks through all template files, renders them with the config data,
and writes the results to the target directory.


```go
func (g *BaseGenerator) GenerateProject((config ProjectConfig)) (config ProjectConfig)
```


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


📍 *Расположение:* `go/cli/internal/common/generator/base.go:55`



---


[function] name: NewBaseGenerator file: go/cli/internal/common/generator/base.go:42 returns_error: нет description: NewBaseGenerator creates a new base generator with the specified configuration.


### NewBaseGenerator (go/cli/internal/common/generator/base.go:42)


NewBaseGenerator creates a new base generator with the specified configuration.


```go
func NewBaseGenerator((templateFiles fs.FS, templateRoot string)) (templateFiles fs.FS, templateRoot string)
```


**Тип ответа:** templateFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fs.FS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** templateRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/generator/base.go:42`



---


[function] name: ReadTemplateFile file: go/cli/internal/common/generator/base.go:160 returns_error: да description: ReadTemplateFile reads a template file from the embedded filesystem.
This is a convenience method for reading individual


### ReadTemplateFile (go/cli/internal/common/generator/base.go:160)


ReadTemplateFile reads a template file from the embedded filesystem.
This is a convenience method for reading individual template files.


```go
func (g *BaseGenerator) ReadTemplateFile(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/generator/base.go:160`



---


[function] name: RenderTemplate file: go/cli/internal/common/generator/base.go:128 returns_error: да description: RenderTemplate renders a template string with the provided data.
This is the core template rendering logic used by all g


### RenderTemplate (go/cli/internal/common/generator/base.go:128)


RenderTemplate renders a template string with the provided data.
This is the core template rendering logic used by all generators.


```go
func (g *BaseGenerator) RenderTemplate((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/generator/base.go:128`



---


[function] name: initGitRepo file: go/cli/internal/common/generator/base.go:143 returns_error: нет description: initGitRepo initializes a git repository in the specified directory.


### initGitRepo (go/cli/internal/common/generator/base.go:143)


initGitRepo initializes a git repository in the specified directory.


```go
func (g *BaseGenerator) initGitRepo((dir string, verbose bool)) (dir string, verbose bool)
```


**Тип ответа:** dir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/generator/base.go:143`




## go/cli/internal/common/image/image.go


📄 Исходный файл: `go/cli/internal/common/image/image.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ConstructImageName](#constructimagename-gocliinternalcommonimageimagego13) `:13`

- 🔗 [ConstructMCPServerImageName](#constructmcpserverimagename-gocliinternalcommonimageimagego23) `:23`


</details>


[function] name: ConstructImageName file: go/cli/internal/common/image/image.go:13 returns_error: нет description: ConstructImageName constructs a Docker image name with default registry and tag.
If configImage is provided (non-empty),


### ConstructImageName (go/cli/internal/common/image/image.go:13)


ConstructImageName constructs a Docker image name with default registry and tag.
If configImage is provided (non-empty), it is returned as-is.
Otherwise, constructs: DefaultRegistry/imageName:DefaultTag (e.g., "localhost:5001/my-agent:latest")


```go
func ConstructImageName((configImage, imageName string)) (configImage, imageName string)
```


**Тип ответа:** configImage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/image/image.go:13`



---


[function] name: ConstructMCPServerImageName file: go/cli/internal/common/image/image.go:23 returns_error: нет description: ConstructMCPServerImageName constructs a Docker image name for an MCP server.
The image name follows the pattern: Defaul


### ConstructMCPServerImageName (go/cli/internal/common/image/image.go:23)


ConstructMCPServerImageName constructs a Docker image name for an MCP server.
The image name follows the pattern: DefaultRegistry/agentName-serverName:DefaultTag
(e.g., "localhost:5001/my-agent-github-server:latest")


```go
func ConstructMCPServerImageName((agentName, serverName string)) (agentName, serverName string)
```


**Тип ответа:** agentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** serverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/common/image/image.go:23`




## go/cli/internal/common/k8s/config.go


📄 Исходный файл: `go/cli/internal/common/k8s/config.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetCurrentContext](#getcurrentcontext-gocliinternalcommonk8sconfiggo54) `:54`

- 🔗 [GetCurrentKindClusterName](#getcurrentkindclustername-gocliinternalcommonk8sconfiggo29) `:29`

- 🔗 [GetCurrentNamespace](#getcurrentnamespace-gocliinternalcommonk8sconfiggo13) `:13`

- 🔗 [IsKindCluster](#iskindcluster-gocliinternalcommonk8sconfiggo69) `:69`


</details>


[function] name: GetCurrentContext file: go/cli/internal/common/k8s/config.go:54 returns_error: да description: GetCurrentContext returns the name of the current kubeconfig context.


### GetCurrentContext (go/cli/internal/common/k8s/config.go:54)


GetCurrentContext returns the name of the current kubeconfig context.


```go
func GetCurrentContext((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/k8s/config.go:54`



---


[function] name: GetCurrentKindClusterName file: go/cli/internal/common/k8s/config.go:29 returns_error: да description: GetCurrentKindClusterName extracts the kind cluster name from the current kubeconfig context.
Returns an error if the cu


### GetCurrentKindClusterName (go/cli/internal/common/k8s/config.go:29)


GetCurrentKindClusterName extracts the kind cluster name from the current kubeconfig context.
Returns an error if the current context is not a kind cluster.


```go
func GetCurrentKindClusterName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/k8s/config.go:29`



---


[function] name: GetCurrentNamespace file: go/cli/internal/common/k8s/config.go:13 returns_error: да description: GetCurrentNamespace returns the current namespace from the kubeconfig.
If no namespace is configured, it returns an erro


### GetCurrentNamespace (go/cli/internal/common/k8s/config.go:13)


GetCurrentNamespace returns the current namespace from the kubeconfig.
If no namespace is configured, it returns an error.


```go
func GetCurrentNamespace((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/k8s/config.go:13`



---


[function] name: IsKindCluster file: go/cli/internal/common/k8s/config.go:69 returns_error: нет description: IsKindCluster checks if the current kubeconfig context points to a kind cluster.


### IsKindCluster (go/cli/internal/common/k8s/config.go:69)


IsKindCluster checks if the current kubeconfig context points to a kind cluster.


```go
func IsKindCluster(()) ()
```


📍 *Расположение:* `go/cli/internal/common/k8s/config.go:69`




## go/cli/internal/common/prompt/input.go


📄 Исходный файл: `go/cli/internal/common/prompt/input.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [PromptForConfirmation](#promptforconfirmation-gocliinternalcommonpromptinputgo25) `:25`

- 🔗 [PromptForInput](#promptforinput-gocliinternalcommonpromptinputgo13) `:13`

- 🔗 [PromptForSelection](#promptforselection-gocliinternalcommonpromptinputgo53) `:53`

- 🔗 [PromptWithDefault](#promptwithdefault-gocliinternalcommonpromptinputgo37) `:37`


</details>


[function] name: PromptForConfirmation file: go/cli/internal/common/prompt/input.go:25 returns_error: да description: PromptForConfirmation asks a yes/no question and returns true if the user confirms.
Accepts "y", "yes" (case-insensitive


### PromptForConfirmation (go/cli/internal/common/prompt/input.go:25)


PromptForConfirmation asks a yes/no question and returns true if the user confirms.
Accepts "y", "yes" (case-insensitive) as confirmation.


```go
func PromptForConfirmation((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/prompt/input.go:25`



---


[function] name: PromptForInput file: go/cli/internal/common/prompt/input.go:13 returns_error: да description: PromptForInput displays a prompt and reads user input from stdin.
Returns the trimmed input string or an error if readin


### PromptForInput (go/cli/internal/common/prompt/input.go:13)


PromptForInput displays a prompt and reads user input from stdin.
Returns the trimmed input string or an error if reading fails.


```go
func PromptForInput((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/prompt/input.go:13`



---


[function] name: PromptForSelection file: go/cli/internal/common/prompt/input.go:53 returns_error: да description: PromptForSelection displays a list of options and prompts the user to select one.
Returns the index of the selected opti


### PromptForSelection (go/cli/internal/common/prompt/input.go:53)


PromptForSelection displays a list of options and prompts the user to select one.
Returns the index of the selected option (0-based) or an error.


```go
func PromptForSelection((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/prompt/input.go:53`



---


[function] name: PromptWithDefault file: go/cli/internal/common/prompt/input.go:37 returns_error: да description: PromptWithDefault displays a prompt with a default value and reads user input.
If the user presses Enter without typing 


### PromptWithDefault (go/cli/internal/common/prompt/input.go:37)


PromptWithDefault displays a prompt with a default value and reads user input.
If the user presses Enter without typing anything, the default value is returned.


```go
func PromptWithDefault((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/common/prompt/input.go:37`




## go/cli/internal/config/config.go


📄 Исходный файл: `go/cli/internal/config/config.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Client](#client-gocliinternalconfigconfiggo23) `:23`

- 🔗 [Get](#get-gocliinternalconfigconfiggo65) `:65`

- 🔗 [Init](#init-gocliinternalconfigconfiggo27) `:27`


</details>


[function] name: Client file: go/cli/internal/config/config.go:23 returns_error: нет description: —


### Client (go/cli/internal/config/config.go:23)


Client is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Config) Client(()) ()
```


📍 *Расположение:* `go/cli/internal/config/config.go:23`



---


[function] name: Get file: go/cli/internal/config/config.go:65 returns_error: да description: —


### Get (go/cli/internal/config/config.go:65)


Get is a function that retrieves data based on the provided parameters and may return an error.


```go
func Get((*Config, error)) (*Config, error)
```


**Тип запроса:** Config


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


**Тип ответа:** Config


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


*Типы возврата:* `*Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/config/config.go:65`



---


[function] name: Init file: go/cli/internal/config/config.go:27 returns_error: нет description: —


### Init (go/cli/internal/config/config.go:27)


Init is a function that performs operations based on the provided parameters and returns ().


```go
func Init(()) ()
```


📍 *Расположение:* `go/cli/internal/config/config.go:27`




## go/cli/internal/config/utils.go


📄 Исходный файл: `go/cli/internal/config/utils.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [BoldBlue](#boldblue-gocliinternalconfigutilsgo34) `:34`

- 🔗 [BoldGreen](#boldgreen-gocliinternalconfigutilsgo38) `:38`

- 🔗 [BoldRed](#boldred-gocliinternalconfigutilsgo46) `:46`

- 🔗 [BoldYellow](#boldyellow-gocliinternalconfigutilsgo42) `:42`

- 🔗 [GetCfg](#getcfg-gocliinternalconfigutilsgo26) `:26`

- 🔗 [GetClient](#getclient-gocliinternalconfigutilsgo30) `:30`

- 🔗 [GetConfigDir](#getconfigdir-gocliinternalconfigutilsgo50) `:50`

- 🔗 [SetCfg](#setcfg-gocliinternalconfigutilsgo18) `:18`

- 🔗 [SetClient](#setclient-gocliinternalconfigutilsgo22) `:22`

- 🔗 [SetHistoryPath](#sethistorypath-gocliinternalconfigutilsgo66) `:66`


</details>


[function] name: BoldBlue file: go/cli/internal/config/utils.go:34 returns_error: нет description: —


### BoldBlue (go/cli/internal/config/utils.go:34)


BoldBlue is a function that performs operations based on the provided parameters and returns (s string).


```go
func BoldBlue((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/config/utils.go:34`



---


[function] name: BoldGreen file: go/cli/internal/config/utils.go:38 returns_error: нет description: —


### BoldGreen (go/cli/internal/config/utils.go:38)


BoldGreen is a function that performs operations based on the provided parameters and returns (s string).


```go
func BoldGreen((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/config/utils.go:38`



---


[function] name: BoldRed file: go/cli/internal/config/utils.go:46 returns_error: нет description: —


### BoldRed (go/cli/internal/config/utils.go:46)


BoldRed is a function that performs operations based on the provided parameters and returns (s string).


```go
func BoldRed((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/config/utils.go:46`



---


[function] name: BoldYellow file: go/cli/internal/config/utils.go:42 returns_error: нет description: —


### BoldYellow (go/cli/internal/config/utils.go:42)


BoldYellow is a function that performs operations based on the provided parameters and returns (s string).


```go
func BoldYellow((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/config/utils.go:42`



---


[function] name: GetCfg file: go/cli/internal/config/utils.go:26 returns_error: нет description: —


### GetCfg (go/cli/internal/config/utils.go:26)


GetCfg is a function that retrieves data based on the provided parameters and returns (shell *ishell.Context).


```go
func GetCfg((shell *ishell.Context)) (shell *ishell.Context)
```


**Тип запроса:** ishell.Context


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


**Тип ответа:** shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ishell.Context


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


📍 *Расположение:* `go/cli/internal/config/utils.go:26`



---


[function] name: GetClient file: go/cli/internal/config/utils.go:30 returns_error: нет description: —


### GetClient (go/cli/internal/config/utils.go:30)


GetClient is a function that retrieves data based on the provided parameters and returns (shell *ishell.Context).


```go
func GetClient((shell *ishell.Context)) (shell *ishell.Context)
```


**Тип запроса:** ishell.Context


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


**Тип ответа:** shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ishell.Context


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


📍 *Расположение:* `go/cli/internal/config/utils.go:30`



---


[function] name: GetConfigDir file: go/cli/internal/config/utils.go:50 returns_error: да description: —


### GetConfigDir (go/cli/internal/config/utils.go:50)


GetConfigDir is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetConfigDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/config/utils.go:50`



---


[function] name: SetCfg file: go/cli/internal/config/utils.go:18 returns_error: нет description: —


### SetCfg (go/cli/internal/config/utils.go:18)


SetCfg is a function that updates data based on the provided parameters and returns (shell *ishell.Shell, cfg *Config).


```go
func SetCfg((shell *ishell.Shell, cfg *Config)) (shell *ishell.Shell, cfg *Config)
```


**Тип запроса:** ishell.Shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** Config


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


**Тип ответа:** shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ishell.Shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Config


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


📍 *Расположение:* `go/cli/internal/config/utils.go:18`



---


[function] name: SetClient file: go/cli/internal/config/utils.go:22 returns_error: нет description: —


### SetClient (go/cli/internal/config/utils.go:22)


SetClient is a function that updates data based on the provided parameters and returns (shell *ishell.Shell, client *client.ClientSet).


```go
func SetClient((shell *ishell.Shell, client *client.ClientSet)) (shell *ishell.Shell, client *client.ClientSet)
```


**Тип запроса:** ishell.Shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


**Тип ответа:** shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ishell.Shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


📍 *Расположение:* `go/cli/internal/config/utils.go:22`



---


[function] name: SetHistoryPath file: go/cli/internal/config/utils.go:66 returns_error: нет description: —


### SetHistoryPath (go/cli/internal/config/utils.go:66)


SetHistoryPath is a function that updates data based on the provided parameters and returns (homeDir string, shell *ishell.Shell).


```go
func SetHistoryPath((homeDir string, shell *ishell.Shell)) (homeDir string, shell *ishell.Shell)
```


**Тип запроса:** ishell.Shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** homeDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ishell.Shell


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/config/utils.go:66`




## go/cli/internal/mcp/builder/builder.go


📄 Исходный файл: `go/cli/internal/mcp/builder/builder.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Build](#build-gocliinternalmcpbuilderbuildergo30) `:30`

- 🔗 [New](#new-gocliinternalmcpbuilderbuildergo25) `:25`

- 🔗 [buildDockerImage](#builddockerimage-gocliinternalmcpbuilderbuildergo95) `:95`

- 🔗 [detectProjectType](#detectprojecttype-gocliinternalmcpbuilderbuildergo61) `:61`

- 🔗 [fileExists](#fileexists-gocliinternalmcpbuilderbuildergo89) `:89`


</details>


[function] name: Build file: go/cli/internal/mcp/builder/builder.go:30 returns_error: нет description: Build executes the build process for an MCP server


### Build (go/cli/internal/mcp/builder/builder.go:30)


Build executes the build process for an MCP server


```go
func (b *Builder) Build((opts Options)) (opts Options)
```


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Options


```json
{
  "ProjectDir": "string",
  "Tag": "string",
  "Platform": "string",
  "Verbose": false
}
```


*Определено в:* `go/cli/internal/mcp/builder/builder.go`


📍 *Расположение:* `go/cli/internal/mcp/builder/builder.go:30`



---


[function] name: New file: go/cli/internal/mcp/builder/builder.go:25 returns_error: нет description: New creates a new Builder instance


### New (go/cli/internal/mcp/builder/builder.go:25)


New creates a new Builder instance


```go
func New(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/builder/builder.go:25`



---


[function] name: buildDockerImage file: go/cli/internal/mcp/builder/builder.go:95 returns_error: нет description: buildDockerImage builds a Docker image


### buildDockerImage (go/cli/internal/mcp/builder/builder.go:95)


buildDockerImage builds a Docker image


```go
func (b *Builder) buildDockerImage((opts Options, projectType string)) (opts Options, projectType string)
```


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Options


```json
{
  "ProjectDir": "string",
  "Tag": "string",
  "Platform": "string",
  "Verbose": false
}
```


*Определено в:* `go/cli/internal/mcp/builder/builder.go`


**Тип ответа:** projectType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/builder/builder.go:95`



---


[function] name: detectProjectType file: go/cli/internal/mcp/builder/builder.go:61 returns_error: да description: detectProjectType determines the project type based on files present


### detectProjectType (go/cli/internal/mcp/builder/builder.go:61)


detectProjectType determines the project type based on files present


```go
func (b *Builder) detectProjectType((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/mcp/builder/builder.go:61`



---


[function] name: fileExists file: go/cli/internal/mcp/builder/builder.go:89 returns_error: нет description: fileExists checks if a file exists


### fileExists (go/cli/internal/mcp/builder/builder.go:89)


fileExists checks if a file exists


```go
func (b *Builder) fileExists((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/builder/builder.go:89`




## go/cli/internal/mcp/frameworks/common/base_generator.go


📄 Исходный файл: `go/cli/internal/mcp/frameworks/common/base_generator.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [GenerateProject](#generateproject-gocliinternalmcpframeworkscommonbase_generatorgo56) `:56`

- 🔗 [GenerateTool](#generatetool-gocliinternalmcpframeworkscommonbase_generatorgo65) `:65`

- 🔗 [GenerateToolFile](#generatetoolfile-gocliinternalmcpframeworkscommonbase_generatorgo103) `:103`

- 🔗 [GetDirectory](#getdirectory-gocliinternalmcpframeworkscommonbase_generatorgo24) `:24`

- 🔗 [IsVerbose](#isverbose-gocliinternalmcpframeworkscommonbase_generatorgo28) `:28`

- 🔗 [NewBaseGenerator](#newbasegenerator-gocliinternalmcpframeworkscommonbase_generatorgo48) `:48`

- 🔗 [ShouldInitGit](#shouldinitgit-gocliinternalmcpframeworkscommonbase_generatorgo32) `:32`

- 🔗 [ShouldSkipPath](#shouldskippath-gocliinternalmcpframeworkscommonbase_generatorgo36) `:36`


</details>


[function] name: GenerateProject file: go/cli/internal/mcp/frameworks/common/base_generator.go:56 returns_error: нет description: GenerateProject generates a new project using the shared generator


### GenerateProject (go/cli/internal/mcp/frameworks/common/base_generator.go:56)


GenerateProject generates a new project using the shared generator


```go
func (g *BaseGenerator) GenerateProject((config mcp.ProjectConfig)) (config mcp.ProjectConfig)
```


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:56`



---


[function] name: GenerateTool file: go/cli/internal/mcp/frameworks/common/base_generator.go:65 returns_error: нет description: GenerateTool generates a new tool for a project.


### GenerateTool (go/cli/internal/mcp/frameworks/common/base_generator.go:65)


GenerateTool generates a new tool for a project.


```go
func (g *BaseGenerator) GenerateTool((projectRoot string, config mcp.ToolConfig)) (projectRoot string, config mcp.ToolConfig)
```


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:65`



---


[function] name: GenerateToolFile file: go/cli/internal/mcp/frameworks/common/base_generator.go:103 returns_error: нет description: GenerateToolFile generates a new tool file from the unified template.
This uses the shared generator's RenderTemplate me


### GenerateToolFile (go/cli/internal/mcp/frameworks/common/base_generator.go:103)


GenerateToolFile generates a new tool file from the unified template.
This uses the shared generator's RenderTemplate method.


```go
func (g *BaseGenerator) GenerateToolFile((filePath string, config mcp.ToolConfig)) (filePath string, config mcp.ToolConfig)
```


**Тип ответа:** filePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:103`



---


[function] name: GetDirectory file: go/cli/internal/mcp/frameworks/common/base_generator.go:24 returns_error: нет description: —


### GetDirectory (go/cli/internal/mcp/frameworks/common/base_generator.go:24)


GetDirectory is a method that retrieves data based on the provided parameters and returns ().


```go
func (a mcpConfigAdapter) GetDirectory(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:24`



---


[function] name: IsVerbose file: go/cli/internal/mcp/frameworks/common/base_generator.go:28 returns_error: нет description: —


### IsVerbose (go/cli/internal/mcp/frameworks/common/base_generator.go:28)


IsVerbose is a method that performs operations based on the provided parameters and returns ().


```go
func (a mcpConfigAdapter) IsVerbose(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:28`



---


[function] name: NewBaseGenerator file: go/cli/internal/mcp/frameworks/common/base_generator.go:48 returns_error: нет description: NewBaseGenerator creates a new MCP base generator


### NewBaseGenerator (go/cli/internal/mcp/frameworks/common/base_generator.go:48)


NewBaseGenerator creates a new MCP base generator


```go
func NewBaseGenerator((templateFiles fs.FS, toolTemplateName string)) (templateFiles fs.FS, toolTemplateName string)
```


**Тип ответа:** templateFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fs.FS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** toolTemplateName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:48`



---


[function] name: ShouldInitGit file: go/cli/internal/mcp/frameworks/common/base_generator.go:32 returns_error: нет description: —


### ShouldInitGit (go/cli/internal/mcp/frameworks/common/base_generator.go:32)


ShouldInitGit is a method that performs operations based on the provided parameters and returns ().


```go
func (a mcpConfigAdapter) ShouldInitGit(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:32`



---


[function] name: ShouldSkipPath file: go/cli/internal/mcp/frameworks/common/base_generator.go:36 returns_error: нет description: —


### ShouldSkipPath (go/cli/internal/mcp/frameworks/common/base_generator.go:36)


ShouldSkipPath is a method that performs operations based on the provided parameters and returns (path string).


```go
func (a mcpConfigAdapter) ShouldSkipPath((path string)) (path string)
```


**Тип ответа:** path


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/common/base_generator.go:36`




## go/cli/internal/mcp/frameworks/frameworks.go


📄 Исходный файл: `go/cli/internal/mcp/frameworks/frameworks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetGenerator](#getgenerator-gocliinternalmcpframeworksframeworksgo20) `:20`


</details>


[function] name: GetGenerator file: go/cli/internal/mcp/frameworks/frameworks.go:20 returns_error: да description: GetGenerator returns a generator for the specified framework.


### GetGenerator (go/cli/internal/mcp/frameworks/frameworks.go:20)


GetGenerator returns a generator for the specified framework.


```go
func GetGenerator((Generator, error)) (Generator, error)
```


**Тип ответа:** Generator


```json
{
  "TemplateFiles": {},
  "TemplateRoot": "string"
}
```


*Определено в:* `go/cli/internal/common/generator/base.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Generator`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/mcp/frameworks/frameworks.go:20`




## go/cli/internal/mcp/frameworks/golang/generator.go


📄 Исходный файл: `go/cli/internal/mcp/frameworks/golang/generator.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GenerateProject](#generateproject-gocliinternalmcpframeworksgolanggeneratorgo29) `:29`

- 🔗 [GenerateTool](#generatetool-gocliinternalmcpframeworksgolanggeneratorgo47) `:47`

- 🔗 [NewGenerator](#newgenerator-gocliinternalmcpframeworksgolanggeneratorgo22) `:22`

- 🔗 [tidyGoMod](#tidygomod-gocliinternalmcpframeworksgolanggeneratorgo65) `:65`


</details>


[function] name: GenerateProject file: go/cli/internal/mcp/frameworks/golang/generator.go:29 returns_error: нет description: GenerateProject generates a new Go project.


### GenerateProject (go/cli/internal/mcp/frameworks/golang/generator.go:29)


GenerateProject generates a new Go project.


```go
func (g *Generator) GenerateProject((config mcp.ProjectConfig)) (config mcp.ProjectConfig)
```


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/golang/generator.go:29`



---


[function] name: GenerateTool file: go/cli/internal/mcp/frameworks/golang/generator.go:47 returns_error: нет description: GenerateTool generates a new tool for a Python project.


### GenerateTool (go/cli/internal/mcp/frameworks/golang/generator.go:47)


GenerateTool generates a new tool for a Python project.


```go
func (g *Generator) GenerateTool((projectroot string, config mcp.ToolConfig)) (projectroot string, config mcp.ToolConfig)
```


**Тип ответа:** projectroot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/golang/generator.go:47`



---


[function] name: NewGenerator file: go/cli/internal/mcp/frameworks/golang/generator.go:22 returns_error: нет description: NewGenerator creates a new Go generator.


### NewGenerator (go/cli/internal/mcp/frameworks/golang/generator.go:22)


NewGenerator creates a new Go generator.


```go
func NewGenerator(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/frameworks/golang/generator.go:22`



---


[function] name: tidyGoMod file: go/cli/internal/mcp/frameworks/golang/generator.go:65 returns_error: нет description: —


### tidyGoMod (go/cli/internal/mcp/frameworks/golang/generator.go:65)


tidyGoMod is a method that performs operations based on the provided parameters and returns (dir string, verbose bool).


```go
func (g *Generator) tidyGoMod((dir string, verbose bool)) (dir string, verbose bool)
```


**Тип ответа:** dir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/golang/generator.go:65`




## go/cli/internal/mcp/frameworks/java/generator.go


📄 Исходный файл: `go/cli/internal/mcp/frameworks/java/generator.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [GenerateProject](#generateproject-gocliinternalmcpframeworksjavageneratorgo34) `:34`

- 🔗 [GenerateTool](#generatetool-gocliinternalmcpframeworksjavageneratorgo53) `:53`

- 🔗 [NewGenerator](#newgenerator-gocliinternalmcpframeworksjavageneratorgo27) `:27`

- 🔗 [regenerateToolsClass](#regeneratetoolsclass-gocliinternalmcpframeworksjavageneratorgo85) `:85`

- 🔗 [renderTemplate](#rendertemplate-gocliinternalmcpframeworksjavageneratorgo142) `:142`

- 🔗 [scanToolsDirectory](#scantoolsdirectory-gocliinternalmcpframeworksjavageneratorgo115) `:115`


</details>


[function] name: GenerateProject file: go/cli/internal/mcp/frameworks/java/generator.go:34 returns_error: нет description: GenerateProject generates a new Java project


### GenerateProject (go/cli/internal/mcp/frameworks/java/generator.go:34)


GenerateProject generates a new Java project


```go
func (g *Generator) GenerateProject((config mcp.ProjectConfig)) (config mcp.ProjectConfig)
```


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/java/generator.go:34`



---


[function] name: GenerateTool file: go/cli/internal/mcp/frameworks/java/generator.go:53 returns_error: нет description: GenerateTool generates a new tool for a Java project.


### GenerateTool (go/cli/internal/mcp/frameworks/java/generator.go:53)


GenerateTool generates a new tool for a Java project.


```go
func (g *Generator) GenerateTool((projectRoot string, config mcp.ToolConfig)) (projectRoot string, config mcp.ToolConfig)
```


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/java/generator.go:53`



---


[function] name: NewGenerator file: go/cli/internal/mcp/frameworks/java/generator.go:27 returns_error: нет description: NewGenerator creates a new Java generator


### NewGenerator (go/cli/internal/mcp/frameworks/java/generator.go:27)


NewGenerator creates a new Java generator


```go
func NewGenerator(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/frameworks/java/generator.go:27`



---


[function] name: regenerateToolsClass file: go/cli/internal/mcp/frameworks/java/generator.go:85 returns_error: нет description: regenerateToolsClass regenerates the Tools.java file in the tools directory


### regenerateToolsClass (go/cli/internal/mcp/frameworks/java/generator.go:85)


regenerateToolsClass regenerates the Tools.java file in the tools directory


```go
func (g *Generator) regenerateToolsClass((toolsDir string)) (toolsDir string)
```


**Тип ответа:** toolsDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/java/generator.go:85`



---


[function] name: renderTemplate file: go/cli/internal/mcp/frameworks/java/generator.go:142 returns_error: да description: renderTemplate renders a template string with the provided data


### renderTemplate (go/cli/internal/mcp/frameworks/java/generator.go:142)


renderTemplate renders a template string with the provided data


```go
func renderTemplate((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/mcp/frameworks/java/generator.go:142`



---


[function] name: scanToolsDirectory file: go/cli/internal/mcp/frameworks/java/generator.go:115 returns_error: да description: scanToolsDirectory scans the tools directory and returns a list of tool names


### scanToolsDirectory (go/cli/internal/mcp/frameworks/java/generator.go:115)


scanToolsDirectory scans the tools directory and returns a list of tool names


```go
func (g *Generator) scanToolsDirectory(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/mcp/frameworks/java/generator.go:115`




## go/cli/internal/mcp/frameworks/python/generator.go


📄 Исходный файл: `go/cli/internal/mcp/frameworks/python/generator.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [GenerateProject](#generateproject-gocliinternalmcpframeworkspythongeneratorgo31) `:31`

- 🔗 [GenerateTool](#generatetool-gocliinternalmcpframeworkspythongeneratorgo44) `:44`

- 🔗 [NewGenerator](#newgenerator-gocliinternalmcpframeworkspythongeneratorgo24) `:24`

- 🔗 [generateInitContent](#generateinitcontent-gocliinternalmcpframeworkspythongeneratorgo114) `:114`

- 🔗 [regenerateToolsInit](#regeneratetoolsinit-gocliinternalmcpframeworkspythongeneratorgo71) `:71`

- 🔗 [scanToolsDirectory](#scantoolsdirectory-gocliinternalmcpframeworkspythongeneratorgo87) `:87`


</details>


[function] name: GenerateProject file: go/cli/internal/mcp/frameworks/python/generator.go:31 returns_error: нет description: GenerateProject generates a new Python project


### GenerateProject (go/cli/internal/mcp/frameworks/python/generator.go:31)


GenerateProject generates a new Python project


```go
func (g *Generator) GenerateProject((config mcp.ProjectConfig)) (config mcp.ProjectConfig)
```


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/python/generator.go:31`



---


[function] name: GenerateTool file: go/cli/internal/mcp/frameworks/python/generator.go:44 returns_error: нет description: GenerateTool generates a new tool for a Python project.


### GenerateTool (go/cli/internal/mcp/frameworks/python/generator.go:44)


GenerateTool generates a new tool for a Python project.


```go
func (g *Generator) GenerateTool((projectroot string, config mcp.ToolConfig)) (projectroot string, config mcp.ToolConfig)
```


**Тип ответа:** projectroot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/python/generator.go:44`



---


[function] name: NewGenerator file: go/cli/internal/mcp/frameworks/python/generator.go:24 returns_error: нет description: NewGenerator creates a new Python generator


### NewGenerator (go/cli/internal/mcp/frameworks/python/generator.go:24)


NewGenerator creates a new Python generator


```go
func NewGenerator(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/frameworks/python/generator.go:24`



---


[function] name: generateInitContent file: go/cli/internal/mcp/frameworks/python/generator.go:114 returns_error: нет description: generateInitContent generates the content for the __init__.py file


### generateInitContent (go/cli/internal/mcp/frameworks/python/generator.go:114)


generateInitContent generates the content for the __init__.py file


```go
func (g *Generator) generateInitContent((tools []string)) (tools []string)
```


**Тип ответа:** tools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/python/generator.go:114`



---


[function] name: regenerateToolsInit file: go/cli/internal/mcp/frameworks/python/generator.go:71 returns_error: нет description: regenerateToolsInit regenerates the __init__.py file in the tools directory


### regenerateToolsInit (go/cli/internal/mcp/frameworks/python/generator.go:71)


regenerateToolsInit regenerates the __init__.py file in the tools directory


```go
func (g *Generator) regenerateToolsInit((toolsDir string)) (toolsDir string)
```


**Тип ответа:** toolsDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/python/generator.go:71`



---


[function] name: scanToolsDirectory file: go/cli/internal/mcp/frameworks/python/generator.go:87 returns_error: да description: scanToolsDirectory scans the tools directory and returns a list of tool names


### scanToolsDirectory (go/cli/internal/mcp/frameworks/python/generator.go:87)


scanToolsDirectory scans the tools directory and returns a list of tool names


```go
func (g *Generator) scanToolsDirectory(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/mcp/frameworks/python/generator.go:87`




## go/cli/internal/mcp/frameworks/typescript/generator.go


📄 Исходный файл: `go/cli/internal/mcp/frameworks/typescript/generator.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [GenerateProject](#generateproject-gocliinternalmcpframeworkstypescriptgeneratorgo32) `:32`

- 🔗 [GenerateTool](#generatetool-gocliinternalmcpframeworkstypescriptgeneratorgo50) `:50`

- 🔗 [NewGenerator](#newgenerator-gocliinternalmcpframeworkstypescriptgeneratorgo25) `:25`

- 🔗 [generateToolsContent](#generatetoolscontent-gocliinternalmcpframeworkstypescriptgeneratorgo132) `:132`

- 🔗 [generateTypeScriptTool](#generatetypescripttool-gocliinternalmcpframeworkstypescriptgeneratorgo78) `:78`

- 🔗 [regenerateToolsFile](#regeneratetoolsfile-gocliinternalmcpframeworkstypescriptgeneratorgo116) `:116`

- 🔗 [scanToolsDirectory](#scantoolsdirectory-gocliinternalmcpframeworkstypescriptgeneratorgo162) `:162`


</details>


[function] name: GenerateProject file: go/cli/internal/mcp/frameworks/typescript/generator.go:32 returns_error: нет description: GenerateProject generates a new TypeScript project


### GenerateProject (go/cli/internal/mcp/frameworks/typescript/generator.go:32)


GenerateProject generates a new TypeScript project


```go
func (g *Generator) GenerateProject((config mcp.ProjectConfig)) (config mcp.ProjectConfig)
```


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ProjectConfig


```json
{
  "ProjectName": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "Directory": "string",
  "NoGit": false,
  "Verbose": false,
  "GoModuleName": "string"
}
```


*Определено в:* `go/cli/internal/mcp/config.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/typescript/generator.go:32`



---


[function] name: GenerateTool file: go/cli/internal/mcp/frameworks/typescript/generator.go:50 returns_error: нет description: GenerateTool generates a new tool for a TypeScript project.


### GenerateTool (go/cli/internal/mcp/frameworks/typescript/generator.go:50)


GenerateTool generates a new tool for a TypeScript project.


```go
func (g *Generator) GenerateTool((projectroot string, config mcp.ToolConfig)) (projectroot string, config mcp.ToolConfig)
```


**Тип ответа:** projectroot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/typescript/generator.go:50`



---


[function] name: NewGenerator file: go/cli/internal/mcp/frameworks/typescript/generator.go:25 returns_error: нет description: NewGenerator creates a new TypeScript generator


### NewGenerator (go/cli/internal/mcp/frameworks/typescript/generator.go:25)


NewGenerator creates a new TypeScript generator


```go
func NewGenerator(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/frameworks/typescript/generator.go:25`



---


[function] name: generateToolsContent file: go/cli/internal/mcp/frameworks/typescript/generator.go:132 returns_error: нет description: generateToolsContent generates the content for the tools.ts file


### generateToolsContent (go/cli/internal/mcp/frameworks/typescript/generator.go:132)


generateToolsContent generates the content for the tools.ts file


```go
func (g *Generator) generateToolsContent((tools []string)) (tools []string)
```


**Тип ответа:** tools


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/typescript/generator.go:132`



---


[function] name: generateTypeScriptTool file: go/cli/internal/mcp/frameworks/typescript/generator.go:78 returns_error: нет description: generateTypeScriptTool generates a TypeScript tool with camelCase file naming


### generateTypeScriptTool (go/cli/internal/mcp/frameworks/typescript/generator.go:78)


generateTypeScriptTool generates a TypeScript tool with camelCase file naming


```go
func (g *Generator) generateTypeScriptTool((projectRoot string, config mcp.ToolConfig)) (projectRoot string, config mcp.ToolConfig)
```


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mcp.ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/frameworks/typescript/generator.go:78`



---


[function] name: regenerateToolsFile file: go/cli/internal/mcp/frameworks/typescript/generator.go:116 returns_error: нет description: regenerateToolsFile regenerates the tools.ts file in the src directory


### regenerateToolsFile (go/cli/internal/mcp/frameworks/typescript/generator.go:116)


regenerateToolsFile regenerates the tools.ts file in the src directory


```go
func (g *Generator) regenerateToolsFile((projectRoot string)) (projectRoot string)
```


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/frameworks/typescript/generator.go:116`



---


[function] name: scanToolsDirectory file: go/cli/internal/mcp/frameworks/typescript/generator.go:162 returns_error: да description: scanToolsDirectory scans the tools directory and returns a list of tool names


### scanToolsDirectory (go/cli/internal/mcp/frameworks/typescript/generator.go:162)


scanToolsDirectory scans the tools directory and returns a list of tool names


```go
func (g *Generator) scanToolsDirectory(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/mcp/frameworks/typescript/generator.go:162`




## go/cli/internal/mcp/manifests/manager.go


📄 Исходный файл: `go/cli/internal/mcp/manifests/manager.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [AddTool](#addtool-gocliinternalmcpmanifestsmanagergo151) `:151`

- 🔗 [Exists](#exists-gocliinternalmcpmanifestsmanagergo77) `:77`

- 🔗 [GetDefault](#getdefault-gocliinternalmcpmanifestsmanagergo84) `:84`

- 🔗 [Load](#load-gocliinternalmcpmanifestsmanagergo29) `:29`

- 🔗 [NewManager](#newmanager-gocliinternalmcpmanifestsmanagergo22) `:22`

- 🔗 [RemoveTool](#removetool-gocliinternalmcpmanifestsmanagergo169) `:169`

- 🔗 [Save](#save-gocliinternalmcpmanifestsmanagergo54) `:54`

- 🔗 [Validate](#validate-gocliinternalmcpmanifestsmanagergo121) `:121`

- 🔗 [isValidFramework](#isvalidframework-gocliinternalmcpmanifestsmanagergo204) `:204`

- 🔗 [isValidSecretProvider](#isvalidsecretprovider-gocliinternalmcpmanifestsmanagergo215) `:215`

- 🔗 [validateSecrets](#validatesecrets-gocliinternalmcpmanifestsmanagergo191) `:191`

- 🔗 [validateTool](#validatetool-gocliinternalmcpmanifestsmanagergo184) `:184`


</details>


[function] name: AddTool file: go/cli/internal/mcp/manifests/manager.go:151 returns_error: нет description: AddTool adds a new tool to the manifest


### AddTool (go/cli/internal/mcp/manifests/manager.go:151)


AddTool adds a new tool to the manifest


```go
func (m *Manager) AddTool((manifest *ProjectManifest, name string, config ToolConfig)) (manifest *ProjectManifest, name string, config ToolConfig)
```


**Тип запроса:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:151`



---


[function] name: Exists file: go/cli/internal/mcp/manifests/manager.go:77 returns_error: нет description: Exists checks if a manifest.yaml file exists in the project root


### Exists (go/cli/internal/mcp/manifests/manager.go:77)


Exists checks if a manifest.yaml file exists in the project root


```go
func (m *Manager) Exists(()) ()
```


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:77`



---


[function] name: GetDefault file: go/cli/internal/mcp/manifests/manager.go:84 returns_error: нет description: GetDefault returns a new ProjectManifest with default values


### GetDefault (go/cli/internal/mcp/manifests/manager.go:84)


GetDefault returns a new ProjectManifest with default values


```go
func GetDefault((name, framework, description, author, email, namespace string)) (name, framework, description, author, email, namespace string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** author


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** email


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:84`



---


[function] name: Load file: go/cli/internal/mcp/manifests/manager.go:29 returns_error: да description: Load reads and parses the manifest.yaml file


### Load (go/cli/internal/mcp/manifests/manager.go:29)


Load reads and parses the manifest.yaml file


```go
func (m *Manager) Load((*ProjectManifest, error)) (*ProjectManifest, error)
```


**Тип запроса:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ProjectManifest`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:29`



---


[function] name: NewManager file: go/cli/internal/mcp/manifests/manager.go:22 returns_error: нет description: NewManager creates a new manifest manager


### NewManager (go/cli/internal/mcp/manifests/manager.go:22)


NewManager creates a new manifest manager


```go
func NewManager((projectRoot string)) (projectRoot string)
```


**Тип ответа:** projectRoot


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:22`



---


[function] name: RemoveTool file: go/cli/internal/mcp/manifests/manager.go:169 returns_error: нет description: RemoveTool removes a tool from the manifest


### RemoveTool (go/cli/internal/mcp/manifests/manager.go:169)


RemoveTool removes a tool from the manifest


```go
func (m *Manager) RemoveTool((manifest *ProjectManifest, name string)) (manifest *ProjectManifest, name string)
```


**Тип запроса:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:169`



---


[function] name: Save file: go/cli/internal/mcp/manifests/manager.go:54 returns_error: нет description: Save writes the manifest to manifest.yaml


### Save (go/cli/internal/mcp/manifests/manager.go:54)


Save writes the manifest to manifest.yaml


```go
func (m *Manager) Save((manifest *ProjectManifest)) (manifest *ProjectManifest)
```


**Тип запроса:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:54`



---


[function] name: Validate file: go/cli/internal/mcp/manifests/manager.go:121 returns_error: нет description: Validate checks if the manifest is valid


### Validate (go/cli/internal/mcp/manifests/manager.go:121)


Validate checks if the manifest is valid


```go
func (m *Manager) Validate((manifest *ProjectManifest)) (manifest *ProjectManifest)
```


**Тип запроса:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


**Тип ответа:** manifest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ProjectManifest


```json
{
  "Name": "string",
  "Framework": "string",
  "Version": "string",
  "Description": "string",
  "Author": "string",
  "Email": "string",
  "Tools": {},
  "Secrets": {},
  "CreatedAt": {},
  "UpdatedAt": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:121`



---


[function] name: isValidFramework file: go/cli/internal/mcp/manifests/manager.go:204 returns_error: нет description: Helper functions


### isValidFramework (go/cli/internal/mcp/manifests/manager.go:204)


Helper functions


```go
func isValidFramework((framework string)) (framework string)
```


**Тип ответа:** framework


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:204`



---


[function] name: isValidSecretProvider file: go/cli/internal/mcp/manifests/manager.go:215 returns_error: нет description: —


### isValidSecretProvider (go/cli/internal/mcp/manifests/manager.go:215)


isValidSecretProvider is a function that performs operations based on the provided parameters and returns (provider string).


```go
func isValidSecretProvider((provider string)) (provider string)
```


**Тип ответа:** provider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:215`



---


[function] name: validateSecrets file: go/cli/internal/mcp/manifests/manager.go:191 returns_error: нет description: —


### validateSecrets (go/cli/internal/mcp/manifests/manager.go:191)


validateSecrets is a method that performs operations based on the provided parameters and returns (secrets SecretsConfig).


```go
func (m *Manager) validateSecrets((secrets SecretsConfig)) (secrets SecretsConfig)
```


**Тип ответа:** secrets


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SecretsConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:191`



---


[function] name: validateTool file: go/cli/internal/mcp/manifests/manager.go:184 returns_error: нет description: Private validation methods


### validateTool (go/cli/internal/mcp/manifests/manager.go:184)


Private validation methods


```go
func (m *Manager) validateTool((_ string, tool ToolConfig)) (_ string, tool ToolConfig)
```


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tool


```json
{
  "Name": "string",
  "ID": "string",
  "Args": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Тип ответа:** ToolConfig


```json
{
  "Name": "string",
  "Description": "string",
  "Handler": "string",
  "Enabled": false,
  "Type": "string",
  "Config": {}
}
```


*Определено в:* `go/cli/internal/mcp/manifests/types.go`


📍 *Расположение:* `go/cli/internal/mcp/manifests/manager.go:184`




## go/cli/internal/profiles/profiles.go


📄 Исходный файл: `go/cli/internal/profiles/profiles.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetProfileYaml](#getprofileyaml-gocliinternalprofilesprofilesgo18) `:18`


</details>


[function] name: GetProfileYaml file: go/cli/internal/profiles/profiles.go:18 returns_error: нет description: —


### GetProfileYaml (go/cli/internal/profiles/profiles.go:18)


GetProfileYaml is a function that retrieves data based on the provided parameters and returns (profile string).


```go
func GetProfileYaml((profile string)) (profile string)
```


**Тип ответа:** profile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/profiles/profiles.go:18`




## go/cli/internal/tui/chat.go


📄 Исходный файл: `go/cli/internal/tui/chat.go`


<details open>
<summary><b>Функции в этом файле (19)</b></summary>


- 🔗 [Init](#init-gocliinternaltuichatgo104) `:104`

- 🔗 [ResetTranscript](#resettranscript-gocliinternaltuichatgo443) `:443`

- 🔗 [RunChat](#runchat-gocliinternaltuichatgo25) `:25`

- 🔗 [SetInputVisible](#setinputvisible-gocliinternaltuichatgo450) `:450`

- 🔗 [Update](#update-gocliinternaltuichatgo108) `:108`

- 🔗 [View](#view-gocliinternaltuichatgo191) `:191`

- 🔗 [appendError](#appenderror-gocliinternaltuichatgo308) `:308`

- 🔗 [appendEvent](#appendevent-gocliinternaltuichatgo264) `:264`

- 🔗 [appendLine](#appendline-gocliinternaltuichatgo427) `:427`

- 🔗 [appendUser](#appenduser-gocliinternaltuichatgo260) `:260`

- 🔗 [extractTextFromParts](#extracttextfromparts-gocliinternaltuichatgo455) `:455`

- 🔗 [getString](#getstring-gocliinternaltuichatgo506) `:506`

- 🔗 [handleMessageParts](#handlemessageparts-gocliinternaltuichatgo313) `:313`

- 🔗 [newChatModel](#newchatmodel-gocliinternaltuichatgo73) `:73`

- 🔗 [setWorkingTime](#setworkingtime-gocliinternaltuichatgo484) `:484`

- 🔗 [submit](#submit-gocliinternaltuichatgo218) `:218`

- 🔗 [tick](#tick-gocliinternaltuichatgo477) `:477`

- 🔗 [updateStatus](#updatestatus-gocliinternaltuichatgo496) `:496`

- 🔗 [waitNext](#waitnext-gocliinternaltuichatgo246) `:246`


</details>


[function] name: Init file: go/cli/internal/tui/chat.go:104 returns_error: нет description: —


### Init (go/cli/internal/tui/chat.go:104)


Init is a method that performs operations based on the provided parameters and returns ().


```go
func (m *chatModel) Init(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/chat.go:104`



---


[function] name: ResetTranscript file: go/cli/internal/tui/chat.go:443 returns_error: нет description: ResetTranscript clears the viewport with a new header/title.


### ResetTranscript (go/cli/internal/tui/chat.go:443)


ResetTranscript clears the viewport with a new header/title.


```go
func (m *chatModel) ResetTranscript((title string)) (title string)
```


**Тип ответа:** title


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:443`



---


[function] name: RunChat file: go/cli/internal/tui/chat.go:25 returns_error: нет description: RunChat starts the TUI chat, blocking until the user exits.


### RunChat (go/cli/internal/tui/chat.go:25)


RunChat starts the TUI chat, blocking until the user exits.


```go
func RunChat((agentRef string, sessionID string, sendFn SendMessageFn, verbose bool)) (agentRef string, sessionID string, sendFn SendMessageFn, verbose bool)
```


**Тип ответа:** agentRef


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sendFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SendMessageFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:25`



---


[function] name: SetInputVisible file: go/cli/internal/tui/chat.go:450 returns_error: нет description: SetInputVisible toggles input visibility.


### SetInputVisible (go/cli/internal/tui/chat.go:450)


SetInputVisible toggles input visibility.


```go
func (m *chatModel) SetInputVisible((visible bool)) (visible bool)
```


**Тип ответа:** visible


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:450`



---


[function] name: Update file: go/cli/internal/tui/chat.go:108 returns_error: нет description: —


### Update (go/cli/internal/tui/chat.go:108)


Update is a method that updates data based on the provided parameters and returns (tea.Model, tea.Cmd).


```go
func (m *chatModel) Update((tea.Model, tea.Cmd)) (tea.Model, tea.Cmd)
```


**Тип ответа:** tea.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** tea.Cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:108`



---


[function] name: View file: go/cli/internal/tui/chat.go:191 returns_error: нет description: —


### View (go/cli/internal/tui/chat.go:191)


View is a method that performs operations based on the provided parameters and returns ().


```go
func (m *chatModel) View(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/chat.go:191`



---


[function] name: appendError file: go/cli/internal/tui/chat.go:308 returns_error: да description: —


### appendError (go/cli/internal/tui/chat.go:308)


appendError is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *chatModel) appendError((err error)) (err error)
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


📍 *Расположение:* `go/cli/internal/tui/chat.go:308`



---


[function] name: appendEvent file: go/cli/internal/tui/chat.go:264 returns_error: нет description: —


### appendEvent (go/cli/internal/tui/chat.go:264)


appendEvent is a method that performs operations based on the provided parameters and returns (ev protocol.StreamingMessageEvent).


```go
func (m *chatModel) appendEvent((ev protocol.StreamingMessageEvent)) (ev protocol.StreamingMessageEvent)
```


**Тип ответа:** ev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.StreamingMessageEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:264`



---


[function] name: appendLine file: go/cli/internal/tui/chat.go:427 returns_error: нет description: —


### appendLine (go/cli/internal/tui/chat.go:427)


appendLine is a method that performs operations based on the provided parameters and returns (s string).


```go
func (m *chatModel) appendLine((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/tui/chat.go:427`



---


[function] name: appendUser file: go/cli/internal/tui/chat.go:260 returns_error: нет description: —


### appendUser (go/cli/internal/tui/chat.go:260)


appendUser is a method that performs operations based on the provided parameters and returns (text string).


```go
func (m *chatModel) appendUser((text string)) (text string)
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


📍 *Расположение:* `go/cli/internal/tui/chat.go:260`



---


[function] name: extractTextFromParts file: go/cli/internal/tui/chat.go:455 returns_error: нет description: extractTextFromParts concatenates text from a slice of protocol.Part, stringifying non-text when reasonable.


### extractTextFromParts (go/cli/internal/tui/chat.go:455)


extractTextFromParts concatenates text from a slice of protocol.Part, stringifying non-text when reasonable.


```go
func extractTextFromParts((parts []protocol.Part)) (parts []protocol.Part)
```


**Тип ответа:** parts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Part


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:455`



---


[function] name: getString file: go/cli/internal/tui/chat.go:506 returns_error: нет description: getString safely extracts a string value from a map


### getString (go/cli/internal/tui/chat.go:506)


getString safely extracts a string value from a map


```go
func getString((m map[string]any, key string)) (m map[string]any, key string)
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


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:506`



---


[function] name: handleMessageParts file: go/cli/internal/tui/chat.go:313 returns_error: нет description: handleMessageParts processes a message and displays text, tool calls, and tool results


### handleMessageParts (go/cli/internal/tui/chat.go:313)


handleMessageParts processes a message and displays text, tool calls, and tool results


```go
func (m *chatModel) handleMessageParts((msg protocol.Message, shouldDisplay bool)) (msg protocol.Message, shouldDisplay bool)
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol.Message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shouldDisplay


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:313`



---


[function] name: newChatModel file: go/cli/internal/tui/chat.go:73 returns_error: нет description: —


### newChatModel (go/cli/internal/tui/chat.go:73)


newChatModel is a function that performs operations based on the provided parameters and returns (agentRef string, sessionID string, send SendMessageFn, verbose bool).


```go
func newChatModel((agentRef string, sessionID string, send SendMessageFn, verbose bool)) (agentRef string, sessionID string, send SendMessageFn, verbose bool)
```


**Тип ответа:** agentRef


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** send


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SendMessageFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:73`



---


[function] name: setWorkingTime file: go/cli/internal/tui/chat.go:484 returns_error: нет description: —


### setWorkingTime (go/cli/internal/tui/chat.go:484)


setWorkingTime is a method that performs operations based on the provided parameters and returns (ts time.Time).


```go
func (m *chatModel) setWorkingTime((ts time.Time)) (ts time.Time)
```


**Тип ответа:** ts


```json
{
  "Agents": []
}
```


*Определено в:* `go/internal/mcp/mcp_handler.go`


**Тип ответа:** time.Time


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/chat.go:484`



---


[function] name: submit file: go/cli/internal/tui/chat.go:218 returns_error: нет description: —


### submit (go/cli/internal/tui/chat.go:218)


submit is a method that performs operations based on the provided parameters and returns (text string).


```go
func (m *chatModel) submit((text string)) (text string)
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


📍 *Расположение:* `go/cli/internal/tui/chat.go:218`



---


[function] name: tick file: go/cli/internal/tui/chat.go:477 returns_error: нет description: —


### tick (go/cli/internal/tui/chat.go:477)


tick is a method that performs operations based on the provided parameters and returns ().


```go
func (m *chatModel) tick(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/chat.go:477`



---


[function] name: updateStatus file: go/cli/internal/tui/chat.go:496 returns_error: нет description: —


### updateStatus (go/cli/internal/tui/chat.go:496)


updateStatus is a method that performs operations based on the provided parameters and returns ().


```go
func (m *chatModel) updateStatus(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/chat.go:496`



---


[function] name: waitNext file: go/cli/internal/tui/chat.go:246 returns_error: нет description: —


### waitNext (go/cli/internal/tui/chat.go:246)


waitNext is a method that performs operations based on the provided parameters and returns ().


```go
func (m *chatModel) waitNext(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/chat.go:246`




## go/cli/internal/tui/dialogs/agent_chooser.go


📄 Исходный файл: `go/cli/internal/tui/dialogs/agent_chooser.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [Description](#description-gocliinternaltuidialogsagent_choosergo16) `:16`

- 🔗 [FilterValue](#filtervalue-gocliinternaltuidialogsagent_choosergo17) `:17`

- 🔗 [Fullscreen](#fullscreen-gocliinternaltuidialogsagent_choosergo148) `:148`

- 🔗 [ID](#id-gocliinternaltuidialogsagent_choosergo147) `:147`

- 🔗 [Init](#init-gocliinternaltuidialogsagent_choosergo84) `:84`

- 🔗 [Namespace](#namespace-gocliinternaltuidialogsagent_choosergo15) `:15`

- 🔗 [NewAgentChooser](#newagentchooser-gocliinternaltuidialogsagent_choosergo28) `:28`

- 🔗 [Title](#title-gocliinternaltuidialogsagent_choosergo14) `:14`

- 🔗 [Update](#update-gocliinternaltuidialogsagent_choosergo86) `:86`

- 🔗 [View](#view-gocliinternaltuidialogsagent_choosergo143) `:143`

- 🔗 [buildColumns](#buildcolumns-gocliinternaltuidialogsagent_choosergo58) `:58`

- 🔗 [buildRows](#buildrows-gocliinternaltuidialogsagent_choosergo73) `:73`

- 🔗 [selectedIndex](#selectedindex-gocliinternaltuidialogsagent_choosergo115) `:115`


</details>


[function] name: Description file: go/cli/internal/tui/dialogs/agent_chooser.go:16 returns_error: нет description: —


### Description (go/cli/internal/tui/dialogs/agent_chooser.go:16)


Description is a method that performs operations based on the provided parameters and returns ().


```go
func (i AgentItem) Description(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:16`



---


[function] name: FilterValue file: go/cli/internal/tui/dialogs/agent_chooser.go:17 returns_error: нет description: —


### FilterValue (go/cli/internal/tui/dialogs/agent_chooser.go:17)


FilterValue is a method that performs operations based on the provided parameters and returns ().


```go
func (i AgentItem) FilterValue(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:17`



---


[function] name: Fullscreen file: go/cli/internal/tui/dialogs/agent_chooser.go:148 returns_error: нет description: —


### Fullscreen (go/cli/internal/tui/dialogs/agent_chooser.go:148)


Fullscreen is a method that performs operations based on the provided parameters and returns ().


```go
func (a *AgentChooser) Fullscreen(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:148`



---


[function] name: ID file: go/cli/internal/tui/dialogs/agent_chooser.go:147 returns_error: нет description: —


### ID (go/cli/internal/tui/dialogs/agent_chooser.go:147)


ID is a method that performs operations based on the provided parameters and returns ().


```go
func (a *AgentChooser) ID(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:147`



---


[function] name: Init file: go/cli/internal/tui/dialogs/agent_chooser.go:84 returns_error: нет description: —


### Init (go/cli/internal/tui/dialogs/agent_chooser.go:84)


Init is a method that performs operations based on the provided parameters and returns ().


```go
func (a *AgentChooser) Init(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:84`



---


[function] name: Namespace file: go/cli/internal/tui/dialogs/agent_chooser.go:15 returns_error: нет description: —


### Namespace (go/cli/internal/tui/dialogs/agent_chooser.go:15)


Namespace is a method that performs operations based on the provided parameters and returns ().


```go
func (i AgentItem) Namespace(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:15`



---


[function] name: NewAgentChooser file: go/cli/internal/tui/dialogs/agent_chooser.go:28 returns_error: нет description: —


### NewAgentChooser (go/cli/internal/tui/dialogs/agent_chooser.go:28)


NewAgentChooser is a function that performs operations based on the provided parameters and returns (items []*AgentItem, onOK func(item list.Item) tea.Cmd).


```go
func NewAgentChooser((items []*AgentItem, onOK func(item list.Item) tea.Cmd)) (items []*AgentItem, onOK func(item list.Item) tea.Cmd)
```


**Тип запроса:** AgentItem


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** items


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentItem


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** onOK


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** item


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** list.Item


```json
{
  "s": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


**Тип ответа:** tea.Cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:28`



---


[function] name: Title file: go/cli/internal/tui/dialogs/agent_chooser.go:14 returns_error: нет description: —


### Title (go/cli/internal/tui/dialogs/agent_chooser.go:14)


Title is a method that performs operations based on the provided parameters and returns ().


```go
func (i AgentItem) Title(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:14`



---


[function] name: Update file: go/cli/internal/tui/dialogs/agent_chooser.go:86 returns_error: нет description: —


### Update (go/cli/internal/tui/dialogs/agent_chooser.go:86)


Update is a method that updates data based on the provided parameters and returns (tea.Model, tea.Cmd).


```go
func (a *AgentChooser) Update((tea.Model, tea.Cmd)) (tea.Model, tea.Cmd)
```


**Тип ответа:** tea.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** tea.Cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:86`



---


[function] name: View file: go/cli/internal/tui/dialogs/agent_chooser.go:143 returns_error: нет description: —


### View (go/cli/internal/tui/dialogs/agent_chooser.go:143)


View is a method that performs operations based on the provided parameters and returns ().


```go
func (a *AgentChooser) View(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:143`



---


[function] name: buildColumns file: go/cli/internal/tui/dialogs/agent_chooser.go:58 returns_error: нет description: —


### buildColumns (go/cli/internal/tui/dialogs/agent_chooser.go:58)


buildColumns is a method that performs operations based on the provided parameters and returns (innerWidth int).


```go
func (a *AgentChooser) buildColumns((innerWidth int)) (innerWidth int)
```


**Тип ответа:** innerWidth


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:58`



---


[function] name: buildRows file: go/cli/internal/tui/dialogs/agent_chooser.go:73 returns_error: нет description: —


### buildRows (go/cli/internal/tui/dialogs/agent_chooser.go:73)


buildRows is a method that performs operations based on the provided parameters and returns (items []*AgentItem).


```go
func (a *AgentChooser) buildRows((items []*AgentItem)) (items []*AgentItem)
```


**Тип запроса:** AgentItem


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** items


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AgentItem


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:73`



---


[function] name: selectedIndex file: go/cli/internal/tui/dialogs/agent_chooser.go:115 returns_error: нет description: —


### selectedIndex (go/cli/internal/tui/dialogs/agent_chooser.go:115)


selectedIndex is a method that performs operations based on the provided parameters and returns ().


```go
func (a *AgentChooser) selectedIndex(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/agent_chooser.go:115`




## go/cli/internal/tui/dialogs/manager.go


📄 Исходный файл: `go/cli/internal/tui/dialogs/manager.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Active](#active-gocliinternaltuidialogsmanagergo31) `:31`

- 🔗 [Handle](#handle-gocliinternaltuidialogsmanagergo39) `:39`

- 🔗 [HasDialogs](#hasdialogs-gocliinternaltuidialogsmanagergo29) `:29`

- 🔗 [NewManager](#newmanager-gocliinternaltuidialogsmanagergo27) `:27`

- 🔗 [ViewOverlay](#viewoverlay-gocliinternaltuidialogsmanagergo87) `:87`


</details>


[function] name: Active file: go/cli/internal/tui/dialogs/manager.go:31 returns_error: нет description: —


### Active (go/cli/internal/tui/dialogs/manager.go:31)


Active is a method that performs operations based on the provided parameters and returns ().


```go
func (m *Manager) Active(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/manager.go:31`



---


[function] name: Handle file: go/cli/internal/tui/dialogs/manager.go:39 returns_error: нет description: Handle processes messages and routes them to the dialog stack. It returns a Cmd to be run by Bubble Tea.


### Handle (go/cli/internal/tui/dialogs/manager.go:39)


Handle processes messages and routes them to the dialog stack. It returns a Cmd to be run by Bubble Tea.


```go
func (m *Manager) Handle((msg tea.Msg)) (msg tea.Msg)
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tea.Msg


```json
{
  "Event": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


📍 *Расположение:* `go/cli/internal/tui/dialogs/manager.go:39`



---


[function] name: HasDialogs file: go/cli/internal/tui/dialogs/manager.go:29 returns_error: нет description: —


### HasDialogs (go/cli/internal/tui/dialogs/manager.go:29)


HasDialogs is a method that performs operations based on the provided parameters and returns ().


```go
func (m *Manager) HasDialogs(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/manager.go:29`



---


[function] name: NewManager file: go/cli/internal/tui/dialogs/manager.go:27 returns_error: нет description: —


### NewManager (go/cli/internal/tui/dialogs/manager.go:27)


NewManager is a function that performs operations based on the provided parameters and returns ().


```go
func NewManager(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/manager.go:27`



---


[function] name: ViewOverlay file: go/cli/internal/tui/dialogs/manager.go:87 returns_error: нет description: ViewOverlay returns the view of the active dialog if present, otherwise empty string.


### ViewOverlay (go/cli/internal/tui/dialogs/manager.go:87)


ViewOverlay returns the view of the active dialog if present, otherwise empty string.


```go
func (m *Manager) ViewOverlay((string, bool)) (string, bool)
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/manager.go:87`




## go/cli/internal/tui/dialogs/mcp_server_wizard.go


📄 Исходный файл: `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


<details open>
<summary><b>Функции в этом файле (53)</b></summary>


- 🔗 [Description](#description-gocliinternaltuidialogsmcp_server_wizardgo969) `:969`

- 🔗 [FilterValue](#filtervalue-gocliinternaltuidialogsmcp_server_wizardgo970) `:970`

- 🔗 [Fullscreen](#fullscreen-gocliinternaltuidialogsmcp_server_wizardgo242) `:242`

- 🔗 [Height](#height-gocliinternaltuidialogsmcp_server_wizardgo974) `:974`

- 🔗 [ID](#id-gocliinternaltuidialogsmcp_server_wizardgo241) `:241`

- 🔗 [Init](#init-gocliinternaltuidialogsmcp_server_wizardgo246) `:246`

- 🔗 [NewMcpServerWizard](#newmcpserverwizard-gocliinternaltuidialogsmcp_server_wizardgo165) `:165`

- 🔗 [Ok](#ok-gocliinternaltuidialogsmcp_server_wizardgo243) `:243`

- 🔗 [Render](#render-gocliinternaltuidialogsmcp_server_wizardgo977) `:977`

- 🔗 [Result](#result-gocliinternaltuidialogsmcp_server_wizardgo244) `:244`

- 🔗 [Spacing](#spacing-gocliinternaltuidialogsmcp_server_wizardgo975) `:975`

- 🔗 [Title](#title-gocliinternaltuidialogsmcp_server_wizardgo968) `:968`

- 🔗 [Update](#update-gocliinternaltuidialogsmcp_server_wizardgo251) `:251`

- 🔗 [Update](#update-gocliinternaltuidialogsmcp_server_wizardgo976) `:976`

- 🔗 [View](#view-gocliinternaltuidialogsmcp_server_wizardgo352) `:352`

- 🔗 [applyCommandMode](#applycommandmode-gocliinternaltuidialogsmcp_server_wizardgo576) `:576`

- 🔗 [buildFinalResult](#buildfinalresult-gocliinternaltuidialogsmcp_server_wizardgo642) `:642`

- 🔗 [chooseCommandType](#choosecommandtype-gocliinternaltuidialogsmcp_server_wizardgo546) `:546`

- 🔗 [chooseRemoteType](#chooseremotetype-gocliinternaltuidialogsmcp_server_wizardgo537) `:537`

- 🔗 [close](#close-gocliinternaltuidialogsmcp_server_wizardgo893) `:893`

- 🔗 [detailOrderKeys](#detailorderkeys-gocliinternaltuidialogsmcp_server_wizardgo774) `:774`

- 🔗 [enterArgsEnv](#enterargsenv-gocliinternaltuidialogsmcp_server_wizardgo517) `:517`

- 🔗 [enterCommandDetails](#entercommanddetails-gocliinternaltuidialogsmcp_server_wizardgo503) `:503`

- 🔗 [enterCommandMethod](#entercommandmethod-gocliinternaltuidialogsmcp_server_wizardgo485) `:485`

- 🔗 [enterCommandMode](#entercommandmode-gocliinternaltuidialogsmcp_server_wizardgo494) `:494`

- 🔗 [enterMethodDetails](#entermethoddetails-gocliinternaltuidialogsmcp_server_wizardgo552) `:552`

- 🔗 [enterName](#entername-gocliinternaltuidialogsmcp_server_wizardgo525) `:525`

- 🔗 [enterPickType](#enterpicktype-gocliinternaltuidialogsmcp_server_wizardgo420) `:420`

- 🔗 [enterRemoteHeaders](#enterremoteheaders-gocliinternaltuidialogsmcp_server_wizardgo449) `:449`

- 🔗 [enterRemoteURL](#enterremoteurl-gocliinternaltuidialogsmcp_server_wizardgo433) `:433`

- 🔗 [errorView](#errorview-gocliinternaltuidialogsmcp_server_wizardgo886) `:886`

- 🔗 [focusDetailKey](#focusdetailkey-gocliinternaltuidialogsmcp_server_wizardgo808) `:808`

- 🔗 [inputModel](#inputmodel-gocliinternaltuidialogsmcp_server_wizardgo787) `:787`

- 🔗 [interpretModeFromSelection](#interpretmodefromselection-gocliinternaltuidialogsmcp_server_wizardgo600) `:600`

- 🔗 [isFocusedKey](#isfocusedkey-gocliinternaltuidialogsmcp_server_wizardgo800) `:800`

- 🔗 [labeled](#labeled-gocliinternaltuidialogsmcp_server_wizardgo818) `:818`

- 🔗 [lineCount](#linecount-gocliinternaltuidialogsmcp_server_wizardgo993) `:993`

- 🔗 [maxInt](#maxint-gocliinternaltuidialogsmcp_server_wizardgo1014) `:1014`

- 🔗 [onEnter](#onenter-gocliinternaltuidialogsmcp_server_wizardgo396) `:396`

- 🔗 [onTab](#ontab-gocliinternaltuidialogsmcp_server_wizardgo686) `:686`

- 🔗 [prevStep](#prevstep-gocliinternaltuidialogsmcp_server_wizardgo898) `:898`

- 🔗 [proceedToArgsEnv](#proceedtoargsenv-gocliinternaltuidialogsmcp_server_wizardgo634) `:634`

- 🔗 [renderCommandDetails](#rendercommanddetails-gocliinternaltuidialogsmcp_server_wizardgo837) `:837`

- 🔗 [renderHeader](#renderheader-gocliinternaltuidialogsmcp_server_wizardgo866) `:866`

- 🔗 [renderHeadersStep](#renderheadersstep-gocliinternaltuidialogsmcp_server_wizardgo928) `:928`

- 🔗 [renderRows](#renderrows-gocliinternaltuidialogsmcp_server_wizardgo824) `:824`

- 🔗 [splitCSV](#splitcsv-gocliinternaltuidialogsmcp_server_wizardgo1001) `:1001`

- 🔗 [tabArgsEnv](#tabargsenv-gocliinternaltuidialogsmcp_server_wizardgo750) `:750`

- 🔗 [tabCommandDetails](#tabcommanddetails-gocliinternaltuidialogsmcp_server_wizardgo728) `:728`

- 🔗 [tabName](#tabname-gocliinternaltuidialogsmcp_server_wizardgo772) `:772`

- 🔗 [tabRemoteHeaders](#tabremoteheaders-gocliinternaltuidialogsmcp_server_wizardgo706) `:706`

- 🔗 [tabRemoteURL](#tabremoteurl-gocliinternaltuidialogsmcp_server_wizardgo703) `:703`

- 🔗 [validateCommandDetails](#validatecommanddetails-gocliinternaltuidialogsmcp_server_wizardgo611) `:611`


</details>


[function] name: Description file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:969 returns_error: нет description: —


### Description (go/cli/internal/tui/dialogs/mcp_server_wizard.go:969)


Description is a method that performs operations based on the provided parameters and returns ().


```go
func (i choiceItem) Description(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:969`



---


[function] name: FilterValue file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:970 returns_error: нет description: —


### FilterValue (go/cli/internal/tui/dialogs/mcp_server_wizard.go:970)


FilterValue is a method that performs operations based on the provided parameters and returns ().


```go
func (i choiceItem) FilterValue(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:970`



---


[function] name: Fullscreen file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:242 returns_error: нет description: —


### Fullscreen (go/cli/internal/tui/dialogs/mcp_server_wizard.go:242)


Fullscreen is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) Fullscreen(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:242`



---


[function] name: Height file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:974 returns_error: нет description: —


### Height (go/cli/internal/tui/dialogs/mcp_server_wizard.go:974)


Height is a method that performs operations based on the provided parameters and returns ().


```go
func (d choiceDelegate) Height(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:974`



---


[function] name: ID file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:241 returns_error: нет description: —


### ID (go/cli/internal/tui/dialogs/mcp_server_wizard.go:241)


ID is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) ID(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:241`



---


[function] name: Init file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:246 returns_error: нет description: —


### Init (go/cli/internal/tui/dialogs/mcp_server_wizard.go:246)


Init is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) Init(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:246`



---


[function] name: NewMcpServerWizard file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:165 returns_error: нет description: —


### NewMcpServerWizard (go/cli/internal/tui/dialogs/mcp_server_wizard.go:165)


NewMcpServerWizard is a function that performs operations based on the provided parameters and returns ().


```go
func NewMcpServerWizard(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:165`



---


[function] name: Ok file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:243 returns_error: нет description: —


### Ok (go/cli/internal/tui/dialogs/mcp_server_wizard.go:243)


Ok is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) Ok(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:243`



---


[function] name: Render file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:977 returns_error: нет description: —


### Render (go/cli/internal/tui/dialogs/mcp_server_wizard.go:977)


Render is a method that performs operations based on the provided parameters and returns (w io.Writer, m list.Model, index int, it list.Item).


```go
func (d choiceDelegate) Render((w io.Writer, m list.Model, index int, it list.Item)) (w io.Writer, m list.Model, index int, it list.Item)
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


**Тип ответа:** io.Writer


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** m


```json
{
  "db": null
}
```


*Определено в:* `go/internal/database/client.go`


**Тип ответа:** list.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** index


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** it


```json
{
  "DatabasePath": "string",
  "VectorEnabled": false
}
```


*Определено в:* `go/internal/database/manager.go`


**Тип ответа:** list.Item


```json
{
  "s": null
}
```


*Определено в:* `go/cli/internal/tui/workspace.go`


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:977`



---


[function] name: Result file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:244 returns_error: нет description: —


### Result (go/cli/internal/tui/dialogs/mcp_server_wizard.go:244)


Result is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) Result(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:244`



---


[function] name: Spacing file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:975 returns_error: нет description: —


### Spacing (go/cli/internal/tui/dialogs/mcp_server_wizard.go:975)


Spacing is a method that performs operations based on the provided parameters and returns ().


```go
func (d choiceDelegate) Spacing(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:975`



---


[function] name: Title file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:968 returns_error: нет description: —


### Title (go/cli/internal/tui/dialogs/mcp_server_wizard.go:968)


Title is a method that performs operations based on the provided parameters and returns ().


```go
func (i choiceItem) Title(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:968`



---


[function] name: Update file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:251 returns_error: нет description: Update handles Bubble Tea messages and routes to the current step's components.


### Update (go/cli/internal/tui/dialogs/mcp_server_wizard.go:251)


Update handles Bubble Tea messages and routes to the current step's components.


```go
func (w *McpServerWizard) Update((tea.Model, tea.Cmd)) (tea.Model, tea.Cmd)
```


**Тип ответа:** tea.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** tea.Cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:251`



---


[function] name: Update file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:976 returns_error: нет description: —


### Update (go/cli/internal/tui/dialogs/mcp_server_wizard.go:976)


Update is a method that updates data based on the provided parameters and returns (_ tea.Msg, _ *list.Model).


```go
func (d choiceDelegate) Update((_ tea.Msg, _ *list.Model)) (_ tea.Msg, _ *list.Model)
```


**Тип запроса:** list.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tea.Msg


```json
{
  "Event": {}
}
```


*Определено в:* `go/cli/internal/tui/chat.go`


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** list.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:976`



---


[function] name: View file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:352 returns_error: нет description: View assembles the frame and delegates step-specific content rendering.


### View (go/cli/internal/tui/dialogs/mcp_server_wizard.go:352)


View assembles the frame and delegates step-specific content rendering.


```go
func (w *McpServerWizard) View(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:352`



---


[function] name: applyCommandMode file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:576 returns_error: нет description: applyCommandMode configures fields based on the chosen command mode title
and moves to the details step, focusing the ap


### applyCommandMode (go/cli/internal/tui/dialogs/mcp_server_wizard.go:576)


applyCommandMode configures fields based on the chosen command mode title
and moves to the details step, focusing the appropriate input.


```go
func (w *McpServerWizard) applyCommandMode((title string)) (title string)
```


**Тип ответа:** title


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:576`



---


[function] name: buildFinalResult file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:642 returns_error: нет description: buildFinalResult constructs the final result object from the wizard state.


### buildFinalResult (go/cli/internal/tui/dialogs/mcp_server_wizard.go:642)


buildFinalResult constructs the final result object from the wizard state.


```go
func (w *McpServerWizard) buildFinalResult((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:642`



---


[function] name: chooseCommandType file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:546 returns_error: нет description: chooseCommandType transitions to the command method selection step.


### chooseCommandType (go/cli/internal/tui/dialogs/mcp_server_wizard.go:546)


chooseCommandType transitions to the command method selection step.


```go
func (w *McpServerWizard) chooseCommandType(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:546`



---


[function] name: chooseRemoteType file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:537 returns_error: нет description: chooseRemoteType transitions to the remote URL entry step and prepares input.


### chooseRemoteType (go/cli/internal/tui/dialogs/mcp_server_wizard.go:537)


chooseRemoteType transitions to the remote URL entry step and prepares input.


```go
func (w *McpServerWizard) chooseRemoteType(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:537`



---


[function] name: close file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:893 returns_error: нет description: —


### close (go/cli/internal/tui/dialogs/mcp_server_wizard.go:893)


close is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) close(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:893`



---


[function] name: detailOrderKeys file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:774 returns_error: нет description: —


### detailOrderKeys (go/cli/internal/tui/dialogs/mcp_server_wizard.go:774)


detailOrderKeys is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) detailOrderKeys(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:774`



---


[function] name: enterArgsEnv file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:517 returns_error: нет description: enterArgsEnv advances to naming with a suggested name.


### enterArgsEnv (go/cli/internal/tui/dialogs/mcp_server_wizard.go:517)


enterArgsEnv advances to naming with a suggested name.


```go
func (w *McpServerWizard) enterArgsEnv(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:517`



---


[function] name: enterCommandDetails file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:503 returns_error: нет description: enterCommandDetails validates inputs for the chosen method and proceeds.


### enterCommandDetails (go/cli/internal/tui/dialogs/mcp_server_wizard.go:503)


enterCommandDetails validates inputs for the chosen method and proceeds.


```go
func (w *McpServerWizard) enterCommandDetails(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:503`



---


[function] name: enterCommandMethod file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:485 returns_error: нет description: enterCommandMethod records the chosen run method and routes to the right detail step.


### enterCommandMethod (go/cli/internal/tui/dialogs/mcp_server_wizard.go:485)


enterCommandMethod records the chosen run method and routes to the right detail step.


```go
func (w *McpServerWizard) enterCommandMethod(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:485`



---


[function] name: enterCommandMode file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:494 returns_error: нет description: enterCommandMode applies the chosen sub-mode (Custom/npx/uvx) and advances.


### enterCommandMode (go/cli/internal/tui/dialogs/mcp_server_wizard.go:494)


enterCommandMode applies the chosen sub-mode (Custom/npx/uvx) and advances.


```go
func (w *McpServerWizard) enterCommandMode(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:494`



---


[function] name: enterMethodDetails file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:552 returns_error: нет description: enterMethodDetails stores the chosen method and focuses the appropriate input.


### enterMethodDetails (go/cli/internal/tui/dialogs/mcp_server_wizard.go:552)


enterMethodDetails stores the chosen method and focuses the appropriate input.


```go
func (w *McpServerWizard) enterMethodDetails((displayName string)) (displayName string)
```


**Тип ответа:** displayName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:552`



---


[function] name: enterName file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:525 returns_error: нет description: enterName finalizes the result and closes the wizard.


### enterName (go/cli/internal/tui/dialogs/mcp_server_wizard.go:525)


enterName finalizes the result and closes the wizard.


```go
func (w *McpServerWizard) enterName(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:525`



---


[function] name: enterPickType file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:420 returns_error: нет description: enterPickType processes selection of the top-level type (Remote or Command).


### enterPickType (go/cli/internal/tui/dialogs/mcp_server_wizard.go:420)


enterPickType processes selection of the top-level type (Remote or Command).


```go
func (w *McpServerWizard) enterPickType(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:420`



---


[function] name: enterRemoteHeaders file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:449 returns_error: нет description: enterRemoteHeaders handles adding headers or skipping to name step.


### enterRemoteHeaders (go/cli/internal/tui/dialogs/mcp_server_wizard.go:449)


enterRemoteHeaders handles adding headers or skipping to name step.


```go
func (w *McpServerWizard) enterRemoteHeaders(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:449`



---


[function] name: enterRemoteURL file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:433 returns_error: нет description: enterRemoteURL validates the remote URL and advances to headers step.


### enterRemoteURL (go/cli/internal/tui/dialogs/mcp_server_wizard.go:433)


enterRemoteURL validates the remote URL and advances to headers step.


```go
func (w *McpServerWizard) enterRemoteURL(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:433`



---


[function] name: errorView file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:886 returns_error: нет description: —


### errorView (go/cli/internal/tui/dialogs/mcp_server_wizard.go:886)


errorView is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) errorView(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:886`



---


[function] name: focusDetailKey file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:808 returns_error: нет description: —


### focusDetailKey (go/cli/internal/tui/dialogs/mcp_server_wizard.go:808)


focusDetailKey is a method that performs operations based on the provided parameters and returns (k inputKey).


```go
func (w *McpServerWizard) focusDetailKey((k inputKey)) (k inputKey)
```


**Тип ответа:** k


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** inputKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:808`



---


[function] name: inputModel file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:787 returns_error: нет description: —


### inputModel (go/cli/internal/tui/dialogs/mcp_server_wizard.go:787)


inputModel is a method that performs operations based on the provided parameters and returns (k inputKey).


```go
func (w *McpServerWizard) inputModel((k inputKey)) (k inputKey)
```


**Тип ответа:** k


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** inputKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:787`



---


[function] name: interpretModeFromSelection file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:600 returns_error: нет description: interpretModeFromSelection reads the current selection in the mode list and applies it.
Returns true if a selection was 


### interpretModeFromSelection (go/cli/internal/tui/dialogs/mcp_server_wizard.go:600)


interpretModeFromSelection reads the current selection in the mode list and applies it.
Returns true if a selection was applied.


```go
func (w *McpServerWizard) interpretModeFromSelection(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:600`



---


[function] name: isFocusedKey file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:800 returns_error: нет description: —


### isFocusedKey (go/cli/internal/tui/dialogs/mcp_server_wizard.go:800)


isFocusedKey is a method that performs operations based on the provided parameters and returns (k inputKey).


```go
func (w *McpServerWizard) isFocusedKey((k inputKey)) (k inputKey)
```


**Тип ответа:** k


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** inputKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:800`



---


[function] name: labeled file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:818 returns_error: нет description: —


### labeled (go/cli/internal/tui/dialogs/mcp_server_wizard.go:818)


labeled is a method that performs operations based on the provided parameters and returns (label, view string).


```go
func (w *McpServerWizard) labeled((label, view string)) (label, view string)
```


**Тип ответа:** label


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** view


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:818`



---


[function] name: lineCount file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:993 returns_error: нет description: lineCount counts lines in a string (>=1 if non-empty)


### lineCount (go/cli/internal/tui/dialogs/mcp_server_wizard.go:993)


lineCount counts lines in a string (>=1 if non-empty)


```go
func lineCount((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:993`



---


[function] name: maxInt file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:1014 returns_error: нет description: maxInt returns the maximum of two ints


### maxInt (go/cli/internal/tui/dialogs/mcp_server_wizard.go:1014)


maxInt returns the maximum of two ints


```go
func maxInt((a, b int)) (a, b int)
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


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:1014`



---


[function] name: onEnter file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:396 returns_error: нет description: onEnter handles the Enter key by delegating to a step-specific handler.


### onEnter (go/cli/internal/tui/dialogs/mcp_server_wizard.go:396)


onEnter handles the Enter key by delegating to a step-specific handler.


```go
func (w *McpServerWizard) onEnter(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:396`



---


[function] name: onTab file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:686 returns_error: нет description: onTab cycles focus within the current step.


### onTab (go/cli/internal/tui/dialogs/mcp_server_wizard.go:686)


onTab cycles focus within the current step.


```go
func (w *McpServerWizard) onTab((reverse bool)) (reverse bool)
```


**Тип ответа:** reverse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:686`



---


[function] name: prevStep file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:898 returns_error: нет description: prevStep moves the wizard back by one logical step based on current state.


### prevStep (go/cli/internal/tui/dialogs/mcp_server_wizard.go:898)


prevStep moves the wizard back by one logical step based on current state.


```go
func (w *McpServerWizard) prevStep(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:898`



---


[function] name: proceedToArgsEnv file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:634 returns_error: нет description: proceedToArgsEnv transitions to the args/env step and prepares inputs.


### proceedToArgsEnv (go/cli/internal/tui/dialogs/mcp_server_wizard.go:634)


proceedToArgsEnv transitions to the args/env step and prepares inputs.


```go
func (w *McpServerWizard) proceedToArgsEnv(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:634`



---


[function] name: renderCommandDetails file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:837 returns_error: нет description: —


### renderCommandDetails (go/cli/internal/tui/dialogs/mcp_server_wizard.go:837)


renderCommandDetails is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) renderCommandDetails(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:837`



---


[function] name: renderHeader file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:866 returns_error: нет description: —


### renderHeader (go/cli/internal/tui/dialogs/mcp_server_wizard.go:866)


renderHeader is a method that performs operations based on the provided parameters and returns ().


```go
func (w *McpServerWizard) renderHeader(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:866`



---


[function] name: renderHeadersStep file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:928 returns_error: нет description: renderHeadersStep displays the headers input interface with current headers.


### renderHeadersStep (go/cli/internal/tui/dialogs/mcp_server_wizard.go:928)


renderHeadersStep displays the headers input interface with current headers.


```go
func (w *McpServerWizard) renderHeadersStep(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:928`



---


[function] name: renderRows file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:824 returns_error: нет description: —


### renderRows (go/cli/internal/tui/dialogs/mcp_server_wizard.go:824)


renderRows is a method that performs operations based on the provided parameters and returns (rows []detailRow).


```go
func (w *McpServerWizard) renderRows((rows []detailRow)) (rows []detailRow)
```


**Тип ответа:** rows


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** detailRow


```json
{
  "label": "string"
}
```


*Определено в:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go`


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:824`



---


[function] name: splitCSV file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:1001 returns_error: нет description: splitCSV splits comma-separated values, trimming whitespace and skipping empties


### splitCSV (go/cli/internal/tui/dialogs/mcp_server_wizard.go:1001)


splitCSV splits comma-separated values, trimming whitespace and skipping empties


```go
func splitCSV((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:1001`



---


[function] name: tabArgsEnv file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:750 returns_error: нет description: tabArgsEnv toggles focus between args and env.


### tabArgsEnv (go/cli/internal/tui/dialogs/mcp_server_wizard.go:750)


tabArgsEnv toggles focus between args and env.


```go
func (w *McpServerWizard) tabArgsEnv((reverse bool)) (reverse bool)
```


**Тип ответа:** reverse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:750`



---


[function] name: tabCommandDetails file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:728 returns_error: нет description: tabCommandDetails cycles across visible detail inputs.


### tabCommandDetails (go/cli/internal/tui/dialogs/mcp_server_wizard.go:728)


tabCommandDetails cycles across visible detail inputs.


```go
func (w *McpServerWizard) tabCommandDetails((reverse bool)) (reverse bool)
```


**Тип ответа:** reverse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:728`



---


[function] name: tabName file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:772 returns_error: нет description: tabName has a single input; nothing to cycle.


### tabName (go/cli/internal/tui/dialogs/mcp_server_wizard.go:772)


tabName has a single input; nothing to cycle.


```go
func (w *McpServerWizard) tabName((_ bool)) (_ bool)
```


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:772`



---


[function] name: tabRemoteHeaders file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:706 returns_error: нет description: tabRemoteHeaders toggles focus between header key and value inputs.


### tabRemoteHeaders (go/cli/internal/tui/dialogs/mcp_server_wizard.go:706)


tabRemoteHeaders toggles focus between header key and value inputs.


```go
func (w *McpServerWizard) tabRemoteHeaders((reverse bool)) (reverse bool)
```


**Тип ответа:** reverse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:706`



---


[function] name: tabRemoteURL file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:703 returns_error: нет description: tabRemoteURL has a single input; nothing to cycle.


### tabRemoteURL (go/cli/internal/tui/dialogs/mcp_server_wizard.go:703)


tabRemoteURL has a single input; nothing to cycle.


```go
func (w *McpServerWizard) tabRemoteURL((_ bool)) (_ bool)
```


**Тип ответа:** _


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:703`



---


[function] name: validateCommandDetails file: go/cli/internal/tui/dialogs/mcp_server_wizard.go:611 returns_error: нет description: validateCommandDetails validates inputs for the selected method. For Command
method without a chosen mode, it interprets


### validateCommandDetails (go/cli/internal/tui/dialogs/mcp_server_wizard.go:611)


validateCommandDetails validates inputs for the selected method. For Command
method without a chosen mode, it interprets the selected mode and stays on the page.
Returns true if validation passes and we can proceed to the next step.


```go
func (w *McpServerWizard) validateCommandDetails(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/dialogs/mcp_server_wizard.go:611`




## go/cli/internal/tui/keys/keys.go


📄 Исходный файл: `go/cli/internal/tui/keys/keys.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DefaultKeyMap](#defaultkeymap-gocliinternaltuikeyskeysgo11) `:11`

- 🔗 [FullHelp](#fullhelp-gocliinternaltuikeyskeysgo28) `:28`

- 🔗 [ShortHelp](#shorthelp-gocliinternaltuikeyskeysgo34) `:34`


</details>


[function] name: DefaultKeyMap file: go/cli/internal/tui/keys/keys.go:11 returns_error: нет description: —


### DefaultKeyMap (go/cli/internal/tui/keys/keys.go:11)


DefaultKeyMap is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultKeyMap(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/keys/keys.go:11`



---


[function] name: FullHelp file: go/cli/internal/tui/keys/keys.go:28 returns_error: нет description: —


### FullHelp (go/cli/internal/tui/keys/keys.go:28)


FullHelp is a method that performs operations based on the provided parameters and returns ().


```go
func (k KeyMap) FullHelp(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/keys/keys.go:28`



---


[function] name: ShortHelp file: go/cli/internal/tui/keys/keys.go:34 returns_error: нет description: —


### ShortHelp (go/cli/internal/tui/keys/keys.go:34)


ShortHelp is a method that performs operations based on the provided parameters and returns ().


```go
func (k KeyMap) ShortHelp(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/keys/keys.go:34`




## go/cli/internal/tui/theme/colors.go


📄 Исходный файл: `go/cli/internal/tui/theme/colors.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [AgentStyle](#agentstyle-gocliinternaltuithemecolorsgo19) `:19`

- 🔗 [DimStyle](#dimstyle-gocliinternaltuithemecolorsgo41) `:41`

- 🔗 [ErrorStyle](#errorstyle-gocliinternaltuithemecolorsgo21) `:21`

- 🔗 [HeadingStyle](#headingstyle-gocliinternaltuithemecolorsgo14) `:14`

- 🔗 [SeparatorStyle](#separatorstyle-gocliinternaltuithemecolorsgo25) `:25`

- 🔗 [StatusStyle](#statusstyle-gocliinternaltuithemecolorsgo29) `:29`

- 🔗 [ToolCallStyle](#toolcallstyle-gocliinternaltuithemecolorsgo33) `:33`

- 🔗 [ToolResultStyle](#toolresultstyle-gocliinternaltuithemecolorsgo37) `:37`

- 🔗 [UserStyle](#userstyle-gocliinternaltuithemecolorsgo18) `:18`


</details>


[function] name: AgentStyle file: go/cli/internal/tui/theme/colors.go:19 returns_error: нет description: —


### AgentStyle (go/cli/internal/tui/theme/colors.go:19)


AgentStyle is a function that performs operations based on the provided parameters and returns ().


```go
func AgentStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:19`



---


[function] name: DimStyle file: go/cli/internal/tui/theme/colors.go:41 returns_error: нет description: —


### DimStyle (go/cli/internal/tui/theme/colors.go:41)


DimStyle is a function that performs operations based on the provided parameters and returns ().


```go
func DimStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:41`



---


[function] name: ErrorStyle file: go/cli/internal/tui/theme/colors.go:21 returns_error: нет description: —


### ErrorStyle (go/cli/internal/tui/theme/colors.go:21)


ErrorStyle is a function that performs operations based on the provided parameters and returns ().


```go
func ErrorStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:21`



---


[function] name: HeadingStyle file: go/cli/internal/tui/theme/colors.go:14 returns_error: нет description: —


### HeadingStyle (go/cli/internal/tui/theme/colors.go:14)


HeadingStyle is a function that performs operations based on the provided parameters and returns ().


```go
func HeadingStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:14`



---


[function] name: SeparatorStyle file: go/cli/internal/tui/theme/colors.go:25 returns_error: нет description: —


### SeparatorStyle (go/cli/internal/tui/theme/colors.go:25)


SeparatorStyle is a function that performs operations based on the provided parameters and returns ().


```go
func SeparatorStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:25`



---


[function] name: StatusStyle file: go/cli/internal/tui/theme/colors.go:29 returns_error: нет description: —


### StatusStyle (go/cli/internal/tui/theme/colors.go:29)


StatusStyle is a function that performs operations based on the provided parameters and returns ().


```go
func StatusStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:29`



---


[function] name: ToolCallStyle file: go/cli/internal/tui/theme/colors.go:33 returns_error: нет description: —


### ToolCallStyle (go/cli/internal/tui/theme/colors.go:33)


ToolCallStyle is a function that performs operations based on the provided parameters and returns ().


```go
func ToolCallStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:33`



---


[function] name: ToolResultStyle file: go/cli/internal/tui/theme/colors.go:37 returns_error: нет description: —


### ToolResultStyle (go/cli/internal/tui/theme/colors.go:37)


ToolResultStyle is a function that performs operations based on the provided parameters and returns ().


```go
func ToolResultStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:37`



---


[function] name: UserStyle file: go/cli/internal/tui/theme/colors.go:18 returns_error: нет description: —


### UserStyle (go/cli/internal/tui/theme/colors.go:18)


UserStyle is a function that performs operations based on the provided parameters and returns ().


```go
func UserStyle(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/theme/colors.go:18`




## go/cli/internal/tui/workspace.go


📄 Исходный файл: `go/cli/internal/tui/workspace.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [Description](#description-gocliinternaltuiworkspacego74) `:74`

- 🔗 [FilterValue](#filtervalue-gocliinternaltuiworkspacego75) `:75`

- 🔗 [Init](#init-gocliinternaltuiworkspacego148) `:148`

- 🔗 [RunWorkspace](#runworkspace-gocliinternaltuiworkspacego32) `:32`

- 🔗 [Title](#title-gocliinternaltuiworkspacego68) `:68`

- 🔗 [Update](#update-gocliinternaltuiworkspacego190) `:190`

- 🔗 [View](#view-gocliinternaltuiworkspacego546) `:546`

- 🔗 [createSession](#createsession-gocliinternaltuiworkspacego177) `:177`

- 🔗 [fetchSessionHistoryCmd](#fetchsessionhistorycmd-gocliinternaltuiworkspacego490) `:490`

- 🔗 [lineCount](#linecount-gocliinternaltuiworkspacego706) `:706`

- 🔗 [loadAgents](#loadagents-gocliinternaltuiworkspacego152) `:152`

- 🔗 [loadSessions](#loadsessions-gocliinternaltuiworkspacego159) `:159`

- 🔗 [newWorkspaceModel](#newworkspacemodel-gocliinternaltuiworkspacego114) `:114`

- 🔗 [renderDetails](#renderdetails-gocliinternaltuiworkspacego509) `:509`

- 🔗 [renderTitle](#rendertitle-gocliinternaltuiworkspacego699) `:699`

- 🔗 [resize](#resize-gocliinternaltuiworkspacego434) `:434`

- 🔗 [sortSessions](#sortsessions-gocliinternaltuiworkspacego720) `:720`

- 🔗 [startChat](#startchat-gocliinternaltuiworkspacego459) `:459`


</details>


[function] name: Description file: go/cli/internal/tui/workspace.go:74 returns_error: нет description: —


### Description (go/cli/internal/tui/workspace.go:74)


Description is a method that performs operations based on the provided parameters and returns ().


```go
func (i sessionListItem) Description(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:74`



---


[function] name: FilterValue file: go/cli/internal/tui/workspace.go:75 returns_error: нет description: —


### FilterValue (go/cli/internal/tui/workspace.go:75)


FilterValue is a method that performs operations based on the provided parameters and returns ().


```go
func (i sessionListItem) FilterValue(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:75`



---


[function] name: Init file: go/cli/internal/tui/workspace.go:148 returns_error: нет description: —


### Init (go/cli/internal/tui/workspace.go:148)


Init is a method that performs operations based on the provided parameters and returns ().


```go
func (m *workspaceModel) Init(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:148`



---


[function] name: RunWorkspace file: go/cli/internal/tui/workspace.go:32 returns_error: нет description: RunWorkspace launches a split-pane TUI: sessions (left), chat (center), details (toggleable right).


### RunWorkspace (go/cli/internal/tui/workspace.go:32)


RunWorkspace launches a split-pane TUI: sessions (left), chat (center), details (toggleable right).


```go
func RunWorkspace((cfg *config.Config, clientSet *client.ClientSet, verbose bool)) (cfg *config.Config, clientSet *client.ClientSet, verbose bool)
```


**Тип запроса:** config.Config


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


**Тип запроса:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/workspace.go:32`



---


[function] name: Title file: go/cli/internal/tui/workspace.go:68 returns_error: нет description: —


### Title (go/cli/internal/tui/workspace.go:68)


Title is a method that performs operations based on the provided parameters and returns ().


```go
func (i sessionListItem) Title(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:68`



---


[function] name: Update file: go/cli/internal/tui/workspace.go:190 returns_error: нет description: —


### Update (go/cli/internal/tui/workspace.go:190)


Update is a method that updates data based on the provided parameters and returns (tea.Model, tea.Cmd).


```go
func (m *workspaceModel) Update((tea.Model, tea.Cmd)) (tea.Model, tea.Cmd)
```


**Тип ответа:** tea.Model


```json
{
  "Scheme": null,
  "Reconciler": {}
}
```


*Определено в:* `go/internal/controller/modelproviderconfig_controller.go`


**Тип ответа:** tea.Cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/workspace.go:190`



---


[function] name: View file: go/cli/internal/tui/workspace.go:546 returns_error: нет description: —


### View (go/cli/internal/tui/workspace.go:546)


View is a method that performs operations based on the provided parameters and returns ().


```go
func (m *workspaceModel) View(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:546`



---


[function] name: createSession file: go/cli/internal/tui/workspace.go:177 returns_error: нет description: —


### createSession (go/cli/internal/tui/workspace.go:177)


createSession is a method that performs operations based on the provided parameters and returns (name string).


```go
func (m *workspaceModel) createSession((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "client": null
}
```


*Определено в:* `go/pkg/client/namespace.go`


📍 *Расположение:* `go/cli/internal/tui/workspace.go:177`



---


[function] name: fetchSessionHistoryCmd file: go/cli/internal/tui/workspace.go:490 returns_error: нет description: —


### fetchSessionHistoryCmd (go/cli/internal/tui/workspace.go:490)


fetchSessionHistoryCmd is a method that performs operations based on the provided parameters and returns (sessionID string).


```go
func (m *workspaceModel) fetchSessionHistoryCmd((sessionID string)) (sessionID string)
```


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/workspace.go:490`



---


[function] name: lineCount file: go/cli/internal/tui/workspace.go:706 returns_error: нет description: —


### lineCount (go/cli/internal/tui/workspace.go:706)


lineCount is a function that performs operations based on the provided parameters and returns (s string).


```go
func lineCount((s string)) (s string)
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


📍 *Расположение:* `go/cli/internal/tui/workspace.go:706`



---


[function] name: loadAgents file: go/cli/internal/tui/workspace.go:152 returns_error: нет description: —


### loadAgents (go/cli/internal/tui/workspace.go:152)


loadAgents is a method that performs operations based on the provided parameters and returns ().


```go
func (m *workspaceModel) loadAgents(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:152`



---


[function] name: loadSessions file: go/cli/internal/tui/workspace.go:159 returns_error: нет description: —


### loadSessions (go/cli/internal/tui/workspace.go:159)


loadSessions is a method that performs operations based on the provided parameters and returns ().


```go
func (m *workspaceModel) loadSessions(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:159`



---


[function] name: newWorkspaceModel file: go/cli/internal/tui/workspace.go:114 returns_error: нет description: —


### newWorkspaceModel (go/cli/internal/tui/workspace.go:114)


newWorkspaceModel is a function that performs operations based on the provided parameters and returns (cfg *config.Config, clientSet *client.ClientSet, verbose bool).


```go
func newWorkspaceModel((cfg *config.Config, clientSet *client.ClientSet, verbose bool)) (cfg *config.Config, clientSet *client.ClientSet, verbose bool)
```


**Тип запроса:** config.Config


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


**Тип запроса:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


**Тип ответа:** cfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config.Config


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


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client.ClientSet


```json
{
  "baseClient": null,
  "Health": {},
  "Version": {},
  "ModelConfig": {},
  "Session": {},
  "Agent": {},
  "Tool": {},
  "ToolServer": {},
  "Memory": {},
  "ModelProviderConfig": {},
  "Model": {},
  "Namespace": {},
  "Feedback": {}
}
```


*Определено в:* `go/pkg/client/clientset.go`


**Тип ответа:** verbose


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/workspace.go:114`



---


[function] name: renderDetails file: go/cli/internal/tui/workspace.go:509 returns_error: нет description: renderDetails creates the contents for the right pane


### renderDetails (go/cli/internal/tui/workspace.go:509)


renderDetails creates the contents for the right pane


```go
func (m *workspaceModel) renderDetails(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:509`



---


[function] name: renderTitle file: go/cli/internal/tui/workspace.go:699 returns_error: нет description: renderTitle returns a styled block-art banner for the header.


### renderTitle (go/cli/internal/tui/workspace.go:699)


renderTitle returns a styled block-art banner for the header.


```go
func renderTitle((width int)) (width int)
```


**Тип ответа:** width


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/workspace.go:699`



---


[function] name: resize file: go/cli/internal/tui/workspace.go:434 returns_error: нет description: —


### resize (go/cli/internal/tui/workspace.go:434)


resize is a method that performs operations based on the provided parameters and returns ().


```go
func (m *workspaceModel) resize(()) ()
```


📍 *Расположение:* `go/cli/internal/tui/workspace.go:434`



---


[function] name: sortSessions file: go/cli/internal/tui/workspace.go:720 returns_error: нет description: sortSessions sorts sessions by UpdatedAt then CreatedAt descending.


### sortSessions (go/cli/internal/tui/workspace.go:720)


sortSessions sorts sessions by UpdatedAt then CreatedAt descending.


```go
func sortSessions((sessions []*api.Session)) (sessions []*api.Session)
```


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


**Тип ответа:** sessions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `go/cli/internal/tui/workspace.go:720`



---


[function] name: startChat file: go/cli/internal/tui/workspace.go:459 returns_error: нет description: —


### startChat (go/cli/internal/tui/workspace.go:459)


startChat is a method that performs operations based on the provided parameters and returns (loadHistory bool).


```go
func (m *workspaceModel) startChat((loadHistory bool)) (loadHistory bool)
```


**Тип ответа:** loadHistory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/cli/internal/tui/workspace.go:459`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_api.md)

- [Следующая директория](go_cmd.md)


---

