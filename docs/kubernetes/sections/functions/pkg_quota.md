---
title: "Функции: pkg/quota"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/quota
---


# Функции: pkg/quota


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_proxy.md)

- [Следующая директория](pkg_registry.md)


---


## Меню по файлам


- 📄 [pkg/quota/v1/evaluator/core/persistent_volume_claims.go](#pkgquotav1evaluatorcorepersistent_volume_claimsgo)

- 📄 [pkg/quota/v1/evaluator/core/pods.go](#pkgquotav1evaluatorcorepodsgo)

- 📄 [pkg/quota/v1/evaluator/core/registry.go](#pkgquotav1evaluatorcoreregistrygo)

- 📄 [pkg/quota/v1/evaluator/core/resource_claims.go](#pkgquotav1evaluatorcoreresource_claimsgo)

- 📄 [pkg/quota/v1/evaluator/core/services.go](#pkgquotav1evaluatorcoreservicesgo)

- 📄 [pkg/quota/v1/install/registry.go](#pkgquotav1installregistrygo)

- 📄 [pkg/quota/v1/install/update_filter.go](#pkgquotav1installupdate_filtergo)


---


## pkg/quota/v1/evaluator/core/persistent_volume_claims.go


📄 Исходный файл: `pkg/quota/v1/evaluator/core/persistent_volume_claims.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [Constraints](#constraints-pkgquotav1evaluatorcorepersistent_volume_claimsgo85) `:85`

- 🔗 [GroupResource](#groupresource-pkgquotav1evaluatorcorepersistent_volume_claimsgo91) `:91`

- 🔗 [Handles](#handles-pkgquotav1evaluatorcorepersistent_volume_claimsgo96) `:96`

- 🔗 [Matches](#matches-pkgquotav1evaluatorcorepersistent_volume_claimsgo114) `:114`

- 🔗 [MatchingResources](#matchingresources-pkgquotav1evaluatorcorepersistent_volume_claimsgo163) `:163`

- 🔗 [MatchingScopes](#matchingscopes-pkgquotav1evaluatorcorepersistent_volume_claimsgo122) `:122`

- 🔗 [NewPersistentVolumeClaimEvaluator](#newpersistentvolumeclaimevaluator-pkgquotav1evaluatorcorepersistent_volume_claimsgo72) `:72`

- 🔗 [RequiresQuotaReplenish](#requiresquotareplenish-pkgquotav1evaluatorcorepersistent_volume_claimsgo276) `:276`

- 🔗 [UncoveredQuotaScopes](#uncoveredquotascopes-pkgquotav1evaluatorcorepersistent_volume_claimsgo141) `:141`

- 🔗 [Usage](#usage-pkgquotav1evaluatorcorepersistent_volume_claimsgo189) `:189`

- 🔗 [UsageStats](#usagestats-pkgquotav1evaluatorcorepersistent_volume_claimsgo250) `:250`

- 🔗 [V1ResourceByStorageClass](#v1resourcebystorageclass-pkgquotav1evaluatorcorepersistent_volume_claimsgo67) `:67`

- 🔗 [getReferencedVolumeAttributesClassNames](#getreferencedvolumeattributesclassnames-pkgquotav1evaluatorcorepersistent_volume_claimsgo330) `:330`

- 🔗 [getStorageUsage](#getstorageusage-pkgquotav1evaluatorcorepersistent_volume_claimsgo218) `:218`

- 🔗 [pvcMatchesScopeFunc](#pvcmatchesscopefunc-pkgquotav1evaluatorcorepersistent_volume_claimsgo293) `:293`

- 🔗 [pvcMatchesSelector](#pvcmatchesselector-pkgquotav1evaluatorcorepersistent_volume_claimsgo311) `:311`

- 🔗 [toExternalPersistentVolumeClaimOrError](#toexternalpersistentvolumeclaimorerror-pkgquotav1evaluatorcorepersistent_volume_claimsgo260) `:260`


</details>


[function] name: Constraints file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:85 returns_error: нет description: Constraints verifies that all required resources are present on the item.


### Constraints (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:85)


Constraints verifies that all required resources are present on the item.


```go
func (p *pvcEvaluator) Constraints((required []corev1.ResourceName, item runtime.Object)) (required []corev1.ResourceName, item runtime.Object)
```


**Тип ответа:** required


```json
{
  "mode": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/required.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** item


```json
{
  "allocator": null,
  "serviceCIDRs": {}
}
```


*Определено в:* `pkg/registry/core/service/ipallocator/cidrallocator.go`


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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:85`



---


[function] name: GroupResource file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:91 returns_error: нет description: GroupResource that this evaluator tracks


### GroupResource (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:91)


GroupResource that this evaluator tracks


```go
func (p *pvcEvaluator) GroupResource(()) ()
```


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:91`



---


[function] name: Handles file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:96 returns_error: нет description: Handles returns true if the evaluator should handle the specified operation.


### Handles (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:96)


Handles returns true if the evaluator should handle the specified operation.


```go
func (p *pvcEvaluator) Handles((a admission.Attributes)) (a admission.Attributes)
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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:96`



---


[function] name: Matches file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:114 returns_error: да description: Matches returns true if the evaluator matches the specified quota with the provided input item


### Matches (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:114)


Matches returns true if the evaluator matches the specified quota with the provided input item


```go
func (p *pvcEvaluator) Matches((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:114`



---


[function] name: MatchingResources file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:163 returns_error: нет description: MatchingResources takes the input specified list of resources and returns the set of resources it matches.


### MatchingResources (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:163)


MatchingResources takes the input specified list of resources and returns the set of resources it matches.


```go
func (p *pvcEvaluator) MatchingResources((items []corev1.ResourceName)) (items []corev1.ResourceName)
```


**Тип ответа:** items


```json
{
  "path": [],
  "t": null,
  "expr": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/library/cost.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:163`



---


[function] name: MatchingScopes file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:122 returns_error: да description: MatchingScopes takes the input specified list of scopes and input object. Returns the set of scopes resource matches.


### MatchingScopes (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:122)


MatchingScopes takes the input specified list of scopes and input object. Returns the set of scopes resource matches.


```go
func (p *pvcEvaluator) MatchingScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:122`



---


[function] name: NewPersistentVolumeClaimEvaluator file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:72 returns_error: нет description: NewPersistentVolumeClaimEvaluator returns an evaluator that can evaluate persistent volume claims


### NewPersistentVolumeClaimEvaluator (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:72)


NewPersistentVolumeClaimEvaluator returns an evaluator that can evaluate persistent volume claims


```go
func NewPersistentVolumeClaimEvaluator((f quota.ListerForResourceFunc)) (f quota.ListerForResourceFunc)
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


**Тип ответа:** quota.ListerForResourceFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:72`



---


[function] name: RequiresQuotaReplenish file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:276 returns_error: нет description: RequiresQuotaReplenish enables quota monitoring for PVCs.


### RequiresQuotaReplenish (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:276)


RequiresQuotaReplenish enables quota monitoring for PVCs.


```go
func RequiresQuotaReplenish((pvc, oldPVC *corev1.PersistentVolumeClaim)) (pvc, oldPVC *corev1.PersistentVolumeClaim)
```


**Тип запроса:** corev1.PersistentVolumeClaim


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


**Тип ответа:** oldPVC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:276`



---


[function] name: UncoveredQuotaScopes file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:141 returns_error: да description: UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It 


### UncoveredQuotaScopes (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:141)


UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It returns the scopes which are in limited scopes but don't have a corresponding covering quota scope


```go
func (p *pvcEvaluator) UncoveredQuotaScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:141`



---


[function] name: Usage file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:189 returns_error: да description: Usage knows how to measure usage associated with item.


### Usage (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:189)


Usage knows how to measure usage associated with item.


```go
func (p *pvcEvaluator) Usage((corev1.ResourceList, error)) (corev1.ResourceList, error)
```


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `corev1.ResourceList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:189`



---


[function] name: UsageStats file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:250 returns_error: да description: UsageStats calculates aggregate usage for the object.


### UsageStats (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:250)


UsageStats calculates aggregate usage for the object.


```go
func (p *pvcEvaluator) UsageStats((quota.UsageStats, error)) (quota.UsageStats, error)
```


**Тип ответа:** quota.UsageStats


```json
{
  "Used": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/quota/v1/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `quota.UsageStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:250`



---


[function] name: V1ResourceByStorageClass file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:67 returns_error: нет description: V1ResourceByStorageClass returns a quota resource name by storage class.


### V1ResourceByStorageClass (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:67)


V1ResourceByStorageClass returns a quota resource name by storage class.


```go
func V1ResourceByStorageClass((storageClass string, resourceName corev1.ResourceName)) (storageClass string, resourceName corev1.ResourceName)
```


**Тип ответа:** storageClass


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/storage/v1beta1/storageclass.go`


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:67`



---


[function] name: getReferencedVolumeAttributesClassNames file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:330 returns_error: нет description: —


### getReferencedVolumeAttributesClassNames (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:330)


getReferencedVolumeAttributesClassNames is a function that performs operations based on the provided parameters and returns (pvc *corev1.PersistentVolumeClaim).


```go
func getReferencedVolumeAttributesClassNames((pvc *corev1.PersistentVolumeClaim)) (pvc *corev1.PersistentVolumeClaim)
```


**Тип запроса:** corev1.PersistentVolumeClaim


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


**Тип ответа:** corev1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:330`



---


[function] name: getStorageUsage file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:218 returns_error: нет description: —


### getStorageUsage (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:218)


getStorageUsage is a method that performs operations based on the provided parameters and returns (pvc *corev1.PersistentVolumeClaim).


```go
func (p *pvcEvaluator) getStorageUsage((pvc *corev1.PersistentVolumeClaim)) (pvc *corev1.PersistentVolumeClaim)
```


**Тип запроса:** corev1.PersistentVolumeClaim


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


**Тип ответа:** corev1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:218`



---


[function] name: pvcMatchesScopeFunc file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:293 returns_error: да description: pvcMatchesScopeFunc is a function that knows how to evaluate if a pvc matches a scope


### pvcMatchesScopeFunc (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:293)


pvcMatchesScopeFunc is a function that knows how to evaluate if a pvc matches a scope


```go
func pvcMatchesScopeFunc((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:293`



---


[function] name: pvcMatchesSelector file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:311 returns_error: да description: —


### pvcMatchesSelector (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:311)


pvcMatchesSelector is a function that performs operations based on the provided parameters and may return an error.


```go
func pvcMatchesSelector((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:311`



---


[function] name: toExternalPersistentVolumeClaimOrError file: pkg/quota/v1/evaluator/core/persistent_volume_claims.go:260 returns_error: да description: —


### toExternalPersistentVolumeClaimOrError (pkg/quota/v1/evaluator/core/persistent_volume_claims.go:260)


toExternalPersistentVolumeClaimOrError is a function that performs operations based on the provided parameters and may return an error.


```go
func toExternalPersistentVolumeClaimOrError((*corev1.PersistentVolumeClaim, error)) (*corev1.PersistentVolumeClaim, error)
```


**Тип запроса:** corev1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.PersistentVolumeClaim`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/persistent_volume_claims.go:260`




## pkg/quota/v1/evaluator/core/pods.go


📄 Исходный файл: `pkg/quota/v1/evaluator/core/pods.go`


<details open>
<summary><b>Функции в этом файле (25)</b></summary>


- 🔗 [Constraints](#constraints-pkgquotav1evaluatorcorepodsgo129) `:129`

- 🔗 [GroupResource](#groupresource-pkgquotav1evaluatorcorepodsgo174) `:174`

- 🔗 [Handles](#handles-pkgquotav1evaluatorcorepodsgo179) `:179`

- 🔗 [IsTerminating](#isterminating-pkgquotav1evaluatorcorepodsgo417) `:417`

- 🔗 [Matches](#matches-pkgquotav1evaluatorcorepodsgo203) `:203`

- 🔗 [MatchingResources](#matchingresources-pkgquotav1evaluatorcorepodsgo208) `:208`

- 🔗 [MatchingScopes](#matchingscopes-pkgquotav1evaluatorcorepodsgo225) `:225`

- 🔗 [NewPodEvaluator](#newpodevaluator-pkgquotav1evaluatorcorepodsgo113) `:113`

- 🔗 [PodUsageFunc](#podusagefunc-pkgquotav1evaluatorcorepodsgo381) `:381`

- 🔗 [QuotaV1Pod](#quotav1pod-pkgquotav1evaluatorcorepodsgo491) `:491`

- 🔗 [UncoveredQuotaScopes](#uncoveredquotascopes-pkgquotav1evaluatorcorepodsgo241) `:241`

- 🔗 [Usage](#usage-pkgquotav1evaluatorcorepodsgo260) `:260`

- 🔗 [UsageStats](#usagestats-pkgquotav1evaluatorcorepodsgo266) `:266`

- 🔗 [crossNamespacePodAffinityTerm](#crossnamespacepodaffinityterm-pkgquotav1evaluatorcorepodsgo439) `:439`

- 🔗 [crossNamespacePodAffinityTerms](#crossnamespacepodaffinityterms-pkgquotav1evaluatorcorepodsgo443) `:443`

- 🔗 [crossNamespaceWeightedPodAffinityTerms](#crossnamespaceweightedpodaffinityterms-pkgquotav1evaluatorcorepodsgo452) `:452`

- 🔗 [enforcePodContainerConstraints](#enforcepodcontainerconstraints-pkgquotav1evaluatorcorepodsgo275) `:275`

- 🔗 [isBestEffort](#isbesteffort-pkgquotav1evaluatorcorepodsgo413) `:413`

- 🔗 [isExtendedResourceNameForQuota](#isextendedresourcenameforquota-pkgquotav1evaluatorcorepodsgo86) `:86`

- 🔗 [maskResourceWithPrefix](#maskresourcewithprefix-pkgquotav1evaluatorcorepodsgo80) `:80`

- 🔗 [podComputeUsageHelper](#podcomputeusagehelper-pkgquotav1evaluatorcorepodsgo294) `:294`

- 🔗 [podMatchesScopeFunc](#podmatchesscopefunc-pkgquotav1evaluatorcorepodsgo350) `:350`

- 🔗 [podMatchesSelector](#podmatchesselector-pkgquotav1evaluatorcorepodsgo424) `:424`

- 🔗 [toExternalPodOrError](#toexternalpodorerror-pkgquotav1evaluatorcorepodsgo334) `:334`

- 🔗 [usesCrossNamespacePodAffinity](#usescrossnamespacepodaffinity-pkgquotav1evaluatorcorepodsgo461) `:461`


</details>


[function] name: Constraints file: pkg/quota/v1/evaluator/core/pods.go:129 returns_error: нет description: Constraints verifies that all required resources are present on the pod
In addition, it validates that the resources are


### Constraints (pkg/quota/v1/evaluator/core/pods.go:129)


Constraints verifies that all required resources are present on the pod
In addition, it validates that the resources are valid (i.e. requests < limits)


```go
func (p *podEvaluator) Constraints((required []corev1.ResourceName, item runtime.Object)) (required []corev1.ResourceName, item runtime.Object)
```


**Тип ответа:** required


```json
{
  "mode": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/required.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** item


```json
{
  "allocator": null,
  "serviceCIDRs": {}
}
```


*Определено в:* `pkg/registry/core/service/ipallocator/cidrallocator.go`


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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:129`



---


[function] name: GroupResource file: pkg/quota/v1/evaluator/core/pods.go:174 returns_error: нет description: GroupResource that this evaluator tracks


### GroupResource (pkg/quota/v1/evaluator/core/pods.go:174)


GroupResource that this evaluator tracks


```go
func (p *podEvaluator) GroupResource(()) ()
```


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:174`



---


[function] name: Handles file: pkg/quota/v1/evaluator/core/pods.go:179 returns_error: нет description: Handles returns true if the evaluator should handle the specified attributes.


### Handles (pkg/quota/v1/evaluator/core/pods.go:179)


Handles returns true if the evaluator should handle the specified attributes.


```go
func (p *podEvaluator) Handles((a admission.Attributes)) (a admission.Attributes)
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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:179`



---


[function] name: IsTerminating file: pkg/quota/v1/evaluator/core/pods.go:417 returns_error: нет description: —


### IsTerminating (pkg/quota/v1/evaluator/core/pods.go:417)


IsTerminating is a function that performs operations based on the provided parameters and returns (pod *corev1.Pod).


```go
func IsTerminating((pod *corev1.Pod)) (pod *corev1.Pod)
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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:417`



---


[function] name: Matches file: pkg/quota/v1/evaluator/core/pods.go:203 returns_error: да description: Matches returns true if the evaluator matches the specified quota with the provided input item


### Matches (pkg/quota/v1/evaluator/core/pods.go:203)


Matches returns true if the evaluator matches the specified quota with the provided input item


```go
func (p *podEvaluator) Matches((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:203`



---


[function] name: MatchingResources file: pkg/quota/v1/evaluator/core/pods.go:208 returns_error: нет description: MatchingResources takes the input specified list of resources and returns the set of resources it matches.


### MatchingResources (pkg/quota/v1/evaluator/core/pods.go:208)


MatchingResources takes the input specified list of resources and returns the set of resources it matches.


```go
func (p *podEvaluator) MatchingResources((input []corev1.ResourceName)) (input []corev1.ResourceName)
```


**Тип ответа:** input


```json
{
  "builder": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/client-gen/args/gvpackages.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:208`



---


[function] name: MatchingScopes file: pkg/quota/v1/evaluator/core/pods.go:225 returns_error: да description: MatchingScopes takes the input specified list of scopes and pod object. Returns the set of scope selectors pod matches.


### MatchingScopes (pkg/quota/v1/evaluator/core/pods.go:225)


MatchingScopes takes the input specified list of scopes and pod object. Returns the set of scope selectors pod matches.


```go
func (p *podEvaluator) MatchingScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:225`



---


[function] name: NewPodEvaluator file: pkg/quota/v1/evaluator/core/pods.go:113 returns_error: нет description: NewPodEvaluator returns an evaluator that can evaluate pods


### NewPodEvaluator (pkg/quota/v1/evaluator/core/pods.go:113)


NewPodEvaluator returns an evaluator that can evaluate pods


```go
func NewPodEvaluator((f quota.ListerForResourceFunc, clock clock.Clock)) (f quota.ListerForResourceFunc, clock clock.Clock)
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


**Тип ответа:** quota.ListerForResourceFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clock.Clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:113`



---


[function] name: PodUsageFunc file: pkg/quota/v1/evaluator/core/pods.go:381 returns_error: да description: PodUsageFunc returns the quota usage for a pod.
A pod is charged for quota if the following are not true.
- pod has a te


### PodUsageFunc (pkg/quota/v1/evaluator/core/pods.go:381)


PodUsageFunc returns the quota usage for a pod.
A pod is charged for quota if the following are not true.
- pod has a terminal phase (failed or succeeded)
- pod has been marked for deletion and grace period has expired


```go
func PodUsageFunc((corev1.ResourceList, error)) (corev1.ResourceList, error)
```


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `corev1.ResourceList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:381`



---


[function] name: QuotaV1Pod file: pkg/quota/v1/evaluator/core/pods.go:491 returns_error: нет description: QuotaV1Pod returns true if the pod is eligible to track against a quota
if it's not in a terminal state according to its


### QuotaV1Pod (pkg/quota/v1/evaluator/core/pods.go:491)


QuotaV1Pod returns true if the pod is eligible to track against a quota
if it's not in a terminal state according to its phase.


```go
func QuotaV1Pod((pod *corev1.Pod, clock clock.Clock)) (pod *corev1.Pod, clock clock.Clock)
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


**Тип ответа:** clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clock.Clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:491`



---


[function] name: UncoveredQuotaScopes file: pkg/quota/v1/evaluator/core/pods.go:241 returns_error: да description: UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It 


### UncoveredQuotaScopes (pkg/quota/v1/evaluator/core/pods.go:241)


UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It returns the scopes which are in limited scopes but don't have a corresponding covering quota scope


```go
func (p *podEvaluator) UncoveredQuotaScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:241`



---


[function] name: Usage file: pkg/quota/v1/evaluator/core/pods.go:260 returns_error: да description: Usage knows how to measure usage associated with pods


### Usage (pkg/quota/v1/evaluator/core/pods.go:260)


Usage knows how to measure usage associated with pods


```go
func (p *podEvaluator) Usage((corev1.ResourceList, error)) (corev1.ResourceList, error)
```


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `corev1.ResourceList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:260`



---


[function] name: UsageStats file: pkg/quota/v1/evaluator/core/pods.go:266 returns_error: да description: UsageStats calculates aggregate usage for the object.


### UsageStats (pkg/quota/v1/evaluator/core/pods.go:266)


UsageStats calculates aggregate usage for the object.


```go
func (p *podEvaluator) UsageStats((quota.UsageStats, error)) (quota.UsageStats, error)
```


**Тип ответа:** quota.UsageStats


```json
{
  "Used": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/quota/v1/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `quota.UsageStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:266`



---


[function] name: crossNamespacePodAffinityTerm file: pkg/quota/v1/evaluator/core/pods.go:439 returns_error: нет description: —


### crossNamespacePodAffinityTerm (pkg/quota/v1/evaluator/core/pods.go:439)


crossNamespacePodAffinityTerm is a function that performs operations based on the provided parameters and returns (term *corev1.PodAffinityTerm).


```go
func crossNamespacePodAffinityTerm((term *corev1.PodAffinityTerm)) (term *corev1.PodAffinityTerm)
```


**Тип запроса:** corev1.PodAffinityTerm


```json
{
  "LabelSelector": null,
  "Namespaces": [],
  "TopologyKey": "string",
  "NamespaceSelector": null,
  "MatchLabelKeys": [],
  "MismatchLabelKeys": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** term


```json
{
  "phase": "string",
  "readOnlyObserver": {},
  "lock": {},
  "readOnlyWatermark": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/maxinflight.go`


**Тип ответа:** corev1.PodAffinityTerm


```json
{
  "LabelSelector": null,
  "Namespaces": [],
  "TopologyKey": "string",
  "NamespaceSelector": null,
  "MatchLabelKeys": [],
  "MismatchLabelKeys": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:439`



---


[function] name: crossNamespacePodAffinityTerms file: pkg/quota/v1/evaluator/core/pods.go:443 returns_error: нет description: —


### crossNamespacePodAffinityTerms (pkg/quota/v1/evaluator/core/pods.go:443)


crossNamespacePodAffinityTerms is a function that performs operations based on the provided parameters and returns (terms []corev1.PodAffinityTerm).


```go
func crossNamespacePodAffinityTerms((terms []corev1.PodAffinityTerm)) (terms []corev1.PodAffinityTerm)
```


**Тип ответа:** terms


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.PodAffinityTerm


```json
{
  "LabelSelector": null,
  "Namespaces": [],
  "TopologyKey": "string",
  "NamespaceSelector": null,
  "MatchLabelKeys": [],
  "MismatchLabelKeys": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:443`



---


[function] name: crossNamespaceWeightedPodAffinityTerms file: pkg/quota/v1/evaluator/core/pods.go:452 returns_error: нет description: —


### crossNamespaceWeightedPodAffinityTerms (pkg/quota/v1/evaluator/core/pods.go:452)


crossNamespaceWeightedPodAffinityTerms is a function that performs operations based on the provided parameters and returns (terms []corev1.WeightedPodAffinityTerm).


```go
func crossNamespaceWeightedPodAffinityTerms((terms []corev1.WeightedPodAffinityTerm)) (terms []corev1.WeightedPodAffinityTerm)
```


**Тип ответа:** terms


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.WeightedPodAffinityTerm


```json
{
  "Weight": 0,
  "PodAffinityTerm": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:452`



---


[function] name: enforcePodContainerConstraints file: pkg/quota/v1/evaluator/core/pods.go:275 returns_error: нет description: enforcePodContainerConstraints checks for required resources that are not set on this container and
adds them to missing


### enforcePodContainerConstraints (pkg/quota/v1/evaluator/core/pods.go:275)


enforcePodContainerConstraints checks for required resources that are not set on this container and
adds them to missingSet.


```go
func enforcePodContainerConstraints((container *corev1.Container, requiredSet sets.String, missingSetResourceToContainerNames map[string]sets.String)) (container *corev1.Container, requiredSet sets.String, missingSetResourceToContainerNames map[string]sets.String)
```


**Тип запроса:** corev1.Container


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


**Тип ответа:** corev1.Container


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


**Тип ответа:** requiredSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.String


```json
{
  "ID": "string",
  "Secret": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/bootstraptoken/v1/types.go`


**Тип ответа:** missingSetResourceToContainerNames


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** sets.String


```json
{
  "ID": "string",
  "Secret": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/bootstraptoken/v1/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:275`



---


[function] name: isBestEffort file: pkg/quota/v1/evaluator/core/pods.go:413 returns_error: нет description: —


### isBestEffort (pkg/quota/v1/evaluator/core/pods.go:413)


isBestEffort is a function that performs operations based on the provided parameters and returns (pod *corev1.Pod).


```go
func isBestEffort((pod *corev1.Pod)) (pod *corev1.Pod)
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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:413`



---


[function] name: isExtendedResourceNameForQuota file: pkg/quota/v1/evaluator/core/pods.go:86 returns_error: нет description: isExtendedResourceNameForQuota returns true if the extended resource name
has the quota related resource prefix.


### isExtendedResourceNameForQuota (pkg/quota/v1/evaluator/core/pods.go:86)


isExtendedResourceNameForQuota returns true if the extended resource name
has the quota related resource prefix.


```go
func isExtendedResourceNameForQuota((name corev1.ResourceName)) (name corev1.ResourceName)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:86`



---


[function] name: maskResourceWithPrefix file: pkg/quota/v1/evaluator/core/pods.go:80 returns_error: нет description: maskResourceWithPrefix mask resource with certain prefix
e.g. hugepages-XXX -> requests.hugepages-XXX


### maskResourceWithPrefix (pkg/quota/v1/evaluator/core/pods.go:80)


maskResourceWithPrefix mask resource with certain prefix
e.g. hugepages-XXX -> requests.hugepages-XXX


```go
func maskResourceWithPrefix((resource corev1.ResourceName, prefix string)) (resource corev1.ResourceName, prefix string)
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


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:80`



---


[function] name: podComputeUsageHelper file: pkg/quota/v1/evaluator/core/pods.go:294 returns_error: нет description: podComputeUsageHelper can summarize the pod compute quota usage based on requests and limits


### podComputeUsageHelper (pkg/quota/v1/evaluator/core/pods.go:294)


podComputeUsageHelper can summarize the pod compute quota usage based on requests and limits


```go
func podComputeUsageHelper((requests corev1.ResourceList, limits corev1.ResourceList)) (requests corev1.ResourceList, limits corev1.ResourceList)
```


**Тип ответа:** requests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** limits


```json
{
  "minUID": 0
}
```


*Определено в:* `cmd/kubeadm/app/util/users/users_linux.go`


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:294`



---


[function] name: podMatchesScopeFunc file: pkg/quota/v1/evaluator/core/pods.go:350 returns_error: да description: podMatchesScopeFunc is a function that knows how to evaluate if a pod matches a scope


### podMatchesScopeFunc (pkg/quota/v1/evaluator/core/pods.go:350)


podMatchesScopeFunc is a function that knows how to evaluate if a pod matches a scope


```go
func podMatchesScopeFunc((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:350`



---


[function] name: podMatchesSelector file: pkg/quota/v1/evaluator/core/pods.go:424 returns_error: да description: —


### podMatchesSelector (pkg/quota/v1/evaluator/core/pods.go:424)


podMatchesSelector is a function that performs operations based on the provided parameters and may return an error.


```go
func podMatchesSelector((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:424`



---


[function] name: toExternalPodOrError file: pkg/quota/v1/evaluator/core/pods.go:334 returns_error: да description: —


### toExternalPodOrError (pkg/quota/v1/evaluator/core/pods.go:334)


toExternalPodOrError is a function that performs operations based on the provided parameters and may return an error.


```go
func toExternalPodOrError((*corev1.Pod, error)) (*corev1.Pod, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Pod`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:334`



---


[function] name: usesCrossNamespacePodAffinity file: pkg/quota/v1/evaluator/core/pods.go:461 returns_error: нет description: —


### usesCrossNamespacePodAffinity (pkg/quota/v1/evaluator/core/pods.go:461)


usesCrossNamespacePodAffinity is a function that performs operations based on the provided parameters and returns (pod *corev1.Pod).


```go
func usesCrossNamespacePodAffinity((pod *corev1.Pod)) (pod *corev1.Pod)
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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/pods.go:461`




## pkg/quota/v1/evaluator/core/registry.go


📄 Исходный файл: `pkg/quota/v1/evaluator/core/registry.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NewEvaluators](#newevaluators-pkgquotav1evaluatorcoreregistrygo46) `:46`


</details>


[function] name: NewEvaluators file: pkg/quota/v1/evaluator/core/registry.go:46 returns_error: да description: NewEvaluators returns the list of static evaluators that manage more than counts


### NewEvaluators (pkg/quota/v1/evaluator/core/registry.go:46)


NewEvaluators returns the list of static evaluators that manage more than counts


```go
func NewEvaluators(([]quota.Evaluator, error)) ([]quota.Evaluator, error)
```


**Тип ответа:** quota.Evaluator


```json
{
  "PluginName": "string",
  "Handler": {},
  "PodLister": {},
  "PdbLister": {},
  "enableAsyncPreemption": false
}
```


*Определено в:* `pkg/scheduler/framework/preemption/preemption.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]quota.Evaluator`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/registry.go:46`




## pkg/quota/v1/evaluator/core/resource_claims.go


📄 Исходный файл: `pkg/quota/v1/evaluator/core/resource_claims.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [Constraints](#constraints-pkgquotav1evaluatorcoreresource_claimsgo75) `:75`

- 🔗 [GroupResource](#groupresource-pkgquotav1evaluatorcoreresource_claimsgo81) `:81`

- 🔗 [Handles](#handles-pkgquotav1evaluatorcoreresource_claimsgo86) `:86`

- 🔗 [Matches](#matches-pkgquotav1evaluatorcoreresource_claimsgo95) `:95`

- 🔗 [MatchingResources](#matchingresources-pkgquotav1evaluatorcoreresource_claimsgo111) `:111`

- 🔗 [MatchingScopes](#matchingscopes-pkgquotav1evaluatorcoreresource_claimsgo100) `:100`

- 🔗 [NewResourceClaimEvaluator](#newresourceclaimevaluator-pkgquotav1evaluatorcoreresource_claimsgo56) `:56`

- 🔗 [UncoveredQuotaScopes](#uncoveredquotascopes-pkgquotav1evaluatorcoreresource_claimsgo106) `:106`

- 🔗 [Usage](#usage-pkgquotav1evaluatorcoreresource_claimsgo227) `:227`

- 🔗 [UsageStats](#usagestats-pkgquotav1evaluatorcoreresource_claimsgo299) `:299`

- 🔗 [V1ResourceByDeviceClass](#v1resourcebydeviceclass-pkgquotav1evaluatorcoreresource_claimsgo51) `:51`

- 🔗 [addExtendedResourceQuota](#addextendedresourcequota-pkgquotav1evaluatorcoreresource_claimsgo138) `:138`

- 🔗 [extendedResourceClaimPodUIDOwnerIndex](#extendedresourceclaimpoduidownerindex-pkgquotav1evaluatorcoreresource_claimsgo354) `:354`

- 🔗 [getVerifiedPodUsage](#getverifiedpodusage-pkgquotav1evaluatorcoreresource_claimsgo171) `:171`

- 🔗 [makeResourceClaimPodOwnerGetter](#makeresourceclaimpodownergetter-pkgquotav1evaluatorcoreresource_claimsgo329) `:329`

- 🔗 [resourceClaimPodOwnerKey](#resourceclaimpodownerkey-pkgquotav1evaluatorcoreresource_claimsgo323) `:323`

- 🔗 [toExternalResourceClaimOrError](#toexternalresourceclaimorerror-pkgquotav1evaluatorcoreresource_claimsgo306) `:306`


</details>


[function] name: Constraints file: pkg/quota/v1/evaluator/core/resource_claims.go:75 returns_error: нет description: Constraints verifies that all required resources are present on the item.


### Constraints (pkg/quota/v1/evaluator/core/resource_claims.go:75)


Constraints verifies that all required resources are present on the item.


```go
func (p *claimEvaluator) Constraints((required []corev1.ResourceName, item runtime.Object)) (required []corev1.ResourceName, item runtime.Object)
```


**Тип ответа:** required


```json
{
  "mode": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/required.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** item


```json
{
  "allocator": null,
  "serviceCIDRs": {}
}
```


*Определено в:* `pkg/registry/core/service/ipallocator/cidrallocator.go`


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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:75`



---


[function] name: GroupResource file: pkg/quota/v1/evaluator/core/resource_claims.go:81 returns_error: нет description: GroupResource that this evaluator tracks


### GroupResource (pkg/quota/v1/evaluator/core/resource_claims.go:81)


GroupResource that this evaluator tracks


```go
func (p *claimEvaluator) GroupResource(()) ()
```


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:81`



---


[function] name: Handles file: pkg/quota/v1/evaluator/core/resource_claims.go:86 returns_error: нет description: Handles returns true if the evaluator should handle the specified operation.


### Handles (pkg/quota/v1/evaluator/core/resource_claims.go:86)


Handles returns true if the evaluator should handle the specified operation.


```go
func (p *claimEvaluator) Handles((a admission.Attributes)) (a admission.Attributes)
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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:86`



---


[function] name: Matches file: pkg/quota/v1/evaluator/core/resource_claims.go:95 returns_error: да description: Matches returns true if the evaluator matches the specified quota with the provided input item


### Matches (pkg/quota/v1/evaluator/core/resource_claims.go:95)


Matches returns true if the evaluator matches the specified quota with the provided input item


```go
func (p *claimEvaluator) Matches((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:95`



---


[function] name: MatchingResources file: pkg/quota/v1/evaluator/core/resource_claims.go:111 returns_error: нет description: MatchingResources takes the input specified list of resources and returns the set of resources it matches.


### MatchingResources (pkg/quota/v1/evaluator/core/resource_claims.go:111)


MatchingResources takes the input specified list of resources and returns the set of resources it matches.


```go
func (p *claimEvaluator) MatchingResources((items []corev1.ResourceName)) (items []corev1.ResourceName)
```


**Тип ответа:** items


```json
{
  "path": [],
  "t": null,
  "expr": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/library/cost.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:111`



---


[function] name: MatchingScopes file: pkg/quota/v1/evaluator/core/resource_claims.go:100 returns_error: да description: MatchingScopes takes the input specified list of scopes and input object. Returns the set of scopes resource matches.


### MatchingScopes (pkg/quota/v1/evaluator/core/resource_claims.go:100)


MatchingScopes takes the input specified list of scopes and input object. Returns the set of scopes resource matches.


```go
func (p *claimEvaluator) MatchingScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:100`



---


[function] name: NewResourceClaimEvaluator file: pkg/quota/v1/evaluator/core/resource_claims.go:56 returns_error: нет description: NewResourceClaimEvaluator returns an evaluator that can evaluate resource claims


### NewResourceClaimEvaluator (pkg/quota/v1/evaluator/core/resource_claims.go:56)


NewResourceClaimEvaluator returns an evaluator that can evaluate resource claims


```go
func NewResourceClaimEvaluator((f quota.ListerForResourceFunc, m *extendedresourcecache.ExtendedResourceCache, podsGetter corev1listers.PodLister, claimGetter resourceClaimPodOwnerGetter)) (f quota.ListerForResourceFunc, m *extendedresourcecache.ExtendedResourceCache, podsGetter corev1listers.PodLister, claimGetter resourceClaimPodOwnerGetter)
```


**Тип запроса:** extendedresourcecache.ExtendedResourceCache


```json
{
  "logger": {},
  "handlers": [],
  "mutex": {},
  "resourceName2class": {},
  "class2ResourceName": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/deviceclass/extendedresourcecache/extendedresourcecache.go`


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


**Тип ответа:** quota.ListerForResourceFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** m


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** extendedresourcecache.ExtendedResourceCache


```json
{
  "logger": {},
  "handlers": [],
  "mutex": {},
  "resourceName2class": {},
  "class2ResourceName": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/deviceclass/extendedresourcecache/extendedresourcecache.go`


**Тип ответа:** podsGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1listers.PodLister


```json
{
  "client": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/pods.go`


**Тип ответа:** claimGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resourceClaimPodOwnerGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:56`



---


[function] name: UncoveredQuotaScopes file: pkg/quota/v1/evaluator/core/resource_claims.go:106 returns_error: да description: UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It 


### UncoveredQuotaScopes (pkg/quota/v1/evaluator/core/resource_claims.go:106)


UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It returns the scopes which are in limited scopes but don't have a corresponding covering quota scope


```go
func (p *claimEvaluator) UncoveredQuotaScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:106`



---


[function] name: Usage file: pkg/quota/v1/evaluator/core/resource_claims.go:227 returns_error: да description: Usage knows how to measure usage associated with item.


### Usage (pkg/quota/v1/evaluator/core/resource_claims.go:227)


Usage knows how to measure usage associated with item.


```go
func (p *claimEvaluator) Usage((corev1.ResourceList, error)) (corev1.ResourceList, error)
```


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `corev1.ResourceList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:227`



---


[function] name: UsageStats file: pkg/quota/v1/evaluator/core/resource_claims.go:299 returns_error: да description: UsageStats calculates aggregate usage for the object.


### UsageStats (pkg/quota/v1/evaluator/core/resource_claims.go:299)


UsageStats calculates aggregate usage for the object.


```go
func (p *claimEvaluator) UsageStats((quota.UsageStats, error)) (quota.UsageStats, error)
```


**Тип ответа:** quota.UsageStats


```json
{
  "Used": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/quota/v1/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `quota.UsageStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:299`



---


[function] name: V1ResourceByDeviceClass file: pkg/quota/v1/evaluator/core/resource_claims.go:51 returns_error: нет description: V1ResourceByDeviceClass returns a quota resource name by device class.
gpuclass -> gpuclass.deviceclass.resource.k8s.io/


### V1ResourceByDeviceClass (pkg/quota/v1/evaluator/core/resource_claims.go:51)


V1ResourceByDeviceClass returns a quota resource name by device class.
gpuclass -> gpuclass.deviceclass.resource.k8s.io/devices


```go
func V1ResourceByDeviceClass((className string)) (className string)
```


**Тип ответа:** className


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:51`



---


[function] name: addExtendedResourceQuota file: pkg/quota/v1/evaluator/core/resource_claims.go:138 returns_error: нет description: —


### addExtendedResourceQuota (pkg/quota/v1/evaluator/core/resource_claims.go:138)


addExtendedResourceQuota is a method that performs operations based on the provided parameters and returns (resourceClaimUsage map[corev1.ResourceName]resource.Quantity, podUsage corev1.ResourceList).


```go
func (p *claimEvaluator) addExtendedResourceQuota((resourceClaimUsage map[corev1.ResourceName]resource.Quantity, podUsage corev1.ResourceList)) (resourceClaimUsage map[corev1.ResourceName]resource.Quantity, podUsage corev1.ResourceList)
```


**Тип ответа:** resourceClaimUsage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** corev1.ResourceName


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


**Тип ответа:** podUsage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:138`



---


[function] name: extendedResourceClaimPodUIDOwnerIndex file: pkg/quota/v1/evaluator/core/resource_claims.go:354 returns_error: да description: —


### extendedResourceClaimPodUIDOwnerIndex (pkg/quota/v1/evaluator/core/resource_claims.go:354)


extendedResourceClaimPodUIDOwnerIndex is a function that performs operations based on the provided parameters and may return an error.


```go
func extendedResourceClaimPodUIDOwnerIndex(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:354`



---


[function] name: getVerifiedPodUsage file: pkg/quota/v1/evaluator/core/resource_claims.go:171 returns_error: нет description: Verify extended resource claim owning pod exists, and the pod's ExtendedResourceClaimStatus points
back to the claim if 


### getVerifiedPodUsage (pkg/quota/v1/evaluator/core/resource_claims.go:171)


Verify extended resource claim owning pod exists, and the pod's ExtendedResourceClaimStatus points
back to the claim if it's not nil, and returns the pod's quota usage. If any error is encountered, nil is returned.


```go
func (p *claimEvaluator) getVerifiedPodUsage((claim *resourceapi.ResourceClaim)) (claim *resourceapi.ResourceClaim)
```


**Тип запроса:** resourceapi.ResourceClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** claim


```json
{
  "ctx": {},
  "claim": "string",
  "audiences": {},
  "client": null,
  "config": null,
  "verifierPerIssuer": {},
  "m": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** resourceapi.ResourceClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:171`



---


[function] name: makeResourceClaimPodOwnerGetter file: pkg/quota/v1/evaluator/core/resource_claims.go:329 returns_error: да description: —


### makeResourceClaimPodOwnerGetter (pkg/quota/v1/evaluator/core/resource_claims.go:329)


makeResourceClaimPodOwnerGetter is a function that performs operations based on the provided parameters and may return an error.


```go
func makeResourceClaimPodOwnerGetter((resourceClaimPodOwnerGetter, error)) (resourceClaimPodOwnerGetter, error)
```


**Тип ответа:** resourceClaimPodOwnerGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `resourceClaimPodOwnerGetter`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:329`



---


[function] name: resourceClaimPodOwnerKey file: pkg/quota/v1/evaluator/core/resource_claims.go:323 returns_error: нет description: —


### resourceClaimPodOwnerKey (pkg/quota/v1/evaluator/core/resource_claims.go:323)


resourceClaimPodOwnerKey is a function that performs operations based on the provided parameters and returns (namespace string, podUID types.UID).


```go
func resourceClaimPodOwnerKey((namespace string, podUID types.UID)) (namespace string, podUID types.UID)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podUID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.UID


```json
{
  "key": "string"
}
```


*Определено в:* `pkg/controller/controller_utils.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:323`



---


[function] name: toExternalResourceClaimOrError file: pkg/quota/v1/evaluator/core/resource_claims.go:306 returns_error: да description: —


### toExternalResourceClaimOrError (pkg/quota/v1/evaluator/core/resource_claims.go:306)


toExternalResourceClaimOrError is a function that performs operations based on the provided parameters and may return an error.


```go
func toExternalResourceClaimOrError((*resourceapi.ResourceClaim, error)) (*resourceapi.ResourceClaim, error)
```


**Тип запроса:** resourceapi.ResourceClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** resourceapi.ResourceClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*resourceapi.ResourceClaim`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/resource_claims.go:306`




## pkg/quota/v1/evaluator/core/services.go


📄 Исходный файл: `pkg/quota/v1/evaluator/core/services.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [Constraints](#constraints-pkgquotav1evaluatorcoreservicesgo58) `:58`

- 🔗 [GetQuotaServiceType](#getquotaservicetype-pkgquotav1evaluatorcoreservicesgo168) `:168`

- 🔗 [GroupResource](#groupresource-pkgquotav1evaluatorcoreservicesgo64) `:64`

- 🔗 [Handles](#handles-pkgquotav1evaluatorcoreservicesgo69) `:69`

- 🔗 [Matches](#matches-pkgquotav1evaluatorcoreservicesgo79) `:79`

- 🔗 [MatchingResources](#matchingresources-pkgquotav1evaluatorcoreservicesgo84) `:84`

- 🔗 [MatchingScopes](#matchingscopes-pkgquotav1evaluatorcoreservicesgo89) `:89`

- 🔗 [NewServiceEvaluator](#newserviceevaluator-pkgquotav1evaluatorcoreservicesgo45) `:45`

- 🔗 [UncoveredQuotaScopes](#uncoveredquotascopes-pkgquotav1evaluatorcoreservicesgo95) `:95`

- 🔗 [Usage](#usage-pkgquotav1evaluatorcoreservicesgo116) `:116`

- 🔗 [UsageStats](#usagestats-pkgquotav1evaluatorcoreservicesgo161) `:161`

- 🔗 [portsWithNodePorts](#portswithnodeports-pkgquotav1evaluatorcoreservicesgo150) `:150`

- 🔗 [toExternalServiceOrError](#toexternalserviceorerror-pkgquotav1evaluatorcoreservicesgo100) `:100`


</details>


[function] name: Constraints file: pkg/quota/v1/evaluator/core/services.go:58 returns_error: нет description: Constraints verifies that all required resources are present on the item


### Constraints (pkg/quota/v1/evaluator/core/services.go:58)


Constraints verifies that all required resources are present on the item


```go
func (p *serviceEvaluator) Constraints((required []corev1.ResourceName, item runtime.Object)) (required []corev1.ResourceName, item runtime.Object)
```


**Тип ответа:** required


```json
{
  "mode": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/required.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** item


```json
{
  "allocator": null,
  "serviceCIDRs": {}
}
```


*Определено в:* `pkg/registry/core/service/ipallocator/cidrallocator.go`


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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:58`



---


[function] name: GetQuotaServiceType file: pkg/quota/v1/evaluator/core/services.go:168 returns_error: нет description: GetQuotaServiceType returns ServiceType if the service type is eligible to track against a quota, nor return ""


### GetQuotaServiceType (pkg/quota/v1/evaluator/core/services.go:168)


GetQuotaServiceType returns ServiceType if the service type is eligible to track against a quota, nor return ""


```go
func GetQuotaServiceType((service *corev1.Service)) (service *corev1.Service)
```


**Тип запроса:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:168`



---


[function] name: GroupResource file: pkg/quota/v1/evaluator/core/services.go:64 returns_error: нет description: GroupResource that this evaluator tracks


### GroupResource (pkg/quota/v1/evaluator/core/services.go:64)


GroupResource that this evaluator tracks


```go
func (p *serviceEvaluator) GroupResource(()) ()
```


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:64`



---


[function] name: Handles file: pkg/quota/v1/evaluator/core/services.go:69 returns_error: нет description: Handles returns true of the evaluator should handle the specified operation.


### Handles (pkg/quota/v1/evaluator/core/services.go:69)


Handles returns true of the evaluator should handle the specified operation.


```go
func (p *serviceEvaluator) Handles((a admission.Attributes)) (a admission.Attributes)
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


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:69`



---


[function] name: Matches file: pkg/quota/v1/evaluator/core/services.go:79 returns_error: да description: Matches returns true if the evaluator matches the specified quota with the provided input item


### Matches (pkg/quota/v1/evaluator/core/services.go:79)


Matches returns true if the evaluator matches the specified quota with the provided input item


```go
func (p *serviceEvaluator) Matches((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:79`



---


[function] name: MatchingResources file: pkg/quota/v1/evaluator/core/services.go:84 returns_error: нет description: MatchingResources takes the input specified list of resources and returns the set of resources it matches.


### MatchingResources (pkg/quota/v1/evaluator/core/services.go:84)


MatchingResources takes the input specified list of resources and returns the set of resources it matches.


```go
func (p *serviceEvaluator) MatchingResources((input []corev1.ResourceName)) (input []corev1.ResourceName)
```


**Тип ответа:** input


```json
{
  "builder": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/client-gen/args/gvpackages.go`


**Тип ответа:** corev1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:84`



---


[function] name: MatchingScopes file: pkg/quota/v1/evaluator/core/services.go:89 returns_error: да description: MatchingScopes takes the input specified list of scopes and input object. Returns the set of scopes resource matches.


### MatchingScopes (pkg/quota/v1/evaluator/core/services.go:89)


MatchingScopes takes the input specified list of scopes and input object. Returns the set of scopes resource matches.


```go
func (p *serviceEvaluator) MatchingScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:89`



---


[function] name: NewServiceEvaluator file: pkg/quota/v1/evaluator/core/services.go:45 returns_error: нет description: NewServiceEvaluator returns an evaluator that can evaluate services.


### NewServiceEvaluator (pkg/quota/v1/evaluator/core/services.go:45)


NewServiceEvaluator returns an evaluator that can evaluate services.


```go
func NewServiceEvaluator((f quota.ListerForResourceFunc)) (f quota.ListerForResourceFunc)
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


**Тип ответа:** quota.ListerForResourceFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:45`



---


[function] name: UncoveredQuotaScopes file: pkg/quota/v1/evaluator/core/services.go:95 returns_error: да description: UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It 


### UncoveredQuotaScopes (pkg/quota/v1/evaluator/core/services.go:95)


UncoveredQuotaScopes takes the input matched scopes which are limited by configuration and the matched quota scopes.
It returns the scopes which are in limited scopes but don't have a corresponding covering quota scope


```go
func (p *serviceEvaluator) UncoveredQuotaScopes(([]corev1.ScopedResourceSelectorRequirement, error)) ([]corev1.ScopedResourceSelectorRequirement, error)
```


**Тип ответа:** corev1.ScopedResourceSelectorRequirement


```json
{
  "ScopeName": {},
  "Operator": {},
  "Values": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]corev1.ScopedResourceSelectorRequirement`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:95`



---


[function] name: Usage file: pkg/quota/v1/evaluator/core/services.go:116 returns_error: да description: Usage knows how to measure usage associated with services


### Usage (pkg/quota/v1/evaluator/core/services.go:116)


Usage knows how to measure usage associated with services


```go
func (p *serviceEvaluator) Usage((corev1.ResourceList, error)) (corev1.ResourceList, error)
```


**Тип ответа:** corev1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `corev1.ResourceList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:116`



---


[function] name: UsageStats file: pkg/quota/v1/evaluator/core/services.go:161 returns_error: да description: UsageStats calculates aggregate usage for the object.


### UsageStats (pkg/quota/v1/evaluator/core/services.go:161)


UsageStats calculates aggregate usage for the object.


```go
func (p *serviceEvaluator) UsageStats((quota.UsageStats, error)) (quota.UsageStats, error)
```


**Тип ответа:** quota.UsageStats


```json
{
  "Used": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/quota/v1/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `quota.UsageStats`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:161`



---


[function] name: portsWithNodePorts file: pkg/quota/v1/evaluator/core/services.go:150 returns_error: нет description: —


### portsWithNodePorts (pkg/quota/v1/evaluator/core/services.go:150)


portsWithNodePorts is a function that performs operations based on the provided parameters and returns (svc *corev1.Service).


```go
func portsWithNodePorts((svc *corev1.Service)) (svc *corev1.Service)
```


**Тип запроса:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:150`



---


[function] name: toExternalServiceOrError file: pkg/quota/v1/evaluator/core/services.go:100 returns_error: да description: convert the input object to an internal service object or error.


### toExternalServiceOrError (pkg/quota/v1/evaluator/core/services.go:100)


convert the input object to an internal service object or error.


```go
func toExternalServiceOrError((*corev1.Service, error)) (*corev1.Service, error)
```


**Тип запроса:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** corev1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Service`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/evaluator/core/services.go:100`




## pkg/quota/v1/install/registry.go


📄 Исходный файл: `pkg/quota/v1/install/registry.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DefaultIgnoredResources](#defaultignoredresources-pkgquotav1installregistrygo72) `:72`

- 🔗 [NewQuotaConfigurationForAdmission](#newquotaconfigurationforadmission-pkgquotav1installregistrygo32) `:32`

- 🔗 [NewQuotaConfigurationForControllers](#newquotaconfigurationforcontrollers-pkgquotav1installregistrygo45) `:45`


</details>


[function] name: DefaultIgnoredResources file: pkg/quota/v1/install/registry.go:72 returns_error: нет description: DefaultIgnoredResources returns the default set of resources that quota system
should ignore. This is exposed so downstr


### DefaultIgnoredResources (pkg/quota/v1/install/registry.go:72)


DefaultIgnoredResources returns the default set of resources that quota system
should ignore. This is exposed so downstream integrators can have access to them.


```go
func DefaultIgnoredResources(()) ()
```


📍 *Расположение:* `pkg/quota/v1/install/registry.go:72`



---


[function] name: NewQuotaConfigurationForAdmission file: pkg/quota/v1/install/registry.go:32 returns_error: да description: NewQuotaConfigurationForAdmission returns a quota configuration for admission control.


### NewQuotaConfigurationForAdmission (pkg/quota/v1/install/registry.go:32)


NewQuotaConfigurationForAdmission returns a quota configuration for admission control.


```go
func NewQuotaConfigurationForAdmission((quota.Configuration, error)) (quota.Configuration, error)
```


**Тип ответа:** quota.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `quota.Configuration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/install/registry.go:32`



---


[function] name: NewQuotaConfigurationForControllers file: pkg/quota/v1/install/registry.go:45 returns_error: да description: NewQuotaConfigurationForControllers returns a quota configuration for controllers.


### NewQuotaConfigurationForControllers (pkg/quota/v1/install/registry.go:45)


NewQuotaConfigurationForControllers returns a quota configuration for controllers.


```go
func NewQuotaConfigurationForControllers((quota.Configuration, error)) (quota.Configuration, error)
```


**Тип ответа:** quota.Configuration


```json
{
  "Default": [],
  "Whitelist": []
}
```


*Определено в:* `plugin/pkg/admission/podtolerationrestriction/apis/podtolerationrestriction/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `quota.Configuration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/quota/v1/install/registry.go:45`




## pkg/quota/v1/install/update_filter.go


📄 Исходный файл: `pkg/quota/v1/install/update_filter.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [DefaultUpdateFilter](#defaultupdatefilter-pkgquotav1installupdate_filtergo31) `:31`

- 🔗 [hasResourcesChanged](#hasresourceschanged-pkgquotav1installupdate_filtergo63) `:63`


</details>


[function] name: DefaultUpdateFilter file: pkg/quota/v1/install/update_filter.go:31 returns_error: нет description: DefaultUpdateFilter returns the default update filter for resource update events for consideration for quota.


### DefaultUpdateFilter (pkg/quota/v1/install/update_filter.go:31)


DefaultUpdateFilter returns the default update filter for resource update events for consideration for quota.


```go
func DefaultUpdateFilter(()) ()
```


📍 *Расположение:* `pkg/quota/v1/install/update_filter.go:31`



---


[function] name: hasResourcesChanged file: pkg/quota/v1/install/update_filter.go:63 returns_error: нет description: hasResourcesChanged function to compare resources in container statuses


### hasResourcesChanged (pkg/quota/v1/install/update_filter.go:63)


hasResourcesChanged function to compare resources in container statuses


```go
func hasResourcesChanged((oldPod *v1.Pod, newPod *v1.Pod)) (oldPod *v1.Pod, newPod *v1.Pod)
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


**Тип ответа:** oldPod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** newPod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/quota/v1/install/update_filter.go:63`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_proxy.md)

- [Следующая директория](pkg_registry.md)


---

