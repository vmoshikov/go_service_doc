---
title: "Функции: pkg/kubeapiserver"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/kubeapiserver
---


# Функции: pkg/kubeapiserver


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_generated.md)

- [Следующая директория](pkg_kubectl.md)


---


## Меню по файлам


- 📄 [pkg/kubeapiserver/admission/config.go](#pkgkubeapiserveradmissionconfiggo)

- 📄 [pkg/kubeapiserver/admission/exclusion/resources.go](#pkgkubeapiserveradmissionexclusionresourcesgo)

- 📄 [pkg/kubeapiserver/admission/initializer.go](#pkgkubeapiserveradmissioninitializergo)

- 📄 [pkg/kubeapiserver/authenticator/config.go](#pkgkubeapiserverauthenticatorconfiggo)

- 📄 [pkg/kubeapiserver/authorizer/config.go](#pkgkubeapiserverauthorizerconfiggo)

- 📄 [pkg/kubeapiserver/authorizer/modes/modes.go](#pkgkubeapiserverauthorizermodesmodesgo)

- 📄 [pkg/kubeapiserver/authorizer/reload.go](#pkgkubeapiserverauthorizerreloadgo)

- 📄 [pkg/kubeapiserver/default_storage_factory_builder.go](#pkgkubeapiserverdefault_storage_factory_buildergo)

- 📄 [pkg/kubeapiserver/options/admission.go](#pkgkubeapiserveroptionsadmissiongo)

- 📄 [pkg/kubeapiserver/options/authentication.go](#pkgkubeapiserveroptionsauthenticationgo)

- 📄 [pkg/kubeapiserver/options/authorization.go](#pkgkubeapiserveroptionsauthorizationgo)

- 📄 [pkg/kubeapiserver/options/plugins.go](#pkgkubeapiserveroptionspluginsgo)

- 📄 [pkg/kubeapiserver/options/serving.go](#pkgkubeapiserveroptionsservinggo)


---


## pkg/kubeapiserver/admission/config.go


📄 Исходный файл: `pkg/kubeapiserver/admission/config.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [New](#new-pkgkubeapiserveradmissionconfiggo27) `:27`


</details>


[function] name: New file: pkg/kubeapiserver/admission/config.go:27 returns_error: да description: New sets up the plugins and admission start hooks needed for admission


### New (pkg/kubeapiserver/admission/config.go:27)


New sets up the plugins and admission start hooks needed for admission


```go
func (c *Config) New(([]admission.PluginInitializer, error)) ([]admission.PluginInitializer, error)
```


**Тип ответа:** admission.PluginInitializer


```json
{
  "quotaConfiguration": {},
  "excludedAdmissionResources": []
}
```


*Определено в:* `pkg/controlplane/apiserver/admission/initializer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]admission.PluginInitializer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/admission/config.go:27`




## pkg/kubeapiserver/admission/exclusion/resources.go


📄 Исходный файл: `pkg/kubeapiserver/admission/exclusion/resources.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Excluded](#excluded-pkgkubeapiserveradmissionexclusionresourcesgo64) `:64`

- 🔗 [Included](#included-pkgkubeapiserveradmissionexclusionresourcesgo58) `:58`


</details>


[function] name: Excluded file: pkg/kubeapiserver/admission/exclusion/resources.go:64 returns_error: нет description: Excluded returns a copy of the list of resources that the expression-based admission controllers
should ignore.


### Excluded (pkg/kubeapiserver/admission/exclusion/resources.go:64)


Excluded returns a copy of the list of resources that the expression-based admission controllers
should ignore.


```go
func Excluded(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/admission/exclusion/resources.go:64`



---


[function] name: Included file: pkg/kubeapiserver/admission/exclusion/resources.go:58 returns_error: нет description: Included returns a copy of the list of resources that the expression-based admission controllers
should intercept.


### Included (pkg/kubeapiserver/admission/exclusion/resources.go:58)


Included returns a copy of the list of resources that the expression-based admission controllers
should intercept.


```go
func Included(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/admission/exclusion/resources.go:58`




## pkg/kubeapiserver/admission/initializer.go


📄 Исходный файл: `pkg/kubeapiserver/admission/initializer.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Initialize](#initialize-pkgkubeapiserveradmissioninitializergo38) `:38`

- 🔗 [NewPluginInitializer](#newplugininitializer-pkgkubeapiserveradmissioninitializergo32) `:32`


</details>


[function] name: Initialize file: pkg/kubeapiserver/admission/initializer.go:38 returns_error: нет description: Initialize checks the initialization interfaces implemented by each plugin
and provide the appropriate initialization da


### Initialize (pkg/kubeapiserver/admission/initializer.go:38)


Initialize checks the initialization interfaces implemented by each plugin
and provide the appropriate initialization data


```go
func (i *PluginInitializer) Initialize((plugin admission.Interface)) (plugin admission.Interface)
```


**Тип ответа:** plugin


```json
{
  "observer": {},
  "extraLabels": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/metrics/metrics.go`


**Тип ответа:** admission.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `pkg/kubeapiserver/admission/initializer.go:38`



---


[function] name: NewPluginInitializer file: pkg/kubeapiserver/admission/initializer.go:32 returns_error: нет description: NewPluginInitializer constructs new instance of PluginInitializer


### NewPluginInitializer (pkg/kubeapiserver/admission/initializer.go:32)


NewPluginInitializer constructs new instance of PluginInitializer


```go
func NewPluginInitializer(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/admission/initializer.go:32`




## pkg/kubeapiserver/authenticator/config.go


📄 Исходный файл: `pkg/kubeapiserver/authenticator/config.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [New](#new-pkgkubeapiserverauthenticatorconfiggo107) `:107`

- 🔗 [newAuthenticatorFromTokenFile](#newauthenticatorfromtokenfile-pkgkubeapiserverauthenticatorconfiggo370) `:370`

- 🔗 [newJWTAuthenticator](#newjwtauthenticator-pkgkubeapiserverauthenticatorconfiggo257) `:257`

- 🔗 [newLegacyServiceAccountAuthenticator](#newlegacyserviceaccountauthenticator-pkgkubeapiserverauthenticatorconfiggo380) `:380`

- 🔗 [newServiceAccountAuthenticator](#newserviceaccountauthenticator-pkgkubeapiserverauthenticatorconfiggo394) `:394`

- 🔗 [newWebhookTokenAuthenticator](#newwebhooktokenauthenticator-pkgkubeapiserverauthenticatorconfiggo402) `:402`

- 🔗 [updateAuthenticationConfig](#updateauthenticationconfig-pkgkubeapiserverauthenticatorconfiggo314) `:314`


</details>


[function] name: New file: pkg/kubeapiserver/authenticator/config.go:107 returns_error: да description: New returns an authenticator.Request or an error that supports the standard
Kubernetes authentication mechanisms.


### New (pkg/kubeapiserver/authenticator/config.go:107)


New returns an authenticator.Request or an error that supports the standard
Kubernetes authentication mechanisms.


```go
func (config Config) New((authenticator.Request, func(context.Context, *apiserver.AuthenticationConfiguration) error, *spec.SecurityDefinitions, spec3.SecuritySchemes, error)) (authenticator.Request, func(context.Context, *apiserver.AuthenticationConfiguration) error, *spec.SecurityDefinitions, spec3.SecuritySchemes, error)
```


**Тип запроса:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Тип запроса:** spec.SecurityDefinitions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authenticator.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Тип ответа:** spec.SecurityDefinitions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** spec3.SecuritySchemes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authenticator.Request`, `func(context.Context`, `*apiserver.AuthenticationConfiguration) error`, `*spec.SecurityDefinitions`, `spec3.SecuritySchemes`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authenticator/config.go:107`



---


[function] name: newAuthenticatorFromTokenFile file: pkg/kubeapiserver/authenticator/config.go:370 returns_error: да description: newAuthenticatorFromTokenFile returns an authenticator.Token or an error


### newAuthenticatorFromTokenFile (pkg/kubeapiserver/authenticator/config.go:370)


newAuthenticatorFromTokenFile returns an authenticator.Token or an error


```go
func newAuthenticatorFromTokenFile((authenticator.Token, error)) (authenticator.Token, error)
```


**Тип ответа:** authenticator.Token


```json
{
  "IDToken": "string",
  "AccessToken": "string",
  "TokenType": "string",
  "RefreshToken": "string",
  "ExpiresIn": 0
}
```


*Определено в:* `test/utils/oidc/handlers/handlers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authenticator.Token`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authenticator/config.go:370`



---


[function] name: newJWTAuthenticator file: pkg/kubeapiserver/authenticator/config.go:257 returns_error: да description: —


### newJWTAuthenticator (pkg/kubeapiserver/authenticator/config.go:257)


newJWTAuthenticator is a function that performs operations based on the provided parameters and may return an error.


```go
func newJWTAuthenticator((_ *jwtAuthenticatorWithCancel, buildErr error)) (_ *jwtAuthenticatorWithCancel, buildErr error)
```


**Тип запроса:** jwtAuthenticatorWithCancel


```json
{
  "jwtAuthenticator": {},
  "healthCheck": {},
  "cancel": {}
}
```


*Определено в:* `pkg/kubeapiserver/authenticator/config.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** jwtAuthenticatorWithCancel


```json
{
  "jwtAuthenticator": {},
  "healthCheck": {},
  "cancel": {}
}
```


*Определено в:* `pkg/kubeapiserver/authenticator/config.go`


**Тип ответа:** buildErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `_ *jwtAuthenticatorWithCancel`, `buildErr error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authenticator/config.go:257`



---


[function] name: newLegacyServiceAccountAuthenticator file: pkg/kubeapiserver/authenticator/config.go:380 returns_error: да description: newLegacyServiceAccountAuthenticator returns an authenticator.Token or an error


### newLegacyServiceAccountAuthenticator (pkg/kubeapiserver/authenticator/config.go:380)


newLegacyServiceAccountAuthenticator returns an authenticator.Token or an error


```go
func newLegacyServiceAccountAuthenticator((authenticator.Token, error)) (authenticator.Token, error)
```


**Тип ответа:** authenticator.Token


```json
{
  "IDToken": "string",
  "AccessToken": "string",
  "TokenType": "string",
  "RefreshToken": "string",
  "ExpiresIn": 0
}
```


*Определено в:* `test/utils/oidc/handlers/handlers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authenticator.Token`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authenticator/config.go:380`



---


[function] name: newServiceAccountAuthenticator file: pkg/kubeapiserver/authenticator/config.go:394 returns_error: да description: newServiceAccountAuthenticator returns an authenticator.Token or an error


### newServiceAccountAuthenticator (pkg/kubeapiserver/authenticator/config.go:394)


newServiceAccountAuthenticator returns an authenticator.Token or an error


```go
func newServiceAccountAuthenticator((authenticator.Token, error)) (authenticator.Token, error)
```


**Тип ответа:** authenticator.Token


```json
{
  "IDToken": "string",
  "AccessToken": "string",
  "TokenType": "string",
  "RefreshToken": "string",
  "ExpiresIn": 0
}
```


*Определено в:* `test/utils/oidc/handlers/handlers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authenticator.Token`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authenticator/config.go:394`



---


[function] name: newWebhookTokenAuthenticator file: pkg/kubeapiserver/authenticator/config.go:402 returns_error: да description: —


### newWebhookTokenAuthenticator (pkg/kubeapiserver/authenticator/config.go:402)


newWebhookTokenAuthenticator is a function that performs operations based on the provided parameters and may return an error.


```go
func newWebhookTokenAuthenticator((authenticator.Token, error)) (authenticator.Token, error)
```


**Тип ответа:** authenticator.Token


```json
{
  "IDToken": "string",
  "AccessToken": "string",
  "TokenType": "string",
  "RefreshToken": "string",
  "ExpiresIn": 0
}
```


*Определено в:* `test/utils/oidc/handlers/handlers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authenticator.Token`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authenticator/config.go:402`



---


[function] name: updateAuthenticationConfig file: pkg/kubeapiserver/authenticator/config.go:314 returns_error: нет description: the input ctx controls the timeout for updateAuthenticationConfig to return, not the lifetime of the constructed authent


### updateAuthenticationConfig (pkg/kubeapiserver/authenticator/config.go:314)


the input ctx controls the timeout for updateAuthenticationConfig to return, not the lifetime of the constructed authenticators.


```go
func (c *authenticationConfigUpdater) updateAuthenticationConfig((ctx context.Context, authConfig *apiserver.AuthenticationConfiguration)) (ctx context.Context, authConfig *apiserver.AuthenticationConfiguration)
```


**Тип запроса:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


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


**Тип ответа:** authConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


📍 *Расположение:* `pkg/kubeapiserver/authenticator/config.go:314`




## pkg/kubeapiserver/authorizer/config.go


📄 Исходный файл: `pkg/kubeapiserver/authorizer/config.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetNameForAuthorizerMode](#getnameforauthorizermode-pkgkubeapiserverauthorizerconfiggo169) `:169`

- 🔗 [LoadAndValidateData](#loadandvalidatedata-pkgkubeapiserverauthorizerconfiggo185) `:185`

- 🔗 [LoadAndValidateFile](#loadandvalidatefile-pkgkubeapiserverauthorizerconfiggo173) `:173`

- 🔗 [New](#new-pkgkubeapiserverauthorizerconfiggo82) `:82`


</details>


[function] name: GetNameForAuthorizerMode file: pkg/kubeapiserver/authorizer/config.go:169 returns_error: нет description: GetNameForAuthorizerMode returns the name to be set for the mode in AuthorizationConfiguration
For now, lower cases the 


### GetNameForAuthorizerMode (pkg/kubeapiserver/authorizer/config.go:169)


GetNameForAuthorizerMode returns the name to be set for the mode in AuthorizationConfiguration
For now, lower cases the mode name


```go
func GetNameForAuthorizerMode((mode string)) (mode string)
```


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


📍 *Расположение:* `pkg/kubeapiserver/authorizer/config.go:169`



---


[function] name: LoadAndValidateData file: pkg/kubeapiserver/authorizer/config.go:185 returns_error: да description: —


### LoadAndValidateData (pkg/kubeapiserver/authorizer/config.go:185)


LoadAndValidateData is a function that performs operations based on the provided parameters and may return an error.


```go
func LoadAndValidateData((*authzconfig.AuthorizationConfiguration, error)) (*authzconfig.AuthorizationConfiguration, error)
```


**Тип запроса:** authzconfig.AuthorizationConfiguration


```json
{
  "Authorizers": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Тип ответа:** authzconfig.AuthorizationConfiguration


```json
{
  "Authorizers": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*authzconfig.AuthorizationConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authorizer/config.go:185`



---


[function] name: LoadAndValidateFile file: pkg/kubeapiserver/authorizer/config.go:173 returns_error: да description: —


### LoadAndValidateFile (pkg/kubeapiserver/authorizer/config.go:173)


LoadAndValidateFile is a function that performs operations based on the provided parameters and may return an error.


```go
func LoadAndValidateFile((*authzconfig.AuthorizationConfiguration, string, error)) (*authzconfig.AuthorizationConfiguration, string, error)
```


**Тип запроса:** authzconfig.AuthorizationConfiguration


```json
{
  "Authorizers": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Тип ответа:** authzconfig.AuthorizationConfiguration


```json
{
  "Authorizers": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*authzconfig.AuthorizationConfiguration`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authorizer/config.go:173`



---


[function] name: New file: pkg/kubeapiserver/authorizer/config.go:82 returns_error: да description: New returns the right sort of union of multiple authorizer.Authorizer objects
based on the authorizationMode or an error


### New (pkg/kubeapiserver/authorizer/config.go:82)


New returns the right sort of union of multiple authorizer.Authorizer objects
based on the authorizationMode or an error.
stopCh is used to shut down config reload goroutines when the server is shutting down.

Note: the cel compiler construction depends on feature gates and the compatibility version to be initialized.


```go
func (config Config) New((authorizer.Authorizer, authorizer.RuleResolver, error)) (authorizer.Authorizer, authorizer.RuleResolver, error)
```


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


**Тип ответа:** authorizer.RuleResolver


```json
{
  "roleGetter": {},
  "roleBindingLister": {},
  "clusterRoleGetter": {},
  "clusterRoleBindingLister": {}
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authorizer.Authorizer`, `authorizer.RuleResolver`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authorizer/config.go:82`




## pkg/kubeapiserver/authorizer/modes/modes.go


📄 Исходный файл: `pkg/kubeapiserver/authorizer/modes/modes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IsValidAuthorizationMode](#isvalidauthorizationmode-pkgkubeapiserverauthorizermodesmodesgo40) `:40`


</details>


[function] name: IsValidAuthorizationMode file: pkg/kubeapiserver/authorizer/modes/modes.go:40 returns_error: нет description: IsValidAuthorizationMode returns true if the given authorization mode is a valid one for the apiserver


### IsValidAuthorizationMode (pkg/kubeapiserver/authorizer/modes/modes.go:40)


IsValidAuthorizationMode returns true if the given authorization mode is a valid one for the apiserver


```go
func IsValidAuthorizationMode((authzMode string)) (authzMode string)
```


**Тип ответа:** authzMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/kubeapiserver/authorizer/modes/modes.go:40`




## pkg/kubeapiserver/authorizer/reload.go


📄 Исходный файл: `pkg/kubeapiserver/authorizer/reload.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Authorize](#authorize-pkgkubeapiserverauthorizerreloadgo78) `:78`

- 🔗 [RulesFor](#rulesfor-pkgkubeapiserverauthorizerreloadgo82) `:82`

- 🔗 [checkFile](#checkfile-pkgkubeapiserverauthorizerreloadgo210) `:210`

- 🔗 [newForConfig](#newforconfig-pkgkubeapiserverauthorizerreloadgo87) `:87`

- 🔗 [runReload](#runreload-pkgkubeapiserverauthorizerreloadgo193) `:193`


</details>


[function] name: Authorize file: pkg/kubeapiserver/authorizer/reload.go:78 returns_error: да description: —


### Authorize (pkg/kubeapiserver/authorizer/reload.go:78)


Authorize is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *reloadableAuthorizerResolver) Authorize((authorized authorizer.Decision, reason string, err error)) (authorized authorizer.Decision, reason string, err error)
```


**Тип ответа:** authorized


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authorizer.Decision


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** err


```json
{
  "msg": {},
  "cause": {},
  "stack": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/errors/errors.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authorized authorizer.Decision`, `reason string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authorizer/reload.go:78`



---


[function] name: RulesFor file: pkg/kubeapiserver/authorizer/reload.go:82 returns_error: да description: —


### RulesFor (pkg/kubeapiserver/authorizer/reload.go:82)


RulesFor is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *reloadableAuthorizerResolver) RulesFor(([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)) ([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)
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


📍 *Расположение:* `pkg/kubeapiserver/authorizer/reload.go:82`



---


[function] name: checkFile file: pkg/kubeapiserver/authorizer/reload.go:210 returns_error: нет description: —


### checkFile (pkg/kubeapiserver/authorizer/reload.go:210)


checkFile is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (r *reloadableAuthorizerResolver) checkFile((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/kubeapiserver/authorizer/reload.go:210`



---


[function] name: newForConfig file: pkg/kubeapiserver/authorizer/reload.go:87 returns_error: да description: newForConfig constructs


### newForConfig (pkg/kubeapiserver/authorizer/reload.go:87)


newForConfig constructs


```go
func (r *reloadableAuthorizerResolver) newForConfig((authorizer.Authorizer, authorizer.RuleResolver, error)) (authorizer.Authorizer, authorizer.RuleResolver, error)
```


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


**Тип ответа:** authorizer.RuleResolver


```json
{
  "roleGetter": {},
  "roleBindingLister": {},
  "clusterRoleGetter": {},
  "clusterRoleBindingLister": {}
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `authorizer.Authorizer`, `authorizer.RuleResolver`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/authorizer/reload.go:87`



---


[function] name: runReload file: pkg/kubeapiserver/authorizer/reload.go:193 returns_error: нет description: runReload starts checking the config file for changes and reloads the authorizer when it changes.
Blocks until ctx is co


### runReload (pkg/kubeapiserver/authorizer/reload.go:193)


runReload starts checking the config file for changes and reloads the authorizer when it changes.
Blocks until ctx is complete.


```go
func (r *reloadableAuthorizerResolver) runReload((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/kubeapiserver/authorizer/reload.go:193`




## pkg/kubeapiserver/default_storage_factory_builder.go


📄 Исходный файл: `pkg/kubeapiserver/default_storage_factory_builder.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Complete](#complete-pkgkubeapiserverdefault_storage_factory_buildergo109) `:109`

- 🔗 [DefaultWatchCacheSizes](#defaultwatchcachesizes-pkgkubeapiserverdefault_storage_factory_buildergo56) `:56`

- 🔗 [New](#new-pkgkubeapiserverdefault_storage_factory_buildergo125) `:125`

- 🔗 [NewStorageFactoryConfig](#newstoragefactoryconfig-pkgkubeapiserverdefault_storage_factory_buildergo64) `:64`

- 🔗 [NewStorageFactoryConfigEffectiveVersion](#newstoragefactoryconfigeffectiveversion-pkgkubeapiserverdefault_storage_factory_buildergo69) `:69`


</details>


[function] name: Complete file: pkg/kubeapiserver/default_storage_factory_builder.go:109 returns_error: нет description: Complete completes the StorageFactoryConfig with provided etcdOptions returning completedStorageFactoryConfig.
This meth


### Complete (pkg/kubeapiserver/default_storage_factory_builder.go:109)


Complete completes the StorageFactoryConfig with provided etcdOptions returning completedStorageFactoryConfig.
This method mutates the receiver (StorageFactoryConfig).  It must never mutate the inputs.


```go
func (c *StorageFactoryConfig) Complete((etcdOptions *serveroptions.EtcdOptions)) (etcdOptions *serveroptions.EtcdOptions)
```


**Тип запроса:** serveroptions.EtcdOptions


```json
{
  "StorageConfig": {},
  "EncryptionProviderConfigFilepath": "string",
  "EncryptionProviderConfigAutomaticReload": false,
  "EtcdServersOverrides": [],
  "DefaultStorageMediaType": "string",
  "DeleteCollectionWorkers": 0,
  "EnableGarbageCollection": false,
  "EnableWatchCache": false,
  "DefaultWatchCacheSize": 0,
  "WatchCacheSizes": [],
  "SkipHealthEndpoints": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/options/etcd.go`


**Тип ответа:** etcdOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** serveroptions.EtcdOptions


```json
{
  "StorageConfig": {},
  "EncryptionProviderConfigFilepath": "string",
  "EncryptionProviderConfigAutomaticReload": false,
  "EtcdServersOverrides": [],
  "DefaultStorageMediaType": "string",
  "DeleteCollectionWorkers": 0,
  "EnableGarbageCollection": false,
  "EnableWatchCache": false,
  "DefaultWatchCacheSize": 0,
  "WatchCacheSizes": [],
  "SkipHealthEndpoints": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/options/etcd.go`


📍 *Расположение:* `pkg/kubeapiserver/default_storage_factory_builder.go:109`



---


[function] name: DefaultWatchCacheSizes file: pkg/kubeapiserver/default_storage_factory_builder.go:56 returns_error: нет description: DefaultWatchCacheSizes defines default resources for which watchcache
should be disabled.


### DefaultWatchCacheSizes (pkg/kubeapiserver/default_storage_factory_builder.go:56)


DefaultWatchCacheSizes defines default resources for which watchcache
should be disabled.


```go
func DefaultWatchCacheSizes(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/default_storage_factory_builder.go:56`



---


[function] name: New file: pkg/kubeapiserver/default_storage_factory_builder.go:125 returns_error: да description: New returns a new storage factory created from the completed storage factory configuration.


### New (pkg/kubeapiserver/default_storage_factory_builder.go:125)


New returns a new storage factory created from the completed storage factory configuration.


```go
func (c *completedStorageFactoryConfig) New((*serverstorage.DefaultStorageFactory, error)) (*serverstorage.DefaultStorageFactory, error)
```


**Тип запроса:** serverstorage.DefaultStorageFactory


```json
{
  "StorageConfig": {},
  "Overrides": {},
  "DefaultResourcePrefixes": {},
  "DefaultMediaType": "string",
  "DefaultSerializer": {},
  "ResourceEncodingConfig": {},
  "APIResourceConfigSource": {},
  "newStorageCodecFn": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/storage/storage_factory.go`


**Тип ответа:** serverstorage.DefaultStorageFactory


```json
{
  "StorageConfig": {},
  "Overrides": {},
  "DefaultResourcePrefixes": {},
  "DefaultMediaType": "string",
  "DefaultSerializer": {},
  "ResourceEncodingConfig": {},
  "APIResourceConfigSource": {},
  "newStorageCodecFn": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/storage/storage_factory.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*serverstorage.DefaultStorageFactory`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/default_storage_factory_builder.go:125`



---


[function] name: NewStorageFactoryConfig file: pkg/kubeapiserver/default_storage_factory_builder.go:64 returns_error: нет description: NewStorageFactoryConfig returns a new StorageFactoryConfig set up with necessary resource overrides.


### NewStorageFactoryConfig (pkg/kubeapiserver/default_storage_factory_builder.go:64)


NewStorageFactoryConfig returns a new StorageFactoryConfig set up with necessary resource overrides.


```go
func NewStorageFactoryConfig(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/default_storage_factory_builder.go:64`



---


[function] name: NewStorageFactoryConfigEffectiveVersion file: pkg/kubeapiserver/default_storage_factory_builder.go:69 returns_error: нет description: NewStorageFactoryConfigEffectiveVersion returns a new StorageFactoryConfig set up with necessary resource overrides for 


### NewStorageFactoryConfigEffectiveVersion (pkg/kubeapiserver/default_storage_factory_builder.go:69)


NewStorageFactoryConfigEffectiveVersion returns a new StorageFactoryConfig set up with necessary resource overrides for a given EffectiveVersion.


```go
func NewStorageFactoryConfigEffectiveVersion((effectiveVersion basecompatibility.EffectiveVersion)) (effectiveVersion basecompatibility.EffectiveVersion)
```


**Тип ответа:** effectiveVersion


```json
{
  "useDefaultBuildBinaryVersion": {},
  "binaryVersion": {},
  "emulationVersion": {},
  "minCompatibilityVersion": {},
  "emulationVersionFloor": null,
  "minCompatibilityVersionFloor": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/compatibility/version.go`


**Тип ответа:** basecompatibility.EffectiveVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/kubeapiserver/default_storage_factory_builder.go:69`




## pkg/kubeapiserver/options/admission.go


📄 Исходный файл: `pkg/kubeapiserver/options/admission.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AddFlags](#addflags-pkgkubeapiserveroptionsadmissiongo71) `:71`

- 🔗 [ApplyTo](#applyto-pkgkubeapiserveroptionsadmissiongo115) `:115`

- 🔗 [NewAdmissionOptions](#newadmissionoptions-pkgkubeapiserveroptionsadmissiongo56) `:56`

- 🔗 [Validate](#validate-pkgkubeapiserveroptionsadmissiongo91) `:91`

- 🔗 [computePluginNames](#computepluginnames-pkgkubeapiserveroptionsadmissiongo137) `:137`


</details>


[function] name: AddFlags file: pkg/kubeapiserver/options/admission.go:71 returns_error: нет description: AddFlags adds flags related to admission for kube-apiserver to the specified FlagSet


### AddFlags (pkg/kubeapiserver/options/admission.go:71)


AddFlags adds flags related to admission for kube-apiserver to the specified FlagSet


```go
func (a *AdmissionOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `pkg/kubeapiserver/options/admission.go:71`



---


[function] name: ApplyTo file: pkg/kubeapiserver/options/admission.go:115 returns_error: нет description: ApplyTo adds the admission chain to the server configuration.
Kube-apiserver just call generic AdmissionOptions.ApplyTo.


### ApplyTo (pkg/kubeapiserver/options/admission.go:115)


ApplyTo adds the admission chain to the server configuration.
Kube-apiserver just call generic AdmissionOptions.ApplyTo.


```go
func (a *AdmissionOptions) ApplyTo((
	c *server.Config,
	informers informers.SharedInformerFactory,
	kubeClient kubernetes.Interface,
	dynamicClient dynamic.Interface,
	features featuregate.FeatureGate,
	effectiveVersion compatibility.EffectiveVersion,
	pluginInitializers ...admission.PluginInitializer,
)) (
	c *server.Config,
	informers informers.SharedInformerFactory,
	kubeClient kubernetes.Interface,
	dynamicClient dynamic.Interface,
	features featuregate.FeatureGate,
	effectiveVersion compatibility.EffectiveVersion,
	pluginInitializers ...admission.PluginInitializer,
)
```


**Тип запроса:** server.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** c


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


**Тип ответа:** server.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** informers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** informers.SharedInformerFactory


```json
{
  "client": {},
  "defaultResync": {},
  "namespace": "string",
  "lock": {},
  "informers": {},
  "startedInformers": {},
  "tweakListOptions": {},
  "wg": {},
  "shuttingDown": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/dynamicinformer/informer.go`


**Тип ответа:** kubeClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** dynamicClient


```json
{
  "logger": {},
  "clientCert": null,
  "certMtx": {},
  "reload": {},
  "connDialer": null,
  "queue": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/cert_rotation.go`


**Тип ответа:** dynamic.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** features


```json
{
  "cpuHardcapping": false
}
```


*Определено в:* `pkg/kubelet/cm/container_manager_linux.go`


**Тип ответа:** featuregate.FeatureGate


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** effectiveVersion


```json
{
  "useDefaultBuildBinaryVersion": {},
  "binaryVersion": {},
  "emulationVersion": {},
  "minCompatibilityVersion": {},
  "emulationVersionFloor": null,
  "minCompatibilityVersionFloor": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/compatibility/version.go`


**Тип ответа:** compatibility.EffectiveVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pluginInitializers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** admission.PluginInitializer


```json
{
  "quotaConfiguration": {},
  "excludedAdmissionResources": []
}
```


*Определено в:* `pkg/controlplane/apiserver/admission/initializer.go`


📍 *Расположение:* `pkg/kubeapiserver/options/admission.go:115`



---


[function] name: NewAdmissionOptions file: pkg/kubeapiserver/options/admission.go:56 returns_error: нет description: NewAdmissionOptions creates a new instance of AdmissionOptions
Note:

In addition it calls RegisterAllAdmissionPlugins t


### NewAdmissionOptions (pkg/kubeapiserver/options/admission.go:56)


NewAdmissionOptions creates a new instance of AdmissionOptions
Note:

In addition it calls RegisterAllAdmissionPlugins to register
all kube-apiserver admission plugins.

Provides the list of RecommendedPluginOrder that holds sane values
that can be used by servers that don't care about admission chain.
Servers that do care can overwrite/append that field after creation.


```go
func NewAdmissionOptions(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/admission.go:56`



---


[function] name: Validate file: pkg/kubeapiserver/options/admission.go:91 returns_error: нет description: Validate verifies flags passed to kube-apiserver AdmissionOptions.
Kube-apiserver verifies PluginNames and then call gen


### Validate (pkg/kubeapiserver/options/admission.go:91)


Validate verifies flags passed to kube-apiserver AdmissionOptions.
Kube-apiserver verifies PluginNames and then call generic AdmissionOptions.Validate.


```go
func (a *AdmissionOptions) Validate(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/admission.go:91`



---


[function] name: computePluginNames file: pkg/kubeapiserver/options/admission.go:137 returns_error: нет description: explicitly disable all plugins that are not in the enabled list


### computePluginNames (pkg/kubeapiserver/options/admission.go:137)


explicitly disable all plugins that are not in the enabled list


```go
func computePluginNames((enabled []string, disabled []string)) (enabled []string, disabled []string)
```


**Тип ответа:** enabled


```json
{
  "value": "string",
  "register": false
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/generators/deepcopy.go`


**Тип ответа:** disabled


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/kubeapiserver/options/admission.go:137`




## pkg/kubeapiserver/options/authentication.go


📄 Исходный файл: `pkg/kubeapiserver/options/authentication.go`


<details open>
<summary><b>Функции в этом файле (21)</b></summary>


- 🔗 [AddFlags](#addflags-pkgkubeapiserveroptionsauthenticationgo341) `:341`

- 🔗 [ApplyAuthorization](#applyauthorization-pkgkubeapiserveroptionsauthenticationgo833) `:833`

- 🔗 [ApplyTo](#applyto-pkgkubeapiserveroptionsauthenticationgo672) `:672`

- 🔗 [NewBuiltInAuthenticationOptions](#newbuiltinauthenticationoptions-pkgkubeapiserveroptionsauthenticationgo166) `:166`

- 🔗 [ToAuthenticationConfig](#toauthenticationconfig-pkgkubeapiserveroptionsauthenticationgo492) `:492`

- 🔗 [Validate](#validate-pkgkubeapiserveroptionsauthenticationgo249) `:249`

- 🔗 [WithAll](#withall-pkgkubeapiserveroptionsauthenticationgo174) `:174`

- 🔗 [WithAnonymous](#withanonymous-pkgkubeapiserveroptionsauthenticationgo187) `:187`

- 🔗 [WithBootstrapToken](#withbootstraptoken-pkgkubeapiserveroptionsauthenticationgo195) `:195`

- 🔗 [WithClientCert](#withclientcert-pkgkubeapiserveroptionsauthenticationgo201) `:201`

- 🔗 [WithOIDC](#withoidc-pkgkubeapiserveroptionsauthenticationgo207) `:207`

- 🔗 [WithRequestHeader](#withrequestheader-pkgkubeapiserveroptionsauthenticationgo216) `:216`

- 🔗 [WithServiceAccounts](#withserviceaccounts-pkgkubeapiserveroptionsauthenticationgo222) `:222`

- 🔗 [WithTokenFile](#withtokenfile-pkgkubeapiserveroptionsauthenticationgo233) `:233`

- 🔗 [WithWebHook](#withwebhook-pkgkubeapiserveroptionsauthenticationgo239) `:239`

- 🔗 [certificatesOverlap](#certificatesoverlap-pkgkubeapiserveroptionsauthenticationgo329) `:329`

- 🔗 [init](#init-pkgkubeapiserveroptionsauthenticationgo883) `:883`

- 🔗 [loadAuthenticationConfig](#loadauthenticationconfig-pkgkubeapiserveroptionsauthenticationgo888) `:888`

- 🔗 [loadAuthenticationConfigFromData](#loadauthenticationconfigfromdata-pkgkubeapiserveroptionsauthenticationgo902) `:902`

- 🔗 [trackProvidedFlag](#trackprovidedflag-pkgkubeapiserveroptionsauthenticationgo846) `:846`

- 🔗 [validateOIDCOptions](#validateoidcoptions-pkgkubeapiserveroptionsauthenticationgo851) `:851`


</details>


[function] name: AddFlags file: pkg/kubeapiserver/options/authentication.go:341 returns_error: нет description: AddFlags returns flags of authentication for a API Server


### AddFlags (pkg/kubeapiserver/options/authentication.go:341)


AddFlags returns flags of authentication for a API Server


```go
func (o *BuiltInAuthenticationOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:341`



---


[function] name: ApplyAuthorization file: pkg/kubeapiserver/options/authentication.go:833 returns_error: нет description: ApplyAuthorization will conditionally modify the authentication options based on the authorization options


### ApplyAuthorization (pkg/kubeapiserver/options/authentication.go:833)


ApplyAuthorization will conditionally modify the authentication options based on the authorization options


```go
func (o *BuiltInAuthenticationOptions) ApplyAuthorization((authorization *BuiltInAuthorizationOptions)) (authorization *BuiltInAuthorizationOptions)
```


**Тип запроса:** BuiltInAuthorizationOptions


```json
{
  "Modes": [],
  "PolicyFile": "string",
  "WebhookConfigFile": "string",
  "WebhookVersion": "string",
  "WebhookCacheAuthorizedTTL": {},
  "WebhookCacheUnauthorizedTTL": {},
  "WebhookRetryBackoff": null,
  "AuthorizationConfigurationFile": "string",
  "AreLegacyFlagsSet": {}
}
```


*Определено в:* `pkg/kubeapiserver/options/authorization.go`


**Тип ответа:** authorization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BuiltInAuthorizationOptions


```json
{
  "Modes": [],
  "PolicyFile": "string",
  "WebhookConfigFile": "string",
  "WebhookVersion": "string",
  "WebhookCacheAuthorizedTTL": {},
  "WebhookCacheUnauthorizedTTL": {},
  "WebhookRetryBackoff": null,
  "AuthorizationConfigurationFile": "string",
  "AreLegacyFlagsSet": {}
}
```


*Определено в:* `pkg/kubeapiserver/options/authorization.go`


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:833`



---


[function] name: ApplyTo file: pkg/kubeapiserver/options/authentication.go:672 returns_error: нет description: ApplyTo requires already applied OpenAPIConfig and EgressSelector if present.
The input context controls the lifecycle o


### ApplyTo (pkg/kubeapiserver/options/authentication.go:672)


ApplyTo requires already applied OpenAPIConfig and EgressSelector if present.
The input context controls the lifecycle of background goroutines started to reload the authentication config file.


```go
func (o *BuiltInAuthenticationOptions) ApplyTo((
	ctx context.Context,
	authInfo *genericapiserver.AuthenticationInfo,
	secureServing *genericapiserver.SecureServingInfo,
	egressSelector *egressselector.EgressSelector,
	openAPIConfig *openapicommon.Config,
	openAPIV3Config *openapicommon.OpenAPIV3Config,
	extclient kubernetes.Interface,
	versionedInformer informers.SharedInformerFactory,
	apiServerID string)) (
	ctx context.Context,
	authInfo *genericapiserver.AuthenticationInfo,
	secureServing *genericapiserver.SecureServingInfo,
	egressSelector *egressselector.EgressSelector,
	openAPIConfig *openapicommon.Config,
	openAPIV3Config *openapicommon.OpenAPIV3Config,
	extclient kubernetes.Interface,
	versionedInformer informers.SharedInformerFactory,
	apiServerID string)
```


**Тип запроса:** genericapiserver.AuthenticationInfo


```json
{
  "APIAudiences": {},
  "Authenticator": {},
  "RequestHeaderConfig": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/config.go`


**Тип запроса:** genericapiserver.SecureServingInfo


```json
{
  "Listener": {},
  "Cert": {},
  "SNICerts": [],
  "ClientCA": {},
  "MinTLSVersion": 0,
  "CipherSuites": [],
  "HTTP2MaxStreamsPerConnection": 0,
  "DisableHTTP2": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/config.go`


**Тип запроса:** egressselector.EgressSelector


```json
{
  "egressToDialer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/egressselector/egress_selector.go`


**Тип запроса:** openapicommon.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип запроса:** openapicommon.OpenAPIV3Config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** authInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genericapiserver.AuthenticationInfo


```json
{
  "APIAudiences": {},
  "Authenticator": {},
  "RequestHeaderConfig": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/config.go`


**Тип ответа:** secureServing


```json
{
  "Listener": {},
  "Name": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/deprecated_insecure_serving.go`


**Тип ответа:** genericapiserver.SecureServingInfo


```json
{
  "Listener": {},
  "Cert": {},
  "SNICerts": [],
  "ClientCA": {},
  "MinTLSVersion": 0,
  "CipherSuites": [],
  "HTTP2MaxStreamsPerConnection": 0,
  "DisableHTTP2": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/config.go`


**Тип ответа:** egressSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** egressselector.EgressSelector


```json
{
  "egressToDialer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/egressselector/egress_selector.go`


**Тип ответа:** openAPIConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** openapicommon.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** openAPIV3Config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** openapicommon.OpenAPIV3Config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** extclient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** versionedInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** informers.SharedInformerFactory


```json
{
  "client": {},
  "defaultResync": {},
  "namespace": "string",
  "lock": {},
  "informers": {},
  "startedInformers": {},
  "tweakListOptions": {},
  "wg": {},
  "shuttingDown": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/dynamicinformer/informer.go`


**Тип ответа:** apiServerID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:672`



---


[function] name: NewBuiltInAuthenticationOptions file: pkg/kubeapiserver/options/authentication.go:166 returns_error: нет description: NewBuiltInAuthenticationOptions create a new BuiltInAuthenticationOptions, just set default token cache TTL


### NewBuiltInAuthenticationOptions (pkg/kubeapiserver/options/authentication.go:166)


NewBuiltInAuthenticationOptions create a new BuiltInAuthenticationOptions, just set default token cache TTL


```go
func NewBuiltInAuthenticationOptions(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:166`



---


[function] name: ToAuthenticationConfig file: pkg/kubeapiserver/options/authentication.go:492 returns_error: да description: ToAuthenticationConfig convert BuiltInAuthenticationOptions to kubeauthenticator.Config. Returns
an empty config if o is


### ToAuthenticationConfig (pkg/kubeapiserver/options/authentication.go:492)


ToAuthenticationConfig convert BuiltInAuthenticationOptions to kubeauthenticator.Config. Returns
an empty config if o is nil.


```go
func (o *BuiltInAuthenticationOptions) ToAuthenticationConfig((kubeauthenticator.Config, error)) (kubeauthenticator.Config, error)
```


**Тип ответа:** kubeauthenticator.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `kubeauthenticator.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:492`



---


[function] name: Validate file: pkg/kubeapiserver/options/authentication.go:249 returns_error: нет description: Validate checks invalid config combination


### Validate (pkg/kubeapiserver/options/authentication.go:249)


Validate checks invalid config combination


```go
func (o *BuiltInAuthenticationOptions) Validate(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:249`



---


[function] name: WithAll file: pkg/kubeapiserver/options/authentication.go:174 returns_error: нет description: WithAll set default value for every build-in authentication option


### WithAll (pkg/kubeapiserver/options/authentication.go:174)


WithAll set default value for every build-in authentication option


```go
func (o *BuiltInAuthenticationOptions) WithAll(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:174`



---


[function] name: WithAnonymous file: pkg/kubeapiserver/options/authentication.go:187 returns_error: нет description: WithAnonymous set default value for anonymous authentication


### WithAnonymous (pkg/kubeapiserver/options/authentication.go:187)


WithAnonymous set default value for anonymous authentication


```go
func (o *BuiltInAuthenticationOptions) WithAnonymous(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:187`



---


[function] name: WithBootstrapToken file: pkg/kubeapiserver/options/authentication.go:195 returns_error: нет description: WithBootstrapToken set default value for bootstrap token authentication


### WithBootstrapToken (pkg/kubeapiserver/options/authentication.go:195)


WithBootstrapToken set default value for bootstrap token authentication


```go
func (o *BuiltInAuthenticationOptions) WithBootstrapToken(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:195`



---


[function] name: WithClientCert file: pkg/kubeapiserver/options/authentication.go:201 returns_error: нет description: WithClientCert set default value for client cert


### WithClientCert (pkg/kubeapiserver/options/authentication.go:201)


WithClientCert set default value for client cert


```go
func (o *BuiltInAuthenticationOptions) WithClientCert(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:201`



---


[function] name: WithOIDC file: pkg/kubeapiserver/options/authentication.go:207 returns_error: нет description: WithOIDC set default value for OIDC authentication


### WithOIDC (pkg/kubeapiserver/options/authentication.go:207)


WithOIDC set default value for OIDC authentication


```go
func (o *BuiltInAuthenticationOptions) WithOIDC(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:207`



---


[function] name: WithRequestHeader file: pkg/kubeapiserver/options/authentication.go:216 returns_error: нет description: WithRequestHeader set default value for request header authentication


### WithRequestHeader (pkg/kubeapiserver/options/authentication.go:216)


WithRequestHeader set default value for request header authentication


```go
func (o *BuiltInAuthenticationOptions) WithRequestHeader(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:216`



---


[function] name: WithServiceAccounts file: pkg/kubeapiserver/options/authentication.go:222 returns_error: нет description: WithServiceAccounts set default value for service account authentication


### WithServiceAccounts (pkg/kubeapiserver/options/authentication.go:222)


WithServiceAccounts set default value for service account authentication


```go
func (o *BuiltInAuthenticationOptions) WithServiceAccounts(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:222`



---


[function] name: WithTokenFile file: pkg/kubeapiserver/options/authentication.go:233 returns_error: нет description: WithTokenFile set default value for token file authentication


### WithTokenFile (pkg/kubeapiserver/options/authentication.go:233)


WithTokenFile set default value for token file authentication


```go
func (o *BuiltInAuthenticationOptions) WithTokenFile(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:233`



---


[function] name: WithWebHook file: pkg/kubeapiserver/options/authentication.go:239 returns_error: нет description: WithWebHook set default value for web hook authentication


### WithWebHook (pkg/kubeapiserver/options/authentication.go:239)


WithWebHook set default value for web hook authentication


```go
func (o *BuiltInAuthenticationOptions) WithWebHook(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:239`



---


[function] name: certificatesOverlap file: pkg/kubeapiserver/options/authentication.go:329 returns_error: нет description: certificatesOverlap returns true when there's at least one identical
certificate in the two certificate bundles


### certificatesOverlap (pkg/kubeapiserver/options/authentication.go:329)


certificatesOverlap returns true when there's at least one identical
certificate in the two certificate bundles


```go
func certificatesOverlap((a, b []*x509.Certificate)) (a, b []*x509.Certificate)
```


**Тип запроса:** x509.Certificate


```json
{
  "Name": "string",
  "ExpirationDate": {},
  "ResidualTimeSeconds": 0,
  "ExternallyManaged": false,
  "CAName": "string",
  "Missing": false
}
```


*Определено в:* `cmd/kubeadm/app/apis/output/v1alpha3/types.go`


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


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** x509.Certificate


```json
{
  "Name": "string",
  "ExpirationDate": {},
  "ResidualTimeSeconds": 0,
  "ExternallyManaged": false,
  "CAName": "string",
  "Missing": false
}
```


*Определено в:* `cmd/kubeadm/app/apis/output/v1alpha3/types.go`


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:329`



---


[function] name: init file: pkg/kubeapiserver/options/authentication.go:883 returns_error: нет description: —


### init (pkg/kubeapiserver/options/authentication.go:883)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:883`



---


[function] name: loadAuthenticationConfig file: pkg/kubeapiserver/options/authentication.go:888 returns_error: да description: loadAuthenticationConfig parses the authentication configuration from the given file and returns it and the file's conte


### loadAuthenticationConfig (pkg/kubeapiserver/options/authentication.go:888)


loadAuthenticationConfig parses the authentication configuration from the given file and returns it and the file's contents.


```go
func loadAuthenticationConfig((*apiserver.AuthenticationConfiguration, string, error)) (*apiserver.AuthenticationConfiguration, string, error)
```


**Тип запроса:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Тип ответа:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apiserver.AuthenticationConfiguration`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:888`



---


[function] name: loadAuthenticationConfigFromData file: pkg/kubeapiserver/options/authentication.go:902 returns_error: да description: —


### loadAuthenticationConfigFromData (pkg/kubeapiserver/options/authentication.go:902)


loadAuthenticationConfigFromData is a function that performs operations based on the provided parameters and may return an error.


```go
func loadAuthenticationConfigFromData((*apiserver.AuthenticationConfiguration, error)) (*apiserver.AuthenticationConfiguration, error)
```


**Тип запроса:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Тип ответа:** apiserver.AuthenticationConfiguration


```json
{
  "JWT": [],
  "Anonymous": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apiserver.AuthenticationConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:902`



---


[function] name: trackProvidedFlag file: pkg/kubeapiserver/options/authentication.go:846 returns_error: нет description: —


### trackProvidedFlag (pkg/kubeapiserver/options/authentication.go:846)


trackProvidedFlag is a function that performs operations based on the provided parameters and returns (fs *pflag.FlagSet, flagName string, provided *bool).


```go
func trackProvidedFlag((fs *pflag.FlagSet, flagName string, provided *bool)) (fs *pflag.FlagSet, flagName string, provided *bool)
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


**Тип ответа:** flagName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** provided


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:846`



---


[function] name: validateOIDCOptions file: pkg/kubeapiserver/options/authentication.go:851 returns_error: нет description: —


### validateOIDCOptions (pkg/kubeapiserver/options/authentication.go:851)


validateOIDCOptions is a method that performs operations based on the provided parameters and returns ().


```go
func (o *BuiltInAuthenticationOptions) validateOIDCOptions(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authentication.go:851`




## pkg/kubeapiserver/options/authorization.go


📄 Исходный файл: `pkg/kubeapiserver/options/authorization.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [AddFlags](#addflags-pkgkubeapiserveroptionsauthorizationgo161) `:161`

- 🔗 [Complete](#complete-pkgkubeapiserveroptionsauthorizationgo85) `:85`

- 🔗 [NewBuiltInAuthorizationOptions](#newbuiltinauthorizationoptions-pkgkubeapiserveroptionsauthorizationgo74) `:74`

- 🔗 [ToAuthorizationConfig](#toauthorizationconfig-pkgkubeapiserveroptionsauthorizationgo208) `:208`

- 🔗 [Validate](#validate-pkgkubeapiserveroptionsauthorizationgo97) `:97`

- 🔗 [buildAuthorizationConfiguration](#buildauthorizationconfiguration-pkgkubeapiserveroptionsauthorizationgo253) `:253`


</details>


[function] name: AddFlags file: pkg/kubeapiserver/options/authorization.go:161 returns_error: нет description: AddFlags returns flags of authorization for a API Server


### AddFlags (pkg/kubeapiserver/options/authorization.go:161)


AddFlags returns flags of authorization for a API Server


```go
func (o *BuiltInAuthorizationOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `pkg/kubeapiserver/options/authorization.go:161`



---


[function] name: Complete file: pkg/kubeapiserver/options/authorization.go:85 returns_error: нет description: Complete modifies authorization options


### Complete (pkg/kubeapiserver/options/authorization.go:85)


Complete modifies authorization options


```go
func (o *BuiltInAuthorizationOptions) Complete(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authorization.go:85`



---


[function] name: NewBuiltInAuthorizationOptions file: pkg/kubeapiserver/options/authorization.go:74 returns_error: нет description: NewBuiltInAuthorizationOptions create a BuiltInAuthorizationOptions with default value


### NewBuiltInAuthorizationOptions (pkg/kubeapiserver/options/authorization.go:74)


NewBuiltInAuthorizationOptions create a BuiltInAuthorizationOptions with default value


```go
func NewBuiltInAuthorizationOptions(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authorization.go:74`



---


[function] name: ToAuthorizationConfig file: pkg/kubeapiserver/options/authorization.go:208 returns_error: да description: ToAuthorizationConfig convert BuiltInAuthorizationOptions to authorizer.Config


### ToAuthorizationConfig (pkg/kubeapiserver/options/authorization.go:208)


ToAuthorizationConfig convert BuiltInAuthorizationOptions to authorizer.Config


```go
func (o *BuiltInAuthorizationOptions) ToAuthorizationConfig((*authorizer.Config, error)) (*authorizer.Config, error)
```


**Тип запроса:** authorizer.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** authorizer.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*authorizer.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/options/authorization.go:208`



---


[function] name: Validate file: pkg/kubeapiserver/options/authorization.go:97 returns_error: нет description: Validate checks invalid config combination


### Validate (pkg/kubeapiserver/options/authorization.go:97)


Validate checks invalid config combination


```go
func (o *BuiltInAuthorizationOptions) Validate(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/authorization.go:97`



---


[function] name: buildAuthorizationConfiguration file: pkg/kubeapiserver/options/authorization.go:253 returns_error: да description: buildAuthorizationConfiguration converts existing flags to the AuthorizationConfiguration format


### buildAuthorizationConfiguration (pkg/kubeapiserver/options/authorization.go:253)


buildAuthorizationConfiguration converts existing flags to the AuthorizationConfiguration format


```go
func (o *BuiltInAuthorizationOptions) buildAuthorizationConfiguration((*authzconfig.AuthorizationConfiguration, error)) (*authzconfig.AuthorizationConfiguration, error)
```


**Тип запроса:** authzconfig.AuthorizationConfiguration


```json
{
  "Authorizers": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Тип ответа:** authzconfig.AuthorizationConfiguration


```json
{
  "Authorizers": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*authzconfig.AuthorizationConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubeapiserver/options/authorization.go:253`




## pkg/kubeapiserver/options/plugins.go


📄 Исходный файл: `pkg/kubeapiserver/options/plugins.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DefaultOffAdmissionPlugins](#defaultoffadmissionplugins-pkgkubeapiserveroptionspluginsgo158) `:158`

- 🔗 [RegisterAllAdmissionPlugins](#registeralladmissionplugins-pkgkubeapiserveroptionspluginsgo122) `:122`

- 🔗 [registerAllAdmissionPluginFlags](#registeralladmissionpluginflags-pkgkubeapiserveroptionspluginsgo116) `:116`


</details>


[function] name: DefaultOffAdmissionPlugins file: pkg/kubeapiserver/options/plugins.go:158 returns_error: нет description: DefaultOffAdmissionPlugins get admission plugins off by default for kube-apiserver.


### DefaultOffAdmissionPlugins (pkg/kubeapiserver/options/plugins.go:158)


DefaultOffAdmissionPlugins get admission plugins off by default for kube-apiserver.


```go
func DefaultOffAdmissionPlugins(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/plugins.go:158`



---


[function] name: RegisterAllAdmissionPlugins file: pkg/kubeapiserver/options/plugins.go:122 returns_error: нет description: RegisterAllAdmissionPlugins registers all admission plugins.
The order of registration is irrelevant, see AllOrderedPlug


### RegisterAllAdmissionPlugins (pkg/kubeapiserver/options/plugins.go:122)


RegisterAllAdmissionPlugins registers all admission plugins.
The order of registration is irrelevant, see AllOrderedPlugins for execution order.


```go
func RegisterAllAdmissionPlugins((plugins *admission.Plugins)) (plugins *admission.Plugins)
```


**Тип запроса:** admission.Plugins


```json
{
  "PreEnqueue": {},
  "QueueSort": {},
  "PreFilter": {},
  "Filter": {},
  "PostFilter": {},
  "PreScore": {},
  "Score": {},
  "Reserve": {},
  "Permit": {},
  "PreBind": {},
  "Bind": {},
  "PostBind": {},
  "MultiPoint": {}
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


**Тип ответа:** plugins


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** admission.Plugins


```json
{
  "PreEnqueue": {},
  "QueueSort": {},
  "PreFilter": {},
  "Filter": {},
  "PostFilter": {},
  "PreScore": {},
  "Score": {},
  "Reserve": {},
  "Permit": {},
  "PreBind": {},
  "Bind": {},
  "PostBind": {},
  "MultiPoint": {}
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


📍 *Расположение:* `pkg/kubeapiserver/options/plugins.go:122`



---


[function] name: registerAllAdmissionPluginFlags file: pkg/kubeapiserver/options/plugins.go:116 returns_error: нет description: registerAllAdmissionPluginFlags registers legacy CLI flag options for admission plugins.
No new plugins should use CLI f


### registerAllAdmissionPluginFlags (pkg/kubeapiserver/options/plugins.go:116)


registerAllAdmissionPluginFlags registers legacy CLI flag options for admission plugins.
No new plugins should use CLI flags to configure themselves.


```go
func registerAllAdmissionPluginFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `pkg/kubeapiserver/options/plugins.go:116`




## pkg/kubeapiserver/options/serving.go


📄 Исходный файл: `pkg/kubeapiserver/options/serving.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewSecureServingOptions](#newsecureservingoptions-pkgkubeapiserveroptionsservinggo27) `:27`


</details>


[function] name: NewSecureServingOptions file: pkg/kubeapiserver/options/serving.go:27 returns_error: нет description: NewSecureServingOptions gives default values for the kube-apiserver which are not the options wanted by
"normal" API ser


### NewSecureServingOptions (pkg/kubeapiserver/options/serving.go:27)


NewSecureServingOptions gives default values for the kube-apiserver which are not the options wanted by
"normal" API servers running on the platform


```go
func NewSecureServingOptions(()) ()
```


📍 *Расположение:* `pkg/kubeapiserver/options/serving.go:27`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_generated.md)

- [Следующая директория](pkg_kubectl.md)


---

