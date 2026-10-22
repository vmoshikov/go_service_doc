---
title: "Функции: pkg/auth"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/auth
---


# Функции: pkg/auth


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_apis.md)

- [Следующая директория](pkg_capabilities.md)


---


## Меню по файлам


- 📄 [pkg/auth/authorizer/abac/abac.go](#pkgauthauthorizerabacabacgo)

- 📄 [pkg/auth/nodeidentifier/default.go](#pkgauthnodeidentifierdefaultgo)


---


## pkg/auth/authorizer/abac/abac.go


📄 Исходный файл: `pkg/auth/authorizer/abac/abac.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Authorize](#authorize-pkgauthauthorizerabacabacgo229) `:229`

- 🔗 [Error](#error-pkgauthauthorizerabacabacgo46) `:46`

- 🔗 [NewFromFile](#newfromfile-pkgauthauthorizerabacabacgo59) `:59`

- 🔗 [RulesFor](#rulesfor-pkgauthauthorizerabacabacgo242) `:242`

- 🔗 [getVerbs](#getverbs-pkgauthauthorizerabacabacgo274) `:274`

- 🔗 [matches](#matches-pkgauthauthorizerabacabacgo121) `:121`

- 🔗 [nonResourceMatches](#nonresourcematches-pkgauthauthorizerabacabacgo195) `:195`

- 🔗 [resourceMatches](#resourcematches-pkgauthauthorizerabacabacgo214) `:214`

- 🔗 [subjectMatches](#subjectmatches-pkgauthauthorizerabacabacgo137) `:137`

- 🔗 [verbMatches](#verbmatches-pkgauthauthorizerabacabacgo179) `:179`


</details>


[function] name: Authorize file: pkg/auth/authorizer/abac/abac.go:229 returns_error: да description: Authorize implements authorizer.Authorize


### Authorize (pkg/auth/authorizer/abac/abac.go:229)


Authorize implements authorizer.Authorize


```go
func (pl PolicyList) Authorize((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
```


**Тип ответа:** authorizer.Decision


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authorizer.Decision`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:229`



---


[function] name: Error file: pkg/auth/authorizer/abac/abac.go:46 returns_error: нет description: —


### Error (pkg/auth/authorizer/abac/abac.go:46)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (p policyLoadError) Error(()) ()
```


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:46`



---


[function] name: NewFromFile file: pkg/auth/authorizer/abac/abac.go:59 returns_error: да description: NewFromFile attempts to create a policy list from the given file.

TODO: Have policies be created via an API call and st


### NewFromFile (pkg/auth/authorizer/abac/abac.go:59)


NewFromFile attempts to create a policy list from the given file.

TODO: Have policies be created via an API call and stored in REST storage.


```go
func NewFromFile((PolicyList, error)) (PolicyList, error)
```


**Тип ответа:** PolicyList


```json
{
  "items": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/audit/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PolicyList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:59`



---


[function] name: RulesFor file: pkg/auth/authorizer/abac/abac.go:242 returns_error: да description: RulesFor returns rules for the given user and namespace.


### RulesFor (pkg/auth/authorizer/abac/abac.go:242)


RulesFor returns rules for the given user and namespace.


```go
func (pl PolicyList) RulesFor(([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)) ([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)
```


**Тип ответа:** authorizer.ResourceRuleInfo


```json
{
  "Verbs": [],
  "APIGroups": [],
  "Resources": [],
  "ResourceNames": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authorization/authorizer/rule.go`


**Тип ответа:** authorizer.NonResourceRuleInfo


```json
{
  "Verbs": [],
  "NonResourceURLs": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authorization/authorizer/rule.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]authorizer.ResourceRuleInfo`, `[]authorizer.NonResourceRuleInfo`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:242`



---


[function] name: getVerbs file: pkg/auth/authorizer/abac/abac.go:274 returns_error: нет description: —


### getVerbs (pkg/auth/authorizer/abac/abac.go:274)


getVerbs is a function that performs operations based on the provided parameters and returns (isReadOnly bool).


```go
func getVerbs((isReadOnly bool)) (isReadOnly bool)
```


**Тип ответа:** isReadOnly


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:274`



---


[function] name: matches file: pkg/auth/authorizer/abac/abac.go:121 returns_error: нет description: —


### matches (pkg/auth/authorizer/abac/abac.go:121)


matches is a function that performs operations based on the provided parameters and returns (p abac.Policy, a authorizer.Attributes).


```go
func matches((p abac.Policy, a authorizer.Attributes)) (p abac.Policy, a authorizer.Attributes)
```


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** abac.Policy


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/abac/v1beta1/types.go`


**Тип ответа:** a


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


**Тип ответа:** authorizer.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:121`



---


[function] name: nonResourceMatches file: pkg/auth/authorizer/abac/abac.go:195 returns_error: нет description: —


### nonResourceMatches (pkg/auth/authorizer/abac/abac.go:195)


nonResourceMatches is a function that performs operations based on the provided parameters and returns (p abac.Policy, a authorizer.Attributes).


```go
func nonResourceMatches((p abac.Policy, a authorizer.Attributes)) (p abac.Policy, a authorizer.Attributes)
```


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** abac.Policy


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/abac/v1beta1/types.go`


**Тип ответа:** a


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


**Тип ответа:** authorizer.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:195`



---


[function] name: resourceMatches file: pkg/auth/authorizer/abac/abac.go:214 returns_error: нет description: —


### resourceMatches (pkg/auth/authorizer/abac/abac.go:214)


resourceMatches is a function that performs operations based on the provided parameters and returns (p abac.Policy, a authorizer.Attributes).


```go
func resourceMatches((p abac.Policy, a authorizer.Attributes)) (p abac.Policy, a authorizer.Attributes)
```


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** abac.Policy


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/abac/v1beta1/types.go`


**Тип ответа:** a


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


**Тип ответа:** authorizer.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:214`



---


[function] name: subjectMatches file: pkg/auth/authorizer/abac/abac.go:137 returns_error: нет description: subjectMatches returns true if specified user and group properties in the policy match the attributes


### subjectMatches (pkg/auth/authorizer/abac/abac.go:137)


subjectMatches returns true if specified user and group properties in the policy match the attributes


```go
func subjectMatches((p abac.Policy, user user.Info)) (p abac.Policy, user user.Info)
```


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** abac.Policy


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/abac/v1beta1/types.go`


**Тип ответа:** user


```json
{
  "agent": "string",
  "rt": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


**Тип ответа:** user.Info


```json
{
  "Major": "string",
  "Minor": "string",
  "EmulationMajor": "string",
  "EmulationMinor": "string",
  "MinCompatibilityMajor": "string",
  "MinCompatibilityMinor": "string",
  "GitVersion": "string",
  "GitCommit": "string",
  "GitTreeState": "string",
  "BuildDate": "string",
  "GoVersion": "string",
  "Compiler": "string",
  "Platform": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/version/types.go`


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:137`



---


[function] name: verbMatches file: pkg/auth/authorizer/abac/abac.go:179 returns_error: нет description: —


### verbMatches (pkg/auth/authorizer/abac/abac.go:179)


verbMatches is a function that performs operations based on the provided parameters and returns (p abac.Policy, a authorizer.Attributes).


```go
func verbMatches((p abac.Policy, a authorizer.Attributes)) (p abac.Policy, a authorizer.Attributes)
```


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** abac.Policy


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/abac/v1beta1/types.go`


**Тип ответа:** a


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


**Тип ответа:** authorizer.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `pkg/auth/authorizer/abac/abac.go:179`




## pkg/auth/nodeidentifier/default.go


📄 Исходный файл: `pkg/auth/nodeidentifier/default.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [NewDefaultNodeIdentifier](#newdefaultnodeidentifier-pkgauthnodeidentifierdefaultgo29) `:29`

- 🔗 [NodeIdentity](#nodeidentity-pkgauthnodeidentifierdefaultgo42) `:42`


</details>


[function] name: NewDefaultNodeIdentifier file: pkg/auth/nodeidentifier/default.go:29 returns_error: нет description: NewDefaultNodeIdentifier returns a default NodeIdentifier implementation,
which returns isNode=true if the user groups c


### NewDefaultNodeIdentifier (pkg/auth/nodeidentifier/default.go:29)


NewDefaultNodeIdentifier returns a default NodeIdentifier implementation,
which returns isNode=true if the user groups contain the system:nodes group
and the user name matches the format system:node:<nodeName>, and populates
nodeName if isNode is true


```go
func NewDefaultNodeIdentifier(()) ()
```


📍 *Расположение:* `pkg/auth/nodeidentifier/default.go:29`



---


[function] name: NodeIdentity file: pkg/auth/nodeidentifier/default.go:42 returns_error: нет description: NodeIdentity returns isNode=true if the user groups contain the system:nodes
group and the user name matches the format 


### NodeIdentity (pkg/auth/nodeidentifier/default.go:42)


NodeIdentity returns isNode=true if the user groups contain the system:nodes
group and the user name matches the format system:node:<nodeName>, and
populates nodeName if isNode is true


```go
func (defaultNodeIdentifier) NodeIdentity((string, bool)) (string, bool)
```


📍 *Расположение:* `pkg/auth/nodeidentifier/default.go:42`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_apis.md)

- [Следующая директория](pkg_capabilities.md)


---

