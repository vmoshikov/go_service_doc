---
title: "Функции: pkg/certauthorization"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/certauthorization
---


# Функции: pkg/certauthorization


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_capabilities.md)

- [Следующая директория](pkg_client.md)


---


## Меню по файлам


- 📄 [pkg/certauthorization/certauthorization.go](#pkgcertauthorizationcertauthorizationgo)


---


## pkg/certauthorization/certauthorization.go


📄 Исходный файл: `pkg/certauthorization/certauthorization.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [IsAuthorizedForSignerName](#isauthorizedforsignername-pkgcertauthorizationcertauthorizationgo34) `:34`

- 🔗 [buildAttributes](#buildattributes-pkgcertauthorizationcertauthorizationgo59) `:59`

- 🔗 [buildWildcardAttributes](#buildwildcardattributes-pkgcertauthorizationcertauthorizationgo71) `:71`


</details>


[function] name: IsAuthorizedForSignerName file: pkg/certauthorization/certauthorization.go:34 returns_error: нет description: IsAuthorizedForSignerName returns true if 'info' is authorized to perform the given
'verb' on the synthetic 'signers' re


### IsAuthorizedForSignerName (pkg/certauthorization/certauthorization.go:34)


IsAuthorizedForSignerName returns true if 'info' is authorized to perform the given
'verb' on the synthetic 'signers' resource with the given signerName.
If the user does not have permission to perform the 'verb' on the given signerName,
it will also perform an authorization check against {domain portion}/*, for example
`kubernetes.io/*`. This allows an entity to be granted permission to 'verb' on all
signerNames with a given 'domain portion'.


```go
func IsAuthorizedForSignerName((ctx context.Context, authz authorizer.Authorizer, info user.Info, verb, signerName string)) (ctx context.Context, authz authorizer.Authorizer, info user.Info, verb, signerName string)
```


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


**Тип ответа:** authz


```json
{
  "authorized": {},
  "reason": "string",
  "err": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/authorizer/caching_authorizer.go`


**Тип ответа:** authorizer.Authorizer


```json
{
  "subjectAccessReview": {},
  "responseCache": null,
  "authorizedTTL": {},
  "unauthorizedTTL": {},
  "retryBackoff": {},
  "decisionOnError": {},
  "metrics": {},
  "celMatcher": null,
  "name": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go`


**Тип ответа:** info


```json
{
  "lister": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/pods.go`


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


**Тип ответа:** verb


```json
{
  "value": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/pflags.go`


**Тип ответа:** signerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/certauthorization/certauthorization.go:34`



---


[function] name: buildAttributes file: pkg/certauthorization/certauthorization.go:59 returns_error: нет description: —


### buildAttributes (pkg/certauthorization/certauthorization.go:59)


buildAttributes is a function that performs operations based on the provided parameters and returns (info user.Info, verb, signerName string).


```go
func buildAttributes((info user.Info, verb, signerName string)) (info user.Info, verb, signerName string)
```


**Тип ответа:** info


```json
{
  "lister": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/pods.go`


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


**Тип ответа:** verb


```json
{
  "value": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/pflags.go`


**Тип ответа:** signerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/certauthorization/certauthorization.go:59`



---


[function] name: buildWildcardAttributes file: pkg/certauthorization/certauthorization.go:71 returns_error: нет description: —


### buildWildcardAttributes (pkg/certauthorization/certauthorization.go:71)


buildWildcardAttributes is a function that performs operations based on the provided parameters and returns (info user.Info, verb, signerName string).


```go
func buildWildcardAttributes((info user.Info, verb, signerName string)) (info user.Info, verb, signerName string)
```


**Тип ответа:** info


```json
{
  "lister": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/pods.go`


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


**Тип ответа:** verb


```json
{
  "value": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/pflags.go`


**Тип ответа:** signerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/certauthorization/certauthorization.go:71`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_capabilities.md)

- [Следующая директория](pkg_client.md)


---

