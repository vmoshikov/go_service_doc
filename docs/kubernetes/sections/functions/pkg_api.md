---
title: "Функции: pkg/api"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/api
---


# Функции: pkg/api


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](hack_tools.md)

- [Следующая директория](pkg_apis.md)


---


## Меню по файлам


- 📄 [pkg/api/endpoints/testing/make.go](#pkgapiendpointstestingmakego)

- 📄 [pkg/api/job/warnings.go](#pkgapijobwarningsgo)

- 📄 [pkg/api/node/util.go](#pkgapinodeutilgo)

- 📄 [pkg/api/persistentvolume/util.go](#pkgapipersistentvolumeutilgo)

- 📄 [pkg/api/persistentvolumeclaim/util.go](#pkgapipersistentvolumeclaimutilgo)

- 📄 [pkg/api/pod/testing/make.go](#pkgapipodtestingmakego)

- 📄 [pkg/api/pod/util.go](#pkgapipodutilgo)

- 📄 [pkg/api/pod/warnings.go](#pkgapipodwarningsgo)

- 📄 [pkg/api/resourceclaimspec/util.go](#pkgapiresourceclaimspecutilgo)

- 📄 [pkg/api/service/testing/make.go](#pkgapiservicetestingmakego)

- 📄 [pkg/api/service/util.go](#pkgapiserviceutilgo)

- 📄 [pkg/api/service/warnings.go](#pkgapiservicewarningsgo)

- 📄 [pkg/api/servicecidr/servicecidr.go](#pkgapiservicecidrservicecidrgo)

- 📄 [pkg/api/storage/util.go](#pkgapistorageutilgo)

- 📄 [pkg/api/testing/compat/compatibility_tester.go](#pkgapitestingcompatcompatibility_testergo)

- 📄 [pkg/api/testing/conversion.go](#pkgapitestingconversiongo)

- 📄 [pkg/api/testing/fuzzer.go](#pkgapitestingfuzzergo)

- 📄 [pkg/api/testing/validation.go](#pkgapitestingvalidationgo)

- 📄 [pkg/api/v1/endpoints/util.go](#pkgapiv1endpointsutilgo)

- 📄 [pkg/api/v1/persistentvolume/util.go](#pkgapiv1persistentvolumeutilgo)

- 📄 [pkg/api/v1/pod/util.go](#pkgapiv1podutilgo)

- 📄 [pkg/api/v1/resource/helpers.go](#pkgapiv1resourcehelpersgo)

- 📄 [pkg/api/v1/service/util.go](#pkgapiv1serviceutilgo)


---


## pkg/api/endpoints/testing/make.go


📄 Исходный файл: `pkg/api/endpoints/testing/make.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MakeEndpointAddress](#makeendpointaddress-pkgapiendpointstestingmakego53) `:53`

- 🔗 [MakeEndpointPort](#makeendpointport-pkgapiendpointstestingmakego65) `:65`

- 🔗 [MakeEndpoints](#makeendpoints-pkgapiendpointstestingmakego30) `:30`


</details>


[function] name: MakeEndpointAddress file: pkg/api/endpoints/testing/make.go:53 returns_error: нет description: MakeEndpointAddress helps construct EndpointAddress objects which pass API
validation.


### MakeEndpointAddress (pkg/api/endpoints/testing/make.go:53)


MakeEndpointAddress helps construct EndpointAddress objects which pass API
validation.


```go
func MakeEndpointAddress((ip string, pod string)) (ip string, pod string)
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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


📍 *Расположение:* `pkg/api/endpoints/testing/make.go:53`



---


[function] name: MakeEndpointPort file: pkg/api/endpoints/testing/make.go:65 returns_error: нет description: MakeEndpointPort helps construct EndpointPort objects which pass API
validation.


### MakeEndpointPort (pkg/api/endpoints/testing/make.go:65)


MakeEndpointPort helps construct EndpointPort objects which pass API
validation.


```go
func MakeEndpointPort((name string, port int)) (name string, port int)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** port


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `pkg/api/endpoints/testing/make.go:65`



---


[function] name: MakeEndpoints file: pkg/api/endpoints/testing/make.go:30 returns_error: нет description: MakeEndpoints helps construct Endpoints objects (which pass API validation)
more legibly and tersely than a Go struct de


### MakeEndpoints (pkg/api/endpoints/testing/make.go:30)


MakeEndpoints helps construct Endpoints objects (which pass API validation)
more legibly and tersely than a Go struct definition.


```go
func MakeEndpoints((name string, addrs []api.EndpointAddress, ports []api.EndpointPort, tweaks ...Tweak)) (name string, addrs []api.EndpointAddress, ports []api.EndpointPort, tweaks ...Tweak)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** addrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** ports


```json
{
  "Verbs": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/discovery/helper.go`


**Тип ответа:** api.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** tweaks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Tweak


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/endpoints/testing/make.go:30`




## pkg/api/job/warnings.go


📄 Исходный файл: `pkg/api/job/warnings.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [WarningsForJobSpec](#warningsforjobspec-pkgapijobwarningsgo36) `:36`


</details>


[function] name: WarningsForJobSpec file: pkg/api/job/warnings.go:36 returns_error: нет description: WarningsForJobSpec produces warnings for fields in the JobSpec.


### WarningsForJobSpec (pkg/api/job/warnings.go:36)


WarningsForJobSpec produces warnings for fields in the JobSpec.


```go
func WarningsForJobSpec((ctx context.Context, path *field.Path, spec, oldSpec *batch.JobSpec)) (ctx context.Context, path *field.Path, spec, oldSpec *batch.JobSpec)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип запроса:** batch.JobSpec


```json
{
  "Parallelism": 0,
  "Completions": 0,
  "PodFailurePolicy": null,
  "SuccessPolicy": null,
  "ActiveDeadlineSeconds": 0,
  "BackoffLimit": 0,
  "BackoffLimitPerIndex": 0,
  "MaxFailedIndexes": 0,
  "Selector": null,
  "ManualSelector": false,
  "Template": {},
  "TTLSecondsAfterFinished": 0,
  "CompletionMode": null,
  "Suspend": false,
  "PodReplacementPolicy": null,
  "ManagedBy": "string"
}
```


*Определено в:* `pkg/apis/batch/types.go`


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


**Тип ответа:** path


```json
{
  "muxName": "string",
  "pathToHandler": {},
  "prefixHandlers": [],
  "notFoundHandler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** oldSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** batch.JobSpec


```json
{
  "Parallelism": 0,
  "Completions": 0,
  "PodFailurePolicy": null,
  "SuccessPolicy": null,
  "ActiveDeadlineSeconds": 0,
  "BackoffLimit": 0,
  "BackoffLimitPerIndex": 0,
  "MaxFailedIndexes": 0,
  "Selector": null,
  "ManualSelector": false,
  "Template": {},
  "TTLSecondsAfterFinished": 0,
  "CompletionMode": null,
  "Suspend": false,
  "PodReplacementPolicy": null,
  "ManagedBy": "string"
}
```


*Определено в:* `pkg/apis/batch/types.go`


📍 *Расположение:* `pkg/api/job/warnings.go:36`




## pkg/api/node/util.go


📄 Исходный файл: `pkg/api/node/util.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetNodeLabelDeprecatedMessage](#getnodelabeldeprecatedmessage-pkgapinodeutilgo42) `:42`

- 🔗 [GetWarningsForNodeSelector](#getwarningsfornodeselector-pkgapinodeutilgo64) `:64`

- 🔗 [GetWarningsForNodeSelectorTerm](#getwarningsfornodeselectorterm-pkgapinodeutilgo95) `:95`

- 🔗 [GetWarningsForRuntimeClass](#getwarningsforruntimeclass-pkgapinodeutilgo47) `:47`


</details>


[function] name: GetNodeLabelDeprecatedMessage file: pkg/api/node/util.go:42 returns_error: нет description: GetNodeLabelDeprecatedMessage returns the message for the deprecated node label
and a bool indicating if the label is de


### GetNodeLabelDeprecatedMessage (pkg/api/node/util.go:42)


GetNodeLabelDeprecatedMessage returns the message for the deprecated node label
and a bool indicating if the label is deprecated.


```go
func GetNodeLabelDeprecatedMessage((string, bool)) (string, bool)
```


📍 *Расположение:* `pkg/api/node/util.go:42`



---


[function] name: GetWarningsForNodeSelector file: pkg/api/node/util.go:64 returns_error: нет description: GetWarningsForNodeSelector tests if any of the node selector requirements in the template is deprecated.
If there are de


### GetWarningsForNodeSelector (pkg/api/node/util.go:64)


GetWarningsForNodeSelector tests if any of the node selector requirements in the template is deprecated.
If there are deprecated node selector requirements in either match expressions or match labels, a warning is returned.


```go
func GetWarningsForNodeSelector((nodeSelector *metav1.LabelSelector, fieldPath *field.Path)) (nodeSelector *metav1.LabelSelector, fieldPath *field.Path)
```


**Тип запроса:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** nodeSelector


```json
{
  "matchLabels": {},
  "matchFields": {},
  "parseErrs": []
}
```


*Определено в:* `staging/src/k8s.io/component-helpers/scheduling/corev1/nodeaffinity/nodeaffinity.go`


**Тип ответа:** metav1.LabelSelector


```json
{
  "matchLabels": {},
  "matchExpressions": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


📍 *Расположение:* `pkg/api/node/util.go:64`



---


[function] name: GetWarningsForNodeSelectorTerm file: pkg/api/node/util.go:95 returns_error: нет description: GetWarningsForNodeSelectorTerm checks match expressions of node selector term


### GetWarningsForNodeSelectorTerm (pkg/api/node/util.go:95)


GetWarningsForNodeSelectorTerm checks match expressions of node selector term


```go
func GetWarningsForNodeSelectorTerm((nodeSelectorTerm api.NodeSelectorTerm, checkLabelValue bool, fieldPath *field.Path)) (nodeSelectorTerm api.NodeSelectorTerm, checkLabelValue bool, fieldPath *field.Path)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** nodeSelectorTerm


```json
{
  "matchLabels": {},
  "matchFields": {},
  "parseErrs": []
}
```


*Определено в:* `staging/src/k8s.io/component-helpers/scheduling/corev1/nodeaffinity/nodeaffinity.go`


**Тип ответа:** api.NodeSelectorTerm


```json
{
  "MatchExpressions": [],
  "MatchFields": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** checkLabelValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


📍 *Расположение:* `pkg/api/node/util.go:95`



---


[function] name: GetWarningsForRuntimeClass file: pkg/api/node/util.go:47 returns_error: нет description: —


### GetWarningsForRuntimeClass (pkg/api/node/util.go:47)


GetWarningsForRuntimeClass is a function that retrieves data based on the provided parameters and returns (rc *node.RuntimeClass).


```go
func GetWarningsForRuntimeClass((rc *node.RuntimeClass)) (rc *node.RuntimeClass)
```


**Тип запроса:** node.RuntimeClass


```json
{
  "Handler": "string",
  "Overhead": null,
  "Scheduling": null
}
```


*Определено в:* `pkg/apis/node/types.go`


**Тип ответа:** rc


```json
{
  "Printer": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/output/output.go`


**Тип ответа:** node.RuntimeClass


```json
{
  "Handler": "string",
  "Overhead": null,
  "Scheduling": null
}
```


*Определено в:* `pkg/apis/node/types.go`


📍 *Расположение:* `pkg/api/node/util.go:47`




## pkg/api/persistentvolume/util.go


📄 Исходный файл: `pkg/api/persistentvolume/util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DropDisabledSpecFields](#dropdisabledspecfields-pkgapipersistentvolumeutilgo32) `:32`

- 🔗 [GetWarningsForPersistentVolume](#getwarningsforpersistentvolume-pkgapipersistentvolumeutilgo40) `:40`

- 🔗 [warningsForPersistentVolumeSpecAndMeta](#warningsforpersistentvolumespecandmeta-pkgapipersistentvolumeutilgo61) `:61`


</details>


[function] name: DropDisabledSpecFields file: pkg/api/persistentvolume/util.go:32 returns_error: нет description: DropDisabledSpecFields removes disabled fields from the pv spec.
This should be called from PrepareForCreate/PrepareForU


### DropDisabledSpecFields (pkg/api/persistentvolume/util.go:32)


DropDisabledSpecFields removes disabled fields from the pv spec.
This should be called from PrepareForCreate/PrepareForUpdate for all resources containing a pv spec.


```go
func DropDisabledSpecFields((pvSpec *api.PersistentVolumeSpec, oldPVSpec *api.PersistentVolumeSpec)) (pvSpec *api.PersistentVolumeSpec, oldPVSpec *api.PersistentVolumeSpec)
```


**Тип запроса:** api.PersistentVolumeSpec


```json
{
  "Capacity": {},
  "AccessModes": [],
  "ClaimRef": null,
  "PersistentVolumeReclaimPolicy": {},
  "StorageClassName": "string",
  "MountOptions": [],
  "VolumeMode": null,
  "NodeAffinity": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.PersistentVolumeSpec


```json
{
  "Capacity": {},
  "AccessModes": [],
  "ClaimRef": null,
  "PersistentVolumeReclaimPolicy": {},
  "StorageClassName": "string",
  "MountOptions": [],
  "VolumeMode": null,
  "NodeAffinity": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PersistentVolumeSpec


```json
{
  "Capacity": {},
  "AccessModes": [],
  "ClaimRef": null,
  "PersistentVolumeReclaimPolicy": {},
  "StorageClassName": "string",
  "MountOptions": [],
  "VolumeMode": null,
  "NodeAffinity": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPVSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PersistentVolumeSpec


```json
{
  "Capacity": {},
  "AccessModes": [],
  "ClaimRef": null,
  "PersistentVolumeReclaimPolicy": {},
  "StorageClassName": "string",
  "MountOptions": [],
  "VolumeMode": null,
  "NodeAffinity": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolume/util.go:32`



---


[function] name: GetWarningsForPersistentVolume file: pkg/api/persistentvolume/util.go:40 returns_error: нет description: —


### GetWarningsForPersistentVolume (pkg/api/persistentvolume/util.go:40)


GetWarningsForPersistentVolume is a function that retrieves data based on the provided parameters and returns (pv *api.PersistentVolume).


```go
func GetWarningsForPersistentVolume((pv *api.PersistentVolume)) (pv *api.PersistentVolume)
```


**Тип запроса:** api.PersistentVolume


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


**Тип ответа:** api.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolume/util.go:40`



---


[function] name: warningsForPersistentVolumeSpecAndMeta file: pkg/api/persistentvolume/util.go:61 returns_error: нет description: —


### warningsForPersistentVolumeSpecAndMeta (pkg/api/persistentvolume/util.go:61)


warningsForPersistentVolumeSpecAndMeta is a function that performs operations based on the provided parameters and returns (fieldPath *field.Path, pvSpec *api.PersistentVolumeSpec, pvMeta *metav1.ObjectMeta).


```go
func warningsForPersistentVolumeSpecAndMeta((fieldPath *field.Path, pvSpec *api.PersistentVolumeSpec, pvMeta *metav1.ObjectMeta)) (fieldPath *field.Path, pvSpec *api.PersistentVolumeSpec, pvMeta *metav1.ObjectMeta)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип запроса:** api.PersistentVolumeSpec


```json
{
  "Capacity": {},
  "AccessModes": [],
  "ClaimRef": null,
  "PersistentVolumeReclaimPolicy": {},
  "StorageClassName": "string",
  "MountOptions": [],
  "VolumeMode": null,
  "NodeAffinity": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** pvSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PersistentVolumeSpec


```json
{
  "Capacity": {},
  "AccessModes": [],
  "ClaimRef": null,
  "PersistentVolumeReclaimPolicy": {},
  "StorageClassName": "string",
  "MountOptions": [],
  "VolumeMode": null,
  "NodeAffinity": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvMeta


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/api/persistentvolume/util.go:61`




## pkg/api/persistentvolumeclaim/util.go


📄 Исходный файл: `pkg/api/persistentvolumeclaim/util.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [DropDisabledFields](#dropdisabledfields-pkgapipersistentvolumeclaimutilgo37) `:37`

- 🔗 [DropDisabledFieldsFromStatus](#dropdisabledfieldsfromstatus-pkgapipersistentvolumeclaimutilgo101) `:101`

- 🔗 [EnforceDataSourceBackwardsCompatibility](#enforcedatasourcebackwardscompatibility-pkgapipersistentvolumeclaimutilgo76) `:76`

- 🔗 [GetWarningsForPersistentVolumeClaim](#getwarningsforpersistentvolumeclaim-pkgapipersistentvolumeclaimutilgo192) `:192`

- 🔗 [GetWarningsForPersistentVolumeClaimSpec](#getwarningsforpersistentvolumeclaimspec-pkgapipersistentvolumeclaimutilgo214) `:214`

- 🔗 [NormalizeDataSources](#normalizedatasources-pkgapipersistentvolumeclaimutilgo162) `:162`

- 🔗 [dataSourceInUse](#datasourceinuse-pkgapipersistentvolumeclaimutilgo121) `:121`

- 🔗 [dataSourceIsPvcOrSnapshot](#datasourceispvcorsnapshot-pkgapipersistentvolumeclaimutilgo131) `:131`

- 🔗 [dataSourceRefInUse](#datasourcerefinuse-pkgapipersistentvolumeclaimutilgo149) `:149`


</details>


[function] name: DropDisabledFields file: pkg/api/persistentvolumeclaim/util.go:37 returns_error: нет description: DropDisabledFields removes disabled fields from the pvc spec.
This should be called from PrepareForCreate/PrepareForUpda


### DropDisabledFields (pkg/api/persistentvolumeclaim/util.go:37)


DropDisabledFields removes disabled fields from the pvc spec.
This should be called from PrepareForCreate/PrepareForUpdate for all resources containing a pvc spec.


```go
func DropDisabledFields((pvcSpec, oldPVCSpec *core.PersistentVolumeClaimSpec)) (pvcSpec, oldPVCSpec *core.PersistentVolumeClaimSpec)
```


**Тип запроса:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvcSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPVCSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:37`



---


[function] name: DropDisabledFieldsFromStatus file: pkg/api/persistentvolumeclaim/util.go:101 returns_error: нет description: —


### DropDisabledFieldsFromStatus (pkg/api/persistentvolumeclaim/util.go:101)


DropDisabledFieldsFromStatus is a function that performs operations based on the provided parameters and returns (pvc, oldPVC *core.PersistentVolumeClaim).


```go
func DropDisabledFieldsFromStatus((pvc, oldPVC *core.PersistentVolumeClaim)) (pvc, oldPVC *core.PersistentVolumeClaim)
```


**Тип запроса:** core.PersistentVolumeClaim


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


**Тип ответа:** core.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:101`



---


[function] name: EnforceDataSourceBackwardsCompatibility file: pkg/api/persistentvolumeclaim/util.go:76 returns_error: нет description: EnforceDataSourceBackwardsCompatibility drops the data source field under certain conditions
to maintain backwards compa


### EnforceDataSourceBackwardsCompatibility (pkg/api/persistentvolumeclaim/util.go:76)


EnforceDataSourceBackwardsCompatibility drops the data source field under certain conditions
to maintain backwards compatibility with old behavior.
See KEP 1495 for details.
Specifically, if this is an update of a PVC with no data source, or a creation of a new PVC,
and the dataSourceRef field is not filled in, then we will drop "invalid" data sources
(anything other than a PVC or a VolumeSnapshot) from this request as if an empty PVC had
been requested.
This should be called after DropDisabledFields so that if the AnyVolumeDataSource feature
gate is disabled, dataSourceRef will be forced to empty, ensuring pre-1.22 behavior.
This should be called before NormalizeDataSources, so that data sources other than PVCs
and VolumeSnapshots can only be set through the dataSourceRef field and not the dataSource
field.


```go
func EnforceDataSourceBackwardsCompatibility((pvcSpec, oldPVCSpec *core.PersistentVolumeClaimSpec)) (pvcSpec, oldPVCSpec *core.PersistentVolumeClaimSpec)
```


**Тип запроса:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvcSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPVCSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:76`



---


[function] name: GetWarningsForPersistentVolumeClaim file: pkg/api/persistentvolumeclaim/util.go:192 returns_error: нет description: —


### GetWarningsForPersistentVolumeClaim (pkg/api/persistentvolumeclaim/util.go:192)


GetWarningsForPersistentVolumeClaim is a function that retrieves data based on the provided parameters and returns (pv *core.PersistentVolumeClaim).


```go
func GetWarningsForPersistentVolumeClaim((pv *core.PersistentVolumeClaim)) (pv *core.PersistentVolumeClaim)
```


**Тип запроса:** core.PersistentVolumeClaim


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


**Тип ответа:** core.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:192`



---


[function] name: GetWarningsForPersistentVolumeClaimSpec file: pkg/api/persistentvolumeclaim/util.go:214 returns_error: нет description: —


### GetWarningsForPersistentVolumeClaimSpec (pkg/api/persistentvolumeclaim/util.go:214)


GetWarningsForPersistentVolumeClaimSpec is a function that retrieves data based on the provided parameters and returns (fieldPath *field.Path, pvSpec core.PersistentVolumeClaimSpec).


```go
func GetWarningsForPersistentVolumeClaimSpec((fieldPath *field.Path, pvSpec core.PersistentVolumeClaimSpec)) (fieldPath *field.Path, pvSpec core.PersistentVolumeClaimSpec)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** pvSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:214`



---


[function] name: NormalizeDataSources file: pkg/api/persistentvolumeclaim/util.go:162 returns_error: нет description: NormalizeDataSources ensures that DataSource and DataSourceRef have the same contents
as long as both are not explicitly


### NormalizeDataSources (pkg/api/persistentvolumeclaim/util.go:162)


NormalizeDataSources ensures that DataSource and DataSourceRef have the same contents
as long as both are not explicitly set.
This should be used by creates/gets of PVCs, but not updates


```go
func NormalizeDataSources((pvcSpec *core.PersistentVolumeClaimSpec)) (pvcSpec *core.PersistentVolumeClaimSpec)
```


**Тип запроса:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvcSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:162`



---


[function] name: dataSourceInUse file: pkg/api/persistentvolumeclaim/util.go:121 returns_error: нет description: —


### dataSourceInUse (pkg/api/persistentvolumeclaim/util.go:121)


dataSourceInUse is a function that performs operations based on the provided parameters and returns (oldPVCSpec *core.PersistentVolumeClaimSpec).


```go
func dataSourceInUse((oldPVCSpec *core.PersistentVolumeClaimSpec)) (oldPVCSpec *core.PersistentVolumeClaimSpec)
```


**Тип запроса:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPVCSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:121`



---


[function] name: dataSourceIsPvcOrSnapshot file: pkg/api/persistentvolumeclaim/util.go:131 returns_error: нет description: —


### dataSourceIsPvcOrSnapshot (pkg/api/persistentvolumeclaim/util.go:131)


dataSourceIsPvcOrSnapshot is a function that performs operations based on the provided parameters and returns (dataSource *core.TypedLocalObjectReference).


```go
func dataSourceIsPvcOrSnapshot((dataSource *core.TypedLocalObjectReference)) (dataSource *core.TypedLocalObjectReference)
```


**Тип запроса:** core.TypedLocalObjectReference


```json
{
  "APIGroup": "string",
  "Kind": "string",
  "Name": "string"
}
```


*Определено в:* `pkg/apis/scheduling/types.go`


**Тип ответа:** dataSource


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.TypedLocalObjectReference


```json
{
  "APIGroup": "string",
  "Kind": "string",
  "Name": "string"
}
```


*Определено в:* `pkg/apis/scheduling/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:131`



---


[function] name: dataSourceRefInUse file: pkg/api/persistentvolumeclaim/util.go:149 returns_error: нет description: —


### dataSourceRefInUse (pkg/api/persistentvolumeclaim/util.go:149)


dataSourceRefInUse is a function that performs operations based on the provided parameters and returns (oldPVCSpec *core.PersistentVolumeClaimSpec).


```go
func dataSourceRefInUse((oldPVCSpec *core.PersistentVolumeClaimSpec)) (oldPVCSpec *core.PersistentVolumeClaimSpec)
```


**Тип запроса:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPVCSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** core.PersistentVolumeClaimSpec


```json
{
  "AccessModes": [],
  "Selector": null,
  "Resources": {},
  "VolumeName": "string",
  "StorageClassName": "string",
  "VolumeMode": null,
  "DataSource": null,
  "DataSourceRef": null,
  "VolumeAttributesClassName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/persistentvolumeclaim/util.go:149`




## pkg/api/pod/testing/make.go


📄 Исходный файл: `pkg/api/pod/testing/make.go`


<details open>
<summary><b>Функции в этом файле (50)</b></summary>


- 🔗 [MakeContainer](#makecontainer-pkgapipodtestingmakego259) `:259`

- 🔗 [MakeContainerStatus](#makecontainerstatus-pkgapipodtestingmakego354) `:354`

- 🔗 [MakeEmptyVolume](#makeemptyvolume-pkgapipodtestingmakego105) `:105`

- 🔗 [MakePod](#makepod-pkgapipodtestingmakego36) `:36`

- 🔗 [MakePodSpec](#makepodspec-pkgapipodtestingmakego59) `:59`

- 🔗 [MakePodStatus](#makepodstatus-pkgapipodtestingmakego326) `:326`

- 🔗 [MakeResourceRequirements](#makeresourcerequirements-pkgapipodtestingmakego285) `:285`

- 🔗 [SetActiveDeadlineSeconds](#setactivedeadlineseconds-pkgapipodtestingmakego121) `:121`

- 🔗 [SetAffinity](#setaffinity-pkgapipodtestingmakego139) `:139`

- 🔗 [SetAnnotations](#setannotations-pkgapipodtestingmakego193) `:193`

- 🔗 [SetContainerImage](#setcontainerimage-pkgapipodtestingmakego273) `:273`

- 🔗 [SetContainerLifecycle](#setcontainerlifecycle-pkgapipodtestingmakego279) `:279`

- 🔗 [SetContainerPorts](#setcontainerports-pkgapipodtestingmakego302) `:302`

- 🔗 [SetContainerResizePolicy](#setcontainerresizepolicy-pkgapipodtestingmakego308) `:308`

- 🔗 [SetContainerResources](#setcontainerresources-pkgapipodtestingmakego296) `:296`

- 🔗 [SetContainerRestartPolicy](#setcontainerrestartpolicy-pkgapipodtestingmakego320) `:320`

- 🔗 [SetContainerSecurityContext](#setcontainersecuritycontext-pkgapipodtestingmakego314) `:314`

- 🔗 [SetContainerStatuses](#setcontainerstatuses-pkgapipodtestingmakego336) `:336`

- 🔗 [SetContainers](#setcontainers-pkgapipodtestingmakego81) `:81`

- 🔗 [SetDNSConfig](#setdnsconfig-pkgapipodtestingmakego175) `:175`

- 🔗 [SetDNSPolicy](#setdnspolicy-pkgapipodtestingmakego169) `:169`

- 🔗 [SetEphemeralContainerStatuses](#setephemeralcontainerstatuses-pkgapipodtestingmakego348) `:348`

- 🔗 [SetEphemeralContainers](#setephemeralcontainers-pkgapipodtestingmakego93) `:93`

- 🔗 [SetGeneration](#setgeneration-pkgapipodtestingmakego205) `:205`

- 🔗 [SetHostAliases](#sethostaliases-pkgapipodtestingmakego145) `:145`

- 🔗 [SetInitContainerStatuses](#setinitcontainerstatuses-pkgapipodtestingmakego342) `:342`

- 🔗 [SetInitContainers](#setinitcontainers-pkgapipodtestingmakego87) `:87`

- 🔗 [SetLabels](#setlabels-pkgapipodtestingmakego199) `:199`

- 🔗 [SetNamespace](#setnamespace-pkgapipodtestingmakego63) `:63`

- 🔗 [SetNodeName](#setnodename-pkgapipodtestingmakego115) `:115`

- 🔗 [SetNodeSelector](#setnodeselector-pkgapipodtestingmakego109) `:109`

- 🔗 [SetOS](#setos-pkgapipodtestingmakego223) `:223`

- 🔗 [SetObjectMeta](#setobjectmeta-pkgapipodtestingmakego247) `:247`

- 🔗 [SetOverhead](#setoverhead-pkgapipodtestingmakego163) `:163`

- 🔗 [SetPodResources](#setpodresources-pkgapipodtestingmakego75) `:75`

- 🔗 [SetPriorityClassName](#setpriorityclassname-pkgapipodtestingmakego151) `:151`

- 🔗 [SetResourceClaims](#setresourceclaims-pkgapipodtestingmakego235) `:235`

- 🔗 [SetResourceVersion](#setresourceversion-pkgapipodtestingmakego69) `:69`

- 🔗 [SetRestartPolicy](#setrestartpolicy-pkgapipodtestingmakego181) `:181`

- 🔗 [SetRuntimeClassName](#setruntimeclassname-pkgapipodtestingmakego157) `:157`

- 🔗 [SetSchedulingGates](#setschedulinggates-pkgapipodtestingmakego211) `:211`

- 🔗 [SetSecurityContext](#setsecuritycontext-pkgapipodtestingmakego133) `:133`

- 🔗 [SetServiceAccountName](#setserviceaccountname-pkgapipodtestingmakego127) `:127`

- 🔗 [SetStatus](#setstatus-pkgapipodtestingmakego229) `:229`

- 🔗 [SetTerminationGracePeriodSeconds](#setterminationgraceperiodseconds-pkgapipodtestingmakego217) `:217`

- 🔗 [SetTolerations](#settolerations-pkgapipodtestingmakego187) `:187`

- 🔗 [SetTopologySpreadConstraints](#settopologyspreadconstraints-pkgapipodtestingmakego241) `:241`

- 🔗 [SetVolumes](#setvolumes-pkgapipodtestingmakego99) `:99`

- 🔗 [SetWorkloadRef](#setworkloadref-pkgapipodtestingmakego253) `:253`

- 🔗 [TweakContainers](#tweakcontainers-pkgapipodtestingmakego365) `:365`


</details>


[function] name: MakeContainer file: pkg/api/pod/testing/make.go:259 returns_error: нет description: —


### MakeContainer (pkg/api/pod/testing/make.go:259)


MakeContainer is a function that performs operations based on the provided parameters and returns (name string, tweaks ...TweakContainer).


```go
func MakeContainer((name string, tweaks ...TweakContainer)) (name string, tweaks ...TweakContainer)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** tweaks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TweakContainer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:259`



---


[function] name: MakeContainerStatus file: pkg/api/pod/testing/make.go:354 returns_error: нет description: —


### MakeContainerStatus (pkg/api/pod/testing/make.go:354)


MakeContainerStatus is a function that performs operations based on the provided parameters and returns (name string, allocatedResources api.ResourceList).


```go
func MakeContainerStatus((name string, allocatedResources api.ResourceList)) (name string, allocatedResources api.ResourceList)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** allocatedResources


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:354`



---


[function] name: MakeEmptyVolume file: pkg/api/pod/testing/make.go:105 returns_error: нет description: —


### MakeEmptyVolume (pkg/api/pod/testing/make.go:105)


MakeEmptyVolume is a function that performs operations based on the provided parameters and returns (name string).


```go
func MakeEmptyVolume((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:105`



---


[function] name: MakePod file: pkg/api/pod/testing/make.go:36 returns_error: нет description: MakePod helps construct Pod objects (which pass API validation) more
legibly and tersely than a Go struct definition.  B


### MakePod (pkg/api/pod/testing/make.go:36)


MakePod helps construct Pod objects (which pass API validation) more
legibly and tersely than a Go struct definition.  By default this produces
a Pod with a single container, ctr.  The caller can pass any number of tweak
functions to further modify the result.


```go
func MakePod((name string, tweaks ...Tweak)) (name string, tweaks ...Tweak)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** tweaks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Tweak


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:36`



---


[function] name: MakePodSpec file: pkg/api/pod/testing/make.go:59 returns_error: нет description: —


### MakePodSpec (pkg/api/pod/testing/make.go:59)


MakePodSpec is a function that performs operations based on the provided parameters and returns (tweaks ...Tweak).


```go
func MakePodSpec((tweaks ...Tweak)) (tweaks ...Tweak)
```


**Тип ответа:** tweaks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Tweak


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:59`



---


[function] name: MakePodStatus file: pkg/api/pod/testing/make.go:326 returns_error: нет description: —


### MakePodStatus (pkg/api/pod/testing/make.go:326)


MakePodStatus is a function that performs operations based on the provided parameters and returns (tweaks ...TweakPodStatus).


```go
func MakePodStatus((tweaks ...TweakPodStatus)) (tweaks ...TweakPodStatus)
```


**Тип ответа:** tweaks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TweakPodStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:326`



---


[function] name: MakeResourceRequirements file: pkg/api/pod/testing/make.go:285 returns_error: нет description: —


### MakeResourceRequirements (pkg/api/pod/testing/make.go:285)


MakeResourceRequirements is a function that performs operations based on the provided parameters and returns (requests, limits map[string]string).


```go
func MakeResourceRequirements((requests, limits map[string]string)) (requests, limits map[string]string)
```


**Тип ответа:** requests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** limits


```json
{
  "minUID": 0
}
```


*Определено в:* `cmd/kubeadm/app/util/users/users_linux.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:285`



---


[function] name: SetActiveDeadlineSeconds file: pkg/api/pod/testing/make.go:121 returns_error: нет description: —


### SetActiveDeadlineSeconds (pkg/api/pod/testing/make.go:121)


SetActiveDeadlineSeconds is a function that updates data based on the provided parameters and returns (deadline int64).


```go
func SetActiveDeadlineSeconds((deadline int64)) (deadline int64)
```


**Тип ответа:** deadline


```json
{
  "deadline": {}
}
```


*Определено в:* `test/utils/ktesting/contexthelper.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:121`



---


[function] name: SetAffinity file: pkg/api/pod/testing/make.go:139 returns_error: нет description: —


### SetAffinity (pkg/api/pod/testing/make.go:139)


SetAffinity is a function that updates data based on the provided parameters and returns (affinity *api.Affinity).


```go
func SetAffinity((affinity *api.Affinity)) (affinity *api.Affinity)
```


**Тип запроса:** api.Affinity


```json
{
  "NodeAffinity": null,
  "PodAffinity": null,
  "PodAntiAffinity": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** affinity


```json
{
  "hostTrace": []
}
```


*Определено в:* `test/e2e/network/service.go`


**Тип ответа:** api.Affinity


```json
{
  "NodeAffinity": null,
  "PodAffinity": null,
  "PodAntiAffinity": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:139`



---


[function] name: SetAnnotations file: pkg/api/pod/testing/make.go:193 returns_error: нет description: —


### SetAnnotations (pkg/api/pod/testing/make.go:193)


SetAnnotations is a function that updates data based on the provided parameters and returns (annos map[string]string).


```go
func SetAnnotations((annos map[string]string)) (annos map[string]string)
```


**Тип ответа:** annos


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:193`



---


[function] name: SetContainerImage file: pkg/api/pod/testing/make.go:273 returns_error: нет description: —


### SetContainerImage (pkg/api/pod/testing/make.go:273)


SetContainerImage is a function that updates data based on the provided parameters and returns (image string).


```go
func SetContainerImage((image string)) (image string)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:273`



---


[function] name: SetContainerLifecycle file: pkg/api/pod/testing/make.go:279 returns_error: нет description: —


### SetContainerLifecycle (pkg/api/pod/testing/make.go:279)


SetContainerLifecycle is a function that updates data based on the provided parameters and returns (lifecycle api.Lifecycle).


```go
func SetContainerLifecycle((lifecycle api.Lifecycle)) (lifecycle api.Lifecycle)
```


**Тип ответа:** lifecycle


```json
{
  "ShutdownInitiated": {},
  "AfterShutdownDelayDuration": {},
  "PreShutdownHooksStopped": {},
  "NotAcceptingNewRequest": {},
  "InFlightRequestsDrained": {},
  "HTTPServerStoppedListening": {},
  "HasBeenReady": {},
  "MuxAndDiscoveryComplete": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/lifecycle_signals.go`


**Тип ответа:** api.Lifecycle


```json
{
  "PostStart": null,
  "PreStop": null,
  "StopSignal": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:279`



---


[function] name: SetContainerPorts file: pkg/api/pod/testing/make.go:302 returns_error: нет description: —


### SetContainerPorts (pkg/api/pod/testing/make.go:302)


SetContainerPorts is a function that updates data based on the provided parameters and returns (ports ...api.ContainerPort).


```go
func SetContainerPorts((ports ...api.ContainerPort)) (ports ...api.ContainerPort)
```


**Тип ответа:** ports


```json
{
  "Verbs": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/discovery/helper.go`


**Тип ответа:** api.ContainerPort


```json
{
  "Name": "string",
  "HostPort": 0,
  "ContainerPort": 0,
  "Protocol": {},
  "HostIP": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:302`



---


[function] name: SetContainerResizePolicy file: pkg/api/pod/testing/make.go:308 returns_error: нет description: —


### SetContainerResizePolicy (pkg/api/pod/testing/make.go:308)


SetContainerResizePolicy is a function that updates data based on the provided parameters and returns (policies ...api.ContainerResizePolicy).


```go
func SetContainerResizePolicy((policies ...api.ContainerResizePolicy)) (policies ...api.ContainerResizePolicy)
```


**Тип ответа:** policies


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ContainerResizePolicy


```json
{
  "ResourceName": {},
  "RestartPolicy": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:308`



---


[function] name: SetContainerResources file: pkg/api/pod/testing/make.go:296 returns_error: нет description: —


### SetContainerResources (pkg/api/pod/testing/make.go:296)


SetContainerResources is a function that updates data based on the provided parameters and returns (rr api.ResourceRequirements).


```go
func SetContainerResources((rr api.ResourceRequirements)) (rr api.ResourceRequirements)
```


**Тип ответа:** rr


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** api.ResourceRequirements


```json
{
  "Limits": {},
  "Requests": {},
  "Claims": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:296`



---


[function] name: SetContainerRestartPolicy file: pkg/api/pod/testing/make.go:320 returns_error: нет description: —


### SetContainerRestartPolicy (pkg/api/pod/testing/make.go:320)


SetContainerRestartPolicy is a function that updates data based on the provided parameters and returns (policy api.ContainerRestartPolicy).


```go
func SetContainerRestartPolicy((policy api.ContainerRestartPolicy)) (policy api.ContainerRestartPolicy)
```


**Тип ответа:** policy


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Тип ответа:** api.ContainerRestartPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:320`



---


[function] name: SetContainerSecurityContext file: pkg/api/pod/testing/make.go:314 returns_error: нет description: —


### SetContainerSecurityContext (pkg/api/pod/testing/make.go:314)


SetContainerSecurityContext is a function that updates data based on the provided parameters and returns (ctx api.SecurityContext).


```go
func SetContainerSecurityContext((ctx api.SecurityContext)) (ctx api.SecurityContext)
```


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** api.SecurityContext


```json
{
  "Capabilities": null,
  "Privileged": false,
  "SELinuxOptions": null,
  "WindowsOptions": null,
  "RunAsUser": 0,
  "RunAsGroup": 0,
  "RunAsNonRoot": false,
  "ReadOnlyRootFilesystem": false,
  "AllowPrivilegeEscalation": false,
  "ProcMount": null,
  "SeccompProfile": null,
  "AppArmorProfile": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:314`



---


[function] name: SetContainerStatuses file: pkg/api/pod/testing/make.go:336 returns_error: нет description: —


### SetContainerStatuses (pkg/api/pod/testing/make.go:336)


SetContainerStatuses is a function that updates data based on the provided parameters and returns (containerStatuses ...api.ContainerStatus).


```go
func SetContainerStatuses((containerStatuses ...api.ContainerStatus)) (containerStatuses ...api.ContainerStatus)
```


**Тип ответа:** containerStatuses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ContainerStatus


```json
{
  "Name": "string",
  "State": {},
  "LastTerminationState": {},
  "Ready": false,
  "RestartCount": 0,
  "Image": "string",
  "ImageID": "string",
  "ContainerID": "string",
  "Started": false,
  "AllocatedResources": {},
  "Resources": null,
  "VolumeMounts": [],
  "User": null,
  "AllocatedResourcesStatus": [],
  "StopSignal": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:336`



---


[function] name: SetContainers file: pkg/api/pod/testing/make.go:81 returns_error: нет description: —


### SetContainers (pkg/api/pod/testing/make.go:81)


SetContainers is a function that updates data based on the provided parameters and returns (containers ...api.Container).


```go
func SetContainers((containers ...api.Container)) (containers ...api.Container)
```


**Тип ответа:** containers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/pod/testing/make.go:81`



---


[function] name: SetDNSConfig file: pkg/api/pod/testing/make.go:175 returns_error: нет description: —


### SetDNSConfig (pkg/api/pod/testing/make.go:175)


SetDNSConfig is a function that updates data based on the provided parameters and returns (config *api.PodDNSConfig).


```go
func SetDNSConfig((config *api.PodDNSConfig)) (config *api.PodDNSConfig)
```


**Тип запроса:** api.PodDNSConfig


```json
{
  "Nameservers": [],
  "Searches": [],
  "Options": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** api.PodDNSConfig


```json
{
  "Nameservers": [],
  "Searches": [],
  "Options": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:175`



---


[function] name: SetDNSPolicy file: pkg/api/pod/testing/make.go:169 returns_error: нет description: —


### SetDNSPolicy (pkg/api/pod/testing/make.go:169)


SetDNSPolicy is a function that updates data based on the provided parameters and returns (policy api.DNSPolicy).


```go
func SetDNSPolicy((policy api.DNSPolicy)) (policy api.DNSPolicy)
```


**Тип ответа:** policy


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Тип ответа:** api.DNSPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:169`



---


[function] name: SetEphemeralContainerStatuses file: pkg/api/pod/testing/make.go:348 returns_error: нет description: —


### SetEphemeralContainerStatuses (pkg/api/pod/testing/make.go:348)


SetEphemeralContainerStatuses is a function that updates data based on the provided parameters and returns (containerStatuses ...api.ContainerStatus).


```go
func SetEphemeralContainerStatuses((containerStatuses ...api.ContainerStatus)) (containerStatuses ...api.ContainerStatus)
```


**Тип ответа:** containerStatuses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ContainerStatus


```json
{
  "Name": "string",
  "State": {},
  "LastTerminationState": {},
  "Ready": false,
  "RestartCount": 0,
  "Image": "string",
  "ImageID": "string",
  "ContainerID": "string",
  "Started": false,
  "AllocatedResources": {},
  "Resources": null,
  "VolumeMounts": [],
  "User": null,
  "AllocatedResourcesStatus": [],
  "StopSignal": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:348`



---


[function] name: SetEphemeralContainers file: pkg/api/pod/testing/make.go:93 returns_error: нет description: —


### SetEphemeralContainers (pkg/api/pod/testing/make.go:93)


SetEphemeralContainers is a function that updates data based on the provided parameters and returns (containers ...api.EphemeralContainer).


```go
func SetEphemeralContainers((containers ...api.EphemeralContainer)) (containers ...api.EphemeralContainer)
```


**Тип ответа:** containers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.EphemeralContainer


```json
{
  "TargetContainerName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:93`



---


[function] name: SetGeneration file: pkg/api/pod/testing/make.go:205 returns_error: нет description: —


### SetGeneration (pkg/api/pod/testing/make.go:205)


SetGeneration is a function that updates data based on the provided parameters and returns (gen int64).


```go
func SetGeneration((gen int64)) (gen int64)
```


**Тип ответа:** gen


```json
{
  "kubeadmConfigPath": "string",
  "certDir": "string",
  "kubeConfigDir": "string",
  "kubeadmConfig": null
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:205`



---


[function] name: SetHostAliases file: pkg/api/pod/testing/make.go:145 returns_error: нет description: —


### SetHostAliases (pkg/api/pod/testing/make.go:145)


SetHostAliases is a function that updates data based on the provided parameters and returns (hostAliases ...api.HostAlias).


```go
func SetHostAliases((hostAliases ...api.HostAlias)) (hostAliases ...api.HostAlias)
```


**Тип ответа:** hostAliases


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.HostAlias


```json
{
  "IP": "string",
  "Hostnames": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:145`



---


[function] name: SetInitContainerStatuses file: pkg/api/pod/testing/make.go:342 returns_error: нет description: —


### SetInitContainerStatuses (pkg/api/pod/testing/make.go:342)


SetInitContainerStatuses is a function that updates data based on the provided parameters and returns (containerStatuses ...api.ContainerStatus).


```go
func SetInitContainerStatuses((containerStatuses ...api.ContainerStatus)) (containerStatuses ...api.ContainerStatus)
```


**Тип ответа:** containerStatuses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ContainerStatus


```json
{
  "Name": "string",
  "State": {},
  "LastTerminationState": {},
  "Ready": false,
  "RestartCount": 0,
  "Image": "string",
  "ImageID": "string",
  "ContainerID": "string",
  "Started": false,
  "AllocatedResources": {},
  "Resources": null,
  "VolumeMounts": [],
  "User": null,
  "AllocatedResourcesStatus": [],
  "StopSignal": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:342`



---


[function] name: SetInitContainers file: pkg/api/pod/testing/make.go:87 returns_error: нет description: —


### SetInitContainers (pkg/api/pod/testing/make.go:87)


SetInitContainers is a function that updates data based on the provided parameters and returns (containers ...api.Container).


```go
func SetInitContainers((containers ...api.Container)) (containers ...api.Container)
```


**Тип ответа:** containers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/pod/testing/make.go:87`



---


[function] name: SetLabels file: pkg/api/pod/testing/make.go:199 returns_error: нет description: —


### SetLabels (pkg/api/pod/testing/make.go:199)


SetLabels is a function that updates data based on the provided parameters and returns (annos map[string]string).


```go
func SetLabels((annos map[string]string)) (annos map[string]string)
```


**Тип ответа:** annos


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:199`



---


[function] name: SetNamespace file: pkg/api/pod/testing/make.go:63 returns_error: нет description: —


### SetNamespace (pkg/api/pod/testing/make.go:63)


SetNamespace is a function that updates data based on the provided parameters and returns (ns string).


```go
func SetNamespace((ns string)) (ns string)
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


📍 *Расположение:* `pkg/api/pod/testing/make.go:63`



---


[function] name: SetNodeName file: pkg/api/pod/testing/make.go:115 returns_error: нет description: —


### SetNodeName (pkg/api/pod/testing/make.go:115)


SetNodeName is a function that updates data based on the provided parameters and returns (name string).


```go
func SetNodeName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:115`



---


[function] name: SetNodeSelector file: pkg/api/pod/testing/make.go:109 returns_error: нет description: —


### SetNodeSelector (pkg/api/pod/testing/make.go:109)


SetNodeSelector is a function that updates data based on the provided parameters and returns (nodeSelector map[string]string).


```go
func SetNodeSelector((nodeSelector map[string]string)) (nodeSelector map[string]string)
```


**Тип ответа:** nodeSelector


```json
{
  "matchLabels": {},
  "matchFields": {},
  "parseErrs": []
}
```


*Определено в:* `staging/src/k8s.io/component-helpers/scheduling/corev1/nodeaffinity/nodeaffinity.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:109`



---


[function] name: SetOS file: pkg/api/pod/testing/make.go:223 returns_error: нет description: —


### SetOS (pkg/api/pod/testing/make.go:223)


SetOS is a function that updates data based on the provided parameters and returns (name api.OSName).


```go
func SetOS((name api.OSName)) (name api.OSName)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** api.OSName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:223`



---


[function] name: SetObjectMeta file: pkg/api/pod/testing/make.go:247 returns_error: нет description: —


### SetObjectMeta (pkg/api/pod/testing/make.go:247)


SetObjectMeta is a function that updates data based on the provided parameters and returns (objectMeta metav1.ObjectMeta).


```go
func SetObjectMeta((objectMeta metav1.ObjectMeta)) (objectMeta metav1.ObjectMeta)
```


**Тип ответа:** objectMeta


```json
{
  "OwnerReferences": [],
  "UID": {}
}
```


*Определено в:* `pkg/controller/history/controller_history.go`


**Тип ответа:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:247`



---


[function] name: SetOverhead file: pkg/api/pod/testing/make.go:163 returns_error: нет description: —


### SetOverhead (pkg/api/pod/testing/make.go:163)


SetOverhead is a function that updates data based on the provided parameters and returns (overhead api.ResourceList).


```go
func SetOverhead((overhead api.ResourceList)) (overhead api.ResourceList)
```


**Тип ответа:** overhead


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:163`



---


[function] name: SetPodResources file: pkg/api/pod/testing/make.go:75 returns_error: нет description: —


### SetPodResources (pkg/api/pod/testing/make.go:75)


SetPodResources is a function that updates data based on the provided parameters and returns (resources *api.ResourceRequirements).


```go
func SetPodResources((resources *api.ResourceRequirements)) (resources *api.ResourceRequirements)
```


**Тип запроса:** api.ResourceRequirements


```json
{
  "Limits": {},
  "Requests": {},
  "Claims": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** resources


```json
{
  "status": null,
  "scale": null
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** api.ResourceRequirements


```json
{
  "Limits": {},
  "Requests": {},
  "Claims": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:75`



---


[function] name: SetPriorityClassName file: pkg/api/pod/testing/make.go:151 returns_error: нет description: —


### SetPriorityClassName (pkg/api/pod/testing/make.go:151)


SetPriorityClassName is a function that updates data based on the provided parameters and returns (name string).


```go
func SetPriorityClassName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:151`



---


[function] name: SetResourceClaims file: pkg/api/pod/testing/make.go:235 returns_error: нет description: —


### SetResourceClaims (pkg/api/pod/testing/make.go:235)


SetResourceClaims is a function that updates data based on the provided parameters and returns (claims ...api.PodResourceClaim).


```go
func SetResourceClaims((claims ...api.PodResourceClaim)) (claims ...api.PodResourceClaim)
```


**Тип ответа:** claims


```json
{
  "Kubernetes": {}
}
```


*Определено в:* `test/images/agnhost/openidmetadata/openidmetadata.go`


**Тип ответа:** api.PodResourceClaim


```json
{
  "Name": "string",
  "ResourceClaimName": "string",
  "ResourceClaimTemplateName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:235`



---


[function] name: SetResourceVersion file: pkg/api/pod/testing/make.go:69 returns_error: нет description: —


### SetResourceVersion (pkg/api/pod/testing/make.go:69)


SetResourceVersion is a function that updates data based on the provided parameters and returns (rv string).


```go
func SetResourceVersion((rv string)) (rv string)
```


**Тип ответа:** rv


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


📍 *Расположение:* `pkg/api/pod/testing/make.go:69`



---


[function] name: SetRestartPolicy file: pkg/api/pod/testing/make.go:181 returns_error: нет description: —


### SetRestartPolicy (pkg/api/pod/testing/make.go:181)


SetRestartPolicy is a function that updates data based on the provided parameters and returns (policy api.RestartPolicy).


```go
func SetRestartPolicy((policy api.RestartPolicy)) (policy api.RestartPolicy)
```


**Тип ответа:** policy


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Тип ответа:** api.RestartPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:181`



---


[function] name: SetRuntimeClassName file: pkg/api/pod/testing/make.go:157 returns_error: нет description: —


### SetRuntimeClassName (pkg/api/pod/testing/make.go:157)


SetRuntimeClassName is a function that updates data based on the provided parameters and returns (name string).


```go
func SetRuntimeClassName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:157`



---


[function] name: SetSchedulingGates file: pkg/api/pod/testing/make.go:211 returns_error: нет description: —


### SetSchedulingGates (pkg/api/pod/testing/make.go:211)


SetSchedulingGates is a function that updates data based on the provided parameters and returns (gates ...api.PodSchedulingGate).


```go
func SetSchedulingGates((gates ...api.PodSchedulingGate)) (gates ...api.PodSchedulingGate)
```


**Тип ответа:** gates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSchedulingGate


```json
{
  "Name": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:211`



---


[function] name: SetSecurityContext file: pkg/api/pod/testing/make.go:133 returns_error: нет description: —


### SetSecurityContext (pkg/api/pod/testing/make.go:133)


SetSecurityContext is a function that updates data based on the provided parameters and returns (ctx *api.PodSecurityContext).


```go
func SetSecurityContext((ctx *api.PodSecurityContext)) (ctx *api.PodSecurityContext)
```


**Тип запроса:** api.PodSecurityContext


```json
{
  "HostNetwork": false,
  "HostPID": false,
  "HostIPC": false,
  "ShareProcessNamespace": false,
  "HostUsers": false,
  "SELinuxOptions": null,
  "WindowsOptions": null,
  "RunAsUser": 0,
  "RunAsGroup": 0,
  "RunAsNonRoot": false,
  "SupplementalGroups": [],
  "SupplementalGroupsPolicy": null,
  "FSGroup": 0,
  "FSGroupChangePolicy": null,
  "Sysctls": [],
  "SeccompProfile": null,
  "AppArmorProfile": null,
  "SELinuxChangePolicy": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** api.PodSecurityContext


```json
{
  "HostNetwork": false,
  "HostPID": false,
  "HostIPC": false,
  "ShareProcessNamespace": false,
  "HostUsers": false,
  "SELinuxOptions": null,
  "WindowsOptions": null,
  "RunAsUser": 0,
  "RunAsGroup": 0,
  "RunAsNonRoot": false,
  "SupplementalGroups": [],
  "SupplementalGroupsPolicy": null,
  "FSGroup": 0,
  "FSGroupChangePolicy": null,
  "Sysctls": [],
  "SeccompProfile": null,
  "AppArmorProfile": null,
  "SELinuxChangePolicy": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:133`



---


[function] name: SetServiceAccountName file: pkg/api/pod/testing/make.go:127 returns_error: нет description: —


### SetServiceAccountName (pkg/api/pod/testing/make.go:127)


SetServiceAccountName is a function that updates data based on the provided parameters and returns (name string).


```go
func SetServiceAccountName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:127`



---


[function] name: SetStatus file: pkg/api/pod/testing/make.go:229 returns_error: нет description: —


### SetStatus (pkg/api/pod/testing/make.go:229)


SetStatus is a function that updates data based on the provided parameters and returns (status api.PodStatus).


```go
func SetStatus((status api.PodStatus)) (status api.PodStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:229`



---


[function] name: SetTerminationGracePeriodSeconds file: pkg/api/pod/testing/make.go:217 returns_error: нет description: —


### SetTerminationGracePeriodSeconds (pkg/api/pod/testing/make.go:217)


SetTerminationGracePeriodSeconds is a function that updates data based on the provided parameters and returns (grace int64).


```go
func SetTerminationGracePeriodSeconds((grace int64)) (grace int64)
```


**Тип ответа:** grace


```json
{
  "lock": {},
  "list": {}
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:217`



---


[function] name: SetTolerations file: pkg/api/pod/testing/make.go:187 returns_error: нет description: —


### SetTolerations (pkg/api/pod/testing/make.go:187)


SetTolerations is a function that updates data based on the provided parameters and returns (tolerations ...api.Toleration).


```go
func SetTolerations((tolerations ...api.Toleration)) (tolerations ...api.Toleration)
```


**Тип ответа:** tolerations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/pod/testing/make.go:187`



---


[function] name: SetTopologySpreadConstraints file: pkg/api/pod/testing/make.go:241 returns_error: нет description: —


### SetTopologySpreadConstraints (pkg/api/pod/testing/make.go:241)


SetTopologySpreadConstraints is a function that updates data based on the provided parameters and returns (tsc ...api.TopologySpreadConstraint).


```go
func SetTopologySpreadConstraints((tsc ...api.TopologySpreadConstraint)) (tsc ...api.TopologySpreadConstraint)
```


**Тип ответа:** tsc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.TopologySpreadConstraint


```json
{
  "MaxSkew": 0,
  "TopologyKey": "string",
  "WhenUnsatisfiable": {},
  "LabelSelector": null,
  "MinDomains": 0,
  "NodeAffinityPolicy": null,
  "NodeTaintsPolicy": null,
  "MatchLabelKeys": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:241`



---


[function] name: SetVolumes file: pkg/api/pod/testing/make.go:99 returns_error: нет description: —


### SetVolumes (pkg/api/pod/testing/make.go:99)


SetVolumes is a function that updates data based on the provided parameters and returns (volumes ...api.Volume).


```go
func SetVolumes((volumes ...api.Volume)) (volumes ...api.Volume)
```


**Тип ответа:** volumes


```json
{
  "tsInfo": {}
}
```


*Определено в:* `test/e2e/storage/testsuites/volumes.go`


**Тип ответа:** api.Volume


```json
{
  "Name": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:99`



---


[function] name: SetWorkloadRef file: pkg/api/pod/testing/make.go:253 returns_error: нет description: —


### SetWorkloadRef (pkg/api/pod/testing/make.go:253)


SetWorkloadRef is a function that updates data based on the provided parameters and returns (workloadRef *api.WorkloadReference).


```go
func SetWorkloadRef((workloadRef *api.WorkloadReference)) (workloadRef *api.WorkloadReference)
```


**Тип запроса:** api.WorkloadReference


```json
{
  "Name": "string",
  "PodGroup": "string",
  "PodGroupReplicaKey": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** workloadRef


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.WorkloadReference


```json
{
  "Name": "string",
  "PodGroup": "string",
  "PodGroupReplicaKey": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/testing/make.go:253`



---


[function] name: TweakContainers file: pkg/api/pod/testing/make.go:365 returns_error: нет description: TweakContainers applies the container tweaks to all containers (regular & init) in the pod.
Note: this should typically 


### TweakContainers (pkg/api/pod/testing/make.go:365)


TweakContainers applies the container tweaks to all containers (regular & init) in the pod.
Note: this should typically be added to pod tweaks after all containers have been added.


```go
func TweakContainers((tweaks ...TweakContainer)) (tweaks ...TweakContainer)
```


**Тип ответа:** tweaks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TweakContainer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/testing/make.go:365`




## pkg/api/pod/util.go


📄 Исходный файл: `pkg/api/pod/util.go`


<details open>
<summary><b>Функции в этом файле (91)</b></summary>


- 🔗 [AllFeatureEnabledContainers](#allfeatureenabledcontainers-pkgapipodutilgo52) `:52`

- 🔗 [ApparmorFieldForAnnotation](#apparmorfieldforannotation-pkgapipodutilgo1776) `:1776`

- 🔗 [ContainerIter](#containeriter-pkgapipodutilgo75) `:75`

- 🔗 [DropDisabledPodFields](#dropdisabledpodfields-pkgapipodutilgo698) `:698`

- 🔗 [DropDisabledTemplateFields](#dropdisabledtemplatefields-pkgapipodutilgo678) `:678`

- 🔗 [GetPodCondition](#getpodcondition-pkgapipodutilgo272) `:272`

- 🔗 [GetPodReadyCondition](#getpodreadycondition-pkgapipodutilgo265) `:265`

- 🔗 [GetValidationOptionsFromPodSpecAndMeta](#getvalidationoptionsfrompodspecandmeta-pkgapipodutilgo411) `:411`

- 🔗 [GetValidationOptionsFromPodTemplate](#getvalidationoptionsfrompodtemplate-pkgapipodutilgo660) `:660`

- 🔗 [HasAPIObjectReference](#hasapiobjectreference-pkgapipodutilgo1702) `:1702`

- 🔗 [IsPodReady](#ispodready-pkgapipodutilgo253) `:253`

- 🔗 [IsPodReadyConditionTrue](#ispodreadyconditiontrue-pkgapipodutilgo258) `:258`

- 🔗 [IsRestartableInitContainer](#isrestartableinitcontainer-pkgapipodutilgo1547) `:1547`

- 🔗 [UpdatePodCondition](#updatepodcondition-pkgapipodutilgo287) `:287`

- 🔗 [VisitContainers](#visitcontainers-pkgapipodutilgo64) `:64`

- 🔗 [VisitPodConfigmapNames](#visitpodconfigmapnames-pkgapipodutilgo208) `:208`

- 🔗 [VisitPodSecretNames](#visitpodsecretnames-pkgapipodutilgo119) `:119`

- 🔗 [allowTaintTolerationComparisonOperators](#allowtainttolerationcomparisonoperators-pkgapipodutilgo1660) `:1660`

- 🔗 [checkContainerUseIndivisibleHugePagesValues](#checkcontaineruseindivisiblehugepagesvalues-pkgapipodutilgo313) `:313`

- 🔗 [clusterTrustBundleProjectionInUse](#clustertrustbundleprojectioninuse-pkgapipodutilgo1407) `:1407`

- 🔗 [containerRestartRulesInUse](#containerrestartrulesinuse-pkgapipodutilgo1820) `:1820`

- 🔗 [containerStopSignalsInUse](#containerstopsignalsinuse-pkgapipodutilgo883) `:883`

- 🔗 [draExendedResourceInUse](#draexendedresourceinuse-pkgapipodutilgo1107) `:1107`

- 🔗 [dropContainerRestartRules](#dropcontainerrestartrules-pkgapipodutilgo1800) `:1800`

- 🔗 [dropContainerStopSignals](#dropcontainerstopsignals-pkgapipodutilgo857) `:857`

- 🔗 [dropDisabledClusterTrustBundleProjection](#dropdisabledclustertrustbundleprojection-pkgapipodutilgo1443) `:1443`

- 🔗 [dropDisabledDynamicResourceAllocationFields](#dropdisableddynamicresourceallocationfields-pkgapipodutilgo1098) `:1098`

- 🔗 [dropDisabledFields](#dropdisabledfields-pkgapipodutilgo722) `:722`

- 🔗 [dropDisabledMatchLabelKeysFieldInPodAffinity](#dropdisabledmatchlabelkeysfieldinpodaffinity-pkgapipodutilgo1172) `:1172`

- 🔗 [dropDisabledMatchLabelKeysFieldInTopologySpread](#dropdisabledmatchlabelkeysfieldintopologyspread-pkgapipodutilgo1189) `:1189`

- 🔗 [dropDisabledNodeInclusionPolicyFields](#dropdisablednodeinclusionpolicyfields-pkgapipodutilgo1155) `:1155`

- 🔗 [dropDisabledPodCertificateProjection](#dropdisabledpodcertificateprojection-pkgapipodutilgo1486) `:1486`

- 🔗 [dropDisabledPodLevelResources](#dropdisabledpodlevelresources-pkgapipodutilgo901) `:901`

- 🔗 [dropDisabledPodStatusFields](#dropdisabledpodstatusfields-pkgapipodutilgo1005) `:1005`

- 🔗 [dropDisabledProcMountField](#dropdisabledprocmountfield-pkgapipodutilgo1138) `:1138`

- 🔗 [dropDisabledWorkloadRef](#dropdisabledworkloadref-pkgapipodutilgo1842) `:1842`

- 🔗 [dropEphemeralResourceClaimRequests](#dropephemeralresourceclaimrequests-pkgapipodutilgo1130) `:1130`

- 🔗 [dropFileKeyRefInUse](#dropfilekeyrefinuse-pkgapipodutilgo824) `:824`

- 🔗 [dropImageVolumeWithDigest](#dropimagevolumewithdigest-pkgapipodutilgo1913) `:1913`

- 🔗 [dropImageVolumes](#dropimagevolumes-pkgapipodutilgo1565) `:1565`

- 🔗 [dropMatchLabelKeysFieldInPodAffnityTerm](#dropmatchlabelkeysfieldinpodaffnityterm-pkgapipodutilgo1206) `:1206`

- 🔗 [dropMatchLabelKeysFieldInWeightedPodAffnityTerm](#dropmatchlabelkeysfieldinweightedpodaffnityterm-pkgapipodutilgo1198) `:1198`

- 🔗 [dropPodLifecycleSleepAction](#droppodlifecyclesleepaction-pkgapipodutilgo909) `:909`

- 🔗 [dropResourceClaimRequests](#dropresourceclaimrequests-pkgapipodutilgo1124) `:1124`

- 🔗 [dropSELinuxChangePolicy](#dropselinuxchangepolicy-pkgapipodutilgo1617) `:1617`

- 🔗 [dynamicResourceAllocationInUse](#dynamicresourceallocationinuse-pkgapipodutilgo1114) `:1114`

- 🔗 [gatherPodEnvVarNames](#gatherpodenvvarnames-pkgapipodutilgo600) `:600`

- 🔗 [hasDotOrUnderscore](#hasdotorunderscore-pkgapipodutilgo536) `:536`

- 🔗 [hasEnvFileKeyRef](#hasenvfilekeyref-pkgapipodutilgo591) `:591`

- 🔗 [hasInvalidLabelValueInAffinitySelector](#hasinvalidlabelvalueinaffinityselector-pkgapipodutilgo1510) `:1510`

- 🔗 [hasInvalidLabelValueInRequiredNodeAffinity](#hasinvalidlabelvalueinrequirednodeaffinity-pkgapipodutilgo1554) `:1554`

- 🔗 [hasInvalidTopologySpreadConstrainMatchLabelKeys](#hasinvalidtopologyspreadconstrainmatchlabelkeys-pkgapipodutilgo371) `:371`

- 🔗 [hasInvalidTopologySpreadConstraintLabelSelector](#hasinvalidtopologyspreadconstraintlabelselector-pkgapipodutilgo360) `:360`

- 🔗 [hasLegacyInvalidTopologySpreadConstrainMatchLabelKeys](#haslegacyinvalidtopologyspreadconstrainmatchlabelkeys-pkgapipodutilgo382) `:382`

- 🔗 [hasNonLocalProjectedTokenPath](#hasnonlocalprojectedtokenpath-pkgapipodutilgo393) `:393`

- 🔗 [hasRestartableInitContainerResizePolicy](#hasrestartableinitcontainerresizepolicy-pkgapipodutilgo1688) `:1688`

- 🔗 [hasUserNamespacesWithVolumeDevices](#hasusernamespaceswithvolumedevices-pkgapipodutilgo1670) `:1670`

- 🔗 [hostUsersInUse](#hostusersinuse-pkgapipodutilgo1294) `:1294`

- 🔗 [imageVolumeWithDigestInUse](#imagevolumewithdigestinuse-pkgapipodutilgo1881) `:1881`

- 🔗 [imageVolumesInUse](#imagevolumesinuse-pkgapipodutilgo1603) `:1603`

- 🔗 [inPlacePodVerticalScalingInUse](#inplacepodverticalscalinginuse-pkgapipodutilgo1353) `:1353`

- 🔗 [matchLabelKeysFieldInPodAffinityInUse](#matchlabelkeysfieldinpodaffinityinuse-pkgapipodutilgo1214) `:1214`

- 🔗 [matchLabelKeysInTopologySpreadInUse](#matchlabelkeysintopologyspreadinuse-pkgapipodutilgo1252) `:1252`

- 🔗 [nodeAffinityPolicyInUse](#nodeaffinitypolicyinuse-pkgapipodutilgo1267) `:1267`

- 🔗 [nodeTaintsPolicyInUse](#nodetaintspolicyinuse-pkgapipodutilgo1281) `:1281`

- 🔗 [podCertificateProjectionInUse](#podcertificateprojectioninuse-pkgapipodutilgo1467) `:1467`

- 🔗 [podFileKeyRefInUse](#podfilekeyrefinuse-pkgapipodutilgo839) `:839`

- 🔗 [podLevelResourcesInUse](#podlevelresourcesinuse-pkgapipodutilgo1322) `:1322`

- 🔗 [podLevelStatusResourcesInUse](#podlevelstatusresourcesinuse-pkgapipodutilgo1344) `:1344`

- 🔗 [podLifecycleSleepActionInUse](#podlifecyclesleepactioninuse-pkgapipodutilgo960) `:960`

- 🔗 [podLifecycleSleepActionZeroValueInUse](#podlifecyclesleepactionzerovalueinuse-pkgapipodutilgo982) `:982`

- 🔗 [podObservedGenerationTrackingInUse](#podobservedgenerationtrackinginuse-pkgapipodutilgo1302) `:1302`

- 🔗 [procMountInUse](#procmountinuse-pkgapipodutilgo1370) `:1370`

- 🔗 [relaxedEnvVarUsed](#relaxedenvvarused-pkgapipodutilgo636) `:636`

- 🔗 [restartAllContainersActionInUse](#restartallcontainersactioninuse-pkgapipodutilgo1856) `:1856`

- 🔗 [restartableInitContainersInUse](#restartableinitcontainersinuse-pkgapipodutilgo1392) `:1392`

- 🔗 [rroInUse](#rroinuse-pkgapipodutilgo1426) `:1426`

- 🔗 [seLinuxChangePolicyInUse](#selinuxchangepolicyinuse-pkgapipodutilgo1627) `:1627`

- 🔗 [setHostnameOverrideInUse](#sethostnameoverrideinuse-pkgapipodutilgo817) `:817`

- 🔗 [skipEmptyNames](#skipemptynames-pkgapipodutilgo104) `:104`

- 🔗 [supplementalGroupsPolicyInUse](#supplementalgroupspolicyinuse-pkgapipodutilgo1298) `:1298`

- 🔗 [taintTolerationComparisonOperatorsInUse](#tainttolerationcomparisonoperatorsinuse-pkgapipodutilgo1648) `:1648`

- 🔗 [useAllowEnvFilesValidation](#useallowenvfilesvalidation-pkgapipodutilgo562) `:562`

- 🔗 [useAllowUserNamespacesHostNetworkSupport](#useallowusernamespaceshostnetworksupport-pkgapipodutilgo545) `:545`

- 🔗 [useOnlyRecursiveSELinuxChangePolicy](#useonlyrecursiveselinuxchangepolicy-pkgapipodutilgo1634) `:1634`

- 🔗 [useRelaxedDNSSearchValidation](#userelaxeddnssearchvalidation-pkgapipodutilgo521) `:521`

- 🔗 [useRelaxedEnvironmentVariableValidation](#userelaxedenvironmentvariablevalidation-pkgapipodutilgo498) `:498`

- 🔗 [usesIndivisibleHugePagesValues](#usesindivisiblehugepagesvalues-pkgapipodutilgo335) `:335`

- 🔗 [visitContainerConfigmapNames](#visitcontainerconfigmapnames-pkgapipodutilgo234) `:234`

- 🔗 [visitContainerSecretNames](#visitcontainersecretnames-pkgapipodutilgo186) `:186`

- 🔗 [workloadRefInUse](#workloadrefinuse-pkgapipodutilgo1848) `:1848`


</details>


[function] name: AllFeatureEnabledContainers file: pkg/api/pod/util.go:52 returns_error: нет description: AllFeatureEnabledContainers returns a ContainerType mask which includes all container
types except for the ones guarded 


### AllFeatureEnabledContainers (pkg/api/pod/util.go:52)


AllFeatureEnabledContainers returns a ContainerType mask which includes all container
types except for the ones guarded by feature gate.


```go
func AllFeatureEnabledContainers(()) ()
```


📍 *Расположение:* `pkg/api/pod/util.go:52`



---


[function] name: ApparmorFieldForAnnotation file: pkg/api/pod/util.go:1776 returns_error: нет description: ApparmorFieldForAnnotation takes a pod annotation and returns the converted
apparmor profile field.


### ApparmorFieldForAnnotation (pkg/api/pod/util.go:1776)


ApparmorFieldForAnnotation takes a pod annotation and returns the converted
apparmor profile field.


```go
func ApparmorFieldForAnnotation((annotation string)) (annotation string)
```


**Тип ответа:** annotation


```json
{
  "level": {},
  "value": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/attributes.go`


📍 *Расположение:* `pkg/api/pod/util.go:1776`



---


[function] name: ContainerIter file: pkg/api/pod/util.go:75 returns_error: нет description: ContainerIter returns an iterator over all containers in the given pod spec with a masked type.
The iteration order is I


### ContainerIter (pkg/api/pod/util.go:75)


ContainerIter returns an iterator over all containers in the given pod spec with a masked type.
The iteration order is InitContainers, then main Containers, then EphemeralContainers.


```go
func ContainerIter((podSpec *api.PodSpec, mask ContainerType)) (podSpec *api.PodSpec, mask ContainerType)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** mask


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/util.go:75`



---


[function] name: DropDisabledPodFields file: pkg/api/pod/util.go:698 returns_error: нет description: DropDisabledPodFields removes disabled fields from the pod metadata and spec.
This should be called from PrepareForCreat


### DropDisabledPodFields (pkg/api/pod/util.go:698)


DropDisabledPodFields removes disabled fields from the pod metadata and spec.
This should be called from PrepareForCreate/PrepareForUpdate for all resources containing a Pod


```go
func DropDisabledPodFields((pod, oldPod *api.Pod)) (pod, oldPod *api.Pod)
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


**Тип ответа:** oldPod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/pod/util.go:698`



---


[function] name: DropDisabledTemplateFields file: pkg/api/pod/util.go:678 returns_error: нет description: DropDisabledTemplateFields removes disabled fields from the pod template metadata and spec.
This should be called from P


### DropDisabledTemplateFields (pkg/api/pod/util.go:678)


DropDisabledTemplateFields removes disabled fields from the pod template metadata and spec.
This should be called from PrepareForCreate/PrepareForUpdate for all resources containing a PodTemplateSpec


```go
func DropDisabledTemplateFields((podTemplate, oldPodTemplate *api.PodTemplateSpec)) (podTemplate, oldPodTemplate *api.PodTemplateSpec)
```


**Тип запроса:** api.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


**Тип ответа:** oldPodTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:678`



---


[function] name: GetPodCondition file: pkg/api/pod/util.go:272 returns_error: нет description: GetPodCondition extracts the provided condition from the given status and returns that.
Returns nil and -1 if the condit


### GetPodCondition (pkg/api/pod/util.go:272)


GetPodCondition extracts the provided condition from the given status and returns that.
Returns nil and -1 if the condition is not present, and the index of the located condition.


```go
func GetPodCondition((int, *api.PodCondition)) (int, *api.PodCondition)
```


**Тип запроса:** api.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** api.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:272`



---


[function] name: GetPodReadyCondition file: pkg/api/pod/util.go:265 returns_error: нет description: GetPodReadyCondition extracts the pod ready condition from the given status and returns that.
Returns nil if the conditi


### GetPodReadyCondition (pkg/api/pod/util.go:265)


GetPodReadyCondition extracts the pod ready condition from the given status and returns that.
Returns nil if the condition is not present.


```go
func GetPodReadyCondition((status api.PodStatus)) (status api.PodStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:265`



---


[function] name: GetValidationOptionsFromPodSpecAndMeta file: pkg/api/pod/util.go:411 returns_error: нет description: GetValidationOptionsFromPodSpecAndMeta returns validation options based on pod specs and metadata


### GetValidationOptionsFromPodSpecAndMeta (pkg/api/pod/util.go:411)


GetValidationOptionsFromPodSpecAndMeta returns validation options based on pod specs and metadata


```go
func GetValidationOptionsFromPodSpecAndMeta((podSpec, oldPodSpec *api.PodSpec, podMeta, oldPodMeta *metav1.ObjectMeta)) (podSpec, oldPodSpec *api.PodSpec, podMeta, oldPodMeta *metav1.ObjectMeta)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podMeta


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodMeta


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:411`



---


[function] name: GetValidationOptionsFromPodTemplate file: pkg/api/pod/util.go:660 returns_error: нет description: GetValidationOptionsFromPodTemplate will return pod validation options for specified template.


### GetValidationOptionsFromPodTemplate (pkg/api/pod/util.go:660)


GetValidationOptionsFromPodTemplate will return pod validation options for specified template.


```go
func GetValidationOptionsFromPodTemplate((podTemplate, oldPodTemplate *api.PodTemplateSpec)) (podTemplate, oldPodTemplate *api.PodTemplateSpec)
```


**Тип запроса:** api.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


**Тип ответа:** oldPodTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:660`



---


[function] name: HasAPIObjectReference file: pkg/api/pod/util.go:1702 returns_error: да description: HasAPIObjectReference returns true if a reference to an API object is found in the pod spec,
along with the plural resou


### HasAPIObjectReference (pkg/api/pod/util.go:1702)


HasAPIObjectReference returns true if a reference to an API object is found in the pod spec,
along with the plural resource of the referenced API type, or an error if an unknown field is encountered.


```go
func HasAPIObjectReference((bool, string, error)) (bool, string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/pod/util.go:1702`



---


[function] name: IsPodReady file: pkg/api/pod/util.go:253 returns_error: нет description: IsPodReady returns true if a pod is ready; false otherwise.


### IsPodReady (pkg/api/pod/util.go:253)


IsPodReady returns true if a pod is ready; false otherwise.


```go
func IsPodReady((pod *api.Pod)) (pod *api.Pod)
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


📍 *Расположение:* `pkg/api/pod/util.go:253`



---


[function] name: IsPodReadyConditionTrue file: pkg/api/pod/util.go:258 returns_error: нет description: IsPodReadyConditionTrue returns true if a pod is ready; false otherwise.


### IsPodReadyConditionTrue (pkg/api/pod/util.go:258)


IsPodReadyConditionTrue returns true if a pod is ready; false otherwise.


```go
func IsPodReadyConditionTrue((status api.PodStatus)) (status api.PodStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:258`



---


[function] name: IsRestartableInitContainer file: pkg/api/pod/util.go:1547 returns_error: нет description: IsRestartableInitContainer returns true if the container has ContainerRestartPolicyAlways.
This function is not checking


### IsRestartableInitContainer (pkg/api/pod/util.go:1547)


IsRestartableInitContainer returns true if the container has ContainerRestartPolicyAlways.
This function is not checking if the container passed to it is indeed an init container.
It is just checking if the container restart policy has been set to always.


```go
func IsRestartableInitContainer((initContainer *api.Container)) (initContainer *api.Container)
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


**Тип ответа:** initContainer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/pod/util.go:1547`



---


[function] name: UpdatePodCondition file: pkg/api/pod/util.go:287 returns_error: нет description: UpdatePodCondition updates existing pod condition or creates a new one. Sets LastTransitionTime to now if the
status has


### UpdatePodCondition (pkg/api/pod/util.go:287)


UpdatePodCondition updates existing pod condition or creates a new one. Sets LastTransitionTime to now if the
status has changed.
Returns true if pod condition has changed or has been added.


```go
func UpdatePodCondition((status *api.PodStatus, condition *api.PodCondition)) (status *api.PodStatus, condition *api.PodCondition)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип запроса:** api.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** api.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:287`



---


[function] name: VisitContainers file: pkg/api/pod/util.go:64 returns_error: нет description: VisitContainers invokes the visitor function with a pointer to every container
spec in the given pod spec with type set 


### VisitContainers (pkg/api/pod/util.go:64)


VisitContainers invokes the visitor function with a pointer to every container
spec in the given pod spec with type set in mask. If visitor returns false,
visiting is short-circuited. VisitContainers returns true if visiting completes,
false if visiting was short-circuited.


```go
func VisitContainers((podSpec *api.PodSpec, mask ContainerType, visitor ContainerVisitor)) (podSpec *api.PodSpec, mask ContainerType, visitor ContainerVisitor)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** mask


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerVisitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/util.go:64`



---


[function] name: VisitPodConfigmapNames file: pkg/api/pod/util.go:208 returns_error: нет description: VisitPodConfigmapNames invokes the visitor function with the name of every configmap
referenced by the pod spec. If visi


### VisitPodConfigmapNames (pkg/api/pod/util.go:208)


VisitPodConfigmapNames invokes the visitor function with the name of every configmap
referenced by the pod spec. If visitor returns false, visiting is short-circuited.
Transitive references (e.g. pod -> pvc -> pv -> secret) are not visited.
Returns true if visiting completed, false if visiting was short-circuited.


```go
func VisitPodConfigmapNames((pod *api.Pod, visitor Visitor, containerType ContainerType)) (pod *api.Pod, visitor Visitor, containerType ContainerType)
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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


**Тип ответа:** containerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/util.go:208`



---


[function] name: VisitPodSecretNames file: pkg/api/pod/util.go:119 returns_error: нет description: VisitPodSecretNames invokes the visitor function with the name of every secret
referenced by the pod spec. If visitor re


### VisitPodSecretNames (pkg/api/pod/util.go:119)


VisitPodSecretNames invokes the visitor function with the name of every secret
referenced by the pod spec. If visitor returns false, visiting is short-circuited.
Transitive references (e.g. pod -> pvc -> pv -> secret) are not visited.
Returns true if visiting completed, false if visiting was short-circuited.


```go
func VisitPodSecretNames((pod *api.Pod, visitor Visitor, containerType ContainerType)) (pod *api.Pod, visitor Visitor, containerType ContainerType)
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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


**Тип ответа:** containerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/util.go:119`



---


[function] name: allowTaintTolerationComparisonOperators file: pkg/api/pod/util.go:1660 returns_error: нет description: —


### allowTaintTolerationComparisonOperators (pkg/api/pod/util.go:1660)


allowTaintTolerationComparisonOperators is a function that performs operations based on the provided parameters and returns (oldPodSpec *api.PodSpec).


```go
func allowTaintTolerationComparisonOperators((oldPodSpec *api.PodSpec)) (oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1660`



---


[function] name: checkContainerUseIndivisibleHugePagesValues file: pkg/api/pod/util.go:313 returns_error: нет description: —


### checkContainerUseIndivisibleHugePagesValues (pkg/api/pod/util.go:313)


checkContainerUseIndivisibleHugePagesValues is a function that performs operations based on the provided parameters and returns (container api.Container).


```go
func checkContainerUseIndivisibleHugePagesValues((container api.Container)) (container api.Container)
```


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


📍 *Расположение:* `pkg/api/pod/util.go:313`



---


[function] name: clusterTrustBundleProjectionInUse file: pkg/api/pod/util.go:1407 returns_error: нет description: —


### clusterTrustBundleProjectionInUse (pkg/api/pod/util.go:1407)


clusterTrustBundleProjectionInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func clusterTrustBundleProjectionInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1407`



---


[function] name: containerRestartRulesInUse file: pkg/api/pod/util.go:1820 returns_error: нет description: —


### containerRestartRulesInUse (pkg/api/pod/util.go:1820)


containerRestartRulesInUse is a function that performs operations based on the provided parameters and returns (oldPodSpec *api.PodSpec).


```go
func containerRestartRulesInUse((oldPodSpec *api.PodSpec)) (oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1820`



---


[function] name: containerStopSignalsInUse file: pkg/api/pod/util.go:883 returns_error: нет description: —


### containerStopSignalsInUse (pkg/api/pod/util.go:883)


containerStopSignalsInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func containerStopSignalsInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:883`



---


[function] name: draExendedResourceInUse file: pkg/api/pod/util.go:1107 returns_error: нет description: —


### draExendedResourceInUse (pkg/api/pod/util.go:1107)


draExendedResourceInUse is a function that performs operations based on the provided parameters and returns (podStatus *api.PodStatus).


```go
func draExendedResourceInUse((podStatus *api.PodStatus)) (podStatus *api.PodStatus)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** podStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:1107`



---


[function] name: dropContainerRestartRules file: pkg/api/pod/util.go:1800 returns_error: нет description: —


### dropContainerRestartRules (pkg/api/pod/util.go:1800)


dropContainerRestartRules is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func dropContainerRestartRules((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1800`



---


[function] name: dropContainerStopSignals file: pkg/api/pod/util.go:857 returns_error: нет description: —


### dropContainerStopSignals (pkg/api/pod/util.go:857)


dropContainerStopSignals is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func dropContainerStopSignals((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:857`



---


[function] name: dropDisabledClusterTrustBundleProjection file: pkg/api/pod/util.go:1443 returns_error: нет description: —


### dropDisabledClusterTrustBundleProjection (pkg/api/pod/util.go:1443)


dropDisabledClusterTrustBundleProjection is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func dropDisabledClusterTrustBundleProjection((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1443`



---


[function] name: dropDisabledDynamicResourceAllocationFields file: pkg/api/pod/util.go:1098 returns_error: нет description: dropDisabledDynamicResourceAllocationFields removes pod claim references from
container specs and pod-level resource cla


### dropDisabledDynamicResourceAllocationFields (pkg/api/pod/util.go:1098)


dropDisabledDynamicResourceAllocationFields removes pod claim references from
container specs and pod-level resource claims unless they are already used
by the old pod spec.


```go
func dropDisabledDynamicResourceAllocationFields((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1098`



---


[function] name: dropDisabledFields file: pkg/api/pod/util.go:722 returns_error: нет description: dropDisabledFields removes disabled fields from the pod metadata and spec.


### dropDisabledFields (pkg/api/pod/util.go:722)


dropDisabledFields removes disabled fields from the pod metadata and spec.


```go
func dropDisabledFields((
	podSpec *api.PodSpec, podAnnotations map[string]string,
	oldPodSpec *api.PodSpec, oldPodAnnotations map[string]string,
)) (
	podSpec *api.PodSpec, podAnnotations map[string]string,
	oldPodSpec *api.PodSpec, oldPodAnnotations map[string]string,
)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podAnnotations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodAnnotations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/api/pod/util.go:722`



---


[function] name: dropDisabledMatchLabelKeysFieldInPodAffinity file: pkg/api/pod/util.go:1172 returns_error: нет description: dropDisabledMatchLabelKeysFieldInPodAffinity removes disabled fields from PodSpec related
to MatchLabelKeys in required/


### dropDisabledMatchLabelKeysFieldInPodAffinity (pkg/api/pod/util.go:1172)


dropDisabledMatchLabelKeysFieldInPodAffinity removes disabled fields from PodSpec related
to MatchLabelKeys in required/preferred PodAffinity/PodAntiAffinity only if it is not already used by the old spec.


```go
func dropDisabledMatchLabelKeysFieldInPodAffinity((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1172`



---


[function] name: dropDisabledMatchLabelKeysFieldInTopologySpread file: pkg/api/pod/util.go:1189 returns_error: нет description: dropDisabledMatchLabelKeysFieldInTopologySpread removes disabled fields from PodSpec related
to MatchLabelKeys in Topolo


### dropDisabledMatchLabelKeysFieldInTopologySpread (pkg/api/pod/util.go:1189)


dropDisabledMatchLabelKeysFieldInTopologySpread removes disabled fields from PodSpec related
to MatchLabelKeys in TopologySpread only if it is not already used by the old spec.


```go
func dropDisabledMatchLabelKeysFieldInTopologySpread((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1189`



---


[function] name: dropDisabledNodeInclusionPolicyFields file: pkg/api/pod/util.go:1155 returns_error: нет description: dropDisabledNodeInclusionPolicyFields removes disabled fields from PodSpec related
to NodeInclusionPolicy only if it is 


### dropDisabledNodeInclusionPolicyFields (pkg/api/pod/util.go:1155)


dropDisabledNodeInclusionPolicyFields removes disabled fields from PodSpec related
to NodeInclusionPolicy only if it is not used by the old spec.


```go
func dropDisabledNodeInclusionPolicyFields((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1155`



---


[function] name: dropDisabledPodCertificateProjection file: pkg/api/pod/util.go:1486 returns_error: нет description: —


### dropDisabledPodCertificateProjection (pkg/api/pod/util.go:1486)


dropDisabledPodCertificateProjection is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func dropDisabledPodCertificateProjection((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1486`



---


[function] name: dropDisabledPodLevelResources file: pkg/api/pod/util.go:901 returns_error: нет description: —


### dropDisabledPodLevelResources (pkg/api/pod/util.go:901)


dropDisabledPodLevelResources is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func dropDisabledPodLevelResources((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:901`



---


[function] name: dropDisabledPodStatusFields file: pkg/api/pod/util.go:1005 returns_error: нет description: dropDisabledPodStatusFields removes disabled fields from the pod status


### dropDisabledPodStatusFields (pkg/api/pod/util.go:1005)


dropDisabledPodStatusFields removes disabled fields from the pod status


```go
func dropDisabledPodStatusFields((podStatus, oldPodStatus *api.PodStatus, podSpec, oldPodSpec *api.PodSpec)) (podStatus, oldPodStatus *api.PodStatus, podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1005`



---


[function] name: dropDisabledProcMountField file: pkg/api/pod/util.go:1138 returns_error: нет description: dropDisabledProcMountField removes disabled fields from PodSpec related
to ProcMount only if it is not already used by t


### dropDisabledProcMountField (pkg/api/pod/util.go:1138)


dropDisabledProcMountField removes disabled fields from PodSpec related
to ProcMount only if it is not already used by the old spec


```go
func dropDisabledProcMountField((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1138`



---


[function] name: dropDisabledWorkloadRef file: pkg/api/pod/util.go:1842 returns_error: нет description: dropDisabledWorkloadRef removes pod workload reference from its spec
unless it is already used by the old pod spec.


### dropDisabledWorkloadRef (pkg/api/pod/util.go:1842)


dropDisabledWorkloadRef removes pod workload reference from its spec
unless it is already used by the old pod spec.


```go
func dropDisabledWorkloadRef((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1842`



---


[function] name: dropEphemeralResourceClaimRequests file: pkg/api/pod/util.go:1130 returns_error: нет description: —


### dropEphemeralResourceClaimRequests (pkg/api/pod/util.go:1130)


dropEphemeralResourceClaimRequests is a function that performs operations based on the provided parameters and returns (containers []api.EphemeralContainer).


```go
func dropEphemeralResourceClaimRequests((containers []api.EphemeralContainer)) (containers []api.EphemeralContainer)
```


**Тип ответа:** containers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.EphemeralContainer


```json
{
  "TargetContainerName": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1130`



---


[function] name: dropFileKeyRefInUse file: pkg/api/pod/util.go:824 returns_error: нет description: —


### dropFileKeyRefInUse (pkg/api/pod/util.go:824)


dropFileKeyRefInUse is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func dropFileKeyRefInUse((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:824`



---


[function] name: dropImageVolumeWithDigest file: pkg/api/pod/util.go:1913 returns_error: нет description: —


### dropImageVolumeWithDigest (pkg/api/pod/util.go:1913)


dropImageVolumeWithDigest is a function that performs operations based on the provided parameters and returns (podStatus *api.PodStatus).


```go
func dropImageVolumeWithDigest((podStatus *api.PodStatus)) (podStatus *api.PodStatus)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** podStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:1913`



---


[function] name: dropImageVolumes file: pkg/api/pod/util.go:1565 returns_error: нет description: KEP: https://kep.k8s.io/4639


### dropImageVolumes (pkg/api/pod/util.go:1565)


KEP: https://kep.k8s.io/4639


```go
func dropImageVolumes((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1565`



---


[function] name: dropMatchLabelKeysFieldInPodAffnityTerm file: pkg/api/pod/util.go:1206 returns_error: нет description: dropMatchLabelKeysFieldInPodAffnityTerm removes MatchLabelKeys and MismatchLabelKeys fields from PodAffinityTerm


### dropMatchLabelKeysFieldInPodAffnityTerm (pkg/api/pod/util.go:1206)


dropMatchLabelKeysFieldInPodAffnityTerm removes MatchLabelKeys and MismatchLabelKeys fields from PodAffinityTerm


```go
func dropMatchLabelKeysFieldInPodAffnityTerm((terms []api.PodAffinityTerm)) (terms []api.PodAffinityTerm)
```


**Тип ответа:** terms


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodAffinityTerm


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


📍 *Расположение:* `pkg/api/pod/util.go:1206`



---


[function] name: dropMatchLabelKeysFieldInWeightedPodAffnityTerm file: pkg/api/pod/util.go:1198 returns_error: нет description: dropMatchLabelKeysFieldInWeightedPodAffnityTerm removes MatchLabelKeys and MismatchLabelKeys fields from WeightedPodAffi


### dropMatchLabelKeysFieldInWeightedPodAffnityTerm (pkg/api/pod/util.go:1198)


dropMatchLabelKeysFieldInWeightedPodAffnityTerm removes MatchLabelKeys and MismatchLabelKeys fields from WeightedPodAffinityTerm


```go
func dropMatchLabelKeysFieldInWeightedPodAffnityTerm((terms []api.WeightedPodAffinityTerm)) (terms []api.WeightedPodAffinityTerm)
```


**Тип ответа:** terms


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.WeightedPodAffinityTerm


```json
{
  "Weight": 0,
  "PodAffinityTerm": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1198`



---


[function] name: dropPodLifecycleSleepAction file: pkg/api/pod/util.go:909 returns_error: нет description: —


### dropPodLifecycleSleepAction (pkg/api/pod/util.go:909)


dropPodLifecycleSleepAction is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func dropPodLifecycleSleepAction((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:909`



---


[function] name: dropResourceClaimRequests file: pkg/api/pod/util.go:1124 returns_error: нет description: —


### dropResourceClaimRequests (pkg/api/pod/util.go:1124)


dropResourceClaimRequests is a function that performs operations based on the provided parameters and returns (containers []api.Container).


```go
func dropResourceClaimRequests((containers []api.Container)) (containers []api.Container)
```


**Тип ответа:** containers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/pod/util.go:1124`



---


[function] name: dropSELinuxChangePolicy file: pkg/api/pod/util.go:1617 returns_error: нет description: —


### dropSELinuxChangePolicy (pkg/api/pod/util.go:1617)


dropSELinuxChangePolicy is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func dropSELinuxChangePolicy((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1617`



---


[function] name: dynamicResourceAllocationInUse file: pkg/api/pod/util.go:1114 returns_error: нет description: —


### dynamicResourceAllocationInUse (pkg/api/pod/util.go:1114)


dynamicResourceAllocationInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func dynamicResourceAllocationInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1114`



---


[function] name: gatherPodEnvVarNames file: pkg/api/pod/util.go:600 returns_error: нет description: —


### gatherPodEnvVarNames (pkg/api/pod/util.go:600)


gatherPodEnvVarNames is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func gatherPodEnvVarNames((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:600`



---


[function] name: hasDotOrUnderscore file: pkg/api/pod/util.go:536 returns_error: нет description: Helper function to check if any domain is a dot or contains an underscore.


### hasDotOrUnderscore (pkg/api/pod/util.go:536)


Helper function to check if any domain is a dot or contains an underscore.


```go
func hasDotOrUnderscore((searches []string)) (searches []string)
```


**Тип ответа:** searches


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/pod/util.go:536`



---


[function] name: hasEnvFileKeyRef file: pkg/api/pod/util.go:591 returns_error: нет description: —


### hasEnvFileKeyRef (pkg/api/pod/util.go:591)


hasEnvFileKeyRef is a function that performs operations based on the provided parameters and returns (envs []api.EnvVar).


```go
func hasEnvFileKeyRef((envs []api.EnvVar)) (envs []api.EnvVar)
```


**Тип ответа:** envs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.EnvVar


```json
{
  "Name": "string",
  "Value": "string"
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:591`



---


[function] name: hasInvalidLabelValueInAffinitySelector file: pkg/api/pod/util.go:1510 returns_error: нет description: —


### hasInvalidLabelValueInAffinitySelector (pkg/api/pod/util.go:1510)


hasInvalidLabelValueInAffinitySelector is a function that performs operations based on the provided parameters and returns (spec *api.PodSpec).


```go
func hasInvalidLabelValueInAffinitySelector((spec *api.PodSpec)) (spec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1510`



---


[function] name: hasInvalidLabelValueInRequiredNodeAffinity file: pkg/api/pod/util.go:1554 returns_error: нет description: —


### hasInvalidLabelValueInRequiredNodeAffinity (pkg/api/pod/util.go:1554)


hasInvalidLabelValueInRequiredNodeAffinity is a function that performs operations based on the provided parameters and returns (spec *api.PodSpec).


```go
func hasInvalidLabelValueInRequiredNodeAffinity((spec *api.PodSpec)) (spec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1554`



---


[function] name: hasInvalidTopologySpreadConstrainMatchLabelKeys file: pkg/api/pod/util.go:371 returns_error: нет description: hasInvalidTopologySpreadConstrainMatchLabelKeys return true if spec.TopologySpreadConstraints have any entry with invali


### hasInvalidTopologySpreadConstrainMatchLabelKeys (pkg/api/pod/util.go:371)


hasInvalidTopologySpreadConstrainMatchLabelKeys return true if spec.TopologySpreadConstraints have any entry with invalid MatchLabelKeys


```go
func hasInvalidTopologySpreadConstrainMatchLabelKeys((spec *api.PodSpec)) (spec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:371`



---


[function] name: hasInvalidTopologySpreadConstraintLabelSelector file: pkg/api/pod/util.go:360 returns_error: нет description: hasInvalidTopologySpreadConstraintLabelSelector return true if spec.TopologySpreadConstraints have any entry with invali


### hasInvalidTopologySpreadConstraintLabelSelector (pkg/api/pod/util.go:360)


hasInvalidTopologySpreadConstraintLabelSelector return true if spec.TopologySpreadConstraints have any entry with invalid labelSelector


```go
func hasInvalidTopologySpreadConstraintLabelSelector((spec *api.PodSpec)) (spec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:360`



---


[function] name: hasLegacyInvalidTopologySpreadConstrainMatchLabelKeys file: pkg/api/pod/util.go:382 returns_error: нет description: hasLegacyInvalidTopologySpreadConstrainMatchLabelKeys return true if spec.TopologySpreadConstraints have any entry with 


### hasLegacyInvalidTopologySpreadConstrainMatchLabelKeys (pkg/api/pod/util.go:382)


hasLegacyInvalidTopologySpreadConstrainMatchLabelKeys return true if spec.TopologySpreadConstraints have any entry with invalid MatchLabelKeys against legacy validation


```go
func hasLegacyInvalidTopologySpreadConstrainMatchLabelKeys((spec *api.PodSpec)) (spec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:382`



---


[function] name: hasNonLocalProjectedTokenPath file: pkg/api/pod/util.go:393 returns_error: нет description: hasNonLocalProjectedTokenPath return true if spec.Volumes have any entry with non-local projected token path


### hasNonLocalProjectedTokenPath (pkg/api/pod/util.go:393)


hasNonLocalProjectedTokenPath return true if spec.Volumes have any entry with non-local projected token path


```go
func hasNonLocalProjectedTokenPath((spec *api.PodSpec)) (spec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:393`



---


[function] name: hasRestartableInitContainerResizePolicy file: pkg/api/pod/util.go:1688 returns_error: нет description: hasRestartableInitContainerResizePolicy returns true if the pod spec is non-nil and
it has any init container with Conta


### hasRestartableInitContainerResizePolicy (pkg/api/pod/util.go:1688)


hasRestartableInitContainerResizePolicy returns true if the pod spec is non-nil and
it has any init container with ContainerRestartPolicyAlways and non-nil ResizePolicy.


```go
func hasRestartableInitContainerResizePolicy((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1688`



---


[function] name: hasUserNamespacesWithVolumeDevices file: pkg/api/pod/util.go:1670 returns_error: нет description: —


### hasUserNamespacesWithVolumeDevices (pkg/api/pod/util.go:1670)


hasUserNamespacesWithVolumeDevices is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func hasUserNamespacesWithVolumeDevices((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1670`



---


[function] name: hostUsersInUse file: pkg/api/pod/util.go:1294 returns_error: нет description: hostUsersInUse returns true if the pod spec has spec.hostUsers field set.


### hostUsersInUse (pkg/api/pod/util.go:1294)


hostUsersInUse returns true if the pod spec has spec.hostUsers field set.


```go
func hostUsersInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1294`



---


[function] name: imageVolumeWithDigestInUse file: pkg/api/pod/util.go:1881 returns_error: нет description: —


### imageVolumeWithDigestInUse (pkg/api/pod/util.go:1881)


imageVolumeWithDigestInUse is a function that performs operations based on the provided parameters and returns (oldPodStatus *api.PodStatus).


```go
func imageVolumeWithDigestInUse((oldPodStatus *api.PodStatus)) (oldPodStatus *api.PodStatus)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** oldPodStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:1881`



---


[function] name: imageVolumesInUse file: pkg/api/pod/util.go:1603 returns_error: нет description: —


### imageVolumesInUse (pkg/api/pod/util.go:1603)


imageVolumesInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func imageVolumesInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1603`



---


[function] name: inPlacePodVerticalScalingInUse file: pkg/api/pod/util.go:1353 returns_error: нет description: inPlacePodVerticalScalingInUse returns true if pod spec is non-nil and ResizePolicy is set


### inPlacePodVerticalScalingInUse (pkg/api/pod/util.go:1353)


inPlacePodVerticalScalingInUse returns true if pod spec is non-nil and ResizePolicy is set


```go
func inPlacePodVerticalScalingInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1353`



---


[function] name: matchLabelKeysFieldInPodAffinityInUse file: pkg/api/pod/util.go:1214 returns_error: нет description: matchLabelKeysFieldInPodAffinityInUse returns true if given affinityTerms have MatchLabelKeys field set.


### matchLabelKeysFieldInPodAffinityInUse (pkg/api/pod/util.go:1214)


matchLabelKeysFieldInPodAffinityInUse returns true if given affinityTerms have MatchLabelKeys field set.


```go
func matchLabelKeysFieldInPodAffinityInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1214`



---


[function] name: matchLabelKeysInTopologySpreadInUse file: pkg/api/pod/util.go:1252 returns_error: нет description: matchLabelKeysInTopologySpreadInUse returns true if the pod spec is non-nil
and has MatchLabelKeys field set in Topology


### matchLabelKeysInTopologySpreadInUse (pkg/api/pod/util.go:1252)


matchLabelKeysInTopologySpreadInUse returns true if the pod spec is non-nil
and has MatchLabelKeys field set in TopologySpreadConstraints.


```go
func matchLabelKeysInTopologySpreadInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1252`



---


[function] name: nodeAffinityPolicyInUse file: pkg/api/pod/util.go:1267 returns_error: нет description: nodeAffinityPolicyInUse returns true if the pod spec is non-nil and has NodeAffinityPolicy field set
in TopologySpreadCo


### nodeAffinityPolicyInUse (pkg/api/pod/util.go:1267)


nodeAffinityPolicyInUse returns true if the pod spec is non-nil and has NodeAffinityPolicy field set
in TopologySpreadConstraints


```go
func nodeAffinityPolicyInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1267`



---


[function] name: nodeTaintsPolicyInUse file: pkg/api/pod/util.go:1281 returns_error: нет description: nodeTaintsPolicyInUse returns true if the pod spec is non-nil and has NodeTaintsPolicy field set
in TopologySpreadConstr


### nodeTaintsPolicyInUse (pkg/api/pod/util.go:1281)


nodeTaintsPolicyInUse returns true if the pod spec is non-nil and has NodeTaintsPolicy field set
in TopologySpreadConstraints


```go
func nodeTaintsPolicyInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1281`



---


[function] name: podCertificateProjectionInUse file: pkg/api/pod/util.go:1467 returns_error: нет description: —


### podCertificateProjectionInUse (pkg/api/pod/util.go:1467)


podCertificateProjectionInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func podCertificateProjectionInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1467`



---


[function] name: podFileKeyRefInUse file: pkg/api/pod/util.go:839 returns_error: нет description: —


### podFileKeyRefInUse (pkg/api/pod/util.go:839)


podFileKeyRefInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func podFileKeyRefInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:839`



---


[function] name: podLevelResourcesInUse file: pkg/api/pod/util.go:1322 returns_error: нет description: podLevelResourcesInUse returns true if pod-spec is non-nil and Resources field at
pod-level has non-empty Requests or Li


### podLevelResourcesInUse (pkg/api/pod/util.go:1322)


podLevelResourcesInUse returns true if pod-spec is non-nil and Resources field at
pod-level has non-empty Requests or Limits.


```go
func podLevelResourcesInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1322`



---


[function] name: podLevelStatusResourcesInUse file: pkg/api/pod/util.go:1344 returns_error: нет description: podLevelStatusResourcesInUse checks if AllocationResources or Resources are set
in PodStatus.


### podLevelStatusResourcesInUse (pkg/api/pod/util.go:1344)


podLevelStatusResourcesInUse checks if AllocationResources or Resources are set
in PodStatus.


```go
func podLevelStatusResourcesInUse((podStatus *api.PodStatus)) (podStatus *api.PodStatus)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** podStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:1344`



---


[function] name: podLifecycleSleepActionInUse file: pkg/api/pod/util.go:960 returns_error: нет description: —


### podLifecycleSleepActionInUse (pkg/api/pod/util.go:960)


podLifecycleSleepActionInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func podLifecycleSleepActionInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:960`



---


[function] name: podLifecycleSleepActionZeroValueInUse file: pkg/api/pod/util.go:982 returns_error: нет description: —


### podLifecycleSleepActionZeroValueInUse (pkg/api/pod/util.go:982)


podLifecycleSleepActionZeroValueInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func podLifecycleSleepActionZeroValueInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:982`



---


[function] name: podObservedGenerationTrackingInUse file: pkg/api/pod/util.go:1302 returns_error: нет description: —


### podObservedGenerationTrackingInUse (pkg/api/pod/util.go:1302)


podObservedGenerationTrackingInUse is a function that performs operations based on the provided parameters and returns (podStatus *api.PodStatus).


```go
func podObservedGenerationTrackingInUse((podStatus *api.PodStatus)) (podStatus *api.PodStatus)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** podStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/pod/util.go:1302`



---


[function] name: procMountInUse file: pkg/api/pod/util.go:1370 returns_error: нет description: procMountInUse returns true if the pod spec is non-nil and has a SecurityContext's ProcMount field set to a non-default 


### procMountInUse (pkg/api/pod/util.go:1370)


procMountInUse returns true if the pod spec is non-nil and has a SecurityContext's ProcMount field set to a non-default value


```go
func procMountInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1370`



---


[function] name: relaxedEnvVarUsed file: pkg/api/pod/util.go:636 returns_error: нет description: —


### relaxedEnvVarUsed (pkg/api/pod/util.go:636)


relaxedEnvVarUsed is a function that performs operations based on the provided parameters and returns (name string, oldPodEnvVarNames sets.Set[string]).


```go
func relaxedEnvVarUsed((name string, oldPodEnvVarNames sets.Set[string])) (name string, oldPodEnvVarNames sets.Set[string])
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** oldPodEnvVarNames


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


📍 *Расположение:* `pkg/api/pod/util.go:636`



---


[function] name: restartAllContainersActionInUse file: pkg/api/pod/util.go:1856 returns_error: нет description: —


### restartAllContainersActionInUse (pkg/api/pod/util.go:1856)


restartAllContainersActionInUse is a function that performs operations based on the provided parameters and returns (oldPodSpec *api.PodSpec).


```go
func restartAllContainersActionInUse((oldPodSpec *api.PodSpec)) (oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1856`



---


[function] name: restartableInitContainersInUse file: pkg/api/pod/util.go:1392 returns_error: нет description: restartableInitContainersInUse returns true if the pod spec is non-nil and
it has any init container with ContainerResta


### restartableInitContainersInUse (pkg/api/pod/util.go:1392)


restartableInitContainersInUse returns true if the pod spec is non-nil and
it has any init container with ContainerRestartPolicyAlways.


```go
func restartableInitContainersInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1392`



---


[function] name: rroInUse file: pkg/api/pod/util.go:1426 returns_error: нет description: —


### rroInUse (pkg/api/pod/util.go:1426)


rroInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func rroInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1426`



---


[function] name: seLinuxChangePolicyInUse file: pkg/api/pod/util.go:1627 returns_error: нет description: —


### seLinuxChangePolicyInUse (pkg/api/pod/util.go:1627)


seLinuxChangePolicyInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func seLinuxChangePolicyInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1627`



---


[function] name: setHostnameOverrideInUse file: pkg/api/pod/util.go:817 returns_error: нет description: setHostnameOverrideInUse returns true if any pod's spec defines HostnameOverride field.


### setHostnameOverrideInUse (pkg/api/pod/util.go:817)


setHostnameOverrideInUse returns true if any pod's spec defines HostnameOverride field.


```go
func setHostnameOverrideInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:817`



---


[function] name: skipEmptyNames file: pkg/api/pod/util.go:104 returns_error: нет description: —


### skipEmptyNames (pkg/api/pod/util.go:104)


skipEmptyNames is a function that performs operations based on the provided parameters and returns (visitor Visitor).


```go
func skipEmptyNames((visitor Visitor)) (visitor Visitor)
```


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/pod/util.go:104`



---


[function] name: supplementalGroupsPolicyInUse file: pkg/api/pod/util.go:1298 returns_error: нет description: —


### supplementalGroupsPolicyInUse (pkg/api/pod/util.go:1298)


supplementalGroupsPolicyInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func supplementalGroupsPolicyInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1298`



---


[function] name: taintTolerationComparisonOperatorsInUse file: pkg/api/pod/util.go:1648 returns_error: нет description: —


### taintTolerationComparisonOperatorsInUse (pkg/api/pod/util.go:1648)


taintTolerationComparisonOperatorsInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func taintTolerationComparisonOperatorsInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1648`



---


[function] name: useAllowEnvFilesValidation file: pkg/api/pod/util.go:562 returns_error: нет description: —


### useAllowEnvFilesValidation (pkg/api/pod/util.go:562)


useAllowEnvFilesValidation is a function that performs operations based on the provided parameters and returns (oldPodSpec *api.PodSpec).


```go
func useAllowEnvFilesValidation((oldPodSpec *api.PodSpec)) (oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:562`



---


[function] name: useAllowUserNamespacesHostNetworkSupport file: pkg/api/pod/util.go:545 returns_error: нет description: —


### useAllowUserNamespacesHostNetworkSupport (pkg/api/pod/util.go:545)


useAllowUserNamespacesHostNetworkSupport is a function that performs operations based on the provided parameters and returns (oldPodSpec *api.PodSpec).


```go
func useAllowUserNamespacesHostNetworkSupport((oldPodSpec *api.PodSpec)) (oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:545`



---


[function] name: useOnlyRecursiveSELinuxChangePolicy file: pkg/api/pod/util.go:1634 returns_error: нет description: —


### useOnlyRecursiveSELinuxChangePolicy (pkg/api/pod/util.go:1634)


useOnlyRecursiveSELinuxChangePolicy is a function that performs operations based on the provided parameters and returns (oldPodSpec *api.PodSpec).


```go
func useOnlyRecursiveSELinuxChangePolicy((oldPodSpec *api.PodSpec)) (oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1634`



---


[function] name: useRelaxedDNSSearchValidation file: pkg/api/pod/util.go:521 returns_error: нет description: —


### useRelaxedDNSSearchValidation (pkg/api/pod/util.go:521)


useRelaxedDNSSearchValidation is a function that performs operations based on the provided parameters and returns (oldPodSpec *api.PodSpec).


```go
func useRelaxedDNSSearchValidation((oldPodSpec *api.PodSpec)) (oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:521`



---


[function] name: useRelaxedEnvironmentVariableValidation file: pkg/api/pod/util.go:498 returns_error: нет description: —


### useRelaxedEnvironmentVariableValidation (pkg/api/pod/util.go:498)


useRelaxedEnvironmentVariableValidation is a function that performs operations based on the provided parameters and returns (podSpec, oldPodSpec *api.PodSpec).


```go
func useRelaxedEnvironmentVariableValidation((podSpec, oldPodSpec *api.PodSpec)) (podSpec, oldPodSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:498`



---


[function] name: usesIndivisibleHugePagesValues file: pkg/api/pod/util.go:335 returns_error: нет description: usesIndivisibleHugePagesValues returns true if the one of the containers uses non-integer multiple
of huge page unit siz


### usesIndivisibleHugePagesValues (pkg/api/pod/util.go:335)


usesIndivisibleHugePagesValues returns true if the one of the containers uses non-integer multiple
of huge page unit size


```go
func usesIndivisibleHugePagesValues((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:335`



---


[function] name: visitContainerConfigmapNames file: pkg/api/pod/util.go:234 returns_error: нет description: —


### visitContainerConfigmapNames (pkg/api/pod/util.go:234)


visitContainerConfigmapNames is a function that performs operations based on the provided parameters and returns (container *api.Container, visitor Visitor).


```go
func visitContainerConfigmapNames((container *api.Container, visitor Visitor)) (container *api.Container, visitor Visitor)
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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/pod/util.go:234`



---


[function] name: visitContainerSecretNames file: pkg/api/pod/util.go:186 returns_error: нет description: —


### visitContainerSecretNames (pkg/api/pod/util.go:186)


visitContainerSecretNames is a function that performs operations based on the provided parameters and returns (container *api.Container, visitor Visitor).


```go
func visitContainerSecretNames((container *api.Container, visitor Visitor)) (container *api.Container, visitor Visitor)
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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/pod/util.go:186`



---


[function] name: workloadRefInUse file: pkg/api/pod/util.go:1848 returns_error: нет description: —


### workloadRefInUse (pkg/api/pod/util.go:1848)


workloadRefInUse is a function that performs operations based on the provided parameters and returns (podSpec *api.PodSpec).


```go
func workloadRefInUse((podSpec *api.PodSpec)) (podSpec *api.PodSpec)
```


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/util.go:1848`




## pkg/api/pod/warnings.go


📄 Исходный файл: `pkg/api/pod/warnings.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [GetWarningsForPod](#getwarningsforpod-pkgapipodwarningsgo38) `:38`

- 🔗 [GetWarningsForPodTemplate](#getwarningsforpodtemplate-pkgapipodwarningsgo54) `:54`

- 🔗 [String](#string-pkgapipodwarningsgo509) `:509`

- 🔗 [checkForOverlap](#checkforoverlap-pkgapipodwarningsgo552) `:552`

- 🔗 [checkVolumeMappingForOverlap](#checkvolumemappingforoverlap-pkgapipodwarningsgo534) `:534`

- 🔗 [extractPaths](#extractpaths-pkgapipodwarningsgo516) `:516`

- 🔗 [extractPathsDownwardAPI](#extractpathsdownwardapi-pkgapipodwarningsgo525) `:525`

- 🔗 [warningsForOverlappingVirtualPaths](#warningsforoverlappingvirtualpaths-pkgapipodwarningsgo415) `:415`

- 🔗 [warningsForPodAffinityTerms](#warningsforpodaffinityterms-pkgapipodwarningsgo381) `:381`

- 🔗 [warningsForPodSpecAndMeta](#warningsforpodspecandmeta-pkgapipodwarningsgo89) `:89`

- 🔗 [warningsForWeightedPodAffinityTerms](#warningsforweightedpodaffinityterms-pkgapipodwarningsgo391) `:391`


</details>


[function] name: GetWarningsForPod file: pkg/api/pod/warnings.go:38 returns_error: нет description: —


### GetWarningsForPod (pkg/api/pod/warnings.go:38)


GetWarningsForPod is a function that retrieves data based on the provided parameters and returns (ctx context.Context, pod, oldPod *api.Pod).


```go
func GetWarningsForPod((ctx context.Context, pod, oldPod *api.Pod)) (ctx context.Context, pod, oldPod *api.Pod)
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


**Тип ответа:** oldPod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/pod/warnings.go:38`



---


[function] name: GetWarningsForPodTemplate file: pkg/api/pod/warnings.go:54 returns_error: нет description: —


### GetWarningsForPodTemplate (pkg/api/pod/warnings.go:54)


GetWarningsForPodTemplate is a function that retrieves data based on the provided parameters and returns (ctx context.Context, fieldPath *field.Path, podTemplate, oldPodTemplate *api.PodTemplateSpec).


```go
func GetWarningsForPodTemplate((ctx context.Context, fieldPath *field.Path, podTemplate, oldPodTemplate *api.PodTemplateSpec)) (ctx context.Context, fieldPath *field.Path, podTemplate, oldPodTemplate *api.PodTemplateSpec)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип запроса:** api.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


**Тип ответа:** oldPodTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:54`



---


[function] name: String file: pkg/api/pod/warnings.go:509 returns_error: нет description: —


### String (pkg/api/pod/warnings.go:509)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (ps pathAndSource) String(()) ()
```


📍 *Расположение:* `pkg/api/pod/warnings.go:509`



---


[function] name: checkForOverlap file: pkg/api/pod/warnings.go:552 returns_error: нет description: —


### checkForOverlap (pkg/api/pod/warnings.go:552)


checkForOverlap is a function that performs operations based on the provided parameters and returns (haystack []pathAndSource, needle pathAndSource).


```go
func checkForOverlap((haystack []pathAndSource, needle pathAndSource)) (haystack []pathAndSource, needle pathAndSource)
```


**Тип ответа:** haystack


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pathAndSource


```json
{
  "path": "string",
  "source": "string"
}
```


*Определено в:* `pkg/api/pod/warnings.go`


**Тип ответа:** needle


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pathAndSource


```json
{
  "path": "string",
  "source": "string"
}
```


*Определено в:* `pkg/api/pod/warnings.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:552`



---


[function] name: checkVolumeMappingForOverlap file: pkg/api/pod/warnings.go:534 returns_error: нет description: —


### checkVolumeMappingForOverlap (pkg/api/pod/warnings.go:534)


checkVolumeMappingForOverlap is a function that performs operations based on the provided parameters and returns (paths []pathAndSource).


```go
func checkVolumeMappingForOverlap((paths []pathAndSource)) (paths []pathAndSource)
```


**Тип ответа:** paths


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pathAndSource


```json
{
  "path": "string",
  "source": "string"
}
```


*Определено в:* `pkg/api/pod/warnings.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:534`



---


[function] name: extractPaths file: pkg/api/pod/warnings.go:516 returns_error: нет description: —


### extractPaths (pkg/api/pod/warnings.go:516)


extractPaths is a function that performs operations based on the provided parameters and returns (mapping []api.KeyToPath, source string).


```go
func extractPaths((mapping []api.KeyToPath, source string)) (mapping []api.KeyToPath, source string)
```


**Тип ответа:** mapping


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.KeyToPath


```json
{
  "Key": "string",
  "Path": "string",
  "Mode": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** source


```json
{
  "Printer": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/output/output.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:516`



---


[function] name: extractPathsDownwardAPI file: pkg/api/pod/warnings.go:525 returns_error: нет description: —


### extractPathsDownwardAPI (pkg/api/pod/warnings.go:525)


extractPathsDownwardAPI is a function that performs operations based on the provided parameters and returns (mapping []api.DownwardAPIVolumeFile, source string).


```go
func extractPathsDownwardAPI((mapping []api.DownwardAPIVolumeFile, source string)) (mapping []api.DownwardAPIVolumeFile, source string)
```


**Тип ответа:** mapping


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.DownwardAPIVolumeFile


```json
{
  "Path": "string",
  "FieldRef": null,
  "ResourceFieldRef": null,
  "Mode": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** source


```json
{
  "Printer": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/output/output.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:525`



---


[function] name: warningsForOverlappingVirtualPaths file: pkg/api/pod/warnings.go:415 returns_error: нет description: warningsForOverlappingVirtualPaths validates that there are no overlapping paths in single ConfigMapVolume, SecretVolume


### warningsForOverlappingVirtualPaths (pkg/api/pod/warnings.go:415)


warningsForOverlappingVirtualPaths validates that there are no overlapping paths in single ConfigMapVolume, SecretVolume, DownwardAPIVolume and ProjectedVolume.
A volume can try to load different keys to the same path which will result in overwriting of the value from the latest registered key
Another possible scenario is when one of the path contains the other key path. Example:
configMap:

name: myconfig
items:
- key: key1
path: path
- key: key2
path: path/path2

In such cases we either get `is directory` or 'file exists' error message.


```go
func warningsForOverlappingVirtualPaths((volumes []api.Volume)) (volumes []api.Volume)
```


**Тип ответа:** volumes


```json
{
  "tsInfo": {}
}
```


*Определено в:* `test/e2e/storage/testsuites/volumes.go`


**Тип ответа:** api.Volume


```json
{
  "Name": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:415`



---


[function] name: warningsForPodAffinityTerms file: pkg/api/pod/warnings.go:381 returns_error: нет description: —


### warningsForPodAffinityTerms (pkg/api/pod/warnings.go:381)


warningsForPodAffinityTerms is a function that performs operations based on the provided parameters and returns (terms []api.PodAffinityTerm, fieldPath *field.Path).


```go
func warningsForPodAffinityTerms((terms []api.PodAffinityTerm, fieldPath *field.Path)) (terms []api.PodAffinityTerm, fieldPath *field.Path)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** terms


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodAffinityTerm


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


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:381`



---


[function] name: warningsForPodSpecAndMeta file: pkg/api/pod/warnings.go:89 returns_error: нет description: —


### warningsForPodSpecAndMeta (pkg/api/pod/warnings.go:89)


warningsForPodSpecAndMeta is a function that performs operations based on the provided parameters and returns (fieldPath *field.Path, podSpec *api.PodSpec, meta *metav1.ObjectMeta, oldPodSpec *api.PodSpec, oldMeta *metav1.ObjectMeta).


```go
func warningsForPodSpecAndMeta((fieldPath *field.Path, podSpec *api.PodSpec, meta *metav1.ObjectMeta, oldPodSpec *api.PodSpec, oldMeta *metav1.ObjectMeta)) (fieldPath *field.Path, podSpec *api.PodSpec, meta *metav1.ObjectMeta, oldPodSpec *api.PodSpec, oldMeta *metav1.ObjectMeta)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип запроса:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** meta


```json
{
  "lister": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/metadata/metadatalister/shim.go`


**Тип ответа:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** oldPodSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldMeta


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.ObjectMeta


```json
{
  "name": "string",
  "generateName": "string",
  "namespace": "string",
  "selfLink": "string",
  "uid": {},
  "resourceVersion": "string",
  "generation": 0,
  "creationTimestamp": {},
  "deletionTimestamp": null,
  "deletionGracePeriodSeconds": 0,
  "labels": {},
  "annotations": {},
  "ownerReferences": [],
  "finalizers": [],
  "managedFields": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:89`



---


[function] name: warningsForWeightedPodAffinityTerms file: pkg/api/pod/warnings.go:391 returns_error: нет description: —


### warningsForWeightedPodAffinityTerms (pkg/api/pod/warnings.go:391)


warningsForWeightedPodAffinityTerms is a function that performs operations based on the provided parameters and returns (terms []api.WeightedPodAffinityTerm, fieldPath *field.Path).


```go
func warningsForWeightedPodAffinityTerms((terms []api.WeightedPodAffinityTerm, fieldPath *field.Path)) (terms []api.WeightedPodAffinityTerm, fieldPath *field.Path)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** terms


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.WeightedPodAffinityTerm


```json
{
  "Weight": 0,
  "PodAffinityTerm": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** fieldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


📍 *Расположение:* `pkg/api/pod/warnings.go:391`




## pkg/api/resourceclaimspec/util.go


📄 Исходный файл: `pkg/api/resourceclaimspec/util.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [DRAAdminAccessFeatureInUse](#draadminaccessfeatureinuse-pkgapiresourceclaimspecutilgo117) `:117`

- 🔗 [DRAConsumableCapacityFeatureInUse](#draconsumablecapacityfeatureinuse-pkgapiresourceclaimspecutilgo154) `:154`

- 🔗 [DropDisabledFields](#dropdisabledfields-pkgapiresourceclaimspecutilgo33) `:33`

- 🔗 [draDeviceTaintsInUse](#dradevicetaintsinuse-pkgapiresourceclaimspecutilgo56) `:56`

- 🔗 [draPrioritizedListFeatureInUse](#draprioritizedlistfeatureinuse-pkgapiresourceclaimspecutilgo88) `:88`

- 🔗 [dropDisabledDRAAdminAccessFields](#dropdisableddraadminaccessfields-pkgapiresourceclaimspecutilgo102) `:102`

- 🔗 [dropDisabledDRADeviceTaintsFields](#dropdisableddradevicetaintsfields-pkgapiresourceclaimspecutilgo40) `:40`

- 🔗 [dropDisabledDRAPrioritizedListFields](#dropdisableddraprioritizedlistfields-pkgapiresourceclaimspecutilgo75) `:75`

- 🔗 [dropDisabledDRAResourceClaimConsumableCapacityFields](#dropdisableddraresourceclaimconsumablecapacityfields-pkgapiresourceclaimspecutilgo131) `:131`


</details>


[function] name: DRAAdminAccessFeatureInUse file: pkg/api/resourceclaimspec/util.go:117 returns_error: нет description: DRAAdminAccessFeatureInUse checks whether the feature is in use in the spec.


### DRAAdminAccessFeatureInUse (pkg/api/resourceclaimspec/util.go:117)


DRAAdminAccessFeatureInUse checks whether the feature is in use in the spec.


```go
func DRAAdminAccessFeatureInUse((spec *resource.ResourceClaimSpec)) (spec *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:117`



---


[function] name: DRAConsumableCapacityFeatureInUse file: pkg/api/resourceclaimspec/util.go:154 returns_error: нет description: DRAConsumableCapacityFeatureInUse checks whether the feature is in use in the spec.


### DRAConsumableCapacityFeatureInUse (pkg/api/resourceclaimspec/util.go:154)


DRAConsumableCapacityFeatureInUse checks whether the feature is in use in the spec.


```go
func DRAConsumableCapacityFeatureInUse((spec *resource.ResourceClaimSpec)) (spec *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:154`



---


[function] name: DropDisabledFields file: pkg/api/resourceclaimspec/util.go:33 returns_error: нет description: DropDisabledFields removes disabled fields from the spec unless they were in
use there before.

Theoretically some featu


### DropDisabledFields (pkg/api/resourceclaimspec/util.go:33)


DropDisabledFields removes disabled fields from the spec unless they were in
use there before.

Theoretically some features could be in use in an old ResourceClaim status
and not in use in the spec. This can only occur in a spec update, which is
currently prevented because the entire spec is immutable. Even if it was
allowed, preventing adding disabled fields to the spec is the right thing to
do regardless of what may have ended up in the status earlier.


```go
func DropDisabledFields((new, old *resource.ResourceClaimSpec)) (new, old *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** new


```json
{
  "cfgPath": "string",
  "kubeconfigPath": "string",
  "cfg": {}
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:33`



---


[function] name: draDeviceTaintsInUse file: pkg/api/resourceclaimspec/util.go:56 returns_error: нет description: —


### draDeviceTaintsInUse (pkg/api/resourceclaimspec/util.go:56)


draDeviceTaintsInUse is a function that performs operations based on the provided parameters and returns (spec *resource.ResourceClaimSpec).


```go
func draDeviceTaintsInUse((spec *resource.ResourceClaimSpec)) (spec *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:56`



---


[function] name: draPrioritizedListFeatureInUse file: pkg/api/resourceclaimspec/util.go:88 returns_error: нет description: —


### draPrioritizedListFeatureInUse (pkg/api/resourceclaimspec/util.go:88)


draPrioritizedListFeatureInUse is a function that performs operations based on the provided parameters and returns (spec *resource.ResourceClaimSpec).


```go
func draPrioritizedListFeatureInUse((spec *resource.ResourceClaimSpec)) (spec *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:88`



---


[function] name: dropDisabledDRAAdminAccessFields file: pkg/api/resourceclaimspec/util.go:102 returns_error: нет description: —


### dropDisabledDRAAdminAccessFields (pkg/api/resourceclaimspec/util.go:102)


dropDisabledDRAAdminAccessFields is a function that performs operations based on the provided parameters and returns (new, old *resource.ResourceClaimSpec).


```go
func dropDisabledDRAAdminAccessFields((new, old *resource.ResourceClaimSpec)) (new, old *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** new


```json
{
  "cfgPath": "string",
  "kubeconfigPath": "string",
  "cfg": {}
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:102`



---


[function] name: dropDisabledDRADeviceTaintsFields file: pkg/api/resourceclaimspec/util.go:40 returns_error: нет description: —


### dropDisabledDRADeviceTaintsFields (pkg/api/resourceclaimspec/util.go:40)


dropDisabledDRADeviceTaintsFields is a function that performs operations based on the provided parameters and returns (new, old *resource.ResourceClaimSpec).


```go
func dropDisabledDRADeviceTaintsFields((new, old *resource.ResourceClaimSpec)) (new, old *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** new


```json
{
  "cfgPath": "string",
  "kubeconfigPath": "string",
  "cfg": {}
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:40`



---


[function] name: dropDisabledDRAPrioritizedListFields file: pkg/api/resourceclaimspec/util.go:75 returns_error: нет description: —


### dropDisabledDRAPrioritizedListFields (pkg/api/resourceclaimspec/util.go:75)


dropDisabledDRAPrioritizedListFields is a function that performs operations based on the provided parameters and returns (new, old *resource.ResourceClaimSpec).


```go
func dropDisabledDRAPrioritizedListFields((new, old *resource.ResourceClaimSpec)) (new, old *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** new


```json
{
  "cfgPath": "string",
  "kubeconfigPath": "string",
  "cfg": {}
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:75`



---


[function] name: dropDisabledDRAResourceClaimConsumableCapacityFields file: pkg/api/resourceclaimspec/util.go:131 returns_error: нет description: —


### dropDisabledDRAResourceClaimConsumableCapacityFields (pkg/api/resourceclaimspec/util.go:131)


dropDisabledDRAResourceClaimConsumableCapacityFields is a function that performs operations based on the provided parameters and returns (new, old *resource.ResourceClaimSpec).


```go
func dropDisabledDRAResourceClaimConsumableCapacityFields((new, old *resource.ResourceClaimSpec)) (new, old *resource.ResourceClaimSpec)
```


**Тип запроса:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** new


```json
{
  "cfgPath": "string",
  "kubeconfigPath": "string",
  "cfg": {}
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


**Тип ответа:** resource.ResourceClaimSpec


```json
{
  "Devices": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/api/resourceclaimspec/util.go:131`




## pkg/api/service/testing/make.go


📄 Исходный файл: `pkg/api/service/testing/make.go`


<details open>
<summary><b>Функции в этом файле (21)</b></summary>


- 🔗 [MakeService](#makeservice-pkgapiservicetestingmakego34) `:34`

- 🔗 [MakeServicePort](#makeserviceport-pkgapiservicetestingmakego112) `:112`

- 🔗 [SetAllocateLoadBalancerNodePorts](#setallocateloadbalancernodeports-pkgapiservicetestingmakego194) `:194`

- 🔗 [SetClusterIP](#setclusterip-pkgapiservicetestingmakego138) `:138`

- 🔗 [SetClusterIPs](#setclusterips-pkgapiservicetestingmakego145) `:145`

- 🔗 [SetExternalName](#setexternalname-pkgapiservicetestingmakego233) `:233`

- 🔗 [SetExternalTrafficPolicy](#setexternaltrafficpolicy-pkgapiservicetestingmakego187) `:187`

- 🔗 [SetHeadless](#setheadless-pkgapiservicetestingmakego122) `:122`

- 🔗 [SetHealthCheckNodePort](#sethealthchecknodeport-pkgapiservicetestingmakego208) `:208`

- 🔗 [SetIPFamilies](#setipfamilies-pkgapiservicetestingmakego153) `:153`

- 🔗 [SetIPFamilyPolicy](#setipfamilypolicy-pkgapiservicetestingmakego160) `:160`

- 🔗 [SetInternalTrafficPolicy](#setinternaltrafficpolicy-pkgapiservicetestingmakego180) `:180`

- 🔗 [SetNodePorts](#setnodeports-pkgapiservicetestingmakego168) `:168`

- 🔗 [SetPorts](#setports-pkgapiservicetestingmakego104) `:104`

- 🔗 [SetSelector](#setselector-pkgapiservicetestingmakego128) `:128`

- 🔗 [SetSessionAffinity](#setsessionaffinity-pkgapiservicetestingmakego215) `:215`

- 🔗 [SetTypeClusterIP](#settypeclusterip-pkgapiservicetestingmakego60) `:60`

- 🔗 [SetTypeExternalName](#settypeexternalname-pkgapiservicetestingmakego93) `:93`

- 🔗 [SetTypeLoadBalancer](#settypeloadbalancer-pkgapiservicetestingmakego83) `:83`

- 🔗 [SetTypeNodePort](#settypenodeport-pkgapiservicetestingmakego73) `:73`

- 🔗 [SetUniqueNodePorts](#setuniquenodeports-pkgapiservicetestingmakego201) `:201`


</details>


[function] name: MakeService file: pkg/api/service/testing/make.go:34 returns_error: нет description: MakeService helps construct Service objects (which pass API validation) more
legibly and tersely than a Go struct defini


### MakeService (pkg/api/service/testing/make.go:34)


MakeService helps construct Service objects (which pass API validation) more
legibly and tersely than a Go struct definition.  By default this produces
a ClusterIP service with a single port and a trivial selector.  The caller
can pass any number of tweak functions to further modify the result.


```go
func MakeService((name string, tweaks ...Tweak)) (name string, tweaks ...Tweak)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** tweaks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Tweak


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:34`



---


[function] name: MakeServicePort file: pkg/api/service/testing/make.go:112 returns_error: нет description: MakeServicePort helps construct ServicePort objects which pass API
validation.


### MakeServicePort (pkg/api/service/testing/make.go:112)


MakeServicePort helps construct ServicePort objects which pass API
validation.


```go
func MakeServicePort((name string, port int, tgtPort intstr.IntOrString, proto api.Protocol)) (name string, port int, tgtPort intstr.IntOrString, proto api.Protocol)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** port


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** tgtPort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** intstr.IntOrString


```json
{
  "Type": {},
  "IntVal": 0,
  "StrVal": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/intstr/intstr.go`


**Тип ответа:** proto


```json
{
  "providerID": "string"
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/controllers/service/controller.go`


**Тип ответа:** api.Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:112`



---


[function] name: SetAllocateLoadBalancerNodePorts file: pkg/api/service/testing/make.go:194 returns_error: нет description: SetAllocateLoadBalancerNodePorts sets the allocate LB node port field.


### SetAllocateLoadBalancerNodePorts (pkg/api/service/testing/make.go:194)


SetAllocateLoadBalancerNodePorts sets the allocate LB node port field.


```go
func SetAllocateLoadBalancerNodePorts((val bool)) (val bool)
```


**Тип ответа:** val


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/admissionregistration/v1beta1/validatingwebhookconfiguration.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:194`



---


[function] name: SetClusterIP file: pkg/api/service/testing/make.go:138 returns_error: нет description: SetClusterIP sets the service ClusterIP fields.


### SetClusterIP (pkg/api/service/testing/make.go:138)


SetClusterIP sets the service ClusterIP fields.


```go
func SetClusterIP((ip string)) (ip string)
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


📍 *Расположение:* `pkg/api/service/testing/make.go:138`



---


[function] name: SetClusterIPs file: pkg/api/service/testing/make.go:145 returns_error: нет description: SetClusterIPs sets the service ClusterIP and ClusterIPs fields.


### SetClusterIPs (pkg/api/service/testing/make.go:145)


SetClusterIPs sets the service ClusterIP and ClusterIPs fields.


```go
func SetClusterIPs((ips ...string)) (ips ...string)
```


**Тип ответа:** ips


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:145`



---


[function] name: SetExternalName file: pkg/api/service/testing/make.go:233 returns_error: нет description: SetExternalName sets the ExternalName field.


### SetExternalName (pkg/api/service/testing/make.go:233)


SetExternalName sets the ExternalName field.


```go
func SetExternalName((val string)) (val string)
```


**Тип ответа:** val


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/admissionregistration/v1beta1/validatingwebhookconfiguration.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:233`



---


[function] name: SetExternalTrafficPolicy file: pkg/api/service/testing/make.go:187 returns_error: нет description: SetExternalTrafficPolicy sets the externalTrafficPolicy field for a Service.


### SetExternalTrafficPolicy (pkg/api/service/testing/make.go:187)


SetExternalTrafficPolicy sets the externalTrafficPolicy field for a Service.


```go
func SetExternalTrafficPolicy((policy api.ServiceExternalTrafficPolicy)) (policy api.ServiceExternalTrafficPolicy)
```


**Тип ответа:** policy


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Тип ответа:** api.ServiceExternalTrafficPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:187`



---


[function] name: SetHeadless file: pkg/api/service/testing/make.go:122 returns_error: нет description: SetHeadless sets the service as headless and clears other fields.


### SetHeadless (pkg/api/service/testing/make.go:122)


SetHeadless sets the service as headless and clears other fields.


```go
func SetHeadless((svc *api.Service)) (svc *api.Service)
```


**Тип запроса:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:122`



---


[function] name: SetHealthCheckNodePort file: pkg/api/service/testing/make.go:208 returns_error: нет description: SetHealthCheckNodePort sets the healthCheckNodePort field for a Service.


### SetHealthCheckNodePort (pkg/api/service/testing/make.go:208)


SetHealthCheckNodePort sets the healthCheckNodePort field for a Service.


```go
func SetHealthCheckNodePort((value int32)) (value int32)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:208`



---


[function] name: SetIPFamilies file: pkg/api/service/testing/make.go:153 returns_error: нет description: SetIPFamilies sets the service IPFamilies field.


### SetIPFamilies (pkg/api/service/testing/make.go:153)


SetIPFamilies sets the service IPFamilies field.


```go
func SetIPFamilies((families ...api.IPFamily)) (families ...api.IPFamily)
```


**Тип ответа:** families


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:153`



---


[function] name: SetIPFamilyPolicy file: pkg/api/service/testing/make.go:160 returns_error: нет description: SetIPFamilyPolicy sets the service IPFamilyPolicy field.


### SetIPFamilyPolicy (pkg/api/service/testing/make.go:160)


SetIPFamilyPolicy sets the service IPFamilyPolicy field.


```go
func SetIPFamilyPolicy((policy api.IPFamilyPolicy)) (policy api.IPFamilyPolicy)
```


**Тип ответа:** policy


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Тип ответа:** api.IPFamilyPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:160`



---


[function] name: SetInternalTrafficPolicy file: pkg/api/service/testing/make.go:180 returns_error: нет description: SetInternalTrafficPolicy sets the internalTrafficPolicy field for a Service.


### SetInternalTrafficPolicy (pkg/api/service/testing/make.go:180)


SetInternalTrafficPolicy sets the internalTrafficPolicy field for a Service.


```go
func SetInternalTrafficPolicy((policy api.ServiceInternalTrafficPolicy)) (policy api.ServiceInternalTrafficPolicy)
```


**Тип ответа:** policy


```json
{
  "Definition": null,
  "Binding": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`


**Тип ответа:** api.ServiceInternalTrafficPolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:180`



---


[function] name: SetNodePorts file: pkg/api/service/testing/make.go:168 returns_error: нет description: SetNodePorts sets the values for each node port, in order.  If less values
are specified than there are ports, the rest 


### SetNodePorts (pkg/api/service/testing/make.go:168)


SetNodePorts sets the values for each node port, in order.  If less values
are specified than there are ports, the rest are untouched.


```go
func SetNodePorts((values ...int)) (values ...int)
```


**Тип ответа:** values


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:168`



---


[function] name: SetPorts file: pkg/api/service/testing/make.go:104 returns_error: нет description: SetPorts sets the service ports list.


### SetPorts (pkg/api/service/testing/make.go:104)


SetPorts sets the service ports list.


```go
func SetPorts((ports ...api.ServicePort)) (ports ...api.ServicePort)
```


**Тип ответа:** ports


```json
{
  "Verbs": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/discovery/helper.go`


**Тип ответа:** api.ServicePort


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


📍 *Расположение:* `pkg/api/service/testing/make.go:104`



---


[function] name: SetSelector file: pkg/api/service/testing/make.go:128 returns_error: нет description: SetSelector sets the service selector.


### SetSelector (pkg/api/service/testing/make.go:128)


SetSelector sets the service selector.


```go
func SetSelector((sel map[string]string)) (sel map[string]string)
```


**Тип ответа:** sel


```json
{
  "name": "string",
  "fieldPath": null,
  "err": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/strategy.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:128`



---


[function] name: SetSessionAffinity file: pkg/api/service/testing/make.go:215 returns_error: нет description: SetSessionAffinity sets the SessionAffinity field.


### SetSessionAffinity (pkg/api/service/testing/make.go:215)


SetSessionAffinity sets the SessionAffinity field.


```go
func SetSessionAffinity((affinity api.ServiceAffinity)) (affinity api.ServiceAffinity)
```


**Тип ответа:** affinity


```json
{
  "hostTrace": []
}
```


*Определено в:* `test/e2e/network/service.go`


**Тип ответа:** api.ServiceAffinity


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/testing/make.go:215`



---


[function] name: SetTypeClusterIP file: pkg/api/service/testing/make.go:60 returns_error: нет description: SetTypeClusterIP sets the service type to ClusterIP and clears other fields.


### SetTypeClusterIP (pkg/api/service/testing/make.go:60)


SetTypeClusterIP sets the service type to ClusterIP and clears other fields.


```go
func SetTypeClusterIP((svc *api.Service)) (svc *api.Service)
```


**Тип запроса:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:60`



---


[function] name: SetTypeExternalName file: pkg/api/service/testing/make.go:93 returns_error: нет description: SetTypeExternalName sets the service type to ExternalName and clears other fields.


### SetTypeExternalName (pkg/api/service/testing/make.go:93)


SetTypeExternalName sets the service type to ExternalName and clears other fields.


```go
func SetTypeExternalName((svc *api.Service)) (svc *api.Service)
```


**Тип запроса:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:93`



---


[function] name: SetTypeLoadBalancer file: pkg/api/service/testing/make.go:83 returns_error: нет description: SetTypeLoadBalancer sets the service type to LoadBalancer and clears other fields.


### SetTypeLoadBalancer (pkg/api/service/testing/make.go:83)


SetTypeLoadBalancer sets the service type to LoadBalancer and clears other fields.


```go
func SetTypeLoadBalancer((svc *api.Service)) (svc *api.Service)
```


**Тип запроса:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:83`



---


[function] name: SetTypeNodePort file: pkg/api/service/testing/make.go:73 returns_error: нет description: SetTypeNodePort sets the service type to NodePort and clears other fields.


### SetTypeNodePort (pkg/api/service/testing/make.go:73)


SetTypeNodePort sets the service type to NodePort and clears other fields.


```go
func SetTypeNodePort((svc *api.Service)) (svc *api.Service)
```


**Тип запроса:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:73`



---


[function] name: SetUniqueNodePorts file: pkg/api/service/testing/make.go:201 returns_error: нет description: SetUniqueNodePorts sets all nodeports to unique values.


### SetUniqueNodePorts (pkg/api/service/testing/make.go:201)


SetUniqueNodePorts sets all nodeports to unique values.


```go
func SetUniqueNodePorts((svc *api.Service)) (svc *api.Service)
```


**Тип запроса:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/testing/make.go:201`




## pkg/api/service/util.go


📄 Исходный файл: `pkg/api/service/util.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [ExternallyAccessible](#externallyaccessible-pkgapiserviceutilgo71) `:71`

- 🔗 [GetLoadBalancerSourceRanges](#getloadbalancersourceranges-pkgapiserviceutilgo44) `:44`

- 🔗 [IsAllowAll](#isallowall-pkgapiserviceutilgo32) `:32`

- 🔗 [NeedsHealthCheck](#needshealthcheck-pkgapiserviceutilgo88) `:88`

- 🔗 [RequestsOnlyLocalTraffic](#requestsonlylocaltraffic-pkgapiserviceutilgo78) `:78`


</details>


[function] name: ExternallyAccessible file: pkg/api/service/util.go:71 returns_error: нет description: ExternallyAccessible checks if service is externally accessible.


### ExternallyAccessible (pkg/api/service/util.go:71)


ExternallyAccessible checks if service is externally accessible.


```go
func ExternallyAccessible((service *api.Service)) (service *api.Service)
```


**Тип запроса:** api.Service


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


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/util.go:71`



---


[function] name: GetLoadBalancerSourceRanges file: pkg/api/service/util.go:44 returns_error: да description: GetLoadBalancerSourceRanges first try to parse and verify LoadBalancerSourceRanges field from a service.
If the field is


### GetLoadBalancerSourceRanges (pkg/api/service/util.go:44)


GetLoadBalancerSourceRanges first try to parse and verify LoadBalancerSourceRanges field from a service.
If the field is not specified, turn to parse and verify the AnnotationLoadBalancerSourceRangesKey annotation from a service,
extracting the source ranges to allow, and if not present returns a default (allow-all) value.


```go
func GetLoadBalancerSourceRanges((utilnet.IPNetSet, error)) (utilnet.IPNetSet, error)
```


**Тип ответа:** utilnet.IPNetSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `utilnet.IPNetSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/service/util.go:44`



---


[function] name: IsAllowAll file: pkg/api/service/util.go:32 returns_error: нет description: IsAllowAll checks whether the utilnet.IPNet allows traffic from 0.0.0.0/0


### IsAllowAll (pkg/api/service/util.go:32)


IsAllowAll checks whether the utilnet.IPNet allows traffic from 0.0.0.0/0


```go
func IsAllowAll((ipnets utilnet.IPNetSet)) (ipnets utilnet.IPNetSet)
```


**Тип ответа:** ipnets


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilnet.IPNetSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/service/util.go:32`



---


[function] name: NeedsHealthCheck file: pkg/api/service/util.go:88 returns_error: нет description: NeedsHealthCheck checks if service needs health check.


### NeedsHealthCheck (pkg/api/service/util.go:88)


NeedsHealthCheck checks if service needs health check.


```go
func NeedsHealthCheck((service *api.Service)) (service *api.Service)
```


**Тип запроса:** api.Service


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


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/util.go:88`



---


[function] name: RequestsOnlyLocalTraffic file: pkg/api/service/util.go:78 returns_error: нет description: RequestsOnlyLocalTraffic checks if service requests OnlyLocal traffic.


### RequestsOnlyLocalTraffic (pkg/api/service/util.go:78)


RequestsOnlyLocalTraffic checks if service requests OnlyLocal traffic.


```go
func RequestsOnlyLocalTraffic((service *api.Service)) (service *api.Service)
```


**Тип запроса:** api.Service


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


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/util.go:78`




## pkg/api/service/warnings.go


📄 Исходный файл: `pkg/api/service/warnings.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetWarningsForService](#getwarningsforservice-pkgapiservicewarningsgo28) `:28`

- 🔗 [isHeadlessService](#isheadlessservice-pkgapiservicewarningsgo82) `:82`


</details>


[function] name: GetWarningsForService file: pkg/api/service/warnings.go:28 returns_error: нет description: —


### GetWarningsForService (pkg/api/service/warnings.go:28)


GetWarningsForService is a function that retrieves data based on the provided parameters and returns (service, oldService *api.Service).


```go
func GetWarningsForService((service, oldService *api.Service)) (service, oldService *api.Service)
```


**Тип запроса:** api.Service


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


**Тип ответа:** oldService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/warnings.go:28`



---


[function] name: isHeadlessService file: pkg/api/service/warnings.go:82 returns_error: нет description: —


### isHeadlessService (pkg/api/service/warnings.go:82)


isHeadlessService is a function that performs operations based on the provided parameters and returns (service *api.Service).


```go
func isHeadlessService((service *api.Service)) (service *api.Service)
```


**Тип запроса:** api.Service


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


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/service/warnings.go:82`




## pkg/api/servicecidr/servicecidr.go


📄 Исходный файл: `pkg/api/servicecidr/servicecidr.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [ContainsAddress](#containsaddress-pkgapiservicecidrservicecidrgo76) `:76`

- 🔗 [ContainsIP](#containsip-pkgapiservicecidrservicecidrgo70) `:70`

- 🔗 [ContainsPrefix](#containsprefix-pkgapiservicecidrservicecidrgo50) `:50`

- 🔗 [IPToAddr](#iptoaddr-pkgapiservicecidrservicecidrgo146) `:146`

- 🔗 [OverlapsPrefix](#overlapsprefix-pkgapiservicecidrservicecidrgo30) `:30`

- 🔗 [PrefixContainsIP](#prefixcontainsip-pkgapiservicecidrservicecidrgo100) `:100`

- 🔗 [broadcastAddress](#broadcastaddress-pkgapiservicecidrservicecidrgo120) `:120`


</details>


[function] name: ContainsAddress file: pkg/api/servicecidr/servicecidr.go:76 returns_error: нет description: ContainsAddress return the list of ServiceCIDR that contains the address passed as argument


### ContainsAddress (pkg/api/servicecidr/servicecidr.go:76)


ContainsAddress return the list of ServiceCIDR that contains the address passed as argument


```go
func ContainsAddress((serviceCIDRLister networkinglisters.ServiceCIDRLister, address netip.Addr)) (serviceCIDRLister networkinglisters.ServiceCIDRLister, address netip.Addr)
```


**Тип ответа:** serviceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** networkinglisters.ServiceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** address


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** netip.Addr


```json
{
  "Namespace": "string",
  "Port": 0
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


📍 *Расположение:* `pkg/api/servicecidr/servicecidr.go:76`



---


[function] name: ContainsIP file: pkg/api/servicecidr/servicecidr.go:70 returns_error: нет description: ContainsIP return the list of ServiceCIDR that contains the IP address passed as argument


### ContainsIP (pkg/api/servicecidr/servicecidr.go:70)


ContainsIP return the list of ServiceCIDR that contains the IP address passed as argument


```go
func ContainsIP((serviceCIDRLister networkinglisters.ServiceCIDRLister, ip net.IP)) (serviceCIDRLister networkinglisters.ServiceCIDRLister, ip net.IP)
```


**Тип ответа:** serviceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** networkinglisters.ServiceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/api/servicecidr/servicecidr.go:70`



---


[function] name: ContainsPrefix file: pkg/api/servicecidr/servicecidr.go:50 returns_error: нет description: ContainsPrefix return the list of ServiceCIDR that contains the prefix passed as argument


### ContainsPrefix (pkg/api/servicecidr/servicecidr.go:50)


ContainsPrefix return the list of ServiceCIDR that contains the prefix passed as argument


```go
func ContainsPrefix((serviceCIDRLister networkinglisters.ServiceCIDRLister, prefix netip.Prefix)) (serviceCIDRLister networkinglisters.ServiceCIDRLister, prefix netip.Prefix)
```


**Тип ответа:** serviceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** networkinglisters.ServiceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** netip.Prefix


```json
{
  "Claim": "string",
  "Prefix": "string",
  "Expression": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


📍 *Расположение:* `pkg/api/servicecidr/servicecidr.go:50`



---


[function] name: IPToAddr file: pkg/api/servicecidr/servicecidr.go:146 returns_error: нет description: IPToAddr converts a net.IP to a netip.Addr
if the net.IP is not valid it returns an empty netip.Addr{}


### IPToAddr (pkg/api/servicecidr/servicecidr.go:146)


IPToAddr converts a net.IP to a netip.Addr
if the net.IP is not valid it returns an empty netip.Addr{}


```go
func IPToAddr((ip net.IP)) (ip net.IP)
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


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/api/servicecidr/servicecidr.go:146`



---


[function] name: OverlapsPrefix file: pkg/api/servicecidr/servicecidr.go:30 returns_error: нет description: OverlapsPrefix return the list of ServiceCIDR that overlaps with the prefix passed as argument


### OverlapsPrefix (pkg/api/servicecidr/servicecidr.go:30)


OverlapsPrefix return the list of ServiceCIDR that overlaps with the prefix passed as argument


```go
func OverlapsPrefix((serviceCIDRLister networkinglisters.ServiceCIDRLister, prefix netip.Prefix)) (serviceCIDRLister networkinglisters.ServiceCIDRLister, prefix netip.Prefix)
```


**Тип ответа:** serviceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** networkinglisters.ServiceCIDRLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** netip.Prefix


```json
{
  "Claim": "string",
  "Prefix": "string",
  "Expression": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


📍 *Расположение:* `pkg/api/servicecidr/servicecidr.go:30`



---


[function] name: PrefixContainsIP file: pkg/api/servicecidr/servicecidr.go:100 returns_error: нет description: PrefixContainsIP returns true if the given IP is contained with the prefix,
is not the network address and also, if IPv4


### PrefixContainsIP (pkg/api/servicecidr/servicecidr.go:100)


PrefixContainsIP returns true if the given IP is contained with the prefix,
is not the network address and also, if IPv4, is not the broadcast address.
This is required (rather than just `prefix.Contains(ip)`) because a ServiceCIDR
covering prefix will not allocate those IPs, so a service with one of those IPs
can't belong to that ServiceCIDR.


```go
func PrefixContainsIP((prefix netip.Prefix, ip netip.Addr)) (prefix netip.Prefix, ip netip.Addr)
```


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** netip.Prefix


```json
{
  "Claim": "string",
  "Prefix": "string",
  "Expression": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1alpha1/types.go`


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


**Тип ответа:** netip.Addr


```json
{
  "Namespace": "string",
  "Port": 0
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


📍 *Расположение:* `pkg/api/servicecidr/servicecidr.go:100`



---


[function] name: broadcastAddress file: pkg/api/servicecidr/servicecidr.go:120 returns_error: да description: broadcastAddress returns the broadcast address of the subnet
The broadcast address is obtained by setting all the host b


### broadcastAddress (pkg/api/servicecidr/servicecidr.go:120)


broadcastAddress returns the broadcast address of the subnet
The broadcast address is obtained by setting all the host bits
in a subnet to 1.
network 192.168.0.0/24 : subnet bits 24 host bits 32 - 24 = 8
broadcast address 192.168.0.255


```go
func broadcastAddress((netip.Addr, error)) (netip.Addr, error)
```


**Тип ответа:** netip.Addr


```json
{
  "Namespace": "string",
  "Port": 0
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `netip.Addr`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/servicecidr/servicecidr.go:120`




## pkg/api/storage/util.go


📄 Исходный файл: `pkg/api/storage/util.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetWarningsForCSIStorageCapacity](#getwarningsforcsistoragecapacity-pkgapistorageutilgo44) `:44`

- 🔗 [GetWarningsForStorageClass](#getwarningsforstorageclass-pkgapistorageutilgo27) `:27`


</details>


[function] name: GetWarningsForCSIStorageCapacity file: pkg/api/storage/util.go:44 returns_error: нет description: —


### GetWarningsForCSIStorageCapacity (pkg/api/storage/util.go:44)


GetWarningsForCSIStorageCapacity is a function that retrieves data based on the provided parameters and returns (csc *storage.CSIStorageCapacity).


```go
func GetWarningsForCSIStorageCapacity((csc *storage.CSIStorageCapacity)) (csc *storage.CSIStorageCapacity)
```


**Тип запроса:** storage.CSIStorageCapacity


```json
{
  "NodeTopology": null,
  "StorageClassName": "string",
  "Capacity": null,
  "MaximumVolumeSize": null
}
```


*Определено в:* `pkg/apis/storage/types.go`


**Тип ответа:** csc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** storage.CSIStorageCapacity


```json
{
  "NodeTopology": null,
  "StorageClassName": "string",
  "Capacity": null,
  "MaximumVolumeSize": null
}
```


*Определено в:* `pkg/apis/storage/types.go`


📍 *Расположение:* `pkg/api/storage/util.go:44`



---


[function] name: GetWarningsForStorageClass file: pkg/api/storage/util.go:27 returns_error: нет description: —


### GetWarningsForStorageClass (pkg/api/storage/util.go:27)


GetWarningsForStorageClass is a function that retrieves data based on the provided parameters and returns (sc *storage.StorageClass).


```go
func GetWarningsForStorageClass((sc *storage.StorageClass)) (sc *storage.StorageClass)
```


**Тип запроса:** storage.StorageClass


```json
{
  "Provisioner": "string",
  "Parameters": {},
  "ReclaimPolicy": null,
  "MountOptions": [],
  "AllowVolumeExpansion": false,
  "VolumeBindingMode": null,
  "AllowedTopologies": []
}
```


*Определено в:* `pkg/apis/storage/types.go`


**Тип ответа:** sc


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


**Тип ответа:** storage.StorageClass


```json
{
  "Provisioner": "string",
  "Parameters": {},
  "ReclaimPolicy": null,
  "MountOptions": [],
  "AllowVolumeExpansion": false,
  "VolumeBindingMode": null,
  "AllowedTopologies": []
}
```


*Определено в:* `pkg/apis/storage/types.go`


📍 *Расположение:* `pkg/api/storage/util.go:27`




## pkg/api/testing/compat/compatibility_tester.go


📄 Исходный файл: `pkg/api/testing/compat/compatibility_tester.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [TestCompatibility](#testcompatibility-pkgapitestingcompatcompatibility_testergo38) `:38`

- 🔗 [getJSONValue](#getjsonvalue-pkgapitestingcompatcompatibility_testergo100) `:100`


</details>


[function] name: TestCompatibility file: pkg/api/testing/compat/compatibility_tester.go:38 returns_error: нет description: TestCompatibility reencodes the input using the codec for the given
version and checks for the presence of the expected 


### TestCompatibility (pkg/api/testing/compat/compatibility_tester.go:38)


TestCompatibility reencodes the input using the codec for the given
version and checks for the presence of the expected keys and absent
keys in the resulting JSON.
Based on: https://github.com/openshift/origin/blob/master/pkg/api/compatibility_test.go


```go
func TestCompatibility((
	t *testing.T,
	version schema.GroupVersion,
	input []byte,
	validator func(obj runtime.Object) field.ErrorList,
	expectedKeys map[string]string,
	absentKeys []string,
)) (
	t *testing.T,
	version schema.GroupVersion,
	input []byte,
	validator func(obj runtime.Object) field.ErrorList,
	expectedKeys map[string]string,
	absentKeys []string,
)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


**Тип ответа:** schema.GroupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** input


```json
{
  "builder": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/client-gen/args/gvpackages.go`


**Тип ответа:** validator


```json
{
  "getter": {}
}
```


*Определено в:* `pkg/serviceaccount/claims.go`


**Тип ответа:** func


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


**Тип ответа:** field.ErrorList


```json
{
  "SchemaErrors": {},
  "CELErrors": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`


**Тип ответа:** expectedKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** absentKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/testing/compat/compatibility_tester.go:38`



---


[function] name: getJSONValue file: pkg/api/testing/compat/compatibility_tester.go:100 returns_error: да description: —


### getJSONValue (pkg/api/testing/compat/compatibility_tester.go:100)


getJSONValue is a function that performs operations based on the provided parameters and may return an error.


```go
func getJSONValue((interface{}, bool, error)) (interface{}, bool, error)
```


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `interface{}`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/testing/compat/compatibility_tester.go:100`




## pkg/api/testing/conversion.go


📄 Исходный файл: `pkg/api/testing/conversion.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TestSelectableFieldLabelConversionsOfKind](#testselectablefieldlabelconversionsofkind-pkgapitestingconversiongo31) `:31`


</details>


[function] name: TestSelectableFieldLabelConversionsOfKind file: pkg/api/testing/conversion.go:31 returns_error: нет description: TestSelectableFieldLabelConversionsOfKind verifies that given resource have field
label conversion defined for each its 


### TestSelectableFieldLabelConversionsOfKind (pkg/api/testing/conversion.go:31)


TestSelectableFieldLabelConversionsOfKind verifies that given resource have field
label conversion defined for each its selectable field.
fields contains selectable fields of the resource.
labelMap maps deprecated labels to their canonical names.


```go
func TestSelectableFieldLabelConversionsOfKind((t *testing.T, apiVersion string, kind string, fields fields.Set, labelMap map[string]string)) (t *testing.T, apiVersion string, kind string, fields fields.Set, labelMap map[string]string)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** apiVersion


```json
{
  "client": {},
  "prefVersion": null,
  "mu": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/discovery.go`


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


**Тип ответа:** fields


```json
{
  "Recursive": false
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/explain/fields_printer_builder.go`


**Тип ответа:** fields.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Тип ответа:** labelMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/api/testing/conversion.go:31`




## pkg/api/testing/fuzzer.go


📄 Исходный файл: `pkg/api/testing/fuzzer.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [overrideGenericFuncs](#overridegenericfuncs-pkgapitestingfuzzergo52) `:52`


</details>


[function] name: overrideGenericFuncs file: pkg/api/testing/fuzzer.go:52 returns_error: нет description: overrideGenericFuncs override some generic fuzzer funcs from k8s.io/apiserver in order to have more realistic
values in 


### overrideGenericFuncs (pkg/api/testing/fuzzer.go:52)


overrideGenericFuncs override some generic fuzzer funcs from k8s.io/apiserver in order to have more realistic
values in a Kubernetes context.


```go
func overrideGenericFuncs((codecs runtimeserializer.CodecFactory)) (codecs runtimeserializer.CodecFactory)
```


**Тип ответа:** codecs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** runtimeserializer.CodecFactory


```json
{
  "scheme": null,
  "universal": {},
  "accepts": [],
  "legacySerializer": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/codec_factory.go`


📍 *Расположение:* `pkg/api/testing/fuzzer.go:52`




## pkg/api/testing/validation.go


📄 Исходный файл: `pkg/api/testing/validation.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [VerifyUpdateValidationEquivalence](#verifyupdatevalidationequivalence-pkgapitestingvalidationgo303) `:303`

- 🔗 [VerifyValidationEquivalence](#verifyvalidationequivalence-pkgapitestingvalidationgo272) `:272`

- 🔗 [VerifyVersionedValidationEquivalence](#verifyversionedvalidationequivalence-pkgapitestingvalidationgo50) `:50`

- 🔗 [WithFuzzer](#withfuzzer-pkgapitestingvalidationgo248) `:248`

- 🔗 [WithIgnoreObjectConversionErrors](#withignoreobjectconversionerrors-pkgapitestingvalidationgo242) `:242`

- 🔗 [WithNormalizationRules](#withnormalizationrules-pkgapitestingvalidationgo236) `:236`

- 🔗 [WithSubResources](#withsubresources-pkgapitestingvalidationgo230) `:230`

- 🔗 [convertToInternal](#converttointernal-pkgapitestingvalidationgo191) `:191`

- 🔗 [deDuplicateErrors](#deduplicateerrors-pkgapitestingvalidationgo441) `:441`

- 🔗 [fmtErrs](#fmterrs-pkgapitestingvalidationgo175) `:175`

- 🔗 [verifyValidationEquivalence](#verifyvalidationequivalence-pkgapitestingvalidationgo317) `:317`


</details>


[function] name: VerifyUpdateValidationEquivalence file: pkg/api/testing/validation.go:303 returns_error: нет description: VerifyUpdateValidationEquivalence provides a helper for testing the migration from
hand-written imperative validation to


### VerifyUpdateValidationEquivalence (pkg/api/testing/validation.go:303)


VerifyUpdateValidationEquivalence provides a helper for testing the migration from
hand-written imperative validation to declarative validation for update operations.
It ensures that the validation logic remains consistent before and after the feature is enabled.

The function operates by running the provided validation function under four scenarios:
1. With DeclarativeValidation and DeclarativeValidationBeta feature gates enabled,
using the new declarative validation rules (Beta stage).
2. With DeclarativeValidation enabled and DeclarativeValidationBeta disabled,
using the new declarative validation rules (Standard stage).
3. With DeclarativeValidation and DeclarativeValidationTakeover feature gates disabled,
simulating the legacy hand-written validation.
4. With all declarative rules enforced (including Alpha), ensuring that the full set of
declarative validations is correctly implemented (testing only).

It then asserts that the validation errors produced in all scenarios are equivalent,
guaranteeing a safe migration. It also checks the errors against an expected set.
It compares errors by field, origin and type; all three should match to be called equivalent.
It also make sure all versions of the given API returns equivalent errors.


```go
func VerifyUpdateValidationEquivalence((t *testing.T, ctx context.Context, obj, old runtime.Object, validateUpdateFn ValidateUpdateFunc, expectedErrs field.ErrorList, testConfigs ...ValidationTestConfig)) (t *testing.T, ctx context.Context, obj, old runtime.Object, validateUpdateFn ValidateUpdateFunc, expectedErrs field.ErrorList, testConfigs ...ValidationTestConfig)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


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


**Тип ответа:** validateUpdateFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateUpdateFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** expectedErrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.ErrorList


```json
{
  "SchemaErrors": {},
  "CELErrors": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`


**Тип ответа:** testConfigs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidationTestConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/testing/validation.go:303`



---


[function] name: VerifyValidationEquivalence file: pkg/api/testing/validation.go:272 returns_error: нет description: VerifyValidationEquivalence provides a helper for testing the migration from
hand-written imperative validation to decla


### VerifyValidationEquivalence (pkg/api/testing/validation.go:272)


VerifyValidationEquivalence provides a helper for testing the migration from
hand-written imperative validation to declarative validation. It ensures that
the validation logic remains consistent before and after the feature is enabled.

The function operates by running the provided validation function under four scenarios:
1. With DeclarativeValidation and DeclarativeValidationBeta feature gates enabled,
using the new declarative validation rules (Beta stage).
2. With DeclarativeValidation enabled and DeclarativeValidationBeta disabled,
using the new declarative validation rules (Standard stage).
3. With DeclarativeValidation and DeclarativeValidationTakeover feature gates disabled,
simulating the legacy hand-written validation.
4. With all declarative rules enforced (including Alpha), ensuring that the full set of
declarative validations is correctly implemented (testing only).

It then asserts that the validation errors produced in all scenarios are equivalent,
guaranteeing a safe migration. It also checks the errors against an expected set.
It compares errors by field, origin and type; all three should match to be called equivalent.
It also make sure all versions of the given API returns equivalent errors.


```go
func VerifyValidationEquivalence((t *testing.T, ctx context.Context, obj runtime.Object, validateFn ValidateFunc, expectedErrs field.ErrorList, testConfigs ...ValidationTestConfig)) (t *testing.T, ctx context.Context, obj runtime.Object, validateFn ValidateFunc, expectedErrs field.ErrorList, testConfigs ...ValidationTestConfig)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** validateFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** expectedErrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.ErrorList


```json
{
  "SchemaErrors": {},
  "CELErrors": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`


**Тип ответа:** testConfigs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidationTestConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/testing/validation.go:272`



---


[function] name: VerifyVersionedValidationEquivalence file: pkg/api/testing/validation.go:50 returns_error: нет description: VerifyVersionedValidationEquivalence tests that all versions of an API return equivalent validation errors.
It accepts o


### VerifyVersionedValidationEquivalence (pkg/api/testing/validation.go:50)


VerifyVersionedValidationEquivalence tests that all versions of an API return equivalent validation errors.
It accepts optional configuration to handle path normalization across API versions where structures differ.


```go
func VerifyVersionedValidationEquivalence((t *testing.T, obj, old runtime.Object, testConfigs ...ValidationTestConfig)) (t *testing.T, obj, old runtime.Object, testConfigs ...ValidationTestConfig)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


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


**Тип ответа:** testConfigs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidationTestConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/testing/validation.go:50`



---


[function] name: WithFuzzer file: pkg/api/testing/validation.go:248 returns_error: нет description: —


### WithFuzzer (pkg/api/testing/validation.go:248)


WithFuzzer is a function that performs operations based on the provided parameters and returns (fuzzer *randfill.Filler).


```go
func WithFuzzer((fuzzer *randfill.Filler)) (fuzzer *randfill.Filler)
```


**Тип запроса:** randfill.Filler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fuzzer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** randfill.Filler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/testing/validation.go:248`



---


[function] name: WithIgnoreObjectConversionErrors file: pkg/api/testing/validation.go:242 returns_error: нет description: —


### WithIgnoreObjectConversionErrors (pkg/api/testing/validation.go:242)


WithIgnoreObjectConversionErrors is a function that performs operations based on the provided parameters and returns ().


```go
func WithIgnoreObjectConversionErrors(()) ()
```


📍 *Расположение:* `pkg/api/testing/validation.go:242`



---


[function] name: WithNormalizationRules file: pkg/api/testing/validation.go:236 returns_error: нет description: —


### WithNormalizationRules (pkg/api/testing/validation.go:236)


WithNormalizationRules is a function that performs operations based on the provided parameters and returns (rules ...field.NormalizationRule).


```go
func WithNormalizationRules((rules ...field.NormalizationRule)) (rules ...field.NormalizationRule)
```


**Тип ответа:** rules


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.NormalizationRule


```json
{
  "Regexp": null,
  "Replacement": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/error_matcher.go`


📍 *Расположение:* `pkg/api/testing/validation.go:236`



---


[function] name: WithSubResources file: pkg/api/testing/validation.go:230 returns_error: нет description: —


### WithSubResources (pkg/api/testing/validation.go:230)


WithSubResources is a function that performs operations based on the provided parameters and returns (subResources ...string).


```go
func WithSubResources((subResources ...string)) (subResources ...string)
```


**Тип ответа:** subResources


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/testing/validation.go:230`



---


[function] name: convertToInternal file: pkg/api/testing/validation.go:191 returns_error: да description: —


### convertToInternal (pkg/api/testing/validation.go:191)


convertToInternal is a function that performs operations based on the provided parameters and may return an error.


```go
func convertToInternal((runtime.Object, error)) (runtime.Object, error)
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


📍 *Расположение:* `pkg/api/testing/validation.go:191`



---


[function] name: deDuplicateErrors file: pkg/api/testing/validation.go:441 returns_error: нет description: deDuplicateErrors removes duplicate errors from an ErrorList based on the provided matcher.


### deDuplicateErrors (pkg/api/testing/validation.go:441)


deDuplicateErrors removes duplicate errors from an ErrorList based on the provided matcher.


```go
func deDuplicateErrors((errs field.ErrorList, matcher field.ErrorMatcher)) (errs field.ErrorList, matcher field.ErrorMatcher)
```


**Тип ответа:** errs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.ErrorList


```json
{
  "SchemaErrors": {},
  "CELErrors": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`


**Тип ответа:** matcher


```json
{
  "match": {},
  "failure": {}
}
```


*Определено в:* `test/e2e/framework/expect.go`


**Тип ответа:** field.ErrorMatcher


```json
{
  "matchType": false,
  "matchField": false,
  "matchValue": false,
  "matchOrigin": false,
  "matchDetail": {},
  "requireOriginWhenInvalid": false,
  "matchValidationStabilityLevel": false,
  "matchSource": false,
  "normalizationRules": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/error_matcher.go`


📍 *Расположение:* `pkg/api/testing/validation.go:441`



---


[function] name: fmtErrs file: pkg/api/testing/validation.go:175 returns_error: нет description: helper for nicer output


### fmtErrs (pkg/api/testing/validation.go:175)


helper for nicer output


```go
func fmtErrs((errs field.ErrorList)) (errs field.ErrorList)
```


**Тип ответа:** errs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.ErrorList


```json
{
  "SchemaErrors": {},
  "CELErrors": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`


📍 *Расположение:* `pkg/api/testing/validation.go:175`



---


[function] name: verifyValidationEquivalence file: pkg/api/testing/validation.go:317 returns_error: нет description: verifyValidationEquivalence is a generic helper that verifies validation equivalence with and without declarative valida


### verifyValidationEquivalence (pkg/api/testing/validation.go:317)


verifyValidationEquivalence is a generic helper that verifies validation equivalence with and without declarative validation.


```go
func verifyValidationEquivalence((t *testing.T, expectedErrs field.ErrorList, runValidations func(context.Context) field.ErrorList, ctx context.Context, opt *validationOption)) (t *testing.T, expectedErrs field.ErrorList, runValidations func(context.Context) field.ErrorList, ctx context.Context, opt *validationOption)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** validationOption


```json
{
  "SubResources": [],
  "NormalizationRules": [],
  "IgnoreObjectConversionErrors": false,
  "Fuzzer": null
}
```


*Определено в:* `pkg/api/testing/validation.go`


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** expectedErrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.ErrorList


```json
{
  "SchemaErrors": {},
  "CELErrors": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`


**Тип ответа:** runValidations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** field.ErrorList


```json
{
  "SchemaErrors": {},
  "CELErrors": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`


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


**Тип ответа:** opt


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


**Тип ответа:** validationOption


```json
{
  "SubResources": [],
  "NormalizationRules": [],
  "IgnoreObjectConversionErrors": false,
  "Fuzzer": null
}
```


*Определено в:* `pkg/api/testing/validation.go`


📍 *Расположение:* `pkg/api/testing/validation.go:317`




## pkg/api/v1/endpoints/util.go


📄 Исходный файл: `pkg/api/v1/endpoints/util.go`


<details open>
<summary><b>Функции в этом файле (20)</b></summary>


- 🔗 [Len](#len-pkgapiv1endpointsutilgo169) `:169`

- 🔗 [Len](#len-pkgapiv1endpointsutilgo210) `:210`

- 🔗 [Len](#len-pkgapiv1endpointsutilgo221) `:221`

- 🔗 [Len](#len-pkgapiv1endpointsutilgo229) `:229`

- 🔗 [Less](#less-pkgapiv1endpointsutilgo171) `:171`

- 🔗 [Less](#less-pkgapiv1endpointsutilgo212) `:212`

- 🔗 [Less](#less-pkgapiv1endpointsutilgo223) `:223`

- 🔗 [Less](#less-pkgapiv1endpointsutilgo231) `:231`

- 🔗 [LessEndpointAddress](#lessendpointaddress-pkgapiv1endpointsutilgo176) `:176`

- 🔗 [RepackSubsets](#repacksubsets-pkgapiv1endpointsutilgo35) `:35`

- 🔗 [SortSubsets](#sortsubsets-pkgapiv1endpointsutilgo192) `:192`

- 🔗 [Swap](#swap-pkgapiv1endpointsutilgo170) `:170`

- 🔗 [Swap](#swap-pkgapiv1endpointsutilgo211) `:211`

- 🔗 [Swap](#swap-pkgapiv1endpointsutilgo222) `:222`

- 🔗 [Swap](#swap-pkgapiv1endpointsutilgo230) `:230`

- 🔗 [hashAddresses](#hashaddresses-pkgapiv1endpointsutilgo147) `:147`

- 🔗 [hashObject](#hashobject-pkgapiv1endpointsutilgo203) `:203`

- 🔗 [lessAddrReady](#lessaddrready-pkgapiv1endpointsutilgo162) `:162`

- 🔗 [mapAddressByPort](#mapaddressbyport-pkgapiv1endpointsutilgo107) `:107`

- 🔗 [mapAddressesByPort](#mapaddressesbyport-pkgapiv1endpointsutilgo96) `:96`


</details>


[function] name: Len file: pkg/api/v1/endpoints/util.go:169 returns_error: нет description: —


### Len (pkg/api/v1/endpoints/util.go:169)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (sl addrsReady) Len(()) ()
```


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:169`



---


[function] name: Len file: pkg/api/v1/endpoints/util.go:210 returns_error: нет description: —


### Len (pkg/api/v1/endpoints/util.go:210)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (sl subsetsByHash) Len(()) ()
```


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:210`



---


[function] name: Len file: pkg/api/v1/endpoints/util.go:221 returns_error: нет description: —


### Len (pkg/api/v1/endpoints/util.go:221)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (sl addrsByIPAndUID) Len(()) ()
```


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:221`



---


[function] name: Len file: pkg/api/v1/endpoints/util.go:229 returns_error: нет description: —


### Len (pkg/api/v1/endpoints/util.go:229)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (sl portsByHash) Len(()) ()
```


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:229`



---


[function] name: Less file: pkg/api/v1/endpoints/util.go:171 returns_error: нет description: —


### Less (pkg/api/v1/endpoints/util.go:171)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl addrsReady) Less((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:171`



---


[function] name: Less file: pkg/api/v1/endpoints/util.go:212 returns_error: нет description: —


### Less (pkg/api/v1/endpoints/util.go:212)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl subsetsByHash) Less((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:212`



---


[function] name: Less file: pkg/api/v1/endpoints/util.go:223 returns_error: нет description: —


### Less (pkg/api/v1/endpoints/util.go:223)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl addrsByIPAndUID) Less((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:223`



---


[function] name: Less file: pkg/api/v1/endpoints/util.go:231 returns_error: нет description: —


### Less (pkg/api/v1/endpoints/util.go:231)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl portsByHash) Less((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:231`



---


[function] name: LessEndpointAddress file: pkg/api/v1/endpoints/util.go:176 returns_error: нет description: LessEndpointAddress compares IP addresses lexicographically and returns true if first argument is lesser than second


### LessEndpointAddress (pkg/api/v1/endpoints/util.go:176)


LessEndpointAddress compares IP addresses lexicographically and returns true if first argument is lesser than second


```go
func LessEndpointAddress((a, b *v1.EndpointAddress)) (a, b *v1.EndpointAddress)
```


**Тип запроса:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:176`



---


[function] name: RepackSubsets file: pkg/api/v1/endpoints/util.go:35 returns_error: нет description: RepackSubsets takes a slice of EndpointSubset objects, expands it to the full
representation, and then repacks that into


### RepackSubsets (pkg/api/v1/endpoints/util.go:35)


RepackSubsets takes a slice of EndpointSubset objects, expands it to the full
representation, and then repacks that into the canonical layout.  This
ensures that code which operates on these objects can rely on the common
form for things like comparison.  The result is a newly allocated slice.


```go
func RepackSubsets((subsets []v1.EndpointSubset)) (subsets []v1.EndpointSubset)
```


**Тип ответа:** subsets


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.EndpointSubset


```json
{
  "Addresses": [],
  "NotReadyAddresses": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:35`



---


[function] name: SortSubsets file: pkg/api/v1/endpoints/util.go:192 returns_error: нет description: SortSubsets sorts an array of EndpointSubset objects in place.  For ease of
use it returns the input slice.


### SortSubsets (pkg/api/v1/endpoints/util.go:192)


SortSubsets sorts an array of EndpointSubset objects in place.  For ease of
use it returns the input slice.


```go
func SortSubsets((subsets []v1.EndpointSubset)) (subsets []v1.EndpointSubset)
```


**Тип ответа:** subsets


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.EndpointSubset


```json
{
  "Addresses": [],
  "NotReadyAddresses": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:192`



---


[function] name: Swap file: pkg/api/v1/endpoints/util.go:170 returns_error: нет description: —


### Swap (pkg/api/v1/endpoints/util.go:170)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl addrsReady) Swap((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:170`



---


[function] name: Swap file: pkg/api/v1/endpoints/util.go:211 returns_error: нет description: —


### Swap (pkg/api/v1/endpoints/util.go:211)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl subsetsByHash) Swap((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:211`



---


[function] name: Swap file: pkg/api/v1/endpoints/util.go:222 returns_error: нет description: —


### Swap (pkg/api/v1/endpoints/util.go:222)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl addrsByIPAndUID) Swap((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:222`



---


[function] name: Swap file: pkg/api/v1/endpoints/util.go:230 returns_error: нет description: —


### Swap (pkg/api/v1/endpoints/util.go:230)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (sl portsByHash) Swap((i, j int)) (i, j int)
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


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:230`



---


[function] name: hashAddresses file: pkg/api/v1/endpoints/util.go:147 returns_error: нет description: —


### hashAddresses (pkg/api/v1/endpoints/util.go:147)


hashAddresses is a function that performs operations based on the provided parameters and returns (addrs addressSet).


```go
func hashAddresses((addrs addressSet)) (addrs addressSet)
```


**Тип ответа:** addrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** addressSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:147`



---


[function] name: hashObject file: pkg/api/v1/endpoints/util.go:203 returns_error: нет description: —


### hashObject (pkg/api/v1/endpoints/util.go:203)


hashObject is a function that performs operations based on the provided parameters and returns (hasher hash.Hash, obj interface{}).


```go
func hashObject((hasher hash.Hash, obj interface{})) (hasher hash.Hash, obj interface{})
```


**Тип ответа:** hasher


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hash.Hash


```json
{
  "jwtIssuerHash": "string",
  "apiServerIDHash": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/metrics.go`


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


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:203`



---


[function] name: lessAddrReady file: pkg/api/v1/endpoints/util.go:162 returns_error: нет description: —


### lessAddrReady (pkg/api/v1/endpoints/util.go:162)


lessAddrReady is a function that performs operations based on the provided parameters and returns (a, b addrReady).


```go
func lessAddrReady((a, b addrReady)) (a, b addrReady)
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


**Тип ответа:** addrReady


```json
{
  "addr": null,
  "ready": false
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:162`



---


[function] name: mapAddressByPort file: pkg/api/v1/endpoints/util.go:107 returns_error: нет description: mapAddressByPort adds one address into a map by port, registering the address with a unique pointer, and preserving
any 


### mapAddressByPort (pkg/api/v1/endpoints/util.go:107)


mapAddressByPort adds one address into a map by port, registering the address with a unique pointer, and preserving
any existing ready state.


```go
func mapAddressByPort((addr *v1.EndpointAddress, port v1.EndpointPort, ready bool, allAddrs map[addressKey]*v1.EndpointAddress, portToAddrReadyMap map[v1.EndpointPort]addressSet)) (addr *v1.EndpointAddress, port v1.EndpointPort, ready bool, allAddrs map[addressKey]*v1.EndpointAddress, portToAddrReadyMap map[v1.EndpointPort]addressSet)
```


**Тип запроса:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** addr


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** port


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** v1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


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


**Тип ответа:** allAddrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** addressKey


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** portToAddrReadyMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** v1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** addressSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:107`



---


[function] name: mapAddressesByPort file: pkg/api/v1/endpoints/util.go:96 returns_error: нет description: mapAddressesByPort adds all ready and not-ready addresses into a map by a single port.


### mapAddressesByPort (pkg/api/v1/endpoints/util.go:96)


mapAddressesByPort adds all ready and not-ready addresses into a map by a single port.


```go
func mapAddressesByPort((subset *v1.EndpointSubset, port v1.EndpointPort, allAddrs map[addressKey]*v1.EndpointAddress, portToAddrReadyMap map[v1.EndpointPort]addressSet)) (subset *v1.EndpointSubset, port v1.EndpointPort, allAddrs map[addressKey]*v1.EndpointAddress, portToAddrReadyMap map[v1.EndpointPort]addressSet)
```


**Тип запроса:** v1.EndpointSubset


```json
{
  "Addresses": [],
  "NotReadyAddresses": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** subset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.EndpointSubset


```json
{
  "Addresses": [],
  "NotReadyAddresses": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** port


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Тип ответа:** v1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** allAddrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** addressKey


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** v1.EndpointAddress


```json
{
  "IP": "string",
  "Hostname": "string",
  "NodeName": "string",
  "TargetRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** portToAddrReadyMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** v1.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** addressSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/endpoints/util.go:96`




## pkg/api/v1/persistentvolume/util.go


📄 Исходный файл: `pkg/api/v1/persistentvolume/util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [VisitPVSecretNames](#visitpvsecretnames-pkgapiv1persistentvolumeutilgo47) `:47`

- 🔗 [getClaimRefNamespace](#getclaimrefnamespace-pkgapiv1persistentvolumeutilgo23) `:23`

- 🔗 [skipEmptyNames](#skipemptynames-pkgapiv1persistentvolumeutilgo33) `:33`


</details>


[function] name: VisitPVSecretNames file: pkg/api/v1/persistentvolume/util.go:47 returns_error: нет description: VisitPVSecretNames invokes the visitor function with the name of every secret
referenced by the PV spec. If visitor retu


### VisitPVSecretNames (pkg/api/v1/persistentvolume/util.go:47)


VisitPVSecretNames invokes the visitor function with the name of every secret
referenced by the PV spec. If visitor returns false, visiting is short-circuited.
Returns true if visiting completed, false if visiting was short-circuited.


```go
func VisitPVSecretNames((pv *corev1.PersistentVolume, visitor Visitor)) (pv *corev1.PersistentVolume, visitor Visitor)
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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/v1/persistentvolume/util.go:47`



---


[function] name: getClaimRefNamespace file: pkg/api/v1/persistentvolume/util.go:23 returns_error: нет description: —


### getClaimRefNamespace (pkg/api/v1/persistentvolume/util.go:23)


getClaimRefNamespace is a function that performs operations based on the provided parameters and returns (pv *corev1.PersistentVolume).


```go
func getClaimRefNamespace((pv *corev1.PersistentVolume)) (pv *corev1.PersistentVolume)
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


📍 *Расположение:* `pkg/api/v1/persistentvolume/util.go:23`



---


[function] name: skipEmptyNames file: pkg/api/v1/persistentvolume/util.go:33 returns_error: нет description: —


### skipEmptyNames (pkg/api/v1/persistentvolume/util.go:33)


skipEmptyNames is a function that performs operations based on the provided parameters and returns (visitor Visitor).


```go
func skipEmptyNames((visitor Visitor)) (visitor Visitor)
```


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/v1/persistentvolume/util.go:33`




## pkg/api/v1/pod/util.go


📄 Исходный файл: `pkg/api/v1/pod/util.go`


<details open>
<summary><b>Функции в этом файле (29)</b></summary>


- 🔗 [AllContainersCouldRestart](#allcontainerscouldrestart-pkgapiv1podutilgo494) `:494`

- 🔗 [AllFeatureEnabledContainers](#allfeatureenabledcontainers-pkgapiv1podutilgo46) `:46`

- 🔗 [CalculatePodConditionObservedGeneration](#calculatepodconditionobservedgeneration-pkgapiv1podutilgo533) `:533`

- 🔗 [CalculatePodStatusObservedGeneration](#calculatepodstatusobservedgeneration-pkgapiv1podutilgo521) `:521`

- 🔗 [ContainerIter](#containeriter-pkgapiv1podutilgo83) `:83`

- 🔗 [ContainerShouldRestart](#containershouldrestart-pkgapiv1podutilgo419) `:419`

- 🔗 [FindMatchingContainerRestartRule](#findmatchingcontainerrestartrule-pkgapiv1podutilgo465) `:465`

- 🔗 [GetContainerStatus](#getcontainerstatus-pkgapiv1podutilgo251) `:251`

- 🔗 [GetContainersReadyCondition](#getcontainersreadycondition-pkgapiv1podutilgo332) `:332`

- 🔗 [GetExistingContainerStatus](#getexistingcontainerstatus-pkgapiv1podutilgo262) `:262`

- 🔗 [GetIndexOfContainerStatus](#getindexofcontainerstatus-pkgapiv1podutilgo269) `:269`

- 🔗 [GetPodCondition](#getpodcondition-pkgapiv1podutilgo339) `:339`

- 🔗 [GetPodConditionFromList](#getpodconditionfromlist-pkgapiv1podutilgo348) `:348`

- 🔗 [GetPodReadyCondition](#getpodreadycondition-pkgapiv1podutilgo325) `:325`

- 🔗 [IsContainerRestartable](#iscontainerrestartable-pkgapiv1podutilgo403) `:403`

- 🔗 [IsContainersReadyConditionTrue](#iscontainersreadyconditiontrue-pkgapiv1podutilgo318) `:318`

- 🔗 [IsPodAvailable](#ispodavailable-pkgapiv1podutilgo283) `:283`

- 🔗 [IsPodPhaseTerminal](#ispodphaseterminal-pkgapiv1podutilgo307) `:307`

- 🔗 [IsPodReady](#ispodready-pkgapiv1podutilgo297) `:297`

- 🔗 [IsPodReadyConditionTrue](#ispodreadyconditiontrue-pkgapiv1podutilgo312) `:312`

- 🔗 [IsPodTerminal](#ispodterminal-pkgapiv1podutilgo302) `:302`

- 🔗 [IsRestartableInitContainer](#isrestartableinitcontainer-pkgapiv1podutilgo392) `:392`

- 🔗 [UpdatePodCondition](#updatepodcondition-pkgapiv1podutilgo363) `:363`

- 🔗 [VisitContainers](#visitcontainers-pkgapiv1podutilgo72) `:72`

- 🔗 [VisitPodConfigmapNames](#visitpodconfigmapnames-pkgapiv1podutilgo204) `:204`

- 🔗 [VisitPodSecretNames](#visitpodsecretnames-pkgapiv1podutilgo113) `:113`

- 🔗 [skipEmptyNames](#skipemptynames-pkgapiv1podutilgo57) `:57`

- 🔗 [visitContainerConfigmapNames](#visitcontainerconfigmapnames-pkgapiv1podutilgo231) `:231`

- 🔗 [visitContainerSecretNames](#visitcontainersecretnames-pkgapiv1podutilgo182) `:182`


</details>


[function] name: AllContainersCouldRestart file: pkg/api/v1/pod/util.go:494 returns_error: нет description: AllContainersCouldRestart returns true if all containers could be restarted
for the given pod. This is true if any conta


### AllContainersCouldRestart (pkg/api/v1/pod/util.go:494)


AllContainersCouldRestart returns true if all containers could be restarted
for the given pod. This is true if any container has a RestartAllContainers
action.


```go
func AllContainersCouldRestart((pod *v1.PodSpec)) (pod *v1.PodSpec)
```


**Тип запроса:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
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


**Тип ответа:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:494`



---


[function] name: AllFeatureEnabledContainers file: pkg/api/v1/pod/util.go:46 returns_error: нет description: AllFeatureEnabledContainers returns a ContainerType mask which includes all container
types except for the ones guarded 


### AllFeatureEnabledContainers (pkg/api/v1/pod/util.go:46)


AllFeatureEnabledContainers returns a ContainerType mask which includes all container
types except for the ones guarded by feature gate.


```go
func AllFeatureEnabledContainers(()) ()
```


📍 *Расположение:* `pkg/api/v1/pod/util.go:46`



---


[function] name: CalculatePodConditionObservedGeneration file: pkg/api/v1/pod/util.go:533 returns_error: нет description: CalculatePodConditionObservedGeneration calculates the observedGeneration for a particular pod condition.
The observedGe


### CalculatePodConditionObservedGeneration (pkg/api/v1/pod/util.go:533)


CalculatePodConditionObservedGeneration calculates the observedGeneration for a particular pod condition.
The observedGeneration is set to the pod's generation when the feature gate
PodObservedGenerationTracking is enabled OR if condition[].observedGeneration is already set.
This protects against an infinite loop of kubelet trying to clear the value after the FG is turned off, and
the API server preserving existing values when an incoming update tries to clear it.


```go
func CalculatePodConditionObservedGeneration((podStatus *v1.PodStatus, generation int64, conditionType v1.PodConditionType)) (podStatus *v1.PodStatus, generation int64, conditionType v1.PodConditionType)
```


**Тип запроса:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** podStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** generation


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** conditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.PodConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/pod/util.go:533`



---


[function] name: CalculatePodStatusObservedGeneration file: pkg/api/v1/pod/util.go:521 returns_error: нет description: CalculatePodStatusObservedGeneration calculates the observedGeneration for the pod status.
This is used to track the gen


### CalculatePodStatusObservedGeneration (pkg/api/v1/pod/util.go:521)


CalculatePodStatusObservedGeneration calculates the observedGeneration for the pod status.
This is used to track the generation of the pod that was observed by the kubelet.
The observedGeneration is set to the pod's generation when the feature gate
PodObservedGenerationTracking is enabled OR if status.observedGeneration is already set.
This protects against an infinite loop of kubelet trying to clear the value after the FG is turned off, and
the API server preserving existing values when an incoming update tries to clear it.


```go
func CalculatePodStatusObservedGeneration((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `pkg/api/v1/pod/util.go:521`



---


[function] name: ContainerIter file: pkg/api/v1/pod/util.go:83 returns_error: нет description: ContainerIter returns an iterator over all containers in the given pod spec with a masked type.
The iteration order is I


### ContainerIter (pkg/api/v1/pod/util.go:83)


ContainerIter returns an iterator over all containers in the given pod spec with a masked type.
The iteration order is InitContainers, then main Containers, then EphemeralContainers.


```go
func ContainerIter((podSpec *v1.PodSpec, mask ContainerType)) (podSpec *v1.PodSpec, mask ContainerType)
```


**Тип запроса:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** mask


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/pod/util.go:83`



---


[function] name: ContainerShouldRestart file: pkg/api/v1/pod/util.go:419 returns_error: нет description: ContainerShouldRestart checks if a container should be restarted by its restart policy.
First, the container-level resta


### ContainerShouldRestart (pkg/api/v1/pod/util.go:419)


ContainerShouldRestart checks if a container should be restarted by its restart policy.
First, the container-level restartPolicyRules are evaluated in order. An action is taken if any
rules are matched. Second, the container-level restart policy is used. Lastly, if no container
level policy are specified, pod-level restart policy is used.


```go
func ContainerShouldRestart((container v1.Container, pod v1.PodSpec, exitCode int32)) (container v1.Container, pod v1.PodSpec, exitCode int32)
```


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


**Тип ответа:** v1.Container


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** exitCode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/pod/util.go:419`



---


[function] name: FindMatchingContainerRestartRule file: pkg/api/v1/pod/util.go:465 returns_error: нет description: FindMatchingContainerRestartRule returns a rule and true if the exitCode matched
one of the restart rules for the given 


### FindMatchingContainerRestartRule (pkg/api/v1/pod/util.go:465)


FindMatchingContainerRestartRule returns a rule and true if the exitCode matched
one of the restart rules for the given container. Returns and empty rule and
false if no rules matched.


```go
func FindMatchingContainerRestartRule((rule v1.ContainerRestartRule, found bool)) (rule v1.ContainerRestartRule, found bool)
```


**Тип ответа:** rule


```json
{
  "rules": [],
  "errors": []
}
```


*Определено в:* `pkg/registry/rbac/validation/rule.go`


**Тип ответа:** v1.ContainerRestartRule


```json
{
  "Action": {},
  "ExitCodes": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** found


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/pod/util.go:465`



---


[function] name: GetContainerStatus file: pkg/api/v1/pod/util.go:251 returns_error: нет description: GetContainerStatus extracts the status of container "name" from "statuses".
It returns true if "name" exists, else retur


### GetContainerStatus (pkg/api/v1/pod/util.go:251)


GetContainerStatus extracts the status of container "name" from "statuses".
It returns true if "name" exists, else returns false.


```go
func GetContainerStatus((v1.ContainerStatus, bool)) (v1.ContainerStatus, bool)
```


**Тип ответа:** v1.ContainerStatus


```json
{
  "Name": "string",
  "State": {},
  "LastTerminationState": {},
  "Ready": false,
  "RestartCount": 0,
  "Image": "string",
  "ImageID": "string",
  "ContainerID": "string",
  "Started": false,
  "AllocatedResources": {},
  "Resources": null,
  "VolumeMounts": [],
  "User": null,
  "AllocatedResourcesStatus": [],
  "StopSignal": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:251`



---


[function] name: GetContainersReadyCondition file: pkg/api/v1/pod/util.go:332 returns_error: нет description: GetContainersReadyCondition extracts the containers ready condition from the given status and returns that.
Returns nil 


### GetContainersReadyCondition (pkg/api/v1/pod/util.go:332)


GetContainersReadyCondition extracts the containers ready condition from the given status and returns that.
Returns nil if the condition is not present.


```go
func GetContainersReadyCondition((status v1.PodStatus)) (status v1.PodStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:332`



---


[function] name: GetExistingContainerStatus file: pkg/api/v1/pod/util.go:262 returns_error: нет description: GetExistingContainerStatus extracts the status of container "name" from "statuses",
It also returns if "name" exists.


### GetExistingContainerStatus (pkg/api/v1/pod/util.go:262)


GetExistingContainerStatus extracts the status of container "name" from "statuses",
It also returns if "name" exists.


```go
func GetExistingContainerStatus((statuses []v1.ContainerStatus, name string)) (statuses []v1.ContainerStatus, name string)
```


**Тип ответа:** statuses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.ContainerStatus


```json
{
  "Name": "string",
  "State": {},
  "LastTerminationState": {},
  "Ready": false,
  "RestartCount": 0,
  "Image": "string",
  "ImageID": "string",
  "ContainerID": "string",
  "Started": false,
  "AllocatedResources": {},
  "Resources": null,
  "VolumeMounts": [],
  "User": null,
  "AllocatedResourcesStatus": [],
  "StopSignal": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:262`



---


[function] name: GetIndexOfContainerStatus file: pkg/api/v1/pod/util.go:269 returns_error: нет description: GetIndexOfContainerStatus gets the index of status of container "name" from "statuses",
It returns (index, true) if "nam


### GetIndexOfContainerStatus (pkg/api/v1/pod/util.go:269)


GetIndexOfContainerStatus gets the index of status of container "name" from "statuses",
It returns (index, true) if "name" exists, else returns (0, false).


```go
func GetIndexOfContainerStatus((int, bool)) (int, bool)
```


📍 *Расположение:* `pkg/api/v1/pod/util.go:269`



---


[function] name: GetPodCondition file: pkg/api/v1/pod/util.go:339 returns_error: нет description: GetPodCondition extracts the provided condition from the given status and returns that.
Returns nil and -1 if the condit


### GetPodCondition (pkg/api/v1/pod/util.go:339)


GetPodCondition extracts the provided condition from the given status and returns that.
Returns nil and -1 if the condition is not present, and the index of the located condition.


```go
func GetPodCondition((int, *v1.PodCondition)) (int, *v1.PodCondition)
```


**Тип запроса:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:339`



---


[function] name: GetPodConditionFromList file: pkg/api/v1/pod/util.go:348 returns_error: нет description: GetPodConditionFromList extracts the provided condition from the given list of condition and
returns the index of the co


### GetPodConditionFromList (pkg/api/v1/pod/util.go:348)


GetPodConditionFromList extracts the provided condition from the given list of condition and
returns the index of the condition and the condition. Returns -1 and nil if the condition is not present.


```go
func GetPodConditionFromList((int, *v1.PodCondition)) (int, *v1.PodCondition)
```


**Тип запроса:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:348`



---


[function] name: GetPodReadyCondition file: pkg/api/v1/pod/util.go:325 returns_error: нет description: GetPodReadyCondition extracts the pod ready condition from the given status and returns that.
Returns nil if the conditi


### GetPodReadyCondition (pkg/api/v1/pod/util.go:325)


GetPodReadyCondition extracts the pod ready condition from the given status and returns that.
Returns nil if the condition is not present.


```go
func GetPodReadyCondition((status v1.PodStatus)) (status v1.PodStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:325`



---


[function] name: IsContainerRestartable file: pkg/api/v1/pod/util.go:403 returns_error: нет description: IsContainerRestartable returns true if the container can be restarted. A container can be
restarted if it has a pod-leve


### IsContainerRestartable (pkg/api/v1/pod/util.go:403)


IsContainerRestartable returns true if the container can be restarted. A container can be
restarted if it has a pod-level restart policy "Always" or "OnFailure" and not override by
container-level restart policy, or a container-level restart policy "Always" or "OnFailure",
or a container level restart rule with action "Restart".


```go
func IsContainerRestartable((pod v1.PodSpec, container v1.Container)) (pod v1.PodSpec, container v1.Container)
```


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
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


**Тип ответа:** v1.Container


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


📍 *Расположение:* `pkg/api/v1/pod/util.go:403`



---


[function] name: IsContainersReadyConditionTrue file: pkg/api/v1/pod/util.go:318 returns_error: нет description: IsContainersReadyConditionTrue returns true if a pod is ready; false otherwise.


### IsContainersReadyConditionTrue (pkg/api/v1/pod/util.go:318)


IsContainersReadyConditionTrue returns true if a pod is ready; false otherwise.


```go
func IsContainersReadyConditionTrue((status v1.PodStatus)) (status v1.PodStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:318`



---


[function] name: IsPodAvailable file: pkg/api/v1/pod/util.go:283 returns_error: нет description: IsPodAvailable returns true if a pod is available; false otherwise.
Precondition for an available pod is that it must be


### IsPodAvailable (pkg/api/v1/pod/util.go:283)


IsPodAvailable returns true if a pod is available; false otherwise.
Precondition for an available pod is that it must be ready. On top
of that, there are two cases when a pod can be considered available:
1. minReadySeconds == 0, or
2. LastTransitionTime (is set) + minReadySeconds <= current time


```go
func IsPodAvailable((pod *v1.Pod, minReadySeconds int32, now metav1.Time)) (pod *v1.Pod, minReadySeconds int32, now metav1.Time)
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


**Тип ответа:** minReadySeconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** now


```json
{
  "Key": "string",
  "Obj": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/delta_fifo.go`


**Тип ответа:** metav1.Time


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


📍 *Расположение:* `pkg/api/v1/pod/util.go:283`



---


[function] name: IsPodPhaseTerminal file: pkg/api/v1/pod/util.go:307 returns_error: нет description: IsPodPhaseTerminal returns true if the pod's phase is terminal.


### IsPodPhaseTerminal (pkg/api/v1/pod/util.go:307)


IsPodPhaseTerminal returns true if the pod's phase is terminal.


```go
func IsPodPhaseTerminal((phase v1.PodPhase)) (phase v1.PodPhase)
```


**Тип ответа:** phase


```json
{
  "parent": null,
  "level": 0,
  "selfPath": [],
  "generatedName": "string",
  "use": "string"
}
```


*Определено в:* `cmd/kubeadm/app/cmd/phases/workflow/runner.go`


**Тип ответа:** v1.PodPhase


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/pod/util.go:307`



---


[function] name: IsPodReady file: pkg/api/v1/pod/util.go:297 returns_error: нет description: IsPodReady returns true if a pod is ready; false otherwise.


### IsPodReady (pkg/api/v1/pod/util.go:297)


IsPodReady returns true if a pod is ready; false otherwise.


```go
func IsPodReady((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `pkg/api/v1/pod/util.go:297`



---


[function] name: IsPodReadyConditionTrue file: pkg/api/v1/pod/util.go:312 returns_error: нет description: IsPodReadyConditionTrue returns true if a pod is ready; false otherwise.


### IsPodReadyConditionTrue (pkg/api/v1/pod/util.go:312)


IsPodReadyConditionTrue returns true if a pod is ready; false otherwise.


```go
func IsPodReadyConditionTrue((status v1.PodStatus)) (status v1.PodStatus)
```


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:312`



---


[function] name: IsPodTerminal file: pkg/api/v1/pod/util.go:302 returns_error: нет description: IsPodTerminal returns true if a pod is terminal, all containers are stopped and cannot ever regress.


### IsPodTerminal (pkg/api/v1/pod/util.go:302)


IsPodTerminal returns true if a pod is terminal, all containers are stopped and cannot ever regress.


```go
func IsPodTerminal((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `pkg/api/v1/pod/util.go:302`



---


[function] name: IsRestartableInitContainer file: pkg/api/v1/pod/util.go:392 returns_error: нет description: IsRestartableInitContainer returns true if the container has ContainerRestartPolicyAlways.
This function is not checking


### IsRestartableInitContainer (pkg/api/v1/pod/util.go:392)


IsRestartableInitContainer returns true if the container has ContainerRestartPolicyAlways.
This function is not checking if the container passed to it is indeed an init container.
It is just checking if the container restart policy has been set to always.


```go
func IsRestartableInitContainer((initContainer *v1.Container)) (initContainer *v1.Container)
```


**Тип запроса:** v1.Container


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


**Тип ответа:** initContainer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Container


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


📍 *Расположение:* `pkg/api/v1/pod/util.go:392`



---


[function] name: UpdatePodCondition file: pkg/api/v1/pod/util.go:363 returns_error: нет description: UpdatePodCondition updates existing pod condition or creates a new one. Sets LastTransitionTime to now if the
status has


### UpdatePodCondition (pkg/api/v1/pod/util.go:363)


UpdatePodCondition updates existing pod condition or creates a new one. Sets LastTransitionTime to now if the
status has changed.
Returns true if pod condition has changed or has been added.


```go
func UpdatePodCondition((status *v1.PodStatus, condition *v1.PodCondition)) (status *v1.PodStatus, condition *v1.PodCondition)
```


**Тип запроса:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип запроса:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** v1.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** v1.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:363`



---


[function] name: VisitContainers file: pkg/api/v1/pod/util.go:72 returns_error: нет description: VisitContainers invokes the visitor function with a pointer to every container
spec in the given pod spec with type set 


### VisitContainers (pkg/api/v1/pod/util.go:72)


VisitContainers invokes the visitor function with a pointer to every container
spec in the given pod spec with type set in mask. If visitor returns false,
visiting is short-circuited. VisitContainers returns true if visiting completes,
false if visiting was short-circuited.


```go
func VisitContainers((podSpec *v1.PodSpec, mask ContainerType, visitor ContainerVisitor)) (podSpec *v1.PodSpec, mask ContainerType, visitor ContainerVisitor)
```


**Тип запроса:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** podSpec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.PodSpec


```json
{
  "Volumes": [],
  "InitContainers": [],
  "Containers": [],
  "EphemeralContainers": [],
  "RestartPolicy": {},
  "TerminationGracePeriodSeconds": 0,
  "ActiveDeadlineSeconds": 0,
  "DNSPolicy": {},
  "NodeSelector": {},
  "ServiceAccountName": "string",
  "AutomountServiceAccountToken": false,
  "NodeName": "string",
  "SecurityContext": null,
  "ImagePullSecrets": [],
  "Hostname": "string",
  "Subdomain": "string",
  "SetHostnameAsFQDN": false,
  "Affinity": null,
  "SchedulerName": "string",
  "Tolerations": [],
  "HostAliases": [],
  "PriorityClassName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "DNSConfig": null,
  "ReadinessGates": [],
  "RuntimeClassName": "string",
  "Overhead": {},
  "EnableServiceLinks": false,
  "TopologySpreadConstraints": [],
  "OS": null,
  "SchedulingGates": [],
  "ResourceClaims": [],
  "Resources": null,
  "HostnameOverride": "string",
  "WorkloadRef": null
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** mask


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerVisitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/pod/util.go:72`



---


[function] name: VisitPodConfigmapNames file: pkg/api/v1/pod/util.go:204 returns_error: нет description: VisitPodConfigmapNames invokes the visitor function with the name of every configmap
referenced by the pod spec. If visi


### VisitPodConfigmapNames (pkg/api/v1/pod/util.go:204)


VisitPodConfigmapNames invokes the visitor function with the name of every configmap
referenced by the pod spec. If visitor returns false, visiting is short-circuited.
Transitive references (e.g. pod -> pvc -> pv -> secret) are not visited.
Returns true if visiting completed, false if visiting was short-circuited.


```go
func VisitPodConfigmapNames((pod *v1.Pod, visitor Visitor)) (pod *v1.Pod, visitor Visitor)
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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:204`



---


[function] name: VisitPodSecretNames file: pkg/api/v1/pod/util.go:113 returns_error: нет description: VisitPodSecretNames invokes the visitor function with the name of every secret
referenced by the pod spec. If visitor re


### VisitPodSecretNames (pkg/api/v1/pod/util.go:113)


VisitPodSecretNames invokes the visitor function with the name of every secret
referenced by the pod spec. If visitor returns false, visiting is short-circuited.
Transitive references (e.g. pod -> pvc -> pv -> secret) are not visited.
Returns true if visiting completed, false if visiting was short-circuited.


```go
func VisitPodSecretNames((pod *v1.Pod, visitor Visitor)) (pod *v1.Pod, visitor Visitor)
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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:113`



---


[function] name: skipEmptyNames file: pkg/api/v1/pod/util.go:57 returns_error: нет description: —


### skipEmptyNames (pkg/api/v1/pod/util.go:57)


skipEmptyNames is a function that performs operations based on the provided parameters and returns (visitor Visitor).


```go
func skipEmptyNames((visitor Visitor)) (visitor Visitor)
```


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:57`



---


[function] name: visitContainerConfigmapNames file: pkg/api/v1/pod/util.go:231 returns_error: нет description: visitContainerConfigmapNames returns true unless the visitor returned false when invoked with a configmap reference


### visitContainerConfigmapNames (pkg/api/v1/pod/util.go:231)


visitContainerConfigmapNames returns true unless the visitor returned false when invoked with a configmap reference


```go
func visitContainerConfigmapNames((container *v1.Container, visitor Visitor)) (container *v1.Container, visitor Visitor)
```


**Тип запроса:** v1.Container


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


**Тип ответа:** v1.Container


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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:231`



---


[function] name: visitContainerSecretNames file: pkg/api/v1/pod/util.go:182 returns_error: нет description: visitContainerSecretNames returns true unless the visitor returned false when invoked with a secret reference


### visitContainerSecretNames (pkg/api/v1/pod/util.go:182)


visitContainerSecretNames returns true unless the visitor returned false when invoked with a secret reference


```go
func visitContainerSecretNames((container *v1.Container, visitor Visitor)) (container *v1.Container, visitor Visitor)
```


**Тип запроса:** v1.Container


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


**Тип ответа:** v1.Container


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


**Тип ответа:** visitor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Visitor


```json
{
  "Structural": {},
  "NestedValueValidation": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/visitor.go`


📍 *Расположение:* `pkg/api/v1/pod/util.go:182`




## pkg/api/v1/resource/helpers.go


📄 Исходный файл: `pkg/api/v1/resource/helpers.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [ExtractContainerResourceValue](#extractcontainerresourcevalue-pkgapiv1resourcehelpersgo105) `:105`

- 🔗 [ExtractResourceValueByContainerName](#extractresourcevaluebycontainername-pkgapiv1resourcehelpersgo80) `:80`

- 🔗 [ExtractResourceValueByContainerNameAndNodeAllocatable](#extractresourcevaluebycontainernameandnodeallocatable-pkgapiv1resourcehelpersgo90) `:90`

- 🔗 [GetResourceRequest](#getresourcerequest-pkgapiv1resourcehelpersgo64) `:64`

- 🔗 [GetResourceRequestQuantity](#getresourcerequestquantity-pkgapiv1resourcehelpersgo33) `:33`

- 🔗 [IsHugePageResourceName](#ishugepageresourcename-pkgapiv1resourcehelpersgo207) `:207`

- 🔗 [MergeContainerResourceLimits](#mergecontainerresourcelimits-pkgapiv1resourcehelpersgo189) `:189`

- 🔗 [convertResourceCPUToString](#convertresourcecputostring-pkgapiv1resourcehelpersgo146) `:146`

- 🔗 [convertResourceEphemeralStorageToString](#convertresourceephemeralstoragetostring-pkgapiv1resourcehelpersgo167) `:167`

- 🔗 [convertResourceHugePagesToString](#convertresourcehugepagestostring-pkgapiv1resourcehelpersgo160) `:160`

- 🔗 [convertResourceMemoryToString](#convertresourcememorytostring-pkgapiv1resourcehelpersgo153) `:153`

- 🔗 [findContainerInPod](#findcontainerinpod-pkgapiv1resourcehelpersgo173) `:173`


</details>


[function] name: ExtractContainerResourceValue file: pkg/api/v1/resource/helpers.go:105 returns_error: да description: ExtractContainerResourceValue extracts the value of a resource
in an already known container


### ExtractContainerResourceValue (pkg/api/v1/resource/helpers.go:105)


ExtractContainerResourceValue extracts the value of a resource
in an already known container


```go
func ExtractContainerResourceValue((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:105`



---


[function] name: ExtractResourceValueByContainerName file: pkg/api/v1/resource/helpers.go:80 returns_error: да description: ExtractResourceValueByContainerName extracts the value of a resource
by providing container name


### ExtractResourceValueByContainerName (pkg/api/v1/resource/helpers.go:80)


ExtractResourceValueByContainerName extracts the value of a resource
by providing container name


```go
func ExtractResourceValueByContainerName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:80`



---


[function] name: ExtractResourceValueByContainerNameAndNodeAllocatable file: pkg/api/v1/resource/helpers.go:90 returns_error: да description: ExtractResourceValueByContainerNameAndNodeAllocatable extracts the value of a resource
by providing container name and n


### ExtractResourceValueByContainerNameAndNodeAllocatable (pkg/api/v1/resource/helpers.go:90)


ExtractResourceValueByContainerNameAndNodeAllocatable extracts the value of a resource
by providing container name and node allocatable


```go
func ExtractResourceValueByContainerNameAndNodeAllocatable((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:90`



---


[function] name: GetResourceRequest file: pkg/api/v1/resource/helpers.go:64 returns_error: нет description: GetResourceRequest finds and returns the request value for a specific resource.


### GetResourceRequest (pkg/api/v1/resource/helpers.go:64)


GetResourceRequest finds and returns the request value for a specific resource.


```go
func GetResourceRequest((pod *v1.Pod, resource v1.ResourceName)) (pod *v1.Pod, resource v1.ResourceName)
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


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


**Тип ответа:** v1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:64`



---


[function] name: GetResourceRequestQuantity file: pkg/api/v1/resource/helpers.go:33 returns_error: нет description: GetResourceRequestQuantity finds and returns the request quantity for a specific resource.


### GetResourceRequestQuantity (pkg/api/v1/resource/helpers.go:33)


GetResourceRequestQuantity finds and returns the request quantity for a specific resource.


```go
func GetResourceRequestQuantity((pod *v1.Pod, resourceName v1.ResourceName)) (pod *v1.Pod, resourceName v1.ResourceName)
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


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:33`



---


[function] name: IsHugePageResourceName file: pkg/api/v1/resource/helpers.go:207 returns_error: нет description: IsHugePageResourceName returns true if the resource name has the huge page
resource prefix.


### IsHugePageResourceName (pkg/api/v1/resource/helpers.go:207)


IsHugePageResourceName returns true if the resource name has the huge page
resource prefix.


```go
func IsHugePageResourceName((name v1.ResourceName)) (name v1.ResourceName)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** v1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:207`



---


[function] name: MergeContainerResourceLimits file: pkg/api/v1/resource/helpers.go:189 returns_error: нет description: MergeContainerResourceLimits checks if a limit is applied for
the container, and if not, it sets the limit to the passed


### MergeContainerResourceLimits (pkg/api/v1/resource/helpers.go:189)


MergeContainerResourceLimits checks if a limit is applied for
the container, and if not, it sets the limit to the passed resource list.


```go
func MergeContainerResourceLimits((container *v1.Container,
	allocatable v1.ResourceList)) (container *v1.Container,
	allocatable v1.ResourceList)
```


**Тип запроса:** v1.Container


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


**Тип ответа:** v1.Container


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


**Тип ответа:** allocatable


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.ResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:189`



---


[function] name: convertResourceCPUToString file: pkg/api/v1/resource/helpers.go:146 returns_error: да description: convertResourceCPUToString converts cpu value to the format of divisor and returns
ceiling of the value.


### convertResourceCPUToString (pkg/api/v1/resource/helpers.go:146)


convertResourceCPUToString converts cpu value to the format of divisor and returns
ceiling of the value.


```go
func convertResourceCPUToString((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:146`



---


[function] name: convertResourceEphemeralStorageToString file: pkg/api/v1/resource/helpers.go:167 returns_error: да description: convertResourceEphemeralStorageToString converts ephemeral storage value to the format of divisor and returns
ceiling of


### convertResourceEphemeralStorageToString (pkg/api/v1/resource/helpers.go:167)


convertResourceEphemeralStorageToString converts ephemeral storage value to the format of divisor and returns
ceiling of the value.


```go
func convertResourceEphemeralStorageToString((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:167`



---


[function] name: convertResourceHugePagesToString file: pkg/api/v1/resource/helpers.go:160 returns_error: да description: convertResourceHugePagesToString converts hugepages value to the format of divisor and returns
ceiling of the value.


### convertResourceHugePagesToString (pkg/api/v1/resource/helpers.go:160)


convertResourceHugePagesToString converts hugepages value to the format of divisor and returns
ceiling of the value.


```go
func convertResourceHugePagesToString((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:160`



---


[function] name: convertResourceMemoryToString file: pkg/api/v1/resource/helpers.go:153 returns_error: да description: convertResourceMemoryToString converts memory value to the format of divisor and returns
ceiling of the value.


### convertResourceMemoryToString (pkg/api/v1/resource/helpers.go:153)


convertResourceMemoryToString converts memory value to the format of divisor and returns
ceiling of the value.


```go
func convertResourceMemoryToString((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:153`



---


[function] name: findContainerInPod file: pkg/api/v1/resource/helpers.go:173 returns_error: да description: findContainerInPod finds a container by its name in the provided pod


### findContainerInPod (pkg/api/v1/resource/helpers.go:173)


findContainerInPod finds a container by its name in the provided pod


```go
func findContainerInPod((*v1.Container, error)) (*v1.Container, error)
```


**Тип запроса:** v1.Container


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


**Тип ответа:** v1.Container


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.Container`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/resource/helpers.go:173`




## pkg/api/v1/service/util.go


📄 Исходный файл: `pkg/api/v1/service/util.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [ExternalPolicyLocal](#externalpolicylocal-pkgapiv1serviceutilgo78) `:78`

- 🔗 [ExternallyAccessible](#externallyaccessible-pkgapiv1serviceutilgo71) `:71`

- 🔗 [GetLoadBalancerSourceRanges](#getloadbalancersourceranges-pkgapiv1serviceutilgo44) `:44`

- 🔗 [InternalPolicyLocal](#internalpolicylocal-pkgapiv1serviceutilgo86) `:86`

- 🔗 [IsAllowAll](#isallowall-pkgapiv1serviceutilgo32) `:32`

- 🔗 [NeedsHealthCheck](#needshealthcheck-pkgapiv1serviceutilgo94) `:94`


</details>


[function] name: ExternalPolicyLocal file: pkg/api/v1/service/util.go:78 returns_error: нет description: ExternalPolicyLocal checks if service is externally accessible and has ETP = Local.


### ExternalPolicyLocal (pkg/api/v1/service/util.go:78)


ExternalPolicyLocal checks if service is externally accessible and has ETP = Local.


```go
func ExternalPolicyLocal((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


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


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/service/util.go:78`



---


[function] name: ExternallyAccessible file: pkg/api/v1/service/util.go:71 returns_error: нет description: ExternallyAccessible checks if service is externally accessible.


### ExternallyAccessible (pkg/api/v1/service/util.go:71)


ExternallyAccessible checks if service is externally accessible.


```go
func ExternallyAccessible((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


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


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/service/util.go:71`



---


[function] name: GetLoadBalancerSourceRanges file: pkg/api/v1/service/util.go:44 returns_error: да description: GetLoadBalancerSourceRanges first try to parse and verify LoadBalancerSourceRanges field from a service.
If the field is


### GetLoadBalancerSourceRanges (pkg/api/v1/service/util.go:44)


GetLoadBalancerSourceRanges first try to parse and verify LoadBalancerSourceRanges field from a service.
If the field is not specified, turn to parse and verify the AnnotationLoadBalancerSourceRangesKey annotation from a service,
extracting the source ranges to allow, and if not present returns a default (allow-all) value.


```go
func GetLoadBalancerSourceRanges((utilnet.IPNetSet, error)) (utilnet.IPNetSet, error)
```


**Тип ответа:** utilnet.IPNetSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `utilnet.IPNetSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/api/v1/service/util.go:44`



---


[function] name: InternalPolicyLocal file: pkg/api/v1/service/util.go:86 returns_error: нет description: InternalPolicyLocal checks if service has ITP = Local.


### InternalPolicyLocal (pkg/api/v1/service/util.go:86)


InternalPolicyLocal checks if service has ITP = Local.


```go
func InternalPolicyLocal((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


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


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/service/util.go:86`



---


[function] name: IsAllowAll file: pkg/api/v1/service/util.go:32 returns_error: нет description: IsAllowAll checks whether the utilnet.IPNet allows traffic from 0.0.0.0/0


### IsAllowAll (pkg/api/v1/service/util.go:32)


IsAllowAll checks whether the utilnet.IPNet allows traffic from 0.0.0.0/0


```go
func IsAllowAll((ipnets utilnet.IPNetSet)) (ipnets utilnet.IPNetSet)
```


**Тип ответа:** ipnets


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilnet.IPNetSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/api/v1/service/util.go:32`



---


[function] name: NeedsHealthCheck file: pkg/api/v1/service/util.go:94 returns_error: нет description: NeedsHealthCheck checks if service needs health check.


### NeedsHealthCheck (pkg/api/v1/service/util.go:94)


NeedsHealthCheck checks if service needs health check.


```go
func NeedsHealthCheck((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


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


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/api/v1/service/util.go:94`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](hack_tools.md)

- [Следующая директория](pkg_apis.md)


---

