---
title: "Функции: plugin/pkg"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: plugin/pkg
---


# Функции: plugin/pkg


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_windows.md)

- [Следующая директория](staging_src.md)


---


## Меню по файлам


- 📄 [plugin/pkg/admission/admit/admission.go](#pluginpkgadmissionadmitadmissiongo)

- 📄 [plugin/pkg/admission/alwayspullimages/admission.go](#pluginpkgadmissionalwayspullimagesadmissiongo)

- 📄 [plugin/pkg/admission/antiaffinity/admission.go](#pluginpkgadmissionantiaffinityadmissiongo)

- 📄 [plugin/pkg/admission/certificates/approval/admission.go](#pluginpkgadmissioncertificatesapprovaladmissiongo)

- 📄 [plugin/pkg/admission/certificates/ctbattest/admission.go](#pluginpkgadmissioncertificatesctbattestadmissiongo)

- 📄 [plugin/pkg/admission/certificates/signing/admission.go](#pluginpkgadmissioncertificatessigningadmissiongo)

- 📄 [plugin/pkg/admission/certificates/subjectrestriction/admission.go](#pluginpkgadmissioncertificatessubjectrestrictionadmissiongo)

- 📄 [plugin/pkg/admission/defaulttolerationseconds/admission.go](#pluginpkgadmissiondefaulttolerationsecondsadmissiongo)

- 📄 [plugin/pkg/admission/deny/admission.go](#pluginpkgadmissiondenyadmissiongo)

- 📄 [plugin/pkg/admission/eventratelimit/admission.go](#pluginpkgadmissioneventratelimitadmissiongo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/install/install.go](#pluginpkgadmissioneventratelimitapiseventratelimitinstallinstallgo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go](#pluginpkgadmissioneventratelimitapiseventratelimitregistergo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go](#pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1defaultsgo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go](#pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1registergo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go](#pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go](#pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddeepcopygo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go](#pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddefaultsgo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/validation/validation.go](#pluginpkgadmissioneventratelimitapiseventratelimitvalidationvalidationgo)

- 📄 [plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go](#pluginpkgadmissioneventratelimitapiseventratelimitzz_generateddeepcopygo)

- 📄 [plugin/pkg/admission/eventratelimit/cache.go](#pluginpkgadmissioneventratelimitcachego)

- 📄 [plugin/pkg/admission/eventratelimit/config.go](#pluginpkgadmissioneventratelimitconfiggo)

- 📄 [plugin/pkg/admission/eventratelimit/limitenforcer.go](#pluginpkgadmissioneventratelimitlimitenforcergo)

- 📄 [plugin/pkg/admission/extendedresourcetoleration/admission.go](#pluginpkgadmissionextendedresourcetolerationadmissiongo)

- 📄 [plugin/pkg/admission/gc/gc_admission.go](#pluginpkgadmissiongcgc_admissiongo)

- 📄 [plugin/pkg/admission/imagepolicy/admission.go](#pluginpkgadmissionimagepolicyadmissiongo)

- 📄 [plugin/pkg/admission/imagepolicy/config.go](#pluginpkgadmissionimagepolicyconfiggo)

- 📄 [plugin/pkg/admission/limitranger/admission.go](#pluginpkgadmissionlimitrangeradmissiongo)

- 📄 [plugin/pkg/admission/namespace/autoprovision/admission.go](#pluginpkgadmissionnamespaceautoprovisionadmissiongo)

- 📄 [plugin/pkg/admission/namespace/exists/admission.go](#pluginpkgadmissionnamespaceexistsadmissiongo)

- 📄 [plugin/pkg/admission/network/defaultingressclass/admission.go](#pluginpkgadmissionnetworkdefaultingressclassadmissiongo)

- 📄 [plugin/pkg/admission/network/denyserviceexternalips/admission.go](#pluginpkgadmissionnetworkdenyserviceexternalipsadmissiongo)

- 📄 [plugin/pkg/admission/nodedeclaredfeatures/admission.go](#pluginpkgadmissionnodedeclaredfeaturesadmissiongo)

- 📄 [plugin/pkg/admission/noderestriction/admission.go](#pluginpkgadmissionnoderestrictionadmissiongo)

- 📄 [plugin/pkg/admission/nodetaint/admission.go](#pluginpkgadmissionnodetaintadmissiongo)

- 📄 [plugin/pkg/admission/podnodeselector/admission.go](#pluginpkgadmissionpodnodeselectoradmissiongo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/admission.go](#pluginpkgadmissionpodtolerationrestrictionadmissiongo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/install/install.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictioninstallinstallgo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionregistergo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/defaults.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1defaultsgo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1registergo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generatedconversiongo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generateddeepcopygo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.defaults.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generateddefaultsgo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/validation/validation.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionvalidationvalidationgo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go](#pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionzz_generateddeepcopygo)

- 📄 [plugin/pkg/admission/podtolerationrestriction/config.go](#pluginpkgadmissionpodtolerationrestrictionconfiggo)

- 📄 [plugin/pkg/admission/podtopologylabels/admission.go](#pluginpkgadmissionpodtopologylabelsadmissiongo)

- 📄 [plugin/pkg/admission/priority/admission.go](#pluginpkgadmissionpriorityadmissiongo)

- 📄 [plugin/pkg/admission/runtimeclass/admission.go](#pluginpkgadmissionruntimeclassadmissiongo)

- 📄 [plugin/pkg/admission/security/podsecurity/admission.go](#pluginpkgadmissionsecuritypodsecurityadmissiongo)

- 📄 [plugin/pkg/admission/serviceaccount/admission.go](#pluginpkgadmissionserviceaccountadmissiongo)

- 📄 [plugin/pkg/admission/storage/persistentvolume/resize/admission.go](#pluginpkgadmissionstoragepersistentvolumeresizeadmissiongo)

- 📄 [plugin/pkg/admission/storage/storageclass/setdefault/admission.go](#pluginpkgadmissionstoragestorageclasssetdefaultadmissiongo)

- 📄 [plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go](#pluginpkgadmissionstoragestorageobjectinuseprotectionadmissiongo)

- 📄 [plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go](#pluginpkgauthauthenticatortokenbootstrapbootstrapgo)

- 📄 [plugin/pkg/auth/authorizer/node/graph.go](#pluginpkgauthauthorizernodegraphgo)

- 📄 [plugin/pkg/auth/authorizer/node/graph_populator.go](#pluginpkgauthauthorizernodegraph_populatorgo)

- 📄 [plugin/pkg/auth/authorizer/node/intset.go](#pluginpkgauthauthorizernodeintsetgo)

- 📄 [plugin/pkg/auth/authorizer/node/metrics.go](#pluginpkgauthauthorizernodemetricsgo)

- 📄 [plugin/pkg/auth/authorizer/node/node_authorizer.go](#pluginpkgauthauthorizernodenode_authorizergo)

- 📄 [plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go](#pluginpkgauthauthorizerrbacbootstrappolicycontroller_policygo)

- 📄 [plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go](#pluginpkgauthauthorizerrbacbootstrappolicynamespace_policygo)

- 📄 [plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go](#pluginpkgauthauthorizerrbacbootstrappolicypolicygo)

- 📄 [plugin/pkg/auth/authorizer/rbac/rbac.go](#pluginpkgauthauthorizerrbacrbacgo)

- 📄 [plugin/pkg/auth/authorizer/rbac/subject_locator.go](#pluginpkgauthauthorizerrbacsubject_locatorgo)


---


## plugin/pkg/admission/admit/admission.go


📄 Исходный файл: `plugin/pkg/admission/admit/admission.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionadmitadmissiongo44) `:44`

- 🔗 [Handles](#handles-pluginpkgadmissionadmitadmissiongo55) `:55`

- 🔗 [NewAlwaysAdmit](#newalwaysadmit-pluginpkgadmissionadmitadmissiongo60) `:60`

- 🔗 [Register](#register-pluginpkgadmissionadmitadmissiongo31) `:31`

- 🔗 [Validate](#validate-pluginpkgadmissionadmitadmissiongo49) `:49`


</details>


[function] name: Admit file: plugin/pkg/admission/admit/admission.go:44 returns_error: да description: Admit makes an admission decision based on the request attributes


### Admit (plugin/pkg/admission/admit/admission.go:44)


Admit makes an admission decision based on the request attributes


```go
func (alwaysAdmit) Admit((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/admit/admission.go:44`



---


[function] name: Handles file: plugin/pkg/admission/admit/admission.go:55 returns_error: нет description: Handles returns true if this admission controller can handle the given operation
where operation can be one of CREATE, U


### Handles (plugin/pkg/admission/admit/admission.go:55)


Handles returns true if this admission controller can handle the given operation
where operation can be one of CREATE, UPDATE, DELETE, or CONNECT


```go
func (alwaysAdmit) Handles((operation admission.Operation)) (operation admission.Operation)
```


**Тип ответа:** operation


```json
{
  "key": {},
  "operationName": "string",
  "operationPending": false,
  "expBackoff": {}
}
```


*Определено в:* `pkg/volume/util/nestedpendingoperations/nestedpendingoperations.go`


**Тип ответа:** admission.Operation


```json
{
  "Type": {},
  "Options": [],
  "Request": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `plugin/pkg/admission/admit/admission.go:55`



---


[function] name: NewAlwaysAdmit file: plugin/pkg/admission/admit/admission.go:60 returns_error: нет description: NewAlwaysAdmit creates a new always admit admission handler


### NewAlwaysAdmit (plugin/pkg/admission/admit/admission.go:60)


NewAlwaysAdmit creates a new always admit admission handler


```go
func NewAlwaysAdmit(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/admit/admission.go:60`



---


[function] name: Register file: plugin/pkg/admission/admit/admission.go:31 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/admit/admission.go:31)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/admit/admission.go:31`



---


[function] name: Validate file: plugin/pkg/admission/admit/admission.go:49 returns_error: да description: Validate makes an admission decision based on the request attributes.  It is NOT allowed to mutate.


### Validate (plugin/pkg/admission/admit/admission.go:49)


Validate makes an admission decision based on the request attributes.  It is NOT allowed to mutate.


```go
func (alwaysAdmit) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/admit/admission.go:49`




## plugin/pkg/admission/alwayspullimages/admission.go


📄 Исходный файл: `plugin/pkg/admission/alwayspullimages/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionalwayspullimagesadmissiongo61) `:61`

- 🔗 [NewAlwaysPullImages](#newalwayspullimages-pluginpkgadmissionalwayspullimagesadmissiongo174) `:174`

- 🔗 [Register](#register-pluginpkgadmissionalwayspullimagesadmissiongo45) `:45`

- 🔗 [Validate](#validate-pluginpkgadmissionalwayspullimagesadmissiongo87) `:87`

- 🔗 [isUpdateWithNoNewImages](#isupdatewithnonewimages-pluginpkgadmissionalwayspullimagesadmissiongo128) `:128`

- 🔗 [shouldIgnore](#shouldignore-pluginpkgadmissionalwayspullimagesadmissiongo161) `:161`


</details>


[function] name: Admit file: plugin/pkg/admission/alwayspullimages/admission.go:61 returns_error: да description: Admit makes an admission decision based on the request attributes


### Admit (plugin/pkg/admission/alwayspullimages/admission.go:61)


Admit makes an admission decision based on the request attributes


```go
func (a *AlwaysPullImages) Admit((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/alwayspullimages/admission.go:61`



---


[function] name: NewAlwaysPullImages file: plugin/pkg/admission/alwayspullimages/admission.go:174 returns_error: нет description: NewAlwaysPullImages creates a new always pull images admission control handler


### NewAlwaysPullImages (plugin/pkg/admission/alwayspullimages/admission.go:174)


NewAlwaysPullImages creates a new always pull images admission control handler


```go
func NewAlwaysPullImages(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/alwayspullimages/admission.go:174`



---


[function] name: Register file: plugin/pkg/admission/alwayspullimages/admission.go:45 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/alwayspullimages/admission.go:45)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/alwayspullimages/admission.go:45`



---


[function] name: Validate file: plugin/pkg/admission/alwayspullimages/admission.go:87 returns_error: да description: Validate makes sure that all containers are set to always pull images


### Validate (plugin/pkg/admission/alwayspullimages/admission.go:87)


Validate makes sure that all containers are set to always pull images


```go
func (*AlwaysPullImages) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/alwayspullimages/admission.go:87`



---


[function] name: isUpdateWithNoNewImages file: plugin/pkg/admission/alwayspullimages/admission.go:128 returns_error: нет description: check if it's update and it doesn't change the images referenced by the pod spec


### isUpdateWithNoNewImages (plugin/pkg/admission/alwayspullimages/admission.go:128)


check if it's update and it doesn't change the images referenced by the pod spec


```go
func isUpdateWithNoNewImages((attributes admission.Attributes)) (attributes admission.Attributes)
```


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/alwayspullimages/admission.go:128`



---


[function] name: shouldIgnore file: plugin/pkg/admission/alwayspullimages/admission.go:161 returns_error: нет description: —


### shouldIgnore (plugin/pkg/admission/alwayspullimages/admission.go:161)


shouldIgnore is a function that performs operations based on the provided parameters and returns (attributes admission.Attributes).


```go
func shouldIgnore((attributes admission.Attributes)) (attributes admission.Attributes)
```


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/alwayspullimages/admission.go:161`




## plugin/pkg/admission/antiaffinity/admission.go


📄 Исходный файл: `plugin/pkg/admission/antiaffinity/admission.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [NewInterPodAntiAffinity](#newinterpodantiaffinity-pluginpkgadmissionantiaffinityadmissiongo48) `:48`

- 🔗 [Register](#register-pluginpkgadmissionantiaffinityadmissiongo34) `:34`

- 🔗 [Validate](#validate-pluginpkgadmissionantiaffinityadmissiongo56) `:56`


</details>


[function] name: NewInterPodAntiAffinity file: plugin/pkg/admission/antiaffinity/admission.go:48 returns_error: нет description: NewInterPodAntiAffinity creates a new instance of the LimitPodHardAntiAffinityTopology admission controller


### NewInterPodAntiAffinity (plugin/pkg/admission/antiaffinity/admission.go:48)


NewInterPodAntiAffinity creates a new instance of the LimitPodHardAntiAffinityTopology admission controller


```go
func NewInterPodAntiAffinity(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/antiaffinity/admission.go:48`



---


[function] name: Register file: plugin/pkg/admission/antiaffinity/admission.go:34 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/antiaffinity/admission.go:34)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/antiaffinity/admission.go:34`



---


[function] name: Validate file: plugin/pkg/admission/antiaffinity/admission.go:56 returns_error: да description: Validate will deny any pod that defines AntiAffinity topology key other than v1.LabelHostname i.e. "kubernetes.io/hostna


### Validate (plugin/pkg/admission/antiaffinity/admission.go:56)


Validate will deny any pod that defines AntiAffinity topology key other than v1.LabelHostname i.e. "kubernetes.io/hostname"
in  requiredDuringSchedulingRequiredDuringExecution and requiredDuringSchedulingIgnoredDuringExecution.


```go
func (p *Plugin) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/antiaffinity/admission.go:56`




## plugin/pkg/admission/certificates/approval/admission.go


📄 Исходный файл: `plugin/pkg/admission/certificates/approval/admission.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NewPlugin](#newplugin-pluginpkgadmissioncertificatesapprovaladmissiongo65) `:65`

- 🔗 [Register](#register-pluginpkgadmissioncertificatesapprovaladmissiongo36) `:36`

- 🔗 [SetAuthorizer](#setauthorizer-pluginpkgadmissioncertificatesapprovaladmissiongo49) `:49`

- 🔗 [Validate](#validate-pluginpkgadmissioncertificatesapprovaladmissiongo75) `:75`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissioncertificatesapprovaladmissiongo54) `:54`


</details>


[function] name: NewPlugin file: plugin/pkg/admission/certificates/approval/admission.go:65 returns_error: нет description: NewPlugin creates a new CSR approval admission plugin


### NewPlugin (plugin/pkg/admission/certificates/approval/admission.go:65)


NewPlugin creates a new CSR approval admission plugin


```go
func NewPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/approval/admission.go:65`



---


[function] name: Register file: plugin/pkg/admission/certificates/approval/admission.go:36 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/certificates/approval/admission.go:36)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/certificates/approval/admission.go:36`



---


[function] name: SetAuthorizer file: plugin/pkg/admission/certificates/approval/admission.go:49 returns_error: нет description: SetAuthorizer sets the authorizer.


### SetAuthorizer (plugin/pkg/admission/certificates/approval/admission.go:49)


SetAuthorizer sets the authorizer.


```go
func (p *Plugin) SetAuthorizer((authz authorizer.Authorizer)) (authz authorizer.Authorizer)
```


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


📍 *Расположение:* `plugin/pkg/admission/certificates/approval/admission.go:49`



---


[function] name: Validate file: plugin/pkg/admission/certificates/approval/admission.go:75 returns_error: нет description: Validate verifies that the requesting user has permission to approve
CertificateSigningRequests for the specified signer


### Validate (plugin/pkg/admission/certificates/approval/admission.go:75)


Validate verifies that the requesting user has permission to approve
CertificateSigningRequests for the specified signerName.


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, _ admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, _ admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/certificates/approval/admission.go:75`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/certificates/approval/admission.go:54 returns_error: нет description: ValidateInitialization ensures an authorizer is set.


### ValidateInitialization (plugin/pkg/admission/certificates/approval/admission.go:54)


ValidateInitialization ensures an authorizer is set.


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/approval/admission.go:54`




## plugin/pkg/admission/certificates/ctbattest/admission.go


📄 Исходный файл: `plugin/pkg/admission/certificates/ctbattest/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [InspectFeatureGates](#inspectfeaturegates-pluginpkgadmissioncertificatesctbattestadmissiongo74) `:74`

- 🔗 [NewPlugin](#newplugin-pluginpkgadmissioncertificatesctbattestadmissiongo62) `:62`

- 🔗 [Register](#register-pluginpkgadmissioncertificatesctbattestadmissiongo38) `:38`

- 🔗 [SetAuthorizer](#setauthorizer-pluginpkgadmissioncertificatesctbattestadmissiongo69) `:69`

- 🔗 [Validate](#validate-pluginpkgadmissioncertificatesctbattestadmissiongo92) `:92`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissioncertificatesctbattestadmissiongo80) `:80`


</details>


[function] name: InspectFeatureGates file: plugin/pkg/admission/certificates/ctbattest/admission.go:74 returns_error: нет description: InspectFeatureGates implements WantsFeatures.


### InspectFeatureGates (plugin/pkg/admission/certificates/ctbattest/admission.go:74)


InspectFeatureGates implements WantsFeatures.


```go
func (p *Plugin) InspectFeatureGates((featureGates featuregate.FeatureGate)) (featureGates featuregate.FeatureGate)
```


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featuregate.FeatureGate


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `plugin/pkg/admission/certificates/ctbattest/admission.go:74`



---


[function] name: NewPlugin file: plugin/pkg/admission/certificates/ctbattest/admission.go:62 returns_error: нет description: —


### NewPlugin (plugin/pkg/admission/certificates/ctbattest/admission.go:62)


NewPlugin is a function that performs operations based on the provided parameters and returns ().


```go
func NewPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/ctbattest/admission.go:62`



---


[function] name: Register file: plugin/pkg/admission/certificates/ctbattest/admission.go:38 returns_error: нет description: —


### Register (plugin/pkg/admission/certificates/ctbattest/admission.go:38)


Register is a function that performs operations based on the provided parameters and returns (plugins *admission.Plugins).


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/certificates/ctbattest/admission.go:38`



---


[function] name: SetAuthorizer file: plugin/pkg/admission/certificates/ctbattest/admission.go:69 returns_error: нет description: SetAuthorizer sets the plugin's authorizer.


### SetAuthorizer (plugin/pkg/admission/certificates/ctbattest/admission.go:69)


SetAuthorizer sets the plugin's authorizer.


```go
func (p *Plugin) SetAuthorizer((authz authorizer.Authorizer)) (authz authorizer.Authorizer)
```


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


📍 *Расположение:* `plugin/pkg/admission/certificates/ctbattest/admission.go:69`



---


[function] name: Validate file: plugin/pkg/admission/certificates/ctbattest/admission.go:92 returns_error: нет description: —


### Validate (plugin/pkg/admission/certificates/ctbattest/admission.go:92)


Validate is a method that performs operations based on the provided parameters and returns (ctx context.Context, a admission.Attributes, _ admission.ObjectInterfaces).


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, _ admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, _ admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/certificates/ctbattest/admission.go:92`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/certificates/ctbattest/admission.go:80 returns_error: нет description: ValidateInitialization checks that the plugin was initialized correctly.


### ValidateInitialization (plugin/pkg/admission/certificates/ctbattest/admission.go:80)


ValidateInitialization checks that the plugin was initialized correctly.


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/ctbattest/admission.go:80`




## plugin/pkg/admission/certificates/signing/admission.go


📄 Исходный файл: `plugin/pkg/admission/certificates/signing/admission.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NewPlugin](#newplugin-pluginpkgadmissioncertificatessigningadmissiongo68) `:68`

- 🔗 [Register](#register-pluginpkgadmissioncertificatessigningadmissiongo39) `:39`

- 🔗 [SetAuthorizer](#setauthorizer-pluginpkgadmissioncertificatessigningadmissiongo52) `:52`

- 🔗 [Validate](#validate-pluginpkgadmissioncertificatessigningadmissiongo78) `:78`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissioncertificatessigningadmissiongo57) `:57`


</details>


[function] name: NewPlugin file: plugin/pkg/admission/certificates/signing/admission.go:68 returns_error: нет description: NewPlugin creates a new CSR approval admission plugin


### NewPlugin (plugin/pkg/admission/certificates/signing/admission.go:68)


NewPlugin creates a new CSR approval admission plugin


```go
func NewPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/signing/admission.go:68`



---


[function] name: Register file: plugin/pkg/admission/certificates/signing/admission.go:39 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/certificates/signing/admission.go:39)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/certificates/signing/admission.go:39`



---


[function] name: SetAuthorizer file: plugin/pkg/admission/certificates/signing/admission.go:52 returns_error: нет description: SetAuthorizer sets the authorizer.


### SetAuthorizer (plugin/pkg/admission/certificates/signing/admission.go:52)


SetAuthorizer sets the authorizer.


```go
func (p *Plugin) SetAuthorizer((authz authorizer.Authorizer)) (authz authorizer.Authorizer)
```


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


📍 *Расположение:* `plugin/pkg/admission/certificates/signing/admission.go:52`



---


[function] name: Validate file: plugin/pkg/admission/certificates/signing/admission.go:78 returns_error: нет description: Validate verifies that the requesting user has permission to sign
CertificateSigningRequests for the specified signerNam


### Validate (plugin/pkg/admission/certificates/signing/admission.go:78)


Validate verifies that the requesting user has permission to sign
CertificateSigningRequests for the specified signerName.


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/certificates/signing/admission.go:78`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/certificates/signing/admission.go:57 returns_error: нет description: ValidateInitialization ensures an authorizer is set.


### ValidateInitialization (plugin/pkg/admission/certificates/signing/admission.go:57)


ValidateInitialization ensures an authorizer is set.


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/signing/admission.go:57`




## plugin/pkg/admission/certificates/subjectrestriction/admission.go


📄 Исходный файл: `plugin/pkg/admission/certificates/subjectrestriction/admission.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewPlugin](#newplugin-pluginpkgadmissioncertificatessubjectrestrictionadmissiongo53) `:53`

- 🔗 [Register](#register-pluginpkgadmissioncertificatessubjectrestrictionadmissiongo34) `:34`

- 🔗 [Validate](#validate-pluginpkgadmissioncertificatessubjectrestrictionadmissiongo64) `:64`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissioncertificatessubjectrestrictionadmissiongo46) `:46`


</details>


[function] name: NewPlugin file: plugin/pkg/admission/certificates/subjectrestriction/admission.go:53 returns_error: нет description: NewPlugin constructs a new instance of the CertificateSubjectRestrictions admission interface.


### NewPlugin (plugin/pkg/admission/certificates/subjectrestriction/admission.go:53)


NewPlugin constructs a new instance of the CertificateSubjectRestrictions admission interface.


```go
func NewPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/subjectrestriction/admission.go:53`



---


[function] name: Register file: plugin/pkg/admission/certificates/subjectrestriction/admission.go:34 returns_error: нет description: Register registers the plugin


### Register (plugin/pkg/admission/certificates/subjectrestriction/admission.go:34)


Register registers the plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/certificates/subjectrestriction/admission.go:34`



---


[function] name: Validate file: plugin/pkg/admission/certificates/subjectrestriction/admission.go:64 returns_error: нет description: Validate ensures that if the signerName on a CSR is set to
`kubernetes.io/kube-apiserver-client`, that its organization 


### Validate (plugin/pkg/admission/certificates/subjectrestriction/admission.go:64)


Validate ensures that if the signerName on a CSR is set to
`kubernetes.io/kube-apiserver-client`, that its organization (group)
attribute is not set to `system:masters`.


```go
func (p *Plugin) Validate((_ context.Context, a admission.Attributes, _ admission.ObjectInterfaces)) (_ context.Context, a admission.Attributes, _ admission.ObjectInterfaces)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/certificates/subjectrestriction/admission.go:64`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/certificates/subjectrestriction/admission.go:46 returns_error: нет description: ValidateInitialization always returns nil.


### ValidateInitialization (plugin/pkg/admission/certificates/subjectrestriction/admission.go:46)


ValidateInitialization always returns nil.


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/certificates/subjectrestriction/admission.go:46`




## plugin/pkg/admission/defaulttolerationseconds/admission.go


📄 Исходный файл: `plugin/pkg/admission/defaulttolerationseconds/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissiondefaulttolerationsecondsadmissiongo125) `:125`

- 🔗 [InspectFeatureGates](#inspectfeaturegates-pluginpkgadmissiondefaulttolerationsecondsadmissiongo91) `:91`

- 🔗 [NewDefaultTolerationSeconds](#newdefaulttolerationseconds-pluginpkgadmissiondefaulttolerationsecondsadmissiongo84) `:84`

- 🔗 [Register](#register-pluginpkgadmissiondefaulttolerationsecondsadmissiongo62) `:62`

- 🔗 [RegisterFlags](#registerflags-pluginpkgadmissiondefaulttolerationsecondsadmissiongo48) `:48`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissiondefaulttolerationsecondsadmissiongo114) `:114`


</details>


[function] name: Admit file: plugin/pkg/admission/defaulttolerationseconds/admission.go:125 returns_error: да description: Admit makes an admission decision based on the request attributes


### Admit (plugin/pkg/admission/defaulttolerationseconds/admission.go:125)


Admit makes an admission decision based on the request attributes


```go
func (p *Plugin) Admit((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/defaulttolerationseconds/admission.go:125`



---


[function] name: InspectFeatureGates file: plugin/pkg/admission/defaulttolerationseconds/admission.go:91 returns_error: нет description: InspectFeatureGates runs after command-line flags have been parsed


### InspectFeatureGates (plugin/pkg/admission/defaulttolerationseconds/admission.go:91)


InspectFeatureGates runs after command-line flags have been parsed


```go
func (p *Plugin) InspectFeatureGates((featureGates featuregate.FeatureGate)) (featureGates featuregate.FeatureGate)
```


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featuregate.FeatureGate


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `plugin/pkg/admission/defaulttolerationseconds/admission.go:91`



---


[function] name: NewDefaultTolerationSeconds file: plugin/pkg/admission/defaulttolerationseconds/admission.go:84 returns_error: нет description: NewDefaultTolerationSeconds creates a new instance of the DefaultTolerationSeconds admission controller


### NewDefaultTolerationSeconds (plugin/pkg/admission/defaulttolerationseconds/admission.go:84)


NewDefaultTolerationSeconds creates a new instance of the DefaultTolerationSeconds admission controller


```go
func NewDefaultTolerationSeconds(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/defaulttolerationseconds/admission.go:84`



---


[function] name: Register file: plugin/pkg/admission/defaulttolerationseconds/admission.go:62 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/defaulttolerationseconds/admission.go:62)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/defaulttolerationseconds/admission.go:62`



---


[function] name: RegisterFlags file: plugin/pkg/admission/defaulttolerationseconds/admission.go:48 returns_error: нет description: —


### RegisterFlags (plugin/pkg/admission/defaulttolerationseconds/admission.go:48)


RegisterFlags is a function that performs operations based on the provided parameters and returns (fs *pflag.FlagSet).


```go
func RegisterFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `plugin/pkg/admission/defaulttolerationseconds/admission.go:48`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/defaulttolerationseconds/admission.go:114 returns_error: нет description: ValidateInitialization validates the Plugin was initialized properly


### ValidateInitialization (plugin/pkg/admission/defaulttolerationseconds/admission.go:114)


ValidateInitialization validates the Plugin was initialized properly


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/defaulttolerationseconds/admission.go:114`




## plugin/pkg/admission/deny/admission.go


📄 Исходный файл: `plugin/pkg/admission/deny/admission.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissiondenyadmissiongo46) `:46`

- 🔗 [Handles](#handles-pluginpkgadmissiondenyadmissiongo57) `:57`

- 🔗 [NewAlwaysDeny](#newalwaysdeny-pluginpkgadmissiondenyadmissiongo62) `:62`

- 🔗 [Register](#register-pluginpkgadmissiondenyadmissiongo33) `:33`

- 🔗 [Validate](#validate-pluginpkgadmissiondenyadmissiongo51) `:51`


</details>


[function] name: Admit file: plugin/pkg/admission/deny/admission.go:46 returns_error: да description: Admit makes an admission decision based on the request attributes.


### Admit (plugin/pkg/admission/deny/admission.go:46)


Admit makes an admission decision based on the request attributes.


```go
func (alwaysDeny) Admit((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/deny/admission.go:46`



---


[function] name: Handles file: plugin/pkg/admission/deny/admission.go:57 returns_error: нет description: Handles returns true if this admission controller can handle the given operation
where operation can be one of CREATE, U


### Handles (plugin/pkg/admission/deny/admission.go:57)


Handles returns true if this admission controller can handle the given operation
where operation can be one of CREATE, UPDATE, DELETE, or CONNECT


```go
func (alwaysDeny) Handles((operation admission.Operation)) (operation admission.Operation)
```


**Тип ответа:** operation


```json
{
  "key": {},
  "operationName": "string",
  "operationPending": false,
  "expBackoff": {}
}
```


*Определено в:* `pkg/volume/util/nestedpendingoperations/nestedpendingoperations.go`


**Тип ответа:** admission.Operation


```json
{
  "Type": {},
  "Options": [],
  "Request": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `plugin/pkg/admission/deny/admission.go:57`



---


[function] name: NewAlwaysDeny file: plugin/pkg/admission/deny/admission.go:62 returns_error: нет description: NewAlwaysDeny creates an always deny admission handler


### NewAlwaysDeny (plugin/pkg/admission/deny/admission.go:62)


NewAlwaysDeny creates an always deny admission handler


```go
func NewAlwaysDeny(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/deny/admission.go:62`



---


[function] name: Register file: plugin/pkg/admission/deny/admission.go:33 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/deny/admission.go:33)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/deny/admission.go:33`



---


[function] name: Validate file: plugin/pkg/admission/deny/admission.go:51 returns_error: да description: Validate makes an admission decision based on the request attributes.  It is NOT allowed to mutate.


### Validate (plugin/pkg/admission/deny/admission.go:51)


Validate makes an admission decision based on the request attributes.  It is NOT allowed to mutate.


```go
func (alwaysDeny) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/deny/admission.go:51`




## plugin/pkg/admission/eventratelimit/admission.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/admission.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Register](#register-pluginpkgadmissioneventratelimitadmissiongo37) `:37`

- 🔗 [Validate](#validate-pluginpkgadmissioneventratelimitadmissiongo86) `:86`

- 🔗 [newEventRateLimit](#neweventratelimit-pluginpkgadmissioneventratelimitadmissiongo67) `:67`


</details>


[function] name: Register file: plugin/pkg/admission/eventratelimit/admission.go:37 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/eventratelimit/admission.go:37)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/admission.go:37`



---


[function] name: Validate file: plugin/pkg/admission/eventratelimit/admission.go:86 returns_error: да description: Validate makes admission decisions while enforcing event rate limits


### Validate (plugin/pkg/admission/eventratelimit/admission.go:86)


Validate makes admission decisions while enforcing event rate limits


```go
func (a *Plugin) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/admission.go:86`



---


[function] name: newEventRateLimit file: plugin/pkg/admission/eventratelimit/admission.go:67 returns_error: да description: newEventRateLimit configures an admission controller that can enforce event rate limits


### newEventRateLimit (plugin/pkg/admission/eventratelimit/admission.go:67)


newEventRateLimit configures an admission controller that can enforce event rate limits


```go
func newEventRateLimit((*Plugin, error)) (*Plugin, error)
```


**Тип запроса:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип ответа:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Plugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/admission.go:67`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/install/install.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/install/install.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Install](#install-pluginpkgadmissioneventratelimitapiseventratelimitinstallinstallgo29) `:29`


</details>


[function] name: Install file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/install/install.go:29 returns_error: нет description: Install registers the API group and adds types to a scheme


### Install (plugin/pkg/admission/eventratelimit/apis/eventratelimit/install/install.go:29)


Install registers the API group and adds types to a scheme


```go
func Install((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/install/install.go:29`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Kind](#kind-pluginpkgadmissioneventratelimitapiseventratelimitregistergo38) `:38`

- 🔗 [Resource](#resource-pluginpkgadmissioneventratelimitapiseventratelimitregistergo43) `:43`

- 🔗 [addKnownTypes](#addknowntypes-pluginpkgadmissioneventratelimitapiseventratelimitregistergo47) `:47`


</details>


[function] name: Kind file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:38 returns_error: нет description: Kind takes an unqualified kind and returns a Group qualified GroupKind


### Kind (plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:38)


Kind takes an unqualified kind and returns a Group qualified GroupKind


```go
func Kind((kind string)) (kind string)
```


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:38`



---


[function] name: Resource file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:43 returns_error: нет description: Resource takes an unqualified resource and returns a Group qualified GroupResource


### Resource (plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:43)


Resource takes an unqualified resource and returns a Group qualified GroupResource


```go
func Resource((resource string)) (resource string)
```


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:43`



---


[function] name: addKnownTypes file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:47 returns_error: нет description: —


### addKnownTypes (plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:47)


addKnownTypes is a function that performs operations based on the provided parameters and returns (scheme *runtime.Scheme).


```go
func addKnownTypes((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/register.go:47`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [SetDefaults_Configuration](#setdefaults_configuration-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1defaultsgo25) `:25`

- 🔗 [addDefaultingFuncs](#adddefaultingfuncs-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1defaultsgo21) `:21`


</details>


[function] name: SetDefaults_Configuration file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go:25 returns_error: нет description: —


### SetDefaults_Configuration (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go:25)


SetDefaults_Configuration is a function that updates data based on the provided parameters and returns (obj *Configuration).


```go
func SetDefaults_Configuration((obj *Configuration)) (obj *Configuration)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go:25`



---


[function] name: addDefaultingFuncs file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go:21 returns_error: нет description: —


### addDefaultingFuncs (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go:21)


addDefaultingFuncs is a function that performs operations based on the provided parameters and returns (scheme *kruntime.Scheme).


```go
func addDefaultingFuncs((scheme *kruntime.Scheme)) (scheme *kruntime.Scheme)
```


**Тип запроса:** kruntime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** kruntime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/defaults.go:21`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [addKnownTypes](#addknowntypes-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1registergo48) `:48`

- 🔗 [init](#init-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1registergo41) `:41`


</details>


[function] name: addKnownTypes file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go:48 returns_error: нет description: —


### addKnownTypes (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go:48)


addKnownTypes is a function that performs operations based on the provided parameters and returns (scheme *runtime.Scheme).


```go
func addKnownTypes((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go:48`



---


[function] name: init file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go:41 returns_error: нет description: —


### init (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go:41)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/register.go:41`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Convert_eventratelimit_Configuration_To_v1alpha1_Configuration](#convert_eventratelimit_configuration_to_v1alpha1_configuration-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo78) `:78`

- 🔗 [Convert_eventratelimit_Limit_To_v1alpha1_Limit](#convert_eventratelimit_limit_to_v1alpha1_limit-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo104) `:104`

- 🔗 [Convert_v1alpha1_Configuration_To_eventratelimit_Configuration](#convert_v1alpha1_configuration_to_eventratelimit_configuration-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo68) `:68`

- 🔗 [Convert_v1alpha1_Limit_To_eventratelimit_Limit](#convert_v1alpha1_limit_to_eventratelimit_limit-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo91) `:91`

- 🔗 [RegisterConversions](#registerconversions-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo38) `:38`

- 🔗 [autoConvert_eventratelimit_Configuration_To_v1alpha1_Configuration](#autoconvert_eventratelimit_configuration_to_v1alpha1_configuration-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo72) `:72`

- 🔗 [autoConvert_eventratelimit_Limit_To_v1alpha1_Limit](#autoconvert_eventratelimit_limit_to_v1alpha1_limit-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo95) `:95`

- 🔗 [autoConvert_v1alpha1_Configuration_To_eventratelimit_Configuration](#autoconvert_v1alpha1_configuration_to_eventratelimit_configuration-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo62) `:62`

- 🔗 [autoConvert_v1alpha1_Limit_To_eventratelimit_Limit](#autoconvert_v1alpha1_limit_to_eventratelimit_limit-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo82) `:82`

- 🔗 [init](#init-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generatedconversiongo32) `:32`


</details>


[function] name: Convert_eventratelimit_Configuration_To_v1alpha1_Configuration file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:78 returns_error: нет description: Convert_eventratelimit_Configuration_To_v1alpha1_Configuration is an autogenerated conversion function.


### Convert_eventratelimit_Configuration_To_v1alpha1_Configuration (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:78)


Convert_eventratelimit_Configuration_To_v1alpha1_Configuration is an autogenerated conversion function.


```go
func Convert_eventratelimit_Configuration_To_v1alpha1_Configuration((in *eventratelimit.Configuration, out *Configuration, s conversion.Scope)) (in *eventratelimit.Configuration, out *Configuration, s conversion.Scope)
```


**Тип запроса:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:78`



---


[function] name: Convert_eventratelimit_Limit_To_v1alpha1_Limit file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:104 returns_error: нет description: Convert_eventratelimit_Limit_To_v1alpha1_Limit is an autogenerated conversion function.


### Convert_eventratelimit_Limit_To_v1alpha1_Limit (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:104)


Convert_eventratelimit_Limit_To_v1alpha1_Limit is an autogenerated conversion function.


```go
func Convert_eventratelimit_Limit_To_v1alpha1_Limit((in *eventratelimit.Limit, out *Limit, s conversion.Scope)) (in *eventratelimit.Limit, out *Limit, s conversion.Scope)
```


**Тип запроса:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип запроса:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


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


**Тип ответа:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:104`



---


[function] name: Convert_v1alpha1_Configuration_To_eventratelimit_Configuration file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:68 returns_error: нет description: Convert_v1alpha1_Configuration_To_eventratelimit_Configuration is an autogenerated conversion function.


### Convert_v1alpha1_Configuration_To_eventratelimit_Configuration (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:68)


Convert_v1alpha1_Configuration_To_eventratelimit_Configuration is an autogenerated conversion function.


```go
func Convert_v1alpha1_Configuration_To_eventratelimit_Configuration((in *Configuration, out *eventratelimit.Configuration, s conversion.Scope)) (in *Configuration, out *eventratelimit.Configuration, s conversion.Scope)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:68`



---


[function] name: Convert_v1alpha1_Limit_To_eventratelimit_Limit file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:91 returns_error: нет description: Convert_v1alpha1_Limit_To_eventratelimit_Limit is an autogenerated conversion function.


### Convert_v1alpha1_Limit_To_eventratelimit_Limit (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:91)


Convert_v1alpha1_Limit_To_eventratelimit_Limit is an autogenerated conversion function.


```go
func Convert_v1alpha1_Limit_To_eventratelimit_Limit((in *Limit, out *eventratelimit.Limit, s conversion.Scope)) (in *Limit, out *eventratelimit.Limit, s conversion.Scope)
```


**Тип запроса:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип запроса:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


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


**Тип ответа:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:91`



---


[function] name: RegisterConversions file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:38 returns_error: нет description: RegisterConversions adds conversion functions to the given scheme.
Public to allow building arbitrary schemes.


### RegisterConversions (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:38)


RegisterConversions adds conversion functions to the given scheme.
Public to allow building arbitrary schemes.


```go
func RegisterConversions((s *runtime.Scheme)) (s *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:38`



---


[function] name: autoConvert_eventratelimit_Configuration_To_v1alpha1_Configuration file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:72 returns_error: нет description: —


### autoConvert_eventratelimit_Configuration_To_v1alpha1_Configuration (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:72)


autoConvert_eventratelimit_Configuration_To_v1alpha1_Configuration is a function that performs operations based on the provided parameters and returns (in *eventratelimit.Configuration, out *Configuration, s conversion.Scope).


```go
func autoConvert_eventratelimit_Configuration_To_v1alpha1_Configuration((in *eventratelimit.Configuration, out *Configuration, s conversion.Scope)) (in *eventratelimit.Configuration, out *Configuration, s conversion.Scope)
```


**Тип запроса:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:72`



---


[function] name: autoConvert_eventratelimit_Limit_To_v1alpha1_Limit file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:95 returns_error: нет description: —


### autoConvert_eventratelimit_Limit_To_v1alpha1_Limit (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:95)


autoConvert_eventratelimit_Limit_To_v1alpha1_Limit is a function that performs operations based on the provided parameters and returns (in *eventratelimit.Limit, out *Limit, s conversion.Scope).


```go
func autoConvert_eventratelimit_Limit_To_v1alpha1_Limit((in *eventratelimit.Limit, out *Limit, s conversion.Scope)) (in *eventratelimit.Limit, out *Limit, s conversion.Scope)
```


**Тип запроса:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип запроса:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


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


**Тип ответа:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:95`



---


[function] name: autoConvert_v1alpha1_Configuration_To_eventratelimit_Configuration file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:62 returns_error: нет description: —


### autoConvert_v1alpha1_Configuration_To_eventratelimit_Configuration (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:62)


autoConvert_v1alpha1_Configuration_To_eventratelimit_Configuration is a function that performs operations based on the provided parameters and returns (in *Configuration, out *eventratelimit.Configuration, s conversion.Scope).


```go
func autoConvert_v1alpha1_Configuration_To_eventratelimit_Configuration((in *Configuration, out *eventratelimit.Configuration, s conversion.Scope)) (in *Configuration, out *eventratelimit.Configuration, s conversion.Scope)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** eventratelimit.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:62`



---


[function] name: autoConvert_v1alpha1_Limit_To_eventratelimit_Limit file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:82 returns_error: нет description: —


### autoConvert_v1alpha1_Limit_To_eventratelimit_Limit (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:82)


autoConvert_v1alpha1_Limit_To_eventratelimit_Limit is a function that performs operations based on the provided parameters and returns (in *Limit, out *eventratelimit.Limit, s conversion.Scope).


```go
func autoConvert_v1alpha1_Limit_To_eventratelimit_Limit((in *Limit, out *eventratelimit.Limit, s conversion.Scope)) (in *Limit, out *eventratelimit.Limit, s conversion.Scope)
```


**Тип запроса:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип запроса:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


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


**Тип ответа:** eventratelimit.Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:82`



---


[function] name: init file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:32 returns_error: нет description: —


### init (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:32)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.conversion.go:32`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [DeepCopy](#deepcopy-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddeepcopygo41) `:41`

- 🔗 [DeepCopy](#deepcopy-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddeepcopygo65) `:65`

- 🔗 [DeepCopyInto](#deepcopyinto-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddeepcopygo29) `:29`

- 🔗 [DeepCopyInto](#deepcopyinto-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddeepcopygo59) `:59`

- 🔗 [DeepCopyObject](#deepcopyobject-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddeepcopygo51) `:51`


</details>


[function] name: DeepCopy file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:41 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


### DeepCopy (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:41)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


```go
func (in *Configuration) DeepCopy(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:41`



---


[function] name: DeepCopy file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:65 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Limit.


### DeepCopy (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:65)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Limit.


```go
func (in *Limit) DeepCopy(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:65`



---


[function] name: DeepCopyInto file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:29 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:29)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Configuration) DeepCopyInto((out *Configuration)) (out *Configuration)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:29`



---


[function] name: DeepCopyInto file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:59 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:59)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Limit) DeepCopyInto((out *Limit)) (out *Limit)
```


**Тип запроса:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


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


**Тип ответа:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:59`



---


[function] name: DeepCopyObject file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:51 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:51)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *Configuration) DeepCopyObject(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.deepcopy.go:51`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [RegisterDefaults](#registerdefaults-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddefaultsgo31) `:31`

- 🔗 [SetObjectDefaults_Configuration](#setobjectdefaults_configuration-pluginpkgadmissioneventratelimitapiseventratelimitv1alpha1zz_generateddefaultsgo36) `:36`


</details>


[function] name: RegisterDefaults file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go:31 returns_error: нет description: RegisterDefaults adds defaulters functions to the given scheme.
Public to allow building arbitrary schemes.
All generate


### RegisterDefaults (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go:31)


RegisterDefaults adds defaulters functions to the given scheme.
Public to allow building arbitrary schemes.
All generated defaulters are covering - they call all nested defaulters.


```go
func RegisterDefaults((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go:31`



---


[function] name: SetObjectDefaults_Configuration file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go:36 returns_error: нет description: —


### SetObjectDefaults_Configuration (plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go:36)


SetObjectDefaults_Configuration is a function that updates data based on the provided parameters and returns (in *Configuration).


```go
func SetObjectDefaults_Configuration((in *Configuration)) (in *Configuration)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/zz_generated.defaults.go:36`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/validation/validation.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/validation/validation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ValidateConfiguration](#validateconfiguration-pluginpkgadmissioneventratelimitapiseventratelimitvalidationvalidationgo33) `:33`


</details>


[function] name: ValidateConfiguration file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/validation/validation.go:33 returns_error: нет description: ValidateConfiguration validates the configuration.


### ValidateConfiguration (plugin/pkg/admission/eventratelimit/apis/eventratelimit/validation/validation.go:33)


ValidateConfiguration validates the configuration.


```go
func ValidateConfiguration((config *eventratelimitapi.Configuration)) (config *eventratelimitapi.Configuration)
```


**Тип запроса:** eventratelimitapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** eventratelimitapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/validation/validation.go:33`




## plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [DeepCopy](#deepcopy-pluginpkgadmissioneventratelimitapiseventratelimitzz_generateddeepcopygo41) `:41`

- 🔗 [DeepCopy](#deepcopy-pluginpkgadmissioneventratelimitapiseventratelimitzz_generateddeepcopygo65) `:65`

- 🔗 [DeepCopyInto](#deepcopyinto-pluginpkgadmissioneventratelimitapiseventratelimitzz_generateddeepcopygo29) `:29`

- 🔗 [DeepCopyInto](#deepcopyinto-pluginpkgadmissioneventratelimitapiseventratelimitzz_generateddeepcopygo59) `:59`

- 🔗 [DeepCopyObject](#deepcopyobject-pluginpkgadmissioneventratelimitapiseventratelimitzz_generateddeepcopygo51) `:51`


</details>


[function] name: DeepCopy file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:41 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


### DeepCopy (plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:41)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


```go
func (in *Configuration) DeepCopy(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:41`



---


[function] name: DeepCopy file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:65 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Limit.


### DeepCopy (plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:65)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Limit.


```go
func (in *Limit) DeepCopy(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:65`



---


[function] name: DeepCopyInto file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:29 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:29)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Configuration) DeepCopyInto((out *Configuration)) (out *Configuration)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:29`



---


[function] name: DeepCopyInto file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:59 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:59)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Limit) DeepCopyInto((out *Limit)) (out *Limit)
```


**Тип запроса:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


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


**Тип ответа:** Limit


```json
{
  "Type": {},
  "QPS": 0,
  "Burst": 0,
  "CacheSize": 0
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:59`



---


[function] name: DeepCopyObject file: plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:51 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:51)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *Configuration) DeepCopyObject(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/apis/eventratelimit/zz_generated.deepcopy.go:51`




## plugin/pkg/admission/eventratelimit/cache.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/cache.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [get](#get-pluginpkgadmissioneventratelimitcachego36) `:36`

- 🔗 [get](#get-pluginpkgadmissioneventratelimitcachego48) `:48`


</details>


[function] name: get file: plugin/pkg/admission/eventratelimit/cache.go:36 returns_error: нет description: —


### get (plugin/pkg/admission/eventratelimit/cache.go:36)


get is a method that performs operations based on the provided parameters and returns (key interface{}).


```go
func (c *singleCache) get((key interface{})) (key interface{})
```


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/cache.go:36`



---


[function] name: get file: plugin/pkg/admission/eventratelimit/cache.go:48 returns_error: нет description: —


### get (plugin/pkg/admission/eventratelimit/cache.go:48)


get is a method that performs operations based on the provided parameters and returns (key interface{}).


```go
func (c *lruCache) get((key interface{})) (key interface{})
```


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/cache.go:48`




## plugin/pkg/admission/eventratelimit/config.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/config.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [LoadConfiguration](#loadconfiguration-pluginpkgadmissioneventratelimitconfiggo40) `:40`

- 🔗 [init](#init-pluginpkgadmissioneventratelimitconfiggo35) `:35`


</details>


[function] name: LoadConfiguration file: plugin/pkg/admission/eventratelimit/config.go:40 returns_error: да description: LoadConfiguration loads the provided configuration.


### LoadConfiguration (plugin/pkg/admission/eventratelimit/config.go:40)


LoadConfiguration loads the provided configuration.


```go
func LoadConfiguration((*eventratelimitapi.Configuration, error)) (*eventratelimitapi.Configuration, error)
```


**Тип запроса:** eventratelimitapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** eventratelimitapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*eventratelimitapi.Configuration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/config.go:40`



---


[function] name: init file: plugin/pkg/admission/eventratelimit/config.go:35 returns_error: нет description: —


### init (plugin/pkg/admission/eventratelimit/config.go:35)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/config.go:35`




## plugin/pkg/admission/eventratelimit/limitenforcer.go


📄 Исходный файл: `plugin/pkg/admission/eventratelimit/limitenforcer.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [accept](#accept-pluginpkgadmissioneventratelimitlimitenforcergo89) `:89`

- 🔗 [getNamespaceKey](#getnamespacekey-pluginpkgadmissioneventratelimitlimitenforcergo108) `:108`

- 🔗 [getServerKey](#getserverkey-pluginpkgadmissioneventratelimitlimitenforcergo103) `:103`

- 🔗 [getSourceAndObjectKey](#getsourceandobjectkey-pluginpkgadmissioneventratelimitlimitenforcergo122) `:122`

- 🔗 [getUserKey](#getuserkey-pluginpkgadmissioneventratelimitlimitenforcergo113) `:113`

- 🔗 [newLimitEnforcer](#newlimitenforcer-pluginpkgadmissioneventratelimitlimitenforcergo45) `:45`


</details>


[function] name: accept file: plugin/pkg/admission/eventratelimit/limitenforcer.go:89 returns_error: нет description: —


### accept (plugin/pkg/admission/eventratelimit/limitenforcer.go:89)


accept is a method that performs operations based on the provided parameters and returns (attr admission.Attributes).


```go
func (enforcer *limitEnforcer) accept((attr admission.Attributes)) (attr admission.Attributes)
```


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/limitenforcer.go:89`



---


[function] name: getNamespaceKey file: plugin/pkg/admission/eventratelimit/limitenforcer.go:108 returns_error: нет description: getNamespaceKey returns a cache key that is based on the namespace of the event request


### getNamespaceKey (plugin/pkg/admission/eventratelimit/limitenforcer.go:108)


getNamespaceKey returns a cache key that is based on the namespace of the event request


```go
func getNamespaceKey((attr admission.Attributes)) (attr admission.Attributes)
```


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/limitenforcer.go:108`



---


[function] name: getServerKey file: plugin/pkg/admission/eventratelimit/limitenforcer.go:103 returns_error: нет description: —


### getServerKey (plugin/pkg/admission/eventratelimit/limitenforcer.go:103)


getServerKey is a function that performs operations based on the provided parameters and returns (attr admission.Attributes).


```go
func getServerKey((attr admission.Attributes)) (attr admission.Attributes)
```


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/limitenforcer.go:103`



---


[function] name: getSourceAndObjectKey file: plugin/pkg/admission/eventratelimit/limitenforcer.go:122 returns_error: нет description: getSourceAndObjectKey returns a cache key that is based on the source+object of the event


### getSourceAndObjectKey (plugin/pkg/admission/eventratelimit/limitenforcer.go:122)


getSourceAndObjectKey returns a cache key that is based on the source+object of the event


```go
func getSourceAndObjectKey((attr admission.Attributes)) (attr admission.Attributes)
```


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/limitenforcer.go:122`



---


[function] name: getUserKey file: plugin/pkg/admission/eventratelimit/limitenforcer.go:113 returns_error: нет description: getUserKey returns a cache key that is based on the user of the event request


### getUserKey (plugin/pkg/admission/eventratelimit/limitenforcer.go:113)


getUserKey returns a cache key that is based on the user of the event request


```go
func getUserKey((attr admission.Attributes)) (attr admission.Attributes)
```


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/limitenforcer.go:113`



---


[function] name: newLimitEnforcer file: plugin/pkg/admission/eventratelimit/limitenforcer.go:45 returns_error: да description: —


### newLimitEnforcer (plugin/pkg/admission/eventratelimit/limitenforcer.go:45)


newLimitEnforcer is a function that performs operations based on the provided parameters and may return an error.


```go
func newLimitEnforcer((*limitEnforcer, error)) (*limitEnforcer, error)
```


**Тип запроса:** limitEnforcer


```json
{
  "limitType": {},
  "cache": {},
  "keyFunc": {}
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/limitenforcer.go`


**Тип ответа:** limitEnforcer


```json
{
  "limitType": {},
  "cache": {},
  "keyFunc": {}
}
```


*Определено в:* `plugin/pkg/admission/eventratelimit/limitenforcer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*limitEnforcer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/eventratelimit/limitenforcer.go:45`




## plugin/pkg/admission/extendedresourcetoleration/admission.go


📄 Исходный файл: `plugin/pkg/admission/extendedresourcetoleration/admission.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionextendedresourcetolerationadmissiongo60) `:60`

- 🔗 [Register](#register-pluginpkgadmissionextendedresourcetolerationadmissiongo35) `:35`

- 🔗 [newExtendedResourceToleration](#newextendedresourcetoleration-pluginpkgadmissionextendedresourcetolerationadmissiongo42) `:42`


</details>


[function] name: Admit file: plugin/pkg/admission/extendedresourcetoleration/admission.go:60 returns_error: нет description: Admit updates the toleration of a pod based on the resources requested by it.
If an extended resource of name "example.c


### Admit (plugin/pkg/admission/extendedresourcetoleration/admission.go:60)


Admit updates the toleration of a pod based on the resources requested by it.
If an extended resource of name "example.com/device" is requested, it adds
a toleration with key "example.com/device", operator "Exists" and effect "NoSchedule".
The rationale for this is described in:
https://github.com/kubernetes/kubernetes/issues/55080


```go
func (p *plugin) Admit((ctx context.Context, attributes admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, attributes admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/extendedresourcetoleration/admission.go:60`



---


[function] name: Register file: plugin/pkg/admission/extendedresourcetoleration/admission.go:35 returns_error: нет description: Register is called by the apiserver to register the plugin factory.


### Register (plugin/pkg/admission/extendedresourcetoleration/admission.go:35)


Register is called by the apiserver to register the plugin factory.


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/extendedresourcetoleration/admission.go:35`



---


[function] name: newExtendedResourceToleration file: plugin/pkg/admission/extendedresourcetoleration/admission.go:42 returns_error: нет description: newExtendedResourceToleration creates a new instance of the ExtendedResourceToleration admission controller.


### newExtendedResourceToleration (plugin/pkg/admission/extendedresourcetoleration/admission.go:42)


newExtendedResourceToleration creates a new instance of the ExtendedResourceToleration admission controller.


```go
func newExtendedResourceToleration(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/extendedresourcetoleration/admission.go:42`




## plugin/pkg/admission/gc/gc_admission.go


📄 Исходный файл: `plugin/pkg/admission/gc/gc_admission.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Register](#register-pluginpkgadmissiongcgc_admissiongo39) `:39`

- 🔗 [SetAuthorizer](#setauthorizer-pluginpkgadmissiongcgc_admissiongo296) `:296`

- 🔗 [SetRESTMapper](#setrestmapper-pluginpkgadmissiongcgc_admissiongo300) `:300`

- 🔗 [Validate](#validate-pluginpkgadmissiongcgc_admissiongo89) `:89`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissiongcgc_admissiongo304) `:304`

- 🔗 [blockingOwnerRefs](#blockingownerrefs-pluginpkgadmissiongcgc_admissiongo238) `:238`

- 🔗 [finalizeAnythingRecord](#finalizeanythingrecord-pluginpkgadmissiongcgc_admissiongo189) `:189`

- 🔗 [indexByUID](#indexbyuid-pluginpkgadmissiongcgc_admissiongo248) `:248`

- 🔗 [isChangingOwnerReference](#ischangingownerreference-pluginpkgadmissiongcgc_admissiongo158) `:158`

- 🔗 [isWhiteListed](#iswhitelisted-pluginpkgadmissiongcgc_admissiongo80) `:80`

- 🔗 [newBlockingOwnerDeletionRefs](#newblockingownerdeletionrefs-pluginpkgadmissiongcgc_admissiongo258) `:258`

- 🔗 [ownerRefToDeleteAttributeRecords](#ownerreftodeleteattributerecords-pluginpkgadmissiongcgc_admissiongo206) `:206`


</details>


[function] name: Register file: plugin/pkg/admission/gc/gc_admission.go:39 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/gc/gc_admission.go:39)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:39`



---


[function] name: SetAuthorizer file: plugin/pkg/admission/gc/gc_admission.go:296 returns_error: нет description: —


### SetAuthorizer (plugin/pkg/admission/gc/gc_admission.go:296)


SetAuthorizer is a method that updates data based on the provided parameters and returns (authorizer authorizer.Authorizer).


```go
func (a *gcPermissionsEnforcement) SetAuthorizer((authorizer authorizer.Authorizer)) (authorizer authorizer.Authorizer)
```


**Тип ответа:** authorizer


```json
{
  "userInfo": {},
  "authAuthorizer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/library/authz.go`


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


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:296`



---


[function] name: SetRESTMapper file: plugin/pkg/admission/gc/gc_admission.go:300 returns_error: нет description: —


### SetRESTMapper (plugin/pkg/admission/gc/gc_admission.go:300)


SetRESTMapper is a method that updates data based on the provided parameters and returns (restMapper meta.RESTMapper).


```go
func (a *gcPermissionsEnforcement) SetRESTMapper((restMapper meta.RESTMapper)) (restMapper meta.RESTMapper)
```


**Тип ответа:** restMapper


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** meta.RESTMapper


```json
{
  "initMu": {},
  "delegate": {},
  "cl": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/restmapper/discovery.go`


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:300`



---


[function] name: Validate file: plugin/pkg/admission/gc/gc_admission.go:89 returns_error: да description: —


### Validate (plugin/pkg/admission/gc/gc_admission.go:89)


Validate is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *gcPermissionsEnforcement) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:89`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/gc/gc_admission.go:304 returns_error: нет description: —


### ValidateInitialization (plugin/pkg/admission/gc/gc_admission.go:304)


ValidateInitialization is a method that performs operations based on the provided parameters and returns ().


```go
func (a *gcPermissionsEnforcement) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:304`



---


[function] name: blockingOwnerRefs file: plugin/pkg/admission/gc/gc_admission.go:238 returns_error: нет description: only keeps the blocking refs


### blockingOwnerRefs (plugin/pkg/admission/gc/gc_admission.go:238)


only keeps the blocking refs


```go
func blockingOwnerRefs((refs []metav1.OwnerReference)) (refs []metav1.OwnerReference)
```


**Тип ответа:** refs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.OwnerReference


```json
{
  "apiVersion": "string",
  "kind": "string",
  "name": "string",
  "uid": {},
  "controller": false,
  "blockOwnerDeletion": false
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:238`



---


[function] name: finalizeAnythingRecord file: plugin/pkg/admission/gc/gc_admission.go:189 returns_error: нет description: —


### finalizeAnythingRecord (plugin/pkg/admission/gc/gc_admission.go:189)


finalizeAnythingRecord is a function that performs operations based on the provided parameters and returns (userInfo user.Info).


```go
func finalizeAnythingRecord((userInfo user.Info)) (userInfo user.Info)
```


**Тип ответа:** userInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:189`



---


[function] name: indexByUID file: plugin/pkg/admission/gc/gc_admission.go:248 returns_error: нет description: —


### indexByUID (plugin/pkg/admission/gc/gc_admission.go:248)


indexByUID is a function that performs operations based on the provided parameters and returns (refs []metav1.OwnerReference).


```go
func indexByUID((refs []metav1.OwnerReference)) (refs []metav1.OwnerReference)
```


**Тип ответа:** refs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.OwnerReference


```json
{
  "apiVersion": "string",
  "kind": "string",
  "name": "string",
  "uid": {},
  "controller": false,
  "blockOwnerDeletion": false
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:248`



---


[function] name: isChangingOwnerReference file: plugin/pkg/admission/gc/gc_admission.go:158 returns_error: нет description: —


### isChangingOwnerReference (plugin/pkg/admission/gc/gc_admission.go:158)


isChangingOwnerReference is a function that performs operations based on the provided parameters and returns (newObj, oldObj runtime.Object).


```go
func isChangingOwnerReference((newObj, oldObj runtime.Object)) (newObj, oldObj runtime.Object)
```


**Тип ответа:** newObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:158`



---


[function] name: isWhiteListed file: plugin/pkg/admission/gc/gc_admission.go:80 returns_error: нет description: isWhiteListed returns true if the specified item is in the whitelist.


### isWhiteListed (plugin/pkg/admission/gc/gc_admission.go:80)


isWhiteListed returns true if the specified item is in the whitelist.


```go
func (a *gcPermissionsEnforcement) isWhiteListed((groupResource schema.GroupResource, subresource string)) (groupResource schema.GroupResource, subresource string)
```


**Тип ответа:** groupResource


```json
{
  "etcdLocation": [],
  "etcdPrefix": "string",
  "etcdResourcePrefix": "string",
  "mediaType": "string",
  "serializer": {},
  "cohabitatingResources": [],
  "encoderDecoratorFn": {},
  "decoderDecoratorFn": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/storage/storage_factory.go`


**Тип ответа:** schema.GroupResource


```json
{
  "Group": "string",
  "Resource": "string"
}
```


*Определено в:* `pkg/controller/garbagecollector/config/types.go`


**Тип ответа:** subresource


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:80`



---


[function] name: newBlockingOwnerDeletionRefs file: plugin/pkg/admission/gc/gc_admission.go:258 returns_error: нет description: Returns new blocking ownerReferences, and references whose blockOwnerDeletion
field is changed from nil or false to true


### newBlockingOwnerDeletionRefs (plugin/pkg/admission/gc/gc_admission.go:258)


Returns new blocking ownerReferences, and references whose blockOwnerDeletion
field is changed from nil or false to true.


```go
func newBlockingOwnerDeletionRefs((newObj, oldObj runtime.Object)) (newObj, oldObj runtime.Object)
```


**Тип ответа:** newObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:258`



---


[function] name: ownerRefToDeleteAttributeRecords file: plugin/pkg/admission/gc/gc_admission.go:206 returns_error: да description: Translates ref to a DeleteAttribute deleting the object referred by the ref.
OwnerReference only records the object kind


### ownerRefToDeleteAttributeRecords (plugin/pkg/admission/gc/gc_admission.go:206)


Translates ref to a DeleteAttribute deleting the object referred by the ref.
OwnerReference only records the object kind, which might map to multiple
resources, so multiple DeleteAttribute might be returned.


```go
func (a *gcPermissionsEnforcement) ownerRefToDeleteAttributeRecords(([]authorizer.AttributesRecord, error)) ([]authorizer.AttributesRecord, error)
```


**Тип ответа:** authorizer.AttributesRecord


```json
{
  "User": {},
  "Verb": "string",
  "Namespace": "string",
  "APIGroup": "string",
  "APIVersion": "string",
  "Resource": "string",
  "Subresource": "string",
  "Name": "string",
  "ResourceRequest": false,
  "Path": "string",
  "FieldSelectorRequirements": {},
  "FieldSelectorParsingErr": {},
  "LabelSelectorRequirements": {},
  "LabelSelectorParsingErr": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authorization/authorizer/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]authorizer.AttributesRecord`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/gc/gc_admission.go:206`




## plugin/pkg/admission/imagepolicy/admission.go


📄 Исходный файл: `plugin/pkg/admission/imagepolicy/admission.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [NewImagePolicyWebhook](#newimagepolicywebhook-pluginpkgadmissionimagepolicyadmissiongo256) `:256`

- 🔗 [Register](#register-pluginpkgadmissionimagepolicyadmissiongo71) `:71`

- 🔗 [Validate](#validate-pluginpkgadmissionimagepolicyadmissiongo135) `:135`

- 🔗 [admitPod](#admitpod-pluginpkgadmissionimagepolicyadmissiongo178) `:178`

- 🔗 [filterAnnotations](#filterannotations-pluginpkgadmissionimagepolicyadmissiongo101) `:101`

- 🔗 [statusTTL](#statusttl-pluginpkgadmissionimagepolicyadmissiongo93) `:93`

- 🔗 [webhookError](#webhookerror-pluginpkgadmissionimagepolicyadmissiongo112) `:112`


</details>


[function] name: NewImagePolicyWebhook file: plugin/pkg/admission/imagepolicy/admission.go:256 returns_error: да description: NewImagePolicyWebhook a new ImagePolicyWebhook plugin from the provided config file.
The config file is specified by --a


### NewImagePolicyWebhook (plugin/pkg/admission/imagepolicy/admission.go:256)


NewImagePolicyWebhook a new ImagePolicyWebhook plugin from the provided config file.
The config file is specified by --admission-control-config-file and has the
following format for a webhook:

{
"imagePolicy": {
"kubeConfigFile": "path/to/kubeconfig/for/backend",
"allowTTL": 30,           # time in s to cache approval
"denyTTL": 30,            # time in s to cache denial
"retryBackoff": 500,      # time in ms to wait between retries
"defaultAllow": true      # determines behavior if the webhook backend fails
}
}

The config file may be json or yaml.

The kubeconfig property refers to another file in the kubeconfig format which
specifies how to connect to the webhook backend.

The kubeconfig's cluster field is used to refer to the remote service, user refers to the returned authorizer.

# clusters refers to the remote service.
clusters:
- name: name-of-remote-imagepolicy-service
cluster:
certificate-authority: /path/to/ca.pem      # CA for verifying the remote service.
server: https://images.example.com/policy # URL of remote service to query. Must use 'https'.

# users refers to the API server's webhook configuration.
users:
- name: name-of-api-server
user:
client-certificate: /path/to/cert.pem # cert for the webhook plugin to use
client-key: /path/to/key.pem          # key matching the cert

For additional HTTP configuration, refer to the kubeconfig documentation
http://kubernetes.io/v1.1/docs/user-guide/kubeconfig-file.html.


```go
func NewImagePolicyWebhook((*Plugin, error)) (*Plugin, error)
```


**Тип запроса:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип ответа:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Plugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/admission.go:256`



---


[function] name: Register file: plugin/pkg/admission/imagepolicy/admission.go:71 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/imagepolicy/admission.go:71)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/admission.go:71`



---


[function] name: Validate file: plugin/pkg/admission/imagepolicy/admission.go:135 returns_error: да description: Validate makes an admission decision based on the request attributes


### Validate (plugin/pkg/admission/imagepolicy/admission.go:135)


Validate makes an admission decision based on the request attributes


```go
func (a *Plugin) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/admission.go:135`



---


[function] name: admitPod file: plugin/pkg/admission/imagepolicy/admission.go:178 returns_error: нет description: —


### admitPod (plugin/pkg/admission/imagepolicy/admission.go:178)


admitPod is a method that performs operations based on the provided parameters and returns (ctx context.Context, pod *api.Pod, attributes admission.Attributes, review *v1alpha1.ImageReview).


```go
func (a *Plugin) admitPod((ctx context.Context, pod *api.Pod, attributes admission.Attributes, review *v1alpha1.ImageReview)) (ctx context.Context, pod *api.Pod, attributes admission.Attributes, review *v1alpha1.ImageReview)
```


**Тип запроса:** api.Pod


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


**Тип запроса:** v1alpha1.ImageReview


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/imagepolicy/types.go`


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** review


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1alpha1.ImageReview


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/imagepolicy/types.go`


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/admission.go:178`



---


[function] name: filterAnnotations file: plugin/pkg/admission/imagepolicy/admission.go:101 returns_error: нет description: Filter out annotations that don't match *.image-policy.k8s.io/*


### filterAnnotations (plugin/pkg/admission/imagepolicy/admission.go:101)


Filter out annotations that don't match *.image-policy.k8s.io/*


```go
func (a *Plugin) filterAnnotations((allAnnotations map[string]string)) (allAnnotations map[string]string)
```


**Тип ответа:** allAnnotations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/admission.go:101`



---


[function] name: statusTTL file: plugin/pkg/admission/imagepolicy/admission.go:93 returns_error: нет description: —


### statusTTL (plugin/pkg/admission/imagepolicy/admission.go:93)


statusTTL is a method that performs operations based on the provided parameters and returns (status v1alpha1.ImageReviewStatus).


```go
func (a *Plugin) statusTTL((status v1alpha1.ImageReviewStatus)) (status v1alpha1.ImageReviewStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** v1alpha1.ImageReviewStatus


```json
{
  "Allowed": false,
  "Reason": "string",
  "AuditAnnotations": {}
}
```


*Определено в:* `pkg/apis/imagepolicy/types.go`


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/admission.go:93`



---


[function] name: webhookError file: plugin/pkg/admission/imagepolicy/admission.go:112 returns_error: да description: Function to call on webhook failure; behavior determined by defaultAllow flag


### webhookError (plugin/pkg/admission/imagepolicy/admission.go:112)


Function to call on webhook failure; behavior determined by defaultAllow flag


```go
func (a *Plugin) webhookError((pod *api.Pod, attributes admission.Attributes, err error)) (pod *api.Pod, attributes admission.Attributes, err error)
```


**Тип запроса:** api.Pod


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


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


*Типы возврата:* `pod *api.Pod`, `attributes admission.Attributes`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/admission.go:112`




## plugin/pkg/admission/imagepolicy/config.go


📄 Исходный файл: `plugin/pkg/admission/imagepolicy/config.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [normalizeConfigDuration](#normalizeconfigduration-pluginpkgadmissionimagepolicyconfiggo69) `:69`

- 🔗 [normalizeWebhookConfig](#normalizewebhookconfig-pluginpkgadmissionimagepolicyconfiggo56) `:56`


</details>


[function] name: normalizeConfigDuration file: plugin/pkg/admission/imagepolicy/config.go:69 returns_error: да description: —


### normalizeConfigDuration (plugin/pkg/admission/imagepolicy/config.go:69)


normalizeConfigDuration is a function that performs operations based on the provided parameters and may return an error.


```go
func normalizeConfigDuration((time.Duration, error)) (time.Duration, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `time.Duration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/config.go:69`



---


[function] name: normalizeWebhookConfig file: plugin/pkg/admission/imagepolicy/config.go:56 returns_error: да description: —


### normalizeWebhookConfig (plugin/pkg/admission/imagepolicy/config.go:56)


normalizeWebhookConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func normalizeWebhookConfig((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/imagepolicy/config.go:56`




## plugin/pkg/admission/limitranger/admission.go


📄 Исходный файл: `plugin/pkg/admission/limitranger/admission.go`


<details open>
<summary><b>Функции в этом файле (29)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionlimitrangeradmissiongo111) `:111`

- 🔗 [GetLimitRanges](#getlimitranges-pluginpkgadmissionlimitrangeradmissiongo160) `:160`

- 🔗 [MutateLimit](#mutatelimit-pluginpkgadmissionlimitrangeradmissiongo397) `:397`

- 🔗 [NewLimitRanger](#newlimitranger-pluginpkgadmissionlimitrangeradmissiongo198) `:198`

- 🔗 [PersistentVolumeClaimValidateLimitFunc](#persistentvolumeclaimvalidatelimitfunc-pluginpkgadmissionlimitrangeradmissiongo451) `:451`

- 🔗 [PodMutateLimitFunc](#podmutatelimitfunc-pluginpkgadmissionlimitrangeradmissiongo478) `:478`

- 🔗 [PodValidateLimitFunc](#podvalidatelimitfunc-pluginpkgadmissionlimitrangeradmissiongo486) `:486`

- 🔗 [Register](#register-pluginpkgadmissionlimitrangeradmissiongo55) `:55`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionlimitrangeradmissiongo95) `:95`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionlimitrangeradmissiongo88) `:88`

- 🔗 [SupportsAttributes](#supportsattributes-pluginpkgadmissionlimitrangeradmissiongo420) `:420`

- 🔗 [SupportsLimit](#supportslimit-pluginpkgadmissionlimitrangeradmissiongo443) `:443`

- 🔗 [Validate](#validate-pluginpkgadmissionlimitrangeradmissiongo116) `:116`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionlimitrangeradmissiongo100) `:100`

- 🔗 [ValidateLimit](#validatelimit-pluginpkgadmissionlimitrangeradmissiongo408) `:408`

- 🔗 [addResourceList](#addresourcelist-pluginpkgadmissionlimitrangeradmissiongo692) `:692`

- 🔗 [defaultContainerResourceRequirements](#defaultcontainerresourcerequirements-pluginpkgadmissionlimitrangeradmissiongo216) `:216`

- 🔗 [isSupportedPodLevelResource](#issupportedpodlevelresource-pluginpkgadmissionlimitrangeradmissiongo687) `:687`

- 🔗 [limitRequestRatioConstraint](#limitrequestratioconstraint-pluginpkgadmissionlimitrangeradmissiongo360) `:360`

- 🔗 [maxConstraint](#maxconstraint-pluginpkgadmissionlimitrangeradmissiongo342) `:342`

- 🔗 [maxRequestConstraint](#maxrequestconstraint-pluginpkgadmissionlimitrangeradmissiongo328) `:328`

- 🔗 [maxResourceList](#maxresourcelist-pluginpkgadmissionlimitrangeradmissiongo704) `:704`

- 🔗 [mergeContainerResources](#mergecontainerresources-pluginpkgadmissionlimitrangeradmissiongo236) `:236`

- 🔗 [mergePodResourceRequirements](#mergepodresourcerequirements-pluginpkgadmissionlimitrangeradmissiongo274) `:274`

- 🔗 [minConstraint](#minconstraint-pluginpkgadmissionlimitrangeradmissiongo309) `:309`

- 🔗 [podLimits](#podlimits-pluginpkgadmissionlimitrangeradmissiongo632) `:632`

- 🔗 [podRequests](#podrequests-pluginpkgadmissionlimitrangeradmissiongo574) `:574`

- 🔗 [requestLimitEnforcedValues](#requestlimitenforcedvalues-pluginpkgadmissionlimitrangeradmissiongo295) `:295`

- 🔗 [runLimitFunc](#runlimitfunc-pluginpkgadmissionlimitrangeradmissiongo120) `:120`


</details>


[function] name: Admit file: plugin/pkg/admission/limitranger/admission.go:111 returns_error: да description: Admit admits resources into cluster that do not violate any defined LimitRange in the namespace


### Admit (plugin/pkg/admission/limitranger/admission.go:111)


Admit admits resources into cluster that do not violate any defined LimitRange in the namespace


```go
func (l *LimitRanger) Admit((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:111`



---


[function] name: GetLimitRanges file: plugin/pkg/admission/limitranger/admission.go:160 returns_error: да description: GetLimitRanges returns a LimitRange object with the items held in
the indexer if available, or do alive lookup of the va


### GetLimitRanges (plugin/pkg/admission/limitranger/admission.go:160)


GetLimitRanges returns a LimitRange object with the items held in
the indexer if available, or do alive lookup of the value.


```go
func (l *LimitRanger) GetLimitRanges(([]*corev1.LimitRange, error)) ([]*corev1.LimitRange, error)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*corev1.LimitRange`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:160`



---


[function] name: MutateLimit file: plugin/pkg/admission/limitranger/admission.go:397 returns_error: нет description: MutateLimit enforces resource requirements of incoming resources
against enumerated constraints on the LimitRange.  It m


### MutateLimit (plugin/pkg/admission/limitranger/admission.go:397)


MutateLimit enforces resource requirements of incoming resources
against enumerated constraints on the LimitRange.  It may modify
the incoming object to apply default resource requirements if not
specified, and enumerated on the LimitRange


```go
func (d *DefaultLimitRangerActions) MutateLimit((limitRange *corev1.LimitRange, resourceName string, obj runtime.Object)) (limitRange *corev1.LimitRange, resourceName string, obj runtime.Object)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** limitRange


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/limitrange.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:397`



---


[function] name: NewLimitRanger file: plugin/pkg/admission/limitranger/admission.go:198 returns_error: да description: NewLimitRanger returns an object that enforces limits based on the supplied limit function


### NewLimitRanger (plugin/pkg/admission/limitranger/admission.go:198)


NewLimitRanger returns an object that enforces limits based on the supplied limit function


```go
func NewLimitRanger((*LimitRanger, error)) (*LimitRanger, error)
```


**Тип запроса:** LimitRanger


```json
{
  "client": {},
  "actions": {},
  "lister": {},
  "liveLookupCache": null,
  "group": {},
  "liveTTL": {}
}
```


*Определено в:* `plugin/pkg/admission/limitranger/admission.go`


**Тип ответа:** LimitRanger


```json
{
  "client": {},
  "actions": {},
  "lister": {},
  "liveLookupCache": null,
  "group": {},
  "liveTTL": {}
}
```


*Определено в:* `plugin/pkg/admission/limitranger/admission.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*LimitRanger`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:198`



---


[function] name: PersistentVolumeClaimValidateLimitFunc file: plugin/pkg/admission/limitranger/admission.go:451 returns_error: нет description: PersistentVolumeClaimValidateLimitFunc enforces storage limits for PVCs.
Users request storage via pvc.Spec.Resources.Re


### PersistentVolumeClaimValidateLimitFunc (plugin/pkg/admission/limitranger/admission.go:451)


PersistentVolumeClaimValidateLimitFunc enforces storage limits for PVCs.
Users request storage via pvc.Spec.Resources.Requests.  Min/Max is enforced by an admin with LimitRange.
Claims will not be modified with default values because storage is a required part of pvc.Spec.
All storage enforced values *only* apply to pvc.Spec.Resources.Requests.


```go
func PersistentVolumeClaimValidateLimitFunc((limitRange *corev1.LimitRange, pvc *api.PersistentVolumeClaim)) (limitRange *corev1.LimitRange, pvc *api.PersistentVolumeClaim)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** limitRange


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/limitrange.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvc


```json
{
  "tsInfo": {}
}
```


*Определено в:* `test/e2e/storage/testsuites/pvcdeletionperf.go`


**Тип ответа:** api.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:451`



---


[function] name: PodMutateLimitFunc file: plugin/pkg/admission/limitranger/admission.go:478 returns_error: нет description: PodMutateLimitFunc sets resource requirements enumerated by the pod against
the specified LimitRange.  The pod may be mo


### PodMutateLimitFunc (plugin/pkg/admission/limitranger/admission.go:478)


PodMutateLimitFunc sets resource requirements enumerated by the pod against
the specified LimitRange.  The pod may be modified to apply default resource
requirements if not specified, and enumerated on the LimitRange


```go
func PodMutateLimitFunc((limitRange *corev1.LimitRange, pod *api.Pod)) (limitRange *corev1.LimitRange, pod *api.Pod)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.Pod


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


**Тип ответа:** limitRange


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/limitrange.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:478`



---


[function] name: PodValidateLimitFunc file: plugin/pkg/admission/limitranger/admission.go:486 returns_error: нет description: PodValidateLimitFunc enforces resource requirements enumerated by the pod against
the specified LimitRange.


### PodValidateLimitFunc (plugin/pkg/admission/limitranger/admission.go:486)


PodValidateLimitFunc enforces resource requirements enumerated by the pod against
the specified LimitRange.


```go
func PodValidateLimitFunc((limitRange *corev1.LimitRange, pod *api.Pod)) (limitRange *corev1.LimitRange, pod *api.Pod)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.Pod


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


**Тип ответа:** limitRange


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/limitrange.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:486`



---


[function] name: Register file: plugin/pkg/admission/limitranger/admission.go:55 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/limitranger/admission.go:55)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:55`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/limitranger/admission.go:95 returns_error: нет description: SetExternalKubeClientSet registers the client into LimitRanger


### SetExternalKubeClientSet (plugin/pkg/admission/limitranger/admission.go:95)


SetExternalKubeClientSet registers the client into LimitRanger


```go
func (l *LimitRanger) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:95`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/limitranger/admission.go:88 returns_error: нет description: SetExternalKubeInformerFactory registers an informer factory into the LimitRanger


### SetExternalKubeInformerFactory (plugin/pkg/admission/limitranger/admission.go:88)


SetExternalKubeInformerFactory registers an informer factory into the LimitRanger


```go
func (l *LimitRanger) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:88`



---


[function] name: SupportsAttributes file: plugin/pkg/admission/limitranger/admission.go:420 returns_error: нет description: SupportsAttributes ignores all calls that do not deal with pod resources or storage requests (PVCs).
Also ignores any ca


### SupportsAttributes (plugin/pkg/admission/limitranger/admission.go:420)


SupportsAttributes ignores all calls that do not deal with pod resources or storage requests (PVCs).
Also ignores any call that has a subresource defined.


```go
func (d *DefaultLimitRangerActions) SupportsAttributes((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:420`



---


[function] name: SupportsLimit file: plugin/pkg/admission/limitranger/admission.go:443 returns_error: нет description: SupportsLimit always returns true.


### SupportsLimit (plugin/pkg/admission/limitranger/admission.go:443)


SupportsLimit always returns true.


```go
func (d *DefaultLimitRangerActions) SupportsLimit((limitRange *corev1.LimitRange)) (limitRange *corev1.LimitRange)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** limitRange


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/limitrange.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:443`



---


[function] name: Validate file: plugin/pkg/admission/limitranger/admission.go:116 returns_error: да description: Validate admits resources into cluster that do not violate any defined LimitRange in the namespace


### Validate (plugin/pkg/admission/limitranger/admission.go:116)


Validate admits resources into cluster that do not violate any defined LimitRange in the namespace


```go
func (l *LimitRanger) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:116`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/limitranger/admission.go:100 returns_error: нет description: ValidateInitialization verifies the LimitRanger object has been properly initialized


### ValidateInitialization (plugin/pkg/admission/limitranger/admission.go:100)


ValidateInitialization verifies the LimitRanger object has been properly initialized


```go
func (l *LimitRanger) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:100`



---


[function] name: ValidateLimit file: plugin/pkg/admission/limitranger/admission.go:408 returns_error: нет description: ValidateLimit verifies the resource requirements of incoming
resources against enumerated constraints on the LimitRange 


### ValidateLimit (plugin/pkg/admission/limitranger/admission.go:408)


ValidateLimit verifies the resource requirements of incoming
resources against enumerated constraints on the LimitRange are
valid


```go
func (d *DefaultLimitRangerActions) ValidateLimit((limitRange *corev1.LimitRange, resourceName string, obj runtime.Object)) (limitRange *corev1.LimitRange, resourceName string, obj runtime.Object)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** limitRange


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/limitrange.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:408`



---


[function] name: addResourceList file: plugin/pkg/admission/limitranger/admission.go:692 returns_error: нет description: addResourceList adds the resources in newList to list.


### addResourceList (plugin/pkg/admission/limitranger/admission.go:692)


addResourceList adds the resources in newList to list.


```go
func addResourceList((list, newList api.ResourceList)) (list, newList api.ResourceList)
```


**Тип ответа:** list


```json
{
  "parent": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/listwatch.go`


**Тип ответа:** newList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:692`



---


[function] name: defaultContainerResourceRequirements file: plugin/pkg/admission/limitranger/admission.go:216 returns_error: нет description: defaultContainerResourceRequirements returns the default requirements for a container
the requirement.Limits are taken f


### defaultContainerResourceRequirements (plugin/pkg/admission/limitranger/admission.go:216)


defaultContainerResourceRequirements returns the default requirements for a container
the requirement.Limits are taken from the LimitRange defaults (if specified)
the requirement.Requests are taken from the LimitRange default request (if specified)


```go
func defaultContainerResourceRequirements((limitRange *corev1.LimitRange)) (limitRange *corev1.LimitRange)
```


**Тип запроса:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** limitRange


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/limitrange.go`


**Тип ответа:** corev1.LimitRange


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:216`



---


[function] name: isSupportedPodLevelResource file: plugin/pkg/admission/limitranger/admission.go:687 returns_error: нет description: isSupportedPodLevelResources checks if a given resource is supported by pod-level
resource management through the PodLev


### isSupportedPodLevelResource (plugin/pkg/admission/limitranger/admission.go:687)


isSupportedPodLevelResources checks if a given resource is supported by pod-level
resource management through the PodLevelResources feature. Returns true if
the resource is supported.
isSupportedPodLevelResource method exists in
staging/src/k8s.io/component-helpers/resource/helpers.go.
isSupportedPodLevelResource is added here to avoid conversion of v1.
Pod to api.Pod.
TODO(ndixita): Find alternatives to avoid duplicating the code.


```go
func isSupportedPodLevelResource((name api.ResourceName)) (name api.ResourceName)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** api.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:687`



---


[function] name: limitRequestRatioConstraint file: plugin/pkg/admission/limitranger/admission.go:360 returns_error: нет description: limitRequestRatioConstraint enforces the limit to request ratio over the specified resource


### limitRequestRatioConstraint (plugin/pkg/admission/limitranger/admission.go:360)


limitRequestRatioConstraint enforces the limit to request ratio over the specified resource


```go
func limitRequestRatioConstraint((limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList, limit api.ResourceList)) (limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList, limit api.ResourceList)
```


**Тип ответа:** limitType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** enforced


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resource.Quantity


```json
{
  "i": {},
  "d": {},
  "s": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go`


**Тип ответа:** request


```json
{
  "ctx": {},
  "qs": null,
  "flowDistinguisher": "string",
  "fsName": "string",
  "queue": null,
  "workEstimate": {},
  "decision": {},
  "arrivalTime": {},
  "descr1": {},
  "queueNoteFn": {},
  "removeFromQueueLocked": {},
  "arrivalR": {},
  "startTime": {},
  "waitStarted": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/types.go`


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** limit


```json
{
  "minUID": 0
}
```


*Определено в:* `cmd/kubeadm/app/util/users/users_linux.go`


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:360`



---


[function] name: maxConstraint file: plugin/pkg/admission/limitranger/admission.go:342 returns_error: нет description: maxConstraint enforces the max constraint over the specified resource


### maxConstraint (plugin/pkg/admission/limitranger/admission.go:342)


maxConstraint enforces the max constraint over the specified resource


```go
func maxConstraint((limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList, limit api.ResourceList)) (limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList, limit api.ResourceList)
```


**Тип ответа:** limitType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** enforced


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resource.Quantity


```json
{
  "i": {},
  "d": {},
  "s": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go`


**Тип ответа:** request


```json
{
  "ctx": {},
  "qs": null,
  "flowDistinguisher": "string",
  "fsName": "string",
  "queue": null,
  "workEstimate": {},
  "decision": {},
  "arrivalTime": {},
  "descr1": {},
  "queueNoteFn": {},
  "removeFromQueueLocked": {},
  "arrivalR": {},
  "startTime": {},
  "waitStarted": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/types.go`


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** limit


```json
{
  "minUID": 0
}
```


*Определено в:* `cmd/kubeadm/app/util/users/users_linux.go`


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:342`



---


[function] name: maxRequestConstraint file: plugin/pkg/admission/limitranger/admission.go:328 returns_error: нет description: maxRequestConstraint enforces the max constraint over the specified resource
use when specify LimitType resource doesn't


### maxRequestConstraint (plugin/pkg/admission/limitranger/admission.go:328)


maxRequestConstraint enforces the max constraint over the specified resource
use when specify LimitType resource doesn't recognize limit values


```go
func maxRequestConstraint((limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList)) (limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList)
```


**Тип ответа:** limitType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** enforced


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resource.Quantity


```json
{
  "i": {},
  "d": {},
  "s": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go`


**Тип ответа:** request


```json
{
  "ctx": {},
  "qs": null,
  "flowDistinguisher": "string",
  "fsName": "string",
  "queue": null,
  "workEstimate": {},
  "decision": {},
  "arrivalTime": {},
  "descr1": {},
  "queueNoteFn": {},
  "removeFromQueueLocked": {},
  "arrivalR": {},
  "startTime": {},
  "waitStarted": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/types.go`


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:328`



---


[function] name: maxResourceList file: plugin/pkg/admission/limitranger/admission.go:704 returns_error: нет description: maxResourceList sets list to the greater of list/newList for every resource in newList


### maxResourceList (plugin/pkg/admission/limitranger/admission.go:704)


maxResourceList sets list to the greater of list/newList for every resource in newList


```go
func maxResourceList((list, newList api.ResourceList)) (list, newList api.ResourceList)
```


**Тип ответа:** list


```json
{
  "parent": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/listwatch.go`


**Тип ответа:** newList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:704`



---


[function] name: mergeContainerResources file: plugin/pkg/admission/limitranger/admission.go:236 returns_error: нет description: mergeContainerResources handles defaulting all of the resources on a container.


### mergeContainerResources (plugin/pkg/admission/limitranger/admission.go:236)


mergeContainerResources handles defaulting all of the resources on a container.


```go
func mergeContainerResources((container *api.Container, defaultRequirements *api.ResourceRequirements, annotationPrefix string, annotations []string)) (container *api.Container, defaultRequirements *api.ResourceRequirements, annotationPrefix string, annotations []string)
```


**Тип запроса:** api.Container


```json
{
  "ID": {},
  "Name": "string",
  "Image": "string",
  "ImageID": "string",
  "ImageRef": "string",
  "ImageRuntimeHandler": "string",
  "Hash": 0,
  "State": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип запроса:** api.ResourceRequirements


```json
{
  "Limits": {},
  "Requests": {},
  "Claims": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** container


```json
{
  "Name": "string",
  "State": "string",
  "ExitCode": 0,
  "FinishedAt": "string"
}
```


*Определено в:* `pkg/kubelet/kubelet.go`


**Тип ответа:** api.Container


```json
{
  "ID": {},
  "Name": "string",
  "Image": "string",
  "ImageID": "string",
  "ImageRef": "string",
  "ImageRuntimeHandler": "string",
  "Hash": 0,
  "State": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** defaultRequirements


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ResourceRequirements


```json
{
  "Limits": {},
  "Requests": {},
  "Claims": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** annotationPrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** annotations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:236`



---


[function] name: mergePodResourceRequirements file: plugin/pkg/admission/limitranger/admission.go:274 returns_error: нет description: mergePodResourceRequirements merges enumerated requirements with default requirements
it annotates the pod with informat


### mergePodResourceRequirements (plugin/pkg/admission/limitranger/admission.go:274)


mergePodResourceRequirements merges enumerated requirements with default requirements
it annotates the pod with information about what requirements were modified


```go
func mergePodResourceRequirements((pod *api.Pod, defaultRequirements *api.ResourceRequirements)) (pod *api.Pod, defaultRequirements *api.ResourceRequirements)
```


**Тип запроса:** api.Pod


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


**Тип запроса:** api.ResourceRequirements


```json
{
  "Limits": {},
  "Requests": {},
  "Claims": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


**Тип ответа:** defaultRequirements


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ResourceRequirements


```json
{
  "Limits": {},
  "Requests": {},
  "Claims": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:274`



---


[function] name: minConstraint file: plugin/pkg/admission/limitranger/admission.go:309 returns_error: нет description: minConstraint enforces the min constraint over the specified resource


### minConstraint (plugin/pkg/admission/limitranger/admission.go:309)


minConstraint enforces the min constraint over the specified resource


```go
func minConstraint((limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList, limit api.ResourceList)) (limitType string, resourceName string, enforced resource.Quantity, request api.ResourceList, limit api.ResourceList)
```


**Тип ответа:** limitType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** enforced


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resource.Quantity


```json
{
  "i": {},
  "d": {},
  "s": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go`


**Тип ответа:** request


```json
{
  "ctx": {},
  "qs": null,
  "flowDistinguisher": "string",
  "fsName": "string",
  "queue": null,
  "workEstimate": {},
  "decision": {},
  "arrivalTime": {},
  "descr1": {},
  "queueNoteFn": {},
  "removeFromQueueLocked": {},
  "arrivalR": {},
  "startTime": {},
  "waitStarted": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/types.go`


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** limit


```json
{
  "minUID": 0
}
```


*Определено в:* `cmd/kubeadm/app/util/users/users_linux.go`


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:309`



---


[function] name: podLimits file: plugin/pkg/admission/limitranger/admission.go:632 returns_error: нет description: podLimits is a simplified version of pkg/api/v1/resource/PodLimits that operates against the core version of
pod. Any ch


### podLimits (plugin/pkg/admission/limitranger/admission.go:632)


podLimits is a simplified version of pkg/api/v1/resource/PodLimits that operates against the core version of
pod. Any changes to that calculation should be reflected here.
NOTE: We do not want to check status resources here, only the spec. This is equivalent to setting
UseStatusResources=false in the common helper.
TODO: Maybe we can consider doing a partial conversion of the pod to a v1
type and then using the pkg/api/v1/resource/PodLimits.
TODO(ndixita): PodLimits method exists in
staging/src/k8s.io/component-helpers/resource/helpers.go. Refactor the code to
avoid duplicating podLimits method.


```go
func podLimits((pod *api.Pod, opts podResourcesOptions)) (pod *api.Pod, opts podResourcesOptions)
```


**Тип запроса:** api.Pod


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podResourcesOptions


```json
{
  "PodLevelResourcesEnabled": false
}
```


*Определено в:* `plugin/pkg/admission/limitranger/admission.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:632`



---


[function] name: podRequests file: plugin/pkg/admission/limitranger/admission.go:574 returns_error: нет description: podRequests is a simplified version of pkg/api/v1/resource/PodRequests that operates against the core version of
pod. An


### podRequests (plugin/pkg/admission/limitranger/admission.go:574)


podRequests is a simplified version of pkg/api/v1/resource/PodRequests that operates against the core version of
pod. Any changes to that calculation should be reflected here.
NOTE: We do not want to check status resources here, only the spec. This is equivalent to setting
UseStatusResources=false in the common helper.
TODO: Maybe we can consider doing a partial conversion of the pod to a v1
type and then using the pkg/api/v1/resource/PodRequests.
TODO(ndixita): PodRequests method exists in
staging/src/k8s.io/component-helpers/resource/helpers.go. Refactor the code to
avoid duplicating podRequests method.


```go
func podRequests((pod *api.Pod, opts podResourcesOptions)) (pod *api.Pod, opts podResourcesOptions)
```


**Тип запроса:** api.Pod


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podResourcesOptions


```json
{
  "PodLevelResourcesEnabled": false
}
```


*Определено в:* `plugin/pkg/admission/limitranger/admission.go`


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:574`



---


[function] name: requestLimitEnforcedValues file: plugin/pkg/admission/limitranger/admission.go:295 returns_error: нет description: requestLimitEnforcedValues returns the specified values at a common precision to support comparability


### requestLimitEnforcedValues (plugin/pkg/admission/limitranger/admission.go:295)


requestLimitEnforcedValues returns the specified values at a common precision to support comparability


```go
func requestLimitEnforcedValues((request, limit, enforced int64)) (request, limit, enforced int64)
```


**Тип ответа:** request


```json
{
  "ctx": {},
  "qs": null,
  "flowDistinguisher": "string",
  "fsName": "string",
  "queue": null,
  "workEstimate": {},
  "decision": {},
  "arrivalTime": {},
  "descr1": {},
  "queueNoteFn": {},
  "removeFromQueueLocked": {},
  "arrivalR": {},
  "startTime": {},
  "waitStarted": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/types.go`


**Тип ответа:** limit


```json
{
  "minUID": 0
}
```


*Определено в:* `cmd/kubeadm/app/util/users/users_linux.go`


**Тип ответа:** enforced


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:295`



---


[function] name: runLimitFunc file: plugin/pkg/admission/limitranger/admission.go:120 returns_error: да description: —


### runLimitFunc (plugin/pkg/admission/limitranger/admission.go:120)


runLimitFunc is a method that performs operations based on the provided parameters and may return an error.


```go
func (l *LimitRanger) runLimitFunc((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/limitranger/admission.go:120`




## plugin/pkg/admission/namespace/autoprovision/admission.go


📄 Исходный файл: `plugin/pkg/admission/namespace/autoprovision/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionnamespaceautoprovisionadmissiongo59) `:59`

- 🔗 [NewProvision](#newprovision-pluginpkgadmissionnamespaceautoprovisionadmissiongo102) `:102`

- 🔗 [Register](#register-pluginpkgadmissionnamespaceautoprovisionadmissiongo39) `:39`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionnamespaceautoprovisionadmissiongo109) `:109`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionnamespaceautoprovisionadmissiongo114) `:114`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionnamespaceautoprovisionadmissiongo121) `:121`


</details>


[function] name: Admit file: plugin/pkg/admission/namespace/autoprovision/admission.go:59 returns_error: нет description: Admit makes an admission decision based on the request attributes


### Admit (plugin/pkg/admission/namespace/autoprovision/admission.go:59)


Admit makes an admission decision based on the request attributes


```go
func (p *Provision) Admit((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/namespace/autoprovision/admission.go:59`



---


[function] name: NewProvision file: plugin/pkg/admission/namespace/autoprovision/admission.go:102 returns_error: нет description: NewProvision creates a new namespace provision admission control handler


### NewProvision (plugin/pkg/admission/namespace/autoprovision/admission.go:102)


NewProvision creates a new namespace provision admission control handler


```go
func NewProvision(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/namespace/autoprovision/admission.go:102`



---


[function] name: Register file: plugin/pkg/admission/namespace/autoprovision/admission.go:39 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/namespace/autoprovision/admission.go:39)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/namespace/autoprovision/admission.go:39`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/namespace/autoprovision/admission.go:109 returns_error: нет description: SetExternalKubeClientSet implements the WantsExternalKubeClientSet interface.


### SetExternalKubeClientSet (plugin/pkg/admission/namespace/autoprovision/admission.go:109)


SetExternalKubeClientSet implements the WantsExternalKubeClientSet interface.


```go
func (p *Provision) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/namespace/autoprovision/admission.go:109`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/namespace/autoprovision/admission.go:114 returns_error: нет description: SetExternalKubeInformerFactory implements the WantsExternalKubeInformerFactory interface.


### SetExternalKubeInformerFactory (plugin/pkg/admission/namespace/autoprovision/admission.go:114)


SetExternalKubeInformerFactory implements the WantsExternalKubeInformerFactory interface.


```go
func (p *Provision) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/namespace/autoprovision/admission.go:114`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/namespace/autoprovision/admission.go:121 returns_error: нет description: ValidateInitialization implements the InitializationValidator interface.


### ValidateInitialization (plugin/pkg/admission/namespace/autoprovision/admission.go:121)


ValidateInitialization implements the InitializationValidator interface.


```go
func (p *Provision) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/namespace/autoprovision/admission.go:121`




## plugin/pkg/admission/namespace/exists/admission.go


📄 Исходный файл: `plugin/pkg/admission/namespace/exists/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [NewExists](#newexists-pluginpkgadmissionnamespaceexistsadmissiongo91) `:91`

- 🔗 [Register](#register-pluginpkgadmissionnamespaceexistsadmissiongo38) `:38`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionnamespaceexistsadmissiongo98) `:98`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionnamespaceexistsadmissiongo103) `:103`

- 🔗 [Validate](#validate-pluginpkgadmissionnamespaceexistsadmissiongo58) `:58`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionnamespaceexistsadmissiongo110) `:110`


</details>


[function] name: NewExists file: plugin/pkg/admission/namespace/exists/admission.go:91 returns_error: нет description: NewExists creates a new namespace exists admission control handler


### NewExists (plugin/pkg/admission/namespace/exists/admission.go:91)


NewExists creates a new namespace exists admission control handler


```go
func NewExists(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/namespace/exists/admission.go:91`



---


[function] name: Register file: plugin/pkg/admission/namespace/exists/admission.go:38 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/namespace/exists/admission.go:38)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/namespace/exists/admission.go:38`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/namespace/exists/admission.go:98 returns_error: нет description: SetExternalKubeClientSet implements the WantsExternalKubeClientSet interface.


### SetExternalKubeClientSet (plugin/pkg/admission/namespace/exists/admission.go:98)


SetExternalKubeClientSet implements the WantsExternalKubeClientSet interface.


```go
func (e *Exists) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/namespace/exists/admission.go:98`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/namespace/exists/admission.go:103 returns_error: нет description: SetExternalKubeInformerFactory implements the WantsExternalKubeInformerFactory interface.


### SetExternalKubeInformerFactory (plugin/pkg/admission/namespace/exists/admission.go:103)


SetExternalKubeInformerFactory implements the WantsExternalKubeInformerFactory interface.


```go
func (e *Exists) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/namespace/exists/admission.go:103`



---


[function] name: Validate file: plugin/pkg/admission/namespace/exists/admission.go:58 returns_error: нет description: Validate makes an admission decision based on the request attributes


### Validate (plugin/pkg/admission/namespace/exists/admission.go:58)


Validate makes an admission decision based on the request attributes


```go
func (e *Exists) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/namespace/exists/admission.go:58`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/namespace/exists/admission.go:110 returns_error: нет description: ValidateInitialization implements the InitializationValidator interface.


### ValidateInitialization (plugin/pkg/admission/namespace/exists/admission.go:110)


ValidateInitialization implements the InitializationValidator interface.


```go
func (e *Exists) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/namespace/exists/admission.go:110`




## plugin/pkg/admission/network/defaultingressclass/admission.go


📄 Исходный файл: `plugin/pkg/admission/network/defaultingressclass/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionnetworkdefaultingressclassadmissiongo85) `:85`

- 🔗 [Register](#register-pluginpkgadmissionnetworkdefaultingressclassadmissiongo43) `:43`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionnetworkdefaultingressclassadmissiongo69) `:69`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionnetworkdefaultingressclassadmissiongo76) `:76`

- 🔗 [getDefaultClass](#getdefaultclass-pluginpkgadmissionnetworkdefaultingressclassadmissiongo129) `:129`

- 🔗 [newPlugin](#newplugin-pluginpkgadmissionnetworkdefaultingressclassadmissiongo61) `:61`


</details>


[function] name: Admit file: plugin/pkg/admission/network/defaultingressclass/admission.go:85 returns_error: нет description: Admit sets the default value of a Ingress's class if the user did not specify
a class.


### Admit (plugin/pkg/admission/network/defaultingressclass/admission.go:85)


Admit sets the default value of a Ingress's class if the user did not specify
a class.


```go
func (a *classDefaulterPlugin) Admit((ctx context.Context, attr admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, attr admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/network/defaultingressclass/admission.go:85`



---


[function] name: Register file: plugin/pkg/admission/network/defaultingressclass/admission.go:43 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/network/defaultingressclass/admission.go:43)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/network/defaultingressclass/admission.go:43`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/network/defaultingressclass/admission.go:69 returns_error: нет description: SetExternalKubeInformerFactory sets a lister and readyFunc for this
classDefaulterPlugin using the provided SharedInform


### SetExternalKubeInformerFactory (plugin/pkg/admission/network/defaultingressclass/admission.go:69)


SetExternalKubeInformerFactory sets a lister and readyFunc for this
classDefaulterPlugin using the provided SharedInformerFactory.


```go
func (a *classDefaulterPlugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/network/defaultingressclass/admission.go:69`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/network/defaultingressclass/admission.go:76 returns_error: нет description: ValidateInitialization ensures lister is set.


### ValidateInitialization (plugin/pkg/admission/network/defaultingressclass/admission.go:76)


ValidateInitialization ensures lister is set.


```go
func (a *classDefaulterPlugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/network/defaultingressclass/admission.go:76`



---


[function] name: getDefaultClass file: plugin/pkg/admission/network/defaultingressclass/admission.go:129 returns_error: да description: getDefaultClass returns the default IngressClass from the store, or nil.


### getDefaultClass (plugin/pkg/admission/network/defaultingressclass/admission.go:129)


getDefaultClass returns the default IngressClass from the store, or nil.


```go
func getDefaultClass((*networkingv1.IngressClass, error)) (*networkingv1.IngressClass, error)
```


**Тип запроса:** networkingv1.IngressClass


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/networking/types.go`


**Тип ответа:** networkingv1.IngressClass


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/networking/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*networkingv1.IngressClass`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/network/defaultingressclass/admission.go:129`



---


[function] name: newPlugin file: plugin/pkg/admission/network/defaultingressclass/admission.go:61 returns_error: нет description: newPlugin creates a new admission plugin.


### newPlugin (plugin/pkg/admission/network/defaultingressclass/admission.go:61)


newPlugin creates a new admission plugin.


```go
func newPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/network/defaultingressclass/admission.go:61`




## plugin/pkg/admission/network/denyserviceexternalips/admission.go


📄 Исходный файл: `plugin/pkg/admission/network/denyserviceexternalips/admission.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Register](#register-pluginpkgadmissionnetworkdenyserviceexternalipsadmissiongo36) `:36`

- 🔗 [Validate](#validate-pluginpkgadmissionnetworkdenyserviceexternalipsadmissiongo60) `:60`

- 🔗 [isSubset](#issubset-pluginpkgadmissionnetworkdenyserviceexternalipsadmissiongo94) `:94`

- 🔗 [newPlugin](#newplugin-pluginpkgadmissionnetworkdenyserviceexternalipsadmissiongo52) `:52`


</details>


[function] name: Register file: plugin/pkg/admission/network/denyserviceexternalips/admission.go:36 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/network/denyserviceexternalips/admission.go:36)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/network/denyserviceexternalips/admission.go:36`



---


[function] name: Validate file: plugin/pkg/admission/network/denyserviceexternalips/admission.go:60 returns_error: нет description: Admit ensures that modifications of the Service.Spec.ExternalIPs field are
denied


### Validate (plugin/pkg/admission/network/denyserviceexternalips/admission.go:60)


Admit ensures that modifications of the Service.Spec.ExternalIPs field are
denied


```go
func (plug *externalIPsDenierPlugin) Validate((ctx context.Context, attr admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, attr admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/network/denyserviceexternalips/admission.go:60`



---


[function] name: isSubset file: plugin/pkg/admission/network/denyserviceexternalips/admission.go:94 returns_error: нет description: —


### isSubset (plugin/pkg/admission/network/denyserviceexternalips/admission.go:94)


isSubset is a function that performs operations based on the provided parameters and returns (newSvc, oldSvc *core.Service).


```go
func isSubset((newSvc, oldSvc *core.Service)) (newSvc, oldSvc *core.Service)
```


**Тип запроса:** core.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** newSvc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldSvc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/network/denyserviceexternalips/admission.go:94`



---


[function] name: newPlugin file: plugin/pkg/admission/network/denyserviceexternalips/admission.go:52 returns_error: нет description: newPlugin creates a new admission plugin.


### newPlugin (plugin/pkg/admission/network/denyserviceexternalips/admission.go:52)


newPlugin creates a new admission plugin.


```go
func newPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/network/denyserviceexternalips/admission.go:52`




## plugin/pkg/admission/nodedeclaredfeatures/admission.go


📄 Исходный файл: `plugin/pkg/admission/nodedeclaredfeatures/admission.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [InspectFeatureGates](#inspectfeaturegates-pluginpkgadmissionnodedeclaredfeaturesadmissiongo92) `:92`

- 🔗 [NewPlugin](#newplugin-pluginpkgadmissionnodedeclaredfeaturesadmissiongo67) `:67`

- 🔗 [Register](#register-pluginpkgadmissionnodedeclaredfeaturesadmissiongo47) `:47`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionnodedeclaredfeaturesadmissiongo85) `:85`

- 🔗 [Validate](#validate-pluginpkgadmissionnodedeclaredfeaturesadmissiongo113) `:113`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionnodedeclaredfeaturesadmissiongo97) `:97`

- 🔗 [validatePodUpdate](#validatepodupdate-pluginpkgadmissionnodedeclaredfeaturesadmissiongo159) `:159`


</details>


[function] name: InspectFeatureGates file: plugin/pkg/admission/nodedeclaredfeatures/admission.go:92 returns_error: нет description: SetFeatures sets the feature gates for the plugin.


### InspectFeatureGates (plugin/pkg/admission/nodedeclaredfeatures/admission.go:92)


SetFeatures sets the feature gates for the plugin.


```go
func (p *Plugin) InspectFeatureGates((featureGates featuregate.FeatureGate)) (featureGates featuregate.FeatureGate)
```


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featuregate.FeatureGate


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `plugin/pkg/admission/nodedeclaredfeatures/admission.go:92`



---


[function] name: NewPlugin file: plugin/pkg/admission/nodedeclaredfeatures/admission.go:67 returns_error: да description: New creates a new Plugin admission plugin


### NewPlugin (plugin/pkg/admission/nodedeclaredfeatures/admission.go:67)


New creates a new Plugin admission plugin


```go
func NewPlugin((*Plugin, error)) (*Plugin, error)
```


**Тип запроса:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип ответа:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Plugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/nodedeclaredfeatures/admission.go:67`



---


[function] name: Register file: plugin/pkg/admission/nodedeclaredfeatures/admission.go:47 returns_error: нет description: Register registers a plugin.


### Register (plugin/pkg/admission/nodedeclaredfeatures/admission.go:47)


Register registers a plugin.


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/nodedeclaredfeatures/admission.go:47`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/nodedeclaredfeatures/admission.go:85 returns_error: нет description: SetExternalKubeInformerFactory sets the informer factory for the plugin.


### SetExternalKubeInformerFactory (plugin/pkg/admission/nodedeclaredfeatures/admission.go:85)


SetExternalKubeInformerFactory sets the informer factory for the plugin.


```go
func (p *Plugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/nodedeclaredfeatures/admission.go:85`



---


[function] name: Validate file: plugin/pkg/admission/nodedeclaredfeatures/admission.go:113 returns_error: нет description: Validate is the core of the admission controller logic.


### Validate (plugin/pkg/admission/nodedeclaredfeatures/admission.go:113)


Validate is the core of the admission controller logic.


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/nodedeclaredfeatures/admission.go:113`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/nodedeclaredfeatures/admission.go:97 returns_error: нет description: ValidateInitialization ensures that the plugin is properly initialized.


### ValidateInitialization (plugin/pkg/admission/nodedeclaredfeatures/admission.go:97)


ValidateInitialization ensures that the plugin is properly initialized.


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/nodedeclaredfeatures/admission.go:97`



---


[function] name: validatePodUpdate file: plugin/pkg/admission/nodedeclaredfeatures/admission.go:159 returns_error: нет description: —


### validatePodUpdate (plugin/pkg/admission/nodedeclaredfeatures/admission.go:159)


validatePodUpdate is a method that performs operations based on the provided parameters and returns (pod, oldPod *core.Pod, a admission.Attributes).


```go
func (p *Plugin) validatePodUpdate((pod, oldPod *core.Pod, a admission.Attributes)) (pod, oldPod *core.Pod, a admission.Attributes)
```


**Тип запроса:** core.Pod


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** oldPod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.Pod


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/nodedeclaredfeatures/admission.go:159`




## plugin/pkg/admission/noderestriction/admission.go


📄 Исходный файл: `plugin/pkg/admission/noderestriction/admission.go`


<details open>
<summary><b>Функции в этом файле (29)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionnoderestrictionadmissiongo183) `:183`

- 🔗 [InspectFeatureGates](#inspectfeaturegates-pluginpkgadmissionnoderestrictionadmissiongo107) `:107`

- 🔗 [NewPlugin](#newplugin-pluginpkgadmissionnoderestrictionadmissiongo70) `:70`

- 🔗 [Register](#register-pluginpkgadmissionnoderestrictionadmissiongo62) `:62`

- 🔗 [SetAuthorizer](#setauthorizer-pluginpkgadmissionnoderestrictionadmissiongo164) `:164`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionnoderestrictionadmissiongo117) `:117`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionnoderestrictionadmissiongo130) `:130`

- 🔗 [admitCSINode](#admitcsinode-pluginpkgadmissionnoderestrictionadmissiongo922) `:922`

- 🔗 [admitCSR](#admitcsr-pluginpkgadmissionnoderestrictionadmissiongo974) `:974`

- 🔗 [admitLease](#admitlease-pluginpkgadmissionnoderestrictionadmissiongo897) `:897`

- 🔗 [admitNode](#admitnode-pluginpkgadmissionnoderestrictionadmissiongo501) `:501`

- 🔗 [admitPVCStatus](#admitpvcstatus-pluginpkgadmissionnoderestrictionadmissiongo447) `:447`

- 🔗 [admitPod](#admitpod-pluginpkgadmissionnoderestrictionadmissiongo252) `:252`

- 🔗 [admitPodCertificateRequest](#admitpodcertificaterequest-pluginpkgadmissionnoderestrictionadmissiongo820) `:820`

- 🔗 [admitPodCreate](#admitpodcreate-pluginpkgadmissionnoderestrictionadmissiongo277) `:277`

- 🔗 [admitPodEviction](#admitpodeviction-pluginpkgadmissionnoderestrictionadmissiongo412) `:412`

- 🔗 [admitPodStatus](#admitpodstatus-pluginpkgadmissionnoderestrictionadmissiongo340) `:340`

- 🔗 [admitResourceSlice](#admitresourceslice-pluginpkgadmissionnoderestrictionadmissiongo942) `:942`

- 🔗 [admitServiceAccount](#admitserviceaccount-pluginpkgadmissionnoderestrictionadmissiongo623) `:623`

- 🔗 [csiDriverHasAudience](#csidriverhasaudience-pluginpkgadmissionnoderestrictionadmissiongo806) `:806`

- 🔗 [extendedResourceClaimStatusEqual](#extendedresourceclaimstatusequal-pluginpkgadmissionnoderestrictionadmissiongo395) `:395`

- 🔗 [getCSIFromPVC](#getcsifrompvc-pluginpkgadmissionnoderestrictionadmissiongo779) `:779`

- 🔗 [getForbiddenLabels](#getforbiddenlabels-pluginpkgadmissionnoderestrictionadmissiongo602) `:602`

- 🔗 [getLabelNamespace](#getlabelnamespace-pluginpkgadmissionnoderestrictionadmissiongo594) `:594`

- 🔗 [getModifiedLabels](#getmodifiedlabels-pluginpkgadmissionnoderestrictionadmissiongo568) `:568`

- 🔗 [isKubernetesLabel](#iskuberneteslabel-pluginpkgadmissionnoderestrictionadmissiongo583) `:583`

- 🔗 [podReferencesAudience](#podreferencesaudience-pluginpkgadmissionnoderestrictionadmissiongo721) `:721`

- 🔗 [resourceClaimStatusesEqual](#resourceclaimstatusesequal-pluginpkgadmissionnoderestrictionadmissiongo372) `:372`

- 🔗 [validateNodeServiceAccountAudience](#validatenodeserviceaccountaudience-pluginpkgadmissionnoderestrictionadmissiongo676) `:676`


</details>


[function] name: Admit file: plugin/pkg/admission/noderestriction/admission.go:183 returns_error: нет description: Admit checks the admission policy and triggers corresponding actions


### Admit (plugin/pkg/admission/noderestriction/admission.go:183)


Admit checks the admission policy and triggers corresponding actions


```go
func (p *Plugin) Admit((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:183`



---


[function] name: InspectFeatureGates file: plugin/pkg/admission/noderestriction/admission.go:107 returns_error: нет description: InspectFeatureGates allows setting bools without taking a dep on a global variable


### InspectFeatureGates (plugin/pkg/admission/noderestriction/admission.go:107)


InspectFeatureGates allows setting bools without taking a dep on a global variable


```go
func (p *Plugin) InspectFeatureGates((featureGates featuregate.FeatureGate)) (featureGates featuregate.FeatureGate)
```


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featuregate.FeatureGate


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:107`



---


[function] name: NewPlugin file: plugin/pkg/admission/noderestriction/admission.go:70 returns_error: нет description: NewPlugin creates a new NodeRestriction admission plugin.
This plugin identifies requests from nodes


### NewPlugin (plugin/pkg/admission/noderestriction/admission.go:70)


NewPlugin creates a new NodeRestriction admission plugin.
This plugin identifies requests from nodes


```go
func NewPlugin((nodeIdentifier nodeidentifier.NodeIdentifier)) (nodeIdentifier nodeidentifier.NodeIdentifier)
```


**Тип ответа:** nodeIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeidentifier.NodeIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:70`



---


[function] name: Register file: plugin/pkg/admission/noderestriction/admission.go:62 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/noderestriction/admission.go:62)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:62`



---


[function] name: SetAuthorizer file: plugin/pkg/admission/noderestriction/admission.go:164 returns_error: нет description: SetAuthorizer sets the authorizer.


### SetAuthorizer (plugin/pkg/admission/noderestriction/admission.go:164)


SetAuthorizer sets the authorizer.


```go
func (p *Plugin) SetAuthorizer((authz authorizer.Authorizer)) (authz authorizer.Authorizer)
```


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


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:164`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/noderestriction/admission.go:117 returns_error: нет description: SetExternalKubeInformerFactory registers an informer factory into Plugin


### SetExternalKubeInformerFactory (plugin/pkg/admission/noderestriction/admission.go:117)


SetExternalKubeInformerFactory registers an informer factory into Plugin


```go
func (p *Plugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:117`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/noderestriction/admission.go:130 returns_error: нет description: ValidateInitialization validates the Plugin was initialized properly


### ValidateInitialization (plugin/pkg/admission/noderestriction/admission.go:130)


ValidateInitialization validates the Plugin was initialized properly


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:130`



---


[function] name: admitCSINode file: plugin/pkg/admission/noderestriction/admission.go:922 returns_error: нет description: —


### admitCSINode (plugin/pkg/admission/noderestriction/admission.go:922)


admitCSINode is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitCSINode((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:922`



---


[function] name: admitCSR file: plugin/pkg/admission/noderestriction/admission.go:974 returns_error: нет description: —


### admitCSR (plugin/pkg/admission/noderestriction/admission.go:974)


admitCSR is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitCSR((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:974`



---


[function] name: admitLease file: plugin/pkg/admission/noderestriction/admission.go:897 returns_error: нет description: —


### admitLease (plugin/pkg/admission/noderestriction/admission.go:897)


admitLease is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitLease((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:897`



---


[function] name: admitNode file: plugin/pkg/admission/noderestriction/admission.go:501 returns_error: нет description: —


### admitNode (plugin/pkg/admission/noderestriction/admission.go:501)


admitNode is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitNode((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:501`



---


[function] name: admitPVCStatus file: plugin/pkg/admission/noderestriction/admission.go:447 returns_error: нет description: —


### admitPVCStatus (plugin/pkg/admission/noderestriction/admission.go:447)


admitPVCStatus is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitPVCStatus((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:447`



---


[function] name: admitPod file: plugin/pkg/admission/noderestriction/admission.go:252 returns_error: нет description: admitPod allows creating or deleting a pod if it is assigned to the
current node and fulfills related criteria.


### admitPod (plugin/pkg/admission/noderestriction/admission.go:252)


admitPod allows creating or deleting a pod if it is assigned to the
current node and fulfills related criteria.


```go
func (p *Plugin) admitPod((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:252`



---


[function] name: admitPodCertificateRequest file: plugin/pkg/admission/noderestriction/admission.go:820 returns_error: нет description: —


### admitPodCertificateRequest (plugin/pkg/admission/noderestriction/admission.go:820)


admitPodCertificateRequest is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitPodCertificateRequest((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:820`



---


[function] name: admitPodCreate file: plugin/pkg/admission/noderestriction/admission.go:277 returns_error: нет description: —


### admitPodCreate (plugin/pkg/admission/noderestriction/admission.go:277)


admitPodCreate is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitPodCreate((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:277`



---


[function] name: admitPodEviction file: plugin/pkg/admission/noderestriction/admission.go:412 returns_error: нет description: admitPodEviction allows to evict a pod if it is assigned to the current node.


### admitPodEviction (plugin/pkg/admission/noderestriction/admission.go:412)


admitPodEviction allows to evict a pod if it is assigned to the current node.


```go
func (p *Plugin) admitPodEviction((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:412`



---


[function] name: admitPodStatus file: plugin/pkg/admission/noderestriction/admission.go:340 returns_error: нет description: admitPodStatus allows to update the status of a pod if it is
assigned to the current node.


### admitPodStatus (plugin/pkg/admission/noderestriction/admission.go:340)


admitPodStatus allows to update the status of a pod if it is
assigned to the current node.


```go
func (p *Plugin) admitPodStatus((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:340`



---


[function] name: admitResourceSlice file: plugin/pkg/admission/noderestriction/admission.go:942 returns_error: нет description: —


### admitResourceSlice (plugin/pkg/admission/noderestriction/admission.go:942)


admitResourceSlice is a method that performs operations based on the provided parameters and returns (nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitResourceSlice((nodeName string, a admission.Attributes)) (nodeName string, a admission.Attributes)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:942`



---


[function] name: admitServiceAccount file: plugin/pkg/admission/noderestriction/admission.go:623 returns_error: нет description: —


### admitServiceAccount (plugin/pkg/admission/noderestriction/admission.go:623)


admitServiceAccount is a method that performs operations based on the provided parameters and returns (ctx context.Context, nodeName string, a admission.Attributes).


```go
func (p *Plugin) admitServiceAccount((ctx context.Context, nodeName string, a admission.Attributes)) (ctx context.Context, nodeName string, a admission.Attributes)
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


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:623`



---


[function] name: csiDriverHasAudience file: plugin/pkg/admission/noderestriction/admission.go:806 returns_error: да description: —


### csiDriverHasAudience (plugin/pkg/admission/noderestriction/admission.go:806)


csiDriverHasAudience is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) csiDriverHasAudience((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:806`



---


[function] name: extendedResourceClaimStatusEqual file: plugin/pkg/admission/noderestriction/admission.go:395 returns_error: нет description: —


### extendedResourceClaimStatusEqual (plugin/pkg/admission/noderestriction/admission.go:395)


extendedResourceClaimStatusEqual is a function that performs operations based on the provided parameters and returns (statusA, statusB *api.PodExtendedResourceClaimStatus).


```go
func extendedResourceClaimStatusEqual((statusA, statusB *api.PodExtendedResourceClaimStatus)) (statusA, statusB *api.PodExtendedResourceClaimStatus)
```


**Тип запроса:** api.PodExtendedResourceClaimStatus


```json
{
  "RequestMappings": [],
  "ResourceClaimName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** statusA


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** statusB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodExtendedResourceClaimStatus


```json
{
  "RequestMappings": [],
  "ResourceClaimName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:395`



---


[function] name: getCSIFromPVC file: plugin/pkg/admission/noderestriction/admission.go:779 returns_error: да description: getCSIFromPVC returns the CSI driver name from the PVC->PV->CSI->Driver chain


### getCSIFromPVC (plugin/pkg/admission/noderestriction/admission.go:779)


getCSIFromPVC returns the CSI driver name from the PVC->PV->CSI->Driver chain


```go
func (p *Plugin) getCSIFromPVC((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:779`



---


[function] name: getForbiddenLabels file: plugin/pkg/admission/noderestriction/admission.go:602 returns_error: нет description: getForbiddenLabels returns the set of labels that may not be added, removed, or modified by the node on create or update


### getForbiddenLabels (plugin/pkg/admission/noderestriction/admission.go:602)


getForbiddenLabels returns the set of labels that may not be added, removed, or modified by the node on create or update.


```go
func (p *Plugin) getForbiddenLabels((modifiedLabels sets.String)) (modifiedLabels sets.String)
```


**Тип ответа:** modifiedLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.String


```json
{
  "ID": "string",
  "Secret": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/bootstraptoken/v1/types.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:602`



---


[function] name: getLabelNamespace file: plugin/pkg/admission/noderestriction/admission.go:594 returns_error: нет description: —


### getLabelNamespace (plugin/pkg/admission/noderestriction/admission.go:594)


getLabelNamespace is a function that performs operations based on the provided parameters and returns (key string).


```go
func getLabelNamespace((key string)) (key string)
```


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:594`



---


[function] name: getModifiedLabels file: plugin/pkg/admission/noderestriction/admission.go:568 returns_error: нет description: getModifiedLabels returns the set of label keys that are different between the two maps


### getModifiedLabels (plugin/pkg/admission/noderestriction/admission.go:568)


getModifiedLabels returns the set of label keys that are different between the two maps


```go
func getModifiedLabels((a, b map[string]string)) (a, b map[string]string)
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


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:568`



---


[function] name: isKubernetesLabel file: plugin/pkg/admission/noderestriction/admission.go:583 returns_error: нет description: —


### isKubernetesLabel (plugin/pkg/admission/noderestriction/admission.go:583)


isKubernetesLabel is a function that performs operations based on the provided parameters and returns (key string).


```go
func isKubernetesLabel((key string)) (key string)
```


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:583`



---


[function] name: podReferencesAudience file: plugin/pkg/admission/noderestriction/admission.go:721 returns_error: да description: —


### podReferencesAudience (plugin/pkg/admission/noderestriction/admission.go:721)


podReferencesAudience is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) podReferencesAudience((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:721`



---


[function] name: resourceClaimStatusesEqual file: plugin/pkg/admission/noderestriction/admission.go:372 returns_error: нет description: —


### resourceClaimStatusesEqual (plugin/pkg/admission/noderestriction/admission.go:372)


resourceClaimStatusesEqual is a function that performs operations based on the provided parameters and returns (statusA, statusB []api.PodResourceClaimStatus).


```go
func resourceClaimStatusesEqual((statusA, statusB []api.PodResourceClaimStatus)) (statusA, statusB []api.PodResourceClaimStatus)
```


**Тип ответа:** statusA


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** statusB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodResourceClaimStatus


```json
{
  "Name": "string",
  "ResourceClaimName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:372`



---


[function] name: validateNodeServiceAccountAudience file: plugin/pkg/admission/noderestriction/admission.go:676 returns_error: нет description: —


### validateNodeServiceAccountAudience (plugin/pkg/admission/noderestriction/admission.go:676)


validateNodeServiceAccountAudience is a method that performs operations based on the provided parameters and returns (ctx context.Context, tr *authenticationapi.TokenRequest, pod *v1.Pod, a admission.Attributes).


```go
func (p *Plugin) validateNodeServiceAccountAudience((ctx context.Context, tr *authenticationapi.TokenRequest, pod *v1.Pod, a admission.Attributes)) (ctx context.Context, tr *authenticationapi.TokenRequest, pod *v1.Pod, a admission.Attributes)
```


**Тип запроса:** authenticationapi.TokenRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/authentication/types.go`


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


**Тип ответа:** tr


```json
{
  "stage": "string",
  "fromVersion": "string",
  "defaultVal": false,
  "locked": false
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** authenticationapi.TokenRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/authentication/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/noderestriction/admission.go:676`




## plugin/pkg/admission/nodetaint/admission.go


📄 Исходный файл: `plugin/pkg/admission/nodetaint/admission.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionnodetaintadmissiongo63) `:63`

- 🔗 [NewPlugin](#newplugin-pluginpkgadmissionnodetaintadmissiongo43) `:43`

- 🔗 [Register](#register-pluginpkgadmissionnodetaintadmissiongo35) `:35`

- 🔗 [addNotReadyTaint](#addnotreadytaint-pluginpkgadmissionnodetaintadmissiongo83) `:83`


</details>


[function] name: Admit file: plugin/pkg/admission/nodetaint/admission.go:63 returns_error: нет description: Admit is the main function that checks node identity and adds taints as needed.


### Admit (plugin/pkg/admission/nodetaint/admission.go:63)


Admit is the main function that checks node identity and adds taints as needed.


```go
func (p *Plugin) Admit((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/nodetaint/admission.go:63`



---


[function] name: NewPlugin file: plugin/pkg/admission/nodetaint/admission.go:43 returns_error: нет description: NewPlugin creates a new NodeTaint admission plugin.
This plugin identifies requests from nodes


### NewPlugin (plugin/pkg/admission/nodetaint/admission.go:43)


NewPlugin creates a new NodeTaint admission plugin.
This plugin identifies requests from nodes


```go
func NewPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/nodetaint/admission.go:43`



---


[function] name: Register file: plugin/pkg/admission/nodetaint/admission.go:35 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/nodetaint/admission.go:35)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/nodetaint/admission.go:35`



---


[function] name: addNotReadyTaint file: plugin/pkg/admission/nodetaint/admission.go:83 returns_error: нет description: —


### addNotReadyTaint (plugin/pkg/admission/nodetaint/admission.go:83)


addNotReadyTaint is a function that performs operations based on the provided parameters and returns (node *api.Node).


```go
func addNotReadyTaint((node *api.Node)) (node *api.Node)
```


**Тип запроса:** api.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** node


```json
{
  "identity": {},
  "dependentsLock": {},
  "dependents": {},
  "deletingDependents": false,
  "deletingDependentsLock": {},
  "beingDeleted": false,
  "beingDeletedLock": {},
  "virtual": false,
  "virtualLock": {},
  "owners": [],
  "ownersLock": {}
}
```


*Определено в:* `pkg/controller/garbagecollector/graph.go`


**Тип ответа:** api.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/nodetaint/admission.go:83`




## plugin/pkg/admission/podnodeselector/admission.go


📄 Исходный файл: `plugin/pkg/admission/podnodeselector/admission.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionpodnodeselectoradmissiongo101) `:101`

- 🔗 [NewPodNodeSelector](#newpodnodeselector-pluginpkgadmissionpodnodeselectoradmissiongo196) `:196`

- 🔗 [Register](#register-pluginpkgadmissionpodnodeselectoradmissiongo49) `:49`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionpodnodeselectoradmissiongo204) `:204`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionpodnodeselectoradmissiongo209) `:209`

- 🔗 [Validate](#validate-pluginpkgadmissionpodnodeselectoradmissiongo128) `:128`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionpodnodeselectoradmissiongo216) `:216`

- 🔗 [defaultGetNamespace](#defaultgetnamespace-pluginpkgadmissionpodnodeselectoradmissiongo226) `:226`

- 🔗 [getNamespaceNodeSelectorMap](#getnamespacenodeselectormap-pluginpkgadmissionpodnodeselectoradmissiongo159) `:159`

- 🔗 [getNodeSelectorMap](#getnodeselectormap-pluginpkgadmissionpodnodeselectoradmissiongo234) `:234`

- 🔗 [isSubset](#issubset-pluginpkgadmissionpodnodeselectoradmissiongo264) `:264`

- 🔗 [readConfig](#readconfig-pluginpkgadmissionpodnodeselectoradmissiongo83) `:83`

- 🔗 [shouldIgnore](#shouldignore-pluginpkgadmissionpodnodeselectoradmissiongo176) `:176`


</details>


[function] name: Admit file: plugin/pkg/admission/podnodeselector/admission.go:101 returns_error: нет description: Admit enforces that pod and its namespace node label selectors matches at least a node in the cluster.


### Admit (plugin/pkg/admission/podnodeselector/admission.go:101)


Admit enforces that pod and its namespace node label selectors matches at least a node in the cluster.


```go
func (p *Plugin) Admit((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:101`



---


[function] name: NewPodNodeSelector file: plugin/pkg/admission/podnodeselector/admission.go:196 returns_error: нет description: NewPodNodeSelector initializes a podNodeSelector


### NewPodNodeSelector (plugin/pkg/admission/podnodeselector/admission.go:196)


NewPodNodeSelector initializes a podNodeSelector


```go
func NewPodNodeSelector((clusterNodeSelectors map[string]string)) (clusterNodeSelectors map[string]string)
```


**Тип ответа:** clusterNodeSelectors


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:196`



---


[function] name: Register file: plugin/pkg/admission/podnodeselector/admission.go:49 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/podnodeselector/admission.go:49)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:49`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/podnodeselector/admission.go:204 returns_error: нет description: SetExternalKubeClientSet sets the plugin's client


### SetExternalKubeClientSet (plugin/pkg/admission/podnodeselector/admission.go:204)


SetExternalKubeClientSet sets the plugin's client


```go
func (p *Plugin) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:204`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/podnodeselector/admission.go:209 returns_error: нет description: SetExternalKubeInformerFactory configures the plugin's informer factory


### SetExternalKubeInformerFactory (plugin/pkg/admission/podnodeselector/admission.go:209)


SetExternalKubeInformerFactory configures the plugin's informer factory


```go
func (p *Plugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:209`



---


[function] name: Validate file: plugin/pkg/admission/podnodeselector/admission.go:128 returns_error: нет description: Validate ensures that the pod node selector is allowed


### Validate (plugin/pkg/admission/podnodeselector/admission.go:128)


Validate ensures that the pod node selector is allowed


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:128`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/podnodeselector/admission.go:216 returns_error: нет description: ValidateInitialization verifies the object has been properly initialized


### ValidateInitialization (plugin/pkg/admission/podnodeselector/admission.go:216)


ValidateInitialization verifies the object has been properly initialized


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:216`



---


[function] name: defaultGetNamespace file: plugin/pkg/admission/podnodeselector/admission.go:226 returns_error: да description: —


### defaultGetNamespace (plugin/pkg/admission/podnodeselector/admission.go:226)


defaultGetNamespace is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) defaultGetNamespace((*corev1.Namespace, error)) (*corev1.Namespace, error)
```


**Тип запроса:** corev1.Namespace


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.Namespace


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Namespace`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:226`



---


[function] name: getNamespaceNodeSelectorMap file: plugin/pkg/admission/podnodeselector/admission.go:159 returns_error: да description: —


### getNamespaceNodeSelectorMap (plugin/pkg/admission/podnodeselector/admission.go:159)


getNamespaceNodeSelectorMap is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) getNamespaceNodeSelectorMap((labels.Set, error)) (labels.Set, error)
```


**Тип ответа:** labels.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `labels.Set`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:159`



---


[function] name: getNodeSelectorMap file: plugin/pkg/admission/podnodeselector/admission.go:234 returns_error: да description: —


### getNodeSelectorMap (plugin/pkg/admission/podnodeselector/admission.go:234)


getNodeSelectorMap is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) getNodeSelectorMap((labels.Set, error)) (labels.Set, error)
```


**Тип ответа:** labels.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `labels.Set`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:234`



---


[function] name: isSubset file: plugin/pkg/admission/podnodeselector/admission.go:264 returns_error: нет description: —


### isSubset (plugin/pkg/admission/podnodeselector/admission.go:264)


isSubset is a function that performs operations based on the provided parameters and returns (subSet, superSet labels.Set).


```go
func isSubset((subSet, superSet labels.Set)) (subSet, superSet labels.Set)
```


**Тип ответа:** subSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** superSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labels.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:264`



---


[function] name: readConfig file: plugin/pkg/admission/podnodeselector/admission.go:83 returns_error: нет description: readConfig reads default value of clusterDefaultNodeSelector
from the file provided with --admission-control-config-file


### readConfig (plugin/pkg/admission/podnodeselector/admission.go:83)


readConfig reads default value of clusterDefaultNodeSelector
from the file provided with --admission-control-config-file
If the file is not supplied, it defaults to ""
The format in a file:
podNodeSelectorPluginConfig:

clusterDefaultNodeSelector: <node-selectors-labels>
namespace1: <node-selectors-labels>
namespace2: <node-selectors-labels>


```go
func readConfig((config io.Reader)) (config io.Reader)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** io.Reader


```json
{
  "logger": {},
  "err": {},
  "r": {},
  "ping": false,
  "timeout": {},
  "protocols": {},
  "selectedProtocol": "string",
  "handleCrash": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/stream.go`


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:83`



---


[function] name: shouldIgnore file: plugin/pkg/admission/podnodeselector/admission.go:176 returns_error: нет description: —


### shouldIgnore (plugin/pkg/admission/podnodeselector/admission.go:176)


shouldIgnore is a function that performs operations based on the provided parameters and returns (a admission.Attributes).


```go
func shouldIgnore((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/podnodeselector/admission.go:176`




## plugin/pkg/admission/podtolerationrestriction/admission.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/admission.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionpodtolerationrestrictionadmissiongo76) `:76`

- 🔗 [NewPodTolerationsPlugin](#newpodtolerationsplugin-pluginpkgadmissionpodtolerationrestrictionadmissiongo174) `:174`

- 🔗 [Register](#register-pluginpkgadmissionpodtolerationrestrictionadmissiongo46) `:46`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionpodtolerationrestrictionadmissiongo182) `:182`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionpodtolerationrestrictionadmissiongo187) `:187`

- 🔗 [Validate](#validate-pluginpkgadmissionpodtolerationrestrictionadmissiongo117) `:117`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionpodtolerationrestrictionadmissiongo195) `:195`

- 🔗 [extractNSTolerations](#extractnstolerations-pluginpkgadmissionpodtolerationrestrictionadmissiongo246) `:246`

- 🔗 [getNamespace](#getnamespace-pluginpkgadmissionpodtolerationrestrictionadmissiongo206) `:206`

- 🔗 [getNamespaceDefaultTolerations](#getnamespacedefaulttolerations-pluginpkgadmissionpodtolerationrestrictionadmissiongo224) `:224`

- 🔗 [getNamespaceTolerationsWhitelist](#getnamespacetolerationswhitelist-pluginpkgadmissionpodtolerationrestrictionadmissiongo232) `:232`

- 🔗 [shouldIgnore](#shouldignore-pluginpkgadmissionpodtolerationrestrictionadmissiongo153) `:153`


</details>


[function] name: Admit file: plugin/pkg/admission/podtolerationrestriction/admission.go:76 returns_error: нет description: Admit checks the admission policy and triggers corresponding actions


### Admit (plugin/pkg/admission/podtolerationrestriction/admission.go:76)


Admit checks the admission policy and triggers corresponding actions


```go
func (p *Plugin) Admit((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:76`



---


[function] name: NewPodTolerationsPlugin file: plugin/pkg/admission/podtolerationrestriction/admission.go:174 returns_error: нет description: NewPodTolerationsPlugin initializes a Plugin


### NewPodTolerationsPlugin (plugin/pkg/admission/podtolerationrestriction/admission.go:174)


NewPodTolerationsPlugin initializes a Plugin


```go
func NewPodTolerationsPlugin((pluginConfig *pluginapi.Configuration)) (pluginConfig *pluginapi.Configuration)
```


**Тип запроса:** pluginapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** pluginConfig


```json
{
  "PodNodeSelectorPluginConfig": {}
}
```


*Определено в:* `plugin/pkg/admission/podnodeselector/admission.go`


**Тип ответа:** pluginapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:174`



---


[function] name: Register file: plugin/pkg/admission/podtolerationrestriction/admission.go:46 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/podtolerationrestriction/admission.go:46)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:46`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/podtolerationrestriction/admission.go:182 returns_error: нет description: SetExternalKubeClientSet sets th client


### SetExternalKubeClientSet (plugin/pkg/admission/podtolerationrestriction/admission.go:182)


SetExternalKubeClientSet sets th client


```go
func (p *Plugin) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:182`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/podtolerationrestriction/admission.go:187 returns_error: нет description: SetExternalKubeInformerFactory initializes the Informer Factory


### SetExternalKubeInformerFactory (plugin/pkg/admission/podtolerationrestriction/admission.go:187)


SetExternalKubeInformerFactory initializes the Informer Factory


```go
func (p *Plugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:187`



---


[function] name: Validate file: plugin/pkg/admission/podtolerationrestriction/admission.go:117 returns_error: нет description: Validate we can obtain a whitelist of tolerations


### Validate (plugin/pkg/admission/podtolerationrestriction/admission.go:117)


Validate we can obtain a whitelist of tolerations


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:117`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/podtolerationrestriction/admission.go:195 returns_error: нет description: ValidateInitialization checks the object is properly initialized


### ValidateInitialization (plugin/pkg/admission/podtolerationrestriction/admission.go:195)


ValidateInitialization checks the object is properly initialized


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:195`



---


[function] name: extractNSTolerations file: plugin/pkg/admission/podtolerationrestriction/admission.go:246 returns_error: да description: extractNSTolerations extracts default or whitelist of tolerations from
following namespace annotations keys: "scheduler.


### extractNSTolerations (plugin/pkg/admission/podtolerationrestriction/admission.go:246)


extractNSTolerations extracts default or whitelist of tolerations from
following namespace annotations keys: "scheduler.alpha.kubernetes.io/defaultTolerations"
and "scheduler.alpha.kubernetes.io/tolerationsWhitelist". If these keys are
unset (nil), extractNSTolerations returns nil. If the value to these
keys are set to empty, an empty toleration is returned, otherwise
configured tolerations are returned.


```go
func extractNSTolerations(([]api.Toleration, error)) ([]api.Toleration, error)
```


**Тип ответа:** api.Toleration


```json
{
  "Key": "string",
  "Operator": {},
  "Value": "string",
  "Effect": {},
  "TolerationSeconds": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]api.Toleration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:246`



---


[function] name: getNamespace file: plugin/pkg/admission/podtolerationrestriction/admission.go:206 returns_error: да description: in exceptional cases, this can result in two live calls, but once the cache catches up, that will stop.


### getNamespace (plugin/pkg/admission/podtolerationrestriction/admission.go:206)


in exceptional cases, this can result in two live calls, but once the cache catches up, that will stop.


```go
func (p *Plugin) getNamespace((*corev1.Namespace, error)) (*corev1.Namespace, error)
```


**Тип запроса:** corev1.Namespace


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.Namespace


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Namespace`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:206`



---


[function] name: getNamespaceDefaultTolerations file: plugin/pkg/admission/podtolerationrestriction/admission.go:224 returns_error: да description: —


### getNamespaceDefaultTolerations (plugin/pkg/admission/podtolerationrestriction/admission.go:224)


getNamespaceDefaultTolerations is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) getNamespaceDefaultTolerations(([]api.Toleration, error)) ([]api.Toleration, error)
```


**Тип ответа:** api.Toleration


```json
{
  "Key": "string",
  "Operator": {},
  "Value": "string",
  "Effect": {},
  "TolerationSeconds": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]api.Toleration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:224`



---


[function] name: getNamespaceTolerationsWhitelist file: plugin/pkg/admission/podtolerationrestriction/admission.go:232 returns_error: да description: —


### getNamespaceTolerationsWhitelist (plugin/pkg/admission/podtolerationrestriction/admission.go:232)


getNamespaceTolerationsWhitelist is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) getNamespaceTolerationsWhitelist(([]api.Toleration, error)) ([]api.Toleration, error)
```


**Тип ответа:** api.Toleration


```json
{
  "Key": "string",
  "Operator": {},
  "Value": "string",
  "Effect": {},
  "TolerationSeconds": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]api.Toleration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:232`



---


[function] name: shouldIgnore file: plugin/pkg/admission/podtolerationrestriction/admission.go:153 returns_error: нет description: —


### shouldIgnore (plugin/pkg/admission/podtolerationrestriction/admission.go:153)


shouldIgnore is a function that performs operations based on the provided parameters and returns (a admission.Attributes).


```go
func shouldIgnore((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/admission.go:153`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/install/install.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/install/install.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Install](#install-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictioninstallinstallgo29) `:29`


</details>


[function] name: Install file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/install/install.go:29 returns_error: нет description: Install registers the API group and adds types to a scheme


### Install (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/install/install.go:29)


Install registers the API group and adds types to a scheme


```go
func Install((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/install/install.go:29`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Kind](#kind-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionregistergo38) `:38`

- 🔗 [Resource](#resource-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionregistergo43) `:43`

- 🔗 [addKnownTypes](#addknowntypes-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionregistergo47) `:47`


</details>


[function] name: Kind file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:38 returns_error: нет description: Kind takes an unqualified kind and returns a Group qualified GroupKind


### Kind (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:38)


Kind takes an unqualified kind and returns a Group qualified GroupKind


```go
func Kind((kind string)) (kind string)
```


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:38`



---


[function] name: Resource file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:43 returns_error: нет description: Resource takes an unqualified resource and returns a Group qualified GroupResource


### Resource (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:43)


Resource takes an unqualified resource and returns a Group qualified GroupResource


```go
func Resource((resource string)) (resource string)
```


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:43`



---


[function] name: addKnownTypes file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:47 returns_error: нет description: —


### addKnownTypes (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:47)


addKnownTypes is a function that performs operations based on the provided parameters and returns (scheme *runtime.Scheme).


```go
func addKnownTypes((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/register.go:47`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/defaults.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/defaults.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [addDefaultingFuncs](#adddefaultingfuncs-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1defaultsgo21) `:21`


</details>


[function] name: addDefaultingFuncs file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/defaults.go:21 returns_error: нет description: —


### addDefaultingFuncs (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/defaults.go:21)


addDefaultingFuncs is a function that performs operations based on the provided parameters and returns (scheme *runtime.Scheme).


```go
func addDefaultingFuncs((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/defaults.go:21`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [addKnownTypes](#addknowntypes-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1registergo48) `:48`

- 🔗 [init](#init-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1registergo41) `:41`


</details>


[function] name: addKnownTypes file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go:48 returns_error: нет description: —


### addKnownTypes (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go:48)


addKnownTypes is a function that performs operations based on the provided parameters and returns (scheme *runtime.Scheme).


```go
func addKnownTypes((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go:48`



---


[function] name: init file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go:41 returns_error: нет description: —


### init (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go:41)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/register.go:41`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Convert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration](#convert_podtolerationrestriction_configuration_to_v1alpha1_configuration-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generatedconversiongo72) `:72`

- 🔗 [Convert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration](#convert_v1alpha1_configuration_to_podtolerationrestriction_configuration-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generatedconversiongo61) `:61`

- 🔗 [RegisterConversions](#registerconversions-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generatedconversiongo40) `:40`

- 🔗 [autoConvert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration](#autoconvert_podtolerationrestriction_configuration_to_v1alpha1_configuration-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generatedconversiongo65) `:65`

- 🔗 [autoConvert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration](#autoconvert_v1alpha1_configuration_to_podtolerationrestriction_configuration-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generatedconversiongo54) `:54`

- 🔗 [init](#init-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generatedconversiongo34) `:34`


</details>


[function] name: Convert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:72 returns_error: нет description: Convert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration is an autogenerated conversion function.


### Convert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:72)


Convert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration is an autogenerated conversion function.


```go
func Convert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration((in *podtolerationrestriction.Configuration, out *Configuration, s conversion.Scope)) (in *podtolerationrestriction.Configuration, out *Configuration, s conversion.Scope)
```


**Тип запроса:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:72`



---


[function] name: Convert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:61 returns_error: нет description: Convert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration is an autogenerated conversion function.


### Convert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:61)


Convert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration is an autogenerated conversion function.


```go
func Convert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration((in *Configuration, out *podtolerationrestriction.Configuration, s conversion.Scope)) (in *Configuration, out *podtolerationrestriction.Configuration, s conversion.Scope)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:61`



---


[function] name: RegisterConversions file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:40 returns_error: нет description: RegisterConversions adds conversion functions to the given scheme.
Public to allow building arbitrary schemes.


### RegisterConversions (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:40)


RegisterConversions adds conversion functions to the given scheme.
Public to allow building arbitrary schemes.


```go
func RegisterConversions((s *runtime.Scheme)) (s *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:40`



---


[function] name: autoConvert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:65 returns_error: нет description: —


### autoConvert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:65)


autoConvert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration is a function that performs operations based on the provided parameters and returns (in *podtolerationrestriction.Configuration, out *Configuration, s conversion.Scope).


```go
func autoConvert_podtolerationrestriction_Configuration_To_v1alpha1_Configuration((in *podtolerationrestriction.Configuration, out *Configuration, s conversion.Scope)) (in *podtolerationrestriction.Configuration, out *Configuration, s conversion.Scope)
```


**Тип запроса:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:65`



---


[function] name: autoConvert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:54 returns_error: нет description: —


### autoConvert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:54)


autoConvert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration is a function that performs operations based on the provided parameters and returns (in *Configuration, out *podtolerationrestriction.Configuration, s conversion.Scope).


```go
func autoConvert_v1alpha1_Configuration_To_podtolerationrestriction_Configuration((in *Configuration, out *podtolerationrestriction.Configuration, s conversion.Scope)) (in *Configuration, out *podtolerationrestriction.Configuration, s conversion.Scope)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип запроса:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** podtolerationrestriction.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:54`



---


[function] name: init file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:34 returns_error: нет description: —


### init (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:34)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.conversion.go:34`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DeepCopy](#deepcopy-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generateddeepcopygo51) `:51`

- 🔗 [DeepCopyInto](#deepcopyinto-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generateddeepcopygo30) `:30`

- 🔗 [DeepCopyObject](#deepcopyobject-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generateddeepcopygo61) `:61`


</details>


[function] name: DeepCopy file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:51 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


### DeepCopy (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:51)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


```go
func (in *Configuration) DeepCopy(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:51`



---


[function] name: DeepCopyInto file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:30 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:30)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Configuration) DeepCopyInto((out *Configuration)) (out *Configuration)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:30`



---


[function] name: DeepCopyObject file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:61 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:61)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *Configuration) DeepCopyObject(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.deepcopy.go:61`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.defaults.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.defaults.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RegisterDefaults](#registerdefaults-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionv1alpha1zz_generateddefaultsgo31) `:31`


</details>


[function] name: RegisterDefaults file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.defaults.go:31 returns_error: нет description: RegisterDefaults adds defaulters functions to the given scheme.
Public to allow building arbitrary schemes.
All generate


### RegisterDefaults (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.defaults.go:31)


RegisterDefaults adds defaulters functions to the given scheme.
Public to allow building arbitrary schemes.
All generated defaulters are covering - they call all nested defaulters.


```go
func RegisterDefaults((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/zz_generated.defaults.go:31`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/validation/validation.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/validation/validation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ValidateConfiguration](#validateconfiguration-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionvalidationvalidationgo28) `:28`


</details>


[function] name: ValidateConfiguration file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/validation/validation.go:28 returns_error: нет description: ValidateConfiguration validates the configuration.


### ValidateConfiguration (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/validation/validation.go:28)


ValidateConfiguration validates the configuration.


```go
func ValidateConfiguration((config *internalapi.Configuration)) (config *internalapi.Configuration)
```


**Тип запроса:** internalapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** internalapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/validation/validation.go:28`




## plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DeepCopy](#deepcopy-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionzz_generateddeepcopygo51) `:51`

- 🔗 [DeepCopyInto](#deepcopyinto-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionzz_generateddeepcopygo30) `:30`

- 🔗 [DeepCopyObject](#deepcopyobject-pluginpkgadmissionpodtolerationrestrictionapispodtolerationrestrictionzz_generateddeepcopygo61) `:61`


</details>


[function] name: DeepCopy file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:51 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


### DeepCopy (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:51)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Configuration.


```go
func (in *Configuration) DeepCopy(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:51`



---


[function] name: DeepCopyInto file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:30 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:30)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *Configuration) DeepCopyInto((out *Configuration)) (out *Configuration)
```


**Тип запроса:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


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


**Тип ответа:** Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:30`



---


[function] name: DeepCopyObject file: plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:61 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:61)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *Configuration) DeepCopyObject(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/zz_generated.deepcopy.go:61`




## plugin/pkg/admission/podtolerationrestriction/config.go


📄 Исходный файл: `plugin/pkg/admission/podtolerationrestriction/config.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-pluginpkgadmissionpodtolerationrestrictionconfiggo36) `:36`

- 🔗 [loadConfiguration](#loadconfiguration-pluginpkgadmissionpodtolerationrestrictionconfiggo41) `:41`


</details>


[function] name: init file: plugin/pkg/admission/podtolerationrestriction/config.go:36 returns_error: нет description: —


### init (plugin/pkg/admission/podtolerationrestriction/config.go:36)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/config.go:36`



---


[function] name: loadConfiguration file: plugin/pkg/admission/podtolerationrestriction/config.go:41 returns_error: да description: LoadConfiguration loads the provided configuration.


### loadConfiguration (plugin/pkg/admission/podtolerationrestriction/config.go:41)


LoadConfiguration loads the provided configuration.


```go
func loadConfiguration((*internalapi.Configuration, error)) (*internalapi.Configuration, error)
```


**Тип запроса:** internalapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Тип ответа:** internalapi.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*internalapi.Configuration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podtolerationrestriction/config.go:41`




## plugin/pkg/admission/podtopologylabels/admission.go


📄 Исходный файл: `plugin/pkg/admission/podtopologylabels/admission.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionpodtopologylabelsadmissiongo109) `:109`

- 🔗 [InspectFeatureGates](#inspectfeaturegates-pluginpkgadmissionpodtopologylabelsadmissiongo88) `:88`

- 🔗 [NewPodTopologyPlugin](#newpodtopologyplugin-pluginpkgadmissionpodtopologylabelsadmissiongo65) `:65`

- 🔗 [Register](#register-pluginpkgadmissionpodtopologylabelsadmissiongo48) `:48`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionpodtopologylabelsadmissiongo93) `:93`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionpodtopologylabelsadmissiongo99) `:99`

- 🔗 [admitBinding](#admitbinding-pluginpkgadmissionpodtopologylabelsadmissiongo127) `:127`

- 🔗 [admitPod](#admitpod-pluginpkgadmissionpodtopologylabelsadmissiongo154) `:154`

- 🔗 [isTopologyLabel](#istopologylabel-pluginpkgadmissionpodtopologylabelsadmissiongo209) `:209`

- 🔗 [mergeLabels](#mergelabels-pluginpkgadmissionpodtopologylabelsadmissiongo203) `:203`

- 🔗 [shouldAdmit](#shouldadmit-pluginpkgadmissionpodtopologylabelsadmissiongo221) `:221`

- 🔗 [topologyLabelsForNodeName](#topologylabelsfornodename-pluginpkgadmissionpodtopologylabelsadmissiongo181) `:181`


</details>


[function] name: Admit file: plugin/pkg/admission/podtopologylabels/admission.go:109 returns_error: да description: —


### Admit (plugin/pkg/admission/podtopologylabels/admission.go:109)


Admit is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) Admit((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:109`



---


[function] name: InspectFeatureGates file: plugin/pkg/admission/podtopologylabels/admission.go:88 returns_error: нет description: InspectFeatureGates implements WantsFeatures.


### InspectFeatureGates (plugin/pkg/admission/podtopologylabels/admission.go:88)


InspectFeatureGates implements WantsFeatures.


```go
func (p *Plugin) InspectFeatureGates((featureGates featuregate.FeatureGate)) (featureGates featuregate.FeatureGate)
```


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** featuregate.FeatureGate


```json
{
  "Name": "string",
  "Stages": [],
  "Dependencies": []
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:88`



---


[function] name: NewPodTopologyPlugin file: plugin/pkg/admission/podtopologylabels/admission.go:65 returns_error: нет description: NewPodTopologyPlugin initializes a Plugin


### NewPodTopologyPlugin (plugin/pkg/admission/podtopologylabels/admission.go:65)


NewPodTopologyPlugin initializes a Plugin


```go
func NewPodTopologyPlugin((c Config)) (c Config)
```


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


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:65`



---


[function] name: Register file: plugin/pkg/admission/podtopologylabels/admission.go:48 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/podtopologylabels/admission.go:48)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:48`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/podtopologylabels/admission.go:93 returns_error: нет description: —


### SetExternalKubeInformerFactory (plugin/pkg/admission/podtopologylabels/admission.go:93)


SetExternalKubeInformerFactory is a method that updates data based on the provided parameters and returns (factory informers.SharedInformerFactory).


```go
func (p *Plugin) SetExternalKubeInformerFactory((factory informers.SharedInformerFactory)) (factory informers.SharedInformerFactory)
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


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:93`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/podtopologylabels/admission.go:99 returns_error: нет description: —


### ValidateInitialization (plugin/pkg/admission/podtopologylabels/admission.go:99)


ValidateInitialization is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:99`



---


[function] name: admitBinding file: plugin/pkg/admission/podtopologylabels/admission.go:127 returns_error: нет description: —


### admitBinding (plugin/pkg/admission/podtopologylabels/admission.go:127)


admitBinding is a method that performs operations based on the provided parameters and returns (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces).


```go
func (p *Plugin) admitBinding((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:127`



---


[function] name: admitPod file: plugin/pkg/admission/podtopologylabels/admission.go:154 returns_error: нет description: —


### admitPod (plugin/pkg/admission/podtopologylabels/admission.go:154)


admitPod is a method that performs operations based on the provided parameters and returns (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces).


```go
func (p *Plugin) admitPod((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:154`



---


[function] name: isTopologyLabel file: plugin/pkg/admission/podtopologylabels/admission.go:209 returns_error: нет description: —


### isTopologyLabel (plugin/pkg/admission/podtopologylabels/admission.go:209)


isTopologyLabel is a method that performs operations based on the provided parameters and returns (key string).


```go
func (p *Plugin) isTopologyLabel((key string)) (key string)
```


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:209`



---


[function] name: mergeLabels file: plugin/pkg/admission/podtopologylabels/admission.go:203 returns_error: нет description: mergeLabels merges new into existing, overwriting existing keys.


### mergeLabels (plugin/pkg/admission/podtopologylabels/admission.go:203)


mergeLabels merges new into existing, overwriting existing keys.


```go
func mergeLabels((existing, new map[string]string)) (existing, new map[string]string)
```


**Тип ответа:** existing


```json
{
  "matchConditionExpressions": {},
  "validationExpressions": {},
  "validationMessageExpressions": {},
  "auditAnnotationValuesExpressions": {},
  "applyConfigurationExpressions": {},
  "jsonPatchExpressions": {}
}
```


*Определено в:* `pkg/apis/admissionregistration/validation/validation.go`


**Тип ответа:** new


```json
{
  "cfgPath": "string",
  "kubeconfigPath": "string",
  "cfg": {}
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:203`



---


[function] name: shouldAdmit file: plugin/pkg/admission/podtopologylabels/admission.go:221 returns_error: да description: shouldAdmit inspects the provided adminssion attributes to determine whether the request
requires admittance through thi


### shouldAdmit (plugin/pkg/admission/podtopologylabels/admission.go:221)


shouldAdmit inspects the provided adminssion attributes to determine whether the request
requires admittance through this plugin.


```go
func (p *Plugin) shouldAdmit((bool, admitFunc, error)) (bool, admitFunc, error)
```


**Тип ответа:** admitFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `admitFunc`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:221`



---


[function] name: topologyLabelsForNodeName file: plugin/pkg/admission/podtopologylabels/admission.go:181 returns_error: да description: —


### topologyLabelsForNodeName (plugin/pkg/admission/podtopologylabels/admission.go:181)


topologyLabelsForNodeName is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) topologyLabelsForNodeName((map[string]string, error)) (map[string]string, error)
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


📍 *Расположение:* `plugin/pkg/admission/podtopologylabels/admission.go:181`




## plugin/pkg/admission/priority/admission.go


📄 Исходный файл: `plugin/pkg/admission/priority/admission.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionpriorityadmissiongo98) `:98`

- 🔗 [NewPlugin](#newplugin-pluginpkgadmissionpriorityadmissiongo62) `:62`

- 🔗 [Register](#register-pluginpkgadmissionpriorityadmissiongo43) `:43`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionpriorityadmissiongo80) `:80`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionpriorityadmissiongo85) `:85`

- 🔗 [Validate](#validate-pluginpkgadmissionpriorityadmissiongo117) `:117`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionpriorityadmissiongo69) `:69`

- 🔗 [admitPod](#admitpod-pluginpkgadmissionpriorityadmissiongo137) `:137`

- 🔗 [getDefaultPriority](#getdefaultpriority-pluginpkgadmissionpriorityadmissiongo246) `:246`

- 🔗 [getDefaultPriorityClass](#getdefaultpriorityclass-pluginpkgadmissionpriorityadmissiongo228) `:228`

- 🔗 [validatePriorityClass](#validatepriorityclass-pluginpkgadmissionpriorityadmissiongo206) `:206`


</details>


[function] name: Admit file: plugin/pkg/admission/priority/admission.go:98 returns_error: нет description: Admit checks Pods and admits or rejects them. It also resolves the priority of pods based on their PriorityClass.
Note t


### Admit (plugin/pkg/admission/priority/admission.go:98)


Admit checks Pods and admits or rejects them. It also resolves the priority of pods based on their PriorityClass.
Note that pod validation mechanism prevents update of a pod priority.


```go
func (p *Plugin) Admit((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:98`



---


[function] name: NewPlugin file: plugin/pkg/admission/priority/admission.go:62 returns_error: нет description: NewPlugin creates a new priority admission plugin.


### NewPlugin (plugin/pkg/admission/priority/admission.go:62)


NewPlugin creates a new priority admission plugin.


```go
func NewPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:62`



---


[function] name: Register file: plugin/pkg/admission/priority/admission.go:43 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/priority/admission.go:43)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:43`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/priority/admission.go:80 returns_error: нет description: SetExternalKubeClientSet implements the WantsInternalKubeClientSet interface.


### SetExternalKubeClientSet (plugin/pkg/admission/priority/admission.go:80)


SetExternalKubeClientSet implements the WantsInternalKubeClientSet interface.


```go
func (p *Plugin) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:80`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/priority/admission.go:85 returns_error: нет description: SetExternalKubeInformerFactory implements the WantsInternalKubeInformerFactory interface.


### SetExternalKubeInformerFactory (plugin/pkg/admission/priority/admission.go:85)


SetExternalKubeInformerFactory implements the WantsInternalKubeInformerFactory interface.


```go
func (p *Plugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:85`



---


[function] name: Validate file: plugin/pkg/admission/priority/admission.go:117 returns_error: нет description: Validate checks PriorityClasses and admits or rejects them.


### Validate (plugin/pkg/admission/priority/admission.go:117)


Validate checks PriorityClasses and admits or rejects them.


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:117`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/priority/admission.go:69 returns_error: нет description: ValidateInitialization implements the InitializationValidator interface.


### ValidateInitialization (plugin/pkg/admission/priority/admission.go:69)


ValidateInitialization implements the InitializationValidator interface.


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:69`



---


[function] name: admitPod file: plugin/pkg/admission/priority/admission.go:137 returns_error: нет description: admitPod makes sure a new pod does not set spec.Priority field. It also makes sure that the PriorityClassName exists if 


### admitPod (plugin/pkg/admission/priority/admission.go:137)


admitPod makes sure a new pod does not set spec.Priority field. It also makes sure that the PriorityClassName exists if it is provided and resolves the pod priority from the PriorityClassName.


```go
func (p *Plugin) admitPod((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:137`



---


[function] name: getDefaultPriority file: plugin/pkg/admission/priority/admission.go:246 returns_error: да description: —


### getDefaultPriority (plugin/pkg/admission/priority/admission.go:246)


getDefaultPriority is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) getDefaultPriority((string, int32, *apiv1.PreemptionPolicy, error)) (string, int32, *apiv1.PreemptionPolicy, error)
```


**Тип запроса:** apiv1.PreemptionPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiv1.PreemptionPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `int32`, `*apiv1.PreemptionPolicy`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:246`



---


[function] name: getDefaultPriorityClass file: plugin/pkg/admission/priority/admission.go:228 returns_error: да description: —


### getDefaultPriorityClass (plugin/pkg/admission/priority/admission.go:228)


getDefaultPriorityClass is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) getDefaultPriorityClass((*schedulingv1.PriorityClass, error)) (*schedulingv1.PriorityClass, error)
```


**Тип запроса:** schedulingv1.PriorityClass


```json
{
  "Value": 0,
  "GlobalDefault": false,
  "Description": "string",
  "PreemptionPolicy": null
}
```


*Определено в:* `pkg/apis/scheduling/types.go`


**Тип ответа:** schedulingv1.PriorityClass


```json
{
  "Value": 0,
  "GlobalDefault": false,
  "Description": "string",
  "PreemptionPolicy": null
}
```


*Определено в:* `pkg/apis/scheduling/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*schedulingv1.PriorityClass`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:228`



---


[function] name: validatePriorityClass file: plugin/pkg/admission/priority/admission.go:206 returns_error: нет description: validatePriorityClass ensures that the value field is not larger than the highest user definable priority. If the Global


### validatePriorityClass (plugin/pkg/admission/priority/admission.go:206)


validatePriorityClass ensures that the value field is not larger than the highest user definable priority. If the GlobalDefault is set, it ensures that there is no other PriorityClass whose GlobalDefault is set.


```go
func (p *Plugin) validatePriorityClass((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/priority/admission.go:206`




## plugin/pkg/admission/runtimeclass/admission.go


📄 Исходный файл: `plugin/pkg/admission/runtimeclass/admission.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionruntimeclassadmissiongo95) `:95`

- 🔗 [NewRuntimeClass](#newruntimeclass-pluginpkgadmissionruntimeclassadmissiongo135) `:135`

- 🔗 [Register](#register-pluginpkgadmissionruntimeclassadmissiongo49) `:49`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionruntimeclassadmissiongo72) `:72`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionruntimeclassadmissiongo77) `:77`

- 🔗 [Validate](#validate-pluginpkgadmissionruntimeclassadmissiongo117) `:117`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionruntimeclassadmissiongo84) `:84`

- 🔗 [prepareObjects](#prepareobjects-pluginpkgadmissionruntimeclassadmissiongo142) `:142`

- 🔗 [setOverhead](#setoverhead-pluginpkgadmissionruntimeclassadmissiongo166) `:166`

- 🔗 [setScheduling](#setscheduling-pluginpkgadmissionruntimeclassadmissiongo187) `:187`

- 🔗 [shouldIgnore](#shouldignore-pluginpkgadmissionruntimeclassadmissiongo239) `:239`

- 🔗 [validateOverhead](#validateoverhead-pluginpkgadmissionruntimeclassadmissiongo219) `:219`


</details>


[function] name: Admit file: plugin/pkg/admission/runtimeclass/admission.go:95 returns_error: нет description: Admit makes an admission decision based on the request attributes


### Admit (plugin/pkg/admission/runtimeclass/admission.go:95)


Admit makes an admission decision based on the request attributes


```go
func (r *RuntimeClass) Admit((ctx context.Context, attributes admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, attributes admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:95`



---


[function] name: NewRuntimeClass file: plugin/pkg/admission/runtimeclass/admission.go:135 returns_error: нет description: NewRuntimeClass creates a new RuntimeClass admission control handler


### NewRuntimeClass (plugin/pkg/admission/runtimeclass/admission.go:135)


NewRuntimeClass creates a new RuntimeClass admission control handler


```go
func NewRuntimeClass(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:135`



---


[function] name: Register file: plugin/pkg/admission/runtimeclass/admission.go:49 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/runtimeclass/admission.go:49)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:49`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/runtimeclass/admission.go:72 returns_error: нет description: SetExternalKubeClientSet sets the client for the plugin


### SetExternalKubeClientSet (plugin/pkg/admission/runtimeclass/admission.go:72)


SetExternalKubeClientSet sets the client for the plugin


```go
func (r *RuntimeClass) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:72`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/runtimeclass/admission.go:77 returns_error: нет description: SetExternalKubeInformerFactory implements the WantsExternalKubeInformerFactory interface.


### SetExternalKubeInformerFactory (plugin/pkg/admission/runtimeclass/admission.go:77)


SetExternalKubeInformerFactory implements the WantsExternalKubeInformerFactory interface.


```go
func (r *RuntimeClass) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:77`



---


[function] name: Validate file: plugin/pkg/admission/runtimeclass/admission.go:117 returns_error: нет description: Validate makes sure that pod adhere's to RuntimeClass's definition


### Validate (plugin/pkg/admission/runtimeclass/admission.go:117)


Validate makes sure that pod adhere's to RuntimeClass's definition


```go
func (r *RuntimeClass) Validate((ctx context.Context, attributes admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, attributes admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:117`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/runtimeclass/admission.go:84 returns_error: нет description: ValidateInitialization implements the WantsExternalKubeInformerFactory interface.


### ValidateInitialization (plugin/pkg/admission/runtimeclass/admission.go:84)


ValidateInitialization implements the WantsExternalKubeInformerFactory interface.


```go
func (r *RuntimeClass) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:84`



---


[function] name: prepareObjects file: plugin/pkg/admission/runtimeclass/admission.go:142 returns_error: да description: prepareObjects returns pod and runtimeClass types from the given admission attributes


### prepareObjects (plugin/pkg/admission/runtimeclass/admission.go:142)


prepareObjects returns pod and runtimeClass types from the given admission attributes


```go
func (r *RuntimeClass) prepareObjects((pod *api.Pod, runtimeClass *nodev1.RuntimeClass, err error)) (pod *api.Pod, runtimeClass *nodev1.RuntimeClass, err error)
```


**Тип запроса:** api.Pod


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


**Тип запроса:** nodev1.RuntimeClass


```json
{
  "Handler": "string",
  "Overhead": null,
  "Scheduling": null
}
```


*Определено в:* `pkg/apis/node/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


**Тип ответа:** runtimeClass


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/node/v1alpha1/runtimeclass.go`


**Тип ответа:** nodev1.RuntimeClass


```json
{
  "Handler": "string",
  "Overhead": null,
  "Scheduling": null
}
```


*Определено в:* `pkg/apis/node/types.go`


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


*Типы возврата:* `pod *api.Pod`, `runtimeClass *nodev1.RuntimeClass`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:142`



---


[function] name: setOverhead file: plugin/pkg/admission/runtimeclass/admission.go:166 returns_error: да description: —


### setOverhead (plugin/pkg/admission/runtimeclass/admission.go:166)


setOverhead is a function that performs operations based on the provided parameters and may return an error.


```go
func setOverhead((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:166`



---


[function] name: setScheduling file: plugin/pkg/admission/runtimeclass/admission.go:187 returns_error: да description: —


### setScheduling (plugin/pkg/admission/runtimeclass/admission.go:187)


setScheduling is a function that performs operations based on the provided parameters and may return an error.


```go
func setScheduling((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:187`



---


[function] name: shouldIgnore file: plugin/pkg/admission/runtimeclass/admission.go:239 returns_error: нет description: —


### shouldIgnore (plugin/pkg/admission/runtimeclass/admission.go:239)


shouldIgnore is a function that performs operations based on the provided parameters and returns (attributes admission.Attributes).


```go
func shouldIgnore((attributes admission.Attributes)) (attributes admission.Attributes)
```


**Тип ответа:** attributes


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:239`



---


[function] name: validateOverhead file: plugin/pkg/admission/runtimeclass/admission.go:219 returns_error: да description: —


### validateOverhead (plugin/pkg/admission/runtimeclass/admission.go:219)


validateOverhead is a function that performs operations based on the provided parameters and may return an error.


```go
func validateOverhead((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/runtimeclass/admission.go:219`




## plugin/pkg/admission/security/podsecurity/admission.go


📄 Исходный файл: `plugin/pkg/admission/security/podsecurity/admission.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [GetObject](#getobject-pluginpkgadmissionsecuritypodsecurityadmissiongo247) `:247`

- 🔗 [GetOldObject](#getoldobject-pluginpkgadmissionsecuritypodsecurityadmissiongo254) `:254`

- 🔗 [GetOperation](#getoperation-pluginpkgadmissionsecuritypodsecurityadmissiongo261) `:261`

- 🔗 [GetUserName](#getusername-pluginpkgadmissionsecuritypodsecurityadmissiongo265) `:265`

- 🔗 [InspectEffectiveVersion](#inspecteffectiveversion-pluginpkgadmissionsecuritypodsecurityadmissiongo161) `:161`

- 🔗 [Register](#register-pluginpkgadmissionsecuritypodsecurityadmissiongo62) `:62`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionsecuritypodsecurityadmissiongo127) `:127`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionsecuritypodsecurityadmissiongo118) `:118`

- 🔗 [Validate](#validate-pluginpkgadmissionsecuritypodsecurityadmissiongo193) `:193`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionsecuritypodsecurityadmissiongo173) `:173`

- 🔗 [convert](#convert-pluginpkgadmissionsecuritypodsecurityadmissiongo269) `:269`

- 🔗 [getDefaultRecorder](#getdefaultrecorder-pluginpkgadmissionsecuritypodsecurityadmissiongo91) `:91`

- 🔗 [newPlugin](#newplugin-pluginpkgadmissionsecuritypodsecurityadmissiongo101) `:101`

- 🔗 [updateDelegate](#updatedelegate-pluginpkgadmissionsecuritypodsecurityadmissiongo132) `:132`


</details>


[function] name: GetObject file: plugin/pkg/admission/security/podsecurity/admission.go:247 returns_error: да description: —


### GetObject (plugin/pkg/admission/security/podsecurity/admission.go:247)


GetObject is a method that retrieves data based on the provided parameters and may return an error.


```go
func (l *lazyConvertingAttributes) GetObject((runtime.Object, error)) (runtime.Object, error)
```


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `runtime.Object`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:247`



---


[function] name: GetOldObject file: plugin/pkg/admission/security/podsecurity/admission.go:254 returns_error: да description: —


### GetOldObject (plugin/pkg/admission/security/podsecurity/admission.go:254)


GetOldObject is a method that retrieves data based on the provided parameters and may return an error.


```go
func (l *lazyConvertingAttributes) GetOldObject((runtime.Object, error)) (runtime.Object, error)
```


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `runtime.Object`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:254`



---


[function] name: GetOperation file: plugin/pkg/admission/security/podsecurity/admission.go:261 returns_error: нет description: —


### GetOperation (plugin/pkg/admission/security/podsecurity/admission.go:261)


GetOperation is a method that retrieves data based on the provided parameters and returns ().


```go
func (l *lazyConvertingAttributes) GetOperation(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:261`



---


[function] name: GetUserName file: plugin/pkg/admission/security/podsecurity/admission.go:265 returns_error: нет description: —


### GetUserName (plugin/pkg/admission/security/podsecurity/admission.go:265)


GetUserName is a method that retrieves data based on the provided parameters and returns ().


```go
func (l *lazyConvertingAttributes) GetUserName(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:265`



---


[function] name: InspectEffectiveVersion file: plugin/pkg/admission/security/podsecurity/admission.go:161 returns_error: нет description: —


### InspectEffectiveVersion (plugin/pkg/admission/security/podsecurity/admission.go:161)


InspectEffectiveVersion is a method that performs operations based on the provided parameters and returns (version compatibility.EffectiveVersion).


```go
func (p *Plugin) InspectEffectiveVersion((version compatibility.EffectiveVersion)) (version compatibility.EffectiveVersion)
```


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


**Тип ответа:** compatibility.EffectiveVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:161`



---


[function] name: Register file: plugin/pkg/admission/security/podsecurity/admission.go:62 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/security/podsecurity/admission.go:62)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:62`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/security/podsecurity/admission.go:127 returns_error: нет description: SetExternalKubeClientSet sets the plugin's client


### SetExternalKubeClientSet (plugin/pkg/admission/security/podsecurity/admission.go:127)


SetExternalKubeClientSet sets the plugin's client


```go
func (p *Plugin) SetExternalKubeClientSet((client kubernetes.Interface)) (client kubernetes.Interface)
```


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


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:127`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/security/podsecurity/admission.go:118 returns_error: нет description: SetExternalKubeInformerFactory registers an informer


### SetExternalKubeInformerFactory (plugin/pkg/admission/security/podsecurity/admission.go:118)


SetExternalKubeInformerFactory registers an informer


```go
func (p *Plugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:118`



---


[function] name: Validate file: plugin/pkg/admission/security/podsecurity/admission.go:193 returns_error: нет description: —


### Validate (plugin/pkg/admission/security/podsecurity/admission.go:193)


Validate is a method that performs operations based on the provided parameters and returns (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces).


```go
func (p *Plugin) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:193`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/security/podsecurity/admission.go:173 returns_error: нет description: ValidateInitialization ensures all required options are set


### ValidateInitialization (plugin/pkg/admission/security/podsecurity/admission.go:173)


ValidateInitialization ensures all required options are set


```go
func (p *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:173`



---


[function] name: convert file: plugin/pkg/admission/security/podsecurity/admission.go:269 returns_error: да description: —


### convert (plugin/pkg/admission/security/podsecurity/admission.go:269)


convert is a function that performs operations based on the provided parameters and may return an error.


```go
func convert((runtime.Object, error)) (runtime.Object, error)
```


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `runtime.Object`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:269`



---


[function] name: getDefaultRecorder file: plugin/pkg/admission/security/podsecurity/admission.go:91 returns_error: нет description: —


### getDefaultRecorder (plugin/pkg/admission/security/podsecurity/admission.go:91)


getDefaultRecorder is a function that performs operations based on the provided parameters and returns ().


```go
func getDefaultRecorder(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:91`



---


[function] name: newPlugin file: plugin/pkg/admission/security/podsecurity/admission.go:101 returns_error: да description: newPlugin creates a new admission plugin.


### newPlugin (plugin/pkg/admission/security/podsecurity/admission.go:101)


newPlugin creates a new admission plugin.


```go
func newPlugin((*Plugin, error)) (*Plugin, error)
```


**Тип запроса:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип ответа:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Plugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:101`



---


[function] name: updateDelegate file: plugin/pkg/admission/security/podsecurity/admission.go:132 returns_error: нет description: —


### updateDelegate (plugin/pkg/admission/security/podsecurity/admission.go:132)


updateDelegate is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Plugin) updateDelegate(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/security/podsecurity/admission.go:132`




## plugin/pkg/admission/serviceaccount/admission.go


📄 Исходный файл: `plugin/pkg/admission/serviceaccount/admission.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionserviceaccountadmissiongo138) `:138`

- 🔗 [NewServiceAccount](#newserviceaccount-pluginpkgadmissionserviceaccountadmissiongo100) `:100`

- 🔗 [Register](#register-pluginpkgadmissionserviceaccountadmissiongo64) `:64`

- 🔗 [SetExternalKubeClientSet](#setexternalkubeclientset-pluginpkgadmissionserviceaccountadmissiongo113) `:113`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionserviceaccountadmissiongo118) `:118`

- 🔗 [TokenVolumeSource](#tokenvolumesource-pluginpkgadmissionserviceaccountadmissiongo485) `:485`

- 🔗 [Validate](#validate-pluginpkgadmissionserviceaccountadmissiongo178) `:178`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionserviceaccountadmissiongo127) `:127`

- 🔗 [enforceMountableSecrets](#enforcemountablesecrets-pluginpkgadmissionserviceaccountadmissiongo269) `:269`

- 🔗 [getServiceAccount](#getserviceaccount-pluginpkgadmissionserviceaccountadmissiongo283) `:283`

- 🔗 [limitEphemeralContainerSecretReferences](#limitephemeralcontainersecretreferences-pluginpkgadmissionserviceaccountadmissiongo379) `:379`

- 🔗 [limitSecretReferences](#limitsecretreferences-pluginpkgadmissionserviceaccountadmissiongo315) `:315`

- 🔗 [mountServiceAccountToken](#mountserviceaccounttoken-pluginpkgadmissionserviceaccountadmissiongo416) `:416`

- 🔗 [shouldAutomount](#shouldautomount-pluginpkgadmissionserviceaccountadmissiongo254) `:254`

- 🔗 [shouldIgnore](#shouldignore-pluginpkgadmissionserviceaccountadmissiongo238) `:238`


</details>


[function] name: Admit file: plugin/pkg/admission/serviceaccount/admission.go:138 returns_error: да description: Admit verifies if the pod should be admitted


### Admit (plugin/pkg/admission/serviceaccount/admission.go:138)


Admit verifies if the pod should be admitted


```go
func (s *Plugin) Admit((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:138`



---


[function] name: NewServiceAccount file: plugin/pkg/admission/serviceaccount/admission.go:100 returns_error: нет description: NewServiceAccount returns an admission.Interface implementation which limits admission of Pod CREATE requests based on t


### NewServiceAccount (plugin/pkg/admission/serviceaccount/admission.go:100)


NewServiceAccount returns an admission.Interface implementation which limits admission of Pod CREATE requests based on the pod's ServiceAccount:
1. If the pod does not specify a ServiceAccount, it sets the pod's ServiceAccount to "default"
2. It ensures the ServiceAccount referenced by the pod exists
3. If LimitSecretReferences is true, it rejects the pod if the pod references Secret objects which the pod's ServiceAccount does not reference
4. If the pod does not contain any ImagePullSecrets, the ImagePullSecrets of the service account are added.
5. If MountServiceAccountToken is true, it adds a VolumeMount with the pod's ServiceAccount's api token secret to containers


```go
func NewServiceAccount(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:100`



---


[function] name: Register file: plugin/pkg/admission/serviceaccount/admission.go:64 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/serviceaccount/admission.go:64)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:64`



---


[function] name: SetExternalKubeClientSet file: plugin/pkg/admission/serviceaccount/admission.go:113 returns_error: нет description: SetExternalKubeClientSet sets the client for the plugin


### SetExternalKubeClientSet (plugin/pkg/admission/serviceaccount/admission.go:113)


SetExternalKubeClientSet sets the client for the plugin


```go
func (s *Plugin) SetExternalKubeClientSet((cl kubernetes.Interface)) (cl kubernetes.Interface)
```


**Тип ответа:** cl


```json
{
  "CAKey": {},
  "Organizations": []
}
```


*Определено в:* `cmd/kubeadm/app/phases/kubeconfig/kubeconfig.go`


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:113`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/serviceaccount/admission.go:118 returns_error: нет description: SetExternalKubeInformerFactory registers informers with the plugin


### SetExternalKubeInformerFactory (plugin/pkg/admission/serviceaccount/admission.go:118)


SetExternalKubeInformerFactory registers informers with the plugin


```go
func (s *Plugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:118`



---


[function] name: TokenVolumeSource file: plugin/pkg/admission/serviceaccount/admission.go:485 returns_error: нет description: TokenVolumeSource returns the projected volume source for service account token.


### TokenVolumeSource (plugin/pkg/admission/serviceaccount/admission.go:485)


TokenVolumeSource returns the projected volume source for service account token.


```go
func TokenVolumeSource(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:485`



---


[function] name: Validate file: plugin/pkg/admission/serviceaccount/admission.go:178 returns_error: да description: Validate the data we obtained


### Validate (plugin/pkg/admission/serviceaccount/admission.go:178)


Validate the data we obtained


```go
func (s *Plugin) Validate((err error)) (err error)
```


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


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:178`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/serviceaccount/admission.go:127 returns_error: нет description: ValidateInitialization ensures an authorizer is set.


### ValidateInitialization (plugin/pkg/admission/serviceaccount/admission.go:127)


ValidateInitialization ensures an authorizer is set.


```go
func (s *Plugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:127`



---


[function] name: enforceMountableSecrets file: plugin/pkg/admission/serviceaccount/admission.go:269 returns_error: нет description: enforceMountableSecrets indicates whether mountable secrets should be enforced for a particular service account
A global


### enforceMountableSecrets (plugin/pkg/admission/serviceaccount/admission.go:269)


enforceMountableSecrets indicates whether mountable secrets should be enforced for a particular service account
A global setting of true will override any flag set on the individual service account


```go
func (s *Plugin) enforceMountableSecrets((serviceAccount *corev1.ServiceAccount)) (serviceAccount *corev1.ServiceAccount)
```


**Тип запроса:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** serviceAccount


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:269`



---


[function] name: getServiceAccount file: plugin/pkg/admission/serviceaccount/admission.go:283 returns_error: да description: getServiceAccount returns the ServiceAccount for the given namespace and name if it exists


### getServiceAccount (plugin/pkg/admission/serviceaccount/admission.go:283)


getServiceAccount returns the ServiceAccount for the given namespace and name if it exists


```go
func (s *Plugin) getServiceAccount((*corev1.ServiceAccount, error)) (*corev1.ServiceAccount, error)
```


**Тип запроса:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.ServiceAccount`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:283`



---


[function] name: limitEphemeralContainerSecretReferences file: plugin/pkg/admission/serviceaccount/admission.go:379 returns_error: нет description: —


### limitEphemeralContainerSecretReferences (plugin/pkg/admission/serviceaccount/admission.go:379)


limitEphemeralContainerSecretReferences is a method that performs operations based on the provided parameters and returns (pod *api.Pod, a admission.Attributes).


```go
func (s *Plugin) limitEphemeralContainerSecretReferences((pod *api.Pod, a admission.Attributes)) (pod *api.Pod, a admission.Attributes)
```


**Тип запроса:** api.Pod


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:379`



---


[function] name: limitSecretReferences file: plugin/pkg/admission/serviceaccount/admission.go:315 returns_error: нет description: —


### limitSecretReferences (plugin/pkg/admission/serviceaccount/admission.go:315)


limitSecretReferences is a method that performs operations based on the provided parameters and returns (serviceAccount *corev1.ServiceAccount, pod *api.Pod).


```go
func (s *Plugin) limitSecretReferences((serviceAccount *corev1.ServiceAccount, pod *api.Pod)) (serviceAccount *corev1.ServiceAccount, pod *api.Pod)
```


**Тип запроса:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.Pod


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


**Тип ответа:** serviceAccount


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:315`



---


[function] name: mountServiceAccountToken file: plugin/pkg/admission/serviceaccount/admission.go:416 returns_error: нет description: —


### mountServiceAccountToken (plugin/pkg/admission/serviceaccount/admission.go:416)


mountServiceAccountToken is a method that performs operations based on the provided parameters and returns (serviceAccount *corev1.ServiceAccount, pod *api.Pod).


```go
func (s *Plugin) mountServiceAccountToken((serviceAccount *corev1.ServiceAccount, pod *api.Pod)) (serviceAccount *corev1.ServiceAccount, pod *api.Pod)
```


**Тип запроса:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.Pod


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


**Тип ответа:** serviceAccount


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:416`



---


[function] name: shouldAutomount file: plugin/pkg/admission/serviceaccount/admission.go:254 returns_error: нет description: —


### shouldAutomount (plugin/pkg/admission/serviceaccount/admission.go:254)


shouldAutomount is a function that performs operations based on the provided parameters and returns (sa *corev1.ServiceAccount, pod *api.Pod).


```go
func shouldAutomount((sa *corev1.ServiceAccount, pod *api.Pod)) (sa *corev1.ServiceAccount, pod *api.Pod)
```


**Тип запроса:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.Pod


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


**Тип ответа:** sa


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** corev1.ServiceAccount


```json
{
  "Secrets": [],
  "ImagePullSecrets": [],
  "AutomountServiceAccountToken": false
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** api.Pod


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


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:254`



---


[function] name: shouldIgnore file: plugin/pkg/admission/serviceaccount/admission.go:238 returns_error: нет description: —


### shouldIgnore (plugin/pkg/admission/serviceaccount/admission.go:238)


shouldIgnore is a function that performs operations based on the provided parameters and returns (a admission.Attributes).


```go
func shouldIgnore((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/serviceaccount/admission.go:238`




## plugin/pkg/admission/storage/persistentvolume/resize/admission.go


📄 Исходный файл: `plugin/pkg/admission/storage/persistentvolume/resize/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Register](#register-pluginpkgadmissionstoragepersistentvolumeresizeadmissiongo38) `:38`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionstoragepersistentvolumeresizeadmissiongo61) `:61`

- 🔗 [Validate](#validate-pluginpkgadmissionstoragepersistentvolumeresizeadmissiongo75) `:75`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionstoragepersistentvolumeresizeadmissiongo68) `:68`

- 🔗 [allowResize](#allowresize-pluginpkgadmissionstoragepersistentvolumeresizeadmissiongo117) `:117`

- 🔗 [newPlugin](#newplugin-pluginpkgadmissionstoragepersistentvolumeresizeadmissiongo55) `:55`


</details>


[function] name: Register file: plugin/pkg/admission/storage/persistentvolume/resize/admission.go:38 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/storage/persistentvolume/resize/admission.go:38)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/storage/persistentvolume/resize/admission.go:38`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/storage/persistentvolume/resize/admission.go:61 returns_error: нет description: —


### SetExternalKubeInformerFactory (plugin/pkg/admission/storage/persistentvolume/resize/admission.go:61)


SetExternalKubeInformerFactory is a method that updates data based on the provided parameters and returns (f informers.SharedInformerFactory).


```go
func (pvcr *persistentVolumeClaimResize) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/storage/persistentvolume/resize/admission.go:61`



---


[function] name: Validate file: plugin/pkg/admission/storage/persistentvolume/resize/admission.go:75 returns_error: нет description: —


### Validate (plugin/pkg/admission/storage/persistentvolume/resize/admission.go:75)


Validate is a method that performs operations based on the provided parameters and returns (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces).


```go
func (pvcr *persistentVolumeClaimResize) Validate((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/storage/persistentvolume/resize/admission.go:75`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/storage/persistentvolume/resize/admission.go:68 returns_error: нет description: ValidateInitialization ensures lister is set.


### ValidateInitialization (plugin/pkg/admission/storage/persistentvolume/resize/admission.go:68)


ValidateInitialization ensures lister is set.


```go
func (pvcr *persistentVolumeClaimResize) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/storage/persistentvolume/resize/admission.go:68`



---


[function] name: allowResize file: plugin/pkg/admission/storage/persistentvolume/resize/admission.go:117 returns_error: нет description: Growing Persistent volumes is only allowed for PVCs for which their StorageClass
explicitly allows it.


### allowResize (plugin/pkg/admission/storage/persistentvolume/resize/admission.go:117)


Growing Persistent volumes is only allowed for PVCs for which their StorageClass
explicitly allows it.


```go
func (pvcr *persistentVolumeClaimResize) allowResize((pvc, oldPvc *api.PersistentVolumeClaim)) (pvc, oldPvc *api.PersistentVolumeClaim)
```


**Тип запроса:** api.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvc


```json
{
  "tsInfo": {}
}
```


*Определено в:* `test/e2e/storage/testsuites/pvcdeletionperf.go`


**Тип ответа:** oldPvc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/admission/storage/persistentvolume/resize/admission.go:117`



---


[function] name: newPlugin file: plugin/pkg/admission/storage/persistentvolume/resize/admission.go:55 returns_error: нет description: —


### newPlugin (plugin/pkg/admission/storage/persistentvolume/resize/admission.go:55)


newPlugin is a function that performs operations based on the provided parameters and returns ().


```go
func newPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/storage/persistentvolume/resize/admission.go:55`




## plugin/pkg/admission/storage/storageclass/setdefault/admission.go


📄 Исходный файл: `plugin/pkg/admission/storage/storageclass/setdefault/admission.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionstoragestorageclasssetdefaultadmissiongo86) `:86`

- 🔗 [Register](#register-pluginpkgadmissionstoragestorageclasssetdefaultadmissiongo41) `:41`

- 🔗 [SetExternalKubeInformerFactory](#setexternalkubeinformerfactory-pluginpkgadmissionstoragestorageclasssetdefaultadmissiongo66) `:66`

- 🔗 [ValidateInitialization](#validateinitialization-pluginpkgadmissionstoragestorageclasssetdefaultadmissiongo73) `:73`

- 🔗 [newPlugin](#newplugin-pluginpkgadmissionstoragestorageclasssetdefaultadmissiongo60) `:60`


</details>


[function] name: Admit file: plugin/pkg/admission/storage/storageclass/setdefault/admission.go:86 returns_error: нет description: Admit sets the default value of a PersistentVolumeClaim's storage class, in case the user did
not provide a value.

1.  


### Admit (plugin/pkg/admission/storage/storageclass/setdefault/admission.go:86)


Admit sets the default value of a PersistentVolumeClaim's storage class, in case the user did
not provide a value.

1.  Find available StorageClasses.
2.  Figure which is the default
3.  Write to the PVClaim


```go
func (a *claimDefaulterPlugin) Admit((ctx context.Context, attr admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, attr admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** attr


```json
{
  "r": null,
  "decoder": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/api/attributes.go`


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/storage/storageclass/setdefault/admission.go:86`



---


[function] name: Register file: plugin/pkg/admission/storage/storageclass/setdefault/admission.go:41 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/storage/storageclass/setdefault/admission.go:41)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/storage/storageclass/setdefault/admission.go:41`



---


[function] name: SetExternalKubeInformerFactory file: plugin/pkg/admission/storage/storageclass/setdefault/admission.go:66 returns_error: нет description: —


### SetExternalKubeInformerFactory (plugin/pkg/admission/storage/storageclass/setdefault/admission.go:66)


SetExternalKubeInformerFactory is a method that updates data based on the provided parameters and returns (f informers.SharedInformerFactory).


```go
func (a *claimDefaulterPlugin) SetExternalKubeInformerFactory((f informers.SharedInformerFactory)) (f informers.SharedInformerFactory)
```


**Тип ответа:** f


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


📍 *Расположение:* `plugin/pkg/admission/storage/storageclass/setdefault/admission.go:66`



---


[function] name: ValidateInitialization file: plugin/pkg/admission/storage/storageclass/setdefault/admission.go:73 returns_error: нет description: ValidateInitialization ensures lister is set.


### ValidateInitialization (plugin/pkg/admission/storage/storageclass/setdefault/admission.go:73)


ValidateInitialization ensures lister is set.


```go
func (a *claimDefaulterPlugin) ValidateInitialization(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/storage/storageclass/setdefault/admission.go:73`



---


[function] name: newPlugin file: plugin/pkg/admission/storage/storageclass/setdefault/admission.go:60 returns_error: нет description: newPlugin creates a new admission plugin.


### newPlugin (plugin/pkg/admission/storage/storageclass/setdefault/admission.go:60)


newPlugin creates a new admission plugin.


```go
func newPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/storage/storageclass/setdefault/admission.go:60`




## plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go


📄 Исходный файл: `plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Admit](#admit-pluginpkgadmissionstoragestorageobjectinuseprotectionadmissiongo70) `:70`

- 🔗 [Register](#register-pluginpkgadmissionstoragestorageobjectinuseprotectionadmissiongo38) `:38`

- 🔗 [admitPV](#admitpv-pluginpkgadmissionstoragestorageobjectinuseprotectionadmissiongo87) `:87`

- 🔗 [admitPVC](#admitpvc-pluginpkgadmissionstoragestorageobjectinuseprotectionadmissiongo109) `:109`

- 🔗 [admitVAC](#admitvac-pluginpkgadmissionstoragestorageobjectinuseprotectionadmissiongo132) `:132`

- 🔗 [newPlugin](#newplugin-pluginpkgadmissionstoragestorageobjectinuseprotectionadmissiongo53) `:53`


</details>


[function] name: Admit file: plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:70 returns_error: нет description: Admit sets finalizer on all PVCs(PVs). The finalizer is removed by
PVCProtectionController(PVProtectionController) when 


### Admit (plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:70)


Admit sets finalizer on all PVCs(PVs). The finalizer is removed by
PVCProtectionController(PVProtectionController) when it's not referenced.

This prevents users from deleting a PVC that's used by a running pod.
This also prevents admin from deleting a PV that's bound by a PVC


```go
func (c *storageProtectionPlugin) Admit((ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)) (ctx context.Context, a admission.Attributes, o admission.ObjectInterfaces)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** o


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


**Тип ответа:** admission.ObjectInterfaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:70`



---


[function] name: Register file: plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:38 returns_error: нет description: Register registers a plugin


### Register (plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:38)


Register registers a plugin


```go
func Register((plugins *admission.Plugins)) (plugins *admission.Plugins)
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


📍 *Расположение:* `plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:38`



---


[function] name: admitPV file: plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:87 returns_error: нет description: —


### admitPV (plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:87)


admitPV is a method that performs operations based on the provided parameters and returns (a admission.Attributes).


```go
func (c *storageProtectionPlugin) admitPV((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:87`



---


[function] name: admitPVC file: plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:109 returns_error: нет description: —


### admitPVC (plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:109)


admitPVC is a method that performs operations based on the provided parameters and returns (a admission.Attributes).


```go
func (c *storageProtectionPlugin) admitPVC((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:109`



---


[function] name: admitVAC file: plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:132 returns_error: нет description: —


### admitVAC (plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:132)


admitVAC is a method that performs operations based on the provided parameters and returns (a admission.Attributes).


```go
func (c *storageProtectionPlugin) admitVAC((a admission.Attributes)) (a admission.Attributes)
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


**Тип ответа:** admission.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


📍 *Расположение:* `plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:132`



---


[function] name: newPlugin file: plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:53 returns_error: нет description: newPlugin creates a new admission plugin.


### newPlugin (plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:53)


newPlugin creates a new admission plugin.


```go
func newPlugin(()) ()
```


📍 *Расположение:* `plugin/pkg/admission/storage/storageobjectinuseprotection/admission.go:53`




## plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go


📄 Исходный файл: `plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AuthenticateToken](#authenticatetoken-pluginpkgauthauthenticatortokenbootstrapbootstrapgo90) `:90`

- 🔗 [NewTokenAuthenticator](#newtokenauthenticator-pluginpkgauthauthenticatortokenbootstrapbootstrapgo47) `:47`

- 🔗 [tokenErrorf](#tokenerrorf-pluginpkgauthauthenticatortokenbootstrapbootstrapgo60) `:60`


</details>


[function] name: AuthenticateToken file: plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:90 returns_error: да description: AuthenticateToken tries to match the provided token to a bootstrap token secret
in a given namespace. If found, it authe


### AuthenticateToken (plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:90)


AuthenticateToken tries to match the provided token to a bootstrap token secret
in a given namespace. If found, it authenticates the token in the
"system:bootstrappers" group and with the "system:bootstrap:(token-id)" username.

All secrets must be of type "bootstrap.kubernetes.io/token". An example secret:

apiVersion: v1
kind: Secret
metadata:
# Name MUST be of form "bootstrap-token-( token id )".
name: bootstrap-token-( token id )
namespace: kube-system
# Only secrets of this type will be evaluated.
type: bootstrap.kubernetes.io/token
data:
token-secret: ( private part of token )
token-id: ( token id )
# Required key usage.
usage-bootstrap-authentication: true
auth-extra-groups: "system:bootstrappers:custom-group1,system:bootstrappers:custom-group2"
# May also contain an expiry.

Tokens are expected to be of the form:

( token-id ).( token-secret )


```go
func (t *TokenAuthenticator) AuthenticateToken((*authenticator.Response, bool, error)) (*authenticator.Response, bool, error)
```


**Тип запроса:** authenticator.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Тип ответа:** authenticator.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*authenticator.Response`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:90`



---


[function] name: NewTokenAuthenticator file: plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:47 returns_error: нет description: NewTokenAuthenticator initializes a bootstrap token authenticator.

Lister is expected to be for the "kube-system" names


### NewTokenAuthenticator (plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:47)


NewTokenAuthenticator initializes a bootstrap token authenticator.

Lister is expected to be for the "kube-system" namespace.


```go
func NewTokenAuthenticator((lister corev1listers.SecretNamespaceLister)) (lister corev1listers.SecretNamespaceLister)
```


**Тип ответа:** lister


```json
{
  "indexer": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/internal/generic/lister.go`


**Тип ответа:** corev1listers.SecretNamespaceLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:47`



---


[function] name: tokenErrorf file: plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:60 returns_error: нет description: tokenErrorf prints a error message for a secret that has matched a bearer
token but fails to meet some other criteria.




### tokenErrorf (plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:60)


tokenErrorf prints a error message for a secret that has matched a bearer
token but fails to meet some other criteria.

tokenErrorf(secret, "has invalid value for key %s", key)


```go
func tokenErrorf((s *corev1.Secret, format string, i ...interface{})) (s *corev1.Secret, format string, i ...interface{})
```


**Тип запроса:** corev1.Secret


```json
{
  "Immutable": false,
  "Data": {},
  "Type": {}
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


**Тип ответа:** corev1.Secret


```json
{
  "Immutable": false,
  "Data": {},
  "Type": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** format


```json
{
  "availableOnNodes": null,
  "allocation": null
}
```


*Определено в:* `pkg/scheduler/framework/plugins/dynamicresources/dynamicresources.go`


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `plugin/pkg/auth/authenticator/token/bootstrap/bootstrap.go:60`




## plugin/pkg/auth/authorizer/node/graph.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/node/graph.go`


<details open>
<summary><b>Функции в этом файле (29)</b></summary>


- 🔗 [AddPV](#addpv-pluginpkgauthauthorizernodegraphgo512) `:512`

- 🔗 [AddPod](#addpod-pluginpkgauthauthorizernodegraphgo360) `:360`

- 🔗 [AddPodCertificateRequest](#addpodcertificaterequest-pluginpkgauthauthorizernodegraphgo482) `:482`

- 🔗 [AddResourceSlice](#addresourceslice-pluginpkgauthauthorizernodegraphgo585) `:585`

- 🔗 [AddVolumeAttachment](#addvolumeattachment-pluginpkgauthauthorizernodegraphgo553) `:553`

- 🔗 [DeletePV](#deletepv-pluginpkgauthauthorizernodegraphgo540) `:540`

- 🔗 [DeletePod](#deletepod-pluginpkgauthauthorizernodegraphgo460) `:460`

- 🔗 [DeletePodCertificateRequest](#deletepodcertificaterequest-pluginpkgauthauthorizernodegraphgo497) `:497`

- 🔗 [DeleteResourceSlice](#deleteresourceslice-pluginpkgauthauthorizernodegraphgo604) `:604`

- 🔗 [DeleteVolumeAttachment](#deletevolumeattachment-pluginpkgauthauthorizernodegraphgo572) `:572`

- 🔗 [DestinationID](#destinationid-pluginpkgauthauthorizernodegraphgo74) `:74`

- 🔗 [From](#from-pluginpkgauthauthorizernodegraphgo71) `:71`

- 🔗 [ID](#id-pluginpkgauthauthorizernodegraphgo50) `:50`

- 🔗 [NewGraph](#newgraph-pluginpkgauthauthorizernodegraphgo102) `:102`

- 🔗 [String](#string-pluginpkgauthauthorizernodegraphgo53) `:53`

- 🔗 [To](#to-pluginpkgauthauthorizernodegraphgo72) `:72`

- 🔗 [Weight](#weight-pluginpkgauthauthorizernodegraphgo73) `:73`

- 🔗 [addEdgeLocked](#addedgelocked-pluginpkgauthauthorizernodegraphgo443) `:443`

- 🔗 [addEdgeToDestinationIndexLocked](#addedgetodestinationindexlocked-pluginpkgauthauthorizernodegraphgo298) `:298`

- 🔗 [createVertexLocked](#createvertexlocked-pluginpkgauthauthorizernodegraphgo176) `:176`

- 🔗 [deleteEdgesLocked](#deleteedgeslocked-pluginpkgauthauthorizernodegraphgo241) `:241`

- 🔗 [deleteVertexLocked](#deletevertexlocked-pluginpkgauthauthorizernodegraphgo197) `:197`

- 🔗 [getOrCreateVertexLocked](#getorcreatevertexlocked-pluginpkgauthauthorizernodegraphgo162) `:162`

- 🔗 [getVertexRLocked](#getvertexrlocked-pluginpkgauthauthorizernodegraphgo170) `:170`

- 🔗 [newDestinationEdge](#newdestinationedge-pluginpkgauthauthorizernodegraphgo68) `:68`

- 🔗 [newNamedVertex](#newnamedvertex-pluginpkgauthauthorizernodegraphgo42) `:42`

- 🔗 [recomputeDestinationIndexLocked](#recomputedestinationindexlocked-pluginpkgauthauthorizernodegraphgo326) `:326`

- 🔗 [removeEdgeFromDestinationIndexLocked](#removeedgefromdestinationindexlocked-pluginpkgauthauthorizernodegraphgo278) `:278`

- 🔗 [removeVertexLocked](#removevertexlocked-pluginpkgauthauthorizernodegraphgo315) `:315`


</details>


[function] name: AddPV file: plugin/pkg/auth/authorizer/node/graph.go:512 returns_error: нет description: AddPV sets up edges for the following relationships:

secret -> pv

pv -> pvc


### AddPV (plugin/pkg/auth/authorizer/node/graph.go:512)


AddPV sets up edges for the following relationships:

secret -> pv

pv -> pvc


```go
func (g *Graph) AddPV((pv *corev1.PersistentVolume)) (pv *corev1.PersistentVolume)
```


**Тип запроса:** corev1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pv


```json
{
  "delegate": {},
  "lock": {},
  "docs": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/openapi/cached/groupversion.go`


**Тип ответа:** corev1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:512`



---


[function] name: AddPod file: plugin/pkg/auth/authorizer/node/graph.go:360 returns_error: нет description: AddPod should only be called once spec.NodeName is populated.
It sets up edges for the following relationships (which ar


### AddPod (plugin/pkg/auth/authorizer/node/graph.go:360)


AddPod should only be called once spec.NodeName is populated.
It sets up edges for the following relationships (which are immutable for a pod once bound to a node):

pod       -> node
secret    -> pod
configmap -> pod
pvc       -> pod
svcacct   -> pod


```go
func (g *Graph) AddPod((pod *corev1.Pod)) (pod *corev1.Pod)
```


**Тип запроса:** corev1.Pod


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** corev1.Pod


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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:360`



---


[function] name: AddPodCertificateRequest file: plugin/pkg/auth/authorizer/node/graph.go:482 returns_error: нет description: AddPodCertificateRequest adds a PodCertificateRequest to the graph.

PCRs technically have two valid edges:

* PCR -> Po


### AddPodCertificateRequest (plugin/pkg/auth/authorizer/node/graph.go:482)


AddPodCertificateRequest adds a PodCertificateRequest to the graph.

PCRs technically have two valid edges:

* PCR -> Pod (-> Node)

* PCR -> Node

We only add the direct PCR -> Node edge, since that is enough to perform the
authorization, and it's a shorter graph traversal.  The noderestriction
admission plugin ensures that all PCRs created have a valid node,
serviceaccount, and pod combination that actually exists in the cluster.


```go
func (g *Graph) AddPodCertificateRequest((pcr *certsv1beta1.PodCertificateRequest)) (pcr *certsv1beta1.PodCertificateRequest)
```


**Тип запроса:** certsv1beta1.PodCertificateRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/certificates/types.go`


**Тип ответа:** pcr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** certsv1beta1.PodCertificateRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/certificates/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:482`



---


[function] name: AddResourceSlice file: plugin/pkg/auth/authorizer/node/graph.go:585 returns_error: нет description: AddResourceSlice sets up edges for the following relationships:

node resource slice -> node


### AddResourceSlice (plugin/pkg/auth/authorizer/node/graph.go:585)


AddResourceSlice sets up edges for the following relationships:

node resource slice -> node


```go
func (g *Graph) AddResourceSlice((sliceName, nodeName string)) (sliceName, nodeName string)
```


**Тип ответа:** sliceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:585`



---


[function] name: AddVolumeAttachment file: plugin/pkg/auth/authorizer/node/graph.go:553 returns_error: нет description: AddVolumeAttachment sets up edges for the following relationships:

volume attachment -> node


### AddVolumeAttachment (plugin/pkg/auth/authorizer/node/graph.go:553)


AddVolumeAttachment sets up edges for the following relationships:

volume attachment -> node


```go
func (g *Graph) AddVolumeAttachment((attachmentName, nodeName string)) (attachmentName, nodeName string)
```


**Тип ответа:** attachmentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:553`



---


[function] name: DeletePV file: plugin/pkg/auth/authorizer/node/graph.go:540 returns_error: нет description: —


### DeletePV (plugin/pkg/auth/authorizer/node/graph.go:540)


DeletePV is a method that deletes data based on the provided parameters and returns (name string).


```go
func (g *Graph) DeletePV((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:540`



---


[function] name: DeletePod file: plugin/pkg/auth/authorizer/node/graph.go:460 returns_error: нет description: —


### DeletePod (plugin/pkg/auth/authorizer/node/graph.go:460)


DeletePod is a method that deletes data based on the provided parameters and returns (name, namespace string).


```go
func (g *Graph) DeletePod((name, namespace string)) (name, namespace string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:460`



---


[function] name: DeletePodCertificateRequest file: plugin/pkg/auth/authorizer/node/graph.go:497 returns_error: нет description: DeletePodCertificateRequest removes it from the graph.


### DeletePodCertificateRequest (plugin/pkg/auth/authorizer/node/graph.go:497)


DeletePodCertificateRequest removes it from the graph.


```go
func (g *Graph) DeletePodCertificateRequest((pcr *certsv1beta1.PodCertificateRequest)) (pcr *certsv1beta1.PodCertificateRequest)
```


**Тип запроса:** certsv1beta1.PodCertificateRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/certificates/types.go`


**Тип ответа:** pcr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** certsv1beta1.PodCertificateRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/certificates/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:497`



---


[function] name: DeleteResourceSlice file: plugin/pkg/auth/authorizer/node/graph.go:604 returns_error: нет description: —


### DeleteResourceSlice (plugin/pkg/auth/authorizer/node/graph.go:604)


DeleteResourceSlice is a method that deletes data based on the provided parameters and returns (sliceName string).


```go
func (g *Graph) DeleteResourceSlice((sliceName string)) (sliceName string)
```


**Тип ответа:** sliceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:604`



---


[function] name: DeleteVolumeAttachment file: plugin/pkg/auth/authorizer/node/graph.go:572 returns_error: нет description: —


### DeleteVolumeAttachment (plugin/pkg/auth/authorizer/node/graph.go:572)


DeleteVolumeAttachment is a method that deletes data based on the provided parameters and returns (name string).


```go
func (g *Graph) DeleteVolumeAttachment((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:572`



---


[function] name: DestinationID file: plugin/pkg/auth/authorizer/node/graph.go:74 returns_error: нет description: —


### DestinationID (plugin/pkg/auth/authorizer/node/graph.go:74)


DestinationID is a method that performs operations based on the provided parameters and returns ().


```go
func (e *destinationEdge) DestinationID(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:74`



---


[function] name: From file: plugin/pkg/auth/authorizer/node/graph.go:71 returns_error: нет description: —


### From (plugin/pkg/auth/authorizer/node/graph.go:71)


From is a method that performs operations based on the provided parameters and returns ().


```go
func (e *destinationEdge) From(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:71`



---


[function] name: ID file: plugin/pkg/auth/authorizer/node/graph.go:50 returns_error: нет description: —


### ID (plugin/pkg/auth/authorizer/node/graph.go:50)


ID is a method that performs operations based on the provided parameters and returns ().


```go
func (n *namedVertex) ID(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:50`



---


[function] name: NewGraph file: plugin/pkg/auth/authorizer/node/graph.go:102 returns_error: нет description: —


### NewGraph (plugin/pkg/auth/authorizer/node/graph.go:102)


NewGraph is a function that performs operations based on the provided parameters and returns ().


```go
func NewGraph(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:102`



---


[function] name: String file: plugin/pkg/auth/authorizer/node/graph.go:53 returns_error: нет description: —


### String (plugin/pkg/auth/authorizer/node/graph.go:53)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (n *namedVertex) String(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:53`



---


[function] name: To file: plugin/pkg/auth/authorizer/node/graph.go:72 returns_error: нет description: —


### To (plugin/pkg/auth/authorizer/node/graph.go:72)


To is a method that performs operations based on the provided parameters and returns ().


```go
func (e *destinationEdge) To(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:72`



---


[function] name: Weight file: plugin/pkg/auth/authorizer/node/graph.go:73 returns_error: нет description: —


### Weight (plugin/pkg/auth/authorizer/node/graph.go:73)


Weight is a method that performs operations based on the provided parameters and returns ().


```go
func (e *destinationEdge) Weight(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:73`



---


[function] name: addEdgeLocked file: plugin/pkg/auth/authorizer/node/graph.go:443 returns_error: нет description: Must be called under a write lock.
All edge adds must be handled by that method rather than by calling
g.graph.SetEdge d


### addEdgeLocked (plugin/pkg/auth/authorizer/node/graph.go:443)


Must be called under a write lock.
All edge adds must be handled by that method rather than by calling
g.graph.SetEdge directly.
Note: if "from" belongs to vertexTypeWithAuthoritativeIndex, then
"destination" must be non-nil.


```go
func (g *Graph) addEdgeLocked((from, to, destination *namedVertex)) (from, to, destination *namedVertex)
```


**Тип запроса:** namedVertex


```json
{
  "name": "string",
  "namespace": "string",
  "id": 0,
  "vertexType": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** from


```json
{
  "isInlined": false,
  "matchedKeys": [],
  "parentPath": [],
  "returnUnknownFields": false,
  "unknownFieldErrors": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/converter.go`


**Тип ответа:** to


```json
{
  "cache": {},
  "logger": {}
}
```


*Определено в:* `pkg/controller/volume/selinuxwarning/metrics.go`


**Тип ответа:** destination


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** namedVertex


```json
{
  "name": "string",
  "namespace": "string",
  "id": 0,
  "vertexType": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:443`



---


[function] name: addEdgeToDestinationIndexLocked file: plugin/pkg/auth/authorizer/node/graph.go:298 returns_error: нет description: A fastpath for recomputeDestinationIndexLocked for "adding edge case".


### addEdgeToDestinationIndexLocked (plugin/pkg/auth/authorizer/node/graph.go:298)


A fastpath for recomputeDestinationIndexLocked for "adding edge case".


```go
func (g *Graph) addEdgeToDestinationIndexLocked((e graph.Edge)) (e graph.Edge)
```


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


**Тип ответа:** graph.Edge


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:298`



---


[function] name: createVertexLocked file: plugin/pkg/auth/authorizer/node/graph.go:176 returns_error: нет description: must be called under a write lock


### createVertexLocked (plugin/pkg/auth/authorizer/node/graph.go:176)


must be called under a write lock


```go
func (g *Graph) createVertexLocked((vertexType vertexType, namespace, name string)) (vertexType vertexType, namespace, name string)
```


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:176`



---


[function] name: deleteEdgesLocked file: plugin/pkg/auth/authorizer/node/graph.go:241 returns_error: нет description: must be called under write lock
deletes edges from a given vertex type to a specific vertex
will delete each orphaned "f


### deleteEdgesLocked (plugin/pkg/auth/authorizer/node/graph.go:241)


must be called under write lock
deletes edges from a given vertex type to a specific vertex
will delete each orphaned "from" vertex, but will never delete the "to" vertex


```go
func (g *Graph) deleteEdgesLocked((fromType, toType vertexType, toNamespace, toName string)) (fromType, toType vertexType, toNamespace, toName string)
```


**Тип ответа:** fromType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** toType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** toNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** toName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:241`



---


[function] name: deleteVertexLocked file: plugin/pkg/auth/authorizer/node/graph.go:197 returns_error: нет description: must be called under write lock


### deleteVertexLocked (plugin/pkg/auth/authorizer/node/graph.go:197)


must be called under write lock


```go
func (g *Graph) deleteVertexLocked((vertexType vertexType, namespace, name string)) (vertexType vertexType, namespace, name string)
```


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:197`



---


[function] name: getOrCreateVertexLocked file: plugin/pkg/auth/authorizer/node/graph.go:162 returns_error: нет description: must be called under a write lock


### getOrCreateVertexLocked (plugin/pkg/auth/authorizer/node/graph.go:162)


must be called under a write lock


```go
func (g *Graph) getOrCreateVertexLocked((vertexType vertexType, namespace, name string)) (vertexType vertexType, namespace, name string)
```


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:162`



---


[function] name: getVertexRLocked file: plugin/pkg/auth/authorizer/node/graph.go:170 returns_error: нет description: must be called under a read lock


### getVertexRLocked (plugin/pkg/auth/authorizer/node/graph.go:170)


must be called under a read lock


```go
func (g *Graph) getVertexRLocked((*namedVertex, bool)) (*namedVertex, bool)
```


**Тип запроса:** namedVertex


```json
{
  "name": "string",
  "namespace": "string",
  "id": 0,
  "vertexType": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** namedVertex


```json
{
  "name": "string",
  "namespace": "string",
  "id": 0,
  "vertexType": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:170`



---


[function] name: newDestinationEdge file: plugin/pkg/auth/authorizer/node/graph.go:68 returns_error: нет description: —


### newDestinationEdge (plugin/pkg/auth/authorizer/node/graph.go:68)


newDestinationEdge is a function that performs operations based on the provided parameters and returns (from, to, destination graph.Node).


```go
func newDestinationEdge((from, to, destination graph.Node)) (from, to, destination graph.Node)
```


**Тип ответа:** from


```json
{
  "isInlined": false,
  "matchedKeys": [],
  "parentPath": [],
  "returnUnknownFields": false,
  "unknownFieldErrors": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/converter.go`


**Тип ответа:** to


```json
{
  "cache": {},
  "logger": {}
}
```


*Определено в:* `pkg/controller/volume/selinuxwarning/metrics.go`


**Тип ответа:** destination


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** graph.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:68`



---


[function] name: newNamedVertex file: plugin/pkg/auth/authorizer/node/graph.go:42 returns_error: нет description: —


### newNamedVertex (plugin/pkg/auth/authorizer/node/graph.go:42)


newNamedVertex is a function that performs operations based on the provided parameters and returns (vertexType vertexType, namespace, name string, id int).


```go
func newNamedVertex((vertexType vertexType, namespace, name string, id int)) (vertexType vertexType, namespace, name string, id int)
```


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vertexType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** id


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/coordination/v1beta1/leasecandidate.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:42`



---


[function] name: recomputeDestinationIndexLocked file: plugin/pkg/auth/authorizer/node/graph.go:326 returns_error: нет description: must be called under write lock
recomputeDestinationIndexLocked recomputes the index of destination ids for the specifie


### recomputeDestinationIndexLocked (plugin/pkg/auth/authorizer/node/graph.go:326)


must be called under write lock
recomputeDestinationIndexLocked recomputes the index of destination ids for the specified vertex


```go
func (g *Graph) recomputeDestinationIndexLocked((n graph.Node)) (n graph.Node)
```


**Тип ответа:** n


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** graph.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:326`



---


[function] name: removeEdgeFromDestinationIndexLocked file: plugin/pkg/auth/authorizer/node/graph.go:278 returns_error: нет description: A fastpath for recomputeDestinationIndexLocked for "removing edge" case.


### removeEdgeFromDestinationIndexLocked (plugin/pkg/auth/authorizer/node/graph.go:278)


A fastpath for recomputeDestinationIndexLocked for "removing edge" case.


```go
func (g *Graph) removeEdgeFromDestinationIndexLocked((e graph.Edge)) (e graph.Edge)
```


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


**Тип ответа:** graph.Edge


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:278`



---


[function] name: removeVertexLocked file: plugin/pkg/auth/authorizer/node/graph.go:315 returns_error: нет description: must be called under write lock
removeVertexLocked removes the specified vertex from the graph and from the maintained i


### removeVertexLocked (plugin/pkg/auth/authorizer/node/graph.go:315)


must be called under write lock
removeVertexLocked removes the specified vertex from the graph and from the maintained indices.
It does nothing to indexes of neighbor vertices.


```go
func (g *Graph) removeVertexLocked((v *namedVertex)) (v *namedVertex)
```


**Тип запроса:** namedVertex


```json
{
  "name": "string",
  "namespace": "string",
  "id": 0,
  "vertexType": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** v


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


**Тип ответа:** namedVertex


```json
{
  "name": "string",
  "namespace": "string",
  "id": 0,
  "vertexType": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph.go:315`




## plugin/pkg/auth/authorizer/node/graph_populator.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/node/graph_populator.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [AddGraphEventHandlers](#addgrapheventhandlers-pluginpkgauthauthorizernodegraph_populatorgo42) `:42`

- 🔗 [addPCR](#addpcr-pluginpkgauthauthorizernodegraph_populatorgo218) `:218`

- 🔗 [addPV](#addpv-pluginpkgauthauthorizernodegraph_populatorgo147) `:147`

- 🔗 [addPod](#addpod-pluginpkgauthauthorizernodegraph_populatorgo98) `:98`

- 🔗 [addResourceSlice](#addresourceslice-pluginpkgauthauthorizernodegraph_populatorgo197) `:197`

- 🔗 [addVolumeAttachment](#addvolumeattachment-pluginpkgauthauthorizernodegraph_populatorgo169) `:169`

- 🔗 [deletePCR](#deletepcr-pluginpkgauthauthorizernodegraph_populatorgo227) `:227`

- 🔗 [deletePV](#deletepv-pluginpkgauthauthorizernodegraph_populatorgo157) `:157`

- 🔗 [deletePod](#deletepod-pluginpkgauthauthorizernodegraph_populatorgo127) `:127`

- 🔗 [deleteResourceSlice](#deleteresourceslice-pluginpkgauthauthorizernodegraph_populatorgo206) `:206`

- 🔗 [deleteVolumeAttachment](#deletevolumeattachment-pluginpkgauthauthorizernodegraph_populatorgo185) `:185`

- 🔗 [updatePV](#updatepv-pluginpkgauthauthorizernodegraph_populatorgo151) `:151`

- 🔗 [updatePod](#updatepod-pluginpkgauthauthorizernodegraph_populatorgo102) `:102`

- 🔗 [updateVolumeAttachment](#updatevolumeattachment-pluginpkgauthauthorizernodegraph_populatorgo173) `:173`


</details>


[function] name: AddGraphEventHandlers file: plugin/pkg/auth/authorizer/node/graph_populator.go:42 returns_error: нет description: —


### AddGraphEventHandlers (plugin/pkg/auth/authorizer/node/graph_populator.go:42)


AddGraphEventHandlers is a function that creates new data based on the provided parameters and returns (
	graph *Graph,
	nodes corev1informers.NodeInformer,
	pods corev1informers.PodInformer,
	pvs corev1informers.PersistentVolumeInformer,
	attachments storageinformers.VolumeAttachmentInformer,
	slices resourceinformers.ResourceSliceInformer,
	pcrs certsv1beta1informers.PodCertificateRequestInformer,
).


```go
func AddGraphEventHandlers((
	graph *Graph,
	nodes corev1informers.NodeInformer,
	pods corev1informers.PodInformer,
	pvs corev1informers.PersistentVolumeInformer,
	attachments storageinformers.VolumeAttachmentInformer,
	slices resourceinformers.ResourceSliceInformer,
	pcrs certsv1beta1informers.PodCertificateRequestInformer,
)) (
	graph *Graph,
	nodes corev1informers.NodeInformer,
	pods corev1informers.PodInformer,
	pvs corev1informers.PersistentVolumeInformer,
	attachments storageinformers.VolumeAttachmentInformer,
	slices resourceinformers.ResourceSliceInformer,
	pcrs certsv1beta1informers.PodCertificateRequestInformer,
)
```


**Тип запроса:** Graph


```json
{
  "lock": {},
  "graph": null,
  "vertices": {},
  "destinationEdgeIndex": {},
  "destinationEdgeThreshold": 0
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** graph


```json
{
  "outEdges": {},
  "inDegree": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/sort/sort.go`


**Тип ответа:** Graph


```json
{
  "lock": {},
  "graph": null,
  "vertices": {},
  "destinationEdgeIndex": {},
  "destinationEdgeThreshold": 0
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** nodes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1informers.NodeInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/storage/v1beta1/csinode.go`


**Тип ответа:** pods


```json
{
  "pods": {},
  "mu": {}
}
```


*Определено в:* `pkg/scheduler/framework/runtime/pods_in_prebind_map.go`


**Тип ответа:** corev1informers.PodInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pvs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1informers.PersistentVolumeInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** attachments


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** storageinformers.VolumeAttachmentInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slices


```json
{
  "toCreate": []
}
```


*Определено в:* `pkg/controller/endpointslicemirroring/reconciler_helpers.go`


**Тип ответа:** resourceinformers.ResourceSliceInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pcrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** certsv1beta1informers.PodCertificateRequestInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:42`



---


[function] name: addPCR file: plugin/pkg/auth/authorizer/node/graph_populator.go:218 returns_error: нет description: —


### addPCR (plugin/pkg/auth/authorizer/node/graph_populator.go:218)


addPCR is a method that performs operations based on the provided parameters and returns (obj any).


```go
func (g *graphPopulator) addPCR((obj any)) (obj any)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:218`



---


[function] name: addPV file: plugin/pkg/auth/authorizer/node/graph_populator.go:147 returns_error: нет description: —


### addPV (plugin/pkg/auth/authorizer/node/graph_populator.go:147)


addPV is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) addPV((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:147`



---


[function] name: addPod file: plugin/pkg/auth/authorizer/node/graph_populator.go:98 returns_error: нет description: —


### addPod (plugin/pkg/auth/authorizer/node/graph_populator.go:98)


addPod is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) addPod((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:98`



---


[function] name: addResourceSlice file: plugin/pkg/auth/authorizer/node/graph_populator.go:197 returns_error: нет description: —


### addResourceSlice (plugin/pkg/auth/authorizer/node/graph_populator.go:197)


addResourceSlice is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) addResourceSlice((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:197`



---


[function] name: addVolumeAttachment file: plugin/pkg/auth/authorizer/node/graph_populator.go:169 returns_error: нет description: —


### addVolumeAttachment (plugin/pkg/auth/authorizer/node/graph_populator.go:169)


addVolumeAttachment is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) addVolumeAttachment((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:169`



---


[function] name: deletePCR file: plugin/pkg/auth/authorizer/node/graph_populator.go:227 returns_error: нет description: —


### deletePCR (plugin/pkg/auth/authorizer/node/graph_populator.go:227)


deletePCR is a method that performs operations based on the provided parameters and returns (obj any).


```go
func (g *graphPopulator) deletePCR((obj any)) (obj any)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:227`



---


[function] name: deletePV file: plugin/pkg/auth/authorizer/node/graph_populator.go:157 returns_error: нет description: —


### deletePV (plugin/pkg/auth/authorizer/node/graph_populator.go:157)


deletePV is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) deletePV((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:157`



---


[function] name: deletePod file: plugin/pkg/auth/authorizer/node/graph_populator.go:127 returns_error: нет description: —


### deletePod (plugin/pkg/auth/authorizer/node/graph_populator.go:127)


deletePod is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) deletePod((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:127`



---


[function] name: deleteResourceSlice file: plugin/pkg/auth/authorizer/node/graph_populator.go:206 returns_error: нет description: —


### deleteResourceSlice (plugin/pkg/auth/authorizer/node/graph_populator.go:206)


deleteResourceSlice is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) deleteResourceSlice((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:206`



---


[function] name: deleteVolumeAttachment file: plugin/pkg/auth/authorizer/node/graph_populator.go:185 returns_error: нет description: —


### deleteVolumeAttachment (plugin/pkg/auth/authorizer/node/graph_populator.go:185)


deleteVolumeAttachment is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (g *graphPopulator) deleteVolumeAttachment((obj interface{})) (obj interface{})
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:185`



---


[function] name: updatePV file: plugin/pkg/auth/authorizer/node/graph_populator.go:151 returns_error: нет description: —


### updatePV (plugin/pkg/auth/authorizer/node/graph_populator.go:151)


updatePV is a method that performs operations based on the provided parameters and returns (oldObj, obj interface{}).


```go
func (g *graphPopulator) updatePV((oldObj, obj interface{})) (oldObj, obj interface{})
```


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:151`



---


[function] name: updatePod file: plugin/pkg/auth/authorizer/node/graph_populator.go:102 returns_error: нет description: —


### updatePod (plugin/pkg/auth/authorizer/node/graph_populator.go:102)


updatePod is a method that performs operations based on the provided parameters and returns (oldObj, obj interface{}).


```go
func (g *graphPopulator) updatePod((oldObj, obj interface{})) (oldObj, obj interface{})
```


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:102`



---


[function] name: updateVolumeAttachment file: plugin/pkg/auth/authorizer/node/graph_populator.go:173 returns_error: нет description: —


### updateVolumeAttachment (plugin/pkg/auth/authorizer/node/graph_populator.go:173)


updateVolumeAttachment is a method that performs operations based on the provided parameters and returns (oldObj, obj interface{}).


```go
func (g *graphPopulator) updateVolumeAttachment((oldObj, obj interface{})) (oldObj, obj interface{})
```


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/graph_populator.go:173`




## plugin/pkg/auth/authorizer/node/intset.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/node/intset.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [decrement](#decrement-pluginpkgauthauthorizernodeintsetgo56) `:56`

- 🔗 [has](#has-pluginpkgauthauthorizernodeintsetgo31) `:31`

- 🔗 [increment](#increment-pluginpkgauthauthorizernodeintsetgo48) `:48`

- 🔗 [newIntSet](#newintset-pluginpkgauthauthorizernodeintsetgo25) `:25`

- 🔗 [reset](#reset-pluginpkgauthauthorizernodeintsetgo40) `:40`


</details>


[function] name: decrement file: plugin/pkg/auth/authorizer/node/intset.go:56 returns_error: нет description: decrement removes one from the refcount of the specified id,
and removes the id if the resulting refcount is <= 0.
it wi


### decrement (plugin/pkg/auth/authorizer/node/intset.go:56)


decrement removes one from the refcount of the specified id,
and removes the id if the resulting refcount is <= 0.
it will not track refcounts lower than zero.
it is not thread-safe.


```go
func (s *intSet) decrement((i int)) (i int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/intset.go:56`



---


[function] name: has file: plugin/pkg/auth/authorizer/node/intset.go:31 returns_error: нет description: has returns true if the specified id has a positive refcount.
it is safe to call concurrently, but must not be called co


### has (plugin/pkg/auth/authorizer/node/intset.go:31)


has returns true if the specified id has a positive refcount.
it is safe to call concurrently, but must not be called concurrently with any of the other methods.


```go
func (s *intSet) has((i int)) (i int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/intset.go:31`



---


[function] name: increment file: plugin/pkg/auth/authorizer/node/intset.go:48 returns_error: нет description: increment adds one to the refcount of the specified id.
it is not thread-safe.


### increment (plugin/pkg/auth/authorizer/node/intset.go:48)


increment adds one to the refcount of the specified id.
it is not thread-safe.


```go
func (s *intSet) increment((i int)) (i int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/intset.go:48`



---


[function] name: newIntSet file: plugin/pkg/auth/authorizer/node/intset.go:25 returns_error: нет description: —


### newIntSet (plugin/pkg/auth/authorizer/node/intset.go:25)


newIntSet is a function that performs operations based on the provided parameters and returns ().


```go
func newIntSet(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/intset.go:25`



---


[function] name: reset file: plugin/pkg/auth/authorizer/node/intset.go:40 returns_error: нет description: reset removes all ids, effectively setting their refcounts to 0.
it is not thread-safe.


### reset (plugin/pkg/auth/authorizer/node/intset.go:40)


reset removes all ids, effectively setting their refcounts to 0.
it is not thread-safe.


```go
func (s *intSet) reset(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/intset.go:40`




## plugin/pkg/auth/authorizer/node/metrics.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/node/metrics.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RegisterMetrics](#registermetrics-pluginpkgauthauthorizernodemetricsgo45) `:45`


</details>


[function] name: RegisterMetrics file: plugin/pkg/auth/authorizer/node/metrics.go:45 returns_error: нет description: RegisterMetrics registers metrics for node package.


### RegisterMetrics (plugin/pkg/auth/authorizer/node/metrics.go:45)


RegisterMetrics registers metrics for node package.


```go
func RegisterMetrics(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/metrics.go:45`




## plugin/pkg/auth/authorizer/node/node_authorizer.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/node/node_authorizer.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [Authorize](#authorize-pluginpkgauthauthorizernodenode_authorizergo109) `:109`

- 🔗 [NewAuthorizer](#newauthorizer-pluginpkgauthauthorizernodenode_authorizergo76) `:76`

- 🔗 [RulesFor](#rulesfor-pluginpkgauthauthorizernodenode_authorizergo101) `:101`

- 🔗 [authorize](#authorize-pluginpkgauthauthorizernodenode_authorizergo224) `:224`

- 🔗 [authorizeCSINode](#authorizecsinode-pluginpkgauthauthorizernodenode_authorizergo314) `:314`

- 🔗 [authorizeCreateToken](#authorizecreatetoken-pluginpkgauthauthorizernodenode_authorizergo261) `:261`

- 🔗 [authorizeGet](#authorizeget-pluginpkgauthauthorizernodenode_authorizergo190) `:190`

- 🔗 [authorizeLease](#authorizelease-pluginpkgauthauthorizernodenode_authorizergo285) `:285`

- 🔗 [authorizeNode](#authorizenode-pluginpkgauthauthorizernodenode_authorizergo416) `:416`

- 🔗 [authorizePod](#authorizepod-pluginpkgauthauthorizernodenode_authorizergo450) `:450`

- 🔗 [authorizePodCertificateRequest](#authorizepodcertificaterequest-pluginpkgauthauthorizernodenode_authorizergo387) `:387`

- 🔗 [authorizeReadNamespacedObject](#authorizereadnamespacedobject-pluginpkgauthauthorizernodenode_authorizergo204) `:204`

- 🔗 [authorizeResourceSlice](#authorizeresourceslice-pluginpkgauthauthorizernodenode_authorizergo342) `:342`

- 🔗 [authorizeServiceAccount](#authorizeserviceaccount-pluginpkgauthauthorizernodenode_authorizergo245) `:245`

- 🔗 [authorizeStatusUpdate](#authorizestatusupdate-pluginpkgauthauthorizernodenode_authorizergo172) `:172`

- 🔗 [hasPathFrom](#haspathfrom-pluginpkgauthauthorizernodenode_authorizergo500) `:500`


</details>


[function] name: Authorize file: plugin/pkg/auth/authorizer/node/node_authorizer.go:109 returns_error: да description: —


### Authorize (plugin/pkg/auth/authorizer/node/node_authorizer.go:109)


Authorize is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *NodeAuthorizer) Authorize((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:109`



---


[function] name: NewAuthorizer file: plugin/pkg/auth/authorizer/node/node_authorizer.go:76 returns_error: нет description: NewAuthorizer returns a new node authorizer


### NewAuthorizer (plugin/pkg/auth/authorizer/node/node_authorizer.go:76)


NewAuthorizer returns a new node authorizer


```go
func NewAuthorizer((graph *Graph, identifier nodeidentifier.NodeIdentifier, rules []rbacv1.PolicyRule)) (graph *Graph, identifier nodeidentifier.NodeIdentifier, rules []rbacv1.PolicyRule)
```


**Тип запроса:** Graph


```json
{
  "lock": {},
  "graph": null,
  "vertices": {},
  "destinationEdgeIndex": {},
  "destinationEdgeThreshold": 0
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** graph


```json
{
  "outEdges": {},
  "inDegree": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/sort/sort.go`


**Тип ответа:** Graph


```json
{
  "lock": {},
  "graph": null,
  "vertices": {},
  "destinationEdgeIndex": {},
  "destinationEdgeThreshold": 0
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** identifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeidentifier.NodeIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rules


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacv1.PolicyRule


```json
{
  "Verbs": [],
  "APIGroups": [],
  "Resources": [],
  "ResourceNames": [],
  "NonResourceURLs": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:76`



---


[function] name: RulesFor file: plugin/pkg/auth/authorizer/node/node_authorizer.go:101 returns_error: да description: —


### RulesFor (plugin/pkg/auth/authorizer/node/node_authorizer.go:101)


RulesFor is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *NodeAuthorizer) RulesFor(([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)) ([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:101`



---


[function] name: authorize file: plugin/pkg/auth/authorizer/node/node_authorizer.go:224 returns_error: да description: —


### authorize (plugin/pkg/auth/authorizer/node/node_authorizer.go:224)


authorize is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *NodeAuthorizer) authorize((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:224`



---


[function] name: authorizeCSINode file: plugin/pkg/auth/authorizer/node/node_authorizer.go:314 returns_error: да description: authorizeCSINode authorizes node requests to CSINode storage.k8s.io/csinodes


### authorizeCSINode (plugin/pkg/auth/authorizer/node/node_authorizer.go:314)


authorizeCSINode authorizes node requests to CSINode storage.k8s.io/csinodes


```go
func (r *NodeAuthorizer) authorizeCSINode((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:314`



---


[function] name: authorizeCreateToken file: plugin/pkg/auth/authorizer/node/node_authorizer.go:261 returns_error: да description: authorizeCreateToken authorizes "create" requests to serviceaccounts 'token'
subresource of pods running on a node


### authorizeCreateToken (plugin/pkg/auth/authorizer/node/node_authorizer.go:261)


authorizeCreateToken authorizes "create" requests to serviceaccounts 'token'
subresource of pods running on a node


```go
func (r *NodeAuthorizer) authorizeCreateToken((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:261`



---


[function] name: authorizeGet file: plugin/pkg/auth/authorizer/node/node_authorizer.go:190 returns_error: да description: authorizeGet authorizes "get" requests to objects of the specified type if they are related to the specified node


### authorizeGet (plugin/pkg/auth/authorizer/node/node_authorizer.go:190)


authorizeGet authorizes "get" requests to objects of the specified type if they are related to the specified node


```go
func (r *NodeAuthorizer) authorizeGet((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:190`



---


[function] name: authorizeLease file: plugin/pkg/auth/authorizer/node/node_authorizer.go:285 returns_error: да description: authorizeLease authorizes node requests to coordination.k8s.io/leases.


### authorizeLease (plugin/pkg/auth/authorizer/node/node_authorizer.go:285)


authorizeLease authorizes node requests to coordination.k8s.io/leases.


```go
func (r *NodeAuthorizer) authorizeLease((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:285`



---


[function] name: authorizeNode file: plugin/pkg/auth/authorizer/node/node_authorizer.go:416 returns_error: да description: authorizeNode authorizes node requests to Node API objects


### authorizeNode (plugin/pkg/auth/authorizer/node/node_authorizer.go:416)


authorizeNode authorizes node requests to Node API objects


```go
func (r *NodeAuthorizer) authorizeNode((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:416`



---


[function] name: authorizePod file: plugin/pkg/auth/authorizer/node/node_authorizer.go:450 returns_error: да description: authorizePod authorizes node requests to Pod API objects


### authorizePod (plugin/pkg/auth/authorizer/node/node_authorizer.go:450)


authorizePod authorizes node requests to Pod API objects


```go
func (r *NodeAuthorizer) authorizePod((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:450`



---


[function] name: authorizePodCertificateRequest file: plugin/pkg/auth/authorizer/node/node_authorizer.go:387 returns_error: да description: —


### authorizePodCertificateRequest (plugin/pkg/auth/authorizer/node/node_authorizer.go:387)


authorizePodCertificateRequest is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *NodeAuthorizer) authorizePodCertificateRequest((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:387`



---


[function] name: authorizeReadNamespacedObject file: plugin/pkg/auth/authorizer/node/node_authorizer.go:204 returns_error: да description: authorizeReadNamespacedObject authorizes "get", "list" and "watch" requests to single objects of a
specified types if th


### authorizeReadNamespacedObject (plugin/pkg/auth/authorizer/node/node_authorizer.go:204)


authorizeReadNamespacedObject authorizes "get", "list" and "watch" requests to single objects of a
specified types if they are related to the specified node.


```go
func (r *NodeAuthorizer) authorizeReadNamespacedObject((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:204`



---


[function] name: authorizeResourceSlice file: plugin/pkg/auth/authorizer/node/node_authorizer.go:342 returns_error: да description: authorizeResourceSlice authorizes node requests to ResourceSlice resource.k8s.io/resourceslices


### authorizeResourceSlice (plugin/pkg/auth/authorizer/node/node_authorizer.go:342)


authorizeResourceSlice authorizes node requests to ResourceSlice resource.k8s.io/resourceslices


```go
func (r *NodeAuthorizer) authorizeResourceSlice((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:342`



---


[function] name: authorizeServiceAccount file: plugin/pkg/auth/authorizer/node/node_authorizer.go:245 returns_error: да description: authorizeServiceAccount authorizes
- "get" requests to serviceaccounts when KubeletServiceAccountTokenForCredentialProvi


### authorizeServiceAccount (plugin/pkg/auth/authorizer/node/node_authorizer.go:245)


authorizeServiceAccount authorizes
- "get" requests to serviceaccounts when KubeletServiceAccountTokenForCredentialProviders or PodCertificateRequest features are enabled
- "create" requests to serviceaccounts 'token' subresource of pods running on a node


```go
func (r *NodeAuthorizer) authorizeServiceAccount((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:245`



---


[function] name: authorizeStatusUpdate file: plugin/pkg/auth/authorizer/node/node_authorizer.go:172 returns_error: да description: authorizeStatusUpdate authorizes get/update/patch requests to status subresources of the specified type if they are rela


### authorizeStatusUpdate (plugin/pkg/auth/authorizer/node/node_authorizer.go:172)


authorizeStatusUpdate authorizes get/update/patch requests to status subresources of the specified type if they are related to the specified node


```go
func (r *NodeAuthorizer) authorizeStatusUpdate((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:172`



---


[function] name: hasPathFrom file: plugin/pkg/auth/authorizer/node/node_authorizer.go:500 returns_error: да description: hasPathFrom returns true if there is a directed path from the specified type/namespace/name to the specified Node


### hasPathFrom (plugin/pkg/auth/authorizer/node/node_authorizer.go:500)


hasPathFrom returns true if there is a directed path from the specified type/namespace/name to the specified Node


```go
func (r *NodeAuthorizer) hasPathFrom((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authorizer/node/node_authorizer.go:500`




## plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [ControllerRoleBindings](#controllerrolebindings-pluginpkgauthauthorizerrbacbootstrappolicycontroller_policygo566) `:566`

- 🔗 [ControllerRoles](#controllerroles-pluginpkgauthauthorizerrbacbootstrappolicycontroller_policygo560) `:560`

- 🔗 [addControllerRole](#addcontrollerrole-pluginpkgauthauthorizerrbacbootstrappolicycontroller_policygo36) `:36`

- 🔗 [buildControllerRoles](#buildcontrollerroles-pluginpkgauthauthorizerrbacbootstrappolicycontroller_policygo59) `:59`

- 🔗 [eventsRule](#eventsrule-pluginpkgauthauthorizerrbacbootstrappolicycontroller_policygo55) `:55`


</details>


[function] name: ControllerRoleBindings file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:566 returns_error: нет description: ControllerRoleBindings returns the role bindings used by controllers


### ControllerRoleBindings (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:566)


ControllerRoleBindings returns the role bindings used by controllers


```go
func ControllerRoleBindings(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:566`



---


[function] name: ControllerRoles file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:560 returns_error: нет description: ControllerRoles returns the cluster roles used by controllers


### ControllerRoles (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:560)


ControllerRoles returns the cluster roles used by controllers


```go
func ControllerRoles(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:560`



---


[function] name: addControllerRole file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:36 returns_error: нет description: —


### addControllerRole (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:36)


addControllerRole is a function that performs operations based on the provided parameters and returns (controllerRoles *[]rbacv1.ClusterRole, controllerRoleBindings *[]rbacv1.ClusterRoleBinding, role rbacv1.ClusterRole).


```go
func addControllerRole((controllerRoles *[]rbacv1.ClusterRole, controllerRoleBindings *[]rbacv1.ClusterRoleBinding, role rbacv1.ClusterRole)) (controllerRoles *[]rbacv1.ClusterRole, controllerRoleBindings *[]rbacv1.ClusterRoleBinding, role rbacv1.ClusterRole)
```


**Тип ответа:** controllerRoles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacv1.ClusterRole


```json
{
  "Rules": [],
  "AggregationRule": null
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** controllerRoleBindings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacv1.ClusterRoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** role


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/rbac/v1alpha1/role.go`


**Тип ответа:** rbacv1.ClusterRole


```json
{
  "Rules": [],
  "AggregationRule": null
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:36`



---


[function] name: buildControllerRoles file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:59 returns_error: нет description: —


### buildControllerRoles (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:59)


buildControllerRoles is a function that performs operations based on the provided parameters and returns ([]rbacv1.ClusterRole, []rbacv1.ClusterRoleBinding).


```go
func buildControllerRoles(([]rbacv1.ClusterRole, []rbacv1.ClusterRoleBinding)) ([]rbacv1.ClusterRole, []rbacv1.ClusterRoleBinding)
```


**Тип ответа:** rbacv1.ClusterRole


```json
{
  "Rules": [],
  "AggregationRule": null
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** rbacv1.ClusterRoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:59`



---


[function] name: eventsRule file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:55 returns_error: нет description: —


### eventsRule (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:55)


eventsRule is a function that performs operations based on the provided parameters and returns ().


```go
func eventsRule(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go:55`




## plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NamespaceRoleBindings](#namespacerolebindings-pluginpkgauthauthorizerrbacbootstrappolicynamespace_policygo161) `:161`

- 🔗 [NamespaceRoles](#namespaceroles-pluginpkgauthauthorizerrbacbootstrappolicynamespace_policygo156) `:156`

- 🔗 [addNamespaceRole](#addnamespacerole-pluginpkgauthauthorizerrbacbootstrappolicynamespace_policygo38) `:38`

- 🔗 [addNamespaceRoleBinding](#addnamespacerolebinding-pluginpkgauthauthorizerrbacbootstrappolicynamespace_policygo56) `:56`

- 🔗 [init](#init-pluginpkgauthauthorizerrbacbootstrappolicynamespace_policygo74) `:74`


</details>


[function] name: NamespaceRoleBindings file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:161 returns_error: нет description: NamespaceRoleBindings returns a map of namespace to slice of roles to create


### NamespaceRoleBindings (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:161)


NamespaceRoleBindings returns a map of namespace to slice of roles to create


```go
func NamespaceRoleBindings(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:161`



---


[function] name: NamespaceRoles file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:156 returns_error: нет description: NamespaceRoles returns a map of namespace to slice of roles to create


### NamespaceRoles (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:156)


NamespaceRoles returns a map of namespace to slice of roles to create


```go
func NamespaceRoles(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:156`



---


[function] name: addNamespaceRole file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:38 returns_error: нет description: —


### addNamespaceRole (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:38)


addNamespaceRole is a function that performs operations based on the provided parameters and returns (namespace string, role rbacv1.Role).


```go
func addNamespaceRole((namespace string, role rbacv1.Role)) (namespace string, role rbacv1.Role)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** role


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/rbac/v1alpha1/role.go`


**Тип ответа:** rbacv1.Role


```json
{
  "Rules": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:38`



---


[function] name: addNamespaceRoleBinding file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:56 returns_error: нет description: —


### addNamespaceRoleBinding (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:56)


addNamespaceRoleBinding is a function that performs operations based on the provided parameters and returns (namespace string, roleBinding rbacv1.RoleBinding).


```go
func addNamespaceRoleBinding((namespace string, roleBinding rbacv1.RoleBinding)) (namespace string, roleBinding rbacv1.RoleBinding)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** roleBinding


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/rbac/v1alpha1/rolebinding.go`


**Тип ответа:** rbacv1.RoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:56`



---


[function] name: init file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:74 returns_error: нет description: —


### init (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:74)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/namespace_policy.go:74`




## plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [ClusterRoleBindings](#clusterrolebindings-pluginpkgauthauthorizerrbacbootstrappolicypolicygo685) `:685`

- 🔗 [ClusterRoleBindingsToSplit](#clusterrolebindingstosplit-pluginpkgauthauthorizerrbacbootstrappolicypolicygo739) `:739`

- 🔗 [ClusterRoles](#clusterroles-pluginpkgauthauthorizerrbacbootstrappolicypolicygo295) `:295`

- 🔗 [ClusterRolesToAggregate](#clusterrolestoaggregate-pluginpkgauthauthorizerrbacbootstrappolicypolicygo729) `:729`

- 🔗 [NodeRules](#noderules-pluginpkgauthauthorizerrbacbootstrappolicypolicygo200) `:200`

- 🔗 [addClusterRoleBindingLabel](#addclusterrolebindinglabel-pluginpkgauthauthorizerrbacbootstrappolicypolicygo105) `:105`

- 🔗 [addClusterRoleLabel](#addclusterrolelabel-pluginpkgauthauthorizerrbacbootstrappolicypolicygo98) `:98`

- 🔗 [addDefaultMetadata](#adddefaultmetadata-pluginpkgauthauthorizerrbacbootstrappolicypolicygo72) `:72`

- 🔗 [editRules](#editrules-pluginpkgauthauthorizerrbacbootstrappolicypolicygo155) `:155`

- 🔗 [viewRules](#viewrules-pluginpkgauthauthorizerrbacbootstrappolicypolicygo112) `:112`


</details>


[function] name: ClusterRoleBindings file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:685 returns_error: нет description: ClusterRoleBindings return default rolebindings to the default roles


### ClusterRoleBindings (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:685)


ClusterRoleBindings return default rolebindings to the default roles


```go
func ClusterRoleBindings(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:685`



---


[function] name: ClusterRoleBindingsToSplit file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:739 returns_error: нет description: ClusterRoleBindingsToSplit returns a map of Names of source ClusterRoleBindings
to copy Subjects, Annotations, and Label


### ClusterRoleBindingsToSplit (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:739)


ClusterRoleBindingsToSplit returns a map of Names of source ClusterRoleBindings
to copy Subjects, Annotations, and Labels to destination ClusterRoleBinding templates.


```go
func ClusterRoleBindingsToSplit(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:739`



---


[function] name: ClusterRoles file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:295 returns_error: нет description: ClusterRoles returns the cluster roles to bootstrap an API server with


### ClusterRoles (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:295)


ClusterRoles returns the cluster roles to bootstrap an API server with


```go
func ClusterRoles(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:295`



---


[function] name: ClusterRolesToAggregate file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:729 returns_error: нет description: ClusterRolesToAggregate maps from previous clusterrole name to the new clusterrole name


### ClusterRolesToAggregate (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:729)


ClusterRolesToAggregate maps from previous clusterrole name to the new clusterrole name


```go
func ClusterRolesToAggregate(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:729`



---


[function] name: NodeRules file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:200 returns_error: нет description: NodeRules returns node policy rules, it is slice of rbacv1.PolicyRule.


### NodeRules (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:200)


NodeRules returns node policy rules, it is slice of rbacv1.PolicyRule.


```go
func NodeRules(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:200`



---


[function] name: addClusterRoleBindingLabel file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:105 returns_error: нет description: —


### addClusterRoleBindingLabel (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:105)


addClusterRoleBindingLabel is a function that performs operations based on the provided parameters and returns (rolebindings []rbacv1.ClusterRoleBinding).


```go
func addClusterRoleBindingLabel((rolebindings []rbacv1.ClusterRoleBinding)) (rolebindings []rbacv1.ClusterRoleBinding)
```


**Тип ответа:** rolebindings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacv1.ClusterRoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:105`



---


[function] name: addClusterRoleLabel file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:98 returns_error: нет description: —


### addClusterRoleLabel (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:98)


addClusterRoleLabel is a function that performs operations based on the provided parameters and returns (roles []rbacv1.ClusterRole).


```go
func addClusterRoleLabel((roles []rbacv1.ClusterRole)) (roles []rbacv1.ClusterRole)
```


**Тип ответа:** roles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacv1.ClusterRole


```json
{
  "Rules": [],
  "AggregationRule": null
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:98`



---


[function] name: addDefaultMetadata file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:72 returns_error: нет description: —


### addDefaultMetadata (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:72)


addDefaultMetadata is a function that performs operations based on the provided parameters and returns (obj runtime.Object).


```go
func addDefaultMetadata((obj runtime.Object)) (obj runtime.Object)
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:72`



---


[function] name: editRules file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:155 returns_error: нет description: —


### editRules (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:155)


editRules is a function that performs operations based on the provided parameters and returns ().


```go
func editRules(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:155`



---


[function] name: viewRules file: plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:112 returns_error: нет description: —


### viewRules (plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:112)


viewRules is a function that performs operations based on the provided parameters and returns ().


```go
func viewRules(()) ()
```


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:112`




## plugin/pkg/auth/authorizer/rbac/rbac.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/rbac/rbac.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Authorize](#authorize-pluginpkgauthauthorizerrbacrbacgo75) `:75`

- 🔗 [GetClusterRole](#getclusterrole-pluginpkgauthauthorizerrbacrbacgo215) `:215`

- 🔗 [GetRole](#getrole-pluginpkgauthauthorizerrbacrbacgo199) `:199`

- 🔗 [ListClusterRoleBindings](#listclusterrolebindings-pluginpkgauthauthorizerrbacrbacgo223) `:223`

- 🔗 [ListRoleBindings](#listrolebindings-pluginpkgauthauthorizerrbacrbacgo207) `:207`

- 🔗 [New](#new-pluginpkgauthauthorizerrbacrbacgo159) `:159`

- 🔗 [RuleAllows](#ruleallows-pluginpkgauthauthorizerrbacrbacgo178) `:178`

- 🔗 [RulesAllow](#rulesallow-pluginpkgauthauthorizerrbacrbacgo168) `:168`

- 🔗 [RulesFor](#rulesfor-pluginpkgauthauthorizerrbacrbacgo129) `:129`

- 🔗 [visit](#visit-pluginpkgauthauthorizerrbacrbacgo63) `:63`


</details>


[function] name: Authorize file: plugin/pkg/auth/authorizer/rbac/rbac.go:75 returns_error: да description: —


### Authorize (plugin/pkg/auth/authorizer/rbac/rbac.go:75)


Authorize is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *RBACAuthorizer) Authorize((authorizer.Decision, string, error)) (authorizer.Decision, string, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:75`



---


[function] name: GetClusterRole file: plugin/pkg/auth/authorizer/rbac/rbac.go:215 returns_error: да description: —


### GetClusterRole (plugin/pkg/auth/authorizer/rbac/rbac.go:215)


GetClusterRole is a method that retrieves data based on the provided parameters and may return an error.


```go
func (g *ClusterRoleGetter) GetClusterRole((*rbacv1.ClusterRole, error)) (*rbacv1.ClusterRole, error)
```


**Тип запроса:** rbacv1.ClusterRole


```json
{
  "Rules": [],
  "AggregationRule": null
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** rbacv1.ClusterRole


```json
{
  "Rules": [],
  "AggregationRule": null
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*rbacv1.ClusterRole`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:215`



---


[function] name: GetRole file: plugin/pkg/auth/authorizer/rbac/rbac.go:199 returns_error: да description: —


### GetRole (plugin/pkg/auth/authorizer/rbac/rbac.go:199)


GetRole is a method that retrieves data based on the provided parameters and may return an error.


```go
func (g *RoleGetter) GetRole((*rbacv1.Role, error)) (*rbacv1.Role, error)
```


**Тип запроса:** rbacv1.Role


```json
{
  "Rules": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** rbacv1.Role


```json
{
  "Rules": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*rbacv1.Role`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:199`



---


[function] name: ListClusterRoleBindings file: plugin/pkg/auth/authorizer/rbac/rbac.go:223 returns_error: да description: —


### ListClusterRoleBindings (plugin/pkg/auth/authorizer/rbac/rbac.go:223)


ListClusterRoleBindings is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (l *ClusterRoleBindingLister) ListClusterRoleBindings(([]*rbacv1.ClusterRoleBinding, error)) ([]*rbacv1.ClusterRoleBinding, error)
```


**Тип запроса:** rbacv1.ClusterRoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** rbacv1.ClusterRoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*rbacv1.ClusterRoleBinding`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:223`



---


[function] name: ListRoleBindings file: plugin/pkg/auth/authorizer/rbac/rbac.go:207 returns_error: да description: —


### ListRoleBindings (plugin/pkg/auth/authorizer/rbac/rbac.go:207)


ListRoleBindings is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (l *RoleBindingLister) ListRoleBindings(([]*rbacv1.RoleBinding, error)) ([]*rbacv1.RoleBinding, error)
```


**Тип запроса:** rbacv1.RoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** rbacv1.RoleBinding


```json
{
  "Subjects": [],
  "RoleRef": {}
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*rbacv1.RoleBinding`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:207`



---


[function] name: New file: plugin/pkg/auth/authorizer/rbac/rbac.go:159 returns_error: нет description: —


### New (plugin/pkg/auth/authorizer/rbac/rbac.go:159)


New is a function that performs operations based on the provided parameters and returns (roles rbacregistryvalidation.RoleGetter, roleBindings rbacregistryvalidation.RoleBindingLister, clusterRoles rbacregistryvalidation.ClusterRoleGetter, clusterRoleBindings rbacregistryvalidation.ClusterRoleBindingLister).


```go
func New((roles rbacregistryvalidation.RoleGetter, roleBindings rbacregistryvalidation.RoleBindingLister, clusterRoles rbacregistryvalidation.ClusterRoleGetter, clusterRoleBindings rbacregistryvalidation.ClusterRoleBindingLister)) (roles rbacregistryvalidation.RoleGetter, roleBindings rbacregistryvalidation.RoleBindingLister, clusterRoles rbacregistryvalidation.ClusterRoleGetter, clusterRoleBindings rbacregistryvalidation.ClusterRoleBindingLister)
```


**Тип ответа:** roles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.RoleGetter


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


**Тип ответа:** roleBindings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.RoleBindingLister


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


**Тип ответа:** clusterRoles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.ClusterRoleGetter


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


**Тип ответа:** clusterRoleBindings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.ClusterRoleBindingLister


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:159`



---


[function] name: RuleAllows file: plugin/pkg/auth/authorizer/rbac/rbac.go:178 returns_error: нет description: —


### RuleAllows (plugin/pkg/auth/authorizer/rbac/rbac.go:178)


RuleAllows is a function that performs operations based on the provided parameters and returns (requestAttributes authorizer.Attributes, rule *rbacv1.PolicyRule).


```go
func RuleAllows((requestAttributes authorizer.Attributes, rule *rbacv1.PolicyRule)) (requestAttributes authorizer.Attributes, rule *rbacv1.PolicyRule)
```


**Тип запроса:** rbacv1.PolicyRule


```json
{
  "Verbs": [],
  "APIGroups": [],
  "Resources": [],
  "ResourceNames": [],
  "NonResourceURLs": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** requestAttributes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authorizer.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** rule


```json
{
  "rules": [],
  "errors": []
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Тип ответа:** rbacv1.PolicyRule


```json
{
  "Verbs": [],
  "APIGroups": [],
  "Resources": [],
  "ResourceNames": [],
  "NonResourceURLs": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:178`



---


[function] name: RulesAllow file: plugin/pkg/auth/authorizer/rbac/rbac.go:168 returns_error: нет description: —


### RulesAllow (plugin/pkg/auth/authorizer/rbac/rbac.go:168)


RulesAllow is a function that performs operations based on the provided parameters and returns (requestAttributes authorizer.Attributes, rules ...rbacv1.PolicyRule).


```go
func RulesAllow((requestAttributes authorizer.Attributes, rules ...rbacv1.PolicyRule)) (requestAttributes authorizer.Attributes, rules ...rbacv1.PolicyRule)
```


**Тип ответа:** requestAttributes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authorizer.Attributes


```json
{
  "ReadOnly": false,
  "Managed": false,
  "SELinuxRelabel": false
}
```


*Определено в:* `pkg/volume/volume.go`


**Тип ответа:** rules


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacv1.PolicyRule


```json
{
  "Verbs": [],
  "APIGroups": [],
  "Resources": [],
  "ResourceNames": [],
  "NonResourceURLs": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:168`



---


[function] name: RulesFor file: plugin/pkg/auth/authorizer/rbac/rbac.go:129 returns_error: да description: —


### RulesFor (plugin/pkg/auth/authorizer/rbac/rbac.go:129)


RulesFor is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *RBACAuthorizer) RulesFor(([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)) ([]authorizer.ResourceRuleInfo, []authorizer.NonResourceRuleInfo, bool, error)
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


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:129`



---


[function] name: visit file: plugin/pkg/auth/authorizer/rbac/rbac.go:63 returns_error: да description: —


### visit (plugin/pkg/auth/authorizer/rbac/rbac.go:63)


visit is a method that performs operations based on the provided parameters and may return an error.


```go
func (v *authorizingVisitor) visit((source fmt.Stringer, rule *rbacv1.PolicyRule, err error)) (source fmt.Stringer, rule *rbacv1.PolicyRule, err error)
```


**Тип запроса:** rbacv1.PolicyRule


```json
{
  "Verbs": [],
  "APIGroups": [],
  "Resources": [],
  "ResourceNames": [],
  "NonResourceURLs": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


**Тип ответа:** source


```json
{
  "Printer": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/output/output.go`


**Тип ответа:** fmt.Stringer


```json
{
  "val": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/format/formatting.go`


**Тип ответа:** rule


```json
{
  "rules": [],
  "errors": []
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Тип ответа:** rbacv1.PolicyRule


```json
{
  "Verbs": [],
  "APIGroups": [],
  "Resources": [],
  "ResourceNames": [],
  "NonResourceURLs": []
}
```


*Определено в:* `pkg/apis/rbac/types.go`


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


*Типы возврата:* `source fmt.Stringer`, `rule *rbacv1.PolicyRule`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/rbac.go:63`




## plugin/pkg/auth/authorizer/rbac/subject_locator.go


📄 Исходный файл: `plugin/pkg/auth/authorizer/rbac/subject_locator.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [AllowedSubjects](#allowedsubjects-pluginpkgauthauthorizerrbacsubject_locatorgo64) `:64`

- 🔗 [NewSubjectAccessEvaluator](#newsubjectaccessevaluator-pluginpkgauthauthorizerrbacsubject_locatorgo50) `:50`


</details>


[function] name: AllowedSubjects file: plugin/pkg/auth/authorizer/rbac/subject_locator.go:64 returns_error: да description: AllowedSubjects returns the subjects that can perform an action and any errors encountered while computing the list.
It 


### AllowedSubjects (plugin/pkg/auth/authorizer/rbac/subject_locator.go:64)


AllowedSubjects returns the subjects that can perform an action and any errors encountered while computing the list.
It is possible to have both subjects and errors returned if some rolebindings couldn't be resolved, but others could be.


```go
func (r *SubjectAccessEvaluator) AllowedSubjects(([]rbacv1.Subject, error)) ([]rbacv1.Subject, error)
```


**Тип ответа:** rbacv1.Subject


```json
{
  "Kind": {},
  "User": null,
  "Group": null,
  "ServiceAccount": null
}
```


*Определено в:* `pkg/apis/flowcontrol/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]rbacv1.Subject`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/subject_locator.go:64`



---


[function] name: NewSubjectAccessEvaluator file: plugin/pkg/auth/authorizer/rbac/subject_locator.go:50 returns_error: нет description: —


### NewSubjectAccessEvaluator (plugin/pkg/auth/authorizer/rbac/subject_locator.go:50)


NewSubjectAccessEvaluator is a function that performs operations based on the provided parameters and returns (roles rbacregistryvalidation.RoleGetter, roleBindings rbacregistryvalidation.RoleBindingLister, clusterRoles rbacregistryvalidation.ClusterRoleGetter, clusterRoleBindings rbacregistryvalidation.ClusterRoleBindingLister, superUser string).


```go
func NewSubjectAccessEvaluator((roles rbacregistryvalidation.RoleGetter, roleBindings rbacregistryvalidation.RoleBindingLister, clusterRoles rbacregistryvalidation.ClusterRoleGetter, clusterRoleBindings rbacregistryvalidation.ClusterRoleBindingLister, superUser string)) (roles rbacregistryvalidation.RoleGetter, roleBindings rbacregistryvalidation.RoleBindingLister, clusterRoles rbacregistryvalidation.ClusterRoleGetter, clusterRoleBindings rbacregistryvalidation.ClusterRoleBindingLister, superUser string)
```


**Тип ответа:** roles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.RoleGetter


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


**Тип ответа:** roleBindings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.RoleBindingLister


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


**Тип ответа:** clusterRoles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.ClusterRoleGetter


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


**Тип ответа:** clusterRoleBindings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rbacregistryvalidation.ClusterRoleBindingLister


```json
{
  "Lister": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/rbac/rbac.go`


**Тип ответа:** superUser


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `plugin/pkg/auth/authorizer/rbac/subject_locator.go:50`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_windows.md)

- [Следующая директория](staging_src.md)


---

