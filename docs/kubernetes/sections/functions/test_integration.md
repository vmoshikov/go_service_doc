---
title: "Функции: test/integration"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/integration
---


# Функции: test/integration


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_instrumentation.md)

- [Следующая директория](test_list.md)


---


## Меню по файлам


- 📄 [test/integration/apiserver/cel/admission_test_util.go](#testintegrationapiserverceladmission_test_utilgo)

- 📄 [test/integration/apiserver/cel/authorizerselector/helper.go](#testintegrationapiservercelauthorizerselectorhelpergo)

- 📄 [test/integration/apiserver/discovery/framework.go](#testintegrationapiserverdiscoveryframeworkgo)

- 📄 [test/integration/apiserver/discovery/service.go](#testintegrationapiserverdiscoveryservicego)

- 📄 [test/integration/authutil/authutil.go](#testintegrationauthutilauthutilgo)

- 📄 [test/integration/benchmark/extractlog/main.go](#testintegrationbenchmarkextractlogmaingo)

- 📄 [test/integration/benchmark/jsonify/main.go](#testintegrationbenchmarkjsonifymaingo)

- 📄 [test/integration/daemonset/util.go](#testintegrationdaemonsetutilgo)

- 📄 [test/integration/deployment/util.go](#testintegrationdeploymentutilgo)

- 📄 [test/integration/dra/objects.go](#testintegrationdraobjectsgo)

- 📄 [test/integration/dra/resourceslicecontroller.go](#testintegrationdraresourceslicecontrollergo)

- 📄 [test/integration/etcd/data.go](#testintegrationetcddatago)

- 📄 [test/integration/etcd/server.go](#testintegrationetcdservergo)

- 📄 [test/integration/framework/cbor.go](#testintegrationframeworkcborgo)

- 📄 [test/integration/framework/controlplane_utils.go](#testintegrationframeworkcontrolplane_utilsgo)

- 📄 [test/integration/framework/etcd.go](#testintegrationframeworketcdgo)

- 📄 [test/integration/framework/goleak.go](#testintegrationframeworkgoleakgo)

- 📄 [test/integration/framework/logger.go](#testintegrationframeworkloggergo)

- 📄 [test/integration/framework/serializer.go](#testintegrationframeworkserializergo)

- 📄 [test/integration/framework/test_server.go](#testintegrationframeworktest_servergo)

- 📄 [test/integration/framework/util.go](#testintegrationframeworkutilgo)

- 📄 [test/integration/ipamperf/results.go](#testintegrationipamperfresultsgo)

- 📄 [test/integration/logs/benchmark/load.go](#testintegrationlogsbenchmarkloadgo)

- 📄 [test/integration/scheduler/queueing/queue.go](#testintegrationschedulerqueueingqueuego)

- 📄 [test/integration/scheduler/util.go](#testintegrationschedulerutilgo)

- 📄 [test/integration/scheduler_perf/dra.go](#testintegrationscheduler_perfdrago)

- 📄 [test/integration/scheduler_perf/executor.go](#testintegrationscheduler_perfexecutorgo)

- 📄 [test/integration/scheduler_perf/label_selector.go](#testintegrationscheduler_perflabel_selectorgo)

- 📄 [test/integration/scheduler_perf/node_util.go](#testintegrationscheduler_perfnode_utilgo)

- 📄 [test/integration/scheduler_perf/operations.go](#testintegrationscheduler_perfoperationsgo)

- 📄 [test/integration/scheduler_perf/options.go](#testintegrationscheduler_perfoptionsgo)

- 📄 [test/integration/scheduler_perf/scheduler_perf.go](#testintegrationscheduler_perfscheduler_perfgo)

- 📄 [test/integration/scheduler_perf/update.go](#testintegrationscheduler_perfupdatego)

- 📄 [test/integration/scheduler_perf/util.go](#testintegrationscheduler_perfutilgo)

- 📄 [test/integration/statefulset/util.go](#testintegrationstatefulsetutilgo)

- 📄 [test/integration/storageversionmigrator/util.go](#testintegrationstorageversionmigratorutilgo)

- 📄 [test/integration/util/util.go](#testintegrationutilutilgo)

- 📄 [test/integration/utils.go](#testintegrationutilsgo)

- 📄 [test/integration/volumescheduling/util.go](#testintegrationvolumeschedulingutilgo)


---


## test/integration/apiserver/cel/admission_test_util.go


📄 Исходный файл: `test/integration/apiserver/cel/admission_test_util.go`


<details open>
<summary><b>Функции в этом файле (30)</b></summary>


- 🔗 [createOrGetResource](#createorgetresource-testintegrationapiserverceladmission_test_utilgo490) `:490`

- 🔗 [expect](#expect-testintegrationapiserverceladmission_test_utilgo265) `:265`

- 🔗 [getParentGVR](#getparentgvr-testintegrationapiserverceladmission_test_utilgo748) `:748`

- 🔗 [getStubObj](#getstubobj-testintegrationapiserverceladmission_test_utilgo464) `:464`

- 🔗 [getTestFunc](#gettestfunc-testintegrationapiserverceladmission_test_utilgo445) `:445`

- 🔗 [gvk](#gvk-testintegrationapiserverceladmission_test_utilgo512) `:512`

- 🔗 [gvr](#gvr-testintegrationapiserverceladmission_test_utilgo509) `:509`

- 🔗 [record](#record-testintegrationapiserverceladmission_test_utilgo307) `:307`

- 🔗 [reset](#reset-testintegrationapiserverceladmission_test_utilgo239) `:239`

- 🔗 [shouldTestResource](#shouldtestresource-testintegrationapiserverceladmission_test_utilgo522) `:522`

- 🔗 [shouldTestResourceVerb](#shouldtestresourceverb-testintegrationapiserverceladmission_test_utilgo526) `:526`

- 🔗 [testDeploymentRollback](#testdeploymentrollback-testintegrationapiserverceladmission_test_utilgo906) `:906`

- 🔗 [testNamespaceDelete](#testnamespacedelete-testintegrationapiserverceladmission_test_utilgo863) `:863`

- 🔗 [testPodBindingEviction](#testpodbindingeviction-testintegrationapiserverceladmission_test_utilgo990) `:990`

- 🔗 [testPodConnectSubresource](#testpodconnectsubresource-testintegrationapiserverceladmission_test_utilgo955) `:955`

- 🔗 [testPruningRandomNumbers](#testpruningrandomnumbers-testintegrationapiserverceladmission_test_utilgo1088) `:1088`

- 🔗 [testResourceCreate](#testresourcecreate-testintegrationapiserverceladmission_test_utilgo534) `:534`

- 🔗 [testResourceDelete](#testresourcedelete-testintegrationapiserverceladmission_test_utilgo587) `:587`

- 🔗 [testResourceDeletecollection](#testresourcedeletecollection-testintegrationapiserverceladmission_test_utilgo699) `:699`

- 🔗 [testResourcePatch](#testresourcepatch-testintegrationapiserverceladmission_test_utilgo568) `:568`

- 🔗 [testResourceUpdate](#testresourceupdate-testintegrationapiserverceladmission_test_utilgo552) `:552`

- 🔗 [testSubresourcePatch](#testsubresourcepatch-testintegrationapiserverceladmission_test_utilgo821) `:821`

- 🔗 [testSubresourceProxy](#testsubresourceproxy-testintegrationapiserverceladmission_test_utilgo1042) `:1042`

- 🔗 [testSubresourceUpdate](#testsubresourceupdate-testintegrationapiserverceladmission_test_utilgo779) `:779`

- 🔗 [testTokenCreate](#testtokencreate-testintegrationapiserverceladmission_test_utilgo758) `:758`

- 🔗 [unimplemented](#unimplemented-testintegrationapiserverceladmission_test_utilgo851) `:851`

- 🔗 [verify](#verify-testintegrationapiserverceladmission_test_utilgo362) `:362`

- 🔗 [verifyObject](#verifyobject-testintegrationapiserverceladmission_test_utilgo421) `:421`

- 🔗 [verifyOptions](#verifyoptions-testintegrationapiserverceladmission_test_utilgo435) `:435`

- 🔗 [verifyRequest](#verifyrequest-testintegrationapiserverceladmission_test_utilgo373) `:373`


</details>


[function] name: createOrGetResource file: test/integration/apiserver/cel/admission_test_util.go:490 returns_error: да description: —


### createOrGetResource (test/integration/apiserver/cel/admission_test_util.go:490)


createOrGetResource is a function that performs operations based on the provided parameters and may return an error.


```go
func createOrGetResource((*unstructured.Unstructured, error)) (*unstructured.Unstructured, error)
```


**Тип запроса:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Тип ответа:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*unstructured.Unstructured`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:490`



---


[function] name: expect file: test/integration/apiserver/cel/admission_test_util.go:265 returns_error: нет description: —


### expect (test/integration/apiserver/cel/admission_test_util.go:265)


expect is a method that performs operations based on the provided parameters and returns (gvr schema.GroupVersionResource, gvk, optionsGVK schema.GroupVersionKind, operation v1.Operation, name, namespace string, object, oldObject, options bool).


```go
func (h *holder) expect((gvr schema.GroupVersionResource, gvk, optionsGVK schema.GroupVersionKind, operation v1.Operation, name, namespace string, object, oldObject, options bool)) (gvr schema.GroupVersionResource, gvk, optionsGVK schema.GroupVersionKind, operation v1.Operation, name, namespace string, object, oldObject, options bool)
```


**Тип ответа:** gvr


```json
{
  "finalizerEstimateSeconds": 0,
  "numRemaining": 0,
  "finalizersToNumRemaining": {}
}
```


*Определено в:* `pkg/controller/namespace/deletion/namespaced_resources_deleter.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** gvk


```json
{
  "discoveryClient": {},
  "mu": {},
  "gvkParser": null,
  "lastChecked": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/unstructured.go`


**Тип ответа:** optionsGVK


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** schema.GroupVersionKind


```json
{
  "Group": "string",
  "Version": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


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


**Тип ответа:** v1.Operation


```json
{
  "Type": {},
  "Options": [],
  "Request": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


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


**Тип ответа:** object


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** oldObject


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:265`



---


[function] name: getParentGVR file: test/integration/apiserver/cel/admission_test_util.go:748 returns_error: нет description: —


### getParentGVR (test/integration/apiserver/cel/admission_test_util.go:748)


getParentGVR is a function that performs operations based on the provided parameters and returns (gvr schema.GroupVersionResource).


```go
func getParentGVR((gvr schema.GroupVersionResource)) (gvr schema.GroupVersionResource)
```


**Тип ответа:** gvr


```json
{
  "finalizerEstimateSeconds": 0,
  "numRemaining": 0,
  "finalizersToNumRemaining": {}
}
```


*Определено в:* `pkg/controller/namespace/deletion/namespaced_resources_deleter.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:748`



---


[function] name: getStubObj file: test/integration/apiserver/cel/admission_test_util.go:464 returns_error: да description: —


### getStubObj (test/integration/apiserver/cel/admission_test_util.go:464)


getStubObj is a function that performs operations based on the provided parameters and may return an error.


```go
func getStubObj((*unstructured.Unstructured, error)) (*unstructured.Unstructured, error)
```


**Тип запроса:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Тип ответа:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*unstructured.Unstructured`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:464`



---


[function] name: getTestFunc file: test/integration/apiserver/cel/admission_test_util.go:445 returns_error: нет description: —


### getTestFunc (test/integration/apiserver/cel/admission_test_util.go:445)


getTestFunc is a function that performs operations based on the provided parameters and returns (gvr schema.GroupVersionResource, verb string).


```go
func getTestFunc((gvr schema.GroupVersionResource, verb string)) (gvr schema.GroupVersionResource, verb string)
```


**Тип ответа:** gvr


```json
{
  "finalizerEstimateSeconds": 0,
  "numRemaining": 0,
  "finalizersToNumRemaining": {}
}
```


*Определено в:* `pkg/controller/namespace/deletion/namespaced_resources_deleter.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** verb


```json
{
  "value": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/pflags.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:445`



---


[function] name: gvk file: test/integration/apiserver/cel/admission_test_util.go:512 returns_error: нет description: —


### gvk (test/integration/apiserver/cel/admission_test_util.go:512)


gvk is a function that performs operations based on the provided parameters and returns (group, version, kind string).


```go
func gvk((group, version, kind string)) (group, version, kind string)
```


**Тип ответа:** group


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/interface.go`


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:512`



---


[function] name: gvr file: test/integration/apiserver/cel/admission_test_util.go:509 returns_error: нет description: —


### gvr (test/integration/apiserver/cel/admission_test_util.go:509)


gvr is a function that performs operations based on the provided parameters and returns (group, version, resource string).


```go
func gvr((group, version, resource string)) (group, version, resource string)
```


**Тип ответа:** group


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/interface.go`


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:509`



---


[function] name: record file: test/integration/apiserver/cel/admission_test_util.go:307 returns_error: нет description: —


### record (test/integration/apiserver/cel/admission_test_util.go:307)


record is a method that performs operations based on the provided parameters and returns (version string, phase string, converted bool, request *admissionRequest).


```go
func (h *holder) record((version string, phase string, converted bool, request *admissionRequest)) (version string, phase string, converted bool, request *admissionRequest)
```


**Тип запроса:** admissionRequest


```json
{
  "Operation": "string",
  "Resource": {},
  "SubResource": "string",
  "Namespace": "string",
  "Name": "string",
  "Object": {},
  "OldObject": {},
  "Options": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


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


**Тип ответа:** converted


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** admissionRequest


```json
{
  "Operation": "string",
  "Resource": {},
  "SubResource": "string",
  "Namespace": "string",
  "Name": "string",
  "Object": {},
  "OldObject": {},
  "Options": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:307`



---


[function] name: reset file: test/integration/apiserver/cel/admission_test_util.go:239 returns_error: нет description: —


### reset (test/integration/apiserver/cel/admission_test_util.go:239)


reset is a method that performs operations based on the provided parameters and returns (t *testing.T).


```go
func (h *holder) reset((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:239`



---


[function] name: shouldTestResource file: test/integration/apiserver/cel/admission_test_util.go:522 returns_error: нет description: —


### shouldTestResource (test/integration/apiserver/cel/admission_test_util.go:522)


shouldTestResource is a function that performs operations based on the provided parameters and returns (gvr schema.GroupVersionResource, resource metav1.APIResource).


```go
func shouldTestResource((gvr schema.GroupVersionResource, resource metav1.APIResource)) (gvr schema.GroupVersionResource, resource metav1.APIResource)
```


**Тип ответа:** gvr


```json
{
  "finalizerEstimateSeconds": 0,
  "numRemaining": 0,
  "finalizersToNumRemaining": {}
}
```


*Определено в:* `pkg/controller/namespace/deletion/namespaced_resources_deleter.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


**Тип ответа:** metav1.APIResource


```json
{
  "name": "string",
  "singularName": "string",
  "namespaced": false,
  "group": "string",
  "version": "string",
  "kind": "string",
  "verbs": {},
  "shortNames": [],
  "categories": [],
  "storageVersionHash": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:522`



---


[function] name: shouldTestResourceVerb file: test/integration/apiserver/cel/admission_test_util.go:526 returns_error: нет description: —


### shouldTestResourceVerb (test/integration/apiserver/cel/admission_test_util.go:526)


shouldTestResourceVerb is a function that performs operations based on the provided parameters and returns (gvr schema.GroupVersionResource, resource metav1.APIResource, verb string).


```go
func shouldTestResourceVerb((gvr schema.GroupVersionResource, resource metav1.APIResource, verb string)) (gvr schema.GroupVersionResource, resource metav1.APIResource, verb string)
```


**Тип ответа:** gvr


```json
{
  "finalizerEstimateSeconds": 0,
  "numRemaining": 0,
  "finalizersToNumRemaining": {}
}
```


*Определено в:* `pkg/controller/namespace/deletion/namespaced_resources_deleter.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


**Тип ответа:** metav1.APIResource


```json
{
  "name": "string",
  "singularName": "string",
  "namespaced": false,
  "group": "string",
  "version": "string",
  "kind": "string",
  "verbs": {},
  "shortNames": [],
  "categories": [],
  "storageVersionHash": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** verb


```json
{
  "value": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/pflags.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:526`



---


[function] name: testDeploymentRollback file: test/integration/apiserver/cel/admission_test_util.go:906 returns_error: нет description: testDeploymentRollback verifies rollback-specific behavior:
- creates a parent deployment
- creates a rollback object an


### testDeploymentRollback (test/integration/apiserver/cel/admission_test_util.go:906)


testDeploymentRollback verifies rollback-specific behavior:
- creates a parent deployment
- creates a rollback object and posts it


```go
func testDeploymentRollback((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:906`



---


[function] name: testNamespaceDelete file: test/integration/apiserver/cel/admission_test_util.go:863 returns_error: нет description: testNamespaceDelete verifies namespace-specific delete behavior:
- ensures admission is called on first delete (which on


### testNamespaceDelete (test/integration/apiserver/cel/admission_test_util.go:863)


testNamespaceDelete verifies namespace-specific delete behavior:
- ensures admission is called on first delete (which only sets deletionTimestamp and terminating state)
- removes finalizer from namespace
- ensures admission is called on final delete once finalizers are removed


```go
func testNamespaceDelete((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:863`



---


[function] name: testPodBindingEviction file: test/integration/apiserver/cel/admission_test_util.go:990 returns_error: нет description: testPodBindingEviction verifies pod binding and eviction admission


### testPodBindingEviction (test/integration/apiserver/cel/admission_test_util.go:990)


testPodBindingEviction verifies pod binding and eviction admission


```go
func testPodBindingEviction((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:990`



---


[function] name: testPodConnectSubresource file: test/integration/apiserver/cel/admission_test_util.go:955 returns_error: нет description: testPodConnectSubresource verifies connect subresources


### testPodConnectSubresource (test/integration/apiserver/cel/admission_test_util.go:955)


testPodConnectSubresource verifies connect subresources


```go
func testPodConnectSubresource((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:955`



---


[function] name: testPruningRandomNumbers file: test/integration/apiserver/cel/admission_test_util.go:1088 returns_error: нет description: —


### testPruningRandomNumbers (test/integration/apiserver/cel/admission_test_util.go:1088)


testPruningRandomNumbers is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testPruningRandomNumbers((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:1088`



---


[function] name: testResourceCreate file: test/integration/apiserver/cel/admission_test_util.go:534 returns_error: нет description: generic resource testing


### testResourceCreate (test/integration/apiserver/cel/admission_test_util.go:534)


generic resource testing


```go
func testResourceCreate((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:534`



---


[function] name: testResourceDelete file: test/integration/apiserver/cel/admission_test_util.go:587 returns_error: нет description: —


### testResourceDelete (test/integration/apiserver/cel/admission_test_util.go:587)


testResourceDelete is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testResourceDelete((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:587`



---


[function] name: testResourceDeletecollection file: test/integration/apiserver/cel/admission_test_util.go:699 returns_error: нет description: —


### testResourceDeletecollection (test/integration/apiserver/cel/admission_test_util.go:699)


testResourceDeletecollection is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testResourceDeletecollection((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:699`



---


[function] name: testResourcePatch file: test/integration/apiserver/cel/admission_test_util.go:568 returns_error: нет description: —


### testResourcePatch (test/integration/apiserver/cel/admission_test_util.go:568)


testResourcePatch is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testResourcePatch((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:568`



---


[function] name: testResourceUpdate file: test/integration/apiserver/cel/admission_test_util.go:552 returns_error: нет description: —


### testResourceUpdate (test/integration/apiserver/cel/admission_test_util.go:552)


testResourceUpdate is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testResourceUpdate((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:552`



---


[function] name: testSubresourcePatch file: test/integration/apiserver/cel/admission_test_util.go:821 returns_error: нет description: —


### testSubresourcePatch (test/integration/apiserver/cel/admission_test_util.go:821)


testSubresourcePatch is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testSubresourcePatch((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:821`



---


[function] name: testSubresourceProxy file: test/integration/apiserver/cel/admission_test_util.go:1042 returns_error: нет description: testSubresourceProxy verifies proxy subresources


### testSubresourceProxy (test/integration/apiserver/cel/admission_test_util.go:1042)


testSubresourceProxy verifies proxy subresources


```go
func testSubresourceProxy((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:1042`



---


[function] name: testSubresourceUpdate file: test/integration/apiserver/cel/admission_test_util.go:779 returns_error: нет description: —


### testSubresourceUpdate (test/integration/apiserver/cel/admission_test_util.go:779)


testSubresourceUpdate is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testSubresourceUpdate((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:779`



---


[function] name: testTokenCreate file: test/integration/apiserver/cel/admission_test_util.go:758 returns_error: нет description: —


### testTokenCreate (test/integration/apiserver/cel/admission_test_util.go:758)


testTokenCreate is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func testTokenCreate((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:758`



---


[function] name: unimplemented file: test/integration/apiserver/cel/admission_test_util.go:851 returns_error: нет description: —


### unimplemented (test/integration/apiserver/cel/admission_test_util.go:851)


unimplemented is a function that performs operations based on the provided parameters and returns (c *testContext).


```go
func unimplemented((c *testContext)) (c *testContext)
```


**Тип запроса:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** testContext


```json
{
  "t": null,
  "emulateV1beta1Version": false,
  "admissionHolder": {},
  "client": {},
  "clientset": {},
  "verb": "string",
  "gvr": {},
  "resource": {},
  "resources": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:851`



---


[function] name: verify file: test/integration/apiserver/cel/admission_test_util.go:362 returns_error: нет description: —


### verify (test/integration/apiserver/cel/admission_test_util.go:362)


verify is a method that performs operations based on the provided parameters and returns (t *testing.T).


```go
func (h *holder) verify((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:362`



---


[function] name: verifyObject file: test/integration/apiserver/cel/admission_test_util.go:421 returns_error: нет description: —


### verifyObject (test/integration/apiserver/cel/admission_test_util.go:421)


verifyObject is a method that performs operations based on the provided parameters and returns (converted bool, obj runtime.Object).


```go
func (h *holder) verifyObject((converted bool, obj runtime.Object)) (converted bool, obj runtime.Object)
```


**Тип ответа:** converted


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


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:421`



---


[function] name: verifyOptions file: test/integration/apiserver/cel/admission_test_util.go:435 returns_error: нет description: —


### verifyOptions (test/integration/apiserver/cel/admission_test_util.go:435)


verifyOptions is a method that performs operations based on the provided parameters and returns (options runtime.Object).


```go
func (h *holder) verifyOptions((options runtime.Object)) (options runtime.Object)
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


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:435`



---


[function] name: verifyRequest file: test/integration/apiserver/cel/admission_test_util.go:373 returns_error: нет description: —


### verifyRequest (test/integration/apiserver/cel/admission_test_util.go:373)


verifyRequest is a method that performs operations based on the provided parameters and returns (webhookOptions webhookOptions, request *admissionRequest).


```go
func (h *holder) verifyRequest((webhookOptions webhookOptions, request *admissionRequest)) (webhookOptions webhookOptions, request *admissionRequest)
```


**Тип запроса:** admissionRequest


```json
{
  "Operation": "string",
  "Resource": {},
  "SubResource": "string",
  "Namespace": "string",
  "Name": "string",
  "Object": {},
  "OldObject": {},
  "Options": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


**Тип ответа:** webhookOptions


```json
{
  "version": "string",
  "phase": "string",
  "converted": false
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


**Тип ответа:** webhookOptions


```json
{
  "version": "string",
  "phase": "string",
  "converted": false
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


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


**Тип ответа:** admissionRequest


```json
{
  "Operation": "string",
  "Resource": {},
  "SubResource": "string",
  "Namespace": "string",
  "Name": "string",
  "Object": {},
  "OldObject": {},
  "Options": {}
}
```


*Определено в:* `test/integration/apiserver/cel/admission_test_util.go`


📍 *Расположение:* `test/integration/apiserver/cel/admission_test_util.go:373`




## test/integration/apiserver/cel/authorizerselector/helper.go


📄 Исходный файл: `test/integration/apiserver/cel/authorizerselector/helper.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [RunAuthzSelectorsLibraryTests](#runauthzselectorslibrarytests-testintegrationapiservercelauthorizerselectorhelpergo43) `:43`

- 🔗 [getCauses](#getcauses-testintegrationapiservercelauthorizerselectorhelpergo301) `:301`


</details>


[function] name: RunAuthzSelectorsLibraryTests file: test/integration/apiserver/cel/authorizerselector/helper.go:43 returns_error: нет description: —


### RunAuthzSelectorsLibraryTests (test/integration/apiserver/cel/authorizerselector/helper.go:43)


RunAuthzSelectorsLibraryTests is a function that performs operations based on the provided parameters and returns (t *testing.T, featureEnabled bool).


```go
func RunAuthzSelectorsLibraryTests((t *testing.T, featureEnabled bool)) (t *testing.T, featureEnabled bool)
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


**Тип ответа:** featureEnabled


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/cel/authorizerselector/helper.go:43`



---


[function] name: getCauses file: test/integration/apiserver/cel/authorizerselector/helper.go:301 returns_error: да description: —


### getCauses (test/integration/apiserver/cel/authorizerselector/helper.go:301)


getCauses is a function that performs operations based on the provided parameters and may return an error.


```go
func getCauses((t *testing.T, err error)) (t *testing.T, err error)
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


*Типы возврата:* `t *testing.T`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/cel/authorizerselector/helper.go:301`




## test/integration/apiserver/discovery/framework.go


📄 Исходный файл: `test/integration/apiserver/discovery/framework.go`


<details open>
<summary><b>Функции в этом файле (32)</b></summary>


- 🔗 [Cleanup](#cleanup-testintegrationapiserverdiscoveryframeworkgo140) `:140`

- 🔗 [Cleanup](#cleanup-testintegrationapiserverdiscoveryframeworkgo209) `:209`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo112) `:112`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo173) `:173`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo242) `:242`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo253) `:253`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo270) `:270`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo287) `:287`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo304) `:304`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo321) `:321`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo338) `:338`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo355) `:355`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo398) `:398`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo434) `:434`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo463) `:463`

- 🔗 [Do](#do-testintegrationapiserverdiscoveryframeworkgo486) `:486`

- 🔗 [FetchNoPeerDiscovery](#fetchnopeerdiscovery-testintegrationapiserverdiscoveryframeworkgo723) `:723`

- 🔗 [FetchPeerAggregatedDiscovery](#fetchpeeraggregateddiscovery-testintegrationapiserverdiscoveryframeworkgo747) `:747`

- 🔗 [FetchV1DiscoveryGroups](#fetchv1discoverygroups-testintegrationapiserverdiscoveryframeworkgo513) `:513`

- 🔗 [FetchV1DiscoveryGroupsAtPath](#fetchv1discoverygroupsatpath-testintegrationapiserverdiscoveryframeworkgo521) `:521`

- 🔗 [FetchV1DiscoveryLegacyGroups](#fetchv1discoverylegacygroups-testintegrationapiserverdiscoveryframeworkgo517) `:517`

- 🔗 [FetchV1DiscoveryResource](#fetchv1discoveryresource-testintegrationapiserverdiscoveryframeworkgo544) `:544`

- 🔗 [FetchV2Discovery](#fetchv2discovery-testintegrationapiserverdiscoveryframeworkgo490) `:490`

- 🔗 [FindGroupVersionV1](#findgroupversionv1-testintegrationapiserverdiscoveryframeworkgo690) `:690`

- 🔗 [FindGroupVersionV2](#findgroupversionv2-testintegrationapiserverdiscoveryframeworkgo706) `:706`

- 🔗 [WaitForGroups](#waitforgroups-testintegrationapiserverdiscoveryframeworkgo604) `:604`

- 🔗 [WaitForGroupsAbsent](#waitforgroupsabsent-testintegrationapiserverdiscoveryframeworkgo567) `:567`

- 🔗 [WaitForPeerAggregatedDiscoveryWithCondition](#waitforpeeraggregateddiscoverywithcondition-testintegrationapiserverdiscoveryframeworkgo771) `:771`

- 🔗 [WaitForResultWithCondition](#waitforresultwithcondition-testintegrationapiserverdiscoveryframeworkgo622) `:622`

- 🔗 [WaitForRootPaths](#waitforrootpaths-testintegrationapiserverdiscoveryframeworkgo581) `:581`

- 🔗 [WaitForV1GroupsWithCondition](#waitforv1groupswithcondition-testintegrationapiserverdiscoveryframeworkgo644) `:644`

- 🔗 [WaitForV1ResourcesWithCondition](#waitforv1resourceswithcondition-testintegrationapiserverdiscoveryframeworkgo667) `:667`


</details>


[function] name: Cleanup file: test/integration/apiserver/discovery/framework.go:140 returns_error: нет description: —


### Cleanup (test/integration/apiserver/discovery/framework.go:140)


Cleanup is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (a applyAPIService) Cleanup((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:140`



---


[function] name: Cleanup file: test/integration/apiserver/discovery/framework.go:209 returns_error: нет description: —


### Cleanup (test/integration/apiserver/discovery/framework.go:209)


Cleanup is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (a applyCRD) Cleanup((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:209`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:112 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:112)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (a applyAPIService) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:112`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:173 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:173)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (a applyCRD) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:173`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:242 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:242)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (d deleteObject) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:242`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:253 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:253)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForStaleGroupVersionsV2) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:253`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:270 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:270)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForFreshGroupVersionsV2) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:270`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:287 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:287)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForGroupVersionsV2) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:287`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:304 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:304)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForAbsentGroupVersionsV2) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:304`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:321 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:321)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForGroupVersionsV1) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:321`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:338 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:338)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForAbsentGroupVersionsV1) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:338`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:355 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:355)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForResourcesV1) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:355`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:398 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:398)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForResourcesAbsentV1) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:398`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:434 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:434)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForResourcesV2) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:434`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:463 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:463)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (w waitForResourcesAbsentV2) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:463`



---


[function] name: Do file: test/integration/apiserver/discovery/framework.go:486 returns_error: нет description: —


### Do (test/integration/apiserver/discovery/framework.go:486)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, client testClient).


```go
func (i inlineAction) Do((ctx context.Context, client testClient)) (ctx context.Context, client testClient)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:486`



---


[function] name: FetchNoPeerDiscovery file: test/integration/apiserver/discovery/framework.go:723 returns_error: да description: FetchNoPeerDiscovery explicitly requests no-peer discovery


### FetchNoPeerDiscovery (test/integration/apiserver/discovery/framework.go:723)


FetchNoPeerDiscovery explicitly requests no-peer discovery


```go
func FetchNoPeerDiscovery((apidiscoveryv2.APIGroupDiscoveryList, error)) (apidiscoveryv2.APIGroupDiscoveryList, error)
```


**Тип ответа:** apidiscoveryv2.APIGroupDiscoveryList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/apidiscovery/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `apidiscoveryv2.APIGroupDiscoveryList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:723`



---


[function] name: FetchPeerAggregatedDiscovery file: test/integration/apiserver/discovery/framework.go:747 returns_error: да description: FetchPeerAggregatedDiscovery explicitly requests peer-aggregated discovery


### FetchPeerAggregatedDiscovery (test/integration/apiserver/discovery/framework.go:747)


FetchPeerAggregatedDiscovery explicitly requests peer-aggregated discovery


```go
func FetchPeerAggregatedDiscovery((apidiscoveryv2.APIGroupDiscoveryList, error)) (apidiscoveryv2.APIGroupDiscoveryList, error)
```


**Тип ответа:** apidiscoveryv2.APIGroupDiscoveryList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/apidiscovery/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `apidiscoveryv2.APIGroupDiscoveryList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:747`



---


[function] name: FetchV1DiscoveryGroups file: test/integration/apiserver/discovery/framework.go:513 returns_error: да description: —


### FetchV1DiscoveryGroups (test/integration/apiserver/discovery/framework.go:513)


FetchV1DiscoveryGroups is a function that retrieves data based on the provided parameters and may return an error.


```go
func FetchV1DiscoveryGroups((metav1.APIGroupList, error)) (metav1.APIGroupList, error)
```


**Тип ответа:** metav1.APIGroupList


```json
{
  "groups": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metav1.APIGroupList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:513`



---


[function] name: FetchV1DiscoveryGroupsAtPath file: test/integration/apiserver/discovery/framework.go:521 returns_error: да description: —


### FetchV1DiscoveryGroupsAtPath (test/integration/apiserver/discovery/framework.go:521)


FetchV1DiscoveryGroupsAtPath is a function that retrieves data based on the provided parameters and may return an error.


```go
func FetchV1DiscoveryGroupsAtPath((metav1.APIGroupList, error)) (metav1.APIGroupList, error)
```


**Тип ответа:** metav1.APIGroupList


```json
{
  "groups": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metav1.APIGroupList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:521`



---


[function] name: FetchV1DiscoveryLegacyGroups file: test/integration/apiserver/discovery/framework.go:517 returns_error: да description: —


### FetchV1DiscoveryLegacyGroups (test/integration/apiserver/discovery/framework.go:517)


FetchV1DiscoveryLegacyGroups is a function that retrieves data based on the provided parameters and may return an error.


```go
func FetchV1DiscoveryLegacyGroups((metav1.APIGroupList, error)) (metav1.APIGroupList, error)
```


**Тип ответа:** metav1.APIGroupList


```json
{
  "groups": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metav1.APIGroupList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:517`



---


[function] name: FetchV1DiscoveryResource file: test/integration/apiserver/discovery/framework.go:544 returns_error: да description: —


### FetchV1DiscoveryResource (test/integration/apiserver/discovery/framework.go:544)


FetchV1DiscoveryResource is a function that retrieves data based on the provided parameters and may return an error.


```go
func FetchV1DiscoveryResource((metav1.APIResourceList, error)) (metav1.APIResourceList, error)
```


**Тип ответа:** metav1.APIResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `metav1.APIResourceList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:544`



---


[function] name: FetchV2Discovery file: test/integration/apiserver/discovery/framework.go:490 returns_error: да description: —


### FetchV2Discovery (test/integration/apiserver/discovery/framework.go:490)


FetchV2Discovery is a function that retrieves data based on the provided parameters and may return an error.


```go
func FetchV2Discovery((apidiscoveryv2.APIGroupDiscoveryList, error)) (apidiscoveryv2.APIGroupDiscoveryList, error)
```


**Тип ответа:** apidiscoveryv2.APIGroupDiscoveryList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/apidiscovery/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `apidiscoveryv2.APIGroupDiscoveryList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:490`



---


[function] name: FindGroupVersionV1 file: test/integration/apiserver/discovery/framework.go:690 returns_error: нет description: —


### FindGroupVersionV1 (test/integration/apiserver/discovery/framework.go:690)


FindGroupVersionV1 is a function that lists or finds data based on the provided parameters and returns (discovery metav1.APIGroupList, gv metav1.GroupVersion).


```go
func FindGroupVersionV1((discovery metav1.APIGroupList, gv metav1.GroupVersion)) (discovery metav1.APIGroupList, gv metav1.GroupVersion)
```


**Тип ответа:** discovery


```json
{
  "discoveryClient": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/scale/util.go`


**Тип ответа:** metav1.APIGroupList


```json
{
  "groups": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


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


**Тип ответа:** metav1.GroupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:690`



---


[function] name: FindGroupVersionV2 file: test/integration/apiserver/discovery/framework.go:706 returns_error: нет description: —


### FindGroupVersionV2 (test/integration/apiserver/discovery/framework.go:706)


FindGroupVersionV2 is a function that lists or finds data based on the provided parameters and returns (discovery apidiscoveryv2.APIGroupDiscoveryList, gv metav1.GroupVersion).


```go
func FindGroupVersionV2((discovery apidiscoveryv2.APIGroupDiscoveryList, gv metav1.GroupVersion)) (discovery apidiscoveryv2.APIGroupDiscoveryList, gv metav1.GroupVersion)
```


**Тип ответа:** discovery


```json
{
  "discoveryClient": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/scale/util.go`


**Тип ответа:** apidiscoveryv2.APIGroupDiscoveryList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/apidiscovery/types.go`


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


**Тип ответа:** metav1.GroupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:706`



---


[function] name: WaitForGroups file: test/integration/apiserver/discovery/framework.go:604 returns_error: нет description: —


### WaitForGroups (test/integration/apiserver/discovery/framework.go:604)


WaitForGroups is a function that performs operations based on the provided parameters and returns (ctx context.Context, client testClient, groups ...apidiscoveryv2.APIGroupDiscovery).


```go
func WaitForGroups((ctx context.Context, client testClient, groups ...apidiscoveryv2.APIGroupDiscovery)) (ctx context.Context, client testClient, groups ...apidiscoveryv2.APIGroupDiscovery)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groups


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apidiscoveryv2.APIGroupDiscovery


```json
{
  "Versions": []
}
```


*Определено в:* `pkg/apis/apidiscovery/types.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:604`



---


[function] name: WaitForGroupsAbsent file: test/integration/apiserver/discovery/framework.go:567 returns_error: нет description: —


### WaitForGroupsAbsent (test/integration/apiserver/discovery/framework.go:567)


WaitForGroupsAbsent is a function that performs operations based on the provided parameters and returns (ctx context.Context, client testClient, groups ...string).


```go
func WaitForGroupsAbsent((ctx context.Context, client testClient, groups ...string)) (ctx context.Context, client testClient, groups ...string)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** groups


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:567`



---


[function] name: WaitForPeerAggregatedDiscoveryWithCondition file: test/integration/apiserver/discovery/framework.go:771 returns_error: нет description: WaitForPeerAggregatedDiscoveryWithCondition waits for peer-aggregated discovery to satisfy a condition.


### WaitForPeerAggregatedDiscoveryWithCondition (test/integration/apiserver/discovery/framework.go:771)


WaitForPeerAggregatedDiscoveryWithCondition waits for peer-aggregated discovery to satisfy a condition.


```go
func WaitForPeerAggregatedDiscoveryWithCondition((ctx context.Context, client testClient, condition func(result apidiscoveryv2.APIGroupDiscoveryList) bool)) (ctx context.Context, client testClient, condition func(result apidiscoveryv2.APIGroupDiscoveryList) bool)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** result


```json
{
  "object": {},
  "err": {},
  "reason": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher.go`


**Тип ответа:** apidiscoveryv2.APIGroupDiscoveryList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/apidiscovery/types.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:771`



---


[function] name: WaitForResultWithCondition file: test/integration/apiserver/discovery/framework.go:622 returns_error: нет description: —


### WaitForResultWithCondition (test/integration/apiserver/discovery/framework.go:622)


WaitForResultWithCondition is a function that performs operations based on the provided parameters and returns (ctx context.Context, client testClient, condition func(result apidiscoveryv2.APIGroupDiscoveryList) bool).


```go
func WaitForResultWithCondition((ctx context.Context, client testClient, condition func(result apidiscoveryv2.APIGroupDiscoveryList) bool)) (ctx context.Context, client testClient, condition func(result apidiscoveryv2.APIGroupDiscoveryList) bool)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** result


```json
{
  "object": {},
  "err": {},
  "reason": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher.go`


**Тип ответа:** apidiscoveryv2.APIGroupDiscoveryList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/apidiscovery/types.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:622`



---


[function] name: WaitForRootPaths file: test/integration/apiserver/discovery/framework.go:581 returns_error: нет description: —


### WaitForRootPaths (test/integration/apiserver/discovery/framework.go:581)


WaitForRootPaths is a function that performs operations based on the provided parameters and returns (t *testing.T, ctx context.Context, client testClient, requirePaths, forbidPaths sets.Set[string]).


```go
func WaitForRootPaths((t *testing.T, ctx context.Context, client testClient, requirePaths, forbidPaths sets.Set[string])) (t *testing.T, ctx context.Context, client testClient, requirePaths, forbidPaths sets.Set[string])
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** requirePaths


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** forbidPaths


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:581`



---


[function] name: WaitForV1GroupsWithCondition file: test/integration/apiserver/discovery/framework.go:644 returns_error: нет description: —


### WaitForV1GroupsWithCondition (test/integration/apiserver/discovery/framework.go:644)


WaitForV1GroupsWithCondition is a function that performs operations based on the provided parameters and returns (ctx context.Context, client testClient, condition func(result metav1.APIGroupList) bool).


```go
func WaitForV1GroupsWithCondition((ctx context.Context, client testClient, condition func(result metav1.APIGroupList) bool)) (ctx context.Context, client testClient, condition func(result metav1.APIGroupList) bool)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** result


```json
{
  "object": {},
  "err": {},
  "reason": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher.go`


**Тип ответа:** metav1.APIGroupList


```json
{
  "groups": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:644`



---


[function] name: WaitForV1ResourcesWithCondition file: test/integration/apiserver/discovery/framework.go:667 returns_error: нет description: —


### WaitForV1ResourcesWithCondition (test/integration/apiserver/discovery/framework.go:667)


WaitForV1ResourcesWithCondition is a function that performs operations based on the provided parameters and returns (ctx context.Context, client testClient, gv metav1.GroupVersion, condition func(result metav1.APIResourceList) bool).


```go
func WaitForV1ResourcesWithCondition((ctx context.Context, client testClient, gv metav1.GroupVersion, condition func(result metav1.APIResourceList) bool)) (ctx context.Context, client testClient, gv metav1.GroupVersion, condition func(result metav1.APIResourceList) bool)
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


**Тип ответа:** testClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** metav1.GroupVersion


```json
{
  "Group": "string",
  "Version": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** result


```json
{
  "object": {},
  "err": {},
  "reason": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher.go`


**Тип ответа:** metav1.APIResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `test/integration/apiserver/discovery/framework.go:667`




## test/integration/apiserver/discovery/service.go


📄 Исходный файл: `test/integration/apiserver/discovery/service.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Name](#name-testintegrationapiserverdiscoveryservicego141) `:141`

- 🔗 [NewFakeService](#newfakeservice-testintegrationapiserverdiscoveryservicego56) `:56`

- 🔗 [Port](#port-testintegrationapiserverdiscoveryservicego133) `:133`

- 🔗 [Run](#run-testintegrationapiserverdiscoveryservicego64) `:64`

- 🔗 [WaitForReady](#waitforready-testintegrationapiserverdiscoveryservicego119) `:119`


</details>


[function] name: Name file: test/integration/apiserver/discovery/service.go:141 returns_error: нет description: —


### Name (test/integration/apiserver/discovery/service.go:141)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (f *fakeService) Name(()) ()
```


📍 *Расположение:* `test/integration/apiserver/discovery/service.go:141`



---


[function] name: NewFakeService file: test/integration/apiserver/discovery/service.go:56 returns_error: нет description: —


### NewFakeService (test/integration/apiserver/discovery/service.go:56)


NewFakeService is a function that performs operations based on the provided parameters and returns (name string, client kubernetes.Interface, handler http.Handler).


```go
func NewFakeService((name string, client kubernetes.Interface, handler http.Handler)) (name string, client kubernetes.Interface, handler http.Handler)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


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


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** http.Handler


```json
{
  "notify": [],
  "final": {},
  "once": {}
}
```


*Определено в:* `pkg/util/interrupt/interrupt.go`


📍 *Расположение:* `test/integration/apiserver/discovery/service.go:56`



---


[function] name: Port file: test/integration/apiserver/discovery/service.go:133 returns_error: нет description: —


### Port (test/integration/apiserver/discovery/service.go:133)


Port is a method that performs operations based on the provided parameters and returns ().


```go
func (f *fakeService) Port(()) ()
```


📍 *Расположение:* `test/integration/apiserver/discovery/service.go:133`



---


[function] name: Run file: test/integration/apiserver/discovery/service.go:64 returns_error: нет description: —


### Run (test/integration/apiserver/discovery/service.go:64)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (f *fakeService) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/integration/apiserver/discovery/service.go:64`



---


[function] name: WaitForReady file: test/integration/apiserver/discovery/service.go:119 returns_error: нет description: —


### WaitForReady (test/integration/apiserver/discovery/service.go:119)


WaitForReady is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (f *fakeService) WaitForReady((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/integration/apiserver/discovery/service.go:119`




## test/integration/authutil/authutil.go


📄 Исходный файл: `test/integration/authutil/authutil.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GrantServiceAccountAuthorization](#grantserviceaccountauthorization-testintegrationauthutilauthutilgo73) `:73`

- 🔗 [GrantUserAuthorization](#grantuserauthorization-testintegrationauthutilauthutilgo69) `:69`

- 🔗 [ServiceAccountClient](#serviceaccountclient-testintegrationauthutilauthutilgo141) `:141`

- 🔗 [WaitForNamedAuthorizationUpdate](#waitfornamedauthorizationupdate-testintegrationauthutilauthutilgo39) `:39`

- 🔗 [grantAuthorization](#grantauthorization-testintegrationauthutilauthutilgo77) `:77`


</details>


[function] name: GrantServiceAccountAuthorization file: test/integration/authutil/authutil.go:73 returns_error: нет description: —


### GrantServiceAccountAuthorization (test/integration/authutil/authutil.go:73)


GrantServiceAccountAuthorization is a function that performs operations based on the provided parameters and returns (t *testing.T, ctx context.Context, adminClient clientset.Interface, serviceAccountName, serviceAccountNamespace string, rule rbacv1.PolicyRule).


```go
func GrantServiceAccountAuthorization((t *testing.T, ctx context.Context, adminClient clientset.Interface, serviceAccountName, serviceAccountNamespace string, rule rbacv1.PolicyRule)) (t *testing.T, ctx context.Context, adminClient clientset.Interface, serviceAccountName, serviceAccountNamespace string, rule rbacv1.PolicyRule)
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


**Тип ответа:** adminClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** serviceAccountName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** serviceAccountNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/integration/authutil/authutil.go:73`



---


[function] name: GrantUserAuthorization file: test/integration/authutil/authutil.go:69 returns_error: нет description: —


### GrantUserAuthorization (test/integration/authutil/authutil.go:69)


GrantUserAuthorization is a function that performs operations based on the provided parameters and returns (t *testing.T, ctx context.Context, adminClient clientset.Interface, username string, rule rbacv1.PolicyRule).


```go
func GrantUserAuthorization((t *testing.T, ctx context.Context, adminClient clientset.Interface, username string, rule rbacv1.PolicyRule)) (t *testing.T, ctx context.Context, adminClient clientset.Interface, username string, rule rbacv1.PolicyRule)
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


**Тип ответа:** adminClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** username


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/integration/authutil/authutil.go:69`



---


[function] name: ServiceAccountClient file: test/integration/authutil/authutil.go:141 returns_error: нет description: —


### ServiceAccountClient (test/integration/authutil/authutil.go:141)


ServiceAccountClient is a function that performs operations based on the provided parameters and returns (namespace, name string).


```go
func ServiceAccountClient((namespace, name string)) (namespace, name string)
```


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


📍 *Расположение:* `test/integration/authutil/authutil.go:141`



---


[function] name: WaitForNamedAuthorizationUpdate file: test/integration/authutil/authutil.go:39 returns_error: нет description: WaitForNamedAuthorizationUpdate checks if the given user can perform the named verb and action on the named resource.
Co


### WaitForNamedAuthorizationUpdate (test/integration/authutil/authutil.go:39)


WaitForNamedAuthorizationUpdate checks if the given user can perform the named verb and action on the named resource.
Copied from k8s.io/kubernetes/test/e2e/framework/auth.


```go
func WaitForNamedAuthorizationUpdate((t *testing.T, ctx context.Context, c authorizationv1client.SubjectAccessReviewsGetter, user, namespace, verb, resourceName string, resource schema.GroupResource, allowed bool)) (t *testing.T, ctx context.Context, c authorizationv1client.SubjectAccessReviewsGetter, user, namespace, verb, resourceName string, resource schema.GroupResource, allowed bool)
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


**Тип ответа:** authorizationv1client.SubjectAccessReviewsGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** user


```json
{
  "agent": "string",
  "rt": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** verb


```json
{
  "value": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/pflags.go`


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


**Тип ответа:** schema.GroupResource


```json
{
  "Group": "string",
  "Resource": "string"
}
```


*Определено в:* `pkg/controller/garbagecollector/config/types.go`


**Тип ответа:** allowed


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/authutil/authutil.go:39`



---


[function] name: grantAuthorization file: test/integration/authutil/authutil.go:77 returns_error: нет description: —


### grantAuthorization (test/integration/authutil/authutil.go:77)


grantAuthorization is a function that performs operations based on the provided parameters and returns (t *testing.T, ctx context.Context, adminClient clientset.Interface, name, namespace, accountKind string, rule rbacv1.PolicyRule).


```go
func grantAuthorization((t *testing.T, ctx context.Context, adminClient clientset.Interface, name, namespace, accountKind string, rule rbacv1.PolicyRule)) (t *testing.T, ctx context.Context, adminClient clientset.Interface, name, namespace, accountKind string, rule rbacv1.PolicyRule)
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


**Тип ответа:** adminClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** accountKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/integration/authutil/authutil.go:77`




## test/integration/benchmark/extractlog/main.go


📄 Исходный файл: `test/integration/benchmark/extractlog/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [extractRawLog](#extractrawlog-testintegrationbenchmarkextractlogmaingo50) `:50`

- 🔗 [jsonToRawLog](#jsontorawlog-testintegrationbenchmarkextractlogmaingo42) `:42`

- 🔗 [main](#main-testintegrationbenchmarkextractlogmaingo27) `:27`


</details>


[function] name: extractRawLog file: test/integration/benchmark/extractlog/main.go:50 returns_error: нет description: —


### extractRawLog (test/integration/benchmark/extractlog/main.go:50)


extractRawLog is a function that performs operations based on the provided parameters and returns (r io.Reader).


```go
func extractRawLog((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


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


📍 *Расположение:* `test/integration/benchmark/extractlog/main.go:50`



---


[function] name: jsonToRawLog file: test/integration/benchmark/extractlog/main.go:42 returns_error: да description: jsonToRawLog converts a single line of json formatted log to raw log.
If there is an error, it returns the original inpu


### jsonToRawLog (test/integration/benchmark/extractlog/main.go:42)


jsonToRawLog converts a single line of json formatted log to raw log.
If there is an error, it returns the original input.


```go
func jsonToRawLog((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/benchmark/extractlog/main.go:42`



---


[function] name: main file: test/integration/benchmark/extractlog/main.go:27 returns_error: нет description: —


### main (test/integration/benchmark/extractlog/main.go:27)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/integration/benchmark/extractlog/main.go:27`




## test/integration/benchmark/jsonify/main.go


📄 Исходный файл: `test/integration/benchmark/jsonify/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [appendIfMeasured](#appendifmeasured-testintegrationbenchmarkjsonifymaingo92) `:92`

- 🔗 [main](#main-testintegrationbenchmarkjsonifymaingo56) `:56`

- 🔗 [run](#run-testintegrationbenchmarkjsonifymaingo63) `:63`


</details>


[function] name: appendIfMeasured file: test/integration/benchmark/jsonify/main.go:92 returns_error: нет description: —


### appendIfMeasured (test/integration/benchmark/jsonify/main.go:92)


appendIfMeasured is a function that performs operations based on the provided parameters and returns (items []DataItem, benchmark *benchparse.Benchmark, metricType int, metricName string, unit string, value float64).


```go
func appendIfMeasured((items []DataItem, benchmark *benchparse.Benchmark, metricType int, metricName string, unit string, value float64)) (items []DataItem, benchmark *benchparse.Benchmark, metricType int, metricName string, unit string, value float64)
```


**Тип запроса:** benchparse.Benchmark


```json
{
  "Pods": [],
  "NamespaceNames": [],
  "NodeNames": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/testing/store_benchmarks.go`


**Тип ответа:** items


```json
{
  "path": [],
  "t": null,
  "expr": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/library/cost.go`


**Тип ответа:** DataItem


```json
{
  "Data": {},
  "Unit": "string",
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


**Тип ответа:** benchmark


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** benchparse.Benchmark


```json
{
  "Pods": [],
  "NamespaceNames": [],
  "NodeNames": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/testing/store_benchmarks.go`


**Тип ответа:** metricType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metricName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** unit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/integration/benchmark/jsonify/main.go:92`



---


[function] name: main file: test/integration/benchmark/jsonify/main.go:56 returns_error: нет description: —


### main (test/integration/benchmark/jsonify/main.go:56)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/integration/benchmark/jsonify/main.go:56`



---


[function] name: run file: test/integration/benchmark/jsonify/main.go:63 returns_error: нет description: —


### run (test/integration/benchmark/jsonify/main.go:63)


run is a function that performs operations based on the provided parameters and returns ().


```go
func run(()) ()
```


📍 *Расположение:* `test/integration/benchmark/jsonify/main.go:63`




## test/integration/daemonset/util.go


📄 Исходный файл: `test/integration/daemonset/util.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Handles](#handles-testintegrationdaemonsetutilgo36) `:36`

- 🔗 [Validate](#validate-testintegrationdaemonsetutilgo40) `:40`


</details>


[function] name: Handles file: test/integration/daemonset/util.go:36 returns_error: нет description: —


### Handles (test/integration/daemonset/util.go:36)


Handles is a method that handles or processes requests based on the provided parameters and returns (operation admission.Operation).


```go
func (f *fakePodFailAdmission) Handles((operation admission.Operation)) (operation admission.Operation)
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


📍 *Расположение:* `test/integration/daemonset/util.go:36`



---


[function] name: Validate file: test/integration/daemonset/util.go:40 returns_error: да description: —


### Validate (test/integration/daemonset/util.go:40)


Validate is a method that performs operations based on the provided parameters and may return an error.


```go
func (f *fakePodFailAdmission) Validate((err error)) (err error)
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


📍 *Расположение:* `test/integration/daemonset/util.go:40`




## test/integration/deployment/util.go


📄 Исходный файл: `test/integration/deployment/util.go`


<details open>
<summary><b>Функции в этом файле (32)</b></summary>


- 🔗 [addPodConditionReady](#addpodconditionready-testintegrationdeploymentutilgo162) `:162`

- 🔗 [checkDeploymentStatusReplicasFields](#checkdeploymentstatusreplicasfields-testintegrationdeploymentutilgo507) `:507`

- 🔗 [dcSetup](#dcsetup-testintegrationdeploymentutilgo106) `:106`

- 🔗 [dcSimpleSetup](#dcsimplesetup-testintegrationdeploymentutilgo140) `:140`

- 🔗 [deploymentComplete](#deploymentcomplete-testintegrationdeploymentutilgo255) `:255`

- 🔗 [expectNewReplicaSet](#expectnewreplicaset-testintegrationdeploymentutilgo376) `:376`

- 🔗 [expectNoNewReplicaSet](#expectnonewreplicaset-testintegrationdeploymentutilgo365) `:365`

- 🔗 [getNewReplicaSet](#getnewreplicaset-testintegrationdeploymentutilgo353) `:353`

- 🔗 [listUpdatedPods](#listupdatedpods-testintegrationdeploymentutilgo399) `:399`

- 🔗 [markPodReady](#markpodready-testintegrationdeploymentutilgo182) `:182`

- 🔗 [markUpdatedPodsReady](#markupdatedpodsready-testintegrationdeploymentutilgo190) `:190`

- 🔗 [markUpdatedPodsReadyWithoutComplete](#markupdatedpodsreadywithoutcomplete-testintegrationdeploymentutilgo468) `:468`

- 🔗 [newDeployment](#newdeployment-testintegrationdeploymentutilgo71) `:71`

- 🔗 [removeRSPods](#removerspods-testintegrationdeploymentutilgo534) `:534`

- 🔗 [removeTerminatedPods](#removeterminatedpods-testintegrationdeploymentutilgo226) `:226`

- 🔗 [runControllersAndInformers](#runcontrollersandinformers-testintegrationdeploymentutilgo153) `:153`

- 🔗 [scaleDeployment](#scaledeployment-testintegrationdeploymentutilgo430) `:430`

- 🔗 [testLabels](#testlabels-testintegrationdeploymentutilgo66) `:66`

- 🔗 [updateDeployment](#updatedeployment-testintegrationdeploymentutilgo342) `:342`

- 🔗 [updateReplicaSet](#updatereplicaset-testintegrationdeploymentutilgo387) `:387`

- 🔗 [waitForDeploymentComplete](#waitfordeploymentcomplete-testintegrationdeploymentutilgo272) `:272`

- 🔗 [waitForDeploymentCompleteAndCheckRolling](#waitfordeploymentcompleteandcheckrolling-testintegrationdeploymentutilgo265) `:265`

- 🔗 [waitForDeploymentCompleteAndCheckRollingAndMarkPodsReady](#waitfordeploymentcompleteandcheckrollingandmarkpodsready-testintegrationdeploymentutilgo279) `:279`

- 🔗 [waitForDeploymentCompleteAndMarkPodsReady](#waitfordeploymentcompleteandmarkpodsready-testintegrationdeploymentutilgo299) `:299`

- 🔗 [waitForDeploymentCompleteAndMarkPodsReadyAndRemoveTerminated](#waitfordeploymentcompleteandmarkpodsreadyandremoveterminated-testintegrationdeploymentutilgo320) `:320`

- 🔗 [waitForDeploymentRevisionAndImage](#waitfordeploymentrevisionandimage-testintegrationdeploymentutilgo175) `:175`

- 🔗 [waitForDeploymentStatusReplicasFields](#waitfordeploymentstatusreplicasfields-testintegrationdeploymentutilgo492) `:492`

- 🔗 [waitForDeploymentUpdatedReplicasGTE](#waitfordeploymentupdatedreplicasgte-testintegrationdeploymentutilgo391) `:391`

- 🔗 [waitForDeploymentWithCondition](#waitfordeploymentwithcondition-testintegrationdeploymentutilgo395) `:395`

- 🔗 [waitForObservedDeployment](#waitforobserveddeployment-testintegrationdeploymentutilgo346) `:346`

- 🔗 [waitForReadyReplicas](#waitforreadyreplicas-testintegrationdeploymentutilgo454) `:454`

- 🔗 [waitRSStable](#waitrsstable-testintegrationdeploymentutilgo426) `:426`


</details>


[function] name: addPodConditionReady file: test/integration/deployment/util.go:162 returns_error: нет description: addPodConditionReady sets given pod status to ready at given time


### addPodConditionReady (test/integration/deployment/util.go:162)


addPodConditionReady sets given pod status to ready at given time


```go
func addPodConditionReady((pod *v1.Pod, time metav1.Time)) (pod *v1.Pod, time metav1.Time)
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


**Тип ответа:** time


```json
{
  "impl": {},
  "criSocket": "string",
  "runtimeService": {},
  "imageService": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/runtime/runtime.go`


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


📍 *Расположение:* `test/integration/deployment/util.go:162`



---


[function] name: checkDeploymentStatusReplicasFields file: test/integration/deployment/util.go:507 returns_error: нет description: Verify all replicas fields of DeploymentStatus have desired count.
Immediately return an error when found a non-matching


### checkDeploymentStatusReplicasFields (test/integration/deployment/util.go:507)


Verify all replicas fields of DeploymentStatus have desired count.
Immediately return an error when found a non-matching replicas field.


```go
func (d *deploymentTester) checkDeploymentStatusReplicasFields((replicas, updatedReplicas, readyReplicas, availableReplicas, unavailableReplicas int32, terminatingReplicas *int32)) (replicas, updatedReplicas, readyReplicas, availableReplicas, unavailableReplicas int32, terminatingReplicas *int32)
```


**Тип ответа:** replicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updatedReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** readyReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** availableReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** unavailableReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** terminatingReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:507`



---


[function] name: dcSetup file: test/integration/deployment/util.go:106 returns_error: нет description: dcSetup sets up necessities for Deployment integration test, including control plane, apiserver, informers, and clientse


### dcSetup (test/integration/deployment/util.go:106)


dcSetup sets up necessities for Deployment integration test, including control plane, apiserver, informers, and clientset


```go
func dcSetup((kubeapiservertesting.TearDownFunc, *replicaset.ReplicaSetController, *deployment.DeploymentController, informers.SharedInformerFactory, clientset.Interface)) (kubeapiservertesting.TearDownFunc, *replicaset.ReplicaSetController, *deployment.DeploymentController, informers.SharedInformerFactory, clientset.Interface)
```


**Тип запроса:** replicaset.ReplicaSetController


```json
{
  "kubeClient": {},
  "podControl": {},
  "podIndexer": {},
  "eventBroadcaster": {},
  "burstReplicas": 0,
  "syncHandler": {},
  "expectations": null,
  "rsLister": {},
  "rsListerSynced": {},
  "rsIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "queue": {},
  "clock": {},
  "consistencyStore": {},
  "controllerFeatures": {}
}
```


*Определено в:* `pkg/controller/replicaset/replica_set.go`


**Тип запроса:** deployment.DeploymentController


```json
{
  "rsControl": {},
  "client": {},
  "eventBroadcaster": {},
  "eventRecorder": {},
  "syncHandler": {},
  "enqueueDeployment": {},
  "dLister": {},
  "rsLister": {},
  "podLister": {},
  "podIndexer": {},
  "dListerSynced": {},
  "rsListerSynced": {},
  "podListerSynced": {},
  "queue": {}
}
```


*Определено в:* `pkg/controller/deployment/deployment_controller.go`


**Тип ответа:** kubeapiservertesting.TearDownFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** replicaset.ReplicaSetController


```json
{
  "kubeClient": {},
  "podControl": {},
  "podIndexer": {},
  "eventBroadcaster": {},
  "burstReplicas": 0,
  "syncHandler": {},
  "expectations": null,
  "rsLister": {},
  "rsListerSynced": {},
  "rsIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "queue": {},
  "clock": {},
  "consistencyStore": {},
  "controllerFeatures": {}
}
```


*Определено в:* `pkg/controller/replicaset/replica_set.go`


**Тип ответа:** deployment.DeploymentController


```json
{
  "rsControl": {},
  "client": {},
  "eventBroadcaster": {},
  "eventRecorder": {},
  "syncHandler": {},
  "enqueueDeployment": {},
  "dLister": {},
  "rsLister": {},
  "podLister": {},
  "podIndexer": {},
  "dListerSynced": {},
  "rsListerSynced": {},
  "podListerSynced": {},
  "queue": {}
}
```


*Определено в:* `pkg/controller/deployment/deployment_controller.go`


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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `test/integration/deployment/util.go:106`



---


[function] name: dcSimpleSetup file: test/integration/deployment/util.go:140 returns_error: нет description: dcSimpleSetup sets up necessities for Deployment integration test, including control plane, apiserver,
and clientset, bu


### dcSimpleSetup (test/integration/deployment/util.go:140)


dcSimpleSetup sets up necessities for Deployment integration test, including control plane, apiserver,
and clientset, but not controllers and informers


```go
func dcSimpleSetup((kubeapiservertesting.TearDownFunc, clientset.Interface)) (kubeapiservertesting.TearDownFunc, clientset.Interface)
```


**Тип ответа:** kubeapiservertesting.TearDownFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `test/integration/deployment/util.go:140`



---


[function] name: deploymentComplete file: test/integration/deployment/util.go:255 returns_error: да description: —


### deploymentComplete (test/integration/deployment/util.go:255)


deploymentComplete is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *deploymentTester) deploymentComplete((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/deployment/util.go:255`



---


[function] name: expectNewReplicaSet file: test/integration/deployment/util.go:376 returns_error: да description: —


### expectNewReplicaSet (test/integration/deployment/util.go:376)


expectNewReplicaSet is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *deploymentTester) expectNewReplicaSet((*apps.ReplicaSet, error)) (*apps.ReplicaSet, error)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apps.ReplicaSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/deployment/util.go:376`



---


[function] name: expectNoNewReplicaSet file: test/integration/deployment/util.go:365 returns_error: нет description: —


### expectNoNewReplicaSet (test/integration/deployment/util.go:365)


expectNoNewReplicaSet is a method that performs operations based on the provided parameters and returns ().


```go
func (d *deploymentTester) expectNoNewReplicaSet(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:365`



---


[function] name: getNewReplicaSet file: test/integration/deployment/util.go:353 returns_error: да description: —


### getNewReplicaSet (test/integration/deployment/util.go:353)


getNewReplicaSet is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *deploymentTester) getNewReplicaSet((*apps.ReplicaSet, error)) (*apps.ReplicaSet, error)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apps.ReplicaSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/deployment/util.go:353`



---


[function] name: listUpdatedPods file: test/integration/deployment/util.go:399 returns_error: да description: —


### listUpdatedPods (test/integration/deployment/util.go:399)


listUpdatedPods is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *deploymentTester) listUpdatedPods(([]v1.Pod, error)) ([]v1.Pod, error)
```


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


*Типы возврата:* `[]v1.Pod`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/deployment/util.go:399`



---


[function] name: markPodReady file: test/integration/deployment/util.go:182 returns_error: нет description: —


### markPodReady (test/integration/deployment/util.go:182)


markPodReady is a function that performs operations based on the provided parameters and returns (c clientset.Interface, ns string, pod *v1.Pod).


```go
func markPodReady((c clientset.Interface, ns string, pod *v1.Pod)) (c clientset.Interface, ns string, pod *v1.Pod)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/deployment/util.go:182`



---


[function] name: markUpdatedPodsReady file: test/integration/deployment/util.go:190 returns_error: нет description: markUpdatedPodsReady manually marks updated Deployment pods status to ready,
until the deployment is complete


### markUpdatedPodsReady (test/integration/deployment/util.go:190)


markUpdatedPodsReady manually marks updated Deployment pods status to ready,
until the deployment is complete


```go
func (d *deploymentTester) markUpdatedPodsReady((wg *sync.WaitGroup)) (wg *sync.WaitGroup)
```


**Тип запроса:** sync.WaitGroup


```json
{
  "wg": {},
  "limiter": {},
  "stopCtx": {},
  "mu": {},
  "wait": false,
  "count": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/waitgroup/ratelimited_waitgroup.go`


**Тип ответа:** wg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sync.WaitGroup


```json
{
  "wg": {},
  "limiter": {},
  "stopCtx": {},
  "mu": {},
  "wait": false,
  "count": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/waitgroup/ratelimited_waitgroup.go`


📍 *Расположение:* `test/integration/deployment/util.go:190`



---


[function] name: markUpdatedPodsReadyWithoutComplete file: test/integration/deployment/util.go:468 returns_error: нет description: markUpdatedPodsReadyWithoutComplete marks updated Deployment pods as ready without waiting for deployment to complete.


### markUpdatedPodsReadyWithoutComplete (test/integration/deployment/util.go:468)


markUpdatedPodsReadyWithoutComplete marks updated Deployment pods as ready without waiting for deployment to complete.


```go
func (d *deploymentTester) markUpdatedPodsReadyWithoutComplete(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:468`



---


[function] name: newDeployment file: test/integration/deployment/util.go:71 returns_error: нет description: newDeployment returns a RollingUpdate Deployment with a fake container image


### newDeployment (test/integration/deployment/util.go:71)


newDeployment returns a RollingUpdate Deployment with a fake container image


```go
func newDeployment((name, ns string, replicas int32)) (name, ns string, replicas int32)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


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


**Тип ответа:** replicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:71`



---


[function] name: removeRSPods file: test/integration/deployment/util.go:534 returns_error: нет description: —


### removeRSPods (test/integration/deployment/util.go:534)


removeRSPods is a method that performs operations based on the provided parameters and returns (ctx context.Context, replicaset *apps.ReplicaSet, count int, targetOnlyTerminating bool, gracePeriodSeconds int64).


```go
func (d *deploymentTester) removeRSPods((ctx context.Context, replicaset *apps.ReplicaSet, count int, targetOnlyTerminating bool, gracePeriodSeconds int64)) (ctx context.Context, replicaset *apps.ReplicaSet, count int, targetOnlyTerminating bool, gracePeriodSeconds int64)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** replicaset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** count


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** targetOnlyTerminating


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gracePeriodSeconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:534`



---


[function] name: removeTerminatedPods file: test/integration/deployment/util.go:226 returns_error: нет description: removeTerminatedPods manually removes terminated Deployment pods,
until the deployment is complete


### removeTerminatedPods (test/integration/deployment/util.go:226)


removeTerminatedPods manually removes terminated Deployment pods,
until the deployment is complete


```go
func (d *deploymentTester) removeTerminatedPods((ctx context.Context, wg *sync.WaitGroup)) (ctx context.Context, wg *sync.WaitGroup)
```


**Тип запроса:** sync.WaitGroup


```json
{
  "wg": {},
  "limiter": {},
  "stopCtx": {},
  "mu": {},
  "wait": false,
  "count": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/waitgroup/ratelimited_waitgroup.go`


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


**Тип ответа:** wg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sync.WaitGroup


```json
{
  "wg": {},
  "limiter": {},
  "stopCtx": {},
  "mu": {},
  "wait": false,
  "count": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/waitgroup/ratelimited_waitgroup.go`


📍 *Расположение:* `test/integration/deployment/util.go:226`



---


[function] name: runControllersAndInformers file: test/integration/deployment/util.go:153 returns_error: нет description: runControllersAndInformers runs RS and deployment controllers and informers


### runControllersAndInformers (test/integration/deployment/util.go:153)


runControllersAndInformers runs RS and deployment controllers and informers


```go
func runControllersAndInformers((t *testing.T, rm *replicaset.ReplicaSetController, dc *deployment.DeploymentController, informers informers.SharedInformerFactory)) (t *testing.T, rm *replicaset.ReplicaSetController, dc *deployment.DeploymentController, informers informers.SharedInformerFactory)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** replicaset.ReplicaSetController


```json
{
  "kubeClient": {},
  "podControl": {},
  "podIndexer": {},
  "eventBroadcaster": {},
  "burstReplicas": 0,
  "syncHandler": {},
  "expectations": null,
  "rsLister": {},
  "rsListerSynced": {},
  "rsIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "queue": {},
  "clock": {},
  "consistencyStore": {},
  "controllerFeatures": {}
}
```


*Определено в:* `pkg/controller/replicaset/replica_set.go`


**Тип запроса:** deployment.DeploymentController


```json
{
  "rsControl": {},
  "client": {},
  "eventBroadcaster": {},
  "eventRecorder": {},
  "syncHandler": {},
  "enqueueDeployment": {},
  "dLister": {},
  "rsLister": {},
  "podLister": {},
  "podIndexer": {},
  "dListerSynced": {},
  "rsListerSynced": {},
  "podListerSynced": {},
  "queue": {}
}
```


*Определено в:* `pkg/controller/deployment/deployment_controller.go`


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


**Тип ответа:** rm


```json
{
  "Rules": [],
  "InverseRules": [],
  "path": "string"
}
```


*Определено в:* `cmd/import-boss/main.go`


**Тип ответа:** replicaset.ReplicaSetController


```json
{
  "kubeClient": {},
  "podControl": {},
  "podIndexer": {},
  "eventBroadcaster": {},
  "burstReplicas": 0,
  "syncHandler": {},
  "expectations": null,
  "rsLister": {},
  "rsListerSynced": {},
  "rsIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "queue": {},
  "clock": {},
  "consistencyStore": {},
  "controllerFeatures": {}
}
```


*Определено в:* `pkg/controller/replicaset/replica_set.go`


**Тип ответа:** dc


```json
{
  "mu": {},
  "eventCache": {},
  "sleepDuration": {},
  "sink": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_broadcaster.go`


**Тип ответа:** deployment.DeploymentController


```json
{
  "rsControl": {},
  "client": {},
  "eventBroadcaster": {},
  "eventRecorder": {},
  "syncHandler": {},
  "enqueueDeployment": {},
  "dLister": {},
  "rsLister": {},
  "podLister": {},
  "podIndexer": {},
  "dListerSynced": {},
  "rsListerSynced": {},
  "podListerSynced": {},
  "queue": {}
}
```


*Определено в:* `pkg/controller/deployment/deployment_controller.go`


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


📍 *Расположение:* `test/integration/deployment/util.go:153`



---


[function] name: scaleDeployment file: test/integration/deployment/util.go:430 returns_error: нет description: —


### scaleDeployment (test/integration/deployment/util.go:430)


scaleDeployment is a method that performs operations based on the provided parameters and returns (newReplicas int32).


```go
func (d *deploymentTester) scaleDeployment((newReplicas int32)) (newReplicas int32)
```


**Тип ответа:** newReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:430`



---


[function] name: testLabels file: test/integration/deployment/util.go:66 returns_error: нет description: —


### testLabels (test/integration/deployment/util.go:66)


testLabels is a function that performs operations based on the provided parameters and returns ().


```go
func testLabels(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:66`



---


[function] name: updateDeployment file: test/integration/deployment/util.go:342 returns_error: да description: —


### updateDeployment (test/integration/deployment/util.go:342)


updateDeployment is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *deploymentTester) updateDeployment((*apps.Deployment, error)) (*apps.Deployment, error)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apps.Deployment`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/deployment/util.go:342`



---


[function] name: updateReplicaSet file: test/integration/deployment/util.go:387 returns_error: да description: —


### updateReplicaSet (test/integration/deployment/util.go:387)


updateReplicaSet is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *deploymentTester) updateReplicaSet((*apps.ReplicaSet, error)) (*apps.ReplicaSet, error)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apps.ReplicaSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/deployment/util.go:387`



---


[function] name: waitForDeploymentComplete file: test/integration/deployment/util.go:272 returns_error: нет description: Waits for the deployment to complete, and don't check if rolling update strategy is broken.
Rolling update strategy is u


### waitForDeploymentComplete (test/integration/deployment/util.go:272)


Waits for the deployment to complete, and don't check if rolling update strategy is broken.
Rolling update strategy is used only during a rolling update, and can be violated in other situations,
such as shortly after a scaling event or the deployment is just created.


```go
func (d *deploymentTester) waitForDeploymentComplete(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:272`



---


[function] name: waitForDeploymentCompleteAndCheckRolling file: test/integration/deployment/util.go:265 returns_error: нет description: Waits for the deployment to complete, and check rolling update strategy isn't broken at any times.
Rolling update strate


### waitForDeploymentCompleteAndCheckRolling (test/integration/deployment/util.go:265)


Waits for the deployment to complete, and check rolling update strategy isn't broken at any times.
Rolling update strategy should not be broken during a rolling update.


```go
func (d *deploymentTester) waitForDeploymentCompleteAndCheckRolling(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:265`



---


[function] name: waitForDeploymentCompleteAndCheckRollingAndMarkPodsReady file: test/integration/deployment/util.go:279 returns_error: нет description: waitForDeploymentCompleteAndCheckRollingAndMarkPodsReady waits for the Deployment to complete
while marking updated Depl


### waitForDeploymentCompleteAndCheckRollingAndMarkPodsReady (test/integration/deployment/util.go:279)


waitForDeploymentCompleteAndCheckRollingAndMarkPodsReady waits for the Deployment to complete
while marking updated Deployment pods as ready at the same time.
Uses hard check to make sure rolling update strategy is not violated at any times.


```go
func (d *deploymentTester) waitForDeploymentCompleteAndCheckRollingAndMarkPodsReady(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:279`



---


[function] name: waitForDeploymentCompleteAndMarkPodsReady file: test/integration/deployment/util.go:299 returns_error: нет description: waitForDeploymentCompleteAndMarkPodsReady waits for the Deployment to complete
while marking updated Deployment pods as 


### waitForDeploymentCompleteAndMarkPodsReady (test/integration/deployment/util.go:299)


waitForDeploymentCompleteAndMarkPodsReady waits for the Deployment to complete
while marking updated Deployment pods as ready at the same time.


```go
func (d *deploymentTester) waitForDeploymentCompleteAndMarkPodsReady(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:299`



---


[function] name: waitForDeploymentCompleteAndMarkPodsReadyAndRemoveTerminated file: test/integration/deployment/util.go:320 returns_error: нет description: waitForDeploymentCompleteAndMarkPodsReadyAndRemoveTerminating waits for the Deployment to complete
while marking updated


### waitForDeploymentCompleteAndMarkPodsReadyAndRemoveTerminated (test/integration/deployment/util.go:320)


waitForDeploymentCompleteAndMarkPodsReadyAndRemoveTerminating waits for the Deployment to complete
while marking updated Deployment pods as ready and removes terminated pods at the same time.


```go
func (d *deploymentTester) waitForDeploymentCompleteAndMarkPodsReadyAndRemoveTerminated((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/integration/deployment/util.go:320`



---


[function] name: waitForDeploymentRevisionAndImage file: test/integration/deployment/util.go:175 returns_error: нет description: —


### waitForDeploymentRevisionAndImage (test/integration/deployment/util.go:175)


waitForDeploymentRevisionAndImage is a method that performs operations based on the provided parameters and returns (revision, image string).


```go
func (d *deploymentTester) waitForDeploymentRevisionAndImage((revision, image string)) (revision, image string)
```


**Тип ответа:** revision


```json
{
  "setUID": {},
  "setGeneration": 0,
  "revisionResourceVersion": "string"
}
```


*Определено в:* `pkg/controller/statefulset/stateful_set_control.go`


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `test/integration/deployment/util.go:175`



---


[function] name: waitForDeploymentStatusReplicasFields file: test/integration/deployment/util.go:492 returns_error: нет description: waitForReadyReplicas waits for number of ready replicas to equal number of replicas.


### waitForDeploymentStatusReplicasFields (test/integration/deployment/util.go:492)


waitForReadyReplicas waits for number of ready replicas to equal number of replicas.


```go
func (d *deploymentTester) waitForDeploymentStatusReplicasFields((ctx context.Context, replicas, updatedReplicas, readyReplicas, availableReplicas, unavailableReplicas int32, terminatingReplicas *int32)) (ctx context.Context, replicas, updatedReplicas, readyReplicas, availableReplicas, unavailableReplicas int32, terminatingReplicas *int32)
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


**Тип ответа:** replicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updatedReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** readyReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** availableReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** unavailableReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** terminatingReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:492`



---


[function] name: waitForDeploymentUpdatedReplicasGTE file: test/integration/deployment/util.go:391 returns_error: нет description: —


### waitForDeploymentUpdatedReplicasGTE (test/integration/deployment/util.go:391)


waitForDeploymentUpdatedReplicasGTE is a method that performs operations based on the provided parameters and returns (minUpdatedReplicas int32).


```go
func (d *deploymentTester) waitForDeploymentUpdatedReplicasGTE((minUpdatedReplicas int32)) (minUpdatedReplicas int32)
```


**Тип ответа:** minUpdatedReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:391`



---


[function] name: waitForDeploymentWithCondition file: test/integration/deployment/util.go:395 returns_error: нет description: —


### waitForDeploymentWithCondition (test/integration/deployment/util.go:395)


waitForDeploymentWithCondition is a method that performs operations based on the provided parameters and returns (reason string, condType apps.DeploymentConditionType).


```go
func (d *deploymentTester) waitForDeploymentWithCondition((reason string, condType apps.DeploymentConditionType)) (reason string, condType apps.DeploymentConditionType)
```


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** condType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.DeploymentConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:395`



---


[function] name: waitForObservedDeployment file: test/integration/deployment/util.go:346 returns_error: нет description: —


### waitForObservedDeployment (test/integration/deployment/util.go:346)


waitForObservedDeployment is a method that performs operations based on the provided parameters and returns (desiredGeneration int64).


```go
func (d *deploymentTester) waitForObservedDeployment((desiredGeneration int64)) (desiredGeneration int64)
```


**Тип ответа:** desiredGeneration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/deployment/util.go:346`



---


[function] name: waitForReadyReplicas file: test/integration/deployment/util.go:454 returns_error: нет description: waitForReadyReplicas waits for number of ready replicas to equal number of replicas.


### waitForReadyReplicas (test/integration/deployment/util.go:454)


waitForReadyReplicas waits for number of ready replicas to equal number of replicas.


```go
func (d *deploymentTester) waitForReadyReplicas(()) ()
```


📍 *Расположение:* `test/integration/deployment/util.go:454`



---


[function] name: waitRSStable file: test/integration/deployment/util.go:426 returns_error: нет description: —


### waitRSStable (test/integration/deployment/util.go:426)


waitRSStable is a method that performs operations based on the provided parameters and returns (replicaset *apps.ReplicaSet).


```go
func (d *deploymentTester) waitRSStable((replicaset *apps.ReplicaSet)) (replicaset *apps.ReplicaSet)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** replicaset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


📍 *Расположение:* `test/integration/deployment/util.go:426`




## test/integration/dra/objects.go


📄 Исходный файл: `test/integration/dra/objects.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [NewMaxResourceSlices](#newmaxresourceslices-testintegrationdraobjectsgo34) `:34`

- 🔗 [commonResourceSlice](#commonresourceslice-testintegrationdraobjectsgo124) `:124`

- 🔗 [maxDNSLabel](#maxdnslabel-testintegrationdraobjectsgo176) `:176`

- 🔗 [maxKeyValueMap](#maxkeyvaluemap-testintegrationdraobjectsgo147) `:147`

- 🔗 [maxLabelName](#maxlabelname-testintegrationdraobjectsgo155) `:155`

- 🔗 [maxLabelValue](#maxlabelvalue-testintegrationdraobjectsgo168) `:168`

- 🔗 [maxQualifiedName](#maxqualifiedname-testintegrationdraobjectsgo164) `:164`

- 🔗 [maxResourceQualifiedName](#maxresourcequalifiedname-testintegrationdraobjectsgo160) `:160`

- 🔗 [maxString](#maxstring-testintegrationdraobjectsgo180) `:180`

- 🔗 [maxSubDomain](#maxsubdomain-testintegrationdraobjectsgo172) `:172`

- 🔗 [newBasicResourceSlice](#newbasicresourceslice-testintegrationdraobjectsgo78) `:78`

- 🔗 [newResourceSliceWithTaintsAndConsumesCounters](#newresourceslicewithtaintsandconsumescounters-testintegrationdraobjectsgo43) `:43`

- 🔗 [newSharedCountersResourceSlice](#newsharedcountersresourceslice-testintegrationdraobjectsgo102) `:102`


</details>


[function] name: NewMaxResourceSlices file: test/integration/dra/objects.go:34 returns_error: нет description: NewMaxResourceSlices creates slices that are as large as possible given the current validation constraints.


### NewMaxResourceSlices (test/integration/dra/objects.go:34)


NewMaxResourceSlices creates slices that are as large as possible given the current validation constraints.


```go
func NewMaxResourceSlices(()) ()
```


📍 *Расположение:* `test/integration/dra/objects.go:34`



---


[function] name: commonResourceSlice file: test/integration/dra/objects.go:124 returns_error: нет description: —


### commonResourceSlice (test/integration/dra/objects.go:124)


commonResourceSlice is a function that performs operations based on the provided parameters and returns ().


```go
func commonResourceSlice(()) ()
```


📍 *Расположение:* `test/integration/dra/objects.go:124`



---


[function] name: maxDNSLabel file: test/integration/dra/objects.go:176 returns_error: нет description: —


### maxDNSLabel (test/integration/dra/objects.go:176)


maxDNSLabel is a function that performs operations based on the provided parameters and returns (i int).


```go
func maxDNSLabel((i int)) (i int)
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


📍 *Расположение:* `test/integration/dra/objects.go:176`



---


[function] name: maxKeyValueMap file: test/integration/dra/objects.go:147 returns_error: нет description: maxKeyValueMap produces a map for labels or annotations.


### maxKeyValueMap (test/integration/dra/objects.go:147)


maxKeyValueMap produces a map for labels or annotations.


```go
func maxKeyValueMap((n int)) (n int)
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


📍 *Расположение:* `test/integration/dra/objects.go:147`



---


[function] name: maxLabelName file: test/integration/dra/objects.go:155 returns_error: нет description: —


### maxLabelName (test/integration/dra/objects.go:155)


maxLabelName is a function that performs operations based on the provided parameters and returns (i int).


```go
func maxLabelName((i int)) (i int)
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


📍 *Расположение:* `test/integration/dra/objects.go:155`



---


[function] name: maxLabelValue file: test/integration/dra/objects.go:168 returns_error: нет description: —


### maxLabelValue (test/integration/dra/objects.go:168)


maxLabelValue is a function that performs operations based on the provided parameters and returns (i int).


```go
func maxLabelValue((i int)) (i int)
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


📍 *Расположение:* `test/integration/dra/objects.go:168`



---


[function] name: maxQualifiedName file: test/integration/dra/objects.go:164 returns_error: нет description: —


### maxQualifiedName (test/integration/dra/objects.go:164)


maxQualifiedName is a function that performs operations based on the provided parameters and returns (i int).


```go
func maxQualifiedName((i int)) (i int)
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


📍 *Расположение:* `test/integration/dra/objects.go:164`



---


[function] name: maxResourceQualifiedName file: test/integration/dra/objects.go:160 returns_error: нет description: —


### maxResourceQualifiedName (test/integration/dra/objects.go:160)


maxResourceQualifiedName is a function that performs operations based on the provided parameters and returns (i int).


```go
func maxResourceQualifiedName((i int)) (i int)
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


📍 *Расположение:* `test/integration/dra/objects.go:160`



---


[function] name: maxString file: test/integration/dra/objects.go:180 returns_error: нет description: —


### maxString (test/integration/dra/objects.go:180)


maxString is a function that performs operations based on the provided parameters and returns (i, l int).


```go
func maxString((i, l int)) (i, l int)
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


📍 *Расположение:* `test/integration/dra/objects.go:180`



---


[function] name: maxSubDomain file: test/integration/dra/objects.go:172 returns_error: нет description: —


### maxSubDomain (test/integration/dra/objects.go:172)


maxSubDomain is a function that performs operations based on the provided parameters and returns (i int).


```go
func maxSubDomain((i int)) (i int)
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


📍 *Расположение:* `test/integration/dra/objects.go:172`



---


[function] name: newBasicResourceSlice file: test/integration/dra/objects.go:78 returns_error: нет description: —


### newBasicResourceSlice (test/integration/dra/objects.go:78)


newBasicResourceSlice is a function that performs operations based on the provided parameters and returns (numDevices int).


```go
func newBasicResourceSlice((numDevices int)) (numDevices int)
```


**Тип ответа:** numDevices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/dra/objects.go:78`



---


[function] name: newResourceSliceWithTaintsAndConsumesCounters file: test/integration/dra/objects.go:43 returns_error: нет description: —


### newResourceSliceWithTaintsAndConsumesCounters (test/integration/dra/objects.go:43)


newResourceSliceWithTaintsAndConsumesCounters is a function that performs operations based on the provided parameters and returns ().


```go
func newResourceSliceWithTaintsAndConsumesCounters(()) ()
```


📍 *Расположение:* `test/integration/dra/objects.go:43`



---


[function] name: newSharedCountersResourceSlice file: test/integration/dra/objects.go:102 returns_error: нет description: —


### newSharedCountersResourceSlice (test/integration/dra/objects.go:102)


newSharedCountersResourceSlice is a function that performs operations based on the provided parameters and returns ().


```go
func newSharedCountersResourceSlice(()) ()
```


📍 *Расположение:* `test/integration/dra/objects.go:102`




## test/integration/dra/resourceslicecontroller.go


📄 Исходный файл: `test/integration/dra/resourceslicecontroller.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TestCreateResourceSlices](#testcreateresourceslices-testintegrationdraresourceslicecontrollergo35) `:35`


</details>


[function] name: TestCreateResourceSlices file: test/integration/dra/resourceslicecontroller.go:35 returns_error: нет description: TestCreateResourceSlices uses the ResourceSlice controller to create slices.
It runs both as integration and as E2E test


### TestCreateResourceSlices (test/integration/dra/resourceslicecontroller.go:35)


TestCreateResourceSlices uses the ResourceSlice controller to create slices.
It runs both as integration and as E2E test, with different number of slices.


```go
func TestCreateResourceSlices((tCtx ktesting.TContext, numSlices int)) (tCtx ktesting.TContext, numSlices int)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** numSlices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/dra/resourceslicecontroller.go:35`




## test/integration/etcd/data.go


📄 Исходный файл: `test/integration/etcd/data.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [GetCustomResourceDefinitionData](#getcustomresourcedefinitiondata-testintegrationetcddatago854) `:854`

- 🔗 [GetEtcdStorageData](#getetcdstoragedata-testintegrationetcddatago50) `:50`

- 🔗 [GetEtcdStorageDataForNamespace](#getetcdstoragedatafornamespace-testintegrationetcddatago65) `:65`

- 🔗 [GetEtcdStorageDataForNamespaceServedAt](#getetcdstoragedatafornamespaceservedat-testintegrationetcddatago73) `:73`

- 🔗 [GetEtcdStorageDataServedAt](#getetcdstoragedataservedat-testintegrationetcddatago57) `:57`

- 🔗 [GetSupportedEmulatedVersions](#getsupportedemulatedversions-testintegrationetcddatago38) `:38`

- 🔗 [gvk](#gvk-testintegrationetcddatago999) `:999`

- 🔗 [gvkP](#gvkp-testintegrationetcddatago995) `:995`

- 🔗 [gvr](#gvr-testintegrationetcddatago991) `:991`

- 🔗 [storageVersionAtEmulationVersion](#storageversionatemulationversion-testintegrationetcddatago799) `:799`

- 🔗 [validateStorageData](#validatestoragedata-testintegrationetcddatago776) `:776`


</details>


[function] name: GetCustomResourceDefinitionData file: test/integration/etcd/data.go:854 returns_error: нет description: GetCustomResourceDefinitionData returns the resource definitions that back the custom resources
included in GetEtcdStora


### GetCustomResourceDefinitionData (test/integration/etcd/data.go:854)


GetCustomResourceDefinitionData returns the resource definitions that back the custom resources
included in GetEtcdStorageData.  They should be created using CreateTestCRDs before running any tests.
We can switch this to v1 CRDs based on transitive call site analysis.
Call sites:
1. TestDedupOwnerReferences - beta doesn't matter
2. TestWebhookAdmissionWithWatchCache/TestWebhookAdmissionWithoutWatchCache - beta doesn't matter
3. TestApplyStatus - the version fields don't matter.  Pruning isn't checked, just ownership.
4. TestDryRun - versions and pruning don't matter
5. TestStorageVersionBootstrap - versions and pruning don't matter.
6. TestEtcdStoragePath - beta doesn't matter
7. TestCrossGroupStorage - beta doesn't matter
8. TestOverlappingCustomResourceCustomResourceDefinition - beta doesn't matter
9. TestOverlappingCustomResourceAPIService - beta doesn't matter


```go
func GetCustomResourceDefinitionData(()) ()
```


📍 *Расположение:* `test/integration/etcd/data.go:854`



---


[function] name: GetEtcdStorageData file: test/integration/etcd/data.go:50 returns_error: нет description: GetEtcdStorageData returns etcd data for all persisted objects at the latest release version.
It is exported so that it 


### GetEtcdStorageData (test/integration/etcd/data.go:50)


GetEtcdStorageData returns etcd data for all persisted objects at the latest release version.
It is exported so that it can be reused across multiple tests.
It returns a new map on every invocation to prevent different tests from mutating shared state.


```go
func GetEtcdStorageData(()) ()
```


📍 *Расположение:* `test/integration/etcd/data.go:50`



---


[function] name: GetEtcdStorageDataForNamespace file: test/integration/etcd/data.go:65 returns_error: нет description: GetEtcdStorageDataForNamespace returns etcd data for all persisted objects at the latest release version.
It is exported


### GetEtcdStorageDataForNamespace (test/integration/etcd/data.go:65)


GetEtcdStorageDataForNamespace returns etcd data for all persisted objects at the latest release version.
It is exported so that it can be reused across multiple tests.
It returns a new map on every invocation to prevent different tests from mutating shared state.
Namespaced objects keys are computed for the specified namespace.


```go
func GetEtcdStorageDataForNamespace((namespace string)) (namespace string)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


📍 *Расположение:* `test/integration/etcd/data.go:65`



---


[function] name: GetEtcdStorageDataForNamespaceServedAt file: test/integration/etcd/data.go:73 returns_error: нет description: GetEtcdStorageDataForNamespaceServedAt returns etcd data for all persisted objects at a particular release version.
It i


### GetEtcdStorageDataForNamespaceServedAt (test/integration/etcd/data.go:73)


GetEtcdStorageDataForNamespaceServedAt returns etcd data for all persisted objects at a particular release version.
It is exported so that it can be reused across multiple tests.
It returns a new map on every invocation to prevent different tests from mutating shared state.
Namespaced objects keys are computed for the specified namespace.


```go
func GetEtcdStorageDataForNamespaceServedAt((namespace string, v string, isEmulation bool)) (namespace string, v string, isEmulation bool)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


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


**Тип ответа:** isEmulation


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/etcd/data.go:73`



---


[function] name: GetEtcdStorageDataServedAt file: test/integration/etcd/data.go:57 returns_error: нет description: GetEtcdStorageDataServedAt returns etcd data for all persisted objects at a particular release version.
It is exported s


### GetEtcdStorageDataServedAt (test/integration/etcd/data.go:57)


GetEtcdStorageDataServedAt returns etcd data for all persisted objects at a particular release version.
It is exported so that it can be reused across multiple tests.
It returns a new map on every invocation to prevent different tests from mutating shared state.


```go
func GetEtcdStorageDataServedAt((version string, isEmulation bool)) (version string, isEmulation bool)
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


**Тип ответа:** isEmulation


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/etcd/data.go:57`



---


[function] name: GetSupportedEmulatedVersions file: test/integration/etcd/data.go:38 returns_error: нет description: GetSupportedEmulatedVersions provides the list of supported emulated versions in the etcd data.
Tests aiming for full co


### GetSupportedEmulatedVersions (test/integration/etcd/data.go:38)


GetSupportedEmulatedVersions provides the list of supported emulated versions in the etcd data.
Tests aiming for full coverage of versions should test fixtures of all supported versions.


```go
func GetSupportedEmulatedVersions(()) ()
```


📍 *Расположение:* `test/integration/etcd/data.go:38`



---


[function] name: gvk file: test/integration/etcd/data.go:999 returns_error: нет description: —


### gvk (test/integration/etcd/data.go:999)


gvk is a function that performs operations based on the provided parameters and returns (g, v, k string).


```go
func gvk((g, v, k string)) (g, v, k string)
```


**Тип ответа:** g


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


**Тип ответа:** k


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


📍 *Расположение:* `test/integration/etcd/data.go:999`



---


[function] name: gvkP file: test/integration/etcd/data.go:995 returns_error: нет description: —


### gvkP (test/integration/etcd/data.go:995)


gvkP is a function that performs operations based on the provided parameters and returns (g, v, k string).


```go
func gvkP((g, v, k string)) (g, v, k string)
```


**Тип ответа:** g


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


**Тип ответа:** k


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


📍 *Расположение:* `test/integration/etcd/data.go:995`



---


[function] name: gvr file: test/integration/etcd/data.go:991 returns_error: нет description: —


### gvr (test/integration/etcd/data.go:991)


gvr is a function that performs operations based on the provided parameters and returns (g, v, r string).


```go
func gvr((g, v, r string)) (g, v, r string)
```


**Тип ответа:** g


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


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


📍 *Расположение:* `test/integration/etcd/data.go:991`



---


[function] name: storageVersionAtEmulationVersion file: test/integration/etcd/data.go:799 returns_error: нет description: storageVersionAtEmulationVersion tries to find the correct storage version at an emulation version.
If a GVK is introduc


### storageVersionAtEmulationVersion (test/integration/etcd/data.go:799)


storageVersionAtEmulationVersion tries to find the correct storage version at an emulation version.
If a GVK is introduced after the min compatibility version, we need to use an earlier version in storage.


```go
func storageVersionAtEmulationVersion((key schema.GroupVersionResource, expectedGVK *schema.GroupVersionKind, emuVer string, etcdStorageData map[schema.GroupVersionResource]StorageData)) (key schema.GroupVersionResource, expectedGVK *schema.GroupVersionKind, emuVer string, etcdStorageData map[schema.GroupVersionResource]StorageData)
```


**Тип запроса:** schema.GroupVersionKind


```json
{
  "Group": "string",
  "Version": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** expectedGVK


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** schema.GroupVersionKind


```json
{
  "Group": "string",
  "Version": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** emuVer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** etcdStorageData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** StorageData


```json
{
  "Stub": "string",
  "Prerequisites": [],
  "ExpectedEtcdPath": "string",
  "ExpectedGVK": null,
  "IntroducedVersion": "string",
  "RemovedVersion": "string"
}
```


*Определено в:* `test/integration/etcd/data.go`


📍 *Расположение:* `test/integration/etcd/data.go:799`



---


[function] name: validateStorageData file: test/integration/etcd/data.go:776 returns_error: нет description: —


### validateStorageData (test/integration/etcd/data.go:776)


validateStorageData is a function that performs operations based on the provided parameters and returns (etcdStorageData map[schema.GroupVersionResource]StorageData).


```go
func validateStorageData((etcdStorageData map[schema.GroupVersionResource]StorageData)) (etcdStorageData map[schema.GroupVersionResource]StorageData)
```


**Тип ответа:** etcdStorageData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** schema.GroupVersionResource


```json
{
  "Group": "string",
  "Version": "string",
  "Resource": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** StorageData


```json
{
  "Stub": "string",
  "Prerequisites": [],
  "ExpectedEtcdPath": "string",
  "ExpectedGVK": null,
  "IntroducedVersion": "string",
  "RemovedVersion": "string"
}
```


*Определено в:* `test/integration/etcd/data.go`


📍 *Расположение:* `test/integration/etcd/data.go:776`




## test/integration/etcd/server.go


📄 Исходный файл: `test/integration/etcd/server.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [CrdExistsInDiscovery](#crdexistsindiscovery-testintegrationetcdservergo425) `:425`

- 🔗 [CreateTestCRDs](#createtestcrds-testintegrationetcdservergo383) `:383`

- 🔗 [GetResources](#getresources-testintegrationetcdservergo299) `:299`

- 🔗 [JSONToUnstructured](#jsontounstructured-testintegrationetcdservergo363) `:363`

- 🔗 [StartRealAPIServerOrDie](#startrealapiserverordie-testintegrationetcdservergo71) `:71`

- 🔗 [crdVersionExistsInDiscovery](#crdversionexistsindiscovery-testintegrationetcdservergo440) `:440`

- 🔗 [createTestCRD](#createtestcrd-testintegrationetcdservergo389) `:389`

- 🔗 [scope](#scope-testintegrationetcdservergo354) `:354`

- 🔗 [waitForEstablishedCRD](#waitforestablishedcrd-testintegrationetcdservergo406) `:406`


</details>


[function] name: CrdExistsInDiscovery file: test/integration/etcd/server.go:425 returns_error: нет description: CrdExistsInDiscovery checks to see if the given CRD exists in discovery at all served versions.


### CrdExistsInDiscovery (test/integration/etcd/server.go:425)


CrdExistsInDiscovery checks to see if the given CRD exists in discovery at all served versions.


```go
func CrdExistsInDiscovery((client apiextensionsclientset.Interface, crd *apiextensionsv1.CustomResourceDefinition)) (client apiextensionsclientset.Interface, crd *apiextensionsv1.CustomResourceDefinition)
```


**Тип запроса:** apiextensionsv1.CustomResourceDefinition


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


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


**Тип ответа:** apiextensionsclientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/etcd/server.go:425`



---


[function] name: CreateTestCRDs file: test/integration/etcd/server.go:383 returns_error: нет description: CreateTestCRDs creates the given CRDs, any failure causes the test to Fatal.
If skipCrdExistsInDiscovery is true, the CR


### CreateTestCRDs (test/integration/etcd/server.go:383)


CreateTestCRDs creates the given CRDs, any failure causes the test to Fatal.
If skipCrdExistsInDiscovery is true, the CRDs are only checked for the Established condition via their Status.
If skipCrdExistsInDiscovery is false, the CRDs are checked via discovery, see CrdExistsInDiscovery.


```go
func CreateTestCRDs((t *testing.T, client apiextensionsclientset.Interface, skipCrdExistsInDiscovery bool, crds ...*apiextensionsv1.CustomResourceDefinition)) (t *testing.T, client apiextensionsclientset.Interface, skipCrdExistsInDiscovery bool, crds ...*apiextensionsv1.CustomResourceDefinition)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** apiextensionsv1.CustomResourceDefinition


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


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


**Тип ответа:** apiextensionsclientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** skipCrdExistsInDiscovery


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** crds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiextensionsv1.CustomResourceDefinition


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


📍 *Расположение:* `test/integration/etcd/server.go:383`



---


[function] name: GetResources file: test/integration/etcd/server.go:299 returns_error: нет description: GetResources fetches the Resources associated with serverResources that support get and create


### GetResources (test/integration/etcd/server.go:299)


GetResources fetches the Resources associated with serverResources that support get and create


```go
func GetResources((t *testing.T, serverResources []*metav1.APIResourceList)) (t *testing.T, serverResources []*metav1.APIResourceList)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** metav1.APIResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


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


**Тип ответа:** serverResources


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.APIResourceList


```json
{
  "groupVersion": "string",
  "resources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `test/integration/etcd/server.go:299`



---


[function] name: JSONToUnstructured file: test/integration/etcd/server.go:363 returns_error: да description: JSONToUnstructured converts a JSON stub to unstructured.Unstructured and
returns a dynamic resource client that can be u


### JSONToUnstructured (test/integration/etcd/server.go:363)


JSONToUnstructured converts a JSON stub to unstructured.Unstructured and
returns a dynamic resource client that can be used to interact with it


```go
func JSONToUnstructured((dynamic.ResourceInterface, *unstructured.Unstructured, error)) (dynamic.ResourceInterface, *unstructured.Unstructured, error)
```


**Тип запроса:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Тип ответа:** dynamic.ResourceInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `dynamic.ResourceInterface`, `*unstructured.Unstructured`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/etcd/server.go:363`



---


[function] name: StartRealAPIServerOrDie file: test/integration/etcd/server.go:71 returns_error: нет description: StartRealAPIServerOrDie starts an API server that is appropriate for use in tests that require one of every resource


### StartRealAPIServerOrDie (test/integration/etcd/server.go:71)


StartRealAPIServerOrDie starts an API server that is appropriate for use in tests that require one of every resource


```go
func StartRealAPIServerOrDie((t *testing.T, configFuncs ...func(*options.ServerRunOptions))) (t *testing.T, configFuncs ...func(*options.ServerRunOptions))
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** options.ServerRunOptions


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


**Тип ответа:** configFuncs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options.ServerRunOptions


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


📍 *Расположение:* `test/integration/etcd/server.go:71`



---


[function] name: crdVersionExistsInDiscovery file: test/integration/etcd/server.go:440 returns_error: нет description: —


### crdVersionExistsInDiscovery (test/integration/etcd/server.go:440)


crdVersionExistsInDiscovery is a function that performs operations based on the provided parameters and returns (client apiextensionsclientset.Interface, crd *apiextensionsv1.CustomResourceDefinition, version string).


```go
func crdVersionExistsInDiscovery((client apiextensionsclientset.Interface, crd *apiextensionsv1.CustomResourceDefinition, version string)) (client apiextensionsclientset.Interface, crd *apiextensionsv1.CustomResourceDefinition, version string)
```


**Тип запроса:** apiextensionsv1.CustomResourceDefinition


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


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


**Тип ответа:** apiextensionsclientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


📍 *Расположение:* `test/integration/etcd/server.go:440`



---


[function] name: createTestCRD file: test/integration/etcd/server.go:389 returns_error: нет description: —


### createTestCRD (test/integration/etcd/server.go:389)


createTestCRD is a function that performs operations based on the provided parameters and returns (t *testing.T, client apiextensionsclientset.Interface, skipCrdExistsInDiscovery bool, crd *apiextensionsv1.CustomResourceDefinition).


```go
func createTestCRD((t *testing.T, client apiextensionsclientset.Interface, skipCrdExistsInDiscovery bool, crd *apiextensionsv1.CustomResourceDefinition)) (t *testing.T, client apiextensionsclientset.Interface, skipCrdExistsInDiscovery bool, crd *apiextensionsv1.CustomResourceDefinition)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** apiextensionsv1.CustomResourceDefinition


```json
{
  "spec": {},
  "status": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


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


**Тип ответа:** apiextensionsclientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** skipCrdExistsInDiscovery


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/integration/etcd/server.go:389`



---


[function] name: scope file: test/integration/etcd/server.go:354 returns_error: нет description: —


### scope (test/integration/etcd/server.go:354)


scope is a function that performs operations based on the provided parameters and returns (namespaced bool).


```go
func scope((namespaced bool)) (namespaced bool)
```


**Тип ответа:** namespaced


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


📍 *Расположение:* `test/integration/etcd/server.go:354`



---


[function] name: waitForEstablishedCRD file: test/integration/etcd/server.go:406 returns_error: нет description: —


### waitForEstablishedCRD (test/integration/etcd/server.go:406)


waitForEstablishedCRD is a function that performs operations based on the provided parameters and returns (client apiextensionsclientset.Interface, name string).


```go
func waitForEstablishedCRD((client apiextensionsclientset.Interface, name string)) (client apiextensionsclientset.Interface, name string)
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


**Тип ответа:** apiextensionsclientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/integration/etcd/server.go:406`




## test/integration/framework/cbor.go


📄 Исходный файл: `test/integration/framework/cbor.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [AssertRequestResponseAsCBOR](#assertrequestresponseascbor-testintegrationframeworkcborgo32) `:32`

- 🔗 [RoundTrip](#roundtrip-testintegrationframeworkcborgo86) `:86`


</details>


[function] name: AssertRequestResponseAsCBOR file: test/integration/framework/cbor.go:32 returns_error: нет description: AssertRequestResponseAsCBOR returns a transport.WrapperFunc that will report a test error if a
non-empty request or resp


### AssertRequestResponseAsCBOR (test/integration/framework/cbor.go:32)


AssertRequestResponseAsCBOR returns a transport.WrapperFunc that will report a test error if a
non-empty request or response body contains data that does not appear to be CBOR-encoded.


```go
func AssertRequestResponseAsCBOR((t testing.TB)) (t testing.TB)
```


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


📍 *Расположение:* `test/integration/framework/cbor.go:32`



---


[function] name: RoundTrip file: test/integration/framework/cbor.go:86 returns_error: да description: —


### RoundTrip (test/integration/framework/cbor.go:86)


RoundTrip is a method that performs operations based on the provided parameters and may return an error.


```go
func (f roundTripperFunc) RoundTrip((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Тип ответа:** http.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/framework/cbor.go:86`




## test/integration/framework/controlplane_utils.go


📄 Исходный файл: `test/integration/framework/controlplane_utils.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [DefaultEtcdOptions](#defaultetcdoptions-testintegrationframeworkcontrolplane_utilsgo79) `:79`

- 🔗 [DefaultOpenAPIConfig](#defaultopenapiconfig-testintegrationframeworkcontrolplane_utilsgo41) `:41`

- 🔗 [DefaultOpenAPIV3Config](#defaultopenapiv3config-testintegrationframeworkcontrolplane_utilsgo60) `:60`

- 🔗 [DefaultTestServerFlags](#defaulttestserverflags-testintegrationframeworkcontrolplane_utilsgo102) `:102`

- 🔗 [SharedEtcd](#sharedetcd-testintegrationframeworkcontrolplane_utilsgo95) `:95`


</details>


[function] name: DefaultEtcdOptions file: test/integration/framework/controlplane_utils.go:79 returns_error: нет description: DefaultEtcdOptions are the default EtcdOptions for use with integration tests.


### DefaultEtcdOptions (test/integration/framework/controlplane_utils.go:79)


DefaultEtcdOptions are the default EtcdOptions for use with integration tests.


```go
func DefaultEtcdOptions(()) ()
```


📍 *Расположение:* `test/integration/framework/controlplane_utils.go:79`



---


[function] name: DefaultOpenAPIConfig file: test/integration/framework/controlplane_utils.go:41 returns_error: нет description: DefaultOpenAPIConfig returns an openapicommon.Config initialized to default values.


### DefaultOpenAPIConfig (test/integration/framework/controlplane_utils.go:41)


DefaultOpenAPIConfig returns an openapicommon.Config initialized to default values.


```go
func DefaultOpenAPIConfig(()) ()
```


📍 *Расположение:* `test/integration/framework/controlplane_utils.go:41`



---


[function] name: DefaultOpenAPIV3Config file: test/integration/framework/controlplane_utils.go:60 returns_error: нет description: DefaultOpenAPIV3Config returns an openapicommon.Config initialized to default values.


### DefaultOpenAPIV3Config (test/integration/framework/controlplane_utils.go:60)


DefaultOpenAPIV3Config returns an openapicommon.Config initialized to default values.


```go
func DefaultOpenAPIV3Config(()) ()
```


📍 *Расположение:* `test/integration/framework/controlplane_utils.go:60`



---


[function] name: DefaultTestServerFlags file: test/integration/framework/controlplane_utils.go:102 returns_error: нет description: DefaultAPIServerFlags returns the default flags used to run kube-apiserver on tests


### DefaultTestServerFlags (test/integration/framework/controlplane_utils.go:102)


DefaultAPIServerFlags returns the default flags used to run kube-apiserver on tests


```go
func DefaultTestServerFlags(()) ()
```


📍 *Расположение:* `test/integration/framework/controlplane_utils.go:102`



---


[function] name: SharedEtcd file: test/integration/framework/controlplane_utils.go:95 returns_error: нет description: SharedEtcd creates a storage config for a shared etcd instance, with a unique prefix.

The transport CertFile/KeyFile/Tr


### SharedEtcd (test/integration/framework/controlplane_utils.go:95)


SharedEtcd creates a storage config for a shared etcd instance, with a unique prefix.

The transport CertFile/KeyFile/TrustedCAFile will be empty for insecure connections.
In that case, *no* TLS config should be used because etcd would try to use
it for Unix Domain sockets (https://github.com/etcd-io/etcd/blob/5a8fba466087686fc15815f5bc041fb7eb1f23ea/client/v3/internal/endpoint/endpoint.go#L61-L66)
and fail to connect because the TLS config is insufficient. It works
for TCP because http disables using TLS.


```go
func SharedEtcd(()) ()
```


📍 *Расположение:* `test/integration/framework/controlplane_utils.go:95`




## test/integration/framework/etcd.go


📄 Исходный файл: `test/integration/framework/etcd.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [EtcdMain](#etcdmain-testintegrationframeworketcdgo255) `:255`

- 🔗 [GetEtcdURL](#getetcdurl-testintegrationframeworketcdgo301) `:301`

- 🔗 [RunCustomEtcd](#runcustometcd-testintegrationframeworketcdgo101) `:101`

- 🔗 [StartEtcd](#startetcd-testintegrationframeworketcdgo315) `:315`

- 🔗 [getEtcdPath](#getetcdpath-testintegrationframeworketcdgo55) `:55`

- 🔗 [init](#init-testintegrationframeworketcdgo83) `:83`

- 🔗 [startEtcd](#startetcd-testintegrationframeworketcdgo61) `:61`


</details>


[function] name: EtcdMain file: test/integration/framework/etcd.go:255 returns_error: нет description: EtcdMain starts an etcd instance before running tests.


### EtcdMain (test/integration/framework/etcd.go:255)


EtcdMain starts an etcd instance before running tests.


```go
func EtcdMain((tests func() int)) (tests func() int)
```


**Тип ответа:** tests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/etcd.go:255`



---


[function] name: GetEtcdURL file: test/integration/framework/etcd.go:301 returns_error: нет description: GetEtcdURL returns the URL of the etcd instance started by EtcdMain or StartEtcd.


### GetEtcdURL (test/integration/framework/etcd.go:301)


GetEtcdURL returns the URL of the etcd instance started by EtcdMain or StartEtcd.


```go
func GetEtcdURL(()) ()
```


📍 *Расположение:* `test/integration/framework/etcd.go:301`



---


[function] name: RunCustomEtcd file: test/integration/framework/etcd.go:101 returns_error: да description: RunCustomEtcd starts a custom etcd instance for test purposes.


### RunCustomEtcd (test/integration/framework/etcd.go:101)


RunCustomEtcd starts a custom etcd instance for test purposes.


```go
func RunCustomEtcd((url string, stopFn func(), err error)) (url string, stopFn func(), err error)
```


**Тип ответа:** url


```json
{
  "baseURL": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** stopFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


*Типы возврата:* `url string`, `stopFn func()`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/framework/etcd.go:101`



---


[function] name: StartEtcd file: test/integration/framework/etcd.go:315 returns_error: нет description: StartEtcd starts an etcd instance inside a test. It will abort the test if
startup fails and clean up after the test aut


### StartEtcd (test/integration/framework/etcd.go:315)


StartEtcd starts an etcd instance inside a test. It will abort the test if
startup fails and clean up after the test automatically. Stdout and stderr
of the etcd binary and all log output of the etcd helper code go to the
provided logger.

In contrast to EtcdMain, StartEtcd will not do automatic leak checking.
Tests can decide if and where they want to do that.

Starting etcd multiple times per test run instead of once with EtcdMain
provides better separation between different tests.


```go
func StartEtcd((logger klog.Logger, tb testing.TB, forceCreate bool)) (logger klog.Logger, tb testing.TB, forceCreate bool)
```


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** testing.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** forceCreate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/etcd.go:315`



---


[function] name: getEtcdPath file: test/integration/framework/etcd.go:55 returns_error: да description: getEtcdPath returns a path to an etcd executable.


### getEtcdPath (test/integration/framework/etcd.go:55)


getEtcdPath returns a path to an etcd executable.


```go
func getEtcdPath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/framework/etcd.go:55`



---


[function] name: init file: test/integration/framework/etcd.go:83 returns_error: нет description: —


### init (test/integration/framework/etcd.go:83)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/integration/framework/etcd.go:83`



---


[function] name: startEtcd file: test/integration/framework/etcd.go:61 returns_error: да description: startEtcd executes an etcd instance. The returned function will signal the
etcd process and wait for it to exit.


### startEtcd (test/integration/framework/etcd.go:61)


startEtcd executes an etcd instance. The returned function will signal the
etcd process and wait for it to exit.


```go
func startEtcd((func(), error)) (func(), error)
```


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `func()`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/framework/etcd.go:61`




## test/integration/framework/goleak.go


📄 Исходный файл: `test/integration/framework/goleak.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [GoleakCheck](#goleakcheck-testintegrationframeworkgoleakgo44) `:44`

- 🔗 [IgnoreBackgroundGoroutines](#ignorebackgroundgoroutines-testintegrationframeworkgoleakgo34) `:34`

- 🔗 [goleakFindRetry](#goleakfindretry-testintegrationframeworkgoleakgo55) `:55`


</details>


[function] name: GoleakCheck file: test/integration/framework/goleak.go:44 returns_error: нет description: GoleakCheck sets up leak checking for a test or benchmark.
The check runs as cleanup operation and records an
error when


### GoleakCheck (test/integration/framework/goleak.go:44)


GoleakCheck sets up leak checking for a test or benchmark.
The check runs as cleanup operation and records an
error when goroutines were leaked.


```go
func GoleakCheck((tb testing.TB, opts ...goleak.Option)) (tb testing.TB, opts ...goleak.Option)
```


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** testing.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** goleak.Option


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `test/integration/framework/goleak.go:44`



---


[function] name: IgnoreBackgroundGoroutines file: test/integration/framework/goleak.go:34 returns_error: нет description: IgnoreBackgroundGoroutines returns options for goleak.Find
which ignore goroutines created by "go test" and init functio


### IgnoreBackgroundGoroutines (test/integration/framework/goleak.go:34)


IgnoreBackgroundGoroutines returns options for goleak.Find
which ignore goroutines created by "go test" and init functions,
like the one from go.opencensus.io/stats/view/worker.go.

Goroutines that normally get created later when using the apiserver
get created already when calling this function, therefore they
also get ignored.


```go
func IgnoreBackgroundGoroutines(()) ()
```


📍 *Расположение:* `test/integration/framework/goleak.go:34`



---


[function] name: goleakFindRetry file: test/integration/framework/goleak.go:55 returns_error: нет description: —


### goleakFindRetry (test/integration/framework/goleak.go:55)


goleakFindRetry is a function that performs operations based on the provided parameters and returns (opts ...goleak.Option).


```go
func goleakFindRetry((opts ...goleak.Option)) (opts ...goleak.Option)
```


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** goleak.Option


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `test/integration/framework/goleak.go:55`




## test/integration/framework/logger.go


📄 Исходный файл: `test/integration/framework/logger.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [NewTBWriter](#newtbwriter-testintegrationframeworkloggergo64) `:64`

- 🔗 [RedirectKlog](#redirectklog-testintegrationframeworkloggergo32) `:32`

- 🔗 [Write](#write-testintegrationframeworkloggergo72) `:72`


</details>


[function] name: NewTBWriter file: test/integration/framework/logger.go:64 returns_error: нет description: NewTBWriter creates an io.Writer which turns each write into a tb.Log call.

Note that no attempts are made to determine


### NewTBWriter (test/integration/framework/logger.go:64)


NewTBWriter creates an io.Writer which turns each write into a tb.Log call.

Note that no attempts are made to determine the actual call site because
our caller doesn't know about the TB instance and thus cannot mark itself
as helper. Therefore the code here doesn't do it either and thus shows up
as call site in the testing output. To avoid that, contextual logging
and ktesting have to be used.


```go
func NewTBWriter((tb testing.TB)) (tb testing.TB)
```


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** testing.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/logger.go:64`



---


[function] name: RedirectKlog file: test/integration/framework/logger.go:32 returns_error: нет description: RedirectKlog modifies the global klog logger so that it writes via the given
writer. This only works when different test


### RedirectKlog (test/integration/framework/logger.go:32)


RedirectKlog modifies the global klog logger so that it writes via the given
writer. This only works when different tests run sequentially.

The returned cleanup function restores the previous state. Beware that it is
not thread-safe, all goroutines which call klog must have been stopped.


```go
func RedirectKlog((tb testing.TB, output io.Writer)) (tb testing.TB, output io.Writer)
```


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** testing.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


📍 *Расположение:* `test/integration/framework/logger.go:32`



---


[function] name: Write file: test/integration/framework/logger.go:72 returns_error: да description: —


### Write (test/integration/framework/logger.go:72)


Write is a method that performs operations based on the provided parameters and may return an error.


```go
func (tw testingWriter) Write((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/framework/logger.go:72`




## test/integration/framework/serializer.go


📄 Исходный файл: `test/integration/framework/serializer.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [DecoderToVersion](#decodertoversion-testintegrationframeworkserializergo43) `:43`

- 🔗 [EncoderForVersion](#encoderforversion-testintegrationframeworkserializergo39) `:39`

- 🔗 [SupportedMediaTypes](#supportedmediatypes-testintegrationframeworkserializergo31) `:31`

- 🔗 [UniversalDeserializer](#universaldeserializer-testintegrationframeworkserializergo35) `:35`


</details>


[function] name: DecoderToVersion file: test/integration/framework/serializer.go:43 returns_error: нет description: —


### DecoderToVersion (test/integration/framework/serializer.go:43)


DecoderToVersion is a method that performs operations based on the provided parameters and returns (decoder runtime.Decoder, gv runtime.GroupVersioner).


```go
func (s *wrappedSerializer) DecoderToVersion((decoder runtime.Decoder, gv runtime.GroupVersioner)) (decoder runtime.Decoder, gv runtime.GroupVersioner)
```


**Тип ответа:** decoder


```json
{
  "decoders": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/recognizer/recognizer.go`


**Тип ответа:** runtime.Decoder


```json
{
  "decoder": {},
  "embeddedDecoder": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/rest/watch/decoder.go`


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


**Тип ответа:** runtime.GroupVersioner


```json
{
  "target": {},
  "acceptedGroupKinds": [],
  "coerce": false
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/codec.go`


📍 *Расположение:* `test/integration/framework/serializer.go:43`



---


[function] name: EncoderForVersion file: test/integration/framework/serializer.go:39 returns_error: нет description: —


### EncoderForVersion (test/integration/framework/serializer.go:39)


EncoderForVersion is a method that performs operations based on the provided parameters and returns (encoder runtime.Encoder, gv runtime.GroupVersioner).


```go
func (s *wrappedSerializer) EncoderForVersion((encoder runtime.Encoder, gv runtime.GroupVersioner)) (encoder runtime.Encoder, gv runtime.GroupVersioner)
```


**Тип ответа:** encoder


```json
{
  "writer": {},
  "encoder": {},
  "buf": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/streaming/streaming.go`


**Тип ответа:** runtime.Encoder


```json
{
  "encoder": {},
  "embeddedEncoder": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/rest/watch/encoder.go`


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


**Тип ответа:** runtime.GroupVersioner


```json
{
  "target": {},
  "acceptedGroupKinds": [],
  "coerce": false
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/codec.go`


📍 *Расположение:* `test/integration/framework/serializer.go:39`



---


[function] name: SupportedMediaTypes file: test/integration/framework/serializer.go:31 returns_error: нет description: —


### SupportedMediaTypes (test/integration/framework/serializer.go:31)


SupportedMediaTypes is a method that performs operations based on the provided parameters and returns ().


```go
func (s *wrappedSerializer) SupportedMediaTypes(()) ()
```


📍 *Расположение:* `test/integration/framework/serializer.go:31`



---


[function] name: UniversalDeserializer file: test/integration/framework/serializer.go:35 returns_error: нет description: —


### UniversalDeserializer (test/integration/framework/serializer.go:35)


UniversalDeserializer is a method that performs operations based on the provided parameters and returns ().


```go
func (s *wrappedSerializer) UniversalDeserializer(()) ()
```


📍 *Расположение:* `test/integration/framework/serializer.go:35`




## test/integration/framework/test_server.go


📄 Исходный файл: `test/integration/framework/test_server.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [StartTestServer](#starttestserver-testintegrationframeworktest_servergo75) `:75`


</details>


[function] name: StartTestServer file: test/integration/framework/test_server.go:75 returns_error: нет description: StartTestServer runs a kube-apiserver, optionally calling out to the setup.ModifyServerRunOptions and setup.ModifyServer


### StartTestServer (test/integration/framework/test_server.go:75)


StartTestServer runs a kube-apiserver, optionally calling out to the setup.ModifyServerRunOptions and setup.ModifyServerConfig functions
TODO (pohly): convert to ktesting contexts


```go
func StartTestServer((client.Interface, *rest.Config, TearDownFunc)) (client.Interface, *rest.Config, TearDownFunc)
```


**Тип запроса:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** client.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** TearDownFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/test_server.go:75`




## test/integration/framework/util.go


📄 Исходный файл: `test/integration/framework/util.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [CreateNamespaceOrDie](#createnamespaceordie-testintegrationframeworkutilgo34) `:34`

- 🔗 [DeleteNamespaceOrDie](#deletenamespaceordie-testintegrationframeworkutilgo44) `:44`

- 🔗 [Filter](#filter-testintegrationframeworkutilgo53) `:53`

- 🔗 [IsConditionSetAsExpected](#isconditionsetasexpected-testintegrationframeworkutilgo85) `:85`

- 🔗 [IsConditionSetAsExpectedSilent](#isconditionsetasexpectedsilent-testintegrationframeworkutilgo90) `:90`

- 🔗 [IsNodeReady](#isnodeready-testintegrationframeworkutilgo77) `:77`

- 🔗 [IsNodeSchedulable](#isnodeschedulable-testintegrationframeworkutilgo67) `:67`

- 🔗 [isConditionUnset](#isconditionunset-testintegrationframeworkutilgo95) `:95`

- 🔗 [isNodeConditionSetAsExpected](#isnodeconditionsetasexpected-testintegrationframeworkutilgo105) `:105`


</details>


[function] name: CreateNamespaceOrDie file: test/integration/framework/util.go:34 returns_error: нет description: CreateNamespaceOrDie creates a namespace.


### CreateNamespaceOrDie (test/integration/framework/util.go:34)


CreateNamespaceOrDie creates a namespace.


```go
func CreateNamespaceOrDie((c clientset.Interface, baseName string, t testing.TB)) (c clientset.Interface, baseName string, t testing.TB)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** baseName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/integration/framework/util.go:34`



---


[function] name: DeleteNamespaceOrDie file: test/integration/framework/util.go:44 returns_error: нет description: DeleteNamespaceOrDie deletes a namespace.


### DeleteNamespaceOrDie (test/integration/framework/util.go:44)


DeleteNamespaceOrDie deletes a namespace.


```go
func DeleteNamespaceOrDie((c clientset.Interface, ns *v1.Namespace, t testing.TB)) (c clientset.Interface, ns *v1.Namespace, t testing.TB)
```


**Тип запроса:** v1.Namespace


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** v1.Namespace


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


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


📍 *Расположение:* `test/integration/framework/util.go:44`



---


[function] name: Filter file: test/integration/framework/util.go:53 returns_error: нет description: Filter filters nodes in NodeList in place, removing nodes that do not
satisfy the given condition


### Filter (test/integration/framework/util.go:53)


Filter filters nodes in NodeList in place, removing nodes that do not
satisfy the given condition


```go
func Filter((nodeList *v1.NodeList, fn func(node v1.Node) bool)) (nodeList *v1.NodeList, fn func(node v1.Node) bool)
```


**Тип запроса:** v1.NodeList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** nodeList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.NodeList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/framework/util.go:53`



---


[function] name: IsConditionSetAsExpected file: test/integration/framework/util.go:85 returns_error: нет description: IsConditionSetAsExpected returns a wantTrue value if the node has a match to the conditionType, otherwise returns an opp


### IsConditionSetAsExpected (test/integration/framework/util.go:85)


IsConditionSetAsExpected returns a wantTrue value if the node has a match to the conditionType, otherwise returns an opposite value of the wantTrue with detailed logging.


```go
func IsConditionSetAsExpected((node *v1.Node, conditionType v1.NodeConditionType, wantTrue bool)) (node *v1.Node, conditionType v1.NodeConditionType, wantTrue bool)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** conditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.NodeConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** wantTrue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/util.go:85`



---


[function] name: IsConditionSetAsExpectedSilent file: test/integration/framework/util.go:90 returns_error: нет description: IsConditionSetAsExpectedSilent returns a wantTrue value if the node has a match to the conditionType, otherwise returns 


### IsConditionSetAsExpectedSilent (test/integration/framework/util.go:90)


IsConditionSetAsExpectedSilent returns a wantTrue value if the node has a match to the conditionType, otherwise returns an opposite value of the wantTrue.


```go
func IsConditionSetAsExpectedSilent((node *v1.Node, conditionType v1.NodeConditionType, wantTrue bool)) (node *v1.Node, conditionType v1.NodeConditionType, wantTrue bool)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** conditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.NodeConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** wantTrue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/util.go:90`



---


[function] name: IsNodeReady file: test/integration/framework/util.go:77 returns_error: нет description: IsNodeReady returns true if:
1) it's Ready condition is set to true
2) doesn't have NetworkUnavailable condition set to 


### IsNodeReady (test/integration/framework/util.go:77)


IsNodeReady returns true if:
1) it's Ready condition is set to true
2) doesn't have NetworkUnavailable condition set to true


```go
func IsNodeReady((node *v1.Node)) (node *v1.Node)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/framework/util.go:77`



---


[function] name: IsNodeSchedulable file: test/integration/framework/util.go:67 returns_error: нет description: IsNodeSchedulable returns true if:
1) doesn't have "unschedulable" field set
2) it also returns true from IsNodeReady


### IsNodeSchedulable (test/integration/framework/util.go:67)


IsNodeSchedulable returns true if:
1) doesn't have "unschedulable" field set
2) it also returns true from IsNodeReady


```go
func IsNodeSchedulable((node *v1.Node)) (node *v1.Node)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/framework/util.go:67`



---


[function] name: isConditionUnset file: test/integration/framework/util.go:95 returns_error: нет description: isConditionUnset returns true if conditions of the given node do not have a match to the given conditionType, otherwise 


### isConditionUnset (test/integration/framework/util.go:95)


isConditionUnset returns true if conditions of the given node do not have a match to the given conditionType, otherwise false.


```go
func isConditionUnset((node *v1.Node, conditionType v1.NodeConditionType)) (node *v1.Node, conditionType v1.NodeConditionType)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** conditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.NodeConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/util.go:95`



---


[function] name: isNodeConditionSetAsExpected file: test/integration/framework/util.go:105 returns_error: нет description: isNodeConditionSetAsExpected checks a node for a condition, and returns 'true' if the wanted value is the same as the co


### isNodeConditionSetAsExpected (test/integration/framework/util.go:105)


isNodeConditionSetAsExpected checks a node for a condition, and returns 'true' if the wanted value is the same as the condition value, useful for polling until a condition on a node is met.


```go
func isNodeConditionSetAsExpected((node *v1.Node, conditionType v1.NodeConditionType, wantTrue, silent bool)) (node *v1.Node, conditionType v1.NodeConditionType, wantTrue, silent bool)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** conditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.NodeConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** wantTrue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** silent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/framework/util.go:105`




## test/integration/ipamperf/results.go


📄 Исходный файл: `test/integration/ipamperf/results.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-testintegrationipamperfresultsgo210) `:210`

- 🔗 [NewObserver](#newobserver-testintegrationipamperfresultsgo85) `:85`

- 🔗 [Results](#results-testintegrationipamperfresultsgo105) `:105`

- 🔗 [StartObserving](#startobserving-testintegrationipamperfresultsgo97) `:97`

- 🔗 [String](#string-testintegrationipamperfresultsgo194) `:194`

- 🔗 [UnmarshalJSON](#unmarshaljson-testintegrationipamperfresultsgo215) `:215`

- 🔗 [monitor](#monitor-testintegrationipamperfresultsgo146) `:146`


</details>


[function] name: MarshalJSON file: test/integration/ipamperf/results.go:210 returns_error: да description: MarshalJSON implements the json.Marshaler interface


### MarshalJSON (test/integration/ipamperf/results.go:210)


MarshalJSON implements the json.Marshaler interface


```go
func (jDuration *JSONDuration) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/ipamperf/results.go:210`



---


[function] name: NewObserver file: test/integration/ipamperf/results.go:85 returns_error: нет description: NewObserver creates a new observer given a handle to the Clientset


### NewObserver (test/integration/ipamperf/results.go:85)


NewObserver creates a new observer given a handle to the Clientset


```go
func NewObserver((clientSet *clientset.Clientset, numNodes int)) (clientSet *clientset.Clientset, numNodes int)
```


**Тип запроса:** clientset.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


**Тип ответа:** numNodes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/ipamperf/results.go:85`



---


[function] name: Results file: test/integration/ipamperf/results.go:105 returns_error: нет description: Results returns the test results. It waits for the observer to finish
and returns the computed results of the observatio


### Results (test/integration/ipamperf/results.go:105)


Results returns the test results. It waits for the observer to finish
and returns the computed results of the observations.


```go
func (o *Observer) Results((name string, config *Config)) (name string, config *Config)
```


**Тип запроса:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


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


📍 *Расположение:* `test/integration/ipamperf/results.go:105`



---


[function] name: StartObserving file: test/integration/ipamperf/results.go:97 returns_error: нет description: StartObserving starts an asynchronous loop to monitor for node changes.
Call Results() to get the test results after sta


### StartObserving (test/integration/ipamperf/results.go:97)


StartObserving starts an asynchronous loop to monitor for node changes.
Call Results() to get the test results after starting observer.


```go
func (o *Observer) StartObserving(()) ()
```


📍 *Расположение:* `test/integration/ipamperf/results.go:97`



---


[function] name: String file: test/integration/ipamperf/results.go:194 returns_error: нет description: String implements the Stringer interface and returns a multi-line representation
of the test results.


### String (test/integration/ipamperf/results.go:194)


String implements the Stringer interface and returns a multi-line representation
of the test results.


```go
func (results *Results) String(()) ()
```


📍 *Расположение:* `test/integration/ipamperf/results.go:194`



---


[function] name: UnmarshalJSON file: test/integration/ipamperf/results.go:215 returns_error: да description: UnmarshalJSON implements the json.Unmarshaler interface


### UnmarshalJSON (test/integration/ipamperf/results.go:215)


UnmarshalJSON implements the json.Unmarshaler interface


```go
func (jDuration *JSONDuration) UnmarshalJSON((err error)) (err error)
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


📍 *Расположение:* `test/integration/ipamperf/results.go:215`



---


[function] name: monitor file: test/integration/ipamperf/results.go:146 returns_error: нет description: —


### monitor (test/integration/ipamperf/results.go:146)


monitor is a method that performs operations based on the provided parameters and returns ().


```go
func (o *Observer) monitor(()) ()
```


📍 *Расположение:* `test/integration/ipamperf/results.go:146`




## test/integration/logs/benchmark/load.go


📄 Исходный файл: `test/integration/logs/benchmark/load.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [String](#string-testintegrationlogsbenchmarkloadgo106) `:106`

- 🔗 [loadLog](#loadlog-testintegrationlogsbenchmarkloadgo115) `:115`

- 🔗 [parseLine](#parseline-testintegrationlogsbenchmarkloadgo159) `:159`

- 🔗 [toObject](#toobject-testintegrationlogsbenchmarkloadgo258) `:258`


</details>


[function] name: String file: test/integration/logs/benchmark/load.go:106 returns_error: нет description: Doesn't work?
Unrecognized lines: {{with $delta := sub .TotalLines .JsonLines}}{{$delta}} ({{percent $delta .TotalLines}


### String (test/integration/logs/benchmark/load.go:106)


Doesn't work?
Unrecognized lines: {{with $delta := sub .TotalLines .JsonLines}}{{$delta}} ({{percent $delta .TotalLines}} of total lines){{end}}


```go
func (s logStats) String(()) ()
```


📍 *Расположение:* `test/integration/logs/benchmark/load.go:106`



---


[function] name: loadLog file: test/integration/logs/benchmark/load.go:115 returns_error: да description: —


### loadLog (test/integration/logs/benchmark/load.go:115)


loadLog is a function that performs operations based on the provided parameters and may return an error.


```go
func loadLog((messages []logMessage, stats logStats, err error)) (messages []logMessage, stats logStats, err error)
```


**Тип ответа:** messages


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logMessage


```json
{
  "msg": "string",
  "verbosity": 0,
  "err": {},
  "isError": false,
  "kvs": []
}
```


*Определено в:* `test/integration/logs/benchmark/load.go`


**Тип ответа:** stats


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logStats


```json
{
  "TotalLines": 0,
  "ArgCounts": {},
  "OtherLines": [],
  "OtherArgs": [],
  "MultiLineArgs": [],
  "ObjectTypes": {}
}
```


*Определено в:* `test/integration/logs/benchmark/load.go`


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


*Типы возврата:* `messages []logMessage`, `stats logStats`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/logs/benchmark/load.go:115`



---


[function] name: parseLine file: test/integration/logs/benchmark/load.go:159 returns_error: да description: —


### parseLine (test/integration/logs/benchmark/load.go:159)


parseLine is a function that performs operations based on the provided parameters and may return an error.


```go
func parseLine((item logMessage, err error)) (item logMessage, err error)
```


**Тип ответа:** item


```json
{
  "allocator": null,
  "serviceCIDRs": {}
}
```


*Определено в:* `pkg/registry/core/service/ipallocator/cidrallocator.go`


**Тип ответа:** logMessage


```json
{
  "msg": "string",
  "verbosity": 0,
  "err": {},
  "isError": false,
  "kvs": []
}
```


*Определено в:* `test/integration/logs/benchmark/load.go`


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


*Типы возврата:* `item logMessage`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/logs/benchmark/load.go:159`



---


[function] name: toObject file: test/integration/logs/benchmark/load.go:258 returns_error: нет description: —


### toObject (test/integration/logs/benchmark/load.go:258)


toObject is a function that performs operations based on the provided parameters and returns (value interface{}).


```go
func toObject((value interface{})) (value interface{})
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/integration/logs/benchmark/load.go:258`




## test/integration/scheduler/queueing/queue.go


📄 Исходный файл: `test/integration/scheduler/queueing/queue.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RunTestCoreResourceEnqueue](#runtestcoreresourceenqueue-testintegrationschedulerqueueingqueuego2704) `:2704`


</details>


[function] name: RunTestCoreResourceEnqueue file: test/integration/scheduler/queueing/queue.go:2704 returns_error: нет description: TestCoreResourceEnqueue verify Pods failed by in-tree default plugins can be
moved properly upon their registered events


### RunTestCoreResourceEnqueue (test/integration/scheduler/queueing/queue.go:2704)


TestCoreResourceEnqueue verify Pods failed by in-tree default plugins can be
moved properly upon their registered events.


```go
func RunTestCoreResourceEnqueue((t *testing.T, tt *CoreResourceEnqueueTestCase)) (t *testing.T, tt *CoreResourceEnqueueTestCase)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** CoreResourceEnqueueTestCase


```json
{
  "Name": "string",
  "InitialNodes": [],
  "InitialPods": [],
  "InitialPVCs": [],
  "InitialPVs": [],
  "InitialStorageClasses": [],
  "InitialCSINodes": [],
  "InitialCSIDrivers": [],
  "InitialStorageCapacities": [],
  "InitialVolumeAttachment": [],
  "InitialDeviceClasses": [],
  "InitialWorkloads": [],
  "Pods": [],
  "ExpectedInitialRejectingPhase": {},
  "TriggerFn": {},
  "WantRequeuedPods": {},
  "EnableSchedulingQueueHint": {},
  "EnablePlugins": [],
  "EnableDRAExtendedResource": false,
  "EnableNodeDeclaredFeatures": false,
  "EnableGangScheduling": false
}
```


*Определено в:* `test/integration/scheduler/queueing/queue.go`


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


**Тип ответа:** tt


```json
{
  "client": {}
}
```


*Определено в:* `cmd/kubeadm/app/phases/upgrade/versiongetter.go`


**Тип ответа:** CoreResourceEnqueueTestCase


```json
{
  "Name": "string",
  "InitialNodes": [],
  "InitialPods": [],
  "InitialPVCs": [],
  "InitialPVs": [],
  "InitialStorageClasses": [],
  "InitialCSINodes": [],
  "InitialCSIDrivers": [],
  "InitialStorageCapacities": [],
  "InitialVolumeAttachment": [],
  "InitialDeviceClasses": [],
  "InitialWorkloads": [],
  "Pods": [],
  "ExpectedInitialRejectingPhase": {},
  "TriggerFn": {},
  "WantRequeuedPods": {},
  "EnableSchedulingQueueHint": {},
  "EnablePlugins": [],
  "EnableDRAExtendedResource": false,
  "EnableNodeDeclaredFeatures": false,
  "EnableGangScheduling": false
}
```


*Определено в:* `test/integration/scheduler/queueing/queue.go`


📍 *Расположение:* `test/integration/scheduler/queueing/queue.go:2704`




## test/integration/scheduler/util.go


📄 Исходный файл: `test/integration/scheduler/util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [InitRegistryAndConfig](#initregistryandconfig-testintegrationschedulerutilgo94) `:94`

- 🔗 [InitTestSchedulerForFrameworkTest](#inittestschedulerforframeworktest-testintegrationschedulerutilgo48) `:48`

- 🔗 [NewPlugin](#newplugin-testintegrationschedulerutilgo87) `:87`


</details>


[function] name: InitRegistryAndConfig file: test/integration/scheduler/util.go:94 returns_error: нет description: InitRegistryAndConfig returns registry and plugins config based on give plugins.


### InitRegistryAndConfig (test/integration/scheduler/util.go:94)


InitRegistryAndConfig returns registry and plugins config based on give plugins.


```go
func InitRegistryAndConfig((frameworkruntime.Registry, schedulerconfig.KubeSchedulerProfile)) (frameworkruntime.Registry, schedulerconfig.KubeSchedulerProfile)
```


**Тип ответа:** frameworkruntime.Registry


```json
{
  "Username": "string",
  "Password": "string",
  "Email": "string"
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/credentialconfig/registry.go`


**Тип ответа:** schedulerconfig.KubeSchedulerProfile


```json
{
  "SchedulerName": "string",
  "PercentageOfNodesToScore": 0,
  "Plugins": null,
  "PluginConfig": []
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


📍 *Расположение:* `test/integration/scheduler/util.go:94`



---


[function] name: InitTestSchedulerForFrameworkTest file: test/integration/scheduler/util.go:48 returns_error: нет description: The returned shutdown func will delete created resources and scheduler, resources should be those
that will affect the s


### InitTestSchedulerForFrameworkTest (test/integration/scheduler/util.go:48)


The returned shutdown func will delete created resources and scheduler, resources should be those
that will affect the scheduling result, like nodes, pods, etc.. Namespaces should not be
deleted here because it's created together with the apiserver, they should be deleted
simultaneously or we'll have no namespace.
This should only be called when you want to kill the scheduler alone, away from apiserver.
For example, in scheduler integration tests, recreating apiserver is performance consuming,
then shutdown the scheduler and recreate it between each test case is a better approach.


```go
func InitTestSchedulerForFrameworkTest((*testutils.TestContext, testutils.ShutdownFunc)) (*testutils.TestContext, testutils.ShutdownFunc)
```


**Тип запроса:** testutils.TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** testutils.TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** testutils.ShutdownFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler/util.go:48`



---


[function] name: NewPlugin file: test/integration/scheduler/util.go:87 returns_error: нет description: NewPlugin returns a plugin factory with specified Plugin.


### NewPlugin (test/integration/scheduler/util.go:87)


NewPlugin returns a plugin factory with specified Plugin.


```go
func NewPlugin((plugin fwk.Plugin)) (plugin fwk.Plugin)
```


**Тип ответа:** plugin


```json
{
  "observer": {},
  "extraLabels": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/metrics/metrics.go`


**Тип ответа:** fwk.Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


📍 *Расположение:* `test/integration/scheduler/util.go:87`




## test/integration/scheduler_perf/dra.go


📄 Исходный файл: `test/integration/scheduler_perf/dra.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfdrago82) `:82`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfdrago159) `:159`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfdrago267) `:267`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfdrago69) `:69`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfdrago146) `:146`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfdrago263) `:263`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfdrago85) `:85`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfdrago162) `:162`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfdrago270) `:270`

- 🔗 [requiredNamespaces](#requirednamespaces-testintegrationscheduler_perfdrago96) `:96`

- 🔗 [requiredNamespaces](#requirednamespaces-testintegrationscheduler_perfdrago274) `:274`

- 🔗 [resourceSlice](#resourceslice-testintegrationscheduler_perfdrago215) `:215`

- 🔗 [run](#run-testintegrationscheduler_perfdrago100) `:100`

- 🔗 [run](#run-testintegrationscheduler_perfdrago173) `:173`

- 🔗 [run](#run-testintegrationscheduler_perfdrago276) `:276`


</details>


[function] name: collectsMetrics file: test/integration/scheduler_perf/dra.go:82 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/dra.go:82)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (op *createResourceClaimsOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:82`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/dra.go:159 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/dra.go:159)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (op *createResourceDriverOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:159`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/dra.go:267 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/dra.go:267)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (op *allocResourceClaimsOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:267`



---


[function] name: isValid file: test/integration/scheduler_perf/dra.go:69 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/dra.go:69)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (op *createResourceClaimsOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:69`



---


[function] name: isValid file: test/integration/scheduler_perf/dra.go:146 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/dra.go:146)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (op *createResourceDriverOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:146`



---


[function] name: isValid file: test/integration/scheduler_perf/dra.go:263 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/dra.go:263)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (op *allocResourceClaimsOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:263`



---


[function] name: patchParams file: test/integration/scheduler_perf/dra.go:85 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/dra.go:85)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (op *createResourceClaimsOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:85`



---


[function] name: patchParams file: test/integration/scheduler_perf/dra.go:162 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/dra.go:162)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (op *createResourceDriverOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:162`



---


[function] name: patchParams file: test/integration/scheduler_perf/dra.go:270 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/dra.go:270)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (op *allocResourceClaimsOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:270`



---


[function] name: requiredNamespaces file: test/integration/scheduler_perf/dra.go:96 returns_error: нет description: —


### requiredNamespaces (test/integration/scheduler_perf/dra.go:96)


requiredNamespaces is a method that performs operations based on the provided parameters and returns ().


```go
func (op *createResourceClaimsOp) requiredNamespaces(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:96`



---


[function] name: requiredNamespaces file: test/integration/scheduler_perf/dra.go:274 returns_error: нет description: —


### requiredNamespaces (test/integration/scheduler_perf/dra.go:274)


requiredNamespaces is a method that performs operations based on the provided parameters and returns ().


```go
func (op *allocResourceClaimsOp) requiredNamespaces(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:274`



---


[function] name: resourceSlice file: test/integration/scheduler_perf/dra.go:215 returns_error: нет description: —


### resourceSlice (test/integration/scheduler_perf/dra.go:215)


resourceSlice is a function that performs operations based on the provided parameters and returns (driverName, nodeName string, capacity int).


```go
func resourceSlice((driverName, nodeName string, capacity int)) (driverName, nodeName string, capacity int)
```


**Тип ответа:** driverName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** capacity


```json
{
  "tsInfo": {}
}
```


*Определено в:* `test/e2e/storage/testsuites/capacity.go`


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:215`



---


[function] name: run file: test/integration/scheduler_perf/dra.go:100 returns_error: нет description: —


### run (test/integration/scheduler_perf/dra.go:100)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (op *createResourceClaimsOp) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:100`



---


[function] name: run file: test/integration/scheduler_perf/dra.go:173 returns_error: нет description: —


### run (test/integration/scheduler_perf/dra.go:173)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, draManager framework.SharedDRAManager).


```go
func (op *createResourceDriverOp) run((tCtx ktesting.TContext, draManager framework.SharedDRAManager)) (tCtx ktesting.TContext, draManager framework.SharedDRAManager)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** draManager


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** framework.SharedDRAManager


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:173`



---


[function] name: run file: test/integration/scheduler_perf/dra.go:276 returns_error: нет description: —


### run (test/integration/scheduler_perf/dra.go:276)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (op *allocResourceClaimsOp) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/dra.go:276`




## test/integration/scheduler_perf/executor.go


📄 Исходный файл: `test/integration/scheduler_perf/executor.go`


<details open>
<summary><b>Функции в этом файле (33)</b></summary>


- 🔗 [GetNodeTemplate](#getnodetemplate-testintegrationscheduler_perfexecutorgo864) `:864`

- 🔗 [GetPodTemplate](#getpodtemplate-testintegrationscheduler_perfexecutorgo874) `:874`

- 🔗 [cleanup](#cleanup-testintegrationscheduler_perfexecutorgo965) `:965`

- 🔗 [createNamespaceIfNotPresent](#createnamespaceifnotpresent-testintegrationscheduler_perfexecutorgo499) `:499`

- 🔗 [createPodsRapidly](#createpodsrapidly-testintegrationscheduler_perfexecutorgo514) `:514`

- 🔗 [createPodsSteadily](#createpodssteadily-testintegrationscheduler_perfexecutorgo531) `:531`

- 🔗 [getCustomVolumeFactory](#getcustomvolumefactory-testintegrationscheduler_perfexecutorgo898) `:898`

- 🔗 [getNodePreparer](#getnodepreparer-testintegrationscheduler_perfexecutorgo783) `:783`

- 🔗 [getPersistentVolumeClaimSpecFromFile](#getpersistentvolumeclaimspecfromfile-testintegrationscheduler_perfexecutorgo890) `:890`

- 🔗 [getPersistentVolumeSpecFromFile](#getpersistentvolumespecfromfile-testintegrationscheduler_perfexecutorgo882) `:882`

- 🔗 [getPodStrategy](#getpodstrategy-testintegrationscheduler_perfexecutorgo842) `:842`

- 🔗 [getUnstructuredFromFile](#getunstructuredfromfile-testintegrationscheduler_perfexecutorgo977) `:977`

- 🔗 [namespaces](#namespaces-testintegrationscheduler_perfexecutorgo936) `:936`

- 🔗 [newNamespacePreparer](#newnamespacepreparer-testintegrationscheduler_perfexecutorgo920) `:920`

- 🔗 [prepare](#prepare-testintegrationscheduler_perfexecutorgo945) `:945`

- 🔗 [runBarrierOp](#runbarrierop-testintegrationscheduler_perfexecutorgo137) `:137`

- 🔗 [runChurnOp](#runchurnop-testintegrationscheduler_perfexecutorgo292) `:292`

- 🔗 [runCreateNamespaceOp](#runcreatenamespaceop-testintegrationscheduler_perfexecutorgo115) `:115`

- 🔗 [runCreateNodesOp](#runcreatenodesop-testintegrationscheduler_perfexecutorgo103) `:103`

- 🔗 [runCreatePodsOp](#runcreatepodsop-testintegrationscheduler_perfexecutorgo186) `:186`

- 🔗 [runDefaultOp](#rundefaultop-testintegrationscheduler_perfexecutorgo399) `:399`

- 🔗 [runDeletePodsOp](#rundeletepodsop-testintegrationscheduler_perfexecutorgo241) `:241`

- 🔗 [runOp](#runop-testintegrationscheduler_perfexecutorgo75) `:75`

- 🔗 [runSleepOp](#runsleepop-testintegrationscheduler_perfexecutorgo168) `:168`

- 🔗 [runStartCollectingMetricsOp](#runstartcollectingmetricsop-testintegrationscheduler_perfexecutorgo414) `:414`

- 🔗 [runStopCollectingMetrics](#runstopcollectingmetrics-testintegrationscheduler_perfexecutorgo176) `:176`

- 🔗 [startCollectingMetrics](#startcollectingmetrics-testintegrationscheduler_perfexecutorgo426) `:426`

- 🔗 [stopCollectingMetrics](#stopcollectingmetrics-testintegrationscheduler_perfexecutorgo458) `:458`

- 🔗 [wait](#wait-testintegrationscheduler_perfexecutorgo70) `:70`

- 🔗 [waitUntilPodsAttempted](#waituntilpodsattempted-testintegrationscheduler_perfexecutorgo724) `:724`

- 🔗 [waitUntilPodsAttemptedInNamespace](#waituntilpodsattemptedinnamespace-testintegrationscheduler_perfexecutorgo751) `:751`

- 🔗 [waitUntilPodsScheduled](#waituntilpodsscheduled-testintegrationscheduler_perfexecutorgo698) `:698`

- 🔗 [waitUntilPodsScheduledInNamespace](#waituntilpodsscheduledinnamespace-testintegrationscheduler_perfexecutorgo808) `:808`


</details>


[function] name: GetNodeTemplate file: test/integration/scheduler_perf/executor.go:864 returns_error: да description: —


### GetNodeTemplate (test/integration/scheduler_perf/executor.go:864)


GetNodeTemplate is a method that retrieves data based on the provided parameters and may return an error.


```go
func (f nodeTemplateFromFile) GetNodeTemplate((*v1.Node, error)) (*v1.Node, error)
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


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:864`



---


[function] name: GetPodTemplate file: test/integration/scheduler_perf/executor.go:874 returns_error: да description: —


### GetPodTemplate (test/integration/scheduler_perf/executor.go:874)


GetPodTemplate is a method that retrieves data based on the provided parameters and may return an error.


```go
func (f podTemplateFromFile) GetPodTemplate((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:874`



---


[function] name: cleanup file: test/integration/scheduler_perf/executor.go:965 returns_error: нет description: cleanup deletes existing test namespaces.


### cleanup (test/integration/scheduler_perf/executor.go:965)


cleanup deletes existing test namespaces.


```go
func (p *namespacePreparer) cleanup((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:965`



---


[function] name: createNamespaceIfNotPresent file: test/integration/scheduler_perf/executor.go:499 returns_error: нет description: —


### createNamespaceIfNotPresent (test/integration/scheduler_perf/executor.go:499)


createNamespaceIfNotPresent is a function that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, namespace string, podsPerNamespace *map[string]int).


```go
func createNamespaceIfNotPresent((tCtx ktesting.TContext, namespace string, podsPerNamespace *map[string]int)) (tCtx ktesting.TContext, namespace string, podsPerNamespace *map[string]int)
```


**Тип запроса:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podsPerNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:499`



---


[function] name: createPodsRapidly file: test/integration/scheduler_perf/executor.go:514 returns_error: нет description: createPodsRapidly implements the "create pods rapidly" mode of [createPodsOp].
It's a nop when cpo.SteadyState is true.


### createPodsRapidly (test/integration/scheduler_perf/executor.go:514)


createPodsRapidly implements the "create pods rapidly" mode of [createPodsOp].
It's a nop when cpo.SteadyState is true.


```go
func createPodsRapidly((tCtx ktesting.TContext, namespace string, cpo *createPodsOp)) (tCtx ktesting.TContext, namespace string, cpo *createPodsOp)
```


**Тип запроса:** createPodsOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "SteadyState": false,
  "SteadyStateParam": "string",
  "Duration": {},
  "DurationParam": "string",
  "CollectMetrics": false,
  "Namespace": "string",
  "PodTemplatePath": "string",
  "SkipWaitToCompletion": false,
  "PersistentVolumeTemplatePath": "string",
  "PersistentVolumeClaimTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** cpo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** createPodsOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "SteadyState": false,
  "SteadyStateParam": "string",
  "Duration": {},
  "DurationParam": "string",
  "CollectMetrics": false,
  "Namespace": "string",
  "PodTemplatePath": "string",
  "SkipWaitToCompletion": false,
  "PersistentVolumeTemplatePath": "string",
  "PersistentVolumeClaimTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:514`



---


[function] name: createPodsSteadily file: test/integration/scheduler_perf/executor.go:531 returns_error: нет description: createPodsSteadily implements the "create pods and delete pods" mode of [createPodsOp].
It's a nop when cpo.SteadyState 


### createPodsSteadily (test/integration/scheduler_perf/executor.go:531)


createPodsSteadily implements the "create pods and delete pods" mode of [createPodsOp].
It's a nop when cpo.SteadyState is false.


```go
func createPodsSteadily((tCtx ktesting.TContext, namespace string, podInformer coreinformers.PodInformer, cpo *createPodsOp)) (tCtx ktesting.TContext, namespace string, podInformer coreinformers.PodInformer, cpo *createPodsOp)
```


**Тип запроса:** createPodsOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "SteadyState": false,
  "SteadyStateParam": "string",
  "Duration": {},
  "DurationParam": "string",
  "CollectMetrics": false,
  "Namespace": "string",
  "PodTemplatePath": "string",
  "SkipWaitToCompletion": false,
  "PersistentVolumeTemplatePath": "string",
  "PersistentVolumeClaimTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/pod.go`


**Тип ответа:** coreinformers.PodInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cpo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** createPodsOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "SteadyState": false,
  "SteadyStateParam": "string",
  "Duration": {},
  "DurationParam": "string",
  "CollectMetrics": false,
  "Namespace": "string",
  "PodTemplatePath": "string",
  "SkipWaitToCompletion": false,
  "PersistentVolumeTemplatePath": "string",
  "PersistentVolumeClaimTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:531`



---


[function] name: getCustomVolumeFactory file: test/integration/scheduler_perf/executor.go:898 returns_error: нет description: —


### getCustomVolumeFactory (test/integration/scheduler_perf/executor.go:898)


getCustomVolumeFactory is a function that performs operations based on the provided parameters and returns (pvTemplate *v1.PersistentVolume).


```go
func getCustomVolumeFactory((pvTemplate *v1.PersistentVolume)) (pvTemplate *v1.PersistentVolume)
```


**Тип запроса:** v1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** pvTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:898`



---


[function] name: getNodePreparer file: test/integration/scheduler_perf/executor.go:783 returns_error: да description: —


### getNodePreparer (test/integration/scheduler_perf/executor.go:783)


getNodePreparer is a function that performs operations based on the provided parameters and may return an error.


```go
func getNodePreparer((testutils.TestNodePreparer, error)) (testutils.TestNodePreparer, error)
```


**Тип ответа:** testutils.TestNodePreparer


```json
{
  "client": {},
  "countToStrategy": [],
  "nodeTemplate": {}
}
```


*Определено в:* `test/integration/scheduler_perf/node_util.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `testutils.TestNodePreparer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:783`



---


[function] name: getPersistentVolumeClaimSpecFromFile file: test/integration/scheduler_perf/executor.go:890 returns_error: да description: —


### getPersistentVolumeClaimSpecFromFile (test/integration/scheduler_perf/executor.go:890)


getPersistentVolumeClaimSpecFromFile is a function that performs operations based on the provided parameters and may return an error.


```go
func getPersistentVolumeClaimSpecFromFile((*v1.PersistentVolumeClaim, error)) (*v1.PersistentVolumeClaim, error)
```


**Тип запроса:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.PersistentVolumeClaim`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:890`



---


[function] name: getPersistentVolumeSpecFromFile file: test/integration/scheduler_perf/executor.go:882 returns_error: да description: —


### getPersistentVolumeSpecFromFile (test/integration/scheduler_perf/executor.go:882)


getPersistentVolumeSpecFromFile is a function that performs operations based on the provided parameters and may return an error.


```go
func getPersistentVolumeSpecFromFile((*v1.PersistentVolume, error)) (*v1.PersistentVolume, error)
```


**Тип запроса:** v1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.PersistentVolume`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:882`



---


[function] name: getPodStrategy file: test/integration/scheduler_perf/executor.go:842 returns_error: да description: —


### getPodStrategy (test/integration/scheduler_perf/executor.go:842)


getPodStrategy is a function that performs operations based on the provided parameters and may return an error.


```go
func getPodStrategy((testutils.TestPodCreateStrategy, error)) (testutils.TestPodCreateStrategy, error)
```


**Тип ответа:** testutils.TestPodCreateStrategy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `testutils.TestPodCreateStrategy`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:842`



---


[function] name: getUnstructuredFromFile file: test/integration/scheduler_perf/executor.go:977 returns_error: да description: —


### getUnstructuredFromFile (test/integration/scheduler_perf/executor.go:977)


getUnstructuredFromFile is a function that performs operations based on the provided parameters and may return an error.


```go
func getUnstructuredFromFile((*unstructured.Unstructured, *schema.GroupVersionKind, error)) (*unstructured.Unstructured, *schema.GroupVersionKind, error)
```


**Тип запроса:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Тип запроса:** schema.GroupVersionKind


```json
{
  "Group": "string",
  "Version": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Тип ответа:** schema.GroupVersionKind


```json
{
  "Group": "string",
  "Version": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*unstructured.Unstructured`, `*schema.GroupVersionKind`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:977`



---


[function] name: namespaces file: test/integration/scheduler_perf/executor.go:936 returns_error: нет description: namespaces returns namespace names have been (or will be) created by this namespacePreparer


### namespaces (test/integration/scheduler_perf/executor.go:936)


namespaces returns namespace names have been (or will be) created by this namespacePreparer


```go
func (p *namespacePreparer) namespaces(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:936`



---


[function] name: newNamespacePreparer file: test/integration/scheduler_perf/executor.go:920 returns_error: да description: —


### newNamespacePreparer (test/integration/scheduler_perf/executor.go:920)


newNamespacePreparer is a function that performs operations based on the provided parameters and may return an error.


```go
func newNamespacePreparer((*namespacePreparer, error)) (*namespacePreparer, error)
```


**Тип запроса:** namespacePreparer


```json
{
  "count": 0,
  "prefix": "string",
  "spec": null
}
```


*Определено в:* `test/integration/scheduler_perf/executor.go`


**Тип ответа:** namespacePreparer


```json
{
  "count": 0,
  "prefix": "string",
  "spec": null
}
```


*Определено в:* `test/integration/scheduler_perf/executor.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*namespacePreparer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:920`



---


[function] name: prepare file: test/integration/scheduler_perf/executor.go:945 returns_error: нет description: prepare creates the namespaces.


### prepare (test/integration/scheduler_perf/executor.go:945)


prepare creates the namespaces.


```go
func (p *namespacePreparer) prepare((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:945`



---


[function] name: runBarrierOp file: test/integration/scheduler_perf/executor.go:137 returns_error: нет description: —


### runBarrierOp (test/integration/scheduler_perf/executor.go:137)


runBarrierOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op *barrierOp).


```go
func (e *WorkloadExecutor) runBarrierOp((tCtx ktesting.TContext, opIndex int, op *barrierOp)) (tCtx ktesting.TContext, opIndex int, op *barrierOp)
```


**Тип запроса:** barrierOp


```json
{
  "Opcode": {},
  "Namespaces": [],
  "LabelSelector": {},
  "StageRequirement": {}
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** barrierOp


```json
{
  "Opcode": {},
  "Namespaces": [],
  "LabelSelector": {},
  "StageRequirement": {}
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:137`



---


[function] name: runChurnOp file: test/integration/scheduler_perf/executor.go:292 returns_error: нет description: —


### runChurnOp (test/integration/scheduler_perf/executor.go:292)


runChurnOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op *churnOp).


```go
func (e *WorkloadExecutor) runChurnOp((tCtx ktesting.TContext, opIndex int, op *churnOp)) (tCtx ktesting.TContext, opIndex int, op *churnOp)
```


**Тип запроса:** churnOp


```json
{
  "Opcode": {},
  "Mode": "string",
  "Number": 0,
  "IntervalMilliseconds": 0,
  "Namespace": "string",
  "TemplatePaths": []
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** churnOp


```json
{
  "Opcode": {},
  "Mode": "string",
  "Number": 0,
  "IntervalMilliseconds": 0,
  "Namespace": "string",
  "TemplatePaths": []
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:292`



---


[function] name: runCreateNamespaceOp file: test/integration/scheduler_perf/executor.go:115 returns_error: нет description: —


### runCreateNamespaceOp (test/integration/scheduler_perf/executor.go:115)


runCreateNamespaceOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op *createNamespacesOp).


```go
func (e *WorkloadExecutor) runCreateNamespaceOp((tCtx ktesting.TContext, opIndex int, op *createNamespacesOp)) (tCtx ktesting.TContext, opIndex int, op *createNamespacesOp)
```


**Тип запроса:** createNamespacesOp


```json
{
  "Opcode": {},
  "Prefix": "string",
  "Count": 0,
  "CountParam": "string",
  "NamespaceTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** createNamespacesOp


```json
{
  "Opcode": {},
  "Prefix": "string",
  "Count": 0,
  "CountParam": "string",
  "NamespaceTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:115`



---


[function] name: runCreateNodesOp file: test/integration/scheduler_perf/executor.go:103 returns_error: нет description: —


### runCreateNodesOp (test/integration/scheduler_perf/executor.go:103)


runCreateNodesOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op *createNodesOp).


```go
func (e *WorkloadExecutor) runCreateNodesOp((tCtx ktesting.TContext, opIndex int, op *createNodesOp)) (tCtx ktesting.TContext, opIndex int, op *createNodesOp)
```


**Тип запроса:** createNodesOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "NodeTemplatePath": "string",
  "NodeAllocatableStrategy": null,
  "LabelNodePrepareStrategy": null,
  "UniqueNodeLabelStrategy": null
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** createNodesOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "NodeTemplatePath": "string",
  "NodeAllocatableStrategy": null,
  "LabelNodePrepareStrategy": null,
  "UniqueNodeLabelStrategy": null
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:103`



---


[function] name: runCreatePodsOp file: test/integration/scheduler_perf/executor.go:186 returns_error: нет description: —


### runCreatePodsOp (test/integration/scheduler_perf/executor.go:186)


runCreatePodsOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op *createPodsOp).


```go
func (e *WorkloadExecutor) runCreatePodsOp((tCtx ktesting.TContext, opIndex int, op *createPodsOp)) (tCtx ktesting.TContext, opIndex int, op *createPodsOp)
```


**Тип запроса:** createPodsOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "SteadyState": false,
  "SteadyStateParam": "string",
  "Duration": {},
  "DurationParam": "string",
  "CollectMetrics": false,
  "Namespace": "string",
  "PodTemplatePath": "string",
  "SkipWaitToCompletion": false,
  "PersistentVolumeTemplatePath": "string",
  "PersistentVolumeClaimTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** createPodsOp


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "SteadyState": false,
  "SteadyStateParam": "string",
  "Duration": {},
  "DurationParam": "string",
  "CollectMetrics": false,
  "Namespace": "string",
  "PodTemplatePath": "string",
  "SkipWaitToCompletion": false,
  "PersistentVolumeTemplatePath": "string",
  "PersistentVolumeClaimTemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:186`



---


[function] name: runDefaultOp file: test/integration/scheduler_perf/executor.go:399 returns_error: нет description: —


### runDefaultOp (test/integration/scheduler_perf/executor.go:399)


runDefaultOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op realOp).


```go
func (e *WorkloadExecutor) runDefaultOp((tCtx ktesting.TContext, opIndex int, op realOp)) (tCtx ktesting.TContext, opIndex int, op realOp)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:399`



---


[function] name: runDeletePodsOp file: test/integration/scheduler_perf/executor.go:241 returns_error: нет description: —


### runDeletePodsOp (test/integration/scheduler_perf/executor.go:241)


runDeletePodsOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op *deletePodsOp).


```go
func (e *WorkloadExecutor) runDeletePodsOp((tCtx ktesting.TContext, opIndex int, op *deletePodsOp)) (tCtx ktesting.TContext, opIndex int, op *deletePodsOp)
```


**Тип запроса:** deletePodsOp


```json
{
  "Opcode": {},
  "Namespace": "string",
  "LabelSelector": {},
  "SkipWaitToCompletion": false,
  "DeletePodsPerSecond": 0
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** deletePodsOp


```json
{
  "Opcode": {},
  "Namespace": "string",
  "LabelSelector": {},
  "SkipWaitToCompletion": false,
  "DeletePodsPerSecond": 0
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:241`



---


[function] name: runOp file: test/integration/scheduler_perf/executor.go:75 returns_error: нет description: —


### runOp (test/integration/scheduler_perf/executor.go:75)


runOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, op realOp, opIndex int).


```go
func (e *WorkloadExecutor) runOp((tCtx ktesting.TContext, op realOp, opIndex int)) (tCtx ktesting.TContext, op realOp, opIndex int)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:75`



---


[function] name: runSleepOp file: test/integration/scheduler_perf/executor.go:168 returns_error: нет description: —


### runSleepOp (test/integration/scheduler_perf/executor.go:168)


runSleepOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, op *sleepOp).


```go
func (e *WorkloadExecutor) runSleepOp((tCtx ktesting.TContext, op *sleepOp)) (tCtx ktesting.TContext, op *sleepOp)
```


**Тип запроса:** sleepOp


```json
{
  "Opcode": {},
  "Duration": {},
  "DurationParam": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** sleepOp


```json
{
  "Opcode": {},
  "Duration": {},
  "DurationParam": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:168`



---


[function] name: runStartCollectingMetricsOp file: test/integration/scheduler_perf/executor.go:414 returns_error: нет description: —


### runStartCollectingMetricsOp (test/integration/scheduler_perf/executor.go:414)


runStartCollectingMetricsOp is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int, op *startCollectingMetricsOp).


```go
func (e *WorkloadExecutor) runStartCollectingMetricsOp((tCtx ktesting.TContext, opIndex int, op *startCollectingMetricsOp)) (tCtx ktesting.TContext, opIndex int, op *startCollectingMetricsOp)
```


**Тип запроса:** startCollectingMetricsOp


```json
{
  "Opcode": {},
  "Name": "string",
  "Namespaces": [],
  "LabelSelector": {}
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** startCollectingMetricsOp


```json
{
  "Opcode": {},
  "Name": "string",
  "Namespaces": [],
  "LabelSelector": {}
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:414`



---


[function] name: runStopCollectingMetrics file: test/integration/scheduler_perf/executor.go:176 returns_error: нет description: —


### runStopCollectingMetrics (test/integration/scheduler_perf/executor.go:176)


runStopCollectingMetrics is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, opIndex int).


```go
func (e *WorkloadExecutor) runStopCollectingMetrics((tCtx ktesting.TContext, opIndex int)) (tCtx ktesting.TContext, opIndex int)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** opIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:176`



---


[function] name: startCollectingMetrics file: test/integration/scheduler_perf/executor.go:426 returns_error: да description: —


### startCollectingMetrics (test/integration/scheduler_perf/executor.go:426)


startCollectingMetrics is a function that performs operations based on the provided parameters and may return an error.


```go
func startCollectingMetrics(([]testDataCollector, func(string), error)) ([]testDataCollector, func(string), error)
```


**Тип ответа:** testDataCollector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]testDataCollector`, `func(string)`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:426`



---


[function] name: stopCollectingMetrics file: test/integration/scheduler_perf/executor.go:458 returns_error: да description: —


### stopCollectingMetrics (test/integration/scheduler_perf/executor.go:458)


stopCollectingMetrics is a function that performs operations based on the provided parameters and may return an error.


```go
func stopCollectingMetrics(([]DataItem, error)) ([]DataItem, error)
```


**Тип ответа:** DataItem


```json
{
  "Data": {},
  "Unit": "string",
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]DataItem`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:458`



---


[function] name: wait file: test/integration/scheduler_perf/executor.go:70 returns_error: нет description: —


### wait (test/integration/scheduler_perf/executor.go:70)


wait is a method that performs operations based on the provided parameters and returns ().


```go
func (e *WorkloadExecutor) wait(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:70`



---


[function] name: waitUntilPodsAttempted file: test/integration/scheduler_perf/executor.go:724 returns_error: нет description: waitUntilPodsAttempted blocks until the all pods in the given namespaces are
attempted (at least once went through a sch


### waitUntilPodsAttempted (test/integration/scheduler_perf/executor.go:724)


waitUntilPodsAttempted blocks until the all pods in the given namespaces are
attempted (at least once went through a scheduling cycle).


```go
func waitUntilPodsAttempted((tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespaces []string, numPodsScheduledPerNamespace map[string]int)) (tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespaces []string, numPodsScheduledPerNamespace map[string]int)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** podInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/pod.go`


**Тип ответа:** coreinformers.PodInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** namespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** numPodsScheduledPerNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:724`



---


[function] name: waitUntilPodsAttemptedInNamespace file: test/integration/scheduler_perf/executor.go:751 returns_error: нет description: waitUntilPodsAttemptedInNamespace blocks until all pods in the given
namespace at least once went through a scheduling c


### waitUntilPodsAttemptedInNamespace (test/integration/scheduler_perf/executor.go:751)


waitUntilPodsAttemptedInNamespace blocks until all pods in the given
namespace at least once went through a scheduling cycle.
Times out after 10 minutes similarly to waitUntilPodsScheduledInNamespace.


```go
func waitUntilPodsAttemptedInNamespace((tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespace string, wantCount int)) (tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespace string, wantCount int)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** podInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/pod.go`


**Тип ответа:** coreinformers.PodInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** wantCount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:751`



---


[function] name: waitUntilPodsScheduled file: test/integration/scheduler_perf/executor.go:698 returns_error: нет description: waitUntilPodsScheduled blocks until the all pods in the given namespaces are
scheduled.


### waitUntilPodsScheduled (test/integration/scheduler_perf/executor.go:698)


waitUntilPodsScheduled blocks until the all pods in the given namespaces are
scheduled.


```go
func waitUntilPodsScheduled((tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespaces []string, numPodsScheduledPerNamespace map[string]int)) (tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespaces []string, numPodsScheduledPerNamespace map[string]int)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** podInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/pod.go`


**Тип ответа:** coreinformers.PodInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** namespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** numPodsScheduledPerNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:698`



---


[function] name: waitUntilPodsScheduledInNamespace file: test/integration/scheduler_perf/executor.go:808 returns_error: нет description: waitUntilPodsScheduledInNamespace blocks until all pods in the given
namespace are scheduled. Times out after 10 minutes


### waitUntilPodsScheduledInNamespace (test/integration/scheduler_perf/executor.go:808)


waitUntilPodsScheduledInNamespace blocks until all pods in the given
namespace are scheduled. Times out after 10 minutes because even at the
lowest observed QPS of ~10 pods/sec, a 5000-node test should complete.


```go
func waitUntilPodsScheduledInNamespace((tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespace string, wantCount int)) (tCtx ktesting.TContext, podInformer coreinformers.PodInformer, labelSelector map[string]string, namespace string, wantCount int)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** podInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/pod.go`


**Тип ответа:** coreinformers.PodInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** wantCount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/executor.go:808`




## test/integration/scheduler_perf/label_selector.go


📄 Исходный файл: `test/integration/scheduler_perf/label_selector.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [containsStr](#containsstr-testintegrationscheduler_perflabel_selectorgo41) `:41`

- 🔗 [enabled](#enabled-testintegrationscheduler_perflabel_selectorgo24) `:24`


</details>


[function] name: containsStr file: test/integration/scheduler_perf/label_selector.go:41 returns_error: нет description: —


### containsStr (test/integration/scheduler_perf/label_selector.go:41)


containsStr is a function that performs operations based on the provided parameters and returns (hay []string, needle string).


```go
func containsStr((hay []string, needle string)) (hay []string, needle string)
```


**Тип ответа:** hay


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** needle


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/label_selector.go:41`



---


[function] name: enabled file: test/integration/scheduler_perf/label_selector.go:24 returns_error: нет description: enabled checks a label filter that works as in GitHub:
- empty string means enabled
- individual labels are comma-separa


### enabled (test/integration/scheduler_perf/label_selector.go:24)


enabled checks a label filter that works as in GitHub:
- empty string means enabled
- individual labels are comma-separated
- [+]<label> means the workload must have that label
- -<label> means the workload must not have that label


```go
func enabled((labelFilters []string, labels ...string)) (labelFilters []string, labels ...string)
```


**Тип ответа:** labelFilters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


📍 *Расположение:* `test/integration/scheduler_perf/label_selector.go:24`




## test/integration/scheduler_perf/node_util.go


📄 Исходный файл: `test/integration/scheduler_perf/node_util.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [CleanupNodes](#cleanupnodes-testintegrationscheduler_perfnode_utilgo138) `:138`

- 🔗 [GetNodeTemplate](#getnodetemplate-testintegrationscheduler_perfnode_utilgo64) `:64`

- 🔗 [NewIntegrationTestNodePreparer](#newintegrationtestnodepreparer-testintegrationscheduler_perfnode_utilgo76) `:76`

- 🔗 [PrepareNodes](#preparenodes-testintegrationscheduler_perfnode_utilgo85) `:85`

- 🔗 [StaticNodeTemplate](#staticnodetemplate-testintegrationscheduler_perfnode_utilgo56) `:56`

- 🔗 [waitListAllNodes](#waitlistallnodes-testintegrationscheduler_perfnode_utilgo156) `:156`


</details>


[function] name: CleanupNodes file: test/integration/scheduler_perf/node_util.go:138 returns_error: нет description: CleanupNodes deletes existing test nodes.


### CleanupNodes (test/integration/scheduler_perf/node_util.go:138)


CleanupNodes deletes existing test nodes.


```go
func (p *IntegrationTestNodePreparer) CleanupNodes((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/integration/scheduler_perf/node_util.go:138`



---


[function] name: GetNodeTemplate file: test/integration/scheduler_perf/node_util.go:64 returns_error: да description: GetNodeTemplate implements [NodeTemplate.GetNodeTemplate] by returning the same node
for each call.


### GetNodeTemplate (test/integration/scheduler_perf/node_util.go:64)


GetNodeTemplate implements [NodeTemplate.GetNodeTemplate] by returning the same node
for each call.


```go
func (s *staticNodeTemplate) GetNodeTemplate((*v1.Node, error)) (*v1.Node, error)
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


📍 *Расположение:* `test/integration/scheduler_perf/node_util.go:64`



---


[function] name: NewIntegrationTestNodePreparer file: test/integration/scheduler_perf/node_util.go:76 returns_error: нет description: NewIntegrationTestNodePreparer creates an IntegrationTestNodePreparer with a given nodeTemplate.


### NewIntegrationTestNodePreparer (test/integration/scheduler_perf/node_util.go:76)


NewIntegrationTestNodePreparer creates an IntegrationTestNodePreparer with a given nodeTemplate.


```go
func NewIntegrationTestNodePreparer((client clientset.Interface, countToStrategy []testutils.CountToStrategy, nodeTemplate NodeTemplate)) (client clientset.Interface, countToStrategy []testutils.CountToStrategy, nodeTemplate NodeTemplate)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** countToStrategy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** testutils.CountToStrategy


```json
{
  "Count": 0,
  "Strategy": {}
}
```


*Определено в:* `test/utils/runners.go`


**Тип ответа:** nodeTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** NodeTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/node_util.go:76`



---


[function] name: PrepareNodes file: test/integration/scheduler_perf/node_util.go:85 returns_error: нет description: PrepareNodes prepares countToStrategy test nodes.


### PrepareNodes (test/integration/scheduler_perf/node_util.go:85)


PrepareNodes prepares countToStrategy test nodes.


```go
func (p *IntegrationTestNodePreparer) PrepareNodes((ctx context.Context, nextNodeIndex int)) (ctx context.Context, nextNodeIndex int)
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


**Тип ответа:** nextNodeIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/node_util.go:85`



---


[function] name: StaticNodeTemplate file: test/integration/scheduler_perf/node_util.go:56 returns_error: нет description: StaticNodeTemplate returns an implementation of NodeTemplate for a fixed node that is the same regardless of the index.


### StaticNodeTemplate (test/integration/scheduler_perf/node_util.go:56)


StaticNodeTemplate returns an implementation of NodeTemplate for a fixed node that is the same regardless of the index.


```go
func StaticNodeTemplate((node *v1.Node)) (node *v1.Node)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/scheduler_perf/node_util.go:56`



---


[function] name: waitListAllNodes file: test/integration/scheduler_perf/node_util.go:156 returns_error: да description: waitListAllNodes is a wrapper around listing nodes supporting retries.


### waitListAllNodes (test/integration/scheduler_perf/node_util.go:156)


waitListAllNodes is a wrapper around listing nodes supporting retries.


```go
func waitListAllNodes((*v1.NodeList, error)) (*v1.NodeList, error)
```


**Тип запроса:** v1.NodeList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.NodeList


```json
{
  "Items": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.NodeList`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/node_util.go:156`




## test/integration/scheduler_perf/operations.go


📄 Исходный файл: `test/integration/scheduler_perf/operations.go`


<details open>
<summary><b>Функции в этом файле (49)</b></summary>


- 🔗 [addFloat](#addfloat-testintegrationscheduler_perfoperationsgo679) `:679`

- 🔗 [addInt](#addint-testintegrationscheduler_perfoperationsgo663) `:663`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo70) `:70`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo214) `:214`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo252) `:252`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo341) `:341`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo394) `:394`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo441) `:441`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo488) `:488`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo529) `:529`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo555) `:555`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo594) `:594`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfoperationsgo614) `:614`

- 🔗 [create](#create-testintegrationscheduler_perfoperationsgo102) `:102`

- 🔗 [divideFloat](#dividefloat-testintegrationscheduler_perfoperationsgo701) `:701`

- 🔗 [divideInt](#divideint-testintegrationscheduler_perfoperationsgo675) `:675`

- 🔗 [getSpecFromTextTemplateFile](#getspecfromtexttemplatefile-testintegrationscheduler_perfoperationsgo153) `:153`

- 🔗 [getTemplateFuncs](#gettemplatefuncs-testintegrationscheduler_perfoperationsgo622) `:622`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo61) `:61`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo207) `:207`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo245) `:245`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo322) `:322`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo387) `:387`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo431) `:431`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo472) `:472`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo522) `:522`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo551) `:551`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo587) `:587`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfoperationsgo610) `:610`

- 🔗 [mod](#mod-testintegrationscheduler_perfoperationsgo710) `:710`

- 🔗 [multiplyFloat](#multiplyfloat-testintegrationscheduler_perfoperationsgo693) `:693`

- 🔗 [multiplyInt](#multiplyint-testintegrationscheduler_perfoperationsgo671) `:671`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo74) `:74`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo218) `:218`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo256) `:256`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo345) `:345`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo398) `:398`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo445) `:445`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo492) `:492`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo533) `:533`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo559) `:559`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo598) `:598`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfoperationsgo618) `:618`

- 🔗 [requiredNamespaces](#requirednamespaces-testintegrationscheduler_perfoperationsgo85) `:85`

- 🔗 [restMappingFromUnstructuredObj](#restmappingfromunstructuredobj-testintegrationscheduler_perfoperationsgo170) `:170`

- 🔗 [run](#run-testintegrationscheduler_perfoperationsgo92) `:92`

- 🔗 [subtractFloat](#subtractfloat-testintegrationscheduler_perfoperationsgo687) `:687`

- 🔗 [subtractInt](#subtractint-testintegrationscheduler_perfoperationsgo667) `:667`

- 🔗 [toFloat64](#tofloat64-testintegrationscheduler_perfoperationsgo636) `:636`


</details>


[function] name: addFloat file: test/integration/scheduler_perf/operations.go:679 returns_error: нет description: —


### addFloat (test/integration/scheduler_perf/operations.go:679)


addFloat is a function that performs operations based on the provided parameters and returns (numbers ...any).


```go
func addFloat((numbers ...any)) (numbers ...any)
```


**Тип ответа:** numbers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:679`



---


[function] name: addInt file: test/integration/scheduler_perf/operations.go:663 returns_error: нет description: —


### addInt (test/integration/scheduler_perf/operations.go:663)


addInt is a function that performs operations based on the provided parameters and returns (numbers ...any).


```go
func addInt((numbers ...any)) (numbers ...any)
```


**Тип ответа:** numbers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:663`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:70 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:70)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (c *createAny) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:70`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:214 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:214)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (*createNodesOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:214`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:252 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:252)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (*createNamespacesOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:252`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:341 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:341)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (cpo *createPodsOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:341`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:394 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:394)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (cpso *createPodSetsOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:394`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:441 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:441)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (dpo *deletePodsOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:441`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:488 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:488)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (*churnOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:488`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:529 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:529)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (*barrierOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:529`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:555 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:555)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (so *sleepOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:555`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:594 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:594)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (*startCollectingMetricsOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:594`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/operations.go:614 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/operations.go:614)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (*stopCollectingMetricsOp) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:614`



---


[function] name: create file: test/integration/scheduler_perf/operations.go:102 returns_error: нет description: —


### create (test/integration/scheduler_perf/operations.go:102)


create is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, env map[string]any).


```go
func (c *createAny) create((tCtx ktesting.TContext, env map[string]any)) (tCtx ktesting.TContext, env map[string]any)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** env


```json
{
  "callSiteName": "string",
  "readEnvVarsOnce": {},
  "known": {},
  "enabledViaEnvVar": {},
  "lockEnabledViaSetMethod": {},
  "enabledViaSetMethod": {},
  "readEnvVars": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/features/envvar.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:102`



---


[function] name: divideFloat file: test/integration/scheduler_perf/operations.go:701 returns_error: нет description: —


### divideFloat (test/integration/scheduler_perf/operations.go:701)


divideFloat is a function that performs operations based on the provided parameters and returns (i, j any).


```go
func divideFloat((i, j any)) (i, j any)
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


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:701`



---


[function] name: divideInt file: test/integration/scheduler_perf/operations.go:675 returns_error: нет description: —


### divideInt (test/integration/scheduler_perf/operations.go:675)


divideInt is a function that performs operations based on the provided parameters and returns (i, j any).


```go
func divideInt((i, j any)) (i, j any)
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


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:675`



---


[function] name: getSpecFromTextTemplateFile file: test/integration/scheduler_perf/operations.go:153 returns_error: нет description: —


### getSpecFromTextTemplateFile (test/integration/scheduler_perf/operations.go:153)


getSpecFromTextTemplateFile is a function that performs operations based on the provided parameters and returns (path string, env map[string]any, spec interface{}).


```go
func getSpecFromTextTemplateFile((path string, env map[string]any, spec interface{})) (path string, env map[string]any, spec interface{})
```


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


**Тип ответа:** env


```json
{
  "callSiteName": "string",
  "readEnvVarsOnce": {},
  "known": {},
  "enabledViaEnvVar": {},
  "lockEnabledViaSetMethod": {},
  "enabledViaSetMethod": {},
  "readEnvVars": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/features/envvar.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:153`



---


[function] name: getTemplateFuncs file: test/integration/scheduler_perf/operations.go:622 returns_error: нет description: —


### getTemplateFuncs (test/integration/scheduler_perf/operations.go:622)


getTemplateFuncs is a function that performs operations based on the provided parameters and returns ().


```go
func getTemplateFuncs(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:622`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:61 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:61)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (c *createAny) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:61`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:207 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:207)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (cno *createNodesOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:207`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:245 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:245)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (cmo *createNamespacesOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:245`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:322 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:322)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (cpo *createPodsOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:322`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:387 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:387)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (cpso *createPodSetsOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:387`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:431 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:431)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (dpo *deletePodsOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:431`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:472 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:472)


isValid is a method that performs operations based on the provided parameters and returns (_ bool).


```go
func (co *churnOp) isValid((_ bool)) (_ bool)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:472`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:522 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:522)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (bo *barrierOp) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:522`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:551 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:551)


isValid is a method that performs operations based on the provided parameters and returns (_ bool).


```go
func (so *sleepOp) isValid((_ bool)) (_ bool)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:551`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:587 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:587)


isValid is a method that performs operations based on the provided parameters and returns (_ bool).


```go
func (scm *startCollectingMetricsOp) isValid((_ bool)) (_ bool)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:587`



---


[function] name: isValid file: test/integration/scheduler_perf/operations.go:610 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/operations.go:610)


isValid is a method that performs operations based on the provided parameters and returns (_ bool).


```go
func (scm *stopCollectingMetricsOp) isValid((_ bool)) (_ bool)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:610`



---


[function] name: mod file: test/integration/scheduler_perf/operations.go:710 returns_error: нет description: —


### mod (test/integration/scheduler_perf/operations.go:710)


mod is a function that performs operations based on the provided parameters and returns (a, b any).


```go
func mod((a, b any)) (a, b any)
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


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:710`



---


[function] name: multiplyFloat file: test/integration/scheduler_perf/operations.go:693 returns_error: нет description: —


### multiplyFloat (test/integration/scheduler_perf/operations.go:693)


multiplyFloat is a function that performs operations based on the provided parameters and returns (numbers ...any).


```go
func multiplyFloat((numbers ...any)) (numbers ...any)
```


**Тип ответа:** numbers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:693`



---


[function] name: multiplyInt file: test/integration/scheduler_perf/operations.go:671 returns_error: нет description: —


### multiplyInt (test/integration/scheduler_perf/operations.go:671)


multiplyInt is a function that performs operations based on the provided parameters and returns (numbers ...any).


```go
func multiplyInt((numbers ...any)) (numbers ...any)
```


**Тип ответа:** numbers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:671`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:74 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:74)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (c createAny) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:74`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:218 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:218)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (cno createNodesOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:218`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:256 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:256)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (cmo createNamespacesOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:256`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:345 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:345)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (cpo createPodsOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:345`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:398 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:398)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (cpso createPodSetsOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:398`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:445 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:445)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (dpo deletePodsOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:445`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:492 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:492)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (co churnOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:492`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:533 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:533)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (bo barrierOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:533`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:559 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:559)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (so sleepOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:559`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:598 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:598)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (scm startCollectingMetricsOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:598`



---


[function] name: patchParams file: test/integration/scheduler_perf/operations.go:618 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/operations.go:618)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (scm stopCollectingMetricsOp) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:618`



---


[function] name: requiredNamespaces file: test/integration/scheduler_perf/operations.go:85 returns_error: нет description: —


### requiredNamespaces (test/integration/scheduler_perf/operations.go:85)


requiredNamespaces is a method that performs operations based on the provided parameters and returns ().


```go
func (c *createAny) requiredNamespaces(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:85`



---


[function] name: restMappingFromUnstructuredObj file: test/integration/scheduler_perf/operations.go:170 returns_error: да description: —


### restMappingFromUnstructuredObj (test/integration/scheduler_perf/operations.go:170)


restMappingFromUnstructuredObj is a function that performs operations based on the provided parameters and may return an error.


```go
func restMappingFromUnstructuredObj((*meta.RESTMapping, error)) (*meta.RESTMapping, error)
```


**Тип запроса:** meta.RESTMapping


```json
{
  "Resource": {},
  "GroupVersionKind": {},
  "Scope": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/meta/interfaces.go`


**Тип ответа:** meta.RESTMapping


```json
{
  "Resource": {},
  "GroupVersionKind": {},
  "Scope": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/meta/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*meta.RESTMapping`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:170`



---


[function] name: run file: test/integration/scheduler_perf/operations.go:92 returns_error: нет description: —


### run (test/integration/scheduler_perf/operations.go:92)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (c *createAny) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:92`



---


[function] name: subtractFloat file: test/integration/scheduler_perf/operations.go:687 returns_error: нет description: —


### subtractFloat (test/integration/scheduler_perf/operations.go:687)


subtractFloat is a function that performs operations based on the provided parameters and returns (i, j any).


```go
func subtractFloat((i, j any)) (i, j any)
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


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:687`



---


[function] name: subtractInt file: test/integration/scheduler_perf/operations.go:667 returns_error: нет description: —


### subtractInt (test/integration/scheduler_perf/operations.go:667)


subtractInt is a function that performs operations based on the provided parameters and returns (i, j any).


```go
func subtractInt((i, j any)) (i, j any)
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


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:667`



---


[function] name: toFloat64 file: test/integration/scheduler_perf/operations.go:636 returns_error: нет description: —


### toFloat64 (test/integration/scheduler_perf/operations.go:636)


toFloat64 is a function that performs operations based on the provided parameters and returns (val any).


```go
func toFloat64((val any)) (val any)
```


**Тип ответа:** val


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/admissionregistration/v1beta1/validatingwebhookconfiguration.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/operations.go:636`




## test/integration/scheduler_perf/options.go


📄 Исходный файл: `test/integration/scheduler_perf/options.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [WithPrepareFn](#withpreparefn-testintegrationscheduler_perfoptionsgo32) `:32`


</details>


[function] name: WithPrepareFn file: test/integration/scheduler_perf/options.go:32 returns_error: нет description: WithPrepareFn is the option to set a function that is called
before each workload is run. (e.g. applying CRDs for custom


### WithPrepareFn (test/integration/scheduler_perf/options.go:32)


WithPrepareFn is the option to set a function that is called
before each workload is run. (e.g. applying CRDs for custom plugins)


```go
func WithPrepareFn((prepareFn PrepareFn)) (prepareFn PrepareFn)
```


**Тип ответа:** prepareFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PrepareFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/options.go:32`




## test/integration/scheduler_perf/scheduler_perf.go


📄 Исходный файл: `test/integration/scheduler_perf/scheduler_perf.go`


<details open>
<summary><b>Функции в этом файле (35)</b></summary>


- 🔗 [Get](#get-testintegrationscheduler_perfscheduler_perfgo377) `:377`

- 🔗 [InitTests](#inittests-testintegrationscheduler_perfscheduler_perfgo199) `:199`

- 🔗 [RunBenchmarkPerfScheduling](#runbenchmarkperfscheduling-testintegrationscheduler_perfscheduler_perfgo763) `:763`

- 🔗 [RunIntegrationPerfScheduling](#runintegrationperfscheduling-testintegrationscheduler_perfscheduler_perfgo901) `:901`

- 🔗 [UnmarshalJSON](#unmarshaljson-testintegrationscheduler_perfscheduler_perfgo367) `:367`

- 🔗 [UnmarshalJSON](#unmarshaljson-testintegrationscheduler_perfscheduler_perfgo447) `:447`

- 🔗 [UnmarshalJSON](#unmarshaljson-testintegrationscheduler_perfscheduler_perfgo504) `:504`

- 🔗 [applyThreshold](#applythreshold-testintegrationscheduler_perfscheduler_perfgo1023) `:1023`

- 🔗 [checkEmptyInFlightEvents](#checkemptyinflightevents-testintegrationscheduler_perfscheduler_perfgo1051) `:1051`

- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfscheduler_perfgo281) `:281`

- 🔗 [featureGatesMerge](#featuregatesmerge-testintegrationscheduler_perfscheduler_perfgo725) `:725`

- 🔗 [fixJSONOutput](#fixjsonoutput-testintegrationscheduler_perfscheduler_perfgo740) `:740`

- 🔗 [get](#get-testintegrationscheduler_perfscheduler_perfgo460) `:460`

- 🔗 [getParam](#getparam-testintegrationscheduler_perfscheduler_perfgo472) `:472`

- 🔗 [getSpecFromFile](#getspecfromfile-testintegrationscheduler_perfscheduler_perfgo1139) `:1139`

- 🔗 [getTestCases](#gettestcases-testintegrationscheduler_perfscheduler_perfgo1147) `:1147`

- 🔗 [init](#init-testintegrationscheduler_perfscheduler_perfgo112) `:112`

- 🔗 [initTestOutput](#inittestoutput-testintegrationscheduler_perfscheduler_perfgo589) `:589`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfscheduler_perfgo334) `:334`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfscheduler_perfgo398) `:398`

- 🔗 [isValidCount](#isvalidcount-testintegrationscheduler_perfscheduler_perfgo581) `:581`

- 🔗 [isValidParameterizable](#isvalidparameterizable-testintegrationscheduler_perfscheduler_perfgo577) `:577`

- 🔗 [labelsMatch](#labelsmatch-testintegrationscheduler_perfscheduler_perfgo1004) `:1004`

- 🔗 [loadSchedulerConfig](#loadschedulerconfig-testintegrationscheduler_perfscheduler_perfgo950) `:950`

- 🔗 [registerQHintMetrics](#registerqhintmetrics-testintegrationscheduler_perfscheduler_perfgo235) `:235`

- 🔗 [runWorkload](#runworkload-testintegrationscheduler_perfscheduler_perfgo1065) `:1065`

- 🔗 [setDefaults](#setdefaults-testintegrationscheduler_perfscheduler_perfgo347) `:347`

- 🔗 [setupClusterForWorkload](#setupclusterforworkload-testintegrationscheduler_perfscheduler_perfgo989) `:989`

- 🔗 [setupTestCase](#setuptestcase-testintegrationscheduler_perfscheduler_perfgo622) `:622`

- 🔗 [unregisterQHintMetrics](#unregisterqhintmetrics-testintegrationscheduler_perfscheduler_perfgo241) `:241`

- 🔗 [unrollWorkloadTemplate](#unrollworkloadtemplate-testintegrationscheduler_perfscheduler_perfgo966) `:966`

- 🔗 [unusedParams](#unusedparams-testintegrationscheduler_perfscheduler_perfgo487) `:487`

- 🔗 [validateTestCases](#validatetestcases-testintegrationscheduler_perfscheduler_perfgo1160) `:1160`

- 🔗 [valueWithinThreshold](#valuewithinthreshold-testintegrationscheduler_perfscheduler_perfgo1014) `:1014`

- 🔗 [workloadNamesUnique](#workloadnamesunique-testintegrationscheduler_perfscheduler_perfgo290) `:290`


</details>


[function] name: Get file: test/integration/scheduler_perf/scheduler_perf.go:377 returns_error: нет description: —


### Get (test/integration/scheduler_perf/scheduler_perf.go:377)


Get is a method that retrieves data based on the provided parameters and returns (topicName string).


```go
func (t *thresholds) Get((topicName string)) (topicName string)
```


**Тип ответа:** topicName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:377`



---


[function] name: InitTests file: test/integration/scheduler_perf/scheduler_perf.go:199 returns_error: нет description: InitTests should be called in a TestMain in each config subdirectory.


### InitTests (test/integration/scheduler_perf/scheduler_perf.go:199)


InitTests should be called in a TestMain in each config subdirectory.


```go
func InitTests(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:199`



---


[function] name: RunBenchmarkPerfScheduling file: test/integration/scheduler_perf/scheduler_perf.go:763 returns_error: нет description: RunBenchmarkPerfScheduling runs the scheduler performance benchmark tests.

You can pass your own scheduler plugins via 


### RunBenchmarkPerfScheduling (test/integration/scheduler_perf/scheduler_perf.go:763)


RunBenchmarkPerfScheduling runs the scheduler performance benchmark tests.

You can pass your own scheduler plugins via outOfTreePluginRegistry.
Also, you may want to put your plugins in PluginNames variable in this package
to collect metrics for them.


```go
func RunBenchmarkPerfScheduling((b *testing.B, configFile string, topicName string, outOfTreePluginRegistry frameworkruntime.Registry, options ...SchedulerPerfOption)) (b *testing.B, configFile string, topicName string, outOfTreePluginRegistry frameworkruntime.Registry, options ...SchedulerPerfOption)
```


**Тип запроса:** testing.B


```json
{
  "GroupVersion": {},
  "userSupplied": false
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/configset.go`


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** testing.B


```json
{
  "GroupVersion": {},
  "userSupplied": false
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/configset.go`


**Тип ответа:** configFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** topicName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** outOfTreePluginRegistry


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** frameworkruntime.Registry


```json
{
  "Username": "string",
  "Password": "string",
  "Email": "string"
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/credentialconfig/registry.go`


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


**Тип ответа:** SchedulerPerfOption


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:763`



---


[function] name: RunIntegrationPerfScheduling file: test/integration/scheduler_perf/scheduler_perf.go:901 returns_error: нет description: RunIntegrationPerfScheduling runs the scheduler performance integration tests.


### RunIntegrationPerfScheduling (test/integration/scheduler_perf/scheduler_perf.go:901)


RunIntegrationPerfScheduling runs the scheduler performance integration tests.


```go
func RunIntegrationPerfScheduling((t *testing.T, configFile string)) (t *testing.T, configFile string)
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


**Тип ответа:** configFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:901`



---


[function] name: UnmarshalJSON file: test/integration/scheduler_perf/scheduler_perf.go:367 returns_error: нет description: —


### UnmarshalJSON (test/integration/scheduler_perf/scheduler_perf.go:367)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (t *thresholds) UnmarshalJSON((text []byte)) (text []byte)
```


**Тип ответа:** text


```json
{
  "ClientBuilder": {},
  "InformerFactory": {},
  "ObjectOrMetadataInformerFactory": {},
  "RESTMapper": null,
  "Stop": {},
  "InformersStarted": {},
  "ResyncPeriod": {},
  "ControllerManagerMetrics": null
}
```


*Определено в:* `staging/src/k8s.io/controller-manager/app/controllercontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:367`



---


[function] name: UnmarshalJSON file: test/integration/scheduler_perf/scheduler_perf.go:447 returns_error: нет description: UnmarshalJSON is a custom unmarshaler for params.

from(json):

{
"initNodes": 500,
"initPods": 50
}

to:

params{
param


### UnmarshalJSON (test/integration/scheduler_perf/scheduler_perf.go:447)


UnmarshalJSON is a custom unmarshaler for params.

from(json):

{
"initNodes": 500,
"initPods": 50
}

to:

params{
params: map[string]any{
"intNodes": 500,
"initPods": 50,
},
isUsed: map[string]bool{}, // empty map
}


```go
func (p *params) UnmarshalJSON((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:447`



---


[function] name: UnmarshalJSON file: test/integration/scheduler_perf/scheduler_perf.go:504 returns_error: нет description: UnmarshalJSON is a custom unmarshaler for the op struct since we don't know
which op we're decoding at runtime.


### UnmarshalJSON (test/integration/scheduler_perf/scheduler_perf.go:504)


UnmarshalJSON is a custom unmarshaler for the op struct since we don't know
which op we're decoding at runtime.


```go
func (op *op) UnmarshalJSON((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:504`



---


[function] name: applyThreshold file: test/integration/scheduler_perf/scheduler_perf.go:1023 returns_error: нет description: applyThreshold adds the threshold to data item with metric specified via metricSelector and verifies that
this metrics v


### applyThreshold (test/integration/scheduler_perf/scheduler_perf.go:1023)


applyThreshold adds the threshold to data item with metric specified via metricSelector and verifies that
this metrics value is within threshold.


```go
func applyThreshold((items []DataItem, threshold float64, metricSelector thresholdMetricSelector)) (items []DataItem, threshold float64, metricSelector thresholdMetricSelector)
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


**Тип ответа:** DataItem


```json
{
  "Data": {},
  "Unit": "string",
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


**Тип ответа:** threshold


```json
{
  "value": 0.0,
  "valuesByTopic": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** metricSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** thresholdMetricSelector


```json
{
  "Name": "string",
  "Labels": {},
  "DataBucket": "string",
  "ExpectLower": false
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1023`



---


[function] name: checkEmptyInFlightEvents file: test/integration/scheduler_perf/scheduler_perf.go:1051 returns_error: нет description: —


### checkEmptyInFlightEvents (test/integration/scheduler_perf/scheduler_perf.go:1051)


checkEmptyInFlightEvents is a function that performs operations based on the provided parameters and returns ().


```go
func checkEmptyInFlightEvents(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1051`



---


[function] name: collectsMetrics file: test/integration/scheduler_perf/scheduler_perf.go:281 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/scheduler_perf.go:281)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (tc *testCase) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:281`



---


[function] name: featureGatesMerge file: test/integration/scheduler_perf/scheduler_perf.go:725 returns_error: нет description: —


### featureGatesMerge (test/integration/scheduler_perf/scheduler_perf.go:725)


featureGatesMerge is a function that performs operations based on the provided parameters and returns (src map[featuregate.Feature]bool, overrides map[featuregate.Feature]bool).


```go
func featureGatesMerge((src map[featuregate.Feature]bool, overrides map[featuregate.Feature]bool)) (src map[featuregate.Feature]bool, overrides map[featuregate.Feature]bool)
```


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** featuregate.Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


**Тип ответа:** overrides


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** featuregate.Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:725`



---


[function] name: fixJSONOutput file: test/integration/scheduler_perf/scheduler_perf.go:740 returns_error: нет description: fixJSONOutput works around Go not emitting a "pass" action for
sub-benchmarks
(https://github.com/golang/go/issues/66825


### fixJSONOutput (test/integration/scheduler_perf/scheduler_perf.go:740)


fixJSONOutput works around Go not emitting a "pass" action for
sub-benchmarks
(https://github.com/golang/go/issues/66825#issuecomment-2343229005), which
causes gotestsum to report a successful benchmark run as failed
(https://github.com/gotestyourself/gotestsum/issues/413#issuecomment-2343206787).

It does this by printing the missing "PASS" output line that test2json
then converts into the "pass" action.


```go
func fixJSONOutput((b *testing.B)) (b *testing.B)
```


**Тип запроса:** testing.B


```json
{
  "GroupVersion": {},
  "userSupplied": false
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/configset.go`


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** testing.B


```json
{
  "GroupVersion": {},
  "userSupplied": false
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/configset.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:740`



---


[function] name: get file: test/integration/scheduler_perf/scheduler_perf.go:460 returns_error: да description: get retrieves the parameter as an integer


### get (test/integration/scheduler_perf/scheduler_perf.go:460)


get retrieves the parameter as an integer


```go
func (p params) get((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:460`



---


[function] name: getParam file: test/integration/scheduler_perf/scheduler_perf.go:472 returns_error: да description: getParam retrieves the parameter as specific type. There is no conversion,
so in practice this means that only types tha


### getParam (test/integration/scheduler_perf/scheduler_perf.go:472)


getParam retrieves the parameter as specific type. There is no conversion,
so in practice this means that only types that JSON unmarshalling uses
(float64, string, bool) work.


```go
func getParam((T, error)) (T, error)
```


**Тип ответа:** T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `T`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:472`



---


[function] name: getSpecFromFile file: test/integration/scheduler_perf/scheduler_perf.go:1139 returns_error: нет description: —


### getSpecFromFile (test/integration/scheduler_perf/scheduler_perf.go:1139)


getSpecFromFile is a function that performs operations based on the provided parameters and returns (path *string, spec interface{}).


```go
func getSpecFromFile((path *string, spec interface{})) (path *string, spec interface{})
```


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


**Тип ответа:** spec


```json
{
  "Version": "string",
  "Kind": "string",
  "Devices": []
}
```


*Определено в:* `test/e2e/dra/test-driver/app/cdi.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1139`



---


[function] name: getTestCases file: test/integration/scheduler_perf/scheduler_perf.go:1147 returns_error: да description: —


### getTestCases (test/integration/scheduler_perf/scheduler_perf.go:1147)


getTestCases is a function that performs operations based on the provided parameters and may return an error.


```go
func getTestCases(([]*testCase, error)) ([]*testCase, error)
```


**Тип запроса:** testCase


```json
{
  "name": "string",
  "podResources": null,
  "containers": [],
  "expected": {},
  "expectedPodLevelResourcesOverride": null
}
```


*Определено в:* `test/e2e/common/node/pod_level_resources.go`


**Тип ответа:** testCase


```json
{
  "name": "string",
  "podResources": null,
  "containers": [],
  "expected": {},
  "expectedPodLevelResourcesOverride": null
}
```


*Определено в:* `test/e2e/common/node/pod_level_resources.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*testCase`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1147`



---


[function] name: init file: test/integration/scheduler_perf/scheduler_perf.go:112 returns_error: нет description: —


### init (test/integration/scheduler_perf/scheduler_perf.go:112)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:112`



---


[function] name: initTestOutput file: test/integration/scheduler_perf/scheduler_perf.go:589 returns_error: нет description: —


### initTestOutput (test/integration/scheduler_perf/scheduler_perf.go:589)


initTestOutput is a function that performs operations based on the provided parameters and returns (tb testing.TB).


```go
func initTestOutput((tb testing.TB)) (tb testing.TB)
```


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** testing.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:589`



---


[function] name: isValid file: test/integration/scheduler_perf/scheduler_perf.go:334 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/scheduler_perf.go:334)


isValid is a method that performs operations based on the provided parameters and returns (mcc *metricsCollectorConfig).


```go
func (w *workload) isValid((mcc *metricsCollectorConfig)) (mcc *metricsCollectorConfig)
```


**Тип запроса:** metricsCollectorConfig


```json
{
  "Metrics": {}
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


**Тип ответа:** mcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metricsCollectorConfig


```json
{
  "Metrics": {}
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:334`



---


[function] name: isValid file: test/integration/scheduler_perf/scheduler_perf.go:398 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/scheduler_perf.go:398)


isValid is a method that performs operations based on the provided parameters and returns (mcc *metricsCollectorConfig).


```go
func (ms thresholdMetricSelector) isValid((mcc *metricsCollectorConfig)) (mcc *metricsCollectorConfig)
```


**Тип запроса:** metricsCollectorConfig


```json
{
  "Metrics": {}
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


**Тип ответа:** mcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metricsCollectorConfig


```json
{
  "Metrics": {}
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:398`



---


[function] name: isValidCount file: test/integration/scheduler_perf/scheduler_perf.go:581 returns_error: нет description: —


### isValidCount (test/integration/scheduler_perf/scheduler_perf.go:581)


isValidCount is a function that performs operations based on the provided parameters and returns (allowParameterization bool, count int, countParam string).


```go
func isValidCount((allowParameterization bool, count int, countParam string)) (allowParameterization bool, count int, countParam string)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** count


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** countParam


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:581`



---


[function] name: isValidParameterizable file: test/integration/scheduler_perf/scheduler_perf.go:577 returns_error: нет description: —


### isValidParameterizable (test/integration/scheduler_perf/scheduler_perf.go:577)


isValidParameterizable is a function that performs operations based on the provided parameters and returns (val string).


```go
func isValidParameterizable((val string)) (val string)
```


**Тип ответа:** val


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/admissionregistration/v1beta1/validatingwebhookconfiguration.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:577`



---


[function] name: labelsMatch file: test/integration/scheduler_perf/scheduler_perf.go:1004 returns_error: нет description: —


### labelsMatch (test/integration/scheduler_perf/scheduler_perf.go:1004)


labelsMatch is a function that performs operations based on the provided parameters and returns (actualLabels, requiredLabels map[string]string).


```go
func labelsMatch((actualLabels, requiredLabels map[string]string)) (actualLabels, requiredLabels map[string]string)
```


**Тип ответа:** actualLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** requiredLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1004`



---


[function] name: loadSchedulerConfig file: test/integration/scheduler_perf/scheduler_perf.go:950 returns_error: да description: —


### loadSchedulerConfig (test/integration/scheduler_perf/scheduler_perf.go:950)


loadSchedulerConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func loadSchedulerConfig((*config.KubeSchedulerConfiguration, error)) (*config.KubeSchedulerConfiguration, error)
```


**Тип запроса:** config.KubeSchedulerConfiguration


```json
{
  "Parallelism": 0,
  "LeaderElection": {},
  "ClientConnection": {},
  "PercentageOfNodesToScore": 0,
  "PodInitialBackoffSeconds": 0,
  "PodMaxBackoffSeconds": 0,
  "Profiles": [],
  "Extenders": [],
  "DelayCacheUntilActive": false
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


**Тип ответа:** config.KubeSchedulerConfiguration


```json
{
  "Parallelism": 0,
  "LeaderElection": {},
  "ClientConnection": {},
  "PercentageOfNodesToScore": 0,
  "PodInitialBackoffSeconds": 0,
  "PodMaxBackoffSeconds": 0,
  "Profiles": [],
  "Extenders": [],
  "DelayCacheUntilActive": false
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*config.KubeSchedulerConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:950`



---


[function] name: registerQHintMetrics file: test/integration/scheduler_perf/scheduler_perf.go:235 returns_error: нет description: —


### registerQHintMetrics (test/integration/scheduler_perf/scheduler_perf.go:235)


registerQHintMetrics is a function that performs operations based on the provided parameters and returns ().


```go
func registerQHintMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:235`



---


[function] name: runWorkload file: test/integration/scheduler_perf/scheduler_perf.go:1065 returns_error: да description: —


### runWorkload (test/integration/scheduler_perf/scheduler_perf.go:1065)


runWorkload is a function that performs operations based on the provided parameters and may return an error.


```go
func runWorkload(([]DataItem, error)) ([]DataItem, error)
```


**Тип ответа:** DataItem


```json
{
  "Data": {},
  "Unit": "string",
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]DataItem`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1065`



---


[function] name: setDefaults file: test/integration/scheduler_perf/scheduler_perf.go:347 returns_error: нет description: —


### setDefaults (test/integration/scheduler_perf/scheduler_perf.go:347)


setDefaults is a method that performs operations based on the provided parameters and returns (testCaseThresholdMetricSelector *thresholdMetricSelector).


```go
func (w *workload) setDefaults((testCaseThresholdMetricSelector *thresholdMetricSelector)) (testCaseThresholdMetricSelector *thresholdMetricSelector)
```


**Тип запроса:** thresholdMetricSelector


```json
{
  "Name": "string",
  "Labels": {},
  "DataBucket": "string",
  "ExpectLower": false
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** testCaseThresholdMetricSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** thresholdMetricSelector


```json
{
  "Name": "string",
  "Labels": {},
  "DataBucket": "string",
  "ExpectLower": false
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:347`



---


[function] name: setupClusterForWorkload file: test/integration/scheduler_perf/scheduler_perf.go:989 returns_error: нет description: —


### setupClusterForWorkload (test/integration/scheduler_perf/scheduler_perf.go:989)


setupClusterForWorkload is a function that performs operations based on the provided parameters and returns (*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext).


```go
func setupClusterForWorkload((*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext)) (*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext)
```


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


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


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:989`



---


[function] name: setupTestCase file: test/integration/scheduler_perf/scheduler_perf.go:622 returns_error: нет description: —


### setupTestCase (test/integration/scheduler_perf/scheduler_perf.go:622)


setupTestCase is a function that performs operations based on the provided parameters and returns (*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext).


```go
func setupTestCase((*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext)) (*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext)
```


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


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


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:622`



---


[function] name: unregisterQHintMetrics file: test/integration/scheduler_perf/scheduler_perf.go:241 returns_error: нет description: —


### unregisterQHintMetrics (test/integration/scheduler_perf/scheduler_perf.go:241)


unregisterQHintMetrics is a function that performs operations based on the provided parameters and returns ().


```go
func unregisterQHintMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:241`



---


[function] name: unrollWorkloadTemplate file: test/integration/scheduler_perf/scheduler_perf.go:966 returns_error: нет description: —


### unrollWorkloadTemplate (test/integration/scheduler_perf/scheduler_perf.go:966)


unrollWorkloadTemplate is a function that performs operations based on the provided parameters and returns (tb ktesting.TB, wt []op, w *workload).


```go
func unrollWorkloadTemplate((tb ktesting.TB, wt []op, w *workload)) (tb ktesting.TB, wt []op, w *workload)
```


**Тип запроса:** workload


```json
{
  "Name": "string",
  "Params": {},
  "Labels": [],
  "Threshold": {},
  "ThresholdMetricSelector": null,
  "FeatureGates": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** ktesting.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** wt


```json
{
  "jwtAuthenticator": {},
  "verifier": {},
  "resolver": null,
  "celMapper": {},
  "requiredClaims": {},
  "healthCheck": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** w


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


**Тип ответа:** workload


```json
{
  "Name": "string",
  "Params": {},
  "Labels": [],
  "Threshold": {},
  "ThresholdMetricSelector": null,
  "FeatureGates": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:966`



---


[function] name: unusedParams file: test/integration/scheduler_perf/scheduler_perf.go:487 returns_error: нет description: unusedParams returns the names of unusedParams


### unusedParams (test/integration/scheduler_perf/scheduler_perf.go:487)


unusedParams returns the names of unusedParams


```go
func (w workload) unusedParams(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:487`



---


[function] name: validateTestCases file: test/integration/scheduler_perf/scheduler_perf.go:1160 returns_error: нет description: —


### validateTestCases (test/integration/scheduler_perf/scheduler_perf.go:1160)


validateTestCases is a function that performs operations based on the provided parameters and returns (testCases []*testCase).


```go
func validateTestCases((testCases []*testCase)) (testCases []*testCase)
```


**Тип запроса:** testCase


```json
{
  "name": "string",
  "podResources": null,
  "containers": [],
  "expected": {},
  "expectedPodLevelResourcesOverride": null
}
```


*Определено в:* `test/e2e/common/node/pod_level_resources.go`


**Тип ответа:** testCases


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** testCase


```json
{
  "name": "string",
  "podResources": null,
  "containers": [],
  "expected": {},
  "expectedPodLevelResourcesOverride": null
}
```


*Определено в:* `test/e2e/common/node/pod_level_resources.go`


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1160`



---


[function] name: valueWithinThreshold file: test/integration/scheduler_perf/scheduler_perf.go:1014 returns_error: нет description: —


### valueWithinThreshold (test/integration/scheduler_perf/scheduler_perf.go:1014)


valueWithinThreshold is a function that performs operations based on the provided parameters and returns (value, threshold float64, expectLower bool).


```go
func valueWithinThreshold((value, threshold float64, expectLower bool)) (value, threshold float64, expectLower bool)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


**Тип ответа:** threshold


```json
{
  "value": 0.0,
  "valuesByTopic": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** expectLower


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:1014`



---


[function] name: workloadNamesUnique file: test/integration/scheduler_perf/scheduler_perf.go:290 returns_error: нет description: —


### workloadNamesUnique (test/integration/scheduler_perf/scheduler_perf.go:290)


workloadNamesUnique is a method that performs operations based on the provided parameters and returns ().


```go
func (tc *testCase) workloadNamesUnique(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/scheduler_perf.go:290`




## test/integration/scheduler_perf/update.go


📄 Исходный файл: `test/integration/scheduler_perf/update.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [collectsMetrics](#collectsmetrics-testintegrationscheduler_perfupdatego72) `:72`

- 🔗 [isValid](#isvalid-testintegrationscheduler_perfupdatego60) `:60`

- 🔗 [patchParams](#patchparams-testintegrationscheduler_perfupdatego76) `:76`

- 🔗 [requiredNamespaces](#requirednamespaces-testintegrationscheduler_perfupdatego88) `:88`

- 🔗 [run](#run-testintegrationscheduler_perfupdatego95) `:95`

- 🔗 [update](#update-testintegrationscheduler_perfupdatego126) `:126`


</details>


[function] name: collectsMetrics file: test/integration/scheduler_perf/update.go:72 returns_error: нет description: —


### collectsMetrics (test/integration/scheduler_perf/update.go:72)


collectsMetrics is a method that performs operations based on the provided parameters and returns ().


```go
func (c *updateAny) collectsMetrics(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/update.go:72`



---


[function] name: isValid file: test/integration/scheduler_perf/update.go:60 returns_error: нет description: —


### isValid (test/integration/scheduler_perf/update.go:60)


isValid is a method that performs operations based on the provided parameters and returns (allowParameterization bool).


```go
func (c *updateAny) isValid((allowParameterization bool)) (allowParameterization bool)
```


**Тип ответа:** allowParameterization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/update.go:60`



---


[function] name: patchParams file: test/integration/scheduler_perf/update.go:76 returns_error: да description: —


### patchParams (test/integration/scheduler_perf/update.go:76)


patchParams is a method that performs operations based on the provided parameters and may return an error.


```go
func (c updateAny) patchParams((realOp, error)) (realOp, error)
```


**Тип ответа:** realOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `realOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/update.go:76`



---


[function] name: requiredNamespaces file: test/integration/scheduler_perf/update.go:88 returns_error: нет description: —


### requiredNamespaces (test/integration/scheduler_perf/update.go:88)


requiredNamespaces is a method that performs operations based on the provided parameters and returns ().


```go
func (c *updateAny) requiredNamespaces(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/update.go:88`



---


[function] name: run file: test/integration/scheduler_perf/update.go:95 returns_error: нет description: —


### run (test/integration/scheduler_perf/update.go:95)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (c *updateAny) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/update.go:95`



---


[function] name: update file: test/integration/scheduler_perf/update.go:126 returns_error: нет description: —


### update (test/integration/scheduler_perf/update.go:126)


update is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, env map[string]any).


```go
func (c *updateAny) update((tCtx ktesting.TContext, env map[string]any)) (tCtx ktesting.TContext, env map[string]any)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


**Тип ответа:** env


```json
{
  "callSiteName": "string",
  "readEnvVarsOnce": {},
  "known": {},
  "enabledViaEnvVar": {},
  "lockEnabledViaSetMethod": {},
  "enabledViaSetMethod": {},
  "readEnvVars": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/features/envvar.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/update.go:126`




## test/integration/scheduler_perf/util.go


📄 Исходный файл: `test/integration/scheduler_perf/util.go`


<details open>
<summary><b>Функции в этом файле (28)</b></summary>


- 🔗 [collect](#collect-testintegrationscheduler_perfutilgo362) `:362`

- 🔗 [collect](#collect-testintegrationscheduler_perfutilgo632) `:632`

- 🔗 [collect](#collect-testintegrationscheduler_perfutilgo744) `:744`

- 🔗 [collect](#collect-testintegrationscheduler_perfutilgo806) `:806`

- 🔗 [collectHistogramVec](#collecthistogramvec-testintegrationscheduler_perfutilgo409) `:409`

- 🔗 [collectSample](#collectsample-testintegrationscheduler_perfutilgo705) `:705`

- 🔗 [createMetricDataItem](#createmetricdataitem-testintegrationscheduler_perfutilgo719) `:719`

- 🔗 [dataFilename](#datafilename-testintegrationscheduler_perfutilgo307) `:307`

- 🔗 [dataItems2JSONFile](#dataitems2jsonfile-testintegrationscheduler_perfutilgo265) `:265`

- 🔗 [getScheduledPods](#getscheduledpods-testintegrationscheduler_perfutilgo173) `:173`

- 🔗 [init](#init-testintegrationscheduler_perfutilgo343) `:343`

- 🔗 [init](#init-testintegrationscheduler_perfutilgo479) `:479`

- 🔗 [init](#init-testintegrationscheduler_perfutilgo686) `:686`

- 🔗 [init](#init-testintegrationscheduler_perfutilgo795) `:795`

- 🔗 [isAttempted](#isattempted-testintegrationscheduler_perfutilgo160) `:160`

- 🔗 [makeBaseNode](#makebasenode-testintegrationscheduler_perfutilgo240) `:240`

- 🔗 [makeBasePod](#makebasepod-testintegrationscheduler_perfutilgo229) `:229`

- 🔗 [mustSetupCluster](#mustsetupcluster-testintegrationscheduler_perfutilgo95) `:95`

- 🔗 [newDefaultComponentConfig](#newdefaultcomponentconfig-testintegrationscheduler_perfutilgo76) `:76`

- 🔗 [newMemoryCollector](#newmemorycollector-testintegrationscheduler_perfutilgo679) `:679`

- 🔗 [newMetricsCollector](#newmetricscollector-testintegrationscheduler_perfutilgo336) `:336`

- 🔗 [newSchedulingDurationCollector](#newschedulingdurationcollector-testintegrationscheduler_perfutilgo789) `:789`

- 🔗 [newThroughputCollector](#newthroughputcollector-testintegrationscheduler_perfutilgo469) `:469`

- 🔗 [run](#run-testintegrationscheduler_perfutilgo358) `:358`

- 🔗 [run](#run-testintegrationscheduler_perfutilgo483) `:483`

- 🔗 [run](#run-testintegrationscheduler_perfutilgo691) `:691`

- 🔗 [run](#run-testintegrationscheduler_perfutilgo799) `:799`

- 🔗 [uniqueLVCombos](#uniquelvcombos-testintegrationscheduler_perfutilgo386) `:386`


</details>


[function] name: collect file: test/integration/scheduler_perf/util.go:362 returns_error: нет description: —


### collect (test/integration/scheduler_perf/util.go:362)


collect is a method that performs operations based on the provided parameters and returns ().


```go
func (mc *metricsCollector) collect(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:362`



---


[function] name: collect file: test/integration/scheduler_perf/util.go:632 returns_error: нет description: —


### collect (test/integration/scheduler_perf/util.go:632)


collect is a method that performs operations based on the provided parameters and returns ().


```go
func (tc *throughputCollector) collect(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:632`



---


[function] name: collect file: test/integration/scheduler_perf/util.go:744 returns_error: нет description: —


### collect (test/integration/scheduler_perf/util.go:744)


collect is a method that performs operations based on the provided parameters and returns ().


```go
func (mc *memoryCollector) collect(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:744`



---


[function] name: collect file: test/integration/scheduler_perf/util.go:806 returns_error: нет description: —


### collect (test/integration/scheduler_perf/util.go:806)


collect is a method that performs operations based on the provided parameters and returns ().


```go
func (sdc *schedulingDurationCollector) collect(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:806`



---


[function] name: collectHistogramVec file: test/integration/scheduler_perf/util.go:409 returns_error: нет description: —


### collectHistogramVec (test/integration/scheduler_perf/util.go:409)


collectHistogramVec is a function that performs operations based on the provided parameters and returns (metric string, labels map[string]string, lvMap map[string]string).


```go
func collectHistogramVec((metric string, labels map[string]string, lvMap map[string]string)) (metric string, labels map[string]string, lvMap map[string]string)
```


**Тип ответа:** metric


```json
{
  "base": {},
  "jwksURL": "string",
  "jwtIssuer": "string",
  "apiServerID": "string",
  "shouldRecordFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** lvMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:409`



---


[function] name: collectSample file: test/integration/scheduler_perf/util.go:705 returns_error: нет description: —


### collectSample (test/integration/scheduler_perf/util.go:705)


collectSample is a method that performs operations based on the provided parameters and returns ().


```go
func (mc *memoryCollector) collectSample(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:705`



---


[function] name: createMetricDataItem file: test/integration/scheduler_perf/util.go:719 returns_error: нет description: —


### createMetricDataItem (test/integration/scheduler_perf/util.go:719)


createMetricDataItem is a method that performs operations based on the provided parameters and returns (values []float64, unit, metricName string).


```go
func (mc *memoryCollector) createMetricDataItem((values []float64, unit, metricName string)) (values []float64, unit, metricName string)
```


**Тип ответа:** values


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** unit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metricName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/util.go:719`



---


[function] name: dataFilename file: test/integration/scheduler_perf/util.go:307 returns_error: да description: —


### dataFilename (test/integration/scheduler_perf/util.go:307)


dataFilename is a function that performs operations based on the provided parameters and may return an error.


```go
func dataFilename((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/util.go:307`



---


[function] name: dataItems2JSONFile file: test/integration/scheduler_perf/util.go:265 returns_error: нет description: —


### dataItems2JSONFile (test/integration/scheduler_perf/util.go:265)


dataItems2JSONFile is a function that performs operations based on the provided parameters and returns (dataItems DataItems, namePrefix string).


```go
func dataItems2JSONFile((dataItems DataItems, namePrefix string)) (dataItems DataItems, namePrefix string)
```


**Тип ответа:** dataItems


```json
{
  "Key": "string",
  "Value": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Тип ответа:** DataItems


```json
{
  "Version": "string",
  "DataItems": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


**Тип ответа:** namePrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/util.go:265`



---


[function] name: getScheduledPods file: test/integration/scheduler_perf/util.go:173 returns_error: да description: getScheduledPods returns the list of scheduled, attempted but unschedulable
and unattempted pods in the specified namesp


### getScheduledPods (test/integration/scheduler_perf/util.go:173)


getScheduledPods returns the list of scheduled, attempted but unschedulable
and unattempted pods in the specified namespaces.
Label selector can be used to filter the pods.
Note that no namespaces specified matches all namespaces.


```go
func getScheduledPods(([]*v1.Pod, []*v1.Pod, []*v1.Pod, error)) ([]*v1.Pod, []*v1.Pod, []*v1.Pod, error)
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


*Типы возврата:* `[]*v1.Pod`, `[]*v1.Pod`, `[]*v1.Pod`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/util.go:173`



---


[function] name: init file: test/integration/scheduler_perf/util.go:343 returns_error: нет description: —


### init (test/integration/scheduler_perf/util.go:343)


init is a method that performs operations based on the provided parameters and returns ().


```go
func (mc *metricsCollector) init(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:343`



---


[function] name: init file: test/integration/scheduler_perf/util.go:479 returns_error: нет description: —


### init (test/integration/scheduler_perf/util.go:479)


init is a method that performs operations based on the provided parameters and returns ().


```go
func (tc *throughputCollector) init(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:479`



---


[function] name: init file: test/integration/scheduler_perf/util.go:686 returns_error: нет description: —


### init (test/integration/scheduler_perf/util.go:686)


init is a method that performs operations based on the provided parameters and returns ().


```go
func (mc *memoryCollector) init(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:686`



---


[function] name: init file: test/integration/scheduler_perf/util.go:795 returns_error: нет description: —


### init (test/integration/scheduler_perf/util.go:795)


init is a method that performs operations based on the provided parameters and returns ().


```go
func (sdc *schedulingDurationCollector) init(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:795`



---


[function] name: isAttempted file: test/integration/scheduler_perf/util.go:160 returns_error: нет description: —


### isAttempted (test/integration/scheduler_perf/util.go:160)


isAttempted is a function that performs operations based on the provided parameters and returns (pod *v1.Pod).


```go
func isAttempted((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `test/integration/scheduler_perf/util.go:160`



---


[function] name: makeBaseNode file: test/integration/scheduler_perf/util.go:240 returns_error: нет description: makeBaseNode creates a Node object with given nodeNamePrefix to be used as a template.


### makeBaseNode (test/integration/scheduler_perf/util.go:240)


makeBaseNode creates a Node object with given nodeNamePrefix to be used as a template.


```go
func makeBaseNode((nodeNamePrefix string)) (nodeNamePrefix string)
```


**Тип ответа:** nodeNamePrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/util.go:240`



---


[function] name: makeBasePod file: test/integration/scheduler_perf/util.go:229 returns_error: нет description: makeBasePod creates a Pod object to be used as a template.


### makeBasePod (test/integration/scheduler_perf/util.go:229)


makeBasePod creates a Pod object to be used as a template.


```go
func makeBasePod(()) ()
```


📍 *Расположение:* `test/integration/scheduler_perf/util.go:229`



---


[function] name: mustSetupCluster file: test/integration/scheduler_perf/util.go:95 returns_error: нет description: mustSetupCluster starts the following components:
- k8s api server
- scheduler
- some of the kube-controller-manager con


### mustSetupCluster (test/integration/scheduler_perf/util.go:95)


mustSetupCluster starts the following components:
- k8s api server
- scheduler
- some of the kube-controller-manager controllers

It returns regular and dynamic clients, and destroyFunc which should be used to
remove resources after finished.
Notes on rate limiter:
- client rate limit is set to 5000.


```go
func mustSetupCluster((*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext)) (*scheduler.Scheduler, informers.SharedInformerFactory, ktesting.TContext)
```


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


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


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:95`



---


[function] name: newDefaultComponentConfig file: test/integration/scheduler_perf/util.go:76 returns_error: да description: —


### newDefaultComponentConfig (test/integration/scheduler_perf/util.go:76)


newDefaultComponentConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func newDefaultComponentConfig((*config.KubeSchedulerConfiguration, error)) (*config.KubeSchedulerConfiguration, error)
```


**Тип запроса:** config.KubeSchedulerConfiguration


```json
{
  "Parallelism": 0,
  "LeaderElection": {},
  "ClientConnection": {},
  "PercentageOfNodesToScore": 0,
  "PodInitialBackoffSeconds": 0,
  "PodMaxBackoffSeconds": 0,
  "Profiles": [],
  "Extenders": [],
  "DelayCacheUntilActive": false
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


**Тип ответа:** config.KubeSchedulerConfiguration


```json
{
  "Parallelism": 0,
  "LeaderElection": {},
  "ClientConnection": {},
  "PercentageOfNodesToScore": 0,
  "PodInitialBackoffSeconds": 0,
  "PodMaxBackoffSeconds": 0,
  "Profiles": [],
  "Extenders": [],
  "DelayCacheUntilActive": false
}
```


*Определено в:* `pkg/scheduler/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*config.KubeSchedulerConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/scheduler_perf/util.go:76`



---


[function] name: newMemoryCollector file: test/integration/scheduler_perf/util.go:679 returns_error: нет description: —


### newMemoryCollector (test/integration/scheduler_perf/util.go:679)


newMemoryCollector is a function that performs operations based on the provided parameters and returns (resultLabels map[string]string, interval time.Duration).


```go
func newMemoryCollector((resultLabels map[string]string, interval time.Duration)) (resultLabels map[string]string, interval time.Duration)
```


**Тип ответа:** resultLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** interval


```json
{
  "First": 0,
  "Last": 0
}
```


*Определено в:* `pkg/controller/job/indexed_job_utils.go`


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


📍 *Расположение:* `test/integration/scheduler_perf/util.go:679`



---


[function] name: newMetricsCollector file: test/integration/scheduler_perf/util.go:336 returns_error: нет description: —


### newMetricsCollector (test/integration/scheduler_perf/util.go:336)


newMetricsCollector is a function that performs operations based on the provided parameters and returns (config *metricsCollectorConfig, labels map[string]string).


```go
func newMetricsCollector((config *metricsCollectorConfig, labels map[string]string)) (config *metricsCollectorConfig, labels map[string]string)
```


**Тип запроса:** metricsCollectorConfig


```json
{
  "Metrics": {}
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** metricsCollectorConfig


```json
{
  "Metrics": {}
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:336`



---


[function] name: newSchedulingDurationCollector file: test/integration/scheduler_perf/util.go:789 returns_error: нет description: —


### newSchedulingDurationCollector (test/integration/scheduler_perf/util.go:789)


newSchedulingDurationCollector is a function that performs operations based on the provided parameters and returns (resultLabels map[string]string).


```go
func newSchedulingDurationCollector((resultLabels map[string]string)) (resultLabels map[string]string)
```


**Тип ответа:** resultLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:789`



---


[function] name: newThroughputCollector file: test/integration/scheduler_perf/util.go:469 returns_error: нет description: —


### newThroughputCollector (test/integration/scheduler_perf/util.go:469)


newThroughputCollector is a function that performs operations based on the provided parameters and may return an error.


```go
func newThroughputCollector((podInformer coreinformers.PodInformer, resultLabels map[string]string, labelSelector map[string]string, namespaces []string, errorMargin float64)) (podInformer coreinformers.PodInformer, resultLabels map[string]string, labelSelector map[string]string, namespaces []string, errorMargin float64)
```


**Тип ответа:** podInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/pod.go`


**Тип ответа:** coreinformers.PodInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resultLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** labelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** namespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errorMargin


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/scheduler_perf/util.go:469`



---


[function] name: run file: test/integration/scheduler_perf/util.go:358 returns_error: нет description: —


### run (test/integration/scheduler_perf/util.go:358)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (*metricsCollector) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:358`



---


[function] name: run file: test/integration/scheduler_perf/util.go:483 returns_error: нет description: —


### run (test/integration/scheduler_perf/util.go:483)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (tc *throughputCollector) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:483`



---


[function] name: run file: test/integration/scheduler_perf/util.go:691 returns_error: нет description: —


### run (test/integration/scheduler_perf/util.go:691)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (mc *memoryCollector) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:691`



---


[function] name: run file: test/integration/scheduler_perf/util.go:799 returns_error: нет description: —


### run (test/integration/scheduler_perf/util.go:799)


run is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (sdc *schedulingDurationCollector) run((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ktesting.TContext


```json
{
  "perTestHeader": {},
  "cancel": {},
  "steps": "string",
  "isSyncTest": false,
  "restConfig": null,
  "restMapper": null,
  "client": {},
  "dynamic": {},
  "apiextensions": {},
  "namespace": "string",
  "capture": null
}
```


*Определено в:* `test/utils/ktesting/tcontext.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:799`



---


[function] name: uniqueLVCombos file: test/integration/scheduler_perf/util.go:386 returns_error: нет description: uniqueLVCombos lists up all possible label values combinations.
e.g., if there are 3 labelValues, each of which has 2 va


### uniqueLVCombos (test/integration/scheduler_perf/util.go:386)


uniqueLVCombos lists up all possible label values combinations.
e.g., if there are 3 labelValues, each of which has 2 values,
the result would be {A: a1, B: b1, C: c1}, {A: a2, B: b1, C: c1}, {A: a1, B: b2, C: c1}, ... (2^3 = 8 combinations).


```go
func uniqueLVCombos((lvs []*labelValues)) (lvs []*labelValues)
```


**Тип запроса:** labelValues


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


**Тип ответа:** lvs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelValues


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/integration/scheduler_perf/util.go:386`




## test/integration/statefulset/util.go


📄 Исходный файл: `test/integration/statefulset/util.go`


<details open>
<summary><b>Функции в этом файле (20)</b></summary>


- 🔗 [Handles](#handles-testintegrationstatefulsetutilgo369) `:369`

- 🔗 [Validate](#validate-testintegrationstatefulsetutilgo373) `:373`

- 🔗 [createHeadlessService](#createheadlessservice-testintegrationstatefulsetutilgo203) `:203`

- 🔗 [createPods](#createpods-testintegrationstatefulsetutilgo222) `:222`

- 🔗 [createSTSs](#createstss-testintegrationstatefulsetutilgo210) `:210`

- 🔗 [createSTSsPods](#createstsspods-testintegrationstatefulsetutilgo235) `:235`

- 🔗 [getPods](#getpods-testintegrationstatefulsetutilgo286) `:286`

- 🔗 [getStatefulSetPVCs](#getstatefulsetpvcs-testintegrationstatefulsetutilgo299) `:299`

- 🔗 [labelMap](#labelmap-testintegrationstatefulsetutilgo54) `:54`

- 🔗 [newHeadlessService](#newheadlessservice-testintegrationstatefulsetutilgo59) `:59`

- 🔗 [newSTS](#newsts-testintegrationstatefulsetutilgo80) `:80`

- 🔗 [newStatefulSetPVC](#newstatefulsetpvc-testintegrationstatefulsetutilgo144) `:144`

- 🔗 [runControllerAndInformers](#runcontrollerandinformers-testintegrationstatefulsetutilgo196) `:196`

- 🔗 [scSetup](#scsetup-testintegrationstatefulsetutilgo166) `:166`

- 🔗 [scaleSTS](#scalests-testintegrationstatefulsetutilgo345) `:345`

- 🔗 [updatePod](#updatepod-testintegrationstatefulsetutilgo254) `:254`

- 🔗 [updatePodStatus](#updatepodstatus-testintegrationstatefulsetutilgo270) `:270`

- 🔗 [updateSTS](#updatests-testintegrationstatefulsetutilgo328) `:328`

- 🔗 [verifyOwnerRef](#verifyownerref-testintegrationstatefulsetutilgo312) `:312`

- 🔗 [waitSTSStable](#waitstsstable-testintegrationstatefulsetutilgo240) `:240`


</details>


[function] name: Handles file: test/integration/statefulset/util.go:369 returns_error: нет description: —


### Handles (test/integration/statefulset/util.go:369)


Handles is a method that handles or processes requests based on the provided parameters and returns (operation admission.Operation).


```go
func (f *fakePodFailAdmission) Handles((operation admission.Operation)) (operation admission.Operation)
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


📍 *Расположение:* `test/integration/statefulset/util.go:369`



---


[function] name: Validate file: test/integration/statefulset/util.go:373 returns_error: да description: —


### Validate (test/integration/statefulset/util.go:373)


Validate is a method that performs operations based on the provided parameters and may return an error.


```go
func (f *fakePodFailAdmission) Validate((err error)) (err error)
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


📍 *Расположение:* `test/integration/statefulset/util.go:373`



---


[function] name: createHeadlessService file: test/integration/statefulset/util.go:203 returns_error: нет description: —


### createHeadlessService (test/integration/statefulset/util.go:203)


createHeadlessService is a function that performs operations based on the provided parameters and returns (t *testing.T, clientSet clientset.Interface, headlessService *v1.Service).


```go
func createHeadlessService((t *testing.T, clientSet clientset.Interface, headlessService *v1.Service)) (t *testing.T, clientSet clientset.Interface, headlessService *v1.Service)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** headlessService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/statefulset/util.go:203`



---


[function] name: createPods file: test/integration/statefulset/util.go:222 returns_error: нет description: —


### createPods (test/integration/statefulset/util.go:222)


createPods is a function that performs operations based on the provided parameters and returns (t *testing.T, clientSet clientset.Interface, pods []*v1.Pod).


```go
func createPods((t *testing.T, clientSet clientset.Interface, pods []*v1.Pod)) (t *testing.T, clientSet clientset.Interface, pods []*v1.Pod)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** pods


```json
{
  "pods": {},
  "mu": {}
}
```


*Определено в:* `pkg/scheduler/framework/runtime/pods_in_prebind_map.go`


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


📍 *Расположение:* `test/integration/statefulset/util.go:222`



---


[function] name: createSTSs file: test/integration/statefulset/util.go:210 returns_error: нет description: —


### createSTSs (test/integration/statefulset/util.go:210)


createSTSs is a function that performs operations based on the provided parameters and returns (t *testing.T, clientSet clientset.Interface, stss []*appsv1.StatefulSet).


```go
func createSTSs((t *testing.T, clientSet clientset.Interface, stss []*appsv1.StatefulSet)) (t *testing.T, clientSet clientset.Interface, stss []*appsv1.StatefulSet)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** stss


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


📍 *Расположение:* `test/integration/statefulset/util.go:210`



---


[function] name: createSTSsPods file: test/integration/statefulset/util.go:235 returns_error: нет description: —


### createSTSsPods (test/integration/statefulset/util.go:235)


createSTSsPods is a function that performs operations based on the provided parameters and returns ([]*appsv1.StatefulSet, []*v1.Pod).


```go
func createSTSsPods(([]*appsv1.StatefulSet, []*v1.Pod)) ([]*appsv1.StatefulSet, []*v1.Pod)
```


**Тип запроса:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


📍 *Расположение:* `test/integration/statefulset/util.go:235`



---


[function] name: getPods file: test/integration/statefulset/util.go:286 returns_error: нет description: —


### getPods (test/integration/statefulset/util.go:286)


getPods is a function that performs operations based on the provided parameters and returns (t *testing.T, podClient typedv1.PodInterface, labelMap map[string]string).


```go
func getPods((t *testing.T, podClient typedv1.PodInterface, labelMap map[string]string)) (t *testing.T, podClient typedv1.PodInterface, labelMap map[string]string)
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


**Тип ответа:** podClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** typedv1.PodInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/statefulset/util.go:286`



---


[function] name: getStatefulSetPVCs file: test/integration/statefulset/util.go:299 returns_error: нет description: —


### getStatefulSetPVCs (test/integration/statefulset/util.go:299)


getStatefulSetPVCs is a function that performs operations based on the provided parameters and returns (t *testing.T, pvcClient typedv1.PersistentVolumeClaimInterface, sts *appsv1.StatefulSet).


```go
func getStatefulSetPVCs((t *testing.T, pvcClient typedv1.PersistentVolumeClaimInterface, sts *appsv1.StatefulSet)) (t *testing.T, pvcClient typedv1.PersistentVolumeClaimInterface, sts *appsv1.StatefulSet)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** pvcClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** typedv1.PersistentVolumeClaimInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sts


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/certificates/v1beta1/fake/fake_certificatesigningrequest.go`


**Тип ответа:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


📍 *Расположение:* `test/integration/statefulset/util.go:299`



---


[function] name: labelMap file: test/integration/statefulset/util.go:54 returns_error: нет description: —


### labelMap (test/integration/statefulset/util.go:54)


labelMap is a function that performs operations based on the provided parameters and returns ().


```go
func labelMap(()) ()
```


📍 *Расположение:* `test/integration/statefulset/util.go:54`



---


[function] name: newHeadlessService file: test/integration/statefulset/util.go:59 returns_error: нет description: newService returns a service with a fake name for StatefulSet to be created soon


### newHeadlessService (test/integration/statefulset/util.go:59)


newService returns a service with a fake name for StatefulSet to be created soon


```go
func newHeadlessService((namespace string)) (namespace string)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


📍 *Расположение:* `test/integration/statefulset/util.go:59`



---


[function] name: newSTS file: test/integration/statefulset/util.go:80 returns_error: нет description: newSTS returns a StatefulSet with a fake container image


### newSTS (test/integration/statefulset/util.go:80)


newSTS returns a StatefulSet with a fake container image


```go
func newSTS((name, namespace string, replicas int)) (name, namespace string, replicas int)
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


**Тип ответа:** replicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/statefulset/util.go:80`



---


[function] name: newStatefulSetPVC file: test/integration/statefulset/util.go:144 returns_error: нет description: —


### newStatefulSetPVC (test/integration/statefulset/util.go:144)


newStatefulSetPVC is a function that performs operations based on the provided parameters and returns (name string).


```go
func newStatefulSetPVC((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/integration/statefulset/util.go:144`



---


[function] name: runControllerAndInformers file: test/integration/statefulset/util.go:196 returns_error: нет description: Run STS controller and informers


### runControllerAndInformers (test/integration/statefulset/util.go:196)


Run STS controller and informers


```go
func runControllerAndInformers((ctx context.Context, sc *statefulset.StatefulSetController, informers informers.SharedInformerFactory)) (ctx context.Context, sc *statefulset.StatefulSetController, informers informers.SharedInformerFactory)
```


**Тип запроса:** statefulset.StatefulSetController


```json
{
  "kubeClient": {},
  "control": {},
  "podControl": {},
  "podIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "setLister": {},
  "setListerSynced": {},
  "pvcListerSynced": {},
  "revListerSynced": {},
  "queue": {},
  "eventBroadcaster": {},
  "clock": {},
  "consistencyStore": {}
}
```


*Определено в:* `pkg/controller/statefulset/stateful_set.go`


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


**Тип ответа:** statefulset.StatefulSetController


```json
{
  "kubeClient": {},
  "control": {},
  "podControl": {},
  "podIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "setLister": {},
  "setListerSynced": {},
  "pvcListerSynced": {},
  "revListerSynced": {},
  "queue": {},
  "eventBroadcaster": {},
  "clock": {},
  "consistencyStore": {}
}
```


*Определено в:* `pkg/controller/statefulset/stateful_set.go`


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


📍 *Расположение:* `test/integration/statefulset/util.go:196`



---


[function] name: scSetup file: test/integration/statefulset/util.go:166 returns_error: нет description: scSetup sets up necessities for Statefulset integration test, including control plane, apiserver, informers, and clients


### scSetup (test/integration/statefulset/util.go:166)


scSetup sets up necessities for Statefulset integration test, including control plane, apiserver, informers, and clientset


```go
func scSetup((context.Context, kubeapiservertesting.TearDownFunc, *statefulset.StatefulSetController, informers.SharedInformerFactory, clientset.Interface)) (context.Context, kubeapiservertesting.TearDownFunc, *statefulset.StatefulSetController, informers.SharedInformerFactory, clientset.Interface)
```


**Тип запроса:** statefulset.StatefulSetController


```json
{
  "kubeClient": {},
  "control": {},
  "podControl": {},
  "podIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "setLister": {},
  "setListerSynced": {},
  "pvcListerSynced": {},
  "revListerSynced": {},
  "queue": {},
  "eventBroadcaster": {},
  "clock": {},
  "consistencyStore": {}
}
```


*Определено в:* `pkg/controller/statefulset/stateful_set.go`


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


**Тип ответа:** kubeapiservertesting.TearDownFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** statefulset.StatefulSetController


```json
{
  "kubeClient": {},
  "control": {},
  "podControl": {},
  "podIndexer": {},
  "podLister": {},
  "podListerSynced": {},
  "setLister": {},
  "setListerSynced": {},
  "pvcListerSynced": {},
  "revListerSynced": {},
  "queue": {},
  "eventBroadcaster": {},
  "clock": {},
  "consistencyStore": {}
}
```


*Определено в:* `pkg/controller/statefulset/stateful_set.go`


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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `test/integration/statefulset/util.go:166`



---


[function] name: scaleSTS file: test/integration/statefulset/util.go:345 returns_error: нет description: Update .Spec.Replicas to replicas and verify .Status.Replicas is changed accordingly


### scaleSTS (test/integration/statefulset/util.go:345)


Update .Spec.Replicas to replicas and verify .Status.Replicas is changed accordingly


```go
func scaleSTS((t *testing.T, c clientset.Interface, sts *appsv1.StatefulSet, replicas int32)) (t *testing.T, c clientset.Interface, sts *appsv1.StatefulSet, replicas int32)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** sts


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/certificates/v1beta1/fake/fake_certificatesigningrequest.go`


**Тип ответа:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** replicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/statefulset/util.go:345`



---


[function] name: updatePod file: test/integration/statefulset/util.go:254 returns_error: нет description: —


### updatePod (test/integration/statefulset/util.go:254)


updatePod is a function that performs operations based on the provided parameters and returns (t *testing.T, podClient typedv1.PodInterface, podName string, updateFunc func(*v1.Pod)).


```go
func updatePod((t *testing.T, podClient typedv1.PodInterface, podName string, updateFunc func(*v1.Pod))) (t *testing.T, podClient typedv1.PodInterface, podName string, updateFunc func(*v1.Pod))
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** podClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** typedv1.PodInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updateFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


📍 *Расположение:* `test/integration/statefulset/util.go:254`



---


[function] name: updatePodStatus file: test/integration/statefulset/util.go:270 returns_error: нет description: —


### updatePodStatus (test/integration/statefulset/util.go:270)


updatePodStatus is a function that performs operations based on the provided parameters and returns (t *testing.T, podClient typedv1.PodInterface, podName string, updateStatusFunc func(*v1.Pod)).


```go
func updatePodStatus((t *testing.T, podClient typedv1.PodInterface, podName string, updateStatusFunc func(*v1.Pod))) (t *testing.T, podClient typedv1.PodInterface, podName string, updateStatusFunc func(*v1.Pod))
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** podClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** typedv1.PodInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updateStatusFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


📍 *Расположение:* `test/integration/statefulset/util.go:270`



---


[function] name: updateSTS file: test/integration/statefulset/util.go:328 returns_error: нет description: —


### updateSTS (test/integration/statefulset/util.go:328)


updateSTS is a function that performs operations based on the provided parameters and returns (t *testing.T, stsClient typedappsv1.StatefulSetInterface, stsName string, updateFunc func(*appsv1.StatefulSet)).


```go
func updateSTS((t *testing.T, stsClient typedappsv1.StatefulSetInterface, stsName string, updateFunc func(*appsv1.StatefulSet))) (t *testing.T, stsClient typedappsv1.StatefulSetInterface, stsName string, updateFunc func(*appsv1.StatefulSet))
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** stsClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** typedappsv1.StatefulSetInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stsName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updateFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


📍 *Расположение:* `test/integration/statefulset/util.go:328`



---


[function] name: verifyOwnerRef file: test/integration/statefulset/util.go:312 returns_error: нет description: —


### verifyOwnerRef (test/integration/statefulset/util.go:312)


verifyOwnerRef is a function that performs operations based on the provided parameters and returns (t *testing.T, pvc *v1.PersistentVolumeClaim, kind string, expected bool).


```go
func verifyOwnerRef((t *testing.T, pvc *v1.PersistentVolumeClaim, kind string, expected bool)) (t *testing.T, pvc *v1.PersistentVolumeClaim, kind string, expected bool)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** pvc


```json
{
  "tsInfo": {}
}
```


*Определено в:* `test/e2e/storage/testsuites/pvcdeletionperf.go`


**Тип ответа:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


**Тип ответа:** expected


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/errors/errors.go`


📍 *Расположение:* `test/integration/statefulset/util.go:312`



---


[function] name: waitSTSStable file: test/integration/statefulset/util.go:240 returns_error: нет description: Verify .Status.Replicas is equal to .Spec.Replicas


### waitSTSStable (test/integration/statefulset/util.go:240)


Verify .Status.Replicas is equal to .Spec.Replicas


```go
func waitSTSStable((t *testing.T, clientSet clientset.Interface, sts *appsv1.StatefulSet)) (t *testing.T, clientSet clientset.Interface, sts *appsv1.StatefulSet)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** sts


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/certificates/v1beta1/fake/fake_certificatesigningrequest.go`


**Тип ответа:** appsv1.StatefulSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


📍 *Расположение:* `test/integration/statefulset/util.go:240`




## test/integration/storageversionmigrator/util.go


📄 Исходный файл: `test/integration/storageversionmigrator/util.go`


<details open>
<summary><b>Функции в этом файле (32)</b></summary>


- 🔗 [Fatalf](#fatalf-testintegrationstorageversionmigratorutilgo1201) `:1201`

- 🔗 [Helper](#helper-testintegrationstorageversionmigratorutilgo1200) `:1200`

- 🔗 [countMatchingAuditEvents](#countmatchingauditevents-testintegrationstorageversionmigratorutilgo684) `:684`

- 🔗 [createCR](#createcr-testintegrationstorageversionmigratorutilgo851) `:851`

- 🔗 [createCRD](#createcrd-testintegrationstorageversionmigratorutilgo717) `:717`

- 🔗 [createChaos](#createchaos-testintegrationstorageversionmigratorutilgo1167) `:1167`

- 🔗 [createConversionWebhook](#createconversionwebhook-testintegrationstorageversionmigratorutilgo923) `:923`

- 🔗 [createEncryptionConfig](#createencryptionconfig-testintegrationstorageversionmigratorutilgo355) `:355`

- 🔗 [createKubeConfigFileForRestConfig](#createkubeconfigfileforrestconfig-testintegrationstorageversionmigratorutilgo343) `:343`

- 🔗 [createSVMResource](#createsvmresource-testintegrationstorageversionmigratorutilgo471) `:471`

- 🔗 [createSecret](#createsecret-testintegrationstorageversionmigratorutilgo376) `:376`

- 🔗 [deleteCR](#deletecr-testintegrationstorageversionmigratorutilgo910) `:910`

- 🔗 [getAuditEvents](#getauditevents-testintegrationstorageversionmigratorutilgo696) `:696`

- 🔗 [getAutomaticReloadSuccessTotal](#getautomaticreloadsuccesstotal-testintegrationstorageversionmigratorutilgo526) `:526`

- 🔗 [getCR](#getcr-testintegrationstorageversionmigratorutilgo879) `:879`

- 🔗 [getETCDPathForResource](#getetcdpathforresource-testintegrationstorageversionmigratorutilgo401) `:401`

- 🔗 [getRawCRFromETCD](#getrawcrfrometcd-testintegrationstorageversionmigratorutilgo435) `:435`

- 🔗 [getRawSecretFromETCD](#getrawsecretfrometcd-testintegrationstorageversionmigratorutilgo391) `:391`

- 🔗 [getSVM](#getsvm-testintegrationstorageversionmigratorutilgo493) `:493`

- 🔗 [isCRDMigrated](#iscrdmigrated-testintegrationstorageversionmigratorutilgo1075) `:1075`

- 🔗 [isCRStoredAtVersion](#iscrstoredatversion-testintegrationstorageversionmigratorutilgo1057) `:1057`

- 🔗 [isEncryptionConfigFileUpdated](#isencryptionconfigfileupdated-testintegrationstorageversionmigratorutilgo559) `:559`

- 🔗 [listCR](#listcr-testintegrationstorageversionmigratorutilgo896) `:896`

- 🔗 [readRawRecordFromETCD](#readrawrecordfrometcd-testintegrationstorageversionmigratorutilgo413) `:413`

- 🔗 [setupAudit](#setupaudit-testintegrationstorageversionmigratorutilgo503) `:503`

- 🔗 [setupServerCert](#setupservercert-testintegrationstorageversionmigratorutilgo985) `:985`

- 🔗 [svmSetup](#svmsetup-testintegrationstorageversionmigratorutilgo260) `:260`

- 🔗 [updateCRD](#updatecrd-testintegrationstorageversionmigratorutilgo770) `:770`

- 🔗 [updateFile](#updatefile-testintegrationstorageversionmigratorutilgo445) `:445`

- 🔗 [validateRVAndGeneration](#validatervandgeneration-testintegrationstorageversionmigratorutilgo1135) `:1135`

- 🔗 [waitForCRDUpdate](#waitforcrdupdate-testintegrationstorageversionmigratorutilgo791) `:791`

- 🔗 [waitForResourceMigration](#waitforresourcemigration-testintegrationstorageversionmigratorutilgo579) `:579`


</details>


[function] name: Fatalf file: test/integration/storageversionmigrator/util.go:1201 returns_error: нет description: —


### Fatalf (test/integration/storageversionmigrator/util.go:1201)


Fatalf is a method that performs operations based on the provided parameters and returns (format string, args ...any).


```go
func (ignoreFailures) Fatalf((format string, args ...any)) (format string, args ...any)
```


**Тип ответа:** format


```json
{
  "availableOnNodes": null,
  "allocation": null
}
```


*Определено в:* `pkg/scheduler/framework/plugins/dynamicresources/dynamicresources.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:1201`



---


[function] name: Helper file: test/integration/storageversionmigrator/util.go:1200 returns_error: нет description: —


### Helper (test/integration/storageversionmigrator/util.go:1200)


Helper is a method that performs operations based on the provided parameters and returns ().


```go
func (ignoreFailures) Helper(()) ()
```


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:1200`



---


[function] name: countMatchingAuditEvents file: test/integration/storageversionmigrator/util.go:684 returns_error: нет description: —


### countMatchingAuditEvents (test/integration/storageversionmigrator/util.go:684)


countMatchingAuditEvents is a method that performs operations based on the provided parameters and returns (t *testing.T, f func(utils.AuditEvent) bool).


```go
func (svm *svmTest) countMatchingAuditEvents((t *testing.T, f func(utils.AuditEvent) bool)) (t *testing.T, f func(utils.AuditEvent) bool)
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


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utils.AuditEvent


```json
{
  "ID": {},
  "Level": {},
  "Stage": {},
  "RequestURI": "string",
  "Verb": "string",
  "Code": 0,
  "User": "string",
  "ImpersonatedUser": "string",
  "ImpersonatedGroups": "string",
  "Resource": "string",
  "Namespace": "string",
  "RequestObject": false,
  "ResponseObject": false,
  "AuthorizeDecision": "string",
  "AdmissionWebhookMutationAnnotations": {},
  "AdmissionWebhookPatchAnnotations": {},
  "CustomAuditAnnotations": {}
}
```


*Определено в:* `test/utils/audit.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:684`



---


[function] name: createCR file: test/integration/storageversionmigrator/util.go:851 returns_error: нет description: —


### createCR (test/integration/storageversionmigrator/util.go:851)


createCR is a method that performs operations based on the provided parameters and returns (ctx context.Context, t testingT, crName, version string).


```go
func (svm *svmTest) createCR((ctx context.Context, t testingT, crName, version string)) (ctx context.Context, t testingT, crName, version string)
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


**Тип ответа:** testingT


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** crName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:851`



---


[function] name: createCRD file: test/integration/storageversionmigrator/util.go:717 returns_error: нет description: —


### createCRD (test/integration/storageversionmigrator/util.go:717)


createCRD is a method that performs operations based on the provided parameters and returns (
	t *testing.T,
	name, group string,
	certCtx *certContext,
	crdVersions []apiextensionsv1.CustomResourceDefinitionVersion,
).


```go
func (svm *svmTest) createCRD((
	t *testing.T,
	name, group string,
	certCtx *certContext,
	crdVersions []apiextensionsv1.CustomResourceDefinitionVersion,
)) (
	t *testing.T,
	name, group string,
	certCtx *certContext,
	crdVersions []apiextensionsv1.CustomResourceDefinitionVersion,
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


**Тип запроса:** certContext


```json
{
  "cert": [],
  "key": [],
  "signingCert": []
}
```


*Определено в:* `test/e2e/apimachinery/certs.go`


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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** group


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/interface.go`


**Тип ответа:** certCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** certContext


```json
{
  "cert": [],
  "key": [],
  "signingCert": []
}
```


*Определено в:* `test/e2e/apimachinery/certs.go`


**Тип ответа:** crdVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiextensionsv1.CustomResourceDefinitionVersion


```json
{
  "name": "string",
  "served": false,
  "storage": false,
  "deprecated": false,
  "deprecationWarning": "string",
  "schema": null,
  "subresources": null,
  "additionalPrinterColumns": [],
  "selectableFields": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:717`



---


[function] name: createChaos file: test/integration/storageversionmigrator/util.go:1167 returns_error: нет description: —


### createChaos (test/integration/storageversionmigrator/util.go:1167)


createChaos is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T).


```go
func (svm *svmTest) createChaos((ctx context.Context, t *testing.T)) (ctx context.Context, t *testing.T)
```


**Тип запроса:** testing.T


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


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:1167`



---


[function] name: createConversionWebhook file: test/integration/storageversionmigrator/util.go:923 returns_error: нет description: —


### createConversionWebhook (test/integration/storageversionmigrator/util.go:923)


createConversionWebhook is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T, certCtx *certContext).


```go
func (svm *svmTest) createConversionWebhook((ctx context.Context, t *testing.T, certCtx *certContext)) (ctx context.Context, t *testing.T, certCtx *certContext)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** certContext


```json
{
  "cert": [],
  "key": [],
  "signingCert": []
}
```


*Определено в:* `test/e2e/apimachinery/certs.go`


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


**Тип ответа:** certCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** certContext


```json
{
  "cert": [],
  "key": [],
  "signingCert": []
}
```


*Определено в:* `test/e2e/apimachinery/certs.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:923`



---


[function] name: createEncryptionConfig file: test/integration/storageversionmigrator/util.go:355 returns_error: да description: —


### createEncryptionConfig (test/integration/storageversionmigrator/util.go:355)


createEncryptionConfig is a function that performs operations based on the provided parameters and may return an error.


```go
func createEncryptionConfig((
	filePathForEncryptionConfig string,
	err error,
)) (
	filePathForEncryptionConfig string,
	err error,
)
```


**Тип ответа:** filePathForEncryptionConfig


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


*Типы возврата:* `filePathForEncryptionConfig string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:355`



---


[function] name: createKubeConfigFileForRestConfig file: test/integration/storageversionmigrator/util.go:343 returns_error: нет description: —


### createKubeConfigFileForRestConfig (test/integration/storageversionmigrator/util.go:343)


createKubeConfigFileForRestConfig is a function that performs operations based on the provided parameters and returns (t *testing.T, restConfig *rest.Config).


```go
func createKubeConfigFileForRestConfig((t *testing.T, restConfig *rest.Config)) (t *testing.T, restConfig *rest.Config)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** rest.Config


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


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** restConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:343`



---


[function] name: createSVMResource file: test/integration/storageversionmigrator/util.go:471 returns_error: да description: —


### createSVMResource (test/integration/storageversionmigrator/util.go:471)


createSVMResource is a method that performs operations based on the provided parameters and may return an error.


```go
func (svm *svmTest) createSVMResource((
	*svmv1beta1.StorageVersionMigration,
	error,
)) (
	*svmv1beta1.StorageVersionMigration,
	error,
)
```


**Тип запроса:** svmv1beta1.StorageVersionMigration


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/storagemigration/types.go`


**Тип ответа:** svmv1beta1.StorageVersionMigration


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/storagemigration/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*svmv1beta1.StorageVersionMigration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:471`



---


[function] name: createSecret file: test/integration/storageversionmigrator/util.go:376 returns_error: да description: —


### createSecret (test/integration/storageversionmigrator/util.go:376)


createSecret is a method that performs operations based on the provided parameters and may return an error.


```go
func (svm *svmTest) createSecret((*corev1.Secret, error)) (*corev1.Secret, error)
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


**Тип ответа:** corev1.Secret


```json
{
  "Immutable": false,
  "Data": {},
  "Type": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*corev1.Secret`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:376`



---


[function] name: deleteCR file: test/integration/storageversionmigrator/util.go:910 returns_error: нет description: —


### deleteCR (test/integration/storageversionmigrator/util.go:910)


deleteCR is a method that performs operations based on the provided parameters and returns (ctx context.Context, t testingT, name, version string).


```go
func (svm *svmTest) deleteCR((ctx context.Context, t testingT, name, version string)) (ctx context.Context, t testingT, name, version string)
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


**Тип ответа:** testingT


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:910`



---


[function] name: getAuditEvents file: test/integration/storageversionmigrator/util.go:696 returns_error: нет description: —


### getAuditEvents (test/integration/storageversionmigrator/util.go:696)


getAuditEvents is a method that performs operations based on the provided parameters and returns (t *testing.T).


```go
func (svm *svmTest) getAuditEvents((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:696`



---


[function] name: getAutomaticReloadSuccessTotal file: test/integration/storageversionmigrator/util.go:526 returns_error: нет description: —


### getAutomaticReloadSuccessTotal (test/integration/storageversionmigrator/util.go:526)


getAutomaticReloadSuccessTotal is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T).


```go
func (svm *svmTest) getAutomaticReloadSuccessTotal((ctx context.Context, t *testing.T)) (ctx context.Context, t *testing.T)
```


**Тип запроса:** testing.T


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


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:526`



---


[function] name: getCR file: test/integration/storageversionmigrator/util.go:879 returns_error: нет description: —


### getCR (test/integration/storageversionmigrator/util.go:879)


getCR is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T, crName, version string).


```go
func (svm *svmTest) getCR((ctx context.Context, t *testing.T, crName, version string)) (ctx context.Context, t *testing.T, crName, version string)
```


**Тип запроса:** testing.T


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


**Тип ответа:** crName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:879`



---


[function] name: getETCDPathForResource file: test/integration/storageversionmigrator/util.go:401 returns_error: нет description: —


### getETCDPathForResource (test/integration/storageversionmigrator/util.go:401)


getETCDPathForResource is a function that performs operations based on the provided parameters and returns (t *testing.T, storagePrefix, group, resource, namespaceName, name string).


```go
func getETCDPathForResource((t *testing.T, storagePrefix, group, resource, namespaceName, name string)) (t *testing.T, storagePrefix, group, resource, namespaceName, name string)
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


**Тип ответа:** storagePrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** group


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/interface.go`


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


**Тип ответа:** namespaceName


```json
{
  "Namespace": "string",
  "Name": "string",
  "RV": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/delegator.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:401`



---


[function] name: getRawCRFromETCD file: test/integration/storageversionmigrator/util.go:435 returns_error: да description: —


### getRawCRFromETCD (test/integration/storageversionmigrator/util.go:435)


getRawCRFromETCD is a method that performs operations based on the provided parameters and may return an error.


```go
func (svm *svmTest) getRawCRFromETCD(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:435`



---


[function] name: getRawSecretFromETCD file: test/integration/storageversionmigrator/util.go:391 returns_error: да description: —


### getRawSecretFromETCD (test/integration/storageversionmigrator/util.go:391)


getRawSecretFromETCD is a method that performs operations based on the provided parameters and may return an error.


```go
func (svm *svmTest) getRawSecretFromETCD(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:391`



---


[function] name: getSVM file: test/integration/storageversionmigrator/util.go:493 returns_error: да description: —


### getSVM (test/integration/storageversionmigrator/util.go:493)


getSVM is a method that performs operations based on the provided parameters and may return an error.


```go
func (svm *svmTest) getSVM((
	*svmv1beta1.StorageVersionMigration,
	error,
)) (
	*svmv1beta1.StorageVersionMigration,
	error,
)
```


**Тип запроса:** svmv1beta1.StorageVersionMigration


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/storagemigration/types.go`


**Тип ответа:** svmv1beta1.StorageVersionMigration


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/storagemigration/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*svmv1beta1.StorageVersionMigration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:493`



---


[function] name: isCRDMigrated file: test/integration/storageversionmigrator/util.go:1075 returns_error: нет description: —


### isCRDMigrated (test/integration/storageversionmigrator/util.go:1075)


isCRDMigrated is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T, crdSVMName, triggerCRName string).


```go
func (svm *svmTest) isCRDMigrated((ctx context.Context, t *testing.T, crdSVMName, triggerCRName string)) (ctx context.Context, t *testing.T, crdSVMName, triggerCRName string)
```


**Тип запроса:** testing.T


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


**Тип ответа:** crdSVMName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** triggerCRName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:1075`



---


[function] name: isCRStoredAtVersion file: test/integration/storageversionmigrator/util.go:1057 returns_error: нет description: —


### isCRStoredAtVersion (test/integration/storageversionmigrator/util.go:1057)


isCRStoredAtVersion is a method that performs operations based on the provided parameters and returns (t *testing.T, version, crName string).


```go
func (svm *svmTest) isCRStoredAtVersion((t *testing.T, version, crName string)) (t *testing.T, version, crName string)
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


**Тип ответа:** crName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:1057`



---


[function] name: isEncryptionConfigFileUpdated file: test/integration/storageversionmigrator/util.go:559 returns_error: нет description: —


### isEncryptionConfigFileUpdated (test/integration/storageversionmigrator/util.go:559)


isEncryptionConfigFileUpdated is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T, metricBeforeUpdate int).


```go
func (svm *svmTest) isEncryptionConfigFileUpdated((ctx context.Context, t *testing.T, metricBeforeUpdate int)) (ctx context.Context, t *testing.T, metricBeforeUpdate int)
```


**Тип запроса:** testing.T


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


**Тип ответа:** metricBeforeUpdate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:559`



---


[function] name: listCR file: test/integration/storageversionmigrator/util.go:896 returns_error: нет description: —


### listCR (test/integration/storageversionmigrator/util.go:896)


listCR is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T, version string).


```go
func (svm *svmTest) listCR((ctx context.Context, t *testing.T, version string)) (ctx context.Context, t *testing.T, version string)
```


**Тип запроса:** testing.T


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


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:896`



---


[function] name: readRawRecordFromETCD file: test/integration/storageversionmigrator/util.go:413 returns_error: да description: —


### readRawRecordFromETCD (test/integration/storageversionmigrator/util.go:413)


readRawRecordFromETCD is a method that performs operations based on the provided parameters and may return an error.


```go
func (svm *svmTest) readRawRecordFromETCD((*clientv3.GetResponse, error)) (*clientv3.GetResponse, error)
```


**Тип запроса:** clientv3.GetResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientv3.GetResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*clientv3.GetResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:413`



---


[function] name: setupAudit file: test/integration/storageversionmigrator/util.go:503 returns_error: нет description: —


### setupAudit (test/integration/storageversionmigrator/util.go:503)


setupAudit is a function that performs operations based on the provided parameters and returns (
	policyFile *os.File,
	logFile *os.File,
).


```go
func setupAudit((
	policyFile *os.File,
	logFile *os.File,
)) (
	policyFile *os.File,
	logFile *os.File,
)
```


**Тип запроса:** os.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип запроса:** os.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** policyFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** os.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** logFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** os.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:503`



---


[function] name: setupServerCert file: test/integration/storageversionmigrator/util.go:985 returns_error: нет description: —


### setupServerCert (test/integration/storageversionmigrator/util.go:985)


setupServerCert is a method that performs operations based on the provided parameters and returns (t *testing.T).


```go
func (svm *svmTest) setupServerCert((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:985`



---


[function] name: svmSetup file: test/integration/storageversionmigrator/util.go:260 returns_error: нет description: —


### svmSetup (test/integration/storageversionmigrator/util.go:260)


svmSetup is a function that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T).


```go
func svmSetup((ctx context.Context, t *testing.T)) (ctx context.Context, t *testing.T)
```


**Тип запроса:** testing.T


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


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:260`



---


[function] name: updateCRD file: test/integration/storageversionmigrator/util.go:770 returns_error: нет description: —


### updateCRD (test/integration/storageversionmigrator/util.go:770)


updateCRD is a method that performs operations based on the provided parameters and returns (
	ctx context.Context,
	t *testing.T,
	crdName string,
	updatesCRDVersions []apiextensionsv1.CustomResourceDefinitionVersion,
	expectedServingVersions []string,
	expectedStorageVersion string,
).


```go
func (svm *svmTest) updateCRD((
	ctx context.Context,
	t *testing.T,
	crdName string,
	updatesCRDVersions []apiextensionsv1.CustomResourceDefinitionVersion,
	expectedServingVersions []string,
	expectedStorageVersion string,
)) (
	ctx context.Context,
	t *testing.T,
	crdName string,
	updatesCRDVersions []apiextensionsv1.CustomResourceDefinitionVersion,
	expectedServingVersions []string,
	expectedStorageVersion string,
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


**Тип ответа:** crdName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updatesCRDVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiextensionsv1.CustomResourceDefinitionVersion


```json
{
  "name": "string",
  "served": false,
  "storage": false,
  "deprecated": false,
  "deprecationWarning": "string",
  "schema": null,
  "subresources": null,
  "additionalPrinterColumns": [],
  "selectableFields": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** expectedServingVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** expectedStorageVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:770`



---


[function] name: updateFile file: test/integration/storageversionmigrator/util.go:445 returns_error: нет description: —


### updateFile (test/integration/storageversionmigrator/util.go:445)


updateFile is a method that performs operations based on the provided parameters and returns (t *testing.T, configDir, filename string, newContent []byte).


```go
func (svm *svmTest) updateFile((t *testing.T, configDir, filename string, newContent []byte)) (t *testing.T, configDir, filename string, newContent []byte)
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


**Тип ответа:** configDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newContent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:445`



---


[function] name: validateRVAndGeneration file: test/integration/storageversionmigrator/util.go:1135 returns_error: нет description: —


### validateRVAndGeneration (test/integration/storageversionmigrator/util.go:1135)


validateRVAndGeneration is a method that performs operations based on the provided parameters and returns (ctx context.Context, t *testing.T, crVersions map[string]versions, getCRVersion string).


```go
func (svm *svmTest) validateRVAndGeneration((ctx context.Context, t *testing.T, crVersions map[string]versions, getCRVersion string)) (ctx context.Context, t *testing.T, crVersions map[string]versions, getCRVersion string)
```


**Тип запроса:** testing.T


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


**Тип ответа:** crVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** versions


```json
{
  "generation": 0,
  "rv": "string",
  "isRVUpdated": false
}
```


*Определено в:* `test/integration/storageversionmigrator/util.go`


**Тип ответа:** getCRVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:1135`



---


[function] name: waitForCRDUpdate file: test/integration/storageversionmigrator/util.go:791 returns_error: нет description: —


### waitForCRDUpdate (test/integration/storageversionmigrator/util.go:791)


waitForCRDUpdate is a method that performs operations based on the provided parameters and returns (
	ctx context.Context,
	t *testing.T,
	crdKind string,
	expectedServingVersions []string,
	expectedStorageVersion string,
).


```go
func (svm *svmTest) waitForCRDUpdate((
	ctx context.Context,
	t *testing.T,
	crdKind string,
	expectedServingVersions []string,
	expectedStorageVersion string,
)) (
	ctx context.Context,
	t *testing.T,
	crdKind string,
	expectedServingVersions []string,
	expectedStorageVersion string,
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


**Тип ответа:** crdKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** expectedServingVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** expectedStorageVersion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:791`



---


[function] name: waitForResourceMigration file: test/integration/storageversionmigrator/util.go:579 returns_error: нет description: waitForResourceMigration checks following conditions:
1. The svm resource has SuccessfullyMigrated condition.
2. The aud


### waitForResourceMigration (test/integration/storageversionmigrator/util.go:579)


waitForResourceMigration checks following conditions:
1. The svm resource has SuccessfullyMigrated condition.
2. The audit log contains patch events for the given secret.


```go
func (svm *svmTest) waitForResourceMigration((
	ctx context.Context,
	t *testing.T,
	svmName, name string,
	expectedEvents int,
)) (
	ctx context.Context,
	t *testing.T,
	svmName, name string,
	expectedEvents int,
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


**Тип ответа:** svmName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** expectedEvents


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/storageversionmigrator/util.go:579`




## test/integration/util/util.go


📄 Исходный файл: `test/integration/util/util.go`


<details open>
<summary><b>Функции в этом файле (65)</b></summary>


- 🔗 [AddTaintToNode](#addtainttonode-testintegrationutilutilgo406) `:406`

- 🔗 [CleanupNodes](#cleanupnodes-testintegrationutilutilgo302) `:302`

- 🔗 [CleanupPods](#cleanuppods-testintegrationutilutilgo390) `:390`

- 🔗 [CleanupTest](#cleanuptest-testintegrationutilutilgo347) `:347`

- 🔗 [CreateAndWaitForNodesInCache](#createandwaitfornodesincache-testintegrationutilutilgo791) `:791`

- 🔗 [CreateGCController](#creategccontroller-testintegrationutilutilgo194) `:194`

- 🔗 [CreateNamespaceController](#createnamespacecontroller-testintegrationutilutilgo232) `:232`

- 🔗 [CreateNamespacesWithLabels](#createnamespaceswithlabels-testintegrationutilutilgo1149) `:1149`

- 🔗 [CreateNode](#createnode-testintegrationutilutilgo772) `:772`

- 🔗 [CreatePV](#createpv-testintegrationutilutilgo922) `:922`

- 🔗 [CreatePVC](#createpvc-testintegrationutilutilgo916) `:916`

- 🔗 [CreatePausePod](#createpausepod-testintegrationutilutilgo887) `:887`

- 🔗 [CreatePausePodWithResource](#createpausepodwithresource-testintegrationutilutilgo894) `:894`

- 🔗 [CreateResourceClaimController](#createresourceclaimcontroller-testintegrationutilutilgo129) `:129`

- 🔗 [DeletePV](#deletepv-testintegrationutilutilgo932) `:932`

- 🔗 [DeletePVC](#deletepvc-testintegrationutilutilgo927) `:927`

- 🔗 [DeletePod](#deletepod-testintegrationutilutilgo1141) `:1141`

- 🔗 [GetPod](#getpod-testintegrationutilutilgo1145) `:1145`

- 🔗 [GetTolerationSeconds](#gettolerationseconds-testintegrationutilutilgo477) `:477`

- 🔗 [InitDisruptionController](#initdisruptioncontroller-testintegrationutilutilgo673) `:673`

- 🔗 [InitPausePod](#initpausepod-testintegrationutilutilgo832) `:832`

- 🔗 [InitPodWithContainers](#initpodwithcontainers-testintegrationutilutilgo960) `:960`

- 🔗 [InitTestAPIServer](#inittestapiserver-testintegrationutilutilgo507) `:507`

- 🔗 [InitTestDisablePreemption](#inittestdisablepreemption-testintegrationutilutilgo716) `:716`

- 🔗 [InitTestScheduler](#inittestscheduler-testintegrationutilutilgo581) `:581`

- 🔗 [InitTestSchedulerWithNS](#inittestschedulerwithns-testintegrationutilutilgo707) `:707`

- 🔗 [InitTestSchedulerWithOptions](#inittestschedulerwithoptions-testintegrationutilutilgo591) `:591`

- 🔗 [NextPodOrDie](#nextpodordie-testintegrationutilutilgo1181) `:1181`

- 🔗 [NodeCopyWithConditions](#nodecopywithconditions-testintegrationutilutilgo487) `:487`

- 🔗 [NodeReadyStatus](#nodereadystatus-testintegrationutilutilgo465) `:465`

- 🔗 [NodeTainted](#nodetainted-testintegrationutilutilgo441) `:441`

- 🔗 [PodDeleted](#poddeleted-testintegrationutilutilgo310) `:310`

- 🔗 [PodIsGettingEvicted](#podisgettingevicted-testintegrationutilutilgo990) `:990`

- 🔗 [PodScheduled](#podscheduled-testintegrationutilutilgo657) `:657`

- 🔗 [PodScheduledIn](#podscheduledin-testintegrationutilutilgo1004) `:1004`

- 🔗 [PodSchedulingError](#podschedulingerror-testintegrationutilutilgo1041) `:1041`

- 🔗 [PodSchedulingGated](#podschedulinggated-testintegrationutilutilgo1056) `:1056`

- 🔗 [PodUnschedulable](#podunschedulable-testintegrationutilutilgo1025) `:1025`

- 🔗 [PodsCleanedUp](#podscleanedup-testintegrationutilutilgo324) `:324`

- 🔗 [RemovePodFinalizers](#removepodfinalizers-testintegrationutilutilgo367) `:367`

- 🔗 [RemovePodFinalizersInNamespace](#removepodfinalizersinnamespace-testintegrationutilutilgo357) `:357`

- 🔗 [RemoveTaintOffNode](#removetaintoffnode-testintegrationutilutilgo417) `:417`

- 🔗 [RoundTrip](#roundtrip-testintegrationutilutilgo291) `:291`

- 🔗 [RunPausePod](#runpausepod-testintegrationutilutilgo938) `:938`

- 🔗 [RunPodWithContainers](#runpodwithcontainers-testintegrationutilutilgo975) `:975`

- 🔗 [StartFakePVController](#startfakepvcontroller-testintegrationutilutilgo148) `:148`

- 🔗 [StartScheduler](#startscheduler-testintegrationutilutilgo88) `:88`

- 🔗 [SyncSchedulerInformerFactory](#syncschedulerinformerfactory-testintegrationutilutilgo335) `:335`

- 🔗 [UpdateNode](#updatenode-testintegrationutilutilgo768) `:768`

- 🔗 [UpdateNodeStatus](#updatenodestatus-testintegrationutilutilgo498) `:498`

- 🔗 [WaitCachedPodsStable](#waitcachedpodsstable-testintegrationutilutilgo1117) `:1117`

- 🔗 [WaitForNodeTaints](#waitfornodetaints-testintegrationutilutilgo435) `:435`

- 🔗 [WaitForNodesInCache](#waitfornodesincache-testintegrationutilutilgo802) `:802`

- 🔗 [WaitForNominatedNodeName](#waitfornominatednodename-testintegrationutilutilgo1212) `:1212`

- 🔗 [WaitForNominatedNodeNameWithTimeout](#waitfornominatednodenamewithtimeout-testintegrationutilutilgo1196) `:1196`

- 🔗 [WaitForPDBsStable](#waitforpdbsstable-testintegrationutilutilgo1089) `:1089`

- 🔗 [WaitForPodSchedulingGated](#waitforpodschedulinggated-testintegrationutilutilgo1083) `:1083`

- 🔗 [WaitForPodToSchedule](#waitforpodtoschedule-testintegrationutilutilgo652) `:652`

- 🔗 [WaitForPodToScheduleWithTimeout](#waitforpodtoschedulewithtimeout-testintegrationutilutilgo646) `:646`

- 🔗 [WaitForPodUnschedulable](#waitforpodunschedulable-testintegrationutilutilgo1077) `:1077`

- 🔗 [WaitForPodUnschedulableWithTimeout](#waitforpodunschedulablewithtimeout-testintegrationutilutilgo1071) `:1071`

- 🔗 [WaitForReflection](#waitforreflection-testintegrationutilutilgo740) `:740`

- 🔗 [WaitForSchedulerCacheCleanup](#waitforschedulercachecleanup-testintegrationutilutilgo567) `:567`

- 🔗 [createNodes](#createnodes-testintegrationutilutilgo776) `:776`

- 🔗 [timeout](#timeout-testintegrationutilutilgo1161) `:1161`


</details>


[function] name: AddTaintToNode file: test/integration/util/util.go:406 returns_error: нет description: AddTaintToNode add taints to specific node


### AddTaintToNode (test/integration/util/util.go:406)


AddTaintToNode add taints to specific node


```go
func AddTaintToNode((cs clientset.Interface, nodeName string, taint v1.Taint)) (cs clientset.Interface, nodeName string, taint v1.Taint)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** taint


```json
{
  "numEvictedPods": 0
}
```


*Определено в:* `pkg/controller/devicetainteviction/device_taint_eviction.go`


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/util/util.go:406`



---


[function] name: CleanupNodes file: test/integration/util/util.go:302 returns_error: нет description: CleanupNodes cleans all nodes which were created during integration test


### CleanupNodes (test/integration/util/util.go:302)


CleanupNodes cleans all nodes which were created during integration test


```go
func CleanupNodes((cs clientset.Interface, t *testing.T)) (cs clientset.Interface, t *testing.T)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/util/util.go:302`



---


[function] name: CleanupPods file: test/integration/util/util.go:390 returns_error: нет description: CleanupPods deletes the given pods and waits for them to be actually deleted.


### CleanupPods (test/integration/util/util.go:390)


CleanupPods deletes the given pods and waits for them to be actually deleted.


```go
func CleanupPods((ctx context.Context, cs clientset.Interface, t *testing.T, pods []*v1.Pod)) (ctx context.Context, cs clientset.Interface, t *testing.T, pods []*v1.Pod)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** pods


```json
{
  "pods": {},
  "mu": {}
}
```


*Определено в:* `pkg/scheduler/framework/runtime/pods_in_prebind_map.go`


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


📍 *Расположение:* `test/integration/util/util.go:390`



---


[function] name: CleanupTest file: test/integration/util/util.go:347 returns_error: нет description: CleanupTest cleans related resources which were created during integration test


### CleanupTest (test/integration/util/util.go:347)


CleanupTest cleans related resources which were created during integration test


```go
func CleanupTest((t *testing.T, testCtx *TestContext)) (t *testing.T, testCtx *TestContext)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


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


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


📍 *Расположение:* `test/integration/util/util.go:347`



---


[function] name: CreateAndWaitForNodesInCache file: test/integration/util/util.go:791 returns_error: да description: CreateAndWaitForNodesInCache calls createNodes(), and wait for the created
nodes to be present in scheduler cache.


### CreateAndWaitForNodesInCache (test/integration/util/util.go:791)


CreateAndWaitForNodesInCache calls createNodes(), and wait for the created
nodes to be present in scheduler cache.


```go
func CreateAndWaitForNodesInCache(([]*v1.Node, error)) ([]*v1.Node, error)
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


*Типы возврата:* `[]*v1.Node`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/util/util.go:791`



---


[function] name: CreateGCController file: test/integration/util/util.go:194 returns_error: нет description: CreateGCController creates a garbage controller and returns a run function
for it. The informer factory needs to be star


### CreateGCController (test/integration/util/util.go:194)


CreateGCController creates a garbage controller and returns a run function
for it. The informer factory needs to be started before invoking that
function.


```go
func CreateGCController((ctx context.Context, tb ktesting.TB, restConfig restclient.Config, informerSet informers.SharedInformerFactory)) (ctx context.Context, tb ktesting.TB, restConfig restclient.Config, informerSet informers.SharedInformerFactory)
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


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** ktesting.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** restConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** informerSet


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


📍 *Расположение:* `test/integration/util/util.go:194`



---


[function] name: CreateNamespaceController file: test/integration/util/util.go:232 returns_error: нет description: CreateNamespaceController creates a namespace controller and returns a run
function for it. The informer factory needs t


### CreateNamespaceController (test/integration/util/util.go:232)


CreateNamespaceController creates a namespace controller and returns a run
function for it. The informer factory needs to be started before invoking
that function.


```go
func CreateNamespaceController((ctx context.Context, tb ktesting.TB, restConfig restclient.Config, informerSet informers.SharedInformerFactory)) (ctx context.Context, tb ktesting.TB, restConfig restclient.Config, informerSet informers.SharedInformerFactory)
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


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** ktesting.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** restConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** informerSet


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


📍 *Расположение:* `test/integration/util/util.go:232`



---


[function] name: CreateNamespacesWithLabels file: test/integration/util/util.go:1149 returns_error: нет description: —


### CreateNamespacesWithLabels (test/integration/util/util.go:1149)


CreateNamespacesWithLabels is a function that creates new data based on the provided parameters and returns (cs clientset.Interface, namespaces []string, labels map[string]string).


```go
func CreateNamespacesWithLabels((cs clientset.Interface, namespaces []string, labels map[string]string)) (cs clientset.Interface, namespaces []string, labels map[string]string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** namespaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/integration/util/util.go:1149`



---


[function] name: CreateNode file: test/integration/util/util.go:772 returns_error: да description: —


### CreateNode (test/integration/util/util.go:772)


CreateNode is a function that creates new data based on the provided parameters and may return an error.


```go
func CreateNode((*v1.Node, error)) (*v1.Node, error)
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


📍 *Расположение:* `test/integration/util/util.go:772`



---


[function] name: CreatePV file: test/integration/util/util.go:922 returns_error: да description: CreatePV creates a PersistentVolume with the given config and returns its
pointer and error status.


### CreatePV (test/integration/util/util.go:922)


CreatePV creates a PersistentVolume with the given config and returns its
pointer and error status.


```go
func CreatePV((*v1.PersistentVolume, error)) (*v1.PersistentVolume, error)
```


**Тип запроса:** v1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.PersistentVolume`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/util/util.go:922`



---


[function] name: CreatePVC file: test/integration/util/util.go:916 returns_error: да description: CreatePVC creates a PersistentVolumeClaim with the given config and returns
its pointer and error status.


### CreatePVC (test/integration/util/util.go:916)


CreatePVC creates a PersistentVolumeClaim with the given config and returns
its pointer and error status.


```go
func CreatePVC((*v1.PersistentVolumeClaim, error)) (*v1.PersistentVolumeClaim, error)
```


**Тип запроса:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.PersistentVolumeClaim`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/util/util.go:916`



---


[function] name: CreatePausePod file: test/integration/util/util.go:887 returns_error: да description: CreatePausePod creates a pod with "Pause" image and the given config and
return its pointer and error status.


### CreatePausePod (test/integration/util/util.go:887)


CreatePausePod creates a pod with "Pause" image and the given config and
return its pointer and error status.


```go
func CreatePausePod((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/integration/util/util.go:887`



---


[function] name: CreatePausePodWithResource file: test/integration/util/util.go:894 returns_error: да description: CreatePausePodWithResource creates a pod with "Pause" image and the given
resources and returns its pointer and error st


### CreatePausePodWithResource (test/integration/util/util.go:894)


CreatePausePodWithResource creates a pod with "Pause" image and the given
resources and returns its pointer and error status. The resource list can be
nil.


```go
func CreatePausePodWithResource((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/integration/util/util.go:894`



---


[function] name: CreateResourceClaimController file: test/integration/util/util.go:129 returns_error: нет description: —


### CreateResourceClaimController (test/integration/util/util.go:129)


CreateResourceClaimController is a function that creates new data based on the provided parameters and returns (ctx context.Context, tb ktesting.TB, clientSet clientset.Interface, informerFactory informers.SharedInformerFactory).


```go
func CreateResourceClaimController((ctx context.Context, tb ktesting.TB, clientSet clientset.Interface, informerFactory informers.SharedInformerFactory)) (ctx context.Context, tb ktesting.TB, clientSet clientset.Interface, informerFactory informers.SharedInformerFactory)
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


**Тип ответа:** tb


```json
{
  "logger": {},
  "conn": null,
  "period": {},
  "closer": {},
  "message": [],
  "pongMessage": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/websocket.go`


**Тип ответа:** ktesting.TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** informerFactory


```json
{
  "typedInformerFactory": {},
  "metadataInformerFactory": {}
}
```


*Определено в:* `staging/src/k8s.io/controller-manager/pkg/informerfactory/informer_factory.go`


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


📍 *Расположение:* `test/integration/util/util.go:129`



---


[function] name: DeletePV file: test/integration/util/util.go:932 returns_error: нет description: DeletePV deletes the given PV in the given namespace.


### DeletePV (test/integration/util/util.go:932)


DeletePV deletes the given PV in the given namespace.


```go
func DeletePV((cs clientset.Interface, pvName string)) (cs clientset.Interface, pvName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** pvName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:932`



---


[function] name: DeletePVC file: test/integration/util/util.go:927 returns_error: нет description: DeletePVC deletes the given PVC in the given namespace.


### DeletePVC (test/integration/util/util.go:927)


DeletePVC deletes the given PVC in the given namespace.


```go
func DeletePVC((cs clientset.Interface, pvcName string, nsName string)) (cs clientset.Interface, pvcName string, nsName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** pvcName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nsName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:927`



---


[function] name: DeletePod file: test/integration/util/util.go:1141 returns_error: нет description: DeletePod deletes the given pod in the given namespace.


### DeletePod (test/integration/util/util.go:1141)


DeletePod deletes the given pod in the given namespace.


```go
func DeletePod((cs clientset.Interface, podName string, nsName string)) (cs clientset.Interface, podName string, nsName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nsName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:1141`



---


[function] name: GetPod file: test/integration/util/util.go:1145 returns_error: да description: —


### GetPod (test/integration/util/util.go:1145)


GetPod is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetPod((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/integration/util/util.go:1145`



---


[function] name: GetTolerationSeconds file: test/integration/util/util.go:477 returns_error: да description: GetTolerationSeconds gets the period of time the toleration


### GetTolerationSeconds (test/integration/util/util.go:477)


GetTolerationSeconds gets the period of time the toleration


```go
func GetTolerationSeconds((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/util/util.go:477`



---


[function] name: InitDisruptionController file: test/integration/util/util.go:673 returns_error: нет description: InitDisruptionController initializes and runs a Disruption Controller to properly
update PodDisuptionBudget objects.


### InitDisruptionController (test/integration/util/util.go:673)


InitDisruptionController initializes and runs a Disruption Controller to properly
update PodDisuptionBudget objects.


```go
func InitDisruptionController((t *testing.T, testCtx *TestContext)) (t *testing.T, testCtx *TestContext)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


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


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


📍 *Расположение:* `test/integration/util/util.go:673`



---


[function] name: InitPausePod file: test/integration/util/util.go:832 returns_error: нет description: InitPausePod initializes a pod API object from the given config. It is used
mainly in pod creation process.


### InitPausePod (test/integration/util/util.go:832)


InitPausePod initializes a pod API object from the given config. It is used
mainly in pod creation process.


```go
func InitPausePod((conf *PausePodConfig)) (conf *PausePodConfig)
```


**Тип запроса:** PausePodConfig


```json
{
  "Name": "string",
  "Namespace": "string",
  "Affinity": null,
  "Annotations": {},
  "Resources": null,
  "Tolerations": [],
  "NodeName": "string",
  "SchedulerName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "PriorityClassName": "string",
  "Volumes": [],
  "ContainerPorts": [],
  "RestartableInitContainerPorts": [],
  "NonRestartableInitContainerPorts": []
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** conf


```json
{
  "GroupVersion": {},
  "userSupplied": false
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/configset.go`


**Тип ответа:** PausePodConfig


```json
{
  "Name": "string",
  "Namespace": "string",
  "Affinity": null,
  "Annotations": {},
  "Resources": null,
  "Tolerations": [],
  "NodeName": "string",
  "SchedulerName": "string",
  "Priority": 0,
  "PreemptionPolicy": null,
  "PriorityClassName": "string",
  "Volumes": [],
  "ContainerPorts": [],
  "RestartableInitContainerPorts": [],
  "NonRestartableInitContainerPorts": []
}
```


*Определено в:* `test/integration/util/util.go`


📍 *Расположение:* `test/integration/util/util.go:832`



---


[function] name: InitPodWithContainers file: test/integration/util/util.go:960 returns_error: нет description: InitPodWithContainers initializes a pod API object from the given config. This is used primarily for generating
pods wit


### InitPodWithContainers (test/integration/util/util.go:960)


InitPodWithContainers initializes a pod API object from the given config. This is used primarily for generating
pods with containers each having a specific image.


```go
func InitPodWithContainers((cs clientset.Interface, conf *PodWithContainersConfig)) (cs clientset.Interface, conf *PodWithContainersConfig)
```


**Тип запроса:** PodWithContainersConfig


```json
{
  "Name": "string",
  "Namespace": "string",
  "Containers": []
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** conf


```json
{
  "GroupVersion": {},
  "userSupplied": false
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/configset.go`


**Тип ответа:** PodWithContainersConfig


```json
{
  "Name": "string",
  "Namespace": "string",
  "Containers": []
}
```


*Определено в:* `test/integration/util/util.go`


📍 *Расположение:* `test/integration/util/util.go:960`



---


[function] name: InitTestAPIServer file: test/integration/util/util.go:507 returns_error: нет description: InitTestAPIServer initializes a test environment and creates an API server with default
configuration.
It registers clea


### InitTestAPIServer (test/integration/util/util.go:507)


InitTestAPIServer initializes a test environment and creates an API server with default
configuration.
It registers cleanup functions to t.Cleanup(), they will be called when the test completes,
no need to do this again.


```go
func InitTestAPIServer((t *testing.T, nsPrefix string, admission admission.Interface)) (t *testing.T, nsPrefix string, admission admission.Interface)
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


**Тип ответа:** nsPrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** admission


```json
{
  "attributes": {},
  "finished": {},
  "result": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/controller.go`


**Тип ответа:** admission.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `test/integration/util/util.go:507`



---


[function] name: InitTestDisablePreemption file: test/integration/util/util.go:716 returns_error: нет description: InitTestDisablePreemption initializes a test environment and creates API server and scheduler with default
configuration


### InitTestDisablePreemption (test/integration/util/util.go:716)


InitTestDisablePreemption initializes a test environment and creates API server and scheduler with default
configuration but with pod preemption disabled.


```go
func InitTestDisablePreemption((t *testing.T, nsPrefix string)) (t *testing.T, nsPrefix string)
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


**Тип ответа:** nsPrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:716`



---


[function] name: InitTestScheduler file: test/integration/util/util.go:581 returns_error: нет description: InitTestScheduler initializes a test environment and creates a scheduler with default
configuration.


### InitTestScheduler (test/integration/util/util.go:581)


InitTestScheduler initializes a test environment and creates a scheduler with default
configuration.


```go
func InitTestScheduler((
	t *testing.T,
	testCtx *TestContext,
)) (
	t *testing.T,
	testCtx *TestContext,
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


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


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


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


📍 *Расположение:* `test/integration/util/util.go:581`



---


[function] name: InitTestSchedulerWithNS file: test/integration/util/util.go:707 returns_error: нет description: InitTestSchedulerWithNS initializes a test environment and creates API server and scheduler with default
configuration.


### InitTestSchedulerWithNS (test/integration/util/util.go:707)


InitTestSchedulerWithNS initializes a test environment and creates API server and scheduler with default
configuration.


```go
func InitTestSchedulerWithNS((t *testing.T, nsPrefix string, opts ...scheduler.Option)) (t *testing.T, nsPrefix string, opts ...scheduler.Option)
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


**Тип ответа:** nsPrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scheduler.Option


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `test/integration/util/util.go:707`



---


[function] name: InitTestSchedulerWithOptions file: test/integration/util/util.go:591 returns_error: нет description: InitTestSchedulerWithOptions initializes a test environment and creates a scheduler with default
configuration and other


### InitTestSchedulerWithOptions (test/integration/util/util.go:591)


InitTestSchedulerWithOptions initializes a test environment and creates a scheduler with default
configuration and other options.


```go
func InitTestSchedulerWithOptions((
	t *testing.T,
	testCtx *TestContext,
	resyncPeriod time.Duration,
	opts ...scheduler.Option,
)) (
	t *testing.T,
	testCtx *TestContext,
	resyncPeriod time.Duration,
	opts ...scheduler.Option,
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


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


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


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** resyncPeriod


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


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scheduler.Option


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `test/integration/util/util.go:591`



---


[function] name: NextPodOrDie file: test/integration/util/util.go:1181 returns_error: нет description: NextPodOrDie returns the next Pod in the scheduler queue.
The operation needs to be completed within 5 seconds; otherwis


### NextPodOrDie (test/integration/util/util.go:1181)


NextPodOrDie returns the next Pod in the scheduler queue.
The operation needs to be completed within 5 seconds; otherwise the test gets aborted.


```go
func NextPodOrDie((t *testing.T, testCtx *TestContext)) (t *testing.T, testCtx *TestContext)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


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


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


📍 *Расположение:* `test/integration/util/util.go:1181`



---


[function] name: NodeCopyWithConditions file: test/integration/util/util.go:487 returns_error: нет description: NodeCopyWithConditions duplicates the ode object with conditions


### NodeCopyWithConditions (test/integration/util/util.go:487)


NodeCopyWithConditions duplicates the ode object with conditions


```go
func NodeCopyWithConditions((node *v1.Node, conditions []v1.NodeCondition)) (node *v1.Node, conditions []v1.NodeCondition)
```


**Тип запроса:** v1.Node


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** conditions


```json
{
  "UID": null,
  "ResourceVersion": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/preconditions.go`


**Тип ответа:** v1.NodeCondition


```json
{
  "Type": {},
  "Status": {},
  "LastHeartbeatTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/util/util.go:487`



---


[function] name: NodeReadyStatus file: test/integration/util/util.go:465 returns_error: да description: NodeReadyStatus returns the status of first condition with type NodeReady.
If none of the condition is of type NodeReady


### NodeReadyStatus (test/integration/util/util.go:465)


NodeReadyStatus returns the status of first condition with type NodeReady.
If none of the condition is of type NodeReady, returns an error.


```go
func NodeReadyStatus((v1.ConditionStatus, error)) (v1.ConditionStatus, error)
```


**Тип ответа:** v1.ConditionStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `v1.ConditionStatus`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/util/util.go:465`



---


[function] name: NodeTainted file: test/integration/util/util.go:441 returns_error: нет description: NodeTainted return a condition function that returns true if the given node contains
the taints.


### NodeTainted (test/integration/util/util.go:441)


NodeTainted return a condition function that returns true if the given node contains
the taints.


```go
func NodeTainted((ctx context.Context, cs clientset.Interface, nodeName string, taints []v1.Taint)) (ctx context.Context, cs clientset.Interface, nodeName string, taints []v1.Taint)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** taints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/util/util.go:441`



---


[function] name: PodDeleted file: test/integration/util/util.go:310 returns_error: нет description: PodDeleted returns true if a pod is not found in the given namespace.


### PodDeleted (test/integration/util/util.go:310)


PodDeleted returns true if a pod is not found in the given namespace.


```go
func PodDeleted((ctx context.Context, c clientset.Interface, podNamespace, podName string)) (ctx context.Context, c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:310`



---


[function] name: PodIsGettingEvicted file: test/integration/util/util.go:990 returns_error: нет description: PodIsGettingEvicted returns true if the pod's deletion timestamp is set.


### PodIsGettingEvicted (test/integration/util/util.go:990)


PodIsGettingEvicted returns true if the pod's deletion timestamp is set.


```go
func PodIsGettingEvicted((c clientset.Interface, podNamespace, podName string)) (c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:990`



---


[function] name: PodScheduled file: test/integration/util/util.go:657 returns_error: нет description: PodScheduled checks if the pod has been scheduled


### PodScheduled (test/integration/util/util.go:657)


PodScheduled checks if the pod has been scheduled


```go
func PodScheduled((c clientset.Interface, podNamespace, podName string)) (c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:657`



---


[function] name: PodScheduledIn file: test/integration/util/util.go:1004 returns_error: нет description: PodScheduledIn returns true if a given pod is placed onto one of the expected nodes.


### PodScheduledIn (test/integration/util/util.go:1004)


PodScheduledIn returns true if a given pod is placed onto one of the expected nodes.


```go
func PodScheduledIn((c clientset.Interface, podNamespace, podName string, nodeNames []string)) (c clientset.Interface, podNamespace, podName string, nodeNames []string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeNames


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:1004`



---


[function] name: PodSchedulingError file: test/integration/util/util.go:1041 returns_error: нет description: PodSchedulingError returns a condition function that returns true if the given pod
gets unschedulable status for reasons


### PodSchedulingError (test/integration/util/util.go:1041)


PodSchedulingError returns a condition function that returns true if the given pod
gets unschedulable status for reasons other than "Unschedulable". The scheduler
records such reasons in case of error.


```go
func PodSchedulingError((c clientset.Interface, podNamespace, podName string)) (c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:1041`



---


[function] name: PodSchedulingGated file: test/integration/util/util.go:1056 returns_error: нет description: PodSchedulingGated returns a condition function that returns true if the given pod
gets unschedulable status of reason '


### PodSchedulingGated (test/integration/util/util.go:1056)


PodSchedulingGated returns a condition function that returns true if the given pod
gets unschedulable status of reason 'SchedulingGated'.


```go
func PodSchedulingGated((ctx context.Context, c clientset.Interface, podNamespace, podName string)) (ctx context.Context, c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:1056`



---


[function] name: PodUnschedulable file: test/integration/util/util.go:1025 returns_error: нет description: PodUnschedulable returns a condition function that returns true if the given pod
gets unschedulable status of reason 'Un


### PodUnschedulable (test/integration/util/util.go:1025)


PodUnschedulable returns a condition function that returns true if the given pod
gets unschedulable status of reason 'Unschedulable'.


```go
func PodUnschedulable((c clientset.Interface, podNamespace, podName string)) (c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:1025`



---


[function] name: PodsCleanedUp file: test/integration/util/util.go:324 returns_error: нет description: PodsCleanedUp returns true if all pods are deleted in the specific namespace.


### PodsCleanedUp (test/integration/util/util.go:324)


PodsCleanedUp returns true if all pods are deleted in the specific namespace.


```go
func PodsCleanedUp((ctx context.Context, c clientset.Interface, namespace string)) (ctx context.Context, c clientset.Interface, namespace string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


📍 *Расположение:* `test/integration/util/util.go:324`



---


[function] name: RemovePodFinalizers file: test/integration/util/util.go:367 returns_error: нет description: RemovePodFinalizers removes pod finalizers for the pods


### RemovePodFinalizers (test/integration/util/util.go:367)


RemovePodFinalizers removes pod finalizers for the pods


```go
func RemovePodFinalizers((ctx context.Context, cs clientset.Interface, t *testing.T, pods ...v1.Pod)) (ctx context.Context, cs clientset.Interface, t *testing.T, pods ...v1.Pod)
```


**Тип запроса:** testing.T


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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** pods


```json
{
  "pods": {},
  "mu": {}
}
```


*Определено в:* `pkg/scheduler/framework/runtime/pods_in_prebind_map.go`


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


📍 *Расположение:* `test/integration/util/util.go:367`



---


[function] name: RemovePodFinalizersInNamespace file: test/integration/util/util.go:357 returns_error: нет description: —


### RemovePodFinalizersInNamespace (test/integration/util/util.go:357)


RemovePodFinalizersInNamespace is a function that deletes data based on the provided parameters and returns (ctx context.Context, cs clientset.Interface, t *testing.T, ns string).


```go
func RemovePodFinalizersInNamespace((ctx context.Context, cs clientset.Interface, t *testing.T, ns string)) (ctx context.Context, cs clientset.Interface, t *testing.T, ns string)
```


**Тип запроса:** testing.T


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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/util/util.go:357`



---


[function] name: RemoveTaintOffNode file: test/integration/util/util.go:417 returns_error: нет description: RemoveTaintOffNode removes a specific taint from a node


### RemoveTaintOffNode (test/integration/util/util.go:417)


RemoveTaintOffNode removes a specific taint from a node


```go
func RemoveTaintOffNode((cs clientset.Interface, nodeName string, taint v1.Taint)) (cs clientset.Interface, nodeName string, taint v1.Taint)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** taint


```json
{
  "numEvictedPods": 0
}
```


*Определено в:* `pkg/controller/devicetainteviction/device_taint_eviction.go`


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/util/util.go:417`



---


[function] name: RoundTrip file: test/integration/util/util.go:291 returns_error: да description: —


### RoundTrip (test/integration/util/util.go:291)


RoundTrip is a method that performs operations based on the provided parameters and may return an error.


```go
func (r roundTripWrapper) RoundTrip((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Тип ответа:** http.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/util/util.go:291`



---


[function] name: RunPausePod file: test/integration/util/util.go:938 returns_error: да description: RunPausePod creates a pod with "Pause" image and the given config and waits
until it is scheduled. It returns its pointe


### RunPausePod (test/integration/util/util.go:938)


RunPausePod creates a pod with "Pause" image and the given config and waits
until it is scheduled. It returns its pointer and error status.


```go
func RunPausePod((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/integration/util/util.go:938`



---


[function] name: RunPodWithContainers file: test/integration/util/util.go:975 returns_error: да description: RunPodWithContainers creates a pod with given config and containers and waits
until it is scheduled. It returns its poin


### RunPodWithContainers (test/integration/util/util.go:975)


RunPodWithContainers creates a pod with given config and containers and waits
until it is scheduled. It returns its pointer and error status.


```go
func RunPodWithContainers((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/integration/util/util.go:975`



---


[function] name: StartFakePVController file: test/integration/util/util.go:148 returns_error: нет description: StartFakePVController is a simplified pv controller logic that sets PVC VolumeName and annotation for each PV binding.
T


### StartFakePVController (test/integration/util/util.go:148)


StartFakePVController is a simplified pv controller logic that sets PVC VolumeName and annotation for each PV binding.
TODO(mborsz): Use a real PV controller here.


```go
func StartFakePVController((ctx context.Context, clientSet clientset.Interface, informerFactory informers.SharedInformerFactory)) (ctx context.Context, clientSet clientset.Interface, informerFactory informers.SharedInformerFactory)
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


**Тип ответа:** clientSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** informerFactory


```json
{
  "typedInformerFactory": {},
  "metadataInformerFactory": {}
}
```


*Определено в:* `staging/src/k8s.io/controller-manager/pkg/informerfactory/informer_factory.go`


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


📍 *Расположение:* `test/integration/util/util.go:148`



---


[function] name: StartScheduler file: test/integration/util/util.go:88 returns_error: нет description: StartScheduler configures and starts a scheduler given a handle to the clientSet interface
and event broadcaster. It ret


### StartScheduler (test/integration/util/util.go:88)


StartScheduler configures and starts a scheduler given a handle to the clientSet interface
and event broadcaster. It returns the running scheduler and podInformer. Background goroutines
will keep running until the context is canceled.


```go
func StartScheduler((*scheduler.Scheduler, informers.SharedInformerFactory)) (*scheduler.Scheduler, informers.SharedInformerFactory)
```


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


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


📍 *Расположение:* `test/integration/util/util.go:88`



---


[function] name: SyncSchedulerInformerFactory file: test/integration/util/util.go:335 returns_error: нет description: SyncSchedulerInformerFactory starts informer and waits for caches to be synced


### SyncSchedulerInformerFactory (test/integration/util/util.go:335)


SyncSchedulerInformerFactory starts informer and waits for caches to be synced


```go
func SyncSchedulerInformerFactory((testCtx *TestContext)) (testCtx *TestContext)
```


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


📍 *Расположение:* `test/integration/util/util.go:335`



---


[function] name: UpdateNode file: test/integration/util/util.go:768 returns_error: да description: —


### UpdateNode (test/integration/util/util.go:768)


UpdateNode is a function that updates data based on the provided parameters and may return an error.


```go
func UpdateNode((*v1.Node, error)) (*v1.Node, error)
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


📍 *Расположение:* `test/integration/util/util.go:768`



---


[function] name: UpdateNodeStatus file: test/integration/util/util.go:498 returns_error: нет description: UpdateNodeStatus updates the status of node.


### UpdateNodeStatus (test/integration/util/util.go:498)


UpdateNodeStatus updates the status of node.


```go
func UpdateNodeStatus((cs clientset.Interface, node *v1.Node)) (cs clientset.Interface, node *v1.Node)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/util/util.go:498`



---


[function] name: WaitCachedPodsStable file: test/integration/util/util.go:1117 returns_error: нет description: WaitCachedPodsStable waits until scheduler cache has the given pods.


### WaitCachedPodsStable (test/integration/util/util.go:1117)


WaitCachedPodsStable waits until scheduler cache has the given pods.


```go
func WaitCachedPodsStable((testCtx *TestContext, pods []*v1.Pod)) (testCtx *TestContext, pods []*v1.Pod)
```


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


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


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** pods


```json
{
  "pods": {},
  "mu": {}
}
```


*Определено в:* `pkg/scheduler/framework/runtime/pods_in_prebind_map.go`


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


📍 *Расположение:* `test/integration/util/util.go:1117`



---


[function] name: WaitForNodeTaints file: test/integration/util/util.go:435 returns_error: нет description: WaitForNodeTaints waits for a node to have the target taints and returns
an error if it does not have taints within the 


### WaitForNodeTaints (test/integration/util/util.go:435)


WaitForNodeTaints waits for a node to have the target taints and returns
an error if it does not have taints within the given timeout.


```go
func WaitForNodeTaints((ctx context.Context, cs clientset.Interface, node *v1.Node, taints []v1.Taint)) (ctx context.Context, cs clientset.Interface, node *v1.Node, taints []v1.Taint)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** taints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Taint


```json
{
  "Key": "string",
  "Value": "string",
  "Effect": {},
  "TimeAdded": null
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/integration/util/util.go:435`



---


[function] name: WaitForNodesInCache file: test/integration/util/util.go:802 returns_error: нет description: WaitForNodesInCache ensures at least <nodeCount> nodes are present in scheduler cache
within 30 seconds; otherwise retur


### WaitForNodesInCache (test/integration/util/util.go:802)


WaitForNodesInCache ensures at least <nodeCount> nodes are present in scheduler cache
within 30 seconds; otherwise returns false.


```go
func WaitForNodesInCache((ctx context.Context, sched *scheduler.Scheduler, nodeCount int)) (ctx context.Context, sched *scheduler.Scheduler, nodeCount int)
```


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


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


**Тип ответа:** sched


```json
{
  "prepareFn": {}
}
```


*Определено в:* `test/integration/scheduler_perf/options.go`


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Тип ответа:** nodeCount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:802`



---


[function] name: WaitForNominatedNodeName file: test/integration/util/util.go:1212 returns_error: нет description: —


### WaitForNominatedNodeName (test/integration/util/util.go:1212)


WaitForNominatedNodeName is a function that performs operations based on the provided parameters and returns (ctx context.Context, cs clientset.Interface, pod *v1.Pod).


```go
func WaitForNominatedNodeName((ctx context.Context, cs clientset.Interface, pod *v1.Pod)) (ctx context.Context, cs clientset.Interface, pod *v1.Pod)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/util/util.go:1212`



---


[function] name: WaitForNominatedNodeNameWithTimeout file: test/integration/util/util.go:1196 returns_error: нет description: —


### WaitForNominatedNodeNameWithTimeout (test/integration/util/util.go:1196)


WaitForNominatedNodeNameWithTimeout is a function that performs operations based on the provided parameters and returns (ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration).


```go
func WaitForNominatedNodeNameWithTimeout((ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)) (ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/integration/util/util.go:1196`



---


[function] name: WaitForPDBsStable file: test/integration/util/util.go:1089 returns_error: нет description: WaitForPDBsStable waits for PDBs to have "CurrentHealthy" status equal to
the expected values.


### WaitForPDBsStable (test/integration/util/util.go:1089)


WaitForPDBsStable waits for PDBs to have "CurrentHealthy" status equal to
the expected values.


```go
func WaitForPDBsStable((testCtx *TestContext, pdbs []*policy.PodDisruptionBudget, pdbPodNum []int32)) (testCtx *TestContext, pdbs []*policy.PodDisruptionBudget, pdbPodNum []int32)
```


**Тип запроса:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


**Тип запроса:** policy.PodDisruptionBudget


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/policy/types.go`


**Тип ответа:** testCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestContext


```json
{
  "DisableEventSink": false,
  "NS": null,
  "ClientSet": {},
  "KubeConfig": null,
  "InformerFactory": {},
  "DynInformerFactory": {},
  "Scheduler": null,
  "Ctx": {},
  "CloseFn": {},
  "SchedulerCtx": {},
  "SchedulerCloseFn": {},
  "RoundTrip": {}
}
```


*Определено в:* `test/integration/util/util.go`


**Тип ответа:** pdbs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** policy.PodDisruptionBudget


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/policy/types.go`


**Тип ответа:** pdbPodNum


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:1089`



---


[function] name: WaitForPodSchedulingGated file: test/integration/util/util.go:1083 returns_error: нет description: WaitForPodSchedulingGated waits for a pod to be in scheduling gated state
and returns an error if it does not fall into 


### WaitForPodSchedulingGated (test/integration/util/util.go:1083)


WaitForPodSchedulingGated waits for a pod to be in scheduling gated state
and returns an error if it does not fall into this state within the given timeout.


```go
func WaitForPodSchedulingGated((ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)) (ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/integration/util/util.go:1083`



---


[function] name: WaitForPodToSchedule file: test/integration/util/util.go:652 returns_error: нет description: WaitForPodToSchedule waits for a pod to get scheduled and returns an error if
it does not get scheduled within the timeo


### WaitForPodToSchedule (test/integration/util/util.go:652)


WaitForPodToSchedule waits for a pod to get scheduled and returns an error if
it does not get scheduled within the timeout duration (30 seconds).


```go
func WaitForPodToSchedule((ctx context.Context, cs clientset.Interface, pod *v1.Pod)) (ctx context.Context, cs clientset.Interface, pod *v1.Pod)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/util/util.go:652`



---


[function] name: WaitForPodToScheduleWithTimeout file: test/integration/util/util.go:646 returns_error: нет description: WaitForPodToScheduleWithTimeout waits for a pod to get scheduled and returns
an error if it does not scheduled within th


### WaitForPodToScheduleWithTimeout (test/integration/util/util.go:646)


WaitForPodToScheduleWithTimeout waits for a pod to get scheduled and returns
an error if it does not scheduled within the given timeout.


```go
func WaitForPodToScheduleWithTimeout((ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)) (ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/integration/util/util.go:646`



---


[function] name: WaitForPodUnschedulable file: test/integration/util/util.go:1077 returns_error: нет description: WaitForPodUnschedulable waits for a pod to fail scheduling and returns
an error if it does not become unschedulable with


### WaitForPodUnschedulable (test/integration/util/util.go:1077)


WaitForPodUnschedulable waits for a pod to fail scheduling and returns
an error if it does not become unschedulable within the timeout duration (30 seconds).


```go
func WaitForPodUnschedulable((ctx context.Context, cs clientset.Interface, pod *v1.Pod)) (ctx context.Context, cs clientset.Interface, pod *v1.Pod)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/util/util.go:1077`



---


[function] name: WaitForPodUnschedulableWithTimeout file: test/integration/util/util.go:1071 returns_error: нет description: WaitForPodUnschedulableWithTimeout waits for a pod to fail scheduling and returns
an error if it does not become unsched


### WaitForPodUnschedulableWithTimeout (test/integration/util/util.go:1071)


WaitForPodUnschedulableWithTimeout waits for a pod to fail scheduling and returns
an error if it does not become unschedulable within the given timeout.


```go
func WaitForPodUnschedulableWithTimeout((ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)) (ctx context.Context, cs clientset.Interface, pod *v1.Pod, timeout time.Duration)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/integration/util/util.go:1071`



---


[function] name: WaitForReflection file: test/integration/util/util.go:740 returns_error: нет description: WaitForReflection waits till the passFunc confirms that the object it expects
to see is in the store. Used to observe re


### WaitForReflection (test/integration/util/util.go:740)


WaitForReflection waits till the passFunc confirms that the object it expects
to see is in the store. Used to observe reflected events.


```go
func WaitForReflection((ctx context.Context, t *testing.T, nodeLister corelisters.NodeLister, key string,
	passFunc func(n interface{}) bool)) (ctx context.Context, t *testing.T, nodeLister corelisters.NodeLister, key string,
	passFunc func(n interface{}) bool)
```


**Тип запроса:** testing.T


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


**Тип ответа:** nodeLister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corelisters.NodeLister


```json
{
  "csiNodeLister": {}
}
```


*Определено в:* `pkg/scheduler/framework/plugins/nodevolumelimits/csi_manager.go`


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


**Тип ответа:** passFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/integration/util/util.go:740`



---


[function] name: WaitForSchedulerCacheCleanup file: test/integration/util/util.go:567 returns_error: нет description: WaitForSchedulerCacheCleanup waits for cleanup of scheduler's cache to complete


### WaitForSchedulerCacheCleanup (test/integration/util/util.go:567)


WaitForSchedulerCacheCleanup waits for cleanup of scheduler's cache to complete


```go
func WaitForSchedulerCacheCleanup((ctx context.Context, sched *scheduler.Scheduler, t *testing.T)) (ctx context.Context, sched *scheduler.Scheduler, t *testing.T)
```


**Тип запроса:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


**Тип запроса:** testing.T


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


**Тип ответа:** sched


```json
{
  "prepareFn": {}
}
```


*Определено в:* `test/integration/scheduler_perf/options.go`


**Тип ответа:** scheduler.Scheduler


```json
{
  "Cache": {},
  "Extenders": [],
  "NextPod": {},
  "FailureHandler": {},
  "SchedulePod": {},
  "StopEverything": {},
  "SchedulingQueue": {},
  "APIDispatcher": null,
  "WorkloadManager": {},
  "Profiles": {},
  "client": {},
  "nodeInfoSnapshot": null,
  "percentageOfNodesToScore": 0,
  "nextStartNodeIndex": 0,
  "logger": {},
  "registeredHandlers": [],
  "nominatedNodeNameForExpectationEnabled": false
}
```


*Определено в:* `pkg/scheduler/scheduler.go`


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


📍 *Расположение:* `test/integration/util/util.go:567`



---


[function] name: createNodes file: test/integration/util/util.go:776 returns_error: да description: —


### createNodes (test/integration/util/util.go:776)


createNodes is a function that performs operations based on the provided parameters and may return an error.


```go
func createNodes(([]*v1.Node, error)) ([]*v1.Node, error)
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


*Типы возврата:* `[]*v1.Node`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/integration/util/util.go:776`



---


[function] name: timeout file: test/integration/util/util.go:1161 returns_error: нет description: timeout returns a timeout error if the given `f` function doesn't
complete within `d` duration; otherwise it returns nil


### timeout (test/integration/util/util.go:1161)


timeout returns a timeout error if the given `f` function doesn't
complete within `d` duration; otherwise it returns nil.


```go
func timeout((ctx context.Context, d time.Duration, f func())) (ctx context.Context, d time.Duration, f func())
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


**Тип ответа:** d


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


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


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/util/util.go:1161`




## test/integration/utils.go


📄 Исходный файл: `test/integration/utils.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DeletePodOrErrorf](#deletepodorerrorf-testintegrationutilsgo36) `:36`

- 🔗 [GetEtcdClients](#getetcdclients-testintegrationutilsgo70) `:70`

- 🔗 [WaitForPodToDisappear](#waitforpodtodisappear-testintegrationutilsgo56) `:56`


</details>


[function] name: DeletePodOrErrorf file: test/integration/utils.go:36 returns_error: нет description: DeletePodOrErrorf deletes a pod or fails with a call to t.Errorf.


### DeletePodOrErrorf (test/integration/utils.go:36)


DeletePodOrErrorf deletes a pod or fails with a call to t.Errorf.


```go
func DeletePodOrErrorf((t *testing.T, c clientset.Interface, ns, name string)) (t *testing.T, c clientset.Interface, ns, name string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/integration/utils.go:36`



---


[function] name: GetEtcdClients file: test/integration/utils.go:70 returns_error: да description: GetEtcdClients returns an initialized etcd clientv3.Client and clientv3.KV.


### GetEtcdClients (test/integration/utils.go:70)


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


📍 *Расположение:* `test/integration/utils.go:70`



---


[function] name: WaitForPodToDisappear file: test/integration/utils.go:56 returns_error: нет description: WaitForPodToDisappear polls the API server if the pod has been deleted.


### WaitForPodToDisappear (test/integration/utils.go:56)


WaitForPodToDisappear polls the API server if the pod has been deleted.


```go
func WaitForPodToDisappear((podClient coreclient.PodInterface, podName string, interval, timeout time.Duration)) (podClient coreclient.PodInterface, podName string, interval, timeout time.Duration)
```


**Тип ответа:** podClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** coreclient.PodInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interval


```json
{
  "First": 0,
  "Last": 0
}
```


*Определено в:* `pkg/controller/job/indexed_job_utils.go`


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/integration/utils.go:56`




## test/integration/volumescheduling/util.go


📄 Исходный файл: `test/integration/volumescheduling/util.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [podScheduled](#podscheduled-testintegrationvolumeschedulingutilgo55) `:55`

- 🔗 [podUnschedulable](#podunschedulable-testintegrationvolumeschedulingutilgo71) `:71`

- 🔗 [waitForPodToSchedule](#waitforpodtoschedule-testintegrationvolumeschedulingutilgo38) `:38`

- 🔗 [waitForPodToScheduleWithTimeout](#waitforpodtoschedulewithtimeout-testintegrationvolumeschedulingutilgo32) `:32`

- 🔗 [waitForPodUnschedulable](#waitforpodunschedulable-testintegrationvolumeschedulingutilgo50) `:50`

- 🔗 [waitForPodUnschedulableWithTimeout](#waitforpodunschedulablewithtimeout-testintegrationvolumeschedulingutilgo44) `:44`


</details>


[function] name: podScheduled file: test/integration/volumescheduling/util.go:55 returns_error: нет description: podScheduled returns true if a node is assigned to the given pod.


### podScheduled (test/integration/volumescheduling/util.go:55)


podScheduled returns true if a node is assigned to the given pod.


```go
func podScheduled((c clientset.Interface, podNamespace, podName string)) (c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/volumescheduling/util.go:55`



---


[function] name: podUnschedulable file: test/integration/volumescheduling/util.go:71 returns_error: нет description: podUnschedulable returns a condition function that returns true if the given pod
gets unschedulable status.


### podUnschedulable (test/integration/volumescheduling/util.go:71)


podUnschedulable returns a condition function that returns true if the given pod
gets unschedulable status.


```go
func podUnschedulable((c clientset.Interface, podNamespace, podName string)) (c clientset.Interface, podNamespace, podName string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/integration/volumescheduling/util.go:71`



---


[function] name: waitForPodToSchedule file: test/integration/volumescheduling/util.go:38 returns_error: нет description: waitForPodToSchedule waits for a pod to get scheduled and returns an error if
it does not get scheduled within the timeo


### waitForPodToSchedule (test/integration/volumescheduling/util.go:38)


waitForPodToSchedule waits for a pod to get scheduled and returns an error if
it does not get scheduled within the timeout duration (30 seconds).


```go
func waitForPodToSchedule((cs clientset.Interface, pod *v1.Pod)) (cs clientset.Interface, pod *v1.Pod)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/volumescheduling/util.go:38`



---


[function] name: waitForPodToScheduleWithTimeout file: test/integration/volumescheduling/util.go:32 returns_error: нет description: waitForPodToScheduleWithTimeout waits for a pod to get scheduled and returns
an error if it does not scheduled within th


### waitForPodToScheduleWithTimeout (test/integration/volumescheduling/util.go:32)


waitForPodToScheduleWithTimeout waits for a pod to get scheduled and returns
an error if it does not scheduled within the given timeout.


```go
func waitForPodToScheduleWithTimeout((cs clientset.Interface, pod *v1.Pod, timeout time.Duration)) (cs clientset.Interface, pod *v1.Pod, timeout time.Duration)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/integration/volumescheduling/util.go:32`



---


[function] name: waitForPodUnschedulable file: test/integration/volumescheduling/util.go:50 returns_error: нет description: waitForPodUnschedule waits for a pod to fail scheduling and returns
an error if it does not become unschedulable within 


### waitForPodUnschedulable (test/integration/volumescheduling/util.go:50)


waitForPodUnschedule waits for a pod to fail scheduling and returns
an error if it does not become unschedulable within the timeout duration (30 seconds).


```go
func waitForPodUnschedulable((cs clientset.Interface, pod *v1.Pod)) (cs clientset.Interface, pod *v1.Pod)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/integration/volumescheduling/util.go:50`



---


[function] name: waitForPodUnschedulableWithTimeout file: test/integration/volumescheduling/util.go:44 returns_error: нет description: waitForPodUnscheduleWithTimeout waits for a pod to fail scheduling and returns
an error if it does not become unschedula


### waitForPodUnschedulableWithTimeout (test/integration/volumescheduling/util.go:44)


waitForPodUnscheduleWithTimeout waits for a pod to fail scheduling and returns
an error if it does not become unschedulable within the given timeout.


```go
func waitForPodUnschedulableWithTimeout((cs clientset.Interface, pod *v1.Pod, timeout time.Duration)) (cs clientset.Interface, pod *v1.Pod, timeout time.Duration)
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


**Тип ответа:** cs


```json
{
  "timestamp": {},
  "window": {},
  "usage": {}
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/metrics/v1alpha1/types.go`


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/integration/volumescheduling/util.go:44`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_instrumentation.md)

- [Следующая директория](test_list.md)


---

