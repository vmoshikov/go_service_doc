---
title: "Функции: cmd/kube-apiserver"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/kube-apiserver
---


# Функции: cmd/kube-apiserver


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_importverifier.md)

- [Следующая директория](cmd_kube-controller-manager.md)


---


## Меню по файлам


- 📄 [cmd/kube-apiserver/apiserver.go](#cmdkube-apiserverapiservergo)

- 📄 [cmd/kube-apiserver/app/aggregator.go](#cmdkube-apiserverappaggregatorgo)

- 📄 [cmd/kube-apiserver/app/config.go](#cmdkube-apiserverappconfiggo)

- 📄 [cmd/kube-apiserver/app/options/completion.go](#cmdkube-apiserverappoptionscompletiongo)

- 📄 [cmd/kube-apiserver/app/options/options.go](#cmdkube-apiserverappoptionsoptionsgo)

- 📄 [cmd/kube-apiserver/app/options/validation.go](#cmdkube-apiserverappoptionsvalidationgo)

- 📄 [cmd/kube-apiserver/app/server.go](#cmdkube-apiserverappservergo)

- 📄 [cmd/kube-apiserver/app/testing/testserver.go](#cmdkube-apiserverapptestingtestservergo)


---


## cmd/kube-apiserver/apiserver.go


📄 Исходный файл: `cmd/kube-apiserver/apiserver.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdkube-apiserverapiservergo32) `:32`


</details>


[function] name: main file: cmd/kube-apiserver/apiserver.go:32 returns_error: нет description: —


### main (cmd/kube-apiserver/apiserver.go:32)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/kube-apiserver/apiserver.go:32`




## cmd/kube-apiserver/app/aggregator.go


📄 Исходный файл: `cmd/kube-apiserver/app/aggregator.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [merge](#merge-cmdkube-apiserverappaggregatorgo63) `:63`


</details>


[function] name: merge file: cmd/kube-apiserver/app/aggregator.go:63 returns_error: нет description: —


### merge (cmd/kube-apiserver/app/aggregator.go:63)


merge is a function that performs operations based on the provided parameters and returns (a, b map[schema.GroupVersion]controlplaneapiserver.APIServicePriority).


```go
func merge((a, b map[schema.GroupVersion]controlplaneapiserver.APIServicePriority)) (a, b map[schema.GroupVersion]controlplaneapiserver.APIServicePriority)
```


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


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** schema.GroupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** controlplaneapiserver.APIServicePriority


```json
{
  "Group": 0,
  "Version": 0
}
```


*Определено в:* `pkg/controlplane/apiserver/aggregator.go`


📍 *Расположение:* `cmd/kube-apiserver/app/aggregator.go:63`




## cmd/kube-apiserver/app/config.go


📄 Исходный файл: `cmd/kube-apiserver/app/config.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Complete](#complete-cmdkube-apiserverappconfiggo61) `:61`

- 🔗 [NewConfig](#newconfig-cmdkube-apiserverappconfiggo74) `:74`


</details>


[function] name: Complete file: cmd/kube-apiserver/app/config.go:61 returns_error: да description: —


### Complete (cmd/kube-apiserver/app/config.go:61)


Complete is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *Config) Complete((CompletedConfig, error)) (CompletedConfig, error)
```


**Тип ответа:** CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CompletedConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/config.go:61`



---


[function] name: NewConfig file: cmd/kube-apiserver/app/config.go:74 returns_error: да description: NewConfig creates all the resources for running kube-apiserver, but runs none of them.


### NewConfig (cmd/kube-apiserver/app/config.go:74)


NewConfig creates all the resources for running kube-apiserver, but runs none of them.


```go
func NewConfig((*Config, error)) (*Config, error)
```


**Тип запроса:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/config.go:74`




## cmd/kube-apiserver/app/options/completion.go


📄 Исходный файл: `cmd/kube-apiserver/app/options/completion.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Complete](#complete-cmdkube-apiserverappoptionscompletiongo47) `:47`

- 🔗 [getServiceIPAndRanges](#getserviceipandranges-cmdkube-apiserverappoptionscompletiongo94) `:94`


</details>


[function] name: Complete file: cmd/kube-apiserver/app/options/completion.go:47 returns_error: да description: Complete set default ServerRunOptions.
Should be called after kube-apiserver flags parsed.


### Complete (cmd/kube-apiserver/app/options/completion.go:47)


Complete set default ServerRunOptions.
Should be called after kube-apiserver flags parsed.


```go
func (s *ServerRunOptions) Complete((CompletedOptions, error)) (CompletedOptions, error)
```


**Тип ответа:** CompletedOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CompletedOptions`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/options/completion.go:47`



---


[function] name: getServiceIPAndRanges file: cmd/kube-apiserver/app/options/completion.go:94 returns_error: да description: —


### getServiceIPAndRanges (cmd/kube-apiserver/app/options/completion.go:94)


getServiceIPAndRanges is a function that performs operations based on the provided parameters and may return an error.


```go
func getServiceIPAndRanges((net.IP, net.IPNet, net.IPNet, error)) (net.IP, net.IPNet, net.IPNet, error)
```


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `net.IP`, `net.IPNet`, `net.IPNet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/options/completion.go:94`




## cmd/kube-apiserver/app/options/options.go


📄 Исходный файл: `cmd/kube-apiserver/app/options/options.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Flags](#flags-cmdkube-apiserverappoptionsoptionsgo100) `:100`

- 🔗 [NewServerRunOptions](#newserverrunoptions-cmdkube-apiserverappoptionsoptionsgo66) `:66`


</details>


[function] name: Flags file: cmd/kube-apiserver/app/options/options.go:100 returns_error: нет description: Flags returns flags for a specific APIServer by section name


### Flags (cmd/kube-apiserver/app/options/options.go:100)


Flags returns flags for a specific APIServer by section name


```go
func (s *ServerRunOptions) Flags((fss cliflag.NamedFlagSets)) (fss cliflag.NamedFlagSets)
```


**Тип ответа:** fss


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cliflag.NamedFlagSets


```json
{
  "Order": [],
  "FlagSets": {},
  "NormalizeNameFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/cli/flag/sectioned.go`


📍 *Расположение:* `cmd/kube-apiserver/app/options/options.go:100`



---


[function] name: NewServerRunOptions file: cmd/kube-apiserver/app/options/options.go:66 returns_error: нет description: NewServerRunOptions creates and returns ServerRunOptions according to the given featureGate and effectiveVersion of the 


### NewServerRunOptions (cmd/kube-apiserver/app/options/options.go:66)


NewServerRunOptions creates and returns ServerRunOptions according to the given featureGate and effectiveVersion of the server binary to run.


```go
func NewServerRunOptions(()) ()
```


📍 *Расположение:* `cmd/kube-apiserver/app/options/options.go:66`




## cmd/kube-apiserver/app/options/validation.go


📄 Исходный файл: `cmd/kube-apiserver/app/options/validation.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Validate](#validate-cmdkube-apiserverappoptionsvalidationgo131) `:131`

- 🔗 [validateClusterIPFlags](#validateclusteripflags-cmdkube-apiserverappoptionsvalidationgo36) `:36`

- 🔗 [validateMaxCIDRRange](#validatemaxcidrrange-cmdkube-apiserverappoptionsvalidationgo86) `:86`

- 🔗 [validatePublicIPServiceClusterIPRangeIPFamilies](#validatepublicipserviceclusteriprangeipfamilies-cmdkube-apiserverappoptionsvalidationgo111) `:111`

- 🔗 [validateServiceNodePort](#validateservicenodeport-cmdkube-apiserverappoptionsvalidationgo98) `:98`


</details>


[function] name: Validate file: cmd/kube-apiserver/app/options/validation.go:131 returns_error: нет description: Validate checks ServerRunOptions and return a slice of found errs.


### Validate (cmd/kube-apiserver/app/options/validation.go:131)


Validate checks ServerRunOptions and return a slice of found errs.


```go
func (s CompletedOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-apiserver/app/options/validation.go:131`



---


[function] name: validateClusterIPFlags file: cmd/kube-apiserver/app/options/validation.go:36 returns_error: нет description: TODO: Longer term we should read this from some config store, rather than a flag.
validateClusterIPFlags is expected to 


### validateClusterIPFlags (cmd/kube-apiserver/app/options/validation.go:36)


TODO: Longer term we should read this from some config store, rather than a flag.
validateClusterIPFlags is expected to be called after Complete()


```go
func validateClusterIPFlags((options Extra)) (options Extra)
```


**Тип ответа:** options


```json
{
  "SinceTime": "2023-01-01T00:00:00Z",
  "UntilTime": "2023-01-01T00:00:00Z",
  "TailLines": 0,
  "Boot": 0,
  "Pattern": "string"
}
```


*Определено в:* `pkg/kubelet/kubelet_server_journal.go`


**Тип ответа:** Extra


```json
{
  "ClusterAuthenticationInfo": {},
  "APIResourceConfigSource": {},
  "StorageFactory": {},
  "EventTTL": {},
  "EnableLogsSupport": false,
  "ProxyTransport": null,
  "PeerProxy": {},
  "PeerEndpointReconcileInterval": {},
  "PeerEndpointLeaseReconciler": {},
  "PeerAdvertiseAddress": {},
  "ServiceAccountIssuer": {},
  "ServiceAccountMaxExpiration": {},
  "ServiceAccountExtendedMaxExpiration": {},
  "ExtendExpiration": false,
  "ServiceAccountIssuerURL": "string",
  "ServiceAccountJWKSURI": "string",
  "ServiceAccountPublicKeysGetter": {},
  "SystemNamespaces": [],
  "VersionedInformers": {},
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/config.go`


📍 *Расположение:* `cmd/kube-apiserver/app/options/validation.go:36`



---


[function] name: validateMaxCIDRRange file: cmd/kube-apiserver/app/options/validation.go:86 returns_error: нет description: —


### validateMaxCIDRRange (cmd/kube-apiserver/app/options/validation.go:86)


validateMaxCIDRRange is a function that performs operations based on the provided parameters and returns (cidr net.IPNet, maxCIDRBits int, cidrFlag string).


```go
func validateMaxCIDRRange((cidr net.IPNet, maxCIDRBits int, cidrFlag string)) (cidr net.IPNet, maxCIDRBits int, cidrFlag string)
```


**Тип ответа:** cidr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxCIDRBits


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cidrFlag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-apiserver/app/options/validation.go:86`



---


[function] name: validatePublicIPServiceClusterIPRangeIPFamilies file: cmd/kube-apiserver/app/options/validation.go:111 returns_error: нет description: —


### validatePublicIPServiceClusterIPRangeIPFamilies (cmd/kube-apiserver/app/options/validation.go:111)


validatePublicIPServiceClusterIPRangeIPFamilies is a function that performs operations based on the provided parameters and returns (extra Extra, generic genericoptions.ServerRunOptions).


```go
func validatePublicIPServiceClusterIPRangeIPFamilies((extra Extra, generic genericoptions.ServerRunOptions)) (extra Extra, generic genericoptions.ServerRunOptions)
```


**Тип ответа:** extra


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/unstructured.go`


**Тип ответа:** Extra


```json
{
  "ClusterAuthenticationInfo": {},
  "APIResourceConfigSource": {},
  "StorageFactory": {},
  "EventTTL": {},
  "EnableLogsSupport": false,
  "ProxyTransport": null,
  "PeerProxy": {},
  "PeerEndpointReconcileInterval": {},
  "PeerEndpointLeaseReconciler": {},
  "PeerAdvertiseAddress": {},
  "ServiceAccountIssuer": {},
  "ServiceAccountMaxExpiration": {},
  "ServiceAccountExtendedMaxExpiration": {},
  "ExtendExpiration": false,
  "ServiceAccountIssuerURL": "string",
  "ServiceAccountJWKSURI": "string",
  "ServiceAccountPublicKeysGetter": {},
  "SystemNamespaces": [],
  "VersionedInformers": {},
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/config.go`


**Тип ответа:** generic


```json
{
  "informer": {},
  "resource": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/generic.go`


**Тип ответа:** genericoptions.ServerRunOptions


```json
{
  "AdvertiseAddress": {},
  "CorsAllowedOriginList": [],
  "HSTSDirectives": [],
  "ExternalHost": "string",
  "MaxRequestsInFlight": 0,
  "MaxMutatingRequestsInFlight": 0,
  "RequestTimeout": {},
  "GoawayChance": 0.0,
  "LivezGracePeriod": {},
  "MinRequestTimeout": 0,
  "StorageInitializationTimeout": {},
  "ShutdownDelayDuration": {},
  "JSONPatchMaxCopyBytes": 0,
  "MaxRequestBodyBytes": 0,
  "ShutdownSendRetryAfter": false,
  "ShutdownWatchTerminationGracePeriod": {},
  "ComponentGlobalsRegistry": {},
  "ComponentName": "string",
  "EmulationForwardCompatible": false,
  "RuntimeConfigEmulationForwardCompatible": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/options/server_run_options.go`


📍 *Расположение:* `cmd/kube-apiserver/app/options/validation.go:111`



---


[function] name: validateServiceNodePort file: cmd/kube-apiserver/app/options/validation.go:98 returns_error: нет description: —


### validateServiceNodePort (cmd/kube-apiserver/app/options/validation.go:98)


validateServiceNodePort is a function that performs operations based on the provided parameters and returns (options Extra).


```go
func validateServiceNodePort((options Extra)) (options Extra)
```


**Тип ответа:** options


```json
{
  "SinceTime": "2023-01-01T00:00:00Z",
  "UntilTime": "2023-01-01T00:00:00Z",
  "TailLines": 0,
  "Boot": 0,
  "Pattern": "string"
}
```


*Определено в:* `pkg/kubelet/kubelet_server_journal.go`


**Тип ответа:** Extra


```json
{
  "ClusterAuthenticationInfo": {},
  "APIResourceConfigSource": {},
  "StorageFactory": {},
  "EventTTL": {},
  "EnableLogsSupport": false,
  "ProxyTransport": null,
  "PeerProxy": {},
  "PeerEndpointReconcileInterval": {},
  "PeerEndpointLeaseReconciler": {},
  "PeerAdvertiseAddress": {},
  "ServiceAccountIssuer": {},
  "ServiceAccountMaxExpiration": {},
  "ServiceAccountExtendedMaxExpiration": {},
  "ExtendExpiration": false,
  "ServiceAccountIssuerURL": "string",
  "ServiceAccountJWKSURI": "string",
  "ServiceAccountPublicKeysGetter": {},
  "SystemNamespaces": [],
  "VersionedInformers": {},
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/config.go`


📍 *Расположение:* `cmd/kube-apiserver/app/options/validation.go:98`




## cmd/kube-apiserver/app/server.go


📄 Исходный файл: `cmd/kube-apiserver/app/server.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [CreateKubeAPIServerConfig](#createkubeapiserverconfig-cmdkube-apiserverappservergo200) `:200`

- 🔗 [CreateServerChain](#createserverchain-cmdkube-apiserverappservergo176) `:176`

- 🔗 [NewAPIServerCommand](#newapiservercommand-cmdkube-apiserverappservergo70) `:70`

- 🔗 [Run](#run-cmdkube-apiserverappservergo148) `:148`

- 🔗 [SetServiceResolverForTests](#setserviceresolverfortests-cmdkube-apiserverappservergo271) `:271`

- 🔗 [buildServiceResolver](#buildserviceresolver-cmdkube-apiserverappservergo283) `:283`

- 🔗 [init](#init-cmdkube-apiserverappservergo65) `:65`


</details>


[function] name: CreateKubeAPIServerConfig file: cmd/kube-apiserver/app/server.go:200 returns_error: да description: CreateKubeAPIServerConfig creates all the resources for running the API server, but runs none of them


### CreateKubeAPIServerConfig (cmd/kube-apiserver/app/server.go:200)


CreateKubeAPIServerConfig creates all the resources for running the API server, but runs none of them


```go
func CreateKubeAPIServerConfig((
	*controlplane.Config,
	aggregatorapiserver.ServiceResolver,
	[]admission.PluginInitializer,
	error,
)) (
	*controlplane.Config,
	aggregatorapiserver.ServiceResolver,
	[]admission.PluginInitializer,
	error,
)
```


**Тип запроса:** controlplane.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** controlplane.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** aggregatorapiserver.ServiceResolver


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** admission.PluginInitializer


```json
{
  "quotaConfiguration": {},
  "excludedAdmissionResources": []
}
```


*Определено в:* `pkg/controlplane/apiserver/admission/initializer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*controlplane.Config`, `aggregatorapiserver.ServiceResolver`, `[]admission.PluginInitializer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/server.go:200`



---


[function] name: CreateServerChain file: cmd/kube-apiserver/app/server.go:176 returns_error: да description: CreateServerChain creates the apiservers connected via delegation.


### CreateServerChain (cmd/kube-apiserver/app/server.go:176)


CreateServerChain creates the apiservers connected via delegation.


```go
func CreateServerChain((*aggregatorapiserver.APIAggregator, error)) (*aggregatorapiserver.APIAggregator, error)
```


**Тип запроса:** aggregatorapiserver.APIAggregator


```json
{
  "GenericAPIServer": null,
  "APIRegistrationInformers": {},
  "delegateHandler": {},
  "proxyCurrentCertKeyContent": {},
  "proxyTransportDial": null,
  "proxyHandlers": {},
  "handledGroupVersions": {},
  "lister": {},
  "serviceResolver": {},
  "openAPIConfig": null,
  "openAPIV3Config": null,
  "openAPIAggregationController": null,
  "openAPIV3AggregationController": null,
  "discoveryAggregationController": {},
  "rejectForwardingRedirects": false,
  "tracerProvider": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/apiserver/apiserver.go`


**Тип ответа:** aggregatorapiserver.APIAggregator


```json
{
  "GenericAPIServer": null,
  "APIRegistrationInformers": {},
  "delegateHandler": {},
  "proxyCurrentCertKeyContent": {},
  "proxyTransportDial": null,
  "proxyHandlers": {},
  "handledGroupVersions": {},
  "lister": {},
  "serviceResolver": {},
  "openAPIConfig": null,
  "openAPIV3Config": null,
  "openAPIAggregationController": null,
  "openAPIV3AggregationController": null,
  "discoveryAggregationController": {},
  "rejectForwardingRedirects": false,
  "tracerProvider": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/apiserver/apiserver.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*aggregatorapiserver.APIAggregator`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/server.go:176`



---


[function] name: NewAPIServerCommand file: cmd/kube-apiserver/app/server.go:70 returns_error: нет description: NewAPIServerCommand creates a *cobra.Command object with default parameters


### NewAPIServerCommand (cmd/kube-apiserver/app/server.go:70)


NewAPIServerCommand creates a *cobra.Command object with default parameters


```go
func NewAPIServerCommand(()) ()
```


📍 *Расположение:* `cmd/kube-apiserver/app/server.go:70`



---


[function] name: Run file: cmd/kube-apiserver/app/server.go:148 returns_error: нет description: Run runs the specified APIServer.  This should never exit.


### Run (cmd/kube-apiserver/app/server.go:148)


Run runs the specified APIServer.  This should never exit.


```go
func Run((ctx context.Context, opts options.CompletedOptions)) (ctx context.Context, opts options.CompletedOptions)
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


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options.CompletedOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-apiserver/app/server.go:148`



---


[function] name: SetServiceResolverForTests file: cmd/kube-apiserver/app/server.go:271 returns_error: нет description: SetServiceResolverForTests allows the service resolver to be overridden during tests.
Tests using this function must run


### SetServiceResolverForTests (cmd/kube-apiserver/app/server.go:271)


SetServiceResolverForTests allows the service resolver to be overridden during tests.
Tests using this function must run serially as this function is not safe to call concurrently with server start.


```go
func SetServiceResolverForTests((resolver webhook.ServiceResolver)) (resolver webhook.ServiceResolver)
```


**Тип ответа:** resolver


```json
{
  "m": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/prometheus/restclient/metrics.go`


**Тип ответа:** webhook.ServiceResolver


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-apiserver/app/server.go:271`



---


[function] name: buildServiceResolver file: cmd/kube-apiserver/app/server.go:283 returns_error: да description: —


### buildServiceResolver (cmd/kube-apiserver/app/server.go:283)


buildServiceResolver is a function that performs operations based on the provided parameters and may return an error.


```go
func buildServiceResolver((webhook.ServiceResolver, error)) (webhook.ServiceResolver, error)
```


**Тип ответа:** webhook.ServiceResolver


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `webhook.ServiceResolver`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/server.go:283`



---


[function] name: init file: cmd/kube-apiserver/app/server.go:65 returns_error: нет description: —


### init (cmd/kube-apiserver/app/server.go:65)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kube-apiserver/app/server.go:65`




## cmd/kube-apiserver/app/testing/testserver.go


📄 Исходный файл: `cmd/kube-apiserver/app/testing/testserver.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [GetEtcdClients](#getetcdclients-cmdkube-apiserverapptestingtestservergo538) `:538`

- 🔗 [NewDefaultTestServerOptions](#newdefaulttestserveroptions-cmdkube-apiserverapptestingtestservergo144) `:144`

- 🔗 [StartTestServer](#starttestserver-cmdkube-apiserverapptestingtestservergo156) `:156`

- 🔗 [StartTestServerOrDie](#starttestserverordie-cmdkube-apiserverapptestingtestservergo577) `:577`

- 🔗 [createLocalhostListenerOnFreePort](#createlocalhostlisteneronfreeport-cmdkube-apiserverapptestingtestservergo587) `:587`

- 🔗 [init](#init-cmdkube-apiserverapptestingtestservergo74) `:74`

- 🔗 [pkgPath](#pkgpath-cmdkube-apiserverapptestingtestservergo610) `:610`


</details>


[function] name: GetEtcdClients file: cmd/kube-apiserver/app/testing/testserver.go:538 returns_error: да description: GetEtcdClients returns an initialized etcd clientv3.Client and clientv3.KV.


### GetEtcdClients (cmd/kube-apiserver/app/testing/testserver.go:538)


GetEtcdClients returns an initialized etcd clientv3.Client and clientv3.KV.


```go
func GetEtcdClients((*clientv3.Client, clientv3.KV, error)) (*clientv3.Client, clientv3.KV, error)
```


**Тип запроса:** clientv3.Client


```json
{
  "clientSet": {},
  "useAPI": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/client/client.go`


**Тип ответа:** clientv3.Client


```json
{
  "clientSet": {},
  "useAPI": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/client/client.go`


**Тип ответа:** clientv3.KV


```json
{
  "reads": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/testing/recorder.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*clientv3.Client`, `clientv3.KV`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/testing/testserver.go:538`



---


[function] name: NewDefaultTestServerOptions file: cmd/kube-apiserver/app/testing/testserver.go:144 returns_error: нет description: NewDefaultTestServerOptions Default options for TestServer instances


### NewDefaultTestServerOptions (cmd/kube-apiserver/app/testing/testserver.go:144)


NewDefaultTestServerOptions Default options for TestServer instances


```go
func NewDefaultTestServerOptions(()) ()
```


📍 *Расположение:* `cmd/kube-apiserver/app/testing/testserver.go:144`



---


[function] name: StartTestServer file: cmd/kube-apiserver/app/testing/testserver.go:156 returns_error: да description: StartTestServer starts a etcd server and kube-apiserver. A rest client config and a tear-down func,
and location of the 


### StartTestServer (cmd/kube-apiserver/app/testing/testserver.go:156)


StartTestServer starts a etcd server and kube-apiserver. A rest client config and a tear-down func,
and location of the tmpdir are returned.

Note: we return a tear-down func instead of a stop channel because the later will leak temporary
files that because Golang testing's call to os.Exit will not give a stop channel go routine
enough time to remove temporary files.


```go
func StartTestServer((result TestServer, err error)) (result TestServer, err error)
```


**Тип ответа:** result


```json
{
  "object": {},
  "err": {},
  "reason": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher.go`


**Тип ответа:** TestServer


```json
{
  "ClientConfig": null,
  "ServerOpts": null,
  "TearDownFn": {},
  "TmpDir": "string",
  "EtcdClient": null,
  "EtcdStoragePrefix": "string"
}
```


*Определено в:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go`


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


*Типы возврата:* `result TestServer`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/testing/testserver.go:156`



---


[function] name: StartTestServerOrDie file: cmd/kube-apiserver/app/testing/testserver.go:577 returns_error: нет description: StartTestServerOrDie calls StartTestServer t.Fatal if it does not succeed.


### StartTestServerOrDie (cmd/kube-apiserver/app/testing/testserver.go:577)


StartTestServerOrDie calls StartTestServer t.Fatal if it does not succeed.


```go
func StartTestServerOrDie((t testing.TB, instanceOptions *TestServerInstanceOptions, flags []string, storageConfig *storagebackend.Config)) (t testing.TB, instanceOptions *TestServerInstanceOptions, flags []string, storageConfig *storagebackend.Config)
```


**Тип запроса:** TestServerInstanceOptions


```json
{
  "SkipHealthzCheck": false
}
```


*Определено в:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go`


**Тип запроса:** storagebackend.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** t


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** testing.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** instanceOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestServerInstanceOptions


```json
{
  "SkipHealthzCheck": false
}
```


*Определено в:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go`


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** storageConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** storagebackend.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `cmd/kube-apiserver/app/testing/testserver.go:577`



---


[function] name: createLocalhostListenerOnFreePort file: cmd/kube-apiserver/app/testing/testserver.go:587 returns_error: да description: —


### createLocalhostListenerOnFreePort (cmd/kube-apiserver/app/testing/testserver.go:587)


createLocalhostListenerOnFreePort is a function that performs operations based on the provided parameters and may return an error.


```go
func createLocalhostListenerOnFreePort((net.Listener, int, error)) (net.Listener, int, error)
```


**Тип ответа:** net.Listener


```json
{
  "logger": {},
  "nextCh": {},
  "addCh": {},
  "done": {},
  "handler": {},
  "syncTracker": null,
  "upstreamHasSynced": {},
  "pendingNotifications": {},
  "requestedResyncPeriod": {},
  "resyncPeriod": {},
  "nextResync": {},
  "resyncLock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/shared_informer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `net.Listener`, `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/testing/testserver.go:587`



---


[function] name: init file: cmd/kube-apiserver/app/testing/testserver.go:74 returns_error: нет description: —


### init (cmd/kube-apiserver/app/testing/testserver.go:74)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kube-apiserver/app/testing/testserver.go:74`



---


[function] name: pkgPath file: cmd/kube-apiserver/app/testing/testserver.go:610 returns_error: да description: pkgPath returns the absolute file path to this package's directory. With go
test, we can just look at the runtime call s


### pkgPath (cmd/kube-apiserver/app/testing/testserver.go:610)


pkgPath returns the absolute file path to this package's directory. With go
test, we can just look at the runtime call stack. However, bazel compiles go
binaries with the -trimpath option so the simple approach fails however we
can consult environment variables to derive the path.

The approach taken here works for both go test and bazel on the assumption
that if and only if trimpath is passed, we are running under bazel.


```go
func pkgPath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-apiserver/app/testing/testserver.go:610`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_importverifier.md)

- [Следующая директория](cmd_kube-controller-manager.md)


---

