---
title: "Функции: pkg/controlplane"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/controlplane
---


# Функции: pkg/controlplane


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_controller.md)

- [Следующая директория](pkg_credentialprovider.md)


---


## Меню по файлам


- 📄 [pkg/controlplane/apiserver/admission/config.go](#pkgcontrolplaneapiserveradmissionconfiggo)

- 📄 [pkg/controlplane/apiserver/admission/initializer.go](#pkgcontrolplaneapiserveradmissioninitializergo)

- 📄 [pkg/controlplane/apiserver/aggregator.go](#pkgcontrolplaneapiserveraggregatorgo)

- 📄 [pkg/controlplane/apiserver/apiextensions.go](#pkgcontrolplaneapiserverapiextensionsgo)

- 📄 [pkg/controlplane/apiserver/apis.go](#pkgcontrolplaneapiserverapisgo)

- 📄 [pkg/controlplane/apiserver/completion.go](#pkgcontrolplaneapiservercompletiongo)

- 📄 [pkg/controlplane/apiserver/config.go](#pkgcontrolplaneapiserverconfiggo)

- 📄 [pkg/controlplane/apiserver/options/options.go](#pkgcontrolplaneapiserveroptionsoptionsgo)

- 📄 [pkg/controlplane/apiserver/options/validation.go](#pkgcontrolplaneapiserveroptionsvalidationgo)

- 📄 [pkg/controlplane/apiserver/peer.go](#pkgcontrolplaneapiserverpeergo)

- 📄 [pkg/controlplane/apiserver/samples/generic/main.go](#pkgcontrolplaneapiserversamplesgenericmaingo)

- 📄 [pkg/controlplane/apiserver/samples/generic/server/admission.go](#pkgcontrolplaneapiserversamplesgenericserveradmissiongo)

- 📄 [pkg/controlplane/apiserver/samples/generic/server/config.go](#pkgcontrolplaneapiserversamplesgenericserverconfiggo)

- 📄 [pkg/controlplane/apiserver/samples/generic/server/server.go](#pkgcontrolplaneapiserversamplesgenericserverservergo)

- 📄 [pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go](#pkgcontrolplaneapiserversamplesgenericserverserviceaccountsgo)

- 📄 [pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go](#pkgcontrolplaneapiserversamplesgenericservertestingtestservergo)

- 📄 [pkg/controlplane/apiserver/server.go](#pkgcontrolplaneapiserverservergo)

- 📄 [pkg/controlplane/controller/apiserverleasegc/gc_controller.go](#pkgcontrolplanecontrollerapiserverleasegcgc_controllergo)

- 📄 [pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go](#pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo)

- 📄 [pkg/controlplane/controller/crdregistration/crdregistration_controller.go](#pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo)

- 📄 [pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go](#pkgcontrolplanecontrollerdefaultservicecidrdefault_servicecidr_controllergo)

- 📄 [pkg/controlplane/controller/kubernetesservice/controller.go](#pkgcontrolplanecontrollerkubernetesservicecontrollergo)

- 📄 [pkg/controlplane/controller/leaderelection/election.go](#pkgcontrolplanecontrollerleaderelectionelectiongo)

- 📄 [pkg/controlplane/controller/leaderelection/leaderelection_controller.go](#pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo)

- 📄 [pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go](#pkgcontrolplanecontrollerleaderelectionleasecandidategc_controllergo)

- 📄 [pkg/controlplane/controller/leaderelection/run_with_leaderelection.go](#pkgcontrolplanecontrollerleaderelectionrun_with_leaderelectiongo)

- 📄 [pkg/controlplane/controller/legacytokentracking/controller.go](#pkgcontrolplanecontrollerlegacytokentrackingcontrollergo)

- 📄 [pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go](#pkgcontrolplanecontrollersystemnamespacessystem_namespaces_controllergo)

- 📄 [pkg/controlplane/instance.go](#pkgcontrolplaneinstancego)

- 📄 [pkg/controlplane/reconcilers/endpointsadapter.go](#pkgcontrolplanereconcilersendpointsadaptergo)

- 📄 [pkg/controlplane/reconcilers/instancecount.go](#pkgcontrolplanereconcilersinstancecountgo)

- 📄 [pkg/controlplane/reconcilers/lease.go](#pkgcontrolplanereconcilersleasego)

- 📄 [pkg/controlplane/reconcilers/none.go](#pkgcontrolplanereconcilersnonego)

- 📄 [pkg/controlplane/reconcilers/reconcilers.go](#pkgcontrolplanereconcilersreconcilersgo)


---


## pkg/controlplane/apiserver/admission/config.go


📄 Исходный файл: `pkg/controlplane/apiserver/admission/config.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [New](#new-pkgcontrolplaneapiserveradmissionconfiggo43) `:43`


</details>


[function] name: New file: pkg/controlplane/apiserver/admission/config.go:43 returns_error: да description: New sets up the plugins and admission start hooks needed for admission


### New (pkg/controlplane/apiserver/admission/config.go:43)


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


📍 *Расположение:* `pkg/controlplane/apiserver/admission/config.go:43`




## pkg/controlplane/apiserver/admission/initializer.go


📄 Исходный файл: `pkg/controlplane/apiserver/admission/initializer.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Initialize](#initialize-pkgcontrolplaneapiserveradmissioninitializergo47) `:47`

- 🔗 [NewPluginInitializer](#newplugininitializer-pkgcontrolplaneapiserveradmissioninitializergo35) `:35`


</details>


[function] name: Initialize file: pkg/controlplane/apiserver/admission/initializer.go:47 returns_error: нет description: Initialize checks the initialization interfaces implemented by each plugin
and provide the appropriate initialization da


### Initialize (pkg/controlplane/apiserver/admission/initializer.go:47)


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


📍 *Расположение:* `pkg/controlplane/apiserver/admission/initializer.go:47`



---


[function] name: NewPluginInitializer file: pkg/controlplane/apiserver/admission/initializer.go:35 returns_error: нет description: NewPluginInitializer constructs new instance of PluginInitializer


### NewPluginInitializer (pkg/controlplane/apiserver/admission/initializer.go:35)


NewPluginInitializer constructs new instance of PluginInitializer


```go
func NewPluginInitializer((
	quotaConfiguration quota.Configuration,
	excludedAdmissionResources []schema.GroupResource,
)) (
	quotaConfiguration quota.Configuration,
	excludedAdmissionResources []schema.GroupResource,
)
```


**Тип ответа:** quotaConfiguration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** quota.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** excludedAdmissionResources


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** schema.GroupResource


```json
{
  "Group": "string",
  "Resource": "string"
}
```


*Определено в:* `pkg/controller/garbagecollector/config/types.go`


📍 *Расположение:* `pkg/controlplane/apiserver/admission/initializer.go:35`




## pkg/controlplane/apiserver/aggregator.go


📄 Исходный файл: `pkg/controlplane/apiserver/aggregator.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [CreateAggregatorConfig](#createaggregatorconfig-pkgcontrolplaneapiserveraggregatorgo53) `:53`

- 🔗 [CreateAggregatorServer](#createaggregatorserver-pkgcontrolplaneapiserveraggregatorgo130) `:130`

- 🔗 [DefaultGenericAPIServicePriorities](#defaultgenericapiservicepriorities-pkgcontrolplaneapiserveraggregatorgo313) `:313`

- 🔗 [apiServiceExtractor](#apiserviceextractor-pkgcontrolplaneapiserveraggregatorgo231) `:231`

- 🔗 [apiServicesToRegister](#apiservicestoregister-pkgcontrolplaneapiserveraggregatorgo354) `:354`

- 🔗 [crdExtractor](#crdextractor-pkgcontrolplaneapiserveraggregatorgo215) `:215`

- 🔗 [makeAPIService](#makeapiservice-pkgcontrolplaneapiserveraggregatorgo245) `:245`

- 🔗 [makeAPIServiceAvailableHealthCheck](#makeapiserviceavailablehealthcheck-pkgcontrolplaneapiserveraggregatorgo266) `:266`


</details>


[function] name: CreateAggregatorConfig file: pkg/controlplane/apiserver/aggregator.go:53 returns_error: да description: —


### CreateAggregatorConfig (pkg/controlplane/apiserver/aggregator.go:53)


CreateAggregatorConfig is a function that creates new data based on the provided parameters and may return an error.


```go
func CreateAggregatorConfig((*aggregatorapiserver.Config, error)) (*aggregatorapiserver.Config, error)
```


**Тип запроса:** aggregatorapiserver.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** aggregatorapiserver.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*aggregatorapiserver.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:53`



---


[function] name: CreateAggregatorServer file: pkg/controlplane/apiserver/aggregator.go:130 returns_error: да description: —


### CreateAggregatorServer (pkg/controlplane/apiserver/aggregator.go:130)


CreateAggregatorServer is a function that creates new data based on the provided parameters and may return an error.


```go
func CreateAggregatorServer((*aggregatorapiserver.APIAggregator, error)) (*aggregatorapiserver.APIAggregator, error)
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


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:130`



---


[function] name: DefaultGenericAPIServicePriorities file: pkg/controlplane/apiserver/aggregator.go:313 returns_error: нет description: DefaultGenericAPIServicePriorities returns the APIService priorities for generic APIs


### DefaultGenericAPIServicePriorities (pkg/controlplane/apiserver/aggregator.go:313)


DefaultGenericAPIServicePriorities returns the APIService priorities for generic APIs


```go
func DefaultGenericAPIServicePriorities(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:313`



---


[function] name: apiServiceExtractor file: pkg/controlplane/apiserver/aggregator.go:231 returns_error: нет description: apiServiceExtractor extracts group-versions from APIService objects
for use in the peer proxy exclusion filter. Only agg


### apiServiceExtractor (pkg/controlplane/apiserver/aggregator.go:231)


apiServiceExtractor extracts group-versions from APIService objects
for use in the peer proxy exclusion filter. Only aggregated APIs
(those with a Service reference) are excluded.


```go
func apiServiceExtractor((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:231`



---


[function] name: apiServicesToRegister file: pkg/controlplane/apiserver/aggregator.go:354 returns_error: нет description: —


### apiServicesToRegister (pkg/controlplane/apiserver/aggregator.go:354)


apiServicesToRegister is a function that performs operations based on the provided parameters and returns (delegateAPIServer genericapiserver.DelegationTarget, registration autoregister.AutoAPIServiceRegistration, apiVersionPriorities map[schema.GroupVersion]APIServicePriority).


```go
func apiServicesToRegister((delegateAPIServer genericapiserver.DelegationTarget, registration autoregister.AutoAPIServiceRegistration, apiVersionPriorities map[schema.GroupVersion]APIServicePriority)) (delegateAPIServer genericapiserver.DelegationTarget, registration autoregister.AutoAPIServiceRegistration, apiVersionPriorities map[schema.GroupVersion]APIServicePriority)
```


**Тип ответа:** delegateAPIServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genericapiserver.DelegationTarget


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** registration


```json
{
  "restClient": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/admissionregistration/v1/admissionregistration_client.go`


**Тип ответа:** autoregister.AutoAPIServiceRegistration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiVersionPriorities


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** APIServicePriority


```json
{
  "Group": 0,
  "Version": 0
}
```


*Определено в:* `pkg/controlplane/apiserver/aggregator.go`


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:354`



---


[function] name: crdExtractor file: pkg/controlplane/apiserver/aggregator.go:215 returns_error: нет description: crdExtractor extracts group-versions from CustomResourceDefinition objects
for use in the peer proxy exclusion filter.


### crdExtractor (pkg/controlplane/apiserver/aggregator.go:215)


crdExtractor extracts group-versions from CustomResourceDefinition objects
for use in the peer proxy exclusion filter.


```go
func crdExtractor((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:215`



---


[function] name: makeAPIService file: pkg/controlplane/apiserver/aggregator.go:245 returns_error: нет description: —


### makeAPIService (pkg/controlplane/apiserver/aggregator.go:245)


makeAPIService is a function that performs operations based on the provided parameters and returns (gv schema.GroupVersion, apiVersionPriorities map[schema.GroupVersion]APIServicePriority).


```go
func makeAPIService((gv schema.GroupVersion, apiVersionPriorities map[schema.GroupVersion]APIServicePriority)) (gv schema.GroupVersion, apiVersionPriorities map[schema.GroupVersion]APIServicePriority)
```


**Тип ответа:** gv


```json
{
  "discoveryClient": {},
  "mu": {},
  "gvkParser": null,
  "lastChecked": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/unstructured.go`


**Тип ответа:** schema.GroupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** apiVersionPriorities


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** APIServicePriority


```json
{
  "Group": 0,
  "Version": 0
}
```


*Определено в:* `pkg/controlplane/apiserver/aggregator.go`


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:245`



---


[function] name: makeAPIServiceAvailableHealthCheck file: pkg/controlplane/apiserver/aggregator.go:266 returns_error: нет description: makeAPIServiceAvailableHealthCheck returns a healthz check that returns healthy
once all of the specified services have 


### makeAPIServiceAvailableHealthCheck (pkg/controlplane/apiserver/aggregator.go:266)


makeAPIServiceAvailableHealthCheck returns a healthz check that returns healthy
once all of the specified services have been observed to be available at least once.


```go
func makeAPIServiceAvailableHealthCheck((name string, apiServices []*v1.APIService, apiServiceInformer informers.APIServiceInformer)) (name string, apiServices []*v1.APIService, apiServiceInformer informers.APIServiceInformer)
```


**Тип запроса:** v1.APIService


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/apis/apiregistration/v1beta1/types.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** apiServices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.APIService


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/apis/apiregistration/v1beta1/types.go`


**Тип ответа:** apiServiceInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** informers.APIServiceInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/apiserver/aggregator.go:266`




## pkg/controlplane/apiserver/apiextensions.go


📄 Исходный файл: `pkg/controlplane/apiserver/apiextensions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CreateAPIExtensionsConfig](#createapiextensionsconfig-pkgcontrolplaneapiserverapiextensionsgo34) `:34`


</details>


[function] name: CreateAPIExtensionsConfig file: pkg/controlplane/apiserver/apiextensions.go:34 returns_error: да description: —


### CreateAPIExtensionsConfig (pkg/controlplane/apiserver/apiextensions.go:34)


CreateAPIExtensionsConfig is a function that creates new data based on the provided parameters and may return an error.


```go
func CreateAPIExtensionsConfig((*apiextensionsapiserver.Config, error)) (*apiextensionsapiserver.Config, error)
```


**Тип запроса:** apiextensionsapiserver.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** apiextensionsapiserver.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apiextensionsapiserver.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/apiextensions.go:34`




## pkg/controlplane/apiserver/apis.go


📄 Исходный файл: `pkg/controlplane/apiserver/apis.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [GenericStorageProviders](#genericstorageproviders-pkgcontrolplaneapiserverapisgo64) `:64`

- 🔗 [InstallAPIs](#installapis-pkgcontrolplaneapiserverapisgo88) `:88`

- 🔗 [NewCoreGenericConfig](#newcoregenericconfig-pkgcontrolplaneapiserverapisgo48) `:48`


</details>


[function] name: GenericStorageProviders file: pkg/controlplane/apiserver/apis.go:64 returns_error: да description: GenericStorageProviders returns a set of APIs for a generic control plane.
They ought to be a subset of those served by 


### GenericStorageProviders (pkg/controlplane/apiserver/apis.go:64)


GenericStorageProviders returns a set of APIs for a generic control plane.
They ought to be a subset of those served by kube-apiserver.


```go
func (c *CompletedConfig) GenericStorageProviders(([]RESTStorageProvider, error)) ([]RESTStorageProvider, error)
```


**Тип ответа:** RESTStorageProvider


```json
{
  "Authenticator": {},
  "APIAudiences": {}
}
```


*Определено в:* `pkg/registry/authentication/rest/storage_authentication.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]RESTStorageProvider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/apis.go:64`



---


[function] name: InstallAPIs file: pkg/controlplane/apiserver/apis.go:88 returns_error: нет description: InstallAPIs will install the APIs for the restStorageProviders if they are enabled.


### InstallAPIs (pkg/controlplane/apiserver/apis.go:88)


InstallAPIs will install the APIs for the restStorageProviders if they are enabled.


```go
func (s *Server) InstallAPIs((restStorageProviders ...RESTStorageProvider)) (restStorageProviders ...RESTStorageProvider)
```


**Тип ответа:** restStorageProviders


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RESTStorageProvider


```json
{
  "Authenticator": {},
  "APIAudiences": {}
}
```


*Определено в:* `pkg/registry/authentication/rest/storage_authentication.go`


📍 *Расположение:* `pkg/controlplane/apiserver/apis.go:88`



---


[function] name: NewCoreGenericConfig file: pkg/controlplane/apiserver/apis.go:48 returns_error: нет description: NewCoreGenericConfig returns a new core rest generic config.


### NewCoreGenericConfig (pkg/controlplane/apiserver/apis.go:48)


NewCoreGenericConfig returns a new core rest generic config.


```go
func (c *CompletedConfig) NewCoreGenericConfig(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/apis.go:48`




## pkg/controlplane/apiserver/completion.go


📄 Исходный файл: `pkg/controlplane/apiserver/completion.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Complete](#complete-pkgcontrolplaneapiservercompletiongo34) `:34`


</details>


[function] name: Complete file: pkg/controlplane/apiserver/completion.go:34 returns_error: нет description: —


### Complete (pkg/controlplane/apiserver/completion.go:34)


Complete is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Config) Complete(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/completion.go:34`




## pkg/controlplane/apiserver/config.go


📄 Исходный файл: `pkg/controlplane/apiserver/config.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [BuildAuthorizer](#buildauthorizer-pkgcontrolplaneapiserverconfiggo245) `:245`

- 🔗 [BuildGenericConfig](#buildgenericconfig-pkgcontrolplaneapiserverconfiggo115) `:115`

- 🔗 [CreateConfig](#createconfig-pkgcontrolplaneapiserverconfiggo277) `:277`

- 🔗 [CreateProxyTransport](#createproxytransport-pkgcontrolplaneapiserverconfiggo418) `:418`


</details>


[function] name: BuildAuthorizer file: pkg/controlplane/apiserver/config.go:245 returns_error: да description: BuildAuthorizer constructs the authorizer. If authorization is not set in s, it returns nil, nil, false, nil


### BuildAuthorizer (pkg/controlplane/apiserver/config.go:245)


BuildAuthorizer constructs the authorizer. If authorization is not set in s, it returns nil, nil, false, nil


```go
func BuildAuthorizer((authorizer.Authorizer, authorizer.RuleResolver, bool, error)) (authorizer.Authorizer, authorizer.RuleResolver, bool, error)
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


*Типы возврата:* `authorizer.Authorizer`, `authorizer.RuleResolver`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/config.go:245`



---


[function] name: BuildGenericConfig file: pkg/controlplane/apiserver/config.go:115 returns_error: да description: BuildGenericConfig takes the generic controlplane apiserver options and produces
the genericapiserver.Config associated 


### BuildGenericConfig (pkg/controlplane/apiserver/config.go:115)


BuildGenericConfig takes the generic controlplane apiserver options and produces
the genericapiserver.Config associated with it. The genericapiserver.Config is
often shared between multiple delegated apiservers.


```go
func BuildGenericConfig((
	genericConfig *genericapiserver.Config,
	versionedInformers clientgoinformers.SharedInformerFactory,
	storageFactory *serverstorage.DefaultStorageFactory,
	lastErr error,
)) (
	genericConfig *genericapiserver.Config,
	versionedInformers clientgoinformers.SharedInformerFactory,
	storageFactory *serverstorage.DefaultStorageFactory,
	lastErr error,
)
```


**Тип запроса:** genericapiserver.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


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


**Тип ответа:** genericConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genericapiserver.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** versionedInformers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientgoinformers.SharedInformerFactory


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


**Тип ответа:** storageFactory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** lastErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `genericConfig *genericapiserver.Config`, `versionedInformers clientgoinformers.SharedInformerFactory`, `storageFactory *serverstorage.DefaultStorageFactory`, `lastErr error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/config.go:115`



---


[function] name: CreateConfig file: pkg/controlplane/apiserver/config.go:277 returns_error: да description: CreateConfig takes the generic controlplane apiserver options and
creates a config for the generic Kube APIs out of it.


### CreateConfig (pkg/controlplane/apiserver/config.go:277)


CreateConfig takes the generic controlplane apiserver options and
creates a config for the generic Kube APIs out of it.


```go
func CreateConfig((
	*Config,
	[]admission.PluginInitializer,
	error,
)) (
	*Config,
	[]admission.PluginInitializer,
	error,
)
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


**Тип ответа:** admission.PluginInitializer


```json
{
  "quotaConfiguration": {},
  "excludedAdmissionResources": []
}
```


*Определено в:* `pkg/controlplane/apiserver/admission/initializer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Config`, `[]admission.PluginInitializer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/config.go:277`



---


[function] name: CreateProxyTransport file: pkg/controlplane/apiserver/config.go:418 returns_error: нет description: CreateProxyTransport creates the dialer infrastructure to connect to the nodes.


### CreateProxyTransport (pkg/controlplane/apiserver/config.go:418)


CreateProxyTransport creates the dialer infrastructure to connect to the nodes.


```go
func CreateProxyTransport(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/config.go:418`




## pkg/controlplane/apiserver/options/options.go


📄 Исходный файл: `pkg/controlplane/apiserver/options/options.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AddFlags](#addflags-pkgcontrolplaneapiserveroptionsoptionsgo143) `:143`

- 🔗 [Complete](#complete-pkgcontrolplaneapiserveroptionsoptionsgo221) `:221`

- 🔗 [NewOptions](#newoptions-pkgcontrolplaneapiserveroptionsoptionsgo112) `:112`

- 🔗 [ServiceIPRange](#serviceiprange-pkgcontrolplaneapiserveroptionsoptionsgo366) `:366`

- 🔗 [completeServiceAccountOptions](#completeserviceaccountoptions-pkgcontrolplaneapiserveroptionsoptionsgo292) `:292`


</details>


[function] name: AddFlags file: pkg/controlplane/apiserver/options/options.go:143 returns_error: нет description: —


### AddFlags (pkg/controlplane/apiserver/options/options.go:143)


AddFlags is a method that creates new data based on the provided parameters and returns (fss *cliflag.NamedFlagSets).


```go
func (s *Options) AddFlags((fss *cliflag.NamedFlagSets)) (fss *cliflag.NamedFlagSets)
```


**Тип запроса:** cliflag.NamedFlagSets


```json
{
  "Order": [],
  "FlagSets": {},
  "NormalizeNameFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/cli/flag/sectioned.go`


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


📍 *Расположение:* `pkg/controlplane/apiserver/options/options.go:143`



---


[function] name: Complete file: pkg/controlplane/apiserver/options/options.go:221 returns_error: да description: —


### Complete (pkg/controlplane/apiserver/options/options.go:221)


Complete is a method that performs operations based on the provided parameters and may return an error.


```go
func (o *Options) Complete((CompletedOptions, error)) (CompletedOptions, error)
```


**Тип ответа:** CompletedOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CompletedOptions`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/options/options.go:221`



---


[function] name: NewOptions file: pkg/controlplane/apiserver/options/options.go:112 returns_error: нет description: NewOptions creates a new ServerRunOptions object with default parameters


### NewOptions (pkg/controlplane/apiserver/options/options.go:112)


NewOptions creates a new ServerRunOptions object with default parameters


```go
func NewOptions(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/options/options.go:112`



---


[function] name: ServiceIPRange file: pkg/controlplane/apiserver/options/options.go:366 returns_error: да description: ServiceIPRange checks if the serviceClusterIPRange flag is nil, raising a warning if so and
setting service ip range to 


### ServiceIPRange (pkg/controlplane/apiserver/options/options.go:366)


ServiceIPRange checks if the serviceClusterIPRange flag is nil, raising a warning if so and
setting service ip range to the default value in kubeoptions.DefaultServiceIPCIDR
for now until the default is removed per the deprecation timeline guidelines.
Returns service ip range, api server service IP, and an error


```go
func ServiceIPRange((net.IPNet, net.IP, error)) (net.IPNet, net.IP, error)
```


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `net.IPNet`, `net.IP`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/options/options.go:366`



---


[function] name: completeServiceAccountOptions file: pkg/controlplane/apiserver/options/options.go:292 returns_error: нет description: —


### completeServiceAccountOptions (pkg/controlplane/apiserver/options/options.go:292)


completeServiceAccountOptions is a method that performs operations based on the provided parameters and returns (ctx context.Context, completed *completedOptions).


```go
func (o *Options) completeServiceAccountOptions((ctx context.Context, completed *completedOptions)) (ctx context.Context, completed *completedOptions)
```


**Тип запроса:** completedOptions


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


**Тип ответа:** completed


```json
{
  "Options": {},
  "Aggregator": {},
  "ControlPlane": {},
  "APIExtensions": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/samples/generic/server/config.go`


**Тип ответа:** completedOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/apiserver/options/options.go:292`




## pkg/controlplane/apiserver/options/validation.go


📄 Исходный файл: `pkg/controlplane/apiserver/options/validation.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Validate](#validate-pkgcontrolplaneapiserveroptionsvalidationgo125) `:125`

- 🔗 [validateAPIPriorityAndFairness](#validateapipriorityandfairness-pkgcontrolplaneapiserveroptionsvalidationgo54) `:54`

- 🔗 [validateCoordinatedLeadershipFlags](#validatecoordinatedleadershipflags-pkgcontrolplaneapiserveroptionsvalidationgo113) `:113`

- 🔗 [validateServiceAccountTokenSigningConfig](#validateserviceaccounttokensigningconfig-pkgcontrolplaneapiserveroptionsvalidationgo92) `:92`

- 🔗 [validateTokenRequest](#validatetokenrequest-pkgcontrolplaneapiserveroptionsvalidationgo34) `:34`

- 🔗 [validateUnknownVersionInteroperabilityProxyFlags](#validateunknownversioninteroperabilityproxyflags-pkgcontrolplaneapiserveroptionsvalidationgo74) `:74`


</details>


[function] name: Validate file: pkg/controlplane/apiserver/options/validation.go:125 returns_error: нет description: Validate checks Options and return a slice of found errs.


### Validate (pkg/controlplane/apiserver/options/validation.go:125)


Validate checks Options and return a slice of found errs.


```go
func (s *Options) Validate(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/options/validation.go:125`



---


[function] name: validateAPIPriorityAndFairness file: pkg/controlplane/apiserver/options/validation.go:54 returns_error: нет description: —


### validateAPIPriorityAndFairness (pkg/controlplane/apiserver/options/validation.go:54)


validateAPIPriorityAndFairness is a function that performs operations based on the provided parameters and returns (options *Options).


```go
func validateAPIPriorityAndFairness((options *Options)) (options *Options)
```


**Тип запроса:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


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


**Тип ответа:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


📍 *Расположение:* `pkg/controlplane/apiserver/options/validation.go:54`



---


[function] name: validateCoordinatedLeadershipFlags file: pkg/controlplane/apiserver/options/validation.go:113 returns_error: нет description: —


### validateCoordinatedLeadershipFlags (pkg/controlplane/apiserver/options/validation.go:113)


validateCoordinatedLeadershipFlags is a function that performs operations based on the provided parameters and returns (options *Options).


```go
func validateCoordinatedLeadershipFlags((options *Options)) (options *Options)
```


**Тип запроса:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


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


**Тип ответа:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


📍 *Расположение:* `pkg/controlplane/apiserver/options/validation.go:113`



---


[function] name: validateServiceAccountTokenSigningConfig file: pkg/controlplane/apiserver/options/validation.go:92 returns_error: нет description: —


### validateServiceAccountTokenSigningConfig (pkg/controlplane/apiserver/options/validation.go:92)


validateServiceAccountTokenSigningConfig is a function that performs operations based on the provided parameters and returns (options *Options).


```go
func validateServiceAccountTokenSigningConfig((options *Options)) (options *Options)
```


**Тип запроса:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


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


**Тип ответа:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


📍 *Расположение:* `pkg/controlplane/apiserver/options/validation.go:92`



---


[function] name: validateTokenRequest file: pkg/controlplane/apiserver/options/validation.go:34 returns_error: нет description: —


### validateTokenRequest (pkg/controlplane/apiserver/options/validation.go:34)


validateTokenRequest is a function that performs operations based on the provided parameters and returns (options *Options).


```go
func validateTokenRequest((options *Options)) (options *Options)
```


**Тип запроса:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


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


**Тип ответа:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


📍 *Расположение:* `pkg/controlplane/apiserver/options/validation.go:34`



---


[function] name: validateUnknownVersionInteroperabilityProxyFlags file: pkg/controlplane/apiserver/options/validation.go:74 returns_error: нет description: —


### validateUnknownVersionInteroperabilityProxyFlags (pkg/controlplane/apiserver/options/validation.go:74)


validateUnknownVersionInteroperabilityProxyFlags is a function that performs operations based on the provided parameters and returns (options *Options).


```go
func validateUnknownVersionInteroperabilityProxyFlags((options *Options)) (options *Options)
```


**Тип запроса:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


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


**Тип ответа:** Options


```json
{
  "Flagz": {},
  "GenericServerRunOptions": null,
  "Etcd": null,
  "SecureServing": null,
  "Audit": null,
  "Features": null,
  "Admission": null,
  "Authentication": null,
  "Authorization": null,
  "APIEnablement": null,
  "EgressSelector": null,
  "Metrics": null,
  "Logs": null,
  "Traces": null,
  "EnableLogsHandler": false,
  "EventTTL": {},
  "MaxConnectionBytesPerSec": 0,
  "ProxyClientCertFile": "string",
  "ProxyClientKeyFile": "string",
  "PeerCAFile": "string",
  "PeerAdvertiseAddress": {},
  "EnableAggregatorRouting": false,
  "AggregatorRejectForwardingRedirects": false,
  "ServiceAccountSigningKeyFile": "string",
  "ServiceAccountIssuer": {},
  "ServiceAccountTokenMaxExpiration": {},
  "ShowHiddenMetricsForVersion": "string",
  "SystemNamespaces": [],
  "ServiceAccountSigningEndpoint": "string",
  "CoordinatedLeadershipLeaseDuration": {},
  "CoordinatedLeadershipRenewDeadline": {},
  "CoordinatedLeadershipRetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/options/options.go`


📍 *Расположение:* `pkg/controlplane/apiserver/options/validation.go:74`




## pkg/controlplane/apiserver/peer.go


📄 Исходный файл: `pkg/controlplane/apiserver/peer.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [BuildPeerProxy](#buildpeerproxy-pkgcontrolplaneapiserverpeergo47) `:47`

- 🔗 [CreatePeerEndpointLeaseReconciler](#createpeerendpointleasereconciler-pkgcontrolplaneapiserverpeergo101) `:101`

- 🔗 [getPeerAddress](#getpeeraddress-pkgcontrolplaneapiserverpeergo113) `:113`


</details>


[function] name: BuildPeerProxy file: pkg/controlplane/apiserver/peer.go:47 returns_error: да description: —


### BuildPeerProxy (pkg/controlplane/apiserver/peer.go:47)


BuildPeerProxy is a function that performs operations based on the provided parameters and may return an error.


```go
func BuildPeerProxy((utilpeerproxy.Interface, error)) (utilpeerproxy.Interface, error)
```


**Тип ответа:** utilpeerproxy.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `utilpeerproxy.Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/peer.go:47`



---


[function] name: CreatePeerEndpointLeaseReconciler file: pkg/controlplane/apiserver/peer.go:101 returns_error: да description: CreatePeerEndpointLeaseReconciler creates a apiserver endpoint lease reconciliation loop
The peer endpoint leases are us


### CreatePeerEndpointLeaseReconciler (pkg/controlplane/apiserver/peer.go:101)


CreatePeerEndpointLeaseReconciler creates a apiserver endpoint lease reconciliation loop
The peer endpoint leases are used to find network locations of apiservers for peer proxy


```go
func CreatePeerEndpointLeaseReconciler((reconcilers.PeerEndpointLeaseReconciler, error)) (reconcilers.PeerEndpointLeaseReconciler, error)
```


**Тип ответа:** reconcilers.PeerEndpointLeaseReconciler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `reconcilers.PeerEndpointLeaseReconciler`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/peer.go:101`



---


[function] name: getPeerAddress file: pkg/controlplane/apiserver/peer.go:113 returns_error: нет description: utility function to get the apiserver address that is used by peer apiservers to proxy
requests to this apiserver in cas


### getPeerAddress (pkg/controlplane/apiserver/peer.go:113)


utility function to get the apiserver address that is used by peer apiservers to proxy
requests to this apiserver in case the peer is incapable of serving the request


```go
func getPeerAddress((peerAdvertiseAddress reconcilers.PeerAdvertiseAddress, publicAddress net.IP, publicServicePort int)) (peerAdvertiseAddress reconcilers.PeerAdvertiseAddress, publicAddress net.IP, publicServicePort int)
```


**Тип ответа:** peerAdvertiseAddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reconcilers.PeerAdvertiseAddress


```json
{
  "PeerAdvertiseIP": "string",
  "PeerAdvertisePort": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/reconcilers/peer_endpoint_lease.go`


**Тип ответа:** publicAddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** publicServicePort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/apiserver/peer.go:113`




## pkg/controlplane/apiserver/samples/generic/main.go


📄 Исходный файл: `pkg/controlplane/apiserver/samples/generic/main.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-pkgcontrolplaneapiserversamplesgenericmaingo32) `:32`


</details>


[function] name: main file: pkg/controlplane/apiserver/samples/generic/main.go:32 returns_error: нет description: —


### main (pkg/controlplane/apiserver/samples/generic/main.go:32)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/main.go:32`




## pkg/controlplane/apiserver/samples/generic/server/admission.go


📄 Исходный файл: `pkg/controlplane/apiserver/samples/generic/server/admission.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DefaultOffAdmissionPlugins](#defaultoffadmissionplugins-pkgcontrolplaneapiserversamplesgenericserveradmissiongo37) `:37`


</details>


[function] name: DefaultOffAdmissionPlugins file: pkg/controlplane/apiserver/samples/generic/server/admission.go:37 returns_error: нет description: DefaultOffAdmissionPlugins get admission plugins off by default for kube-apiserver.


### DefaultOffAdmissionPlugins (pkg/controlplane/apiserver/samples/generic/server/admission.go:37)


DefaultOffAdmissionPlugins get admission plugins off by default for kube-apiserver.


```go
func DefaultOffAdmissionPlugins(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/admission.go:37`




## pkg/controlplane/apiserver/samples/generic/server/config.go


📄 Исходный файл: `pkg/controlplane/apiserver/samples/generic/server/config.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Complete](#complete-pkgcontrolplaneapiserversamplesgenericserverconfiggo61) `:61`

- 🔗 [NewConfig](#newconfig-pkgcontrolplaneapiserversamplesgenericserverconfiggo75) `:75`


</details>


[function] name: Complete file: pkg/controlplane/apiserver/samples/generic/server/config.go:61 returns_error: да description: —


### Complete (pkg/controlplane/apiserver/samples/generic/server/config.go:61)


Complete is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *Config) Complete((CompletedConfig, error)) (CompletedConfig, error)
```


**Тип ответа:** CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CompletedConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/config.go:61`



---


[function] name: NewConfig file: pkg/controlplane/apiserver/samples/generic/server/config.go:75 returns_error: да description: NewConfig creates all the self-contained pieces making up an
sample-generic-controlplane, but does not wire them yet int


### NewConfig (pkg/controlplane/apiserver/samples/generic/server/config.go:75)


NewConfig creates all the self-contained pieces making up an
sample-generic-controlplane, but does not wire them yet into a server object.


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/config.go:75`




## pkg/controlplane/apiserver/samples/generic/server/server.go


📄 Исходный файл: `pkg/controlplane/apiserver/samples/generic/server/server.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [CreateServerChain](#createserverchain-pkgcontrolplaneapiserversamplesgenericserverservergo170) `:170`

- 🔗 [NewCommand](#newcommand-pkgcontrolplaneapiserversamplesgenericserverservergo59) `:59`

- 🔗 [NewOptions](#newoptions-pkgcontrolplaneapiserversamplesgenericserverservergo128) `:128`

- 🔗 [Run](#run-pkgcontrolplaneapiserversamplesgenericserverservergo142) `:142`

- 🔗 [init](#init-pkgcontrolplaneapiserversamplesgenericserverservergo54) `:54`


</details>


[function] name: CreateServerChain file: pkg/controlplane/apiserver/samples/generic/server/server.go:170 returns_error: да description: CreateServerChain creates the apiservers connected via delegation.


### CreateServerChain (pkg/controlplane/apiserver/samples/generic/server/server.go:170)


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/server.go:170`



---


[function] name: NewCommand file: pkg/controlplane/apiserver/samples/generic/server/server.go:59 returns_error: нет description: NewCommand creates a *cobra.Command object with default parameters


### NewCommand (pkg/controlplane/apiserver/samples/generic/server/server.go:59)


NewCommand creates a *cobra.Command object with default parameters


```go
func NewCommand(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/server.go:59`



---


[function] name: NewOptions file: pkg/controlplane/apiserver/samples/generic/server/server.go:128 returns_error: нет description: —


### NewOptions (pkg/controlplane/apiserver/samples/generic/server/server.go:128)


NewOptions is a function that performs operations based on the provided parameters and returns ().


```go
func NewOptions(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/server.go:128`



---


[function] name: Run file: pkg/controlplane/apiserver/samples/generic/server/server.go:142 returns_error: нет description: Run runs the specified APIServer. This should never exit.


### Run (pkg/controlplane/apiserver/samples/generic/server/server.go:142)


Run runs the specified APIServer. This should never exit.


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/server.go:142`



---


[function] name: init file: pkg/controlplane/apiserver/samples/generic/server/server.go:54 returns_error: нет description: —


### init (pkg/controlplane/apiserver/samples/generic/server/server.go:54)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/server.go:54`




## pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go


📄 Исходный файл: `pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GetNode](#getnode-pkgcontrolplaneapiserversamplesgenericserverserviceaccountsgo53) `:53`

- 🔗 [GetPod](#getpod-pkgcontrolplaneapiserversamplesgenericserverserviceaccountsgo45) `:45`

- 🔗 [GetSecret](#getsecret-pkgcontrolplaneapiserversamplesgenericserverserviceaccountsgo49) `:49`

- 🔗 [GetServiceAccount](#getserviceaccount-pkgcontrolplaneapiserversamplesgenericserverserviceaccountsgo41) `:41`

- 🔗 [genericTokenGetter](#generictokengetter-pkgcontrolplaneapiserversamplesgenericserverserviceaccountsgo37) `:37`


</details>


[function] name: GetNode file: pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:53 returns_error: да description: —


### GetNode (pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:53)


GetNode is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c clientGetter) GetNode((*v1.Node, error)) (*v1.Node, error)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.Node`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:53`



---


[function] name: GetPod file: pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:45 returns_error: да description: —


### GetPod (pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:45)


GetPod is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c clientGetter) GetPod((*v1.Pod, error)) (*v1.Pod, error)
```


**Тип запроса:** v1.Pod


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "CreatedAt": 0,
  "Containers": [],
  "Sandboxes": []
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** v1.Pod


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "CreatedAt": 0,
  "Containers": [],
  "Sandboxes": []
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.Pod`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:45`



---


[function] name: GetSecret file: pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:49 returns_error: да description: —


### GetSecret (pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:49)


GetSecret is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c clientGetter) GetSecret((*v1.Secret, error)) (*v1.Secret, error)
```


**Тип запроса:** v1.Secret


```json
{
  "Immutable": false,
  "Data": {},
  "Type": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.Secret


```json
{
  "Immutable": false,
  "Data": {},
  "Type": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.Secret`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:49`



---


[function] name: GetServiceAccount file: pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:41 returns_error: да description: —


### GetServiceAccount (pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:41)


GetServiceAccount is a method that retrieves data based on the provided parameters and may return an error.


```go
func (c clientGetter) GetServiceAccount((*v1.ServiceAccount, error)) (*v1.ServiceAccount, error)
```


**Тип запроса:** v1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.ServiceAccount`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:41`



---


[function] name: genericTokenGetter file: pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:37 returns_error: нет description: genericTokenGetter returns a ServiceAccountTokenGetter that does not depend
on pods and nodes.


### genericTokenGetter (pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:37)


genericTokenGetter returns a ServiceAccountTokenGetter that does not depend
on pods and nodes.


```go
func genericTokenGetter((factory informers.SharedInformerFactory)) (factory informers.SharedInformerFactory)
```


**Тип ответа:** factory


```json
{
  "clientGetter": {},
  "openAPIParser": null,
  "oapi": null,
  "parser": {},
  "getter": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/util/factory_client_access.go`


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/serviceaccounts.go:37`




## pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go


📄 Исходный файл: `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [NewDefaultTestServerOptions](#newdefaulttestserveroptions-pkgcontrolplaneapiserversamplesgenericservertestingtestservergo88) `:88`

- 🔗 [StartTestServer](#starttestserver-pkgcontrolplaneapiserversamplesgenericservertestingtestservergo95) `:95`

- 🔗 [StartTestServerOrDie](#starttestserverordie-pkgcontrolplaneapiserversamplesgenericservertestingtestservergo297) `:297`

- 🔗 [createLocalhostListenerOnFreePort](#createlocalhostlisteneronfreeport-pkgcontrolplaneapiserversamplesgenericservertestingtestservergo307) `:307`

- 🔗 [init](#init-pkgcontrolplaneapiserversamplesgenericservertestingtestservergo52) `:52`

- 🔗 [pkgPath](#pkgpath-pkgcontrolplaneapiserversamplesgenericservertestingtestservergo330) `:330`


</details>


[function] name: NewDefaultTestServerOptions file: pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:88 returns_error: нет description: NewDefaultTestServerOptions default options for TestServer instances


### NewDefaultTestServerOptions (pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:88)


NewDefaultTestServerOptions default options for TestServer instances


```go
func NewDefaultTestServerOptions(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:88`



---


[function] name: StartTestServer file: pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:95 returns_error: да description: StartTestServer starts an etcd server and sample-generic-controlplane and
returns a TestServer struct with a tear-down f


### StartTestServer (pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:95)


StartTestServer starts an etcd server and sample-generic-controlplane and
returns a TestServer struct with a tear-down func and clients to access it
and its backing store.


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:95`



---


[function] name: StartTestServerOrDie file: pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:297 returns_error: нет description: StartTestServerOrDie calls StartTestServer t.Fatal if it does not succeed.


### StartTestServerOrDie (pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:297)


StartTestServerOrDie calls StartTestServer t.Fatal if it does not succeed.


```go
func StartTestServerOrDie((t ktesting.TB, instanceOptions *TestServerInstanceOptions, flags []string, storageConfig *storagebackend.Config)) (t ktesting.TB, instanceOptions *TestServerInstanceOptions, flags []string, storageConfig *storagebackend.Config)
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


**Тип ответа:** ktesting.TB


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:297`



---


[function] name: createLocalhostListenerOnFreePort file: pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:307 returns_error: да description: —


### createLocalhostListenerOnFreePort (pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:307)


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:307`



---


[function] name: init file: pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:52 returns_error: нет description: —


### init (pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:52)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:52`



---


[function] name: pkgPath file: pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:330 returns_error: да description: pkgPath returns the absolute file path to this package's directory. With go
test, we can just look at the runtime call s


### pkgPath (pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:330)


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


📍 *Расположение:* `pkg/controlplane/apiserver/samples/generic/server/testing/testserver.go:330`




## pkg/controlplane/apiserver/server.go


📄 Исходный файл: `pkg/controlplane/apiserver/server.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [New](#new-pkgcontrolplaneapiserverservergo92) `:92`

- 🔗 [labelAPIServerHeartbeatFunc](#labelapiserverheartbeatfunc-pkgcontrolplaneapiserverservergo307) `:307`


</details>


[function] name: New file: pkg/controlplane/apiserver/server.go:92 returns_error: да description: New returns a new instance of Master from the given config.
Certain config fields will be set to a default value if unse


### New (pkg/controlplane/apiserver/server.go:92)


New returns a new instance of Master from the given config.
Certain config fields will be set to a default value if unset.
Certain config fields must be specified, including:
KubeletClientConfig


```go
func (c completedConfig) New((*Server, error)) (*Server, error)
```


**Тип запроса:** Server


```json
{
  "flagz": {},
  "auth": {},
  "host": {},
  "restfulCont": {},
  "metricsBuckets": {},
  "metricsMethodBuckets": {},
  "resourceAnalyzer": {},
  "extendedCheckers": []
}
```


*Определено в:* `pkg/kubelet/server/server.go`


**Тип ответа:** Server


```json
{
  "flagz": {},
  "auth": {},
  "host": {},
  "restfulCont": {},
  "metricsBuckets": {},
  "metricsMethodBuckets": {},
  "resourceAnalyzer": {},
  "extendedCheckers": []
}
```


*Определено в:* `pkg/kubelet/server/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Server`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/apiserver/server.go:92`



---


[function] name: labelAPIServerHeartbeatFunc file: pkg/controlplane/apiserver/server.go:307 returns_error: нет description: —


### labelAPIServerHeartbeatFunc (pkg/controlplane/apiserver/server.go:307)


labelAPIServerHeartbeatFunc is a function that performs operations based on the provided parameters and returns (identity string, peeraddress string).


```go
func labelAPIServerHeartbeatFunc((identity string, peeraddress string)) (identity string, peeraddress string)
```


**Тип ответа:** identity


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** peeraddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/apiserver/server.go:307`




## pkg/controlplane/controller/apiserverleasegc/gc_controller.go


📄 Исходный файл: `pkg/controlplane/controller/apiserverleasegc/gc_controller.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NewAPIServerLeaseGC](#newapiserverleasegc-pkgcontrolplanecontrollerapiserverleasegcgc_controllergo51) `:51`

- 🔗 [Run](#run-pkgcontrolplanecontrollerapiserverleasegcgc_controllergo75) `:75`

- 🔗 [RunWithContext](#runwithcontext-pkgcontrolplanecontrollerapiserverleasegcgc_controllergo80) `:80`

- 🔗 [gc](#gc-pkgcontrolplanecontrollerapiserverleasegcgc_controllergo100) `:100`

- 🔗 [isLeaseExpired](#isleaseexpired-pkgcontrolplanecontrollerapiserverleasegcgc_controllergo143) `:143`


</details>


[function] name: NewAPIServerLeaseGC file: pkg/controlplane/controller/apiserverleasegc/gc_controller.go:51 returns_error: нет description: NewAPIServerLeaseGC creates a new Controller.


### NewAPIServerLeaseGC (pkg/controlplane/controller/apiserverleasegc/gc_controller.go:51)


NewAPIServerLeaseGC creates a new Controller.


```go
func NewAPIServerLeaseGC((clientset kubernetes.Interface, gcCheckPeriod time.Duration, leaseNamespace, leaseLabelSelector string)) (clientset kubernetes.Interface, gcCheckPeriod time.Duration, leaseNamespace, leaseLabelSelector string)
```


**Тип ответа:** clientset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** gcCheckPeriod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** leaseNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** leaseLabelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/apiserverleasegc/gc_controller.go:51`



---


[function] name: Run file: pkg/controlplane/controller/apiserverleasegc/gc_controller.go:75 returns_error: нет description: Run starts one worker.

logcheck:context // RunWithContext should be used instead of Run in code which supports contextu


### Run (pkg/controlplane/controller/apiserverleasegc/gc_controller.go:75)


Run starts one worker.

logcheck:context // RunWithContext should be used instead of Run in code which supports contextual logging.


```go
func (c *Controller) Run((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/controlplane/controller/apiserverleasegc/gc_controller.go:75`



---


[function] name: RunWithContext file: pkg/controlplane/controller/apiserverleasegc/gc_controller.go:80 returns_error: нет description: RunWithContext starts one worker with a context.


### RunWithContext (pkg/controlplane/controller/apiserverleasegc/gc_controller.go:80)


RunWithContext starts one worker with a context.


```go
func (c *Controller) RunWithContext((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/apiserverleasegc/gc_controller.go:80`



---


[function] name: gc file: pkg/controlplane/controller/apiserverleasegc/gc_controller.go:100 returns_error: нет description: —


### gc (pkg/controlplane/controller/apiserverleasegc/gc_controller.go:100)


gc is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) gc((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/apiserverleasegc/gc_controller.go:100`



---


[function] name: isLeaseExpired file: pkg/controlplane/controller/apiserverleasegc/gc_controller.go:143 returns_error: нет description: —


### isLeaseExpired (pkg/controlplane/controller/apiserverleasegc/gc_controller.go:143)


isLeaseExpired is a function that performs operations based on the provided parameters and returns (lease *v1.Lease).


```go
func isLeaseExpired((lease *v1.Lease)) (lease *v1.Lease)
```


**Тип запроса:** v1.Lease


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** lease


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/coordination/v1beta1/lease.go`


**Тип ответа:** v1.Lease


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/apiserverleasegc/gc_controller.go:143`




## pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go


📄 Исходный файл: `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [Enqueue](#enqueue-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo449) `:449`

- 🔗 [NewClusterAuthenticationTrustController](#newclusterauthenticationtrustcontroller-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo96) `:96`

- 🔗 [Run](#run-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo454) `:454`

- 🔗 [combineCertLists](#combinecertlists-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo382) `:382`

- 🔗 [combineUniqueStringSlices](#combineuniquestringslices-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo355) `:355`

- 🔗 [combinedClusterAuthenticationInfo](#combinedclusterauthenticationinfo-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo222) `:222`

- 🔗 [createNamespaceIfNeeded](#createnamespaceifneeded-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo181) `:181`

- 🔗 [encodeCertificates](#encodecertificates-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo527) `:527`

- 🔗 [filterExpiredCerts](#filterexpiredcerts-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo435) `:435`

- 🔗 [getClusterAuthenticationInfoFor](#getclusterauthenticationinfofor-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo290) `:290`

- 🔗 [getConfigMapDataFor](#getconfigmapdatafor-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo244) `:244`

- 🔗 [jsonDeserializeStringSlice](#jsondeserializestringslice-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo343) `:343`

- 🔗 [jsonSerializeStringSlice](#jsonserializestringslice-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo335) `:335`

- 🔗 [keyFn](#keyfn-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo522) `:522`

- 🔗 [processNextWorkItem](#processnextworkitem-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo492) `:492`

- 🔗 [runWorker](#runworker-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo484) `:484`

- 🔗 [syncConfigMap](#syncconfigmap-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo140) `:140`

- 🔗 [writeConfigMap](#writeconfigmap-pkgcontrolplanecontrollerclusterauthenticationtrustcluster_authentication_trust_controllergo199) `:199`


</details>


[function] name: Enqueue file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:449 returns_error: нет description: Enqueue a method to allow separate control loops to cause the controller to trigger and reconcile content.


### Enqueue (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:449)


Enqueue a method to allow separate control loops to cause the controller to trigger and reconcile content.


```go
func (c *Controller) Enqueue(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:449`



---


[function] name: NewClusterAuthenticationTrustController file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:96 returns_error: нет description: NewClusterAuthenticationTrustController returns a controller that will maintain the kube-system configmap/extension-apis


### NewClusterAuthenticationTrustController (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:96)


NewClusterAuthenticationTrustController returns a controller that will maintain the kube-system configmap/extension-apiserver-authentication
that holds information about how to aggregated apiservers are recommended (but not required) to configure themselves.


```go
func NewClusterAuthenticationTrustController((requiredAuthenticationData ClusterAuthenticationInfo, kubeClient kubernetes.Interface)) (requiredAuthenticationData ClusterAuthenticationInfo, kubeClient kubernetes.Interface)
```


**Тип ответа:** requiredAuthenticationData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ClusterAuthenticationInfo


```json
{
  "ClientCA": {},
  "RequestHeaderUsernameHeaders": {},
  "RequestHeaderUIDHeaders": {},
  "RequestHeaderGroupHeaders": {},
  "RequestHeaderExtraHeaderPrefixes": {},
  "RequestHeaderAllowedNames": {},
  "RequestHeaderCA": {}
}
```


*Определено в:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go`


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


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:96`



---


[function] name: Run file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:454 returns_error: нет description: Run the controller until stopped.


### Run (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:454)


Run the controller until stopped.


```go
func (c *Controller) Run((ctx context.Context, workers int)) (ctx context.Context, workers int)
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


**Тип ответа:** workers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:454`



---


[function] name: combineCertLists file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:382 returns_error: да description: —


### combineCertLists (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:382)


combineCertLists is a function that performs operations based on the provided parameters and may return an error.


```go
func combineCertLists((dynamiccertificates.CAContentProvider, error)) (dynamiccertificates.CAContentProvider, error)
```


**Тип ответа:** dynamiccertificates.CAContentProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `dynamiccertificates.CAContentProvider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:382`



---


[function] name: combineUniqueStringSlices file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:355 returns_error: нет description: —


### combineUniqueStringSlices (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:355)


combineUniqueStringSlices is a function that performs operations based on the provided parameters and returns (lhs, rhs headerrequest.StringSliceProvider).


```go
func combineUniqueStringSlices((lhs, rhs headerrequest.StringSliceProvider)) (lhs, rhs headerrequest.StringSliceProvider)
```


**Тип ответа:** lhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** headerrequest.StringSliceProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:355`



---


[function] name: combinedClusterAuthenticationInfo file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:222 returns_error: да description: combinedClusterAuthenticationInfo combines two sets of authentication information into a new one


### combinedClusterAuthenticationInfo (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:222)


combinedClusterAuthenticationInfo combines two sets of authentication information into a new one


```go
func combinedClusterAuthenticationInfo((ClusterAuthenticationInfo, error)) (ClusterAuthenticationInfo, error)
```


**Тип ответа:** ClusterAuthenticationInfo


```json
{
  "ClientCA": {},
  "RequestHeaderUsernameHeaders": {},
  "RequestHeaderUIDHeaders": {},
  "RequestHeaderGroupHeaders": {},
  "RequestHeaderExtraHeaderPrefixes": {},
  "RequestHeaderAllowedNames": {},
  "RequestHeaderCA": {}
}
```


*Определено в:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ClusterAuthenticationInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:222`



---


[function] name: createNamespaceIfNeeded file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:181 returns_error: нет description: —


### createNamespaceIfNeeded (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:181)


createNamespaceIfNeeded is a function that performs operations based on the provided parameters and returns (nsClient corev1client.NamespacesGetter, ns string).


```go
func createNamespaceIfNeeded((nsClient corev1client.NamespacesGetter, ns string)) (nsClient corev1client.NamespacesGetter, ns string)
```


**Тип ответа:** nsClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1client.NamespacesGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ns


```json
{
  "Generic": null,
  "KubeCloudShared": null,
  "ServiceController": null,
  "AttachDetachController": null,
  "CSRSigningController": null,
  "DaemonSetController": null,
  "DeploymentController": null,
  "DeviceTaintEvictionController": null,
  "ResourceClaimController": null,
  "StatefulSetController": null,
  "DeprecatedFlags": null,
  "EndpointController": null,
  "EndpointSliceController": null,
  "EndpointSliceMirroringController": null,
  "EphemeralVolumeController": null,
  "GarbageCollectorController": null,
  "HPAController": null,
  "JobController": null,
  "CronJobController": null,
  "LegacySATokenCleaner": null,
  "NamespaceController": null,
  "NodeIPAMController": null,
  "NodeLifecycleController": null,
  "PersistentVolumeBinderController": null,
  "PodGCController": null,
  "ReplicaSetController": null,
  "ReplicationController": null,
  "ResourceQuotaController": null,
  "SAController": null,
  "TTLAfterFinishedController": null,
  "ValidatingAdmissionPolicyStatusController": null,
  "SecureServing": null,
  "Authentication": null,
  "Authorization": null,
  "Metrics": null,
  "Logs": null,
  "Master": "string",
  "ShowHiddenMetricsForVersion": "string",
  "ControllerShutdownTimeout": {},
  "ComponentGlobalsRegistry": {},
  "ParsedFlags": null
}
```


*Определено в:* `cmd/kube-controller-manager/app/options/options.go`


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:181`



---


[function] name: encodeCertificates file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:527 returns_error: да description: —


### encodeCertificates (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:527)


encodeCertificates is a function that performs operations based on the provided parameters and may return an error.


```go
func encodeCertificates(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:527`



---


[function] name: filterExpiredCerts file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:435 returns_error: нет description: filterExpiredCerts checks are all certificates in the bundle valid, i.e. they have not expired.
The function returns new


### filterExpiredCerts (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:435)


filterExpiredCerts checks are all certificates in the bundle valid, i.e. they have not expired.
The function returns new bundle with only valid certificates or error if no valid certificate is found.
We allow five minutes of slack for NotAfter comparisons


```go
func filterExpiredCerts((certs ...*x509.Certificate)) (certs ...*x509.Certificate)
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


**Тип ответа:** certs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:435`



---


[function] name: getClusterAuthenticationInfoFor file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:290 returns_error: да description: —


### getClusterAuthenticationInfoFor (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:290)


getClusterAuthenticationInfoFor is a function that performs operations based on the provided parameters and may return an error.


```go
func getClusterAuthenticationInfoFor((ClusterAuthenticationInfo, error)) (ClusterAuthenticationInfo, error)
```


**Тип ответа:** ClusterAuthenticationInfo


```json
{
  "ClientCA": {},
  "RequestHeaderUsernameHeaders": {},
  "RequestHeaderUIDHeaders": {},
  "RequestHeaderGroupHeaders": {},
  "RequestHeaderExtraHeaderPrefixes": {},
  "RequestHeaderAllowedNames": {},
  "RequestHeaderCA": {}
}
```


*Определено в:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ClusterAuthenticationInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:290`



---


[function] name: getConfigMapDataFor file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:244 returns_error: да description: —


### getConfigMapDataFor (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:244)


getConfigMapDataFor is a function that performs operations based on the provided parameters and may return an error.


```go
func getConfigMapDataFor((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:244`



---


[function] name: jsonDeserializeStringSlice file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:343 returns_error: да description: —


### jsonDeserializeStringSlice (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:343)


jsonDeserializeStringSlice is a function that performs operations based on the provided parameters and may return an error.


```go
func jsonDeserializeStringSlice((headerrequest.StringSliceProvider, error)) (headerrequest.StringSliceProvider, error)
```


**Тип ответа:** headerrequest.StringSliceProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `headerrequest.StringSliceProvider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:343`



---


[function] name: jsonSerializeStringSlice file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:335 returns_error: да description: —


### jsonSerializeStringSlice (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:335)


jsonSerializeStringSlice is a function that performs operations based on the provided parameters and may return an error.


```go
func jsonSerializeStringSlice((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:335`



---


[function] name: keyFn file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:522 returns_error: нет description: —


### keyFn (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:522)


keyFn is a function that performs operations based on the provided parameters and returns ().


```go
func keyFn(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:522`



---


[function] name: processNextWorkItem file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:492 returns_error: нет description: processNextWorkItem deals with one key off the queue.  It returns false when it's time to quit.


### processNextWorkItem (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:492)


processNextWorkItem deals with one key off the queue.  It returns false when it's time to quit.


```go
func (c *Controller) processNextWorkItem(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:492`



---


[function] name: runWorker file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:484 returns_error: нет description: —


### runWorker (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:484)


runWorker is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Controller) runWorker(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:484`



---


[function] name: syncConfigMap file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:140 returns_error: нет description: —


### syncConfigMap (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:140)


syncConfigMap is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Controller) syncConfigMap(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:140`



---


[function] name: writeConfigMap file: pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:199 returns_error: нет description: —


### writeConfigMap (pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:199)


writeConfigMap is a function that performs operations based on the provided parameters and returns (configMapClient corev1client.ConfigMapsGetter, required *corev1.ConfigMap).


```go
func writeConfigMap((configMapClient corev1client.ConfigMapsGetter, required *corev1.ConfigMap)) (configMapClient corev1client.ConfigMapsGetter, required *corev1.ConfigMap)
```


**Тип запроса:** corev1.ConfigMap


```json
{
  "Immutable": false,
  "Data": {},
  "BinaryData": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** configMapClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1client.ConfigMapsGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** required


```json
{
  "mode": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/required.go`


**Тип ответа:** corev1.ConfigMap


```json
{
  "Immutable": false,
  "Data": {},
  "BinaryData": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/controlplane/controller/clusterauthenticationtrust/cluster_authentication_trust_controller.go:199`




## pkg/controlplane/controller/crdregistration/crdregistration_controller.go


📄 Исходный файл: `pkg/controlplane/controller/crdregistration/crdregistration_controller.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [NewCRDRegistrationController](#newcrdregistrationcontroller-pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo64) `:64`

- 🔗 [Run](#run-pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo109) `:109`

- 🔗 [WaitForInitialSync](#waitforinitialsync-pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo148) `:148`

- 🔗 [enqueueCRD](#enqueuecrd-pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo190) `:190`

- 🔗 [handleVersionUpdate](#handleversionupdate-pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo196) `:196`

- 🔗 [processNextWorkItem](#processnextworkitem-pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo160) `:160`

- 🔗 [runWorker](#runworker-pkgcontrolplanecontrollercrdregistrationcrdregistration_controllergo152) `:152`


</details>


[function] name: NewCRDRegistrationController file: pkg/controlplane/controller/crdregistration/crdregistration_controller.go:64 returns_error: нет description: NewCRDRegistrationController returns a controller which will register CRD GroupVersions with the auto APIService registr


### NewCRDRegistrationController (pkg/controlplane/controller/crdregistration/crdregistration_controller.go:64)


NewCRDRegistrationController returns a controller which will register CRD GroupVersions with the auto APIService registration
controller so they automatically stay in sync.


```go
func NewCRDRegistrationController((crdinformer crdinformers.CustomResourceDefinitionInformer, apiServiceRegistration AutoAPIServiceRegistration)) (crdinformer crdinformers.CustomResourceDefinitionInformer, apiServiceRegistration AutoAPIServiceRegistration)
```


**Тип ответа:** crdinformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** crdinformers.CustomResourceDefinitionInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiServiceRegistration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AutoAPIServiceRegistration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/crdregistration/crdregistration_controller.go:64`



---


[function] name: Run file: pkg/controlplane/controller/crdregistration/crdregistration_controller.go:109 returns_error: нет description: —


### Run (pkg/controlplane/controller/crdregistration/crdregistration_controller.go:109)


Run is a method that performs operations based on the provided parameters and returns (workers int, stopCh <-chan struct{}).


```go
func (c *crdRegistrationController) Run((workers int, stopCh <-chan struct{})) (workers int, stopCh <-chan struct{})
```


**Тип ответа:** workers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/controlplane/controller/crdregistration/crdregistration_controller.go:109`



---


[function] name: WaitForInitialSync file: pkg/controlplane/controller/crdregistration/crdregistration_controller.go:148 returns_error: нет description: WaitForInitialSync blocks until the initial set of CRD resources has been processed


### WaitForInitialSync (pkg/controlplane/controller/crdregistration/crdregistration_controller.go:148)


WaitForInitialSync blocks until the initial set of CRD resources has been processed


```go
func (c *crdRegistrationController) WaitForInitialSync(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/crdregistration/crdregistration_controller.go:148`



---


[function] name: enqueueCRD file: pkg/controlplane/controller/crdregistration/crdregistration_controller.go:190 returns_error: нет description: —


### enqueueCRD (pkg/controlplane/controller/crdregistration/crdregistration_controller.go:190)


enqueueCRD is a method that performs operations based on the provided parameters and returns (crd *apiextensionsv1.CustomResourceDefinition).


```go
func (c *crdRegistrationController) enqueueCRD((crd *apiextensionsv1.CustomResourceDefinition)) (crd *apiextensionsv1.CustomResourceDefinition)
```


**Тип запроса:** apiextensionsv1.CustomResourceDefinition


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** crd


```json
{
  "versionDiscoveryHandler": null,
  "groupDiscoveryHandler": null,
  "customStorageLock": {},
  "customStorage": {},
  "crdLister": {},
  "delegate": {},
  "restOptionsGetter": {},
  "admission": {},
  "establishingController": null,
  "masterCount": 0,
  "converterFactory": null,
  "authorizer": {},
  "requestTimeout": {},
  "minRequestTimeout": {},
  "staticOpenAPISpec": {},
  "maxRequestBodyBytes": 0
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/customresource_handler.go`


**Тип ответа:** apiextensionsv1.CustomResourceDefinition


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


📍 *Расположение:* `pkg/controlplane/controller/crdregistration/crdregistration_controller.go:190`



---


[function] name: handleVersionUpdate file: pkg/controlplane/controller/crdregistration/crdregistration_controller.go:196 returns_error: нет description: —


### handleVersionUpdate (pkg/controlplane/controller/crdregistration/crdregistration_controller.go:196)


handleVersionUpdate is a method that performs operations based on the provided parameters and returns (groupVersion schema.GroupVersion).


```go
func (c *crdRegistrationController) handleVersionUpdate((groupVersion schema.GroupVersion)) (groupVersion schema.GroupVersion)
```


**Тип ответа:** groupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `pkg/apis/admissionregistration/validation/validation.go`


**Тип ответа:** schema.GroupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


📍 *Расположение:* `pkg/controlplane/controller/crdregistration/crdregistration_controller.go:196`



---


[function] name: processNextWorkItem file: pkg/controlplane/controller/crdregistration/crdregistration_controller.go:160 returns_error: нет description: processNextWorkItem deals with one key off the queue.  It returns false when it's time to quit.


### processNextWorkItem (pkg/controlplane/controller/crdregistration/crdregistration_controller.go:160)


processNextWorkItem deals with one key off the queue.  It returns false when it's time to quit.


```go
func (c *crdRegistrationController) processNextWorkItem(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/crdregistration/crdregistration_controller.go:160`



---


[function] name: runWorker file: pkg/controlplane/controller/crdregistration/crdregistration_controller.go:152 returns_error: нет description: —


### runWorker (pkg/controlplane/controller/crdregistration/crdregistration_controller.go:152)


runWorker is a method that performs operations based on the provided parameters and returns ().


```go
func (c *crdRegistrationController) runWorker(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/crdregistration/crdregistration_controller.go:152`




## pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go


📄 Исходный файл: `pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewController](#newcontroller-pkgcontrolplanecontrollerdefaultservicecidrdefault_servicecidr_controllergo54) `:54`

- 🔗 [Start](#start-pkgcontrolplanecontrollerdefaultservicecidrdefault_servicecidr_controllergo101) `:101`

- 🔗 [sync](#sync-pkgcontrolplanecontrollerdefaultservicecidrdefault_servicecidr_controllergo142) `:142`

- 🔗 [syncStatus](#syncstatus-pkgcontrolplanecontrollerdefaultservicecidrdefault_servicecidr_controllergo187) `:187`


</details>


[function] name: NewController file: pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:54 returns_error: нет description: NewController returns a new *Controller that generates the default ServiceCIDR
from the `--service-cluster-ip-range` fla


### NewController (pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:54)


NewController returns a new *Controller that generates the default ServiceCIDR
from the `--service-cluster-ip-range` flag and recreates it if necessary,
but doesn't update it if is different.
It follows the same logic that the kubernetes.default Service.


```go
func NewController((
	primaryRange net.IPNet,
	secondaryRange net.IPNet,
	client clientset.Interface,
)) (
	primaryRange net.IPNet,
	secondaryRange net.IPNet,
	client clientset.Interface,
)
```


**Тип ответа:** primaryRange


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** secondaryRange


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** client


```json
{
  "mutex": {},
  "resource": "string",
  "socket": "string",
  "grpc": null,
  "handler": {},
  "client": {}
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/plugin/v1beta1/client.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:54`



---


[function] name: Start file: pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:101 returns_error: нет description: Start will not return until the default ServiceCIDR exists or stopCh is closed.


### Start (pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:101)


Start will not return until the default ServiceCIDR exists or stopCh is closed.


```go
func (c *Controller) Start((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:101`



---


[function] name: sync file: pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:142 returns_error: нет description: —


### sync (pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:142)


sync is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Controller) sync(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:142`



---


[function] name: syncStatus file: pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:187 returns_error: нет description: —


### syncStatus (pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:187)


syncStatus is a method that performs operations based on the provided parameters and returns (serviceCIDR *networkingapiv1.ServiceCIDR).


```go
func (c *Controller) syncStatus((serviceCIDR *networkingapiv1.ServiceCIDR)) (serviceCIDR *networkingapiv1.ServiceCIDR)
```


**Тип запроса:** networkingapiv1.ServiceCIDR


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/networking/types.go`


**Тип ответа:** serviceCIDR


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/networking/v1beta1/servicecidr.go`


**Тип ответа:** networkingapiv1.ServiceCIDR


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/networking/types.go`


📍 *Расположение:* `pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go:187`




## pkg/controlplane/controller/kubernetesservice/controller.go


📄 Исходный файл: `pkg/controlplane/controller/kubernetesservice/controller.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [CreateOrUpdateMasterServiceIfNeeded](#createorupdatemasterserviceifneeded-pkgcontrolplanecontrollerkubernetesservicecontrollergo212) `:212`

- 🔗 [New](#new-pkgcontrolplanecontrollerkubernetesservicecontrollergo75) `:75`

- 🔗 [Run](#run-pkgcontrolplanecontrollerkubernetesservicecontrollergo146) `:146`

- 🔗 [Start](#start-pkgcontrolplanecontrollerkubernetesservicecontrollergo87) `:87`

- 🔗 [Stop](#stop-pkgcontrolplanecontrollerkubernetesservicecontrollergo113) `:113`

- 🔗 [UpdateKubernetesService](#updatekubernetesservice-pkgcontrolplanecontrollerkubernetesservicecontrollergo169) `:169`

- 🔗 [checkServiceFormat](#checkserviceformat-pkgcontrolplanecontrollerkubernetesservicecontrollergo266) `:266`

- 🔗 [createEndpointPortSpec](#createendpointportspec-pkgcontrolplanecontrollerkubernetesservicecontrollergo202) `:202`

- 🔗 [createPortAndServiceSpec](#createportandservicespec-pkgcontrolplanecontrollerkubernetesservicecontrollergo184) `:184`

- 🔗 [getMasterServiceUpdateIfNeeded](#getmasterserviceupdateifneeded-pkgcontrolplanecontrollerkubernetesservicecontrollergo251) `:251`


</details>


[function] name: CreateOrUpdateMasterServiceIfNeeded file: pkg/controlplane/controller/kubernetesservice/controller.go:212 returns_error: нет description: CreateOrUpdateMasterServiceIfNeeded will create the specified service if it
doesn't already exist.


### CreateOrUpdateMasterServiceIfNeeded (pkg/controlplane/controller/kubernetesservice/controller.go:212)


CreateOrUpdateMasterServiceIfNeeded will create the specified service if it
doesn't already exist.


```go
func (c *Controller) CreateOrUpdateMasterServiceIfNeeded((serviceName string, serviceIP net.IP, servicePorts []corev1.ServicePort, serviceType corev1.ServiceType, reconcile bool)) (serviceName string, serviceIP net.IP, servicePorts []corev1.ServicePort, serviceType corev1.ServiceType, reconcile bool)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** serviceIP


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** servicePorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** serviceType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ServiceType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reconcile


```json
{
  "operationExecutor": {},
  "loopSleepDuration": {},
  "desiredStateOfWorld": {},
  "actualStateOfWorld": {},
  "handlers": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/reconciler/reconciler.go`


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:212`



---


[function] name: New file: pkg/controlplane/controller/kubernetesservice/controller.go:75 returns_error: нет description: New returns a controller for watching the kubernetes service endpoints.


### New (pkg/controlplane/controller/kubernetesservice/controller.go:75)


New returns a controller for watching the kubernetes service endpoints.


```go
func New((config Config, client kubernetes.Interface, serviceInformer v1informers.ServiceInformer)) (config Config, client kubernetes.Interface, serviceInformer v1informers.ServiceInformer)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** client


```json
{
  "mutex": {},
  "resource": "string",
  "socket": "string",
  "grpc": null,
  "handler": {},
  "client": {}
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/plugin/v1beta1/client.go`


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** serviceInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** v1informers.ServiceInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/client/informers/externalversions/apiregistration/v1beta1/apiservice.go`


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:75`



---


[function] name: Run file: pkg/controlplane/controller/kubernetesservice/controller.go:146 returns_error: нет description: Run periodically updates the kubernetes service


### Run (pkg/controlplane/controller/kubernetesservice/controller.go:146)


Run periodically updates the kubernetes service


```go
func (c *Controller) Run((ch <-chan struct{})) (ch <-chan struct{})
```


**Тип ответа:** ch


```json
{
  "Directory": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:146`



---


[function] name: Start file: pkg/controlplane/controller/kubernetesservice/controller.go:87 returns_error: нет description: Start begins the core controller loops that must exist for bootstrapping
a cluster.


### Start (pkg/controlplane/controller/kubernetesservice/controller.go:87)


Start begins the core controller loops that must exist for bootstrapping
a cluster.


```go
func (c *Controller) Start((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:87`



---


[function] name: Stop file: pkg/controlplane/controller/kubernetesservice/controller.go:113 returns_error: нет description: Stop cleans up this API Servers endpoint reconciliation leases so another master can take over more quickly.


### Stop (pkg/controlplane/controller/kubernetesservice/controller.go:113)


Stop cleans up this API Servers endpoint reconciliation leases so another master can take over more quickly.


```go
func (c *Controller) Stop(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:113`



---


[function] name: UpdateKubernetesService file: pkg/controlplane/controller/kubernetesservice/controller.go:169 returns_error: нет description: UpdateKubernetesService attempts to update the default Kube service.


### UpdateKubernetesService (pkg/controlplane/controller/kubernetesservice/controller.go:169)


UpdateKubernetesService attempts to update the default Kube service.


```go
func (c *Controller) UpdateKubernetesService((reconcile bool)) (reconcile bool)
```


**Тип ответа:** reconcile


```json
{
  "operationExecutor": {},
  "loopSleepDuration": {},
  "desiredStateOfWorld": {},
  "actualStateOfWorld": {},
  "handlers": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/reconciler/reconciler.go`


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:169`



---


[function] name: checkServiceFormat file: pkg/controlplane/controller/kubernetesservice/controller.go:266 returns_error: нет description: Determine if the service is in the correct format
getMasterServiceUpdateIfNeeded expects (servicePorts are correct
and s


### checkServiceFormat (pkg/controlplane/controller/kubernetesservice/controller.go:266)


Determine if the service is in the correct format
getMasterServiceUpdateIfNeeded expects (servicePorts are correct
and service type matches).


```go
func checkServiceFormat((formatCorrect bool)) (formatCorrect bool)
```


**Тип ответа:** formatCorrect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:266`



---


[function] name: createEndpointPortSpec file: pkg/controlplane/controller/kubernetesservice/controller.go:202 returns_error: нет description: createEndpointPortSpec creates the endpoint ports


### createEndpointPortSpec (pkg/controlplane/controller/kubernetesservice/controller.go:202)


createEndpointPortSpec creates the endpoint ports


```go
func createEndpointPortSpec((endpointPort int, endpointPortName string)) (endpointPort int, endpointPortName string)
```


**Тип ответа:** endpointPort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:202`



---


[function] name: createPortAndServiceSpec file: pkg/controlplane/controller/kubernetesservice/controller.go:184 returns_error: нет description: createPortAndServiceSpec creates an array of service ports.
If the NodePort value is 0, just the servicePort is used, ot


### createPortAndServiceSpec (pkg/controlplane/controller/kubernetesservice/controller.go:184)


createPortAndServiceSpec creates an array of service ports.
If the NodePort value is 0, just the servicePort is used, otherwise, a node port is exposed.


```go
func createPortAndServiceSpec(([]corev1.ServicePort, corev1.ServiceType)) ([]corev1.ServicePort, corev1.ServiceType)
```


**Тип ответа:** corev1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.ServiceType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:184`



---


[function] name: getMasterServiceUpdateIfNeeded file: pkg/controlplane/controller/kubernetesservice/controller.go:251 returns_error: нет description: getMasterServiceUpdateIfNeeded sets service attributes for the given apiserver service.


### getMasterServiceUpdateIfNeeded (pkg/controlplane/controller/kubernetesservice/controller.go:251)


getMasterServiceUpdateIfNeeded sets service attributes for the given apiserver service.


```go
func getMasterServiceUpdateIfNeeded((s *corev1.Service, updated bool)) (s *corev1.Service, updated bool)
```


**Тип запроса:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** updated


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/kubernetesservice/controller.go:251`




## pkg/controlplane/controller/leaderelection/election.go


📄 Исходный файл: `pkg/controlplane/controller/leaderelection/election.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [compare](#compare-pkgcontrolplanecontrollerleaderelectionelectiongo93) `:93`

- 🔗 [getBinaryVersionOrZero](#getbinaryversionorzero-pkgcontrolplanecontrollerleaderelectionelectiongo83) `:83`

- 🔗 [getEmulationVersionOrZero](#getemulationversionorzero-pkgcontrolplanecontrollerleaderelectionelectiongo74) `:74`

- 🔗 [isLeaseCandidateExpired](#isleasecandidateexpired-pkgcontrolplanecontrollerleaderelectionelectiongo118) `:118`

- 🔗 [isLeaseExpired](#isleaseexpired-pkgcontrolplanecontrollerleaderelectionelectiongo111) `:111`

- 🔗 [pickBestLeaderOldestEmulationVersion](#pickbestleaderoldestemulationversion-pkgcontrolplanecontrollerleaderelectionelectiongo29) `:29`

- 🔗 [pickBestStrategy](#pickbeststrategy-pkgcontrolplanecontrollerleaderelectionelectiongo42) `:42`

- 🔗 [validLeaseCandidateForOldestEmulationVersion](#validleasecandidateforoldestemulationversion-pkgcontrolplanecontrollerleaderelectionelectiongo65) `:65`


</details>


[function] name: compare file: pkg/controlplane/controller/leaderelection/election.go:93 returns_error: нет description: -1: lhs better, 1: rhs better


### compare (pkg/controlplane/controller/leaderelection/election.go:93)


-1: lhs better, 1: rhs better


```go
func compare((lhs, rhs *v1beta1.LeaseCandidate)) (lhs, rhs *v1beta1.LeaseCandidate)
```


**Тип запроса:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** lhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:93`



---


[function] name: getBinaryVersionOrZero file: pkg/controlplane/controller/leaderelection/election.go:83 returns_error: нет description: —


### getBinaryVersionOrZero (pkg/controlplane/controller/leaderelection/election.go:83)


getBinaryVersionOrZero is a function that performs operations based on the provided parameters and returns (l *v1beta1.LeaseCandidate).


```go
func getBinaryVersionOrZero((l *v1beta1.LeaseCandidate)) (l *v1beta1.LeaseCandidate)
```


**Тип запроса:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** l


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


**Тип ответа:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:83`



---


[function] name: getEmulationVersionOrZero file: pkg/controlplane/controller/leaderelection/election.go:74 returns_error: нет description: —


### getEmulationVersionOrZero (pkg/controlplane/controller/leaderelection/election.go:74)


getEmulationVersionOrZero is a function that performs operations based on the provided parameters and returns (l *v1beta1.LeaseCandidate).


```go
func getEmulationVersionOrZero((l *v1beta1.LeaseCandidate)) (l *v1beta1.LeaseCandidate)
```


**Тип запроса:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** l


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


**Тип ответа:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:74`



---


[function] name: isLeaseCandidateExpired file: pkg/controlplane/controller/leaderelection/election.go:118 returns_error: нет description: —


### isLeaseCandidateExpired (pkg/controlplane/controller/leaderelection/election.go:118)


isLeaseCandidateExpired is a function that performs operations based on the provided parameters and returns (clock clock.Clock, lease *v1beta1.LeaseCandidate).


```go
func isLeaseCandidateExpired((clock clock.Clock, lease *v1beta1.LeaseCandidate)) (clock clock.Clock, lease *v1beta1.LeaseCandidate)
```


**Тип запроса:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clock.Clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lease


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/coordination/v1beta1/lease.go`


**Тип ответа:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:118`



---


[function] name: isLeaseExpired file: pkg/controlplane/controller/leaderelection/election.go:111 returns_error: нет description: —


### isLeaseExpired (pkg/controlplane/controller/leaderelection/election.go:111)


isLeaseExpired is a function that performs operations based on the provided parameters and returns (clock clock.Clock, lease *v1.Lease).


```go
func isLeaseExpired((clock clock.Clock, lease *v1.Lease)) (clock clock.Clock, lease *v1.Lease)
```


**Тип запроса:** v1.Lease


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clock.Clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lease


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/coordination/v1beta1/lease.go`


**Тип ответа:** v1.Lease


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:111`



---


[function] name: pickBestLeaderOldestEmulationVersion file: pkg/controlplane/controller/leaderelection/election.go:29 returns_error: нет description: —


### pickBestLeaderOldestEmulationVersion (pkg/controlplane/controller/leaderelection/election.go:29)


pickBestLeaderOldestEmulationVersion is a function that performs operations based on the provided parameters and returns (candidates []*v1beta1.LeaseCandidate).


```go
func pickBestLeaderOldestEmulationVersion((candidates []*v1beta1.LeaseCandidate)) (candidates []*v1beta1.LeaseCandidate)
```


**Тип запроса:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** candidates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:29`



---


[function] name: pickBestStrategy file: pkg/controlplane/controller/leaderelection/election.go:42 returns_error: да description: —


### pickBestStrategy (pkg/controlplane/controller/leaderelection/election.go:42)


pickBestStrategy is a function that performs operations based on the provided parameters and may return an error.


```go
func pickBestStrategy((v1.CoordinatedLeaseStrategy, error)) (v1.CoordinatedLeaseStrategy, error)
```


**Тип ответа:** v1.CoordinatedLeaseStrategy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `v1.CoordinatedLeaseStrategy`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:42`



---


[function] name: validLeaseCandidateForOldestEmulationVersion file: pkg/controlplane/controller/leaderelection/election.go:65 returns_error: нет description: —


### validLeaseCandidateForOldestEmulationVersion (pkg/controlplane/controller/leaderelection/election.go:65)


validLeaseCandidateForOldestEmulationVersion is a function that performs operations based on the provided parameters and returns (l *v1beta1.LeaseCandidate).


```go
func validLeaseCandidateForOldestEmulationVersion((l *v1beta1.LeaseCandidate)) (l *v1beta1.LeaseCandidate)
```


**Тип запроса:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** l


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


**Тип ответа:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/election.go:65`




## pkg/controlplane/controller/leaderelection/leaderelection_controller.go


📄 Исходный файл: `pkg/controlplane/controller/leaderelection/leaderelection_controller.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [NewController](#newcontroller-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo113) `:113`

- 🔗 [Run](#run-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo77) `:77`

- 🔗 [electionNeeded](#electionneeded-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo200) `:200`

- 🔗 [enqueueCandidate](#enqueuecandidate-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo177) `:177`

- 🔗 [enqueueLease](#enqueuelease-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo192) `:192`

- 🔗 [listAdmissableCandidates](#listadmissablecandidates-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo425) `:425`

- 🔗 [processNextElectionItem](#processnextelectionitem-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo162) `:162`

- 🔗 [reconcileElectionStep](#reconcileelectionstep-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo248) `:248`

- 🔗 [runElectionWorker](#runelectionworker-pkgcontrolplanecontrollerleaderelectionleaderelection_controllergo157) `:157`


</details>


[function] name: NewController file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:113 returns_error: да description: —


### NewController (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:113)


NewController is a function that performs operations based on the provided parameters and may return an error.


```go
func NewController((*Controller, error)) (*Controller, error)
```


**Тип запроса:** Controller


```json
{
  "cidrs": [],
  "client": {},
  "eventBroadcaster": {},
  "eventRecorder": {},
  "serviceCIDRInformer": {},
  "serviceCIDRLister": {},
  "serviceCIDRsSynced": {},
  "interval": {},
  "reportedMismatchedCIDRs": false,
  "reportedNotReadyCondition": false
}
```


*Определено в:* `pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go`


**Тип ответа:** Controller


```json
{
  "cidrs": [],
  "client": {},
  "eventBroadcaster": {},
  "eventRecorder": {},
  "serviceCIDRInformer": {},
  "serviceCIDRLister": {},
  "serviceCIDRsSynced": {},
  "interval": {},
  "reportedMismatchedCIDRs": false,
  "reportedNotReadyCondition": false
}
```


*Определено в:* `pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:113`



---


[function] name: Run file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:77 returns_error: нет description: —


### Run (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:77)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context, workers int).


```go
func (c *Controller) Run((ctx context.Context, workers int)) (ctx context.Context, workers int)
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


**Тип ответа:** workers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:77`



---


[function] name: electionNeeded file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:200 returns_error: да description: —


### electionNeeded (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:200)


electionNeeded is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *Controller) electionNeeded((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:200`



---


[function] name: enqueueCandidate file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:177 returns_error: нет description: —


### enqueueCandidate (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:177)


enqueueCandidate is a method that performs operations based on the provided parameters and returns (obj any).


```go
func (c *Controller) enqueueCandidate((obj any)) (obj any)
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:177`



---


[function] name: enqueueLease file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:192 returns_error: нет description: —


### enqueueLease (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:192)


enqueueLease is a method that performs operations based on the provided parameters and returns (obj any).


```go
func (c *Controller) enqueueLease((obj any)) (obj any)
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:192`



---


[function] name: listAdmissableCandidates file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:425 returns_error: да description: —


### listAdmissableCandidates (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:425)


listAdmissableCandidates is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *Controller) listAdmissableCandidates(([]*v1beta1.LeaseCandidate, error)) ([]*v1beta1.LeaseCandidate, error)
```


**Тип запроса:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Тип ответа:** v1beta1.LeaseCandidate


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/coordination/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*v1beta1.LeaseCandidate`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:425`



---


[function] name: processNextElectionItem file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:162 returns_error: нет description: —


### processNextElectionItem (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:162)


processNextElectionItem is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) processNextElectionItem((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:162`



---


[function] name: reconcileElectionStep file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:248 returns_error: да description: reconcileElectionStep steps through a step in an election.
A step looks at the current state of Lease and LeaseCandidate


### reconcileElectionStep (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:248)


reconcileElectionStep steps through a step in an election.
A step looks at the current state of Lease and LeaseCandidates and takes one of the following action
- do nothing (because leader is already optimal or still waiting for an event)
- request ack from candidates (update LeaseCandidate PingTime)
- finds the most optimal candidate and elect (update the Lease object)
Instead of keeping a map and lock on election, the state is
calculated every time by looking at the lease, and set of available candidates.
PingTime + electionDuration > time.Now: We just asked all candidates to ack and are still waiting for response
PingTime + electionDuration < time.Now: Candidate has not responded within the appropriate PingTime. Continue the election.
RenewTime + 5 seconds > time.Now: All candidates acked in the last 5 seconds, continue the election.


```go
func (c *Controller) reconcileElectionStep((requeue time.Duration, err error)) (requeue time.Duration, err error)
```


**Тип ответа:** requeue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


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


*Типы возврата:* `requeue time.Duration`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:248`



---


[function] name: runElectionWorker file: pkg/controlplane/controller/leaderelection/leaderelection_controller.go:157 returns_error: нет description: —


### runElectionWorker (pkg/controlplane/controller/leaderelection/leaderelection_controller.go:157)


runElectionWorker is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) runElectionWorker((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leaderelection_controller.go:157`




## pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go


📄 Исходный файл: `pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [NewLeaseCandidateGC](#newleasecandidategc-pkgcontrolplanecontrollerleaderelectionleasecandidategc_controllergo51) `:51`

- 🔗 [Run](#run-pkgcontrolplanecontrollerleaderelectionleasecandidategc_controllergo63) `:63`

- 🔗 [gc](#gc-pkgcontrolplanecontrollerleaderelectionleasecandidategc_controllergo79) `:79`


</details>


[function] name: NewLeaseCandidateGC file: pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:51 returns_error: нет description: NewLeaseCandidateGC creates a new LeaseCandidateGCController.


### NewLeaseCandidateGC (pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:51)


NewLeaseCandidateGC creates a new LeaseCandidateGCController.


```go
func NewLeaseCandidateGC((clientset kubernetes.Interface, gcCheckPeriod time.Duration, leaseCandidateInformer coordinationv1beta1informers.LeaseCandidateInformer)) (clientset kubernetes.Interface, gcCheckPeriod time.Duration, leaseCandidateInformer coordinationv1beta1informers.LeaseCandidateInformer)
```


**Тип ответа:** clientset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** gcCheckPeriod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** leaseCandidateInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/coordination/v1beta1/leasecandidate.go`


**Тип ответа:** coordinationv1beta1informers.LeaseCandidateInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:51`



---


[function] name: Run file: pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:63 returns_error: нет description: Run starts one worker.


### Run (pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:63)


Run starts one worker.


```go
func (c *LeaseCandidateGCController) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:63`



---


[function] name: gc file: pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:79 returns_error: нет description: —


### gc (pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:79)


gc is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *LeaseCandidateGCController) gc((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go:79`




## pkg/controlplane/controller/leaderelection/run_with_leaderelection.go


📄 Исходный файл: `pkg/controlplane/controller/leaderelection/run_with_leaderelection.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RunWithLeaderElection](#runwithleaderelection-pkgcontrolplanecontrollerleaderelectionrun_with_leaderelectiongo45) `:45`


</details>


[function] name: RunWithLeaderElection file: pkg/controlplane/controller/leaderelection/run_with_leaderelection.go:45 returns_error: нет description: RunWithLeaderElection runs the provided runner function with leader election.
newRunnerFn might be called multiple times


### RunWithLeaderElection (pkg/controlplane/controller/leaderelection/run_with_leaderelection.go:45)


RunWithLeaderElection runs the provided runner function with leader election.
newRunnerFn might be called multiple times, and it should return another
controller instance's Run method each time.
RunWithLeaderElection only returns when the context is done, or initial
leader election fails.


```go
func RunWithLeaderElection((ctx context.Context, config *rest.Config, newRunnerFn NewRunner, timers LeaderElectionTimers)) (ctx context.Context, config *rest.Config, newRunnerFn NewRunner, timers LeaderElectionTimers)
```


**Тип запроса:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


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


**Тип ответа:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** newRunnerFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** NewRunner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** timers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LeaderElectionTimers


```json
{
  "LeaseDuration": {},
  "RenewDeadline": {},
  "RetryPeriod": {}
}
```


*Определено в:* `pkg/controlplane/controller/leaderelection/run_with_leaderelection.go`


📍 *Расположение:* `pkg/controlplane/controller/leaderelection/run_with_leaderelection.go:45`




## pkg/controlplane/controller/legacytokentracking/controller.go


📄 Исходный файл: `pkg/controlplane/controller/legacytokentracking/controller.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [NewController](#newcontroller-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo72) `:72`

- 🔗 [Run](#run-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo116) `:116`

- 🔗 [RunWithContext](#runwithcontext-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo121) `:121`

- 🔗 [enqueue](#enqueue-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo109) `:109`

- 🔗 [newController](#newcontroller-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo76) `:76`

- 🔗 [processNext](#processnext-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo148) `:148`

- 🔗 [runWorker](#runworker-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo143) `:143`

- 🔗 [syncConfigMap](#syncconfigmap-pkgcontrolplanecontrollerlegacytokentrackingcontrollergo164) `:164`


</details>


[function] name: NewController file: pkg/controlplane/controller/legacytokentracking/controller.go:72 returns_error: нет description: NewController returns a Controller struct.


### NewController (pkg/controlplane/controller/legacytokentracking/controller.go:72)


NewController returns a Controller struct.


```go
func NewController((cs kubernetes.Interface)) (cs kubernetes.Interface)
```


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:72`



---


[function] name: Run file: pkg/controlplane/controller/legacytokentracking/controller.go:116 returns_error: нет description: Run starts the controller sync loop.

logcheck:context // RunWithContext should be used instead of Run in code which sup


### Run (pkg/controlplane/controller/legacytokentracking/controller.go:116)


Run starts the controller sync loop.

logcheck:context // RunWithContext should be used instead of Run in code which supports contextual logging.


```go
func (c *Controller) Run((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:116`



---


[function] name: RunWithContext file: pkg/controlplane/controller/legacytokentracking/controller.go:121 returns_error: нет description: RunWithContext starts the controller sync loop with a context.


### RunWithContext (pkg/controlplane/controller/legacytokentracking/controller.go:121)


RunWithContext starts the controller sync loop with a context.


```go
func (c *Controller) RunWithContext((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:121`



---


[function] name: enqueue file: pkg/controlplane/controller/legacytokentracking/controller.go:109 returns_error: нет description: —


### enqueue (pkg/controlplane/controller/legacytokentracking/controller.go:109)


enqueue is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Controller) enqueue(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:109`



---


[function] name: newController file: pkg/controlplane/controller/legacytokentracking/controller.go:76 returns_error: нет description: —


### newController (pkg/controlplane/controller/legacytokentracking/controller.go:76)


newController is a function that performs operations based on the provided parameters and returns (cs kubernetes.Interface, cl clock.Clock, limiter *rate.Limiter).


```go
func newController((cs kubernetes.Interface, cl clock.Clock, limiter *rate.Limiter)) (cs kubernetes.Interface, cl clock.Clock, limiter *rate.Limiter)
```


**Тип запроса:** rate.Limiter


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** cl


```json
{
  "CAKey": {},
  "Organizations": []
}
```


*Определено в:* `cmd/kubeadm/app/phases/kubeconfig/kubeconfig.go`


**Тип ответа:** clock.Clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** limiter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rate.Limiter


```json
{
  "limiter": null,
  "qps": 0.0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/util/flowcontrol/throttle.go`


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:76`



---


[function] name: processNext file: pkg/controlplane/controller/legacytokentracking/controller.go:148 returns_error: нет description: —


### processNext (pkg/controlplane/controller/legacytokentracking/controller.go:148)


processNext is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) processNext((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:148`



---


[function] name: runWorker file: pkg/controlplane/controller/legacytokentracking/controller.go:143 returns_error: нет description: —


### runWorker (pkg/controlplane/controller/legacytokentracking/controller.go:143)


runWorker is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) runWorker((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:143`



---


[function] name: syncConfigMap file: pkg/controlplane/controller/legacytokentracking/controller.go:164 returns_error: нет description: —


### syncConfigMap (pkg/controlplane/controller/legacytokentracking/controller.go:164)


syncConfigMap is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) syncConfigMap((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/controlplane/controller/legacytokentracking/controller.go:164`




## pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go


📄 Исходный файл: `pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewController](#newcontroller-pkgcontrolplanecontrollersystemnamespacessystem_namespaces_controllergo49) `:49`

- 🔗 [Run](#run-pkgcontrolplanecontrollersystemnamespacessystem_namespaces_controllergo62) `:62`

- 🔗 [createNamespaceIfNeeded](#createnamespaceifneeded-pkgcontrolplanecontrollersystemnamespacessystem_namespaces_controllergo87) `:87`

- 🔗 [sync](#sync-pkgcontrolplanecontrollersystemnamespacessystem_namespaces_controllergo78) `:78`


</details>


[function] name: NewController file: pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:49 returns_error: нет description: NewController creates a new Controller to ensure system namespaces exist.


### NewController (pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:49)


NewController creates a new Controller to ensure system namespaces exist.


```go
func NewController((systemNamespaces []string, clientset kubernetes.Interface, namespaceInformer coreinformers.NamespaceInformer)) (systemNamespaces []string, clientset kubernetes.Interface, namespaceInformer coreinformers.NamespaceInformer)
```


**Тип ответа:** systemNamespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** namespaceInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/namespace.go`


**Тип ответа:** coreinformers.NamespaceInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:49`



---


[function] name: Run file: pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:62 returns_error: нет description: Run starts one worker.


### Run (pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:62)


Run starts one worker.


```go
func (c *Controller) Run((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:62`



---


[function] name: createNamespaceIfNeeded file: pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:87 returns_error: нет description: —


### createNamespaceIfNeeded (pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:87)


createNamespaceIfNeeded is a method that performs operations based on the provided parameters and returns (ns string).


```go
func (c *Controller) createNamespaceIfNeeded((ns string)) (ns string)
```


**Тип ответа:** ns


```json
{
  "Generic": null,
  "KubeCloudShared": null,
  "ServiceController": null,
  "AttachDetachController": null,
  "CSRSigningController": null,
  "DaemonSetController": null,
  "DeploymentController": null,
  "DeviceTaintEvictionController": null,
  "ResourceClaimController": null,
  "StatefulSetController": null,
  "DeprecatedFlags": null,
  "EndpointController": null,
  "EndpointSliceController": null,
  "EndpointSliceMirroringController": null,
  "EphemeralVolumeController": null,
  "GarbageCollectorController": null,
  "HPAController": null,
  "JobController": null,
  "CronJobController": null,
  "LegacySATokenCleaner": null,
  "NamespaceController": null,
  "NodeIPAMController": null,
  "NodeLifecycleController": null,
  "PersistentVolumeBinderController": null,
  "PodGCController": null,
  "ReplicaSetController": null,
  "ReplicationController": null,
  "ResourceQuotaController": null,
  "SAController": null,
  "TTLAfterFinishedController": null,
  "ValidatingAdmissionPolicyStatusController": null,
  "SecureServing": null,
  "Authentication": null,
  "Authorization": null,
  "Metrics": null,
  "Logs": null,
  "Master": "string",
  "ShowHiddenMetricsForVersion": "string",
  "ControllerShutdownTimeout": {},
  "ComponentGlobalsRegistry": {},
  "ParsedFlags": null
}
```


*Определено в:* `cmd/kube-controller-manager/app/options/options.go`


📍 *Расположение:* `pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:87`



---


[function] name: sync file: pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:78 returns_error: нет description: —


### sync (pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:78)


sync is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Controller) sync(()) ()
```


📍 *Расположение:* `pkg/controlplane/controller/systemnamespaces/system_namespaces_controller.go:78`




## pkg/controlplane/instance.go


📄 Исходный файл: `pkg/controlplane/instance.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [Complete](#complete-pkgcontrolplaneinstancego256) `:256`

- 🔗 [DefaultAPIResourceConfigSource](#defaultapiresourceconfigsource-pkgcontrolplaneinstancego521) `:521`

- 🔗 [DefaultGenericAPIResourceConfigSource](#defaultgenericapiresourceconfigsource-pkgcontrolplaneinstancego510) `:510`

- 🔗 [New](#new-pkgcontrolplaneinstancego317) `:317`

- 🔗 [StorageProviders](#storageproviders-pkgcontrolplaneinstancego387) `:387`

- 🔗 [createEndpointReconciler](#createendpointreconciler-pkgcontrolplaneinstancego239) `:239`

- 🔗 [createLeaseReconciler](#createleasereconciler-pkgcontrolplaneinstancego221) `:221`

- 🔗 [createMasterCountReconciler](#createmastercountreconciler-pkgcontrolplaneinstancego209) `:209`

- 🔗 [createNoneReconciler](#createnonereconciler-pkgcontrolplaneinstancego217) `:217`


</details>


[function] name: Complete file: pkg/controlplane/instance.go:256 returns_error: нет description: Complete fills in any fields not set that are required to have valid data. It's mutating the receiver.


### Complete (pkg/controlplane/instance.go:256)


Complete fills in any fields not set that are required to have valid data. It's mutating the receiver.


```go
func (c *Config) Complete(()) ()
```


📍 *Расположение:* `pkg/controlplane/instance.go:256`



---


[function] name: DefaultAPIResourceConfigSource file: pkg/controlplane/instance.go:521 returns_error: нет description: DefaultAPIResourceConfigSource returns default configuration for resources served by kube-apiserver.


### DefaultAPIResourceConfigSource (pkg/controlplane/instance.go:521)


DefaultAPIResourceConfigSource returns default configuration for resources served by kube-apiserver.


```go
func DefaultAPIResourceConfigSource(()) ()
```


📍 *Расположение:* `pkg/controlplane/instance.go:521`



---


[function] name: DefaultGenericAPIResourceConfigSource file: pkg/controlplane/instance.go:510 returns_error: нет description: DefaultGenericAPIResourceConfigSource returns default configuration for resources served by GenericStorageProviders.


### DefaultGenericAPIResourceConfigSource (pkg/controlplane/instance.go:510)


DefaultGenericAPIResourceConfigSource returns default configuration for resources served by GenericStorageProviders.


```go
func DefaultGenericAPIResourceConfigSource(()) ()
```


📍 *Расположение:* `pkg/controlplane/instance.go:510`



---


[function] name: New file: pkg/controlplane/instance.go:317 returns_error: да description: New returns a new instance of Master from the given config.
Certain config fields will be set to a default value if unse


### New (pkg/controlplane/instance.go:317)


New returns a new instance of Master from the given config.
Certain config fields will be set to a default value if unset.
Certain config fields must be specified, including:
KubeletClientConfig


```go
func (c CompletedConfig) New((*Instance, error)) (*Instance, error)
```


**Тип запроса:** Instance


```json
{
  "ControlPlane": null
}
```


*Определено в:* `pkg/controlplane/instance.go`


**Тип ответа:** Instance


```json
{
  "ControlPlane": null
}
```


*Определено в:* `pkg/controlplane/instance.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Instance`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/instance.go:317`



---


[function] name: StorageProviders file: pkg/controlplane/instance.go:387 returns_error: да description: —


### StorageProviders (pkg/controlplane/instance.go:387)


StorageProviders is a method that performs operations based on the provided parameters and may return an error.


```go
func (c CompletedConfig) StorageProviders(([]controlplaneapiserver.RESTStorageProvider, error)) ([]controlplaneapiserver.RESTStorageProvider, error)
```


**Тип ответа:** controlplaneapiserver.RESTStorageProvider


```json
{
  "Authenticator": {},
  "APIAudiences": {}
}
```


*Определено в:* `pkg/registry/authentication/rest/storage_authentication.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]controlplaneapiserver.RESTStorageProvider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/instance.go:387`



---


[function] name: createEndpointReconciler file: pkg/controlplane/instance.go:239 returns_error: нет description: —


### createEndpointReconciler (pkg/controlplane/instance.go:239)


createEndpointReconciler is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Config) createEndpointReconciler(()) ()
```


📍 *Расположение:* `pkg/controlplane/instance.go:239`



---


[function] name: createLeaseReconciler file: pkg/controlplane/instance.go:221 returns_error: нет description: —


### createLeaseReconciler (pkg/controlplane/instance.go:221)


createLeaseReconciler is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Config) createLeaseReconciler(()) ()
```


📍 *Расположение:* `pkg/controlplane/instance.go:221`



---


[function] name: createMasterCountReconciler file: pkg/controlplane/instance.go:209 returns_error: нет description: —


### createMasterCountReconciler (pkg/controlplane/instance.go:209)


createMasterCountReconciler is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Config) createMasterCountReconciler(()) ()
```


📍 *Расположение:* `pkg/controlplane/instance.go:209`



---


[function] name: createNoneReconciler file: pkg/controlplane/instance.go:217 returns_error: нет description: —


### createNoneReconciler (pkg/controlplane/instance.go:217)


createNoneReconciler is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Config) createNoneReconciler(()) ()
```


📍 *Расположение:* `pkg/controlplane/instance.go:217`




## pkg/controlplane/reconcilers/endpointsadapter.go


📄 Исходный файл: `pkg/controlplane/reconcilers/endpointsadapter.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Create](#create-pkgcontrolplanereconcilersendpointsadaptergo62) `:62`

- 🔗 [EnsureEndpointSliceFromEndpoints](#ensureendpointslicefromendpoints-pkgcontrolplanereconcilersendpointsadaptergo83) `:83`

- 🔗 [Get](#get-pkgcontrolplanereconcilersendpointsadaptergo55) `:55`

- 🔗 [NewEndpointsAdapter](#newendpointsadapter-pkgcontrolplanereconcilersendpointsadaptergo46) `:46`

- 🔗 [Update](#update-pkgcontrolplanereconcilersendpointsadaptergo72) `:72`

- 🔗 [allAddressesIPv6](#alladdressesipv6-pkgcontrolplanereconcilersendpointsadaptergo180) `:180`

- 🔗 [endpointFromAddress](#endpointfromaddress-pkgcontrolplanereconcilersendpointsadaptergo165) `:165`

- 🔗 [endpointSliceFromEndpoints](#endpointslicefromendpoints-pkgcontrolplanereconcilersendpointsadaptergo118) `:118`

- 🔗 [getEndpointsFromAddresses](#getendpointsfromaddresses-pkgcontrolplanereconcilersendpointsadaptergo151) `:151`

- 🔗 [setSkipMirrorTrue](#setskipmirrortrue-pkgcontrolplanereconcilersendpointsadaptergo196) `:196`


</details>


[function] name: Create file: pkg/controlplane/reconcilers/endpointsadapter.go:62 returns_error: да description: Create accepts a namespace and Endpoints object and creates the Endpoints
object and matching EndpointSlice. The created


### Create (pkg/controlplane/reconcilers/endpointsadapter.go:62)


Create accepts a namespace and Endpoints object and creates the Endpoints
object and matching EndpointSlice. The created Endpoints object or an error will be
returned.


```go
func (adapter *EndpointsAdapter) Create((*corev1.Endpoints, error)) (*corev1.Endpoints, error)
```


**Тип запроса:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Endpoints`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:62`



---


[function] name: EnsureEndpointSliceFromEndpoints file: pkg/controlplane/reconcilers/endpointsadapter.go:83 returns_error: нет description: EnsureEndpointSliceFromEndpoints accepts a namespace and Endpoints resource
and creates or updates a corresponding Endpo


### EnsureEndpointSliceFromEndpoints (pkg/controlplane/reconcilers/endpointsadapter.go:83)


EnsureEndpointSliceFromEndpoints accepts a namespace and Endpoints resource
and creates or updates a corresponding EndpointSlice. An error will be returned
if it fails to sync the EndpointSlice.


```go
func (adapter *EndpointsAdapter) EnsureEndpointSliceFromEndpoints((namespace string, endpoints *corev1.Endpoints)) (namespace string, endpoints *corev1.Endpoints)
```


**Тип запроса:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:83`



---


[function] name: Get file: pkg/controlplane/reconcilers/endpointsadapter.go:55 returns_error: да description: Get takes the name and namespace of the Endpoints resource, and returns a
corresponding Endpoints object if it exists, a


### Get (pkg/controlplane/reconcilers/endpointsadapter.go:55)


Get takes the name and namespace of the Endpoints resource, and returns a
corresponding Endpoints object if it exists, and an error if there is any.


```go
func (adapter *EndpointsAdapter) Get((*corev1.Endpoints, error)) (*corev1.Endpoints, error)
```


**Тип запроса:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Endpoints`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:55`



---


[function] name: NewEndpointsAdapter file: pkg/controlplane/reconcilers/endpointsadapter.go:46 returns_error: нет description: NewEndpointsAdapter returns a new EndpointsAdapter.


### NewEndpointsAdapter (pkg/controlplane/reconcilers/endpointsadapter.go:46)


NewEndpointsAdapter returns a new EndpointsAdapter.


```go
func NewEndpointsAdapter((endpointClient corev1client.EndpointsGetter, endpointSliceClient discoveryclient.EndpointSlicesGetter)) (endpointClient corev1client.EndpointsGetter, endpointSliceClient discoveryclient.EndpointSlicesGetter)
```


**Тип ответа:** endpointClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1client.EndpointsGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointSliceClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** discoveryclient.EndpointSlicesGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:46`



---


[function] name: Update file: pkg/controlplane/reconcilers/endpointsadapter.go:72 returns_error: да description: Update accepts a namespace and Endpoints object and updates it and its
matching EndpointSlice. The updated Endpoints obj


### Update (pkg/controlplane/reconcilers/endpointsadapter.go:72)


Update accepts a namespace and Endpoints object and updates it and its
matching EndpointSlice. The updated Endpoints object or an error will be returned.


```go
func (adapter *EndpointsAdapter) Update((*corev1.Endpoints, error)) (*corev1.Endpoints, error)
```


**Тип запроса:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Endpoints`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:72`



---


[function] name: allAddressesIPv6 file: pkg/controlplane/reconcilers/endpointsadapter.go:180 returns_error: нет description: allAddressesIPv6 returns true if all provided addresses are IPv6.


### allAddressesIPv6 (pkg/controlplane/reconcilers/endpointsadapter.go:180)


allAddressesIPv6 returns true if all provided addresses are IPv6.


```go
func allAddressesIPv6((addresses []corev1.EndpointAddress)) (addresses []corev1.EndpointAddress)
```


**Тип ответа:** addresses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:180`



---


[function] name: endpointFromAddress file: pkg/controlplane/reconcilers/endpointsadapter.go:165 returns_error: нет description: endpointFromAddress generates an Endpoint from an EndpointAddress resource.


### endpointFromAddress (pkg/controlplane/reconcilers/endpointsadapter.go:165)


endpointFromAddress generates an Endpoint from an EndpointAddress resource.


```go
func endpointFromAddress((address corev1.EndpointAddress, ready bool)) (address corev1.EndpointAddress, ready bool)
```


**Тип ответа:** address


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** corev1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** ready


```json
{
  "state": {},
  "lastErr": {},
  "generation": 0,
  "lock": {},
  "restartLock": {},
  "waitCh": {},
  "clock": {},
  "lastStateChangeTime": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/ready.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:165`



---


[function] name: endpointSliceFromEndpoints file: pkg/controlplane/reconcilers/endpointsadapter.go:118 returns_error: нет description: endpointSliceFromEndpoints generates an EndpointSlice from an Endpoints
resource.


### endpointSliceFromEndpoints (pkg/controlplane/reconcilers/endpointsadapter.go:118)


endpointSliceFromEndpoints generates an EndpointSlice from an Endpoints
resource.


```go
func endpointSliceFromEndpoints((endpoints *corev1.Endpoints)) (endpoints *corev1.Endpoints)
```


**Тип запроса:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:118`



---


[function] name: getEndpointsFromAddresses file: pkg/controlplane/reconcilers/endpointsadapter.go:151 returns_error: нет description: getEndpointsFromAddresses returns a list of Endpoints from addresses that
match the provided address type.


### getEndpointsFromAddresses (pkg/controlplane/reconcilers/endpointsadapter.go:151)


getEndpointsFromAddresses returns a list of Endpoints from addresses that
match the provided address type.


```go
func getEndpointsFromAddresses((addresses []corev1.EndpointAddress, addressType discovery.AddressType, ready bool)) (addresses []corev1.EndpointAddress, addressType discovery.AddressType, ready bool)
```


**Тип ответа:** addresses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** addressType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** discovery.AddressType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ready


```json
{
  "state": {},
  "lastErr": {},
  "generation": 0,
  "lock": {},
  "restartLock": {},
  "waitCh": {},
  "clock": {},
  "lastStateChangeTime": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/ready.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:151`



---


[function] name: setSkipMirrorTrue file: pkg/controlplane/reconcilers/endpointsadapter.go:196 returns_error: нет description: setSkipMirrorTrue sets endpointslice.kubernetes.io/skip-mirror to true. It
returns true if this has resulted in a change


### setSkipMirrorTrue (pkg/controlplane/reconcilers/endpointsadapter.go:196)


setSkipMirrorTrue sets endpointslice.kubernetes.io/skip-mirror to true. It
returns true if this has resulted in a change to the Endpoints resource.


```go
func setSkipMirrorTrue((e *corev1.Endpoints)) (e *corev1.Endpoints)
```


**Тип запроса:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** e


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


**Тип ответа:** corev1.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/endpointsadapter.go:196`




## pkg/controlplane/reconcilers/instancecount.go


📄 Исходный файл: `pkg/controlplane/reconcilers/instancecount.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Destroy](#destroy-pkgcontrolplanereconcilersinstancecountgo184) `:184`

- 🔗 [NewMasterCountEndpointReconciler](#newmastercountendpointreconciler-pkgcontrolplanereconcilersinstancecountgo43) `:43`

- 🔗 [ReconcileEndpoints](#reconcileendpoints-pkgcontrolplanereconcilersinstancecountgo62) `:62`

- 🔗 [RemoveEndpoints](#removeendpoints-pkgcontrolplanereconcilersinstancecountgo145) `:145`

- 🔗 [StopReconciling](#stopreconciling-pkgcontrolplanereconcilersinstancecountgo178) `:178`

- 🔗 [checkEndpointSubsetFormat](#checkendpointsubsetformat-pkgcontrolplanereconcilersinstancecountgo195) `:195`


</details>


[function] name: Destroy file: pkg/controlplane/reconcilers/instancecount.go:184 returns_error: нет description: —


### Destroy (pkg/controlplane/reconcilers/instancecount.go:184)


Destroy is a method that performs operations based on the provided parameters and returns ().


```go
func (r *masterCountEndpointReconciler) Destroy(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/instancecount.go:184`



---


[function] name: NewMasterCountEndpointReconciler file: pkg/controlplane/reconcilers/instancecount.go:43 returns_error: нет description: NewMasterCountEndpointReconciler creates a new EndpointReconciler that reconciles based on a
specified expected number o


### NewMasterCountEndpointReconciler (pkg/controlplane/reconcilers/instancecount.go:43)


NewMasterCountEndpointReconciler creates a new EndpointReconciler that reconciles based on a
specified expected number of masters.


```go
func NewMasterCountEndpointReconciler((masterCount int, epAdapter EndpointsAdapter)) (masterCount int, epAdapter EndpointsAdapter)
```


**Тип ответа:** masterCount


```json
{
  "masterCount": 0,
  "epAdapter": {},
  "stopReconcilingCalled": false,
  "reconcilingLock": {}
}
```


*Определено в:* `pkg/controlplane/reconcilers/instancecount.go`


**Тип ответа:** epAdapter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** EndpointsAdapter


```json
{
  "endpointClient": {},
  "endpointSliceClient": {}
}
```


*Определено в:* `pkg/controlplane/reconcilers/endpointsadapter.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/instancecount.go:43`



---


[function] name: ReconcileEndpoints file: pkg/controlplane/reconcilers/instancecount.go:62 returns_error: нет description: ReconcileEndpoints sets the endpoints for the given apiserver service (ro or rw).
ReconcileEndpoints expects that the en


### ReconcileEndpoints (pkg/controlplane/reconcilers/instancecount.go:62)


ReconcileEndpoints sets the endpoints for the given apiserver service (ro or rw).
ReconcileEndpoints expects that the endpoints objects it manages will all be
managed only by ReconcileEndpoints; therefore, to understand this, you need only
understand the requirements and the body of this function.

Requirements:
- All apiservers MUST use the same ports for their {rw, ro} services.
- All apiservers MUST use ReconcileEndpoints and only ReconcileEndpoints to manage the
endpoints for their {rw, ro} services.
- All apiservers MUST know and agree on the number of apiservers expected
to be running (c.masterCount).
- ReconcileEndpoints is called periodically from all apiservers.


```go
func (r *masterCountEndpointReconciler) ReconcileEndpoints((serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort, reconcilePorts bool)) (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort, reconcilePorts bool)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** endpointPorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** reconcilePorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/reconcilers/instancecount.go:62`



---


[function] name: RemoveEndpoints file: pkg/controlplane/reconcilers/instancecount.go:145 returns_error: нет description: —


### RemoveEndpoints (pkg/controlplane/reconcilers/instancecount.go:145)


RemoveEndpoints is a method that deletes data based on the provided parameters and returns (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort).


```go
func (r *masterCountEndpointReconciler) RemoveEndpoints((serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort)) (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** endpointPorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/instancecount.go:145`



---


[function] name: StopReconciling file: pkg/controlplane/reconcilers/instancecount.go:178 returns_error: нет description: —


### StopReconciling (pkg/controlplane/reconcilers/instancecount.go:178)


StopReconciling is a method that performs operations based on the provided parameters and returns ().


```go
func (r *masterCountEndpointReconciler) StopReconciling(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/instancecount.go:178`



---


[function] name: checkEndpointSubsetFormat file: pkg/controlplane/reconcilers/instancecount.go:195 returns_error: нет description: Determine if the endpoint is in the format ReconcileEndpoints expects.

Return values:
- formatCorrect is true if exactl


### checkEndpointSubsetFormat (pkg/controlplane/reconcilers/instancecount.go:195)


Determine if the endpoint is in the format ReconcileEndpoints expects.

Return values:
- formatCorrect is true if exactly one subset is found.
- ipCorrect is true when current master's IP is found and the number
of addresses is less than or equal to the master count.
- portsCorrect is true when endpoint ports exactly match provided ports.
portsCorrect is only evaluated when reconcilePorts is set to true.


```go
func checkEndpointSubsetFormat((formatCorrect bool, ipCorrect bool, portsCorrect bool)) (formatCorrect bool, ipCorrect bool, portsCorrect bool)
```


**Тип ответа:** formatCorrect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ipCorrect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** portsCorrect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/reconcilers/instancecount.go:195`




## pkg/controlplane/reconcilers/lease.go


📄 Исходный файл: `pkg/controlplane/reconcilers/lease.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Destroy](#destroy-pkgcontrolplanereconcilersleasego129) `:129`

- 🔗 [Destroy](#destroy-pkgcontrolplanereconcilersleasego345) `:345`

- 🔗 [ListLeases](#listleases-pkgcontrolplanereconcilersleasego71) `:71`

- 🔗 [NewLeaseEndpointReconciler](#newleaseendpointreconciler-pkgcontrolplanereconcilersleasego158) `:158`

- 🔗 [NewLeases](#newleases-pkgcontrolplanereconcilersleasego134) `:134`

- 🔗 [ReconcileEndpoints](#reconcileendpoints-pkgcontrolplanereconcilersleasego172) `:172`

- 🔗 [RemoveEndpoints](#removeendpoints-pkgcontrolplanereconcilersleasego329) `:329`

- 🔗 [RemoveLease](#removelease-pkgcontrolplanereconcilersleasego124) `:124`

- 🔗 [StopReconciling](#stopreconciling-pkgcontrolplanereconcilersleasego341) `:341`

- 🔗 [UpdateLease](#updatelease-pkgcontrolplanereconcilersleasego97) `:97`

- 🔗 [checkEndpointSubsetFormatWithLease](#checkendpointsubsetformatwithlease-pkgcontrolplanereconcilersleasego284) `:284`

- 🔗 [doReconcile](#doreconcile-pkgcontrolplanereconcilersleasego194) `:194`


</details>


[function] name: Destroy file: pkg/controlplane/reconcilers/lease.go:129 returns_error: нет description: —


### Destroy (pkg/controlplane/reconcilers/lease.go:129)


Destroy is a method that performs operations based on the provided parameters and returns ().


```go
func (s *storageLeases) Destroy(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:129`



---


[function] name: Destroy file: pkg/controlplane/reconcilers/lease.go:345 returns_error: нет description: —


### Destroy (pkg/controlplane/reconcilers/lease.go:345)


Destroy is a method that performs operations based on the provided parameters and returns ().


```go
func (r *leaseEndpointReconciler) Destroy(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:345`



---


[function] name: ListLeases file: pkg/controlplane/reconcilers/lease.go:71 returns_error: да description: ListLeases retrieves a list of the current master IPs from storage


### ListLeases (pkg/controlplane/reconcilers/lease.go:71)


ListLeases retrieves a list of the current master IPs from storage


```go
func (s *storageLeases) ListLeases(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:71`



---


[function] name: NewLeaseEndpointReconciler file: pkg/controlplane/reconcilers/lease.go:158 returns_error: нет description: NewLeaseEndpointReconciler creates a new LeaseEndpoint reconciler


### NewLeaseEndpointReconciler (pkg/controlplane/reconcilers/lease.go:158)


NewLeaseEndpointReconciler creates a new LeaseEndpoint reconciler


```go
func NewLeaseEndpointReconciler((epAdapter EndpointsAdapter, masterLeases Leases)) (epAdapter EndpointsAdapter, masterLeases Leases)
```


**Тип ответа:** epAdapter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** EndpointsAdapter


```json
{
  "endpointClient": {},
  "endpointSliceClient": {}
}
```


*Определено в:* `pkg/controlplane/reconcilers/endpointsadapter.go`


**Тип ответа:** masterLeases


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Leases


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/coordination/v1beta1/fake/fake_lease.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:158`



---


[function] name: NewLeases file: pkg/controlplane/reconcilers/lease.go:134 returns_error: да description: NewLeases creates a new etcd-based Leases implementation.


### NewLeases (pkg/controlplane/reconcilers/lease.go:134)


NewLeases creates a new etcd-based Leases implementation.


```go
func NewLeases((Leases, error)) (Leases, error)
```


**Тип ответа:** Leases


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/coordination/v1beta1/fake/fake_lease.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Leases`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:134`



---


[function] name: ReconcileEndpoints file: pkg/controlplane/reconcilers/lease.go:172 returns_error: нет description: ReconcileEndpoints lists keys in a special etcd directory.
Each key is expected to have a TTL of R+n, where R is the ref


### ReconcileEndpoints (pkg/controlplane/reconcilers/lease.go:172)


ReconcileEndpoints lists keys in a special etcd directory.
Each key is expected to have a TTL of R+n, where R is the refresh interval
at which this function is called, and n is some small value.  If an
apiserver goes down, it will fail to refresh its key's TTL and the key will
expire. ReconcileEndpoints will notice that the endpoints object is
different from the directory listing, and update the endpoints object
accordingly.


```go
func (r *leaseEndpointReconciler) ReconcileEndpoints((serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort, reconcilePorts bool)) (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort, reconcilePorts bool)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** endpointPorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** reconcilePorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:172`



---


[function] name: RemoveEndpoints file: pkg/controlplane/reconcilers/lease.go:329 returns_error: нет description: —


### RemoveEndpoints (pkg/controlplane/reconcilers/lease.go:329)


RemoveEndpoints is a method that deletes data based on the provided parameters and returns (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort).


```go
func (r *leaseEndpointReconciler) RemoveEndpoints((serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort)) (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** endpointPorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:329`



---


[function] name: RemoveLease file: pkg/controlplane/reconcilers/lease.go:124 returns_error: нет description: RemoveLease removes the lease on a master IP in storage


### RemoveLease (pkg/controlplane/reconcilers/lease.go:124)


RemoveLease removes the lease on a master IP in storage


```go
func (s *storageLeases) RemoveLease((ip string)) (ip string)
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:124`



---


[function] name: StopReconciling file: pkg/controlplane/reconcilers/lease.go:341 returns_error: нет description: —


### StopReconciling (pkg/controlplane/reconcilers/lease.go:341)


StopReconciling is a method that performs operations based on the provided parameters and returns ().


```go
func (r *leaseEndpointReconciler) StopReconciling(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:341`



---


[function] name: UpdateLease file: pkg/controlplane/reconcilers/lease.go:97 returns_error: нет description: UpdateLease resets the TTL on a master IP in storage
UpdateLease will create a new key if it doesn't exist.


### UpdateLease (pkg/controlplane/reconcilers/lease.go:97)


UpdateLease resets the TTL on a master IP in storage
UpdateLease will create a new key if it doesn't exist.


```go
func (s *storageLeases) UpdateLease((ip string)) (ip string)
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:97`



---


[function] name: checkEndpointSubsetFormatWithLease file: pkg/controlplane/reconcilers/lease.go:284 returns_error: нет description: checkEndpointSubsetFormatWithLease determines if the endpoint is in the
format ReconcileEndpoints expects when the contr


### checkEndpointSubsetFormatWithLease (pkg/controlplane/reconcilers/lease.go:284)


checkEndpointSubsetFormatWithLease determines if the endpoint is in the
format ReconcileEndpoints expects when the controller is using leases.

Return values:
- formatCorrect is true if exactly one subset is found.
- ipsCorrect when the addresses in the endpoints match the expected addresses list
- portsCorrect is true when endpoint ports exactly match provided ports.
portsCorrect is only evaluated when reconcilePorts is set to true.


```go
func checkEndpointSubsetFormatWithLease((formatCorrect bool, ipsCorrect bool, portsCorrect bool)) (formatCorrect bool, ipsCorrect bool, portsCorrect bool)
```


**Тип ответа:** formatCorrect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ipsCorrect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** portsCorrect


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:284`



---


[function] name: doReconcile file: pkg/controlplane/reconcilers/lease.go:194 returns_error: нет description: doReconcile can be called from ReconcileEndpoints() or RemoveEndpoints().
it is NOT SAFE to call it from multiple gorout


### doReconcile (pkg/controlplane/reconcilers/lease.go:194)


doReconcile can be called from ReconcileEndpoints() or RemoveEndpoints().
it is NOT SAFE to call it from multiple goroutines.


```go
func (r *leaseEndpointReconciler) doReconcile((serviceName string, endpointPorts []corev1.EndpointPort, reconcilePorts bool)) (serviceName string, endpointPorts []corev1.EndpointPort, reconcilePorts bool)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** endpointPorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** reconcilePorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/reconcilers/lease.go:194`




## pkg/controlplane/reconcilers/none.go


📄 Исходный файл: `pkg/controlplane/reconcilers/none.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Destroy](#destroy-pkgcontrolplanereconcilersnonego48) `:48`

- 🔗 [NewNoneEndpointReconciler](#newnoneendpointreconciler-pkgcontrolplanereconcilersnonego31) `:31`

- 🔗 [ReconcileEndpoints](#reconcileendpoints-pkgcontrolplanereconcilersnonego36) `:36`

- 🔗 [RemoveEndpoints](#removeendpoints-pkgcontrolplanereconcilersnonego41) `:41`

- 🔗 [StopReconciling](#stopreconciling-pkgcontrolplanereconcilersnonego45) `:45`


</details>


[function] name: Destroy file: pkg/controlplane/reconcilers/none.go:48 returns_error: нет description: —


### Destroy (pkg/controlplane/reconcilers/none.go:48)


Destroy is a method that performs operations based on the provided parameters and returns ().


```go
func (r *noneEndpointReconciler) Destroy(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/none.go:48`



---


[function] name: NewNoneEndpointReconciler file: pkg/controlplane/reconcilers/none.go:31 returns_error: нет description: NewNoneEndpointReconciler creates a new EndpointReconciler that reconciles based on a
nothing. It is a no-op.


### NewNoneEndpointReconciler (pkg/controlplane/reconcilers/none.go:31)


NewNoneEndpointReconciler creates a new EndpointReconciler that reconciles based on a
nothing. It is a no-op.


```go
func NewNoneEndpointReconciler(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/none.go:31`



---


[function] name: ReconcileEndpoints file: pkg/controlplane/reconcilers/none.go:36 returns_error: нет description: ReconcileEndpoints noop reconcile


### ReconcileEndpoints (pkg/controlplane/reconcilers/none.go:36)


ReconcileEndpoints noop reconcile


```go
func (r *noneEndpointReconciler) ReconcileEndpoints((serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort, reconcilePorts bool)) (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort, reconcilePorts bool)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** endpointPorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** reconcilePorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/controlplane/reconcilers/none.go:36`



---


[function] name: RemoveEndpoints file: pkg/controlplane/reconcilers/none.go:41 returns_error: нет description: RemoveEndpoints noop reconcile


### RemoveEndpoints (pkg/controlplane/reconcilers/none.go:41)


RemoveEndpoints noop reconcile


```go
func (r *noneEndpointReconciler) RemoveEndpoints((serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort)) (serviceName string, ip net.IP, endpointPorts []corev1.EndpointPort)
```


**Тип ответа:** serviceName


```json
{
  "services": [],
  "namespace": "string"
}
```


*Определено в:* `pkg/scheduler/testing/framework/fake_listers.go`


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** endpointPorts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/controlplane/reconcilers/none.go:41`



---


[function] name: StopReconciling file: pkg/controlplane/reconcilers/none.go:45 returns_error: нет description: —


### StopReconciling (pkg/controlplane/reconcilers/none.go:45)


StopReconciling is a method that performs operations based on the provided parameters and returns ().


```go
func (r *noneEndpointReconciler) StopReconciling(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/none.go:45`




## pkg/controlplane/reconcilers/reconcilers.go


📄 Исходный файл: `pkg/controlplane/reconcilers/reconcilers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Names](#names-pkgcontrolplanereconcilersreconcilersgo72) `:72`


</details>


[function] name: Names file: pkg/controlplane/reconcilers/reconcilers.go:72 returns_error: нет description: Names returns a slice of all the reconciler names


### Names (pkg/controlplane/reconcilers/reconcilers.go:72)


Names returns a slice of all the reconciler names


```go
func (t Types) Names(()) ()
```


📍 *Расположение:* `pkg/controlplane/reconcilers/reconcilers.go:72`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_controller.md)

- [Следующая директория](pkg_credentialprovider.md)


---

